#!/usr/bin/env python3
"""Validate machine-readable JSON Schema contracts registered in .knowledge/schema.yaml.

Run from repository root:
    python scripts/validate_contract_schemas.py

Для каждой записи ``machine_readable_contracts`` с ``format: json-schema``:

* файл читается как JSON и проверяется мета-схемой JSON Schema 2020-12;
* ``$id`` уникален среди зарегистрированных схем;
* поле ``contract_version`` схемы совпадает с ``version`` записи реестра;
* каждая позитивная фикстура ``<fixtures>/valid_*.json`` проходит схему;
* каждая негативная фикстура ``<fixtures>/invalid_*.json`` схемой ОТВЕРГАЕТСЯ —
  фикстура, которую схема пропустила, — ошибка (негатив, который ничего не
  ловит, хуже отсутствия теста).

Пустой каталог фикстур — ошибка: схема без свидетелей не считается проверенной.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_REGISTRY = ROOT / ".knowledge" / "schema.yaml"


def registered_json_schemas() -> dict[str, dict[str, Any]]:
    data = yaml.safe_load(SCHEMA_REGISTRY.read_text(encoding="utf-8"))
    entries = data.get("machine_readable_contracts") or {}
    return {name: entry for name, entry in entries.items() if entry.get("format") == "json-schema"}


def validate_entry(name: str, entry: dict[str, Any], seen_ids: dict[str, str]) -> list[str]:
    errors: list[str] = []
    path = ROOT / entry["path"]
    try:
        schema = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{name}: схема не читается: {exc}"]

    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:  # jsonschema.SchemaError
        errors.append(f"{name}: не проходит мета-схему 2020-12: {exc}")
        return errors

    schema_id = schema.get("$id")
    if not isinstance(schema_id, str) or not schema_id:
        errors.append(f"{name}: нет $id")
    elif schema_id in seen_ids:
        errors.append(f"{name}: $id {schema_id!r} уже занят {seen_ids[schema_id]!r}")
    else:
        seen_ids[schema_id] = name

    declared = entry.get("version")
    cv = schema.get("properties", {}).get("contract_version", {})
    if "contract_version" not in schema.get("required", []):
        errors.append(f"{name}: contract_version обязан быть в required")
    if "const" in cv:
        if cv["const"] != declared:
            errors.append(
                f"{name}: properties.contract_version.const={cv['const']!r} "
                f"не совпадает с version={declared!r} в реестре"
            )
    elif "pattern" in cv:
        # Совместимая minor допускается, неизвестная major отвергается (правило версий контрактов).
        major = str(declared).split(".")[0]
        probe_ok = Draft202012Validator(cv).is_valid(declared)
        probe_next_major = Draft202012Validator(cv).is_valid(f"{int(major) + 1}.0")
        if not probe_ok:
            errors.append(f"{name}: pattern contract_version не принимает объявленную version={declared!r}")
        if probe_next_major:
            errors.append(f"{name}: pattern contract_version принимает следующую major — неизвестная major не отвергается")
    else:
        errors.append(f"{name}: properties.contract_version должен задавать const или pattern")

    fixtures = ROOT / entry["fixtures"]
    valid = sorted(fixtures.glob("valid_*.json"))
    invalid = sorted(fixtures.glob("invalid_*.json"))
    if not valid or not invalid:
        errors.append(f"{name}: нужны и valid_*.json, и invalid_*.json в {entry['fixtures']}")
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for fixture in valid:
        instance = json.loads(fixture.read_text(encoding="utf-8"))
        problems = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
        if problems:
            errors.append(f"{name}: позитивная фикстура {fixture.name} отвергнута: {problems[0].message}")
    for fixture in invalid:
        instance = json.loads(fixture.read_text(encoding="utf-8"))
        if validator.is_valid(instance):
            errors.append(f"{name}: негативная фикстура {fixture.name} ПРОШЛА схему — негатив ничего не ловит")
    return errors


def validate_all() -> list[str]:
    errors: list[str] = []
    seen_ids: dict[str, str] = {}
    entries = registered_json_schemas()
    if not entries:
        return ["machine_readable_contracts: нет ни одной json-schema — проверять нечего"]
    for name, entry in sorted(entries.items()):
        errors.extend(validate_entry(name, entry, seen_ids))
    return errors


def main() -> int:
    errors = validate_all()
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    names = ", ".join(sorted(registered_json_schemas()))
    print(f"OK: json-schema contracts validated — {names}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
