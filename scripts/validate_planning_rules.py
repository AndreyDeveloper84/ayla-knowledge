#!/usr/bin/env python3
"""Validate the Ayla planning rules registry.

Проверяет ``03 AI System/Contracts/planning-rules-registry.yaml`` против
PLANNING_CONSTRAINTS_CONTRACT_v1.0.md (§3 закрытый перечень kind, §4 форма
UNKNOWN, §5 provenance) и направления владельца от 08.09.2026 (статусы
KNOWN / UNKNOWN / INTENTIONALLY_UNSUPPORTED).

Главный инвариант: ``UNKNOWN`` — значение, а не отсутствие поля. Отсутствие
поля ``value`` — ошибка сборки, а не UNKNOWN (контракт §4.1).
"""

from __future__ import annotations

import datetime
import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "03 AI System" / "Contracts" / "planning-rules-registry.yaml"

REGISTRY_NAME = "ayla.planning-rules-registry"

CLOSED_KINDS = {
    "CAPABILITY_SEMANTICS",
    "SERVICE_CAPABILITY_MAPPING",
    "DURATION",
    "EVENT_WINDOW",
    "MIN_INTERVAL",
    "MAX_INTERVAL",
    "REPETITION",
    "SEQUENCE",
    "PRECONDITION",
    "COMPATIBILITY",
    "INCOMPATIBILITY",
    "RECOVERY_WINDOW",
    "SAFETY_CONSTRAINT",
}

CLOSED_STATUSES = {"KNOWN", "UNKNOWN", "INTENTIONALLY_UNSUPPORTED"}

CLOSED_UNKNOWN_REASONS = {
    "NO_RULE_EXISTS",
    "RULE_NOT_APPLICABLE",
    "SOURCE_UNREACHABLE",
    "SOURCE_STALE",
    "MAPPING_MISSING",
    "POLICY_WITHHELD",
}

CLOSED_SCOPES = {"GENERAL", "TENANT", "MARKETPLACE"}
CLOSED_SUBJECT_KINDS = {"capability", "canonical_service", "tenant_offer", "category"}

RULE_ID_RE = re.compile(r"^PR-[A-Z0-9_]+(?:-[A-Z0-9_]+)*$")
VERSION_RE = re.compile(r"^\d+\.\d+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

REQUIRED_RULE_FIELDS = {
    "rule_id",
    "kind",
    "value",
    "unit",
    "applicability",
    "provenance",
    "status",
}


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


def load_registry(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = yaml.load(handle, Loader=UniqueKeyLoader)
    if not isinstance(data, dict):
        raise ValueError(f"реестр должен быть mapping, получено {type(data).__name__}")
    return data


def _is_date(value: Any) -> bool:
    # YAML парсит незакавыченную дату в datetime.date — обе формы допустимы.
    if isinstance(value, datetime.date):
        return True
    return isinstance(value, str) and bool(DATE_RE.match(value))


def _check_header(registry: dict[str, Any], errors: list[str]) -> None:
    if registry.get("registry") != REGISTRY_NAME:
        errors.append(f"registry: ожидалось {REGISTRY_NAME!r}, получено {registry.get('registry')!r}")
    version = registry.get("registry_version")
    if not isinstance(version, str) or not VERSION_RE.match(version):
        errors.append(f"registry_version: ожидалась строка вида 'X.Y', получено {version!r}")
    contract = registry.get("compatible_contract_version")
    if not isinstance(contract, str) or not VERSION_RE.match(contract):
        errors.append(
            f"compatible_contract_version: ожидалась строка вида 'X.Y', получено {contract!r}"
        )
    if not isinstance(registry.get("status"), str) or not registry["status"]:
        errors.append("status реестра: обязательная непустая строка")
    if not _is_date(registry.get("updated")):
        errors.append(f"updated: ожидалась дата YYYY-MM-DD, получено {registry.get('updated')!r}")

    kinds = registry.get("kinds")
    if not isinstance(kinds, list) or set(kinds) != CLOSED_KINDS or len(kinds) != len(CLOSED_KINDS):
        errors.append(
            "kinds: обязан быть ровно закрытым перечнем из 13 типов контракта §3; "
            f"получено {kinds!r}"
        )
    statuses = registry.get("statuses")
    if not isinstance(statuses, list) or set(statuses) != CLOSED_STATUSES:
        errors.append(f"statuses: обязан быть {sorted(CLOSED_STATUSES)}, получено {statuses!r}")
    reasons = registry.get("unknown_reasons")
    if not isinstance(reasons, list) or set(reasons) != CLOSED_UNKNOWN_REASONS:
        errors.append(
            f"unknown_reasons: обязан быть закрытым перечнем §4.2, получено {reasons!r}"
        )


def _check_applicability(rule_id: str, value: Any, errors: list[str]) -> None:
    if not isinstance(value, dict):
        errors.append(f"{rule_id}: applicability должен быть mapping")
        return
    scope = value.get("scope")
    if scope not in CLOSED_SCOPES:
        errors.append(f"{rule_id}: applicability.scope ∈ {sorted(CLOSED_SCOPES)}, получено {scope!r}")
    subject_kind = value.get("subject_kind")
    if subject_kind not in CLOSED_SUBJECT_KINDS:
        errors.append(
            f"{rule_id}: applicability.subject_kind ∈ {sorted(CLOSED_SUBJECT_KINDS)}, "
            f"получено {subject_kind!r}"
        )
    for field in ("subject_ids", "conditions"):
        items = value.get(field)
        if not isinstance(items, list):
            errors.append(f"{rule_id}: applicability.{field} должен быть списком")


def _check_provenance(rule_id: str, value: Any, errors: list[str]) -> None:
    if not isinstance(value, dict):
        errors.append(f"{rule_id}: provenance должен быть mapping")
        return
    source = value.get("source")
    if not isinstance(source, str) or ":" not in source or not source.split(":", 1)[1]:
        errors.append(
            f"{rule_id}: provenance.source обязан быть адресом '<repo>:<artifact>[:<node>]', "
            f"получено {source!r}"
        )
    version = value.get("version")
    if not isinstance(version, str) or not version:
        errors.append(f"{rule_id}: provenance.version обязан быть непустой строкой")


def _check_value_by_status(rule: dict[str, Any], errors: list[str]) -> None:
    rule_id = rule.get("rule_id", "<без rule_id>")
    status = rule.get("status")
    value = rule.get("value")
    unit = rule.get("unit")

    if status == "KNOWN":
        if value is None:
            errors.append(f"{rule_id}: KNOWN требует заполненного value")
        elif isinstance(value, dict) and {"reason", "asked_source", "as_of"} & set(value):
            errors.append(f"{rule_id}: KNOWN не может нести поля формы Unknown (reason/asked_source/as_of)")
        if not isinstance(unit, str) or not unit:
            errors.append(f"{rule_id}: KNOWN требует заполненного unit")
    elif status == "UNKNOWN":
        if not isinstance(value, dict):
            errors.append(
                f"{rule_id}: UNKNOWN обязан нести value={{reason, asked_source, as_of}} "
                f"(контракт §4.1), получено {value!r}"
            )
            return
        reason = value.get("reason")
        if reason not in CLOSED_UNKNOWN_REASONS:
            errors.append(
                f"{rule_id}: value.reason ∈ {sorted(CLOSED_UNKNOWN_REASONS)}, получено {reason!r}"
            )
        asked_source = value.get("asked_source")
        if not isinstance(asked_source, str) or not asked_source:
            errors.append(f"{rule_id}: value.asked_source обязан быть непустым адресом источника")
        if not _is_date(value.get("as_of")):
            errors.append(f"{rule_id}: value.as_of ожидалась дата YYYY-MM-DD")
        if unit is not None:
            errors.append(f"{rule_id}: при UNKNOWN unit обязан быть null")
    elif status == "INTENTIONALLY_UNSUPPORTED":
        if value is not None:
            errors.append(
                f"{rule_id}: INTENTIONALLY_UNSUPPORTED требует value: null — "
                f"тип пуст по решению владельца, значение запрещено"
            )
        if unit is not None:
            errors.append(f"{rule_id}: при INTENTIONALLY_UNSUPPORTED unit обязан быть null")


def _check_rule(rule: Any, seen_ids: set[str], errors: list[str]) -> None:
    if not isinstance(rule, dict):
        errors.append(f"rule: ожидался mapping, получено {type(rule).__name__}")
        return
    rule_id = rule.get("rule_id", "<без rule_id>")

    missing = REQUIRED_RULE_FIELDS - set(rule)
    if missing:
        errors.append(
            f"{rule_id}: отсутствуют обязательные поля {sorted(missing)}; "
            f"отсутствие value — ошибка сборки, а не UNKNOWN (контракт §4.1)"
        )
        return

    if not isinstance(rule_id, str) or not RULE_ID_RE.match(rule_id):
        errors.append(f"rule_id {rule_id!r}: ожидался формат 'PR-<ВИД>-<NNNN>'")
    elif rule_id in seen_ids:
        errors.append(f"{rule_id}: дубликат rule_id")
    else:
        seen_ids.add(rule_id)

    if rule.get("kind") not in CLOSED_KINDS:
        errors.append(f"{rule_id}: kind ∈ закрытого перечня §3, получено {rule.get('kind')!r}")
    if rule.get("status") not in CLOSED_STATUSES:
        errors.append(
            f"{rule_id}: status ∈ {sorted(CLOSED_STATUSES)}, получено {rule.get('status')!r}"
        )
        return  # без валидного статуса форму value проверять нельзя

    _check_value_by_status(rule, errors)
    _check_applicability(rule_id, rule.get("applicability"), errors)
    _check_provenance(rule_id, rule.get("provenance"), errors)


def validate(registry: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    _check_header(registry, errors)
    rules = registry.get("rules")
    if not isinstance(rules, list):
        errors.append("rules: обязан быть списком записей")
        return errors
    seen_ids: set[str] = set()
    for rule in rules:
        _check_rule(rule, seen_ids, errors)
    return errors


def main() -> int:
    try:
        registry = load_registry(REGISTRY_PATH)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"FAIL: реестр не читается: {exc}", file=sys.stderr)
        return 1
    errors = validate(registry)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    rules = registry.get("rules", [])
    by_status: dict[str, int] = {}
    for rule in rules:
        by_status[rule["status"]] = by_status.get(rule["status"], 0) + 1
    summary = ", ".join(f"{status}={count}" for status, count in sorted(by_status.items()))
    print(
        f"OK: {REGISTRY_PATH.relative_to(ROOT)} — "
        f"registry_version {registry['registry_version']}, "
        f"{len(rules)} записей ({summary})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
