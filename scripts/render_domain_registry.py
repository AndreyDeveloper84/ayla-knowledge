#!/usr/bin/env python3
"""Render the human-readable metadata registry from the canonical schema."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / ".knowledge" / "schema.yaml"
OUTPUT_PATH = ROOT / "00 Foundation" / "Ayla Domain and Metadata Registry.md"
SOURCE_SHA256 = "6e39062d3e8aa7234f3cf904eb233bfddd03ad34b45a105b80c8cd87100261f5"


def load_schema() -> dict[str, Any]:
    with SCHEMA_PATH.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def cell(value: Any) -> str:
    if isinstance(value, bool):
        return "yes" if value else "no"
    if value is None:
        return "—"
    if isinstance(value, list):
        return "<br>".join(f"`{item}`" for item in value) or "—"
    return str(value).replace("|", "\\|")


def yaml_block(value: Any) -> str:
    return yaml.safe_dump(
        value,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    ).rstrip()


def render_registry(schema: dict[str, Any]) -> str:
    schema_version = str(schema["schema_version"])
    required = schema.get("required_fields", [])
    enums = schema.get("enums", {})
    transitions = schema.get("lifecycle_transitions", {})
    document_types = schema.get("document_type_rules", {})
    relationships = schema.get("relationships", {})

    enum_rows = "\n".join(
        f"| `{name}` | {cell(values)} |" for name, values in enums.items()
    )
    lifecycle_rows = "\n".join(
        f"| `{source}` | {cell(targets)} |" for source, targets in transitions.items()
    )
    type_rows = "\n".join(
        "| `{}` | {} | {} |".format(
            name,
            cell(rules.get("normative", False)),
            cell(rules.get("require_sections", rules.get("require", []))),
        )
        for name, rules in document_types.items()
    )
    relationship_rows = "\n".join(
        "| `{}` | {} | {} | {} |".format(
            name,
            cell(rules.get("directed")),
            cell(rules.get("acyclic")),
            cell(rules.get("target_must_exist")),
        )
        for name, rules in relationships.items()
    )

    return f"""---
node_id: ayla.foundation.domain-metadata-registry
title: Ayla Domain and Metadata Registry
type: metadata-registry
status: review
activation_status: pending-infrastructure
version: "1.0"
owner: Product Architecture
priority: P0
knowledge_area:
  - foundation
domain: []
concerns:
  - knowledge-management
  - governance
system_owner:
  - ayla-knowledge
source_repository: ayla-knowledge
created: 2026-07-18
updated: 2026-07-19
source_kind: canonical
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
review_cycle: monthly
implements: []
depends_on:
  - "[[Ayla Knowledge Architecture Specification]]"
related:
  - "[[Ayla Glossary]]"
  - "[[Knowledge Schema Reference]]"
supersedes: []
migration_source:
  repository: beautygo_backend
  path: docs/00 Foundation/Ayla Domain and Metadata Registry v1.0.md
  tracked_in_source_git: false
  sha256: {SOURCE_SHA256}
  imported: 2026-07-19
generated_from:
  path: .knowledge/schema.yaml
  schema_version: "{schema_version}"
  command: python scripts/render_domain_registry.py
---

# Ayla Domain and Metadata Registry v1.0

> GENERATED FILE. Не редактировать вручную. Изменения вносятся в
> `.knowledge/schema.yaml` или renderer и затем материализуются командой,
> указанной во frontmatter.

## 1. Purpose and authority

Документ предоставляет авторам и reviewers человекочитаемое представление
машинного metadata-контракта Ayla. Он не создаёт независимый набор enum:
таблицы ниже детерминированно сгенерированы из schema v{schema_version}.

## 2. Source of truth

Машинным источником истины является `.knowledge/schema.yaml`. При расхождении
registry считается устаревшим, CI завершается ошибкой, а значение из registry
не применяется до повторной генерации.

## 3. Required metadata fields

Обязательные поля каждого активного Knowledge Node:

{", ".join(f"`{field}`" for field in required)}.

Дополнительные обязательства могут включаться conditional rules и правилами
конкретного document type.

## 4. Controlled vocabularies

| Field | Allowed values |
|---|---|
{enum_rows}

## 5. Lifecycle transitions

| Current status | Allowed next statuses |
|---|---|
{lifecycle_rows}

Переход, отсутствующий в таблице, запрещён без предварительного изменения
schema и review migration impact.

## 6. Document types

| Type | Normative | Required sections or metadata |
|---|---:|---|
{type_rows}

Неизвестный `type` отклоняется validator.

## 7. Relationship semantics

| Field | Directed | Acyclic | Target must exist |
|---|---:|---:|---:|
{relationship_rows}

Дополнительные ограничения конкретной связи определены непосредственно в
`.knowledge/schema.yaml`.

## 8. Ownership model

- `owner` — accountable роль или команда; это свободный человекочитаемый текст.
- `system_owner` — один или несколько bounded systems из одноимённого enum.
- `source_repository` — репозиторий канонического источника или mirror source.
- `domain` — предметная область, но не автоматическое назначение владельца.

Schema пока не задаёт default mapping `domain → system_owner`. Такой mapping
нельзя выводить из имени domain: его введение меняет архитектурную
ответственность и требует отдельного ADR. До этого каждый документ указывает
ownership явно, а `to-be-confirmed` допускается только по provisional rule.

## 9. Conditional and safety rules

### Conditional rules

```yaml
{yaml_block(schema.get("conditional_rules", {}))}
```

### Field constraints

```yaml
{yaml_block(schema.get("field_constraints", {}))}
```

### Uniqueness rules

```yaml
{yaml_block(schema.get("uniqueness_rules", {}))}
```

### AI export policy

```yaml
{yaml_block(schema.get("ai_export", {}))}
```

## 10. Update procedure

1. Изменить `.knowledge/schema.yaml` и повысить `schema_version`.
2. Оценить migration impact для существующих nodes и automation.
3. Выполнить `python scripts/render_domain_registry.py`.
4. Выполнить renderer в режиме `--check`, validator и unit tests.
5. Провести pull-request review schema и сгенерированного diff вместе.

## 11. Definition of Done

- содержимое registry детерминированно совпадает с schema;
- неизвестные document types отклоняются;
- enum и lifecycle не поддерживаются вручную в другом документе;
- ownership dimensions разделены и не создают скрытого domain mapping;
- CI проверяет актуальность generated file.

## 12. Knowledge Node versioning (Variant C)

> Source of truth: Owner Decision Session 2026-08-05, Variant C.

**Knowledge Node** — логическая сущность, идентифицируемая неизменным `node_id`. Knowledge Node не является конкретной редакцией документа и не создаётся заново при каждой версии.

**Revision** — материализованная редакция Knowledge Node в конкретный момент времени. Редакции различаются полем `version` и историей Git, но сохраняют один и тот же `node_id`.

**Active Canon** — revision со `source_kind: canonical` и `status` из множества активных canonical-статусов (`approved`, `approved-with-amendments`, `implemented`, `delivered`). На каждый Knowledge Node одновременно допускается только одна Active Canon.

**Historical Revision** — предыдущая редакция Knowledge Node, которая не является Active Canon, но сохраняет тот же `node_id`. Исторические редакции могут существовать одновременно с Active Canon.

**Superseded Revision** — редакция, явно переведённая в терминальный статус `superseded`, `deprecated`, `archived` или `cancelled`. Она не участвует в проверках Active Canon.

**Правило уникальности (Variant C):** уникальность `node_id` и `title` проверяется только среди Active Canon revisions. Coexistence approved-редакции и candidate-редакции одного Knowledge Node не является конфликтом. Одновременное наличие двух Active Canon revisions с одним `node_id` или `title` — ошибка.

# Change Log

## v1.0 — 2026-07-19

- planned stub материализован как schema-generated registry;
- добавлены required fields, enums, lifecycle, document types и relationships;
- разделены `owner`, `system_owner`, `source_repository` и `domain`;
- зафиксировано отсутствие неутверждённого default domain ownership mapping;
- добавлены deterministic renderer и CI drift check.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail when the committed registry differs from rendered output",
    )
    args = parser.parse_args()
    rendered = render_registry(load_schema())

    if args.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
            print(
                "Domain and Metadata Registry is stale; "
                "run python scripts/render_domain_registry.py"
            )
            return 1
        print("Domain and Metadata Registry is up to date")
        return 0

    OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"Rendered {OUTPUT_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
