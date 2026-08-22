---
node_id: ayla.product.conversation-design-principles
title: Ayla Conversation Design Principles
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
  - ayla-knowledge
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
updated: 2026-08-13
review_cycle: monthly
depends_on:
  - "[[Ayla Product Essence]]"
  - "[[Ayla Product Principles]]"
  - "[[BOT-001 First Contact Specification]]"
  - "[[BOT-002 Conversation Lifecycle Specification]]"
  - "[[Ayla Conversation Product Map]]"
  - "[[Ayla Glossary]]"
related:
  - "[[Ayla Conversation Model Specification]]"
  - "[[Ayla Intent Model Specification]]"
  - "[[Ayla MVP Recommendation Contract]]"
  - "[[Ayla Memory Model Specification]]"
  - "[[Consent Scope Registry]]"
  - "[[Product Canon Index]]"
supersedes: []
open_schema_question: >
  A dedicated `principles` document type is not registered in
  `.knowledge/schema.yaml`. `specification` is used as the closest registered
  normative type for a Product-layer document, consistent with the precedent
  noted in `Ayla Product Principles` (`foundation` used for an unregistered
  `product-principles` type). Registration of an explicit type is a separate
  schema decision.
---

# Ayla Conversation Design Principles

**Status:** CANONICAL
**Version:** 1.0
**Scope:** All Ayla conversational Product experiences
**Implementation:** FORBIDDEN in this document

---

## 1. Purpose

This document defines the universal Product principles that govern **every Ayla conversational experience**, regardless of which conversational capability is currently being performed: First Contact, clarification, discovery, recommendation, booking, reschedule, cancellation, recovery, follow-up or proactive interaction.

It answers one question:

> What must remain true regardless of which conversational capability Ayla is currently performing?

This document is consumed by:

- `BOT-001 First Contact Specification` (canonical);
- `BOT-002 Conversation Lifecycle Specification` (canonical);
- future BOT-003 Discovery and Recommendation Conversation;
- future BOT-004 Booking, Reschedule and Cancellation Conversation;
- future BOT-005 Proactive Conversation and Follow-up;
- conversational UX on MAX Bot;
- Bot-side boundaries with Mini App;
- future conversational surfaces where applicable.

This is **not** a BOT specification. It does not describe individual flows and does not duplicate behaviour owned by BOT-001 or BOT-002. It extracts the stable cross-cutting principles those specifications already honour, so that future conversational specifications inherit them by reference instead of re-deciding them.

---

## 2. Status and Authority

This document is **canonical**. It became canonical through the Ayla Product Decision & Canon Authoring Process and the Ayla Canon Review Standard, with Product Owner approval (see §9, Canonicalization Record).

Where this document and another canonical specification appear to conflict, the conflict must be reported, not silently resolved.

### 2.1. Relationship to Ayla Product Principles

`Ayla Product Principles` defines the **universal Product decision rules** for all of Ayla (Human First, Goal at the Center, Honest Representation, User Outcome First, and the rest).

This document defines the **application of those rules to conversational Product behaviour**, plus the conversational invariants established by BOT-001 and BOT-002.

The distinction:

- A Product Principle says *what is always true for the product* (e.g., User Outcome First).
- A Conversation Design Principle says *what that means inside a conversation* (e.g., a Task completes on user outcome, not on system action; a completed Task must not manufacture a new one).

This document derives from Ayla Product Principles; it does not compete with it, restate it wholesale, or create a parallel value system. If a proposed conversational rule is already fully expressed by a Product Principle with no conversation-specific constraint, it does not belong here.

### 2.2. Relationship to BOT specifications

Conversation Design Principles define **cross-cutting invariants**. BOT specifications define **capability-specific Product behaviour**.

```text
            Ayla Conversation Design Principles
            (cross-cutting invariants)
                          ↓
        ┌─────────┬──────┴───────┬──────────┐
        ▼         ▼              ▼          ▼
     BOT-001   BOT-002        BOT-003    BOT-004 …
   (canonical, (canonical,   (future)   (future)
    entry)     lifecycle)
```

BOT specifications are **not** a linear lifecycle hierarchy. Each BOT specification owns one conversational capability; they are connected through BOT-002, which owns the generic lifecycle foundation. A user journey may branch between capabilities at any time.

### 2.3. What this document does not do

In accordance with its authoring window, this document does NOT:

- rewrite, amend or reinterpret BOT-001 or BOT-002;
- start BOT-003, BOT-004 or BOT-005;
- define recommendation ranking, booking lifecycle or memory persistence;
- define APIs, prompts, runtime state, LLM behaviour or screen layouts;
- create implementation tasks;
- promote working decisions to canon.

---

## 3. How to Read the Principles

Each principle uses a fixed format:

- **Rule** — one concise normative statement.
- **Why** — the Product reason.
- **Applies to** — the conversational capabilities it governs.
- **Does NOT mean** — common misinterpretations, explicitly excluded.
- **Canon basis** — the existing canonical sources and approved decisions that support it.
- **Product test** — questions a reviewer can ask of any future conversational design.

Authority labels used below: approved/canonical sources are normative; `CANDIDATE SUPPORTING BASIS — NON-CANONICAL` sources provide traceability but do not carry
canonical authority; `WORKING EVIDENCE — non-canonical` is supporting evidence only.

The principles are Product-level. They constrain *what the conversation must be like for the user*, never *how the system implements it*.

The twelve principles group into four themes:

| Theme | Principles |
|---|---|
| **A. Follow the user's goal** | CDP-01, CDP-02, CDP-03 |
| **B. Keep the user in control** | CDP-04, CDP-05, CDP-06, CDP-07 |
| **C. Preserve continuity and truth** | CDP-08, CDP-09, CDP-10 |
| **D. Optimize for outcome, not activity** | CDP-11, CDP-12 |

---

## Theme A — Follow the user's goal

## CDP-01 — Goal Before Mechanism

### Rule

Every Ayla conversation orients around what the user is trying to achieve — the user's Goal — and never requires the user to understand Ayla's services, categories, screens or internal structure in order to make progress.

### Why

Ayla is not a service catalogue with a chat wrapper: services, specialists and booking are instruments on the user's path, not centres of the product. The canonical hierarchy — Conversation → Goal → Task → Current Focus — already fixes Goal above every conversational work item. A conversation organised around product structure forces the user to adapt to the system; a conversation organised around the Goal lets the system adapt to the user.

### Applies to

All conversational capabilities: First Contact, clarification, discovery, recommendation, booking, reschedule, cancellation, recovery, follow-up, proactive interaction.

### Does NOT mean

- The user must explicitly articulate a Transformation Goal before anything useful happens — an actionable intent is enough to begin a Task (BOT-001 §16.4).
- Ayla never asks clarifying questions — targeted clarification in service of the Goal is expected.
- Domain structure (services, slots, providers) is hidden from the user when it becomes relevant to their Goal.

### Canon basis

- `BOT-002` §3–§4 (Goal above Task; Conversation organised around a Goal or Goal cluster; MM-D1).
- `BOT-001` §16 (Task presupposes a user Goal).
- `Ayla Product Principles` v0.2 — **CANDIDATE SUPPORTING BASIS — NON-CANONICAL** 4.2 (Goal at the Center).
- `Ayla Product Essence` v1.2 — **CANDIDATE SUPPORTING BASIS — NON-CANONICAL** §1, §20 (Ayla is not a catalogue; Transformation Goal is the centre).
- `Ayla Glossary` §4 (Goal is not a service or an action).

### Product test

- Can the user reach a useful next step by stating what they want, without learning Ayla's menu, category or screen structure first?
- Does each conversational step trace to a user Goal rather than to an internal product module?

---

## CDP-02 — Intent Before Ceremony

### Rule

When the user's intent is sufficiently clear, useful progression of that intent begins immediately; no greeting, onboarding, introduction, category selection or other conversational ceremony may delay it.

### Why

This principle is canonical in BOT-001 (P1, Q9) and BOT-002 explicitly extends it to the ongoing conversation (§5.2). Ceremony that delays a clear intent spends the user's patience on the product's process instead of the user's goal. The cross-conversation formulation is identical in force to the BOT-001 original; nothing in this document weakens it.

### Applies to

First Contact and every subsequent conversational capability — an explicit new intent at any point in an ongoing conversation is honoured immediately, including when it changes the Current Focus (BOT-002 §6.3, cause 1).

### Does NOT mean

- Ayla must act on ambiguous input without understanding it — where intent is not sufficiently clear, clarification is the useful progression (Intent Model: guessing at low confidence is forbidden).
- Warmth is forbidden — a brief acknowledgment that does not delay the actionable response is acceptable (BOT-001 §7.2).
- Safety or consent gates are skipped — they apply at the point of need (CDP-07).

### Canon basis

- `BOT-001` P1, Q9, §7, §17 (Intent Before Ceremony, CUX-012).
- `BOT-002` §5.2, §6.3 (intent-driven progression and focus change in the ongoing Conversation).
- `Ayla Canon Review Standard` §2 (intent-first as protected Product philosophy).

### Product test

- If the user's first or next message already contains a clear actionable intent, does anything — greeting, onboarding, category picker, questionnaire — still delay the actionable response?
- Does a new explicit intent mid-conversation take effect immediately, or is it queued behind a scripted step?

---

## CDP-03 — Conversation Leads, Surfaces Assist

### Rule

Natural language remains a first-class path to every supported intent; Quick Actions, cards, Mini App UI and future surfaces support and accelerate the conversation but never replace the user's ability to express intent in their own words — and the same canonical Product semantics apply on every surface.

### Why

Free-text input is canonical primary interaction (BOT-001 P2, §11): Quick Actions are optional contextual accelerators, not navigation or menus, and must never constrain routing. The Mini App exists for scenarios chat cannot serve well (Glossary §10), and handoff to it is legitimate — but the canonical conversational logic is owned once (BOT-001 P6, CUX-010) and rendered per surface, so the user meets the same product, not per-channel re-implementations. Conversation identity and continuity survive channel changes (Conversation Model §19–§21).

### Applies to

All conversational capabilities and all surfaces: MAX Bot, Mini App rendering of Bot-owned flows, future Mobile where applicable.

### Does NOT mean

- Every task must stay inside chat — rich UI (calendars, lists, selectors) and Mini App handoff are legitimate where chat is insufficient.
- Every surface must offer identical UI — rendering is channel-specific; Product semantics are not (BOT-001 §5).
- Quick Actions or cards are forbidden — they are welcome as optional accelerators.

### Canon basis

- `BOT-001` P2, §11, §12 (free text primary; Quick Actions optional and non-constraining); P6, §15 (single canonical conversational logic, CUX-010); §5 (channel-agnostic logic, channel-specific rendering).
- `Ayla Conversation Model Specification` §19–§21 (cross-channel continuity; channel change ≠ new Conversation).
- `Ayla Glossary` §10 (Mini App serves scenarios chat cannot).

### Product test

- Can the user express any supported intent in free text even when no matching button is shown?
- Do buttons or cards ever become the only way to reach a supported intent?
- Does moving between Bot and Mini App preserve the same conversational meaning and ownership, or does the user meet a different product?

---

## Theme B — Keep the user in control

## CDP-04 — One Current Focus, User-Controlled Switching

### Rule

A conversation keeps exactly one coherent Current Focus; the user may change direction at any time, Ayla may propose a change, and Ayla never redirects the Current Focus silently.

### Why

Attention coherence is what makes a conversation feel like one story instead of competing threads. BOT-002 fixes the mechanics: Current Focus belongs to the Conversation, exactly one Task holds it, and it changes only through explicit new user intent, explicit return, explicit abandonment or Task completion (MM-D2, MM-D4, MM-D5). This principle carries the *behavioural invariant* into every capability without restating the lifecycle mechanics: any capability that quietly steers the user to a different topic breaks trust, however helpful the intent.

### Applies to

All conversational capabilities operating inside an ongoing conversation — most critically discovery, recommendation, booking and proactive interaction, where the temptation to redirect is highest.

### Does NOT mean

- Ayla can never suggest a change of direction — it may offer; the user decides (BOT-002 §5.6: an offer changes nothing until explicitly accepted).
- Clarification within the current work counts as a switch — it is part of the current Task (BOT-002 §5.3).
- Unfinished work is lost when focus moves — it remains and may be returned to (BOT-002 §6.2).

### Canon basis

- `BOT-002` §4, §5.4, §6 (MM-D2, MM-D4, MM-D5; Ayla never switches Current Focus silently).
- `BOT-001` §9.3, §10.1 (user may always start a new intent; continuation is offered, never forced).

### Product test

- Can the user name, at any moment, what the current exchange is serving?
- Does any Ayla message move the conversation to different work without an explicit user signal?
- When Ayla proposes a change, does the proposal wait for explicit acceptance?

---

## CDP-05 — User Agency Over Automation

### Rule

Ayla may suggest, clarify, recommend and guide, but it never silently takes a consequential conversational decision on the user's behalf where canon requires user choice.

### Why

Trust is the precondition of the entire product cycle: the user opens context only to a system they control. Canon fixes user choice at every consequential point: focus changes only on explicit user signals (BOT-002 MM-D5); recommendation acceptance is an explicit user selection and decline is explicit only (Recommendation Contract §17); continuing unfinished work is offered, never forced (BOT-001 §10.1); persistent memory crosses a consent gate (Product Principles 4.5). A system that quietly decides for the user may look efficient and is in fact a trust failure.

### Applies to

Focus switching, recommendation acceptance or rejection, booking commitment, reschedule and cancellation, consent and memory persistence, proactive contact.

### Does NOT mean

- Ayla must ask permission for every conversational step — progression within the user's expressed intent requires no per-step confirmation.
- Ayla cannot have a point of view — a clear primary recommendation is desirable (Product Principles 4.6); the decision remains the user's.
- Routine, reversible, clearly-signalled conveniences are forbidden — this principle governs consequential decisions, not every micro-interaction.

### Canon basis

- `BOT-002` §6.3 (MM-D5); §5.6 (offer, never force).
- `BOT-001` §10.1 (continuation never forced).
- `Ayla Product Principles` v0.2 — **CANDIDATE SUPPORTING BASIS — NON-CANONICAL** 4.6 (final decision always with the user), 4.8 (User in Control).
- `Ayla MVP Recommendation Contract` v0.3 — **SUPPORTING CANDIDATE BASIS — NON-CANONICAL** (§17 acceptance is explicit user choice; inaction ≠ decline).
- `Ayla Memory Model Specification` §7 (silence ≠ confirmation; dialogue continuation ≠ confirmation).

### Product test

- Which decisions in this flow commit the user to something — and does each one require an explicit user signal?
- Does user inaction ever get interpreted as acceptance, agreement or consent?

---

## CDP-06 — Ask Only at the Point of Need

### Rule

A conversation asks only for the information required by the user's current progression — a specific intent, Task, booking, safety or consent requirement — and never fronts broad questionnaires, premature profiling or re-asking of stable information Ayla already has and has reason to trust.

### Why

Progressive information collection is canonical for First Contact (BOT-001 P5, §13) and BOT-002 extends it into ongoing clarification (§5.3). Each unnecessary question is friction between the user and their goal; each repeated question signals that Ayla does not remember, which undermines continuity. Data minimisation is also the default in canon: collection "for later" without a user-visible purpose is an explicit anti-pattern (Product Principles 4.5, §6 Personalization vs minimization).

### Applies to

All conversational capabilities that collect information: First Contact, clarification, discovery, recommendation, booking, cancellation, follow-up.

### Does NOT mean

- Ayla never asks questions — targeted clarification in service of the current progression is a core conversational tool.
- Known information is never re-confirmed — dynamic or time-sensitive facts are revalidated before action under CDP-08; this principle protects *stable* information from gratuitous re-asking.
- Personalization is forbidden — it proceeds progressively, with consent, as it becomes useful.

### Canon basis

- `BOT-001` P5, §13 (progressive collection only; questionnaire patterns forbidden; Q5).
- `BOT-002` §5.3 (clarification inside a Task stays targeted), §5.6 (stable context continues without unnecessary re-asking).
- `Ayla Product Principles` v0.2 — **CANDIDATE SUPPORTING BASIS — NON-CANONICAL** 4.5 (no collection "on future spec"), §6 (minimization by default).
- `Consent Scope Registry` §3 (session use vs persistent consent distinction).

### Product test

- Does this interaction make the user repeat stable information Ayla already has and has reason to trust?
- Is every question traceable to the current intent, Task, booking, safety or consent requirement — or is some of it profiling "for later"?

---

## CDP-07 — Consent and Safety at the Point of Need

### Rule

Consent, privacy and safety requirements constrain the conversation exactly where the corresponding processing, persistence or risk arises — requested in the context of the specific flow that needs them — and never as a universal upfront gate on conversation itself.

### Why

BOT-001 fixes consent timing canonically: consent is requested at the point where processing or persistence of personal data becomes necessary, not as a first-screen wall (P7, §14). The Consent Scope Registry confirms the underlying model: processing the user's current message within the session needs no separate consent; persistence, reuse across sessions, proactive use and transfer do — fail-closed (CSR §2–§3). Upfront gating would both violate canon and destroy First Contact; absent gating at the real point of need would violate privacy and safety canon. The timing is the principle.

### Applies to

All conversational capabilities — with particular force at First Contact, memory persistence, recommendation personalization, booking personal data, and proactive contact.

### Does NOT mean

- Consent is optional or deferrable past the point where the corresponding processing begins — the gate is fail-closed (CSR §2).
- Safety boundaries yield to conversational momentum — safety constraints outrank goals, preferences and commercial factors (Glossary §5, Safety Constraint; Product Principles Hard Precedence Layer).
- Every conversation must contain a consent moment — one arises only when a flow actually requires it.

### Canon basis

- `BOT-001` P7, §14 (consent on demand; no mandatory first-screen gate; Q4).
- `Consent Scope Registry` §2 (fail-closed; scope-specific permission), §3 (session use vs persistent consent).
- `Ayla Product Principles` v0.2 — **CANDIDATE SUPPORTING BASIS — NON-CANONICAL** 4.5 (persistent memory crosses policy/consent gate), §3 (Hard Precedence Layer: safety and autonomy above outcome, engagement, commercial).
- `Ayla Glossary` §9 (Consent is purpose-specific, revocable; silence is not consent).

### Product test

- Is any consent requested before the flow that actually needs it — or after the processing it was meant to authorize?
- Can the user reach useful value without passing through a consent or data-collection wall unrelated to their current intent?

---

## Theme C — Preserve continuity and truth

## CDP-08 — Preserve Meaning, Revalidate Reality

### Rule

Across pauses, returns and resumed conversations, Ayla preserves the meaning of the exchange — goals, preferences, unfinished work and relevant context — while treating dynamic, time-sensitive or externally changeable facts as unconfirmed until refreshed from an authoritative source or re-confirmed with the user before acting on them.

### Why

Continuity is Ayla's core promise: the user never starts from zero (Product Principles 4.5; Essence §13, Memory). But continuity of meaning is not currency of facts: availability, prices, schedules and similar facts change outside the conversation, and acting on them stale is an honesty failure. BOT-002 fixes the balance canonically (§5.6, PD-03): preserve meaning, selectively revalidate what may be stale, and do not re-ask stable context unnecessarily. This is a Product principle; freshness durations, TTLs and revalidation mechanisms are runtime concerns outside it.

### Applies to

Resumption after any gap, proactive re-contact, booking and reschedule (stale slots), recommendation (stale availability or price), follow-up.

### Does NOT mean

- Every fact is re-confirmed on every resume — stable context with no reasonable indication of staleness continues without unnecessary re-asking (BOT-002 §5.6).
- Ayla defines freshness windows or TTLs here — no freshness algorithm is Product Canon (BOT-002 §9).
- Conversation context is persistent memory — the boundary between conversational context and Memory remains with BOT-002 follow-ups and the Memory Model (§7: Conversation Context ≠ Persistent Memory).

### Canon basis

- `BOT-002` §5.6, §8 (BOT-002-PD-03: preserve meaning, selectively revalidate, no unnecessary re-asking).
- `Ayla Conversation Model Specification` §20–§21 (pause ≠ closure; resumption preserves identity while semantic continuity remains).
- `Ayla Memory Model Specification` §7 (memory is context, not truth; conversation context ≠ persistent memory).
- `Ayla MVP Recommendation Contract` v0.3 — **SUPPORTING CANDIDATE BASIS — NON-CANONICAL** (§22 expired recommendation requires refresh; booking revalidates availability and price).

### Product test

- Before acting, does the design distinguish stable context from dynamic facts that may have changed since they were obtained?
- Does a resumed conversation preserve what the user meant — or does it either restart from zero or silently trust stale facts?

---

## CDP-09 — Honest Representation

### Rule

In conversation, Ayla never presents stale information as current, unavailable actions as possible, uncertain conclusions as certain, or a system action as an achieved user outcome — and says so plainly when it does not know, cannot do, or has failed.

### Why

Trust in the entire path rests on honesty of representation: one class-of-certainty substitution devalues everything the product shows (Product Principles 4.4). Canon forbids guessing at low confidence (Intent Model: low confidence must return clarification or UNKNOWN), prefers `Unknown` to an invented answer (Glossary §6), and requires honest failure without fake operator or imitation of live support (Product Principles 4.4; UX-OD-002 — WORKING EVIDENCE, non-canonical). A conversation that bluffs may win a turn and lose the user.

### Applies to

All conversational capabilities — especially recommendation (certainty of fit), booking (availability, confirmation state), recovery (failure admission) and proactive interaction (signalled basis).

### Does NOT mean

- Every message carries confidence disclaimers — a stream of disclaimers over insignificant matters is itself an anti-pattern (Product Principles 4.6).
- Ayla cannot make recommendations under uncertainty — it recommends with honest indication of basis and limits, per the Explanation Contract.
- Uncertainty blocks safe progression — clarification and safe intermediate steps remain available.

### Canon basis

- `Ayla Product Principles` v0.2 — **CANDIDATE SUPPORTING BASIS — NON-CANONICAL** 4.4 (Honest Representation; Observation ≠ Confirmed Fact; AI Inference ≠ User Fact; no deceptive precision).
- `Ayla Product Essence` v1.2 — **CANDIDATE SUPPORTING BASIS — NON-CANONICAL** §8, §14 (classes of certainty never substituted; acknowledge insufficient data).
- `Ayla Glossary` §6 (Unknown preferred to an invented answer).
- `Ayla Intent Model Specification` (Confidence and Clarification: guessing forbidden at low confidence).
- `Ayla MVP Recommendation Contract` v0.3 — **SUPPORTING CANDIDATE BASIS — NON-CANONICAL** §12–§13 (explanation derived from the real decision; stale evidence marked).

> **WORKING EVIDENCE — non-canonical:** `UX-OD-002` documents an honest terminal-fallback posture (no fake operator availability, no imitation of live support). It is retained for historical context but does not carry canonical authority.

### Product test

- Could the user tell, from the conversation alone, which statements are facts, which are estimates, and which are proposals?
- When Ayla cannot do something or something failed, does the conversation say so — or does it improvise availability, certainty or success?

---

## CDP-10 — Graceful Recovery, Not Reset

### Rule

When something in a conversation fails — an unrecognized intent, a stale slot, an unavailable action, a dead end — Ayla preserves valid user context, states the changed condition honestly, and offers or continues with a viable next step toward the user's Goal where one exists. The owning BOT specification determines the domain-specific recovery behaviour.

### Why

Failure is where continuity is most easily lost and where honesty is most tested. Canon already fixes the recovery posture: honest failure messages, preserved safe session context, and a viable next step where one exists — without fake rescue (CDP-09; UX-OD-002 — WORKING EVIDENCE, non-canonical). BOT-002's pause/resume semantics mean a failure or gap does not destroy the conversation or its meaning (§5.5–§5.6). Recovery that resets the user to zero punishes them for the system's failure.

### Applies to

All conversational capabilities: misunderstanding recovery, no-match discovery, booking failure and stale-slot recovery, cancellation failure, tool unavailability, proactive misfires.

### Does NOT mean

- Failure is hidden or smoothed over — the changed condition is stated honestly (CDP-09); pretending a failed action succeeded is strictly worse than a reset.
- Domain-specific recovery flows are defined here — they belong to the owning BOT specifications (e.g., stale-slot recovery to future BOT-004).
- Recovery loops forever — bounded clarification attempts and an honest terminal state are canon (Intent Model: max two consecutive clarification approaches; then honest fallback).

### Canon basis

- `BOT-002` §5.5–§5.6 (pause ≠ closure; resume preserves meaning).
- `Ayla Intent Model Specification` (Confidence and Clarification: bounded clarification, then honest fallback).
- `Ayla Product Principles` v0.2 — **CANDIDATE SUPPORTING BASIS — NON-CANONICAL** 4.5 (Progressive Memory + User Control: continuity must not restart from zero) and 4.4 (Honest Representation: state the changed condition honestly).
- `Ayla Conversation Product Map` §3 (failure/recovery ownership sketch: BOT-002 + canonical Intent Model fallback boundaries) — WORKING EVIDENCE, non-canonical.

> **WORKING EVIDENCE — non-canonical:** `UX-OD-002` documents a self-service terminal-fallback vocabulary (retry, reformulate, return_to_previous_safe_step, try_later, exit; preserve_safe_session_context). It is retained for historical context but does not carry canonical authority.

### Product test

- After a failure, does the user keep their expressed intent, context and progress — or are they silently returned to the beginning?
- Does the owning BOT specification offer or continue with a viable next step toward the Goal where one exists, with an honest statement of what changed?

---

## Theme D — Optimize for outcome, not activity

## CDP-11 — User Outcome Before System Activity

### Rule

Conversational progress is judged by whether the user moved toward their intended outcome — never by whether the system executed an internal action, kept the conversation alive, or produced further activity; a completed Task manufactures no new Task, and "no further action" is a valid successful ending.

### Why

BOT-002 fixes Task completion canonically: the expected user outcome achieved, or explicit user confirmation — intermediate action execution alone does not complete a Task (§5.7.1, PD-01). The same decision record bars manufacturing continuation: no automatic next Tasks after completion (BOT-002 §8). This is the conversational form of User Outcome First (Product Principles 4.13) and Contextual Proactivity (4.11): engagement and activity are business metrics, not user value. A conversation that treats "request sent" as success, or invents a follow-up to stay alive, optimizes itself instead of the user.

### Applies to

All conversational capabilities: task progression, booking and cancellation confirmation, recommendation follow-through, follow-up and proactive interaction.

### Does NOT mean

- Follow-up is forbidden — follow-up with a legitimate, explainable, goal-relevant reason is valid (future BOT-005; Product Principles 4.11); manufactured follow-up is not.
- System actions are unimportant — they are means; the principle governs what counts as *success*.
- The conversation must push to a transaction — "do nothing" can be the correct recommendation outcome (Product Principles 4.6, 4.13; Glossary §7 No Action).

### Canon basis

- `BOT-002` §5.7.1, §8 (BOT-002-PD-01; technical execution ≠ completion; no manufactured next Tasks).
- `Ayla Product Principles` v0.2 — **CANDIDATE SUPPORTING BASIS — NON-CANONICAL** 4.13 (User Outcome First), 4.11 (Contextual Proactivity: useful when needed, quiet when not), 4.7 (Booking Is Downstream).
- `Ayla Glossary` §12 (Expected User Success is not the mere fact of a booking), §7 (No Action).
- `Ayla Product Essence` v1.2 — **CANDIDATE SUPPORTING BASIS — NON-CANONICAL** §14 (help, not sell; support without pressure).

### Product test

- In this design, what counts as "done" — a system action completing, or the user's expected outcome?
- After a Task completes, does anything automatically generate new conversational work to keep the user engaged?
- Is "nothing further needed" an expressible, respectable end state of this flow?

---

## CDP-12 — Explainable Recommendation, Never Manipulation

### Rule

When a conversation presents a recommendation, the user can learn why it is relevant to them, reasonable alternatives remain reachable, and no commercial or engagement motive silently shapes what is offered.

### Why

Explainability is what turns a recommendation from a black box into a step the user can trust (Product Principles 4.6). Canon is strict on all three legs: explanation derives from the real decision and may not claim unused reasons or disguise commercial ranking as personalization (Recommendation Contract §13); alternatives are available on request, after refusal, on unavailability or close relevance (Product Principles 4.6; Recommendation Contract §10) and are not shown as artificial assortment either; commercial status never influences organic ranking (Product Principles 4.10; Constitution Art. IV — here referenced, not rewritten). Manipulative recommendation is not a grey area in Ayla canon; it is a named violation.

### Applies to

Discovery and recommendation conversation (future BOT-003), booking suggestions (future BOT-004), proactive suggestions (future BOT-005), and any conversational surface where Ayla proposes a next step.

### Does NOT mean

- Ayla cannot recommend a primary option — a clear primary recommendation is desirable (Product Principles 4.6); concealment and pressure are what is forbidden.
- Every recommendation must display a full alternatives list — alternatives must be *reachable* under the canonical conditions, not dumped as catalogue (Recommendation Contract §10).
- This document defines ranking — ranking, scoring and gating belong to the Recommendation Contract and Recommendation Formation (Conversation Product Map §5).

### Canon basis

- `Ayla Product Principles` v0.2 — **CANDIDATE SUPPORTING BASIS — NON-CANONICAL** (4.6: Explainability & User Agency: recommend, explain, never coerce; 4.10: Economic Neutrality: organic relevance ≠ commercial value).
- `Ayla MVP Recommendation Contract` v0.3 — **SUPPORTING CANDIDATE BASIS — NON-CANONICAL** (§10 alternatives conditions; §11 economic neutrality; §13 explanation derived from real decision and forbidden claims).
- `Ayla Product Essence` v1.2 — **CANDIDATE SUPPORTING BASIS — NON-CANONICAL** §14 (Explainable Transformation; help, not sell).
- `Ayla Constitution` Art. IV (economic neutrality — referenced, not rewritten).

### Product test

- Can the user ask "why this?" and get an answer traceable to their actual situation — not a generic or invented rationale?
- Can the user reach a reasonable alternative, and decline without pressure or repetition of the same offer?
- Is anything shown in this conversation because it benefits Ayla commercially rather than because it serves the user?

---

## 4. Conversation Product Graph (non-normative)

This map shows ownership relationships between conversational Product specifications. It is **not** a state machine and not a user-flow prescription; the user journey may branch between capabilities at any point, and deep links may enter anywhere (Conversation Product Map §6).

```text
                    BOT-003
               Discovery / Rec
                (proposed)
                     ▲
                     │
BOT-001 ───────► BOT-002 ◄────── BOT-005
First Contact   Lifecycle       Proactive
 (canonical)   (canonical)      (proposed, LATER)
                     │
                     ▼
                  BOT-004
                  Booking
                (proposed)
```

- **BOT-002 Conversation Lifecycle** is the generic lifecycle foundation: Conversation → Goal → Task → Current Focus, progression, focus switching, pause, resume, completion.
- **BOT-001 First Contact** owns entry: greeting- and intent-driven entry, Quick Actions at entry, segmentation, consent timing, initial Task emergence.
- **BOT-003 / BOT-004 / BOT-005** are capability-specific conversational owners (proposed): discovery/recommendation, booking/reschedule/cancellation, proactive/follow-up.
- All of them inherit the principles in this document and operate on the BOT-002 lifecycle foundation.

Source: `Ayla Conversation Product Map` §3–§8.

---

## 5. Cross-Cutting Conversational Anti-Patterns

The following patterns violate the principles above and are forbidden in any conversational capability. Each is grounded in existing canon.

1. **Navigation before intent.** Forcing menus, category pickers or screen flows when the user has already expressed a clear intent. — Violates CDP-02, CDP-03 (`BOT-001` P1, P2).
2. **Questionnaire as entry price.** A broad questionnaire, profile-completion gate or "tell us about yourself" sequence before useful action. — Violates CDP-06 (`BOT-001` §13.3).
3. **Silent redirection.** Steering the conversation to a different topic or work item without an explicit user signal. — Violates CDP-04 (`BOT-002` MM-D5).
4. **Technical success presented as user success.** Treating "request sent" / "flow executed" as the user outcome being achieved. — Violates CDP-11 (`BOT-002` PD-01).
5. **Amnesia.** Forgetting valid context and restarting the user from zero after a pause, failure or channel change. — Violates CDP-08, CDP-10 (`BOT-002` §5.6). `UX-OD-002` — WORKING EVIDENCE, non-canonical — documents the terminal-fallback posture that preserves safe session context.
6. **Stale trust.** Acting on dynamic facts (availability, price, schedule) obtained earlier without revalidation. — Violates CDP-08 (`BOT-002` PD-03; Recommendation Contract §22).
7. **Confirmation theatre.** Re-asking stable, already-known information as a ritual of thoroughness. — Violates CDP-06 (`BOT-002` §5.6).
8. **Invented certainty.** Presenting guesses, estimates or unavailable actions as facts or possibilities. — Violates CDP-09 (Intent Model low-confidence rule; Glossary Unknown rule).
9. **Engagement manufacturing.** Creating follow-ups, new Tasks or proactive contact after completion merely to keep the conversation active. — Violates CDP-11 (Product Principles 4.11, 4.13; `BOT-002` §8).
10. **Automation over choice.** Interpreting inaction as acceptance, auto-continuing unfinished work, or committing the user without an explicit signal. — Violates CDP-05 (Recommendation Contract §17; Memory Model §7).
11. **Fake rescue.** Implying operator availability, live support or capabilities Ayla does not have, as a way out of failure. — Violates CDP-09 (`Ayla Product Principles` 4.4; `Ayla Product Essence` §8, §14) and CDP-10. `UX-OD-002` — WORKING EVIDENCE, non-canonical — records the same prohibition.
12. **Consent wall.** Gating the entire conversation behind consent or data collection before any useful value. — Violates CDP-07 (`BOT-001` §14.2).

---

## 6. Canon Review Checklist for Future BOT Specifications

A reviewer of any future conversational Product specification (BOT-003, BOT-004, BOT-005 or later) should be able to answer **yes** to each question below. Each question derives from the principles in this document.

1. Is the conversation oriented around the user's Goal rather than product structure? — CDP-01
2. Is the user's clear intent allowed to lead immediately, without ceremony? — CDP-02
3. Is free text a first-class path to every supported intent, with surfaces assisting rather than replacing conversation? — CDP-03
4. Is Current Focus coherent, and does every change have an explicit user-visible cause? — CDP-04
5. Can the user change direction, decline, or abandon at any point — and is inaction never read as acceptance? — CDP-05
6. Does the design ask only for information the current progression requires, without re-asking stable known facts? — CDP-06
7. Do consent and safety requirements appear exactly at the point of need, never as a universal upfront gate? — CDP-07
8. Does resumption preserve meaning while revalidating dynamic facts before acting on them? — CDP-08
9. Are uncertainty, unavailability and failure represented honestly? — CDP-09
10. Does failure recovery preserve context and continue toward the Goal instead of resetting? — CDP-10
11. Is success defined as the user's outcome, with no manufactured follow-up after completion? — CDP-11
12. Is every recommendation explainable, are alternatives reachable, and is the offer free of hidden commercial or engagement motive? — CDP-12

---

## 7. Boundaries and Non-Goals

This document does not define:

- individual conversational flows, entry behaviour or lifecycle mechanics (owned by BOT-001 and BOT-002 respectively, and not reopened here);
- discovery, recommendation, booking or proactive conversation behaviour (future BOT-003/004/005);
- recommendation ranking, scoring or candidate gating (`Ayla MVP Recommendation Contract` / Recommendation Formation);
- booking domain lifecycle (`Ayla MVP Appointment Contract`);
- memory persistence, eligibility or the conversation-context/memory boundary in detail (`Ayla Memory Model Specification`; BOT-002 open follow-ups Q27/Q28);
- intent classification, slots or confidence thresholds (`Ayla Intent Model Specification`);
- consent scopes, categories or legal bases (`Consent Scope Registry`);
- prompts, runtime state, state machines, APIs, transport, storage, LLM behaviour or screen layouts;
- freshness durations, TTLs or revalidation algorithms;
- localized copy or tone of voice.

---

## 8. Deferred Repository Follow-up

- **Dedicated principles schema type.** Registration of a dedicated `principles` type in `.knowledge/schema.yaml` may be considered separately. This document remains `type: specification`; the deferred infrastructure follow-up does not affect Product semantics or Canon readiness.

---

## 9. Canonicalization Record

- **Canonicalization date:** 2026-08-13
- **Canonicalization authority:** Product Owner
- **Independent Canon Review (initial verdict):** READY AFTER ONE WRITER PASS — 4 required corrections, 0 blockers
- **Canon Verification (final verdict):** READY FOR CANON — RC-1, RC-2, RC-3, RC-4 all RESOLVED; no remediation-induced blocker
- **Governing process:** Ayla Product Decision & Canon Authoring Process v1.0
- **Governing review:** Ayla Canon Review Standard v1.0

**Document status:** CANONICAL
