from __future__ import annotations

import copy
import unittest

import yaml

from scripts.validate_planning_rules import (
    CLOSED_KINDS,
    REGISTRY_PATH,
    UniqueKeyLoader,
    load_registry,
    validate,
)


def _valid_rule(**overrides: object) -> dict:
    rule: dict = {
        "rule_id": "PR-DURATION-0001",
        "kind": "DURATION",
        "status": "UNKNOWN",
        "value": {
            "reason": "NO_RULE_EXISTS",
            "asked_source": "ayla-knowledge:03 AI System/Contracts/planning-rules-registry.yaml",
            "as_of": "2026-09-08",
        },
        "unit": None,
        "applicability": {
            "scope": "GENERAL",
            "subject_kind": "canonical_service",
            "subject_ids": [],
            "conditions": [],
        },
        "provenance": {
            "source": "ayla-knowledge:03 AI System/Contracts/planning-rules-registry.yaml",
            "version": "0.1",
        },
    }
    rule.update(overrides)
    return rule


def _valid_registry(rules: list | None = None) -> dict:
    return {
        "registry": "ayla.planning-rules-registry",
        "registry_version": "0.1",
        "compatible_contract_version": "1.0",
        "status": "draft",
        "updated": "2026-09-08",
        "kinds": sorted(CLOSED_KINDS),
        "statuses": ["KNOWN", "UNKNOWN", "INTENTIONALLY_UNSUPPORTED"],
        "unknown_reasons": [
            "NO_RULE_EXISTS",
            "RULE_NOT_APPLICABLE",
            "SOURCE_UNREACHABLE",
            "SOURCE_STALE",
            "MAPPING_MISSING",
            "POLICY_WITHHELD",
        ],
        "rules": rules if rules is not None else [_valid_rule()],
    }


class PlanningRulesValidatorTests(unittest.TestCase):
    def test_committed_registry_is_valid(self) -> None:
        registry = load_registry(REGISTRY_PATH)
        self.assertEqual(validate(registry), [])

    def test_valid_minimal_registry_passes(self) -> None:
        self.assertEqual(validate(_valid_registry()), [])

    def test_fourteenth_kind_is_rejected(self) -> None:
        registry = _valid_registry()
        registry["kinds"] = sorted(CLOSED_KINDS) + ["MADE_UP_KIND"]
        self.assertTrue(any("kinds" in error for error in validate(registry)))

    def test_missing_kind_in_list_is_rejected(self) -> None:
        registry = _valid_registry()
        registry["kinds"] = sorted(CLOSED_KINDS - {"DURATION"})
        self.assertTrue(any("kinds" in error for error in validate(registry)))

    def test_unknown_status_value_is_rejected(self) -> None:
        registry = _valid_registry(rules=[_valid_rule(status="MAYBE")])
        errors = validate(registry)
        self.assertTrue(any("status" in error for error in errors))

    def test_missing_value_key_is_build_error_not_unknown(self) -> None:
        rule = _valid_rule()
        del rule["value"]
        errors = validate(_valid_registry(rules=[rule]))
        self.assertTrue(any("ошибка сборки, а не UNKNOWN" in error for error in errors))

    def test_unknown_with_null_value_is_rejected(self) -> None:
        errors = validate(_valid_registry(rules=[_valid_rule(value=None)]))
        self.assertTrue(any("value" in error for error in errors))

    def test_unknown_with_invented_reason_is_rejected(self) -> None:
        rule = _valid_rule(
            value={
                "reason": "PROBABLY_THREE_WEEKS",
                "asked_source": "ayla-knowledge:x",
                "as_of": "2026-09-08",
            }
        )
        errors = validate(_valid_registry(rules=[rule]))
        self.assertTrue(any("reason" in error for error in errors))

    def test_unknown_without_as_of_is_rejected(self) -> None:
        rule = _valid_rule(value={"reason": "NO_RULE_EXISTS", "asked_source": "ayla-knowledge:x"})
        errors = validate(_valid_registry(rules=[rule]))
        self.assertTrue(any("as_of" in error for error in errors))

    def test_unknown_with_unit_is_rejected(self) -> None:
        errors = validate(_valid_registry(rules=[_valid_rule(unit="days")]))
        self.assertTrue(any("unit" in error for error in errors))

    def test_intentionally_unsupported_with_value_is_rejected(self) -> None:
        rule = _valid_rule(status="INTENTIONALLY_UNSUPPORTED", value=14, unit="days")
        errors = validate(_valid_registry(rules=[rule]))
        self.assertTrue(any("INTENTIONALLY_UNSUPPORTED" in error for error in errors))

    def test_known_requires_value_and_unit(self) -> None:
        rule = _valid_rule(status="KNOWN", value=None, unit=None)
        errors = validate(_valid_registry(rules=[rule]))
        self.assertTrue(any("KNOWN требует заполненного value" in error for error in errors))
        self.assertTrue(any("KNOWN требует заполненного unit" in error for error in errors))

    def test_known_with_valid_value_passes(self) -> None:
        rule = _valid_rule(status="KNOWN", value=21, unit="days")
        self.assertEqual(validate(_valid_registry(rules=[rule])), [])

    def test_known_cannot_carry_unknown_shape(self) -> None:
        rule = _valid_rule(
            status="KNOWN",
            value={"reason": "NO_RULE_EXISTS"},
            unit="days",
        )
        errors = validate(_valid_registry(rules=[rule]))
        self.assertTrue(any("формы Unknown" in error for error in errors))

    def test_duplicate_rule_id_is_rejected(self) -> None:
        errors = validate(_valid_registry(rules=[_valid_rule(), _valid_rule()]))
        self.assertTrue(any("дубликат" in error for error in errors))

    def test_bad_rule_id_format_is_rejected(self) -> None:
        errors = validate(_valid_registry(rules=[_valid_rule(rule_id="duration-rule-1")]))
        self.assertTrue(any("rule_id" in error for error in errors))

    def test_bad_scope_is_rejected(self) -> None:
        rule = _valid_rule()
        rule["applicability"]["scope"] = "GLOBAL"
        errors = validate(_valid_registry(rules=[rule]))
        self.assertTrue(any("scope" in error for error in errors))

    def test_provenance_without_version_is_rejected(self) -> None:
        rule = _valid_rule()
        rule["provenance"] = {"source": "ayla-knowledge:x"}
        errors = validate(_valid_registry(rules=[rule]))
        self.assertTrue(any("provenance.version" in error for error in errors))

    def test_provenance_source_must_be_address(self) -> None:
        rule = _valid_rule()
        rule["provenance"] = {"source": "канон", "version": "0.1"}
        errors = validate(_valid_registry(rules=[rule]))
        self.assertTrue(any("provenance.source" in error for error in errors))

    def test_duplicate_yaml_key_is_rejected(self) -> None:
        with self.assertRaises(yaml.constructor.ConstructorError):
            yaml.load("kind: DURATION\nkind: EVENT_WINDOW\n", Loader=UniqueKeyLoader)

    def test_date_objects_from_yaml_are_accepted(self) -> None:
        registry = _valid_registry()
        registry["rules"][0]["value"]["as_of"] = __import__("datetime").date(2026, 9, 8)
        registry["updated"] = __import__("datetime").date(2026, 9, 8)
        self.assertEqual(validate(registry), [])

    def test_registry_is_serializable_roundtrip(self) -> None:
        registry = load_registry(REGISTRY_PATH)
        clone = copy.deepcopy(registry)
        self.assertEqual(validate(clone), [])


if __name__ == "__main__":
    unittest.main()
