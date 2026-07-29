---
artifact: ux-owner-decisions
version: "0.1"
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
updated: 2026-07-29
review_cycle: monthly
---

# UX Owner Decisions — Customer Surface (2026-07-29)

Пять решений Product Owner по Owner Review Package 001
(`reviews/owner-review-001.md`, вопросы D1–D5). Применены к рабочим
UX-документам в UX-SYNC-001.

> **Пометка:** формальная регистрация этих решений в Ayla Decision Log
> (ayla-knowledge, review-gate) — отдельный процесс и в рамках UX-SYNC-001
> **не выполняется**.

## UX-OD-001 — minimal_conversational_cancel_and_reschedule

```yaml
decision_id: UX-OD-001
title: minimal_conversational_cancel_and_reschedule
status: accepted
date: 2026-07-29
owner: Product Owner
resolves: [UX-GAP-0105 (owner part), SRC-02 OQ5]
affected_screens: [SCR-CUST-012, SCR-CUST-013, SCR-CUST-010, SCR-CUST-011]
decision:
  cancel_flow: >-
    Отмена записи — через диалог в bot DM: identify_booking →
    show_booking_summary → explicit_confirmation →
    authoritative_cancellation → result.
  reschedule_flow: >-
    Перенос = cancel_then_create_new_booking (bot DM; Mini App — когда нужен
    расширенный выбор слота).
  deferred_to_W2:
    - смена мастера при переносе
    - расширенные альтернативы
    - standalone full-screen cancel/reschedule flows
constraints:
  - no cancelled state до authoritative confirmation
  - обязательны состояния cancel_pending и cancel_failed
  - заранее раскрывать пользователю неатомарность переноса, если backend не
    гарантирует атомарность
follow_up: >-
  Stage specs готовятся в UX-SPEC-001
  (flows/customer-cancel-reschedule-stages.md).
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
