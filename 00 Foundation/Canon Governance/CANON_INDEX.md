---
node_id: ayla.foundation.canon-governance.canon-index
title: CANON_INDEX
type: moc
status: draft
version: "0.1"
owner: Product Owner
knowledge_area:
  - foundation
system_owner:
  - ayla-knowledge
source_repository: ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
created: 2026-07-29
updated: 2026-07-29
review_cycle: monthly
---

# CANON_INDEX

Управляющий реестр канонических документов Ayla. Содержит только статусы и ссылки — не контент.

## Допустимые статусы

```text
CANONICAL
CANONICAL_DRAFT
READY_FOR_OWNER_REVIEW
DRAFT
LEGACY
DUPLICATE
MISSING
SUPERSEDED
```

Статус `CANONICAL` присваивается только после owner approval. Foundation Canon Window самостоятельно доводит документы максимум до `READY_FOR_OWNER_REVIEW`.

## Реестр

Статус `—` означает: классификация будет присвоена на Foundation Intake and Alignment Pass. Неподтверждённые статусы не присваиваются.

| Document | Layer | Canonical file | Status | Supersedes | Notes |
|---|---|---|---|---|---|
| Ayla Product Essence v1.0 | Essence | `00 Foundation\Ayla Product Essence.md` | CANONICAL | — | Высший продуктовый источник. Owner approved 2026-07-29. Canonical working version is stored in ayla-knowledge. External D: copy is non-authoritative. Остаётся CANONICAL до утверждения v1.1; в SUPERSEDED не переводить до owner approval v1.1. |
| Ayla Product Essence v1.1 | Essence | `00 Foundation\Ayla Product Essence.md` на ветке `canon/essence-v1.1-candidate` | READY_FOR_OWNER_REVIEW | v1.0 (after approval) | Semantic patch по AYLA-DEC-0026 (Living Digital Twin). Кандидат подготовлен 2026-07-29 на отдельной ветке (`6327947`), revision pass по owner review (CHANGES_REQUESTED: P0=0, P1=5) применён 2026-07-29 (`9e0a15d`); merge запрещён до owner approval; после approval v1.1 → CANONICAL, v1.0 → SUPERSEDED. Alignment: `windows\living-digital-twin\LIVING_DIGITAL_TWIN_ALIGNMENT_REPORT.md`. |
| Ayla Living Digital Twin Manifesto | Foundation | `00 Foundation\Ayla Living Digital Twin Manifesto.md` (планируемый) | MISSING / CREATE AFTER ESSENCE V1.1 APPROVAL | — | Ниже Product Essence; не может её переопределять. Первоначальный статус после создания: DRAFT. |
| Ayla MVP Reset Roadmap | Operational | `02 Strategy\Ayla MVP Reset Roadmap.md` | CANONICAL | — | Операционный источник порядка перестройки и выпуска. Owner approved 2026-07-29. Canonical working version is stored in ayla-knowledge. External D: copy is non-authoritative. Не переопределяет Product Essence и не занимает места в иерархии между Essence и Product Vision. |
| Product Vision | Foundation | `01 Product\Ayla Product Vision.md` | — | — | Кандидат. Дубликаты в `D:\Проекты\Ayla` сверяются на Intake. |
| Product Thesis | Foundation | `02 Strategy\Ayla MVP Product Thesis.md` | — | — | Кандидат. Дубликаты в `D:\Проекты\Ayla` сверяются на Intake. |
| Product Principles | Foundation | — | MISSING / CREATE | — | Constitution — только conditional reference, не шаблон. |
| MVP Scope | Foundation | — | MISSING / CREATE FROM NEW CANON | — | Создаётся сверху вниз от нового канона. Существующий `02 Strategy\Ayla MVP Scope and Release Contract.md` классифицируется на Intake (ожидаемо LEGACY-вход). |
| MVP User Journey | Foundation | `01 Product\User Journeys\Ayla MVP User Journey Specification.md` | — | — | Кандидат. Версии в `D:\Проекты\Ayla` сверяются на Intake. |
| Killer PRD | Legacy | `02 Strategy\Killer PRD.md`; `D:\Проекты\Ayla\Killer_PRD_v1.1_RU.md` | LEGACY REFERENCE ONLY | — | Только для поиска требований/решений/рисков. Не родительский документ и не основа структуры MVP Scope. |
