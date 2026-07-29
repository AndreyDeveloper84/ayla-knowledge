---
gap_id: UX-GAP-0103
severity: P0
detected_in: UX-CUST-001 (screen inventory customer)
date: 2026-07-29
status: delivered
gap_status: closed
closed_date: 2026-07-29
resolution: sync error — документ существует и approved
node_id: ayla.ux.gap-0103
title: UX-GAP-0103 — Ayla Intent Model Specification не материализован
type: specification
owner: UX Architecture
version: "0.1"
domain:
  - intent
system_owner:
  - ayla-ai-core
knowledge_area:
  - product
source_repository: ayla-knowledge
source_kind: product-requirements
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
updated: 2026-07-29
review_cycle: monthly
---

# UX-GAP-0103 — Ayla Intent Model Specification не материализован

## resolution (2026-07-29)

**Ошибка синхронизации.** Gap возник из устаревшей ссылки в SRC-02 (OQ7).
Фактическая проверка (UX-SYNC-001): Ayla Intent Model Specification v0.9.2
существует — `ayla-knowledge/03 AI System/Ayla Intent Model Specification.md`,
frontmatter: status approved, decision_status accepted, owner AI Architecture,
updated 2026-07-28. Output Contract (10 обязательных полей, инварианты,
status_reason enum) определён; Acceptance Criteria выполнены полностью;
machine-readable appendix материализован (`intent-registry.yaml`,
`slot-registry.yaml`, `intent-output.schema.json`, OQ-9/OQ-10).

Acceptance criteria этого gap выполнены: спецификация материализована и
approved; для каждого MVP intent type известны slot requirements и
confidence bands (числовые пороги — versioned runtime configuration
ayla-ai-core, OQ-1 закрыт owner ruling 2026-07-28).

Резидуального UX-gap нет: contract-test fixtures и исполняемые тесты —
implementation-owned артефакты ayla-ai-core (волна 3, AYLA-DEC-0014), не
UX-зависимость. Открытые OQ спецификации (таймаут clarification, метрики,
persistence intent_id) — downstream решения других владельцев, не блокируют
проектирование SCR-CUST-003. Переоформление в P1 не требуется.

## description (исходная формулировка — устарела)

Этапы 4–5 (Intent detection, Clarification) ссылаются на output contract
intent resolution — intent types, required/optional slots, confidence levels,
`requires_clarification` — который фиксируется в Ayla Intent Model
Specification; документ в разработке и не материализован (SRC-02 OQ7;
SRC-01 §10 п. 3 — predecessor document волны 1). Минимальный набор intent
types зафиксирован (SRC-02 этап 4), но слоты и пороги confidence — нет.

## why_it_matters

SCR-CUST-003 (intent & clarification dialog) — основная разговорная
поверхность W1: без slot-контракта нельзя определить required data, набор
состояний уточнения и exit-критерии. Также частично затрагивается
SCR-CUST-004 (confidence влияет на показ рекомендации). Это release blocker
по SRC-01 §10 п. 3.

## blocked_screens

SCR-CUST-003; частично SCR-CUST-004

## missing_decision

Материализация и approval Ayla Intent Model Specification: intent types,
required/optional slots, confidence levels, output contract
`requires_clarification` (Roadmap §3.1).

## required_owner

Product Owner / AI-команда (владелец Intent Model Specification).

## recommended_artifact

Specification (Ayla Intent Model Specification, planned — Roadmap §3.1).

## can_use_temporary_assumption

Да.

## temporary_assumption

Проектировать диалог уточнения по зафиксированным фактам SRC-02 (не более
5 вопросов Discovery, продолжение при отказе отвечать, suppression известного)
и по минимальному набору intent types этапа 4; конкретные slots/confidence
оставить параметризуемыми.

## acceptance_criteria

- Intent Model Specification материализован и approved.
- Формулировки этапов 4–5 SRC-02 сверены с ним (OQ7 закрыт).
- Для каждого MVP intent type известны required slots и confidence-пороги.
