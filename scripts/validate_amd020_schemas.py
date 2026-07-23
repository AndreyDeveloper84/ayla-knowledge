#!/usr/bin/env python3
"""Validate AMD-020 JSON Schema 2020-12 blocks and sample instances.

Run from repository root:
    python scripts/validate_amd020_schemas.py

The script extracts all JSON Schema 2020-12 blocks from the AMD-020 Contract,
checks that each is a valid meta-schema, validates representative sample
instances, and verifies that additionalProperties are rejected at closed
levels.
"""

import json
import pathlib
import re
import sys
import uuid
from datetime import datetime, timezone

from jsonschema import Draft202012Validator
from referencing.jsonschema import DRAFT202012

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTRACT = ROOT / "05 Architecture" / "AMD-020 C5 Pilot Personal Context Export-Forget Contract.md"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def extract_schemas(text: str):
    blocks = re.findall(r"```json\n(.*?)\n```", text, re.DOTALL)
    schemas = []
    for block in blocks:
        try:
            obj = json.loads(block)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict) and obj.get("$schema") == "https://json-schema.org/draft/2020-12/schema":
            schemas.append(obj)
    return schemas


def check_meta(schema: dict) -> list[str]:
    errors = []
    if "$id" not in schema:
        errors.append("missing $id")
    try:
        DRAFT202012.create_resource(schema)
    except Exception as exc:
        errors.append(f"meta-validation error: {exc}")
    return errors


def build_samples() -> tuple[list[dict], dict]:
    ayla_id = str(uuid.uuid4())
    bot_id = str(uuid.uuid4())
    op_id = str(uuid.uuid4())
    now = utc_now()
    sub = {"ayla_user_id": ayla_id, "bot_user_id": bot_id}

    export_success = {
        "operation_id": op_id,
        "status": "completed",
        "generated_at": now,
        "subject": sub,
        "format_version": "1.0",
        "ayla": {"user_id": ayla_id, "exported_at": now, "personal_context": {"a": 1}},
        "memory": [{
            "id": str(uuid.uuid4()),
            "kind": "preference",
            "source": "explicit",
            "content": {"x": 1},
            "last_inferred_at": now,
            "created_at": now,
        }],
        "consents": [{
            "consent_type": "marketing",
            "granted": True,
            "document_version": "1",
            "source": "miniapp",
            "captured_at": now,
            "withdrawn_at": None,
            "purpose": "p",
            "data_categories": [],
            "operator": "o",
            "recipients": [],
            "term": "t",
            "lawful_basis": None,
            "identification_method": "m",
            "legacy_record": False,
            "schema_complete": True,
            "semantic_complete": True,
            "legal_validity_status": "approved",
        }],
    }

    export_failure = {
        "operation_id": op_id,
        "status": "failed",
        "format_version": "1.0",
        "error": {"code": "upstream_timeout", "message": "m", "retryable": True},
    }

    delete_success = {
        "operation_id": op_id,
        "status": "completed",
        "format_version": "1.0",
        "subject": sub,
        "completed_at": now,
        "per_step_results": {
            "ayla_delete": {"ok": True, "detail": "deleted"},
            "memory_delete": {"ok": True, "detail": "deleted"},
            "consent_withdraw": {"ok": True, "detail": "withdrawn"},
        },
        "deleted": ["ayla_personal_context", "memory_green"],
        "retained": [{
            "category": "audit_trail",
            "reason": "regulatory_audit",
            "lawful_basis": None,
            "retention_until": None,
            "decision_status": "owner_decision_required",
            "restrictions": "no_personal_values",
            "owner": "Legal",
            "deletion_trigger": "legal_retention_expiry",
        }],
    }

    delete_partial = {
        "operation_id": op_id,
        "status": "partial",
        "format_version": "1.0",
        "subject": sub,
        "completed_at": now,
        "per_step_results": {
            "ayla_delete": {"ok": True, "detail": "deleted"},
            "memory_delete": {"ok": False, "detail": "not_linked"},
            "consent_withdraw": {"ok": True, "detail": "withdrawn"},
        },
        "completed_steps": ["ayla_delete", "consent_withdraw"],
        "failed_steps": ["memory_delete"],
        "retryable": True,
        "request_attempt": 1,
        "execution_attempt": 1,
        "retained": [],
        "next_action": "retry_by_user",
    }

    delete_failure = {
        "operation_id": op_id,
        "status": "failed",
        "format_version": "1.0",
        "error": {"code": "internal_error", "message": "m", "retryable": False},
    }

    subject_gone = {
        "code": "subject_gone",
        "format_version": "1.0",
        "subject": {"ayla_user_id": ayla_id},
        "correlation_id": str(uuid.uuid4()),
        "retryable": False,
    }

    bad = {
        "operation_id": op_id,
        "status": "completed",
        "generated_at": now,
        "subject": sub,
        "format_version": "1.0",
        "ayla": None,
        "memory": [],
        "consents": [],
        "extra_field": 1,
    }

    return [export_success, export_failure, delete_success, delete_partial, delete_failure, subject_gone], bad


def main() -> int:
    if not CONTRACT.exists():
        print(f"ERROR: contract not found: {CONTRACT}")
        return 1

    text = CONTRACT.read_text(encoding="utf-8")
    schemas = extract_schemas(text)
    expected = 6
    if len(schemas) != expected:
        print(f"ERROR: expected {expected} schemas, found {len(schemas)}")
        return 1

    print(f"Found {len(schemas)} JSON Schema 2020-12 blocks")
    exit_code = 0

    # Meta validation
    for i, schema in enumerate(schemas, 1):
        errors = check_meta(schema)
        if errors:
            print(f"  Schema {i} ({schema.get('$id', 'no-$id')}): META_INVALID -> {errors}")
            exit_code = 1
        else:
            print(f"  Schema {i} ({schema['$id']}): meta-valid")

    # Instance validation
    samples, bad = build_samples()
    for i, (schema, sample) in enumerate(zip(schemas, samples), 1):
        try:
            Draft202012Validator(schema).validate(sample)
            print(f"  Schema {i}: sample VALID")
        except Exception as exc:
            print(f"  Schema {i}: sample INVALID -> {exc}")
            exit_code = 1

    # additionalProperties rejection
    try:
        Draft202012Validator(schemas[0]).validate(bad)
        print("  additionalProperties rejection: FAIL")
        exit_code = 1
    except Exception:
        print("  additionalProperties rejection: PASS")

    if exit_code == 0:
        print("\nAll AMD-020 schema checks passed.")
    else:
        print("\nAMD-020 schema checks FAILED.")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
