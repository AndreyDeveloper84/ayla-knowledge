---
node_id: ayla.foundation.canon-governance.canon-index
title: CANON_INDEX
type: moc
status: draft
version: "0.2"
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
updated: 2026-08-07
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
| Ayla Product Essence v1.2 | Essence | `00 Foundation\Ayla Product Essence.md` | DRAFT (v1.2, canonical_status: candidate) | v1.1 (approved 2026-07-30; Git history) | Targeted amendment 2026-08-07 per Owner Decisions AYLA-DEC-0063…0066 (OD-MVP-1…4): LDT removed from mandatory first-MVP critical path; representation-neutral value loop. Awaiting Product Owner Final Review — NOT YET CANONICAL. Canonical working version is stored in ayla-knowledge. |
| Ayla Product Essence v1.1 | Essence history | Git history (тот же файл, стабильное имя) | SUPERSEDED_PENDING_REAPPROVAL | v1.0 | Was CANONICAL 2026-07-30 → 2026-08-05; superseded by v1.2 candidate 2026-08-07, pending Product Owner Final Review. Basis of v1.1: AYLA-DEC-0026. |
| Ayla Living Digital Twin Manifesto | Foundation | `00 Foundation\Ayla Living Digital Twin Manifesto.md` | DRAFT (v1.1, canonical_status: candidate) | v1.0 (approved 2026-07-30; Git history) | Minimal targeted amendment 2026-08-07: §14 made conditional on LDT being included in a release (AYLA-DEC-0063 / OD-MVP-1); §1–13, §15–18 unchanged and remain in force where LDT is used. Awaiting Product Owner Final Review. Depends on: Ayla Product Essence v1.2. Sibling к Vision/Thesis/Principles; authoritative input для LDT-тем downstream-документов. |
| Ayla MVP Reset Roadmap | Operational | `02 Strategy\Ayla MVP Reset Roadmap.md` | CANONICAL | — | Операционный источник порядка перестройки и выпуска. Owner approved 2026-07-29. Не содержит LDT-specific текста — NO_CHANGE_REQUIRED при канонизации OD-MVP-1…4 (2026-08-07). Не переопределяет Product Essence и не занимает места в иерархии между Essence и Product Vision. |
| Product Vision | Foundation | `01 Product\Ayla Product Vision.md` | DRAFT (v2.1, canonical_status: candidate) | v2.0 (approved 2026-07-30; Git history) | Minimal derived-alignment amendment 2026-08-07 (DERIVED_UPSTREAM_ALIGNMENT, без отдельного amendment plan) per AYLA-DEC-0063…0066. Ниже Product Essence v1.2; Manifesto v1.1 — согласующий input. Awaiting Product Owner Final Review. |
| Product Thesis | Foundation | `02 Strategy\Ayla MVP Product Thesis.md` | DRAFT (v0.6, canonical_status: candidate) | v0.5 (approved 2026-07-30; Git history) | Targeted amendment 2026-08-07 per Amendment Plan v0.5 → v0.6: LDT-dependent MVP hypothesis заменена representation-neutral value loop. Ниже Essence v1.2 и Vision v2.1; Manifesto v1.1 — согласующий input. Awaiting Product Owner Final Review. |
| Product Principles | Foundation | `01 Product\Ayla Product Principles.md` | DRAFT (v0.2, canonical_status: candidate) | v0.1 (approved 2026-07-31; Git history) | Targeted amendment 2026-08-07 per Amendment Plan v0.1 → v0.2: 14 core principles (было 11); Contextual Proactivity, Safety & Wellness Boundary, User Outcome First, Product Restraint добавлены; Identity Continuity стала условной нормой внутри 4.3. Ниже Essence v1.2; не выше Vision v2.1 и Thesis v0.6. Awaiting Product Owner Final Review. Note: untracked scratch draft `00 Foundation\Ayla Product Principles.md` обнаружен в ходе этой канонизации — не используется как источник (нарушает §27 amendment plan, без frontmatter); требует решения владельца (удалить/архивировать). |
| MVP Scope | Foundation | `02 Strategy\Ayla MVP Scope and Release Contract.md` | DRAFT (v0.4, proposed, canonical_status: candidate) | v0.3 (Git history) | Targeted amendment 2026-08-07 per AYLA-DEC-0063…0066: LDT переведён в CONDITIONAL (не обязателен для MVP); Food Intelligence и Memory Foundation введены как явные IN_SCOPE capabilities. Foundation Window документ №4. canonization NOT_COMPLETE; Internal Consistency Review, Migration Readiness Review и Product Owner Final Review — pending. |
| Ayla Single-Provider Technical Pilot Execution Scope | Strategy execution | `02 Strategy\Ayla Single-Provider Technical Pilot Execution Scope.md` | DRAFT (v0.3, proposed, CROSS_DOCUMENT_ALIGNED) | — | Non-canonical execution scope for A0/A1/A2. Downstream of MVP Scope v0.3; не входит в Foundation hierarchy и не создаёт canonical dependency edge. |
| Ayla Multi-Provider Product Validation Execution Scope | Strategy execution | `02 Strategy\Ayla Multi-Provider Product Validation Execution Scope.md` | DRAFT (v0.2, proposed, CROSS_DOCUMENT_ALIGNED) | — | Non-canonical execution scope for B0/B1. Downstream of MVP Scope v0.3 и Single-Provider Execution Scope v0.3; не входит в Foundation hierarchy. |
| Ayla MVP v0.3 Downstream Migration Plan | Strategy execution | `02 Strategy\Ayla MVP v0.3 Downstream Migration Plan.md` | DRAFT (v0.1, proposed, INTERNALLY_APPROVED) | — | Non-canonical migration execution plan (waves D0–D6). Downstream of MVP Scope v0.3 и обоих execution scopes; не входит в Foundation hierarchy. |
| MVP User Journey | Foundation | `01 Product\User Journeys\Ayla MVP User Journey Specification.md` | PARTIALLY_ALIGNED (v1.2, содержит собственные owner decisions AYLA-DEC-0037…0054, 2026-08-04) | v1.1, v1.0 | Foundation Window документ №5. Требует alignment pass с AYLA-DEC-0063…0066 (OD-MVP-1…4, 2026-08-07): §6.3/§6.4-ссылки на MVP Scope §6.4 MUST_HAVE Twin-требования устарели после MVP Scope v0.4. Follow-up gate, не выполнен в этой канонизации. |
| Killer PRD | Legacy | `02 Strategy\Killer PRD.md`; `D:\Проекты\Ayla\Killer_PRD_v1.1_RU.md` | LEGACY REFERENCE ONLY | — | Только для поиска требований/решений/рисков. Не родительский документ и не основа структуры MVP Scope. |
