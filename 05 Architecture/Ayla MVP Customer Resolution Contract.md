---
node_id: ayla.architecture.mvp-customer-resolution-contract
title: Ayla MVP Customer Resolution Contract
type: specification
status: approved
decision_status: accepted
canonical_status: approved
version: "1.0"
owner: Domain Architecture
owners:
  - Domain Architecture
  - Product Architecture
  - Product Owner
knowledge_area:
  - architecture
domain:
  - identity
  - booking
system_owner:
  - shared
source_repository: ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: high
data_categories:
  - pii
security_sensitivity: high
ai_indexing: allowed
export_policy: sanitized
created: 2026-08-17
updated: 2026-08-18
review_cycle: monthly
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Glossary]]"
  - "[[Ayla Repository Responsibility Matrix]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Ayla Core Domain Model Specification]]"
  - "[[Ayla Decision Log]]"
  - "[[Ayla MVP Appointment Contract]]"
  - "[[Ayla Master MVP Auth and Authority Contract]]"
  - "[[Consent Scope Registry]]"
  - "[[Data Inventory Matrix]]"
related:
  - "[[Ayla Master Schedule UX Contract]]"
  - "[[Ayla Salon Operations MVP Contract]]"
  - "[[Ayla Master Appointment Flow MVP]]"
  - "[[Ayla Appointment Detail Screen Contract]]"
---

# Ayla MVP Customer Resolution Contract

> Статус: **Canonical** — принят в canon 2026-08-18 (Canon Review: READY FOR
> CANON; governance ruling AYLA-DEC-0026). Master MVP canonical set:
> FROZEN FOR ENGINEERING / CONTROLLED PILOT.
>
> Этот документ закрывает P0-B3 (minimum Customer Resolution / identity /
> deduplication / consent для booking) по результатам аудита
> `docs/REPLY_MASTER_MVP_FINAL_GAP_CHECK.md` и owner ruling
> `docs/MASTER_MVP_P0_AUTHORITY_RUNTIME_CLOSURE(1).md`.
> Это НЕ CRM. Контракт определяет только минимум, необходимый для Manual
> Booking и Ayla Booking в Master MVP Controlled Pilot.

## 1. Purpose

Этот контракт определяет canonical путь customer resolution для booking:

```text
BOOKING DRAFT
      ↓
SEARCH CUSTOMER
      ↓
existing customer → SELECT / DISAMBIGUATE
      ↓
NO SUITABLE CUSTOMER → CREATE MINIMUM CUSTOMER
      ↓
CUSTOMER ID
      ↓
CreateAppointment
```

Документ является canonical owner для booking-time customer resolution
semantics: search, projection, disambiguation, deduplication, minimum creation
fields, booking consent basis. Он не создаёт Customer aggregate, не определяет
customer profile ownership сверх существующего canon и не расширяет Customer
Context до CRM/history.

## 2. Customer Concept and Authoritative Identifier

- Customer — tenant-scoped роль User относительно конкретного Provider
  (`Ayla Glossary`, Customer). Отдельный Customer aggregate не вводится.
- **Authoritative customer identifier для booking — `subject_id`**
  (canonical candidate согласно `Ayla MVP Appointment Contract`; AYLA-DEC-0016:
  `subject_id` ссылается на Subject и никогда не переписывается в исторических
  записях).
- UI и Ayla обязаны передавать в booking **authoritative Customer ID
  (`subject_id`)**, а не имя/телефон. Имя и телефон — атрибуты поиска и
  отображения, не Appointment identity.
- Телефон — Identity Reference (`ref_type: phone`, CDM §7.1): **deduplication
  signal, не глобальный immutable ID**. Master-entered телефон существует в
  состоянии `pending` до подтверждения (status enum CDM §7.1:
  `pending | verified | revoked`); relink допустим только для
  `verified` (AYLA-DEC-0016 п. 6).

## 3. Customer Search

- **Scope:** поиск выполняется только в текущем authorized tenant scope
  (см. `Ayla Master MVP Auth and Authority Contract` §5). Cross-tenant поиск
  запрещён и fail-closed (Consent Scope Registry §6).
- **P0 search fields:** name и phone. Другие поля поиска в P0 не
  используются.
- **Minimum necessary result projection:** display name, masked phone,
  customer reference (`subject_id`). Projection purpose-limited
  (`Ayla Repository Responsibility Matrix` §13).
- **В picker не возвращаются:** customer history, unrelated notes, marketing
  profile, wellness history, semantic memory, AI hypotheses, sensitive context
  без необходимости, unrelated customers (`Ayla Master Schedule UX Contract`
  §13; RRM §13).
- Failed search — не доказательство отсутствия customer; identity matching и
  duplicate prevention остаются ответственностью домена, а не UI
  (`Ayla Master Schedule UX Contract` §13).

## 4. Disambiguation

- При нескольких matches система **не угадывает**: выбор выполняет инициатор
  (мастер) через explicit select/disambiguate.
- Ayla может conversationally собрать query/context, но authoritative
  resolution общий (§8). «Запиши Марию» при нескольких подходящих Мариях
  обязывает Ayla запросить disambiguation; произвольный выбор запрещён.
- Masking применяется в projection до показа инициатору там, где полное
  значение не нужно для выбора (masked phone).

## 5. Deduplication

- Normalized phone exact match — strong deduplication signal:

```text
new customer attempt
        ↓
existing match
        ↓
do not silently create duplicate
        ↓
offer / select / disambiguate existing customer
```

- Silent duplicate creation очевидного существующего customer запрещено.
- Automatic merge запрещён (AYLA-DEC-0016 п. 4). Merge — отдельная управляемая
  support/privacy операция с audit events; в booking flow не входит и не может
  инициироваться владельцем tenant.
- Name-only совпадение без phone match не является достаточным основанием ни
  для автоматического выбора, ни для блокировки создания: применяется
  disambiguation §4.

## 6. New Customer Creation (Minimum)

- **Minimum fields P0: name + phone** — floor, утверждённый
  `Ayla Master Schedule UX Contract` §14. Поля «на будущее» не добавляются.
- Name и phone собираются только для booking purpose; local customer
  placeholder вне canonical resolution запрещён.
- Создание — WRITE владеющего домена через canonical command. Инициатор —
  actor с CreateAppointment authority (`Ayla Master MVP Auth and Authority
  Contract` §7.2). Ayla не создаёт customer автономно: Ayla может
  PROPOSE/COMMAND только с подтверждением мастера
  (`Ayla Master Schedule UX Contract`: Ayla may not create customers).
- Результат создания — authoritative Customer ID (`subject_id`), пригодный для
  `CreateAppointment`.

## 7. Consent and Privacy (Booking Minimum)

- Customer creation + appointment booking выполняются на основании
  **`service_necessity`** — тот же authorization basis, что зарегистрирован в
  Consent Scope Registry для session-level операций (`intent_understanding`,
  `provider_selection`, CSR §5.1–5.2). Отдельный personalization consent для
  booking не требуется и не запрашивается.
- Consent для marketing, wellness, semantic memory, recommendation
  personalization, health profile в P0 booking **не требуется и не
  запрашивается**; эти scopes не активируются booking operation.
- Notice-only информирование (назначение имени и телефона — только эта
  запись) — presentation responsibility booking flow; тексты — UX/privacy
  downstream, не этот контракт.
- Открытый вопрос draft-privacy-consent-mapping Q4 (регистрировать ли отдельные
  scopes `booking_execution` / `transactional_booking_support` в CSR) —
  OWNER DECISION, **не блокирует**: до решения booking покрывается
  `service_necessity` вне personalization scopes.
- Consent unknown/unavailable → fail-closed (`Ayla MVP Appointment Contract`,
  failure semantics; RRM §11).

## 8. Shared Resolver (Manual UI и Ayla)

- Manual Booking и Ayla Booking используют **один canonical customer
  resolver**: один search scope, одна projection, одна deduplication, одни
  minimum fields, один creation command.
- Разные identity semantics для Manual UI и AI запрещены. Ayla собирает
  query/context conversationally, но authoritative resolution, disambiguation
  и creation — общие (см. `Ayla Master MVP Auth and Authority Contract` §7.1:
  Ayla has no elevated authority).

## 9. Ownership and SoR

- Семантика booking-time customer resolution — настоящий контракт.
- System of Record не изменяется (AYLA-DEC-0016 п. 10): Subject → Memory &
  Identity Domain; User, Account, Identity Reference → Identity and Access
  (CAP-019).
- Владелец customer profile и salon-specific operational customer projection
  (OQ-SO-4) остаётся **Open question — owner decision, не блокирует**:
  resolution semantics определены настоящим контрактом; физическое размещение —
  implementation/ownership вопрос уровня OD-RRM-1.
- Customer PII в provider/master projections (OQ-AC-8) для P0 booking
  ограничивается проекцией §3: display name + masked phone + `subject_id`;
  расширение — отдельное privacy/owner decision.

## 10. Non-Goals

Не строится: CRM, customer history, photo context, Operational Notes,
marketing/loyalty profile, wellness context, ML-dedup, merge UI, customer
self-service identity management, customer-side channels.

## 11. Open Questions Classification

| Item | Classification | Основание |
|---|---|---|
| Customer search/dedup/disambiguation/minimum fields/consent для booking (SCH-OQ-03) | RESOLVED BY CANON (этот контракт) | §§3–8 |
| Customer profile / salon projection owner (OQ-SO-4) | OWNER DECISION REQUIRED — не блокирует P0 | §9 |
| CSR-регистрация `booking_execution` scope (privacy-mapping Q4) | OWNER DECISION REQUIRED — не блокирует P0 | §7 (`service_necessity`) |
| Расширение customer PII projection сверх §3 (OQ-AC-8) | DEFERRED — privacy/owner decision | §9 |
| Физический resolver service, нормализация телефона, индексы поиска | ENGINEERING DETAIL | Обязаны соблюдать §§3–6 |
| Previous-visit history в Appointment Detail (UX-ADS-OQ-07) | DEFERRED | Вне booking resolution |
