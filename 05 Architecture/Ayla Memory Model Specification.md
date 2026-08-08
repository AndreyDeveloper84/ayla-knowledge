---
node_id: ayla.domain.memory-model

title: Ayla Memory Model Specification
title_ru: Спецификация модели памяти Ayla

type: domain-specification
status: draft
decision_status: proposed
canonical_status: candidate
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
| Document status | draft |
| Decision status | proposed |
| Canonical status | candidate |
| Wave | Wave 1 — Foundation |
| Active Canon | no |

This document contains the Foundation of the Ayla Memory Model Specification.
Only §§1–10 are written in Wave 1. Sections §§11 and above are intentionally
omitted and will be added by subsequent locked waves.

This release establishes terminology, ownership boundaries, normative
principles, and the conceptual position of the Memory Domain. It does not yet
define entity field schemas, lifecycle state machines, eligibility algorithms,
retrieval algorithms, TTL values, event payloads, or storage contracts.

Until the remaining waves are completed and the document is moved out of draft
status, this specification must **not** be treated as an implementation
contract.

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

On the candidate stage, the position above is a **normative target**, not a
claim that the document is already Active Canon.

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
| OWNER_DECISION_REGISTER AYLA-DEC-0067…0073 | Locked foundation rulings for Memory Domain. | Required; present. |

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
AYLA-DEC-0067…0073 and compatible upstream canon:

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
