---
gap_id: UX-GAP-0105
severity: P0
detected_in: UX-CUST-001 (screen inventory customer)
date: 2026-07-29
status: delivered
gap_status: closed
closed_date: 2026-07-29
resolution: UX-OD-001 (owner part)
node_id: ayla.ux.gap-0105
title: UX-GAP-0105 — Ветки переноса/отмены записи без stage specifications (SRC-02 OQ5)
type: specification
owner: UX Architecture
version: "0.1"
domain:
  - booking
system_owner:
  - ayla-booking
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

# UX-GAP-0105 — Ветки переноса/отмены записи без stage specifications (SRC-02 OQ5)

## resolution (2026-07-29)

Закрыт в owner-части решением UX-OD-001
minimal_conversational_cancel_and_reschedule (`decisions/ux-owner-decisions.md`):
отмена — через диалог в bot DM (identify_booking → show_booking_summary →
explicit_confirmation → authoritative_cancellation → result); перенос =
cancel_then_create_new_booking. Смена мастера при переносе, расширенные
альтернативы и standalone full-screen flows отложены в W2. Constraints:
no cancelled state до authoritative confirmation; обязательны cancel_pending
и cancel_failed; неатомарность переноса раскрывается пользователю заранее,
если backend не гарантирует атомарность.

Оставшаяся работа — не gap, а задача: stage specifications готовятся в
UX-SPEC-001 (`flows/customer-cancel-reschedule-stages.md`); до их появления
SCR-CUST-012/013 имеют readiness PARTIAL с явной зависимостью от UX-SPEC-001.

## description (исходная формулировка)

CAP-011 Appointment Management включён в MVP в полном составе: «создание,
подтверждение, перенос, отмена записи» (SRC-01 §4.1 п. 3); intent types
RESCHEDULE_APPOINTMENT и CANCEL_APPOINTMENT входят в минимальный набор
(SRC-02 этап 4). При этом stage specifications для веток переноса/отмены
вынесены за пределы MVP-среза как proposal (SRC-02 Non-goals п. 5), и вопрос
их включения открыт (SRC-02 OQ5). Существующая спека SRC-12
(customer-cancellation-reschedule-flow.md) покрывает оба flow, но является
материалом ревизии, не каноном, и содержит устаревшие основания (дата пилота,
billing chain Q12-α).

## why_it_matters

Пользовательские сценарии отмены/переноса неизбежны в пилоте; без
канонических stage specifications нельзя подтвердить actor/цель/entry/exit/
primary action для SCR-CUST-012/013 и сверить спеку SRC-12 на соответствие
канону (policy checks, authoritative state transitions, voice). Экраны
формально в W1 (capability included), но поведение не утверждено.

## blocked_screens

SCR-CUST-012, SCR-CUST-013; частично SCR-CUST-010, SCR-CUST-011 (действия
«Отменить»/«Перенести» на карточках записи)

## missing_decision

Решение OQ5: включаются ли stage specifications переноса/отмены в MVP-срез
(и в каком объёме — полные flow или минимальный путь через диалог).

## required_owner

Product Owner.

## recommended_artifact

Decision Record (OQ5) + Specification (stage specs для cancel/reschedule —
расширение SRC-02 или отдельный срез).

## can_use_temporary_assumption

Да.

## temporary_assumption

Считать cancel/reschedule входящими в W1 (CAP-011 включён, SRC-01 §4.1 п. 3)
и использовать SRC-12 customer-cancellation-reschedule-flow.md как рабочий
драфт поведения до утверждения stage specs, с пометкой stale-оснований.

## acceptance_criteria

- OQ5 закрыт решением Product Owner.
- Stage specifications cancel/reschedule утверждены (или зафиксирован
  минимальный путь); SRC-12 спека сверена с ними.

## update 2026-07-29

Owner-часть закрыта UX-OD-001; stage specifications доставлены:
`docs/ux/flows/customer-cancel-reschedule-stages.md` (UX-SPEC-001, draft).
Остаточные вопросы — OQ-1 (политика отмены, Product Owner), OQ-2/OQ-4
(Booking owner), OQ-3 (Platform). Gap закрыт для целей Design Wave 1A;
финальное закрытие — после утверждения stage specs.
