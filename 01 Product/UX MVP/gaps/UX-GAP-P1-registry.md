---
artifact: gap-registry-p1
version: "0.1"
status: draft
date: 2026-07-29
task_id: UX-CUST-001
node_id: ayla.ux.gap-p1-registry
title: UX-GAP P1 Registry — Customer Surface
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

# UX-GAP P1 Registry — Customer Surface

Реестр P1-пробелов, обнаруженных при инвентаризации UX-CUST-001. Формат
сокращённый; при эскалации в P0 пробел выносится в отдельный файл.

## UX-GAP-P1-01 — Mini App landing/home для MVP не определён каноном

- **status:** CLOSED (2026-07-29) — UX-OD-005 records_list_as_phase_1_mini_app_home.
- **resolution:** home Mini App Phase 1 = SCR-CUST-010 (upcoming bookings,
  relevant booking states, history when available); contextual navigation
  может миновать home (slot picker, booking detail, cancel/reschedule
  context); wellness dashboard, food scanner, water tracker, proactive
  recommendations — excluded.
- **domain:** information architecture
- **detected_in:** UX-CUST-001
- **description:** Этап 1 допускает вход по deep link в Mini App (SRC-02 этап
  1), но какой экран там рендерится, канон не определяет. Единственная
  существующая home-спека SRC-12 (customer-main-wellness-dashboard.md)
  построена на wellness-контенте (питание/вода/цели), который вне MVP scope
  (SRC-01 §4.1, SRC-02 Non-goals).
- **why_it_matters:** Без landing-решения Mini App-часть entry (этап 1) и
  fallback этапа 13 («детали записи в Mini App», proposal) не имеют точки
  приземления.
- **blocked_screens:** SCR-CUST-001 (Mini App-вариант entry), SCR-CUST-010
  (кандидат на landing).
- **missing_decision:** Что является Mini App home в MVP: список записей,
  диалог-first заглушка с переходом в бот, или иное.
- **required_owner:** Product Owner.
- **recommended_artifact:** Decision Record.
- **can_use_temporary_assumption:** да — считать SCR-CUST-010 (Records list)
  рабочим landing для Mini App.
- **acceptance_criteria:** Решение PO зафиксировано; landing имеет screen_id в
  инвентаре.

## UX-GAP-P1-02 — Surface assignment для slot picker и booking confirmation

- **status:** CLOSED (2026-07-29) — UX-OD-004 hybrid_booking_surface.
- **resolution:** bot DM владеет compact slot suggestions, quick slot
  selection, booking intent confirmation, pending state, result notification,
  retry/stale-slot recovery; Mini App владеет expanded calendar, long slot
  lists, booking details, records list, booking management, complex filters.
  Навигация — contextual deep link в релевантное состояние Mini App (не
  generic home, когда контекст известен). Constraints: подтверждение намерения
  ≠ подтверждение записи; no confirmed state до authoritative backend
  confirmation; stale_slot state обязателен; preserve recommendation_id через
  весь booking flow.
- **domain:** channel UX
- **detected_in:** UX-CUST-001
- **description:** Канон фиксирует роли каналов в общем виде (бот — диалог и
  быстрые действия; Mini App — сложные действия, SRC-02 §Cross-channel
  Experience), но не назначает поверхность для выбора слота (этап 10) и
  подтверждения записи (этап 12). SRC-12 выносит их в Mini App (F3–F5);
  inline-вариант в bot DM каноном не исключён.
- **why_it_matters:** От поверхности зависят required data, навигация и
  контракт экрана SCR-CUST-006/008.
- **blocked_screens:** SCR-CUST-006, SCR-CUST-008.
- **missing_decision:** Поверхность для этапов 10–12 (bot DM inline vs Mini
  App vs гибрид).
- **required_owner:** Product Owner.
- **recommended_artifact:** Decision Record или строка в Screen Contract.
- **can_use_temporary_assumption:** да — следовать SRC-12 (Mini App) как
  рабочей гипотезе.
- **acceptance_criteria:** Поверхность зафиксирована для SCR-CUST-006/008.

## UX-GAP-P1-03 — Anonymous-режим: существование в MVP не подтверждено каноном

- **domain:** identity / onboarding
- **detected_in:** UX-CUST-001
- **description:** SRC-12 предполагает anonymous browsing с gate на момент
  записи (customer-booking-flow.md, customer-booking-confirm-registration-
  spec.md). Канонический journey стартует с MAX-бота/Deep link без описания
  анонимного режима (SRC-02 этап 1); identity-модель зафиксирована
  (AYLA-DEC-0016), но момент обязательной регистрации для customer — нет.
- **why_it_matters:** Определяет, существует ли SCR-CUST-009 как отдельный
  gate и что показывать до регистрации.
- **blocked_screens:** SCR-CUST-009, SCR-CUST-001.
- **missing_decision:** Допустим ли anonymous browsing в MVP и где граница
  «анонимно → идентифицирован».
- **required_owner:** Product Owner.
- **recommended_artifact:** Decision Record.
- **can_use_temporary_assumption:** да — считать, что идентификация MAX
  происходит при первом действии, требующем backend-записи (booking).
- **acceptance_criteria:** Решение PO; SCR-CUST-009 получает подтверждённый
  entry/exit.

## UX-GAP-P1-04 — MVP UX State Contract и Error/Reason Code Registry не созданы

- **domain:** UX contracts
- **detected_in:** UX-CUST-001
- **description:** Термины состояний (loading, clarification required,
  recommendation ready, no recommendation, consent required, slot unavailable,
  booking pending/confirmed/failed, retry, human handoff) и коды ошибок
  используются в SRC-02 по planned-документам (Roadmap §2.2, §6.5), которые не
  материализованы.
- **why_it_matters:** Экраны W1 именуют состояния и ошибки по неутверждённому
  словарю; риск рассинхрона UX ↔ backend.
- **blocked_screens:** все W1 (уровень naming, не поведения).
- **missing_decision:** Канонический перечень UX-состояний и error/reason
  codes.
- **required_owner:** Product Architecture + UX.
- **recommended_artifact:** Minimal Contract (UX State Contract), Specification
  (Error and Reason Code Registry).
- **can_use_temporary_assumption:** да — использовать словарь SRC-02 §Stage
  Specifications как рабочий.
- **acceptance_criteria:** Оба документа созданы; inventory сверен.

## UX-GAP-P1-05 — Статус CAP-006 и триггер этапа 14 не решены (OQ6, OQ8)

- **domain:** outcome / feedback
- **detected_in:** UX-CUST-001
- **description:** Этап 14 отнесён к CAP-006, но прямой записи в Included
  Capabilities нет (SRC-02 OQ6; кандидат — разделить Basic Feedback Capture и
  Advanced Outcome Learning). Доменный триггер `appointment.completed` и
  финальные payload/owner для этапа 14 — pending Domain Event Registry
  (SRC-02 OQ8, частично решён AYLA-DEC-0025).
- **why_it_matters:** Без триггера и статуса capability у SCR-CUST-015 нет
  подтверждённого entry.
- **blocked_screens:** SCR-CUST-015.
- **missing_decision:** MVP-статус CAP-006; регистрация `appointment.completed`
  в Domain Event Registry.
- **required_owner:** Product Owner (OQ6), Product Architecture (реестр).
- **recommended_artifact:** Decision Record (OQ6) + Specification (Domain
  Event Registry, мандат AYLA-DEC-0025).
- **can_use_temporary_assumption:** да — считать простой feedback prompt по
  факту завершения записи входящим в W1 (SRC-02 этап 14).
- **acceptance_criteria:** OQ6 закрыт; триггер этапа 14 зарегистрирован.

## UX-GAP-P1-06 — Финальные имена analytics events (OQ1)

- **domain:** analytics
- **detected_in:** UX-CUST-001
- **description:** Имена analytics events в Stage Specifications — рабочие
  (proposal) до Analytics Event Contract (SRC-02 OQ1); семантика семейств
  `recommendation.*` и `qualified_action.*` намеренно не утверждена
  (AYLA-DEC-0025 п. 8).
- **why_it_matters:** Не блокирует визуальное проектирование, но блокирует
  инструментацию экранов метриками SRC-01 §9.
- **blocked_screens:** все W1/W2 (уровень инструментации).
- **missing_decision:** Analytics Event Contract; регистрация
  `recommendation.*`, `qualified_action.attributed`.
- **required_owner:** Product Architecture + Analytics.
- **recommended_artifact:** Minimal Contract (Analytics Event Contract).
- **can_use_temporary_assumption:** да — рабочие имена SRC-02.
- **acceptance_criteria:** Контракт создан; OQ1 закрыт.

## UX-GAP-P1-07 — Конфликт AYLA-DEC-0006 vs AYLA-DEC-0015 по клиентской оплате

- **domain:** monetization boundary
- **detected_in:** UX-CUST-001
- **description:** AYLA-DEC-0006 допускал опциональную клиентскую
  онлайн-оплату; AYLA-DEC-0015 и SRC-01 §5.1 исключают клиентскую оплату из
  MVP (только provider-side charge flow). Явной отмены DEC-0006 в Decision
  Log не зафиксировано.
- **why_it_matters:** Определяет, нужен ли (нет — по позднему решению) любой
  payment-экран/CTA на customer surface; устраняет риск «воскрешения»
  оплаты из SRC-12.
- **blocked_screens:** — (подтверждение отсутствия экрана).
- **missing_decision:** Формальная пометка DEC-0006 как superseded в части
  клиентской оплаты (или подтверждение границы).
- **required_owner:** Product Owner.
- **recommended_artifact:** Decision Record (строка в Decision Log).
- **can_use_temporary_assumption:** да — руководствоваться SRC-01 §5.1
  (клиентской оплаты в MVP нет).
- **acceptance_criteria:** Decision Log содержит явное разрешение конфликта.

## UX-GAP-P1-08 — Human handoff (operator chat) после MVP

- **status:** OPEN (P1, Later).
- **domain:** operations / support
- **detected_in:** UX-SYNC-001 (вынос из UX-GAP-0106 по UX-OD-002, 2026-07-29)
- **description:** UX-OD-002 honest_self_service_terminal_fallback закрыл
  тупиковые состояния N1/N7 для MVP честным self-service fallback без
  оператора. Полноценный human handoff (порог срабатывания, канал связи с
  человеком, SLA, что видит пользователь) в MVP не требуется и отложен.
- **why_it_matters:** При масштабировании пилота и появлении операционной
  поддержки состояние SCR-CUST-019 может быть расширено до handoff; решение
  должно быть согласовано с Provider Trust Model (без обхода Ayla-медиации
  и без автоматической выдачи контактов провайдера).
- **blocked_screens:** SCR-CUST-019 (расширение до handoff — post-MVP).
- **missing_decision:** Порог и процедура handoff, владелец операционной
  процедуры, UX handoff.
- **required_owner:** Product Owner + Operations (Pilot Operations Runbook,
  Roadmap §9.3).
- **recommended_artifact:** Decision Record + раздел Pilot Operations Runbook.
- **can_use_temporary_assumption:** н/д — MVP-контур закрыт UX-OD-002.
- **acceptance_criteria:** Порог и процедура handoff зафиксированы в
  Operations Runbook; состояние SCR-CUST-019 расширено без нарушения
  constraints UX-OD-002 (no_fake_operator_availability и др.).
