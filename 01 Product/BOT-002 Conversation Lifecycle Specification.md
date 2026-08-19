---
node_id: ayla.product.bot-002.conversation-lifecycle
title: BOT-002 Conversation Lifecycle Specification
type: specification
status: approved
decision_status: accepted
canonical_status: approved
version: "1.0"
owner: Product Owner
knowledge_area:
  - product
domain:
  - conversation
system_owner:
  - ayla-conversation
source_repository: ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
created: 2026-08-12
updated: 2026-08-12
review_cycle: monthly
---

# BOT-002 Conversation Lifecycle Specification

**Status:** CANONICAL
**Scope:** BOT-002 Conversation Lifecycle only
**Implementation:** FORBIDDEN in this document

---

## 1. Purpose

This specification defines the canonical Product semantics of the **ongoing Ayla Conversation after First Contact**: how a Conversation progresses, how Goals relate to Tasks, how Current Focus works and changes, how Tasks progress, and how Conversations continue, pause, resume and complete.

It is the source of truth for Product, UX, QA, AI/Conversation Design and Engineering when building or validating the lifecycle of an ongoing Ayla Conversation.

This document preserves the approved Product Owner decisions MM-D1–MM-D5 and translates them into one coherent Product specification. It does not invent new Product decisions, runtime entities, state machines, APIs or persistence contracts.

---

## 2. Scope

### 2.1 In scope

- The Product-level definition of an ongoing Conversation after First Contact.
- The relationship between Conversation, Goal, Task and Current Focus.
- The composition of a Conversation: multiple unfinished Tasks with exactly one Current Focus.
- The conditions under which Current Focus changes.
- The conceptual lifecycle of an ongoing Conversation: entering, progressing, clarifying, switching focus, pausing, resuming, completing.
- The boundary with `BOT-001 First Contact Specification`.

### 2.2 Out of scope

Everything listed in §9, including all runtime, technical and AI-layer concerns. This specification is Product Canon only.

---

## 3. Canonical Product Concepts

| Term | Definition | Source |
|---|---|---|
| **Conversation** | The continuous story of Ayla helping the user around one Goal or a cluster of related Goals. Conversation is the root product entity of the dialogue; it preserves its identity across Session, channel, device and pause. | MM-D1; `Ayla Conversation Model Specification` §11 |
| **Goal** | The desired result at the level of user state change. A Goal is not a service and not an action. | `Ayla Glossary` §4; `Ayla Product Vision` §1 |
| **Task** | A canonical Product Concept describing the progression toward a user's Goal: the conversational and product work that moves the user closer to that Goal. Task is official Ayla product language and does not imply a specific runtime or backend entity. | `BOT-001` Q8, §3, §16; `Ayla Glossary` §4 |
| **Current Focus** | The canonical Product/UX concept that names what the Conversation's current exchange is serving: one Task, or no Task. Current Focus belongs to the Conversation. | MM-D3, MM-D4 |
| **Active Task** | A UX continuity concept: the user has an ongoing Task from a previous interaction that may be continued. It does not prescribe persistence or retrieval mechanics. | `BOT-001` Q7, §3, §10 |

Two terms answer two different questions and must not be conflated:

- **Active Task** answers: *is there ongoing work from a previous interaction that may be continued?*
- **Current Focus** answers: *what is this Conversation serving right now?*

An unfinished Task that is not in focus is not automatically an Active Task. `Active Task` keeps its canonical `BOT-001` meaning and nothing more.

The term **Foreground Task** is rejected and must not be used (MM-D3).

---

## 4. Mental Model

The approved Product hierarchy is:

```text
Conversation
    ↓
Goal
    ↓
Task
    ↓
Current Focus
```

The role of each concept:

- **Conversation** — the continuous story of Ayla helping the user around one Goal or a cluster of related Goals (MM-D1). It is the container that gives the dialogue its identity and continuity over time, across visits, channels and pauses.
- **Goal** — what the user wants to achieve. The Goal belongs to the user; it gives the Conversation its direction. A Conversation may revolve around one Goal or a cluster of related Goals.
- **Task** — Ayla's progression toward a Goal: the actual conversational and product work that moves the user closer to it. A Task presupposes a user Goal; it is the work of progressing toward that Goal, not the Goal itself.
- **Current Focus** — what the Conversation's current exchange is serving. Current Focus belongs to the Conversation (MM-D4). A Task never owns Focus.

Ownership rules fixed by this model:

- Current Focus belongs to the Conversation. It is not a property or state of any Task (MM-D4).
- Goal remains above Task: every Task serves a Goal; no Task exists without one.
- A Conversation may contain multiple unfinished Tasks. Exactly one Task may hold Current Focus at a time (MM-D2).

---

## 5. Conversation Lifecycle

This section describes the lifecycle of an ongoing Conversation **conceptually**, as Product semantics. It does not define runtime transitions, a state machine, timeouts, thresholds or any technical lifecycle mechanism.

### 5.1 Entering

BOT-001 ends where the ongoing Conversation Lifecycle begins. The lifecycle of an ongoing Conversation starts once First Contact has established an actionable interaction — for example, when a standalone understood actionable intent has begun a Task-oriented progression under `BOT-001` §16.4.

A user may also re-enter an ongoing Conversation when returning after a gap: a Conversation preserves its identity across Sessions, channels, devices and pauses, so a return continues the same story whenever semantic continuity remains (`Ayla Conversation Model Specification` §11, §18–§21).

### 5.2 Progressing

A Conversation progresses through Tasks. At any moment, the Task holding Current Focus is the work the current exchange serves. Other Tasks may remain unfinished inside the same Conversation; exactly one Task holds Current Focus at a time (MM-D2).

Progression is driven by the user's intent, not by ceremony: Intent Before Ceremony (`BOT-001` P1, Q9) governs the ongoing Conversation exactly as it governs First Contact.

### 5.3 Clarifying

Clarification, correction and supporting dialogue inside a Task are part of that Task's progression. They do not change Current Focus and they do not create a new Task. Information is collected progressively and only when required by the current intent or Task, consistent with `BOT-001` P5 and §13.

### 5.4 Switching focus

Current Focus changes only through the conditions defined in §6.3 (MM-D5): an explicit new user intent, an explicit return, an explicit abandonment, or Task completion. Ayla never switches Current Focus silently.

When Current Focus moves to a new Task, the previously focused Task remains unfinished and may be returned to; it is not thereby completed, abandoned or automatically an Active Task.

### 5.5 Pausing

A pause — a gap in the dialogue, however long — is not closure. A pause does not destroy the Conversation's identity and does not by itself move or clear Current Focus (`Ayla Conversation Model Specification` §20). Silence, inactivity or a long gap do **not** by themselves complete a Conversation; they are compatible with pause semantics.

This specification defines no timeout, inactivity threshold or technical pause mechanics.

### 5.6 Resuming

A Conversation may be resumed after a pause; resumption preserves the Conversation's identity whenever semantic and contextual continuity remains (`Ayla Conversation Model Specification` §21).

When an existing Conversation resumes after a gap, Ayla preserves the meaning and relevant context of the previous exchange. However, previously obtained information that is time-sensitive, dynamic, externally changeable or otherwise reasonably capable of becoming stale must **not** automatically be treated as still valid for an action or decision. Before acting on such information, Ayla must obtain the current value from an authoritative source where available, or re-confirm the relevant information with the user where necessary. Stable context that has no reasonable indication of becoming stale may continue to be used without unnecessarily asking the user again.

This specification defines no universal freshness duration, timeout, TTL, freshness scoring algorithm, caching layer or technical revalidation mechanism (see §9).

The user may explicitly return to earlier unfinished work at any time. An explicit return moves Current Focus back to that Task (MM-D5).

Ayla may offer to continue unfinished work — an offer, never a force, consistent with `BOT-001` §10.1. An offer by itself does not change Current Focus; Focus changes only when the user explicitly accepts, which is an explicit return under MM-D5. The user may always start a new intent instead (`BOT-001` §9.3, §10.1).

### 5.7 Completing

#### 5.7.1 Task completion

A Task is complete when one of the following holds:

1. The expected user outcome of that Task has been achieved.
2. The user explicitly confirms that no further progression on that Task is required.

Executing an intermediate action by itself does **not** complete a Task. If an action is technically executed but the expected user outcome has not yet been achieved, the Task remains unfinished.

> **Conceptual distinction.** Task completion is not the same as technical action execution. For example, Ayla sending a request is not necessarily Task completion; a confirmed outcome satisfying the Task's expected user result may be Task completion. This example is illustrative only and does not canonicalize booking logic.

When the Task holding Current Focus completes, Current Focus clears. This does **not** automatically close the Conversation.

After a Task completes, Current Focus does not move to any other Task unless the user expresses an explicit new intent or an explicit return — the only causes available under MM-D5.

#### 5.7.2 Conversation closure

A Conversation is complete when one of the following holds:

1. There is no remaining relevant unfinished work within its Goal or related Goal cluster and the expected user outcome has been reached.
2. The user explicitly indicates that they do not want to continue that Conversation.

Completion of one Task does **not** automatically complete the Conversation if relevant unfinished work remains within its Goal or Goal cluster. Silence, inactivity or a long gap do **not** by themselves complete a Conversation; they are compatible with pause semantics (see §5.5).

Conversation closure is distinct from Task completion by construction. Consistent with `Ayla Conversation Model Specification` §22, Conversation closure does **not** mean deletion of Conversation data; existing Conversation Canon remains authoritative for that distinction.

---

## 6. Current Focus

### 6.1 Ownership

**Current Focus belongs to the Conversation.**

In the approved hierarchy — Conversation ↓ Goal ↓ Task ↓ Current Focus (MM-D4) — Focus is a Conversation-level Product/UX concept. A Task never owns Focus; no Task carries, stores or controls it. Current Focus is a Product/UX notion only: it implies no runtime pointer, field, state or data structure.

### 6.2 Behaviour

- Exactly one Task may hold Current Focus at a time (MM-D2). There is never more than one.
- Current Focus may rest on no Task at all — for example, during a pure greeting, or after a Task has completed or been explicitly abandoned. There is exactly one Current Focus at any moment, including the empty case.
- A Conversation may contain multiple unfinished Tasks. Tasks that do not hold Current Focus remain unfinished and may be returned to explicitly (MM-D2, MM-D5).
- An unfinished Task that has lost Current Focus is not automatically an `Active Task`. `Active Task` keeps its canonical `BOT-001` meaning: ongoing work from a previous interaction that may be continued (§3).

### 6.3 Change conditions

Current Focus changes only through (MM-D5):

1. **Explicit new user intent.** The user expresses a new standalone intent that does not belong to the current Task — in free text or through a Quick Action. Current Focus moves to the new Task. This protects Intent Before Ceremony and the user's freedom to start a new intent at any time (`BOT-001` P1, Q9, §9.3, §10.1).
2. **Explicit return.** The user explicitly returns to earlier unfinished work. Current Focus moves back to that Task.
3. **Explicit abandonment.** The user explicitly abandons the current work. Current Focus clears; it does not move to another Task.
4. **Task completion.** The current Task completes. Current Focus clears; it does not move to another Task. Task completion is defined in §5.7.1.

**Ayla never switches Current Focus silently.** No event outside this list changes Current Focus. In particular, clarification and supporting dialogue inside a Task, a pause in the conversation, and changes in the surrounding domain situation do not change Current Focus; and an Ayla offer to resume earlier work changes nothing until the user explicitly accepts.

---

## 7. Relationship with BOT-001

`BOT-001 First Contact Specification` is canonical and remains untouched by this document.

The boundary is:

- **BOT-001 owns First Contact**: the entry surface, greeting- and intent-driven entry, MVP segmentation (New User / Returning User / User with an Active Task), Quick Actions at entry, progressive information collection rules, consent timing, and the initial emergence of a Task (`BOT-001` §5–§16).
- **BOT-002 owns the ongoing Conversation Lifecycle**: everything that happens once the interaction has progressed beyond First Contact into an ongoing Conversation — progression, clarification, focus switching, pause, resumption and completion as defined in §5–§6.

BOT-001 ends where the ongoing Conversation Lifecycle begins. The transition is sufficiently defined by existing canon: BOT-001 §16.4 fixes when a Task-oriented progression begins, and BOT-002 governs everything beyond First Contact. This specification does not reopen, amend or reinterpret any BOT-001 decision; in particular, the canonical meanings of `Task` and `Active Task` are consumed here exactly as BOT-001 defines them.

---

## 8. Existing Canon Preservation

| Canon item | Source | How this specification preserves it |
|---|---|---|
| Intent Before Ceremony | `BOT-001` P1, Q9 | Focus change cause 1 honours a new explicit intent immediately (§5.2, §6.3); no ceremony delays it. |
| Conversation-first | `Ayla Conversation Model Specification` §11 | Conversation is the root of the mental model; Tasks and Focus live inside it (§3, §4). |
| Goal-centric product philosophy | `Ayla Glossary` §4; `Ayla Product Principles` 4.2 | Goal sits above Task in the hierarchy; every Task is progression toward a user Goal (§3, §4). |
| Human-first interaction | `Ayla Product Principles` 4.1; `Ayla Product Essence` §4 | The user is the hero of the story; Focus moves only on user intent signals or Task completion, never by Ayla's silent initiative (§6.3). |
| Progressive information collection | `BOT-001` P5, §13 | Clarification inside a Task is part of the Task and stays targeted; no questionnaires are introduced (§5.3). |
| User agency | `BOT-001` §9.3, §10.1; `Ayla Product Principles` 4.6, 4.8 | The user may start a new intent, return to earlier work, or abandon current work at any time; Ayla offers but never forces (§5.6, §6.3). |
| Transparency | `Ayla Product Principles` 4.4, 4.6 | Ayla never switches Current Focus silently; every focus change has an explicit, user-visible cause (§6.3). |
| Trust | `Ayla Product Essence` §14 | No hidden focus switches, no forced continuations and no manufactured next Tasks after completion (§5.7, §6.3). |
| MVP-first | `Ayla Product Principles` 4.14; authoring process §2.6 | The model adds exactly one new Product term (Current Focus) and defers all runtime, storage and selection mechanics (§9). |
| Task as canonical Product Concept | `BOT-001` Q8, §16 | Task is used as product language only; no runtime, API or persistence mapping is defined (§3, §9). |
| Active Task meaning | `BOT-001` Q7, §3, §10 | Active Task remains a UX continuity concept for ongoing work from a previous interaction; it is not redefined and not merged with Current Focus (§3, §6.2). |
| Conversation ownership | `Ayla Conversation Model Specification` §11.2, §25 | This specification assigns Conversation no new ownership; Current Focus is a Product/UX concept, not a context store, and implies no implementation (§6.1). |
| Task completion = user outcome achieved or user-confirmed | BOT-002-PD-01; `Ayla Product Principles` 4.13 (User Outcome First), 4.7 (Booking Is Downstream) | A Task completes when the expected user outcome is achieved or the user explicitly confirms completion; intermediate action execution does not complete a Task (§5.7.1). |
| Conversation closure = Goal-thread resolution or user ends it | BOT-002-PD-02; `Ayla Conversation Model Specification` §22 | A Conversation closes only when its Goal or Goal cluster has no remaining relevant unfinished work and the expected outcome is reached, or when the user explicitly ends it (§5.7.2). |
| Resumption freshness = selective revalidation | BOT-002-PD-03; `Ayla Product Principles` 4.4 (Honest Representation), 4.8 (User in Control) | On resume, time-sensitive or externally changeable information is revalidated against an authoritative source or with the user; stable context continues without unnecessary re-asking (§5.6). |

---

## 9. Out of Scope

This specification does not define:

- LLM behaviour, prompt engineering or AI architecture;
- Intent resolution, classification or slot filling (owned by `Ayla Intent Model Specification`);
- runtime orchestration, runtime transitions or any state machine;
- Conversation State enums or technical lifecycle states (the canonical Conversation State enum remains `NOT_DEFINED`; see `Ayla Conversation Model Specification` §23);
- memory implementation, persistent Memory, or the boundary between conversational context and Memory;
- APIs, payloads, databases, persistence, Event Bus or event contracts, transport;
- the technical Conversation/Session/Interaction data model or Conversation Model implementation (owned conceptually by `Ayla Conversation Model Specification`);
- Task runtime mapping: Task storage, retrieval, inventory, selection mechanics, or Task-to-Conversation mapping (FOLLOW-UP — TASK RUNTIME MAPPING, per `BOT-001` §10.3, §21);
- how the system detects that a message belongs to the current Task;
- booking logic or booking lifecycle;
- recommendation logic or the recommendation engine;
- discovery, proactive outreach, notifications or reminders;
- Mobile App conversation lifecycle (out of MVP pilot scope per `BOT-001` Q1);
- exact copy, localized strings or visual design;
- universal freshness duration, freshness scoring algorithm or caching policy for resumed context;
- technical revalidation mechanism or protocol for stale information;
- runtime detection of Task completion (e.g., success-state mapping, backend status checks);
- Conversation closure state machine, lifecycle enum, TTL or archive policy.

---

## 10. Decision Index

### 10.1 Approved decisions MM-D1–MM-D5

Each approved Product Owner decision appears exactly once below. No superseded or rejected option is presented as active.

| Decision ID | Decision | How preserved in this specification |
|---|---|---|
| **MM-D1** | Conversation is the continuous story of Ayla helping the user around one Goal or a cluster of related Goals. | §3 (Conversation); §4 (role of Conversation); §5.1. |
| **MM-D2** | A Conversation may contain multiple unfinished Tasks. Exactly one Task may hold Current Focus at a time. | §4 (ownership rules); §5.2; §5.4; §6.2. |
| **MM-D3** | Current Focus is the canonical Product/UX concept. Foreground Task is rejected. | §3 (Current Focus definition; Foreground Task rejected); §6. |
| **MM-D4** | Current Focus belongs to the Conversation. Hierarchy: Conversation ↓ Goal ↓ Task ↓ Current Focus. Task is never the owner of Focus. | §4 (mental model hierarchy); §6.1 (ownership). |
| **MM-D5** | Current Focus changes only through explicit new user intent, explicit return, explicit abandonment, or Task completion. Ayla never switches Current Focus silently. | §5.4; §5.6; §5.7; §6.3 (change conditions). |
| **BOT-002-PD-01** | A Task is complete when the expected user outcome of that Task has been achieved, or the user explicitly confirms that no further progression is required. Intermediate action execution by itself does not complete a Task. | §5.7.1; §8 (canon preservation). |
| **BOT-002-PD-02** | A Conversation is complete when there is no remaining relevant unfinished work within its Goal or related Goal cluster and the expected user outcome has been reached, or when the user explicitly indicates they do not want to continue. Completion of one Task does not automatically complete the Conversation. | §5.5; §5.7.2; §8 (canon preservation). |
| **BOT-002-PD-03** | On resumption after a gap, Ayla preserves meaning and relevant context, but time-sensitive / dynamic / externally changeable information must be revalidated before acting. Stable context may continue without unnecessary re-asking. | §5.6; §8 (canon preservation). |

### 10.2 Open follow-ups (not decided by this specification)

The following items are intentionally deferred. They are listed for traceability only; nothing in this specification decides them.

- Detailed pause semantics, including any inactivity thresholds or states (BOT-002-Q15).
- Detailed proactive resume policy: when Ayla may proactively offer to continue unfinished work (BOT-002-Q16).
- Abandonment cleanup and retention detail after explicit abandonment (BOT-002-Q23 detail).
- The detailed boundary between conversational context and persistent Memory (BOT-002-Q27, Q28).
- Runtime Task selection among unfinished Tasks.
- Runtime/storage mechanics for Task inventory, persistence, retrieval or Task-to-Conversation mapping (FOLLOW-UP — TASK RUNTIME MAPPING, per `BOT-001` §10.3, §21).

---

## 11. Canonicalization Record

- **Canonicalization date:** 2026-08-12
- **Canonicalization authority:** Product Owner
- **Canon Review:** READY FOR CANON; 0 blockers; 0 required corrections
- **Canonicalization basis:** Ayla Product Decision & Canon Authoring Process v1.0, Phase 10; Ayla Canon Review Standard v1.0

**Document status:** CANONICAL
