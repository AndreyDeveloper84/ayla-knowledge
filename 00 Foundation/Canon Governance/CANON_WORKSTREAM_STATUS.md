---
node_id: ayla.foundation.canon-governance.canon-workstream-status
title: CANON_WORKSTREAM_STATUS
type: dashboard
status: draft
version: "0.3"
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

# CANON_WORKSTREAM_STATUS

Статус рабочих направлений канонизации.

```text
Current gate: FOUNDATION_REOPENED_BY_OWNER_DECISION
Blocker: NONE (owner decisions decided; document re-review pending)
Reopening basis: AYLA-DEC-0063…0066 (OD-MVP-1…4, 2026-08-07) — Living
  Digital Twin excluded from mandatory first-MVP critical path
Documents reopened: Product Essence (v1.1→v1.2), LDT Manifesto §14 only
  (v1.0→v1.1), Product Vision (v2.0→v2.1), Product Thesis (v0.5→v0.6),
  Product Principles (v0.1→v0.2), MVP Scope (v0.3→v0.4) — all
  status: draft / canonical_status: candidate, awaiting Product Owner
  Final Review
Prior MVP Scope migration (v0.3, Wave D0 COMPLETE, D1 next) — SUPERSEDED
  BY MVP Scope v0.4 candidate; Migration Plan v0.1 waves D0-D6 require
  re-evaluation against v0.4 before D1 resumes
Next action: Product Owner Final Review for the six candidate documents
  above, in upstream→downstream order; then re-plan downstream migration
  (User Journey v1.2 alignment; execution scope docs; Migration Plan v0.1)
```

> **2026-08-07 — MVP v2 canonization pass.** Owner Decisions OD-MVP-1…4
> (`Ayla MVP v2 — Owner Decisions`) reopened five Foundation documents
> previously marked COMPLETE/CANONICAL below (Essence, Vision, Thesis,
> Principles) plus MVP Scope (previously draft/candidate, migration
> in-progress) and the LDT Manifesto (minimal §14 fix only). This is an
> explicit, owner-authorized reopening — not a canon violation. The D0/D1
> MVP Scope v0.3 migration status described below is now historical
> context for what was in progress *before* this reopening; it does not
> describe current state. See amendment plans in this canonization pass
> and the six documents' own Change Logs for what changed and why.
> `Ayla MVP User Journey Specification v1.2` was **not** touched by this
> pass (it carries its own recent owner decision session, AYLA-DEC-0037…
> 0054, 2026-08-04) — its alignment with AYLA-DEC-0063…0066 is a
> registered follow-up gate.

Foundation Canon Window открыто 2026-07-30 (Essence v1.1 CANONICAL, Manifesto v1.0 CANONICAL). Порядок канонизации: Vision → Thesis → Principles → MVP Scope → User Journey. **Product Vision — was COMPLETE / CANONICAL (v2.0); reopened, now v2.1 candidate. Product Thesis — was COMPLETE / CANONICAL (v0.5); reopened, now v0.6 candidate. Product Principles — was COMPLETE / CANONICAL (v0.1, owner approved 2026-07-31); reopened, now v0.2 candidate.** Текущий документ (pre-reopening) — MVP Scope (v0.3, draft / proposed / candidate, CROSS_DOCUMENT_ALIGNED; canonization NOT_COMPLETE), теперь также reopened как v0.4 candidate. Оба execution scope (Single-Provider v0.3, Multi-Provider v0.2) non-canonical и ссылаются на MVP Scope v0.3 — version-pin устарел после v0.4, зарегистрировано как follow-up. Downstream-миграция по Ayla MVP v0.3 Downstream Migration Plan v0.1 (waves D0–D6, D0 was COMPLETE) требует пересмотра относительно MVP Scope v0.4 до возобновления D1.

## Модель источников

- Product Essence — высший продуктовый источник.
- MVP Reset Roadmap — операционный источник порядка перестройки и выпуска.
- Approved Owner Decisions — обязательные точечные решения в пределах своего scope.
- Owner Decision не может неявно переопределять Product Essence.

## Направления

| Workstream | Gate | Window | Last handoff |
|---|---|---|---|
| Foundation | OPEN / INITIALIZED | Foundation Canon Window (открыто 2026-07-30; Vision — COMPLETE v2.0, Thesis — COMPLETE v0.5, Principles — COMPLETE v0.1; текущий документ — MVP Scope v0.3 CROSS_DOCUMENT_ALIGNED, migration wave D0 COMPLETE; D1 NEXT по Migration Plan v0.1; subagents FORBIDDEN) | — |
| Living Digital Twin (Essence v1.1) | ESSENCE_V1_1_CANONICAL | Living Digital Twin Foundation Window (Phase A: COMPLETE; owner approved 2026-07-30, merge в `agent/ux-mvp`) | LIVING_DIGITAL_TWIN_ALIGNMENT_REPORT.md |
| Living Digital Twin Manifesto Phase B | COMPLETE | Manifesto CANONICAL / v1.0 (owner approval RECORDED 2026-07-30); subagents NOT_USED | LIVING_DIGITAL_TWIN_ALIGNMENT_REPORT.md |
| Domain | BLOCKED | — | — |
| UX | BLOCKED | — | — |
| AI architecture | BLOCKED | — | — |
| Engineering architecture | BLOCKED | — | — |
| API migration | BLOCKED | — | — |
| Implementation backlog | BLOCKED | — | — |

## Foundation gate model

```text
FOUNDATION_NOT_STARTED
FOUNDATION_ALIGNMENT_IN_PROGRESS
FOUNDATION_ALIGNMENT_COMPLETE
OWNER_DECISIONS_REQUIRED
FOUNDATION_CANONICALIZATION_IN_PROGRESS
FOUNDATION_READY_FOR_OWNER_REVIEW
FOUNDATION_COMPLETE
```

Критерии переходов между состояниями (включая обработку P0 и Owner Decisions) определены в `windows\foundation\FOUNDATION_WINDOW_CHARTER.md` и обязательны для обоих файлов в согласованном виде.

P0 не считается разрешённым только потому, что он оформлен как открытый Owner Decision.

- **FOUNDATION_ALIGNMENT_COMPLETE** — допустимы P0 со статусом `ESCALATED`, Owner Decisions со статусом `OPEN`, canonical rewrite ещё не начат.
- **OWNER_DECISIONS_REQUIRED** — каждый эскалированный P0 связан с конкретным Owner Decision с точным scope; canonical rewrite в затронутой области приостановлен до решения владельца.
- **FOUNDATION_READY_FOR_OWNER_REVIEW** — ноль P0 в статусах `OPEN` и `ESCALATED`; все применимые Owner Decisions `DECIDED` и применены; consistency review завершён; пять документов имеют статус `READY_FOR_OWNER_REVIEW`.
- **FOUNDATION_COMPLETE** — итоговый пакет одобрен Product Owner; пять документов получили `CANONICAL`; создан `FOUNDATION_HANDOFF.md`; в этом файле зафиксировано открытие следующего разрешённого gate.
