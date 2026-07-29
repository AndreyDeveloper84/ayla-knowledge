---
node_id: ayla.ux.scr-cust-006
screen_id: SCR-CUST-006
title: SCR-CUST-006 — Slot picker (выбор слота, N4)
name: Slot picker (выбор слота, N4)
type: specification
version: "0.2"
status: draft
task_id: UX-CUST-002b
owner: UX Architecture
knowledge_area:
  - product
domain:
  - booking
system_owner:
  - ayla-booking
  - ayla-mini-app
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
wave: 1A.1 Happy Path Booking
date: 2026-07-29
sources: [UJS этап 10, N4; UX-OD-004; recommendation-ux-addendum (UXA §5); CANON Ayla MVP Recommendation Contract v0.3 (SRC-16: §10, §22); AYLA-DEC-0021; SS R4/N-CR1; SRC-12 customer-booking-flow F3 (компоненты)]
---

# SCR-CUST-006 — Slot picker

| Поле | Значение |
|---|---|
| screen_id | SCR-CUST-006 |
| name | Slot picker (выбор слота, N4) |
| actor | Customer ↔ Ayla ↔ Backend (SoR availability) |
| surface | bot DM (compact) + Mini App (expanded) — UX-OD-004 |
| mvp_flow | W1, подволна 1A.1; UJS этап 10, вход из SCR-CUST-004 (accept) |
| purpose | Дать выбрать удобное время записи по принятой рекомендации |
| user_goal | Найти подходящий слот и перейти к созданию записи |
| primary_action | Выбрать слот (кнопка в bot DM / тап в Mini App) |
| secondary_actions | «Показать другие варианты» → contextual deep link в Mini App; запросить другое время (N4); запросить другого мастера (только initial booking, UXA §5); выход из flow |

## required_data

- `recommendation_id` (неизменным из SCR-CUST-004; сохраняется в deep link и далее в booking creation — UX-OD-004, UXA §4; идентичность — CANON §3–4).
- Услуга, специалист/салон (из карточки рекомендации).
- Актуальные слоты от Backend (CAP-010; displayed slot ≠ reservation, перепроверка при commit — факт UJS этап 10; CANON §22 revalidation).
- Conversation context ref для deep link (assumption — состав не формализован, OQ-REC-7).

## key_components

- **bot DM compact:** сообщение с несколькими ближайшими слотами inline-кнопками (quick selection) + «Показать другие варианты» → deep link в Mini App slot picker с контекстом (услуга, специалист, даты, `recommendation_id`).
- **Mini App expanded:** календарь / длинный список слотов по дням.
- **Hold-индикатор после выбора:** «Слот временно закреплён за вами до HH:MM» (серверный `expires_at`, TTL 15 мин, AYLA-DEC-0021); внутренние термины (hold, ledger) не показываются.
- Reuse из stale-спеки F3 (только компоненты): day-grouped slot grid, «закрыто — выходной», карточка замещающего мастера. НЕ переносятся: smart suggestions на behavioral-паттернах и state-dependent headers (persistent memory off, UX-OD-003).

## states

| state | Что видит пользователь | Доступные действия |
|---|---|---|
| loading | Скелетон списка/календаря | Выход |
| slot_list (default) | Compact: слоты кнопками + «Показать другие варианты». Mini App: календарь/список по дням | Выбрать слот; открыть Mini App; запросить другое время/мастера; выход |
| empty / no_available_slots (N4) | Честное «свободного времени нет» на запрошенные условия | Другое время; другой мастер (initial booking, alternative с собственным `recommendation_id`); выход |
| stale_slot (обязателен, UX-OD-004) | «Это время только что заняли» + актуализированные слоты (терминология согласована с SS N-CR1) | Выбрать другой слот; выход |
| error (слоты не загрузились) | Честное сообщение о сбое загрузки | retry; try_later; выход (UX-OD-002) |
| offline (Mini App) | Webview без сети: сообщение + кнопка обновления | retry; возврат в bot DM |

## dependencies

- CAP-010 (Availability Management), CAP-004 (вход из рекомендации).
- UX-OD-004 (hybrid surface, stale_slot обязателен); recommendation-ux-addendum §5 + CANON §10/§22 (UX-facing constraints, рабочая норма до owner decisions).
- AYLA-DEC-0021 (slot hold, TTL, confirm chain).
- Выход: SCR-CUST-007 (booking pending); смена мастера в reschedule — W2 (UX-OD-001).

## assumptions

1. Число слотов в compact-выдаче bot DM («несколько ближайших») источниками не нормировано — рабочее допущение 3–5, решение за Product Owner + UX.
2. Состав и TTL контекста deep link (гарантии доставки `recommendation_id` в Mini App) — OQ-REC-7, рабочее допущение: передаём полный набор полей UX-OD-004.
3. Hold-индикатор — только после фактического создания hold (AYLA-DEC-0021); истечение hold до commit — в SCR-CUST-007.
4. Гарантия `NO_AVAILABLE_SLOTS` — UXA §5 (рабочая норма до owner decisions, UX-GAP-0104). **Финальная сверка экрана с CANON и addendum — после ответов Recommendation Owner (OQ-REC-2/4/6/7).**

## blockers

Нет (readiness READY_WITH_ASSUMPTIONS).

## design_notes

- Никаких формулировок «слот забронирован» до commit — displayed slot ≠ reservation.
- Deep link — НЕ на generic home (UX-OD-004): всегда contextual; цена/длительность/слот на карточке — не обязательные поля до OQ-REC-4.
- Session-only: никакой персонализации выдачи слотов на persistent memory (UX-OD-003).

## changelog

- 2026-07-29 — UX-MERGE-001: ссылки RC (draft) → recommendation-ux-addendum
  (UXA) + CANON (SRC-16): sources, required_data (UXA §4), secondary_actions
  и dependencies (UXA §5; revalidation — CANON §22; alternatives — CANON §10);
  assumption 4 — финальная сверка после ответов Recommendation Owner
  (OQ-REC-2/4/6/7).
