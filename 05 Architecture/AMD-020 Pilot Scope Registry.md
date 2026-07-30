---
node_id: amd-020-pilot-scope-registry
title: AMD-020 Pilot Scope Registry
type: adr
status: approved
version: "0.3"
created: 2026-05-15
updated: 2026-07-24
last_updated: 2026-07-24
owner: Architecture Domain
knowledge_area:
  - architecture
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
decision_status: approved
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
| **Physical Custodian** | W2 Profile Implementation |
| **Source of Truth** | User Context Domain |
| **Write Authority** | User (self), System (provisioning) |
| **Consumers** | All authenticated services (read-only) |
| **Consent/Purpose** | Account provisioning, service delivery |
| **Retention** | Account lifetime + legal hold |
| **Deletion Orchestrator** | User Context Domain |

### Operational Preferences

| Attribute | Value |
|-----------|-------|
| **Normative Domain Owner** | User Context Domain / Notification Preferences Domain |
| **Physical Custodian** | W2 Preferences Service |
| **Source of Truth** | Respective Domain (Notification, Locale, Timezone) |
| **Write Authority** | User (self), System (defaults) |
| **Consumers** | Notification Service, Localization Service, Scheduling Service |
| **Consent/Purpose** | Service personalization, communication delivery |
| **Retention** | Account lifetime |
| **Deletion Orchestrator** | User Context Domain |

**Note:** Language, timezone, locale settings belong to User Context Domain. Notification-specific preferences belong to Notification Preferences Domain.

### Consent Records

| Attribute | Value |
|-----------|-------|
| **Normative Domain Owner** | Consent Domain |
| **Physical Custodian** | Consent System Implementation |
| **Source of Truth** | Consent Domain Registry |
| **Write Authority** | User (grant/revoke), System (expiry) |
| **Consumers** | All domains requiring consent verification |
| **Consent/Purpose** | N/A — this is the consent record itself |
| **Retention** | Legal requirement period post-revocation |
| **Deletion Orchestrator** | Consent Domain |

**Critical Boundary:** All systems must use authoritative consent state either directly from Consent Service or from purpose-bound authoritative cache with established freshness, TTL, and invalidation guarantees. Independent source of truth is prohibited.

### Raw Wellness History

| Attribute | Value |
|-----------|-------|
| **Normative Domain Owner** | Wellness Domain |
| **Physical Custodian** | Wellness Data Service |
| **Source of Truth** | Wellness Domain |
| **Write Authority** | Wellness ingestion pipeline, User (correction) |
| **Consumers** | Wellness analytics, Memory proposal gate (input only) |
| **Consent/Purpose** | Wellness tracking, health insights (requires explicit consent) |
| **Retention** | User-defined + legal minimum |
| **Deletion Orchestrator** | Wellness Domain |

**Critical Boundary:** Raw wellness records do not constitute memory. They become memory candidates only after passing through the memory proposal and consent gates.

### Semantic Memory

| Attribute | Value |
|-----------|-------|
| **Normative Domain Owner** | Memory & Identity Domain |
| **Physical Custodian** | W3 Memory Service |
| **Source of Truth** | Memory Domain (post-gate entries only) |
| **Write Authority** | Memory proposal flow (automated), User (correction/deletion) |
| **Consumers** | Personalization services, Conversation context (purpose-limited) |
| **Consent/Purpose** | Requires explicit memory consent per purpose |
| **Retention** | User-controlled, subject to privacy requests |
| **Deletion Orchestrator** | W3 Privacy Flow |

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

| Data Class | Normative Owner | Physical Custodian | Source of Truth |
|------------|-----------------|-------------------|-----------------|
| Account/Profile | User Context Domain | W2 Profile | User Context Domain |
| Operational Preferences | User Context / Notification Domain | W2 Preferences | Respective Domain |
| Consent Records | Consent Domain | Consent System | Consent Domain |
| Raw Wellness History | Wellness Domain | Wellness Service | Wellness Domain |
| Semantic Memory | Memory & Identity Domain | W3 Memory Service | Memory Domain |
| Purpose-Limited Projections | Inherits from source | Varies | Source data class |

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

### v0.2 (2026-06-10) — Pilot Expansion

- Added wellness data classes
- Expanded consent scope definitions

### v0.1 (2026-05-15) — Initial Registry

- Established baseline pilot scope definitions
- Defined initial data class boundaries
