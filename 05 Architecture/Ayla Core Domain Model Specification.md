---
node_id: ayla.domain.core-domain-model

title: Ayla Core Domain Model Specification
title_ru: Спецификация основной доменной модели Ayla

type: domain-specification
status: draft
decision_status: proposed
version: "1.2.3"

owner: Domain Architecture
owners:
  - Product Owner
  - Domain Architecture

reviewers:
  - Backend Architecture
  - AI Architecture
  - Product Design
  - Privacy and Safety

knowledge_area:
  - domain-model
  - product
  - architecture

system_owner:
  - ayla-platform

system_scope:
  - all Ayla production systems

source_kind: canonical

classification: internal
data_sensitivity: none
security_sensitivity: low

ai_indexing: allowed
export_policy: full

depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Product Vision]]"
  - "[[Ayla Repository Responsibility Matrix]]"
  - "[[Ayla Glossary]]"
  - "[[Ayla MVP Scope and Release Contract]]"
  - "[[Ayla MVP Documentation Roadmap]]"
  - "[[Ayla Intent Model Specification]]"
  - "[[Consent Scope Registry]]"
  - "[[AMD-020 Pilot Scope Registry]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Ayla Decision Log]]"

related_documents:
  - Ayla Intent Model Specification
  - Ayla User Journey Specification
  - Ayla Killer PRD
  - Ayla Repository Responsibility Matrix
  - Ayla Glossary



supersedes: []
superseded_by: []

updated: 2026-07-28
review_cycle: quarterly
---

# Ayla Core Domain Model Specification

## 1. Статус и назначение

Документ определяет каноническую доменную модель Ayla: ключевые бизнес-понятия, их идентичность, владение состоянием, жизненные циклы, инварианты, команды и доменные события.

Он описывает бизнес-смысл системы, а не конкретную реализацию в Django, PostgreSQL, REST API, Python-классах, LLM prompts или пользовательском интерфейсе.

### Readiness

| Гейт | Статус |
|---|---|
| Ready for technical review | No |
| Ready for owner review | No |
| Ready for approval | No |
| Ready for canonicalization | No |

Текущий статус: **Draft / Proposed — substantively developed, internally incomplete**. Блокирующие области: identity foundation (Subject/Tenant/Membership), scheduling и Appointment, lifecycle completeness, Handoff Coverage Matrix, SoR owners (§18, §22, §24).

## 2. Scope

### 2.1. MVP-значимые доменные объекты

1. User
2. Consent
3. Context Fact
4. Inference
5. Intent
6. Service
7. Provider
8. Specialist
9. Service Offering
10. Availability Slot
11. Recommendation
12. Appointment
13. Attribution Link
14. Feedback (deferred / proposal — см. §7.14, §17)
15. Outcome

### 2.2. Вне полного scope этой версии

- универсальный payment domain;
- wallet, payouts, chargebacks;
- полноценный financial ledger;
- advanced outcome learning;
- многосторонний marketplace settlement;
- multi-country compliance;
- полная микросервисная декомпозиция.

Исключение из пункта «универсальный payment domain»: в MVP разрешён ограниченный provider-side monetary flow по AYLA-DEC-0015 ([[Ayla Decision Log]]) — списание подписки, списание booking fee 90 ₽, обработка результата списания, обновление billing status, применение provider eligibility и минимальная reconciliation с YooKassa. Всё остальное (клиентская онлайн-оплата, wallet, payouts, refunds, chargebacks, split-payment, полноценный payment lifecycle, financial ledger) остаётся deferred.

### 2.3. Normative Force

`source_kind: canonical` описывает происхождение (место источника истины), а не нормативную зрелость; нормативная сила наступает только при `status: approved` (см. AYLA-DEC-0013, отклонение `canonical-candidate`).

После получения статуса `approved` настоящий документ становится нормативным источником описания доменной модели Ayla.

Документы более низкого уровня, включая PRD, ADR, API Specifications, Data Models, Event Specifications, Prompt Specifications и техническую документацию, не должны переопределять канонический смысл доменных понятий, определённых настоящим документом.

Изменение канонического значения доменного понятия допускается только посредством внесения изменений в настоящий документ с последующим обновлением зависимой документации.

Терминология, канонические определения и правила использования альтернативных наименований определяются [[Ayla Glossary]] (§3.10), который является нормативным источником терминологического управления. Настоящий документ использует эти определения и не переопределяет их.

## 3. Нормативные принципы

### 3.1. Domain before implementation

Сначала определяется бизнес-смысл объекта, затем таблица, ORM-модель, API, event schema, tool schema и UI.

### 3.2. Technical representations

Доменная Entity не тождественна:

- строке базы данных;
- ORM-модели;
- API DTO;
- UI-компоненту;
- LLM output;
- runtime artifact.

Все технические представления (домен → ORM → API → UI) должны иметь явное сопоставление с канонической доменной моделью. Наличие таблицы, класса или контракта не создаёт отдельную доменную сущность.

### 3.3. Stable identity

Ключевые объекты имеют стабильные идентификаторы:

```text
user_id
consent_id
context_fact_id
inference_id
intent_id
service_id
provider_id
specialist_id
offering_id
slot_id
recommendation_id
appointment_id
attribution_id
outcome_id
```

ID не меняется при переименовании, смене статуса, миграции и повторной обработке.

### 3.4. Aggregate consistency

Изменения состояния выполняются только через владельца агрегата, с проверкой инвариантов, авторизации, idempotency и аудита.

### 3.5. AI is never source of truth

LLM может интерпретировать, классифицировать, объяснять и предлагать. LLM не является authoritative source для consent, appointment, price, availability, payment result, profile status или подтвержденных пользовательских фактов.

### 3.6. Facts, inferences and actions are distinct

```text
Fact
Inference
Action
```

Inference не становится Fact автоматически.

### 3.7. Conversation is not System of Record

```text
Transcript ≠ Consent
Transcript ≠ Appointment
Transcript ≠ Context Fact
LLM output ≠ Recommendation record
Tool request ≠ completed action
```

### 3.8. Commands and Events

Command выражает намерение изменить состояние. Event фиксирует уже произошедший факт.

### 3.9. Semantic evolution

- patch — уточнение без изменения смысла;
- minor — совместимое расширение;
- major — breaking change.

### 3.10. One Canonical Meaning

Каждое самостоятельное доменное понятие должно иметь одно каноническое значение и одно каноническое наименование.

Правила регистрации, классификации и использования альтернативных наименований определяются исключительно [[Ayla Glossary]] — единственным авторитетным источником терминологии.

### 3.11. Historical Consistency

Изменение текущего состояния системы не должно изменять исторические бизнес-факты.

Доменная модель должна обеспечивать сохранение исторической информации, необходимой для аудита, аналитики, разрешения споров и соблюдения нормативных требований.

## 4. Ubiquitous Language

> [[Ayla Glossary]] — единственный авторитетный источник терминологии (§3.10). Данный раздел — прикладная таблица терминов доменных объектов; при расхождении приоритет имеет Glossary. Полные определения, правила альтернативных наименований и запрещённые термины фиксируются в Glossary и здесь не переопределяются.

| Термин | Каноническое значение |
|---|---|
| User | Человек, взаимодействующий с Ayla |
| Provider | Организация или самостоятельный поставщик услуг |
| Specialist | Конкретный исполнитель услуги |
| Service | Каноническое описание типа услуги |
| Service Offering | Конкретное коммерческое предложение |
| Intent | Структурированная цель пользователя |
| Context Fact | Подтвержденный факт |
| Inference | Вывод системы |
| Recommendation | Структурированное предложение следующего действия |
| Availability Slot | Потенциально доступный интервал |
| Appointment | Authoritative запись на услугу |
| Consent | Разрешение на конкретную обработку данных |
| Attribution Link | Связь рекомендации с действием |
| Outcome | Зафиксированный результат |
| Feedback | Явная оценка пользователя |
| System of Record | Авторитетный владелец состояния |
| Aggregate | Граница согласованного изменения |
| Invariant | Правило, которое нельзя нарушить |

## 5. Identity and Ownership

Каждый доменный объект обязан иметь:

- стабильный ID;
- owning context;
- System of Record;
- статус;
- provenance;
- timestamps;
- правила архивирования или удаления.

Контексты ссылаются друг на друга по идентификаторам. Копирование поля не переносит ownership.

## 6. Facts, Inferences and Actions

### 6.1. Fact

```yaml
fact_id:
subject_id:
fact_type:
value:
source:
verification_status:
consent_scope:
valid_from:
valid_until:
status:
```

Fact имеет источник, назначение, актуальность и статус подтверждения.

### 6.2. Inference

```yaml
inference_id:
subject_id:
inference_type:
value:
confidence:
evidence_refs:
model_version:
purpose:
created_at:
expires_at:
status:
```

Inference отделен от Fact, имеет confidence, evidence, purpose и срок действия.

### 6.3. Action

```yaml
action_id:
action_type:
subject_id:
actor_id:
result:
source_command_id:
created_at:
```

Action является результатом выполненной команды.

## 7. Core Domain Objects

### 7.1. User

Представляет человека, взаимодействующего с Ayla.

```yaml
user_id:
status:
identity_refs:
created_at:
updated_at:
```

Инварианты:

1. User не зависит от канала.
2. Один User может иметь несколько identity references.
3. User не равен Account, Specialist или Provider.
4. Удаление аккаунта не удаляет автоматически обязательные юридические записи.

### 7.2. Consent

The normative structure, identifiers, allowed scopes, purposes and policy bindings for Consent are defined by the [[Consent Scope Registry]]. This document defines only the domain role, ownership, lifecycle and invariants of Consent.

Lifecycle, commands и events Consent нормативно определены в [[Consent Scope Registry]] (§7–§9); ниже — сводка для чтения модели, при расхождении приоритет имеет CSR.

Consent имеет стабильный `consent_id`, привязан к `subject_id` и фиксирует состояние разрешения в рамках scope, зарегистрированного в [[Consent Scope Registry]]. Собственная схема полей Consent в настоящем документе не определяется.

Lifecycle (состояния — дословно по CSR §7; `not_requested` — отсутствие consent record):

```text
not_requested → granted
not_requested → denied

granted → revoked
granted → expired

denied  → granted  ┐
revoked → granted  ├─ создаёт новую consent record
expired → granted  ┘
```

Правило повторного согласия (CSR §7): переход к `granted` после терминального состояния (`denied` / `revoked` / `expired`) создаёт новую consent record (`previous_consent_record_id` + `transition_reason`); прежняя запись остаётся в своём терминальном статусе и не возвращается в `granted`. Переходы `granted → revoked` и `granted → expired` изменяют статус той же записи, не создавая новую. Для комбинации `subject_id` + `tenant_id` + `scope_id` существует не более одного effective (`granted`) состояния одновременно.

Инварианты:

1. Consent имеет scope и purpose.
2. Consent может быть отозван.
3. Отсутствие Consent нельзя компенсировать inference (отсутствие consent record не интерпретируется как согласие — CSR §7).
4. Новая версия политики не расширяет старое согласие автоматически.

Commands:

```text
GrantConsent
DenyConsent
RevokeConsent
ExpireConsent
```

Events (канонические имена audit events — snake_case в CSR §9.1: `consent_granted`, `consent_denied`, `consent_revoked`, `consent_expired`):

```text
ConsentGranted
ConsentDenied
ConsentRevoked
ConsentExpired
```

### 7.3. Context Fact

```yaml
context_fact_id:
subject_id:
fact_type:
value:
source:
verification_status:
consent_scope:
valid_from:
valid_until:
status:
created_at:
updated_at:
```

Lifecycle:

```text
recorded → confirmed → corrected → expired / deleted
```

Инварианты:

1. Fact имеет provenance.
2. Fact не создается только из LLM output.
3. Fact связан с разрешенным purpose.
4. Исправление сохраняет историю.
5. Устаревший Fact не используется как актуальный.

### 7.4. Inference

```yaml
inference_id:
subject_id:
inference_type:
value:
confidence:
evidence_refs:
model_version:
purpose:
status:
created_at:
expires_at:
```

Lifecycle:

```text
generated → active → superseded / expired / deleted
```

Инварианты:

1. Inference не является Fact.
2. Inference имеет confidence и provenance.
3. Inference имеет срок действия.
4. Inference не меняет authoritative state напрямую.
5. Запрещенные sensitive inference не создаются.

### 7.5. Intent

```yaml
intent_id:
subject_id:
intent_type:
status:
confidence:
slots:
missing_required_slots:
evidence_refs:
safety_flags:
created_at:
resolved_at:
superseded_by:
```

Нормативный состав runtime output, intent types, slot requirements и инварианты контракта определяются [[Ayla Intent Model Specification]] (Output Contract); настоящий раздел определяет доменную роль, границу lifecycle и владение состоянием Intent.

#### Internal resolution processing ≠ Intent status

Обработка resolution проходит внутренние состояния:

```text
received → detected → resolving → first output produced
```

Эти состояния — не значения `Intent.status`: они не сериализуются, не являются orchestration state, не означают intent-level или execution readiness и не запускают downstream processing или side effects. Они существуют только для traces, logs, metrics, recovery и replay.

`detected` — внутреннее lifecycle-состояние процесса resolution (owner ruling KM-IM-1). Оно **не отображается в `unresolved`**: отсутствие output ≠ status `unresolved`.

`intent_id` создаётся при начале resolution, но `status` присваивается только после завершения первого resolution pass; до первого output объект недоступен business consumers. Запрещён default `status = unresolved` для NOT NULL поля (ложная семантика); допустимые реализационные варианты — отдельный processing state, nullable `status` или создание aggregate после первого pass — конкретный вариант не предписывается.

#### Published Intent status

Поле `status` принимает только значения Output Contract [[Ayla Intent Model Specification]]:

```text
resolved | needs_clarification | unresolved | superseded | expired | blocked_safety
```

`unresolved` — consumer-meaningful результат **завершённого** resolution pass (resolver завершил проход без результата), а не признак того, что resolver ещё работает.

Первый публикуемый output создаётся после первого resolution pass и принимает одно из: `resolved`, `needs_clarification`, `unresolved`, `blocked_safety`. Значения `superseded` и `expired` — не результаты resolution pass, а последующие lifecycle-переходы уже опубликованного Intent.

Lifecycle опубликованного Intent (transition matrix по [[Ayla Intent Model Specification]]; семантика переходных событий — pending Domain Event Registry reconciliation, §24, Governance п. 6):

```text
needs_clarification → resolved | unresolved | expired | superseded
resolved            → superseded | expired
unresolved          → superseded | expired
blocked_safety      → superseded
```

#### Intent-level readiness

`resolved` означает только intent-level readiness (распознанность типа по Output Contract) и ничего более:

```text
resolved ≠ action authorized ≠ action confirmed ≠ action executed ≠ action succeeded
```

Выполнение действия фиксируется owning downstream capability (Appointment/Action); Intent не меняет свой `status` по факту выполнения.

#### Events

- `IntentDetected` — internal technical/observability event: не integration contract, не запускает capabilities, не используется для attribution, не равен `IntentResolved`.
- `IntentFulfilled` — производная корреляционная проекция от authoritative downstream event (например, `AppointmentCompleted`), а не самостоятельный факт выполнения.
- Семантика `IntentResolved`, `IntentAbandoned`, `IntentFulfilled`, `IntentSuperseded`, `IntentExpired` — pending Domain Event Registry reconciliation (§24, Governance п. 6); `IntentResolved` как универсальное событие не использовать до этого решения.

Инварианты:

1. Intent имеет стабильный `intent_id`.
2. Query ≠ Intent: Intent не равен сообщению.
3. Intent имеет evidence.
4. Низкая уверенность требует clarification.
5. Required slots заполняются до irreversible action.
6. Sensitive Intent проходит safety policy.
7. `detected` ∉ `Intent.status` и `detected` ↛ `unresolved`: внутреннее состояние resolver не отображается в контрактное значение.
8. `unresolved` присваивается только после завершённого resolution pass.
9. Output соответствует Output Contract [[Ayla Intent Model Specification]].
10. `resolved` = intent-level readiness только.
11. Intent не выполняет side effects и не создаёт Appointment напрямую; выполнение подтверждает owning downstream.
12. Supersession сохраняет историю.
13. Blocking safety предотвращает запуск downstream pipeline.
14. Internal telemetry ≠ публичный контракт.

### 7.6. Service

```yaml
service_id:
canonical_name:
category_id:
description:
constraints:
safety_profile:
status:
version:
```

Инварианты:

1. Service не содержит конкретную цену исполнителя.
2. Service не равен Service Offering.
3. Смена названия не меняет service_id.
4. Деактивированная услуга не предлагается.

### 7.7. Provider

```yaml
provider_id:
provider_type:
legal_name:
display_name:
tenant_id:
status:
created_at:
updated_at:
```

Инварианты:

1. Provider может иметь нескольких Specialists.
2. Самозанятый может играть роли Provider и Specialist, но идентичности не смешиваются.
3. Provider status влияет на коммерческие действия.
4. Provider не владеет каноническим Service.

### 7.8. Specialist

```yaml
specialist_id:
provider_id:
user_id:
display_name:
profile_status:
qualification_refs:
eligibility_status:
created_at:
updated_at:
```

Инварианты:

1. Specialist связан с Provider.
2. Specialist не принимает запись при запрещающем eligibility status.
3. Qualification data имеет provenance.
4. Specialist оказывает Service через Offering.

### 7.9. Service Offering

```yaml
offering_id:
service_id:
provider_id:
specialist_id:
duration_minutes:
price:
currency:
status:
eligibility_rules:
created_at:
updated_at:
```

Инварианты:

1. Offering ссылается на существующий Service.
2. Price относится к Offering.
3. Неактивное Offering не участвует в подборе.
4. Duration допустима для scheduling.
5. Offering не ослабляет глобальные safety rules.

### 7.10. Availability Slot

```yaml
slot_id:
specialist_id:
offering_id:
starts_at:
ends_at:
status:
source:
version:
expires_at:
```

Lifecycle:

```text
available → held → booked
           ↘ released / expired
```

Инварианты:

1. starts_at < ends_at.
2. Slot не может быть забронирован дважды.
3. Доступный Slot не гарантирует Appointment.
4. Hold имеет TTL.
5. Устаревший Slot нельзя использовать.

### 7.11. Recommendation

```yaml
recommendation_id:
subject_id:
intent_id:
primary_candidate:
alternative_candidates:
ranking_inputs:
gating_results:
explanation:
status:
created_at:
presented_at:
expires_at:
accepted_at:
rejected_at:
```

Lifecycle:

```text
draft → validated → presented → accepted → acted_upon
         ↘ blocked        ↘ rejected / expired
```

Инварианты:

1. Recommendation имеет recommendation_id.
2. Recommendation связана с resolved Intent.
3. Primary recommendation не означает единственный вариант.
4. Recommendation проходит eligibility и safety gates.
5. Explanation не содержит неподтвержденные факты.
6. Экономический интерес не искажает organic ranking скрыто.
7. Recommendation имеет expiry.
8. Recommendation не равна Appointment.
9. Accepted Recommendation не означает выполненное действие.
10. Для attribution сохраняется recommendation_id.

### 7.12. Appointment

```yaml
appointment_id:
subject_id:
provider_id:
specialist_id:
offering_id:
slot_id:
recommendation_id:
status:
scheduled_at:
created_at:
confirmed_at:
cancelled_at:
completed_at:
version:
```

Lifecycle:

```text
requested → pending_confirmation → confirmed → completed
    ↘ rejected          ↘ expired       ↘ cancelled / rescheduled / no_show
```

Инварианты:

1. Нельзя подтвердить запись на недоступный Slot.
2. Нельзя создать конфликтующую запись.
3. Create Appointment идемпотентен.
4. Appointment — SoR статуса записи.
5. LLM не объявляет запись созданной без backend result.
6. Reschedule сохраняет историю.
7. Cancellation имеет actor и reason.
8. recommendation_id сохраняется.
9. Provider eligibility проверяется до подтверждения.
10. Side effects имеют audit trail.

### 7.13. Attribution Link

```yaml
attribution_id:
recommendation_id:
action_type:
action_id:
attribution_type:
window_type:
created_at:
```

Типы:

```text
direct
assisted
unattributed
```

Инварианты:

1. Direct attribution требует recommendation_id.
2. Assisted attribution имеет формализованное окно.
3. Attribution не создается без Action.
4. Одно действие не получает конфликтующие direct attribution records.
5. Версия attribution rule прослеживаема.

### 7.14. Feedback (deferred / proposal)

**Статус: deferred / proposal.** Feedback не входит в Included Capabilities [[Ayla MVP Scope and Release Contract]] §4 и не перечислен среди моделей [[Ayla MVP Documentation Roadmap]] §4.3. Активация Feedback в MVP допускается только через change control Scope Contract §11 (owner decision). Определение ниже — proposal и не является основанием для реализации.

```yaml
feedback_id:
subject_id:
target_type:
target_id:
value:
comment:
source:
created_at:
```

Инварианты (proposal):

1. Feedback — пользовательский ввод, не inference.
2. Feedback не равен Outcome.
3. Изменения Feedback аудируются.
4. Свободный текст проходит privacy и safety обработку.

### 7.15. Outcome

```yaml
outcome_id:
subject_id:
appointment_id:
recommendation_id:
outcome_type:
value:
source:
status:
recorded_at:
```

Инварианты:

1. Outcome имеет источник.
2. Feedback и Outcome не смешиваются.
3. Inferred Outcome маркируется отдельно.
4. Health-related Outcome не превращается в диагноз.
5. Outcome Learning не меняет исторические факты.

## 8. Aggregate Boundaries

### 8.1. Consent Aggregate

Root: `Consent`.

Владеет состоянием согласия: grant, revoke, expiry. Нормативная структура scope, purpose и policy bindings определяется [[Consent Scope Registry]] (§7.2) и здесь не дублируется.

### 8.2. Personal Context Aggregate

Root: `Context Subject`.

Владеет Context Facts, correction history и usage metadata. Не владеет Consent, но проверяет его.

### 8.3. Intent Aggregate

Root: `Intent`.

Владеет slots, missing slots, evidence refs, clarification state и supersession.

### 8.4. Recommendation Aggregate

Root: `Recommendation`.

Владеет primary candidate, alternatives, explanation, gating results, status и expiry.

### 8.5. Appointment Aggregate

Root: `Appointment`.

Владеет selected offering reference, selected slot reference, participants и status transitions.

### 8.6. Recommendation Aggregate: owns / references / does-not-own

Owns:

- выбор кандидатов (primary candidate, alternative candidates — как ссылки, §7.11);
- Explanation;
- Ranking Result (ranking inputs, gating results);
- Presentation State (status, presented_at, expiry).

References (по идентификаторам, §5, §13):

- Intent (`intent_id`);
- кандидаты: Service Offering / Availability Slot;
- Provider.

Does not own:

- Appointment (создаётся downstream после accepted Recommendation — §7.11, инвариант 8);
- Specialist;
- Service;
- Service Offering и Availability Slot как объекты каталога и расписания.

### 8.7. Appointment Aggregate: owns / references / does-not-own

Owns:

- status transitions (lifecycle §7.12);
- Timeline (scheduled_at, confirmed_at, cancelled_at, completed_at);
- Booking Metadata (participants, version, actor и reason изменений).

References (по идентификаторам, §5, §13):

- Availability Slot (`slot_id`);
- Service Offering (`offering_id`);
- Recommendation (`recommendation_id` — сохраняется для attribution, §7.12, инвариант 8);
- Provider и Specialist (`provider_id`, `specialist_id`).

Does not own:

- Specialist, Provider, Service;
- Service Offering и его price (`price_snapshot` — исторический snapshot, §13);
- Availability Slot как объект расписания.

## 9. Lifecycle Rules

Каждый lifecycle должен:

- иметь допустимые состояния;
- запрещать недопустимые переходы;
- фиксировать actor и reason;
- публиковать событие;
- поддерживать idempotency;
- сохранять audit trail.

Статусы являются стабильными enum-значениями, а не свободным текстом.

## 10. Commands

Общий контракт:

```yaml
command_id:
command_type:
actor_id:
subject_id:
aggregate_id:
idempotency_key:
payload:
issued_at:
correlation_id:
causation_id:
```

MVP commands (группировка по превалирующему actor; классификация не меняет состав реестра и контракт команд):

User commands:

```text
GrantConsent
DenyConsent
RevokeConsent
ConfirmContextFact
CorrectContextFact
DeleteContextFact
AcceptRecommendation
RejectRecommendation
RequestAppointment
RescheduleAppointment
CancelAppointment
```

System commands:

```text
RecordContextFact
SupersedeIntent
AbandonIntent
ExpireRecommendation
CompleteAppointment
MarkAppointmentNoShow
CreateAttribution
RecordOutcome
```

AI commands:

```text
RequestIntentClarification
ResolveIntent
CreateRecommendation
ValidateRecommendation
PresentRecommendation
```

Administrative commands:

```text
ConfirmAppointment
RejectAppointment
```

Deferred (активация через change control [[Ayla MVP Scope and Release Contract]] §11 — см. §7.14):

```text
SubmitFeedback
```

Примечание: `DetectIntent` исключён из реестра команд (KM-IM-1): `detected` — внутренний этап обработки `ResolveIntent`, а не создание опубликованного результата (§7.5).

## 11. Domain Events

Общий контракт:

```yaml
event_id:
event_type:
aggregate_id:
aggregate_type:
aggregate_version:
occurred_at:
producer:
payload:
correlation_id:
causation_id:
schema_version:
```

Правила:

1. Event описывает произошедший факт.
2. Event immutable.
3. Event schema versioned.
4. Consumer idempotent.
5. PII classification обязательна.
6. Event не содержит лишние sensitive data.

MVP events (группировка по характеру события; классификация не меняет состав реестра и контракт событий):

Business events — фиксируют факты доменных lifecycle:

```text
ConsentGranted
ConsentDenied
ConsentRevoked
ConsentExpired
ContextFactRecorded
ContextFactConfirmed
ContextFactCorrected
ContextFactDeleted
IntentClarificationRequested
IntentResolved
IntentSuperseded
IntentAbandoned
RecommendationCreated
RecommendationValidated
RecommendationBlocked
RecommendationPresented
RecommendationAccepted
RecommendationRejected
RecommendationExpired
RecommendationActedUpon
AppointmentRequested
AppointmentConfirmed
AppointmentRejected
AppointmentRescheduled
AppointmentCancelled
AppointmentCompleted
AppointmentMarkedNoShow
OutcomeRecorded
```

Technical events — системные факты инфраструктурного характера:

```text
PendingAppointmentExpired
IntentDetected
```

Integration events — фиксируют факты на стыке контекстов:

```text
IntentFulfilled
QualifiedActionAttributed
```

Deferred (активация через change control [[Ayla MVP Scope and Release Contract]] §11 — см. §7.14):

```text
FeedbackSubmitted
```

Примечание: `IntentDetected` — internal technical/observability candidate (KM-IM-1): не business и не integration event, не запускает capabilities, не используется для attribution, не равен `IntentResolved` (§7.5). `IntentFulfilled` — производная корреляционная проекция от authoritative downstream event, а не самостоятельный факт выполнения. Семантика `IntentResolved` — pending Domain Event Registry (как универсальное событие не использовать до решения); классификация `IntentAbandoned` (доменное событие vs analytics/session/derived label) — pending reconciliation (§24, Governance п. 6–7). `IntentDetected`, `IntentAbandoned`, `IntentFulfilled` фиксируют переходы потока и не являются значениями `Intent.status` (§7.5).

## 12. Systems of Record

| Объект | System of Record | Caching allowed | Snapshot allowed | Replicated |
|---|---|---|---|---|
| User identity | Identity / Backend | proposal | proposal | proposal |
| Consent | Consent Management | YES (purpose-bound authoritative cache с freshness, TTL и invalidation — [[AMD-020 Pilot Scope Registry]], [[Consent Scope Registry]]) | NO | NO |
| Context Fact | Personal Context | proposal | proposal | proposal |
| Inference (persistent) | Memory & Identity Domain | proposal | proposal | proposal |
| Intent aggregate (lifecycle/persistence) | Core Domain owner | proposal | proposal | proposal |
| Intent Resolution Output Contract | Intent Model / AI Architecture | proposal | proposal | proposal |
| Internal resolver processing state | AI Runtime (internal telemetry, без публичного контракта — §7.5) | proposal | proposal | NO |
| Authoritative execution result | owning downstream capability | proposal | proposal | proposal |
| Cross-intent attribution | Attribution / analytics | proposal | proposal | proposal |
| Service | Service Catalog | proposal | proposal | proposal |
| Provider | Provider Management | proposal | proposal | proposal |
| Specialist | Provider Management | proposal | proposal | proposal |
| Service Offering | Provider/Catalog boundary | proposal | proposal | proposal |
| Availability Slot | Availability and Scheduling | proposal | proposal | proposal |
| Recommendation | Recommendation | proposal | proposal | proposal |
| Appointment | Appointment Management | proposal | YES (historical integrity snapshot — §13) | proposal |
| Attribution Link | Attribution | proposal | proposal | proposal |
| Feedback | Feedback Collection (deferred / proposal — §7.14) | proposal | proposal | proposal |
| Outcome | Outcome Learning / Backend facts | proposal | proposal | proposal |
| Conversation transcript | Conversation Experience | proposal | proposal | proposal |
| Billing eligibility | owning capability defined outside this document (граница по AYLA-DEC-0015, CAP-022 Billing Eligibility — см. §2.2, §17) | proposal | proposal | proposal |
| Payment result | external deferred (ограниченный контур по AYLA-DEC-0015 — см. §2.2, §17) | proposal | proposal | proposal |

Разграничение ролей для Inference: AI Runtime — producer/processor, который генерирует Inference, но не становится его System of Record. Persistent Inference хранится в Memory & Identity Domain ([[AMD-020 Pilot Scope Registry]], Ownership Summary: Semantic Memory → Memory & Identity Domain). Ephemeral Inference (session-scoped) не имеет persistent System of Record и не переживает сессию.

Разграничение ролей для Intent (KM-IM-1, §7.5): AI Runtime производит resolution, но не становится SoR для Appointment или completed action; authoritative execution result фиксирует owning downstream capability. Internal resolver processing state — внутренняя телеметрия AI Runtime и не является публичным доменным состоянием.

Смысл колонок: Caching allowed — допускается ли кэширование состояния вне SoR; Snapshot allowed — допускается ли snapshot по правилам §13; Replicated — допускается ли реплика состояния в другом контуре. Пометка `proposal` означает, что значение не зафиксировано нормативным источником и требует решения владельца (§24).

## 13. Cross-Context References

Контекст хранит чужие идентификаторы, а не копии чужих агрегатов.

Snapshot допускается, когда он нужен для исторической целостности, имеет timestamp и не используется как новая authoritative версия.

```text
Appointment.price_snapshot
не делает Appointment владельцем Offering price.
```

## 14. AI Interaction Rules

### 14.1. Input boundary

AI получает только разрешенные facts, допустимые inferences, минимальную историю, tool definitions, policy constraints и provenance references.

### 14.2. Output boundary

LLM output считается proposal, classification, explanation, candidate result или draft text.

LLM output не считается completed action, confirmed fact, consent, booking result, payment result или authoritative status.

### 14.3. Tool execution

```text
LLM proposes tool call
→ runtime validates schema
→ authorization check
→ consent check
→ safety check
→ backend executes command
→ backend returns result
→ runtime renders result
```

### 14.4. Side effects

Side effect требует explicit command, authorization, idempotency, audit, deterministic validation и authoritative backend result.

### 14.5. Grounding

Утверждения о цене, доступности, статусе, записи, специалисте, услуге и согласии опираются на структурированный источник.

### 14.6. Safety

Safety не существует только в prompt. Нужны deterministic gates, policy checks, tool restrictions, schema validation, audit events и block reasons.

## 15. Error and Reason Codes

```text
CONSENT_REQUIRED
CONSENT_REVOKED
CONTEXT_NOT_ALLOWED
CONTEXT_FACT_EXPIRED
INTENT_UNRESOLVED
INTENT_CLARIFICATION_REQUIRED
UNSUPPORTED_INTENT
NO_CANDIDATES
RECOMMENDATION_BLOCKED
SAFETY_BLOCKED
NO_AVAILABLE_SLOTS
SLOT_EXPIRED
SLOT_CONFLICT
PROVIDER_INELIGIBLE
APPOINTMENT_CONFLICT
APPOINTMENT_NOT_CONFIRMED
APPOINTMENT_ALREADY_CANCELLED
TOOL_TIMEOUT
MODEL_UNAVAILABLE
DEPENDENCY_UNAVAILABLE
IDEMPOTENCY_CONFLICT
UNAUTHORIZED
FORBIDDEN
VALIDATION_FAILED
```

## 16. Versioning and Evolution

Breaking change включает:

- удаление поля;
- изменение смысла поля;
- изменение enum semantics;
- изменение ownership;
- изменение lifecycle;
- изменение aggregate boundary;
- изменение required field;
- изменение event interpretation.

Stable ID удаленного типа не переиспользуется.

Lifecycle контракта:

```text
active → deprecated → retired
```

Cross-repository breaking change требует Decision Log entry, impact analysis, consumer matrix update, migration plan, rollback plan и coordinated release.

## 17. MVP Alignment

MVP-active:

```text
User
Consent
Context Fact
Intent
Service
Provider
Specialist
Service Offering
Availability Slot
Recommendation
Appointment
Attribution Link
```

Ограниченный MVP scope:

```text
Inference
Outcome
```

Deferred / proposal:

- Feedback — активация только через change control [[Ayla MVP Scope and Release Contract]] §11 (owner decision), см. §7.14;
- full payment aggregate;
- refund lifecycle;
- payout lifecycle;
- advanced outcome learning;
- provider settlement;
- universal ledger;
- multi-country compliance model.

**Cross-source contradiction record (P1-5): Feedback.** Core Scope: Feedback deferred ([[Ayla MVP Scope and Release Contract]] §5). Внешний источник (master-reviews-feedback handoff): production-blocking. Resolution owner: Product Owner. Activation prohibited until scope change через change control §11. См. §24 (Product, п. 7).

Ограниченный monetary contour по AYLA-DEC-0015 ([[Ayla Decision Log]]): списание подписки, списание booking fee 90 ₽, обработка результата списания, обновление billing status, применение provider eligibility, минимальная reconciliation с YooKassa. Этот контур не считается активацией полной Payment Processing capability и не создаёт универсальный payment domain (§2.2).

## 18. Acceptance Criteria

Документ готов к approval, когда все критерии в статусе PASSED:

| ID | Criterion | Status | Evidence | Blocker |
|---|---|---|---|---|
| CDM-AC-01 | Все MVP-active objects имеют owner | PARTIAL | §22 (unresolved: Service Offering, Availability Slot, Recommendation, Attribution Link) | Yes |
| CDM-AC-02 | Все объекты имеют stable ID | PASSED | §3.3 | No |
| CDM-AC-03 | Aggregate roots подтверждены | PARTIAL | §8 (roots определены, не подтверждены владельцем) | Yes |
| CDM-AC-04 | Lifecycles не конфликтуют с Intent Model и MVP Scope | PARTIAL | §7.5 (Intent — конфликт устранён); lifecycle coverage неполон — см. примечание ниже | Yes |
| CDM-AC-05 | Systems of Record согласованы | PARTIAL | §12 (обновлён v1.2), §22 (статусы proposal/unresolved) | Yes |
| CDM-AC-06 | Commands сопоставлены с API/tool contracts | FAILED | §10 (сопоставление не выполнено) | Yes |
| CDM-AC-07 | Events сопоставлены с Event Registry | FAILED | §11 (Event Registry не создан — §24, Governance п. 6) | Yes |
| CDM-AC-08 | Consent rules согласованы с Consent Scope Registry | PASSED | §7.2 (v1.2.1, KM-CDM-6) | No |
| CDM-AC-09 | Safety rules согласованы с Safety Policy | FAILED | §24, Safety (открытые вопросы 1–4) | Yes |
| CDM-AC-10 | Recommendation и Appointment связаны через recommendation_id | PASSED | §7.11, §7.12 (универсальность — §24, Architecture п. 9) | No |
| CDM-AC-11 | Нет скрытого ownership между contexts | PARTIAL | §8.6–§8.7, §13, §22 | Yes |
| CDM-AC-12 | Open questions закрыты или оформлены решениями | FAILED | §24 (пополнён в v1.2.1) | Yes |

Текущий статус по критерию CDM-AC-04: Intent lifecycle приведён к status-enum Output Contract [[Ayla Intent Model Specification]] (§7.5) — конфликт устранён, критерий в части Intent выполнен.

Полнота покрытия lifecycle и per-object commands/events по [[Ayla MVP Documentation Roadmap]] §4.3 на текущей версии выполнена **частично**: lifecycle определён для Consent, Context Fact, Inference, Intent, Availability Slot, Recommendation и Appointment; для User, Service, Provider, Specialist, Service Offering, Attribution Link и Outcome lifecycle и per-object commands/events не определены — см. §24 (Architecture, п. 6).

## 19. Entity Relationship Diagram

```text
                                   ┌────────┐
                                   │  User  │
                                   └───┬────┘
              grants                   │        owns
        ┌──────────────────────────────┼─────────────────────────┐
        ▼                              ▼                         │
    ┌─────────┐                 ┌─────────────┐   derived from   │
    │ Consent │                 │ Context Fact│◄─────────────┐   │
    └────┬────┘                 └──────┬──────┘              │   │
         │ gates                       │ evidence            │   │
         │                             ▼                     │   │
         │                       ┌──────────┐          ┌───────────┐
         │                       │  Intent  │◄─────────│ Inference │
         │                       └────┬─────┘ evidence └───────────┘
         │                            │ resolved
         │                            ▼
         │                    ┌─────────────────┐   candidates: Service Offering /
         └───────────────────►│  Recommendation │   Availability Slot / Provider /
                              │ (recommendation │   Specialist / Service
                              │      _id)       │
                              └───────┬─────────┘
                                      │ accepted
                                      ▼
                              ┌──────────────┐         ┌─────────┐
                              │ Appointment  │────────►│ Outcome │
                              └──────┬───────┘         └─────────┘
                                     │
                                     ▼
                              ┌──────────────┐
                              │   Feedback   │ (deferred / proposal — §7.14)
                              └──────────────┘
```

Дополнительные связи, не показанные на схеме: Appointment хранит `recommendation_id` (§7.12); Outcome ссылается на `appointment_id` и `recommendation_id` (§7.15); Attribution Link связывает Recommendation с Action через `recommendation_id` (§7.13); Consent ограничивает (gates) обработку Context Fact и Inference (§7.3, §7.4).

Граница resolver (KM-IM-1): Intent Resolver processing (internal, §7.5) → produces → Intent Resolution Result / aggregate state; внутренние состояния resolver (`received`, `detected`, `resolving`) на схеме не отображаются и не являются доменными объектами.

## 20. Domain Dependency Graph

```text
Consent ──► Context Fact ──► Intent ──► Recommendation ──► Appointment ──► Outcome
  │             ▲                ▲             │
  │             │                │             ▼
  │          Inference ──────────┘      Attribution Link ──► Action
  │
  └── ребро Consent → Context Fact действует только для consent-gated facts
      (persistent context, personalization по [[Consent Scope Registry]])
```

Правила чтения графа:

1. Consent не зависит ни от одного объекта. Consent гейтует только обработку на основании согласия — persistent context и personalization по [[Consent Scope Registry]]; факты service delivery обрабатываются на договорном основании и не требуют Consent.
2. Inference является производной от Context Fact и не создаёт обратной зависимости. Граница: Intent Resolver processing (internal, §7.5) → produces → Intent Resolution Result / aggregate state; internal processing states в граф зависимостей не входят.
3. Recommendation зависит от resolved Intent; Appointment зависит от Offering/Slot и — только для recommendation-originated appointments — от Recommendation (через `recommendation_id`; универсальная обязательность `recommendation_id` — открытый вопрос, §24, Architecture п. 9); Outcome зависит от Appointment.
4. Обратных (циклических) зависимостей владения не допускается (§5, §8).

## 21. Global Domain Invariants

Сквозные инварианты уровня всей доменной модели. Дополняют per-object инварианты §7 и принципы §3, не заменяя их.

1. Recommendation не существует без Intent: каждая Recommendation ссылается на resolved Intent (дополняет §7.11, инвариант 2).
2. Appointment не существует без Service Offering: Appointment всегда ссылается на конкретное Offering (дополняет §7.12).
3. Service Offering не существует без Service: Offering всегда ссылается на существующий канонический Service (дополняет §7.9, инвариант 1).
4. Consent никогда не выводится из поведения: ни поведение пользователя, ни Inference, ни отсутствие возражений не создают и не расширяют Consent; допустимы только явные переходы lifecycle Consent (§7.2) по структуре [[Consent Scope Registry]].
5. Inference никогда не становится Fact автоматически (§3.6): переход Inference → подтверждённый Context Fact возможен только через явное подтверждение (user confirmation / verification) с фиксацией provenance (§7.3, инварианты 1–2).
6. Копирование поля не переносит ownership (§5); snapshot не становится новой authoritative версией (§13).
7. LLM output не создаёт authoritative state ни для одного объекта модели (§3.5, §14.2).
8. Internal processing state ≠ published domain state: внутренние состояния обработки (resolver, runtime) не входят в публичные контракты и не запускают downstream (§7.5, KM-IM-1).
9. Readiness одного слоя не означает readiness downstream: `resolved` Intent — только intent-level readiness, не execution readiness (§7.5).
10. Ни один internal resolver state не может быть представлен публичным контрактным значением с иным бизнес-смыслом (нарушение §3.10 One Canonical Meaning).

## 22. Bounded Context Ownership Matrix

Матрица владения доменными объектами. Сводит §7, §8 и §12; при расхождении приоритет имеет §12.

Статусы: `confirmed` — владение подтверждено нормативным источником вне настоящего документа ([[AMD-020 Pilot Scope Registry]], [[Ayla Domain Capability Registry]]); `proposal` — владение зафиксировано настоящим документом и ожидает подтверждения владельца; `unresolved` — открытый вопрос (§24).

| Domain Object | Owner Context | Статус |
|---|---|---|
| User | Identity / Backend | proposal |
| Consent | Consent Management | confirmed (AMD-020: Consent Records → Consent Domain; CAP-002) |
| Context Fact | Personal Context | proposal |
| Inference (persistent) | Memory & Identity Domain | confirmed (AMD-020, Ownership Summary: Semantic Memory → Memory & Identity Domain) |
| Intent | Intent Understanding (разделение владения: aggregate lifecycle/persistence vs Output Contract vs AI Runtime — §12, KM-IM-1) | proposal |
| Service | Service Catalog | proposal |
| Provider | Provider Management | proposal |
| Specialist | Provider Management | proposal |
| Service Offering | Provider/Catalog boundary | unresolved (§24, Architecture п. 1) |
| Availability Slot | Availability and Scheduling | unresolved (§24, Architecture п. 2) |
| Recommendation | Recommendation | unresolved (§24, Architecture п. 4) |
| Appointment | Appointment Management | proposal |
| Attribution Link | Attribution | unresolved (§24, Architecture п. 5) |
| Feedback (deferred / proposal — §7.14) | Feedback Collection | proposal |
| Outcome | Outcome Learning / Backend facts | proposal |

## 23. Domain Object ↔ Capability Mapping

Сопоставление доменных объектов с capability из [[Ayla Domain Capability Registry]]. Статусы: `confirmed` — объект входит в `owned_concepts` соответствующей capability; `proposal` — маппинг не зафиксирован нормативным решением и требует подтверждения владельца (§24); `unresolved` — маппинг затрагивает открытый вопрос (§24).

| Domain Object | CAP-ID | Capability (canonical_name) | Статус маппинга |
|---|---|---|---|
| User | CAP-019 | Identity and Access | proposal |
| Consent | CAP-002 | Consent Management | confirmed |
| Context Fact | CAP-001 | Personal Context Management | confirmed |
| Inference | CAP-001 | Personal Context Management | proposal |
| Intent | CAP-003 | Intent Understanding | confirmed |
| Service | CAP-008 | Service Catalog Management | confirmed |
| Provider | CAP-009 | Provider and Specialist Management | confirmed |
| Specialist | CAP-009 | Provider and Specialist Management | confirmed |
| Service Offering | CAP-009 | Provider and Specialist Management | unresolved (концепт в `owned_concepts` CAP-009; owner context — §24, Architecture п. 1) |
| Availability Slot | CAP-010 | Availability Management | confirmed |
| Recommendation | CAP-004 | Recommendation Formation | confirmed |
| Appointment | CAP-011 | Appointment Management | confirmed |
| Attribution Link | CAP-013 | Recommendation Attribution | confirmed |
| Feedback | CAP-012 | Feedback Collection (deferred / proposal — §7.14) | proposal |
| Outcome | CAP-006 | Outcome Capture | confirmed |
| Billing eligibility | CAP-022 | Billing Eligibility | confirmed (контур AYLA-DEC-0015) |
| Payment result | CAP-023 | Payment Processing | confirmed (external deferred, контур AYLA-DEC-0015) |

## 24. Open Questions

### Architecture

1. Граница Provider Management и Service Catalog для Offering.
2. Owner Availability Slot.
3. Нужен ли отдельный Personal Context aggregate root.
4. Где хранится authoritative Recommendation record.
5. Нужен ли отдельный Attribution context в MVP.
6. User, Service, Provider, Specialist, Service Offering, Attribution Link и Outcome не имеют определённых lifecycle и per-object commands/events — требуется дополнение до соответствия [[Ayla MVP Documentation Roadmap]] §4.3 (см. §18).
7. Провенанс записи Change Log v1.1 («восстановленная MVP-aligned версия после удаления предыдущего файла») требует подтверждения владельца документа.
8. ~~Двойная семантика `Intent.status = unresolved`~~ — **закрыт owner ruling KM-IM-1 (ACCEPTED, 2026-07-28)**: `detected` — internal resolver lifecycle, не входит в Output Contract; `unresolved` — только результат завершённого resolution pass (§7.5).
9. `recommendation_id` обязателен для всех Appointment или только для recommendation-originated (§7.12, §20) (v1.3, требует owner decision).
10. Action — полноценный доменный объект или generic `action_id` подлежит удалению из модели (§6.3, §7.13) (v1.3, требует owner decision).
11. Финальный владелец Service Offering: Provider Management vs Service Catalog — конкретизация п. 1 до единственного owner context (v1.3, требует owner decision).
12. Формализация Appointment reschedule lifecycle: отдельные состояния/события или переиспользование cancel+create (§7.12) (v1.3, требует owner decision).

### Product

1. Какие intent types входят в release.
2. Какие user facts разрешены для persistent context.
3. Какие alternatives обязательны.
4. Какое окно assisted attribution использовать.
5. Какие feedback types входят в пилот (только после активации Feedback через Scope Contract §11 — см. §7.14).
6. Active Outcome slice: какие outcome types фиксируются в MVP и через какой источник (§7.15, §17) (v1.3, требует owner decision).
7. Cross-source contradiction P1-5: Feedback deferred по Scope Contract §5 vs production-blocking по master-reviews-feedback handoff — resolution owner Product Owner, активация только через change control §11 (см. §17) (v1.3, требует owner decision).

### Privacy

1. Какие Context Facts требуют отдельного consent scope.
2. Какие inferred preferences разрешены.
3. Retention transcript и Recommendation.
4. Какие данные запрещено передавать в LLM.

### Safety

1. Полный список health-sensitive triggers.
2. Какие рекомендации требуют deterministic block.
3. Где требуется human escalation.
4. Какие категории запрещены без health check.

### Governance

1. Кто owner public domain schemas.
2. Кто утверждает lifecycle changes.
3. Кто owner tool schemas при конфликте consumers.
4. Как синхронно обновляются pins consumers.
5. Какой документ canonical для enum values.
6. Согласование event names с [[Ayla MVP Documentation Roadmap]] и [[Ayla MVP User Journey Specification]] (включая CamelCase доменных событий vs snake_case audit events CSR §9.1) (v1.3, требует owner decision). Семантика `IntentResolved` — pending Domain Event Registry; как универсальное событие не использовать до решения (KM-IM-1, §7.5).
7. `IntentAbandoned` — доменное событие vs analytics/session/derived label (KM-IM-1, §7.5, §11) (v1.3, требует owner decision).

## 25. Approval

| Роль | Статус | Имя | Дата |
|---|---|---|---|
| Product Owner | Pending |  |  |
| Domain Architecture | Pending |  |  |
| Backend Owner | Pending |  |  |
| AI Platform Owner | Pending |  |  |
| Privacy/Safety Owner | Pending |  |  |

## 26. Change Log

| Версия | Дата | Изменение | Автор |
|---|---|---|---|
| 1.1 | 2026-07-28 | Восстановленная MVP-aligned версия после удаления предыдущего файла (провенанс требует подтверждения владельца — см. §24, Architecture п. 7) | Ayla Architecture |
| 1.1.1 | 2026-07-28 | Слияние с vault-версией 1.0: перенесены §2.3 Normative Force, §3.2 Technical Representations, §3.10 One Canonical Meaning, §3.11 Historical Consistency; Intent lifecycle (§7.5) приведён к status-enum Output Contract [[Ayla Intent Model Specification]] с маппинг-таблицей состояний потока; §4 подчинён [[Ayla Glossary]] (нормативная оговорка); Feedback переведён в deferred / proposal (§7.14, §17) — активация только через Scope Contract §11; `client_id` унифицирован к `subject_id` (§7.12); строки Billing eligibility / Payment result в §12 помечены как ограниченный контур по AYLA-DEC-0015; frontmatter приведён к schema v1.12 | Domain Architecture |
| 1.2 | 2026-07-28 | Пакет доработок по результатам независимого ревью. A: §7.2 и §8.1 — собственная схема полей Consent заменена ссылкой на [[Consent Scope Registry]] (нормативная структура scope/purpose/policy bindings выведена из документа); §12 — Inference SoR разделён на producer/processor (AI Runtime) и persistent storage (Memory & Identity Domain по [[AMD-020 Pilot Scope Registry]], Ownership Summary), добавлено пояснение про ephemeral Inference; строки Billing eligibility / Payment result приведены к «owning capability defined outside this document» (CAP-022) и «external deferred» без введения новых bounded contexts. B: добавлены §19 Entity Relationship Diagram, §20 Domain Dependency Graph, §21 Global Domain Invariants, §22 Bounded Context Ownership Matrix, §23 Domain Object ↔ Capability Mapping, §8.6–§8.7 Aggregate owns/references/does-not-own для Recommendation и Appointment; §10 Commands сгруппированы (User/System/AI/Administrative) и §11 Events сгруппированы (Business/Technical/Integration) без изменения состава; §12 дополнен колонками Caching allowed / Snapshot allowed / Replicated; бывшие §19–§21 перенумерованы в §24–§26 | Domain Architecture |
| 1.2.1 | 2026-07-28 | Пакет «внутренние противоречия» + KM-CDM-6. (1) §7.2 — lifecycle/commands/events Consent приведены к актуальной модели [[Consent Scope Registry]] (состояния not_requested/granted/denied/revoked/expired, правило повторного согласия через новую consent record, добавлены DenyConsent/ConsentDenied), делегирование CSR усилено (lifecycle/commands/events нормативно в CSR §7–§9, здесь — сводка); (2) §20 правило 1 — Consent гейтует только обработку на основании согласия (persistent context, personalization), факты service delivery — на договорном основании; ASCII-схема помечена «consent-gated facts only»; (3) §20 правило 3 — зависимость Appointment от Recommendation смягчена до recommendation-originated, универсальность `recommendation_id` вынесена в §24 (Architecture п. 9); (4) §26 — вторая запись 1.1 переименована в 1.1.1, broken reference «§19» исправлена на «§24»; (5) §22 и §23 — добавлены статусы строк confirmed / proposal / unresolved с легендой; (6) §10/§11 — SubmitFeedback и FeedbackSubmitted вынесены в подраздел Deferred (активация через Scope Contract §11), состав сохранён; в §10/§11 добавлены DenyConsent/ConsentDenied для согласованности с §7.2; (7) §24 — добавлены пункты v1.3: двойная семантика Intent.status unresolved, обязательность `recommendation_id`, статус Action, владелец Service Offering, reschedule lifecycle Appointment (Architecture п. 8–12), active Outcome slice (Product п. 6), согласование event names (Governance п. 6) | Domain Architecture |
| 1.2.2 | 2026-07-28 | Governance repair (без доменных решений): (1) §1 — добавлен Readiness-блок (все гейты No; статус Draft / Proposed — substantively developed, internally incomplete; блокирующие области: identity foundation, scheduling и Appointment, lifecycle completeness, Handoff Coverage Matrix, SoR owners); (2) §2.3 — пояснение `source_kind: canonical` (происхождение, не нормативная зрелость; нормативная сила только при `status: approved` — AYLA-DEC-0013, отклонение `canonical-candidate`); (3) frontmatter `depends_on` дополнен нормативными ссылками ([[Ayla MVP Scope and Release Contract]], [[Ayla MVP Documentation Roadmap]], [[Ayla Intent Model Specification]], [[Consent Scope Registry]], [[AMD-020 Pilot Scope Registry]], [[Ayla Domain Capability Registry]], [[Ayla Decision Log]]); (4) §17 — зарегистрирован cross-source contradiction P1-5 по Feedback (deferred по Scope Contract §5 vs production-blocking по master-reviews-feedback handoff; resolution owner Product Owner), пункт в §24 (Product п. 7); (5) §18 — Acceptance Criteria формализованы в таблицу CDM-AC-01…12 (Criterion / Status / Evidence / Blocker) без изменения содержания критериев | Domain Architecture |
| 1.2.3 | 2026-07-28 | KM-IM-1 Intent lifecycle boundary (owner ruling, ACCEPTED): (1) §7.5 переработан — разделены internal resolution processing (`received → detected → resolving → first output produced`, не сериализуется, не orchestration/readiness) и published Intent status (6 значений Output Contract [[Ayla Intent Model Specification]]; `unresolved` — только результат завершённого pass; переход «detected → unresolved» и «unresolved (interim)» удалены; guard против default `status = unresolved` для NOT NULL); добавлены подразделы Intent-level readiness (`resolved` ≠ action authorized/confirmed/executed/succeeded) и Events; инварианты пересобраны (14); (2) §11 — `IntentDetected` переведён в technical/observability, `IntentResolved`/`IntentAbandoned` — semantics pending Domain Event Registry, `IntentFulfilled` — derived projection; (3) §10 — `DetectIntent` исключён (detected = внутренний этап `ResolveIntent`); (4) §12 — владение Intent разделено (aggregate lifecycle/persistence, Output Contract, internal resolver state, execution result, cross-intent attribution), AI Runtime не SoR для completed action; (5) §21 — добавлены инварианты 8–10 (internal ≠ published, readiness послойно, запрет подмены бизнес-смысла); (6) §19/§20 — зафиксирована граница Intent Resolver processing → produces → Intent Resolution Result; (7) §24 — Architecture п. 8 закрыт (KM-IM-1), Governance п. 6 дополнен, добавлен Governance п. 7 (`IntentAbandoned`). Статус документа и readiness-блокеры не изменены | Domain Architecture |
