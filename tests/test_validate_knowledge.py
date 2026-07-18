from __future__ import annotations

import unittest
from pathlib import Path

import yaml

from scripts.validate_knowledge import (
    ROOT,
    Node,
    Reporter,
    UniqueKeyLoader,
    check_links,
    check_metadata,
    load_yaml,
)


class KnowledgeValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = load_yaml(ROOT / ".knowledge" / "schema.yaml")

    def test_duplicate_frontmatter_key_is_rejected(self) -> None:
        with self.assertRaises(yaml.constructor.ConstructorError):
            yaml.load("title: One\ntitle: Two\n", Loader=UniqueKeyLoader)

    def test_versioned_canonical_filename_is_rejected(self) -> None:
        node = Node(
            path=ROOT / "00 Foundation" / "Example v1.2.md",
            metadata={
                "node_id": "ayla.example",
                "source_kind": "canonical",
                "system_owner": ["ayla-knowledge"],
            },
            body="",
        )
        reporter = Reporter()

        check_metadata(node, self.schema, reporter)

        self.assertTrue(
            any("filename must not contain a version suffix" in error for error in reporter.errors)
        )

    def test_versioned_node_id_is_rejected(self) -> None:
        node = Node(
            path=ROOT / "00 Foundation" / "Example.md",
            metadata={
                "node_id": "ayla.example.v1.2",
                "source_kind": "canonical",
                "system_owner": ["ayla-knowledge"],
            },
            body="",
        )
        reporter = Reporter()

        check_metadata(node, self.schema, reporter)

        self.assertTrue(
            any("node_id must not contain a version suffix" in error for error in reporter.errors)
        )

    def test_staged_missing_relationship_is_warning(self) -> None:
        node = Node(
            path=ROOT / "00 Foundation" / "Example.md",
            metadata={
                "node_id": "ayla.example",
                "title": "Example",
                "status": "review",
                "activation_status": "pending-infrastructure",
                "implements": ["[[Missing Foundation]]"],
            },
            body="",
        )
        reporter = Reporter()

        check_links([node], self.schema, reporter)

        self.assertEqual([], reporter.errors)
        self.assertTrue(
            any("Missing Foundation" in warning for warning in reporter.warnings)
        )

    def test_unknown_document_type_is_rejected(self) -> None:
        node = Node(
            path=ROOT / "00 Foundation" / "Example.md",
            metadata={
                "node_id": "ayla.example",
                "title": "Example",
                "type": "definitely-not-a-real-type",
                "source_kind": "canonical",
                "system_owner": ["ayla-knowledge"],
            },
            body="",
        )
        reporter = Reporter()

        check_metadata(node, self.schema, reporter)

        self.assertTrue(
            any("unknown document type" in error for error in reporter.errors)
        )

    def test_decision_log_type_requires_normative_sections(self) -> None:
        from scripts.validate_knowledge import check_required_sections

        node = Node(
            path=ROOT / "02 Strategy" / "Ayla Decision Log.md",
            metadata={
                "node_id": "ayla.example.decision-log",
                "title": "Example Decision Log",
                "type": "decision-log",
                "source_kind": "canonical",
                "system_owner": ["shared"],
            },
            body="# Empty\n",
        )
        reporter = Reporter()

        check_required_sections(node, self.schema, reporter)

        for section in ("Назначение", "Реестр решений", "Change Log"):
            self.assertTrue(
                any(
                    f"missing required section {section!r}" in error
                    for error in reporter.errors
                ),
                f"expected missing-section error for {section!r}",
            )


if __name__ == "__main__":
    unittest.main()
