---
node_id: ayla.foundation.canon-governance.canon-workstream-status
title: CANON_WORKSTREAM_STATUS
type: dashboard
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

# CANON_WORKSTREAM_STATUS

Статус рабочих направлений канонизации.

```text
Current gate: FOUNDATION_IN_PROGRESS
Blocker: NONE
Current Foundation document: Product Vision
```

Foundation Canon Window открыто 2026-07-30 после завершения Living Digital Twin Phase B (Essence v1.1 CANONICAL, Manifesto v1.0 CANONICAL). Порядок канонизации: Vision → Thesis → Principles → MVP Scope → User Journey (см. `windows\foundation\FOUNDATION_CANONIZATION_SEQUENCE.md`).

## Модель источников

- Product Essence — высший продуктовый источник.
- MVP Reset Roadmap — операционный источник порядка перестройки и выпуска.
- Approved Owner Decisions — обязательные точечные решения в пределах своего scope.
- Owner Decision не может неявно переопределять Product Essence.

## Направления

| Workstream | Gate | Window | Last handoff |
|---|---|---|---|
| Foundation | OPEN / INITIALIZED | Foundation Canon Window (открыто 2026-07-30; текущий документ — Product Vision; subagents FORBIDDEN) | — |
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
