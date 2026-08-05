---
node_id: amd-020-pilot-scope-registry
title: AMD-020 Pilot Scope Registry
type: adr
status: review
version: "0.3"
created: 2026-05-15
updated: 2026-08-06
last_updated: 2026-08-06
owner: Architecture Domain
knowledge_area:
  - architecture
domain:
  - cross-domain
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
export_policy: sanitized
review_cycle: quarterly
reviewers: []
tags: [architecture, pilot, scope, registry, memory-ownership]
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Data Inventory Matrix]]"
adr_id: AMD-020
decision_status: proposed
revision: 3
amendments: []
superseded_by: null
---

# AMD-020 Pilot Scope Registry — Memory Ownership Alignment

## Purpose

This document defines the authoritative scope registry for the Ayla pilot, aligning data ownership boundaries with the [[Data Inventory Matrix]].

**Goal:** Reconcile pilot scope definitions with canonical data ownership without modifying runtime contracts, API shapes, or C5 implementation.

## Non-Goals / Unchanged Constraints

The following are explicitly **out of scope** for this alignment:

- C5 API shapes and endpoint contracts
- Database models and schemas
- Runtime logic in C5 services
- Consent implementation details
- Memory proposal flow mechanics
- Handoff document operational procedures
- ADR-0012 decision status (remains `proposed`)

## Data Class Ownership Mapping

### Account / Profile

| Attribute | Value |
|-----------|-------|
| **Normative Domain Owner** | User Context Domain |
| **Physical Custodian** | W2 Profile Service |
| **Source of Truth** | W2 Profile Service |
| **Write Authority** | W2 Profile Service only (initiators: User, System) |
| **Consumers** | All authenticated services (read-only) |
| **Consent/Purpose** | Account provisioning, service delivery |
| **Retention** | Account lifetime + legal hold |
| **Deletion Orchestrator** | W2 Profile Service on user request or account closure |

### Operational Preferences

| Attribute | Value |
|-----------|-------|
| **Normative Domain Owner** | User Context Domain |
| **Physical Custodian** | W2 Preferences Service |
| **Source of Truth** | W2 Preferences Service |
| **Write Authority** | W2 Preferences Service only (initiators: User, System) |
| **Consumers** | Notification Service, Localization Service, Scheduling Service |
| **Consent/Purpose** | Service personalization, communication delivery |
| **Retention** | Account lifetime |
| **Deletion Orchestrator** | W2 Preferences Service on preference change or account closure |

### Notification Preferences

| Attribute | Value |
|-----------|-------|
| **Normative Domain Owner** | Notification Preferences Domain |
| **Physical Custodian** | Notification Service |
| **Source of Truth** | Notification Service |
| **Write Authority** | Notification Service only (initiators: User, System) |
| **Consumers** | Notification Service, Communication Delivery Service |
| **Consent/Purpose** | Communication delivery, user engagement |
| **Retention** | Account lifetime |
| **Deletion Orchestrator** | Notification Domain on preference change |

**Note:** Language, timezone, locale settings belong to User Context Domain (Operational Preferences). Notification-specific preferences (channels, frequency, quiet hours) belong to Notification Preferences Domain.

### Consent Records

| Attribute | Value |
|-----------|-------|
| **Normative Domain Owner** | Consent Domain |
| **Physical Custodian** | Consent Service |
| **Source of Truth** | Consent Service |
| **Write Authority** | Consent Service only |
| **Initiators** | User grant/revoke requests; System expiry events |
| **Consumers** | All domains requiring consent verification |
| **Consent/Purpose** | N/A — this is the consent record itself |
| **Retention** | Legal requirement period post-revocation |
| **Deletion Orchestrator** | Consent Domain per legal requirements; orchestrates deletion requests |

**Critical Boundary:** All systems must use authoritative consent state either directly from Consent Service or from purpose-bound authoritative cache with established freshness, TTL, and invalidation guarantees. Independent source of truth is prohibited. No component may write consent state bypassing Consent Service; User and System act only as initiators of consent state transitions.

### Raw Wellness History

| Attribute | Value |
|-----------|-------|
| **Normative Domain Owner** | Wellness Domain |
| **Physical Custodian** | Wellness Service |
| **Source of Truth** | Wellness Service |
| **Write Authority** | Wellness Service only (initiators: User devices, System ingestion) |
| **Consumers** | Wellness analytics, Memory proposal gate (input only) |
| **Consent/Purpose** | Wellness tracking, health insights (requires explicit consent) |
| **Retention** | User-defined + legal minimum |
| **Deletion Orchestrator** | Wellness Domain per retention policy |

**Critical Boundary:** Raw wellness records do not constitute memory. They become memory candidates only after passing through the memory proposal and consent gates.

### Wellness-Derived Memory

| Attribute | Value |
|-----------|-------|
| **Normative Domain Owner** | Memory & Identity Domain |
| **Physical Custodian** | W3 Memory Service |
| **Source of Truth** | W3 Memory Service (after memory gate) |
| **Write Authority** | W3 Memory Service only (via memory gate) |
| **Consumers** | Personalization services, Conversation context (purpose-limited) |
| **Consent/Purpose** | Requires explicit memory consent per purpose; derived from wellness data only after consent gate |
| **Retention** | User-controlled, subject to privacy requests |
| **Deletion Orchestrator** | W3 privacy flow on user request |

**Critical Boundary:** Wellness-derived memory is distinct from raw wellness history. Creation requires successful passage through wellness-to-memory proposal and consent gates. W2 has no write authority over this class.

### Semantic Memory

| Attribute | Value |
|-----------|-------|
| **Normative Domain Owner** | Memory & Identity Domain |
| **Physical Custodian** | W3 Memory Service |
| **Source of Truth** | W3 Memory Service (after proposal/consent/purpose gate) |
| **Write Authority** | W3 Memory Service only (via proposal/consent/purpose gate) |
| **Consumers** | Personalization services, Conversation context (purpose-limited) |
| **Consent/Purpose** | Requires explicit memory consent per purpose |
| **Retention** | User-controlled, subject to privacy requests |
| **Deletion Orchestrator** | W3 privacy flow on user request |

**Critical Boundary:** W2 is **not** the owner of semantic memory. W3 serves as technical custodian. Memory entries cannot be created by direct write from other domains.

### Purpose-Limited Projections

| Attribute | Value |
|-----------|-------|
| **Normative Domain Owner** | N/A — inherits normative ownership from source data class |
| **Physical Custodian** | Varies by consumer service |
| **Source of Truth** | Source data class (not the projection) |
| **Write Authority** | Derived automatically from source; no independent writes |
| **Consumers** | Specific purpose-bound consumers only |
| **Consent/Purpose** | Must not exceed source consent scope |
| **Retention** | TTL-bound; invalidated on source change |
| **Deletion Orchestrator** | Automatic on TTL expiry or source deletion |

**Critical Boundary:** Projections are not independent data stores. They inherit all ownership, consent, retention, and policy constraints from their source class. No projection may outlive its source consent or become a parallel source of truth.

## Ownership Summary

| Data Class | Normative Owner | Physical Custodian | Source of Truth | Write Authority |
|------------|-----------------|-------------------|-----------------|-----------------|
| Account/Profile | User Context Domain | W2 Profile Service | W2 Profile Service | W2 Profile Service only |
| Operational Preferences | User Context Domain | W2 Preferences Service | W2 Preferences Service | W2 Preferences Service only |
| Notification Preferences | Notification Preferences Domain | Notification Service | Notification Service | Notification Service only |
| Consent Records | Consent Domain | Consent Service | Consent Service | Consent Service only |
| Raw Wellness History | Wellness Domain | Wellness Service | Wellness Service | Wellness Service only |
| Wellness-Derived Memory | Memory & Identity Domain | W3 Memory Service | W3 Memory Service (after memory gate) | W3 Memory Service only |
| Semantic Memory | Memory & Identity Domain | W3 Memory Service | W3 Memory Service (after proposal/consent/purpose gate) | W3 Memory Service only |
| Purpose-Limited Projections | Inherits from source | Varies | Source data class | N/A (derived) |

## Migration Notes

This alignment does **not** require:

- Database migrations
- API version changes
- Breaking changes to existing consumers
- Immediate refactoring of handoff documents

Future work may address implementation gaps identified during reconciliation, but such changes require separate architectural decisions and migration plans.

## Change Log

### v0.3 (2026-07-24) — Memory Ownership Alignment

- Split composite `UserPersonalContext` into distinct data classes per Data Inventory Matrix
- Removed W2 as blanket owner of all user context; assigned domain-specific ownership
- Designated W3 as technical custodian of Semantic Memory (not owner of profile/consent/wellness)
- Elevated Consent Domain and Wellness Domain as independent sources of truth
- Clarified that projections have no independent ownership; they inherit from source
- Added explicit "Non-Goals" section to protect runtime contracts from unintended changes
- Added dependency on [[Data Inventory Matrix]]

Reconciliation update (2026-08-06), closing review findings on PR #8:

- Aligned Source of Truth, Write Authority, and Deletion Orchestrator wording with the service-level formulations of the [[Data Inventory Matrix]]
- Restricted Consent Records write authority to Consent Service; User and System reclassified as initiators, not direct writers
- Removed the unverifiable `migration_source` provenance claim
- Added the `domain` field required by the knowledge schema conditional rules

### Earlier drafts (provenance not verified)

Versions v0.1 and v0.2 are referenced from legacy pilot materials outside this repository. Their content, dates, and history are not independently verified, and they are **not** canonical revisions of this node. The verifiable history of this document is the git history of this repository.
