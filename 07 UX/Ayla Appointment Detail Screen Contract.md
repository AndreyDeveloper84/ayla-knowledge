---
node_id: ayla.ux.appointment-detail-screen-contract
title: Ayla Appointment Detail Screen Contract
type: specification
status: draft
canonical_status: candidate
version: "0.1"
owner: UX Architecture
owners:
  - UX Architecture
  - Product Operations
knowledge_area: design
system_owner:
  - ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: medium
data_categories:
  - pii
security_sensitivity: medium
ai_indexing: allowed
export_policy: sanitized
domain: booking
updated: 2026-08-14
review_cycle: monthly
depends_on:

  - "[[Ayla Master System and Recovery UX Contract]]"
  - Ayla Knowledge Area Taxonomy
  - Ayla Repository Responsibility Matrix
  - Ayla Constitution
  - Ayla Glossary
  - Ayla Domain Capability Registry
  - Ayla Decision Log
  - Ayla MVP Appointment Contract
  - Ayla Domain Event Registry
  - Ayla Domain Context Map
  - Ayla Core Domain Model Specification
  - Ayla Salon Operations MVP Contract
  - Ayla Master App Information Architecture
  - Ayla Master Operations Screen Contract
---

# Ayla Appointment Detail Screen Contract

> Canonical UX contract for the master mobile screen that operates on one appointment. This document defines screen responsibility, projections, authorized actions, states, event relationships, AI boundaries, and privacy constraints. It does not define UI, API, implementation, or a second appointment owner.

## 1. Purpose

Appointment Detail is the focused operational surface for one appointment. It helps the master prepare for the customer, understand the approved service context, perform authorized service-delivery actions, and see the result after the Appointment Domain commits a state change.

The screen is separated from Operations Home because the two surfaces answer different questions:

| Surface | Primary responsibility |
| --- | --- |
| Operations Home | What is happening in the master's working day and what is the next operational task? |
| Appointment Detail | What is true and what may the master do for this particular appointment? |

The screen supports the daily cycle `prepare -> deliver -> record permitted outcome -> return to day context`. It is not a CRM, scheduling administration surface, domain model, source of truth, or replacement for an administrator.

## 2. User Context

### 2.1 Primary user

**Master** — an authorized operational participant assigned to, or otherwise permitted to work with, the appointment.

### 2.2 Goals

- prepare for the customer and the booked service;
- understand the current appointment state and the next permitted step;
- access the minimum customer context needed for the current operational purpose;
- perform the service and, where authorized, record the operational outcome;
- surface an exception when the appointment or provider context is unclear;
- return to an updated day projection after a committed change.

### 2.3 Pain points

- insufficient context before the service;
- uncertainty about what to do next;
- appointment changes after the master opened the screen;
- missing or stale service/customer information;
- risk of treating an AI suggestion, local state, or command acknowledgement as a business fact.

### 2.4 Role assumptions

The master receives a purpose-limited operational projection. The screen does not infer permissions from visibility, assignment, time elapsed, or the presence of an action. Authorization is evaluated by the owning domain and policy boundary.

## 3. Screen Responsibility Boundary

### 3.1 The screen does

- present the current appointment projection and its freshness/version;
- present approved service context and minimum necessary customer context;
- present operational notes only when their purpose, access, and retention rules permit them;
- expose only actions authorized by the domain/policy boundary;
- represent pending, rejected, stale, changed, and committed outcomes explicitly;
- refresh from an updated projection after a committed domain event.

### 3.2 The screen does not

- create an Appointment or become its owner;
- define or own appointment statuses and transitions;
- change booking rules, availability, pricing, assignment, or cancellation policy;
- manage the whole schedule or salon operations;
- replace administrator decision-making or domain validation;
- treat a projection, local screen state, button press, API response, AI output, timeout, or notification as a committed fact;
- expose semantic memory, hidden inference, unrelated customers/providers, or unnecessary profile data.

The invariants are explicit: `Screen State != Domain State` and `Projection != Source of Truth`. Appointment lifecycle remains owned by the Appointment Domain.

## 4. Information Architecture

The logical structure follows the master's operating sequence, not a visual component hierarchy.

| Logical block | Operational purpose | Required context | Not responsible for |
| --- | --- | --- | --- |
| Appointment Summary | Establish identity, time, assigned master, service and authoritative status | Appointment Operational Projection | Recomputing status or changing ownership |
| Customer Context | Provide minimum necessary customer information for this visit | Authorized customer operational projection and permitted notes | Full profile, hidden memory, diagnosis, or inference |
| Service Context | Explain the booked service snapshot and approved constraints | Service/appointment projection | Editing catalog rules or inventing service requirements |
| Operational Notes | Show or capture purpose-limited notes when the capability and policy exist | Approved operational notes projection | AI memory or unrestricted clinical record |
| Current Status | Make authoritative state, freshness, conflicts, and uncertainty understandable | Appointment projection plus exception metadata | Deriving state from time or local flags |
| Available Actions | Offer authorized read/command entry points | Authorization/policy projection and current version | Granting permission or committing state |
| Ayla Assistant Context | Explain approved context and prepare optional next steps | Explicitly passed allowed projection | Independent decision, write authority, or hidden context |
| Exceptions | Make stale data, changed appointments, sync issues, and escalation visible | Exception/operation result projection | Silently resolving domain conflicts |

## 5. Business Operation and Capability Model

### 5.1 Business operation

The screen supports **service delivery for one confirmed or otherwise actionable appointment**. The business operation is owned by Salon Operations and the Appointment Domain according to their respective contracts. The screen only coordinates the human interaction with projections and authorized commands.

### 5.2 Capability sequence

```text
Appointment capability
  -> authorized appointment projection
  -> master reviews service/customer context
  -> master chooses an allowed action
  -> command is validated by the owning domain
  -> registered domain event, if committed
  -> updated projection
  -> screen reflects the authoritative result
```

`StartService` and a separate in-progress service state are not treated as active capabilities here: the Product Operations contract marks them Proposed. The screen may show a preparation state before an owner decision, but must not invent a command or event.

## 6. Screen Data Contract

### 6.1 Data block contract

| Data Block | Data | Source | Owner | Refresh Rule |
| --- | --- | --- | --- | --- |
| Appointment Summary | `appointment_id`, date, start/end time and timezone, service snapshot, duration, assigned master reference, authoritative status, version, freshness | Appointment Operational Projection | Appointment Domain | On entry, explicit refresh, projection version change, registered appointment event, return from background; stale/unknown is not empty or completed |
| Customer Context | Minimum necessary name/display label and approved visit-specific context; operational notes only where authorized | Authorized Customer Operational Projection and approved notes projection | Customer/Consent owner and notes owner; exact ownership remains outside UX | On entry and when authorization, consent scope, note version, or projection version changes; fail closed when scope is unknown |
| Service Context | Booked service name, duration, permitted parameters, assignment/service snapshot, approved constraints | Appointment Projection and Service Domain/Offering projection | Appointment owner for appointment snapshot; Service/Offering owner for service meaning | Refresh when appointment revision or service projection version changes; screen cannot edit the snapshot |
| Operational Notes | Purpose, author, timestamp/version, note content permitted for this role, and correction/retention metadata where defined | Approved Operational Notes Projection | Appointment/Service Delivery owner pending explicit decision | Read on entry; refresh after an approved note result or projection event; never promote to AI memory |
| Current Status | Authoritative status, action eligibility, freshness, conflict/stale marker, pending result, and owner/next step for an exception | Appointment Operational Projection plus policy/exception projection | Appointment Domain and relevant policy/operations owner | Refresh only from authoritative readback or registered event; local pending state is not a domain status |
| Available Actions | Action identifier, current eligibility, required confirmation/evidence indicator, and disabled reason where applicable | Authorization/Policy Projection and appointment version | Appointment Domain/policy owner | Re-evaluate after every projection refresh, version change, role/consent change, or command result |
| Ayla Assistant Context | Only the explicitly allowed fields passed to the assistant, source/freshness labels, and non-authoritative suggestions | Current authorized screen projection | AI is a consumer; source-domain owners retain ownership | Rebuild when the allowed projection changes; no direct read of hidden memory or source aggregate |
| Exceptions | Changed appointment, provider sync issue, stale projection, failed/pending command, or escalation owner/next allowed step | Exception/Operation Result Projection | Relevant operational or domain owner | On operation result, registered event, sync update, or explicit refresh; never dismiss uncertainty as success |

### 6.2 Required data invariants

- `appointment_id` identifies the aggregate; it does not grant access or write authority.
- Displayed status comes from the authoritative projection, not from elapsed time, screen navigation, or AI interpretation.
- A service snapshot shown on the screen is read-only from the screen's perspective.
- Customer data is purpose-limited and may be absent even when an appointment exists.
- Projection freshness and version must be available so the screen can distinguish current, stale, changed, and unknown context.
- A command is not successful until the owning domain has committed the transition and the updated projection is available or an explicit uncertainty state is returned.

### 6.3 Explicitly excluded data

The screen must not expose:

- hidden AI memory, memory candidates, model reasoning, or inferred customer attributes;
- medical conclusions, diagnoses, or unapproved health/safety interpretations;
- unrelated customers, providers, appointments, or full salon data;
- full conversation history or a complete customer profile without a separately approved purpose;
- unapproved pricing, payment, earnings, or internal administrative data;
- stale or unknown data presented as an authoritative current fact.

## 7. User Actions Contract

### 7.1 Action contract

| Action | Purpose | Command | Result Event |
| --- | --- | --- | --- |
| View Appointment | Read the authorized appointment context | Read projection; no domain command | No domain event; updated projection may be requested |
| Refresh Appointment | Resolve stale/changed/unknown context | Read/refresh request; no domain command | No domain event; new projection or explicit failure |
| Start Service | Begin a separately modeled service-delivery state, if approved | `StartService` is Proposed and must not be implemented from this document | No event selected; Open Question pending capability and event semantics |
| Complete Appointment | Optional correction/exception path where canonical policy authorizes it; not required for an ordinary visit | CompleteAppointment only where exposed by canonical policy | appointment.completed only after authoritative commit; normal completion follows the Appointment Contract window |
| Mark No Show | Conditional Master action for recording the existing canonical no-show outcome | Available only when canonical authority, permission, evidence, and command/event semantics are approved; do not infer from `CompleteAppointment` or elapsed time | `appointment.no_show` is consumed only after an authoritative committed outcome; otherwise keep the action unavailable/deferred |
| Request Change | Ask for a change or escalation without silently changing the appointment | Command/proposal/admin workflow is not yet selected | No appointment event until the authorized owner commits a registered transition; Open Question |
| Add Operational Note | Record a purpose-limited operational note when the capability is active | Note command; exact contract pending | Note result/projection update, not an AI-memory event |

### 7.2 Authoritative completion and exception flow

```text
Normal visit
  -> authoritative scheduled_end
  -> 3-hour resolution window
  -> no exception before deadline
  -> authoritative normal completion
  -> updated Appointment Projection
  -> Appointment Detail refresh
```

The screen may show `pending`, `blocked`, `failed`, or `unknown` while the outcome is unresolved. A successful transport response, closed screen, timeout, or AI acknowledgement does not mean completion.

### 7.3 Confirmation and recovery rules

- Confirmation is required for any action whose policy marks it consequential; the exact policy is owned outside this screen contract.
- The screen must present the current appointment version when submitting a state-changing command.
- A changed version or conflict requires reread/reconciliation; silent overwrite is prohibited.
- Retry must be idempotent according to the owning command contract.
- If the result is unknown, the screen shows uncertainty and recovery/escalation rather than asserting success.

## 7A. Post-Visit Resolution Presentation

After scheduled_end and before the authoritative deadline, Appointment Detail may
show: Время визита закончилось. Если всё прошло как запланировано, ничего делать
не нужно. Запись автоматически завершится по истечении трёх часов.

This is a normal zero-action state, not an error or mandatory Завершить визит
ceremony. Клиент не пришёл may appear only when canonical no-show authority,
evidence, permission, and event semantics permit it, with lower visual priority.
Do not add a Клиент пришёл, но услуга не состоялась action; that scenario is the
Appointment Contract Open Question. Feedback/review is not lifecycle outcome.

After the deadline, show completed only from authoritative Appointment
projection/readback; never derive it from local time. Before scheduled_end,
opening the screen does not create a post-visit state. Pending/unknown command
results use existing reconciliation and idempotency behavior.
## 8. Screen States

| State | Meaning | Screen contract behavior |
| --- | --- | --- |
| Normal | Appointment projection is current and actionable | Show approved context and currently authorized actions |
| Before Appointment | Appointment is actionable but service delivery has not been confirmed as started | Show preparation context; do not invent `started` state |
| In Progress (deferred) | Future presentation only if the Start Service capability and authoritative state are approved | Not part of the current P0 temporal model; never infer it from elapsed time or scheduled interval |
| Post-Visit Resolution | scheduled_end passed, deadline not authoritatively resolved, and no exception is known | Explain that nothing is required for a normal visit; show only permitted exception action |
| Completed | appointment.completed is committed and reflected in projection | Show committed outcome; do not infer from local elapsed time |
| Cancelled | `appointment.cancelled` was committed and reflected in projection | Show non-actionable cancellation context; no new cancellation event is created by UX |
| No Show | A separately authorized and approved no-show fact is reflected | Keep distinct from `cancelled`; until approved, show unresolved/proposed semantics |
| Changed | Appointment version or relevant data changed after load | Refresh/reconcile and disclose changed context before allowing consequential action |
| Offline | Current connection cannot retrieve or commit authoritative data | Show last known data as stale if available; do not claim command success |
| Exception | Sync failure, permission block, stale result, conflict, or other operational issue exists | Show the issue, owner/next permitted step, and recovery path; do not hide it locally |

Screen state is presentation state. It must never be written back as a domain fact.
### 8A. MVP Temporal Presentation Model

The current Master MVP temporal presentation model is:

```text
BEFORE APPOINTMENT
  -> SCHEDULED INTERVAL
  -> POST-VISIT RESOLUTION
  -> AUTHORITATIVE OUTCOME

ANY COMMAND / READBACK UNCERTAINTY
  -> PENDING / UNKNOWN
  -> AUTHORITATIVE RECONCILIATION
  -> ACTUAL RESULTING STATE
```

These are presentation states, not new Appointment statuses.

| Presentation context | Contract |
| --- | --- |
| Before Appointment | Before `scheduled_start`, show Appointment Summary, Service Context, minimum necessary Customer Context, and preparation context. Do not claim that service started or show post-visit actions. Relative time such as "До визита 40 минут" is presentation aid only. |
| Scheduled Interval | From `scheduled_start` through `scheduled_end`, show the scheduled time and, where useful, copy such as "Сейчас по расписанию". Current time inside the interval is not proof that service started; do not show "Визит идёт", "Процедура начата", or authoritative `In Progress` without an approved `StartService` capability/state. |
| Post-Visit Resolution | After authoritative `scheduled_end` and before authoritative resolution, show the normal zero-action message: "Время визита закончилось. Если всё прошло как запланировано, ничего делать не нужно. Запись автоматически завершится по истечении трёх часов." A deadline may be shown only as supplied by authoritative context. Do not require manual completion or a positive visit confirmation. `Клиент не пришёл` is lower-priority and appears only when canonical authority, permission, evidence, and event semantics permit the Master action. Do not add the unresolved non-delivery-after-arrival action. |
| Completed | Show a completed outcome only after the authoritative Appointment projection/readback confirms it. Never derive `Completed` from local `now >= scheduled_end + 3 hours`. |
| No Show | Show No Show as a read state only when the authoritative projection reports the existing canonical outcome. The outcome is distinct from the conditional Master `Клиент не пришёл` action; the latter is not a guaranteed P0 write capability while authority/evidence policy remains open. |
| Pending / Unknown | After a consequential command with unknown transport or unconfirmed readback, show "Проверяем результат" / "Не удалось подтвердить, сохранилось ли изменение." Do not assert success or confirmed failure, and do not blindly retry a potentially committed state-changing command. Use existing idempotency, version, reconciliation, and authoritative readback semantics. |

At the resolution deadline, the UI must not locally transition from "resolution window" to `Completed`. The authoritative completion mechanism or reconciliation produces the updated projection; until then, Appointment Detail remains Pending/Unknown where appropriate.

## 9. Ayla Assistant Boundary

### 9.1 Placement

Ayla may appear as a contextual assistant surface within Appointment Detail, using only the current authorized projection. It is not a separate appointment-control surface and does not receive direct access to the Appointment aggregate or hidden memory.

### 9.2 Ayla CAN

- explain the approved service description and known constraints;
- summarize the permitted appointment/customer context;
- remind the master of the appointment and the next permitted operational step;
- help interpret an exception already present in the projection;
- propose or prepare an action for explicit master review;
- explain the result of an authoritative operation and disclose uncertainty.

### 9.3 Ayla CANNOT

- complete the service or change appointment status on its own;
- create, cancel, reschedule, reassign, or otherwise change an appointment without an authorized command and domain validation;
- decide whether a customer is a no-show or whether a service was completed;
- bypass permissions, consent, version checks, or administrator workflow;
- expose hidden memory, inference, unrelated data, or unapproved sensitive context;
- make medical conclusions or diagnoses.

```text
AI suggestion != Business action
AI-prepared command != Committed domain state
Committed domain state -> registered event -> projection
```

## 10. Privacy Boundary

| Actor | Allowed Data | Forbidden Data |
| --- | --- | --- |
| Master | Own/authorized appointments, minimum necessary customer context, approved service snapshot, and purpose-limited operational notes | Other customers/providers, unrelated appointments, hidden AI memory, inference, unnecessary history, unapproved sensitive data |
| Customer | Customer-facing appointment and communication projection for their own appointment | Master-only operational notes, other customers, provider operations, internal exceptions |
| Administrator | Authorized operational projection and exception context within assigned scope | Data outside role, tenant, purpose, or consent scope; hidden AI hypotheses |
| Ayla | Only explicitly passed, authorized projection fields with applicable purpose/consent scope | Direct write authority, source aggregate access, semantic memory without approval, unauthorized PII, hidden reasoning, unapproved sensitive data |

The exact field allowlist and consent gate remain governed by `Consent Scope Registry` and `Data Inventory Matrix`. If the scope cannot be proven, the screen and assistant fail closed.

## 11. Event Relationship

The screen does not create events. It consumes registered events and refreshed projections.

```text
User Action
  -> authorized Command
  -> Appointment Domain validation
  -> registered Domain Event, if committed
  -> Projection Update
  -> Appointment Detail refresh
```

For this contract:

- `appointment.completed` is the registered event used after authoritative normal completion under the Appointment Contract: authoritative `scheduled_end`, the three-hour resolution window, no lifecycle exception before the deadline, authoritative normal completion, then updated projection. Appointment Detail consumes that projection/event semantics and never produces or infers completion locally; remaining producer, evidence/correction, and deadline-race details remain governed by the Appointment Contract Open Questions;
- `appointment.cancelled` and `appointment.rescheduled` may be reflected only when committed by the Appointment owner under their registered semantics;
- `appointment.no_show` remains the existing canonical no-show vocabulary where its outcome is authorized and committed. That outcome is distinct from the Master `Клиент не пришёл` action, which remains conditional on approved authority, permission, evidence, and command/event semantics;
- `StartService`, `Request Change`, and operational-note results do not receive invented domain-event names;
- screen analytics, clicks, API responses, retries, notification delivery, and AI tool calls are not domain events.

## 12. Relationship With Other Screens

```text
Operations Home
  -> Appointment Detail
      -> optional Customer Context
  -> return to Operations Home after read, commit, or escalation
```

| Concern | Owning screen/contract |
| --- | --- |
| Day scope, next appointment, timeline, and day-level exceptions | Operations Home / Master Operations Screen Contract |
| One appointment's context, authorized actions, outcome, and appointment-specific exceptions | Appointment Detail |
| Broader customer context, if separately approved and scoped | Customer Context; dependency and scope remain an Open Question |
| Appointment lifecycle, invariants, status transitions, and events | Appointment Domain / canonical Architecture contracts |
| UI layout, visual components, and implementation | Future UI/Engineering documents, not this contract |

Appointment Detail may link to Customer Context, but it must not duplicate the customer domain or silently expand the master's data access.

## 13. MVP Scope

| Capability / Data | Status | Rationale / Dependency |
| --- | --- | --- |
| Appointment Summary | Included in MVP | Required by Appointment Operational Projection and Operations flow |
| Service Context | Included in MVP, subject to approved service projection | Required to prepare for the booked service; service ownership remains outside UX |
| Basic read actions and freshness handling | Included in MVP | View, refresh, changed, offline, and exception states are foundational |
| Post-Visit Resolution Window | Included in MVP | Three-hour authoritative window after scheduled_end; ordinary visit is zero-action; producer/evidence dependencies remain explicit |
| Operational Notes | Constrained / Proposed | Product Operations allows purpose-limited notes; exact owner, retention, and correction contract pending |
| Customer Context | Included as minimum necessary projection | Full history and broad profile are excluded; consent/data inventory gates apply |
| Start Service and timer | Deferred | Capability/state semantics are Proposed and no event is selected |
| Mark No Show | Deferred | Authority, evidence, and event semantics are incomplete |
| Request Change | Deferred / admin workflow decision required | Command versus proposal boundary is unresolved |
| Embedded Ayla Assistance | Proposed contextual support | Allowed only over explicit projection and with no write authority |
| Photo context | Future / owner decision required | Privacy, consent, retention, and operational purpose are undefined |

### 13A. Lifecycle Reconciliation

Appointment Detail consumes the three-hour window. It does not own timing, run a
completion timer, or add a manual completion ceremony. Master no-show remains
subject to OQ-AC-7 and UX-ADS-OQ-04 authority/evidence decisions.
## 14. Open Questions

| ID | Question | Status | Owner / dependency |
| --- | --- | --- | --- |
| UX-ADS-OQ-01 | Is `StartService` an approved capability, and what is the authoritative service-delivery state? | Open question | Appointment Domain / Product Operations |
| UX-ADS-OQ-02 | Is a procedure timer required, and is it informational or authoritative? | Open question | Product Operations / Appointment owner |
| UX-ADS-OQ-03 | Remaining completion evidence/correction rules and authoritative producer after the approved three-hour window | Open question | Appointment Contract; OQ-AC-3 / OQ-SO-1 |
| UX-ADS-OQ-04 | Who may mark `no_show`, what evidence is required, and when may `appointment.no_show` become available? | Open question | Appointment Domain / Domain Event Registry |
| UX-ADS-OQ-05 | Is Request Change a command, a proposal, or an administrator workflow? | Open question | Product Operations / Appointment owner |
| UX-ADS-OQ-06 | What operational notes may a master read/write, and what are retention and correction rules? | Open question | Notes owner / Consent Scope Registry / Data Inventory Matrix |
| UX-ADS-OQ-07 | Is previous-visit history needed, and what is the minimum approved scope? | Open question | Customer/Consent owner |
| UX-ADS-OQ-08 | Is photo context required, and what consent, retention, and access rules apply? | Open question | Product, Privacy, Consent owner |
| UX-ADS-OQ-09 | Which actions are available to a master without administrator approval? | Open question | Role policy / Appointment Contract |
| UX-ADS-OQ-10 | Should Ayla Assistant be present inside Appointment Detail in MVP, and which fields may it receive? | Open question | Product, UX, AI/privacy owners |

| UX-ADS-OQ-11 | MASTER-REPORTED NON-DELIVERY AFTER CUSTOMER ARRIVAL | Open question; no new action/status/event is defined | Appointment Domain / Product Owner |

## 15. Validation Checklist

### Architecture

- [x] Appointment Domain remains the owner of appointment lifecycle, status, invariants, and committed events.
- [x] Screen state is explicitly separated from domain state.
- [x] Projections are read models and not sources of truth.
- [x] Existing event names are used only with their documented semantics.
- [x] No new domain events were created; unresolved events/capabilities are Open Questions.

### Product Operations

- [x] The screen supports the service-delivery operation described by Salon Operations.
- [x] Operations Home and appointment-specific work remain separated.
- [x] Master actions are constrained by authorization and owner decisions.

### UX

- [x] The master can follow preparation -> scheduled interval -> permitted exception action, if available -> authoritative outcome/exception -> return to day context.
- [x] Data blocks, sources, owners, refresh rules, and failure states are defined.
- [x] Changed, offline, pending, blocked, and unknown outcomes are distinguishable.

### AI

- [x] Ayla receives only an explicitly allowed projection.
- [x] Ayla has no WRITE authority.
- [x] `AI suggestion != Business action` is explicit.

### Privacy

- [x] Master access is purpose-limited and role-scoped.
- [x] Hidden memory, inference, unrelated actors, and unnecessary profile data are excluded.
- [x] Consent and field allowlists defer to `Consent Scope Registry` and `Data Inventory Matrix`.


## 15A. Shared System and Recovery UX

Appointment Detail consumes the shared [[Ayla Master System and Recovery UX Contract]] for loading, empty, offline, stale, error, permission, Pending/Unknown, conflict, and localized failure presentation. Its frozen temporal lifecycle model and Appointment Domain boundaries remain authoritative for appointment-specific behavior; this reference adds no lifecycle state or command.

## 16. Source and Non-Override Rule

This Screen Contract is subordinate to the canonical Foundation, Architecture, and Product Operations documents listed in `depends_on`. Those documents remain authoritative for ownership, appointment lifecycle, permissions, event semantics, consent, and business behavior. This document does not override them, add a second source of truth, or turn a proposed capability into an implementation requirement.

Handoff documents are historical context only and are not canonical dependencies for this contract.

## 17. P0 UX Freeze

**Appointment Detail P0 UX is frozen for Master MVP implementation.**

The frozen P0 contract includes the current information architecture, the
Before Appointment / Scheduled Interval / Post-Visit Resolution / Authoritative
Outcome temporal presentation model, zero-action normal completion, and
Pending/Unknown reconciliation behavior. `StartService`, timer, mandatory
manual completion, Request Change, broad customer history, photo context,
embedded Ayla, and master-reported non-delivery after customer arrival remain
deferred or open and do not block this freeze.

Further Appointment Detail changes require one of: a demonstrated
implementation blocker, a canonical domain contradiction, or an explicit owner
decision. Open Questions alone do not reopen this P0 freeze.

## Change Log

| Version | Date | Change |
| --- | --- | --- |
| 0.1 | 2026-08-14 | Initial proposed Appointment Detail Screen Contract |
