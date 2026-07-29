---
gap_id: UX-GAP-0106
severity: P0
detected_in: UX-CUST-001 (screen inventory customer)
date: 2026-07-29
status: delivered
gap_status: closed
closed_date: 2026-07-29
resolution: UX-OD-002 (для MVP)
node_id: ayla.ux.gap-0106
title: "UX-GAP-0106 — Human handoff не определён (SRC-02 OQ2): тупиковые состояния N1/N7"
type: specification
owner: UX Architecture
version: "0.1"
domain:
  - cross-domain
system_owner:
  - ayla-conversation
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

# UX-GAP-0106 — Human handoff не определён (SRC-02 OQ2): тупиковые состояния N1/N7

## resolution (2026-07-29)

Закрыт для MVP решением UX-OD-002 honest_self_service_terminal_fallback
(`decisions/ux-owner-decisions.md`): human handoff в MVP НЕ требуется,
operator chat — deferred. При повторной неудаче (N1/N7) Ayla прямо сообщает
о неудаче, не обещает оператора, не имитирует живую поддержку, НЕ выдаёт
контакты мастера/салона автоматически. Обязательные действия пользователя:
retry, reformulate, return_to_previous_safe_step, try_later, exit; при ошибке
booking — возврат к выбору слота, если данные актуальны. Constraints:
no_false_success, no_fake_operator_availability,
no_automatic_provider_contact_disclosure, preserve_safe_session_context.
Тупики N1/N7 устранены определённым пользовательским выходом — release
minimum SRC-01 §8 выполняется для MVP.

Будущий human handoff вынесен в `gaps/UX-GAP-P1-registry.md` → UX-GAP-P1-08
(P1, Later, Operations Runbook).

## description (исходная формулировка)

Негативные сценарии N1 (Ayla не поняла запрос после повторного уточнения) и
N7 (повторный сбой tool/LLM) завершаются состоянием human handoff, помеченным
proposal: порог перехода к оператору/человеку и сама процедура не определены
в источниках (SRC-02 OQ2). Предполагаемый владелец решения — Pilot Operations
Runbook (Roadmap §9.3), который не материализован.

## why_it_matters

SRC-01 §8 (Non-Functional Minimum, Product) требует: «fallback существует;
критических тупиков нет». Без определённого handoff N1 и N7 — именно
критические тупики сквозного сценария пилота. Экран/состояние SCR-CUST-019
невозможно спроектировать, пока неизвестно, что происходит дальше: чат с
оператором, контакты мастера, отложенный callback.

## blocked_screens

SCR-CUST-019; как fallback-выход — SCR-CUST-003 (N1), SCR-CUST-007 (N7)

## missing_decision

- Порог срабатывания handoff (число неудачных попыток, классы ошибок).
- Процедура: канал связи с человеком, SLA ответа, что видит пользователь.
- Владелец операционной процедуры на пилот.

## required_owner

Product Owner + Operations (Pilot Operations Runbook, Roadmap §9.3).

## recommended_artifact

Decision Record (порог и UX handoff) + Specification (раздел Pilot Operations
Runbook).

## can_use_temporary_assumption

Да.

## temporary_assumption

До решения: после повторной неудачи показывать честное сообщение о
невозможности продолжить + предложение вернуться позже (факт — полная UJS
Error Recovery 3, по SRC-02 этап 2/N7), без обещания живого оператора.

## acceptance_criteria

- OQ2 закрыт: порог и процедура handoff зафиксированы.
- Pilot Operations Runbook содержит handoff-процедуру с владельцем.
- Состояния N1/N7 имеют определённый пользовательский выход, не тупик.
