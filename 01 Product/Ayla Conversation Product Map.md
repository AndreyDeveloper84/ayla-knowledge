---
node_id: ayla.product.conversation-product-map
title: Ayla Conversation Product Map
type: map
status: draft
decision_status: proposed
version: "0.1"
owner: Product Owner
knowledge_area:
  - product
domain:
  - conversation
system_owner:
  - ayla-knowledge
source_repository: ayla-knowledge
source_kind: canonical
canonical_status: candidate
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
depends_on:
  - "[[BOT-001 First Contact Specification]]"
  - "[[BOT-002 Conversation Lifecycle Specification]]"
  - "[[Ayla Intent Model Specification]]"
  - "[[Ayla Conversation Model Specification]]"
  - "[[Ayla MVP Recommendation Contract]]"
  - "[[Ayla MVP Appointment Contract]]"
  - "[[Ayla Memory Model Specification]]"
  - "[[Consent Scope Registry]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Ayla Domain Context Map]]"
  - "[[Ayla Repository Responsibility Matrix]]"
  - "[[Ayla MVP Scope and Release Contract]]"
related:
  - "[[Product Canon Index]]"
  - "[[Ayla Product Vision]]"
  - "[[Ayla Product Principles]]"
  - "[[Ayla Glossary]]"
  - "[[Ayla Core Domain Model Specification]]"
  - "[[Ayla MVP User Journey Specification]]"
  - "[[UX-GAP P1 Registry — Customer Surface]]"
supersedes: []
---

# Ayla Conversation Product Map v0.1

**Status:** DRAFT / proposed / canonical candidate  
**Type:** Navigation and scope map (MOC), not a normative behavioural specification  
**Owner:** Product Owner  
**Scope:** Conversational Product surface across MAX Bot and related channels for the Ayla Controlled Pilot

---

## 1. Purpose

This document is the canonical navigation map of conversational Product responsibilities in Ayla. It exists to answer:

- Where does a conversational rule belong?
- Which specification owns it today?
- What is already canonical, what is planned, and what should not become its own specification?
- Which future Product specifications are actually needed for the Controlled Pilot?

This is a **map / MOC**, not a normative behavioural specification. It does not create Product decisions, runtime architecture, APIs, prompts, or implementation plans. It reduces future specification count by merging capabilities that do not have an independent Product decision surface.

---

## 2. Current Canon

The Product Canon layer currently contains exactly two BOT specifications.

### BOT-001 — First Contact Specification

Ownership:

- Entry into Ayla (MAX Bot, deep link, Mini App).
- Greeting and initial tone.
- Initial intent-driven interaction.
- Quick Actions and their segmentation.
- First Contact segmentation.
- Initial Task emergence from entry.
- Timing of consent disclosures at first contact.
- Bot/Mini App ownership boundary at the entry edge.

### BOT-002 — Conversation Lifecycle Specification

Ownership:

- The hierarchy `Conversation → Goal → Task → Current Focus`.
- Ongoing conversational lifecycle.
- Focus switching and re-anchoring.
- Task progression and completion.
- Conversation closure.
- Safe pause and resumption within a session.
- Relationship between conversational structure and downstream domain actions.

Both documents are Product Canon only. They intentionally do not own UX canon, technical runtime, prompts, or domain state machines.

---

## 3. Conversation Capability Map

| Capability | Product responsibility | Current canonical owner | AI / architecture owner | New Product spec needed? | Depends on BOT-001 / BOT-002 | MVP relevance |
|---|---|---|---|---|---|---|
| First Contact | Entry, greeting, Quick Actions, initial Task emergence | **BOT-001** | Ayla Conversation Model Specification / ai-bot-platform | No | Foundation for all entry paths | Required |
| Ongoing Conversation Lifecycle | Conversation→Goal→Task→Current Focus, focus switching, completion | **BOT-002** | Ayla Conversation Model Specification / ai-bot-platform | No | Foundation for all ongoing dialogue | Required |
| Intent understanding / clarification | Structured intent, slots, confidence, clarification questions | **Ayla Intent Model Specification** | Intent Understanding capability (CAP-003) / ayla-ai-core | No — unless a distinct conversational clarification UI surface emerges | Consumes BOT-002 structure; feeds into Goal/Task | Required (minimal set) |
| Goal understanding | User’s Transformation Goal and its refinement within conversation | **BOT-002** (hierarchy) + Domain specs for detailed Goal model | Core Domain Model / ayla-ai-core | No independent BOT spec | BOT-002 owns the conversational Goal slot | Required (minimal structure) |
| Task progression | Moving a Task toward completion, switching Current Focus | **BOT-002** | Ayla Conversation Model Specification / ai-bot-platform | No | BOT-002 | Required |
| Service / specialist discovery dialogue | Conversational surfacing of search/discovery options before or alongside recommendation | **BOT-003 (proposed)** | Marketplace Search and Discovery (CAP-024) / Recommendation Formation (CAP-004) | **Yes — merged with Recommendation** | BOT-002 | Required |
| Recommendation dialogue | Presenting, explaining, and confirming a recommended next step | **BOT-003 (proposed)** | Recommendation Formation (CAP-004) / Explanation and Context Attribution (CAP-005) / Ayla MVP Recommendation Contract | **Yes — merged with Discovery** | BOT-002 | Required |
| Booking dialogue | Conversational flow to create a booking | **BOT-004 (proposed)** | Appointment Management (CAP-011) / Ayla MVP Appointment Contract | **Yes — merged with Reschedule/Cancel** | BOT-002 | Required |
| Reschedule / cancellation dialogue | Conversational flow to change or cancel an existing booking | **BOT-004 (proposed)** | Appointment Management (CAP-011) / Domain Event Registry | **Yes — merged with Booking** | BOT-002 | Wave 1 simple reschedule/cancel only |
| Failure / recovery | Handling unrecognized intent, no-match, stale slots, dead-ends | **BOT-002** + UX-OD-002 honest self-service terminal fallback | AI Orchestration (CAP-018) / ayla-ai-core | No | BOT-002 | Required |
| Follow-up after completion | Prompting the user after a recommendation was acted on or an appointment completed | **BOT-005 (proposed, LATER)** | Notification Coordination (CAP-021) / Outcome Capture (CAP-006) | **Yes — deferred** | BOT-001 / BOT-002 | Simple transactional prompt only for MVP; full follow-up deferred |
| Feedback / reviews | Collecting structured or free-text feedback | **CAP-012 Feedback Collection** (not a BOT spec) | Feedback Collection capability | No — stays in domain capability; advanced outcome learning deferred | — | Post-MVP advanced |
| Proactive conversation / reminders / triggers | Bot-initiated conversational contact based on events or memory | **BOT-005 (proposed, LATER)** | Notification Coordination (CAP-021) / Memory Retrieval and Rendering (CAP-017) | **Yes — deferred** | BOT-001 / BOT-002 | Transactional notifications required; proactive dialogue deferred |
| Memory-enabled continuity | Using permitted context across turns and sessions | **BOT-002** (session continuity) + **Ayla Memory Model Specification** (persistent memory) | Memory Retrieval and Rendering (CAP-017) / ayla-ai-core | No | BOT-002 (session) | Phase 1 session-only; Phase 2 opt-in persistent |
| Safety / consent conversational boundaries | What the bot may ask, when consent must be obtained conversationally | **Consent Scope Registry** + BOT-001/BOT-002 timing | Consent Management (CAP-002) / Safety Policy (CAP-014) | No | BOT-001 for first-contact consent timing | Required |
| Mini App handoff / rich UI participation | When and how the bot routes to Mini App screens | **UX screen contracts** + BOT specs own Bot-side boundary | ai-bot-platform channel adapters | No | BOT-001 sets ownership boundary | Required |
| Future Mobile surface | Full Mobile App conversational experience | Out of MVP scope | — | No | — | Deferred |

### Key challenges applied

1. **Intent Clarification** — Owned by the Ayla Intent Model Specification and consumed by BOT-002. No separate BOT spec unless a distinct conversational clarification UI pattern is identified.
2. **Goal Discovery** — Part of the Conversation→Goal→Task hierarchy in BOT-002. Detailed Goal model belongs to Domain/Architecture.
3. **Discovery + Recommendation** — **One Product spec** (BOT-003). Discovery without recommendation is search; recommendation without discovery is push. In conversation they are inseparable at the Product surface.
4. **Booking** — **One Product spec** (BOT-004) covering booking, reschedule, and cancellation. These share the same Appointment domain and the same conversational state transitions.
5. **Follow-up** — Part of proactive conversation; deferred to BOT-005 (LATER). Simple transactional post-appointment prompts can be described within BOT-004/BOT-002 until then.
6. **Memory-enabled continuity** — Persistent memory belongs to the Memory Model; session continuity belongs to BOT-002. The map references both without duplicating either.

---

## 4. Proposed Future Specification Set

Minimum recommended future Product specifications:

### BOT-003 — Discovery and Recommendation Conversation

- **Proposed ID:** BOT-003
- **Working title:** Discovery and Recommendation Conversation
- **Exact Product question it owns:** How does Ayla converse with the user to discover needs, present an explainable primary recommendation with alternatives, and reach a chosen next step?
- **Why existing canon cannot own it:** BOT-002 owns generic lifecycle structure but not the Product semantics of discovery/recommendation turns (clarification vs. alternatives vs. explanation vs. acceptance/rejection). The Ayla MVP Recommendation Contract owns the recommendation as a decision record, not the conversational behaviour around it.
- **Dependencies:** BOT-002, Ayla Intent Model Specification, Ayla MVP Recommendation Contract, Ayla Domain Context Map, Ayla Glossary.
- **Controlled Pilot priority:** **NOW**

### BOT-004 — Booking, Reschedule and Cancellation Conversation

- **Proposed ID:** BOT-004
- **Working title:** Booking, Reschedule and Cancellation Conversation
- **Exact Product question it owns:** How does Ayla converse to turn a chosen recommendation (or direct intent) into a confirmed, changed, or cancelled booking?
- **Why existing canon cannot own it:** BOT-002 owns generic Task progression; the Ayla MVP Appointment Contract owns the booking domain state and lifecycle. Neither owns the conversational Product surface for slot suggestions, intent confirmation, pending state, stale-slot recovery, reschedule, or cancellation.
- **Dependencies:** BOT-002, Ayla MVP Appointment Contract, Domain Event Registry, Consent Scope Registry, UX-OD-004 hybrid booking surface, AYLA-DEC-0022 (Wave 1 simple reschedule).
- **Controlled Pilot priority:** **NOW**

### BOT-005 — Proactive Conversation and Follow-up

- **Proposed ID:** BOT-005
- **Working title:** Proactive Conversation and Follow-up
- **Exact Product question it owns:** When and how may Ayla initiate a conversation, send reminders, or follow up after completion, and what conversational constraints apply?
- **Why existing canon cannot own it:** BOT-001 covers entry in response to user action; BOT-002 covers reactive lifecycle. Neither covers bot-initiated contact, notification-to-dialogue transitions, or follow-up cadence.
- **Dependencies:** BOT-001, BOT-002, Ayla Memory Model Specification, Domain Event Registry, Notification Coordination capability (CAP-021), Consent Scope Registry.
- **Controlled Pilot priority:** **LATER** (transactional notifications are required, but the conversational proactive layer can be minimal in MVP and fully canonicalized later)

---

## 5. Candidates That Should NOT Become Separate BOT Specs

| Subject | Why it should not be a separate BOT spec | Rightful owner |
|---|---|---|
| Low-level Intent classification | Intent types, slots, confidence, and clarification structure are owned by the Intent Model. Conversation consumes them. | Ayla Intent Model Specification |
| Slot filling | Part of Intent Understanding and AI orchestration; not a Product decision surface on its own. | Ayla Intent Model Specification / AI Orchestration (CAP-018) |
| Prompt engineering | Prompt composition, version selection, and channel-specific instructions are implementation/runtime concerns. | ayla-ai-core (composition), ai-bot-platform (runtime registry) |
| Task persistence | How Tasks are stored, replayed, or resumed across turns is a runtime concern. | ai-bot-platform / Ayla Conversation Model Specification |
| Conversation state machine | The abstract lifecycle of Conversation/Session/Turn is an architecture concern. | Ayla Conversation Model Specification |
| Recommendation ranking | How candidates are scored, gated, and ordered is owned by Recommendation Formation. | Ayla MVP Recommendation Contract / Recommendation Formation (CAP-004) |
| Booking domain state | Appointments, slots, holds, status transitions, and eligibility are domain state. | Ayla MVP Appointment Contract / Appointment Management (CAP-011) / beautygo_backend |
| Memory storage / retrieval | Durable memory lifecycle, consent gates, and provenance belong to the Memory Model. | Ayla Memory Model Specification / Memory Retrieval and Rendering (CAP-017) |
| Notifications transport | Delivery via MAX/Telegram/push is a technical transport capability. | Notification Coordination (CAP-021) / ai-bot-platform |
| Mini App surface | Screen layout, deep-link targets, and channel UX are UX canon. | UX screen contracts / UX-OD-004 / UX-OD-005 |
| Human handoff | Operator chat thresholds, SLA, and operational procedures are operations/post-MVP concerns. | Pilot Operations Runbook (post-MVP) |
| Marketplace search as generic search | Non-conversational catalog search is a separate capability. | Marketplace Search and Discovery (CAP-024) |
| Advanced feedback / reviews | Structured feedback, ratings, and outcome learning are domain capabilities. | Feedback Collection (CAP-012) / Outcome Learning (CAP-007) |

---

## 6. End-to-End User Conversation Map

This is a high-level conceptual flow, not a rigid state machine.

```text
User enters Ayla
        ↓
BOT-001 First Contact
  • greeting, Quick Actions, initial intent, consent timing
        ↓
BOT-002 Conversation Lifecycle
  • Conversation → Goal → Task → Current Focus
        ↓
Intent / Goal clarification
  • Ayla Intent Model Specification feeds structured intent
  • BOT-002 manages Goal/Task slots
        ↓
[branch] Direct task (e.g., “show my bookings”) → BOT-004 / Mini App
[branch] Need discovery → BOT-003 Discovery and Recommendation Conversation
        ↓
BOT-003 Discovery and Recommendation Conversation
  • clarifying turns, alternatives, explanation, acceptance/rejection
        ↓
Chosen next step
  • no action (valid outcome)
  • book / reschedule / cancel → BOT-004
  • other action → relevant domain flow
        ↓
BOT-004 Booking, Reschedule and Cancellation Conversation
  • slot suggestions, intent confirmation, pending state, stale-slot recovery
  • handoff to Mini App for expanded calendar/details
        ↓
Outcome
  • appointment confirmed / changed / cancelled
        ↓
[deferred] BOT-005 Proactive Conversation and Follow-up
  • transactional notification
  • follow-up prompt, reminder, memory candidate
        ↓
Memory-enabled continuity
  • session continuity (BOT-002)
  • persistent memory (Memory Model, Phase 2 opt-in)
```

Branching notes:

- The user may enter at any point via deep link; BOT-001 defines entry semantics.
- Focus may switch within BOT-002 at any time; a discovery Task may become a booking Task without leaving the Conversation.
- Booking may be skipped entirely; “do nothing” is a valid recommendation outcome.
- Proactive/follow-up layer is shown as deferred; MVP transactional notifications are not blocked by its absence.

---

## 7. Ownership Matrix

| Capability | Product Canon Owner | AI / Architecture Owner | Domain Owner | Surface |
|---|---|---|---|---|
| First Contact | BOT-001 | Ayla Conversation Model Specification / ai-bot-platform | Conversation Experience (CAP-016) | MAX Bot, Mini App entry |
| Conversation Lifecycle | BOT-002 | Ayla Conversation Model Specification / ai-bot-platform | Conversation Experience (CAP-016) | MAX Bot |
| Intent Understanding | Ayla Intent Model Specification | Intent Understanding (CAP-003) / ayla-ai-core | — | MAX Bot |
| Goal / Task hierarchy | BOT-002 | Ayla Conversation Model Specification / Core Domain Model | Conversation Experience (CAP-016) | MAX Bot |
| Discovery / Recommendation dialogue | BOT-003 (proposed) | Recommendation Formation (CAP-004) / Explanation and Context Attribution (CAP-005) / ayla-ai-core | Ayla MVP Recommendation Contract | MAX Bot, Mini App |
| Booking dialogue | BOT-004 (proposed) | Appointment Management (CAP-011) / ayla-ai-core | Ayla MVP Appointment Contract / beautygo_backend | MAX Bot, Mini App |
| Reschedule / Cancel dialogue | BOT-004 (proposed) | Appointment Management (CAP-011) / ayla-ai-core | Ayla MVP Appointment Contract / Domain Event Registry | MAX Bot, Mini App |
| Failure / recovery | BOT-002 + UX-OD-002 | AI Orchestration (CAP-018) / ayla-ai-core | — | MAX Bot |
| Follow-up / proactive conversation | BOT-005 (proposed, LATER) | Notification Coordination (CAP-021) / Memory Retrieval and Rendering (CAP-017) | Ayla Memory Model Specification / Domain Event Registry | MAX Bot, Mobile |
| Memory continuity (session) | BOT-002 | Ayla Conversation Model Specification / ai-bot-platform | — | MAX Bot |
| Memory continuity (persistent) | Ayla Memory Model Specification | Memory Retrieval and Rendering (CAP-017) / ayla-ai-core | beautygo_backend (durable facts) | MAX Bot, Mobile |
| Consent conversational boundaries | Consent Scope Registry + BOT-001/BOT-002 timing | Consent Management (CAP-002) | Consent Scope Registry | MAX Bot, Mini App, Mobile |
| Mini App handoff | UX screen contracts; BOT specs own Bot-side boundary | ai-bot-platform channel adapters | — | MAX Mini App |
| Notifications transport | — (not a Product spec) | Notification Coordination (CAP-021) / ai-bot-platform | — | MAX Bot, Mobile |

Unresolved ownership is not marked because every row maps to an existing canon owner or a proposed Product spec.

---

## 8. Dependency Graph

```text
                    Ayla Product Vision
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   BOT-001           BOT-002           Ayla Intent Model
   First Contact     Conversation      Specification
        │            Lifecycle               │
        │                  │                 │
        └────────┬─────────┘                 │
                 │                            │
                 ▼                            ▼
            BOT-003 ◄──────────────── Ayla MVP Recommendation Contract
   Discovery and Recommendation      Ayla Domain Context Map
            Conversation
                 │
                 ▼
            BOT-004 ◄──────────────── Ayla MVP Appointment Contract
   Booking, Reschedule and          Domain Event Registry
            Cancellation            Consent Scope Registry
            Conversation
                 │
                 ▼
            [BOT-005] ◄───────────── Ayla Memory Model Specification
   Proactive Conversation and       Notification Coordination (CAP-021)
            Follow-up               Domain Event Registry
```

BOT-001 and BOT-002 form the foundation. BOT-003 and BOT-004 are the next required layer. BOT-005 depends on the earlier specs plus Memory Model and Notification Coordination.

---

## 9. Controlled Pilot Cut

### Must canonicalize next

- **BOT-003 — Discovery and Recommendation Conversation.** Without it, the core value loop (intent → recommendation → chosen next step) has no Product owner for conversational behaviour.
- **BOT-004 — Booking, Reschedule and Cancellation Conversation.** Required for the pilot’s booking optionality and Wave 1 simple reschedule/cancel.

### Can operate under existing canon

- First Contact behaviour (BOT-001).
- Generic conversation lifecycle (BOT-002).
- Intent clarification within the lifecycle (Ayla Intent Model Specification + BOT-002).
- Failure/recovery honest self-service fallback (BOT-002 + UX-OD-002).
- Simple Mini App handoff boundaries (BOT-001 + UX screen contracts + UX-OD-004/005).
- Session-level memory continuity (BOT-002).
- Transactional notification delivery as a technical capability (CAP-021 / ai-bot-platform).

### Can defer

- **BOT-005 — Proactive Conversation and Follow-up.** Transactional notifications can be handled as simple prompts under BOT-002/BOT-004 until the proactive layer is canonicalized.
- Advanced feedback / reviews (CAP-012 / CAP-007).
- Human handoff to operator (post-MVP).
- Full marketplace search as a standalone non-conversational capability (CAP-024).
- Phase 2 opt-in persistent memory (Memory Model already owns the boundary).
- Telegram channel (explicitly out of MVP scope per AYLA-DEC-0004).

---

## 10. Recommended Next Document

**Recommended next Product decision cycle:** **BOT-003 — Discovery and Recommendation Conversation**

**Why it has the highest leverage for the pilot:**

It unlocks the central Ayla experience: understanding the user, discovering needs, forming an explainable recommendation, and agreeing on a next step. It sits at the intersection of Intent Model, Recommendation Contract, Conversation Lifecycle, and Mini App handoff. Decisions made here cascade into booking (BOT-004) and proactive follow-up (BOT-005), but booking cannot be conversationalized until it is clear what is being booked and why.

**Scope:**

- Conversational triggers that initiate discovery vs. direct recommendation.
- How the bot presents primary and alternative recommendations.
- Explanation of context usage and recommendation reasoning.
- User acceptance, rejection, and correction flows.
- When the conversation stays in Bot DM vs. hands off to Mini App.
- How discovery/recommendation results update Goal/Task/Current Focus.
- Fallbacks when no recommendation can be formed.

**What it will NOT own:**

- Recommendation scoring, ranking, or safety gating (Ayla MVP Recommendation Contract).
- Appointment lifecycle or slot availability (Ayla MVP Appointment Contract).
- Generic conversation structure (BOT-002).
- Intent slot structure (Ayla Intent Model Specification).
- Prompts, model routing, or runtime orchestration (ai-bot-platform / ayla-ai-core).
- Mini App screen design (UX screen contracts).

**5–10 initial Product questions (not answered here):**

1. What conversational triggers initiate discovery vs. direct recommendation?
2. How does the bot signal confidence in a recommendation and offer alternatives?
3. What user corrections reset vs. refine a recommendation?
4. When must the bot explicitly explain which context was used?
5. What is the boundary between bot-driven clarification and Mini App expanded discovery?
6. How is recommendation acceptance or rejection carried into the next Task/Goal?
7. What happens when no recommendation can be formed?
8. How does the conversation preserve attribution across turns?
9. What safety or consent gates must be conversationally resolved before a recommendation?
10. What is the fallback when the user rejects all alternatives?

---

## Deliverables Checklist

- Map path: `01 Product/Ayla Conversation Product Map.md`
- Current canonical BOT specs: **BOT-001 First Contact Specification**, **BOT-002 Conversation Lifecycle Specification**
- Recommended future Product spec count: **3** (BOT-003, BOT-004, BOT-005)
- Proposed future spec list: see §4
- Capabilities explicitly NOT getting separate specs: see §5
- Controlled Pilot canon gaps: see §9
- Recommended next decision cycle: **BOT-003 — Discovery and Recommendation Conversation**
- Owner decisions required before starting it: **none identified** — ownership follows existing canon or proposed Product spec boundary

---

**Final status:** `READY FOR PRODUCT OWNER ROADMAP REVIEW`
