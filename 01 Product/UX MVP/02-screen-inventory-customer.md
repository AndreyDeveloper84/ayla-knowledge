---
artifact: screen-inventory-customer
version: "0.6"
status: draft
date: 2026-07-29
task_id: UX-CUST-001
sources:
  - SRC-01
  - SRC-02
  - SRC-06
  - SRC-12
node_id: ayla.ux.screen-inventory-customer
title: MVP Screen Inventory — Customer Surface
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

# MVP Screen Inventory — Customer Surface

Инвентаризация candidate screens customer-поверхности MVP Ayla (пилот
2026-08-15, Пенза; канал — MAX-бот + MAX Mini App, SRC-06 AYLA-DEC-0003/0004).
Документ не принимает продуктовых решений и не проектирует экраны; он фиксирует
состав, дедупликацию, MVP-волну и readiness.

## Changelog

### v0.6 (2026-08-02) — SCR-CUST-013 stale source removed

- **SCR-CUST-013 existing_spec:** удалён отсутствующий/устаревший источник
  `docs/screens/customer-cancellation-reschedule-flow.md` из нормативного
  списка; `flows/customer-cancel-reschedule-stages.md` остаётся
  единственным нормативным stage-source. Ссылка на прежний файл сохранена
  в notes как явно ненормативный historical note (без wikilink/navigation
  dependency). Readiness и остальные строки таблицы не изменены.

### v0.5 (2026-08-02) — Cancellation scope reconciliation

- **SCR-CUST-012** title/notes: явно помечено как minimal conversational
  cancel (C1–C5), не full Cancellation journey; добавлена ссылка на
  AYLA-DEC-0036 в key_dependencies. Устраняет неоднозначность между
  активной Phase 1 веткой и deferred-статусом полной cancellation journey
  (owner ruling 2026-07-28, вариант Б). Поведение/readiness не изменены.

### v0.4 (2026-08-02) — Owner ruling formally registered (AYLA-DEC-0036)

- **SCR-CUST-013 key_dependencies/notes:** добавлена ссылка на
  **AYLA-DEC-0036** (OD-RESCHED-1) — owner ruling для Wave 1 Simple
  Reschedule формально зарегистрирован в `OWNER_DECISION_REGISTER.md`.
  Семантика v0.3 (same-ID/time-only, AYLA-DEC-0022) не изменена.

### v0.3 (2026-08-02) — Wave 1 Simple Reschedule canon alignment

- **SCR-CUST-013 notes:** заменена механика `cancel_then_create_new_booking`
  на same-ID/time-only (Simple Reschedule, Wave 1 — UX-OD-001,
  синхронизировано с AYLA-DEC-0022 п. 1, п. 2, п. 9); добавлена
  зависимость AYLA-DEC-0022; OQ-4 из stage specs закрыт.
- Затронуто точечно: readiness и остальные строки таблицы не менялись.
  Синхронизировано с `decisions/ux-owner-decisions.md` (UX-OD-001 v0.2),
  `flows/customer-cancel-reschedule-stages.md` (v0.2), `gaps/UX-GAP-0105.md`,
  `context/current-session-brief.md`.

### v0.2 (2026-07-29) — UX-SYNC-001: применены owner decisions UX-OD-001…005

- Применены решения (`decisions/ux-owner-decisions.md`): UX-OD-001
  minimal_conversational_cancel_and_reschedule; UX-OD-002
  honest_self_service_terminal_fallback; UX-OD-003
  phase_1_session_only_service_necessity (accepted_as_temporary_assumption);
  UX-OD-004 hybrid_booking_surface; UX-OD-005
  records_list_as_phase_1_mini_app_home.
- Закрыты gaps: UX-GAP-0105 (owner part), UX-GAP-0106 (для MVP), UX-GAP-P1-01,
  UX-GAP-P1-02. UX-GAP-0103 закрыт как ошибка синхронизации: Ayla Intent Model
  Specification v0.9.2 существует и approved (ayla-knowledge, 2026-07-28).
- Readiness: SCR-CUST-003/006/007/019 → READY_WITH_ASSUMPTIONS;
  SCR-CUST-008/010 → READY; SCR-CUST-012/013 → PARTIAL (зависимость от
  UX-SPEC-001, `flows/customer-cancel-reschedule-stages.md`).
- Остаются открытыми: UX-GAP-0101 (release blocker; UX-OD-003 — temporary
  assumption, Privacy task UX-PRIV-001 запущена), UX-GAP-0102 (Phase 2, не
  блокирует Phase 1 при persistent memory disabled), UX-GAP-0104 (recon
  выполнен, UX-RECON-001 вариант B; UX-слой — `contracts/recommendation-ux-addendum.md`,
  доменная семантика — CANON, SRC-16).
- P1-registry: добавлен UX-GAP-P1-08 (human handoff, Later, Operations Runbook).

### v0.1 (2026-07-29) — UX-CUST-001: первичная инвентаризация

19 экранов, 6 P0 Gap Records, 7 P1 в реестре.

## Соглашения

- **surface:** `bot DM` — разговорная нить MAX-бота (сообщения + inline-кнопки);
  `Mini App` — webview в MAX. Роли каналов: бот — диалог, рекомендация, быстрые
  действия, feedback; Mini App — сложные действия (профиль, детали записи)
  (SRC-02 §Cross-channel Experience). Booking surface уточнена решением
  UX-OD-004 (hybrid_booking_surface).
- **mvp_wave:** `W1` — блокер пилота 2026-08-15 (Phase 1, session-only vertical
  slice, SRC-01 §3; подтверждено UX-OD-003); `W2` — следующая волна (Phase 2,
  opt-in persistent preferences, SRC-01 §3; CSR §10.2); `DEFERRED` — SRC-01 §5
  / SRC-02 Non-goals.
- **readiness:** READY / READY_WITH_ASSUMPTIONS / PARTIAL / BLOCKED / DEFERRED.
  READY = известны actor, цель, entry/exit, primary action, required data и нет
  нерешённых P0-зависимостей (consent, memory, safety, доменные статусы).
- **live status (ux / wireframe / ui / frontend):** Not Started / In Progress /
  Review / Approved / Done. Одна таблица = UX backlog + design backlog +
  frontend backlog. Обновляется оркестратором по факту handoff.
- **подволны Wave 1A:** 1A.1 Happy Path Booking (001, 003, 004, 006, 007, 008);
  1A.2 Booking Management (010–013); 1A.3 Supporting (005, 014, 016, 019);
  1A.4 Partial-доработка (004, 009). Батчи итеративные: contracts → wireframes
  → ревью → следующий батч.
- Даты «15 July» и Telegram-упоминания в спеках SRC-12 устарели: канон —
  2026-08-15 и MAX (SRC-06 AYLA-DEC-0003/0004). SRC-12 — материал ревизии,
  не канон (SRC-12 в 00-ux-source-index).

## Таблица экранов

| screen_id | name | surface | mvp_wave | readiness | existing_spec | key_dependencies | notes | ux | wireframe | ui | frontend |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SCR-CUST-001 | Welcome / Entry (приветствие, категории, свободный ввод) | bot DM | W1 | READY_WITH_ASSUMPTIONS | docs/screens/global-bot-welcome-consent-spec.md; docs/screens/customer-onboarding-flow.md | CAP-016; SRC-02 этап 1; UX-GAP-0101 (release-level); UX-OD-003, UX-OD-005 | Этап 1 определён фактами (SRC-02 этап 1). Copy-блок снят UX-OD-003 (2026-07-29, temporary assumption; revalidation before release); Mini App landing решён UX-OD-005. Обе спеки SRC-12 устарели по дате/модели consent; S3–S5 onboarding не подтверждены каноном — см. секцию «Вне MVP». | Review | Not Started | Not Started | Not Started |
| SCR-CUST-002 | Consent request (запрос согласия по scope) | bot DM | W2 | BLOCKED | — | CAP-002; UX-GAP-0101, UX-GAP-0102 | Phase 1 идёт по `service_necessity` без consent-экрана (SRC-02 этап 3; подтверждено UX-OD-003, который НЕ разблокирует этот экран). Явный запрос — только для persistence/проактивности (Phase 2). | Not Started | Not Started | Not Started | Not Started |
| SCR-CUST-003 | Intent & clarification dialog (уточнение, confidence, N1) | bot DM | W1 | READY_WITH_ASSUMPTIONS | — | CAP-003; Ayla Intent Model Specification v0.9.2 (approved); UX-GAP-P1-04 (naming) | UX-GAP-0103 закрыт как sync-ошибка: Intent Model Specification approved (2026-07-28), slot requirements и confidence bands известны; числовые пороги — versioned runtime config. Session-only части подтверждены UX-OD-003. Exit N1 — honest fallback (UX-OD-002). W2 memory-ветки — вне Phase 1 (UX-GAP-0102). | Review | Not Started | Not Started | Not Started |
| SCR-CUST-004 | Recommendation card + explanation + confirm CTA (N9) | bot DM | W1 | PARTIAL | — | CAP-004, CAP-005; UX-GAP-0104 (UX-REC-001 запущена); SRC-02 OQ4/OQ11 | Одна primary + до двух alternatives (SRC-02 этап 7). Объяснение обязательно (SRC-01 §4.1 п. 9). Fallback «без объяснения — не показываем» — принято owner 2026-07-29 в редакции displayable (OQ-REC-1). UX-слой — contracts/recommendation-ux-addendum.md (доменная семантика — CANON, SRC-16). `recommendation_id` сохраняется через весь booking flow (UX-OD-004). | Review | Not Started | Not Started | Not Started |
| SCR-CUST-005 | No-recommendation / контекстные empty states (N3, N5) | bot DM + Mini App | W1 | READY_WITH_ASSUMPTIONS | docs/screens/customer-catalog-empty-states-spec.md | CAP-004, CAP-008; UX-GAP-0104 (частично, fallback-варианты) | Тексты состояний зафиксированы founder в SRC-12; соответствуют SRC-02 N3 (честное no recommendation + обычный поиск). Спека P1-уровня, не противоречит канону. Assumption: draft Recommendation Contract Level B (UX-REC-001) принят как рабочая норма до owner approval — гарантии empty/blocked-состояний `NO_CANDIDATES`/`SAFETY_BLOCKED`. | Not Started | Not Started | Not Started | Not Started |
| SCR-CUST-006 | Slot picker (выбор слота, N4) | bot DM (compact) + Mini App (expanded) | W1 | READY_WITH_ASSUMPTIONS | docs/screens/customer-booking-flow.md (F3, stale) | CAP-010; AYLA-DEC-0021; UX-OD-004 | Поверхность назначена UX-OD-004 (hybrid_booking_surface): compact slot suggestions кнопками и quick selection — bot DM; expanded calendar и long slot lists — Mini App; contextual deep link (услуга, специалист, даты, recommendation_id); stale_slot state обязателен. Поведение этапа 10 определено (SRC-02 этап 10, N4). | Review | Not Started | Not Started | Not Started |
| SCR-CUST-007 | Booking create result (pending / failed / retry, N6, N7) | bot DM | W1 | READY_WITH_ASSUMPTIONS | docs/screens/customer-booking-flow.md (F4–F5, stale) | CAP-011, CAP-018; SRC-02 OQ3; UX-OD-002, UX-OD-004 | Booking Request ≠ Booking Created ≠ Confirmed (SRC-02 этап 11); pending state и result notification — bot DM (UX-OD-004). UX-GAP-0106 закрыт для MVP (UX-OD-002): при ошибке booking — возврат к выбору слота, если данные актуальны; retry/try_later. Поведение при отклонении провайдером — proposal (OQ3), рабочее допущение. | Review | Not Started | Not Started | Not Started |
| SCR-CUST-008 | Booking confirmation + предложение напоминания | bot DM (+ detail в Mini App) | W1 | READY | docs/screens/customer-booking-flow.md (F5, stale) | CAP-011, CAP-021; UX-OD-004 | Подтверждение только после authoritative `confirmed` (SRC-02 этап 12; UX-OD-004: подтверждение намерения ≠ подтверждение записи, no confirmed state до backend confirmation). Result notification — bot DM, detail — Mini App (UX-OD-004). Attribution `recommendation_id` (SRC-01 §4.1 п. 11). | Review | Not Started | Not Started | Not Started |
| SCR-CUST-009 | Registration / MAX OAuth gate при подтверждении записи | Mini App | W1 | PARTIAL | docs/screens/customer-booking-confirm-registration-spec.md | AYLA-DEC-0016 (identity); UX-GAP-0101; UX-GAP-P1-03 (anonymous mode) | Идентичность нужна для создания записи (backend SoR, SRC-01 §6). Session-only часть подтверждена UX-OD-003 (booking_execution по service_necessity). Модель consent в спеке (152-ФЗ PERSONAL_DATA) расходится с CSR scopes — см. UX-GAP-0101; anonymous mode — P1-03. | Not Started | Not Started | Not Started | Not Started |
| SCR-CUST-010 | Records list (ближайшие / история) — Mini App home Phase 1 | Mini App | W1 | READY | docs/screens/customer-records-flow.md | CAP-011; доменные статусы записи (Request ≠ Created ≠ Confirmed, SRC-02 этап 11); UX State Contract — UX-GAP-P1-04 (naming) | Подтверждён как home Mini App Phase 1 (UX-OD-005): upcoming bookings, relevant booking states, history when available; contextual navigation может миновать home. Entry point для cancel/reschedule (SRC-12). | Not Started | Not Started | Not Started | Not Started |
| SCR-CUST-011 | Booking detail (активная/прошлая запись) | Mini App | W1 | READY_WITH_ASSUMPTIONS | docs/screens/customer-records-flow.md (R3) | CAP-011; UX-OD-001; stage specs доставлены (flows/customer-cancel-reschedule-stages.md) | Та же спека; действия по записи определены UX-OD-001 и stage specs UX-SPEC-001 (entry points cancel/reschedule зафиксированы; deep link Mini App→bot DM — proposal, OQ-3). | Not Started | Not Started | Not Started | Not Started |
| SCR-CUST-012 | Minimal conversational cancel flow (identify, summary, confirmation, результат) — не full Cancellation journey | bot DM (+ Mini App при contextual deep link) | W1 | READY_WITH_ASSUMPTIONS | docs/screens/customer-cancellation-reschedule-flow.md (C1–C3); flows/customer-cancel-reschedule-stages.md | CAP-011; UX-OD-001; AYLA-DEC-0036 (OD-RESCHED-1); stage specs доставлены (UX-SPEC-001, draft) | UX-GAP-0105 закрыт (UX-OD-001): отмена через диалог bot DM (identify_booking → show_booking_summary → explicit_confirmation → authoritative_cancellation → result); обязательны cancel_pending и cancel_failed; no cancelled state до authoritative confirmation. Это minimal conversational cancel (C1–C5), не full Cancellation journey — policy/deadline/refund flow, standalone full-screen management, late-window/waitlist остаются deferred (owner ruling 2026-07-28, вариант Б; формализовано AYLA-DEC-0036). Assumptions: stage specs — draft (OQ-1 политика отмены, OQ-3 deep-link механизм — proposals). | Not Started | Not Started | Not Started | Not Started |
| SCR-CUST-013 | Reschedule booking flow (слоты, подтверждение; смена мастера — W2) | bot DM (+ Mini App для расширенного выбора слота) | W1 | READY_WITH_ASSUMPTIONS | flows/customer-cancel-reschedule-stages.md | CAP-011, CAP-010; UX-OD-001, UX-OD-004; AYLA-DEC-0022; AYLA-DEC-0036 (OD-RESCHED-1); stage specs доставлены (UX-SPEC-001, draft); SCR-CUST-006 | Simple Reschedule (Wave 1) = same-ID, time-only (UX-OD-001, канон — AYLA-DEC-0022 п. 1, п. 2, п. 9; owner ruling зарегистрирован как AYLA-DEC-0036): тот же appointment_id, версия монотонно увеличивается, событие appointment.rescheduled; cancel+create не используется. bot DM; Mini App — расширенный выбор слота (UX-OD-004). Assumptions: stage specs — draft (OQ-3 — proposal; OQ-4 закрыт 2026-08-02). Historical, non-normative: docs/screens/customer-cancellation-reschedule-flow.md (R1–R4) ранее использовался как источник reschedule-механики; заменён same-ID моделью (AYLA-DEC-0022/AYLA-DEC-0036), нормативным источником не является. | Not Started | Not Started | Not Started | Not Started |
| SCR-CUST-014 | Транзакционные уведомления и напоминания по записи | bot DM | W1 | READY_WITH_ASSUMPTIONS | docs/screens/customer-reminders-voice.md (B5/B6) | CAP-021 | Только транзакционный контур записи; проактивность вне MVP (SRC-02 этап 13; SRC-01 §8 Privacy; UX-OD-003). B7 (T-15min), B9 (care notes) — DEFERRED. | Not Started | Not Started | Not Started | Not Started |
| SCR-CUST-015 | Outcome / feedback prompt (после визита) | bot DM | W1 | PARTIAL | docs/screens/customer-reminders-voice.md (B11, частично) | CAP-006; UX-GAP-P1-05 (OQ6, OQ8) | Этап 14 определён, но статус CAP-006 в MVP не решён (SRC-02 OQ6) и доменный триггер `appointment.completed` pending Domain Event Registry (OQ8). | Not Started | Not Started | Not Started | Not Started |
| SCR-CUST-016 | Safety boundary message (N8) | bot DM | W1 | READY_WITH_ASSUMPTIONS | — | CAP-014; Killer PRD OD-K6 (по SRC-02 N8) | Поведение определено: остановка, минимальные вопросы о срочности, безопасный следующий шаг, без CTA на заблокированную услугу (SRC-02 N8). Отдельной спеки нет — требуется в следующей задаче. | Not Started | Not Started | Not Started | Not Started |
| SCR-CUST-017 | Memory & privacy controls («Что Ayla знает», отзыв scope, «Забыть это», удаление факта) | bot DM (команды) + Mini App | W2 | BLOCKED | docs/screens/customer-profile-flow.md (R2/R3 — в самой спеке DEFERRED) | CAP-001, CAP-002; UX-GAP-0101, UX-GAP-0102 | Команды — факты CSR §8 (по SRC-02 Memory Interaction), но опираются на persistent memory Phase 2 (disabled в Phase 1, UX-OD-003 — экран не разблокирован) и незакрытые gates (SRC-01 §10.1). | Not Started | Not Started | Not Started | Not Started |
| SCR-CUST-018 | Profile hub (раздел «Я»: header, уведомления, приватность) | Mini App | W2 | PARTIAL | docs/screens/customer-profile-flow.md (R1/R5/R6) | CAP-002, CAP-021 | R2/R3 выделены в SCR-CUST-017; R4 proactive toggle — DEFERRED (проактивность вне MVP, SRC-02 §Recommendation and Proactivity Gates). | Not Started | Not Started | Not Started | Not Started |
| SCR-CUST-019 | Terminal fallback state (N1, N7 — повторная неудача) | bot DM | W1 | READY_WITH_ASSUMPTIONS | — | UX-OD-002 | UX-GAP-0106 закрыт для MVP решением UX-OD-002 honest_self_service_terminal_fallback: честное сообщение о неудаче; без обещания оператора, без имитации живой поддержки, без автоматической выдачи контактов мастера/салона. Обязательные действия: retry, reformulate, return_to_previous_safe_step, try_later, exit; preserve_safe_session_context. Полноценный human handoff — UX-GAP-P1-08 (Later, Operations Runbook). | Not Started | Not Started | Not Started | Not Started |

## Экраны вне MVP (DEFERRED)

Из существующих спек SRC-12 в MVP-волны не входит:

- **customer-food-scanner-flow.md** → DEFERRED. Доменный journey Nutrition
  Guidance — вне MVP-среза (SRC-02 Non-goals); Included Capabilities
  (SRC-01 §4.1) не содержат nutrition/food-scanning; cross-domain
  food→beauty-сценарии заблокированы (SRC-02 Non-goals, CSR §11.2 по SRC-02).
  Спека датирована моделью «wellness MVP» до freeze scope.
- **customer-food-scanner-backdate-postpilot.md** → DEFERRED (в самой спеке —
  post-pilot; родительский flow и так вне MVP).
- **customer-main-wellness-dashboard.md** → DEFERRED как wellness-хаб
  (питание/вода/цели — вне SRC-01 §4.1). Quick action «Найди услугу» живёт в
  SCR-CUST-001/005; Mini App landing для MVP определён решением UX-OD-005
  (home = SCR-CUST-010).
- **customer-onboarding-flow.md S3–S5** (позиционирование «кто такая Ayla»,
  health screening, first-action grid: еда/вода/цель/каталог) → DEFERRED в
  части wellness-навигации; канонический entry — SRC-02 этап 1 без анкеты
  (запрет анкеты при первом контакте — SRC-02 этап 1 ограничения).
- **customer-profile-flow.md R4** (proactive toggle) → DEFERRED — проактивные
  рекомендации вне MVP (SRC-02 §Recommendation and Proactivity Gates;
  scope `proactive_recommendation` blocked).
- **customer-profile-flow.md R2 delete/export** → DEFERRED (в самой спеке —
  post-pilot ADR-0015 epic; согласуется с отсутствием export/forget в MVP).
- **customer-reminders-voice.md B7, B9** → DEFERRED (backend follow-ups,
  не транзакционный минимум записи).
- **Клиентская онлайн-оплата** → DEFERRED (SRC-01 §5/§5.1). Примечание:
  AYLA-DEC-0006 допускал опциональную клиентскую оплату, но более поздний
  контур (AYLA-DEC-0015, SRC-01 §5.1) исключает её из MVP — расхождение
  зафиксировано в UX-GAP-P1-07, экранов оплаты в инвентаре нет.
- **Telegram-варианты всех спек** → DEFERRED (SRC-06 AYLA-DEC-0004).

## Покрытие journey (SRC-02 → screen_id)

| Этап / сценарий SRC-02 | screen_id | Комментарий |
|---|---|---|
| Этап 1 Entry | SCR-CUST-001 | Mini App-вариант entry приземляется на SCR-CUST-010 (UX-OD-005). |
| Этап 2 First interaction | SCR-CUST-001, SCR-CUST-003 | Первый содержательный ответ — в диалоге; отдельного экрана нет. |
| Этап 3 Consent request | SCR-CUST-002 (W2) | Phase 1 — без экрана (`service_necessity`, SRC-02 этап 3; подтверждено UX-OD-003). |
| Этап 4 Intent detection | SCR-CUST-003 | Не экран per se; пользовательская видимость — формулировка понимания. Контракт — Intent Model Specification v0.9.2 (UX-GAP-0103 закрыт). |
| Этап 5 Clarification | SCR-CUST-003 | — |
| Этап 6 Context retrieval | — (не экран) | Результат виден в объяснении SCR-CUST-004 (SRC-02 этап 6). |
| Этап 7 Recommendation | SCR-CUST-004; SCR-CUST-005 при `NO_CANDIDATES` | — |
| Этап 8 Explanation | SCR-CUST-004 | — |
| Этап 9 User confirmation | SCR-CUST-004 (CTA); SCR-CUST-009 (identity gate) | Подтверждение намерения ≠ подтверждение записи (UX-OD-004). |
| Этап 10 Availability selection | SCR-CUST-006 | Поверхность — UX-OD-004 (hybrid). |
| Этап 11 Booking creation | SCR-CUST-007 | — |
| Этап 12 Booking confirmation | SCR-CUST-008 (+ SCR-CUST-011) | — |
| Этап 13 Notification | SCR-CUST-014 | — |
| Этап 14 Outcome / feedback | SCR-CUST-015 | — |
| N1 Ayla не поняла | SCR-CUST-003 → SCR-CUST-019 | Fallback определён (UX-OD-002): honest terminal fallback; handoff deferred (P1-08). |
| N2 Нет consent | SCR-CUST-002 | W2; Phase 1 не возникает для session-операций. |
| N3 Нет подходящей услуги | SCR-CUST-005 | — |
| N4 Нет свободных слотов | SCR-CUST-006 | — |
| N5 Специалист недоступен | SCR-CUST-005, SCR-CUST-004 | Исключение до показа primary — системное; пользовательское состояние — alternative. |
| N6 Запись не подтверждена | SCR-CUST-007 | — |
| N7 Tool/LLM недоступен | SCR-CUST-007 → SCR-CUST-019 | Fallback определён (UX-OD-002): возврат к выбору слота при актуальных данных; handoff deferred (P1-08). |
| N8 Safety-блокировка | SCR-CUST-016 | — |
| N9 Отказ от предложения | SCR-CUST-004 | Suppression после жёсткого отказа — системное правило (SRC-02 N9). |
| Memory Interaction (loop, controls) | SCR-CUST-017 (W2); memory proposal prompt — в диалоге SCR-CUST-002/004 (W2) | Phase 2; persistent memory disabled в Phase 1 (UX-OD-003). |
| Product Thesis Validation Scenario | SCR-CUST-017 + повторный проход SCR-CUST-003/004 (W2) | Не release gate Phase 1 (SRC-06 AYLA-DEC-0018). |

**Непокрытые этапы:** этап 6 — системный (экран не требуется). Mini App
landing/home (точка входа deep link этапа 1 в Mini App) определён решением
UX-OD-005: home = SCR-CUST-010; contextual navigation (UX-OD-004) может
миновать home (slot picker, booking detail, cancel/reschedule context).

## Gap Records

P0 — отдельные файлы в `docs/ux/gaps/`:

- UX-GAP-0101 [OPEN, release blocker] — consent-модель: scopes Phase 1 не
  approved; модель SRC-12 ≠ CSR. Temporary assumption принята (UX-OD-003);
  Privacy task UX-PRIV-001 запущена.
- UX-GAP-0102 [OPEN] — Phase 2 activation gates не закрыты; не блокирует
  Phase 1 при persistent memory disabled (UX-OD-003).
- UX-GAP-0103 [CLOSED 2026-07-29] — ошибка синхронизации: Ayla Intent Model
  Specification v0.9.2 существует и approved (ayla-knowledge, 2026-07-28).
- UX-GAP-0104 [OPEN] — MVP Recommendation Contract отсутствует (вкл. OQ4,
  OQ11); recon выполнен (UX-RECON-001, вариант B), UX draft →
  `contracts/recommendation-ux-addendum.md`; open до решений Recommendation
  Owner (OQ-REC-2/4/6/7) и переноса displayable-правила в CANON §13.
- UX-GAP-0105 [CLOSED 2026-07-29, owner part] — UX-OD-001; stage specs —
  UX-SPEC-001 (`flows/customer-cancel-reschedule-stages.md`).
- UX-GAP-0106 [CLOSED 2026-07-29, для MVP] — UX-OD-002; будущий human
  handoff — UX-GAP-P1-08 (Later, Operations Runbook).

P1 — реестр `docs/ux/gaps/UX-GAP-P1-registry.md` (P1-01…P1-08; P1-01 и P1-02
closed 2026-07-29 решениями UX-OD-005 / UX-OD-004).
