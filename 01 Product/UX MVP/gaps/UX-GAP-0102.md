---
gap_id: UX-GAP-0102
severity: P0
detected_in: UX-CUST-001 (screen inventory customer)
date: 2026-07-29
status: in-progress
gap_status: open
node_id: ayla.ux.gap-0102
title: UX-GAP-0102 — Phase 2 activation gates не закрыты
type: specification
owner: UX Architecture
version: "0.1"
domain:
  - user-context
system_owner:
  - ayla-user-context
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

# UX-GAP-0102 — Phase 2 activation gates не закрыты

## annotation (2026-07-29, UX-SYNC-001)

Gap остаётся **open**, но это Phase 2 scope: при persistent memory disabled
(UX-OD-003 phase_1_session_only_service_necessity) он **не блокирует
Phase 1**. W2-экраны SCR-CUST-002/017 остаются BLOCKED до закрытия gates;
UX-OD-003 их не разблокирует.

## description

Все экраны, опирающиеся на persistent memory (W2), блокируются незакрытыми
gates Phase 2 (SRC-01 §10 п. 1, Consent Scope Registry §10.2): scope
`preference_memory` не approved; открыт CSR-OD-5 (canonical SoR для consent
records); не подтверждены формулировки Privacy Owner; не реализован runtime
authorization contract; отсутствует negative test «отсутствие consent → deny».

## why_it_matters

Экраны SCR-CUST-002 (consent request), SCR-CUST-017 (memory & privacy
controls: «Что Ayla знает обо мне», отзыв scope, «Забыть это», удаление
факта) и память-зависимые ветки SCR-CUST-004/003 (clarification suppression,
объяснение использования памяти) не могут получить required data и
entry/exit-контракт, пока не определены SoR consent records и runtime
authorization contract. Команды управления памятью — факты CSR §8
(SRC-02 Memory Interaction), т.е. обязательны при активации Phase 2.

## blocked_screens

SCR-CUST-002, SCR-CUST-017, SCR-CUST-018 (частично); memory-ветки
SCR-CUST-003, SCR-CUST-004 (W2)

## missing_decision

- Закрытие CSR-OD-5: canonical System of Record для consent records.
- Runtime authorization contract (проверка scope в runtime, fail-closed).
- Approval `preference_memory` + формулировки Privacy Owner.

## required_owner

Privacy Owner + Product Architecture (SoR decision); Product Owner — approval.

## recommended_artifact

Decision Record (CSR-OD-5) + Minimal Contract (runtime authorization contract).

## can_use_temporary_assumption

Да.

## temporary_assumption

Проектировать W2-экраны только на уровне inventory; детальную проработку
начинать после закрытия gates. Phase 1 считать полностью session-only
(SRC-01 §8 Privacy).

## acceptance_criteria

- CSR-OD-5 закрыт Decision Record; SoR consent records назван.
- Runtime authorization contract задокументирован и реализован; negative test
  «отсутствие consent → deny» существует.
- `preference_memory` approved; формулировки Privacy Owner подтверждены.
