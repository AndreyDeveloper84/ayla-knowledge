---
node_id: ayla.foundation.canon-governance.foundation-input-manifest
title: FOUNDATION_INPUT_MANIFEST
type: specification
status: approved
version: "1.0"
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
updated: 2026-07-30
review_cycle: monthly
---

# FOUNDATION_INPUT_MANIFEST

Входной манифест Foundation Canon Window (OPEN / INITIALIZED, 2026-07-30). Каноническая база — репозиторий `ayla-knowledge`, ветка `agent/ux-mvp`.

## REQUIRED

```text
00 Foundation\Ayla Product Essence.md                          — v1.1 CANONICAL, высший источник
00 Foundation\Ayla Living Digital Twin Manifesto.md            — v1.0 CANONICAL, согласующий input для LDT-тем
00 Foundation\Canon Governance\CANON_INDEX.md
00 Foundation\Canon Governance\CANON_WORKSTREAM_STATUS.md
00 Foundation\Canon Governance\OWNER_DECISION_REGISTER.md      — read-only для окна
00 Foundation\Canon Governance\CANON_CONFLICT_REGISTER.md
```

Рабочие версии документов scope (классифицированы в `FOUNDATION_DOCUMENT_STATUS.md`):

```text
01 Product\Ayla Product Vision.md                — CANONICAL v2.0 (approved source; owner approved 2026-07-30)
02 Strategy\Ayla MVP Product Thesis.md           — CURRENT INPUT FOR NEXT WINDOW (Product Thesis Canon Window)
Product Principles — файл отсутствует (создаётся в окне)
02 Strategy\Ayla MVP Scope and Release Contract.md
01 Product\User Journeys\Ayla MVP User Journey Specification.md
```

## CONDITIONAL

Читать только при конкретном unresolved вопросе; каждое чтение записывается (File / Reason / Question resolved / Influence on Foundation document):

```text
02 Strategy\Killer PRD.md
Strategy-документы (02 Strategy: Decision Log, Documentation Roadmap, MVP Reset Roadmap)
05 Architecture\Ayla MVP Recommendation Contract.md
06 Safety and Governance\Consent Scope Registry.md
06 Safety and Governance\Data Inventory Matrix.md
Safety-документы (06 Safety and Governance)
Domain-документы (05 Architecture: Core Domain Model, Domain Event Registry и др.)
UX-документы (01 Product\UX MVP)
AI-документы (03 AI System)
Architecture-документы (05 Architecture)
Roadmaps
```

## FORBIDDEN BY DEFAULT

```text
legacy-копии вне канонического репозитория
D:\-копии (все)
99 Archive\**
полные кодовые базы, tests, backlog
handoff dumps, agent scratch files
старые candidate worktrees
внешние продуктовые заметки
```
