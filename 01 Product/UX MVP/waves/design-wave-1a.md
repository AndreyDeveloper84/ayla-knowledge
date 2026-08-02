---
artifact: design-wave-1a
version: "0.2"
status: draft
date: 2026-07-29
task_id: UX-WAVE-1A
basis:
  - UX-OD-001…005
  - screen-inventory-customer v0.2
  - flows/customer-cancel-reschedule-stages.md v0.4
  - AYLA-DEC-0022
  - AYLA-DEC-0036
node_id: ayla.ux.design-wave-1a
title: Design Wave 1A — Customer Surface (пакет для дизайнера)
type: specification
owner: UX Architecture
domain:
  - cross-domain
system_owner:
  - ayla-conversation
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
updated: 2026-08-02
review_cycle: monthly
---

# Design Wave 1A — Customer Surface (пакет для дизайнера)

## 1. Цель волны и поверхности

Пакет фиксирует scope дизайна первой волны MVP Ayla (пилот 2026-08-15,
Пенза): 17 экранов customer-поверхности, после которых дизайнер рисует
wireframes без изобретения бизнес-правил. Поверхности — **MAX bot DM**
(сообщения + inline-кнопки: диалог, рекомендация, быстрые действия,
pending/result) и **MAX Mini App** (webview: сложные действия — профиль,
детали записи, календарь, списки). Роли каналов — UX-OD-004
(hybrid_booking_surface); Mini App home Phase 1 = SCR-CUST-010 (UX-OD-005).

Critical path:

- **Booking:** SCR-CUST-001 → 003 → 004 → 006 → 007 → 008.
- **Управление записью:** SCR-CUST-010/011 → 012/013.
- **Вспомогательные:** SCR-CUST-005 (empty/no-recommendation), 014
  (транзакционные уведомления), 016 (safety boundary), 019 (terminal
  fallback).

## 2. Таблица волны

Readiness и состав — по inventory v0.2 (`02-screen-inventory-customer.md`);
здесь не переоткрывается. Сокращения источников правил: OD = UX-OD-xxx
(`decisions/ux-owner-decisions.md`); SS = stage specs
(`flows/customer-cancel-reschedule-stages.md`); RC = Recommendation UX
Addendum (`contracts/recommendation-ux-addendum.md`; доменная семантика —
CANON, SRC-16); PC = draft
Privacy/Consent Mapping (`contracts/draft-privacy-consent-mapping.md`);
UJS = SRC-02 (этап/N-ветка).

| screen_id | name | surface | readiness | Scope в волне | Ключевые состояния | Источник правил | Assumptions | Next action |
|---|---|---|---|---|---|---|---|---|
| SCR-CUST-001 | Welcome / Entry | bot DM | RWA | Проектируем: приветствие, категории, свободный ввод, notice-строка ПДн (PC §4, draft-текст N1). НЕ проектируем: анкета, consent-экран, wellness-навигация | default (категории + ввод) | UJS этап 1; OD-003, OD-005; PC §4–5 | Copy — до revalidation UX-OD-003; notice-текст N1 — draft (Privacy Owner) | Screen Contract → wireframe |
| SCR-CUST-003 | Intent & clarification dialog | bot DM | RWA | Уточнение, формулировка понимания, confidence-ветки; exit N1 → SCR-CUST-019. НЕ: memory-ветки W2 | clarification; low-confidence; N1 (не поняла) | Intent Model Spec v0.9.2 (approved); UJS этапы 4–5; OD-002 | Числовые пороги confidence — versioned runtime config; naming состояний — P1-04 | Screen Contract → wireframe |
| SCR-CUST-004 | Recommendation card + explanation + CTA (N9) | bot DM | PARTIAL | Проектируем: состав карточки, объяснение, CTA (RC §1–2), alternatives (≤2, после отказа), suppression N9. НЕ: TTL/expiry/invalidation-поведение (assumption), цена/длительность/слот (OQ-REC-4) | card shown; declined (мягкий/жёсткий); invalidated (специалист недоступен → alternative); «нет displayable объяснения → не показываем» → переход в 005 | RC §1–4; UJS этапы 7–9, N5, N9; OD-004 | RC — draft Level B (UX-GAP-0104): правило «no displayable explanation → no show» принято owner 2026-07-29 (редакция displayable); TTL — рабочая норма до owner approval | Screen Contract (по RC) → wireframe |
| SCR-CUST-005 | No-recommendation / empty states (N3, N5) | bot DM + Mini App | RWA | Контекстные empty states; различение `NO_CANDIDATES` / `PROVIDER_INELIGIBLE` / `SAFETY_BLOCKED`. НЕ: safety-копирайт в деталях (это 016) | empty (нет кандидатов); provider ineligible (post-show → честное сообщение + alternative); blocked (safety, без CTA на заблокированную услугу) | RC §5; UJS N3/N5; SRC-12 customer-catalog-empty-states-spec (P1-уровень) | RC Level B принят как рабочая норма гарантий empty/blocked до owner approval | Screen Contract → wireframe |
| SCR-CUST-006 | Slot picker (N4) | bot DM (compact) + Mini App (expanded) | RWA | Compact: слоты кнопками, quick selection; expanded: календарь, long lists. Deep link с контекстом + `recommendation_id`. НЕ: смена мастера в reschedule (W2) | slot list; empty `NO_AVAILABLE_SLOTS`; **stale_slot** (обязателен) | UJS этап 10, N4; OD-004; RC §5 | Displayed slot ≠ reservation, перепроверка при commit (факт UJS этап 10) | Screen Contract → wireframe |
| SCR-CUST-007 | Booking create result (N6, N7) | bot DM | RWA | Pending, failed, retry; возврат к выбору слота при актуальных данных. НЕ: success-состояние (это 008, только после confirmed) | loading/pending; failed (retry / try_later / return_to_slot_picker); повторная неудача → 019 | UJS этап 11, N6–N7; OD-002, OD-004 | Поведение при отклонении провайдером — proposal (UJS OQ3) | Screen Contract → wireframe |
| SCR-CUST-008 | Booking confirmation + напоминание | bot DM (+ detail в Mini App) | READY | Подтверждение только после authoritative `confirmed`; result notification bot DM, detail — Mini App; предложение напоминания (транзакционного). НЕ: варианты «подтверждено заранее» | success (confirmed); detail (Mini App) | UJS этап 12; OD-004; attribution `recommendation_id` (SRC-01 §4.1 п. 11) | — | Screen Contract → wireframe |
| SCR-CUST-009 | Registration / MAX OAuth gate | Mini App | PARTIAL | Проектируем: session-only identity gate (имя, контакт для записи), notice-строка (PC §4, draft-текст N2). НЕ: consent-копирайт и любые формулировки согласия — после Privacy Owner; модель `PERSONAL_DATA` из спеки SRC-12 не применять | identity form; notice (не consent); error валидации | OD-003; PC §2, §4–5; AYLA-DEC-0016 | Consent-модель не решена (UX-GAP-0101); anonymous mode — P1-03; тексты N2 — draft | Screen Contract (session-only часть) → wireframe формы |
| SCR-CUST-010 | Records list = Mini App home Phase 1 | Mini App | READY | Upcoming bookings, relevant booking states, history when available; entry для cancel/reschedule. НЕ: wellness dashboard, food/water, proactive | default (upcoming); empty (нет записей); history (when available) | OD-005; UJS этап 11 (статусы записи); SRC-12 customer-records-flow | Naming состояний UX State Contract — P1-04 | Screen Contract → wireframe |
| SCR-CUST-011 | Booking detail | Mini App | RWA | Детали активной/прошлой записи; entry points «Отменить»/«Перенести» → deep link в bot DM (C1/R1). НЕ: inline cancel/reschedule в Mini App | active detail; past detail | OD-001; SS (Entry points); SRC-12 customer-records-flow (R3) | Deep link Mini App → bot DM — proposal (SS OQ-3) | Screen Contract → wireframe |
| SCR-CUST-012 | Cancel booking flow | bot DM (+ Mini App entry) | RWA | C1 identify → C2 summary → C3 explicit confirmation → C4 pending → C5 result. НЕ: standalone full-screen flow (W2) | C1 empty / select; C2–C3 summary; C4 cancel_pending; C5 cancelled / cancel_failed; N-CR2 (timeout), N-CR3 (гонка, уже отменена) | OD-001, OD-002; SS §Cancel, §Таблица состояний, N-CR2/3 | Политика отмены (штрафы/дедлайны на C3) — не подтверждена каноном, только нейтральные формулировки (SS OQ-1); SS — draft | Screen Contract (по SS) → wireframe |
| SCR-CUST-013 | Reschedule booking flow | bot DM (+ Mini App слоты) | RWA | R1 identify → R2 new date/time selection → R3 explicit confirmation («было → станет») → R4 reschedule pending → R5 result (rescheduled / reschedule_failed). Same-ID, time-only перенос той же записи (AYLA-DEC-0022 п. 1, 2, 9); НЕ: смена мастера, расширенные альтернативы (W2); впечатление создания отдельной новой записи | R2 slots / slot unavailable (N-CR4); R3 confirm; R4 reschedule_pending; R5 rescheduled / reschedule_failed — UX-facing исход, не отдельный domain status (AYLA-DEC-0022 п. 1, 9) | OD-001, OD-002, OD-004; AYLA-DEC-0022, AYLA-DEC-0036; SS (`flows/customer-cancel-reschedule-stages.md`) §Reschedule, N-CR1/3/4 | SS — draft; retry на R4 — idempotent retry той же pending-операции, не создание отдельной записи (SS OQ-4, закрыт 2026-08-02) | Screen Contract (по SS) → wireframe |
| SCR-CUST-014 | Транзакционные уведомления и напоминания | bot DM | RWA | Только транзакционный контур записи (подтверждение, напоминание). НЕ: B7 (T-15min), B9 (care notes), любой proactive | notification (delivered); preference не запрашивается в Phase 1 | UJS этап 13; OD-003; SRC-12 customer-reminders-voice (B5/B6) | — | Screen Contract → wireframe |
| SCR-CUST-016 | Safety boundary message (N8) | bot DM | RWA | Остановка, минимальные вопросы о срочности, безопасный следующий шаг. НЕ: CTA на заблокированную услугу | boundary message; safe next step | UJS N8; Killer PRD OD-K6; RC §5 (`SAFETY_BLOCKED`) | Отдельной спеки нет — тексты требуют выделенной задачи | Screen Contract → wireframe |
| SCR-CUST-019 | Terminal fallback (N1, N7) | bot DM | RWA | Честное сообщение о неудаче + обязательные действия: retry, reformulate, return_to_previous_safe_step, try_later, exit; preserve_safe_session_context. НЕ: оператор, имитация поддержки, контакты мастера/салона, human handoff (P1-08) | terminal fallback | OD-002 | — | Screen Contract → wireframe |

**Не входят в волну:** SCR-CUST-002 (consent, W2/BLOCKED), SCR-CUST-015
(feedback, PARTIAL — CAP-006 и триггер не решены), SCR-CUST-017 (memory
controls, W2/BLOCKED), SCR-CUST-018 (profile hub, W2/PARTIAL), все
DEFERRED (inventory §«Экраны вне MVP»).

## 3. Обязательные ограничения для всех экранов волны

Из UX-OD-001…005 — нарушение любого пункта = дефект дизайна:

1. **No confirmed до authoritative backend confirmation** (OD-004, UJS
   этап 12): ни одно состояние не показывает «записано/подтверждено» до
   ответа booking SoR.
2. **Подтверждение намерения ≠ подтверждение записи** (OD-004): CTA в
   карточке/диалоге подтверждает намерение, не факт записи.
3. **Впечатление создания отдельной новой записи запрещено** (OD-001,
   AYLA-DEC-0022 п. 1; SS R3): перенос — одна same-ID операция над той же
   записью; на подтверждении показывается «было → станет» той же записи,
   не отмена и создание новой.
4. **Без оператора и автовыдачи контактов** (OD-002): ни один экран не
   обещает оператора, не имитирует живую поддержку, не выдаёт контакты
   мастера/салона автоматически.
5. **Persistent memory и proactive отключены** (OD-003): никаких
   формулировок «запомню», профилей предпочтений, проактивных предложений;
   session-only, service_necessity.
6. **`recommendation_id` сохраняется через весь flow** (OD-004): карточка →
   слот → booking → deep link в Mini App; booking без него — `unattributed`.
7. **Deep link не на generic home** (OD-004): при известном контексте —
   contextual deep link в релевантное состояние (услуга, специалист, даты,
   `recommendation_id`), home (SCR-CUST-010) может миноваться.
8. **Доменные статусы — только канонические:** Request ≠ Created ≠
   Confirmed (UJS этап 11) + `cancelled` / `cancel_failed` (OD-001).
9. **Stale slot обязателен** (OD-004): состояние «время только что заняли»
   в 006/013.
10. **Обязательные pending-состояния:** booking pending (007), cancel
    pending (012, C4/R3) — успех до ответа SoR запрещён.

## 4. Запрещённые предположения (do_not_assume)

- Не показывать success до backend confirmation — ни в booking, ни в
  cancel/reschedule.
- Не добавлять consent-экран в Phase 1 (OD-003); SCR-CUST-002 — W2.
- Не проектировать memory UI («Что Ayla знает», «Забыть это», отзыв
  scope) — W2/BLOCKED (SCR-CUST-017).
- Не проектировать смену мастера при переносе — W2 (OD-001); в initial
  booking альтернатива мастера допустима только как alternative (RC §5).
- Не выдумывать доменные статусы — только Request ≠ Created ≠ Confirmed +
  cancelled/cancel_failed; прочее — к Booking owner (SS OQ-2).
- Не копировать копирайт из stale-спек SRC-12 без проверки: даты «15 July»,
  Telegram, модель consent `PERSONAL_DATA`, «запомню предпочтения» —
  не канон (inventory §Соглашения; PC §1).
- Wellness/food/proactive — вне волны (OD-005 excluded; inventory DEFERRED).
- Не показывать цену/длительность/ближайший слот на карточке как
  обязательные поля до решения OQ-REC-4.
- Не применять политику штрафов/дедлайнов отмены из SRC-12 на C3 до
  подтверждения каноном (SS OQ-1).
- Не проектировать human handoff / operator chat — deferred (P1-08).

## 5. Открытые вопросы, не блокирующие старт

Каждый — рабочее допущение зафиксировано в таблице §2; дизайн стартует по
допущению, решение владельца может скорректировать экран.

| # | Вопрос | Владелец |
|---|---|---|
| OQ-REC-1 | ~~Финальный статус «нет объяснения → не показываем»~~ — **принято owner 2026-07-29 в редакции displayable** («no displayable explanation → no show») | Recommendation / AI Architecture |
| OQ-REC-2 | TTL/expiry/invalidation рекомендации (SCR-CUST-004) | Recommendation / AI Architecture |
| OQ-REC-3 | TTL suppression после мягкого отказа (N9) | Recommendation + Product Owner |
| OQ-REC-4 | Обязательность цены/длительности/слота на карточке | Product Owner + UX |
| OQ-REC-5 | Семантика событий `recommendation.*` | Architecture (Domain Event Registry) |
| OQ-REC-6 | Владелец классификации объяснений displayable vs internal-only (UX-исход при internal-only закрыт: → 005) | Safety/Trust Owner + Recommendation |
| OQ-REC-7 | Deep-link-контракт и TTL `recommendation_id` в Mini App | Platform + UX |
| SS OQ-1 | Политика отмены (штрафы/дедлайны) — формулировки C3 | Product Owner |
| SS OQ-3 | Механизм deep link Mini App → bot DM (entry 011 → 012/013) | Platform owner |
| ~~SS OQ-4~~ | ~~Retry создания по выбранному слоту (R6 failed-critical)~~ — закрыт 2026-08-02: failed-critical для Simple Reschedule не существует, retry на R4 — idempotent retry той же pending-операции (AYLA-DEC-0022 п. 10) | — |
| P1-04 | Naming UX-состояний (UX State Contract) — влияет 003/010 | UX + Product Owner |
| P1-03 | Anonymous mode для SCR-CUST-009 | Product Owner |
| Privacy Q1 | Baseline-слой 152-ФЗ `PERSONAL_DATA` vs service_necessity | Privacy Owner/юрист |
| Privacy Q2 | Достаточность notice без клика-согласия (Variant A) | Privacy Owner/юрист |
| Privacy Q3 | Approval scopes `intent_understanding`/`provider_selection` | Privacy Owner |

Итого: 15 открытых вопросов, все с владельцами и зафиксированными рабочими
допущениями.

## 6. Acceptance

1. Дизайнер может начать wireframe любого экрана таблицы §2, не задавая
   новых бизнес-вопросов: состав, состояния, ограничения и источник правил
   указаны.
2. Всё спорное помечено assumption со ссылкой на источник (RC/SS/PC/OQ) и
   отражено в §5 с владельцем.
3. Ни один экран волны не нарушает ограничения §3 и запреты §4 — это
   проверяется на review wireframes.

## Подволны (owner ruling 2026-07-29)

Итеративная стратегия: contracts → wireframes → ревью → следующий батч.
Не писать все 17 Screen Contracts подряд.

| Подволна | Экраны | Цель |
|---|---|---|
| 1A.1 Happy Path Booking | SCR-CUST-001, 003, 004, 006, 007, 008 | Первый кликабельный сквозной сценарий записи |
| 1A.2 Booking Management | SCR-CUST-010, 011, 012, 013 | Управление записью: карточка, отмена, перенос |
| 1A.3 Supporting | SCR-CUST-005, 014, 016, 019 | Empty/error states, уведомления, safety, fallback |
| 1A.4 Partial | SCR-CUST-004, 009 | Доработка PARTIAL-частей после Privacy/Recommendation owner reviews |

Трекинг: live-статусы ux/wireframe/ui/frontend — в `02-screen-inventory-customer.md`.

## Changelog

- 2026-08-02 — Wave 1 Simple Reschedule canon sync: строка SCR-CUST-013 и
  §3 п.3 переписаны с `cancel + create` (R1–R6, `failed-critical`) на
  same-ID модель R1–R5 (`reschedule_pending`, `rescheduled` — UX-facing
  исход, `reschedule_failed`) по AYLA-DEC-0022 и AYLA-DEC-0036; SS OQ-4
  отмечен закрытым (2026-08-02, `flows/customer-cancel-reschedule-stages.md`
  v0.4); basis дополнен ссылками на stages-документ и оба решения. Full
  Cancellation journey, replacement, смена мастера/услуги, re-offer —
  без изменений, остаются deferred.
- 2026-07-29 — UX-REFINE-001: строки SCR-CUST-004, OQ-REC-1 и OQ-REC-6
  приведены к редакции displayable explanation по owner ruling 2026-07-29
  (правило принято; OQ-REC-6 — владелец классификации displayable /
  internal-only).
