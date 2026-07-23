---
node_id: ayla.architecture.amd020-c5-implementation-amendment
title: AMD-020 C5 Implementation Amendment
aliases:
  - AMD-020 Implementation Amendment
  - C5 Pilot Implementation Amendment
type: specification
status: draft
decision_status: proposed
version: "0.6"
canonical_status: draft
owner: Chief Product Architect
priority: P0
knowledge_area:
  - architecture
domain:
  - user-context
  - identity
  - consent
concerns:
  - privacy
  - security
  - audit
  - compliance
system_owner:
  - ayla-user-context
  - ayla-knowledge
source_repository: ayla-knowledge
created: 2026-07-23
updated: 2026-07-23
source_kind: canonical
source_kind_note: "source_kind=canonical identifies the document as originating in the ayla-knowledge canonical repository; maturity/approval is expressed by status, decision_status, and canonical_status."
classification: internal
data_sensitivity: high
data_categories:
  - pii
security_sensitivity: high
ai_indexing: metadata-only
export_policy: sanitized
tags:
  - ayla
  - ayla/architecture
  - amd020
  - implementation
  - c5
  - privacy
  - 152-fz
depends_on:
  - "[[AMD-020 C5 Pilot Personal Context Export-Forget Contract]]"
related:
  - "[[Ayla Knowledge Architecture Specification]]"
review_cycle: event-driven
---

# AMD-020 C5 Implementation Amendment

## Document State

| Field | Value |
|---|---|
| Document status | Draft |
| Decision status | Proposed |
| Version | 0.6 (2026-07-23) |
| Canonical status | draft |
| Review status | pending_owner_approval |

Этот документ — извлечённый перечень code deltas для W2/W3, необходимых для
реализации AMD-020 v0.6. Он не включает Verification Evidence (создаётся W6
после реализации) и не меняет код самостоятельно.

---

## 1. Code Deltas

### 1.1 Delete barrier and state machine

| Attribute | Value |
|---|---|
| `norm_id` | AMD020-DEL-001 |
| Source section | AMD-020 §3.1, §3.2, §3.3 |
| Current implemented fact | No barrier exists. `delete_personal_data` in `apps/identity/services/privacy.py:186-248` runs steps sequentially without blocking new writes or inference. |
| Required delta | Introduce operation lifecycle: `accepted` is an internal pre-commit state, and the first externally observable state is `blocked`. Operation record, scope lock, and barrier activation must be created in a single database transaction. Track per-class states separately. Block new MemoryEntry writes, inferred writes, and derived-representation creation while a delete operation is active. |
| Repository/module | W3: `apps/identity/services/privacy.py`, `apps/identity/services/memory_writer.py`, `apps/identity/services/memory_inferred.py`, `apps/orchestrator/memory/personal_context.py`, new `apps/identity/services/privacy_operations.py` |
| W2/W3 window | W3 |
| Dependency | operation_id / state store (AMD020-DEL-003) |
| Migration/backfill | New operation-state store; no data backfill. |
| Observability | metric `privacy.delete_barrier_active`; audit event `privacy.delete_barrier_set` |
| Rollback consideration | Revert barrier release on failure; idempotent retry must re-check barrier. |
| SP estimate | 5–8 |
| W6 evidence | Scenarios 1, 9, 10, 11, 12, 29a, 29b, 30 |

### 1.2 Hard-delete purge job and lifecycle

| Attribute | Value |
|---|---|
| `norm_id` | AMD020-DEL-002 |
| Source section | AMD-020 §3.4 |
| Current implemented fact | `MemoryEntry` soft-deleted via `soft_delete_green_entries` (`memory_deleter.py:33-73`). Physical purge after tombstone retention is implied but not implemented. |
| Required delta | Add Celery cron purge-job with per-class states `hard_delete_pending` → `primary_purged` → `backup_expiry_pending` → `backup_expired`; physical `DELETE` of `MemoryEntry` rows after `soft_delete_retention`; backup expiry tracking. |
| Repository/module | W3: new `apps/identity/tasks/purge_deleted_memory.py`; `apps/identity/models.py` (confirm indexes); backup monitoring integration |
| W2/W3 window | W3 |
| Dependency | Retention decision (Legal), backup SLA (SRE) |
| Migration/backfill | None for pilot; future backfill of legacy soft-deleted rows if retention changed. |
| Observability | metric `memory.purged_rows`; audit `memory.purge_run` |
| Rollback consideration | Purge is destructive; implement dry-run mode and soft-launch with limited user cohort. |
| SP estimate | 5–8 |
| W6 evidence | Scenarios 13, 28 |

### 1.3 operation_id, scope_hash, idempotency, correlation

| Attribute | Value |
|---|---|
| `norm_id` | AMD020-DEL-003 |
| Source section | AMD-020 §4 |
| Current implemented fact | No operation-scoped identifiers. W3 view uses `bot_user.id` and internal HTTP client. |
| Required delta | Generate `operation_id` at request acceptance; compute `scope_hash`; accept `Idempotency-Key` header; store operation state; distinguish `request_attempt` vs `execution_attempt`; propagate `correlation_id` to W2 and audit. |
| Repository/module | W3: `apps/miniapp_api/views.py` (export/delete views), `apps/identity/services/privacy.py`, new `apps/identity/services/privacy_operations.py` |
| W2/W3 window | W3 |
| Dependency | None |
| Migration/backfill | New table/column for idempotency records. |
| Observability | metric `privacy.operation_created`; log correlation_id |
| Rollback consideration | Keep idempotency records for retry window; deletion must be safe. |
| SP estimate | 8–13 |
| W6 evidence | Scenarios 1, 2, 31, 32 |

### 1.4 Closed response schemas and error taxonomy

| Attribute | Value |
|---|---|
| `norm_id` | AMD020-DEL-004 |
| Source section | AMD-020 §5 |
| Current implemented fact | W3 returns raw dict from `privacy.py`; W2 returns `success_response({"user_id", "deleted"})` or 404. No machine error codes. |
| Required delta | Implement JSON Schema 2020-12 for success/partial/failure/export using shared `$defs` (`subject`, `perStepResults`, `retainedItem`, `error`); mark `personal_context` and `MemoryEntry.content` as `opaque_payload`; add export failure schema; synchronize failure `enum` with full error taxonomy (`upstream_timeout`, `upstream_unavailable`, `upstream_error`, `upstream_malformed`, `init_data_expired`, etc.); `format_version` on all responses; `per_step_results`; remove `consents` from `deleted[]`; map each error class to HTTP + machine code; external 500 for internal credential failures with internal security-incident classification. |
| Repository/module | W2: `users/personal_data_api.py`; W3: `apps/miniapp_api/views.py`, `apps/identity/services/privacy.py` |
| W2/W3 window | W2 + W3 |
| Dependency | operation_id (AMD020-DEL-003) |
| Migration/backfill | None |
| Observability | structured log with `error_code`; metric `privacy.error.<code>`; security alert for `internal_credential_failure` |
| Rollback consideration | Contract change; keep v0.1 fallback until W6 validates. |
| SP estimate | 8–13 |
| W6 evidence | Scenarios 3, 4, 5, 6, 22, 33, 35, 36 |

### 1.5 subject_gone

| Attribute | Value |
|---|---|
| `norm_id` | AMD020-DEL-005 |
| Source section | AMD-020 §6 |
| Current implemented fact | W2 returns 404 with generic `NOT_FOUND` body (`users/personal_data_api.py:53-58`). W3 interprets `PersonalContextNotFoundError` as `already_deleted`. |
| Required delta | W2 returns JSON body `{"code":"subject_gone","subject":{"ayla_user_id":"..."}}` for missing/soft-deleted users. W3 validates code before treating as gone. |
| Repository/module | W2: `users/personal_data_api.py`; W3: `apps/integrations/ayla/personal_context_client.py`, `apps/identity/services/privacy.py` |
| W2/W3 window | W2 + W3 |
| Dependency | Closed response schemas (AMD020-DEL-004) |
| Migration/backfill | None |
| Observability | log `privacy.subject_gone` |
| Rollback consideration | During rolling deploy an old W2 may still return a generic 404. W3 must treat that as `upstream_error` / `contract_violation`, not as semantic success. Backward compatibility does not weaken delete semantics. |
| SP estimate | 2–3 |
| W6 evidence | Scenario 26 |

### 1.6 Retention manifest in delete response

| Attribute | Value |
|---|---|
| `norm_id` | AMD020-DEL-006 |
| Source section | AMD-020 §7 |
| Current implemented fact | Delete response returns `{"user_id", "deleted"}` only. |
| Required delta | Compute `retained[]` list at delete completion; include audit, tombstones, consent records, backups with categories/reasons/decision_status/owners; use `null` retention_until for owner_decision_required items. |
| Repository/module | W3: `apps/identity/services/privacy.py`, new `apps/identity/services/privacy_retention.py` |
| W2/W3 window | W3 |
| Dependency | Legal retention decisions |
| Migration/backfill | None |
| Observability | log retained categories count |
| Rollback consideration | Manifest is additive; safe to return. |
| SP estimate | 3–5 |
| W6 evidence | Scenario 18 |

### 1.7 Auth, replay protection, step-up controls and safe logging

| Attribute | Value |
|---|---|
| `norm_id` | AMD020-DEL-007 |
| Source section | AMD-020 §8 |
| Current implemented fact | Customer endpoints use `MaxInitData` only. No step-up, nonce, or replay protection beyond Django session. |
| Required delta | Add destructive-operation confirmation challenge (nonce, TTL), rate limits, session/device binding, relink checks, safe-logging rule (no plaintext user IDs); keep `Idempotency-Key` and `correlation_id` separate. Implement fail-closed behavior: if step-up is disabled, unavailable or misconfigured, the destructive endpoint returns `internal_error`; no fallback to MaxInitData-only authentication is permitted. |
| Repository/module | W3: `apps/miniapp_api/views.py`, `apps/miniapp_api/auth.py`, new `apps/identity/services/privacy_security.py`; W4: miniapp UX |
| W2/W3 window | W3 + W4 |
| Dependency | operation_id (AMD020-DEL-003) |
| Migration/backfill | New nonce/challenge store. |
| Observability | metrics `privacy.challenge_issued`, `privacy.challenge_expired`, `privacy.rate_limited`; security alert for credential failures |
| Rollback consideration | A feature flag may disable the entire destructive endpoint, but it cannot weaken the endpoint's required authentication. If step-up cannot be enforced, the endpoint must be unavailable rather than fall back to MaxInitData-only auth. |
| SP estimate | 13–21 |
| W6 evidence | Scenarios 20, 21, 23, 24, 37 |

### 1.8 UserPersonalContext delete semantics

| Attribute | Value |
|---|---|
| `norm_id` | AMD020-DEL-008 |
| Source section | AMD-020 §1.1, §3.2, §3.4 |
| Current implemented fact | W2 endpoint calls `UserPersonalContext.objects.filter(user=user).delete()` — physical DELETE (`users/personal_data_api.py:152`). |
| Required delta | Confirm physical wipe as canonical semantics for W2 UPC (owner/Legal decision); add per-step result; track `deleted` → `backup_expired` states; ensure no residual derived data. |
| Repository/module | W2: `users/personal_data_api.py`; W3: aggregation layer |
| W2/W3 window | W2 |
| Dependency | Backup SLA |
| Migration/backfill | None if physical wipe confirmed. |
| Observability | audit `privacy.ayla_upc_deleted` |
| Rollback consideration | Physical delete is irreversible; require Legal confirmation. |
| SP estimate | 2–4 |
| W6 evidence | Scenarios 9, 14 |

### 1.9 Internal W3→W2 URL PII

| Attribute | Value |
|---|---|
| `norm_id` | AMD020-DEL-009 |
| Source section | AMD-020 §8.3 |
| Current implemented fact | Internal endpoint path contains `{ayla_user_id}` (`/api/v1/internal/users/{ayla_user_id}/personal-data/`). |
| Required delta | Either replace `{ayla_user_id}` with an opaque request-scoped token, or implement strict access-log/trace sanitization and internal-network-only access. If the URL change is deferred, the fallback sanitization must be in place before activation: plaintext `ayla_user_id` must not appear in internal access logs, traces, or metrics. |
| Repository/module | W2: `users/urls.py`, `users/personal_data_api.py`; W3: `apps/integrations/ayla/personal_context_client.py` |
| W2/W3 window | W2 + W3 |
| Dependency | URL contract decision |
| Migration/backfill | URL change requires coordinated deploy. |
| Observability | security alert on internal endpoint access from unexpected source |
| Rollback consideration | Maintain backward-compatible path during transition. |
| SP estimate | 3–8 (if URL change) or 1–2 (if sanitization only) |
| W6 evidence | Scenario 34 |

### 1.10 Consent history schema expansion

| Attribute | Value |
|---|---|
| `norm_id` | AMD020-EXP-001 |
| Source section | AMD-020 §10.2 |
| Current implemented fact | `ConsentRecord` stores `consent_type`, `granted`, `document_version`, `source`, `captured_at`, `withdrawn_at`. |
| Required delta | Add fields: `purpose`, `data_categories`, `operator`, `recipients`, `term`, `lawful_basis`, `identification_method`. Backfill every existing record before activation; if source data is unavailable, populate the sentinel values defined in AMD-020 §10.2. Store an optional `legacy_record` boolean. |
| Repository/module | W3: `apps/consent/models.py`, migrations, `apps/identity/services/privacy.py` export serializer |
| W2/W3 window | W3 |
| Dependency | Legal consent-text approval |
| Migration/backfill | Migration adding non-nullable columns with default sentinel values; verification query must return zero rows with missing expanded fields before activation. |
| Observability | log backfill count |
| Rollback consideration | Keep legacy fields; additive change. |
| SP estimate | 5–8 |
| W6 evidence | Scenario 39 (export contains expanded consent fields) |

### 1.11 Export orchestration and authorization

| Attribute | Value |
|---|---|
| `norm_id` | AMD020-EXP-002 |
| Source section | AMD-020 §1.1, §4, §8 |
| Current implemented fact | Export endpoint exists (`apps/miniapp_api/views.py:1618-1640`) and returns `JsonResponse` on demand. No separate authorization gate beyond `MaxInitData`; no `operation_id` or `scope_hash` for export; no step-up challenge for export. |
| Required delta | Create export operation with `operation_id`, `scope_hash`, `Idempotency-Key` handling, and same subject/tenant binding as delete. Enforce authorization: requester must be allowed to export the subject’s personal context. Return export success/failure schemas. |
| Repository/module | W3: `apps/miniapp_api/views.py`, `apps/identity/services/privacy.py`, new `apps/identity/services/export_operations.py` |
| W2/W3 window | W3 |
| Dependency | AMD020-DEL-003 (operation_id/scope_hash/idempotency), AMD020-DEL-007 (auth/replay/step-up) |
| Migration/backfill | New operation-state records for export; no data backfill. |
| Observability | metric `privacy.export.created`; audit `privacy.personal_data_exported` |
| Rollback consideration | Additive endpoint; may be feature-flagged off entirely. |
| SP estimate | 5–8 |
| W6 evidence | Scenarios 3, 4, 6, 22, 25, 33, 35, 36 |

### 1.12 Export serializers and schema enforcement

| Attribute | Value |
|---|---|
| `norm_id` | AMD020-EXP-003 |
| Source section | AMD-020 §5.1, §5.3, §5.4, §10 |
| Current implemented fact | Export returns raw payload; no JSON Schema validation; `personal_context` and `MemoryEntry.content` are returned as-is; consent history uses existing fields only. |
| Required delta | Implement serializers producing export success/failure responses per JSON Schema 2020-12; mark `personal_context` and `MemoryEntry.content` as `opaque_payload`; include expanded consent fields (AMD020-EXP-001); producer validates closed schema before responding; consumer applies tolerant-reader policy only for `format_version` MINOR bumps. |
| Repository/module | W3: `apps/identity/services/privacy.py`, `apps/identity/serializers.py`; W2: `users/personal_data_api.py` |
| W2/W3 window | W2 + W3 |
| Dependency | AMD020-DEL-004 (closed schemas), AMD020-EXP-001 (consent fields) |
| Migration/backfill | None |
| Observability | metric `privacy.export.schema_validation.failed` |
| Rollback consideration | Contract change; keep v0.1 fallback until W6 validates. |
| SP estimate | 5–8 |
| W6 evidence | Scenarios 5, 33, 35 |

### 1.13 Secure export delivery and audit

| Attribute | Value |
|---|---|
| `norm_id` | AMD020-EXP-004 |
| Source section | AMD-020 §8.5, §9 |
| Current implemented fact | W3 view returns `JsonResponse(payload)` with `Content-Disposition: attachment; filename="personal-data-export.json"` (`apps/miniapp_api/views.py:1618-1640`). Generic filename; no export-specific audit event; no per-subject rate limit. |
| Required delta | Filename pattern `ayla-personal-data-{YYYY-MM-DD}.json` without subject identifier; emit audit event `privacy.personal_data_exported` with scope and `format_version`; apply rate limits; ensure export payload is never logged/traced; no persistent download URL. |
| Repository/module | W3: `apps/miniapp_api/views.py`, `apps/audit/services.py` |
| W2/W3 window | W3 |
| Dependency | AMD020-DEL-007 (rate limits, safe logging), AMD020-EXP-002 (export operation) |
| Migration/backfill | None |
| Observability | audit `privacy.personal_data_exported`; metric `privacy.export.delivered` |
| Rollback consideration | Additive; filename change is consumer-visible but safe. |
| SP estimate | 2–3 |
| W6 evidence | Scenarios 20, 33 |

### 1.14 Export failure, retry and post-forget semantics

| Attribute | Value |
|---|---|
| `norm_id` | AMD020-EXP-005 |
| Source section | AMD-020 §3.4, §4.3, §5.4 |
| Current implemented fact | No export-specific retry policy; no explicit behavior for export after completed delete; partial failures return whatever upstream provided. |
| Required delta | Export failure schema with `upstream_timeout`, `upstream_unavailable`, `upstream_error`, `upstream_malformed`, `init_data_expired`, `internal_error`; retry only transient upstream errors with bounded attempts; same `idempotency_key` returns existing export result without new execution; export after completed delete returns empty `personal_context` and `memory`; partial export returns failure, not a partial JSON body. |
| Repository/module | W3: `apps/identity/services/export_operations.py`, `apps/integrations/ayla/personal_context_client.py` |
| W2/W3 window | W3 |
| Dependency | AMD020-DEL-003 (idempotency), AMD020-DEL-004 (failure schema), AMD020-EXP-002 (export operation) |
| Migration/backfill | None |
| Observability | metric `privacy.export.failed.<code>` |
| Rollback consideration | Additive; failure-code mapping is consumer-visible. |
| SP estimate | 3–5 |
| W6 evidence | Scenarios 4, 6, 25, 36 |

### 1.15 ConsentRecord withdrawal/retention semantics

| Attribute | Value |
|---|---|
| `norm_id` | AMD020-CONSENT-001 |
| Source section | AMD-020 §10.3 |
| Current implemented fact | `withdraw()` stamps `withdrawn_at` but never deletes the row (`apps/consent/models.py:56-183`). |
| Required delta | Define withdrawal cascade on delete; retained fields; subject reference pseudonymization; physical deletion governed by audit-retention policy; relink behavior. |
| Repository/module | W3: `apps/identity/services/privacy.py`, `apps/consent/services.py` |
| W2/W3 window | W3 |
| Dependency | Legal retention decision |
| Migration/backfill | None initially; future cleanup by retention job. |
| Observability | audit `privacy.consent_withdrawn` |
| Rollback consideration | Additive; withdrawal is reversible until retention cleanup. |
| SP estimate | 3–5 |
| W6 evidence | Scenario 15 |

### 1.16 Audit retention policy enforcement

| Attribute | Value |
|---|---|
| `norm_id` | AMD020-AUD-001 |
| Source section | AMD-020 §9 |
| Current implemented fact | Audit records written via `write_audit`; retention not enforced by code. |
| Required delta | Enforce retention schedule per Legal ruling; treat identifiers as personal data; add scheduled cleanup job with exemption list for statutory holds. Cleanup applies to legacy rows; rows without `created_at` or classification require manual inventory and owner decision. |
| Repository/module | W3: `apps/audit/services.py`, new `apps/audit/tasks/retention_cleanup.py`; W2: `users/personal_context_events.py` |
| W2/W3 window | W2 + W3 |
| Dependency | Legal retention decision |
| Migration/backfill | Backfill `retention_until` and `contains_personal_data` for legacy rows; handle rows without `created_at` via manual inventory. |
| Observability | metric `audit.retention_cleanup.rows_deleted` |
| Rollback consideration | Start with dry-run; retention is legally sensitive. |
| SP estimate | 3–5 |
| W6 evidence | Scenarios 38a, 38b |

### 1.17 Derived representation purge

| Attribute | Value |
|---|---|
| `norm_id` | AMD020-DER-001 |
| Source section | AMD-020 §2 |
| Current implemented fact | No persistent derived representations of included classes exist in pilot. |
| Required delta | Maintain physical-store inventory for all 3 included classes; if embeddings/cache/snapshots are added before enforcement, implement corresponding cleanup hooks in purge job and barrier. |
| Repository/module | W3: wherever new representation is added |
| W2/W3 window | W3 |
| Dependency | Hard-delete purge job (AMD020-DEL-002) |
| Migration/backfill | Depends on representation. |
| Observability | per-representation purge metric |
| Rollback consideration | Add representation only with matching deletion path. |
| SP estimate | 0 for pilot; TBD if future representations added |
| W6 evidence | Scenario 17 |

---

## 2. Readiness Gate Mapping

| # | Gate item | Primary delta | Secondary deltas | Implementation status | Activation blocker | Evidence owner |
|---|---|---|---|---|---|---|
| 1 | Delete barrier | AMD020-DEL-001 | — | not implemented | yes | W6 |
| 2 | Block new records during operation | AMD020-DEL-001 | memory_writer guards | not implemented | yes | W6 |
| 3 | Block inference/derived writes during operation | AMD020-DEL-001 | memory_inferred guards | not implemented | yes | W6 |
| 4 | Stable operation_id | AMD020-DEL-003 | — | not implemented | yes | W6 |
| 5 | scope_hash | AMD020-DEL-003 | — | not implemented | yes | W6 |
| 6 | Idempotency key handling | AMD020-DEL-003 | — | not implemented | yes | W6 |
| 7 | Concurrent delete joins active operation | AMD020-DEL-003 | — | not implemented | yes | W6 |
| 8 | Replay / lost-response handling | AMD020-DEL-003, AMD020-DEL-007 | — | not implemented | yes | W6 |
| 9 | W2 returns subject_gone | AMD020-DEL-005 | — | not implemented | yes | W6 |
| 10 | Closed response schemas (JSON Schema) | AMD020-DEL-004 | — | not implemented | yes | W6 |
| 11 | Upstream timeouts + error taxonomy | AMD020-DEL-004 | — | partially implemented | yes | W6 |
| 12 | Soft-delete → purge → hard-delete SLA | AMD020-DEL-002 | Legal retention | not implemented | yes | W6 |
| 13 | Postgres cleanup | AMD020-DEL-002, AMD020-DEL-008 | — | partially implemented (soft-delete exists) | yes | W6 |
| 14 | Redis cleanup | AMD020-DER-001 | inventory evidence | not applicable_pending_inventory_evidence | no | W6 |
| 15 | Derived cleanup | AMD020-DER-001 | read-gate already covers in-memory | partially implemented (read-gate) | yes | W6 |
| 16 | Step-up authentication | AMD020-DEL-007 | W4 UX | not implemented | yes | W6 |
| 17 | Destructive nonce | AMD020-DEL-007 | — | not implemented | yes | W6 |
| 18 | Challenge TTL | AMD020-DEL-007 | — | not implemented | yes | W6 |
| 19 | Replay protection | AMD020-DEL-007 | — | not implemented | yes | W6 |
| 20 | Audit retention approved | AMD020-AUD-001 | Legal decision | pending Legal | yes | Legal/Privacy |
| 21 | W6 acceptance battery passed | all deltas | — | pending W6 | yes | W6 |
| 22 | Code version recorded | release process | — | pending | yes | Release Manager |
| 23 | Export filename pattern | AMD020-EXP-004 | — | implementation_delta | no | W6 |
| 24 | Export operation/auth/schema/failure handling | AMD020-EXP-002, AMD020-EXP-003, AMD020-EXP-005 | — | not implemented | yes | W6 |
| 25 | ConsentRecord expanded-field backfill verified | AMD020-EXP-001 | — | not implemented | yes | W6 |

---

## 3. Rollback and Safety Considerations

- All changes are additive or behind feature flags where possible, except
  physical deletion, consent withdrawal, and retention cleanup, which are
  destructive by design.
- **Committed physical deletion has no data rollback.** Rollback applies only to
  future executions: disable scheduling, stop new purges, preserve evidence, and
  initiate incident handling.
- Destructive operations (hard-delete purge) start with dry-run mode.
- During rolling deploy an old W2 may still return a generic 404. W3 must treat
  a generic 404 as `upstream_error` / `contract_violation`, not as semantic
  success. Semantic success is permitted only with `subject_gone` code and
  confirmed subject correlation.
- A feature flag may disable the entire destructive endpoint, but it must not
  weaken the endpoint's required authentication. If step-up is disabled,
  unavailable, or misconfigured, the destructive endpoint returns
  `internal_error`; no fallback to `MaxInitData`-only authentication is
  permitted.
- Audit retention cleanup must honor statutory holds; dry-run first.
- Internal credential failures trigger security alerts; external response must
  not leak credential details.
- UserPersonalContext physical wipe requires Legal confirmation before
  enforcement.

---

## 4. Open Implementation Questions

| # | Question | Blocks activation? | Owner |
|---|---|---|---|
| 1 | UserPersonalContext physical wipe confirmed? | yes | W2/Legal |
| 2 | ConsentRecord retention and subject pseudonymization | yes | Legal/Privacy |
| 3 | Retention audit-records | yes | Legal/Privacy |
| 4 | Hard-delete deadline (30d) | yes | Legal/Privacy |
| 5 | Backup retention SLA | yes | SRE/Legal |
| 6 | Timeout values (10s/25s) | yes | W3/SRE |
| 7 | Rate-limit values and challenge TTL | yes | W3/Security |
| 8 | Formal operator/processor designation | yes | Legal |
| 9 | Consent history lawful-basis text | yes | Legal |
| 10 | HMAC/pseudonymization method for audit subject references | yes | W3/Security |
| 11 | Internal W3→W2 URL: opaque token vs sanitization | yes | W2/W3 |
| 12 | Handoff scope conflicts with OP6/account-deletion promises | no | Owner/Product/Legal |

---

## 5. Change Log

### v0.6 — 2026-07-23

- Synchronized readiness gate with AMD-020 v0.6: 25 items, same statuses.
- Updated AMD020-EXP-001: mandatory backfill with sentinel values before
  activation; non-nullable expanded consent fields after backfill.
- Updated AMD020-AUD-001: legacy audit rows are in scope for cleanup/backfill.
- Updated AMD020-DEL-001: `accepted` is internal pre-commit; `aborted` terminal
  state; barrier release only after terminal state.
- Removed completed decomposition items from §4 Open Implementation Questions.
- Added v0.6 Change Log entry and version bump.

### v0.5 — 2026-07-23

- Added full export implementation backlog: AMD020-EXP-002 (orchestration/auth),
  AMD020-EXP-003 (serializers/schema enforcement), AMD020-EXP-004 (secure
  delivery/audit), AMD020-EXP-005 (failure/retry/post-forget semantics).
- Rewrote §3 Rollback and Safety: committed physical deletion has no data
  rollback; generic 404 is not semantic success; step-up is fail-closed.
- Updated §2 Readiness Gate with honest implementation statuses and activation
  blockers; added export-specific gate items.
- Expanded §4 Open Implementation Questions with atomic operation creation,
  schema closure, export backlog, and handoff-conflict items.
- Clarified AMD020-DEL-009 fallback: strict access-log/trace sanitization if
  opaque token not adopted.

### v0.4 — 2026-07-23

- Added AMD020-DEL-008 (UserPersonalContext delete semantics).
- Added AMD020-CONSENT-001 (ConsentRecord withdrawal/retention).
- Added AMD020-DEL-009 (internal W3→W2 URL PII).
- Updated AMD020-DEL-001 for operation vs per-class state.
- Updated AMD020-DEL-003 for scope_hash and concurrent join.
- Updated AMD020-DEL-004 for JSON Schema.
- Updated AMD020-DEL-007 for separated idempotency/nonce/correlation.
- Updated W6 evidence references.

### v0.3 — 2026-07-23

- Aligned with AMD-020 v0.3 corrections.

### v0.2 — 2026-07-23

- Extracted implementation deltas from AMD-020 v0.2.

---

**Конец документа — AMD-020 Implementation Amendment v0.6 (Draft, pending owner approval)**
