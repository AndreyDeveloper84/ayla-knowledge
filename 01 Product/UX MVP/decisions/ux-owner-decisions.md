---
artifact: ux-owner-decisions
version: "0.4"
status: approved
date: 2026-07-29
task_id: UX-SYNC-001
sources:
  - reviews/owner-review-001.md
node_id: ayla.ux.owner-decisions
title: UX Owner Decisions — Customer Surface (2026-07-29)
type: specification
owner: UX Architecture
domain:
  - cross-domain
system_owner:
  - ayla-knowledge
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

# UX Owner Decisions — Customer Surface (2026-07-29)

Пять решений Product Owner по Owner Review Package 001
(`reviews/owner-review-001.md`, вопросы D1–D5). Применены к рабочим
UX-документам в UX-SYNC-001.

> **Пометка:** формальная регистрация этих решений в Ayla Decision Log
> (ayla-knowledge, review-gate) — отдельный процесс и в рамках UX-SYNC-001
> **не выполняется**.

> **Обновлено 2026-08-02 (Wave 1 Simple Reschedule canon alignment):**
> `reschedule_flow` в UX-OD-001 приведён в соответствие с AYLA-DEC-0022
> (accepted, 2026-07-28) — same-ID/time-only модель вместо
> `cancel_then_create_new_booking`. Остальные четыре решения (UX-OD-002…005)
> не затронуты. Owner ruling формально зарегистрирован как **AYLA-DEC-0036**
> (OD-RESCHED-1, `OWNER_DECISION_REGISTER.md`). См. Change Log в конце
> документа.

## UX-OD-001 — minimal_conversational_cancel_and_reschedule

```yaml
decision_id: UX-OD-001
title: minimal_conversational_cancel_and_reschedule
status: accepted
date: 2026-07-29
updated: 2026-08-02
owner: Product Owner
resolves: [UX-GAP-0105 (owner part), SRC-02 OQ5]
affected_screens: [SCR-CUST-012, SCR-CUST-013, SCR-CUST-010, SCR-CUST-011]
decision:
  cancel_flow: >-
    Отмена записи — через диалог в bot DM: identify_booking →
    show_booking_summary → explicit_confirmation →
    authoritative_cancellation → result.
  reschedule_flow: >-
    Simple Reschedule (Wave 1) — same-ID, time-only перенос: сохраняется
    appointment_id, меняются только дата/время в пределах того же Offering
    (тот же специалист, та же услуга, неизменные цена/длительность), версия
    записи монотонно увеличивается, публикуется событие
    appointment.rescheduled (канон — AYLA-DEC-0022 п. 1, п. 2, п. 9; Domain
    Event Registry §6.3, registered, v0.4). Механика
    cancel_then_create_new_booking для этого сценария не используется (owner
    ruling AYLA-DEC-0036 / OD-RESCHED-1, 2026-08-02). Bot DM — компактный выбор нового времени; Mini
    App — когда нужен расширенный выбор слота (UX-OD-004). Owner ruling
    зарегистрирован как AYLA-DEC-0036 (OD-RESCHED-1).
  deferred_to_W2:
    - смена мастера при переносе
    - смена услуги / Offering при переносе
    - replacement и re-offer как полноценные ветки
    - расширенные альтернативы
    - standalone full-screen cancel/reschedule flows
  deferred_scope_note: >-
    Перечисленное выше — сужение UX-поверхности Wave 1, а не следствие
    доменной механики: AYLA-DEC-0022 п. 2 технически допускает смену
    специалиста в пределах того же Offering как same-ID (с явным согласием
    клиента), но Wave 1 UX эту ветку не открывает. cancel_flow выше —
    minimal conversational cancel (identify → summary → confirmation →
    cancellation → result), не full Cancellation journey: policy/deadline/
    refund flow (OQ-1), standalone full-screen cancellation management,
    late-window/waitlist-ветки и провайдер-уведомления (OQ-5) в cancel_flow
    не входят. Полная cancellation journey отдельно и явно остаётся
    deferred (owner ruling 2026-07-28, вариант Б; формально зафиксировано
    как AYLA-DEC-0036 / OD-RESCHED-1, 2026-08-02, без расширения или
    сужения этого deferral). Backend cancel capability (CAP-011) может
    существовать шире cancel_flow — это не переводит полную UX
    cancellation journey в Wave 1.
constraints:
  - no cancelled state до authoritative confirmation (cancel flow)
  - обязательны состояния cancel_pending и cancel_failed (cancel flow)
  - reschedule — одна authoritative-транзакция над той же записью; итоговые
    состояния — rescheduled / reschedule_failed; промежуточного cancelled у
    исходной записи не возникает; при любом отказе исходная запись и её
    reservation остаются без изменений (AYLA-DEC-0022 п. 10)
  - terminal-state запись (cancelled/completed) не может быть перенесена
    (AYLA-DEC-0022 п. 1)
traceability:
  - AYLA-DEC-0022 — Appointment Reschedule and Replacement Model (accepted,
    2026-07-28), п. 1, п. 2, п. 9, п. 10
  - AYLA-DEC-0036 (OD-RESCHED-1) — Wave 1 Simple Reschedule owner ruling
    (registered 2026-08-02, `OWNER_DECISION_REGISTER.md`); формализует
    запрет cancel_then_create_new_booking и deferred-scope для Wave 1
  - appointment.rescheduled — Domain Event Registry, registration_status
    registered (v0.4)
follow_up: >-
  Stage specs синхронизированы в UX-SPEC-001
  (flows/customer-cancel-reschedule-stages.md) с AYLA-DEC-0022, 2026-08-02.
```

## UX-OD-002 — honest_self_service_terminal_fallback

```yaml
decision_id: UX-OD-002
title: honest_self_service_terminal_fallback
status: accepted
date: 2026-07-29
owner: Product Owner
resolves: [UX-GAP-0106 (для MVP), SRC-02 OQ2]
affected_screens: [SCR-CUST-019, SCR-CUST-003 (N1), SCR-CUST-007 (N7)]
decision:
  mvp: >-
    Human handoff в MVP НЕ требуется, operator chat — deferred. При повторной
    неудаче (N1/N7) Ayla прямо сообщает о неудаче, не обещает оператора, не
    имитирует живую поддержку, НЕ выдаёт контакты мастера/салона
    автоматически.
  required_user_actions: [retry, reformulate, return_to_previous_safe_step, try_later, exit]
  booking_error: >-
    При ошибке booking — возможность вернуться к выбору слота, если данные
    актуальны.
constraints:
  - no_false_success
  - no_fake_operator_availability
  - no_automatic_provider_contact_disclosure
  - preserve_safe_session_context
follow_up: >-
  Будущий human handoff — P1/Later (Operations Runbook), см.
  gaps/UX-GAP-P1-registry.md → UX-GAP-P1-08.
```

## UX-OD-003 — phase_1_session_only_service_necessity

```yaml
decision_id: UX-OD-003
title: phase_1_session_only_service_necessity
status: accepted_as_temporary_assumption
date: 2026-07-29
owner: Product Owner
resolves: [temporary assumption по UX-GAP-0101]
affected_screens: [SCR-CUST-001, SCR-CUST-003, SCR-CUST-009]
explicitly_not_affected: [SCR-CUST-002, SCR-CUST-017, UX-GAP-0102]
decision:
  phase_1: >-
    Phase 1 = session-only + service_necessity; persistent memory disabled;
    явный экран consent на preference_memory в W1 не создаётся.
  allowed_scopes_session_only:
    - intent_understanding
    - provider_selection
    - booking_execution
    - transactional_booking_support
  forbidden_until_privacy_owner_decision:
    - persistent prefs, Memory Facts
    - трактовка продолжения диалога как согласия
    - скрытое профилирование
    - маркетинг
    - проактивные рекомендации
    - secondary use
    - health inference
    - перенос session data в persistent storage
constraints:
  - >-
    Обязательная параллельная задача Privacy Owner: MVP Personal Data and
    Consent Mapping (уже запущена как UX-PRIV-001).
  - Решение НЕ заменяет заключение Privacy Owner/юриста.
  - revalidation required before release.
effects:
  - снимает copy-блок с SCR-CUST-001 и session-only частей SCR-CUST-003/009
  - НЕ разблокирует SCR-CUST-002/017
  - НЕ закрывает UX-GAP-0102 (Phase 2)
```

## UX-OD-004 — hybrid_booking_surface

```yaml
decision_id: UX-OD-004
title: hybrid_booking_surface
status: accepted
date: 2026-07-29
owner: Product Owner
resolves: [UX-GAP-P1-02]
affected_screens: [SCR-CUST-006, SCR-CUST-007, SCR-CUST-008]
decision:
  bot_dm_owns:
    - compact slot suggestions (несколько ближайших слотов кнопками)
    - quick slot selection
    - booking intent confirmation
    - pending state
    - result notification
    - retry/stale-slot recovery
  mini_app_owns:
    - expanded calendar
    - long slot lists
    - booking details
    - records list
    - booking management
    - complex filters
  navigation: >-
    Contextual deep link в релевантное состояние Mini App (услуга, специалист,
    даты, recommendation_id, conversation context ref); НЕ открывать generic
    home, когда контекст известен.
constraints:
  - подтверждение намерения ≠ подтверждение записи
  - no confirmed state до authoritative backend confirmation
  - stale_slot state обязателен
  - preserve recommendation_id через весь booking flow
```

## UX-OD-005 — records_list_as_phase_1_mini_app_home

```yaml
decision_id: UX-OD-005
title: records_list_as_phase_1_mini_app_home
status: accepted
date: 2026-07-29
owner: Product Owner
resolves: [UX-GAP-P1-01]
affected_screens: [SCR-CUST-010, SCR-CUST-001 (Mini App entry)]
decision:
  mini_app_home_phase_1: >-
    SCR-CUST-010 (upcoming bookings, relevant booking states, history when
    available).
  navigation: >-
    Contextual navigation может миновать home (slot picker, booking detail,
    cancel/reschedule context).
  excluded:
    - wellness dashboard
    - food scanner
    - water tracker
    - proactive recommendations
```

## Change Log

### v0.4 (2026-08-02) — Cancellation scope reconciliation

- `deferred_scope_note` (UX-OD-001) переформулирован: явно указано, что
  `cancel_flow` — minimal conversational cancel, а не full Cancellation
  journey; перечислены элементы full journey, которые в `cancel_flow` не
  входят (policy/deadline/refund, standalone screens, late-window/
  waitlist, провайдер-уведомления). Устраняет неоднозначность: ранее текст
  утверждал полный cancellation journey deferred, не уточняя границу с
  активной Phase 1 веткой C1–C5. Семантика самого `cancel_flow` (шаги
  C1–C5) не изменена.
- Добавлена ссылка на формальную регистрацию deferral как часть
  AYLA-DEC-0036 (без изменения границ deferral).

### v0.3 (2026-08-02) — Owner ruling formally registered (AYLA-DEC-0036)

- Owner ruling для Wave 1 Simple Reschedule (same-ID/time-only,
  cancel_then_create_new_booking запрещён, deferred-scope) формально
  зарегистрирован в `00 Foundation/Canon Governance/OWNER_DECISION_REGISTER.md`
  как **AYLA-DEC-0036** (owner ruling ID `OD-RESCHED-1`). Ранее в v0.2 это
  было отражено как неформальная пометка «owner direction, 2026-08-02» без
  registered ID.
- UX-OD-001: `reschedule_flow` и `traceability` дополнены ссылкой на
  AYLA-DEC-0036. Семантика решения (same-ID/time-only, AYLA-DEC-0022) не
  изменена — только формализация регистрации.
- UX-OD-002…005 не затронуты.

### v0.2 (2026-08-02) — Wave 1 Simple Reschedule canon alignment

- **UX-OD-001, `reschedule_flow`:** заменена механика
  `cancel_then_create_new_booking` на same-ID/time-only модель по
  AYLA-DEC-0022 (accepted, 2026-07-28) — owner direction 2026-08-02:
  `cancel_then_create_new_booking` для Simple Reschedule отклонена.
  Сохраняется `appointment_id`, версия монотонно увеличивается,
  публикуется `appointment.rescheduled`.
- **UX-OD-001, `constraints`:** снят constraint про раскрытие
  неатомарности (относился только к отклонённой механике); добавлены
  constraints про единую транзакцию, отсутствие промежуточного
  `cancelled`, запрет переноса terminal-state записи.
- **UX-OD-001, `deferred_to_W2`:** явно размечено как сужение UX-scope
  Wave 1, а не следствие доменной механики — AYLA-DEC-0022 допускает смену
  специалиста в пределах Offering как same-ID при согласии клиента, но
  Wave 1 эту ветку не открывает.
  Полная cancellation journey (owner ruling 2026-07-28, вариант Б) этим не
  затронута и не расширяется.
  Добавлена **`traceability`** на AYLA-DEC-0022 и `appointment.rescheduled`.
- UX-OD-002…005 не изменены.

### v0.1 (2026-07-29) — Initial

- Пять решений Product Owner по Owner Review Package 001 применены к
  UX-документам (UX-SYNC-001).
