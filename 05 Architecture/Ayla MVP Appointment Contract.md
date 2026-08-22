---
node_id: ayla.architecture.mvp-appointment-contract
title: Ayla MVP Appointment Contract
type: specification
status: draft
decision_status: proposed
version: "1.1-draft"
owner: Product Architecture
owners:
  - Product Architecture
  - Product Owner
  - Domain Architecture
knowledge_area:
  - architecture
  - product
domain:
  - booking
system_owner:
  - shared
source_repository: ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: medium
data_categories:
  - pii
security_sensitivity: medium
ai_indexing: allowed
export_policy: sanitized
created: 2026-07-29
updated: 2026-08-17
review_cycle: monthly
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Ayla Glossary]]"
  - "[[Ayla Decision Log]]"
  - "[[Ayla MVP Scope and Release Contract]]"
  - "[[Ayla Single-Provider Technical Pilot Execution Scope]]"
  - "[[Ayla Multi-Provider Product Validation Execution Scope]]"
  - "[[Ayla Repository Responsibility Matrix]]"
  - "[[Ayla Domain Context Map]]"
  - "[[Ayla Core Domain Model Specification]]"
  - "[[Ayla Domain Event Registry]]"
  - "[[Consent Scope Registry]]"
  - "[[Data Inventory Matrix]]"
related:
  - "[[Ayla Transaction State Model]]"
  - "[[Ayla MVP User Journey Specification]]"
---

# Ayla MVP Appointment Contract

> Статус: **Draft / Proposed**.
>
> Этот документ расширяет `Ayla Repository Responsibility Matrix` для Appointment.
> Он не утверждает нерешённые owner decisions и не заменяет Domain Event Registry,
> Consent Scope Registry, API contracts или UI screen contracts.

## 1. Purpose

Этот контракт определяет минимальное каноническое значение Appointment для MVP и
общие правила его жизненного цикла. Документ используется как основание для Salon
Operations MVP, Master/Admin UX, Screen Data Contracts, Domain Event Registry,
Backend API contracts и AI tool contracts.

Контракт предотвращает смешение доменного состояния, состояния интеграционной
транзакции, отображения экрана, разговора и результата AI-вызова. Техническая
реализация может находиться в конкретном repository, но не становится каноном
только потому, что существует модель, endpoint или legacy payload.

## 2. Appointment Definition

Appointment — доменный объект, представляющий согласованную запись, связанную с
customer, provider/tenant, услугой, исполнителем и временным интервалом. Appointment
имеет собственный lifecycle и audit history.

Appointment не является:

- Recommendation;
- Availability или Slot;
- Conversation;
- Payment;
- Calendar Event;
- provider-specific raw record;
- UI screen state;
- AI hypothesis.

### 2.1. Separate representations

| Representation | Meaning | Authority |
|---|---|---|
| Domain Contract | Appointment, invariants, lifecycle, commands | Appointment Domain |
| Implementation | module, service, database model, adapter | конкретный repository; не доказывает ownership |
| API Representation | request/response DTO and errors | API contract owner; операция принадлежит Appointment Domain |
| UI Projection | screen model and UI states | client/channel; не владеет Appointment |
| AI Tool Representation | schema for proposing/invoking a command | tool adapter; не содержит полного business policy |
| External Provider Representation | provider-local record/status/reference | Provider integration boundary |

### 2.2. Fact versus operation state

| Layer | Examples | Rule |
|---|---|---|
| Appointment lifecycle | `requested`, `pending_confirmation`, `confirmed`, `cancelled`, `completed`,
o_show`, `rejected`, `expired` | domain state; owner performs transitions |
| Operation/transaction | `initiated`, `pending`, `confirmed`, `failed`, `expired`, `cancelled` | result of a command; not automatically Appointment state |
| Integration synchronization | `fresh`, `stale`, `uncertain`, `quarantined` | provider exchange state; not lifecycle |
| UI state | `loading`, `success`, `error`, `unknown` | projection state; not business fact |

`failed`, `timeout`, `HTTP 201`, tool acknowledgement или отсутствие ошибки сети
сами по себе не являются подтверждением Appointment.

## 3. Ownership and Source of Truth

**Appointment Domain owns the Appointment lifecycle.** Это domain ownership, а не
утверждение о repository, database или физической таблице.

`beautygo_backend` — **Proposed** operational transactional SoR для Appointment и
связанного operational booking state согласно `OD-RRM-1`. До принятия owner decision
это не считается утверждённым фактом.

Внешний provider может быть authoritative source для provider-local calendar facts
в пилоте. Это не создаёт второго Ayla Appointment SoR. Provider data входит в Ayla
через integration contract и нормализуется в Appointment или в именованную
projection.

| Question | Contract answer |
|---|---|
| Domain lifecycle owner | Appointment Domain |
| Proposed transactional repository | `beautygo_backend` |
| Authoritative physical model/table | Pending physical implementation decision |
| Runtime storage location | Must be defined by implementation contract |
| Can a projection become SoR? | No |
| Can provider raw state become Ayla Appointment by implication? | No |

## 4. Domain Model

### 4.1. Appointment and related entities

| Entity | Appointment relationship | Appointment owns it? |
|---|---|---|
| Provider | provider reference and boundary | No |
| Tenant | tenant scope for authorization | No |
| Customer/Subject | participant reference | No |
| Specialist Membership | role/membership reference | No |
| Specialist Assignment | selected service-specific assignment | No |
| Service Offering | selected offering reference and snapshots | No |
| Availability | source for valid interval | No |
| Slot Hold | temporary predecessor/coordination state | No |
| Payment | separate payment boundary | No |
| Consent | separate authorization boundary | No |
| Recommendation | optional source/attribution reference | No |

### 4.2. Candidate attributes

Field names and serialization are not final API commitments until API contract
acceptance.

| Attribute | Meaning | Status |
|---|---|---|
| `appointment_id` | stable identity | Proposed, based on Core Domain Model |
| `tenant_id` | tenant scope | Proposed |
| `provider_id` | provider reference | Proposed |
| `subject_id` / customer reference | customer subject | `subject_id` is canonical candidate; API mapping pending |
| `service_offering_id` | selected offering | Proposed, based on AYLA-DEC-0020 |
| specialist assignment reference | selected performer assignment | Proposed; exact field name pending |
| `start_time`, `end_time`, `timezone` | scheduled interval | Proposed |
| `status` | Appointment lifecycle state | Proposed |
| `origin` | source/channel/actor class | Proposed |
| `price_snapshot` | booking-time price | Proposed; payment remains separate |
| `duration_snapshot` | booking-time duration | Proposed |
| `version` | concurrency/version value | Proposed |
| `created_at` | creation timestamp | Proposed |
| revision/lineage references | same-ID revision or replacement history | Proposed, based on AYLA-DEC-0022 |
| external reference | provider id and sync metadata | Proposed; never sole Ayla identity |

## 5. Lifecycle Model

Core Domain Model uses `requested` as the starting-state candidate; event/transaction
materials also use `pending`/`pending_confirmation`. Until owner alignment, this
contract records the gap instead of presenting two independently approved states.

```text
requested -> pending_confirmation -> confirmed -> completed
    |              |                    |
    v              v                    v
 rejected        expired             cancelled / no_show
```

Rules:

- `requested` is the Core Domain starting-state candidate;
- `pending_confirmation` is the provider-confirmation phase candidate;
- `confirmed` requires authoritative confirmation;
- `completed` via normal completion is zero-action and requires no evidence (§5A, §5B); evidence applies only to the correction/exception path (§7);
- normal completion is the owner-approved zero-action outcome after the resolution deadline, but only when the authoritative Appointment lifecycle mechanism confirms that no exception was registered;
- a client-side timer, elapsed local time, or UI refresh is never completion evidence or an authoritative state change;
- `cancelled`, `rejected`, `expired` and
o_show` are distinct outcomes;
- `rescheduled` is not a domain state;
- `failed` is a command/transaction result, not an Appointment state;
- timeout is `unknown`/`uncertain` until reconciliation and must not be reported as
  success.

Canonical state naming and the exact initial transition are `OQ-AC-1`.

## 5A. Owner-Approved Post-Visit Resolution Window

After authoritative scheduled_end, every Appointment enters a POST-VISIT
RESOLUTION WINDOW of three hours.

resolution_window_start = authoritative scheduled_end
resolution_window_duration = 3 hours
resolution_deadline = scheduled_end + 3 hours

The window does not begin at screen open, button press, refresh, app resume,
conversation time, or a local device timer. The mobile client is not the
completion scheduler.

Normal completion is the zero-action happy path. The master is not required to
press Complete, Завершить визит, Визит состоялся, or an equivalent action. If no
lifecycle exception is authoritatively registered before the deadline, the
Appointment reaches normal completed through the authoritative mechanism after
the deadline.

An exception registered before the deadline prevents blind normal completion.
Deadline expiry does not erase or resolve an existing exception. Further
resolution belongs to the applicable canonical lifecycle/process owner.

For Master MVP, Клиент не пришёл reuses existing no_show /
appointment.no_show semantics only where authority, evidence, permissions, and
the Event Registry permit it. This decision grants no new master authority.
Customer intent Визит не состоялся reuses an existing canonical mechanism if one
exists; otherwise its command/outcome remains a dependency.

Feedback/review is not an Appointment lifecycle outcome. Rating, quality
complaint, or other feedback does not itself become a lifecycle exception.

MASTER-REPORTED NON-DELIVERY AFTER CUSTOMER ARRIVAL remains unresolved. Until a
separate owner decision, do not classify it as no_show, normal completed, or a
new status, event, command, or Master action.

Producer/scheduler, deadline-race ordering and the evidence/correction boundary
for normal completion are defined in §5B. Customer-side command/outcome
semantics remain a dependency (OQ-AC-17). Existing version, idempotency,
pending/unknown, and authoritative-readback rules apply.

## 5B. Authoritative Completion Runtime

Этот раздел фиксирует runtime-семантику авторитетного нормального завершения
(normal completion) для owner-approved post-visit resolution window из §5A. Он
не вводит новых статусов, lifecycle events, команд или completion states.

**Producer.** Normal completion производится Appointment Domain через
авторитетный backend completion mechanism: scheduled job/worker внутри
transactional SoR, по существующему backend scheduled-job паттерну `purge_job`
(daily Celery cron) из
[[AMD-001 C5 Pilot Personal Context Export-Forget Contract]] и
[[AMD-020 C5 Implementation Amendment]]. Точный компонент —
engineering detail и каноном не фиксируется; физический SoR `beautygo_backend`
остаётся **Proposed** по OD-RRM-1. Продюсером НЕ являются mobile client,
Ayla / conversation runtime, projection, presentation layer или local device
timer. Mobile UI не является scheduler; local timer никогда не создаёт domain
completion; UI не создаёт Completed.

**Deadline.** `completion_deadline = scheduled_end + 3 hours`. Значение
хранится и сравнивается в UTC согласно AYLA-DEC-0021 п.5; timezone snapshot
записи управляет только отображением. Окно никогда не стартует от screen open,
button press, refresh, app resume, conversation time или local device timer.

**Deadline race.** Normal completion может закоммититься, только если на
authoritative commit boundary не зарегистрирован lifecycle exception,
блокирующий normal completion. Проверка переоценивается at commit time (а не
at job schedule time) внутри одного transactional commit с использованием
существующих примитивов: aggregate `version` / expected-version, deterministic
ordering (§16) и idempotency keys (§23). Exception, зарегистрированный до
completion commit, выигрывает. Уже закоммиченное completion не отменяется
молча поздним exception — только через correction path (ниже и §7).

**Idempotency.** Повторный запуск scheduler/job не создаёт duplicate
completion. Завершение уже `completed` записи — no-op success: без второго
transition и без duplicate `appointment.completed` event; retries безопасны
(§23).

**Unknown.** При runtime/transport uncertainty `UNKNOWN ≠ SUCCESS ≠ CONFIRMED
FAILURE`. Job обязан выполнить authoritative readback / reconciliation из SoR
до retry; blind duplicate completion запрещён (выравнено с §29 и RRM §11).

**Evidence / correction (минимальная граница для Controlled Pilot).** Normal
completion не требует evidence — это zero-action happy path. Коррекция
ошибочно завершённой записи выполняется ТОЛЬКО через авторизованный correction
path Appointment Domain (`CompleteAppointment` correction/exception path, §7)
с current state, version, authority, evidence и audit, в границах авторитета
[[Ayla Master MVP Auth and Authority Contract]]. Direct edit, silent mutation
и history rewrite запрещены. Этот контракт НЕ создаёт dispute subsystem,
support ticketing, customer arbitration или refund workflow. Role authority
для completion/no-show marks остаётся deferred (OQ-AC-7).

## 6. State Transition Rules

| From | Action | To | Actor/producer | Conditions |
|---|---|---|---|---|
| absent | `CreateAppointment` | `requested` or `pending_confirmation` | Appointment Domain via backend | identity, tenant, offering, assignment, slot/hold and applicable consent gates |
| requested | provider confirmation | `confirmed` | authoritative Appointment/booking boundary | acceptance verified; no stale/conflicting slot |
| requested/pending_confirmation | provider rejection | `rejected` or failed transaction | authoritative owner | reason code; mapping is `OQ-AC-2` |
| requested/pending_confirmation | hold/request TTL expires | `expired` | authoritative owner | expiry verified |
| requested/pending_confirmation/confirmed | `CancelAppointment` | `cancelled` | owner after authorization | actor, reason and audit required |
| confirmed | authoritative normal completion after resolution deadline | completed | Appointment Domain via authoritative completion mechanism | scheduled_end + 3 hours and no exception before deadline |
o_show` | pending owner decision | party and evidence required |
| confirmed | same-ID `RescheduleAppointment` | confirmed new revision | Appointment Domain via backend | same meaning; version and slot checks pass |
| confirmed | replacement | old lineage terminal/new Appointment | Appointment Domain via backend | changed business boundary |
| any | failed command/timeout | unchanged or transaction failure | authoritative owner | original Appointment unchanged unless owner confirms transition |

No transition is performed by a client, conversation runtime, projection consumer or
AI tool directly.

## 7. Canonical Commands

Commands request a domain operation. They are not events and do not prove that the
requested state was reached.

| Command | Actor(s) | Permission boundary | Minimum validation | Result |
|---|---|---|---|---|
| `CreateAppointment` | Customer, Admin/Owner, Ayla on behalf of authorized customer | subject/tenant scope | identity, offering, assignment, slot/hold, consent and idempotency | aggregate or explicit failure |
| `ConfirmAppointment` | authoritative booking/provider boundary | owner-only commit | provider/SoR confirmation and version | `confirmed` or unknown/failure |
| `RescheduleAppointment` | Customer, Admin/Owner, Ayla as proposer | authorization and ownership/role checks | version, new slot, policy, same-ID/replacement classification | revision or replacement |
| `ReplaceAppointment` | Admin/Owner or authorized operational actor | policy and tenant scope | changed service/price/payment/consent boundary | new lineage record |
| `CancelAppointment` | Customer, Master/Provider, Admin/Owner subject to policy | ownership/membership/policy | current state, reason, idempotency | `cancelled` or failure |
| `CompleteAppointment` | optional correction/exception path only where canonical policy authorizes it | owner-only | current state, version, authority, evidence and audit | `completed` or pending/unknown; not required for normal visits |
| `MarkNoShow` | authority pending decision | owner-only | confirmed source, party and evidence |
o_show` or failure |

API endpoints and AI tools forward these commands; they do not create a second
lifecycle or business rule set.

## 8. Reschedule Rules

### 8.1. Same-ID reschedule

Same-ID reschedule applies when service meaning, offering/business identity, price
boundary, duration meaning, payment boundary and consent boundary remain the same.
It keeps `appointment_id`, increments `version`, writes an immutable revision/audit
record and emits the registered reschedule event after the authoritative write.

Wave 1 explicitly prohibits implementing this as
`cancel_then_create_new_booking`.

### 8.2. Replacement

Replacement applies when service offering, price, duration meaning, payment
boundary, consent boundary or other business meaning changes. Lineage and terminal
mapping follow AYLA-DEC-0022 and are not redefined here.

### 8.3. Failure

If validation, slot reservation, provider call or version check fails, the original
Appointment remains unchanged. Timeout is not successful reschedule.

## 9. Cancellation Rules

Cancellation changes lifecycle and preserves history. It does not delete the domain
record. Subject to privacy/retention policy, retain actor class, reason code,
timestamp, affected version, external reference and correlation/idempotency key.

Late-cancellation policy, grace periods, fees and refund behavior require separate
owner decisions. Payment/refund state is never inferred from `cancelled`.

## 10. Manual Booking / Admin Booking

Manual salon/admin booking uses the same Appointment Domain and lifecycle as customer
booking. It differs by `origin`, actor and authorization context.

This contract does not introduce `OfflineAppointment`, `ManualAppointment` or a second
booking aggregate. Offline operation may have an integration/transaction state, but
its reconciliation path must be explicit before success is claimed.

## 11. Master Operations

Master/Provider may receive a purpose-limited operational projection of authorized
Appointments: today/upcoming schedule, detail, service, time, permitted customer
identifier and operational status.

View is in provider/tenant scope. Request reschedule/change, complete, no-show and
cancel are capability candidates with role and owner decision gates. Specialist
direct cancellation, reschedule, completion and no-show authority are not silently
granted here.

## 12. Admin Operations

Admin/Owner may be allowed to create, move/reschedule, cancel, assign/reassign a
specialist and resolve integration/data conflicts. Every action requires tenant
membership, explicit permission, audit and domain validation. Admin is not a bypass
around Appointment invariants. Override semantics are `OQ-AC-4`.

## 13. Customer Operations

Customer may, within subject and authorization boundary, create, view, reschedule
and cancel an Appointment and confirm a flow step when the flow requires it.
Customer cannot mark service completed or no-show by merely asserting it in a
conversation; these facts require the accepted authority model.

## 14. Ayla Interaction Model

```text
User request
  -> Ayla interpretation
  -> approved context and permission checks
  -> command proposal
  -> domain command/tool adapter
  -> backend/SoR validation
  -> transactional write by owner
  -> domain event
  -> projection refresh
  -> user response
```

```text
intent understood != command accepted != Appointment persisted
Appointment persisted != provider confirmed
provider confirmed != service completed
tool returned != business success
```

AI may understand, propose and invoke an approved adapter. AI must not write
Appointment storage, assign authoritative status, fabricate confirmation or publish
`appointment.*` events.

## 15. Availability and Slot Hold

Availability is a separate capability. Slot is a computed/read model of bookable time;
Slot Hold is temporary coordination state; neither is a confirmed Appointment.

```text
Availability rules/blocks -> slot projection -> Slot Hold
  -> domain validation and transaction -> Appointment
```

Implementation must recheck freshness/conflicts at commit and prevent overlapping
confirmed reservations. Hold TTL, release and reconciliation follow AYLA-DEC-0021.
This contract does not create a second availability SoR.

## 16. Concurrency and Idempotency

The implementation must provide, subject to backend contract:

- aggregate `version` / expected-version validation;
- idempotency for create, cancel and retryable commands;
- duplicate-command detection;
- race-safe interval conflict handling and double-booking protection;
- deterministic recovery after provider timeout;
- correlation between command, write, event and projection;
- deterministic ordering at the scheduled_end + 3 hours boundary, including exception/completion races.

Retries must not create a second Appointment or duplicate business fact. Exact key
and storage mechanism are implementation decisions.

## 17. Permissions Matrix

`P` = may propose/request; `C` = may issue an authorized command; `W` = may perform
authoritative write. `W` remains restricted to the domain owner.

| Action | Customer | Master | Admin | Owner | Ayla |
|---|---:|---:|---:|---:|---:|
| View authorized Appointment | C | C | C | C | C |
| Create Appointment | C | P | C | C | P/C via authorized flow |
| Confirm Appointment | P | P | P | P | — |
| Request reschedule | C | P | C | C | P/C via authorized flow |
| Authoritative reschedule write | — | — | — | — | — |
| Cancel | C | P | C | C | P/C via authorized flow |
| Complete / correction | P | P | P | P | — |
| Mark no-show | P | P | P | P | — |

The empty authoritative-write row is intentional: the role-facing channel does not
write the aggregate directly. Completion/no-show and specialist write authority are
`Pending owner decision`.

## 18. Events

Only the owner of the fact emits a domain event after authoritative state change.
Domain Event Registry remains the registry of names, schemas and semantic status.

| Event | Producer | When emitted | Consumers | Payload purpose |
|---|---|---|---|---|
| `appointment.created` | Appointment Domain / proposed backend SoR | aggregate created | channels, notifications, analytics, projections | created identity; not external confirmation |
| `appointment.confirmed` | Appointment Domain / confirmation boundary | provider/SoR confirmation accepted | channels, projections, notifications | confirmed state |
| `appointment.cancelled` | Appointment Domain | cancellation committed | channels, projections, audit | cancellation fact/reason |
| `appointment.rescheduled` | Appointment Domain | same-ID revision committed | channels, projections, audit | registered reschedule fact |
| `appointment.completed` | Appointment Domain via authoritative completion mechanism (§5B) | completion committed | outcome/analytics/projections | normal completion semantics defined by §5B; registration wording reconciled in Domain Event Registry; exception-path evidence semantics remain pending |
| `appointment.rejected` | Appointment Domain | rejection accepted | channels/projections | candidate; semantics pending |
| `appointment.no_show` | Appointment Domain | no-show accepted | channels/projections/analytics | candidate; party/authority pending |

Tool invocation, API response, webhook receipt, timeout and notification delivery
are not domain events. Consumer cannot publish `appointment.created` because it
called a tool or observed a projection.

## 19. Screen Projection Requirements

Each screen uses a named projection with source, freshness and error policy. Screen
models do not become Appointment state.

| Screen | Domain data | Projection data | UI-only state |
|---|---|---|---|
| Master Today | id, time, service, specialist, operational status | provider-scoped list, freshness, sync qualifier, permitted customer label | filter, loading, empty, retry |
| Appointment Detail | identity, interval, offering, lifecycle, revision | role-filtered detail, allowed actions, external sync qualifier | modal, optimistic disabled state, toast |
| Admin Calendar | appointments and availability references | tenant calendar, conflicts, freshness indicators | date range, filters, drag state |
| Customer Appointment | identity, time, provider, service, lifecycle | customer-safe details, next action, confirmation certainty | loading, error, unknown, success presentation |

No screen displays success from a tool acknowledgement alone. If a backend write
succeeded but the success screen failed to render, the client re-reads the
authoritative projection and may display `unknown` during reconciliation.


## 20. Operational Appointment Projections

Projection is not a Domain Entity and never becomes Source of Truth.

```text
Appointment
    ↓
Operational Projection
    ↓
Screen DTO
    ↓
UI
```

Every projection must declare `source_system`, `source_entity`, `freshness`,
`version` and the policy for unknown or stale data.

### 20.1. Master Today Projection

| Domain data | Projection data | UI-only state |
|---|---|---|
| `appointment_id`, time range, service name, duration, operational customer name, status, specialist | allowed actions, notes availability, exception flags, source/freshness/version | loading, filters, empty state, retry state |

Customer identity and actions are filtered by tenant, role and privacy scope. Notes
availability does not imply access to note content.

### 20.2. Admin Calendar Projection

The projection may combine appointments, availability, schedule blocks, assignments,
conflicts, unresolved items and sync state. It is an operational calendar view and
is not a Source of Truth. Every change goes through a command owned by the relevant
domain.

### 20.3. Customer Appointment Projection

Contains customer-safe service, provider, specialist, time, status, allowed customer
actions and confirmation state. It must not contain semantic memory, AI reasoning or
hidden recommendation context.

## 21. Appointment Operational Exceptions

`Operational Exception` is a separate operational model or signal. It is not an
Appointment status and does not change lifecycle by itself.

| Exception | Purpose | Owner | Visibility | Lifecycle effect |
|---|---|---|---|---|
| `customer_late` | record possible customer lateness | Pending owner decision | provider/master; customer policy-dependent | does not automatically cancel |
| `master_late` | record specialist delay | Pending owner decision | provider/master; customer policy-dependent | does not automatically cancel |
| `master_absent` | signal specialist absence | Pending owner decision | provider/admin; customer-safe projection by policy | does not mean `cancelled` |
| `equipment_unavailable` | record operational resource issue | Pending owner decision | provider/admin | requires resolution; lifecycle unchanged |
|
eeds_reassignment` | indicate a new assignment is needed | Pending owner decision | provider/admin | does not mean cancellation |
| `provider_sync_issue` | record integration synchronization issue | integration boundary | provider/admin; customer-safe qualifier | status is not inferred from sync failure |
| `payment_issue` | record separate payment capability issue | Payment boundary | minimum-necessary roles | status is not inferred automatically |

An exception requires its own identity, source, timestamp, resolution state and audit
semantics in a separate operational contract. Canonical owner and storage remain open.

## 22. Extended Permission Model

`READ` exposes permitted data; `PROPOSE` forms a suggestion; `COMMAND` submits a
validated command; `WRITE` performs the authoritative domain write. `WRITE` belongs
to the Appointment Domain and is not granted to AI, screens, projections or ordinary
roles directly.

| Action | Read | Propose | Command | Write |
|---|---|---|---|---|
| View appointment | Customer/Master/Admin/Owner/Ayla within scope | — | — | Appointment Domain only |
| Create | Customer/Master/Admin/Owner/Ayla context | Customer/Master/Ayla | authorized Customer/Admin/Owner | Appointment Domain |
| Reschedule | authorized roles | Customer/Master/Ayla | authorized Customer/Admin/Owner | Appointment Domain |
| Cancel | authorized roles | Customer/Master/Ayla | policy-authorized actor | Appointment Domain |
| Complete / correction | P | P | P | P | — |
| No-show | authorized operational roles | Master/Admin/Owner | authority pending | Appointment Domain |
| Reassign | provider/admin operational roles | Master/Admin/Owner | authority pending | Appointment Domain / assignment owner pending |

The earlier role matrix remains a channel-facing view. A `COMMAND` permission never
bypasses domain validation, tenant scope, consent or version checks.

## 23. Idempotency Contract

For retryable commands, effective identity is command semantics plus idempotency key:

```text
same command + same idempotency key = same business result
```

| Command | Required behavior |
|---|---|
| `CreateAppointment` | duplicate click or retry returns the original result or same in-flight/unknown outcome; never creates a second business Appointment |
| `CancelAppointment` | repeated cancellation with the same key is stable; no duplicate cancellation fact |
| `RescheduleAppointment` | repeated request with the same key returns the original revision/result; no second revision |

The key is scoped to actor, tenant and command boundary, retained for an
implementation-defined replay window, and correlated with command, write, event and
projection. Reusing a key with a different payload is a conflict. Exact key format,
replay TTL and storage are pending backend contract decisions.

This covers double-clicks, mobile retries and retries after timeout. Timeout remains
unknown until reconciliation and does not authorize a blind second write.

## 24. Appointment Timeline Model

Timeline is not lifecycle. Lifecycle is current domain state; timeline is a
role-filtered chronological view assembled from `AppointmentRevision`, Domain Events
and permitted Audit Records.

```text
10:00 Created → 10:02 Confirmed → 12 Aug Rescheduled
→ 13 Aug Specialist Changed → 14 Aug Completed
```

| Audience | Visible | Hidden or restricted |
|---|---|---|
| Customer | customer-relevant creation, confirmation, move, cancellation and outcome | internal reasons, audit metadata, hidden recommendation context |
| Master/Provider | operational changes relevant to assigned work | unrelated provider history, AI hypotheses, restricted PII |
| Admin/Owner | tenant-scoped operational timeline and audit subject to governance | data outside tenant, permission or consent scope |
| AI | approved, purpose-limited context only | raw audit, hidden reasoning, semantic memory unless separately governed |

Entries preserve source, timestamp, actor class, correlation and visibility policy.
A projection consumer cannot fabricate a domain timeline event.

## 25. Operational Notes Model

Do not add an unrestricted `Appointment.notes` field. Use a separate `Operational
Note` model or capability with explicit purpose and visibility.

| Field | Meaning | Status |
|---|---|---|
|
ote_id` | note identity | Proposed |
| `appointment_id` | related Appointment | Proposed |
| `author` | actor identity or class | Proposed; privacy mapping pending |
| `purpose` | operational reason | Proposed |
| `visibility` | audience policy | Proposed |
| `created_at` | creation time | Proposed |
| `content` | note body | Proposed; retention/redaction pending |

Allowed visibility values are `customer_visible`, `provider_visible`, `internal_only`
and `ai_unavailable`. Visibility is an access policy, not a client-controlled display
flag. Notes are not semantic memory and cannot contain hidden AI hypotheses or
unrestricted health data. Ownership, storage, editing, retention and event semantics
require a separate contract.

## 26. Customer Arrival / Check-in Boundary

Customer arrival is a separate capability boundary: `Customer Arrival Event` or
`Check-in capability`. This contract does not add `checked_in` to Appointment status
without an owner decision.

```text
arrival ≠ completed
arrival signal ≠ Appointment lifecycle transition
```

An arrival signal may be an operational qualifier or future check-in workflow input.
Its producer, evidence, deduplication, visibility, canonical event name and effect on
completion remain open (`OQ-AC-12`). No `customer_arrived` canonical event is
introduced here.

## 27. Schedule Influence Model

Schedule influences availability; availability produces bookable slots; Appointment
is created only after domain validation and commit:

```text
Master schedule
      ↓
Availability calculation
      ↓
Bookable slots / Slot Hold
      ↓
Appointment command and commit
```

Time off, schedule changes, reassignment and membership revocation can invalidate a
future slot or require revalidation. They do not rewrite an Appointment without the
relevant domain command and policy. Schedule and availability ownership remains
separate or pending where sources do not decide it. This extends AYLA-DEC-0021 and
does not create a new SoR.
## 28. Privacy Boundary

Master/Admin and provider systems receive only a purpose-limited operational
projection required for salon operations and permitted by consent, role and tenant
scope.

The Appointment contract does not authorize exposure of semantic memory, AI
hypotheses, other-provider history, hidden recommendation reasoning, full
conversation/memory context or unrelated health/wellness data.

Consent and data-access gates are governed by Consent Scope Registry and Data
Inventory Matrix, not by a client or AI tool. Event payloads use minimum necessary
and pseudonymous identifiers where possible.

## 29. Failure Semantics

| Situation | Business meaning | Required behavior |
|---|---|---|
| provider timeout | unknown result | no confirmed/success; reconcile with SoR |
| tool validation failure | command not executed | recoverable failure; no Appointment event |
| slot conflict | booking not committed | existing Appointment unchanged; reason/recovery |
| expired hold | proposed booking invalid | no confirmation; request new slot |
| consent unknown/unavailable | authorization not established | fail closed |
| HTTP 201 without confirmation projection | write/presentation split | re-read SoR; display unknown until known |
| duplicate retry | same operation repeated | idempotent result; no duplicate aggregate/event |
| provider data stale | projection unsafe for decision | stale/degraded; fresh validation required |
| notification failure after write | delivery failed after business write | do not silently roll back; expose delivery separately |

Integration failure is never business-operation success. Notification failure does
not erase an already committed Appointment.

## 30. Open Questions and Owner Decisions

| ID | Question/decision | Status |
|---|---|---|
| OQ-AC-1 | Canonical naming/order of `requested` vs `pending_confirmation` | Open question |
| OQ-AC-2 | Exact semantics/reason codes for `appointment.rejected` | Open question |
| OQ-AC-3 | Evidence and correction rules for completion | Normal-completion leg RESOLVED BY CANON (§5B: zero-action, no evidence required; correction boundary fixed via §7 authorized path); exception-path evidence and role authority leg stays pending with OQ-AC-7 |
| OQ-AC-4 | Admin override scope and audit requirements | Pending owner decision |
| OQ-AC-5 | Specialist direct cancellation authority | Pending owner decision |
| OQ-AC-6 | Specialist direct reschedule authority | Pending owner decision |
| OQ-AC-7 | Completion and no-show authority by role | Pending owner decision |
| OQ-AC-8 | Customer PII allowed in provider/master projections | Pending privacy/owner decision |
| OQ-AC-9 | Late cancellation policy, grace period and fees | Open question; payment excluded |
| OQ-AC-10 | Provider-local confirmation/completion mapping | Open integration question |
| OQ-AC-11 | Backend API, event wire schema and idempotency key | Pending contract work |
| OQ-AC-12 | Customer arrival/check-in producer, evidence, canonical event and lifecycle effect | Open question |
| OQ-AC-13 | Operational Exception owner, storage, resolution and event semantics | Open question |
| OQ-AC-14 | Operational Note owner, retention, redaction and provider/AI access policy | Open question |

| OQ-AC-15 | Exact authoritative producer/scheduler and readback behavior after the deadline | RESOLVED BY CANON (§5B): Appointment Domain via authoritative backend scheduled job/worker in the transactional SoR with authoritative readback before retry; physical component is an engineering detail; no client timer |
| OQ-AC-16 | Deadline race ordering between an exception command and automatic completion | RESOLVED BY CANON (§5B): exception check re-evaluated at commit time in a single transactional commit using version/expected-version, deterministic ordering (§16) and idempotency keys (§23); an exception registered before the completion commit wins; a committed completion is not silently reversed |
| OQ-AC-17 | Customer-side Визит не состоялся command/outcome semantics if no existing canonical mechanism covers it | Deferred. Customer-side Визит не состоялся is outside the mandatory scope of the current Master MVP Controlled Pilot; no new status/event/command created here |
| OQ-AC-18 | MASTER-REPORTED NON-DELIVERY AFTER CUSTOMER ARRIVAL | Open question; does not block weekly Master MVP |
Inherited proposals from Repository Responsibility Matrix remain proposals:

- `OD-RRM-1`: `beautygo_backend` operational transactional SoR;
- `OD-RRM-2`: `ai-bot-platform` conversation/orchestration runtime only;
- `OD-RRM-3`: `ayla-ai-core` has no direct domain-storage access;
- `OD-RRM-4`: `formula_tela` is provider integration, not Ayla operational SoR.

## 31. Source and Evidence Notes

Mandatory sources read:

- `Ayla Constitution`, `Ayla Domain Capability Registry`, `Ayla Glossary`;
- `Ayla Decision Log` (AYLA-DEC-0020, AYLA-DEC-0021, AYLA-DEC-0022);
- `Ayla MVP Scope and Release Contract`;
- `Ayla Single-Provider Technical Pilot Execution Scope`;
- `Ayla Multi-Provider Product Validation Execution Scope`;
- `Ayla Repository Responsibility Matrix`;
- `Ayla Domain Context Map`, `Ayla Core Domain Model Specification`;
- `Ayla Domain Event Registry`, `Ayla Transaction State Model`;
- `Consent Scope Registry`, `Data Inventory Matrix`.

Evidence treatment:

- **Verified**: Appointment is a distinct capability/aggregate candidate; AI is not
  source of truth; owner emits events; same-ID reschedule differs from replacement;
  provider boundary is not a second Ayla Appointment SoR.
- **Proposed**: backend repository assignment, exact fields/API schemas, physical
  storage, role write permissions and several event semantics.
- **Open**: completion/no-show authority, state naming, provider mapping and admin
  override policy.

## 32. Validation Checklist

- [x] Appointment has one domain owner: Appointment Domain.
- [x] Domain ownership is separated from repository and physical storage.
- [x] AI, channel, projection and provider raw state are not Appointment owners.
- [x] Appointment is separated from Recommendation, Slot, Conversation, Payment
      and Calendar Event.
- [x] Same-ID reschedule is separated from replacement.
- [x] Failed, timeout and tool acknowledgement are not business success.
- [x] Manual/admin booking uses the same Appointment domain.
- [x] Event producer is owner of the fact.
- [x] Privacy boundary excludes memory, hypotheses and other-provider history.
- [x] Unknown ownership and unresolved semantics are recorded as proposals/open
      questions.
- [ ] OD-RRM-1..4 are accepted.
- [x] Projections are separated from domain state and identify source/freshness/version.
- [x] Operational exceptions are separate from Appointment status.
- [x] READ/PROPOSE/COMMAND/WRITE boundaries preserve domain-owner write authority.
- [x] Create, cancel and reschedule idempotency behavior covers retries and timeouts.
- [x] Timeline is separated from lifecycle and role-filtered.
- [x] Operational notes have purpose and explicit visibility; no unrestricted notes field.
- [x] Arrival/check-in is separate from completion and does not add a status silently.
- [x] Schedule influence is separated from Appointment ownership.
- [ ] OQ-AC-1..14 are resolved by responsible owners.

## 33. Change Log

### v1.1-draft (2026-08-14)

- Added operational projections for Master Today, Admin Calendar and Customer Appointment.
- Added Operational Exceptions, extended permission model and explicit idempotency contract.
- Added Appointment Timeline, Operational Notes and Customer Arrival/Check-in boundary.
- Added schedule influence without creating a new canonical event or SoR.
- Preserved domain ownership, provider boundary, AI boundary and representation separation.
- Recorded unresolved ownership and event semantics as open questions.
### v1.0-draft (2026-08-14)

- Reworked the contract against the Repository Responsibility Matrix.
- Separated Domain Contract, Implementation, API Representation, UI Projection
  and AI Tool Representation.
- Added lifecycle, commands, role, events, projections, failure and privacy
  boundaries required for downstream contracts.
- Preserved unresolved completion, no-show, provider and permission decisions as
  open questions instead of presenting them as facts.

### Previous versions

The previous v0.2 draft is superseded by this draft structure; useful decisions were
retained only where supported by current canonical sources.
