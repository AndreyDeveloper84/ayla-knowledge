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

    def test_terminology_standard_requires_normative_sections(self) -> None:
        from scripts.validate_knowledge import check_required_sections

        node = Node(
            path=ROOT / "00 Foundation" / "Ayla Glossary.md",
            metadata={
                "node_id": "ayla.example.glossary",
                "title": "Example Glossary",
                "type": "terminology-standard",
                "source_kind": "canonical",
                "system_owner": ["ayla-knowledge"],
            },
            body="# Empty\n",
        )
        reporter = Reporter()

        check_required_sections(node, self.schema, reporter)

        for section in (
            "Purpose and authority",
            "Правила использования",
            "Key term authority matrix",
            "Change process",
            "Definition of Done",
            "Change Log",
        ):
            self.assertTrue(
                any(
                    f"missing required section {section!r}" in error
                    for error in reporter.errors
                ),
                f"expected missing-section error for {section!r}",
            )

    def test_generated_domain_registry_matches_schema(self) -> None:
        from scripts.render_domain_registry import OUTPUT_PATH, render_registry

        self.assertEqual(
            render_registry(self.schema),
            OUTPUT_PATH.read_text(encoding="utf-8"),
        )

    def test_user_journey_specification_requires_normative_sections(self) -> None:
        from scripts.validate_knowledge import check_required_sections

        node = Node(
            path=ROOT / "01 Product" / "User Journeys" / "Example.md",
            metadata={
                "node_id": "ayla.example.user-journey",
                "title": "Example User Journey",
                "type": "user-journey-specification",
                "source_kind": "canonical",
                "system_owner": ["shared"],
            },
            body="# Empty\n",
        )
        reporter = Reporter()

        check_required_sections(node, self.schema, reporter)

        for section in (
            "Purpose",
            "Journey Operating Model",
            "Journey Overview",
            "Stage Specifications",
            "Memory Interaction",
            "Recommendation and Proactivity Gates",
            "Cross-channel Experience",
            "Business Alignment",
            "Metrics",
            "Constitutional Traceability",
            "Change Log",
        ):
            self.assertTrue(
                any(
                    f"missing required section {section!r}" in error
                    for error in reporter.errors
                ),
                f"expected missing-section error for {section!r}",
            )

    def test_user_journey_normative_semantics_are_not_regressed(self) -> None:
        path = (
            ROOT
            / "01 Product"
            / "User Journeys"
            / "Ayla User Journey Specification.md"
        )
        body = path.read_text(encoding="utf-8")

        required_fragments = (
            "### Intent Type",
            "### Goal Category",
            "### Product Lifecycle Goal",
            "S2 Minimal Discovery → S3 Lightweight Intent Confirmation",
            "### User-Initiated Recommendation Gate",
            "### Proactive Readiness Gate",
            "Signal или Explicit Statement → Memory Proposal",
            "Backend publishes `booking.confirmed`",
            "Ayla переходит в S8, не подтверждает и не рекомендует",
            "enter_when:\n      all_of:",
            "`execution_failed` ведёт в Recovery",
        )
        forbidden_fragments = (
            "Классы намерений (Intent Classes)",
            "минимум 3 из 4 обязательных слотов",
            "переход к Stage 4 с минимальным контекстом",
            "Я запомнила:",
            "Ayla confirms booking",
            "Ayla не запрещает, но уточняет",
            "Есть новый контекст (например, сезонная акция)",
        )

        for fragment in required_fragments:
            self.assertIn(fragment, body)
        for fragment in forbidden_fragments:
            self.assertNotIn(fragment, body)


if __name__ == "__main__":
    unittest.main()
