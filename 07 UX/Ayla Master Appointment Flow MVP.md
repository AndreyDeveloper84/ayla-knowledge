---
node_id: ayla.ux.master-appointment-flow-mvp
title: Ayla Master Appointment Flow MVP
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
updated: 2026-08-17
review_cycle: monthly
depends_on:
  - "[[Ayla Master System and Recovery UX Contract]]"
  - Ayla Knowledge Area Taxonomy
  - Ayla Repository Responsibility Matrix
  - Ayla MVP Appointment Contract
  - Ayla Domain Event Registry
  - Ayla Salon Operations MVP Contract
  - Ayla Master App Information Architecture
  - Ayla Master Operations Screen Contract
  - Ayla Appointment Detail Screen Contract
  - "[[Ayla Master MVP Auth and Authority Contract]]"
  - "[[Ayla MVP Customer Resolution Contract]]"
---

# Ayla Master Appointment Flow MVP

> Canonical UX flow contract for the minimum working appointment journey of a master in the Ayla mobile application. This document connects existing Screen Contracts; it does not create a screen, capability, domain rule, API contract, or domain event.

## 1. Purpose

`Ayla Master Appointment Flow MVP` connects the existing `Master Operations Screen Contract` and `Appointment Detail Screen Contract` into one minimum working scenario.

The flow covers the master daily path through authoritative post-visit resolution: open day, inspect appointment, deliver the visit or report an authorized exception, receive the authoritative result, and return to the working day.

`Open working day → see the next appointment → open appointment details → perform an authorized action → receive the authoritative result → return to the working day.`

This document defines user intent, screen transitions, available data, action boundaries, result handling, and MVP exceptions. It does not replace the Appointment Contract or make the screens owners of appointment state.

The document does not create new capabilities. It describes the user flow of capabilities already documented by the canonical Product Operations and Architecture sources.

The invariants are:

- `Screen State != Domain State`;
- `Projection != Source of Truth`;
- Appointment Domain remains the owner of appointment lifecycle, status, invariants, and committed events;
- `AI suggestion != Business action`.

## 2. MVP Scenario Definition

### 2.1 Primary user

**Master**

### 2.2 Primary goal

Successfully conduct an assigned working visit using the minimum approved operational path.

### 2.3 Canonical scenario

```text
Master starts day
  → Operations Home
  → selects an appointment
  → Appointment Detail
  → performs an authorized action
  → Appointment Domain validates and commits, if applicable
  → registered event updates a projection
  → Operations Home reflects the updated day
```

The flow is complete only when the result is read back from an authoritative projection or the system explicitly reports that the action is pending, blocked, or failed. A successful UI interaction or command transport response is not proof of a committed business result.

## 3. Entry Point

The canonical entry point is `Master Operations Home`.

It provides the day-level context needed to select work:

- current working day;
- schedule and appointment summary;
- nearest actionable appointment, where available;
- day-level operational exceptions;
- freshness or offline indication when current data is unavailable.

**Input:** current-day operational projection and permitted master context.

**Output:** a selected `appointment_id` that can be opened under the master's authorization scope.

Operations Home does not decide appointment ownership, status, eligibility, or business rules. It consumes permitted projections and routes the master to the appointment-specific contract.

## 4. Flow Steps

| Step | Screen | User Intent | Available Data | Action | Result |
|---|---|---|---|---|---|
| 1 | Operations Home | Understand the current working day and what requires attention next. | Current-day schedule projection, appointment cards, operational exceptions, freshness. | Open the working day; select an available appointment. | A permitted appointment is selected, or the screen reports empty, stale, offline, or exception state. |
| 2 | Operations Home → Appointment Detail | Move from day context to one concrete visit. | `appointment_id`, appointment summary, authorized navigation context. | Select appointment. | Appointment Detail opens for the selected appointment; no domain state changes. |
| 3 | Appointment Detail | Prepare for the visit using current appointment, service, and allowed customer context. | Appointment Operational Projection, service context, permitted customer context, notes where authorized, available actions. | View or refresh appointment context. | The master sees current context, or an explicit changed, offline, permission, or exception state. |
| 4 | Appointment Detail | Perform the minimum approved work action. | Current authoritative status, action eligibility, required confirmation/evidence indication, projection freshness. | Execute only an authorized action already supported by canonical contracts. | The command is committed and reflected, or the result is pending, blocked, failed, or requires reconciliation. |
| 5 | Appointment Detail → Operations Home | Continue the working day after the result is known. | Updated appointment projection, updated day projection, registered event outcome, next permitted task. | Return to working day. | Operations Home refreshes the affected appointment and shows the next operational context without locally inventing a status. |

### 4.1 MVP outcome selection

The normal appointment outcome is a zero-action path:

Appointment confirmed/actionable
  -> authoritative scheduled_end
  -> 3-hour post-visit resolution window
  -> no lifecycle exception registered before deadline
  -> authoritative normal completion after deadline
  -> updated appointment/day projection
  -> Operations Home refresh

The master is not required to press CompleteAppointment after an ordinary visit.
appointment.completed remains the existing event name and is consumed only after
authoritative commit/readback. An exception path uses only existing canonical
authority, commands, events, and recovery; it never overwrites an exception with
normal completion. The customer-arrived/non-delivery case remains Open Question.
## 5. Screen Transition Contract

| From Screen | Action | To Screen | Expected Result |
|---|---|---|---|
| Operations Home | Select permitted appointment | Appointment Detail | Detail context opens for the selected appointment; no domain state changes. |
| Operations Home | Refresh or resume after background | Operations Home | Day projection is reread; stale or unavailable data remains explicit. |
| Appointment Detail | View or refresh | Appointment Detail | Appointment context is reread; changed version, permission, offline, or exception states are explicit. |
| Appointment Detail | Complete authorized action, if approved | Operations Home | After authoritative result readback, the day projection reflects the updated appointment; otherwise the master sees pending, blocked, or failed recovery. |
| Appointment Detail | Return without a committed action | Operations Home | No appointment state is changed; the day context is refreshed according to its freshness rule. |
| Appointment Detail | Encounter cancellation or non-actionable state | Operations Home | The master returns to the day context with the appointment's authoritative state and any permitted next step. |

No transition in this table implies a new route, API, event, or domain capability.

## 6. Data Flow

| Screen | Projection | Domain Source / Owner | Event Affecting Update | Updated Projection |
|---|---|---|---|---|
| Operations Home | Master Operations / day projection | Appointment Domain, Schedule/Operations owners | Registered appointment or schedule events; exact event-to-projection mapping follows existing contracts. | Updated Operations Home projection. |
| Appointment Detail | Appointment Operational Projection | Appointment Domain | Registered appointment events, including `appointment.completed` only after authoritative commit. | Updated appointment projection. |
| Appointment Detail | Authorized service and customer context projections | Service/Offering, Customer/Consent, and approved notes owners | Source-domain projection updates under their existing privacy and ownership rules. | Refreshed permitted detail context. |
| Appointment Detail → Operations Home | Appointment result plus day projection | Appointment Domain and Operations projection owner | Committed domain event and projection update; a command response alone is insufficient. | Updated Operations Home projection with freshness/result state. |

The flow never treats a screen-local state, optimistic update, cached DTO, or AI response as the source of truth.

## 7. Action Boundaries

| Action | Master can | Master cannot | Canonical status |
|---|---|---|---|
| View Appointment | Read the appointment context permitted for the role and purpose. | Read unrelated customers, providers, hidden memory, or unapproved profile data. | Included; read-only. |
| Refresh Appointment | Request a fresh permitted projection and inspect its freshness. | Convert stale data into an authoritative status or overwrite a concurrent change. | Included; read/refresh. |
| Normal visit | No manual completion action is required; wait for authoritative completion after the three-hour window. | Do not use a local timer or claim completion from elapsed time. | Included zero-action path; authoritative readback required. |
| Start Service | Nothing beyond viewing a proposed/preparation state until the capability and event semantics are approved. | Invent `StartService`, an in-progress state, or a new event. | Deferred / Open Question. |
| Mark No Show | Nothing until master authority, evidence, command, and event semantics are approved. | Treat no-show as cancellation or infer it from elapsed time. | Deferred / Open Question. |
| Request Change | Nothing beyond an explicitly approved proposal or administrative workflow. | Change the appointment directly or choose command semantics without an owner decision. | Deferred / Open Question. |
| Cancel Appointment | Follow only an explicitly authorized canonical cancellation flow, if one is exposed to the master. | Change cancellation rules or emit `appointment.cancelled` from UX. | Not part of the default MVP path; permission is unresolved. |

## 8. Exception Flows

Only exceptions that can interrupt the first working path are included.

| Exception | Detection | Master-facing outcome | Boundary |
|---|---|---|---|
| Appointment changed | Projection version or freshness conflict differs from the opened context. | Stop the stale action, reread the appointment, show the authoritative current state, and require a new decision. | No silent overwrite; no local merge of domain state. |
| Appointment cancelled | Authoritative projection reflects `appointment.cancelled`. | Show the appointment as non-actionable and return the master to the day context or permitted next step. | Cancellation semantics remain owned by Appointment Domain. |
| No connection | Current projection or command boundary is unavailable. | Show last known context only with freshness; prevent claims of success and allow retry when supported. | Offline state is not a domain status. |
| Action cannot be executed | Authorization, lifecycle, policy, or validation rejects the action. | Show blocked result and permitted recovery/owner path; do not retry blindly. | Domain/policy owner decides eligibility. |
| Update error or pending result | Command transport succeeded but authoritative readback is absent, or projection update failed. | Show pending/unknown result, preserve idempotency and recovery path, then reconcile through authoritative refresh. | Transport success is not business commit. |

## 9. Ayla Assistant Flow

Ayla is an approved global conversational surface in the application navigation (`Today | Schedule | Ayla`). Inside this appointment flow, Ayla remains contextual support: it is not a third transition path and does not own a step. EMBEDDED Ayla inside the Appointment Detail screen specifically remains Deferred (see §10).

### Ayla can

- explain approved appointment or service context;
- help the master understand the next permitted step;
- summarize explicitly provided operational information;
- propose an action for the master to review;
- guide the master through the canonical write path: conversational intake → preflight → proposal → master confirmation → authoritative command (the same commands as the Manual UI) → authoritative readback;
- handle booking-time customer resolution only through the shared canonical resolver (search/select/disambiguate/create-minimum) defined by [[Ayla MVP Customer Resolution Contract]].

### Ayla cannot

- execute a command without explicit master confirmation, or through any path other than the canonical commands shared with the Manual UI;
- create a customer autonomously or resolve an ambiguous customer match by guessing (disambiguation is mandatory);
- change appointment status, ownership, schedule, or availability;
- create a business fact from an inference;
- decide completion, cancellation, or no-show;
- expose hidden memory, unauthorized customer data, or medical conclusions.

Any actionable proposal follows the canonical write pattern — conversational intake → preflight → proposal → master confirmation → authoritative command → authoritative readback — converging with the Manual UI on one canonical authority boundary defined by [[Ayla Master MVP Auth and Authority Contract]] §7. Ayla holds no elevated authority. `AI suggestion != Business action`.

## 10. MVP Scope

### Included

- Operations Home as the entry point;
- selecting and opening a permitted appointment;
- Appointment Detail with appointment and service context required for the visit;
- minimum necessary customer context under existing privacy rules;
- read and freshness handling;
- the three-hour post-visit resolution window and zero-action normal completion path;
- return to Operations Home after a committed, blocked, pending, or failed result;
- changed, cancelled, offline, and action-failure handling;
- Ayla assistance through the approved global conversational surface (`Today | Schedule | Ayla`) with no elevated authority: any Ayla write follows the canonical pattern and the same authoritative commands as the Manual UI after master confirmation ([[Ayla Master MVP Auth and Authority Contract]] §7).

### Deferred

- Start Service and an authoritative in-progress state;
- procedure timer;
- Mark No Show as a master action until canonical authority/evidence is approved;
- Request Change workflow;
- expanded operational notes and result capture until owner, retention, and correction rules are approved;
- offline command queue/retry semantics;
- separate confirmation screen, unless required by the unresolved action policy;
- EMBEDDED Ayla inside the Appointment Detail screen (the approved global Ayla surface is unaffected).

### Future

- full CRM or customer history;
- salon/business management;
- advanced analytics;
- expanded AI automation;
- photo context and other sensitive media workflows;
- additional post-completion workflows not required for the first working visit.

The deferred and future items do not block the documented minimum path unless an owner decision later makes one a prerequisite for the MVP release.

## 11. Open Questions

| ID | Question | Status |
|---|---|---|
| UX-MAF-OQ-01 | Is a separate confirmation screen required after the completion action, or is authoritative readback on the existing screens sufficient? | Open question; UX/Product Operations owner decision required. |
| UX-MAF-OQ-02 | Is an intermediate appointment/service status required for the MVP flow? | Open question; Appointment Domain and Product Operations. |
| UX-MAF-OQ-03 | Remaining completion evidence/correction rules and authoritative producer after the approved three-hour window | Open question; Appointment Contract / Product Operations. |
| UX-MAF-OQ-04 | Is offline retry required for the MVP, and if so, what idempotency and reconciliation contract applies? | Open question; Engineering/Architecture and domain owner. |
| UX-MAF-OQ-05 | Are additional steps required after completion before the master returns to the working day? | Open question; Product Operations owner decision. |
| UX-MAF-OQ-06 | Should the master be allowed to cancel, mark no-show, or request a change from this flow? | Open question; existing permission and event semantics are not closed. |

An Open Question is not permission to implement a capability. It records a decision needed before the flow may claim that capability is active.

| UX-MAF-OQ-07 | MASTER-REPORTED NON-DELIVERY AFTER CUSTOMER ARRIVAL | Open question; no new action/status/event is defined |

## 12. Validation Checklist

### Architecture

- [x] Appointment Domain remains the owner of appointment lifecycle, status, invariants, and committed events.
- [x] No new domain events were created.
- [x] Existing projections remain consumers of domain truth, not sources of truth.
- [x] The flow does not define API, DTO, backend implementation, or new business rules.

### UX

- [x] The flow can be followed from Operations Home to appointment work and back to the working day.
- [x] Each transition has a user intent, available data, action, and result.
- [x] No additional screen is required for the minimum path.
- [x] Changed, cancelled, offline, blocked, pending, and failed outcomes are distinguishable.

### MVP

- [x] Scope is limited to the first working appointment scenario.
- [x] Non-blocking capabilities are deferred or future.
- [x] Unresolved policies are recorded as Open Questions instead of silently assumed.

### AI

- [x] Ayla has no elevated authority; Ayla writes follow the canonical pattern and the same authoritative commands as the Manual UI after master confirmation.
- [x] AI suggestions converge with the Manual UI on one canonical authority boundary ([[Ayla Master MVP Auth and Authority Contract]] §7).
- [x] AI output is not treated as a business fact.

### Privacy

- [x] Data remains limited to the authorized context of the master and existing projection rules.
- [x] Hidden memory, unrelated customers/providers, unauthorized PII, and medical inference are excluded.


## 12A. Shared System and Recovery UX

Cross-screen loading, freshness, offline, permission, Pending/Unknown, error, and conflict recovery follows the shared [[Ayla Master System and Recovery UX Contract]]. The flow preserves valid context and authoritative readback; it does not create offline writes, hidden retries, or a second state machine.

## 13. Source and Non-Override Rule

This Flow Contract is subordinate to the canonical Foundation, Architecture, Product Operations, and UX documents listed in `depends_on`. Those documents remain authoritative for ownership, appointment lifecycle, permissions, event semantics, consent, business behavior, and screen-level contracts.

This document must not be used to infer a new capability from a user transition, to activate a proposed event, or to override an unresolved owner decision.

## Change Log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-08-15 | Initial MVP flow contract connecting the existing Operations Home and Appointment Detail Screen Contracts. |
| 0.1.1 | 2026-08-17 | CR-3: reconciled Ayla wording with the approved global Ayla surface and the canonical write pattern per [[Ayla Master MVP Auth and Authority Contract]] §7 and [[Ayla MVP Customer Resolution Contract]]; EMBEDDED Ayla in Appointment Detail recorded as Deferred. |
