---
screen_id: SCR-CUST-007
name: Booking create result (pending / failed / retry, N6, N7)
task_id: UX-CUST-002b
wave: 1A.1 Happy Path Booking
status: draft
date: 2026-07-29
sources: [UJS этап 11, N6, N7, OQ3; UX-OD-002, UX-OD-004; SS R5/N-CR1; SRC-12 customer-booking-flow F4 (компоненты)]
node_id: ayla.ux.scr-cust-007
title: SCR-CUST-007 — Booking create result
type: specification
owner: UX Architecture
version: "0.1"
domain:
  - booking
system_owner:
  - ayla-booking
  - ayla-mini-app
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

# SCR-CUST-007 — Booking create result

| Поле | Значение |
|---|---|
| screen_id | SCR-CUST-007 |
| name | Booking create result (N6, N7) |
| actor | Ayla → Backend; результат — пользователю в bot DM |
| surface | bot DM (pending state и result notification — UX-OD-004) |
| mvp_flow | W1, подволна 1A.1; UJS этап 11, вход из SCR-CUST-006 (slot selected) |
| purpose | Честно отразить фактическое состояние создания записи и дать recovery path |
| user_goal | Чтобы запись была создана ровно одна и на выбранных условиях |
| primary_action | Ожидание результата (pending); при failed — выбрать recovery-действие |
| secondary_actions | retry; return_to_slot_selection (если данные актуальны); try_later; exit |

## required_data

- Выбранный слот + контекст записи (услуга, специалист, `recommendation_id` — сохраняется, UX-OD-004).
- Фактический ответ booking SoR: created / conflict / not_confirmed / timeout / hold expired.
- Признак актуальности данных slot picker (для решения о возврате, UX-OD-002).

## key_components

- **Pending-сообщение** в bot DM: «записываю…», hold-индикатор из SCR-CUST-006 остаётся до результата (UJS этап 11). Успех в этом состоянии запрещён.
- **Failed-сообщение** с честным описанием причины без внутренних терминов (`SLOT_TAKEN` → «это время только что заняли»; hold expired → «время брони истекло»).
- **Набор recovery-кнопок** UX-OD-002: retry / return_to_slot_selection / try_later / exit.
- Reuse из stale F4 (только компоненты): commit-loading индикатор, паттерн «время только что заняли». НЕ переносятся: loyalty-блок, штрафы, registration gate, заметка мастеру.

## states

| state | Что видит пользователь | Доступные действия |
|---|---|---|
| booking_pending | «Записываю…» + hold-индикатор; без кнопок успеха | Дождаться результата; exit (без отмены серверной операции — assumption 3) |
| booking_failed (N6: `APPOINTMENT_CONFLICT`, `APPOINTMENT_NOT_CONFIRMED`; N7: `TOOL_TIMEOUT`, `MODEL_UNAVAILABLE`) | Честное описание неудачи; запись НЕ подтверждена | retry; return_to_slot_selection; try_later; exit |
| stale_slot (`SLOT_TAKEN`/conflict при commit) | «Это время только что заняли» | Переход к SCR-CUST-006 с актуальными слотами (паттерн SS N-CR1); exit |
| hold_expired | «Время удержания слота истекло»; подтверждение отключено | Повторная проверка доступности → SCR-CUST-006 (факт — AYLA-DEC-0021); exit |
| повторная неудача | Честное терминальное сообщение | Действия UX-OD-002; переход в SCR-CUST-019 |

**На этом экране НЕТ success-состояния:** confirmed показывается только в
SCR-CUST-008 после authoritative backend confirmation (UX-OD-004).

## dependencies

- CAP-011 (Appointment Management), CAP-018 (tool/LLM fallback, N7).
- UX-OD-002 (honest fallback, без оператора и контактов); UX-OD-004 (Request ≠ Created ≠ Confirmed; pending — bot DM).
- AYLA-DEC-0021 (hold confirm chain, TTL, `SLOT_TAKEN`).
- Идемпотентность tool calls при retry (факт — Roadmap §6.3, по UJS N7): дублирование записи недопустимо.

## assumptions

1. Отклонение провайдером (`APPOINTMENT_NOT_CONFIRMED`): альтернативный слот/мастер — proposal (UJS OQ3); рабочее допущение — failed state + стандартные recovery-действия UX-OD-002.
2. UI-таймаут pending не нормирован — допущение: управляется backend `TOOL_TIMEOUT`, UX не вводит свой таймер.
3. Exit из pending не отменяет серверную операцию; исход доезжает result-уведомлением.
4. Retry не дублирует side effects (идемпотентность — факт, Roadmap §6.3); повторная неудача → SCR-CUST-019.

## blockers

Нет (readiness READY_WITH_ASSUMPTIONS). UX-GAP-0106 закрыт для MVP решением UX-OD-002.

## design_notes

- no_false_success: ни одно состояние не намекает на успех до ответа SoR.
- Без обещания оператора, без имитации поддержки, без автовыдачи контактов мастера/салона (UX-OD-002; N7-формулировка UJS «дать контакты мастера» в MVP не применяется — перекрыта UX-OD-002).
- preserve_safe_session_context: при любом исходе контекст записи и `recommendation_id` не теряются.
- Подтверждение намерения (кнопка слота на 006) ≠ подтверждение записи — копирайт pending это не размывает.
