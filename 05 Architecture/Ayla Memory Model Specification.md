---
node_id: ayla.domain.memory-model

title: Ayla Memory Model Specification
title_ru: Спецификация модели памяти Ayla

type: domain-specification
status: approved
decision_status: accepted
canonical_status: approved
version: "1.0"

owner: Domain Architecture
owners:
  - Product Owner
  - Domain Architecture

reviewers:
  - AI Architecture
  - Backend Architecture
  - Product Design
  - Privacy and Safety

knowledge_area:
  - domain-model
  - product
  - architecture

domain:
  - user-context

system_owner:
  - ayla-user-context

source_repository: ayla-knowledge
source_kind: canonical

classification: internal
data_sensitivity: none
security_sensitivity: low

ai_indexing: allowed
export_policy: full

updated: 2026-08-08
review_cycle: monthly

depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Product Vision]]"
  - "[[Ayla Repository Responsibility Matrix]]"
  - "[[Ayla Glossary]]"
  - "[[OWNER_DECISION_REGISTER]]"
  - "[[Ayla Decision Log]]"
  - "[[Ayla Core Domain Model Specification]]"
  - "[[ADR-0012 Dynamic User Model]]"
  - "[[Ayla Domain Event Registry]]"
  - "[[Consent Scope Registry]]"
  - "[[AMD-020 Pilot Scope Registry]]"
  - "[[Ayla Domain Capability Registry]]"

related:
  - "[[Ayla Conversation Model Specification]]"
  - "[[Ayla Intent Model Specification]]"
  - "[[Ayla MVP Recommendation Contract]]"
  - "[[Ayla MVP User Journey Specification]]"
  - "[[Killer PRD]]"
---

# Ayla Memory Model Specification

## §1. Status and Readiness Gate

| Property | Value |
| --- | --- |
| Version | 1.0 |
| Document status | approved |
| Decision status | accepted |
| Canonical status | approved |
| Wave | Wave 1 - Foundation (locked); Wave 2A - Memory Semantics (locked); Wave 2B - Memory Identity (locked); Wave 3 - Lifecycle & Event Semantics (locked) |
| Active Canon | yes |

This document contains the locked Wave 1 Foundation, the locked Wave 2A Memory Semantics, the locked Wave 2B Memory Identity, and the locked Wave 3 Lifecycle & Event Semantics.

This release establishes terminology, ownership boundaries, normative
principles, lifecycle semantics, event semantics, and the conceptual position
of the Memory Domain. It does not yet define entity field schemas, lifecycle
state machines, eligibility algorithms, retrieval algorithms, TTL values, event
payloads, or storage contracts.

This specification is Active Canon for the Memory Domain.

## §2. Canonical Position

When approved, this specification will be the conceptual Source of Truth for
the following Memory Domain concerns:

- `MemoryProposal` semantics.
- `MemoryEntry` semantics.
- Memory Domain ownership boundary.
- Memory epistemic semantics (what counts as a user fact, what counts as an
  inference, and how the two relate).
- Memory persistence semantics at the conceptual level.
- Memory lifecycle semantics at the conceptual level.
- Memory use/eligibility semantics at the conceptual level.

This specification does **not** own and does not redefine:

- [[Ayla Conversation Model Specification|Conversation Context]] — owned by the
  Conversation Domain.
- Session Context — owned by the Conversation Domain.
- [[Consent Scope Registry|Consent]] — owned by the Consent / Privacy Domain.
- [[Ayla Intent Model Specification|Intent]] — owned by the Intent Domain.
- [[Ayla MVP Recommendation Contract|Recommendation]] — owned by the
  Recommendation Domain.
- Transformation Goal — upstream/cross-cutting canonical product concept; final
  owner definition is outside the scope of this specification.
- Authoritative Backend Facts — owned by the respective backend domains.
- Runtime orchestration — owned by Conversation Orchestration / runtime
  architecture.
- Repository topology — owned by [[Ayla Repository Responsibility Matrix]].
- Event registration, payload schemas, and registry governance — owned by
  [[Ayla Domain Event Registry|Domain Event Registry governance]].

## §3. Purpose

Ayla needs a separate Memory Domain because not everything that appears in a
conversation, an inference, or a backend record should become persistent,
personally relevant memory.

Without an explicit memory model, the product risks silently accumulating
inferences, session snippets, consent state, recommendations, and backend facts
under a single vague label of "context." That collapse breaks privacy design,
auditing, correction, and revocation.

The separation `Observation → MemoryProposal → MemoryEntry` exists to make each
transition visible and governed:

- An **Observation** is an input or signal. It may inform a proposal, but it is
  not itself a persisted memory fact.
- A **MemoryProposal** is a canonical candidate for persistence. It is not a
  `MemoryEntry` until it passes the governed persistence boundary.
- A **MemoryEntry** is a persisted memory fact governed by the Memory Contract.

**Conversation Context** must not be automatically treated as persistent
memory. It is owned by the Conversation Domain and may span multiple Session,
Interaction, and Dialogue Turn instances; its purpose is conversational
continuity, not long-term memory storage.

**AI inference** must not be automatically turned into a user fact. A model may
form a hypothesis, but a persistent memory fact requires explicit user
confirmation or another approved provenance path, plus a whitelist/category
policy check.

Finally, memory use must be **purpose-limited**. Retrieval, rendering, and any
other consumption of MemoryEntry must declare a purpose and be gated by
eligibility. There is no blanket "get all memory" operation.

## §4. Scope

### IN_SCOPE (for the full specification, introduced at Foundation level only)

- Memory conceptual entities and their semantic boundaries.
- Epistemic distinctions (observation, inference, proposal, confirmed fact,
  authoritative backend fact).
- `MemoryProposal` semantics.
- Persistence boundary between session-scoped context and persistent memory.
- Eligibility semantics (what makes a memory usable for a given purpose).
- Retrieval/use semantics at the conceptual level.
- Freshness and reconfirmation semantics at the conceptual level.
- Correction and supersession semantics.
- Revocation, expiry, and deletion boundary at the conceptual level.
- Cross-domain ownership and responsibility boundaries.
- Event semantics (meaning and lifecycle relevance), without registry mechanics.
- Governance and traceability requirements for memory decisions.

### OUT_OF_SCOPE

- Database / ORM schema.
- API design.
- Vector database specifics.
- Embedding formats and algorithms.
- Ranking or search algorithms.
- Prompt assembly.
- Memory rendering format.
- Queues, caches, and replication mechanics.
- Runtime finite-state machines.
- Exact TTL values.
- UI confirmation flows.
- Repository deployment layout.
- Event payload schemas and producer/consumer wiring.

## §5. Non-goals

This specification does **not** attempt to become any of the following:

- A Conversation Model.
- A Consent Registry.
- An Intent Model.
- A Recommendation Contract.
- A backend domain model for non-memory domains.
- A runtime orchestration specification.
- A storage implementation specification.
- A privacy or legal ruling document.
- A Domain Event Registry.

It also does not duplicate the ownership of neighboring documents. Where a
concept is owned by another domain, this specification references it rather
than redefining it.

## §6. Dependencies and Blockers

### Normative dependencies

| Dependency | Relevance to Memory Model | Wave 1 impact |
| --- | --- | --- |
| [[Ayla Constitution]] | Inference ≠ fact, consent control, lawful-basis constraints. | Required; present. |
| [[Ayla Decision Log]] AYLA-DEC-0023 | Memory whitelist: what Ayla may remember. | Required; present. |
| [[Ayla Decision Log]] AYLA-DEC-0024 | Memory Contract: lifecycle of `MemoryProposal` and `MemoryEntry`. | Required; present. |
| [[Ayla Core Domain Model Specification]] §7.3 | `Context Fact` / `MemoryEntry` and `MemoryProposal` definitions. | Required; present. |
| [[ADR-0012 Dynamic User Model]] | Classification/policy dimensions (`knowledge_class`, `confidence`, `lifetime`, `provenance`). | Required as policy/classification layer. |
| [[Ayla Domain Event Registry]] §6.4 | Memory event semantics; registry mechanics stay with DER. | Required; event semantics referenced. |
| [[Consent Scope Registry]] | Consent scope, category policy, and revocation effects. | Required; ownership stays with CSR. |
| OWNER_DECISION_REGISTER AYLA-DEC-0067…0079 | Locked foundation and identity rulings for Memory Domain. | Required; present. |

### Known unresolved dependencies

| ID | Topic | Classification | What it blocks | Blocks Wave 1? |
| --- | --- | --- | --- | --- |
| CSR-OD-5 | Canonical source of truth for consent records. | `NON_BLOCKING_DEPENDENCY` | Future eligibility/retrieval runtime contract and consent-state interpretation in memory use. | No. |
| CSR-OD-4 / OD-1 | Diet/skin and religious signal legal boundary. | `BLOCKS_SECTION` | Future whitelist category policy for sensitive diet/religious signals. | No. |
| ADR-0012 OD-2 | Red TTL 90-day purge vs safety-critical persistence. | `BLOCKS_SECTION` | Future TTL/retention policy for red-zone safety records. | No. |
| DER OQ-E3 | `appointment.completed` / outcome semantics. | `NON_BLOCKING_DEPENDENCY` | Future memory events sourced from appointment outcomes. | No. |
| DER OQ-E4 | `memory.entry_deleted`, deletion contract, and cross-context consumers for memory events. | `BLOCKS_SECTION` | Future deletion-event semantics and cross-context publication of memory events. | No. |
| ADR-0012 OQ-1 | Verification registry for `confidence=verified`. | `NON_BLOCKING_DEPENDENCY` | Future provenance values and verification methods. | No. |
| ADR-0012 OQ-2 | Provenance history format. | `NON_BLOCKING_DEPENDENCY` | Future audit/traceability details for transformed memory records. | No. |

### Downstream follow-ups

- Future targeted amendment to [[Ayla Glossary]] to align memory terminology.
- Future targeted reconciliation of `memory.*` events in
  [[Ayla Domain Event Registry]] (proposed → registered) after Memory Model
  stabilization.
- Future update to [[Ayla Repository Responsibility Matrix]] to reflect current
  implementation mapping without making repository names canonical.

No dependency above is a `GLOBAL_BLOCKER`. Wave 1 Foundation can proceed.

## §7. Normative Principles

The following principles are grounded in the locked Owner Decisions
AYLA-DEC-0067…0079 and compatible upstream canon:

1. **Observation ≠ Persistent Memory Fact.** An observed signal is not a
   persisted memory record merely because it was seen.
2. **AI inference ≠ User Fact.** A model-derived hypothesis is not a user fact
   until it follows an approved confirmation or verification path.
3. **MemoryProposal ≠ MemoryEntry.** A candidate is not a persisted memory fact
   until it crosses the governed persistence boundary.
4. **Silence ≠ confirmation.** The absence of an explicit objection does not
   promote a proposal to a memory fact.
5. **Dialogue continuation ≠ confirmation.** Continuing a conversation does not
   implicitly confirm pending memory proposals.
6. **Conversation Context ≠ Persistent Memory.** Conversation-owned context
   maintains continuity across Sessions, Interactions, and Dialogue Turns; it
   does not automatically become long-term memory.
7. **Session Context ≠ Persistent Memory.** Temporary slots, recent context, and
   current intents are session-scoped.
8. **Intent ≠ Memory.** A user's current intent is a transient or computed
   object, not a persisted memory fact.
9. **Recommendation ≠ Memory.** A recommendation is an output of the
   Recommendation Domain, not a memory fact owned by the Memory Domain.
10. **Consent State ≠ Memory Fact.** Current consent state gates memory use; it
    is not itself a memory record.
11. **Authoritative Backend Fact ≠ MemoryEntry merely by existing.** A fact from
    a backend domain may be read or referenced, but it does not automatically
    become a MemoryEntry.
12. **Memory use is purpose-limited.** Any retrieval or use of memory must
    declare a purpose and pass eligibility checks.
13. **Memory Domain does not acquire ownership of foreign-domain facts.**
    Reading, projecting, or using a fact from another domain does not transfer
    ownership to the Memory Domain.
14. **Correction preserves history.** A change to a memory fact is expressed as
    supersession (old entry becomes superseded, new entry becomes active) rather
    than silent in-place rewriting, consistent with AYLA-DEC-0024.

This section does not define lifecycle states, field schemas, confirmation
state machines, eligibility algorithms, retrieval algorithms, freshness
algorithms, or TTL values.

## §8. Source of Truth and Ownership

| Concept | Canonical owner | Memory Model relation | Ownership transfer? |
| --- | --- | --- | --- |
| `MemoryProposal` | Memory Domain | Owns semantics. | NO — owned by Memory Domain. |
| `MemoryEntry` | Memory Domain | Owns semantics and conceptual lifecycle. | NO — owned by Memory Domain. |
| `Observation` | Source domain (Conversation, Backend, etc.) | Consumes as input; may inform a `MemoryProposal`. | NO — observation remains owned by source domain. |
| Memory Eligibility | Memory Domain (decision concept) | Defines semantics of the eligibility check; does not persist as an entity. | N/A — evaluated, not stored. |
| Conversation Context | Conversation Domain | Uses as input/observation source; does not own. | NO. |
| Session Context | Conversation Domain | Uses as input/observation source; does not own. | NO. |
| Consent | Consent / Privacy Domain | Reads consent state to gate memory use; does not own. | NO. |
| Intent | Intent Domain | May consume memory context; does not own memory semantics. | NO. |
| Recommendation | Recommendation Domain | May consume memory context; does not own memory semantics. | NO. |
| Transformation Goal | Upstream / cross-cutting canonical product concept (owner to be defined by Product Owner) | May be informed by memory; not owned by Memory Domain. | NO. |
| Authoritative Backend Fact | Respective backend domain | May be read or referenced; not converted to MemoryEntry automatically. | NO. |
| Event registration/schema | Domain Event Registry governance | Memory Model defines semantic meaning of memory events; registry mechanics stay with DER. | NO. |
| Runtime retrieval/rendering/orchestration | Runtime / Conversation Orchestration | Memory Model defines eligibility semantics; runtime executes retrieval and rendering. | NO. |

Key rules:

- The Memory Domain owns `MemoryProposal` and `MemoryEntry` semantics.
- An `Observation` may be consumed by the Memory Domain but does not
  automatically become memory.
- Eligibility is evaluated, not owned as a persisted entity.
- Foreign-domain facts remain owned by their source domains.
- Reading, projecting, or using a fact is not ownership transfer.
- Conceptual owners are not bound to specific repository names.

## §9. Terminology

### Foundation-level canonical vocabulary

- **Memory Domain.** The conceptual domain that owns persistent memory
  semantics: `MemoryProposal`, `MemoryEntry`, memory lifecycle, epistemic
  distinctions, and eligibility/use semantics.
- **Observation.** An input or signal that the system observes. An observation
  is not yet a persisted memory fact.
- **MemoryProposal.** A canonical candidate for persistence that is not yet a
  `MemoryEntry`. A `MemoryProposal` is not a persisted memory fact.
- **MemoryEntry.** A confirmed, persisted memory fact governed by the Memory
  Contract.
- **Memory Eligibility.** A decision concept that determines whether a
  `MemoryEntry` may be used for a specific purpose under current policy,
  consent, freshness, and safety constraints. Not a persisted entity.
- **Conversation Context.** Context owned by the Conversation Domain to maintain
  conversational continuity and semantic coherence across Sessions, Interactions,
  and Dialogue Turns. Not persistent memory.
- **Session Context.** Session-scoped part or aspect of Conversation Context,
  associated with a specific Session. Not a separate canonical entity; not an
  independent owner; not persistent memory.
- **Authoritative Backend Fact.** A fact owned and authored by a backend
  domain. It is not a `MemoryEntry` merely by existing, though it may be read or
  referenced.
- **Persistent Memory.** Memory that has crossed the governed persistence
  boundary and is retained across sessions under the Memory Contract, whitelist,
  and consent boundaries. It requires explicit user confirmation or another
  canonically approved provenance/persistence path.
- **Reconfirmation.** A usage/freshness gate that may require explicit
  re-approval before a `MemoryEntry` is used for a particular operation. Not a
  lifecycle state of `MemoryEntry`.

### Legacy / ambiguous mapping

| Legacy term | Canonical treatment |
| --- | --- |
| Memory Candidate | Alias / explanatory term for `MemoryProposal`. Not a separate canonical entity. |
| Working Context | Non-canonical generic term; use the term of the owning context (Conversation Context, Session Context, etc.). |
| Context Fact | Legacy/ambiguous alias; canonical persistent term is `MemoryEntry`. |
| Signal | Generic input/observation term; not a Memory entity. |
| User Fact | Epistemic classification, not a persistence entity. |

Constraints:

- `Memory Candidate` is not a third canonical entity.
- `Memory Eligibility` is not a persisted entity.
- `Reconfirmation` is not a lifecycle state.
- `User Fact` is an epistemic classification, not a persistence entity.

## §10. Memory Domain Overview

The Memory Domain sits between external observations/context and
purpose-limited memory use:

```text
External observations / context / authoritative sources
                    ↓
            MemoryProposal
                    ↓
       confirmation / policy /
          consent / whitelist
                    ↓
              MemoryEntry
                    ↓
   eligibility-gated, purpose-limited retrieval/use
```

This diagram is **conceptual**, not a runtime pipeline. It shows semantic
transitions, not storage queues, API calls, model invocations, or event
ordering.

Caveats:

- Not every `Observation` becomes a `MemoryProposal`.
- Not every `MemoryProposal` becomes a `MemoryEntry`.
- Not every `MemoryEntry` is eligible for every use.

This section does not define transition implementation, storage, queues, APIs,
model calls, thresholds, TTL, event ordering, or runtime sequences.

## §11. Memory Semantics Overview

Wave 2A defines the conceptual semantics that sit between raw inputs and
governed memory use. The conceptual chain is:

```text
Observation
    ↓
possible MemoryProposal
    ↓
governed persistence boundary
    ↓
MemoryEntry
```

An **Observation** is something the system sees or receives. A
**MemoryProposal** is a canonical candidate for persistence. A **MemoryEntry**
is a persisted memory fact that has crossed the governed persistence boundary.

Critical caveats:

```text
not every Observation becomes MemoryProposal
not every MemoryProposal becomes MemoryEntry
MemoryEntry ≠ authoritative backend fact
MemoryEntry ≠ AI inference by default
MemoryProposal ≠ MemoryEntry
```

This section describes conceptual semantics, not a runtime pipeline. It does
not define queues, API contracts, database tables, event ordering,
confirmation UI, TTL values, workflow engines, or state-machine transitions.

## §12. Observation

An **Observation** is an input or signal about the user, their context, their
actions, or an external situation that is not, by itself, a Persistent Memory
Fact.

The following kinds of input or signal may be observed by the system. They are
not automatically equivalent and do not automatically become memory:

| Kind | What it is | Canonical treatment |
| --- | --- | --- |
| User statement | Something the user explicitly said or wrote. | A strong source for a `MemoryProposal`, but not a `MemoryEntry` until it passes policy / consent / whitelist gates. |
| Backend-provided fact | A fact supplied by an authoritative backend domain. | Remains an **Authoritative Backend Fact** owned by that domain; not converted to `MemoryEntry` merely by being read. |
| Conversation observation | Information that appears in Conversation Context or Session Context. | Owned by the Conversation Domain; may inform a proposal, but conversation context is not persistent memory. |
| Behavioral signal | A session-scoped or interaction-scoped signal about user behavior. | Usually session-scoped; persistence requires an approved path. |

An **AI inference** is not an Observation. It is a hypothesis generated by a model, which may arise from Observations but does not become an Observation automatically. Like an Observation, an AI inference is not a user fact. For an AI inference, the canonical path is AI inference -> `MemoryProposal` (pending_confirmation) -> explicit user confirmation -> accepted `MemoryProposal` -> whitelist check -> governed persistence boundary.

**Practical explanation:** An Observation is "what the system saw or received,"
not "what the system has already decided to remember forever." Seeing a signal
does not grant it persistence status.

An Observation is not promoted to `MemoryEntry` automatically. Whether it
becomes a `MemoryProposal` depends on classification, whitelist, consent, and
policy constraints defined elsewhere.

## §13. MemoryProposal

A **MemoryProposal** is a canonical candidate for persistence. It is the
governed intermediate step between an Observation and a `MemoryEntry`.

Canonical meaning (AYLA-DEC-0067, AYLA-DEC-0069):

```text
MemoryProposal
=
canonical candidate for persistence
```

A `MemoryProposal`:

- is **not** a `MemoryEntry`;
- is **not yet** Persistent Memory;
- may carry classification, policy, or audit metadata;
- may originate from different provenance paths.

This section does not define a full lifecycle. The statuses
`pending_confirmation`, `accepted`, `rejected`, and `expired` are recognized in
AYLA-DEC-0024 as part of the canonical `MemoryProposal` lifecycle, but Wave 2A
does not specify transitions, triggers, or runtime mechanics. Those belong to a
future lifecycle wave.

For an AI inference, the canonical order is AI inference -> `MemoryProposal` (pending_confirmation) -> explicit user confirmation -> accepted `MemoryProposal` -> whitelist check -> governed persistence boundary. Other proposals may be accepted through another canonically approved provenance or policy path. The existence of a proposal does not imply a particular confirmation mechanism.

**Practical explanation:** A `MemoryProposal` is "the system thinks this might be
worth remembering, but it has not yet crossed the persistence boundary." It is a
candidate under review. A `MemoryProposal` may be persisted as a proposal record
(for example, to track status, TTL, and audit history), but it is not a
`MemoryEntry` and not a Persistent Memory Fact.

## §14. MemoryEntry

A **MemoryEntry** is a canonical persisted memory record/fact in the Memory
Domain.

A `MemoryEntry` is distinct from:

```text
MemoryEntry
≠ Observation

MemoryEntry
≠ MemoryProposal

MemoryEntry
≠ Authoritative Backend Fact

MemoryEntry
≠ AI inference by default
```

A `MemoryEntry` carries provenance semantics — it must remain traceable to its
origin — but Wave 2A does not define a field schema, metadata object, status
enum, TTL, storage class, event payload, or database representation.

Where upstream canon establishes an immutable correction / supersession
principle, Wave 2A records it as a semantic invariant: a change to a memory fact
is expressed as supersession (old entry becomes superseded, new entry becomes
active) rather than silent in-place rewriting. The detailed correction flow is
left to a future wave.

**Practical explanation:** A `MemoryEntry` is "a fact the system has decided to
keep under the Memory Contract." Persistence makes it available for governed
retrieval; it does not make the fact more true than its provenance allows.

## §15. Knowledge Provenance

**Provenance** shows where Ayla obtained or derived a particular piece of
knowledge.

Canonical provenance values, as established by AYLA-DEC-0024, are:

- `user_stated`
- `user_confirmed_inference`

The following conceptual categories are used to discuss origins that appear in
observations, backend facts, and model outputs. Categories other than the two
canonical values above are treated as **conceptual categories / proposed
mapping** until a separate owner decision canonizes them:

- `authoritative_backend`
- `system_observed`
- `ai_inferred`
- `derived`

### §15.1. Provenance categories

For each origin, the table below shows source authority, epistemic character of
the origin (not a score of truthfulness), whether it may become a
`MemoryProposal`, whether it may become a `MemoryEntry` directly, whether it
requires confirmation, and whether provenance must remain traceable. Where canon
does not define an answer, the cell is marked `NOT_DEFINED`.

| Origin | Source authority | Epistemic character of origin | May become `MemoryProposal`? | May become `MemoryEntry` directly? | Requires confirmation? | Provenance must remain traceable? |
| --- | --- | --- | --- | --- | --- | --- |
| `user_stated` | User | User claim; describes origin, not truth | YES | YES, after policy / consent / whitelist gates | NO for the statement itself | YES |
| `user_confirmed_inference` | User confirming an AI inference | User-adopted inference; confirmed origin, not truth | YES | YES, after policy / consent / whitelist gates | YES, by definition | YES |
| `authoritative_backend` | Authoritative backend domain | Authoritative within that domain's scope; origin is backend | POSSIBLE | NO — foreign-owned fact | NOT_DEFINED | YES |
| `system_observed` | System observation / process | Observation of behavior or state; describes what was seen | POSSIBLE | NO | USUALLY YES | YES |
| `ai_inferred` | AI model | Model hypothesis; not a fact until confirmed | YES, after explicit confirmation | NO — explicit confirmation required per AYLA-DEC-0023 | YES | YES |
| `derived` | Computation over other facts / inferences | Computed from sources; character follows source provenance | POSSIBLE | NO | USUALLY YES | YES |

`POSSIBLE` means the origin can feed a proposal under an approved path; it does
not mean automatic promotion.

`USUALLY YES` indicates the canonical default for this conceptual category, but the exact confirmation rule is `NOT_DEFINED` at the level of Wave 2A.

For ai_inferred, the canonical order is AI inference -> `MemoryProposal` (pending_confirmation) -> explicit user confirmation -> accepted `MemoryProposal` -> whitelist check -> governed persistence boundary.

### §15.2. Provenance matrix (illustrative)

The examples below are illustrative, not a normative data model.

| Knowledge origin | Example | Authority | Persistence implication | Confirmation implication |
| --- | --- | --- | --- | --- |
| `user_stated` | User says "I prefer evening appointments." | User statement | May become `MemoryEntry` after whitelist / consent / policy gates. | No separate confirmation needed for the statement itself. |
| `authoritative_backend` | Backend records that an appointment occurred. | Backend domain | Remains a backend fact; not automatically a `MemoryEntry`. | NOT_DEFINED |
| `ai_inferred` | AI infers the user may prefer recovery massage. | Hypothesis | May become a `MemoryProposal`; cannot become `MemoryEntry` without explicit user confirmation and whitelist check. | Explicit confirmation required. |
| `user_confirmed_inference` | User confirms the AI inference about massage preference. | User-adopted inference | May become `MemoryEntry` after gates. | Confirmation already occurred. |

## §16. Epistemic Model

The epistemic model defines what Ayla treats as a fact, an observation, an
inference, or an assumption.

### §16.1. Epistemic categories

| Concept | What it means | Source | Authoritative? | Persistent by default? | Owned by Memory Domain? | What can promote it toward `MemoryEntry` |
| --- | --- | --- | --- | --- | --- | --- |
| **Authoritative Backend Fact** | A fact owned and authored by a backend domain. | Backend domain | Yes, within that domain | In the backend source system | NO | Reading or referencing it does not transfer ownership; it does not become a `MemoryEntry` automatically. |
| **User-provided statement** | Something the user explicitly communicated. | User | Yes, as the user's statement | NO | NO (as raw statement) | Whitelist / category check, consent, policy gates → `MemoryProposal` → `MemoryEntry`. |
| **Observation** | A signal the system saw or received. Does not include model-generated hypotheses. | User, backend, conversation, behavior | NO | NO | NO | Classification and policy evaluation may produce a `MemoryProposal`. |
| **AI Inference** | A hypothesis generated by a model. | AI / model | NO | NO | NO | Explicit user confirmation -> `MemoryProposal` -> whitelist check -> `MemoryEntry`. |
| **Derived Interpretation** | A conclusion produced by computation over facts or inferences. | Computation | Only as strong as its sources | NO | NO | Re-confirmation or approved derivation path → `MemoryProposal` → `MemoryEntry`. |
| **Preference** | An epistemic classification of knowledge about a user's preference. | User statement, confirmed inference, or approved source | Depends on source | NO | NO (classification, not entity) | Same source path as the underlying knowledge. |
| **MemoryProposal** | A canonical candidate for persistence. | Observation, inference, or approved source | NO (candidate) | NO | YES | Crossing the governed persistence boundary → `MemoryEntry`. |
| **MemoryEntry** | A canonical persisted memory fact governed by the Memory Contract. | Promoted from approved provenance | As strong as its provenance | YES | YES | Already a `MemoryEntry`; may be superseded by a new entry. |

### §16.2. Critical epistemic rules

```text
AI inference ≠ User Fact
Observation ≠ Persistent Memory Fact
Backend Fact ≠ MemoryEntry merely by existing
MemoryProposal ≠ MemoryEntry
Persistence does not magically increase truthfulness
```

The last rule is essential: the fact that information is stored as a
`MemoryEntry` does not make it more true than its original provenance allows.

### §16.3. Entity classification table

| Concept | Canonical entity? | Persisted by Memory Domain? | Owner | Notes |
| --- | --- | --- | --- | --- |
| Observation | NO | NO | Source domain (Conversation, Backend, etc.) | Consumed as input; may inform a `MemoryProposal`. |
| MemoryProposal | YES | YES (as a proposal record) | Memory Domain | Canonical candidate for persistence; may be persisted to track status / TTL / audit, but it is not a `MemoryEntry` and not a Persistent Memory Fact. |
| MemoryEntry | YES | YES | Memory Domain | Canonical persisted memory record / fact. |
| Authoritative Backend Fact | NO | NO | Respective backend domain | Foreign concept; read / referenced, not converted automatically. |
| AI Inference | NO | NO | AI / Intent domain | Not automatically an entity. |
| Preference | NO | NO | Memory Domain (classification only) | Epistemic classification, not a persistence entity. |
| Conversation Context | NO | NO | Conversation Domain | Maintains conversational continuity and semantic coherence across Sessions, Interactions, and Dialogue Turns. |
| Consent State | NO | NO | Consent / Privacy Domain | Gating state, not a memory fact. |

Memory Eligibility is referenced here only as a decision concept, not as a
canonical entity (AYLA-DEC-0070).

### §16.4. Confidence semantics

`confidence` is **not** a mandatory field on `MemoryEntry`. AYLA-DEC-0024
explicitly prohibits `confidence` in the canonical `MemoryEntry`.

The following confidence concepts may exist as proposal / audit / policy
metadata, consistent with AYLA-DEC-0067:

- `proposal_confidence`
- `classification_confidence`
- `inference_confidence`

These are distinct from the truth status of a `MemoryEntry`:

```text
confidence of inference
≠
truth status of MemoryEntry
```

A high-confidence inference remains an inference until it follows an approved
confirmation path.

### §16.5. Preference semantics

A **Preference** is an epistemic classification of knowledge about a user's
preference. It is not a `MemoryEntry` entity type automatically, not an
authoritative backend fact, and not always permanent.

The persistence and authority of a preference depend on the provenance of the
underlying knowledge (for example, `user_stated` vs
`user_confirmed_inference` vs `derived`). The Memory Domain does not introduce a
separate canonical `Preference` persistence entity in Wave 2A.

### §16.6. ADR-0012 classification

ADR-0012 is used in Wave 2A only within the limits set by AYLA-DEC-0067. The
following ADR-0012 elements are absorbed as classification / policy / audit
dimensions attached to `MemoryProposal` and related audit metadata, not as a
second competing lifecycle for `MemoryEntry`:

| ADR-0012 element | Wave 2A classification |
| --- | --- |
| `knowledge_class` | CLASSIFICATION / POLICY / AUDIT_DIMENSION |
| `confidence` dimension (proposal / classification / inference confidence) | CLASSIFICATION / POLICY / AUDIT_DIMENSION |
| `lifetime` | CLASSIFICATION / POLICY / AUDIT_DIMENSION |
| `provenance` (as a policy/classification dimension beyond the canonical values `user_stated` and `user_confirmed_inference`) | CLASSIFICATION / POLICY / AUDIT_DIMENSION |
| `freshness` / `sensitivity` semantics | CLASSIFICATION / POLICY / AUDIT_DIMENSION |

The canonical provenance values `user_stated` and `user_confirmed_inference`
remain CANONICAL_REQUIRED per AYLA-DEC-0024. Any additional provenance
vocabulary proposed by ADR-0012 is PROPOSED / NOT YET CANONICAL until an owner
decision adopts it.

No ADR-0012 draft field is treated as a mandatory contract field for
`MemoryEntry` in Wave 2A.

## §17. Confirmation and Contradiction Semantics

This section defines conceptual meanings only. It does not design confirmation
workflows.

### §17.1. Conceptual definitions

- **Confirmation.** An explicit act that increases the epistemic status of a
  proposal or permits its persistence where canon allows.
- **Contradiction.** New evidence that conflicts with an existing `MemoryEntry`
  or `MemoryProposal`.
- **Correction.** A change to a memory fact expressed as supersession of an old
  entry by a new entry, preserving history.
- **Disagreement.** A user's explicit rejection or objection to a proposal or
  inference.

### §17.2. Confirmation rules

```text
silence ≠ confirmation
dialogue continuation ≠ confirmation
user confirmation may increase epistemic status / permit persistence where canon allows
```

The absence of an explicit objection does not promote a `MemoryProposal` to a
`MemoryEntry`. Continuing a conversation does not implicitly confirm pending
proposals.

### §17.3. Contradiction handling principles

```text
new evidence may contradict an existing MemoryEntry
contradiction ≠ automatic overwrite
contradiction should preserve provenance/history
```

When contradiction occurs, the existing `MemoryEntry` must not be silently
rewritten. A correction produces a new active entry and marks the old entry
superseded, consistent with the immutable correction principle. Detailed
conflict-resolution mechanics are left to a future wave.

If source-priority for conflicting sources is not defined by canon:

```text
SOURCE_PRECEDENCE_NOT_DEFINED
```

This remains a downstream concern.

## §18. Wave 2A Invariants

The following invariants are established by Wave 2A and upstream canon:

1. **Observation ≠ MemoryProposal.** An observed signal is not a candidate for
   persistence merely because it was seen.
2. **MemoryProposal ≠ MemoryEntry.** A candidate is not a persisted memory fact
   until it crosses the governed persistence boundary.
3. **MemoryEntry persistence ≠ increased truth authority.** Persistence does
   not make a fact more true than its provenance allows.
4. **AI inference ≠ User Fact.** A model-derived hypothesis is not a user fact
   without an approved confirmation path.
5. **Authoritative Backend Fact remains owned by backend source.** Reading or
   referencing it does not transfer ownership.
6. **Provenance must not be silently erased.** The origin of a `MemoryEntry`
   must remain traceable.
7. **Confirmation ≠ silence.** The absence of objection does not confirm a
   proposal.
8. **Contradiction ≠ silent overwrite.** Conflicting evidence must not silently
   merge into a single unquestioned fact.
9. **Memory Domain does not acquire ownership of foreign facts.** Reading,
   projecting, or using a fact from another domain does not transfer ownership.

These are Wave 2A invariants only; global invariants for the complete Memory
Model will be finalized in later waves.

## §19. Memory Identity Overview

Wave 2B defines the semantic identity boundary for a `MemoryEntry`. A memory
entry represents one semantic piece of knowledge within a relevant context.
Identity is therefore determined by meaning together with the context that is
relevant to that meaning.

The following distinctions are normative:

```text
record identity ≠ semantic identity
text equality ≠ semantic identity
textual similarity ≠ semantic identity
```

This wave defines semantic relationships only. It does not define a canonical
key, comparison procedure, similarity threshold, storage representation, or
runtime operation.

## §20. Semantic Identity

Two records may refer to the same semantic memory only when their semantic
meaning and relevant context align. Matching wording, matching record
attributes, or an observed degree of similarity is insufficient by itself.

Semantic identity is a property of the knowledge represented, not of the
transport record that carried it. A change in wording does not necessarily
create a different memory, and identical wording does not necessarily identify
the same memory when the relevant context differs.

The complete determination of semantic identity is `NOT_DEFINED` beyond the
normative boundary established here. Canonical identity keys and automated
identity tests are `OUT_OF_SCOPE`.

## §21. Memory Granularity

Memory granularity is determined by meaning and relevant context. It is not
determined by the number of sentences, messages, or source events.

Accordingly:

- one source message may express one or multiple semantic memories;
- multiple source expressions may relate to one semantic memory when the
  applicable semantic and context rules align;
- message, sentence, and source-event boundaries are not memory identity
  boundaries by themselves.

The rules for automatically splitting or grouping source expressions, as well
as any atomic field model, are `OUT_OF_SCOPE`.

## §22. Multiple Provenance

One semantic memory may have multiple independent provenance sources. Different
provenance alone does not require a separate `MemoryEntry`.

Provenance diversity does not change semantic identity by itself. At the same
time, the origin and history of each contributing source must remain
traceable; provenance must not be silently erased or reduced to an
unqualified assertion of authority.

This section does not define a mandatory provenance schema, an `Evidence`
entity, a provenance relation model, or a storage representation. Those details
are `OUT_OF_SCOPE`.

## §23. Semantic Equivalence

Semantic equivalence is a semantic relationship between records or expressed
knowledge. It does not by itself authorize duplicate treatment or any
destructive consolidation.

The following distinctions are mandatory:

```text
semantic similarity ≠ semantic equivalence
semantic equivalence ≠ duplicate
duplicate ≠ merge
merge ≠ deletion
```

No destructive consolidation may be inferred solely from textual similarity,
semantic similarity, or semantic equivalence. Detection and determination
procedures are `NOT_DEFINED`; similarity algorithms, embeddings, LLM
comparison, and thresholds are `OUT_OF_SCOPE`.

## §24. Duplicate vs Merge

`Duplicate` and `merge` describe different semantic decisions. A relationship
that two records are duplicates does not itself define how they are
consolidated. A merge, if a future governed decision permits one, does not
mean that an underlying record or its provenance may be deleted.

The Memory Model therefore preserves these boundaries:

- semantic identity does not automatically establish duplicate status;
- duplicate status does not automatically authorize a merge;
- a merge does not automatically authorize deletion;
- provenance and relevant history remain protected through any future
  downstream policy.

Duplicate determination, merge authorization, merge semantics, and deletion
policy are `OUT_OF_SCOPE` for Wave 2B.

## §25. Relevant Context

Relevant Context is part of the semantic identity of a `MemoryEntry`. The same
meaning in different relevant contexts may therefore represent different
semantic memories.

Context is not an optional annotation external to identity when it changes the
meaning or applicability of the knowledge. Conversely, this decision does not
make every surrounding circumstance an identity dimension.

The complete set of context dimensions is `NOT_DEFINED` and is not made
canonical by this wave. Service, Transformation Goal, scenario, tenant,
locale, channel, time, or any other candidate dimension is not mandatory here
unless established by separate canon.

## §26. Source Precedence Boundary

The Memory Model does not define a universal or global precedence order between
knowledge sources. It does not establish rules such as backend over user,
user over backend, confirmed inference over another source, or AI over user.

The Memory Model owns provenance semantics, relationship semantics, and
contradiction visibility. Source precedence may depend on knowledge type,
policy, purpose or use case, context, consent, safety rules, and future domain
decisions.

Where the applicable source precedence is not defined by canon:

```text
SOURCE_PRECEDENCE_NOT_DEFINED
```

Global source ranking, priority algorithms, and conflict reconciliation are
`OUT_OF_SCOPE`.

## §27. Canonical Identity Invariants

The following invariants are normative for the Memory Domain:

1. A `MemoryEntry` represents semantic meaning within relevant context.
2. Record identity, text equality, and textual similarity do not establish
   semantic identity by themselves.
3. Granularity follows meaning and relevant context, not message or transport
   boundaries.
4. Multiple provenance sources may support one semantic memory.
5. Different provenance alone does not require a new `MemoryEntry`.
6. Provenance origin and history must remain traceable.
7. Semantic similarity does not establish semantic equivalence.
8. Semantic equivalence does not establish duplicate status.
9. Duplicate status does not establish merge authorization.
10. Merge does not establish deletion authorization.
11. Relevant Context participates in semantic identity.
12. Context dimensions are not canonicalized by this wave.
13. The Memory Model does not define global source precedence.
14. An unresolved applicable precedence boundary remains
    `SOURCE_PRECEDENCE_NOT_DEFINED`.

These invariants define semantics only. They do not define identifiers,
schemas, algorithms, storage, APIs, retrieval ranking, or runtime behavior.

## §28. Wave 2B Summary

Wave 2B canonicalizes Memory Identity as semantic meaning plus relevant
context. It establishes that granularity follows meaning and context, that one
semantic memory may have multiple traceable provenance sources, and that
semantic relationships must not be conflated with duplicate, merge, or deletion
decisions.

Relevant Context participates in identity, while its complete dimensions remain
`NOT_DEFINED`. The Memory Model also preserves the boundary that no universal
source precedence is defined. All implementation and policy details expressly
excluded by this wave remain `OUT_OF_SCOPE` for a future governed decision.

## §29. Memory Lifecycle Overview

The Memory Model distinguishes the lifecycle of a MemoryProposal from the lifecycle of a MemoryEntry. A proposal is a candidate for persistence; an entry is the persisted memory fact after the governed persistence boundary has been crossed. Acceptance does not make the proposal and entry the same record or identity. Lifecycle semantics define canonical state meaning, not a runtime state machine, transition algorithm, timer, scheduler, API, or storage mechanism.

Approved AI inference ordering: AI Inference -> MemoryProposal -> explicit user confirmation -> accepted MemoryProposal -> whitelist/policy gate -> governed persistence boundary -> MemoryEntry.

## §30. MemoryProposal Lifecycle

Canonical states are pending_confirmation, accepted, rejected, and expired. pending_confirmation awaits the governed decision; accepted records explicit confirmation and may proceed through policy and persistence; rejected records explicit decline; expired is no longer valid for confirmation under its canonical lifetime. None of these states is Persistent Memory or a MemoryEntry.

## §31. MemoryEntry Lifecycle

Canonical states are active, superseded, expired, deletion_pending, and deleted. active is the current persisted fact subject to purpose-specific eligibility; superseded is an immutable historical entry replaced by a later entry; expired has reached its applicable lifetime and is not readable as current memory; deletion_pending means deletion is not complete; deleted means the canonical deleted lifecycle state has been reached.

superseded is not expired; expired is not revocation; revocation is not deletion; deletion_pending is not deleted. Revocation is a consequence applied to an entry, not an additional canonical state. Reconfirmation is a usage/freshness gate, not a lifecycle state.

## §32. Correction and Supersession

Correction is immutable and is not in-place overwrite:

    old MemoryEntry -> superseded
    new MemoryEntry -> active
    old.superseded_by -> new identity

Supersession preserves history and provenance while the corrected value gets a new record identity. Merge, deduplication, precedence, conflict resolution, and runtime operations remain out of scope.

## §33. Expiry, Revocation, and Deletion Boundary

Expiry means the applicable lifetime has ended and the entry is not readable as current memory; it is not deletion. Revocation means consent revocation was applied, making the entry unreadable and, where applicable, may result in the canonical deletion_pending consequence; it is not deletion. deletion_pending means deletion is pending, not complete. deleted means the canonical deleted state, without defining physical purge, tombstones, legal erasure, or delivery semantics.

memory.entry_revoked means the Memory consequence of consent.revoked; it does not transfer consent ownership to Memory. memory.entry_deleted is not defined in this wave. Its meaning, deletion contract, tombstone behavior, and cross-context consumers remain unresolved under DER_OQ_E4_DEPENDENCY. No final deletion event name, payload, purge implementation, legal-erasure workflow, or delivery contract is introduced.

## §34. Memory Event Semantics

| Event | Semantic meaning | Related entity | Lifecycle relevance | What it does NOT mean |
| --- | --- | --- | --- | --- |
| memory.proposal_created | A MemoryProposal was created as a candidate for governed confirmation. | MemoryProposal | Proposal existence in pending_confirmation context. | Persistence approval or Persistent Memory. |
| memory.proposal_confirmed | The user explicitly confirmed the proposal. | MemoryProposal | Establishes accepted meaning and permits persistence to be considered. | That a MemoryEntry already exists. |
| memory.proposal_rejected | The user rejected the proposal. | MemoryProposal | Establishes rejected meaning; that proposal does not create memory. | Deletion or supersession of an existing entry. |
| memory.entry_created | A MemoryEntry was created in active state after confirmation, whitelist, and policy gates. | MemoryEntry | Establishes persisted-entry existence. | Universal eligibility, automatic retrieval, automatic rendering, automatic permission for every purpose, or ownership of foreign facts. |
| memory.entry_superseded | An immutable old entry was superseded by a new entry through correction semantics. | Old and new MemoryEntry identities | Old becomes superseded and new becomes active. | Deletion, expiry, or in-place overwrite. |
| memory.entry_expired | The entry lifetime has ended and it is no longer readable as current memory. | MemoryEntry | Represents expired lifecycle meaning. | Deletion or revocation. |
| memory.entry_revoked | Consent revocation was applied, making the entry unreadable and producing the canonical deletion_pending consequence. | MemoryEntry and consent consequence | Represents revocation-related lifecycle impact. | Consent ownership transfer, physical deletion, or memory.entry_deleted. |

Event identity is not MemoryEntry identity; source_event_id is not a semantic identity key; event idempotency is not memory deduplication.

## §35. Domain Event Registry Boundary

Memory Model owns event semantic meaning, lifecycle relevance, domain invariants, and relationships to MemoryProposal/MemoryEntry. DER/runtime governance owns registration_status, schema/payload, serialization, versioning, producer and consumer wiring, delivery, retries, topics/queues, outbox, and idempotency implementation. This wave does not change DER status: current memory events remain proposed. Future proposed-to-registered reconciliation is a CROSS_DOCUMENT_FOLLOW_UP.

## §36. Wave 3 Lifecycle & Event Invariants

1. MemoryProposal is not MemoryEntry.
2. An accepted proposal is not the same record identity as the resulting entry.
3. AI inference requires explicit user confirmation before governed persistence.
4. Correction is not in-place overwrite; supersession preserves history.
5. Supersession, expiry, revocation, and deletion_pending are distinct.
6. deletion_pending is not deleted.
7. Reconfirmation is a usage/freshness gate, not a lifecycle state.
8. Event meaning is distinct from DER registration mechanics.
9. Event identity/idempotency are distinct from memory identity/deduplication.
10. Active MemoryEntry is not universally eligible for every use.
11. Consent remains foreign-owned; its change may cause a Memory consequence.
12. memory.entry_deleted remains undefined while DER_OQ_E4_DEPENDENCY is open.

### Conceptual event-to-lifecycle audit

| Event | Before state/context | After state/context | Canon evidence |
| --- | --- | --- | --- |
| memory.proposal_created | Proposal context not established | pending_confirmation | DEC-0023, DEC-0024, DEC-0071, DER 6.4 |
| memory.proposal_confirmed | pending_confirmation | accepted | DEC-0023, DEC-0024, DEC-0071, DER 6.4 |
| memory.proposal_rejected | pending_confirmation | rejected | DEC-0024, DEC-0071, DER 6.4 |
| memory.entry_created | Persistence boundary completed; no entry existence established | active MemoryEntry | DEC-0024, DEC-0067, DEC-0071, DER 6.4 |
| memory.entry_superseded | Old entry active; replacement context exists | Old superseded; new active | DEC-0024, DEC-0067, DEC-0071, DER 6.4 |
| memory.entry_expired | Entry current and lifetime not ended | expired | DEC-0024, DEC-0071, DER 6.4 |
| memory.entry_revoked | Entry readable before applicable consent revocation | Unreadable; deletion_pending consequence where applicable | DEC-0024, DEC-0071, DER 6.4, Consent Scope Registry |

This is a conceptual audit, not a runtime FSM. No transition is inferred for memory.proposal_expired because DER marks it only as a candidate. No deletion transition is inferred because of DER_OQ_E4_DEPENDENCY.
