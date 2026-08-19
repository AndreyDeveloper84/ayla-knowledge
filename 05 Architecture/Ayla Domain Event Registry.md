---
node_id: ayla.architecture.domain-event-registry
title: Ayla Domain Event Registry
type: specification
status: draft
decision_status: proposed
version: "1.0-draft"
owner: Product Architecture / Event Governance
priority: P0
knowledge_area:
  - architecture
domain:
  - cross-domain
concerns:
  - governance
  - observability
  - audit
system_owner:
  - shared
source_repository: ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
created: 2026-07-28
updated: 2026-08-18
review_cycle: monthly
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Decision Log]]"
  - "[[Ayla Core Domain Model Specification]]"
  - "[[Consent Scope Registry]]"
  - "[[Ayla MVP Documentation Roadmap]]"
  - "[[Ayla MVP Scope and Release Contract]]"
related:
  - "[[Ayla MVP User Journey Specification]]"
  - "[[Ayla Intent Model Specification]]"
  - "[[Killer PRD]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Ayla MVP Recommendation Contract]]"
---

# Ayla Domain Event Registry

> **Статус:** Draft v0.4 — proposed. Создан по мандату AYLA-DEC-0025 п. 1
> ([[Ayla Decision Log]]). Нормативную силу получает после approval
> Product Architecture / Event Governance. **До approval реестра записи
> имеют `registration_status: proposed`** — кроме семейств
> `recommendation.*` (7 событий, §6.5) и `qualified_action.attributed`
> (§6.6), зарегистрированных в v0.3 со статусом `registered` (семантика
> утверждена [[Ayla MVP Recommendation Contract]] v0.3, architecture
> review — APPROVED; owner rulings OQ-R), и события
> `appointment.rescheduled` (§6.3), зарегистрированного в v0.4 со
> статусом `registered`: его регистрация нормативно предписана
> AYLA-DEC-0022 п. 9 (accepted), что закрывает вопрос статуса этого
> события для MVP-состава.

## 1. Назначение

Реестр — **единственный нормативный источник для event names и event
semantics** в экосистеме Ayla (AYLA-DEC-0025 п. 1). Для каждого события
он отвечает на пять вопросов:

1. Что произошло? (семантика факта)
2. Кто authoritative owner?
3. К какому классу относится событие?
4. Какой минимальный payload обязателен?
5. Кто имеет право публиковать и потреблять?

Основания: AYLA-DEC-0025 (конвенция, классификация, ownership, envelope),
AYLA-DEC-0019 (граница `detected`), AYLA-DEC-0022 (семантика reschedule:
same-ID событие `appointment.rescheduled`, replacement lineage,
cancellation reason `replaced_by_reschedule`), AYLA-DEC-0023/0024 (memory
lifecycle), [[Ayla MVP Recommendation Contract]] v0.3 (семантика
`recommendation.*` и `qualified_action.attributed`, §6.5/§6.6),
[[Ayla MVP User Journey Specification]] (потребители
событий), [[Ayla Core Domain Model Specification]] §11 (исходный состав
MVP events), [[Consent Scope Registry]] §7/§9.1 (consent lifecycle и
audit), [[Ayla MVP Scope and Release Contract]] (границы MVP).

## 2. Границы реестра: классы событий

Классификация — две независимые оси (факт — AYLA-DEC-0025 п. 3):
`semantic_class` × `publication_scope`.

**Semantic class:**

| Класс | Определение | Пример |
|---|---|---|
| `domain_fact` | Факт внутри bounded context, изменяющий или фиксирующий authoritative business state | `appointment.created` |
| `technical_signal` | Технический сигнал исполнения; запрещён как основание для доменных действий, изменений состояния и side effects; разрешён для observability (logs, tracing, metrics, replay diagnostics) | `intent.detected` |

**Publication scope — строгая иерархия (v0.2):**

```text
internal < cross_context < cross_repository < external
```

- `internal` — в пределах одного bounded context;
- `cross_context` — между bounded contexts внутри одного
  runtime/repository;
- `cross_repository` — между independently deployed consumers или
  репозиториями;
- `external` — контракт за пределами доверенной системы Ayla.

**Терминологические границы (нормативные):**

- **Domain event** — факт внутри bounded context.
- **Integration event** — опубликованный контракт для других bounded
  contexts или сервисов (domain_fact с publication_scope ≥
  cross_context). Не каждый domain event публикуется: перевод в
  integration требует зарегистрированных consumers (OQ-E4).
- **Analytics event** — проекция для измерений; не является источником
  истины для доменной логики и не создаёт доменных фактов.
- **Audit record** — не отдельный конкурирующий event name, а
  неизменяемая запись о произошедшем событии или действии. Audit —
  проекция/consumer доменных событий, а не вторая форма канона
  (AYLA-DEC-0025). Аудиторский перечень [[Consent Scope Registry]] §9.1
  подлежит приведению к этому правилу через Change Control.

### Event categories and boundaries

The registry distinguishes four event categories. A category does not create a second source of truth:

| Category | Meaning | Registry rule |
|---|---|---|
| Domain event | A committed business fact owned by a bounded context | One authoritative owner and one authorized producer |
| Integration event | A published contract derived from an approved domain fact | May cross context/repository boundaries; consumer registration is required |
| Notification event | A delivery/communication fact such as a notification attempt | Must not be used as a substitute for the domain fact that caused it |
| Analytics event | A measurement projection of an interaction or domain fact | Must not create or mutate authoritative business state |

Notification and analytics records are projections or technical/interaction records unless a separate owner decision explicitly defines a domain fact. A tool invocation, API request, click, timeout, retry, or delivery attempt is not by itself a domain event.

## 3. Naming convention

Канон (факт — AYLA-DEC-0025 п. 2): **lowercase dot-separated past-tense
fact** — `<domain>.<entity>.<fact>` (или `<entity>.<fact>` для малого
домена). Событие — факт в прошедшем времени, не команда.

Допустимо:

```text
intent.resolution_produced
consent.granted
consent.revoked
appointment.created
appointment.confirmed
appointment.completed
memory.proposal_created
memory.entry_superseded
```

Не допускаются как новые имена (legacy aliases — только в Migration
Mapping, §11): `IntentResolved`, `ConsentGranted`, `consent_granted`,
`booking.created`, `RecommendationShown`, `ContextFactCorrected`.

Canonical event name стабилен; переименование — новое canonical имя +
legacy alias + deprecation window (факт — AYLA-DEC-0025 п. 6).

## 4. Event Record Schema

Каждая запись реестра заполняется по единой схеме (v0.2 — разделены
статус регистрации и зрелость семантики; producer разделён на
разрешённый и runtime; privacy детализирована):

```yaml
event_name: <domain>.<entity>.<fact>
event_version: 1                    # целочисленная major wire-версия
registration_status: proposed       # proposed | registered | deprecated
                                    # proposed — до approval реестра; registered — только после approval
semantic_status: defined | incomplete | candidate | pending-semantic-definition
semantic_class: domain_fact | technical_signal
publication_scope: internal | cross_context | cross_repository | external
authoritative_owner: ...            # ровно один
authorized_producer:                # право публикации (реестр), не фактический отправитель
  bounded_context: ...
  component: ...
consumers: []                       # структура записи (v0.2):
#   - consumer_id: ayla.memory-service     # стабильный идентификатор
#     purpose: consent read-gate invalidation
#     minimum_version: 1
#     criticality: blocking | non-blocking
# В v0.2 допустимы краткие labels; обязательная регистрация consumer_id —
# после OQ-E6 (Consumer Compatibility Matrix).
trigger: ...                        # какой факт произошёл
payload:
  required: []                      # сверх общего envelope (§5)
  optional: []
idempotency:
  key: ...                          # стабильный бизнес-ключ события (event_id или aggregate key)
deduplication:                      # отдельно от идемпотентности (v0.2)
  key: ...                          # например, source_event_id — dedup повторного inference
  required_when: ...
ordering:
  scope: <aggregate key>            # глобальный порядок не гарантируется
privacy:
  contains_personal_data: true | false
  data_mode: pseudonymous_identifiers_only | none | values
  contains_sensitive_values: false
  subject_linkability: internal | none
retention:
  policy_ref: TBD                   # до OQ-E5
source_of_truth:
  aggregate: ...                    # или null + runtime_component
legacy_names: []
notes: ...
```

Правила:

1. У события **ровно один authoritative owner**; consumers множественны,
   publishers — нет (факт — AYLA-DEC-0025 п. 4).
2. `registration_status: registered` допустим после approval реестра;
   до него все записи — `proposed` (v0.2, ревью п. 1). Исключение:
   записи, чья семантика утверждена authoritative контрактом или
   accepted-решением, регистрируются досрочно — семейства §6.5/§6.6
   (v0.3, [[Ayla MVP Recommendation Contract]] v0.3) и
   `appointment.rescheduled` (v0.4, AYLA-DEC-0022 п. 9).
   `semantic_status: incomplete` — событие обязательно к регистрации,
   но часть семантики ждёт профильного контракта;
   `pending-semantic-definition` — регистрация запрещена (§7).
3. Персональные данные в payload — минимально необходимые; sensitive
   значения (health, safety constraints) в payload не включаются —
   только идентификаторы и ссылки (наследует CSR §9.1). Псевдонимные
   идентификаторы (`subject_id`, `memory_id`, `appointment_id`,
   `consent_record_id`, `session_id`, `message_id`) классифицируются как
   `contains_personal_data: true` с `data_mode:
   pseudonymous_identifiers_only` (v0.2, ревью п. 11).
4. `tenant_id` принадлежит envelope (§5) и **не дублируется** в
   event-specific payload, кроме специально обоснованных cross-tenant
   administrative events (v0.2, ревью п. 9). Бизнес-времена объекта
   (`created_at`, `confirmed_at`) допустимы в payload, только если
   семантически отличаются от `occurred_at` envelope; при постоянном
   равенстве дублирование запрещено.

## 5. Общий Envelope

Обязателен для всех событий с publication_scope ≥ cross_context
(факт — AYLA-DEC-0025 п. 5; `trace_id`, `related_subjects` и runtime
producer — proposal v0.1/0.2):

```yaml
event_id:           # глобально уникальный идентификатор события
event_name:         # canonical name (§3)
event_version:      # целочисленная major wire-версия схемы
occurred_at:        # когда факт произошёл (UTC)
published_at:       # когда событие опубликовано (UTC)
producer:           # фактический runtime producer (v0.2):
                    # {service, component, instance_id, deployment}
primary_subject:    # {entity_type, entity_id} — primary aggregate события;
                    # ordering и ownership привязаны к нему (v0.2)
related_subjects:   # опционально: [{entity_type, entity_id, role}] —
                    # например, recommendation с role: attribution_source (proposal)
tenant_id:          # обязателен для tenant-aware систем; единственное
                    # место tenant identity (не дублируется в data, §4 п. 4)
correlation_id:     # связывает один бизнес-процесс
causation_id:       # событие/команда, вызвавшее это событие
trace_id:           # observability (proposal)
idempotency_key:
data:               # payload события (§4)
metadata:           # классификация, версии политик
```

Инварианты: `event_id` глобально уникален; `correlation_id` стабилен в
пределах бизнес-процесса; персональные данные не попадают в envelope
бесконтрольно — только в `data` и только по правилам §4 п. 3; timestamps
в UTC, tenant timezone — только для отображения (наследует Killer PRD
§6.3 time semantics). Реестр задаёт **право** публикации
(`authorized_producer`, §4); envelope фиксирует **фактического**
отправителя (`producer`) — расхождение недопустимо и подлежит
мониторингу (v0.2, ревью п. 10).

### Common event contract mapping

The canonical wire envelope is defined in §5. The following mapping keeps the prompt-level field names unambiguous without introducing a second envelope:

| Contract field | Canonical registry field | Meaning and source |
|---|---|---|
| `event_id` | `event_id` | Unique event identity generated by the authoritative producer/runtime |
| `event_type` | `event_name` | Stable lowercase canonical event name from §3 |
| `event_version` | `event_version` | Major wire schema version |
| `aggregate_type` | `primary_subject.entity_type` | Aggregate/entity type whose state produced the fact |
| `aggregate_id` | `primary_subject.entity_id` | Aggregate/entity identifier |
| `tenant_id` | `tenant_id` | Tenant boundary from the event envelope; never duplicated in payload by default |
| `occurred_at` | `occurred_at` | Time the business fact occurred, supplied by the authoritative producer |
| `actor` | `metadata` / event-specific payload reference | Actor classification or pseudonymous reference; exact shape is event-specific and must be privacy-reviewed |
| `correlation_id` | `correlation_id` | Business process correlation identifier |
| `causation_id` | `causation_id` | Command or preceding event that caused this fact |
| `payload` | `data` | Event-specific payload listed in each registry entry |

`event_name` remains the canonical field in this registry. Implementations must not introduce a competing `event_type` naming scheme.

## 6. Event Registry

> Записи §6.1–§6.4: `registration_status: proposed` (до approval
> реестра), кроме `appointment.rescheduled` (§6.3) — `registered` по
> AYLA-DEC-0022 п. 9. Записи §6.5–§6.6: `registration_status: registered`
> (семантика утверждена [[Ayla MVP Recommendation Contract]] v0.3,
> architecture review APPROVED + owner rulings OQ-R).

### 6.1 Intent

```yaml
event_name: intent.resolution_produced
event_version: 1
registration_status: proposed
semantic_status: defined
semantic_class: domain_fact
publication_scope: cross_context
authoritative_owner: Intent Resolution
authorized_producer: {bounded_context: Intent Understanding, component: Intent Resolver}
consumers: [Conversation Orchestration, Journey Projection, Analytics]
trigger: >
  Завершён первый resolution pass и сформирован первый consumer-meaningful
  Intent Resolution Output (AYLA-DEC-0025 п. 7, AYLA-DEC-0019).
payload:
  required: [intent_id, resolution_status]
  optional: [primary_intent_type, secondary_intent_refs, clarification_reason,
             allows_immediate_safe_action, evidence_refs]
idempotency: {key: intent_id}
ordering: {scope: intent_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: Intent}
legacy_names: [IntentResolved]
notes: >
  resolution_status: resolved | needs_clarification | unresolved |
  blocked_safety (payload, не имя события). `intent.resolved` как общее
  событие не используется — двусмысленно (AYLA-DEC-0025 п. 7).
  Инвариант: primary_intent_type обязателен, когда resolution_status =
  resolved; при unresolved / blocked_safety может отсутствовать;
  при needs_clarification — по правилам Intent Model (v0.2, ревью).
  allows_immediate_safe_action не подтверждает исполнение действия
  (Intent Model v0.6+). evidence_refs — только ссылки, не фрагменты.
```

```yaml
event_name: intent.detected
event_version: 1
registration_status: proposed
semantic_status: defined
semantic_class: technical_signal
publication_scope: internal
authoritative_owner: Intent Resolution
authorized_producer: {bounded_context: Intent Understanding, component: Intent Resolver}
consumers: [Observability]
trigger: >
  Resolver зафиксировал наличие намерения до первого resolution pass
  (AYLA-DEC-0019).
payload:
  required: [session_id, message_id]
  optional: []
idempotency: {key: event_id}
ordering: {scope: session_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: null, runtime_component: Intent Resolver}
legacy_names: [IntentDetected]
notes: >
  contract_visibility: internal_observability_only;
  integration_allowed: false; public_contract: false. Не является
  значением Intent.status, не запускает capabilities, не используется
  для attribution и не равен intent.resolution_produced (AYLA-DEC-0019,
  CDM §7.5/§11).
```

Кандидаты (semantics определена в Intent Model / CDM, требуется review):
`intent.superseded`, `intent.expired` (CDM §11: `IntentSuperseded`,
`IntentExpired`; соответствуют статусам Output Contract). Pending:
`intent.abandoned` (классификация — pending по CDM §11/§24;
`IntentFulfilled` — derived projection, не самостоятельный факт).

### 6.2 Consent

```yaml
event_name: consent.granted
event_version: 1
registration_status: proposed
semantic_status: defined
semantic_class: domain_fact
publication_scope: cross_context
authoritative_owner: Consent / Authorization context
authorized_producer: {bounded_context: Consent Management, component: Consent Service}
consumers: [Memory Service (read gate), Audit, Analytics]
trigger: Пользователь предоставил согласие (CSR §7 lifecycle).
payload:
  required: [consent_record_id, subject_id, scope_id, scope_version, effective_at]
  optional: [expires_at, source, proof_ref]
idempotency: {key: consent_record_id}
ordering: {scope: subject_id + scope_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: Consent Record}
legacy_names: [ConsentGranted, consent_granted]
notes: >
  purpose не дублируется в payload: он однозначно выводится из
  versioned scope definition (scope_id + scope_version); если отдельная
  policy version отличается от scope_version — фиксируется как
  policy_version (v0.2, ревью). Consent state не является MemoryEntry и
  не публикуется как memory.* (AYLA-DEC-0023/0024).
```

```yaml
event_name: consent.revoked
event_version: 1
registration_status: proposed
semantic_status: defined
semantic_class: domain_fact
publication_scope: cross_context
authoritative_owner: Consent / Authorization context
authorized_producer: {bounded_context: Consent Management, component: Consent Service}
consumers: [Memory Service (revocation layers, AYLA-DEC-0024 п. 5), Audit, Analytics]
trigger: Пользователь отозвал согласие (CSR §7).
payload:
  required: [consent_record_id, subject_id, scope_id, scope_version, revoked_at, revocation_mode]
  optional: [reason_ref]
idempotency: {key: consent_record_id + revoked_at}
ordering: {scope: subject_id + scope_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: Consent Record}
legacy_names: [ConsentRevoked, consent_revoked]
notes: >
  revocation_mode обязателен (v0.2, ревью): downstream обязан различать
  режимы отзыва (session_personalization_stop | consent_record_revocation
  — Intent Model, REVOKE_CONSENT) для применения эффекта. Немедленный
  runtime effect обязателен (AYLA-DEC-0024 п. 5а): read gate применяет
  актуальное consent state независимо от доставки события.
```

Кандидаты: `consent.denied`, `consent.expired` (lifecycle определён в
CSR §7/§9.1, в AYLA-DEC-0025 прямо не названы).

### 6.3 Appointment

Семантика reschedule (факт — AYLA-DEC-0022): перенос — версионируемая
операция, а не статус; статус `rescheduled` не вводится. **Same-ID**
перенос (изменение времени/даты, смена исполнителя в пределах того же
Offering, неизменные коммерческие условия) публикует
`appointment.rescheduled` с увеличением `version` и созданием
AppointmentRevision. **Replacement** (другая услуга/Offering, изменение
цены, новая consent boundary) публикует пару lifecycle-событий:
`appointment.cancelled` старой записи (`cancellation_reason =
replaced_by_reschedule`, ссылка `replacement_appointment_id`) и
`appointment.created` новой записи с lineage-полями (`reschedule_of`,
`root_appointment_id`, `reschedule_count`); `appointment.rescheduled`
при replacement НЕ публикуется. Оба идентификатора создаются до записи
outbox в единой транзакции (AYLA-DEC-0022 п. 10), поэтому ссылка на
replacement в cancellation event обязательна к заполнению. Lineage
только внутри одного tenant: cross-tenant `reschedule_of` запрещён
(AYLA-DEC-0022 п. 3; tenant identity — envelope `tenant_id`, §4 п. 4).
Единственный producer семейства — CAP-011 / Appointment Service
(AYLA-DEC-0022 п. 9, AYLA-DEC-0025 п. 4).

```yaml
event_name: appointment.created
event_version: 1
registration_status: proposed
semantic_status: defined
semantic_class: domain_fact
publication_scope: cross_repository
authoritative_owner: Appointment
authorized_producer: {bounded_context: Appointment, component: Appointment Service}
consumers: [Notification, Journey Projection, Analytics, Attribution]
trigger: >
  Успешное создание authoritative Appointment aggregate в локальном SoR
  со стартовым состоянием pending. НЕ означает принятие записи внешним
  booking authority и НЕ означает подтверждение записи (v0.2, ревью
  п. 2). Booking Request ≠ Booking Created ≠ Confirmed Booking
  (полная UJS, Stage 5).
payload:
  required: [appointment_id, subject_id]
  optional: [user_id, specialist_id, service_offering_id, slot_ref,
             recommendation_id, reschedule_of, root_appointment_id,
             reschedule_count]
idempotency: {key: appointment_id}
ordering: {scope: appointment_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: Appointment}
legacy_names: [AppointmentCreated]
notes: >
  Mapping `AppointmentRequested` (CDM §11) — semantic review required:
  если оно означало команду или входящий request, полным alias не
  является (request submitted ≠ aggregate persisted ≠ external booking
  accepted ≠ appointment confirmed). Финальная граница — Appointment
  Contract (planned). Lineage-поля (v0.4, AYLA-DEC-0022 п. 3):
  заполняются только при создании записи через replacement —
  `reschedule_of` (id непосредственного предка, ациклично, тот же
  tenant), `root_appointment_id`, `reschedule_count` (наследуется +1
  по lineage); при обычном создании поля отсутствуют (стиль: поле
  опускается, не null).
```

```yaml
event_name: appointment.confirmed
event_version: 1
registration_status: proposed
semantic_status: defined
semantic_class: domain_fact
publication_scope: cross_repository
authoritative_owner: Appointment
authorized_producer: {bounded_context: Appointment, component: Appointment Service}
consumers: [Notification, Journey Projection, Analytics, Attribution]
trigger: Booking authority подтвердил переход в authoritative confirmed state (полная UJS, Stage 5).
payload:
  required: [appointment_id]
  optional: [confirmed_by, recommendation_id]
idempotency: {key: appointment_id}
ordering: {scope: appointment_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: Appointment}
legacy_names: [AppointmentConfirmed, booking.confirmed]
notes: User-facing confirmation показывается только после этого факта (полная UJS, Stage 5 Success Criteria).
```

```yaml
event_name: appointment.completed
event_version: 1
registration_status: registered
semantic_status: defined
semantic_class: domain_fact
publication_scope: cross_repository
authoritative_owner: Appointment
authorized_producer: {bounded_context: Appointment, component: Appointment Service}
consumers: [Journey Projection (Stage 14 trigger), Outcome, Analytics]
trigger: Appointment Domain authoritatively commits normal completion after the approved scheduled_end + 3 hours deadline when no lifecycle exception was registered before it, or commits another canonical completion path when its approved semantics apply.
payload:
  required: [appointment_id]
  optional: [completion_evidence_ref]  # не используется для zero-action normal completion; зарезервирован для correction/exception path
idempotency: {key: appointment_id}
ordering: {scope: appointment_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: Appointment}
legacy_names: [AppointmentCompleted]
notes: >
  Normal completion path полностью определён: trigger — Appointment Domain
  authoritatively commits normal completion after the approved
  scheduled_end + 3 hours deadline, если до него не зарегистрирован
  lifecycle exception (см. trigger выше); timing rule задана approved
  three-hour window, producer — authoritative backend completion mechanism
  (scheduled-job pattern, commit-time exception check) по Ayla MVP
  Appointment Contract §5B «Authoritative Completion Runtime» —
  zero-action happy path, не client timer и не UI observation;
  idempotent — повторный запуск job не создаёт duplicate event; UNKNOWN
  обрабатывается через readback/reconciliation. Прохождение времени
  записи не является этим событием (MVP User Journey v0.3, этап 14).
  Открытым остаётся только exception path: evidence/correction authority
  (OQ-AC-3/OQ-AC-7, Ayla MVP Appointment Contract) и customer-side
  «Визит не состоялся» (OQ-AC-17, Deferred — вне текущего Master MVP
  Controlled Pilot). Зарегистрировано v0.5 (2026-08-18) по governance
  decision AYLA-DEC-0026 по прецеденту досрочной регистрации
  AYLA-DEC-0022 п. 9: normal completion path полностью определён
  (semantic_status: defined); exception-path evidence/correction
  authority остаётся pending (OQ-AC-3/OQ-AC-7) и не блокирует
  регистрацию normal path.
```

```yaml
event_name: appointment.cancelled
event_version: 1
registration_status: proposed
semantic_status: defined
semantic_class: domain_fact
publication_scope: cross_repository
authoritative_owner: Appointment
authorized_producer: {bounded_context: Appointment, component: Appointment Service}
consumers: [Notification, Availability, Analytics, Attribution (guardrail)]
trigger: Запись отменена; история не удаляется (CAP-011 invariant).
payload:
  required: [appointment_id]
  optional: [cancelled_by, cancellation_reason, cancellation_reason_ref,
             replacement_appointment_id]
idempotency: {key: appointment_id}
ordering: {scope: appointment_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: Appointment}
legacy_names: [AppointmentCancelled]
notes: >
  Отмена не удаляет ранее выданные или сохранённые attribution evidence;
  downstream-обработка отмены определяется Recommendation/Attribution
  Contract (Killer PRD §6.3), а не этим реестром (v0.2, ревью).
  Причины отмены (v0.4): `cancellation_reason` — канонический enum;
  первое зарегистрированное значение — `replaced_by_reschedule`
  (AYLA-DEC-0022 п. 3: старая запись при replacement); полный enum —
  Appointment Contract (planned). При `cancellation_reason =
  replaced_by_reschedule` поле `replacement_appointment_id` обязательно
  к заполнению: оба идентификатора создаются до записи outbox в единой
  транзакции (AYLA-DEC-0022 п. 10).
```

```yaml
event_name: appointment.rescheduled
event_version: 1
registration_status: registered
semantic_status: defined
semantic_class: domain_fact
publication_scope: cross_repository
authoritative_owner: Appointment
authorized_producer: {bounded_context: Appointment, component: Appointment Service}
consumers: [Notification, Availability, Journey Projection, Analytics, Attribution]
trigger: >
  Same-ID перенос подтверждён: версия Appointment увеличена, создана
  AppointmentRevision (AYLA-DEC-0022 п. 1). НЕ публикуется при
  replacement (там — `appointment.cancelled` + `appointment.created`
  с lineage-полями) и НЕ публикуется, пока Reschedule Proposal в
  статусе pending (CDM §7.12, Reschedule Proposal инв. 1).
payload:
  required: [appointment_id, version, previous_version, revision_id,
             changed_fields, actor]
  optional: [reason, reschedule_count, starts_at, previous_starts_at,
             specialist_offering_assignment_id,
             previous_specialist_offering_assignment_id]
idempotency: {key: revision_id}
ordering: {scope: appointment_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: Appointment}
legacy_names: [AppointmentRescheduled, booking.rescheduled]
notes: >
  Регистрация нормативно предписана AYLA-DEC-0022 п. 9 (accepted
  2026-07-28): same-ID reschedule → `appointment.rescheduled`,
  единственный producer — CAP-011. `changed_fields` — список имён
  изменённых полей (зеркало AppointmentRevision.changed_fields);
  значения передаются dedicated-парами «previous_*/текущее значение»;
  неизменные поля опускаются (стиль: поле отсутствует, не null).
  `tenant_id` — только в envelope (§4 п. 4). `actor` — инициатор
  переноса (user | specialist | admin | owner | system |
  external_system); ограничения на системные изменения — CDM §7.12,
  AYLA-DEC-0022 (автоматический перенос без согласия клиента запрещён).
  Полные условия same-ID vs replacement — AYLA-DEC-0022 п. 2,
  CDM §7.12.
```

Кандидаты: `appointment.rejected`, `appointment.no_show` (CDM §11
перечисляет; детальная семантика — Appointment Contract).
`appointment.rescheduled` зарегистрирован в v0.4 (AYLA-DEC-0022).
Technical signal (candidate): `pending_appointment.expired` (CDM §11:
`PendingAppointmentExpired`).

```yaml
event_name: appointment.no_show
event_version: 1
registration_status: proposed
semantic_status: incomplete
semantic_class: domain_fact
publication_scope: cross_repository
authoritative_owner: Appointment
authorized_producer: {bounded_context: Appointment, component: Appointment Service}
consumers: [Notification, Journey Projection, Outcome, Analytics]
trigger: >
  Candidate only: an authorized actor or authoritative provider evidence commits
  that the appointment was not attended. Passage of appointment time alone is
  not sufficient evidence.
payload:
  required: [appointment_id]
  optional: [marked_by, evidence_ref, reason_ref]
idempotency: {key: appointment_id + no_show_revision}
ordering: {scope: appointment_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: Appointment}
legacy_names: [AppointmentMarkedNoShow]
notes: >
  Candidate mapping only. `no_show` is not `cancelled`, and the event must not
  be emitted until Appointment Contract resolves authority, evidence, correction,
  and provider reconciliation semantics (OQ-E3).
```

Candidate: `appointment.rejected` (CDM §11; semantic review required).
`appointment.rescheduled` is registered in v0.4 (AYLA-DEC-0022).
Technical signal (candidate): `pending_appointment.expired` (CDM §11: `PendingAppointmentExpired`).
### 6.4 Memory

Все события семейства `memory.*`: producer — Memory Service (W3,
единственный владелец state transitions — AYLA-DEC-0024 п. 10);
publication_scope по умолчанию `internal`; перевод в
cross_context/cross_repository — только при зарегистрированных
consumers (OQ-E4), автоматическая публикация каждого события запрещена.

```yaml
event_name: memory.proposal_created
event_version: 1
registration_status: proposed
semantic_status: defined
semantic_class: domain_fact
publication_scope: internal
authoritative_owner: Memory Service (W3)
authorized_producer: {bounded_context: User Context, component: Memory Service}
consumers: [Conversation Orchestration (confirmation prompt), Audit]
trigger: >
  Создан MemoryProposal (pipeline AYLA-DEC-0023 п. 2: user message →
  inference → confirmation request). До подтверждения — не память.
payload:
  required: [proposal_id, subject_id, proposed_category]
  optional: [source_event_id, evidence_refs, proposal_ttl, proposal_confidence]
idempotency: {key: proposal_id}
deduplication: {key: source_event_id, required_when: source_event_id_present}
ordering: {scope: subject_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: MemoryProposal}
legacy_names: []
notes: >
  proposal_confidence: model confidence, что candidate точно отражает
  source evidence; non_authoritative — не переходит в MemoryEntry
  (AYLA-DEC-0024 п. 1). Не каждый proposal создаётся из доменного
  события: источником может быть сообщение, команда, outcome или ручная
  коррекция — поэтому idempotency по бизнес-ключу, а dedup по
  source_event_id только при его наличии (v0.2, ревью п. 5).
```

```yaml
event_name: memory.proposal_confirmed
event_version: 1
registration_status: proposed
semantic_status: defined
semantic_class: domain_fact
publication_scope: internal
authoritative_owner: Memory Service (W3)
authorized_producer: {bounded_context: User Context, component: Memory Service}
consumers: [Audit, Analytics]
trigger: Пользователь явно подтвердил MemoryProposal.
payload:
  required: [proposal_id, subject_id, confirmed_at]
  optional: [confirmation_ref, consent_scope]
idempotency: {key: proposal_id}
ordering: {scope: subject_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: MemoryProposal}
legacy_names: [ContextFactConfirmed (candidate mapping — pending semantic review)]
notes: >
  Событие означает только подтверждение пользователем; memory_id в
  payload отсутствует намеренно (v0.2, ревью п. 6). Инвариант
  (proposal): confirmation transition и создание MemoryEntry коммитятся
  атомарно W3, но остаются двумя разными фактами — создание записи
  фиксируется отдельным memory.entry_created со ссылкой proposal_id.
```

```yaml
event_name: memory.proposal_rejected
event_version: 1
registration_status: proposed
semantic_status: defined
semantic_class: domain_fact
publication_scope: internal
authoritative_owner: Memory Service (W3)
authorized_producer: {bounded_context: User Context, component: Memory Service}
consumers: [Audit, Analytics]
trigger: Пользователь отклонил MemoryProposal; память не создаётся.
payload:
  required: [proposal_id, subject_id, rejected_at]
  optional: []
idempotency: {key: proposal_id}
ordering: {scope: subject_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: MemoryProposal}
legacy_names: []
notes: Отклонение не создаёт негативный факт (полная UJS, Learning Signals).
```

```yaml
event_name: memory.entry_created
event_version: 1
registration_status: proposed
semantic_status: defined
semantic_class: domain_fact
publication_scope: internal
authoritative_owner: Memory Service (W3)
authorized_producer: {bounded_context: User Context, component: Memory Service}
consumers: [Audit, Recommendation (read gate), Analytics]
trigger: Создана MemoryEntry (active) после whitelist check и confirmation (AYLA-DEC-0024 п. 1–2).
payload:
  required: [memory_id, subject_id, category]
  optional: [proposal_id, consent_scope, purpose_tags, effective_from,
             expires_at, source_event_id]
idempotency: {key: memory_id}
deduplication: {key: source_event_id, required_when: source_event_id_present}
ordering: {scope: subject_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: MemoryEntry}
legacy_names: [ContextFactRecorded (candidate mapping — pending semantic review)]
notes: confidence в записи отсутствует (AYLA-DEC-0024 п. 1); value не включается в payload.
```

```yaml
event_name: memory.entry_superseded
event_version: 1
registration_status: proposed
semantic_status: defined
semantic_class: domain_fact
publication_scope: internal
authoritative_owner: Memory Service (W3)
authorized_producer: {bounded_context: User Context, component: Memory Service}
consumers: [Audit, Recommendation (read gate), Analytics]
trigger: >
  Correction/change/consolidation: старая запись → superseded
  (superseded_by = new_id), новая → active; update-in-place запрещён
  (AYLA-DEC-0024 п. 4).
payload:
  required: [memory_id, superseded_by, subject_id, superseded_at, supersession_reason]
  optional: []
idempotency: {key: memory_id + superseded_by}
ordering: {scope: subject_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: MemoryEntry}
legacy_names: [ContextFactCorrected]
notes: >
  supersession_reason: corrected | changed | consolidated — canonical
  enum; policy_migration — candidate reason (v0.2, ревью): перенос при
  смене политики может требовать reconfirmation и не является
  пользовательской коррекцией; канонизируется отдельно.
```

```yaml
event_name: memory.entry_expired
event_version: 1
registration_status: proposed
semantic_status: defined
semantic_class: domain_fact
publication_scope: internal
authoritative_owner: Memory Service (W3)
authorized_producer: {bounded_context: User Context, component: Memory Service}
consumers: [Audit, Recommendation (read gate)]
trigger: Истёк expires_at; запись не читается; expiration ≠ deletion (AYLA-DEC-0024 п. 8).
payload:
  required: [memory_id, subject_id, expired_at]
  optional: []
idempotency: {key: memory_id}
ordering: {scope: subject_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: MemoryEntry}
legacy_names: []
notes: >
  Инвариант (v0.2, ревью): истечение определяется детерминированно по
  expires_at; событие публикуется однократно при материализации перехода
  active → expired. Отсутствие события не разрешает чтение просроченной
  записи — runtime read gate проверяет актуальное состояние (аналог
  consent read gate, AYLA-DEC-0024 п. 5а). User-stated safety
  constraints подлежат reconfirmation (AYLA-DEC-0024 п. 8).
```

```yaml
event_name: memory.entry_revoked
event_version: 1
registration_status: proposed
semantic_status: defined
semantic_class: domain_fact
publication_scope: internal
authoritative_owner: Memory Service (W3)
authorized_producer: {bounded_context: User Context, component: Memory Service}
consumers: [Audit, Recommendation (read gate), Deletion Pipeline]
trigger: >
  Отзыв consent применён к записи: unreadable немедленно, перевод в
  deletion_pending с revoked_at/deletion_due_at (AYLA-DEC-0024 п. 5).
payload:
  required: [memory_id, subject_id, revoked_at, revocation_event_id]
  optional: [deletion_due_at]
idempotency: {key: memory_id + revocation_event_id}
ordering: {scope: subject_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: MemoryEntry}
legacy_names: []
notes: >
  Событие означает ТОЛЬКО следствие consent.revoked (v0.2, ревью п. 7,
  вариант A): revocation_event_id обязателен и ссылается на
  consent.revoked. Иные причины деактивации (user_deleted,
  policy_changed, legal_erasure, tenant_deleted) — отдельный lifecycle
  после OQ-E4, этим событием не покрываются. Физическое удаление и
  tombstone — Deletion Pipeline; memory.entry_deleted не регистрируется
  до OQ-E4.
```

Кандидат: `memory.proposal_expired` (TTL proposal — AYLA-DEC-0024 п. 2).

### 6.5 Recommendation

Семантика утверждена [[Ayla MVP Recommendation Contract]] v0.3
(architecture review — APPROVED; owner rulings OQ-R1, R2/R10, R3, R4,
R5, R6). Все записи подраздела: `registration_status: registered`.

```yaml
event_name: recommendation.created
event_version: 1
registration_status: registered
semantic_status: defined
semantic_class: domain_fact
publication_scope: cross_context
authoritative_owner: Recommendation
authorized_producer: {bounded_context: Recommendation, component: Recommendation Engine}
consumers: [Journey Projection, Analytics, Audit]
trigger: >
  Recommendation record (immutable decision record) успешно persisted
  (Recommendation Contract v0.3 §3, §5, §15). НЕ публикуется после LLM
  generation, ranking calculation, API assembly или presentation.
payload:
  required: [recommendation_id, recommendation_set_id, recommendation_role]
  optional: [parent_recommendation_id, rerank_reason,
             ranking_policy_version, expires_at]
idempotency: {key: recommendation_id}
ordering: {scope: recommendation_set_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: Recommendation}
legacy_names: [RecommendationCreated]
notes: >
  `recommendation.generated` не используется: Recommendation существует с
  persistence; LLM-генерация — internal technical step (RC §15).
  recommendation_role: primary | alternative; каждая alternative —
  отдельная запись со своим recommendation_id и parent_recommendation_id
  (owner ruling OQ-R1). Запись immutable: существенное изменение решения
  — новый recommendation_id (см. recommendation.superseded);
  presentation-only изменение — presentation_version, события не создаёт.
```

```yaml
event_name: recommendation.superseded
event_version: 1
registration_status: registered
semantic_status: defined
semantic_class: domain_fact
publication_scope: cross_context
authoritative_owner: Recommendation
authorized_producer: {bounded_context: Recommendation, component: Recommendation Engine}
consumers: [Journey Projection, Analytics, Audit, Channel Delivery / Interaction]
trigger: >
  Создана новая Recommendation, содержащая supersedes_recommendation_id
  на данную запись (RC §21).
payload:
  required: [recommendation_id, superseded_by_recommendation_id,
             supersession_reason]
  optional: []
idempotency: {key: recommendation_id + superseded_by_recommendation_id}
ordering: {scope: recommendation_set_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: Recommendation}
legacy_names: [RecommendationReplaced]
notes: >
  supersession_reason: user_context_changed | availability_changed |
  price_changed | user_declined | safety_constraint_changed |
  consent_changed | memory_changed | explicit_refresh (RC §21).
  Публикуется только после создания новой Recommendation; payload
  обязан содержать оба идентификатора (owner ruling OQ-R2/R10). Старая
  Recommendation остаётся в истории и не переписывается.
  `recommendation.replaced` — rejected alternative name.
```

```yaml
event_name: recommendation.expired
event_version: 1
registration_status: registered
semantic_status: defined
semantic_class: domain_fact
publication_scope: internal
authoritative_owner: Recommendation
authorized_producer: {bounded_context: Recommendation, component: Recommendation Engine}
consumers: [Recommendation (projection/cleanup), Analytics, Observability]
trigger: >
  Истёк TTL/freshness Recommendation (expires_at): availability или
  price snapshot устарели, journey завершён, пользователь изменил
  intent, candidate стал недоступен (RC §22).
payload:
  required: [recommendation_id, expires_at]
  optional: [expiry_reason]
idempotency: {key: recommendation_id + expires_at}
ordering: {scope: recommendation_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: Recommendation}
legacy_names: []
notes: >
  publication_scope: internal в MVP (owner ruling OQ-R2/R10):
  корректность использования обеспечивается expires_at и read/action
  gate; integration consumers НЕ должны зависеть от гарантированной
  доставки expiry event. Отсутствие события не разрешает использовать
  рекомендацию после expires_at (RC §22, инвариант). Используется для
  projection, cleanup, analytics, observability. expired ≠ invalidated.
```

```yaml
event_name: recommendation.invalidated
event_version: 1
registration_status: registered
semantic_status: defined
semantic_class: domain_fact
publication_scope: cross_context
authoritative_owner: Recommendation
authorized_producer: {bounded_context: Recommendation, component: Recommendation Engine}
consumers: [Channel Delivery / Interaction, Booking, Analytics, Audit]
trigger: >
  Дальнейшее использование Recommendation запрещено policy/action gate:
  consent revocation, safety policy change, provider removal, policy
  prohibition (RC §14, §22, §24).
payload:
  required: [recommendation_id, invalidation_reason]
  optional: [source_event_id]
idempotency: {key: recommendation_id + invalidation_reason}
ordering: {scope: recommendation_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: Recommendation}
legacy_names: []
notes: >
  cross_context (owner ruling OQ-R2/R10): downstream обязан прекратить
  действие по рекомендации; action gate остаётся обязательным
  независимо от доставки события. invalidation_reason: consent_revoked |
  safety_policy_changed | provider_removed | policy_prohibited.
  source_event_id — ссылка на исходное событие (например,
  consent.revoked) при наличии. expired ≠ invalidated: expiry —
  freshness, invalidation — допустимость действия (RC §22).
```

```yaml
event_name: recommendation.presented
event_version: 1
registration_status: registered
semantic_status: defined
semantic_class: domain_fact
publication_scope: cross_context
authoritative_owner: Channel Delivery / Interaction
authorized_producer: {bounded_context: Channel Delivery / Interaction, component: Channel Adapter (MAX)}
consumers: [Recommendation, Attribution / Measurement, Analytics, Audit]
trigger: >
  Сообщение с конкретным recommendation_id принято каналом MAX для
  доставки и получен transport-level delivery acknowledgement
  (owner ruling OQ-R3; RC §16).
payload:
  required: [recommendation_id, recommendation_set_id, channel,
             channel_message_id, delivery_ack_type, acknowledged_at]
  optional: []
idempotency: {key: recommendation_id + channel_message_id}
ordering: {scope: recommendation_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: null, runtime_component: Channel Adapter (MAX)}
legacy_names: [RecommendationShown]
notes: >
  Interaction fact (RC §15): authoritative owner — Channel Delivery /
  Interaction, не Recommendation Engine. presented ≠ viewed: фактический
  просмотр не гарантируется. delivery_ack_type: accepted_by_channel |
  delivered_to_recipient | read_by_recipient; событие допускается уже
  при accepted_by_channel; более сильный acknowledgement — отдельный
  interaction observation, исходное событие не переписывается.
  Attribution policy учитывает силу acknowledgement (RC §16).
  recommendation.presentation_requested — internal technical step,
  не регистрируется.
```

```yaml
event_name: recommendation.accepted
event_version: 1
registration_status: registered
semantic_status: defined
semantic_class: domain_fact
publication_scope: cross_context
authoritative_owner: Channel Delivery / Interaction
authorized_producer: {bounded_context: Channel Delivery / Interaction, component: Channel Adapter (MAX)}
consumers: [Recommendation, Attribution / Measurement, Booking, Analytics]
trigger: >
  Пользователь явно выбрал конкретный recommendation option как
  следующий вариант действия (строгое определение, RC §17).
payload:
  required: [recommendation_id, recommendation_set_id, acceptance_action]
  optional: [parent_recommendation_id]
idempotency: {key: recommendation_id + acceptance_action}
ordering: {scope: recommendation_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: null, runtime_component: Channel Adapter (MAX)}
legacy_names: [RecommendationAccepted]
notes: >
  acceptance_action: select | proceed_to_booking | request_booking
  (RC §17). Acceptance НЕ означает завершённую запись (booking
  completion); открытие booking flow и подтверждение записи — разные
  уровни намерения. При выборе alternative recommendation_id указывает
  на запись выбранного варианта (каждая alternative атрибутируется по
  собственному recommendation_id, Killer PRD §5.1/§6.2).
```

```yaml
event_name: recommendation.declined
event_version: 1
registration_status: registered
semantic_status: defined
semantic_class: domain_fact
publication_scope: cross_context
authoritative_owner: Channel Delivery / Interaction
authorized_producer: {bounded_context: Channel Delivery / Interaction, component: Channel Adapter (MAX)}
consumers: [Recommendation, Analytics]
trigger: >
  Пользователь явно отказался от Recommendation (RC §17).
payload:
  required: [recommendation_id, recommendation_set_id]
  optional: []
idempotency: {key: recommendation_id}
ordering: {scope: recommendation_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: null, runtime_component: Channel Adapter (MAX)}
legacy_names: []
notes: >
  Только явный отказ: бездействие НЕ равно decline (RC §17).
  `recommendation.rejected` — rejected alternative name. Отклонённая
  recommendation не атрибутируется (RC §18).
```

### 6.6 Attribution

Семантика утверждена [[Ayla MVP Recommendation Contract]] v0.3 (owner
rulings OQ-R2/R10, R4, R5). Запись: `registration_status: registered`.

```yaml
event_name: qualified_action.attributed
event_version: 1
registration_status: registered
semantic_status: defined
semantic_class: domain_fact
publication_scope: cross_context
authoritative_owner: Attribution / Measurement
authorized_producer: {bounded_context: Attribution / Measurement, component: Attribution Service}
consumers: [Analytics, Product Thesis Validation, Audit]
trigger: >
  Применена attribution policy: Recommendation существовала + qualified
  action произошёл + policy сопоставила их в пределах window (RC §18).
payload:
  required: [attribution_id, recommendation_id, recommendation_set_id,
             action_type, action_category, attribution_type,
             attributed_at, attribution_policy_version]
  optional: [action_ref, qualifies_for_product_thesis, window_type,
             window_started_at, window_expires_at, evidence_refs]
idempotency: {key: attribution_id}
ordering: {scope: recommendation_id}
privacy:
  contains_personal_data: true
  data_mode: pseudonymous_identifiers_only
  contains_sensitive_values: false
  subject_linkability: internal
retention: {policy_ref: TBD}
source_of_truth: {aggregate: QualifiedActionAttribution}
legacy_names: [QualifiedActionAttributed]
notes: >
  `recommendation.action_attributed` — rejected alternative (RC §15):
  Recommendation context не объявляет сам, что внешнее действие
  принадлежит ему. action_category: engagement | booking_progression |
  transaction | service_outcome (owner ruling OQ-R4); qualified action
  начинается с booking progression; appointment_completed — candidate
  action_type до Appointment Contract (OQ-E3). attribution_type:
  direct | assisted; при недостатке доказуемой связи — unattributed
  (событием не публикуется). qualifies_for_product_thesis отделяет
  thesis-метрику от qualified action (минимальный сигнал —
  appointment_created; threshold — Killer PRD / Measurement Framework).
  Window values принадлежат Measurement Framework / versioned
  Attribution Window Registry (owner ruling OQ-R5): policy_version
  обязателен, применение перспективно, ретроактивная переклассификация
  запрещена. Правила (Killer PRD §6.2): временная близость недостаточна;
  не более одной winning recommendation; declined/invalidated
  recommendation не атрибутируется.
```

## 7. Pending Semantic Definition

**Resolved в v0.3.** Семейства `recommendation.*` и
`qualified_action.attributed` зарегистрированы (§6.5/§6.6) по
[[Ayla MVP Recommendation Contract]] v0.3 (architecture review —
APPROVED; owner rulings OQ-R): определены границы Recommendation
(immutable decision record + RecommendationSet), момент создания
(persistence), отличие generation от presentation, семантика
attribution, владение `recommendation_id` и attribution-событием,
влияние memory на ranking, lifecycle альтернатив.

Отклонённые имена (не используются, rejected alternatives — RC §15):
`recommendation.generated`, `recommendation.rejected`,
`recommendation.replaced`, `recommendation.action_attributed`.

На 2026-08-18 событий со статусом `pending-semantic-definition` в
реестре нет. `appointment.completed` зарегистрирован v0.5
(`semantic_status: defined` — normal completion path по
[[Ayla MVP Appointment Contract]] §5B, AYLA-DEC-0026); exception-path
evidence/correction authority остаётся pending с OQ-AC-3/OQ-AC-7
(см. OQ-E3). Незакрытая семантика, остающаяся в реестре: candidate
mappings семейства `memory.*` (§6.4, §11).

## 8. Ownership Matrix

| Event family | Authoritative owner | Разрешённый publisher | Статус |
|---|---|---|---|
| `intent.*` | Intent Resolution | Intent Resolver | active |
| `consent.*` | Consent / Authorization | Consent Service | active |
| `appointment.*` | Appointment | Appointment Service (CAP-011) | active (`appointment.rescheduled` — registered v0.4, AYLA-DEC-0022; `appointment.completed` — registered v0.5, AYLA-DEC-0026) |
| `memory.*` | Memory Service (W3) | Memory Service | active |
| `recommendation.*` — domain (created, superseded, expired, invalidated) | Recommendation | Recommendation Engine | active (v0.3, registered) |
| `recommendation.*` — interaction (presented, accepted, declined) | Channel Delivery / Interaction | Channel Adapter (MAX) | active (v0.3, registered) |
| `qualified_action.*` | Attribution / Measurement | Attribution Service | active (v0.3, registered) |

Инвариант (факт — AYLA-DEC-0025 п. 4): у события ровно один
authoritative owner. Consumers множественны, publishers — нет. Transport
relays (outbox publisher, broker adapter, CDC) не становятся
владельцами и обязаны сохранять canonical name, producer identity,
event_id, payload version, occurred_at. Вторичные семантические
producer'ы запрещены (аналитика не вправе решить, что запись
завершена).

## 9. Event Consumer Matrix

The matrix is intentionally expressed as roles until stable runtime `consumer_id` values are approved under OQ-E6.

| Event family | Producer | Consumers | Purpose |
|---|---|---|---|
| `appointment.*` | Appointment Service / CAP-011 | Notification, Journey/Screen Projection, Availability, Analytics, Attribution where registered | Synchronize committed appointment facts and derive read models |
| `consent.*` | Consent Service | Memory read gate, Audit, Analytics | Apply consent lifecycle and revocation effects |
| `intent.*` | Intent Resolver | Conversation Orchestration, Observability, Journey Projection | Carry approved intent-resolution facts/signals |
| `memory.*` | Memory Service | Conversation, Recommendation read gate, Audit, Analytics | Carry memory lifecycle facts under consent controls |
| `recommendation.*` | Recommendation Engine or Channel Adapter, according to event entry | Journey Projection, Booking, Attribution, Analytics, Audit | Track recommendation lifecycle and explicit interaction |
| `qualified_action.attributed` | Attribution Service | Analytics, Product Thesis Validation, Audit | Record measurement attribution |

Consumers may build projections, retries, notifications, analytics, or audit records. They may not republish the consumed fact as if they owned it or write the source aggregate directly.

## 10. Compatibility Policy

**Совместимые изменения** (без смены `event_version`):

- добавление optional-поля в payload;
- добавление нового enum-значения только при tolerant-reader policy;
- документационное уточнение без изменения семантики.

**Breaking changes** (требуют `event_version +1`, migration plan,
consumer matrix и deprecation window — факт, AYLA-DEC-0025 п. 6):

- переименование или удаление поля;
- изменение типа или meaning поля;
- смена authoritative owner;
- изменение обязательности поля;
- изменение ordering semantics;
- изменение семантики факта (в этом случае — новое событие или
  раздельные факты: `recommendation.dispatched` ≠
  `recommendation.displayed`).

Доменный producer публикует только canonical; legacy consumers
обслуживает compatibility layer; alias удаляется после миграции всех
зарегистрированных consumers.

## 11. Delivery Semantics (proposal)

Без привязки к брокеру (Kafka/RabbitMQ не предполагаются). Логические
гарантии:

- **at-least-once delivery** — потребитель обязан быть идемпотентным;
- **idempotent consumers** — дедупликация по `event_id` /
  `idempotency_key`;
- **no global ordering** — порядок гарантируется только в пределах
  declared aggregate key (`ordering.scope` записи);
- транзакционная публикация — через outbox или эквивалент (обязательность
  паттерна — OQ-E7).

## 12. Migration Mapping

Legacy-имена — только compatibility mapping, не допустимые новые имена
(факт — AYLA-DEC-0025 п. 2/6). Миграция потребителей **не выполняется**
до approval реестра.

| Legacy name | Источник | Canonical candidate | Статус |
|---|---|---|---|
| `ConsentGranted` | Roadmap §6.4, CDM §11 | `consent.granted` | ready after registry approval |
| `consent_granted` | CSR §9.1 (audit) | `consent.granted` (audit — проекция) | ready after registry approval |
| `ConsentRevoked` / `consent_revoked` | Roadmap §6.4, CSR §9.1 | `consent.revoked` | ready after registry approval |
| `ConsentDenied` / `consent_denied` | CDM §11, CSR §9.1 | `consent.denied` | candidate |
| `ConsentExpired` / `consent_expired` | CDM §11, CSR §9.1 | `consent.expired` | candidate |
| `IntentResolved` | Roadmap §6.4, CDM §11 | `intent.resolution_produced` | ready after registry approval |
| `IntentDetected` | CDM §11 | `intent.detected` (technical signal) | ready after registry approval |
| `IntentClarificationRequested` | CDM §11 | TBD (payload `resolution_status = needs_clarification`?) | blocked by semantic review |
| `IntentSuperseded` / `IntentExpired` | CDM §11 | `intent.superseded` / `intent.expired` | candidate |
| `IntentAbandoned` | CDM §11 | TBD | blocked by classification (CDM §24) |
| `IntentFulfilled` | CDM §11 | TBD (derived projection) | blocked by semantic review |
| `AppointmentCreated` | Roadmap §6.4 | `appointment.created` | ready after registry approval |
| `AppointmentRequested` | CDM §11 | TBD | semantic review required (ревью п. 2) |
| `AppointmentConfirmed` | Roadmap §6.4, CDM §11 | `appointment.confirmed` | ready after registry approval |
| `AppointmentCompleted` | Roadmap §6.4, CDM §11 | `appointment.completed` | registered v0.5 (AYLA-DEC-0026; exception path pending — OQ-E3) |
| `AppointmentCancelled` | Roadmap §6.4, CDM §11 | `appointment.cancelled` | ready after registry approval |
| `AppointmentRescheduled` | CDM §11 | `appointment.rescheduled` | ready after registry approval (registered v0.4, AYLA-DEC-0022) |
| `AppointmentRejected` / `AppointmentMarkedNoShow` | CDM §11 | `appointment.rejected` / `appointment.no_show` | candidate |
| `PendingAppointmentExpired` | CDM §11 | `pending_appointment.expired` (technical) | candidate |
| `ContextFactRecorded` | CDM §11 | `memory.entry_created` | candidate — semantic review |
| `ContextFactConfirmed` | CDM §11 | `memory.proposal_confirmed` | candidate — semantic review |
| `ContextFactCorrected` | Roadmap §6.4, CDM §11 | `memory.entry_superseded` | resolved mapping (AYLA-DEC-0024 п. 4) |
| `ContextFactDeleted` | CDM §11 | `memory.entry_revoked` / deletion pipeline | candidate — OQ-E4 |
| `RecommendationShown` | Roadmap §6.4 | `recommendation.presented` | mapped (v0.3, §6.5) |
| `RecommendationAccepted` | Roadmap §6.4 | `recommendation.accepted` | mapped (v0.3, §6.5) |
| `RecommendationCreated`…`RecommendationActedUpon` | CDM §11 | `recommendation.created` / `.presented` / `.accepted` / `.declined` / `.superseded` / `.expired` / `.invalidated`; `…ActedUpon` → `qualified_action.attributed` | mapped (v0.3, §6.5/§6.6) |
| `QualifiedActionAttributed` | Roadmap §6.4, CDM §11 | `qualified_action.attributed` | mapped (v0.3, §6.6) |
| `OutcomeRecorded` | CDM §11 | TBD | blocked by OQ-E3 (Stage 14) |
| `FeedbackSubmitted` | CDM §11 (deferred) | TBD | deferred |
| `booking.rescheduled` | runtime legacy | `appointment.rescheduled` | legacy alias (compatibility adapter; canonical зарегистрирован v0.4, AYLA-DEC-0022) |
| `booking.*` | runtime legacy | `appointment.*` | legacy alias (compatibility adapter) |

## 13. Open Questions

- **OQ-E1 (ЗАКРЫТ — v0.3).** MVP-состав `recommendation.*` определён
  [[Ayla MVP Recommendation Contract]] v0.3 (architecture review —
  APPROVED; owner ruling OQ-R2/R10, publication matrix RC §15):
  `recommendation.created`, `.superseded`, `.invalidated` — domain,
  cross_context, owner Recommendation; `recommendation.expired` —
  domain, internal; `recommendation.presented`, `.accepted`, `.declined`
  — interaction, cross_context, owner Channel Delivery / Interaction;
  `qualified_action.attributed` — attribution, cross_context, owner
  Attribution / Measurement. Все восемь зарегистрированы (§6.5/§6.6).
- **OQ-E2.** Какой authoritative aggregate для Context Fact correction —
  подтвердить, что Context Fact полностью представлен MemoryEntry
  (AYLA-DEC-0024) и конкурирующая сущность не нужна.
- **OQ-E3 (частично ЗАКРЫТ — v0.5).** Authoritative completion для
  Stage 14 определён: normal completion — zero-action happy path;
  producer — Appointment Domain через authoritative backend completion
  mechanism; deadline `scheduled_end + 3 hours`; commit-time exception
  check ([[Ayla MVP Appointment Contract]] §5A/§5B; регистрация —
  AYLA-DEC-0026); прохождение времени записи не является событием.
  Открытыми остаются: спор/no-show/исправимость (exception-path
  evidence и role authority — OQ-AC-3/OQ-AC-7/OQ-AC-18) и связь с
  `OutcomeRecorded`.
- **OQ-E4.** Какие события — integration (cross_context+), а какие
  остаются domain-only (internal): критерий — зарегистрированные
  consumers; кандидаты на пересмотр — семейство `memory.*`,
  `memory.entry_deleted` и lifecycle деактивации записи вне consent
  revocation (user_deleted, policy_changed, legal_erasure,
  tenant_deleted).
- **OQ-E5.** Retention policy для event log и audit (совместно с
  retention manifest по AYLA-DEC-0016 п. 7 и CSR §9 Audit Retention).
- **OQ-E6.** Порядок обновления consumer compatibility matrix
  (стабильный `consumer_id`, регистрация consumer, review).
- **OQ-E7.** Является ли transactional outbox обязательным runtime
  pattern для publication_scope ≥ cross_context.

## 14. Event vs Timeline

The registry is not an appointment timeline. An operational timeline is assembled from:

```text
Domain Events + Appointment Revision + permitted Audit Records
= Operational Timeline
```

A timeline is a consumer projection with its own visibility, freshness, and privacy rules. It must reference the source event/revision and must not invent a business fact when delivery is delayed, a command times out, or a provider sync fails.

## 15. Provider, failure, and privacy boundaries

- `formula_tela` is a pilot provider integration, not a global Ayla operational System of Record. Provider-originated signals require an explicit integration contract and reconciliation policy before they can produce an Ayla domain event.
- A provider sync success/failure, notification delivery result, timeout, retry, or API response is not an appointment success. A business event is emitted only after the authoritative domain state is committed.
- Event payloads are purpose-limited. Use pseudonymous identifiers and references by default; do not include semantic memory, hidden AI reasoning, data from another provider, or unnecessary sensitive values.
- AI may consume approved event projections. AI, channels, analytics, notification workers, and transport relays cannot publish Appointment, Consent, Availability, Payment, or Provider domain facts.

## 16. Validation Checklist

- [ ] Every domain event has exactly one authoritative owner and one authorized producer.
- [ ] Every domain event is emitted only after the owning state change is committed.
- [ ] Commands, API requests, tool invocations, retries, and notification results are not domain events.
- [ ] AI is never an authoritative producer of business facts.
- [ ] `appointment.created` means persisted Appointment creation, not a click, request, or confirmation.
- [ ] `appointment.confirmed` means authoritative confirmation.
- [ ] `appointment.no_show` remains proposed/incomplete until authority and evidence are decided.
- [ ] Event payloads respect tenant, consent, purpose limitation, and minimum disclosure.
- [ ] Projections, caches, analytics, audit, and timelines are not sources of truth.
- [ ] Delivery retries and duplicate delivery are handled by idempotent consumers.
- [ ] Provider-specific signals do not create a second Ayla Appointment truth.

## 17. Change Log

### v0.5 (2026-08-18) — Регистрация appointment.completed (OQ-E3 частично)

- **§6.3:** `appointment.completed` зарегистрирован
  (`registration_status: registered`, `semantic_status: defined`) по
  governance decision AYLA-DEC-0026 (accepted 2026-08-18) по прецеденту
  досрочной регистрации AYLA-DEC-0022 п. 9: семантика normal completion
  нормативно определена [[Ayla MVP Appointment Contract]] §5A/§5B
  (zero-action happy path; authoritative backend completion mechanism;
  `scheduled_end + 3 hours`; commit-time exception check;
  идемпотентность; UNKNOWN → readback/reconciliation).
- **§7/§8/§12/§13:** статусные ссылки обновлены; OQ-E3 частично закрыт —
  открыт только exception path (спор/no-show/исправимость —
  OQ-AC-3/OQ-AC-7/OQ-AC-18; связь с `OutcomeRecorded`).
- Статус документа не изменён: draft / proposed; остальные записи
  §6.1–§6.4 остаются `proposed` до approval реестра.

### v0.4 (2026-07-29) — Интеграция AYLA-DEC-0022 (Appointment Reschedule Model)

- **§6.3:** `appointment.rescheduled` зарегистрирован
  (`registration_status: registered`) — регистрация нормативно предписана
  AYLA-DEC-0022 п. 9 (accepted 2026-07-28): same-ID перенос с
  увеличением `version` и созданием AppointmentRevision; идемпотентность
  по `revision_id`; `tenant_id` не дублируется в payload (envelope,
  §4 п. 4); неизменные поля опускаются (стиль: отсутствие поля, не null).
- **Replacement-связка:** `appointment.created` дополнен lineage-полями
  (`reschedule_of`, `root_appointment_id`, `reschedule_count` — только
  при replacement); `appointment.cancelled` — поля `cancellation_reason`
  (первое зарегистрированное значение enum — `replaced_by_reschedule`,
  AYLA-DEC-0022 п. 3) и `replacement_appointment_id` (обязательно при
  replacement: оба id создаются до записи outbox, DEC-0022 п. 10).
- **Семейный инвариант §6.3:** reschedule — операция, не статус;
  `appointment.rescheduled` не публикуется при replacement и при
  pending Reschedule Proposal; cross-tenant `reschedule_of` запрещён;
  единственный producer — CAP-011 (AYLA-DEC-0022 п. 9, AYLA-DEC-0025
  п. 4).
- **§11:** `AppointmentRescheduled` → `appointment.rescheduled` —
  ready after registry approval; восстановлен explicit alias
  `booking.rescheduled` → `appointment.rescheduled` (в v0.2 alias
  указывал на незарегистрированное canonical — контрактная ошибка).
- **§1/§4:** основания дополнены AYLA-DEC-0022; правило 2 §4 —
  документировано исключение досрочной регистрации по accepted-решению.
- Статус документа не изменён: draft / proposed; остальные записи
  §6.1–§6.4 остаются `proposed` до approval реестра.

### v0.3 (2026-07-29) — Регистрация recommendation.* и qualified_action.attributed (OQ-E1)

- **§6.5 Recommendation (7 событий, `registered`):** `recommendation.created`
  (после persistence, не LLM generation), `.superseded` (оба id в payload),
  `.expired` (internal — read/action gate вместо integration delivery),
  `.invalidated` (cross_context; expired ≠ invalidated), `.presented`
  (owner Channel Delivery / Interaction, `delivery_ack_type`,
  `presented ≠ viewed`), `.accepted` (acceptance_action; ≠ booking
  completion), `.declined` (только явный отказ).
- **§6.6 Attribution:** `qualified_action.attributed` зарегистрировано,
  owner — Attribution / Measurement; `recommendation.action_attributed` —
  rejected alternative; `action_category` (engagement / booking_progression
  / transaction / service_outcome), `qualifies_for_product_thesis`,
  `attribution_type` (direct | assisted), обязательный
  `attribution_policy_version` (prospective; windows — Measurement
  Framework).
- **§7:** pending-семейства resolved; rejected-имена
  (`recommendation.generated`, `.rejected`, `.replaced`,
  `.action_attributed`) зафиксированы как неиспользуемые.
- **§8:** ownership matrix — Recommendation Engine (domain),
  Channel Adapter MAX (interaction), Attribution Service (attribution).
- **§11:** mapping `RecommendationShown` → `recommendation.presented`,
  `RecommendationAccepted` → `recommendation.accepted`, CDM-состав
  `RecommendationCreated…ActedUpon` → семейство §6.5/§6.6,
  `QualifiedActionAttributed` → `qualified_action.attributed`.
- **OQ-E1 закрыт.** Основание: [[Ayla MVP Recommendation Contract]] v0.3
  (architecture review APPROVED; owner rulings OQ-R1, R2/R10, R3, R4,
  R5, R6). Записи §6.1–§6.4 остаются `proposed` до approval реестра;
  статус документа не изменён: draft / proposed.

### v0.2 (2026-07-28) — Review correction (архитектурное ревью v0.1)

- **P0-1:** статусы разделены — `registration_status` (proposed до
  approval реестра; `registered` только после) и `semantic_status`
  (defined | incomplete | candidate | pending-semantic-definition);
  слово `registered` больше не используется до утверждения.
- **P0-2:** `appointment.created` — закреплён нормативный смысл
  (создание authoritative aggregate в локальном SoR со стартовым
  pending; ≠ принятие внешним booking authority, ≠ подтверждение);
  mapping `AppointmentRequested` → semantic review required.
- **P0-3:** `appointment.completed` — `semantic_status: incomplete` до
  Appointment Contract (OQ-E3 расширен: кто объявляет completion, спор,
  no-show, исправимость).
- **P0-4:** исправлено число memory-событий в Change Log v0.1 (8 → 7).
- **P0-5:** envelope: `primary_subject` + опциональные
  `related_subjects` вместо неоднозначного `subject`.
- **P1:** `tenant_id` удалён из event-specific payload (единственное
  место — envelope); `authorized_producer` (реестр) отделён от runtime
  `producer` (envelope); privacy-классификация детализирована
  (псевдонимные идентификаторы = personal data,
  `pseudonymous_identifiers_only`); идемпотентность memory-событий
  нормализована (бизнес-ключи `proposal_id`/`memory_id`;
  `source_event_id` — deduplication при наличии);
  `memory.proposal_confirmed` отделён от `memory.entry_created`
  (атомарный коммит, два факта); `memory.entry_revoked` — только
  следствие consent.revoked (`revocation_event_id` обязателен);
  `primary_intent_type` — условная обязательность (при `resolved`);
  `revocation_mode` — обязателен; иерархия publication_scope
  формализована; схема consumers предусматривает стабильный
  `consumer_id` (после OQ-E6); примечание `appointment.cancelled`
  освобождено от attribution-семантики; `proposal_confidence` определён
  (non-authoritative); `policy_migration` — candidate reason;
  инвариант детерминированного expiry добавлен; `intent.detected` —
  `aggregate: null` + флаги `contract_visibility` /
  `integration_allowed`.
- Статус документа не изменён: draft / proposed. Approval — после
  MVP Recommendation Contract и повторного ревью.

### v0.1 (2026-07-28) — Initial draft

- Реестр создан по мандату AYLA-DEC-0025 п. 1: назначение, границы
  классов, naming convention, Event Record Schema, общий envelope,
  Ownership Matrix, Compatibility Policy, Delivery Semantics (proposal),
  Migration Mapping, Open Questions OQ-E1..E7.
- Зарегистрированы только события с определённой семантикой:
  `intent.resolution_produced`, `intent.detected` (technical_signal /
  internal), `consent.granted`, `consent.revoked`, `appointment.created /
  confirmed / completed / cancelled`, семейство `memory.*` (7 событий,
  publication internal по умолчанию).
- `recommendation.*` и `qualified_action.attributed` — pending semantic
  definition (§7), не зарегистрированы.
- CDM §11 использован как источник legacy-состава; синхронизация CDM и
  CSR §9.1 с каноном — отдельный Change Control.
- Статус: draft / proposed; миграция потребителей не выполняется до
  approval реестра.
