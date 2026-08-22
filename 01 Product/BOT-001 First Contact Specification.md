---
node_id: ayla.product.bot-001.first-contact
title: BOT-001 First Contact Specification
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
updated: 2026-08-12
review_cycle: monthly
---

# BOT-001 First Contact Specification

**Status:** CANONICAL  
**Scope:** BOT-001 First Contact only  
**Implementation:** FORBIDDEN in this document

---

## 1. Purpose

This specification defines the canonical product and UX behavior for **BOT-001 First Contact**: the first meaningful interaction between a user and Ayla in a conversational entry, within the Controlled Pilot.

It is the source of truth for Product, UX, QA, AI/Conversation Design and Engineering when building or validating First Contact behavior.

This document preserves the approved Product Owner decisions Q1–Q9 and translates them into one coherent normative specification. It does not invent new Product decisions, runtime entities, APIs or persistence contracts.

---

## 2. Scope

### 2.1 In scope

- First Contact behavior for:
  - **MAX Bot** direct message entry;
  - **MAX Mini App** entry / deep-link entry.
- Greeting and intent-driven entry patterns.
- Contextual Quick Actions as optional accelerators.
- Progressive information collection rules.
- Consent timing boundaries.
- Ownership boundary between MAX Bot and Mini App.
- Product-level semantics of Task.
- MVP segmentation for First Contact.

### 2.2 Out of scope

- **Mobile App** First Contact (explicitly excluded by Q1).
- Backend implementation, database schema, API design, EventBus contracts.
- Runtime lifecycle of Task or Conversation.
- Exact marketing copy, brand voice or localized strings.
- Detailed visual design of Mini App screens.

### 2.3 Channels

| Channel | Role in BOT-001 |
|---|---|
| MAX Bot | Primary conversational surface; canonical owner of First Contact logic. |
| MAX Mini App | UI/container/presentation surface; renders Bot-owned First Contact flow. |
| Mobile App | Out of scope. |

---

## 3. Definitions

| Term | Definition |
|---|---|
| **First Contact** | The first meaningful interaction between a user and Ayla in the current conversational entry. It is not necessarily a greeting. |
| **Greeting-driven entry** | The user's first message is a greeting or social opener without an actionable intent. |
| **Intent-driven entry** | The user's first message contains a clear actionable intent. |
| **Task** | A canonical Product Concept describing the progression toward a user's Goal: the conversational and product work that moves the user closer to that Goal. Task is official Ayla product language and does not imply a specific runtime or backend entity. |
| **Active Task** | A UX continuity concept: the user has an ongoing Task from a previous interaction that may be continued. It does not prescribe persistence or retrieval mechanics. |
| **New User** | A user who has no prior recognized interaction with Ayla in the current pilot context. |
| **Returning User** | A user who has prior recognized interaction with Ayla and has no Active Task. |
| **Quick Action** | A contextual, optional button that accelerates a likely intent. It is not navigation and not a menu. |
| **Progressive information collection** | Collecting information only when required by the current intent, Task, booking, safety or consent flow. |
| **Targeted clarification** | A focused question asked to advance a specific intent or satisfy a specific requirement. It is not a questionnaire. |

---

## 4. Product principles

The following principles govern BOT-001 First Contact. They are derived from Q1–Q9 and the conversational UX principles CUX-010 and CUX-012.

**P1 — Intent Before Ceremony (CUX-012).**  
If the user's first message contains a clear actionable intent, Ayla MUST progress that intent immediately. Greeting or scripted introduction MUST NOT delay useful action.

**P2 — Free text is primary.**  
Free-text input MUST remain the primary interaction mode. Quick Actions MUST coexist with free text and MUST NOT replace or block it.

**P3 — Contextual greeting.**  
Greeting behavior MUST adapt to entry context: user state, channel and available context. A single universal scripted greeting MUST NOT be used.

**P4 — Greeting does not create Task.**  
A greeting alone MUST NOT create a Task. A Task emerges only when a standalone understood actionable intent is identified.

**P5 — Progressive information collection only.**  
Information MUST be collected progressively and only when required by the current intent, Task, booking, safety or consent flow. Standalone questionnaires and broad onboarding data collection are forbidden.

**P6 — Single canonical conversational logic (CUX-010).**  
The MAX Bot MUST own the canonical First Contact conversational logic. The Mini App MUST act as a UI/container/presentation surface and MUST NOT implement an independent conversational flow.

**P7 — Consent on demand.**  
Consent MUST be requested only at the point where the corresponding processing or persistence of personal data becomes necessary. Consent MUST NOT be presented as a mandatory first-screen gate.

**P8 — Minimal segmentation.**  
MVP First Contact MUST use exactly three greeting states: New User, Returning User, User with an Active Task. Richer behavioral, profile or cohort segmentation is out of MVP scope.

**P9 — Task as Product Concept.**  
Task is official Ayla product language describing the progression toward a user's Goal. It MUST NOT be treated as a predetermined backend entity, API object or persistence contract.

---

## 5. First Contact entry model

First Contact is the first meaningful interaction in a conversational entry. It can begin with:

- a greeting;
- a clear actionable intent;
- a contextual Quick Action tap;
- a deep link or trigger that carries context.

First Contact is channel-agnostic in logic but channel-specific in rendering. The same canonical Bot-owned logic governs behavior in MAX Bot and MAX Mini App.

The following events, by themselves, MUST NOT create a Task:

- the user opens the Mini App;
- the user sends a greeting;
- the user taps a greeting-style Quick Action;
- the system renders the First Contact surface.

---

## 6. Greeting-driven entry

A greeting-driven entry occurs when the user's first message is a social opener (for example, "Привет") without a clear actionable intent.

### 6.1 Behavior

1. Ayla MAY respond with a brief, contextual greeting.
2. The greeting MUST:
   - be appropriate to the entry context (new/returning/active, channel, trigger);
   - remain lightweight and conversational;
   - not commit the conversation to a fixed path;
   - not create a Task.
3. The greeting SHOULD offer help or invite the user to state their goal in free text.
4. Contextual Quick Actions MAY be presented alongside the greeting.

### 6.2 Invariant

> Greeting never commits or traps the conversation.

If the user responds to a greeting with an actionable intent, Ayla MUST immediately progress that intent.

---

## 7. Intent-driven entry

An intent-driven entry occurs when the user's first message contains a clear actionable intent (for example, "Хочу спортивный массаж").

### 7.1 Behavior

1. Ayla MUST recognize the actionable intent.
2. Ayla MUST progress that intent immediately.
3. Ayla MUST NOT force a standard introduction, onboarding or greeting ceremony before useful action begins.
4. A Task-oriented progression MAY begin once the intent is understood and the next step is offered.

### 7.2 Relationship to greeting

A warm, concise acknowledgment MAY accompany the intent progression, but it MUST NOT delay the actionable response. For example, a brief "Отлично, подбираю варианты" while progressing the request is acceptable; a multi-turn greeting sequence is not.

---

## 8. New User behavior

A New User has no prior recognized interaction with Ayla in the current pilot context.

### 8.1 Greeting behavior

- The greeting SHOULD introduce Ayla's role briefly.
- The greeting MUST NOT deliver a long feature explanation or guided tour.
- The greeting MUST NOT ask broad onboarding questions.

### 8.2 Interaction surface

- Free-text input MUST be available.
- 3–5 contextual Quick Actions MAY be shown. Examples of contextually valid Quick Actions for a New User include:
  - booking a common service category;
  - asking what Ayla can help with;
  - finding a specialist.
- Quick Action copy MUST NOT be canonicalized in this specification; the examples above are illustrative only.

### 8.3 Invariant

If the New User's first message contains a clear intent, greeting behavior MUST be skipped in favor of immediate intent progression.

---

## 9. Returning User behavior

A Returning User has prior recognized interaction with Ayla and no Active Task.

### 9.1 Greeting behavior

- The greeting SHOULD acknowledge the return.
- The greeting MAY surface the most likely next step based on available context.
- The greeting MUST NOT assume or create a new Task automatically.

### 9.2 Interaction surface

- Free-text input MUST be available.
- Contextual Quick Actions MAY be shown. They SHOULD reflect likely continuations relevant to the user's history or recent context, without exposing unavailable actions.

### 9.3 Invariant

A Returning User MUST be able to start a new intent at any time via free text. The system MUST NOT force continuation of a previous topic that is no longer active.

---

## 10. User with Active Task behavior

A User with an Active Task has an ongoing Task from a previous interaction.

### 10.1 Continuity behavior

- Ayla MAY offer to continue the Active Task.
- Ayla MAY contextualize the greeting around the Active Task.
- Ayla MUST NOT force continuation of the Active Task.
- Ayla MUST allow the user to start a new intent via free text at any time.

### 10.2 Quick Actions

Quick Actions MAY include options relevant to the Active Task, such as:

- continue the current Task;
- view or modify a related booking;
- start a new request.

The exact set MUST be contextual and limited to 3–5 actions.

### 10.3 Implementation boundary

How Active Task is detected, persisted or resolved is a runtime concern. This specification does not define:

- Task storage;
- Task retrieval logic;
- Task-to-Conversation mapping;
- Task lifecycle state machine.

If implementation requires such details, mark the item as:

> FOLLOW-UP — TASK RUNTIME MAPPING

---

## 11. Free-text interaction

Free-text input MUST be the primary interaction mode in First Contact.

### 11.1 Requirements

- Free-text input MUST be available on the First Contact surface.
- Free-text input MUST NOT be hidden, disabled or delayed by Quick Actions.
- Free-text input MUST route to intent understanding.
- A user MUST be able to express any supported intent in free text, even if no matching Quick Action is shown.

### 11.2 Unexpected intents

If a user types an intent that is not represented by the visible Quick Actions, Ayla MUST still attempt to understand and progress that intent. Quick Actions MUST NOT constrain routing.

---

## 12. Contextual Quick Actions

Quick Actions are optional contextual accelerators. They are not navigation, not a menu and not mandatory.

### 12.1 Requirements

- First Contact MAY present 3–5 contextual Quick Actions.
- The exact number and labels MUST be determined by context, not fixed globally.
- Quick Actions MUST coexist with free-text input.
- Quick Actions MUST NOT block or replace free-text input.
- Quick Actions MUST be contextually valid for the current user state and entry context.
- Quick Actions MUST NOT expose unavailable actions.
- Tapping a Quick Action MUST start the corresponding intent progression; it MUST NOT launch a broad questionnaire.

### 12.2 Examples (non-canonical)

Depending on context, Quick Actions MAY include:

- "Записаться к мастеру"
- "Выбрать услугу"
- "Перенести запись"
- "Продолжить подбор"

These are examples only. Exact copy is not canonicalized here.

---

## 13. Progressive information collection

First Contact MUST NOT begin with a standalone questionnaire or broad onboarding form.

### 13.1 Allowed collection

Information MAY be collected only when required by:

- the current intent;
- the current Task;
- a booking flow;
- a safety requirement;
- a privacy or consent requirement.

### 13.2 Targeted clarification

Targeted clarification is a focused question asked to satisfy a specific requirement. It is NOT a questionnaire. Targeted clarification is allowed when it meets the conditions in §13.1.

### 13.3 Forbidden patterns

The following MUST NOT appear in First Contact:

- a standalone "Анкета" object or button;
- a multi-field profile completion screen presented as a gate;
- a broad "tell us about yourself" sequence;
- turning the first free-text message into a generalized questionnaire.

---

## 14. Consent boundary

Consent under applicable law (including 152-ФЗ) remains mandatory where legally and product-wise required.

### 14.1 Timing

Consent MUST be requested:

- at the point where the corresponding processing or persistence of personal data becomes necessary;
- in the context of the specific flow that requires it.

### 14.2 Forbidden pattern

Consent MUST NOT be presented as a mandatory first-screen gate before any useful interaction can occur.

### 14.3 Examples of appropriate consent moments

- before storing a preference for future sessions;
- before processing personal data for a recommendation that requires it;
- before a booking flow that requires phone number or other personal data.

The exact consent scopes and UX are governed by the Consent Scope Registry.

---

## 15. Bot / Mini App ownership boundary

### 15.1 Canonical ownership

The MAX Bot owns canonical First Contact conversational logic. This includes:

- conversational flow;
- intent understanding;
- Task creation and routing at the UX level;
- clarification strategy;
- recommendation logic;
- conversation state interpretation;
- next-question selection;
- First Contact behavior.

### 15.2 Mini App role

The MAX Mini App is a UI/container/presentation surface. It is responsible for:

- visual presentation of the Bot-owned flow;
- rich UI components (cards, lists, selectors, calendars);
- rendering the current conversational state;
- forwarding user input to the canonical Bot-owned logic.

### 15.3 Constraints

The Mini App MUST NOT implement:

- an independent First Contact backend flow;
- its own onboarding flow;
- its own intent collection flow;
- its own recommendation engine;
- its own conversation state machine;
- its own clarification strategy;
- its own Task routing logic.

### 15.4 Integration boundary

The payload, transport and integration contract between Bot and Mini App are implementation follow-ups and are intentionally out of scope for this specification.

---

## 16. Task semantics at Product level

### 16.1 Definition

**Task** is a canonical Product Concept and official Ayla product language. Consistent with the Ayla Glossary, it describes:

- the progression toward a user's Goal;
- the conversational and product steps that move the user closer to that Goal.

A Task presupposes a user Goal; it is the work of progressing toward that Goal, not the Goal itself.

### 16.2 What Task is not

For BOT-001, Task MUST NOT be assumed to map one-to-one to:

- a database table;
- an API object;
- an EventBus contract;
- a runtime lifecycle entity;
- a Conversation, Session or Interaction.

### 16.3 Canon layers

The following separation MUST be preserved:

```text
Product Canon
    → UX / Experience Canon
        → Technical Architecture Canon
            → Runtime / Implementation
```

This specification sits at the Product/UX boundary. It uses Task as product language without defining runtime implementation.

### 16.4 Task emergence

A Task-oriented progression begins when Ayla understands a standalone actionable intent and offers a next step. A greeting alone does not create a Task.

---

## 17. First Contact decision flow

The following decision table governs BOT-001 First Contact.

| Step | Condition | Action |
|---|---|---|
| 1 | User sends first message / enters surface. | Determine entry context: channel, user state, trigger/deep link. |
| 2 | First message contains clear actionable intent. | Progress intent immediately (Intent Before Ceremony, CUX-012). Skip scripted greeting. Begin Task-oriented progression if appropriate. |
| 3 | First message is a greeting only. | Respond with contextual greeting. Do not create Task. Offer free-text input and optional Quick Actions. |
| 4 | User state = New User. | Use New User greeting behavior. No onboarding questionnaire. |
| 5 | User state = Returning User, no Active Task. | Use Returning User greeting behavior. No automatic Task creation. |
| 6 | User state = Active Task. | Offer continuity contextualized to the Active Task. Allow free-text new intent. Do not force continuation. |
| 7 | User selects Quick Action. | Progress the corresponding intent. Do not launch a questionnaire. |
| 8 | User types free-text intent. | Route to intent understanding. Progress immediately. |
| 9 | Information is required for intent/Task/booking/safety/consent. | Ask a targeted clarification. Collect progressively. |
| 10 | Consent is required for a specific processing step. | Request consent at that point, not as a universal gate. |

### 17.1 Visual summary

```text
First Contact
├── Intent-driven entry ──→ Progress intent immediately
│                            (CUX-012)
│
└── Greeting-driven entry ──→ Contextual greeting
    ├── New User ──→ brief orientation + free text + optional Quick Actions
    ├── Returning User ──→ contextual greeting + likely continuation + free text
    └── Active Task ──→ continuity offer + allow new intent + free text
```

---

## 18. Examples

Examples use Russian because the pilot user language is Russian. They illustrate behavioral patterns, not canonical copy.

### 18.1 Greeting-driven first entry

**User:** `Привет`

**Behavioral pattern:**

- Ayla responds with a brief contextual greeting.
- Free-text input remains available.
- 3–5 contextual Quick Actions may be shown (for example, "Записаться", "Выбрать услугу", "Узнать о Ayla").
- No Task is created.

### 18.2 Intent-driven first entry

**User:** `Хочу спортивный массаж`

**Behavioral pattern:**

- Ayla does not force a standard introduction.
- Ayla immediately progresses the intent: acknowledges the request, asks a targeted clarification if needed (for example, preferred date/time or specialist), or offers options.
- Task-oriented progression begins.

### 18.3 Returning user, no Active Task

**Context:** User has prior interaction but no Active Task.

**User:** `Привет`

**Behavioral pattern:**

- Ayla greets the user with acknowledgment of the return.
- Ayla may offer the most likely next step based on available context (for example, "Хотите повторить запись к Елене?").
- Free-text input is available.
- No new Task is created automatically.

### 18.4 User with Active Task

**Context:** User has an unfinished booking selection from a previous interaction.

**User:** `Привет`

**Behavioral pattern:**

- Ayla contextualizes the greeting around the Active Task (for example, "Вы искали спортивный массаж. Продолжим?").
- Ayla offers to continue but does not force it.
- Free-text input is available.
- User may continue the Active Task or start a new intent (for example, "Нет, хочу маникюр").

### 18.5 Free-text unexpected intent

**Context:** Quick Actions show booking-related options.

**User:** `Как отменить запись?`

**Behavioral pattern:**

- Ayla recognizes the cancellation intent even though it was not a visible Quick Action.
- Ayla progresses the cancellation intent.
- Quick Actions do not constrain routing.

---

## 19. Explicit non-goals

The following are explicitly out of scope for BOT-001 First Contact:

1. **No mandatory onboarding.** Ayla MUST NOT require a guided onboarding sequence before useful action.
2. **No standalone questionnaire.** Ayla MUST NOT present an "Анкета" object or broad onboarding questionnaire.
3. **No mandatory profile completion.** Ayla MUST NOT require the user to complete a profile before expressing an intent.
4. **No mandatory consent wall.** Consent MUST NOT be a universal first-screen gate.
5. **No independent Mini App conversational implementation.** The Mini App MUST NOT own First Contact conversational logic.
6. **No Mobile App scope.** Mobile App First Contact is excluded from BOT-001.
7. **No behavioral segmentation engine.** MVP segmentation is limited to New User, Returning User and User with an Active Task.
8. **No Task runtime architecture.** This specification does not define Task persistence, API, lifecycle or mapping to Conversation/Session/Interaction.
9. **No API or persistence design.** Payload, transport, storage and runtime contracts are follow-up implementation concerns.
10. **No expansion into BOT-002 discovery.** This specification covers First Contact only.

---

## 20. Acceptance criteria

The following criteria MUST be verifiable for BOT-001 First Contact.

### 20.1 Free text

- AC-1.1: Free-text input is available on the First Contact surface in MAX Bot.
- AC-1.2: Free-text input is available on the First Contact surface in MAX Mini App.
- AC-1.3: Free-text input is not blocked, hidden or delayed by Quick Actions.

### 20.2 Greeting and Task

- AC-2.1: A greeting-only first message does not create a Task.
- AC-2.2: A clear actionable first message is progressed immediately without forced greeting ceremony.
- AC-2.3: A greeting response does not commit the conversation to a fixed path.

### 20.3 Segmentation

- AC-3.1: MVP First Contact supports exactly three greeting states: New User, Returning User, User with an Active Task.
- AC-3.2: No behavioral cohort, RFM, VIP, favorite-service or churn segmentation appears in First Contact.

### 20.4 Quick Actions

- AC-4.1: Quick Actions are optional.
- AC-4.2: No more than 5 Quick Actions are shown at once.
- AC-4.3: Quick Actions are contextually valid for the current state.
- AC-4.4: Quick Actions do not expose unavailable actions.
- AC-4.5: Tapping a Quick Action does not launch a broad questionnaire.

### 20.5 Progressive information collection

- AC-5.1: No standalone questionnaire appears in First Contact.
- AC-5.2: No mandatory profile completion screen appears as a gate.
- AC-5.3: Targeted clarification is allowed when required by intent, Task, booking, safety or consent.

### 20.6 Consent

- AC-6.1: Consent is not presented as a mandatory first-screen gate.
- AC-6.2: Consent is requested at the point where the corresponding processing becomes necessary.

### 20.7 Ownership boundary

- AC-7.1: MAX Bot owns canonical First Contact conversational logic.
- AC-7.2: MAX Mini App does not implement an independent First Contact conversational flow.
- AC-7.3: Mini App behavior is described as rendering/presentation of Bot-owned logic.

### 20.8 Task semantics

- AC-8.1: Task is used as official product language.
- AC-8.2: The specification does not define a Task database table, API, EventBus contract, lifecycle or mapping.
- AC-8.3: Task creation from greeting alone is not described.

---

## 21. Follow-up implementation boundaries

The following items are intentionally deferred to implementation phases. They MUST NOT be treated as decisions made by this specification.

| Topic | Boundary | Follow-up marker |
|---|---|---|
| Task runtime mapping | How Task is persisted, resolved or mapped to Conversation/Session/Interaction. | FOLLOW-UP — TASK RUNTIME MAPPING |
| Bot ↔ Mini App integration | Payload, transport and integration contract. | FOLLOW-UP — BOT MINI APP INTEGRATION CONTRACT |
| Active Task detection | How the system knows a user has an Active Task. | FOLLOW-UP — ACTIVE TASK DETECTION |
| Greeting copy | Exact localized strings for greetings. | FOLLOW-UP — COPY AND LOCALIZATION |
| Quick Action labels | Exact button copy and contextual selection algorithm. | FOLLOW-UP — QUICK ACTION COPY AND SELECTION |
| Consent UX details | Specific consent screens and flows per Consent Scope Registry. | FOLLOW-UP — CONSENT UX DETAILS |
| Intent understanding implementation | NLU model, intent classification and slot filling. | FOLLOW-UP — INTENT UNDERSTANDING IMPLEMENTATION |
| Mobile App | First Contact for Mobile App is out of BOT-001 scope. | FOLLOW-UP — MOBILE APP FIRST CONTACT |

---

## 22. Decision traceability Q1–Q9

Each approved Product Owner decision appears exactly once below. No superseded decision is presented as active.

| Decision ID | Decision | How preserved in this specification |
|---|---|---|
| **Q1** | MAX Bot + MAX Mini App; Mobile App out of scope | §2 Scope; §2.3 Channels; §15 Bot/Mini App ownership; §19 Non-goal #5 and #6. |
| **Q2** | Greeting alone does not create Task; standalone understood intent starts progression | §4 P4; §6.1; §7.1; §16.4; §20.2. |
| **Q3** | Contextual greeting + smart defaults | §4 P3; §6; §8; §9; §10; §17 decision flow. |
| **Q4** | Hybrid First Contact: free-text primary + 3–5 contextual Quick Actions; consent on demand | §4 P2, P7; §11; §12; §14; §20.4; §20.6. |
| **Q5** | No standalone questionnaire; progressive dialogue collection | §4 P5; §13; §19 Non-goal #2; §20.5. |
| **Q6** | Mini App is UI/container; MAX Bot owns First Contact logic | §4 P6; §15; §19 Non-goal #5; §20.7. |
| **Q7** | Minimal segmentation: New User / Returning User / User with an Active Task | §4 P8; §8; §9; §10; §17; §19 Non-goal #7; §20.3. |
| **Q8** | Task is canonical Product Concept; runtime/domain mapping deferred | §3 Definitions (Task); §4 P9; §16; §19 Non-goal #8; §20.8. |
| **Q9** | Intent Before Ceremony (CUX-012) | §4 P1; §7; §17; §18.2; §20.2. |

---

## 23. Canonicalization Record

- **Canonicalization date:** 2026-08-12
- **Canonicalization authority:** Product Owner
- **Canon Review:** READY FOR CANON; 0 blockers; 0 required corrections
- **Canonicalization basis:** Ayla Product Decision & Canon Authoring Process v1.0, Phase 10

**Document status:** CANONICAL
