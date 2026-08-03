---
node_id: ayla.strategy.mvp-v03-downstream-migration-plan
title: Ayla MVP v0.3 Downstream Migration Plan
type: specification
status: draft
decision_status: proposed
canonical_status: draft
version: "0.1"
owner: Product Owner
knowledge_area:
  - strategy
system_owner:
  - ayla-knowledge
source_repository: ayla-knowledge
source_kind: product-requirements
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
created: 2026-07-31
updated: 2026-07-31
review_cycle: monthly
depends_on:
  - "[[Ayla MVP Scope and Release Contract]]"
  - "[[Ayla Single-Provider Technical Pilot Execution Scope]]"
  - "[[Ayla Multi-Provider Product Validation Execution Scope]]"
related:
  - "[[Ayla MVP Product Thesis]]"
  - "[[OWNER_DECISION_REGISTER]]"
  - "[[CANON_WORKSTREAM_STATUS]]"
---

# Ayla MVP v0.3 Downstream Migration Plan

## 1. Purpose and Role

This document is the **migration execution plan** for propagating Ayla MVP Scope and Release Contract v0.3, together with the Single-Provider Technical Pilot Execution Scope v0.3 and the Multi-Provider Product Validation Execution Scope v0.2, into all downstream knowledge artifacts.

The plan:

- is **downstream** of MVP Scope v0.3 and both execution scopes — it never overrides them;
- does **not** redefine release scope or product scope;
- does **not** create new owner decisions (AYLA-DEC-0027…0034 remain closed and are not reopened);
- is **not** a roadmap for the whole product — it covers only the artifacts affected by the v0.3 three-channel reconciliation;
- does **not** start the migration automatically — each wave requires its own execution prompt;
- owns the **ordered migration sequence, dependencies, review gates, and completion criteria** for the downstream propagation.

Product Owner Final Review remains **DEFERRED** until the Final Migration Readiness Review returns `MIGRATION_COMPLETE`.

## 2. Migration Preconditions

All preconditions for materializing this plan are met:

| Precondition | State |
|---|---|
| MVP Scope and Release Contract v0.3 | CROSS_DOCUMENT_ALIGNED |
| Single-Provider Technical Pilot Execution Scope v0.3 | CROSS_DOCUMENT_ALIGNED |
| Multi-Provider Product Validation Execution Scope v0.2 | CROSS_DOCUMENT_ALIGNED |
| Ayla MVP Product Thesis | AYLA-DEC-0027_PROPAGATED |
| Planning verdict | READY_TO_MATERIALIZE_DOWNSTREAM_MIGRATION_PLAN |
| Validation baseline | 0 errors / 20 warnings |
| HEAD at materialization | e397274 — canon: normalize two-phase pilot editorial findings |

## 3. Source Documents and Owner Decisions

Authoritative sources (in hierarchy order):

1. `02 Strategy/Ayla MVP Scope and Release Contract.md` — v0.3, release contract.
2. `02 Strategy/Ayla Single-Provider Technical Pilot Execution Scope.md` — v0.3, phase A0/A1/A2 execution.
3. `02 Strategy/Ayla Multi-Provider Product Validation Execution Scope.md` — v0.2, phase B0/B1 execution.
4. `02 Strategy/Ayla MVP Product Thesis.md` — v0.5, AYLA-DEC-0027 propagated.
5. `00 Foundation/Canon Governance/OWNER_DECISION_REGISTER.md` — AYLA-DEC-0027…0034.

Owner decisions consumed by this plan (closed, not reopened):

| Decision | Content consumed downstream |
|---|---|
| AYLA-DEC-0027 | Mobile App — mandatory primary product channel; MAX Mini App and MAX Bot — mandatory companion channels; full feature parity between channels not required |
| AYLA-DEC-0028 | Food Scanner is one of four equal trigger scenarios (FOUR_EQUAL_TRIGGER_MODEL); not a mandatory activation trigger; food-specific metrics are diagnostic, primary metrics are trigger-agnostic |
| AYLA-DEC-0029 | A complete 28-day cycle is required as A2 exit evidence before B0 entry; the exact denominator and sufficient participant share are defined by the Measurement Framework before A2 launch |
| AYLA-DEC-0030 | Provider mix: B0 = «Формула тела» + 1–2 independent providers (solo specialist and/or small salon up to 3 specialists); B1 = 3–5 salons + 5–10 solo masters; large salon deferred to a separate owner decision |
| AYLA-DEC-0031 | Cold acquisition only in B1 after B0 exit; until then — warm users and users of newly onboarded providers; B0 must include at least one cohort that is not «Формула тела» clients |
| AYLA-DEC-0032 | Monetization validation order: (1) solo-master subscription 690 ₽; (2) salon subscription 990 ₽; (3) fee per completed booking 90 ₽; (4) combined model; the Ayla customer does not pay |
| AYLA-DEC-0033 | Hard gates (user data loss = 0; critical safety incidents = 0; economic influence on ranking = 0; consent bypass = 0; attribution chain technically available and auditable) vs working validation thresholds (all percentage targets); final go/no-go is approved before B1 after B0 evidence and the Measurement Framework |
| AYLA-DEC-0034 | No formal RCT in the initial beta; observational cohort comparison required; causal attribution claims prohibited; formal controlled experiment deferred to Product Experiment Design after the initial beta |

## 4. Migration Inventory

Full inventory: 24 items (I-01…I-24). Classes M1–M5 and severities P0–P3 are defined in §8.

| ID | Artifact | Current path | Exists | Current status | Migration class | Severity | Owner role | Required action | Dependencies | Blocks canonization | Blocks A0/A1/A2 | Blocks B0/B1 | Review gate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I-01 | MVP User Journey Specification | `01 Product/User Journeys/Ayla MVP User Journey Specification.md` | yes | v1.0, canonical | M1, M2 | P0 | Product Owner | Apply AYLA-DEC-0027 three-channel framing; replace stale v0.2 section refs (§14 matrix: §3/§4/§11); repeat owner approval for LDT alignment | MVP Scope v0.3 | yes | yes | no | Product/Journey Consistency Review |
| I-02 | Intent Model Specification | `03 AI System/Ayla Intent Model Specification.md` | yes | v1.0, draft | M2 | P1 | AI System Owner | Update v0.2 refs (§3/§4.1/§4.2/§5); close GAP-1: confirm semantic coverage for Goal/LDT/check-in/weekly review/triggers via Goal relationship, Context, Relationships and Orchestration (§ Recommendation Input Boundary) — no new intent types | I-01 | no | yes | no | Product/Journey Consistency Review |
| I-03 | Core Domain Model Specification | `05 Architecture/Ayla Core Domain Model Specification.md` | yes | v1.3, draft | M3, M4 | P2 | Architecture Owner | Update stale refs to v0.2 §4/§5/§11 | MVP Scope v0.3 | no | no | no | Architecture Review |
| I-04 | MVP Recommendation Contract | `05 Architecture/Ayla MVP Recommendation Contract.md` | yes | v0.3, draft | M2 | P1 | Architecture Owner | Remove memory-first framing from rationale; fix wrong pin "Journey v0.3" → "Journey v1.0" (Ayla MVP User Journey Specification v1.0); extend §16 beyond MAX-only | I-01, I-02 | no | yes | no | Architecture Review |
| I-05 | ADR-0013 Recommendation Snapshot | `05 Architecture/ADR-0013 Recommendation Snapshot.md` | yes | draft / proposed | M4 | P2 | Architecture Owner | Update refs to v0.2 §4.1 items 9/11; fix broken path `contracts/draft-mvp-recommendation-contract.md` → `contracts/recommendation-ux-addendum.md` | I-04 | no | no | no | Architecture Review |
| I-06 | UX MVP source index | `01 Product/UX MVP/00-ux-source-index.md` | yes | active working index | M4 | P3 | UX Owner | Replace non-canonical paths `Ayla/ayla-knowledge/`; update v0.2 anchors §3–5/§7/§10 | MVP Scope v0.3 | no | no | no | Mobile Channel Readiness Review |
| I-07 | Draft privacy-consent mapping | `01 Product/UX MVP/contracts/draft-privacy-consent-mapping.md` | yes | draft, Q1–Q10 pending with Privacy Owner since 2026-07-29 | M2 | P1 | Privacy Owner | Obtain Q1–Q10 answers; extend to LDT media/privacy treatment, mobile camera/local storage/upload/deletion mapping, cross-channel consent consistency, original/derived data deletion (MVP Scope refs already point to v0.3 §8/§10) | Privacy Owner answers | no | yes | no | Privacy/Safety Review |
| I-08 | Recommendation UX addendum | `01 Product/UX MVP/contracts/recommendation-ux-addendum.md` | yes | draft | M2, M4 | P2 | UX Owner | Update refs (v0.2 §4.1 items 2/9/11); extend surfaces beyond bot DM/Mini App to Mobile App | I-04 | no | yes | no | Mobile Channel Readiness Review |
| I-09 | SCR-CUST-004 (screen + screen inventory) | Primary: `01 Product/UX MVP/screens/customer/SCR-CUST-004.md`; inventory ref: `01 Product/UX MVP/02-screen-inventory-customer.md` | yes | draft, OQ-REC-2/4/6/7 pending | M2, M4 | P2 | UX Owner | Update old anchor (v0.2 §4.1 item 9) in both files; add Mobile App surface for bot-DM-only entries; resolve OQ-REC-2/4/6/7 | I-08 | no | yes | no | Mobile Channel Readiness Review |
| I-10 | intent-registry.yaml | `03 AI System/Contracts/intent-registry.yaml` | yes | active | M4 | P3 | AI System Owner | Fix comment referencing v0.2 §4 | I-02 | no | no | no | Product/Journey Consistency Review |
| I-11 | Ayla.md MOC | `Ayla.md` | yes | active | M1, M4 | P3 | Canon Architect | Update statuses: MVP Scope 0.2→0.3, Intent Model 0.1→0.9.2, Thesis 0.4→0.5, Vision 1.4→2.0; register execution scopes and this plan | MVP Scope v0.3 | yes | no | no | none (editorial) |
| I-12 | CANON_INDEX | `00 Foundation/Canon Governance/CANON_INDEX.md` | yes | active | M1 | P3 | Canon Architect | Fix line 58 entry MVP Scope v0.2 → v0.3; add execution scopes and this plan | MVP Scope v0.3 | yes | no | no | none (editorial) |
| I-13 | CANON_WORKSTREAM_STATUS | `00 Foundation/Canon Governance/CANON_WORKSTREAM_STATUS.md` | yes | stale | M1 | P3 | Canon Architect | Replace stale "Next action: Initialize MVP Scope Canon Window" with migration-wave state | MVP Scope v0.3 | yes | no | no | none (editorial) |
| I-14 | Mobile navigation specification | `01 Product/UX MVP/Ayla Mobile Navigation Specification.md` (recommended) | no | TO_BE_CREATED | M5 | P1 | UX Owner | Create per contract §6 | AYLA-DEC-0027, I-19 | no | yes | no | Mobile Channel Readiness Review |
| I-15 | Mobile deep-link contract | `01 Product/UX MVP/contracts/mobile-deep-link-contract.md` (recommended) | no | TO_BE_CREATED | M5 | P1 | UX Owner | Create per contract §6 | I-14 | no | yes | no | Mobile Channel Readiness Review |
| I-16 | Mobile auth/account-linking flow | `01 Product/UX MVP/flows/mobile-auth-account-linking.md` (recommended) | no | TO_BE_CREATED | M5 | P1 | UX Owner | Create per contract §6 | I-14, I-07 | no | yes | no | Mobile Channel Readiness Review |
| I-17 | Push notification contract | `01 Product/UX MVP/contracts/push-notification-contract.md` (recommended) | no | TO_BE_CREATED | M5 | P1 | UX Owner | Create per contract §6 | I-14, I-07 | no | yes | no | Mobile Channel Readiness Review |
| I-18 | Mobile privacy/media consent mapping | `01 Product/UX MVP/contracts/mobile-privacy-media-consent-mapping.md` (recommended) | no | TO_BE_CREATED | M5 | P1 | Privacy Owner | Create per contract §6 | I-07, AYLA-DEC-0027 | no | yes | no | Privacy/Safety Review |
| I-19 | Channel capability matrix | `01 Product/UX MVP/Ayla Channel Capability Matrix.md` (recommended) | no | TO_BE_CREATED | M5 | P1 | Product Owner | Create per contract §6 | AYLA-DEC-0027, MVP Scope v0.3 | no | yes | yes | Mobile Channel Readiness Review |
| I-20 | Mobile UX source index | `01 Product/UX MVP/00-ux-source-index-mobile.md` (recommended) | no | TO_BE_CREATED | M5 | P3 | UX Owner | Create per contract §6 | I-14…I-17 | no | no | no | Mobile Channel Readiness Review |
| I-21 | Operations Runbook | `02 Strategy/Ayla Single-Provider Pilot Operations Runbook.md` (recommended) | no | TO_BE_CREATED (GAP-3) | M5 | P1 | Operations Owner | Create per contract §6 | SP Execution Scope v0.3 | no | yes | no | Operations Readiness Review |
| I-22 | Provider Onboarding Runbook | `02 Strategy/Ayla Provider Onboarding Runbook.md` (recommended) | no | TO_BE_CREATED (GAP-4) | M5 | P1 | Operations Owner | Create per contract §6 | MP Execution Scope v0.2 | no | no | yes | Operations Readiness Review |
| I-23 | Measurement Framework | `02 Strategy/Ayla MVP Measurement Framework.md` (recommended) | no | TO_BE_CREATED (GAP-2) | M5 | P1 | Product Owner | Create per contract §6, incl. A2 denominator per AYLA-DEC-0029 | MVP Scope v0.3, both execution scopes | no | yes (A2) | yes (B1) | Analytics/Measurement Review |
| I-24 | Ayla Transaction State Model | `05 Architecture/Ayla Transaction State Model.md` | yes | v0.1, draft / proposed | M4 | P3 | Architecture Owner | Replace broken recommendation-contract path (`contracts/draft-mvp-recommendation-contract.md`) and revalidate User Journey references | I-01, I-04 | no | no | no | Architecture Review |

## 5. Existing Artifact Audit

Exact stale references and required replacements carried over from the planning report.

### I-01 — MVP User Journey Specification (P0-01, canonical conflict)

- **MAX-only channel conflict**: lines ~106–107 and ~926–930 frame the MAX Bot / MAX Mini App as the product channel, contradicting AYLA-DEC-0027 (Mobile App = primary; MAX Mini App / MAX Bot = companions). Deterministic resolution: apply the three-channel model from MVP Scope v0.3; full feature parity is not required.
- **Stale v0.2 section refs**: ~20 references to MVP Scope v0.2 sections → repoint per the MVP Scope v0.3 §14 reference matrix (UJ-facing anchors: §3, §4, §11). The detailed file-level list (§2/§3/§4.1/§4.2/§5/§6/§7/§9) is retained as an extended file-level audit, not a normative mapping.
- **LDT alignment**: changes touch Living Digital Twin alignment (Foundation principle №5) → repeat owner approval required after revision.

### I-02 — Intent Model Specification

- Refs to v0.2 §3/§4.1/§4.2/§5 → v0.3 equivalents.
- **GAP-1 (coverage)**: Goal setting, LDT check-in, weekly review, and trigger-based re-engagement introduced by v0.3 must have confirmed semantic coverage in the Intent Model. Intent Model v1.0 § Recommendation Input Boundary already resolves this via Goal relationship, permitted runtime context, and the orchestration layer — not via new intent types or new Output Contract fields (`goal_id`, `goal_ref`, `goal_relationship`, `transformation_goal_ref` are explicitly out of scope). Remaining migration work for I-02 is to update the stale v0.2 refs and confirm traceability, not to add intent types.

### I-03 — Core Domain Model Specification

- Refs to v0.2 §4/§5/§11 → v0.3 equivalents. No entity-model conflict identified.

### I-04 — MVP Recommendation Contract

- Rationale still cites the pre-v0.3 **memory-first thesis** → align with v0.3 recommendation contract basis.
- Wrong version pin: "Journey v0.3" → **"Journey v1.0"** (Ayla MVP User Journey Specification v1.0).
- §16 surfaces are MAX-only → extend to Mobile App per AYLA-DEC-0027.

### I-05 — ADR-0013 Recommendation Snapshot

- Refs to v0.2 §4.1 items 9/11 → v0.3 equivalents.
- Broken path: `contracts/draft-mvp-recommendation-contract.md` → renamed to `contracts/recommendation-ux-addendum.md`.

### I-06 — UX MVP source index

- Non-canonical source paths under `Ayla/ayla-knowledge/` → canonical `ayla-knowledge-canon-final` paths.
- Anchors to v0.2 §3–5/§7/§10 → v0.3 anchors.

### I-07 — Draft privacy-consent mapping

- Q1–Q10 to Privacy Owner unanswered since 2026-07-29 → answers required before A0.
- MVP Scope references already point to v0.3 §8/§10 — no re-anchoring needed.
- Remaining migration: resolve Q1–Q10; LDT media/privacy treatment; mobile camera/local storage/upload/deletion mapping; cross-channel consent consistency; original/derived data deletion treatment (feeds I-18).

### I-08 — Recommendation UX addendum

- Refs to v0.2 §4.1 items 2/9/11 → v0.3 equivalents.
- Surfaces limited to bot DM / Mini App → add Mobile App surface.

### I-09 — SCR-CUST-004 (screen + screen inventory)

- Primary artifact: `01 Product/UX MVP/screens/customer/SCR-CUST-004.md`; inventory reference: `01 Product/UX MVP/02-screen-inventory-customer.md`.
- Old anchor v0.2 §4.1 item 9 ("Scope Contract §4.1 п. 9") exists in both files (SCR-CUST-004.md line 65; 02-screen-inventory-customer.md line 102) → v0.3 equivalent.
- Surface listed as bot DM only → add Mobile App surface.
- OQ-REC-2/4/6/7 pending → route to owner decisions before A0.

### I-10 — intent-registry.yaml

- Header comment references v0.2 §4 → v0.3 equivalent.

### I-11 / I-12 / I-13 — Registries and MOC

- `Ayla.md`: stale statuses (MVP Scope 0.2, Intent Model 0.1, Thesis 0.4, Vision 1.4) → 0.3 / 0.9.2 / 0.5 / 2.0; add both execution scopes and this plan.
- `CANON_INDEX.md` line 58: MVP Scope listed as v0.2 → v0.3; add execution scopes and this plan.
- `CANON_WORKSTREAM_STATUS.md`: stale "Next action: Initialize MVP Scope Canon Window" → reflect D0–D6 migration state.

### I-24 — Ayla Transaction State Model

- Broken path on line 171: `contracts/draft-mvp-recommendation-contract.md` → renamed to `contracts/recommendation-ux-addendum.md`.
- User Journey references (UJS этапы 10–13, N6/N7 on the same line) → revalidate against the revised UJ Specification v1.0 after D1.

## 6. TO_BE_CREATED Artifact Contracts

Contracts for I-14…I-23. The artifacts themselves are **not** created by this plan.

### I-14 — Mobile Navigation Specification

- **Recommended path**: `01 Product/UX MVP/Ayla Mobile Navigation Specification.md`
- **Title**: Ayla Mobile Navigation Specification
- **Type**: specification · **Status**: draft · **Owner role**: UX Owner
- **depends_on**: `[[Ayla MVP Scope and Release Contract]]`, ``Ayla Channel Capability Matrix` (TO_BE_CREATED)`
- **related**: `[[Ayla MVP User Journey Specification]]`
- **Minimum sections**: purpose; channel model per AYLA-DEC-0027; primary navigation structure; companion-channel entry points; deep-link targets (ref I-15); empty/error states; acceptance criteria.
- **Acceptance criteria**: every Mobile App surface referenced by UJS v1.0 (post-revision) has a navigation entry; no MAX-only framing.
- **Review gate**: Mobile Channel Readiness Review.

### I-15 — Mobile Deep-Link Contract

- **Recommended path**: `01 Product/UX MVP/contracts/mobile-deep-link-contract.md`
- **Title**: Ayla Mobile Deep-Link Contract
- **Type**: preferred semantic type: contract; schema-valid materialization type: `specification` — use `type: specification` until a separate schema amendment adds the semantic type · **Status**: draft · **Owner role**: UX Owner
- **depends_on**: ``Ayla Mobile Navigation Specification` (TO_BE_CREATED)`
- **related**: `[[Ayla MVP Recommendation Contract]]`
- **Minimum sections**: deep-link scheme; target inventory; parameter contract; fallback behavior; companion-channel handoff links.
- **Acceptance criteria**: every push payload (I-17) and every recommendation card CTA resolves to a defined deep link.
- **Review gate**: Mobile Channel Readiness Review.

### I-16 — Mobile Auth / Account-Linking Flow

- **Recommended path**: `01 Product/UX MVP/flows/mobile-auth-account-linking.md`
- **Title**: Ayla Mobile Auth and Account-Linking Flow
- **Type**: specification · **Status**: draft · **Owner role**: UX Owner
- **depends_on**: ``Ayla Mobile Navigation Specification` (TO_BE_CREATED)`, `[[draft-privacy-consent-mapping]]`
- **related**: `[[Ayla MVP User Journey Specification]]`
- **Minimum sections**: identity model; Mobile App auth; MAX account linking; consent checkpoints; failure and recovery paths.
- **Acceptance criteria**: a single user identity is resolvable across all three channels; consent checkpoints match I-07/I-18.
- **Review gate**: Mobile Channel Readiness Review.

### I-17 — Push Notification Contract

- **Recommended path**: `01 Product/UX MVP/contracts/push-notification-contract.md`
- **Title**: Ayla Push Notification Contract
- **Type**: preferred semantic type: contract; schema-valid materialization type: `specification` — use `type: specification` until a separate schema amendment adds the semantic type · **Status**: draft · **Owner role**: UX Owner
- **depends_on**: ``Ayla Mobile Navigation Specification` (TO_BE_CREATED)`, `[[draft-privacy-consent-mapping]]`
- **related**: `[[Ayla Intent Model Specification]]`
- **Minimum sections**: trigger inventory (incl. weekly review, re-engagement); payload contract; deep-link binding (I-15); opt-in/opt-out; rate limits.
- **Acceptance criteria**: every trigger maps to an intent type from the revised Intent Model; opt-out honored per consent mapping.
- **Review gate**: Mobile Channel Readiness Review.

### I-18 — Mobile Privacy / Media Consent Mapping

- **Recommended path**: `01 Product/UX MVP/contracts/mobile-privacy-media-consent-mapping.md`
- **Title**: Ayla Mobile Privacy and Media Consent Mapping
- **Type**: preferred semantic type: contract; schema-valid materialization type: `specification` — use `type: specification` until a separate schema amendment adds the semantic type · **Status**: draft · **Owner role**: Privacy Owner
- **depends_on**: `[[draft-privacy-consent-mapping]]`
- **related**: `[[Consent Scope Registry]]`, `[[Data Inventory Matrix]]`
- **Minimum sections**: mobile permission inventory (camera/media/notifications); LDT data capture consent; per-channel consent scopes; revocation behavior.
- **Acceptance criteria**: covers every mobile permission used by I-14…I-17; consistent with Consent Scope Registry; Q1–Q10 answers incorporated.
- **Review gate**: Privacy/Safety Review.

### I-19 — Channel Capability Matrix

- **Recommended path**: `01 Product/UX MVP/Ayla Channel Capability Matrix.md`
- **Title**: Ayla Channel Capability Matrix
- **Type**: specification · **Status**: draft · **Owner role**: Product Owner
- **depends_on**: `[[Ayla MVP Scope and Release Contract]]`
- **related**: `[[Ayla Single-Provider Technical Pilot Execution Scope]]`, `[[Ayla Multi-Provider Product Validation Execution Scope]]`
- **Minimum sections**: capability list; per-channel support matrix (Mobile App / MAX Mini App / MAX Bot); A0/A1/A2/B0/B1 capability gating; explicit non-parity statement per AYLA-DEC-0027.
- **Acceptance criteria**: every capability in both execution scopes appears exactly once per channel row; no capability contradicts an execution scope.
- **Review gate**: Mobile Channel Readiness Review.

### I-20 — Mobile UX Source Index

- **Recommended path**: `01 Product/UX MVP/00-ux-source-index-mobile.md`
- **Title**: Ayla Mobile UX Source Index
- **Type**: preferred semantic type: index; schema-valid materialization type: `specification` — use `type: specification` until a separate schema amendment adds the semantic type · **Status**: draft · **Owner role**: UX Owner
- **depends_on**: ``Ayla Mobile Navigation Specification` (TO_BE_CREATED)`, ``Ayla Mobile Deep-Link Contract` (TO_BE_CREATED)`, ``Ayla Mobile Auth and Account-Linking Flow` (TO_BE_CREATED)`, ``Ayla Push Notification Contract` (TO_BE_CREATED)`
- **related**: `[[00-ux-source-index]]`
- **Minimum sections**: canonical source list for all mobile artifacts; anchor map; provenance.
- **Acceptance criteria**: every mobile artifact (I-14…I-18) is indexed with canonical paths only.
- **Review gate**: Mobile Channel Readiness Review.

### I-21 — Operations Runbook (GAP-3)

- **Recommended path**: `02 Strategy/Ayla Single-Provider Pilot Operations Runbook.md`
- **Title**: Ayla Single-Provider Pilot Operations Runbook
- **Type**: preferred semantic type: runbook; schema-valid materialization type: `specification` — use `type: specification` until a separate schema amendment adds the semantic type · **Status**: draft · **Owner role**: Operations Owner
- **depends_on**: `[[Ayla Single-Provider Technical Pilot Execution Scope]]`
- **related**: `[[Ayla MVP Scope and Release Contract]]`
- **Minimum sections**: manual operations inventory per SP scope; escalation paths; booking support procedure; incident handling; daily/weekly checklists for A0/A1/A2.
- **Acceptance criteria**: every manual-operations item in the SP execution scope has a runbook entry.
- **Review gate**: Operations Readiness Review.

### I-22 — Provider Onboarding Runbook (GAP-4)

- **Recommended path**: `02 Strategy/Ayla Provider Onboarding Runbook.md`
- **Title**: Ayla Provider Onboarding Runbook
- **Type**: preferred semantic type: runbook; schema-valid materialization type: `specification` — use `type: specification` until a separate schema amendment adds the semantic type · **Status**: draft · **Owner role**: Operations Owner
- **depends_on**: `[[Ayla Multi-Provider Product Validation Execution Scope]]`
- **related**: ``Ayla Single-Provider Pilot Operations Runbook` (TO_BE_CREATED)`
- **Minimum sections**: provider eligibility checklist (B0/B1 provider mix per AYLA-DEC-0030); onboarding steps; provider workspace setup; booking adapter verification; offboarding.
- **Acceptance criteria**: eligibility-before-ranking per the Multi-Provider Execution Scope v0.2 is enforceable from the checklist alone.
- **Review gate**: Operations Readiness Review.

### I-23 — Measurement Framework (GAP-2)

- **Recommended path**: `02 Strategy/Ayla MVP Measurement Framework.md`
- **Title**: Ayla MVP Measurement Framework
- **Type**: specification · **Status**: draft · **Owner role**: Product Owner
- **depends_on**: `[[Ayla MVP Scope and Release Contract]]`, `[[Ayla Single-Provider Technical Pilot Execution Scope]]`, `[[Ayla Multi-Provider Product Validation Execution Scope]]`
- **related**: `[[Ayla Domain Event Registry]]`
- **Minimum sections**: metric inventory for A0/A1/A2/B0/B1; **A2 denominator per AYLA-DEC-0029**; event taxonomy binding; monetization metrics per AYLA-DEC-0032; hard-gate vs working-threshold status per AYLA-DEC-0033.
- **Acceptance criteria**: every gate metric in both execution scopes has a defined denominator, source event, and owner.
- **Review gate**: Analytics/Measurement Review.

## 7. Dependency Graph

```mermaid
graph TD
    subgraph Canonical sources
        MS[Ayla MVP Scope and Release Contract v0.3]
        SP[Single-Provider Execution Scope v0.3]
        MP[Multi-Provider Execution Scope v0.2]
        DEC[AYLA-DEC-0027...0034]
    end

    MS --> UJ[I-01 User Journey Specification]
    UJ --> IM[I-02 Intent Model]
    IM --> RC[I-04 Recommendation Contract]
    RC --> UX[UX / Architecture / Engineering artifacts]
    RC --> ADR[I-05 ADR-0013]
    RC --> TSM[I-24 Transaction State Model]
    UJ --> TSM
    MS --> CDM[I-03 Core Domain Model]

    DEC --> CCM[I-19 Channel Capability Matrix]
    CCM --> NAV[I-14 Mobile Navigation Spec]
    NAV --> DL[I-15 Deep-Link Contract]
    NAV --> AUTH[I-16 Auth / Account Linking]
    NAV --> PUSH[I-17 Push Contract]
    PRIV[I-07 Privacy-Consent Mapping] --> MPRIV[I-18 Mobile Privacy / Media Consent]
    PRIV --> AUTH
    PRIV --> PUSH
    NAV --> MIDX[I-20 Mobile UX Source Index]
    DL --> MIDX
    AUTH --> MIDX
    PUSH --> MIDX

    SP --> OPS[I-21 Operations Runbook]
    OPS --> A[A0 / A1 / A2 execution]
    MP --> POB[I-22 Provider Onboarding Runbook]
    MP --> MEAS[I-23 Measurement Framework]
    SP --> MEAS
    MEAS --> B[B0 / B1 execution]
    POB --> B
```

Text form (required chains):

```text
Canonical sources → MVP Scope → User Journey → Intent Model → Recommendation Contract → UX / Architecture / Engineering
AYLA-DEC-0027 → Channel Capability Matrix → Mobile Navigation / Auth / Deep Link / Push / Privacy → Mobile UX Source Index
I-07 Privacy-Consent Mapping → I-16 Mobile Auth / I-17 Push Contract / I-18 Mobile Privacy Consent
Single-Provider Scope → Operations Runbook → A0/A1/A2
Multi-Provider Scope → Provider Onboarding / Ranking / Attribution / Measurement → B0/B1
```

**No circular dependencies identified.**

## 8. Migration Classes and Severity Model

Migration classes (when the work must land):

| Class | Meaning |
|---|---|
| M1 | Mandatory before MVP Scope canonization |
| M2 | Mandatory before A0/A1/A2 execution |
| M3 | Mandatory before B0/B1 execution |
| M4 | Propagation / editorial alignment |
| M5 | TO_BE_CREATED artifact |

Severity model (how damaging the gap is):

| Severity | Meaning |
|---|---|
| P0 | Canonical conflict — contradicts an owner decision or the release contract |
| P1 | Execution blocker — a phase cannot start or a gate cannot be evaluated without it |
| P2 | Coherence requirement — cross-document consistency is broken without it |
| P3 | Editorial / navigation — stale pointers, statuses, comments |

Rules:

- **Class ≠ severity.** A class says *when*; severity says *how bad*. Example: I-12 CANON_INDEX is M1 (before canonization) but only P3 (editorial).
- One item may carry several migration classes (e.g., I-01 is M1 + M2).
- **Severity ↔ block flags.** If an item blocks A0/A1/A2 or B0/B1, severity is P1. If an item is not a direct execution blocker, its block flag is NO and severity may remain P2/P3 (applied to I-03, I-15, I-17 in the v0.1 repair).
- **P0-01** (I-01 UJ channel conflict) has a deterministic resolution via AYLA-DEC-0027: apply the three-channel model with no parity requirement. No new owner decision is needed for the resolution itself; repeat owner approval is required only because the revision touches LDT alignment.

## 9. Migration Waves

### D0 — Registry and Reference Normalization

- **Goal**: registries, MOC, and workstream status point at v0.3 reality.
- **Artifacts**: I-10, I-11, I-12, I-13.
- **Entry gate**: this plan materialized (v0.1).
- **Exit gate**: Ayla.md, CANON_INDEX, CANON_WORKSTREAM_STATUS, intent-registry comment reflect v0.3 + execution scopes + this plan.
- **Blockers**: none.
- **Owner roles**: Canon Architect.
- **Parallelization**: all four items in parallel.
- **Commit strategy**: one atomic commit for D0.
- **Validation**: `python scripts/validate_knowledge.py` → 0 errors, warnings ≤ 20.
- **Required review**: none (editorial); verified by diff inspection.

### D1 — Product/Journey Alignment

- **Goal**: close P0-01; align journey and intent layer with v0.3.
- **Artifacts**: I-01, I-02.
- **Entry gate**: D0 complete.
- **Exit gate**: Product/Journey Consistency Review = APPROVED; repeat owner approval of UJ revision recorded.
- **Blockers**: repeat owner approval for I-01 (LDT alignment, Foundation principle №5).
- **Owner roles**: Product Owner, AI System Owner.
- **Parallelization**: I-01 and I-02 sequential (Intent Model depends on UJ revision).
- **Commit strategy**: one commit per artifact.
- **Validation**: 0 errors, warnings ≤ 20; grep sweep for stale v0.2 refs.
- **Required review**: Product/Journey Consistency Review.

### D2 — Consent/Privacy/Channel Contracts

- **Goal**: consent layer covers three channels, LDT, and media capture.
- **Artifacts**: I-07, I-18, I-19.
- **Entry gate**: D1 complete; Privacy Owner answers Q1–Q10 received.
- **Exit gate**: Privacy/Safety Review = APPROVED.
- **Blockers**: Privacy Owner Q1–Q10 (open since 2026-07-29).
- **Owner roles**: Privacy Owner, Product Owner.
- **Parallelization**: I-19 parallel to I-07/I-18; I-18 sequential after I-07.
- **Commit strategy**: one commit per artifact.
- **Validation**: 0 errors; Consent Scope Registry cross-check.
- **Required review**: Privacy/Safety Review.

### D3 — Domain/Architecture Contracts

- **Goal**: architecture layer cites v0.3 and three-channel surfaces.
- **Artifacts**: I-03, I-04, I-05, I-24 (plus Domain Event Registry spot-check).
- **Entry gate**: D1 complete.
- **Exit gate**: Architecture Review = APPROVED.
- **Blockers**: none after D1.
- **Owner roles**: Architecture Owner.
- **Parallelization**: I-03/I-04/I-05/I-24 in parallel.
- **Commit strategy**: one commit per artifact.
- **Validation**: 0 errors; broken-path sweep (`draft-mvp-recommendation-contract`).
- **Required review**: Architecture Review.

### D4 — UX/Mobile Artifacts

- **Goal**: mobile channel artifacts exist and UX contracts cover all three channels.
- **Artifacts**: I-14, I-15, I-16, I-17, I-20 (create); I-06, I-08, I-09 (revise).
- **Entry gate**: D2 complete (I-19 needed by I-14); OQ-REC-2/4/6/7 resolved.
- **Exit gate**: Mobile Channel Readiness Review = APPROVED.
- **Blockers**: I-19 (channel capability matrix) from D2; OQ-REC answers.
- **Owner roles**: UX Owner.
- **Parallelization**: I-14 first; I-15/I-16/I-17 in parallel after I-14; I-20 last; I-06/I-08/I-09 in parallel with creation work.
- **Commit strategy**: one commit per artifact.
- **Validation**: 0 errors; index cross-check.
- **Required review**: Mobile Channel Readiness Review.

### D5 — Analytics/Measurement/Operations

- **Goal**: measurement and operations layer ready for gates A2 and B0/B1.
- **Artifacts**: I-23 (Measurement Framework, incl. event taxonomy binding), I-21, I-22.
- **Entry gate**: D3 complete.
- **Exit gate**: Analytics/Measurement Review = APPROVED and Operations Readiness Review = APPROVED.
- **Blockers**: A2 denominator definition in the Measurement Framework (AYLA-DEC-0029) — Product Owner input before A2 launch.
- **Owner roles**: Product Owner, Operations Owner.
- **Parallelization**: I-21/I-22 in parallel; I-23 independent.
- **Commit strategy**: one commit per artifact.
- **Validation**: 0 errors; metric-to-event traceability check.
- **Required review**: Analytics/Measurement Review; Operations Readiness Review.

### D6 — Final Migration Readiness Reviews

- **Goal**: verify the whole migration landed; open the path to canonization.
- **Artifacts**: all migrated artifacts and gate records (Step 17A, read-only review); migration matrix update — this plan, §4 statuses (Step 17B, conditional).
- **Entry gate**: D0–D5 complete, all gates passed.
- **Exit gate**: Final Migration Readiness Review = `MIGRATION_COMPLETE`.
- **Blockers**: any unresolved P0/P1.
- **Owner roles**: Canon Architect, Product Owner.
- **Parallelization**: n/a (single review).
- **Commit strategy**: Step 17A (review) — read-only, no commit; Step 17B — one atomic commit for the matrix update, only if the verdict is `MIGRATION_COMPLETE`.
- **Validation**: 0 errors; worktree clean.
- **Required review**: Final Migration Readiness Review → then Product Owner Final Review opens.

## 10. Ordered Execution Steps

Eighteen steps. Step 1 is completed by the commit that introduces this plan. Each subsequent step runs under its own execution prompt; recommended prompt file names are listed in the table (prompts themselves are not part of this document). Steps 8, 11, 15 and 17A are read-only reviews: Files Changed = NONE, Commit = NONE. Step 17 is split into 17A (read-only Final Migration Readiness Review) and 17B (conditional matrix-update commit).

| Step | Wave | Artifact(s) | Exact action | Prerequisites | Allowed files | Expected commit message | Validation | Required review | Next allowed action |
|---|---|---|---|---|---|---|---|---|---|
| 1 | — | This plan | Materialize Migration Plan v0.1 | Planning verdict READY | `02 Strategy/Ayla MVP v0.3 Downstream Migration Plan.md` | `canon: add MVP v0.3 downstream migration plan` | 0 errors, warnings ≤ 20 | none | Step 2 |
| 2 | — | This plan | Read-only internal consistency review of the plan | Step 1 | none (read-only) | none (review only) | review report | Migration Plan Internal Consistency Review | Step 3 |
| 3 | D0 | I-11 | Update Ayla.md MOC statuses (MVP Scope 0.3, Intent 0.9.2, Thesis 0.5, Vision 2.0); register execution scopes + this plan | Step 2 | `Ayla.md` | `canon: normalize MOC statuses for MVP v0.3` | 0 errors | none (editorial) | Step 4 |
| 4 | D0 | I-12, I-13 | Fix CANON_INDEX line 58 (v0.2→v0.3) + add entries; replace stale next-action in CANON_WORKSTREAM_STATUS | Step 3 | `CANON_INDEX.md`, `CANON_WORKSTREAM_STATUS.md` | `canon: normalize registries for MVP v0.3` | 0 errors | none (editorial) | Step 5 |
| 5 | D0 | I-10 | Fix intent-registry.yaml comment anchor (v0.2 §4 → v0.3) | Step 4 | `03 AI System/Contracts/intent-registry.yaml` | `canon: fix intent registry source anchor` | 0 errors | none (editorial) | Step 6 |
| 6 | D1 | I-01 | Revise UJ Specification: three-channel model per AYLA-DEC-0027; repoint ~20 stale v0.2 refs; obtain repeat owner approval (LDT alignment) | Step 5, owner approval booked | `01 Product/User Journeys/Ayla MVP User Journey Specification.md` | `canon: align MVP user journeys with three-channel model` | 0 errors; stale-ref grep clean | Product Owner approval | Step 7 |
| 7 | D1 | I-02 | Revise Intent Model: update v0.2 refs; confirm semantic coverage for Goal/LDT/check-in/weekly-review/trigger scenarios via Goal relationship, Context and Orchestration (GAP-1) — no new intent types | Step 6 | `03 AI System/Ayla Intent Model Specification.md` | `canon: extend intent model for MVP v0.3 journeys` | 0 errors | none | Step 8 |
| 8 | D1 | I-01, I-02 | Product/Journey Consistency Review (read-only; Files Changed = NONE; Commit = NONE) | Step 7 | none (read-only) | NONE — read-only review, no commit | review report | Product/Journey Consistency Review | Step 9 |
| 9 | D2 | I-07 | Obtain Privacy Owner answers Q1–Q10; update draft privacy-consent mapping (LDT media/privacy treatment; mobile camera/local storage/upload/deletion mapping; cross-channel consent consistency; original/derived data deletion) | Step 8, Privacy Owner answers | `01 Product/UX MVP/contracts/draft-privacy-consent-mapping.md` | `canon: resolve privacy-consent mapping for MVP v0.3` | 0 errors | none | Step 10 |
| 10 | D2 | I-18, I-19 | Create Channel Capability Matrix; create mobile privacy/media consent mapping | Step 9 | I-18, I-19 recommended paths | `canon: add channel capability matrix and mobile consent mapping` | 0 errors | Privacy/Safety Review (Step 11) | Step 11 |
| 11 | D2 | I-07, I-18, I-19 | Privacy/Safety Review (read-only; Files Changed = NONE; Commit = NONE) | Step 10 | none (read-only) | NONE — read-only review, no commit | review report | Privacy/Safety Review | Step 12 |
| 12 | D3 | I-03, I-04, I-05, I-24 | Update CDM refs; fix Recommendation Contract (memory-first framing, Journey pin v1.0, §16 channels); fix ADR-0013 refs + broken path; fix Transaction State Model broken recommendation-contract path and revalidate UJ refs; Architecture Review | Step 8 (D1 gate) | `05 Architecture/Ayla Core Domain Model Specification.md`, `05 Architecture/Ayla MVP Recommendation Contract.md`, `05 Architecture/ADR-0013 Recommendation Snapshot.md`, `05 Architecture/Ayla Transaction State Model.md` | `canon: align architecture contracts with MVP v0.3` | 0 errors; broken-path sweep clean | Architecture Review | Step 13 |
| 13 | D4 | I-14, I-15, I-16, I-17 | Create mobile navigation spec, deep-link contract, auth/account-linking flow, push contract (I-14 first, then parallel) | Step 11 (I-19), Step 9 (consent) | four recommended paths | `canon: add mobile channel contracts for MVP v0.3` | 0 errors | none | Step 14 |
| 14 | D4 | I-06, I-08, I-09, I-20 | Update UX source index (canonical paths, v0.3 anchors); extend recommendation UX addendum + SCR-CUST-004 (screen file + screen inventory) to Mobile App; create mobile UX source index | Step 13, OQ-REC-2/4/6/7 resolved | `01 Product/UX MVP/00-ux-source-index.md`, `01 Product/UX MVP/contracts/recommendation-ux-addendum.md`, `01 Product/UX MVP/screens/customer/SCR-CUST-004.md`, `01 Product/UX MVP/02-screen-inventory-customer.md`, `01 Product/UX MVP/00-ux-source-index-mobile.md` | `canon: align UX surfaces with three-channel model` | 0 errors | Mobile Channel Readiness Review (Step 15) | Step 15 |
| 15 | D4 | all D4 artifacts | Mobile Channel Readiness Review (read-only; Files Changed = NONE; Commit = NONE) | Step 14 | none (read-only) | NONE — read-only review, no commit | review report | Mobile Channel Readiness Review | Step 16 |
| 16 | D5 | I-21, I-22, I-23 | Create Operations Runbook, Provider Onboarding Runbook, Measurement Framework (A2 denominator per AYLA-DEC-0029; event taxonomy binding) | Step 12 (D3 gate), PO input on A2 denominator | three recommended paths | `canon: add measurement framework and pilot runbooks` | 0 errors; metric-to-event traceability | Analytics/Measurement Review; Operations Readiness Review | Step 17A |
| 17A | D6 | all migrated artifacts + gate records | Final Migration Readiness Review (read-only; Files Changed = NONE; Commit = NONE); verdict target `MIGRATION_COMPLETE` | Steps 1–16, all gates passed | none (read-only) | NONE — read-only review, no commit | review report; 0 errors; worktree clean | Final Migration Readiness Review | Step 17B |
| 17B | D6 | migration matrix (this plan, §4) | If verdict = `MIGRATION_COMPLETE`: update matrix statuses in a separate atomic commit | Step 17A verdict `MIGRATION_COMPLETE` | this plan (matrix only) | `canon: record MVP v0.3 migration completion` | 0 errors; worktree clean | none (uses 17A review record) | Step 18 |
| 18 | D6 | — | Open Product Owner Final Review (canonization path) | Step 17B complete (verdict `MIGRATION_COMPLETE`) | per PO review prompt | per PO review prompt | per PO review prompt | Product Owner Final Review | window closure decision |

Recommended execution prompt names (to be authored separately, in `D:\Проекты\Ayla` per window convention):

```text
MVP_V03_MIGRATION_PLAN_V0_1_INTERNAL_CONSISTENCY_REVIEW_PROMPT.md
MVP_V03_MIGRATION_D0_REGISTRY_NORMALIZATION_PROMPT.md
MVP_V03_MIGRATION_D1_USER_JOURNEY_REVISION_PROMPT.md
MVP_V03_MIGRATION_D1_INTENT_MODEL_REVISION_PROMPT.md
MVP_V03_MIGRATION_D1_PRODUCT_JOURNEY_REVIEW_PROMPT.md
MVP_V03_MIGRATION_D2_PRIVACY_CONSENT_PROMPT.md
MVP_V03_MIGRATION_D2_CHANNEL_MATRIX_AND_MOBILE_CONSENT_PROMPT.md
MVP_V03_MIGRATION_D2_PRIVACY_SAFETY_REVIEW_PROMPT.md
MVP_V03_MIGRATION_D3_ARCHITECTURE_ALIGNMENT_PROMPT.md
MVP_V03_MIGRATION_D4_MOBILE_CONTRACTS_PROMPT.md
MVP_V03_MIGRATION_D4_UX_SURFACE_ALIGNMENT_PROMPT.md
MVP_V03_MIGRATION_D4_MOBILE_READINESS_REVIEW_PROMPT.md
MVP_V03_MIGRATION_D5_MEASUREMENT_AND_RUNBOOKS_PROMPT.md
MVP_V03_MIGRATION_D6_FINAL_READINESS_REVIEW_PROMPT.md
```

## 11. Parallelization Rules

- Waves are strictly sequential: D0 → D1 → D2 → D3 → D4 → D5 → D6. A wave starts only when the previous wave's exit gate is met.
- D3 may start after D1 (it does not depend on D2), but its review evidence joins the D6 record; the default order remains sequential unless the window owner explicitly parallelizes.
- Within D0: all items parallel. Within D1: I-01 before I-02. Within D2: I-19 parallel with I-07 → I-18. Within D4: I-14 first, I-15/I-16/I-17 parallel, I-20 last; revisions I-06/I-08/I-09 parallel with creations. Within D5: I-21/I-22/I-23 parallel.
- One atomic commit per artifact (D0 may use one commit for all four registry items); never mix waves in one commit.
- No parallel edits to the same file; no subagents (window constraint).

## 12. Owner Decisions and Governance Checkpoints

Classification carried over from the planning report without extension. AYLA-DEC-0027…0034 are **not** reopened.

- **Owner Decisions Required Now**: none.
- **Owner Decisions Before A0**: Privacy Owner answers Q1–Q10 (I-07); resolution of OQ-REC-2/4/6/7 (I-09); repeat owner approval of the revised UJ Specification (I-01, LDT alignment).
- **Owner Decisions Before A2**: Product Owner confirms the Measurement Framework including the A2 denominator (AYLA-DEC-0029).
- **Owner Decisions Before B0**: none.
- **Owner Decisions Before B1**: final B1 go/no-go approval after B0 evidence and the Measurement Framework, with hard gates vs working thresholds per AYLA-DEC-0033. Monetization validation order is fixed by AYLA-DEC-0032 (no new decision). Cold acquisition is permitted only in B1 after B0 exit (AYLA-DEC-0031); exact channel selection is an implementation/Growth decision unless explicit Product Owner approval is required elsewhere. AYLA-DEC-0034 covers experiment design only (observational cohort comparison; no formal RCT) and requires no additional approval.

## 13. Review Gates

Seven gates. Product Owner Final Review opens only after `MIGRATION_COMPLETE`.

| Gate | Inputs | Criteria | Blocking findings | Allowed verdicts | Downstream route |
|---|---|---|---|---|---|
| Product/Journey Consistency Review | I-01, I-02 post-revision | P0-01 closed per AYLA-DEC-0027; no stale v0.2 refs; GAP-1 semantic coverage (Goal/Context/Orchestration — no new intent types required); UJ↔Intent traceability | any remaining MAX-only framing; missing LDT/check-in semantic coverage in Recommendation Input Boundary / orchestration layer | APPROVED / NEEDS_WORK | D2, D3 |
| Privacy/Safety Review | I-07, I-18, I-19 | Q1–Q10 answered; three-channel consent coverage; Consent Scope Registry consistency | unanswered consent question; media/LDT gap | APPROVED / NEEDS_WORK | D4 |
| Architecture Review | I-03, I-04, I-05, I-24 | v0.3 refs only; Journey pin v1.0; memory-first framing removed; no broken paths (incl. Transaction State Model) | canonical contradiction; broken reference | APPROVED / NEEDS_WORK | D5 |
| Mobile Channel Readiness Review | I-06, I-08, I-09, I-14…I-17, I-20 | all three channels covered; deep-link/push/auth contracts complete; capability matrix honored | missing Mobile App surface; contract gap | APPROVED / NEEDS_WORK | D6 input |
| Analytics/Measurement Review | I-23 | every gate metric has denominator, source event, owner; A2 denominator per AYLA-DEC-0029 | undefined gate metric | APPROVED / NEEDS_WORK | D6 input |
| Operations Readiness Review | I-21, I-22 | every manual-ops and onboarding item actionable; eligibility-before-ranking (MP Execution Scope) enforceable from checklist | missing runbook entry | APPROVED / NEEDS_WORK | D6 input |
| Final Migration Readiness Review | full migration matrix + all gate records | §16 completion criteria 1–7 met | any open P0/P1; any failed gate | MIGRATION_COMPLETE / MIGRATION_INCOMPLETE | Product Owner Final Review |

## 14. Stop Conditions

Stop the migration and escalate to the window owner if any of the following occurs:

1. An unresolved P0 finding survives its target wave.
2. An authoritative source document is missing or renamed.
3. Two owner decisions contradict each other.
4. A circular dependency appears in the graph (§7).
5. The source-of-truth for an artifact becomes unknown or disputed.
6. A consent question has no identifiable owner.
7. Channel ownership (Mobile App vs MAX Mini App vs MAX Bot) is unclear for a capability.
8. A recommended path collides with an existing file of different content.

**As of v0.1 (2026-07-31): no stop condition is active.**

## 15. Validation and Evidence

After every migration commit:

```text
python scripts/validate_knowledge.py   # expected: 0 errors, warnings ≤ 20 (baseline)
git diff --check
git status --short                     # only wave-allowed files changed
```

Additional evidence per wave: stale-reference grep sweeps (D1, D3), Consent Scope Registry cross-check (D2), index cross-check (D4), metric-to-event traceability check (D5), and the review records for all seven gates (D6). Push is not performed at any step.

## 16. Completion Criteria

This migration plan is considered executed when:

1. all M1 items are closed;
2. all P0 and P1 findings are closed;
3. D1–D5 reviews are passed (APPROVED);
4. D6 verdict = `MIGRATION_COMPLETE`;
5. validation = 0 errors;
6. worktree clean;
7. migration matrix (§4) updated with final statuses;
8. Product Owner Final Review is opened as the next step.

## 17. Window and Lifecycle

- **Window**: Two-Phase Pilot Scope Reconciliation Window — remains open after this step.
- **Reason**: the materialized plan requires a read-only internal consistency review next (Step 2).
- **Next window**: none.
- **Document lifecycle**: v0.1 draft/proposed; the document becomes the migration matrix of record — §4 statuses are updated in place as waves complete (D6), without changing owner decisions or source documents.
- **Versioning rule**: progress/status matrix updates within v0.1 do not require a version bump when strategy, inventory identity, wave order and completion criteria do not change. Material strategy changes require v0.2.

## 18. Change Log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-07-31 | Initial materialization from the mandatory downstream migration planning report: 23 inventory items (I-01…I-23); waves D0–D6; 18 ordered execution steps; 7 review gates; no owner decisions required now; no migration executed in this commit. |
| 0.1 | 2026-07-31 | Targeted material repair after Internal Consistency Review: corrected AYLA-DEC-0028…0034 decision mapping (§3, §6 I-23, §9 D5, §12, gates); added schema fallbacks (preferred semantic type contract/index/runbook → schema-valid materialization type `specification`) for I-15/I-17/I-18/I-20/I-21/I-22; I-09 covers both SCR-CUST-004.md and 02-screen-inventory-customer.md (Step 14 allowed files exact); corrected I-07 claim (MVP Scope refs already point to v0.3 §8/§10; remaining migration = Q1–Q10, LDT media/privacy, mobile camera/local storage/upload/deletion, cross-channel consent, original/derived deletion); added I-24 Ayla Transaction State Model (inventory 23 → 24; D3, Architecture Review, Step 12); corrected artifact statuses (Intent Model approved; Core Domain Model draft; ADR-0013 draft/proposed); exact literal "Journey v0.3" → "Journey v1.0"; UJ audit tied to MVP Scope §14 matrix (§3/§4/§11) with extended file-level audit marked non-normative; graph edges I-07→I-16 and I-07→I-17 (+ I-24 node); severity/block alignment (I-03 block flag NO; I-15/I-17 severity P1); review steps 8/11/15/17A read-only with no commit; Step 17 split into 17A (review) and 17B (conditional matrix commit); versioning rule added (§17). No migration executed; no owner decisions created; no version bump; no wave-strategy change. |
| 0.1 | 2026-08-03 | Governance and machine-readable synchronization pass: corrected I-02 (§4 inventory row, §5 audit, §10 Step 7, §13 gate criteria) — Intent Model status updated from stale "v0.9.2, approved" to actual "v1.0, draft"; GAP-1 requirement changed from "add intent types for Goal/LDT/check-in/weekly review/triggers" to "confirm semantic coverage via Goal relationship, Context and Orchestration — no new intent types," reflecting that Intent Model v1.0 § Recommendation Input Boundary already resolves this coverage without new intent types or Output Contract fields. No new intent types introduced anywhere; no wave order, inventory identity, or completion-criteria change; no version bump. |
