---
node_id: ayla.domain.core-domain-model

title: Ayla Core Domain Model Specification
title_ru: Спецификация основной доменной модели Ayla

type: domain-specification
status: draft
decision_status: proposed
version: "1.1"

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

```yaml
consent_id:
subject_id:
scope:
purpose:
status:
policy_version:
source:
granted_at:
revoked_at:
expires_at:
```

Lifecycle:

```text
proposed → granted → revoked / expired
```

Инварианты:

1. Consent имеет scope и purpose.
2. Consent может быть отозван.
3. Отсутствие Consent нельзя компенсировать inference.
4. Новая версия политики не расширяет старое согласие автоматически.

Commands:

```text
GrantConsent
RevokeConsent
ExpireConsent
```

Events:

```text
ConsentGranted
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

Поле `status` принимает только значения Output Contract [[Ayla Intent Model Specification]]:

```text
resolved | needs_clarification | unresolved | superseded | expired | blocked_safety
```

Lifecycle (в терминах contract status):

```text
unresolved (interim) → needs_clarification → resolved
        ↘                    ↘ expired
        ↘ unresolved (terminal)
        ↘ superseded
        ↘ blocked_safety
```

Маппинг состояний потока на contract status:

| Состояние потока | Contract status (`Intent.status`) | Комментарий |
|---|---|---|
| detected | `unresolved` (interim) | Intent создан, resolution не завершён; не путать с терминальным `unresolved` |
| clarifying | `needs_clarification` | Задан ровно один clarification-вопрос |
| resolved | `resolved` | Intent передан в recommendation pipeline |
| fulfilled | `resolved` | Выполнение действия — не статус Intent; фиксируется downstream (Appointment/Action), Intent остаётся `resolved` |
| abandoned | `unresolved` (terminal) | Resolution прекращён (UNKNOWN после исчерпания clarification-подходов или отказ пользователя) |
| superseded | `superseded` | Вытеснен новым intent (correction) |
| expired | `expired` | `needs_clarification` без ответа до завершения сессии |
| blocked_safety | `blocked_safety` | Непустые `safety_flags`; recommendation pipeline не запускается |

События `IntentDetected`, `IntentAbandoned` и `IntentFulfilled` (§11) фиксируют переходы потока и не являются значениями `Intent.status`.

Инварианты:

1. Intent не равен сообщению.
2. Intent имеет evidence.
3. Низкая уверенность требует clarification.
4. Required slots заполняются до irreversible action.
5. Intent не создает Appointment напрямую.
6. Sensitive Intent проходит safety policy.

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

Владеет scope, purpose, grant, revoke, expiry и policy version.

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

MVP commands:

```text
GrantConsent
RevokeConsent
RecordContextFact
ConfirmContextFact
CorrectContextFact
DeleteContextFact
DetectIntent
RequestIntentClarification
ResolveIntent
SupersedeIntent
AbandonIntent
CreateRecommendation
ValidateRecommendation
PresentRecommendation
AcceptRecommendation
RejectRecommendation
ExpireRecommendation
RequestAppointment
ConfirmAppointment
RejectAppointment
RescheduleAppointment
CancelAppointment
CompleteAppointment
MarkAppointmentNoShow
CreateAttribution
SubmitFeedback
RecordOutcome
```

Примечание: `SubmitFeedback` — proposal, активируется только вместе с Feedback (§7.14).

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

MVP events:

```text
ConsentGranted
ConsentRevoked
ConsentExpired
ContextFactRecorded
ContextFactConfirmed
ContextFactCorrected
ContextFactDeleted
IntentDetected
IntentClarificationRequested
IntentResolved
IntentSuperseded
IntentAbandoned
IntentFulfilled
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
PendingAppointmentExpired
QualifiedActionAttributed
FeedbackSubmitted
OutcomeRecorded
```

Примечание: `IntentDetected`, `IntentAbandoned`, `IntentFulfilled` фиксируют переходы потока и не являются значениями `Intent.status` (§7.5). `FeedbackSubmitted` — proposal, активируется только вместе с Feedback (§7.14).

## 12. Systems of Record

| Объект | System of Record |
|---|---|
| User identity | Identity / Backend |
| Consent | Consent Management |
| Context Fact | Personal Context |
| Inference | Derived Context / AI Runtime |
| Intent | Intent Understanding |
| Service | Service Catalog |
| Provider | Provider Management |
| Specialist | Provider Management |
| Service Offering | Provider/Catalog boundary |
| Availability Slot | Availability and Scheduling |
| Recommendation | Recommendation |
| Appointment | Appointment Management |
| Attribution Link | Attribution |
| Feedback | Feedback Collection (deferred / proposal — §7.14) |
| Outcome | Outcome Learning / Backend facts |
| Conversation transcript | Conversation Experience |
| Billing eligibility | Billing and Eligibility (ограниченный контур по AYLA-DEC-0015 — см. §2.2, §17) |
| Payment result | Payment adapter / Billing boundary (ограниченный контур по AYLA-DEC-0015 — см. §2.2, §17) |

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

Ограниченный monetary contour по AYLA-DEC-0015 ([[Ayla Decision Log]]): списание подписки, списание booking fee 90 ₽, обработка результата списания, обновление billing status, применение provider eligibility, минимальная reconciliation с YooKassa. Этот контур не считается активацией полной Payment Processing capability и не создаёт универсальный payment domain (§2.2).

## 18. Acceptance Criteria

Документ готов к approval, когда:

1. Все MVP-active objects имеют owner.
2. Все объекты имеют stable ID.
3. Aggregate roots подтверждены.
4. Lifecycles не конфликтуют с Intent Model и MVP Scope.
5. Systems of Record согласованы.
6. Commands сопоставлены с API/tool contracts.
7. Events сопоставлены с Event Registry.
8. Consent rules согласованы с Consent Scope Registry.
9. Safety rules согласованы с Safety Policy.
10. Recommendation и Appointment связаны через recommendation_id.
11. Нет скрытого ownership между contexts.
12. Open questions закрыты или оформлены решениями.

Текущий статус по критерию 4: Intent lifecycle приведён к status-enum Output Contract [[Ayla Intent Model Specification]] (§7.5) — конфликт устранён, критерий в части Intent выполнен.

Полнота покрытия lifecycle и per-object commands/events по [[Ayla MVP Documentation Roadmap]] §4.3 на текущей версии выполнена **частично**: lifecycle определён для Consent, Context Fact, Inference, Intent, Availability Slot, Recommendation и Appointment; для User, Service, Provider, Specialist, Service Offering, Attribution Link и Outcome lifecycle и per-object commands/events не определены — см. §19 (Architecture, п. 6).

## 19. Open Questions

### Architecture

1. Граница Provider Management и Service Catalog для Offering.
2. Owner Availability Slot.
3. Нужен ли отдельный Personal Context aggregate root.
4. Где хранится authoritative Recommendation record.
5. Нужен ли отдельный Attribution context в MVP.
6. User, Service, Provider, Specialist, Service Offering, Attribution Link и Outcome не имеют определённых lifecycle и per-object commands/events — требуется дополнение до соответствия [[Ayla MVP Documentation Roadmap]] §4.3 (см. §18).
7. Провенанс записи Change Log v1.1 («восстановленная MVP-aligned версия после удаления предыдущего файла») требует подтверждения владельца документа.

### Product

1. Какие intent types входят в release.
2. Какие user facts разрешены для persistent context.
3. Какие alternatives обязательны.
4. Какое окно assisted attribution использовать.
5. Какие feedback types входят в пилот (только после активации Feedback через Scope Contract §11 — см. §7.14).

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

## 20. Approval

| Роль | Статус | Имя | Дата |
|---|---|---|---|
| Product Owner | Pending |  |  |
| Domain Architecture | Pending |  |  |
| Backend Owner | Pending |  |  |
| AI Platform Owner | Pending |  |  |
| Privacy/Safety Owner | Pending |  |  |

## 21. Change Log

| Версия | Дата | Изменение | Автор |
|---|---|---|---|
| 1.1 | 2026-07-28 | Восстановленная MVP-aligned версия после удаления предыдущего файла (провенанс требует подтверждения владельца — см. §19, Architecture п. 7) | Ayla Architecture |
| 1.1 | 2026-07-28 | Слияние с vault-версией 1.0: перенесены §2.3 Normative Force, §3.2 Technical Representations, §3.10 One Canonical Meaning, §3.11 Historical Consistency; Intent lifecycle (§7.5) приведён к status-enum Output Contract [[Ayla Intent Model Specification]] с маппинг-таблицей состояний потока; §4 подчинён [[Ayla Glossary]] (нормативная оговорка); Feedback переведён в deferred / proposal (§7.14, §17) — активация только через Scope Contract §11; `client_id` унифицирован к `subject_id` (§7.12); строки Billing eligibility / Payment result в §12 помечены как ограниченный контур по AYLA-DEC-0015; frontmatter приведён к schema v1.12 | Domain Architecture |
