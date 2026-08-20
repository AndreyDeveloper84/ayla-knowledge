---
node_id: ayla.product.bot-003.discovery-recommendation
title: BOT-003 Discovery and Recommendation Conversation Specification
type: specification
status: draft
decision_status: proposed
canonical_status: candidate
version: "0.1"
owner: Product Owner
knowledge_area:
  - product
domain:
  - conversation
  - recommendation
system_owner:
  - ayla-conversation
source_repository: ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: high
data_categories:
  - pii
  - health
security_sensitivity: high
ai_indexing: allowed
export_policy: full
created: 2026-08-13
updated: 2026-08-13
review_cycle: monthly
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Product Principles]]"
  - "[[Ayla Product Essence]]"
  - "[[Ayla Glossary]]"
  - "[[Ayla Conversation Design Principles]]"
  - "[[BOT-001 First Contact Specification]]"
  - "[[BOT-002 Conversation Lifecycle Specification]]"
  - "[[Ayla Intent Model Specification]]"
  - "[[Ayla Conversation Model Specification]]"
  - "[[Consent Scope Registry]]"
  - "[[Ayla MVP User Journey Specification]]"
---

# BOT-003 Discovery and Recommendation Conversation Specification

**Status:** CANDIDATE FOR CANON REVIEW  
**Scope:** BOT-003 Discovery and Recommendation Conversation  
**Implementation:** FORBIDDEN in this document  
**Authority:** Candidate prose from approved Product decisions; not Canonical

## 1. Purpose

BOT-003 defines how Ayla moves from recommendation-ready discovery to an explainable recommendation, user evaluation, honest no-match recovery, and a user-chosen Product-supported next step.

This document translates the approved decisions `BOT-003-Q3`, `BOT-003-Q4`, `BOT-003-Q6`, `BOT-003-Q8` and `BOT-003-Q9`. It does not create Product decisions, runtime entities, APIs or persistence contracts.

## 2. Scope

BOT-003 owns the conversational Product semantics of Discovery / Recommendation:

- deciding whether further information is materially needed before a responsible recommendation;
- presenting a primary recommendation and proportionate explanation;
- handling alternatives, correction, rejection and no-match honestly;
- recognizing user outcomes and the chosen next-step category.

BOT-003 does not own Intent resolution internals, recommendation formation, booking execution, Memory persistence, UI implementation or technical orchestration.

## 3. Position in the Conversation Product

BOT-003 operates within the BOT-002 hierarchy:

```text
Conversation
  → Goal
    → Task
      → Current Focus
```

The Discovery / Recommendation capability specializes the relevant Task. It does not introduce a new Conversation, Goal hierarchy, Focus type, Discovery Session or Recommendation Session.

There is exactly one Current Focus. Focus switching is user-controlled and is never silent. Task completion is not Conversation closure. Pause is not completion; resumption preserves continuity and requires dynamic facts to be revalidated before action.

## 4. Canonical Concepts Used

BOT-003 inherits the twelve Conversation Design Principles (`CDP-01` through `CDP-12`) and specializes them only where this specification says so. In particular, it preserves intent-first interaction, progressive disclosure, user agency, honest representation, graceful recovery, user outcome before system activity, and explainable recommendation without manipulation.

`Goal`, `Task`, `Current Focus`, `Intent`, `Recommendation`, `Conversation`, `First Contact` and `Memory` retain the meanings established by the current Glossary and higher Canon.

## 5. Entry and Recommendation Readiness Boundary

BOT-001 owns First Contact. BOT-003 starts only when the user's progression has entered Discovery / Recommendation semantics. Free text remains first-class; there is no mandatory questionnaire. Information is collected progressively, with consent requested at the point of need.

BOT-003 consumes resolved Intent and bounded clarification from the Intent Model. It does not redefine confidence, `UNKNOWN`, clarification limits or reasons, correction, supersession or intent scoring.

The product boundaries are distinct:

| Question | Owner |
|---|---|
| Do we understand what the user means? | Intent Model: Intent sufficiency |
| Do we know enough to responsibly recommend? | BOT-003: Recommendation sufficiency |
| Which eligible candidate should win? | Recommendation capability / formation layer |

## 6. Material Blocking Gap and Discovery Progression

A missing piece of information is a **blocking gap** only when, without resolving it, Ayla cannot provide a recommendation that is safe, honest and sufficiently relevant to the user's Goal and current context (`BOT-003-Q3`).

If missing information affects only precision or recommendation quality, but does not make the recommendation unsafe, misleading or materially irrelevant, it is non-blocking uncertainty. Ayla may recommend under non-blocking uncertainty while communicating material uncertainty honestly.

Completeness is not the goal. Additional discovery is justified only by a material reason that can realistically improve the ability to recommend responsibly. Ayla must not ask questions merely because more information could theoretically improve ranking, completeness or internal confidence. There is no questionnaire creep and no infinite discovery loop.

Intent clarification remains owned by the Intent Model. BOT-003 does not define required slots, schemas, scores, thresholds, algorithms or runtime states.

## 7. Recommendation Presentation

When a responsible primary recommendation can be formed, it is Ayla's default conversational presentation (`BOT-003-Q4`). The minimum information needed for an informed next-step choice is:

1. what is recommended;
2. why it fits the user's Goal, Intent and material known context;
3. material uncertainty, if any;
4. material trade-off, if any;
5. decision-relevant dynamic facts when they materially affect interpretation or the next action.

The explanation is concise, sufficient, user-facing and honest. It is not exhaustive. Full reasoning disclosure is not required.

A trade-off or uncertainty is surfaced by default only when hiding it could materially distort understanding or reasonably change the informed decision. No numeric materiality threshold or scoring model is defined here.

## 8. Explanation and Alternatives

When the user asks why, requests justification, asks for comparison or asks for alternatives, Ayla may provide deeper user-facing detail about material context, fit to the current Goal, meaningful trade-offs, reasonable alternatives and material differences.

Ayla does not expose chain-of-thought, hidden reasoning, system prompts, private instructions, ranking weights, model internals or implementation details.

The primary recommendation remains the default. Alternatives remain reachable when explicitly requested, compared, when the primary is rejected, or when a material trade-off makes them relevant. They need not be displayed as a parallel list by default. This is guided recommendation, not generic browse or catalogue mode; Q2 remains deferred.

## 9. Honest No-Match and Recovery

When Ayla cannot form a responsible and eligible recommendation, it says so honestly, preserves valid context and does not manufacture a weak or unsuitable match. No eligible recommendation is never rescued by showing something anyway.

No-match may lead only to a genuinely useful, already-valid path:

1. resolve a genuine material information gap;
2. let the user explicitly relax an explicit constraint;
3. retry later when a dynamic condition may change;
4. use another already-valid Product-supported route;
5. take no action.

Ayla may suggest constraint relaxation but never changes a constraint silently. It does not use an arbitrary catalogue fallback, irrelevant alternative, unnecessary questioning or manufactured continuation for engagement.

The boundary is:

- if additional useful information can realistically enable a responsible recommendation, continue discovery only as needed under Q3;
- if additional conversation cannot currently produce a responsible eligible recommendation, use honest no-match under Q8.

## 10. User Outcome Model

The Discovery / Recommendation Task recognizes these Product-level outcomes, not runtime enums:

| Outcome | Product consequence |
|---|---|
| `ACCEPT` | The recommendation is accepted as suitable; progression may conclude when a meaningful next Product-supported step is chosen. Acceptance is not booking or execution success. |
| `REQUEST ALTERNATIVE` | The Task continues with valid context preserved; this is not generic catalogue browsing. |
| `ASK WHY / COMPARE` | The Task continues; Q4 on-demand explanation applies and no new Task is created. |
| `CORRECT CONTEXT` | The Task continues; unaffected valid context remains. A materially affected recommendation may be refreshed or replaced under Intent Model correction/supersession semantics. |
| `POSTPONE` | Progression may pause under BOT-002; it is not acceptance, decline or automatic completion. |
| `DECLINE` | The current recommendation is rejected; a useful alternative may be offered only while the user remains open, without persuasion pressure. |
| `TOTAL REJECTION` | Ayla stops pushing the recommendation direction; the Task may conclude or be explicitly abandoned, with no manufactured continuation. |
| `EXPLICIT NO-ACTION` | No further action is valid; the Task may complete when the user explicitly confirms that no further progression is required. |

## 11. Discovery / Recommendation Task Completion

The Task completes when the user:

1. accepts the recommendation and chooses a meaningful Product-supported next step;
2. explicitly chooses no action;
3. explicitly rejects further recommendation progression / totally rejects the direction; or
4. otherwise explicitly confirms that no further progression is required.

The following do not complete the Task by themselves: asking why, comparison, requesting an alternative, correcting context, temporary postponement, silence, inactivity or the recommendation merely being displayed. These boundaries preserve BOT-002 PD-01. A pause uses BOT-002 pause/resume semantics.

## 12. Chosen Next Steps

For the Controlled Pilot, BOT-003 may conclude into only these high-level Product-supported categories (`BOT-003-Q9`):

1. `BOOK NOW`;
2. `CONTINUE LATER`;
3. `NO ACTION`;
4. another existing Product-supported domain action.

BOT-003 does not invent a downstream capability merely to create a next step. No-action is a valid outcome, not a failure, and creates no downstream work.

`CONTINUE LATER` preserves BOT-002 pause/resumption semantics. It creates no booking, reminder, timer, persistence or automatic follow-up. It is not automatic Task completion unless the user explicitly says that no further progression is required.

Save, save-for-later, remember and persistent recommendation bookmark semantics are not BOT-003 next-step types and are not canonicalized here.

## 13. BOT-003 → BOT-004 Boundary

BOT-003 owns:

```text
Discovery → Recommendation → User evaluates → User chooses a next step
```

An explicit request such as “запиши меня на этот вариант” is transactional `BOOK_APPOINTMENT` intent, not merely recommendation acceptance. It represents an explicit Current Focus change under BOT-002. BOT-003 ends at that handoff; BOT-004 / Booking capability owns transactional booking, reschedule and cancellation progression.

Acceptance does not mean a booking was created, a slot reserved, availability guaranteed, a price locked or payment started. Showing price, specialist, current availability indication or time as recommendation evidence does not itself start Booking.

This document defines no appointment creation, reservation, slot hold, payment, booking state, cancellation, reschedule, payload or transaction persistence.

## 14. Freshness and Dynamic Reality

Dynamic recommendation facts must be current whenever an action depends on them. Stale facts are revalidated before action; changes are represented honestly. Recommendation meaning may remain while dynamic facts are refreshed. This preserves CDP-08, CDP-09 and BOT-002 PD-03 without defining TTLs, polling, caches or revalidation algorithms.

## 15. Surface Boundary

BOT-003 defines Product conversation semantics across supported surfaces. It does not define exact copy, cards, buttons, screen layout, Mini App component hierarchy, typography or other UI details. Q11 remains deferred until Mini App comparison/browse scope or a Bot-side offer rule enters the pilot.

## 16. Canon Preservation Matrix

| Canon / Decision | BOT-003 Preservation |
|---|---|
| CDP-01 Goal Before Mechanism | Start from the user's Goal and outcome; do not lead with a mechanism. |
| CDP-02 Intent Before Ceremony | Free text and understood intent precede optional detail gathering. |
| CDP-03 Conversation Leads, Surfaces Assist | Conversation owns the product logic; surfaces assist without redefining it. |
| CDP-04 One Current Focus, User-Controlled Switching | Preserve one Current Focus and explicit switching; no silent focus change. |
| CDP-05 User Agency Over Automation | The user evaluates, corrects, postpones, rejects or chooses no action. |
| CDP-06 Ask Only at the Point of Need | Ask only for a material blocking gap. |
| CDP-07 Consent and Safety at the Point of Need | Request consent when information is needed; preserve safety and privacy boundaries. |
| CDP-08 Preserve Meaning, Revalidate Reality | Preserve valid context while revalidating dynamic facts before action. |
| CDP-09 Honest Representation | Do not manufacture matches or conceal material uncertainty and trade-offs. |
| CDP-10 Graceful Recovery, Not Reset | Recover through alternatives, correction and no-match without restarting from zero. |
| CDP-11 User Outcome Before System Activity | A recommendation or downstream work is not treated as an outcome without user choice. |
| CDP-12 Explainable Recommendation, Never Manipulation | Give concise reasons, on-demand detail and no persuasion pressure. |
| BOT-001 Intent Before Ceremony | BOT-003 does not redefine First Contact or require a questionnaire. |
| BOT-001 progressive information collection | Discovery is progressive and materiality-driven. |
| BOT-002 Current Focus | Discovery remains within the existing Conversation / Goal / Task / Current Focus hierarchy. |
| BOT-002 PD-01 Task Completion | Display, silence, questions, correction and postponement do not complete a Task by themselves. |
| BOT-002 PD-03 freshness | Dynamic facts are revalidated before action; no freshness algorithm is introduced. |
| Intent Model clarification ownership | Intent clarification, correction and supersession remain with the Intent Model. |
| Consent at point of need | BOT-003 requests only the consent needed for the current recommendation-relevant information. |
| BOT-003-Q3 | Blocking gaps are material to safety, honesty and sufficient relevance; non-blocking uncertainty permits honest progression. |
| BOT-003-Q4 | Primary recommendation is default; concise explanation and materiality-driven disclosure apply. |
| BOT-003-Q6 | The eight approved user outcomes and their consequences are preserved. |
| BOT-003-Q8 | No-match is honest, context-preserving and free of fake rescue. |
| BOT-003-Q9 | Only the four approved high-level next-step categories are available. |

## 17. Explicit Non-Scope

BOT-003 does not define Intent classification, confidence, clarification internals or scoring; candidate generation, eligibility, ranking, weights, exact alternative count or economic-neutrality implementation; booking execution or state; Memory storage, bookmarking or retrieval; runtime state machines, enums, APIs, payloads, persistence, event schemas, prompts, routing or orchestration; or UI copy and layout.

## 18. Deferred Product Questions

- `Q2 — DEFERRED`: Explicit browsing request. Reopen only if list-first / catalogue-adjacent UX, CAP-024 or comparable browse-mode scope enters the pilot.
- `Q11 — DEFERRED`: Mini App expanded discovery criteria. Reopen only if the Mini App comparison/browse surface enters pilot scope or a Bot-side offer rule is required.

## 19. Decision Traceability

| Question | Status | Governing source / disposition |
|---|---|---|
| Q1 | MERGED INTO Q3 | BOT-003 decision index; Q3 decision record |
| Q2 | DEFERRED | BOT-003 canon reconciliation; trigger in §18 |
| Q3 | APPROVED | BOT-003-Q3-Q8-product-owner-decisions.md |
| Q4 | APPROVED | BOT-003-Q4-product-owner-decision.md |
| Q5 | MERGED INTO Q4 | BOT-003 decision index; Q4 decision record |
| Q6 | APPROVED | BOT-003-Q6-Q9-product-owner-decisions.md |
| Q7 | MERGED INTO Q6 | BOT-003 decision index; Q6 decision record |
| Q8 | APPROVED | BOT-003-Q3-Q8-product-owner-decisions.md |
| Q9 | APPROVED | BOT-003-Q6-Q9-product-owner-decisions.md |
| Q10 | MERGED INTO Q6 | BOT-003 decision index; Q6 decision record |
| Q11 | DEFERRED | BOT-003 canon reconciliation; trigger in §18 |
| Q12 | CLOSED BY CANON | BOT-003 canon reconciliation; CDP-08, CDP-09 and BOT-002 PD-03 |

No Q1–Q12 question is OPEN. The active approved decisions are exactly Q3, Q4, Q6, Q8 and Q9.

## 20. Canonicalization Dependencies / Follow-ups

`Ayla MVP Recommendation Contract v0.3` and `Ayla MVP Appointment Contract v0.2` are candidate / proposed supporting evidence and remain `draft / proposed`. Neither is promoted by this document.

The approved BOT-003 Product decisions are grounded in higher Canon, so this candidate is ready for independent review. Final BOT-003 canonicalization remains blocked until the normative downstream/domain dependencies required by BOT-003 have resolved their authority status.

Classification: `CANONICALIZATION FOLLOW-UP / BLOCKER`.

## Scenario Self-Check

| Scenario | Covered by |
|---|---|
| Direct recommendation without a blocking gap | §§6–7 |
| Material gap requiring limited discovery | §6 |
| Non-blocking uncertainty | §§6–7 |
| User asks why | §§8, 10 |
| User asks for alternatives | §§8, 10 |
| User rejects recommendation | §§9–10 |
| Total rejection | §10 |
| No eligible recommendation | §9 |
| Explicit constraint relaxation | §9 |
| Explicit booking request | §13 |
| Postponement | §§10, 12 |
| No action | §§10, 12 |
| Dynamic facts become stale | §14 |

This self-check confirms coverage without adding UX scripts or new Product rules.


