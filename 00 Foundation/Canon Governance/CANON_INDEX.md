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
| Ayla Living Digital Twin Manifesto | Foundation | `00 Foundation\Ayla Living Digital Twin Manifesto.md` | CANONICAL (v1.0, canonical_status: approved) | — | Approved by Product Owner 2026-07-30. Depends on: Ayla Product Essence v1.1. Final editorial cleanup completed in `b072a05`. Cannot override Product Essence. Sibling к Vision/Thesis/Principles; authoritative input для LDT-тем downstream-документов. |
| Ayla MVP Reset Roadmap | Operational | `02 Strategy\Ayla MVP Reset Roadmap.md` | CANONICAL | — | Операционный источник порядка перестройки и выпуска. Owner approved 2026-07-29. Canonical working version is stored in ayla-knowledge. External D: copy is non-authoritative. Не переопределяет Product Essence и не занимает места в иерархии между Essence и Product Vision. |
| Product Vision | Foundation | `01 Product\Ayla Product Vision.md` | CANONICAL (v2.0, canonical_status: approved) | v1.4 (Git history) | Foundation Window документ №1 — COMPLETE. Owner approved 2026-07-30. Ниже Product Essence v1.1; Manifesto v1.0 — согласующий input для LDT-положений. Не является источником выше Essence. |
| Product Thesis | Foundation | `02 Strategy\Ayla MVP Product Thesis.md` | CANONICAL (v0.5, canonical_status: approved) | v0.4 (Git history) | Foundation Window документ №2 — COMPLETE. Owner approved 2026-07-30. Ниже Essence v1.1 и Vision v2.0; Manifesto v1.0 — согласующий input. Authoritative input для Principles, MVP Scope, User Journey, Measurement Framework. |
| Product Principles | Foundation | — | MISSING / CREATE | — | Foundation Window документ №3. Создаётся от Essence v1.1 + Manifesto v1.0; Constitution — только conditional reference, не шаблон. |
| MVP Scope | Foundation | `02 Strategy\Ayla MVP Scope and Release Contract.md` | DRAFT (v0.2, proposed) | — | Foundation Window документ №4. Способ канонизации (rewrite from new canon по раннему ruling vs align существующего draft) определяется в окне; при materially unresolved выборе — эскалация владельцу. |
| MVP User Journey | Foundation | `01 Product\User Journeys\Ayla MVP User Journey Specification.md` | PARTIALLY_ALIGNED (v1.0, approved до LDT-канона) | — | Foundation Window документ №5. Требует LDT-alignment и повторного owner approval. |
| Killer PRD | Legacy | `02 Strategy\Killer PRD.md`; `D:\Проекты\Ayla\Killer_PRD_v1.1_RU.md` | LEGACY REFERENCE ONLY | — | Только для поиска требований/решений/рисков. Не родительский документ и не основа структуры MVP Scope. |
