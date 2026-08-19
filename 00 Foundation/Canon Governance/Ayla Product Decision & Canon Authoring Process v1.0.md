---
node_id: ayla.foundation.canon-governance.product-decision-process
title: Ayla Product Decision & Canon Authoring Process v1.0
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

# Ayla Product Decision & Canon Authoring Process v1.0

Status: `CANDIDATE FOR PRODUCT OWNER REVIEW`

## 1. Purpose and Scope

This document defines the standard way Ayla moves from an unresolved Product question to an approved canonical specification.

It applies to product, UX, conversational, and domain-specification authoring where multiple agents collaborate and a canonical outcome is required. It is intentionally lightweight for a startup and compatible with Codex multi-agent work.

It does not replace higher canon such as the Ayla Constitution, Ayla Decision Log, or Ayla Knowledge Architecture Specification. It sits below them and operationalizes how Product decisions become canonical prose.

## 2. Required Principles

The following principles are non-negotiable. Any deviation must be explicitly approved by the Product Owner and recorded.

### 2.1 Decisions before prose
Canonical Writer does not decide Product questions. Product decisions are settled before canonical prose is authored.

### 2.2 Traceability
Every approved Product decision has:

- a stable Question/Decision ID;
- an explicit status;
- a Product Owner decision record;
- one active source.

### 2.3 No silent canonicalization
Architect, Critic, Monitor, Writer, and other agents cannot silently convert a proposal into an approved Product decision. Only the Product Owner can do that.

### 2.4 Supersession is explicit
When a decision changes:

- the new decision explicitly supersedes the old wording;
- active indexes are updated;
- historical evidence remains historical.

### 2.5 Product Canon ≠ Technical Canon
Product concepts may be canonical without implying database, API, or runtime entities. Technical mapping requires separate architecture decisions where necessary.

### 2.6 MVP-first
The process must prevent premature architecture and documentation. Before any detailed design, ask:

- Is the decision required for MVP / Controlled Pilot?
- Would deferring it create unsafe or expensive rework?

If neither is true, defer detailed design.

### 2.7 Writer is downstream
Writer consumes approved decisions. Writer must STOP instead of inventing a missing Product decision.

## 3. Lifecycle

The lifecycle has ten phases. Each phase has an exit criterion that must be met before the next phase begins.

| Phase | Name | Exit criterion |
|---|---|---|
| 1 | Question | Concrete unresolved Product question receives a stable ID. |
| 2 | Context / Evidence | Relevant canon, evidence, constraints, and MVP scope are collected. |
| 3 | Architecture Proposal | Options and trade-offs are documented; status remains proposal. |
| 4 | Critique | Contradictions, scope creep, missing alternatives, and unsafe assumptions are flagged. |
| 5 | Product Owner Decision | Product Owner converts the question into an approved decision record. |
| 6 | Traceability Reconciliation | `TRACEABILITY STATUS: CLEAN` is declared. |
| 7 | Final Architecture Review | `ARCHITECTURE STATUS: READY FOR WRITER` is declared or a blocker is recorded. |
| 8 | Writer | Writer produces candidate canonical prose marked `CANDIDATE FOR CANON REVIEW`. |
| 9 | Canon Review | Independent review confirms fidelity and consistency. |
| 10 | Canonicalization | Document is marked canonical under Ayla's normal approval rules. |

### 3.1 Phase 1 — Question
A concrete unresolved Product question receives a stable ID.

Example ID pattern: `BOT-001-Q7`

The question must be specific enough that a yes/no, chosen-option, or bounded ruling can answer it.

### 3.2 Phase 2 — Context / Evidence
Collect:

- current canon;
- implementation evidence where relevant;
- previous decisions;
- constraints;
- MVP scope boundaries.

This phase is read-heavy. The Context Keeper leads it. No decision is made here.

### 3.3 Phase 3 — Architecture Proposal
The Architect explores design options and trade-offs. The output is a proposal or working decision, not an approved decision.

The proposal should identify at least two real alternatives unless the question is purely factual or has only one valid path.

### 3.4 Phase 4 — Critique
The Critic checks the proposal for:

- contradictions with existing canon;
- scope creep;
- missing alternatives;
- unsafe assumptions;
- MVP fit.

Critique is constructive and specific. It does not veto; it surfaces issues for the Product Owner.

### 3.5 Phase 5 — Product Owner Decision
Only the Product Owner converts the question into an approved Product decision.

The decision record must contain:

- Question ID;
- Decision;
- Status;
- Decided by;
- Date;
- Rationale;
- Scope impact;
- Follow-up items where needed.

### 3.6 Phase 6 — Traceability Reconciliation
Verify:

- correct Question IDs;
- every approved decision appears exactly once as active;
- no duplicate active decision exists;
- superseded files are marked correctly;
- the decision index is current.

Required output before Writer:

```text
TRACEABILITY STATUS: CLEAN
```

### 3.7 Phase 7 — Final Architecture Review
Review the full decision set for:

- internal consistency;
- hidden conflicts;
- completeness against the question set;
- MVP compliance;
- architecture boundaries;
- Writer readiness.

Required result:

```text
ARCHITECTURE STATUS: READY FOR WRITER
```

or an explicit blocker with owner notification.

### 3.8 Phase 8 — Writer
Writer converts approved decisions into coherent candidate canonical prose.

Writer cannot invent Product decisions. If a decision is missing, Writer stops and escalates.

Output:

```text
CANDIDATE FOR CANON REVIEW
```

### 3.9 Phase 9 — Canon Review
An independent Canon Reviewer verifies:

- faithful representation of approved decisions;
- no contradiction with higher canon;
- no invented implementation;
- terminology consistency;
- traceability.

### 3.10 Phase 10 — Canonicalization
Only after successful Canon Review is the document marked canonical according to Ayla's normal approval rules.

## 4. Roles

Roles are lightweight. Not every small decision needs every role.

| Role | Responsibility | Decision authority |
|---|---|---|
| Context Keeper | Recovers relevant prior canon and decisions. | None. |
| Architect | Explores design options and trade-offs. | None. |
| Evidence | Checks current facts, implementation, contracts. | None. |
| Critic | Challenges the proposal for contradictions and risks. | None. |
| Monitor / Gatekeeper | Checks process compliance, traceability, scope, completeness. | Can stop the process; cannot approve Product decisions. |
| Product Owner | Owns Product decisions. | Sole approver of Product decisions. |
| Writer | Writes candidate canonical prose from approved decisions. | None; must stop if a decision is missing. |
| Canon Reviewer | Reviews fidelity and consistency before canonicalization. | None; reports findings to the approval path. |

## 5. Decision Paths

To avoid bureaucracy, use one of two paths.

### 5.1 Lightweight path
For small, reversible, low-risk UX decisions.

```text
Question
→ Architect / Context
→ Product Owner
→ Writer / Review
```

The Monitor may verify traceability after the fact. A formal reconciliation report is optional.

### 5.2 Full path
Use the full multi-agent cycle when the decision is:

- cross-cutting;
- difficult to reverse;
- safety or privacy relevant;
- affects Product Canon;
- affects multiple surfaces or repositories;
- contains multiple dependent Product questions.

`BOT-001` is an example of the full path.

## 6. Decision Status Vocabulary

Keep the vocabulary small.

### 6.1 Questions and decisions

```text
OPEN QUESTION
PROPOSED
WORKING DECISION
OWNER DECISION REQUIRED
APPROVED
SUPERSEDED
DEFERRED
```

### 6.2 Documents

```text
DRAFT
CANDIDATE FOR CANON REVIEW
CANONICAL
```

Do not invent additional statuses without Product Owner approval.

## 7. Required Artifacts

Keep the artifact set minimal.

| Artifact | Full path | Lightweight path | Purpose |
|---|---|---|---|
| Question / decision record | Mandatory | Mandatory | Stable ID and decision history. |
| Decision index | Mandatory | Recommended | Active and superseded decision overview. |
| Reconciliation report | Mandatory | Optional | Proof of `TRACEABILITY STATUS: CLEAN`. |
| Architecture review | Mandatory | Optional | Proof of `ARCHITECTURE STATUS: READY FOR WRITER`. |
| Candidate specification | Mandatory | Mandatory | Writer output for review. |
| Canon review report | Mandatory | Recommended | Independent fidelity check. |

Reports do not become Product decisions.

## 8. Stop Conditions

### 8.1 Writer must stop if

- a Product decision is missing;
- two active decisions contradict each other;
- Question ID traceability is broken;
- the Writer would have to invent API or runtime behavior;
- the current decision conflicts with higher canon.

### 8.2 Gatekeeper must stop canonicalization if

- the decision index is inconsistent;
- superseded decisions remain active;
- new unapproved behavior appears in Writer output;
- `TRACEABILITY STATUS: CLEAN` or `ARCHITECTURE STATUS: READY FOR WRITER` is missing.

## 9. Repository and Canon Hygiene

- Store active Product decisions separately from reports.
- Keep superseded decisions traceable but inactive.
- Do not let reports silently become Product decisions.
- Canonical documents should point to stable decision IDs where useful.
- Implementation evidence is not silently promoted to Product Canon.

Do not prescribe a new repository structure unless current evidence supports one.

## 10. Example

`BOT-001` followed the full path:

```text
Q1–Q9 defined and answered
→ TRACEABILITY STATUS: CLEAN
→ ARCHITECTURE STATUS: READY FOR WRITER
→ Writer produced candidate canonical prose
→ Canon Review
→ Canonicalization
```

This is illustrative only. The content of `BOT-001` is not reproduced here.

## 11. Status

**This document is a `CANDIDATE FOR PRODUCT OWNER REVIEW`.**

It is not canonical until approved by the Product Owner through Ayla's normal approval process.
