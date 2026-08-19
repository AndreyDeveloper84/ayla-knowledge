---
node_id: ayla.ux.master-schedule-ux-contract
title: Ayla Master Schedule UX Contract
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
  - "[[Ayla Knowledge Area Taxonomy]]"
  - "[[Ayla Repository Responsibility Matrix]]"
  - "[[Ayla MVP Appointment Contract]]"
  - "[[Ayla Domain Event Registry]]"
  - "[[Ayla Salon Operations MVP Contract]]"
  - "[[Ayla Master Operations Screen Contract]]"
  - "[[Ayla Master App Information Architecture]]"
  - "[[Ayla Appointment Detail Screen Contract]]"
  - "[[Ayla Master Appointment Flow MVP]]"
  - "[[Ayla Master MVP Auth and Authority Contract]]"
  - "[[Ayla MVP Customer Resolution Contract]]"
---

# Ayla Master Schedule UX Contract

> Canonical UX contract for the P0 Schedule surface of the Ayla mobile app for a
> master. It defines information architecture, presentation states, navigation,
> and interaction boundaries. It does not define a new domain, API, database,
> appointment lifecycle, event, permission model, or availability formula.

## 1. Status / Purpose

**Status:** Draft / Candidate. **Decision:** NEW DOCUMENT.

The existing Information Architecture identifies `Schedule View` as a logical
responsibility, but does not specify its P0 schedule contract. Existing Operations
Home, Appointment Detail, and Master Appointment Flow contracts own their surfaces
and are not duplicated here.

The purpose is to make the following implementable without re-deciding product
behavior: what Schedule shows, how a master moves through a week/day, how time is
presented, how manual booking and block-time flows start, and how stale/conflicting
availability is handled.

## 2. Scope

### In scope (Master MVP / P0)

- global `Today | Schedule | Ayla` navigation;
- week selector, selected day, and day timeline;
- schedule awareness (read-oriented projection) in the master's authorized tenant/provider scope;
- existing appointment entry to shared Appointment Detail;
- manual booking entry and the order `Customer → Service → Date/time`;
- minimal new customer creation (`name + phone`);
- availability revalidation before creation;
- block-time/time-off entry point, subject to the canonical domain command and the
  authority policy in [[Ayla Master MVP Auth and Authority Contract]];
- explicit empty, loading, stale, conflict, offline, and permission states.

### Out of scope

Schedule is not a full calendar administration tool, CRM, service catalog editor,
provider reassignment console, payment surface, or second source of truth.
Exact API fields, database models, provider synchronization and implementation
technology remain implementation-contract responsibilities.

Schedule presentation is not a domain source of truth and does not itself mutate
domain state. The P0 Schedule surface may initiate permitted write intents
(Manual Booking, Working Hours, Specific Day Exception, Time Off); these intents
are routed to canonical authoritative commands (CAP-010 Availability Management,
CAP-011 Appointments) and committed only under the Master authority policy in
[[Ayla Master MVP Auth and Authority Contract]].

## 3. Canonical Dependencies

The contract depends on the documents in frontmatter. In particular:

- Appointment Contract owns Appointment meaning, lifecycle, commands, concurrency,
  and authoritative writes.
- Domain Event Registry owns event names and producer semantics.
- Salon Operations owns the operational journeys and the distinction between
  availability, booking, time off, and operational exceptions.
- Master Operations Screen Contract owns Operations Home, not Schedule.
- Master App Information Architecture owns the application-level screen map.
- Appointment Detail Screen Contract owns the shared appointment detail surface.
- Master Appointment Flow MVP owns the Today/Home ↔ Appointment Detail path.
- Responsibility Matrix and Taxonomy own repository and canonical-area boundaries.

Handoff documents and visual mockups are evidence only; they are not dependencies.

## 4. Visual References / Design Evidence

The owner-reviewed Operations Home concept is a four-state composite showing the
same mobile home surface at: start of day/next customer, between customers,
current scheduled appointment, and a day without appointments. It is retained as
**Visual UX Reference / Owner-Reviewed Concept**.

The concept confirms the stable hierarchy:

```text
DAY CONTEXT
    ↓
FOCUS
    ↓
TODAY TIMELINE
```

It does not define Schedule layout or override contracts. The old bottom navigation
`Расписание | Клиенты | Профиль` is obsolete visual iteration. The current owner
decision is `Сегодня | Расписание | Ayla`.

The referenced session image was not copied into the repository. Its textual
evidence is sufficient for this contract: Operations Home remains one stable IA
through the day, while FOCUS changes presentation state (`NEXT`, `NOW_SCHEDULED`,
`ATTENTION`, `CHANGE`, `DAY_COMPLETE`, `EMPTY`). These are UI states, not
Appointment statuses.

The owner-reviewed availability-management visual reference is a four-screen
composite:

1. Working Hours.
2. Specific Day Exception.
3. Time Off.
4. Conflict Guard.

It is Design Evidence / Visual Reference, not Source of Truth. The Specific Day
Exception visual behavior is explicit: По обычному графику → Сохранить; Не работаю
→ Сохранить; Другие часы → Start/End selection, so only this branch uses Далее.
The owner-reviewed Ayla Master MVP visual reference is a four-state composite:

1. Ayla Start / Day Context.
2. Ask Schedule / Find Availability.
3. Create Appointment / Confirmation / Result.
4. Change Availability / Conflict.

It is Owner-Approved Design Evidence, not Source of Truth. It confirms a compact
day context rather than a duplicate Operations Home, contextual suggestions,
free-interval answers before Service is known, missing-input clarification,
minimum sufficient proposals, standard booking-draft reuse, authoritative result
navigation, and conflict detection before confirmation. The local image reference
was not copied into the repository; these owner decisions are the normative basis.
## 5. Master MVP Global Navigation

```text
Сегодня  |  Расписание  |  Ayla
   │            │           │
Today/Home   Schedule    contextual assistant
   │            │
   └────── Appointment Detail (shared entry)
```

| Destination | Responsibility | MVP status |
| --- | --- | --- |
| `Сегодня` | Current-day operational context, focus, and timeline | P0 |
| `Расписание` | Week/day schedule awareness and schedule actions | P0 |
| `Ayla` | Contextual assistance within approved boundaries | P0 entry; writes only as user-confirmed intents routed to canonical commands |

There is no separate global Customers or Profile tab in Master MVP. Customer
selection is inside manual booking; customer context is purpose-limited.

## 6. Existing Operations Home Visual Concept

Operations Home is not Schedule View. It is a day-level work center with stable IA:

- **NEXT:** the next actionable appointment or working task;
- **NOW_SCHEDULED:** the current scheduled interval, not proof that service began;
- **ATTENTION:** an authoritative operational exception, stale result, conflict, or other issue requires attention; the normal scheduled_end-to-deadline resolution window is not ATTENTION and is not a local lifecycle status;
- **CHANGE:** schedule or appointment data changed and requires reread;
- **DAY_COMPLETE:** no further actionable work in the current day;
- **EMPTY:** no appointments or tasks are available for the selected context.

Completed appointments may remain in the timeline with reduced visual priority.
The timeline should not jump or reorder itself after every completion. The Home
surface may show free windows inline; a large persistent Ayla block is optional.

The UI must not say "master forgot to finish" when it only knows that an
Appointment is not completed. It must describe the observable state and permitted
next action.

## 7. Schedule Responsibility

Schedule is a read-oriented operational surface. It presents an authorized
schedule projection and routes commands to their canonical owners.

| Concern | Schedule responsibility | Owner / boundary |
| --- | --- | --- |
| Appointment lifecycle/status | Display authoritative projection | Appointment Domain |
| Availability/slots | Display validated bookable intervals | Availability owner; exact physical owner remains open |
| Working hours | Display configured working boundary | Schedule/Provider policy owner |
| Time off/block | Start an authorized command flow | Time-off/Availability owner; no local write |
| Manual appointment | Collect intent and submit CreateAppointment | Appointment Domain via authorized contract |
| Customer identity | Search/select or minimally create customer | Customer/identity owner and privacy rules |
| Service offering | Select an existing offering | Service/catalog owner |
| Conflict resolution | Show conflict and recovery/escalation | Appointment/Availability owner or authorized admin |

Schedule never writes a domain fact directly and never infers status from card
color, elapsed time, a cached response, or a successful UI tap. Write intents
initiated on this surface (manual booking, time-off/block, availability changes)
are committed only by canonical authoritative commands under the Master authority
policy in [[Ayla Master MVP Auth and Authority Contract]]; Schedule itself holds
no domain write authority.

## 8. Schedule Information Architecture

```text
Schedule
├── Week selector
├── Selected day context
│   ├── date + timezone
│   ├── working-hours boundary
│   └── freshness / exception indicator
└── Day timeline
    ├── appointment intervals
    ├── available intervals
    ├── blocked / time-off intervals
    └── non-working intervals
```

### Week selector

Shows a bounded week around the selected day and allows selecting a day in the
authorized schedule scope. It does not imply that all future days are bookable.
Navigation retains the selected day until the user changes it or the context is
invalidated.

### Selected day

Shows date, local timezone, working-hours context, and data freshness. "Today" is
a contextual label; Schedule can inspect other days without changing Today’s
meaning.

### Day timeline

Uses one chronological vertical time axis. Entries are distinguishable by type;
free time is visible as an interval, not necessarily as a notification card.
Completed appointments remain historical timeline entries and are visually
secondary. The timeline must not create or change Appointment records.

## 9. Schedule Time Presentation

| Timeline item | Meaning | Required presentation |
| --- | --- | --- |
| Appointment | Existing Appointment projection with time/service/customer context allowed for the role | status label from authoritative data, interval, entry to Appointment Detail |
| Available | Computed bookable interval for a selected service/assignment context | "Свободно"/available affordance; not a held or guaranteed appointment |
| Blocked / Time Off | Interval unavailable because of an authorized block or time-off record | reason/category only when permitted; no booking affordance |
| Non-working | Outside configured working hours or unavailable day boundary | subdued non-actionable interval; distinguish from Time Off |
| Stale / Unknown | Projection cannot be trusted as current | freshness warning; prevent claims of availability or success |

`Available` is a projection, not a domain status. An available interval may become
invalid before commit. Appointment statuses remain those defined by the Appointment
Contract; Schedule adds no status such as `scheduled_now`, `blocked`, or `available`.

### Appointment Card — Minimum Sufficient Information

An Appointment card contains only what is needed to answer Who / What / When:

Мария К.
Классический массаж
10:00–11:00

Responsive compression such as "Мария К. · Массаж спины" is allowed for short
appointments, but readability takes priority over fitting three lines.

Schedule cards must not show phone, price, booking source, payment status, notes,
customer history, CRM metadata, marketing information, or other extended data.
Those belong to Appointment Detail / Customer Context.

Progressive disclosure:

Schedule          → Who / What / When
Appointment Detail → operational appointment information
Customer Context   → extended customer information

Schedule must not become a mini-CRM.

### Visual Priority and Current-Time Indicator

Appointment is the primary visual object; Blocked / Time Off is secondary and
neutral; Available time is a calm interactive background; Non-working time is
minimally visible or outside the main working viewport. Red/error semantics are
reserved for real conflicts and errors.

For today only, show a thin horizontal current-time line with a small dot and
compact time such as 13:37. It is an orientation aid, not a card or large
"Сейчас 13:37" block, and is absent on past/future dates.
## 10. Schedule Actions

### Read actions (P0)

- change week/day;
- refresh schedule;
- open existing Appointment Detail;
- start manual appointment creation from a free interval;
- start block-time/time-off flow;
- inspect explicit conflict, stale, empty, offline, or permission states.

### Write-intent actions (P0, routed to canonical owners)

- `CreateAppointment` through manual booking;
- authorized time-off/block command, if the existing domain contract exposes it.

Schedule does not provide direct drag-and-drop mutation, silent rescheduling,
specialist reassignment, service editing, payment capture, or customer deletion.
Those are deferred or require separate owner decisions.

## 11. Appointment Entry Point

Every appointment card and Today timeline entry uses the same destination:

```text
Today ───────┘
             ├──> Appointment Detail
Schedule ────┘
```

The entry carries the selected `appointment_id` and authorized navigation context.
Appointment Detail rereads the permitted projection and owns appointment-specific
actions. Schedule does not duplicate detail action semantics.

## 12. Manual Appointment Creation

Manual booking is a creation flow, not a second Appointment lifecycle. It is a
progressive booking draft on one primary screen, not a mandatory visual stepper
or long wizard. The logical business order remains Customer → Service → Date/time
→ Availability validation → Review/Create.

Новая запись

Клиент       selected customer / выбрать
Услуга       selected service / выбрать
Дата и время selected date/time / выбрать

Создать запись

Each section may open a picker, bottom sheet, or separate selection surface.


```text
Customer
   ↓
Service
   ↓
Date/time
   ↓
Availability validation
   ↓
Review
   ↓
Create Appointment
```

The order is intentional. Customer identifies the subject, Service determines
duration/assignment context, and only then can a meaningful availability query be
presented. The selected interval is revalidated at the final commit boundary.

### Primary flow

1. Open "Создать запись" from Schedule or an allowed free interval.
2. Search/select an existing customer, or choose "Новый клиент".
3. Select one existing service offering.
4. Select date/time from intervals valid for the service and assignment context.
5. Show a review containing customer, service, date, local time, duration, and
   permitted price snapshot; do not invent missing domain fields.
6. Submit the canonical create command with authorization and idempotency context.
7. Show committed result only after authoritative readback; otherwise show pending,
   conflict, blocked, or failed recovery.

### Free-interval flow

Selecting an available interval pre-fills the user-facing field Выбранное окно,
not "Исходный интервал":

Выбранное окно
21 августа · 15:00–18:00

This is the available range from which the draft started, not Appointment duration.
After Service selection, valid starts inside the window are shown explicitly (for
example 15:00, 15:30, 16:00, 16:30, 17:00 for a 60-minute service). The system
never silently selects or shifts the start time.

## 13. Customer Selection

Search is scoped to the authorized tenant/provider context and exposes only fields
needed to disambiguate a customer, such as name and masked phone. It must not
surface unrelated customers, hidden memory, medical inference, or full history.

The flow supports an explicit "Новый клиент" path. A failed search is not proof that
the customer does not exist; duplicate prevention and identity matching remain
customer-domain responsibilities and are canonical in
[[Ayla MVP Customer Resolution Contract]].

## 14. New Customer Minimal Flow

The MVP minimum is:

```text
Новый клиент → имя + телефон → validate → create/select customer → Service
```

Name and phone are collected only for the booking purpose. Validation, consent,
deduplication, ownership, retention, and canonical customer identity semantics are
not redefined here; they are defined canonically in
[[Ayla MVP Customer Resolution Contract]]. If the customer command is unavailable or ambiguous, return to
selection with an explicit error; do not create a local customer placeholder.

## 15. Service Selection

Service selection is mandatory and precedes date/time. The list contains only
offerings available in the current authorized provider/tenant context. Schedule
does not create or edit offerings, prices, duration rules, or specialist
assignment semantics.

The selected offering supplies the context needed to ask Availability for a valid
interval. Price and duration shown in review are snapshots/projections and must be
confirmed by the authoritative creation boundary.

## 16. Date / Time Selection

The picker starts with the selected day when entered from a free interval. It shows
only intervals returned for the chosen service/assignment context and clearly
distinguishes available, blocked, non-working, and stale intervals.

Changing date, service, or assignment invalidates the prior interval selection.
The user must be able to go back without losing the selected customer unless
canonical validation rejects it.

## 17. Availability Validation

The UX contract treats availability as a layered read-and-commit check:

```text
Working Hours
+ Time Off / Blocks
+ Existing Appointments
+ Service Duration
        ↓
Availability projection
        ↓
freshness + conflict check at commit
        ↓
CreateAppointment or explicit failure
```

Schedule may display a slot, but only the canonical owner validates whether the
appointment can be committed. The client must not calculate a final authoritative
slot from stale local data. Double booking, tenant boundaries, assignment rules,
hold TTL, and idempotency remain domain/implementation responsibilities.

## 18. Review and Create

Review is a confirmation of user intent, not an authoritative booking confirmation.
It must show the selected customer, service, date/time/timezone, duration and any
required policy disclosure available from canonical sources.

After submit, use these presentation outcomes:

| Outcome | UX behavior |
| --- | --- |
| Committed | Show authoritative appointment result and entry to Appointment Detail/timeline |
| Conflict/stale | Preserve entered data, explain that interval is no longer available, return to fresh selection |
| Blocked/unauthorized | Explain permitted recovery or escalation; do not retry blindly |
| Pending/unknown | Do not claim creation; show reconciliation/refresh path and idempotent retry affordance |
| Transport failure before known commit | Show unknown result and reread path, not "failed" if commit is uncertain |

## 19. Conflict / Stale Availability Behavior

If version, freshness, interval, working-hours, time-off, or appointment data has
changed, stop the mutation and reread authoritative state. The UX must:

1. identify that the previously shown interval changed;
2. avoid silently moving the appointment to another time;
3. preserve non-sensitive selections where safe;
4. present fresh alternatives only after the source is available;
5. route unresolved operational conflicts to the authorized owner/admin path.

A timeout is `unknown`, not success and not automatically failure. A cached slot is
never evidence that an Appointment exists.

## 20. Block Time / Time Off

Time Off answers a different question from Working Hours: when is the master
temporarily unavailable inside otherwise working time?

A typical flow is:

Available Interval → Заблокировать время → Start → End → optional reason →
Confirm → authoritative result → availability refresh.

For example, 15:00–16:30 may be shown as Недоступно / Личное время. Reason is
optional unless an existing canonical domain contract requires it. Time Off is a
neutral operational state, not an error state.

Tap an existing Time Off opens only permitted actions: view; edit where canonical
permissions allow; delete where canonical permissions allow. After authoritative
deletion, availability is recalculated. The interval is not automatically
declared bookable; final bookability still follows canonical availability rules.
"Заблокировать время" is a Schedule entry point to an existing authorized
time-off/block capability. It is not an instruction to create a fake Appointment.

The flow must show selected interval, scope, and permitted reason/category, then
submit the canonical command if one exists. It must revalidate overlap with
Appointments and other blocks. If an existing Appointment is affected, show the
conflict and owner escalation; do not cancel, move, or rewrite it silently.

Exact command, reason taxonomy, recurrence, edit/delete behavior, approval model,
and event semantics remain dependencies/open questions where not defined by the
canonical domain documents.

## 21. Working Hours Boundary

Working Hours answer only: when does the master usually work? They are the basic
recurring weekly schedule.

Minimum UX model:

Monday       09:00–18:00
Tuesday      09:00–18:00
Wednesday    09:00–18:00
Thursday     09:00–18:00
Friday       09:00–18:00
Saturday     10:00–16:00
Sunday       Day off

When editing Working Hours, the interface must clearly communicate that the
ordinary recurring weekly schedule is being edited. Working Hours must not be
used to change one specific date.

Specific Day Exception answers a different question: how will the master work on
this one date?

Specific date
How will I work on this day?
- По обычному графику
- Другие часы
- Не работаю

For По обычному графику and Не работаю, the primary action is immediately
Сохранить and no extra time-selection step is required. Only Другие часы opens
the next selection surface for Начало and Конец; only in that branch is Далее
appropriate. Do not use Далее when the current choice can already be saved.

The scope must be explicit: Изменение только на этот день. Working Hours should
instead communicate that the ordinary recurring schedule is being edited.

A full-day absence uses Specific Day Exception → Не работаю; it must not force
the master to create Time Off across the full Working Hours range. A partial-day
absence inside a working day uses Time Off.
Working Hours define the configured working boundary for a provider/specialist/day.
They are not the same as an ad-hoc Time Off block:

| Working Hours | Time Off / Block |
| --- | --- |
| baseline availability boundary | exception inside or across that boundary |
| recurring/configured policy may apply | specific event or interval |
| outside is non-working | inside is blocked/unavailable for its scope |
| not an Appointment | not an Appointment |

Schedule must visually distinguish non-working time from time off. It must not
assume that a gap inside working hours is bookable until service duration,
appointments, blocks, and freshness are evaluated.

## 21A. Availability Management Mental Model

The user-facing model is:

| User intent | UX path |
| --- | --- |
| Change all future Mondays | Working Hours |
| Change only next Monday | Specific Day Exception |
| Do not work at all on one date | Specific Day Exception → Не работаю |
| Temporarily leave for several hours | Time Off |
| Accept a client in free time | Available Interval → Manual Booking |

This model must be understandable without knowledge of domain terminology.

## 21B. Conflict Guard

Availability changes are not Appointment changes. Working Hours, Specific Day
Exception, and Time Off must never silently cancel, move, hide, invalidate, or
change the time of an existing Appointment.

If a proposed availability change intersects an existing Appointment, the write
stops before the change is committed. The conflict must be resolved through the
appropriate Appointment flow.

For a full-day exception such as 26 August → Не работаю, show a minimal affected
list with time, customer, and service:

На этот день уже есть записи.
Сначала нужно решить, что делать с существующими записями.

Primary action: Посмотреть записи. The master may cancel the availability
change. Do not offer "Всё равно сделать выходным" unless canonical Appointment
contracts define safe behavior.

The same guard applies to a partial-day change. If an appointment is 17:00–18:00
and the master changes that date to 09:00–16:00, stop the write and show the
affected appointment.

For Time Off 14:00–16:00 intersecting an appointment 15:00–16:00, do not create
Time Off. Explain Это время занято and show customer, service, and time. Allowed
recovery is Открыть запись or Изменить время блокировки. No silent override.

Specific Day Exception is an approved UX scenario only. It does not imply a new
backend/domain entity. Implementation must use the existing canonical
schedule/availability model or require a separate architecture/domain decision.
## 22. Schedule States

| State | Meaning | Allowed recovery |
| --- | --- | --- |
| Loading | Schedule projection is being requested | wait/cancel |
| Ready | Current permitted projection is available | navigate, open, start allowed flow |
| Empty | No entries for selected context/day | change day, create booking if policy allows |
| Stale | Projection exists but freshness is outside contract | refresh; block claims of availability |
| Offline | Network/source unavailable | view clearly marked last-known data; no authoritative write claim |
| Permission denied | Scope or action is not authorized | return/escalate; do not reveal hidden data |
| Conflict | Selected interval/record changed | reread and choose again |
| Pending/Unknown | Command outcome is not authoritatively known | reconcile/read back; prevent duplicate fact |
| Error | Source or command failed with known failure | retry when safe or escalate |

Empty is not the same as unavailable data. Offline/stale/permission states must not
be rendered as an empty schedule. If Working Hours exist but
appointments.count == 0, available working intervals remain visible, readable,
and clickable. They can start Записать клиента or Заблокировать время; Записей
пока нет may accompany the timeline but must not replace it.

## 23. Relationship with Today

Today is the operational starting surface; Schedule is the expanded planning/read
surface. Both may show the same Appointment projection and route to the same
Appointment Detail. Today’s FOCUS is derived presentation context and may change
with time; Schedule’s selected day is user navigation context.

Completing an Appointment may update projections, but it must not make the timeline
unstable or invent a new Schedule status. Today and Schedule may refresh according
to their own freshness rules while retaining the same authoritative appointment
meaning.

## 24. Relationship with Online Booking

Manual and online booking consume the same canonical availability/appointment
boundaries. Schedule is not a private bypass:

```text
Working Hours + Time Off + Appointments + Service Duration
                         ↓
                    Availability
                    ↙          ↘
             Online booking   Manual booking
                    \          /
                       Appointment
```

A manual booking can use an operational actor and origin, but it does not create a
second lifecycle or a private slot truth. A slot shown in one channel may become
unavailable in another; final authoritative validation resolves the race.

## 25. Ayla Boundary

Ayla may explain the selected schedule projection, summarize permitted context,
and propose a next step. Ayla may not create customers, appointments, blocks,
availability, statuses, or events; may not bypass authorization; and may not expose
hidden memory or unauthorized PII. Any proposal returns to the ordinary explicit
user flow. `AI suggestion != Business action`.

## 25A. Ayla Master MVP Responsibility

The global Master MVP model is:

| Zone | Responsibility |
| --- | --- |
| Today | Execution surface: understand what is happening today and what requires attention |
| Schedule | Planning and availability management: manage time, appointments, and availability |
| Ayla | Conversational interaction surface: ask about work and initiate permitted operational actions |

Ayla is not a second Operations Home, a separate business/domain system, or an
owner of Appointment or Availability. It has no separate rules for changing
either. It is a conversational entry point to the same authoritative operations
available through the ordinary UI.

Manual UI and Ayla must converge on the same domain action and canonical
validation. Ayla must not bypass Appointment validation, availability validation,
Conflict Guard, permissions, tenant boundaries, privacy boundaries, or domain
rules.

## 25B. Ayla Start State and Suggestions

Ayla starts with minimal day context, not a generic empty chatbot and not a full
Operations Home duplicate:

Доброе утро, Анна.

Сегодня
4 записи · первая в 10:00

Посмотреть день

Contextual suggestions may follow:

- Что у меня сегодня?
- Когда есть свободное время?
- Запиши Марию на массаж
- Закрой завтра после 15:00

Suggestions are presentation behavior that teaches Ayla capabilities; they are not
domain capabilities. Suggestions may vary by morning, between appointments,
evening, or an empty appointment day.

## 25C. Read and Write Model

Ayla answers permitted reads immediately, without confirmation for simple reads:

- Что у меня сегодня?
- Когда я свободен завтра?
- Когда следующая запись?

Writes use the shared pattern:

UNDERSTAND → RESOLVE REQUIRED CONTEXT → PREFLIGHT → PROPOSAL
→ USER CONFIRMATION → AUTHORITATIVE COMMAND → RESULT

Examples include booking an Appointment, setting a Specific Day Exception, or
creating Time Off. AI suggestion is never an authoritative business action.
Conversation state, model interpretation, or a generated proposal cannot change
important data by itself.

## 25D. Schedule Queries and Availability Language

For a query such as Когда у меня есть свободное время завтра?, Ayla may answer:

Завтра вы работаете
10:00–16:00.

Свободные интервалы:

10:00–11:00
11:30–13:00
13:30–15:00
15:00–16:00

When Service is not known, use Свободные интервалы, not "Можно записать на...".
An available interval is not a guaranteed valid booking slot for every Service.
Service duration and canonical availability constraints must be checked before
Appointment creation.

## 25E. Booking Conversation

Ayla does not guess required booking inputs. If the master says Запиши Марию К.
на 11:30 and Service is missing, Ayla asks На какую услугу? and may show allowed
options such as Классический массаж — 60 мин, Массаж лица — 60 мин, Выбрать другую.
It must not infer Service from a previous visit, popularity, default, or model
inference. It asks only for missing required data.

After required data is resolved, Ayla runs canonical availability preflight. If
valid, it may say Проверил расписание. Время доступно and show a proposal:

Мария К.
Классический массаж · 60 мин
9 августа, суббота
11:30–12:30

The proposal contains only Customer, Service, Duration, Date, and Start/end time.
Phone, history, CRM, marketing, and other profile data are excluded unless
needed for disambiguation or required by canonical policy.

Изменить детали reuses the standard Schedule booking draft and selection surfaces;
it is not an AI-specific editor. After authoritative CreateAppointment, show a
compact Запись создана result and Открыть запись. That action routes to the same
canonical Appointment Detail used by Today and Schedule; Ayla has no separate
Appointment Detail.

## 25F. Conversational Availability Changes

A request such as В следующую среду я вообще не работаю maps to the existing
Specific Day Exception → Не работаю model, not recurring Working Hours.

Before proposal, Ayla runs availability preflight. If there is no conflict, it
shows the date, ordinary hours, the one-day scope, and the proposed change:

Среда, 19 августа
Обычно: 09:00–18:00
Изменение: Не работаю весь день
Изменение только на этот день.

Only then are Подтвердить and Отмена shown. Confirmation invokes the same
authoritative availability change as the ordinary Schedule UI.

## 25G. Conversational Conflict Guard

If preflight finds existing Appointments, executable confirmation is not shown.
For a full-day exception, Ayla explains the ordinary hours and lists only affected
Appointment time, customer, and service:

На этот день уже есть записи.
Сначала нужно решить, что делать с существующими записями.

Primary action: Посмотреть записи. The master can cancel the current change.
There is no "Всё равно сделать выходным" action unless canonical Appointment
contracts later define safe behavior.

The same guard applies to partial-day changes and Time Off. Availability changes
must never silently cancel, reschedule, hide, invalidate, or change an existing
Appointment. Ayla reuses the Schedule Conflict Guard and never creates an
AI-specific override, lifecycle, availability model, or write path.

## 25H. Progressive Disclosure and P0 Classes

Ayla is not a mini-CRM:

| Surface | Information responsibility |
| --- | --- |
| Ayla | conversational context, proposal, and result |
| Appointment Detail | operational appointment information |
| Customer Context | extended customer information |
| Schedule | planning and availability management |
| Today | execution of the current day |

The four P0 Ayla capability classes are:

1. UNDERSTAND DAY — Что у меня сегодня?
2. FIND AVAILABILITY — Когда я свободен завтра?
3. PREPARE APPOINTMENT — Запиши Марию на массаж.
4. PREPARE AVAILABILITY CHANGE — Завтра после 15:00 не работаю.

Advanced analytics, marketing, payroll, earnings, autonomous CRM, autonomous
rescheduling/cancellation/schedule writes, and unrelated general-purpose AI are
not Master MVP P0.
## 26. Privacy Boundary

Schedule displays minimum necessary data for the authorized master/provider scope:
appointment time, service, permitted customer identifier, and operational state.
Phone and other PII are shown only where required by the approved customer/detail
contract. Other tenants, masters, customers, hidden notes, semantic memory,
medical inferences, and unrelated history are excluded.

Schedule search, navigation, caches, analytics and error messages must not broaden
the access scope or log sensitive data unnecessarily. Missing or uncertain
authorization fails closed.

## 27. MVP / Deferred / Future

| MVP / P0 | Deferred | Future |
| --- | --- | --- |
| Today/Schedule/Ayla navigation; Today execution context; Ayla start/day context and contextual suggestions; read/write distinction; conversational schedule queries; missing-input resolution; booking preflight/proposal/confirmation/result; shared booking draft and Appointment Detail; conversational Specific Day Exception and Time Off preflight; Conflict Guard reuse; week/day/timeline; existing appointment detail; manual booking; customer lookup; minimal new customer; service-before-time; availability revalidation; base Working Hours; Specific Day Exception including Не работаю; partial-day Time Off; permitted Time Off view/edit/delete; availability refresh after authoritative change; block-time entry; explicit states | Drag-and-drop rescheduling; recurring blocks; specialist reassignment; full customer tab; notifications inbox; advanced filters; offline command queue; catalog editing | Multi-resource calendars; advanced analytics; earnings; full CRM/history; automated schedule optimization |

Deferred items do not become implied requirements through the timeline UI.

## 28. Dependencies / Open Questions

| ID | Question | Owner / status |
| --- | --- | --- |
| SCH-OQ-01 | Who is the authoritative Schedule/Availability owner and physical SoR? | Product/Architecture; resolved by canon: AYLA-DEC-0021 п.2 (domain owner: CAP-010 Availability Management); physical SoR remains OD-RRM-1 (Proposed) — engineering dependency, not an open product question |
| SCH-OQ-02 | What exact time-off/block command, reason taxonomy, approval, and events exist? | Schedule/Availability owner; open — canon/engineering dependency of CAP-010 (exact availability command/event names not yet registered); does not block the authority policy |
| SCH-OQ-03 | What customer identity/deduplication and consent contract supports `name + phone`? | Customer/Consent owner; resolved by canon: [[Ayla MVP Customer Resolution Contract]] |
| SCH-OQ-04 | What are the authoritative timezone and DST rules for schedule display and commit? | Domain/Engineering; resolved by canon: AYLA-DEC-0021 п.5 (UTC storage + IANA local wall time; one calendar per tenant inheriting `Tenant.default_timezone`; device timezone is display-only) |
| SCH-OQ-05 | Are slot holds required for manual booking, and what TTL/reconciliation applies? | Appointment/Availability owner; resolved by canon: AYLA-DEC-0021 п.3 (Slot Hold lifecycle; TTL 15 minutes as a platform parameter); any implementation remainder is an engineering detail |
| SCH-OQ-06 | Which master permissions allow block time or manual creation? | Product Owner/Authorization owner; resolved by canon: [[Ayla Master MVP Auth and Authority Contract]] §7 |
| SCH-OQ-07 | What is the exact projection freshness/version contract? | Schedule/Appointment/Engineering; open |

These questions do not reopen the owner decisions recorded by the prompt:
Schedule is P0; navigation is Today/Schedule/Ayla; manual order is
Customer → Service → Date/time; service is mandatory; validation is mandatory;
there is no separate Customers tab; Today and Schedule share Appointment Detail.

## 29. Validation Checklist

- [x] Schedule is defined as a P0 UX/read surface, not a second domain owner.
- [x] Today / Schedule / Ayla navigation is explicit.
- [x] Operations Home remains distinct from Schedule.
- [x] Week selector, selected day, and day timeline are specified.
- [x] Appointment, available, blocked/time-off, and non-working intervals are distinct.
- [x] Manual flow is `Customer → Service → Date/time`.
- [x] New customer minimum is `name + phone` without redefining identity semantics.
- [x] Availability is revalidated at commit; stale/conflicting behavior is explicit.
- [x] Working Hours and Time Off are distinguished.
- [x] Existing Appointment Detail is the shared entry point.
- [x] No new Appointment statuses, domain events, lifecycle, API, or database model were created.
- [x] Owner-approved refinements are incorporated and are not Open Questions.
- [x] Ayla has no independent write authority or alternate domain rules.
- [x] Ayla reads can answer directly; conversational writes require intent, context, preflight, proposal, confirmation, authoritative command, and result.
- [x] Ayla reuses Schedule availability validation, Conflict Guard, booking draft, and Appointment Detail.
- [x] Missing booking Service is requested explicitly and never inferred silently.
- [x] Known availability conflicts suppress executable confirmation.
- [x] Privacy and authorized tenant scope are explicit.
- [x] Reconciliation gaps and Open Questions are recorded.

### Interaction Model

Tap Appointment → Appointment Detail.
Tap Available Interval → Записать клиента or Заблокировать время.
Tap Time Off → permitted Time Off details/actions.
Tap + → Новая запись or Заблокировать время.

+ and Available Interval use one booking draft; + may have empty date/time,
while an Available Interval pre-fills the selected date and Выбранное окно.
### Updated Schedule Visual Reference

The owner-reviewed Schedule reference contains four states:

1. Normal Working Day.
2. Completely Free Working Day.
3. Day With Time Off.
4. Manual Appointment Creation From Available Interval.

It is Design Evidence / Visual Reference only. It confirms minimum Appointment
cards, calm Available time, neutral Time Off, clickable availability on a free
working day, the compact current-time indicator, progressive booking draft
without a stepper, and the term Выбранное окно. Canonical Contract and Owner
Decision take priority over the visual reference.

## 29A. Shared System and Recovery UX

Schedule consumes the shared [[Ayla Master System and Recovery UX Contract]] for loading, empty, offline, stale, error, permission, Pending/Unknown, and conflict presentation. Schedule-specific rules remain authoritative for clickable availability, booking draft, Time Off, and Conflict Guard. A free working day is not an error or unavailable read, and offline/stale context never claims fresh actionable availability.

## Source and Non-Override Rule

This document is subordinate to the canonical dependencies listed above. If a
canonical domain, owner, permission, event, or privacy contract conflicts with a
presentation detail here, the canonical contract wins. The conflict must be
recorded as a UX/canon reconciliation gap; it must not be silently resolved by
changing domain meaning in UX.

## Change Log

| Version | Date | Change |
| --- | --- | --- |
| 0.1 | 2026-08-15 | New proposed P0 Master Schedule UX contract covering navigation, timeline, manual booking, availability, and block-time boundaries. |
