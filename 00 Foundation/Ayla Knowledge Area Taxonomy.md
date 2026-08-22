---
node_id: ayla.foundation.knowledge-area-taxonomy
title: Ayla Knowledge Area Taxonomy
type: foundation
status: approved
canonical_status: approved
version: "1.0"
owner: Governance / Architecture
knowledge_area: foundation
system_owner:
  - ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
domain: cross-domain
updated: 2026-08-14
review_cycle: quarterly
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Knowledge Architecture Specification]]"
  - "[[Ayla Repository Responsibility Matrix]]"
  - "[[Ayla Glossary]]"
  - "[[Ayla Domain Capability Registry]]"
---

# Ayla Knowledge Area Taxonomy

> Official governance document for the organization of knowledge in the Ayla project.

## 1. Purpose

This document defines the official structure of Ayla project knowledge, the purpose and responsibility boundaries of each knowledge area, and the rules for placing future documents.

Its goal is to stop the spread of the knowledge architecture, remove ambiguity between folders, and establish clear boundaries between Foundation, Product, Architecture, UX, Engineering, Product Operations, Operations, and Governance.

Knowledge structure is part of project architecture. Knowledge has boundaries, owners, dependencies, lifecycle, and contracts. A document placed in the wrong area can create conflicting sources of truth, hide ownership, and allow implementation details to silently redefine product or domain decisions.

This document is normative for new documents. It does not move, rename, delete, or edit existing files, folders, indexes, canon documents, or contracts.

## 2. Knowledge Architecture Principles

### One canonical location

Every knowledge subject has one primary canonical owner document and one canonical location. Other documents may link to it, use it, or add context, but must not repeat the same meaning.

### Separation of concerns

Foundation, Strategy, Product, Product Operations, Architecture, UX, Engineering, Operations, and Governance have different responsibilities. Similar vocabulary does not make two documents part of the same area.

### Document purpose over folder name

The structure must not be evaluated only by folder name. A document is classified by its actual content, purpose, question answered, owner, contract, and relationships. Current location is evidence for assessment, not proof of canonical responsibility.

### Canon before implementation

First define the product, business, domain, UX, or system contract. Then document implementation. Engineering documentation may explain realization, but must not silently redefine an accepted contract.

### No silent migration

Adopting this taxonomy does not authorize moving, renaming, deleting, copying, rewriting, or changing existing documents or folders. Any migration requires a separate explicit governance decision with impact assessment.

## 3. Canonical Knowledge Areas

| Area | Purpose / problem solved | Contains | Does not contain | Owner |
|---|---|---|---|---|
| `00 Foundation` | Establishes shared principles, terminology, ownership, metadata, and governance. | Constitution, Glossary, Repository Responsibility Matrix, Domain Capability Registry, Decision Log, taxonomy, governance rules. | Specific business features, screen specifications, code, low-level implementation. | Governance / Architecture |
| `01 Product` | Explains why the product exists, for whom it is built, and what product direction and discovery evidence guide it. | Product Vision, Product Principles, Product Strategy, Product Map, User Journeys, Discovery, Conversation Design. | Domain ownership, technical contracts, backend implementation, event schemas. | Product |
| `05 Architecture` | Defines domain and system boundaries, ownership, contracts, and shared data/event semantics. | Domain models, ownership contracts, system boundaries, data contracts, event contracts, MVP Appointment Contract, Domain Event Registry. | Product strategy, screen specifications, marketing strategy, implementation tasks. | Architecture |
| `06 Product` | Defines how business capabilities and product operations should work. | Operational models, business workflows, capability definitions, Product Operations, MVP behavior and operational contracts, Ayla Salon Operations MVP Contract. | Screen designs, domain ownership, low-level APIs, code implementation. | Product Operations |
| `07 UX` | Defines user interaction and screen contracts independently from business and technical ownership. | Screen specifications, interaction contracts, UX flows, information architecture, customer/admin UX contracts. | Domain ownership decisions, product strategy, backend implementation. | UX |
| `08 Engineering` | Explains how accepted contracts are implemented and operated technically. | Coding standards, API specifications, implementation guides, deployment, infrastructure, technical runbooks. | Product intent, business behavior contracts, domain ownership, UX decisions. | Engineering |
| `09 Operations` | Defines real-world operational management and execution. | Operational procedures, support, service delivery, business execution procedures. | Product strategy, system contracts, screen specifications, code implementation. | Operations |
| `Strategy` | Strategy is a knowledge responsibility, not automatically a new physical area. It covers product direction, strategic choices, and discovery. | Strategy documents when they answer why, direction, positioning, or prioritization questions. | Architecture contracts, UX specifications, implementation details. | Product / Governance decision |
| `Governance` | Governs cross-area rules, approvals, conflicts, and ownership decisions. By default it is a responsibility of `00 Foundation`. | Governance decisions, review rules, conflict records, owner decisions. | Feature requirements, implementation details, duplicated area content. | Governance owner |

The existing repository numbering and folders remain unchanged. The table defines responsibility; it does not prescribe a migration.

## 4. Document Classification Rules

| Question answered by the document | Canonical responsibility |
|---|---|
| Why are we building this? | `01 Product` — Product Strategy / Vision / Discovery |
| How should the business function work? | `06 Product` — Product Operations / Operational Contracts |
| Who owns the data and what are the system boundaries? | `05 Architecture` |
| What data and interactions does the screen need? | `07 UX` |
| How is it implemented in code or infrastructure? | `08 Engineering` |
| How is work executed in real-world operations? | `09 Operations` |
| Is this a cross-project rule, term, ownership, or governance decision? | `00 Foundation` / Governance |

If a document answers multiple questions, split it into focused documents where practical. If it cannot yet be split, place it according to its primary decision and link the dependent areas.

Examples:

- `01 Product` may contain Product Strategy, Vision, and Discovery.
- `06 Product` may contain Product Operations and Operational Contracts.
- They must not be merged automatically; classification follows content and responsibility.
- UX MVP documents and BOT specifications must be assessed by content: product intent belongs to Product, interaction behavior belongs to UX, and technical implementation belongs to Engineering.

## 5. Document Creation Rule

A new document is created only when all conditions below are true:

1. There is a separate knowledge artifact requiring independent ownership.
2. The document has a unique purpose not covered by an existing canonical document.
3. Its responsibility is defined as Foundation, Strategy, Architecture, Product, Product Operations, UX, Engineering, Operations, or Governance.
4. Mixing this content into an existing document would violate separation of concerns.

Before creating a new document, the author must inspect the current `ayla-knowledge` structure and verify:

- whether an existing document already owns the knowledge;
- whether the existing document can be extended without violating its responsibility;
- whether the new document would create a duplicate source of truth;
- whether `owner`, `status`, `domain`, `depends_on`, and `canonical area` are defined.

If the new document contains only details of an existing decision, it must not be created. For example, do not create `Appointment Reschedule Rules.md` if those rules are part of `Ayla MVP Appointment Contract.md`.

Create `Ayla Domain Event Registry.md` when domain events have an independent responsibility and are used by multiple domains.

### Canonical Ownership Rule

Each knowledge subject must have one canonical owner document. Other documents may reference it, use it, or extend its context, but must not redefine the same meaning.

When the question is “create a new document or extend an existing one?”, the decision is made through:

1. analysis of the document's responsibility;
2. review by the relevant area owner;
3. an explicit governance decision.

The decision must not be based only on author convenience.

The ownership model is distributed as follows:

- `Repository Responsibility Matrix` defines ownership;
- `Knowledge Area Taxonomy` defines where knowledge lives;
- canonical documents define the authoritative source of truth.

## 6. Canon Navigation Rules

Every new document must contain:

- purpose;
- owner;
- dependencies;
- status;
- related documents;
- canonical area.

Minimum frontmatter:

```yaml
type: ""
status: draft
owner: ""
domain: ""
depends_on: []
```

The repository metadata registry and `.knowledge/schema.yaml` remain authoritative for machine-validated metadata, controlled vocabularies, lifecycle transitions, and relationship constraints.

## 7. Naming Convention

Names describe the governed artifact and document type. Avoid vague names such as `Notes`, `Plan`, or `Misc`.

Examples:

- Architecture: `Ayla Domain Contract.md`
- Product Operations: `Ayla Capability MVP Contract.md`
- UX: `Ayla Screen Contract.md`
- Engineering: `Ayla System Implementation Guide.md`

Use `Contract` for an agreed behavior, boundary, or interface; `Guide` for implementation or operating instructions; `Registry` for a maintained inventory; and `Decision Log` for recorded decisions.

## 8. Document Lifecycle

| Status | Meaning |
|---|---|
| `Draft` | Work in progress; not authoritative. |
| `Review` | Submitted for review by relevant owners. |
| `Proposed` | Coherent proposal awaiting formal acceptance. |
| `Accepted` | Approved content that may guide implementation or operations. |
| `Canonical` | Authoritative source for its subject and area. |
| `Deprecated` | No longer authoritative; retained for traceability and linked to its replacement. |

Where repository schema values differ in capitalization or vocabulary, the machine-readable schema is authoritative and this lifecycle is the human-readable governance model.

## 9. Current Repository Assessment

Assessment was performed before finalizing this document. No existing content, folder, index, canon document, or contract was modified.

| Document / current structure | Current location | Recommended area | Reason |
|---|---|---|---|
| Ayla Constitution | `00 Foundation/Ayla Constitution.md` | `00 Foundation` | Foundational principles and governance authority. |
| Ayla Repository Responsibility Matrix | `00 Foundation/Ayla Repository Responsibility Matrix.md` | `00 Foundation` | Canonical repository and ownership mapping. |
| Ayla Glossary | `00 Foundation/Ayla Glossary.md` | `00 Foundation` | Shared terminology and definitions. |
| Ayla Domain Capability Registry | `00 Foundation/Ayla Domain Capability Registry.md` | `00 Foundation` | Capability inventory and foundational ownership reference. |
| Ayla Decision Log | `02 Strategy/Ayla Decision Log.md` | `00 Foundation` by responsibility; current location preserved | Cross-cutting governance decisions belong to Foundation, but no migration is authorized by this document. |
| Ayla Knowledge Architecture Specification | `00 Foundation/Ayla Knowledge Architecture Specification.md` | `00 Foundation` | Existing normative knowledge-architecture specification; this taxonomy complements it and does not replace it. |
| Product Vision / Product Principles | `01 Product/` | `01 Product` | Product purpose, principles, and direction. |
| Product Map / Conversation Product Map | `01 Product/` | `01 Product` | Product capabilities and product structure; exact ownership should follow content. |
| User Journeys | `01 Product/User Journeys/` | `01 Product` | Product journeys and discovery context; UX artifacts may link to them. |
| Conversation Design and BOT specifications | `01 Product/` | `01 Product` or `07 UX` by content | Product conversation intent belongs to Product; interaction contracts belong to UX; implementation belongs to Engineering. Existing files remain unchanged. |
| UX MVP documents | `01 Product/UX MVP/` | `07 UX` by responsibility; current location preserved | Screen and interaction contracts are UX knowledge even though the current folder is under Product. |
| Ayla MVP Appointment Contract | `05 Architecture/Ayla MVP Appointment Contract.md` | `05 Architecture` | Domain and system contract for appointment behavior and boundaries. |
| Ayla Domain Event Registry | `05 Architecture/Ayla Domain Event Registry.md` | `05 Architecture` | Shared event ownership and event contract registry. |
| Ayla Salon Operations MVP Contract | `06 Product/Ayla Salon Operations MVP Contract.md` | `06 Product` | Product Operations and operational business behavior contract. |
| `02 Strategy` area | `02 Strategy/` | Strategy responsibility; no automatic merge with `01 Product` | Existing strategy area requires an owner decision before any future consolidation. |
| `03 AI System` area | `03 AI System/` | AI knowledge area by content; open governance question | Existing AI contracts and intent specifications have independent concerns. No migration is proposed. |
| `06 Safety and Governance` area | `06 Safety and Governance/` | Governance / safety responsibility; open governance question | Existing safety and governance documents may require a distinct area decision. No rename or move is proposed. |
| `07 UX`, `08 Engineering`, `09 Operations` | No corresponding top-level folders observed in current assessment | Reserved canonical responsibilities for future documents | Future documents have a defined conceptual home without requiring folders to be created now. |

## 10. Open Questions

| ID | Question | Status |
|---|---|---|
| KAT-001 | What is the final name and scope of `06 Product`? | Owner decision required |
| KAT-002 | Should `02 Strategy` remain a separate physical area, or should Strategy be a responsibility within `01 Product`? | Owner decision required; no migration implied |
| KAT-003 | Is a separate Operations area needed, or is `09 Operations` sufficient as the canonical responsibility? | Owner decision required |
| KAT-004 | Is a separate Governance area needed, or is governance sufficiently covered by `00 Foundation` and `06 Safety and Governance`? | Owner decision required |
| KAT-005 | Is a dedicated AI knowledge area needed, given the existing `03 AI System` area? | Owner decision required |
| KAT-006 | Should UX MVP documents remain physically under `01 Product`, or should a future migration be proposed? | Owner decision required; no migration performed |
| KAT-007 | Which existing document is the canonical owner for cross-cutting decisions currently stored in `02 Strategy/Ayla Decision Log.md`? | Owner decision required |

## 11. Validation Checklist

- [x] Official purpose and scope are defined.
- [x] Current repository structure was inspected before finalizing the document.
- [x] `00 Foundation`, `01 Product`, `05 Architecture`, and `06 Product` were specifically assessed.
- [x] Existing indexes, canon governance files, metadata schema, and relevant contracts were inspected.
- [x] Product Strategy and Architecture are separated.
- [x] UX is not automatically treated as Product merely because of its current folder.
- [x] Implementation knowledge is separated from contracts.
- [x] Product and Product Operations are not merged automatically.
- [x] New-document creation and canonical-ownership rules are defined.
- [x] Future documents have a classification algorithm and canonical area.
- [x] Existing files, folders, indexes, canon documents, and contracts were not modified.
- [x] No migration or folder rename was performed.

