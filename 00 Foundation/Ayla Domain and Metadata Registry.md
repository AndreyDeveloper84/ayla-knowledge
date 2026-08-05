---
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
  sha256: 6e39062d3e8aa7234f3cf904eb233bfddd03ad34b45a105b80c8cd87100261f5
  imported: 2026-07-19
generated_from:
  path: .knowledge/schema.yaml
  schema_version: "1.13"
  command: python scripts/render_domain_registry.py
---

# Ayla Domain and Metadata Registry v1.0

> GENERATED FILE. Не редактировать вручную. Изменения вносятся в
> `.knowledge/schema.yaml` или renderer и затем материализуются командой,
> указанной во frontmatter.

## 1. Purpose and authority

Документ предоставляет авторам и reviewers человекочитаемое представление
машинного metadata-контракта Ayla. Он не создаёт независимый набор enum:
таблицы ниже детерминированно сгенерированы из schema v1.13.

## 2. Source of truth

Машинным источником истины является `.knowledge/schema.yaml`. При расхождении
registry считается устаревшим, CI завершается ошибкой, а значение из registry
не применяется до повторной генерации.

## 3. Required metadata fields

Обязательные поля каждого активного Knowledge Node:

`node_id`, `title`, `type`, `status`, `version`, `owner`, `knowledge_area`, `system_owner`, `source_kind`, `classification`, `data_sensitivity`, `security_sensitivity`, `ai_indexing`, `export_policy`, `updated`, `review_cycle`.

Дополнительные обязательства могут включаться conditional rules и правилами
конкретного document type.

## 4. Controlled vocabularies

| Field | Allowed values |
|---|---|
| `status` | `idea`<br>`draft`<br>`review`<br>`approved`<br>`approved-with-amendments`<br>`implemented`<br>`planned`<br>`scheduled`<br>`in-progress`<br>`blocked`<br>`delivered`<br>`cancelled`<br>`deprecated`<br>`superseded`<br>`archived` |
| `activation_status` | `pending-infrastructure`<br>`active`<br>`suspended` |
| `source_kind` | `canonical`<br>`mirror`<br>`external`<br>`product-requirements` |
| `canonical_status` | `draft`<br>`candidate`<br>`approved`<br>`deprecated` |
| `knowledge_area` | `foundation`<br>`product`<br>`strategy`<br>`ai-system`<br>`domain-model`<br>`architecture`<br>`safety-governance`<br>`design`<br>`business`<br>`research`<br>`operations`<br>`sources` |
| `system_owner` | `ayla-platform`<br>`ayla-ai-core`<br>`ayla-conversation`<br>`ayla-user-context`<br>`ayla-recommendation`<br>`ayla-booking`<br>`ayla-provider-platform`<br>`ayla-mobile`<br>`ayla-mini-app`<br>`ayla-knowledge`<br>`shared`<br>`external`<br>`to-be-confirmed` |
| `source_repository` | `beautygo_backend`<br>`ai-bot-platform`<br>`ayla-knowledge`<br>`ayla-ai-core`<br>`external` |
| `term_maturity` | `planned`<br>`proposed`<br>`accepted`<br>`implemented`<br>`deprecated` |
| `domain` | `cross-domain`<br>`identity`<br>`consent`<br>`user-context`<br>`conversation`<br>`intent`<br>`recommendation`<br>`catalog`<br>`provider`<br>`booking`<br>`payment`<br>`nutrition`<br>`wellness`<br>`notification`<br>`analytics`<br>`marketing`<br>`loyalty` |
| `concerns` | `knowledge-management`<br>`governance`<br>`privacy`<br>`security`<br>`safety`<br>`observability`<br>`audit`<br>`compliance`<br>`explainability`<br>`localization`<br>`accessibility` |
| `classification` | `public`<br>`internal`<br>`confidential`<br>`restricted` |
| `data_sensitivity` | `none`<br>`low`<br>`medium`<br>`high`<br>`critical` |
| `data_categories` | `none`<br>`synthetic`<br>`pii`<br>`health`<br>`financial`<br>`credentials`<br>`raw-user-content`<br>`production-data` |
| `security_sensitivity` | `none`<br>`low`<br>`medium`<br>`high`<br>`critical` |
| `ai_indexing` | `allowed`<br>`metadata-only`<br>`denied` |
| `export_policy` | `full`<br>`sanitized`<br>`metadata-only`<br>`prohibited` |
| `review_cycle` | `monthly`<br>`quarterly`<br>`yearly`<br>`before-major-change`<br>`event-driven` |

## 5. Lifecycle transitions

| Current status | Allowed next statuses |
|---|---|
| `idea` | `draft`<br>`cancelled` |
| `draft` | `review`<br>`cancelled` |
| `review` | `draft`<br>`approved-with-amendments`<br>`approved`<br>`cancelled` |
| `approved-with-amendments` | `approved`<br>`implemented`<br>`superseded`<br>`deprecated` |
| `approved` | `implemented`<br>`superseded`<br>`deprecated` |
| `implemented` | `superseded`<br>`deprecated` |
| `planned` | `scheduled`<br>`cancelled` |
| `scheduled` | `in-progress`<br>`blocked`<br>`cancelled` |
| `in-progress` | `blocked`<br>`delivered`<br>`cancelled` |
| `blocked` | `scheduled`<br>`in-progress`<br>`cancelled` |
| `delivered` | `deprecated`<br>`superseded` |
| `deprecated` | `archived` |
| `superseded` | `archived` |
| `archived` | — |

Переход, отсутствующий в таблице, запрещён без предварительного изменения
schema и review migration impact.

## 6. Document types

| Type | Normative | Required sections or metadata |
|---|---:|---|
| `knowledge-architecture-specification` | yes | `Назначение и нормативность`<br>`Модель источников истины`<br>`Модель версионности`<br>`Ревью и управление изменениями`<br>`Валидация`<br>`Миграция из backend`<br>`Definition of Done`<br>`Change Log` |
| `constitution` | yes | `Преамбула`<br>`Термины`<br>`Статья I. Миссия и предметная область Ayla`<br>`Статья IV. Экономическая нейтральность`<br>`Статья XII. Границы компетенции, безопасность и соразмерность`<br>`Статья XIV. Автономия, согласия и приватность`<br>`Управление Конституцией`<br>`Заключительное положение` |
| `foundation` | yes | — |
| `product-thesis` | yes | — |
| `specification` | yes | — |
| `ai-specification` | yes | `Responsibility`<br>`Inputs`<br>`Outputs`<br>`Owns`<br>`Does not own` |
| `safety-specification` | yes | — |
| `architecture-specification` | yes | — |
| `adr` | yes | `adr_id`<br>`decision_status`<br>`revision`<br>`amendments`<br>`superseded_by` |
| `decision-log` | yes | `Назначение`<br>`Реестр решений`<br>`Change Log` |
| `moc` | no | — |
| `glossary` | no | — |
| `terminology-standard` | yes | `Purpose and authority`<br>`Правила использования`<br>`Key term authority matrix`<br>`Change process`<br>`Definition of Done`<br>`Change Log` |
| `metadata-registry` | yes | `Purpose and authority`<br>`Source of truth`<br>`Required metadata fields`<br>`Controlled vocabularies`<br>`Lifecycle transitions`<br>`Document types`<br>`Relationship semantics`<br>`Ownership model`<br>`Conditional and safety rules`<br>`Update procedure`<br>`Definition of Done`<br>`Change Log` |
| `user-journey-specification` | yes | `Purpose`<br>`Journey Operating Model`<br>`Journey Overview`<br>`Stage Specifications`<br>`Memory Interaction`<br>`Recommendation and Proactivity Gates`<br>`Cross-channel Experience`<br>`Business Alignment`<br>`Metrics`<br>`Constitutional Traceability`<br>`Change Log` |
| `domain-context-map` | yes | `Document Status and Purpose`<br>`Scope and Source Documents`<br>`Context Mapping Method`<br>`Domain Classification — Commentary` |
| `domain-specification` | yes | — |
| `data-inventory-matrix` | yes | `Purpose`<br>`Matrix`<br>`Definitions`<br>`Critical Boundaries`<br>`Change Log` |
| `dashboard` | no | — |
| `source-placeholder` | no | — |

Неизвестный `type` отклоняется validator.

## 7. Relationship semantics

| Field | Directed | Acyclic | Target must exist |
|---|---:|---:|---:|
| `depends_on` | yes | yes | yes |
| `supersedes` | yes | yes | yes |
| `implements` | yes | no | yes |
| `adr` | yes | no | yes |
| `related` | no | no | yes |
| `conflicts_with` | no | no | yes |

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
domain_context:
  when_knowledge_area:
  - product
  - ai-system
  - domain-model
  - architecture
  - safety-governance
  - design
  - business
  require:
  - domain
  non_empty: true
mirror:
  when:
    source_kind: mirror
  require:
  - source_repository
  - source_path
  - source_ref
  - synced
  - source_content_hash
  forbid_manual_edit: true
restricted:
  when:
    classification: restricted
  allowed_ai_indexing:
  - denied
  - metadata-only
  allowed_export_policy:
  - metadata-only
  - prohibited
confidential:
  when:
    classification: confidential
  allowed_export_policy:
  - sanitized
  - metadata-only
  - prohibited
internal:
  when:
    classification: internal
  allowed_export_policy:
  - full
  - sanitized
  - metadata-only
  - prohibited
denied_ai_index:
  when:
    ai_indexing: denied
  allowed_export_policy:
  - metadata-only
  - prohibited
p0_p1:
  when_priority:
  - P0
  - P1
  require:
  - owner
  - review_cycle
  - depends_on
provisional_system_owner:
  when_system_owner_contains:
  - to-be-confirmed
  allowed_status:
  - idea
  - draft
  - review
  - planned
  forbidden_status:
  - approved
  - approved-with-amendments
  - implemented
  - delivered
  allowed_until: 2026-08-15
```

### Field constraints

```yaml
node_id:
  format: ^[a-z0-9]+(?:[.-][a-z0-9]+)*$
  immutable: true
  unique: false
system_owner:
  type: list
  min_items: 1
  unique_items: true
  items_from_enum: system_owner
source_repository:
  optional: true
  value_from_enum: source_repository
data_categories:
  optional: true
  require_when_data_sensitivity:
  - low
  - medium
  - high
  - critical
owners:
  optional: true
  type: list
  unique_items: true
  warn_unless_contains_field: owner
```

### Uniqueness rules

```yaml
node_id:
  source_kind: canonical
  active_statuses:
  - approved
  - approved-with-amendments
  - implemented
  - delivered
  excluded_statuses:
  - archived
  - superseded
  - deprecated
  - cancelled
title:
  source_kind: canonical
  active_statuses:
  - approved
  - approved-with-amendments
  - implemented
  - delivered
  excluded_statuses:
  - archived
  - superseded
  - deprecated
  - cancelled
```

### AI export policy

```yaml
default: deny
require_explicit_allow: true
prohibited_content:
- real-user-pii
- real-health-data
- raw-user-messages
- production-dumps
- credentials
- encryption-material
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
