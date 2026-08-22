---
node_id: ayla.ux.master-system-recovery-ux-contract
title: Ayla Master System and Recovery UX Contract
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
updated: 2026-08-16
review_cycle: monthly
depends_on:
  - "[[Ayla Knowledge Area Taxonomy]]"
  - "[[Ayla Repository Responsibility Matrix]]"
  - "[[Ayla Constitution]]"
  - "[[Ayla Glossary]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Ayla MVP Appointment Contract]]"
  - "[[Ayla Domain Event Registry]]"
  - "[[Ayla Salon Operations MVP Contract]]"
---

# Ayla Master System and Recovery UX Contract

## 1. Purpose and ownership

This contract defines the shared presentation and recovery language for the Ayla Master MVP surfaces:

- Today / Operations Home;
- Schedule;
- Appointment Detail and Master Appointment Flow;
- Ayla conversational surface.

It is a UX presentation contract over existing canonical projections, commands,
permissions, freshness, idempotency, concurrency, and authoritative readback.
It is not a product feature, domain model, new state machine, event registry, or
source of truth for lifecycle semantics.

The Appointment Domain remains the owner of Appointment lifecycle. Schedule and
Appointment Detail remain owners of their screen-specific interaction contracts.
This document owns only the shared System and Recovery presentation vocabulary.

## 2. Source priority and design evidence

The priority order is:

```text
Canonical Domain/Product Contract
  -> Owner Decision
  -> Canonical UX Contract
  -> Design Evidence
```

Handoff documents are not Source of Truth. The System & Recovery composite is
Design Evidence / Visual Reference only. If it is unavailable, this textual
contract remains sufficient for implementation.

## 3. Shared system principle

A system problem must not erase usable working context.

```text
NO USABLE DATA
  -> full-surface recovery state

USABLE PREVIOUS DATA
  -> preserve content
  -> mark trust / freshness / problem
  -> show recovery locally
```

A local failure affects the smallest surface that actually became untrustworthy.
It must not automatically turn a usable Today, Schedule, Appointment Detail, or
Ayla shell into a blank global error screen.

## 4. Trust model

Fresh, Stale, and Offline describe data trust conditions. Unknown primarily
describes an operation result. They are not a single linear lifecycle.

### 4.1 Fresh

- Read is allowed within the authorized scope.
- Permitted writes may start only through canonical server-side validation,
  version, concurrency, and permission rules.
- Fresh data does not bypass authoritative commit or readback.

### 4.2 Stale

- Read is allowed when the data remains useful, with an explicit freshness
  indication.
- A consequential write must trigger authoritative revalidation automatically.
- The user is not required to manually press Refresh before every action.
- A stale appointment, interval, or availability projection is not a guarantee
  that the intended write can commit.

### 4.3 Offline

- Last-known or cached read is allowed only when that context already exists.
- Cached content must be marked last-known / not current / stale as applicable.
- Consequential Master MVP writes are not executed offline.
- Offline command queues, optimistic domain mutation, and offline booking,
  Time Off, Working Hours, or No Show writes are outside P0.

### 4.4 Unknown write result

When a consequential command result is unknown:

- do not present success;
- do not present confirmed failure;
- do not blindly repeat a potentially committed write;
- use the existing idempotency, correlation, version, concurrency, and
  authoritative readback/reconciliation rules.

Unknown is not a new domain status and is not equivalent to Failed.

## 5. Loading

### 5.1 Initial loading

When no usable data exists, show a structural skeleton/loading state that
preserves expected surface geometry. Do not show fake content. Consequential
actions remain unavailable until the required authoritative context is loaded.

### 5.2 Background refresh

When usable data already exists:

- keep the existing content visible;
- show a compact refresh/progress indication;
- do not replace the entire surface with a skeleton;
- avoid unnecessary layout jumps.

The application shell and global navigation remain visible when the user is
already authorized and the shell is known.

## 6. Empty

Empty is a normal authoritative business state. It is not Error, Offline,
Permission denied, Stale, or Loading.

Examples:

- Today may show "На сегодня записей нет".
- Schedule may have no appointments while available working intervals remain
  visible and clickable according to the Schedule Contract.
- An obvious permitted next action may be shown, such as "Добавить запись".

Empty must use neutral presentation and must not use error iconography. A local
absence of appointments must not be inferred from a failed or unavailable read.

## 7. Error

### 7.1 Error without usable data

Show a full-surface error with concise explanation and a safe recovery action,
such as Повторить, Обновить, or Вернуться. Do not claim an empty business state.

### 7.2 Error with usable previous data

Preserve the usable content and show a local/banner error, for example:

- "Не удалось обновить";
- "Показаны последние данные".

Provide the permitted recovery action. Do not confuse Error with Offline and do
not discard previous content unless its trust or privacy boundary is no longer
safe.

## 8. Permission

Permission is an authorization boundary, not a generic technical error.

### 8.1 Object-level permission

If a resource is not readable, do not reveal hidden fields or infer them from
cached context. Show the minimum permitted explanation and a safe return or
escalation path. Unrelated authorized surfaces may remain usable.

### 8.2 Action-level permission

If the object is readable but a consequential action is not permitted:

- keep the readable context when safe;
- explain that the action is unavailable for this role/scope;
- show only an allowed alternative, return, or escalation path;
- never infer permission from visibility, assignment, elapsed time, or a button
  being rendered.

## 9. Pending / Unknown and automatic reconciliation

The shared presentation for an unresolved consequential operation is
Pending / Unknown. Use calm explanatory copy such as:

- "Проверяем результат";
- "Не удалось подтвердить, сохранилось ли изменение".

Where possible, the system starts automatic authoritative readback:

```text
UNKNOWN
  -> automatic authoritative readback / reconciliation
  -> known result
  -> updated presentation
```

If reconciliation is not immediately resolved, keep Unknown explicit and may
provide "Проверить снова" as a recovery affordance. It is not a guarantee that
every unknown write should be repeated. Existing idempotency, version,
correlation, freshness, and concurrency semantics remain authoritative.

A successful transport response, closed screen, timeout, or AI acknowledgement
is not proof of a committed business result.

## 10. Conflict

Conflict is a normal business/concurrency resolution state, not a generic Error.

When a selected appointment, availability interval, or booking context changes
before commit:

- stop the stale write;
- explain the current conflict;
- preserve valid draft context wherever safe;
- show fresh alternatives or the permitted recovery surface;
- require a new authoritative decision;
- never silently shift time, overwrite a concurrent change, cancel, reschedule,
  hide, or invalidate an existing Appointment.

For Manual Booking, retain Customer, Service, Date, and other still-valid draft
fields while requiring fresh time selection. For Schedule availability changes,
reuse the canonical Conflict Guard.

## 11. Smallest Failure Surface Principle

```text
SYSTEM FAILURE SHOULD AFFECT THE SMALLEST SURFACE THAT ACTUALLY BECAME UNTRUSTWORTHY.
```

Examples:

- Customer Context failure may leave Appointment Summary and Service Context
  usable while the Customer Context section shows a local error.
- Unknown CreateAppointment result makes the booking operation Unknown; it does
  not disable the Schedule shell or global navigation.
- Ayla availability read failure prevents a confident current-availability
  answer; it does not necessarily break the entire Ayla conversation.
- Timeline refresh failure preserves last-known timeline when safe and labels
  its freshness.

Do not escalate a local section failure to a full-screen error without a real
trust, privacy, authorization, or safety reason.

## 12. Ayla behavior

Ayla uses the same trust and recovery rules as the manual UI. It does not gain
an AI-specific bypass for availability validation, Conflict Guard, permissions,
tenant boundaries, privacy, or canonical domain rules.

If authoritative schedule data is unavailable, Ayla must not answer as if it
knows current availability. It may provide clearly labeled last-known context
only where allowed. Conversational writes do not become executable proposals
until required authoritative preflight is available.

AI uncertainty never becomes operational certainty.

## 13. Navigation boundary

The canonical Master MVP global navigation remains:

```text
Сегодня | Расписание | Ayla
```

Manual Booking is a contextual Add action, not a global navigation destination.
Create and More tabs shown in a visual iteration are non-canonical/superseded
chrome where they differ from this approved navigation.

## 14. Severity and visual priority

| State | Visual meaning |
| --- | --- |
| Empty | Neutral normal business state |
| Stale | Mild freshness warning |
| Offline | Connectivity warning with readable last-known data |
| Error | Explicit failure and recovery |
| Conflict | Contextual business resolution state |
| Unknown | Informational uncertainty requiring reconciliation |
| Permission | Access/security boundary |

Do not use one alarming treatment for every state. Operational content remains
visually primary; system chrome and recovery messaging must not dominate a
master's time-sensitive work.

## 15. Shared state matrix

| State | Existing data | Read | Consequential write |
| --- | --- | --- | --- |
| Loading | No usable data | Wait | No |
| Empty | Authoritative empty result | Yes | Only where permitted |
| Offline | Cached/last-known may exist | Yes, explicitly marked | No |
| Stale | Usable but freshness is outside contract | Yes | Only after authoritative revalidation |
| Error + cached data | Previous usable data | Yes with warning | Only when required context can be revalidated |
| Error without data | No usable data | No | No |
| Permission | Authorized subset only | Authorized subset | Only authorized actions |
| Pending / Unknown | Existing reads remain where valid | Yes where independent | Do not blindly repeat unknown write |
| Conflict | Fresh conflict context | Yes | Choose/submit an allowed alternative |

This matrix is UX behavior, not a new domain state machine.

## 16. P0 non-goals

The following are outside Master MVP P0:

- offline-first architecture;
- background offline command queue;
- optimistic domain writes;
- complex sync conflict resolution;
- user-facing technical diagnostics;
- retry storms or hidden auto-resubmission;
- generic global error page for every failure;
- duplicate booking retry from Unknown;
- new domain statuses for Loading, Stale, Offline, Unknown, or Conflict.

## 17. Surface reconciliation boundary

Surface-specific contracts consume this shared contract and retain only their
specific content:

- Today / Operations Home keeps day execution, attention, and next-action rules.
- Schedule keeps availability, booking, Time Off, and Conflict Guard rules.
- Appointment Detail keeps appointment context, lifecycle projection, and its
  frozen temporal model.
- Master Appointment Flow keeps cross-screen navigation and action sequencing.
- Master IA keeps information architecture and destinations.
- Ayla reuses the same read/write trust and recovery behavior.

No surface may redefine these shared state meanings or create a second system
of recovery truth.

## 18. Design Evidence boundary

The owner-reviewed System & Recovery composite, when available, represents these
states:

1. Loading;
2. Empty;
3. Offline;
4. Stale;
5. Error without data;
6. Error with previous data;
7. object-level Permission;
8. action-level Permission;
9. Pending / Unknown;
10. Conflict.

The composite confirms behavioral language and visual priority. It does not
create domain statuses, events, commands, permissions, or navigation semantics.
Its navigation must be annotated as non-canonical wherever it differs from
Сегодня | Расписание | Ayla.

## 19. P0 UX freeze

**MASTER MVP SYSTEM & RECOVERY UX — FROZEN FOR IMPLEMENTATION.**

The freeze includes Loading, Empty, Offline, Stale, Error, Permission,
Pending / Unknown, Conflict, the trust model, automatic revalidation,
automatic reconciliation, the Smallest Failure Surface Principle, no offline
writes, and the approved navigation boundary.

Further changes require one of:

1. a demonstrated implementation blocker;
2. a canonical domain contradiction;
3. an explicit owner decision.

Ordinary visual polish does not reopen these UX semantics.

## 20. Validation checklist

- [x] Shared state meanings are presentation/recovery rules, not domain states.
- [x] Cached reads are explicitly trust-labeled and consequential offline writes are excluded.
- [x] Stale writes automatically revalidate before commit.
- [x] Unknown is not treated as success or failure and is reconciled authoritatively.
- [x] Empty is distinct from Error, Offline, Permission, Stale, and Loading.
- [x] Permission is split into object-level and action-level behavior.
- [x] Conflict preserves valid context and forbids silent overwrite/shift.
- [x] Failure is localized to the smallest affected surface.
- [x] Ayla follows the same trust and recovery rules.
- [x] Navigation remains Сегодня | Расписание | Ayla.
- [x] No new domain statuses, events, commands, or state machine were created.
- [x] P0 UX freeze conditions are explicit.

## 21. Source and non-override rule

This contract is subordinate to canonical Foundation, Architecture, Product
Operations, and surface-specific UX contracts listed in `depends_on`. It does
not override Appointment lifecycle, Schedule availability, permissions,
privacy, event semantics, or the frozen Appointment Detail P0 contract.

Handoff documents and visual mockups are evidence only.
