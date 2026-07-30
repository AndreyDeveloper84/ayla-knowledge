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
| Ayla Product Essence v1.1 | Essence | `00 Foundation\Ayla Product Essence.md` | CANONICAL | v1.0 | Высший продуктовый источник. Owner approved 2026-07-30. Canonicalized from candidate commit `9e0a15d`. Basis: AYLA-DEC-0026. Canonical working version is stored in ayla-knowledge. External copies are non-authoritative. |
| Ayla Product Essence v1.0 | Essence history | Git history before v1.1 (тот же файл, стабильное имя) | SUPERSEDED | — | Superseded by v1.1 after owner approval 2026-07-30. Историческая версия доступна через Git history; физический архивный дубликат не создаётся. |
| Ayla Living Digital Twin Manifesto | Foundation | `00 Foundation\Ayla Living Digital Twin Manifesto.md` (планируемый) | MISSING / READY TO CREATE | — | Creation is now allowed after Product Essence v1.1 approval. Initial status after creation: DRAFT. Below Product Essence; cannot override it. |
| Ayla MVP Reset Roadmap | Operational | `02 Strategy\Ayla MVP Reset Roadmap.md` | CANONICAL | — | Операционный источник порядка перестройки и выпуска. Owner approved 2026-07-29. Canonical working version is stored in ayla-knowledge. External D: copy is non-authoritative. Не переопределяет Product Essence и не занимает места в иерархии между Essence и Product Vision. |
| Product Vision | Foundation | `01 Product\Ayla Product Vision.md` | — | — | Кандидат. Дубликаты в `D:\Проекты\Ayla` сверяются на Intake. |
| Product Thesis | Foundation | `02 Strategy\Ayla MVP Product Thesis.md` | — | — | Кандидат. Дубликаты в `D:\Проекты\Ayla` сверяются на Intake. |
| Product Principles | Foundation | — | MISSING / CREATE | — | Constitution — только conditional reference, не шаблон. |
| MVP Scope | Foundation | — | MISSING / CREATE FROM NEW CANON | — | Создаётся сверху вниз от нового канона. Существующий `02 Strategy\Ayla MVP Scope and Release Contract.md` классифицируется на Intake (ожидаемо LEGACY-вход). |
| MVP User Journey | Foundation | `01 Product\User Journeys\Ayla MVP User Journey Specification.md` | — | — | Кандидат. Версии в `D:\Проекты\Ayla` сверяются на Intake. |
| Killer PRD | Legacy | `02 Strategy\Killer PRD.md`; `D:\Проекты\Ayla\Killer_PRD_v1.1_RU.md` | LEGACY REFERENCE ONLY | — | Только для поиска требований/решений/рисков. Не родительский документ и не основа структуры MVP Scope. |
