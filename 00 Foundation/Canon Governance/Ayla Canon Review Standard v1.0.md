---
node_id: ayla.foundation.canon-governance.canon-review-standard
title: Ayla Canon Review Standard v1.0
type: standard
status: draft
canonical_status: candidate
version: "1.0"
owner: Product Owner
knowledge_area:
  - foundation
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
updated: 2026-08-12
review_cycle: quarterly
---

# Ayla Canon Review Standard v1.0

Status: `CANDIDATE FOR PRODUCT OWNER REVIEW`

## 1. Purpose

This document defines the mandatory review standard for every Ayla Canon Review.

Canon Review answers exactly one question:

> Is this document ready to become Ayla Canon?

It validates that a candidate document faithfully expresses approved Product decisions, preserves Ayla Product Philosophy, and remains free of contradictions, scope drift, and implementation leakage.

Canon Review does **not**:

- redesign documents;
- create Product decisions;
- invent implementation;
- reopen approved Product decisions;
- change repository structure;
- define technical architecture.

### Product Decision Lifecycle vs. Canon Review

The [Ayla Product Decision & Canon Authoring Process v1.0](Ayla%20Product%20Decision%20&%20Canon%20Authoring%20Process%20v1.0.md) defines how Product questions move from open question to approved decision to candidate prose.

Canon Review is the independent fidelity check that happens at the end of that lifecycle. It begins only after a Writer has produced a document marked `CANDIDATE FOR CANON REVIEW`.

| Activity | Product Decision Lifecycle | Canon Review |
|---|---|---|
| Decides Product questions | Yes | No |
| Writes candidate prose | Yes | No |
| Validates fidelity to decisions | Partially | Yes |
| Detects contradictions | Yes | Yes |
| Checks terminology consistency | Partially | Yes |
| Verifies implementation leakage | Partially | Yes |
| Produces canonicalization verdict | No | Yes |

## 2. Core Principles

Canon Review is governed by eight principles. They keep the review lightweight, repeatable, and independent of any specific repository or implementation.

1. **Protect Product Canon.** Canon Review exists to prevent weak, contradictory, or premature documents from becoming canonical. A rejected candidate is preferable to a broken canon.
2. **Preserve approved Product decisions.** The reviewer checks that every approved decision appears in the document, unchanged in substance, and that no new decision appears without an approved source.
3. **Validate, do not redesign.** The reviewer reports problems; the Writer fixes them. Reviewer suggestions must not become hidden redesigns.
4. **Detect contradictions.** Internal contradictions and contradictions with higher canon must be surfaced explicitly.
5. **Detect implementation leakage.** Product Canon must not silently invent APIs, databases, payloads, event buses, transport, or runtime contracts.
6. **Preserve terminology.** Canon terms must be used consistently. Synonym drift, accidental renaming, and competing definitions must be flagged.
7. **Preserve Product Philosophy.** The reviewer explicitly checks that Ayla philosophy — intent-first, conversation-first, human-first, progressive disclosure, trust, transparency, MVP-first — remains intact.
8. **Review must remain lightweight.** A Canon Review is a focused gate, not a second authoring cycle. The standard matrix and verdict vocabulary keep it bounded.

## 3. Canon Readiness Matrix

The matrix is the mandatory checklist for every Canon Review. The reviewer must produce evidence for each category before declaring a verdict.

| # | Category | Purpose | What reviewer checks | Typical failure | PASS criteria |
|---|---|---|---|---|---|
| 1 | Product Decisions | Ensure all approved decisions are present and none are invented. | Decision list; decision IDs; approval status; completeness. | Missing decision; new requirement without decision source. | Every approved decision is represented; no unapproved decision appears. |
| 2 | Traceability | Ensure decisions are traceable and stable. | Stable IDs; active/superseded status; index consistency. | Duplicate active decision; broken ID; superseded decision still active. | `TRACEABILITY STATUS: CLEAN` conditions are met. |
| 3 | Product Language | Protect canonical product concepts. | Task, Journey, Intent, Goal, First Contact, and related concepts. | Accidental renaming; competing synonyms; duplicated concepts. | Product language matches approved canon and glossary. |
| 4 | Terminology Stability | Prevent silent terminology drift. | Synonym drift; inconsistent naming; silent term changes. | Same concept called by multiple names; term meaning changed without approval. | Terminology is consistent with Glossary and higher canon. |
| 5 | Canon Level Validation | Keep canon layers separated. | Product Canon vs. UX Canon vs. Technical Canon vs. Runtime. | Product concept moved to technical layer; runtime detail in product layer. | Each concept lives at the correct canon level. |
| 6 | Product Philosophy | Ensure Ayla philosophy is preserved. | Human-first, intent-first, conversation-first, progressive disclosure, trust, transparency, MVP-first. | Principle contradicted; philosophy weakened or reinterpreted. | Philosophy explicitly confirmed preserved. |
| 7 | Architecture Consistency | Ensure internal coherence and boundary discipline. | Internal consistency; hidden contradictions; ownership boundaries; layering. | Contradictory requirements; boundary violation; mixed ownership. | Document is internally consistent and respects boundaries. |
| 8 | Scope Discipline | Prevent scope leakage and expansion. | Scope boundaries; neighbouring specification growth; accidental architecture. | Feature creep; scope expansion beyond approved decisions; new domain introduced silently. | Scope matches approved decisions and release contract. |
| 9 | Implementation Leakage | Prevent product canon from inventing implementation. | APIs, payloads, persistence, database, runtime mapping, EventBus, transport, lifecycle contracts. | API shape specified; database implied; event contract invented. | No implementation detail unless explicitly approved by higher canon. |
| 10 | Writer Fidelity | Ensure Writer did not alter decisions. | Strengthening, weakening, reinterpreting, inventing, or merging decisions. | Decision softened; multiple decisions merged; rationale invented. | Writer faithfully translated approved decisions into prose. |

## 4. Mandatory Review Checks

### 4.1 Product Decisions

Verify that the document is complete with respect to approved Product decisions.

- Check that every approved decision relevant to the document is represented.
- Check that no decision is duplicated unless duplication is intentional and marked.
- Check that no new Product decision appears without an approved source.
- Check that decision IDs referenced in the document match the active decision index.

Typical failures:

- A decision is omitted because it was uncomfortable or inconvenient.
- Two similar decisions are restated as one, losing nuance.
- A requirement is added that was never approved.

PASS criteria: every approved decision is present, no decision is invented, and no active decision is duplicated.

### 4.2 Traceability

Verify that the chain from question to decision to prose is intact.

- Stable Question/Decision IDs are present and correct.
- No duplicate active decision exists for the same question.
- Superseded decisions are inactive but remain traceable.
- References to higher canon are accurate and current.

Typical failures:

- A decision ID in the document does not exist in the index.
- A superseded decision is still treated as active.
- Two active decisions answer the same question differently.

PASS criteria: the document would pass a `TRACEABILITY STATUS: CLEAN` declaration.

### 4.3 Product Language

Review the document's use of canonical Product Concepts.

Examples of Product Concepts to guard:

- Task
- Journey
- Intent
- Goal
- First Contact
- Transformation Goal
- Living Digital Twin
- User Model
- Recommendation

Detect:

- accidental renaming of a canonical concept;
- competing synonyms for the same concept;
- duplicated concepts introduced under new names;
- product terms used as implementation terms.

Typical failures:

- "User objective" is used instead of `Goal`.
- "Flow" and "Journey" are used interchangeably.
- "First Meeting" is introduced as a synonym for `First Contact`.

PASS criteria: Product language matches the Ayla Glossary and approved canon.

### 4.4 Terminology Drift

Reviewer must detect drift across the document and relative to existing canon.

- Synonym drift: the same thing is called by multiple names.
- Inconsistent naming: a term is capitalized, hyphenated, or pluralized differently in different sections.
- Silent terminology changes: a term's meaning is shifted without an approved amendment.

Typical failures:

- "Memory" in one section means persistent memory, but in another means session context.
- "Provider" and "Specialist" are swapped without explanation.
- A term is renamed to avoid a difficult decision.

PASS criteria: terminology is stable, consistent, and aligned with the Glossary.

### 4.5 Canon Level Validation

Verify that each concept lives at the correct canon level.

| Canon level | Examples | Must not leak into |
|---|---|---|
| Product Canon | Goal, Intent, Journey, Task, First Contact | API schemas, database tables, event payloads |
| UX Canon | Screen flows, interaction patterns, voice | Runtime contracts, persistence decisions |
| Technical Canon | Domain model, boundaries, ownership | Product philosophy, user goals |
| Runtime / Implementation | API, database, EventBus, transport | Product Canon or UX Canon |

Typical failures:

- A Product Concept is described as a database entity.
- A UX pattern is treated as a product requirement.
- A runtime event is presented as a domain concept.

PASS criteria: no concept silently moves between canon levels.

### 4.6 Product Philosophy Validation

Reviewer must explicitly confirm whether Ayla Product Philosophy has been preserved.

At minimum, check:

- **Intent-first:** the document starts from user intent, not from product mechanics.
- **Conversation-first:** conversational context is treated as a first-class input, not an afterthought.
- **Human-first:** the human remains the center; Ayla, Twin, and tools are helpers.
- **Progressive disclosure:** complexity is revealed gradually, not dumped upfront.
- **Trust:** the document does not undermine user trust through hidden assumptions or pressure.
- **Transparency:** uncertainty, ownership, and boundaries are stated clearly.
- **MVP-first:** scope is bounded to what is needed now; future capabilities are not smuggled into current canon.

Reviewer must record an explicit statement:

```text
PRODUCT PHILOSOPHY STATUS: PRESERVED / NOT PRESERVED
```

Typical failures:

- A requirement forces the user to provide data before any value is delivered.
- A Twin representation is made mandatory where the decision was representation-neutral.
- Commercial optimization is implied as a product requirement.

PASS criteria: philosophy is explicitly confirmed preserved, with no material exceptions.

### 4.7 Architecture Consistency

Review the document for internal coherence and boundary discipline.

- Internal consistency: no two sections contradict each other.
- Hidden contradictions: no assumption in one section silently violates another.
- Ownership boundaries: responsibilities are not assigned to the wrong owner.
- Layering violations: product, UX, and runtime layers are not mixed.

Typical failures:

- One section says a feature is in MVP; another says it is out.
- A product requirement assumes a capability owned by another domain.
- A UX standard is presented as a product rule.

PASS criteria: the document is internally consistent and respects domain and layer boundaries.

### 4.8 Scope Discipline

Detect unapproved scope expansion.

- Scope leakage: the document adds capabilities beyond approved decisions.
- Neighbouring specification expansion: the document specifies adjacent areas that were not assigned to it.
- Accidental architecture growth: the document introduces structural assumptions that exceed its mandate.

Typical failures:

- A First Contact specification begins defining booking workflows.
- A product concept document specifies analytics events.
- A release-scope document silently expands to future releases.

PASS criteria: the document stays within the boundaries of its approved decisions and release contract.

### 4.9 Implementation Leakage

Reviewer verifies that the document does **not** invent implementation unless already approved by higher canon.

The following must not appear in Product Canon unless explicitly authorized:

- API endpoints or payloads;
- persistence mechanisms;
- database schemas or tables;
- runtime mapping rules;
- EventBus or event contracts;
- transport protocols;
- lifecycle contracts;
- deployment or infrastructure details.

Typical failures:

- "The `/goals` endpoint returns..."
- "Goals are stored in the `goals` table..."
- "The GoalCreated event is published to the event bus..."

PASS criteria: the document contains no implementation detail unless that detail is itself approved canon.

### 4.10 Writer Fidelity

Verify that the Writer faithfully translated approved Product decisions into prose.

Writer must not:

- strengthen a decision beyond what was approved;
- weaken a decision to make it easier to implement;
- reinterpret a decision to match a preferred architecture;
- invent decisions, rationale, or scope;
- silently merge multiple decisions into one, losing distinctions.

Typical failures:

- "Users must set a goal" becomes "Users may set a goal".
- Two distinct decisions about memory and consent are merged into a single vague statement.
- A rationale is invented to make a decision sound more reasonable.

PASS criteria: the prose accurately reflects the substance, nuance, and boundaries of every approved decision.

## 5. Canon Readiness Verdict

The review must end with exactly one of three verdicts.

### READY FOR CANON

The document meets all matrix categories. Traceability is clean. Product Philosophy is preserved. No implementation leakage is present. Writer fidelity is confirmed. The document may proceed to canonicalization under Ayla's normal approval rules.

### READY AFTER ONE WRITER PASS

The document is structurally sound and faithful to approved decisions, but contains minor corrections that the Writer can resolve without reopening any Product decision. Examples: terminology inconsistency, broken reference, unclear phrasing, formatting issue.

The reviewer must list the required corrections. After the Writer applies them, a second review is required only if the corrections materially affect meaning.

### BLOCKED

The document cannot become canon until Product Owner or Writer action resolves a material problem. Blockers include missing decisions, broken traceability, terminology inconsistency, mixed canon levels, invented implementation, contradiction of higher canon, or violation of Product Philosophy.

The reviewer must state the blocker, cite the affected matrix category, and recommend the responsible party.

## 6. Stop Conditions

The reviewer MUST block canonicalization when any of the following are true:

- Product decisions are missing or unapproved decisions appear in the document.
- Traceability is broken: duplicate active decisions, missing IDs, or superseded decisions treated as active.
- Terminology is inconsistent or silently changed relative to the Glossary or higher canon.
- Canon levels are mixed: Product Canon contains runtime detail, or UX Canon contains product philosophy.
- Implementation is invented: API, payload, database, event bus, transport, or lifecycle contract appears without approved source.
- Higher canon is contradicted: the document conflicts with the Ayla Constitution, Ayla Product Essence, approved Product Principles, or other canonical Foundation documents.
- Product Philosophy is violated: human-first, intent-first, conversation-first, progressive disclosure, trust, transparency, or MVP-first is materially undermined.
- Writer fidelity is compromised: decisions are strengthened, weakened, reinterpreted, invented, or silently merged.

The reviewer may also block for severe scope discipline or architecture consistency failures if they risk canonicalizing an unbounded or contradictory document.

## 7. Standard Review Output

Every Canon Review must produce a review report with the following sections.

### 7.1 Executive Summary

One paragraph stating:

- document reviewed;
- review date;
- reviewer;
- final verdict;
- one-sentence reason for the verdict.

### 7.2 Strengths

Bulleted list of what the document does well. Be specific. Examples: "Traceability is clean; all BOT-001-Q1 through Q9 decisions are represented." or "Product language is consistent with the Glossary."

### 7.3 Weaknesses

Bulleted list of issues that do not rise to a blocker but should be addressed. Include the matrix category for each.

### 7.4 Canon Readiness Matrix

Copy the matrix from section 3 with evidence filled in for each category. Use concise statements:

```text
Product Decisions: PASS — all approved decisions present
Traceability: PASS — IDs stable, no duplicates
Product Language: ISSUE — "flow" used as synonym for Journey in §4
Terminology Stability: PASS
Canon Level Validation: BLOCKER — database table referenced in §7
Product Philosophy: PASS
Architecture Consistency: PASS
Scope Discipline: ISSUE — adjacent booking workflow described in §9
Implementation Leakage: BLOCKER — API payload specified in §6
Writer Fidelity: PASS
```

### 7.5 Required Corrections

Numbered list of every correction required to reach `READY FOR CANON`. Each item must include:

- location (section or line);
- problem;
- required action;
- owner (Writer or Product Owner).

### 7.6 Final Verdict

State exactly one of:

```text
READY FOR CANON
READY AFTER ONE WRITER PASS
BLOCKED
```

If `READY AFTER ONE WRITER PASS`, list corrections and confirm no Product decision needs to be reopened.

If `BLOCKED`, list blockers, cite the responsible owner, and explain what must happen before the document can be reviewed again.

## 8. Relationship to Governance

This standard complements the [Ayla Product Decision & Canon Authoring Process v1.0](Ayla%20Product%20Decision%20&%20Canon%20Authoring%20Process%20v1.0.md). It does not replace or redesign it.

Key relationships:

- The Product Decision Lifecycle governs how Product questions become approved decisions and candidate prose.
- Canon Review begins only after the Writer produces a document marked `CANDIDATE FOR CANON REVIEW`.
- Canon Review uses the decision status vocabulary and traceability rules defined in the Product Decision Lifecycle.
- The Canon Review report is a required artifact before canonicalization, as defined in the Product Decision Lifecycle.
- The Product Owner remains the sole approver of Product decisions; Canon Reviewer has no decision authority.

## 9. Future Usage

Every future Canon Review should begin by reading:

1. [Ayla Product Decision & Canon Authoring Process v1.0](Ayla%20Product%20Decision%20&%20Canon%20Authoring%20Process%20v1.0.md)
2. Ayla Canon Review Standard v1.0 (this document)

Review prompts, checklists, and agent instructions should reference these Foundation documents instead of embedding long review instructions inline.

When this standard is updated, the version number and `updated` date in the frontmatter must change, and the change must be recorded in the Ayla Decision Log if it affects how canon is validated.

## 10. Status

**This document is a `CANDIDATE FOR PRODUCT OWNER REVIEW`.**

It is not canonical until approved by the Product Owner through Ayla's normal approval process.
