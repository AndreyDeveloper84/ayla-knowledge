#!/usr/bin/env python3
"""Validate Ayla knowledge nodes against .knowledge/schema.yaml."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / ".knowledge" / "schema.yaml"
IGNORED_PARTS = {".git", ".obsidian", ".venv", "__pycache__", "99 Archive"}
RELATIONSHIP_FIELDS = (
    "depends_on",
    "supersedes",
    "implements",
    "adr",
    "related",
    "conflicts_with",
)
APPROVAL_STATUSES = {
    "approved",
    "approved-with-amendments",
    "implemented",
    "delivered",
}
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|$)", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
VERSIONED_FILENAME_RE = re.compile(
    r"\sv\d+(?:\.\d+){1,2}(?:[-+][0-9A-Za-z.-]+)?$", re.IGNORECASE
)
VERSIONED_NODE_ID_RE = re.compile(
    r"(?:^|[.-])v\d+(?:[.-]\d+){1,2}$", re.IGNORECASE
)


class UniqueKeyLoader(yaml.SafeLoader):
    """YAML loader that rejects duplicate mapping keys."""


def _construct_mapping(
    loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False
) -> dict[str, Any]:
    mapping: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping
)


@dataclass
class Node:
    path: Path
    metadata: dict[str, Any]
    body: str

    @property
    def label(self) -> str:
        return self.path.relative_to(ROOT).as_posix()

    @property
    def staged(self) -> bool:
        return (
            self.metadata.get("status") == "review"
            and self.metadata.get("activation_status") == "pending-infrastructure"
        )


class Reporter:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, path: str, message: str) -> None:
        self.errors.append(f"{path}: {message}")

    def warning(self, path: str, message: str) -> None:
        self.warnings.append(f"{path}: {message}")

    def render(self) -> int:
        for message in self.warnings:
            print(f"WARNING: {message}")
        for message in self.errors:
            print(f"ERROR: {message}")
        print(
            f"Knowledge validation: {len(self.errors)} error(s), "
            f"{len(self.warnings)} warning(s)"
        )
        return 1 if self.errors else 0


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.load(handle, Loader=UniqueKeyLoader)
    if not isinstance(data, dict):
        raise ValueError("root YAML value must be a mapping")
    return data


def markdown_paths() -> list[Path]:
    result: list[Path] = []
    for path in ROOT.rglob("*.md"):
        relative_parts = set(path.relative_to(ROOT).parts)
        if relative_parts & IGNORED_PARTS:
            continue
        result.append(path)
    return sorted(result)


def load_nodes(reporter: Reporter) -> list[Node]:
    nodes: list[Node] = []
    for path in markdown_paths():
        label = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8-sig")
        match = FRONTMATTER_RE.match(text)
        if not match:
            # Repository README files are navigation, not knowledge nodes.
            if path.parent == ROOT and path.name == "README.md":
                continue
            reporter.error(label, "missing YAML frontmatter")
            continue
        try:
            metadata = yaml.load(match.group(1), Loader=UniqueKeyLoader)
        except yaml.YAMLError as exc:
            reporter.error(label, f"invalid frontmatter: {exc}")
            continue
        if not isinstance(metadata, dict):
            reporter.error(label, "frontmatter must be a mapping")
            continue
        nodes.append(Node(path=path, metadata=metadata, body=text[match.end() :]))
    return nodes


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def normalize_link(value: str) -> str:
    target = value.split("|", 1)[0].split("#", 1)[0].strip()
    target = target.replace("\\", "/")
    return target[:-3] if target.lower().endswith(".md") else target


def build_link_index(nodes: list[Node]) -> dict[str, set[str]]:
    index: dict[str, set[str]] = {}
    for node in nodes:
        relative = node.path.relative_to(ROOT).with_suffix("").as_posix()
        keys = {
            node.path.stem.casefold(),
            relative.casefold(),
            str(node.metadata.get("title", "")).casefold(),
        }
        for key in keys:
            if key:
                index.setdefault(key, set()).add(node.label)
    return index


def target_exists(target: str, index: dict[str, set[str]]) -> bool:
    normalized = normalize_link(target).casefold()
    return normalized in index


def relationship_targets(node: Node, field: str) -> list[str]:
    result: list[str] = []
    for value in as_list(node.metadata.get(field)):
        if not isinstance(value, str):
            continue
        match = WIKILINK_RE.fullmatch(value.strip())
        if match:
            result.append(normalize_link(match.group(1)))
    return result


def check_metadata(
    node: Node, schema: dict[str, Any], reporter: Reporter
) -> None:
    metadata = node.metadata
    for field in schema.get("required_fields", []):
        if field not in metadata or metadata[field] is None:
            reporter.error(node.label, f"missing required field {field!r}")

    enums = schema.get("enums", {})
    for field, allowed in enums.items():
        if field not in metadata:
            continue
        for value in as_list(metadata[field]):
            if value not in allowed:
                reporter.error(
                    node.label, f"{field} contains unsupported value {value!r}"
                )

    doc_type = metadata.get("type")
    if doc_type is not None and doc_type not in schema.get("document_type_rules", {}):
        reporter.error(node.label, f"unknown document type {doc_type!r}")

    node_id = metadata.get("node_id")
    node_id_pattern = (
        schema.get("field_constraints", {})
        .get("node_id", {})
        .get("format", r"^[a-z0-9]+(?:[.-][a-z0-9]+)*$")
    )
    if isinstance(node_id, str):
        if not re.fullmatch(node_id_pattern, node_id):
            reporter.error(node.label, f"invalid node_id {node_id!r}")
        if VERSIONED_NODE_ID_RE.search(node_id):
            reporter.error(node.label, "node_id must not contain a version suffix")

    canonical_status = metadata.get(
        "canonical_status", schema.get("defaults", {}).get("canonical_status")
    )
    if canonical_status == "approved":
        if metadata.get("status") == "draft":
            reporter.error(
                node.label, "canonical_status approved conflicts with status draft"
            )
        if metadata.get("decision_status") == "proposed":
            reporter.error(
                node.label,
                "canonical_status approved conflicts with decision_status proposed",
            )

    if metadata.get("source_kind") == "canonical":
        if VERSIONED_FILENAME_RE.search(node.path.stem):
            reporter.error(
                node.label, "canonical filename must not contain a version suffix"
            )

    system_owner = metadata.get("system_owner")
    if system_owner is not None and (
        not isinstance(system_owner, list) or not system_owner
    ):
        reporter.error(node.label, "system_owner must be a non-empty list")

    if metadata.get("priority") in {"P0", "P1"}:
        for field in ("owner", "review_cycle", "depends_on"):
            if field not in metadata:
                reporter.error(
                    node.label, f"{metadata['priority']} document requires {field!r}"
                )

    if metadata.get("source_kind") == "mirror":
        for field in (
            "source_repository",
            "source_path",
            "source_ref",
            "source_content_hash",
            "synced",
        ):
            if not metadata.get(field):
                reporter.error(node.label, f"mirror requires {field!r}")

    if metadata.get("classification") == "restricted":
        if metadata.get("ai_indexing") not in {"denied", "metadata-only"}:
            reporter.error(
                node.label, "restricted content cannot use full AI indexing"
            )
        if metadata.get("export_policy") not in {"metadata-only", "prohibited"}:
            reporter.error(
                node.label, "restricted content has an unsafe export policy"
            )

    if metadata.get("ai_indexing") == "denied":
        if metadata.get("export_policy") not in {"metadata-only", "prohibited"}:
            reporter.error(
                node.label, "AI-denied content has an incompatible export policy"
            )


def check_required_sections(
    node: Node, schema: dict[str, Any], reporter: Reporter
) -> None:
    rules = schema.get("document_type_rules", {}).get(node.metadata.get("type"), {})
    required = rules.get("require_sections", [])
    if not required:
        return
    headings = []
    for line in node.body.splitlines():
        match = re.match(r"^#{1,6}\s+(?:\d+(?:\.\d+)*\.\s*)?(.+?)\s*$", line)
        if match:
            headings.append(match.group(1).casefold())
    for section in required:
        if section.casefold() not in headings:
            reporter.error(node.label, f"missing required section {section!r}")


def check_uniqueness(nodes: list[Node], reporter: Reporter) -> None:
    by_node_id: dict[str, list[str]] = {}
    by_title: dict[str, list[str]] = {}
    for node in nodes:
        node_id = node.metadata.get("node_id")
        if isinstance(node_id, str):
            by_node_id.setdefault(node_id.casefold(), []).append(node.label)
        if (
            node.metadata.get("source_kind") == "canonical"
            and node.metadata.get("status") not in {"archived", "superseded"}
        ):
            title = node.metadata.get("title")
            if isinstance(title, str):
                by_title.setdefault(title.casefold(), []).append(node.label)
    for value, paths in by_node_id.items():
        if len(paths) > 1:
            reporter.error(", ".join(paths), f"duplicate node_id {value!r}")
    for value, paths in by_title.items():
        if len(paths) > 1:
            reporter.error(", ".join(paths), f"duplicate canonical title {value!r}")


def check_links(
    nodes: list[Node], schema: dict[str, Any], reporter: Reporter
) -> None:
    index = build_link_index(nodes)
    relationship_fields = set(schema.get("relationships", {})) | set(
        RELATIONSHIP_FIELDS
    )
    for node in nodes:
        checked: set[str] = set()
        for field in relationship_fields:
            for target in relationship_targets(node, field):
                checked.add(target.casefold())
                if target_exists(target, index):
                    continue
                message = f"unresolved {field} target [[{target}]]"
                if node.staged:
                    reporter.warning(node.label, message)
                else:
                    reporter.error(node.label, message)

        for raw in WIKILINK_RE.findall(node.body):
            target = normalize_link(raw)
            if not target or target.casefold() in checked or target_exists(target, index):
                continue
            message = f"unresolved wikilink [[{target}]]"
            if node.staged or node.metadata.get("status") not in APPROVAL_STATUSES:
                reporter.warning(node.label, message)
            else:
                reporter.error(node.label, message)


def check_dependency_cycles(nodes: list[Node], reporter: Reporter) -> None:
    by_title: dict[str, str] = {}
    by_id: dict[str, str] = {}
    for node in nodes:
        title = node.metadata.get("title")
        node_id = node.metadata.get("node_id")
        if isinstance(title, str) and isinstance(node_id, str):
            by_title[title.casefold()] = node_id
            by_id[node_id] = node.label

    graph: dict[str, set[str]] = {node_id: set() for node_id in by_id}
    for node in nodes:
        source = node.metadata.get("node_id")
        if not isinstance(source, str):
            continue
        for target in relationship_targets(node, "depends_on"):
            target_id = by_title.get(target.casefold())
            if target_id:
                graph[source].add(target_id)

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(current: str, trail: list[str]) -> None:
        if current in visiting:
            cycle = trail[trail.index(current) :] + [current]
            reporter.error(by_id[current], f"depends_on cycle: {' -> '.join(cycle)}")
            return
        if current in visited:
            return
        visiting.add(current)
        for target in graph.get(current, set()):
            visit(target, trail + [target])
        visiting.remove(current)
        visited.add(current)

    for node_id in graph:
        visit(node_id, [node_id])


def main() -> int:
    reporter = Reporter()
    try:
        schema = load_yaml(SCHEMA_PATH)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        reporter.error(str(SCHEMA_PATH), f"cannot load schema: {exc}")
        return reporter.render()

    nodes = load_nodes(reporter)
    for node in nodes:
        check_metadata(node, schema, reporter)
        check_required_sections(node, schema, reporter)
    check_uniqueness(nodes, reporter)
    check_links(nodes, schema, reporter)
    check_dependency_cycles(nodes, reporter)
    print(f"Validated {len(nodes)} knowledge node(s)")
    return reporter.render()


if __name__ == "__main__":
    sys.exit(main())
