#!/usr/bin/env python3
"""Validate AMD-001 JSON Schema 2020-12 blocks and positive/negative fixtures.

Run from repository root:
    python scripts/validate_amd001_schemas.py

The script extracts all JSON Schema 2020-12 blocks from the AMD-001 Contract,
checks that each is a valid meta-schema, verifies stable `$id` values are unique,
validates positive fixtures, and verifies that negative fixtures are rejected.

Note: the contract was renumbered from AMD-020 to AMD-001 (DRF-899); stable
schema `$id` URLs retain the historical `amd020` path segment.
"""

import json
import pathlib
import re
import sys
from collections import defaultdict

from jsonschema import Draft202012Validator
from referencing.jsonschema import DRAFT202012

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTRACT = ROOT / "05 Architecture" / "AMD-001 C5 Pilot Personal Context Export-Forget Contract.md"
FIXTURE_DIR = ROOT / "tests" / "fixtures" / "amd001"
EXPECTED_SCHEMA_COUNT = 7


def extract_schemas(text: str):
    blocks = re.findall(r"```json\n(.*?)\n```", text, re.DOTALL)
    schemas = []
    for block in blocks:
        try:
            obj = json.loads(block)
        except json.JSONDecodeError as exc:
            print(f"WARN: skipping non-JSON block: {exc}")
            continue
        if isinstance(obj, dict) and obj.get("$schema") == "https://json-schema.org/draft/2020-12/schema":
            schemas.append(obj)
    return schemas


def schema_basename(schema_id: str) -> str:
    parts = schema_id.rstrip("/").split("/")
    # IDs are .../<name>/1.0 ; return the name segment.
    if len(parts) >= 2 and parts[-1].replace(".", "", 1).isdigit():
        return parts[-2]
    return parts[-1]


def check_meta(schema: dict) -> list[str]:
    errors = []
    if "$id" not in schema:
        errors.append("missing $id")
    if "type" not in schema:
        errors.append("missing root type")
    if "required" not in schema:
        errors.append("missing required")
    if "properties" not in schema and "$defs" not in schema:
        errors.append("missing properties/$defs")
    if "additionalProperties" not in schema:
        errors.append("missing additionalProperties")
    try:
        DRAFT202012.create_resource(schema)
    except Exception as exc:
        errors.append(f"meta-validation error: {exc}")
    return errors


def load_fixture(name: str) -> dict | None:
    path = FIXTURE_DIR / name
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def run() -> int:
    exit_code = 0
    if not CONTRACT.exists():
        print(f"ERROR: contract not found: {CONTRACT}")
        return 1

    text = CONTRACT.read_text(encoding="utf-8")
    schemas = extract_schemas(text)

    print(f"Found {len(schemas)} JSON Schema 2020-12 blocks")
    if len(schemas) != EXPECTED_SCHEMA_COUNT:
        print(f"ERROR: expected {EXPECTED_SCHEMA_COUNT} schemas, found {len(schemas)}")
        exit_code = 1

    # $id uniqueness
    ids = defaultdict(list)
    for i, schema in enumerate(schemas, 1):
        sid = schema.get("$id", f"no-$id-{i}")
        ids[sid].append(i)
    duplicates = {sid: idxs for sid, idxs in ids.items() if len(idxs) > 1}
    if duplicates:
        print(f"ERROR: duplicate $id values: {duplicates}")
        exit_code = 1

    # Meta validation
    meta_ok = 0
    meta_fail = 0
    for i, schema in enumerate(schemas, 1):
        sid = schema.get("$id", "no-$id")
        errors = check_meta(schema)
        if errors:
            print(f"  Schema {i} ({sid}): META_INVALID -> {errors}")
            meta_fail += 1
            exit_code = 1
        else:
            print(f"  Schema {i} ({sid}): meta-valid")
            meta_ok += 1

    # Fixture validation
    positive_ok = 0
    positive_fail = 0
    negative_ok = 0
    negative_fail = 0
    fixture_missing = 0

    for i, schema in enumerate(schemas, 1):
        sid = schema.get("$id", "no-$id")
        base = schema_basename(sid)
        validator = Draft202012Validator(schema)

        pos = load_fixture(f"{base}-positive.json")
        if pos is None:
            print(f"  Schema {i} ({sid}): POSITIVE fixture MISSING")
            fixture_missing += 1
            exit_code = 1
        else:
            try:
                validator.validate(pos)
                print(f"  Schema {i} ({sid}): positive fixture VALID")
                positive_ok += 1
            except Exception as exc:
                print(f"  Schema {i} ({sid}): positive fixture INVALID -> {exc}")
                positive_fail += 1
                exit_code = 1

        neg = load_fixture(f"{base}-negative.json")
        if neg is None:
            print(f"  Schema {i} ({sid}): NEGATIVE fixture MISSING")
            fixture_missing += 1
            exit_code = 1
        else:
            try:
                validator.validate(neg)
                print(f"  Schema {i} ({sid}): negative fixture UNEXPECTEDLY VALID -> FAIL")
                negative_fail += 1
                exit_code = 1
            except Exception:
                print(f"  Schema {i} ({sid}): negative fixture REJECTED (PASS)")
                negative_ok += 1

    print("\n=== Summary ===")
    print(f"Schemas found: {len(schemas)} (expected {EXPECTED_SCHEMA_COUNT})")
    print(f"Meta-valid: {meta_ok}; meta-invalid: {meta_fail}")
    print(f"Positive fixtures: {positive_ok} valid, {positive_fail} invalid, {fixture_missing} missing")
    print(f"Negative fixtures: {negative_ok} rejected, {negative_fail} unexpectedly valid, {fixture_missing} missing")

    if exit_code == 0:
        print("\nAll AMD-001 schema checks passed.")
    else:
        print("\nAMD-001 schema checks FAILED.")
    return exit_code


if __name__ == "__main__":
    sys.exit(run())
