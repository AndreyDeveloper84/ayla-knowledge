---
node_id: ayla.architecture.amd020-c5-pilot-export-forget
title: AMD-020 — C5 Pilot Personal Context Export/Forget Contract
aliases:
  - AMD-020
  - AMD-020 C5 Pilot Personal Context Export/Forget Contract
  - C5 Pilot Export/Forget
adr_id: AMD-020
type: adr
status: draft
decision_status: proposed
implementation_status: blocked
enforcement_status: not_effective
effective_from: null
version: "0.6"
canonical_status: draft
review_status: pending_owner_approval
owner: Chief Product Architect
priority: P0
knowledge_area:
  - architecture
domain:
  - user-context
  - consent
  - identity
  - cross-domain
concerns:
  - privacy
  - security
  - audit
  - compliance
  - governance
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
  - ayla/adr
  - adr/020
  - privacy
  - 152-fz
  - c5
  - pilot
implements:
  - "[[Ayla Constitution]]"
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Glossary]]"
  - "[[Ayla Knowledge Architecture Specification]]"
  - "[[Document Quality Bar (W7)]]"
related:
  - "[[AMD-020 C5 Implementation Amendment]]"
review_cycle: event-driven
---

# AMD-020 — C5 Pilot Personal Context Export/Forget Contract

## Document State

| Field | Value |
|---|---|
| Document status | Draft |
| Decision status | Proposed |
| Implementation status | Blocked |
| Enforcement status | Not effective |
| Effective from | null |
| Version | 0.6 (2026-07-23) |
| Review status | pending_owner_approval |

**Owner ruling:** Режим 2+ — двухступенчатая канонизация. Настоящий документ
подготовлен для повторного owner review. Самостоятельный перевод в
Canonical/Accepted запрещён.

**What this document IS:** нормативный контракт self-service экспорта и
удаления (forget) данных, входящих в утверждённый Personal Context pilot scope,
для пилота 2026-08-15.

**What this document IS NOT (дословные дисклеймеры):**

- AMD-020 v0.6 не является полным механизмом реализации прав субъекта по 152-ФЗ.
- AMD-020 v0.6 не является формальным ответом по статье 14 152-ФЗ.
- AMD-020 v0.6 не является удалением аккаунта.
- AMD-020 v0.6 не является исчерпывающим удалением всех персональных данных Ayla.

---

## 1. Pilot Scope Registry

### 1.1 Included

| Class | Authoritative system | Authoritative model | Owner | Export semantics | Forget/delete semantics | Physical stores | Derived representations | Current endpoint exists | Current basic behavior | AMD020 compliance status | Source evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UserPersonalContext (declared prefs) | W2 (Ayla) | `users.UserPersonalContext` | W2 | Verbatim payload from `GET /api/v1/internal/users/{id}/personal-data/export/` | Physical wipe via `DELETE /api/v1/internal/users/{id}/personal-data/` | Postgres `users_userpersonalcontext` | None in pilot scope | yes | physical DELETE on request | not compliant: lacks barrier, per-step result, subject_gone, retention manifest, backup tracking | `users/personal_data_api.py:105-118`, `users/personal_data_api.py:147-152`, `users/models.py:425-544` |
| Green `MemoryEntry` | W3 (bot) | `apps.identity.models.MemoryEntry` | W3 | Live green rows for the person (`read_green_entries`) | Soft-delete + `request_forget_all` UPC tombstone; async physical purge after retention | Postgres `identity_memoryentry`; encrypted at rest (Fernet) | In-memory prompt block via `build_concierge_memory_block`; no persistent snapshots or vector DB | yes | soft-delete on request; no explicit purge job | not compliant: lacks barrier, hard-delete SLA, derived-cleanup verification | `apps/identity/services/privacy.py:127-141`, `apps/identity/services/memory_deleter.py:33-101`, `apps/identity/services/memory_reader.py:84-106` |
| `ConsentRecord` | W3 (bot) | `apps.consent.models.ConsentRecord` | W3 | History of consent events for the person | Cascade withdraw (records retained as audit trail, marked withdrawn; physical deletion governed by separate audit-retention policy) | Postgres `consent_consentrecord` | None | yes | withdraw stamps `withdrawn_at`; row retained | not compliant: retention/redaction/pseudonymization not finalized | `apps/identity/services/privacy.py:143-157`, `apps/identity/services/privacy.py:229-233`, `apps/consent/models.py:56-183` |

### 1.2 Excluded

| Class | Status | Owner | Source handoff | Reason excluded | Future inventory obligation | Known conflict |
|---|---|---|---|---|---|---|
| Account deletion | post_pilot_inventory_required | Product Architecture | `2026-05-18-customer-first-time-handoff.md` §12 F4; `2026-05-19-master-device-reauth-handoff.md` §9.1 | Out of pilot scope; AMD-020 covers personal context, not account closure (OP6 is a separate track) | Data Inventory Matrix must define account-deletion orchestration | `customer-first-time` button label «Удалить все мои данные» implies account deletion; must not be conflated with AMD-020 |
| Formal Article 14 response | post_pilot_inventory_required | Legal/Privacy | `owner_verdict_amd020_v01_2026-07-23.md` Part 2 | Export is data-portability, not formal subject-access response | Separate 152-ФЗ Chapter 2 response track | — |
| Conversations / messages | post_pilot_inventory_required | W5 / Conversation Owner | `2026-05-17-conversations-handoff.md` §7; `2026-05-18-master-mobile-handoff.md` §13 E17; `2026-05-19-master-admin-internal-chat-handoff.md` §2.1, §8.5 | Conversation retention governed by separate ownership and statutory limits; ADR-0009 assigns conversations to bot, but Ayla also holds `ai.Conversation/Message` | Inventory + deletion owner per channel/tenant; resolve duplicated ownership | Handoffs assume conversations are hidden/exported on customer deletion; AMD-020 pilot does not cover them |
| Bookings | post_pilot_inventory_required | W2 / Booking Owner | `2026-05-18-customer-first-time-handoff.md` §12 F3; `c5_revision_2026-07-21.md` §2 | Statutory/booking retention; dual ownership (`BookingRequest` local lifecycle) | Data Inventory Matrix row; complete Block D ownership migration | «My visits» shown in profile next to delete button; may imply bookings are deletable |
| Wellness and sleep history | post_pilot_inventory_required | Wellness Owner | `2026-05-19-wellness-sleep-handoff.md` §11.4; `2026-05-19-master-offboarding-handoff.md` §2.4, §6.4; `2026-05-18-customer-first-time-handoff.md` §12 F4 (allergies/contraindications — ambiguous) | Out of pilot personal-context scope; special-category health data | Inventory + lawful basis review; resolve red-zone ownership | `wellness-sleep-handoff` states OP6 export/delete includes raw sleep history; directly contradicts AMD-020 exclusion |
| Loyalty records | post_pilot_inventory_required | Loyalty Owner | `2026-05-18-loyalty-system-handoff.md` §14 | Separate loyalty system/retention | Inventory row | Handoff states account deletion erases loyalty data; AMD-020 is not account deletion |
| Reviews | post_pilot_inventory_required | Gamma / Reviews Owner | `2026-05-19-master-reviews-feedback-handoff.md` §2.10, §7.1, §7.2 | Ayla canonical; mirror-only on bot | Inventory + deletion path | Handoff treats reviews as customer personal data with 30-day hard-delete window; outside AMD-020 pilot scope |
| Support communications | post_pilot_inventory_required | Support Owner | `2026-05-19-master-admin-internal-chat-handoff.md` §2.1, §8.5 | Separate support/ticketing retention | Inventory row | Handoff grants master export/hard-delete of internal chat threads; outside AMD-020 pilot scope |
| Analytics outside pilot scope | post_pilot_inventory_required | Analytics Owner | `2026-05-18-analytics-dashboard-handoff.md` §10, §21 Q-AD3; `2026-05-18-marketing-campaigns-handoff.md` §6 | Aggregated/anonymized; separate retention | Inventory + pseudonymization rules | Marketing `CampaignDispatch` treated as personal data for compliance export; not in AMD-020 included scope |
| System-wide caches and derived data not originating from included scope | post_pilot_inventory_required | SRE / Platform | `owner_verdict_amd020_v01_2026-07-23.md` Part 2 (no first-source handoff) | General infrastructure caches are not personal-context derived | Inventory of system caches with PII potential | — |

**Important:** Исключение system-wide derived data не распространяется на
производные данные трёх included-классов. Производные от included scope
(embeddings, prompt snapshots, cache entries, derived attributes, indexes) —
внутри пилотного deletion boundary (см. §2).

### 1.3 Known conflicts with broader data-subject scope

Several handoff documents frame a broader "delete/export all my data" scope
(OP6 / account-deletion track) that conflicts with the narrow AMD-020 pilot
boundary. These conflicts are **not resolved** in v0.6; they are recorded here
and in §14 for owner decision:

| Conflict | Handoff source | AMD-020 position | Resolution authority |
|---|---|---|---|
| Wellness/sleep export and deletion cascades with OP6 | `2026-05-19-wellness-sleep-handoff.md` §11.4 | Excluded from pilot scope (§1.2) | Owner / Legal / Privacy / OP6 track |
| Loyalty data erased on account deletion | `2026-05-18-loyalty-system-handoff.md` §14 | Loyalty records excluded; AMD-020 not account deletion | Owner / OP6 track |
| Reviews have 30-day customer hard-delete window | `2026-05-19-master-reviews-feedback-handoff.md` §2.10, §7.1, §7.2 | Reviews excluded from pilot scope | Owner / Gamma Reviews Owner |
| Conversations hidden/exported on customer deletion | `2026-05-17-conversations-handoff.md` §7; `2026-05-18-master-mobile-handoff.md` §13 E17; `2026-05-19-master-admin-internal-chat-handoff.md` §8.5 | Conversations/messages excluded from pilot scope | Owner / W5 Conversation Owner |
| Customer profile button «Удалить все мои данные» triggers OP6 | `2026-05-18-customer-first-time-handoff.md` §12 F4 | AMD-020 is not exhaustive deletion / account deletion | Owner / Product / Legal |
| Account-lock state machine includes `DELETED` | `2026-05-19-master-device-reauth-handoff.md` §9.1 | Account deletion excluded from pilot scope | Owner / OP6 track |

### 1.4 Handoff scope analysis

All 16 owner-provided handoff files were reviewed against the AMD-020 pilot boundary.
The table below records the inclusion decision, direct source sections, and any conflict
with the narrow pilot scope. It is the evidence basis for the excluded-scope registry
in §1.2 and the conflicts table in §1.3.

| Handoff file | Reviewed fully | Relevant personal-data classes/data | Inclusion decision | Direct source sections | Conflict with AMD-020 pilot scope | Owner action |
|---|---|---|---|---|---|---|
| `2026-05-18-analytics-dashboard-handoff.md` | yes | Customer, `BookingRequest`, `Conversation`, `Master`, `AnalyticsSnapshot`, billing | `excluded_post_pilot_inventory` | §10 Export, §21 Q-AD3 | none | Add analytics / `AnalyticsSnapshot` to post-pilot Data Inventory Matrix; define retention and ownership. |
| `2026-05-17-salon-onboarding-handoff.md` | yes | Tenant admin identity, YClients credentials, KB documents, billing | `not_applicable_to_customer_pilot` | §8 Data retention | none | Govern tenant-admin data under tenant-data governance, not AMD-020. |
| `2026-05-18-persona-editor-handoff.md` | yes | Persona change history / staff identifiers | `not_applicable_to_customer_pilot` | none | none | Persona config is tenant-level business config; route staff-data requests via OP6 or general DSR track. |
| `2026-05-17-conversations-handoff.md` | yes | `Conversation`/`Message`, customer profile PII, medical notes, visit history, learning suggestions | `excluded_post_pilot_inventory` | §7 Edge cases, §C4 GDPR deletion | Account-deletion cascade implies broader OP6 scope | W5 / Conversation Owner defines export/deletion path in Data Inventory Matrix; route account-deletion cascade to OP6. |
| `2026-05-18-marketing-campaigns-handoff.md` | yes | `CampaignDispatch`, `CampaignAudience`, segmentation profile fields | `excluded_post_pilot_inventory` | §3 Data model, §6 Compliance/export | CSV export of recipient hash + opt-out timestamps is a personal-data export outside pilot | Decide whether marketing CSV export belongs to AMD-020 or a separate compliance module. |
| `2026-05-18-master-mobile-handoff.md` | yes | Customer first name/aftercare notes, conversation transcripts, master profile/audit | `excluded_post_pilot_inventory` | §8 Gating matrix, §13 E17 | Customer-deletion request handling for master deeplinks implies OP6 scope | Resolve Q-M4 aftercare-notes retention; classify master-authored replies as post-pilot inventory. |
| `2026-05-18-loyalty-system-handoff.md` | yes | `LoyaltyAccount`, `LoyaltyEvent`, `ReferralPending`, visit/booking/LTV data | `not_applicable_to_customer_pilot` | §14 Edge cases, §17 Q-L12 | Account deletion erases loyalty data (OP6) | Add loyalty customer data as a separate post-pilot inventory item. |
| `2026-05-19-master-device-reauth-handoff.md` | yes | `MasterSession`, `MasterRecoveryAttempt`, phone/MAX binding, earnings, audit | `excluded_post_pilot_inventory` | §9.1 `DELETED` state, §6.4 retention, §2.5 | Account-lock state machine `DELETED` terminal state conflicts with AMD-020 scope | Reclassify `DELETED` transition as OP6 / account-deletion track. |
| `2026-05-19-master-reviews-feedback-handoff.md` | yes | `CustomerFeedback`, `MasterReviewAggregate`, `ReviewMasterAction`, `ReviewAdminAction` | `excluded_post_pilot_inventory` | §2.10 Privacy, §7.1/§7.2, §9.1 | 30-day customer hard-delete window outside pilot | Classify `CustomerFeedback` as distinct post-pilot inventory; decide 30d delete/anonymization owner. |
| `2026-05-19-master-earnings-handoff.md` | yes | `Master`, Customer initials, `Booking`, `MasterEarning`, `Tip`, `EarningsExport` | `excluded_post_pilot_inventory` | §2.9 Tax export, §10.3 PII minimization, §11.7 | none (tax export is a separate financial export) | Add master earnings classes to post-pilot Data Inventory Matrix. |
| `2026-05-19-master-time-off-handoff.md` | yes | `MasterLeaveRequest`, `MasterLeaveBookingImpact`, `SickDayPatternFlag`, `MasterRecurringSchedule` | `not_applicable_to_customer_pilot` | none | none | Govern master leave records by tenant/HR policy or OP6 if masters are later covered. |
| `2026-05-18-customer-first-time-handoff.md` | yes | Customer profile, preferences, visits, feedback, dispatch logs, phone, location, attachments | `excluded_post_pilot_inventory` | §12 F4, §15 `data-deletion-request` | «Удалить все мои данные» button triggers OP6 customer-deletion workflow; conflicts with narrow pilot | Reconcile F4 button copy with AMD-020 scope: restrict label to pilot-covered classes or expand inventory before shipping. |
| `2026-05-19-master-substitution-handoff.md` | yes | Substitution records, customer preferences/allergies, wellness profile, AI memory, reviews | `not_applicable_to_customer_pilot` | §2.12, §5.3, §5.6 | none | No AMD-020 delta; ensure substitution records are covered by OP6 inventory. |
| `2026-05-19-wellness-sleep-handoff.md` | yes | `WellnessSleepEvent`, `WellnessModuleConsent`, derived profile aggregates | `excluded_post_pilot_inventory` | §2.5, §4.1, §5.1, §9.1, §11.4 | OP6 export includes raw sleep history; 30d revoke deletion outside pilot | Classify `WellnessSleepEvent` and derived aggregates as post-pilot inventory. |
| `2026-05-19-master-admin-internal-chat-handoff.md` | yes | `MasterAdminThread`/`Message`/`Attachment`, linked artifacts | `excluded_post_pilot_inventory` | §2.8, §6 Data models, §8.4/§8.5 | Export/hard-delete promises for master-admin chat outside pilot | Decide whether §8.5/§2.8 promises must be honored pre-pilot or deferred to post-pilot inventory. |
| `2026-05-19-master-offboarding-handoff.md` | yes | Master data, customer-master AI memory, reviews, wellness profile | `excluded_post_pilot_inventory` | §2.2, §2.3, §6.4, §7.1/§7.3/§7.5 | none | Confirm customer-master `MemoryEntry` revocation semantics are compatible with AMD-020 green `MemoryEntry` lifecycle. |

**Classification legend:**

- `excluded_post_pilot_inventory` — personal-data class exists and needs a future export/forget owner, but is outside the AMD-020 pilot boundary.
- `not_applicable_to_customer_pilot` — the file concerns tenant/master/operational data, not the customer personal-context pilot scope.

---

## 2. Derived Boundary

### 2.1 Physical-store inventory for all included classes

| Included class | Postgres | Redis/cache | Embeddings/vector | Prompt snapshots | Audit/events | Queues | Analytics | Logs/traces | Backups | Derived attributes | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UserPersonalContext (W2) | `users_userpersonalcontext` | none found | none found | none found | `AnalyticsEvent` via `emit_personal_data_deleted` | none found | none found | `user_id` in structured logs | Postgres backups | none found | SHA `f6e9572e`: `users/personal_context_events.py`, `users/models.py:425-544`; `personal_data_api.py` not present in this branch |
| Green MemoryEntry (W3) | `identity_memoryentry` | none found | none found (ChromaDB only in `apps/kb/`) | none found | `write_audit("memory.forget_entry")`, `write_audit("memory.forget_all_requested")` | none found | none found | `user_id` in structured logs | Postgres backups | in-memory prompt block | SHA `fe6c1f87`: `apps/identity/models.py:621-838`, `apps/identity/services/memory_writer.py`; `memory_reader.py`/`memory_deleter.py`/`memory_block.py` not present in main branch |
| ConsentRecord (W3) | `consent_consentrecord` | none found | none found | none found | `write_audit("privacy.personal_data_deleted")`; `ConsentRecord` itself is audit trail | none found | none found | `bot_user_id` in audit payload | Postgres backups | none found | SHA `fe6c1f87`: `apps/consent/models.py:56-183`, `apps/identity/services/privacy.py:143-157`, `apps/identity/services/privacy.py:229-233` |

### 2.2 Evidence statement

Reproducible inventory commands (run against pinned SHAs):

```bash
# ai-bot-platform SHA fe6c1f872bcff5a0a2ade8cc0b3d4bdef9a31b8a
grep -n -i 'redis\|cache\|chroma\|embedding\|snapshot\|persist' \
  apps/identity/services/memory_writer.py
# result: <no matches>

grep -n -i 'redis\|cache\|chroma\|embedding\|snapshot\|persist' \
  apps/consent/models.py
# result: line 40/118 mention "document_version snapshots" (metadata, not persistent derived store)

grep -rn 'from django.core.cache\|cache\.\|caches\[' \
  apps/identity apps/consent --include='*.py'
# result: <no matches>

# djangoproject SHA f6e9572e157b8391d21c02e979e07e033f64fd6f
grep -n -i 'redis\|cache\|chroma\|embedding\|snapshot\|persist' \
  users/models.py users/personal_context_events.py
# result: <no matches>
```

- **ChromaDB:** dependency present in `.venv`, but production code using ChromaDB
  lives only in `apps/kb/` (knowledge-base retrieval). No call path from any
  included class to ChromaDB was found.
- **Redis/Django cache:** general cache usage exists in the repo (eventbus,
  catalog sync, etc.), but none of the three included-class read/write paths use
  cache. Status: `not_applicable_pending_inventory_evidence` for pilot.
- **Prompt snapshots:** `build_concierge_memory_block` is not present in the
  pinned main branch of `ai-bot-platform`; the only memory-related service found
  is `apps/identity/services/memory_writer.py`, which persists to Postgres.
- **Audit/events:** all audit rows reference `user_id`/`bot_user_id` but do not
  store deleted personal values.
- **Backups:** standard Postgres backups exist; backup retention SLA is an owner
  decision.

### 2.3 Proposed norm

Deletion of included data must cover:

1. Primary Postgres rows (`UserPersonalContext`, green `MemoryEntry`,
   `ConsentRecord` withdrawal markers).
2. Derived in-memory prompt block (covered by read-gate).
3. Audit rows that are within their retention period (listed in `retained[]`).
4. Backups after `backup_expiry`.

If future implementations add embeddings, cache, or snapshots for any included
class, those representations must be added to the deletion boundary before
enforcement.

---

## 3. Delete Barrier, Operation State and Per-Class State

### 3.1 Operation state

Нормативно определены состояния операции:

- `accepted` — **внутреннее транзакционное состояние**. Запрос прошёл базовую
  валидацию, но `operation_id` ещё не возвращён клиенту и не виден другим
  workers. Barrier и scope lock создаются в той же транзакции, что и запись
  операции. `accepted` не является внешне наблюдаемым состоянием.
- `blocked` — **первое внешне наблюдаемое состояние**. Barrier и scope lock
  установлены атомарно с созданием операции; новые записи и derived writes
  запрещены. Клиент получает `operation_id` только после успешного перехода в
  `blocked`.
- `processing` — активные обработчики остановлены/заблокированы; каскад
  удаления выполняется.
- `partially_completed` — **внутреннее состояние**: каскад завершён с одним
  или более failed steps; retryable. Во внешнем ответе это состояние
  отображается как `status: "partial"`.
- `completed` — каскад завершён успешно; все included-классы обработаны.
- `failed` — каскад завершён с не-retryable ошибкой; terminal state.
- `aborted` — операция прервана авторизованным break-glass, relink или
  неисправимым сбоем; terminal state. Barrier снимается только после
  достижения terminal state и записи incident/audit.

**State-to-response mapping:**

| Internal operation state | External response `status` | HTTP |
|---|---|---|
| `blocked` | `accepted` (or `blocked` in status read) | 202 |
| `processing` | `processing` | 202 |
| `partially_completed` | `partial` | 502 |
| `completed` | `completed` | 200 |
| `failed` | `failed` | 502/504/500 |
| `aborted` | `failed` or `aborted`* | 502/500 |

`*` `aborted` may be exposed as a dedicated external `status` only after owner
approval of the break-glass/relink semantics. Until then, external responses use
`failed` with `error.code: subject_mismatch` / `internal_error`.

**Atomicity requirement:** operation record + scope lock + barrier activation
are created in a single database transaction. If the transaction fails, the
client receives an error and no `operation_id`. There is no externally
observable window between `operation_id` issuance and barrier activation.

**Barrier release rule:** barrier is released only when the operation reaches a
terminal state (`completed`, `failed`, or `aborted`). Automatic release after a
partial or unrecoverable failure without terminal state is prohibited.

### 3.2 Per-class state

| Included class | States |
|---|---|
| UserPersonalContext (W2) | `active` → `deleted` (immediate primary row removal) → `backup_expired` |
| Green MemoryEntry (W3) | `active` → `soft_deleted` → `primary_purged` → `backup_expired` |
| ConsentRecord (W3) | `active` → `withdrawn` → `retained_under_other_basis` (until legal retention expiry) |

**Notes:**

- For `UserPersonalContext` the implemented semantics is **immediate physical
  wipe** (`users/personal_data_api.py:152`). Canonical status is
  `proposed_norm_pending_owner_confirmation` pending owner/Legal confirmation
  (§14). If confirmed, the `deleted` state and primary-row purge are observed
  together; the remaining lifecycle is backup expiry. `primary_purged` is
  therefore implicit in `deleted` for this class.
- `retained_under_other_basis` — параллельное состояние для audit/consent
  history, а не последовательное состояние всей операции.

### 3.3 Barrier requirements

Barrier устанавливается атомарно с созданием операции. Во время операции
заблокированы:

- новые записи included-классов;
- фоновые inference jobs, создающие green MemoryEntry;
- повторное создание derived representations;
- конкурентный delete с другим `idempotency_key`, но совпадающим `scope_hash`,
  не создаёт вторую операцию — такой запрос присоединяется к активной операции
  (см. §4.3).

### 3.4 Hard-delete lifecycle

| Parameter | Proposed value | Status | Rationale |
|---|---|---|---|
| `soft_delete_retention` | 30 days after `soft_deleted_at` | owner_decision_required | Matches current model help-text (`MemoryEntry.soft_deleted_at`: "Physical purge happens 30 days later"), spec §5, and ADR-0011 tombstone semantics. Legal must confirm. |
| `primary_purge_deadline` | `soft_deleted_at + soft_delete_retention` | derived | Primary rows purged after retention. |
| `backup_expiry` | 35 days after soft-delete (5-day backup retention assumed) | owner_decision_required | Must exceed primary purge deadline to cover backup windows. |
| `hard_deleted_at` | `max(primary_purge_deadline, backup_expiry)` | derived | Transition to `backup_expired` only after both primary and backups are clean. |
| `purge_job` | daily Celery cron scanning `soft_deleted_at <= now - soft_delete_retention` | implementation_delta | Explicit job needed for physical purge. |

### 3.5 Full operation lifecycle diagram

```
accepted  (internal pre-commit state; not observable externally)
  │
  ▼ (atomic transaction: operation record + scope lock + barrier)
blocked  ← first externally observable state; barrier active
  │
  ▼
processing  ← каскад выполняется
  │
  ├──► partially_completed  ← есть failed steps; retryable
  │      │
  │      ├──► retry  → processing
  │      │
  │      └──► max retries / unrecoverable → failed  (terminal)
  │
  ├──► completed  ← все шаги успешны (terminal)
  │         │
  │         └──► per-class lifecycle продолжается независимо:
  │                UserPersonalContext: deleted → backup_expired
  │                MemoryEntry: soft_deleted → primary_purged → backup_expired
  │                ConsentRecord: withdrawn → retained_under_other_basis
  │
  └──► aborted  ← break-glass / relink / authorized terminal abort (terminal)

Barrier is released only after a terminal state is persisted.
```

### 3.6 Break-glass and terminal abort

A delete operation may be moved to terminal `aborted` state only by:

1. **Relink** — `scope_hash.link_generation` changes mid-flight (§4.4).
2. **Authorized break-glass** — two authorized operators (W3 on-call + Security)
   approve an explicit abort because the operation is stuck and cannot resume
   safely.
3. **Unrecoverable infrastructure failure** — after all bounded retries are
   exhausted and the incident commander records a terminal abort decision.

Abort procedure:

- Record reason code, operator identities, incident ticket, and audit event
  `privacy.delete_aborted`.
- Move operation to `aborted` **before** releasing the barrier.
- Do **not** auto-retry an `aborted` operation; the client must start a new
  delete operation with a new `idempotency_key` after the incident is resolved.
- Preserve evidence of completed steps; already-deleted classes remain deleted.
- After abort, perform a fresh inventory sweep before any new operation on the
  same `scope_hash`.

---

## 4. operation_id, scope_hash and Idempotency

### 4.1 Identifiers

| Field | Purpose | Source |
|---|---|---|
| `operation_id` | Stable end-to-end identifier of one delete/export operation | Generated by W3 at request acceptance |
| `scope_hash` | Канонический идентификатор семантического scope операции | Вычисляется W3 из `subject_ref + tenant_ref + operation_type + included_classes + contract_version + link_generation` |
| `idempotency_key` | Client-supplied key for safe retry | Miniapp request header (proposed: `Idempotency-Key`) |
| `correlation_id` | Traces request across W4 → W3 → W2 and audit | Carried in request headers and logs |
| `request_attempt` | Ordinal of the client HTTP retry | Incremented by W3 for each request with same `idempotency_key` |
| `execution_attempt` | Ordinal of actual execution | Incremented only when a new execution is attempted |

### 4.2 scope_hash

`scope_hash` определяет активную операцию. Компоненты:

- `subject_ref` — псевдонимизированный или HMAC-дайджест `ayla_user_id`/`bot_user_id`;
- `tenant_ref` — tenant identifier;
- `operation_type` — `export` или `delete`;
- `included_classes` — canonical class list for this contract version;
- `contract_version` — AMD-020 version (e.g., `0.4`);
- `link_generation` — версия связи BotUser ↔ Ayla User, чтобы отслеживать relink; формируется из `BotUser.ayla_link_generation` (или аналогичного поля) и включается в `scope_hash`, чтобы операция, начатая до relink, не применялась к новому субъекту.

### 4.3 Idempotency rules

- Повторный запрос с тем же `idempotency_key` и эквивалентным `scope_hash`
  возвращает результат текущего/предыдущего состояния операции.
- **Concurrent delete:** concurrent request с другим `idempotency_key`, но
  совпадающим `scope_hash`, **joins** активную операцию и получает тот же
  `operation_id`. Вторая destructive execution не создаётся и не queued.
- **Relink during deletion:** операция **aborted**; клиент получает
  `subject_mismatch` и должен инициировать новую операцию после relink.
  Полный lifecycle relink описан в §4.4.
- Retry после потери success-response: клиент повторяет с тем же
  `idempotency_key`; W3 возвращает финальный результат из idempotency store
  (replay read), не запуская новое execution.
- Срок хранения idempotency record: proposed 7 days after operation completion
  (`owner_decision_required`).
- После завершённой операции повторный запрос возвращает `completed_at` и
  финальный `status` без увеличения `execution_attempt`.

### 4.4 Relink lifecycle

`scope_hash` включает `link_generation`. Если связь BotUser ↔ Ayla User
меняется во время активной операции:

1. Текущая операция немедленно переходит в terminal state `aborted`.
2. Внешний ответ: `failed` (или `aborted` после owner approval) с
   `error.code: subject_mismatch`.
3. Уже выполненные шаги остаются выполненными; незавершённые шаги отменяются.
4. Barrier снимается только после достижения `aborted` и записи audit/incident.
5. Клиент должен инициировать **новую** операцию с новым `idempotency_key`;
   новый `scope_hash` будет содержать новое `link_generation`.

**Fate of the old persona:**

- Старая persona (`BotUser` + связанный `Ayla User`) продолжает существовать в
  системе со своей историей согласий, памяти и аудита.
- Пользователь не теряет прав на экспорт/удаление данных старой persona;
  доступ к старой persona осуществляется через OP6 / account-deletion track или
  через отдельный owner-approved flow связывания persona.
- `ConsentRecord`, `MemoryEntry` и `UserPersonalContext` старой persona не
  мигрируют к новой persona автоматически.
- Повторный relink обратно на старый `Ayla User` восстанавливает прежний
  `scope_hash` и позволяет продолжить операции над старой persona.

**Export after relink:**

- An in-flight export operation is aborted if relink occurs; the client must
  retry after relink.
- Export, созданный до relink, привязан к старому `scope_hash` и содержит
  данные старой persona.
- Новый export возвращает данные только для текущей persona.

---

## 5. Response Schemas

### 5.1 Schema contract

- Все ответы описаны JSON Schema 2020-12.
- `additionalProperties: false` на каждом уровне, **кроме намеренно opaque
  payload** (`personal_context`, `MemoryEntry.content`). Эти объекты не закрыты
  данным контрактом; их внутренняя структура определяется
  `UserPersonalContextSerializer` и `MemoryEntry` content contract.
- Producer (W3) **обязан** валидировать ответ по закрытой части схемы.
- Consumer (W4 / miniapp) **обязан** игнорировать неизвестные поля только при
  получении ответа с `format_version` выше известной MINOR-версии
  (tolerant-reader policy).
- Добавление полей требует MINOR-инкремента `format_version` / contract version.
- Удаление/переименование полей требует MAJOR-инкремента и нового amendment.

### 5.2 Schema bundle contract

- Each root schema in §5.3–§5.7 is a self-contained JSON Schema 2020-12 document.
- Shared structures (`subject`, `perStepResults`, `retainedItem`, `error`) are duplicated in every root schema so that all `$ref` resolve within the same document.
- `additionalProperties: false` is enforced at every closed level.
- `personal_context` and `MemoryEntry.content` are intentionally declared `opaque_payload` and are not closed by this contract.
- `subject_gone` is formalized as a separate closed schema in §6.

### 5.3 Export success schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$defs": {
    "subject": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "ayla_user_id",
        "bot_user_id"
      ],
      "properties": {
        "ayla_user_id": {
          "oneOf": [
            {
              "type": "string",
              "format": "uuid"
            },
            {
              "type": "null"
            }
          ]
        },
        "bot_user_id": {
          "type": "string",
          "format": "uuid"
        }
      }
    },
    "perStepResults": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "ayla_delete",
        "memory_delete",
        "consent_withdraw"
      ],
      "properties": {
        "ayla_delete": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "ok",
            "detail"
          ],
          "properties": {
            "ok": {
              "type": "boolean"
            },
            "detail": {
              "type": "string",
              "enum": [
                "deleted",
                "already_deleted",
                "subject_gone",
                "not_linked"
              ]
            }
          }
        },
        "memory_delete": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "ok",
            "detail"
          ],
          "properties": {
            "ok": {
              "type": "boolean"
            },
            "detail": {
              "type": "string",
              "enum": [
                "deleted",
                "already_deleted",
                "not_linked"
              ]
            }
          }
        },
        "consent_withdraw": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "ok",
            "detail"
          ],
          "properties": {
            "ok": {
              "type": "boolean"
            },
            "detail": {
              "type": "string",
              "enum": [
                "withdrawn",
                "already_withdrawn",
                "not_linked"
              ]
            }
          }
        }
      }
    },
    "retainedItem": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "category",
        "reason",
        "lawful_basis",
        "retention_until",
        "decision_status",
        "restrictions",
        "owner",
        "deletion_trigger"
      ],
      "properties": {
        "category": {
          "type": "string",
          "enum": [
            "audit_trail",
            "consent_history",
            "statutory_record",
            "backup",
            "tombstone",
            "other"
          ]
        },
        "reason": {
          "type": "string",
          "enum": [
            "regulatory_audit",
            "withdrawal_evidence",
            "statutory_retention",
            "backup_window",
            "lawful_basis_other"
          ]
        },
        "lawful_basis": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "retention_until": {
          "oneOf": [
            {
              "type": "string",
              "format": "date-time"
            },
            {
              "type": "null"
            }
          ]
        },
        "decision_status": {
          "type": "string",
          "enum": [
            "owner_decision_required",
            "approved"
          ]
        },
        "restrictions": {
          "type": "string",
          "enum": [
            "no_personal_values",
            "read_only",
            "access_role_restriction"
          ]
        },
        "owner": {
          "type": "string"
        },
        "deletion_trigger": {
          "type": "string",
          "enum": [
            "legal_retention_expiry",
            "backup_expiry",
            "owner_decision"
          ]
        }
      }
    },
    "error": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "code",
        "message",
        "retryable"
      ],
      "properties": {
        "code": {
          "type": "string",
          "enum": [
            "upstream_timeout",
            "upstream_unavailable",
            "upstream_error",
            "upstream_malformed",
            "rate_limited",
            "auth_invalid",
            "init_data_expired",
            "subject_mismatch",
            "confirmation_expired",
            "replay_detected",
            "cross_tenant_violation",
            "schema_mismatch",
            "contract_violation",
            "internal_error"
          ]
        },
        "message": {
          "type": "string"
        },
        "retryable": {
          "type": "boolean"
        }
      }
    }
  },
  "type": "object",
  "additionalProperties": false,
  "required": [
    "operation_id",
    "status",
    "generated_at",
    "subject",
    "format_version",
    "ayla",
    "memory",
    "consents"
  ],
  "properties": {
    "operation_id": {
      "type": "string",
      "format": "uuid"
    },
    "status": {
      "type": "string",
      "enum": [
        "completed"
      ]
    },
    "generated_at": {
      "type": "string",
      "format": "date-time"
    },
    "subject": {
      "$ref": "#/$defs/subject"
    },
    "format_version": {
      "type": "string",
      "enum": [
        "1.0"
      ]
    },
    "ayla": {
      "oneOf": [
        {
          "type": "null"
        },
        {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "user_id",
            "exported_at",
            "personal_context"
          ],
          "properties": {
            "user_id": {
              "type": "string",
              "format": "uuid"
            },
            "exported_at": {
              "type": "string",
              "format": "date-time"
            },
            "personal_context": {
              "description": "opaque_payload: structure governed by UserPersonalContextSerializer; not closed by this schema",
              "oneOf": [
                {
                  "type": "object",
                  "additionalProperties": true
                },
                {
                  "type": "null"
                }
              ]
            }
          }
        }
      ]
    },
    "memory": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "id",
          "kind",
          "source",
          "content",
          "last_inferred_at",
          "created_at"
        ],
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "kind": {
            "type": "string"
          },
          "source": {
            "type": "string",
            "enum": [
              "explicit",
              "inferred",
              "signal"
            ]
          },
          "content": {
            "description": "opaque_payload: MemoryEntry content structure; not closed by this schema",
            "type": "object",
            "additionalProperties": true
          },
          "last_inferred_at": {
            "oneOf": [
              {
                "type": "string",
                "format": "date-time"
              },
              {
                "type": "null"
              }
            ]
          },
          "created_at": {
            "type": "string",
            "format": "date-time"
          }
        }
      }
    },
    "consents": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "consent_type",
          "granted",
          "document_version",
          "source",
          "captured_at",
          "withdrawn_at",
          "purpose",
          "data_categories",
          "operator",
          "recipients",
          "term",
          "lawful_basis",
          "identification_method"
        ],
        "properties": {
          "consent_type": {
            "type": "string"
          },
          "granted": {
            "type": "boolean"
          },
          "document_version": {
            "type": "string"
          },
          "source": {
            "type": "string"
          },
          "captured_at": {
            "type": "string",
            "format": "date-time"
          },
          "withdrawn_at": {
            "oneOf": [
              {
                "type": "string",
                "format": "date-time"
              },
              {
                "type": "null"
              }
            ]
          },
          "purpose": {
            "type": "string"
          },
          "data_categories": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "operator": {
            "type": "string"
          },
          "recipients": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "term": {
            "type": "string"
          },
          "lawful_basis": {
            "oneOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ]
          },
          "identification_method": {
            "type": "string"
          }
        }
      }
    }
  }
}
```
*(Export is all-or-nothing; there is no partial export response in the pilot contract. Any upstream failure yields the failure schema with HTTP 502/504.)*

### 5.4 Export failure schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$defs": {
    "subject": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "ayla_user_id",
        "bot_user_id"
      ],
      "properties": {
        "ayla_user_id": {
          "oneOf": [
            {
              "type": "string",
              "format": "uuid"
            },
            {
              "type": "null"
            }
          ]
        },
        "bot_user_id": {
          "type": "string",
          "format": "uuid"
        }
      }
    },
    "perStepResults": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "ayla_delete",
        "memory_delete",
        "consent_withdraw"
      ],
      "properties": {
        "ayla_delete": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "ok",
            "detail"
          ],
          "properties": {
            "ok": {
              "type": "boolean"
            },
            "detail": {
              "type": "string",
              "enum": [
                "deleted",
                "already_deleted",
                "subject_gone",
                "not_linked"
              ]
            }
          }
        },
        "memory_delete": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "ok",
            "detail"
          ],
          "properties": {
            "ok": {
              "type": "boolean"
            },
            "detail": {
              "type": "string",
              "enum": [
                "deleted",
                "already_deleted",
                "not_linked"
              ]
            }
          }
        },
        "consent_withdraw": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "ok",
            "detail"
          ],
          "properties": {
            "ok": {
              "type": "boolean"
            },
            "detail": {
              "type": "string",
              "enum": [
                "withdrawn",
                "already_withdrawn",
                "not_linked"
              ]
            }
          }
        }
      }
    },
    "retainedItem": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "category",
        "reason",
        "lawful_basis",
        "retention_until",
        "decision_status",
        "restrictions",
        "owner",
        "deletion_trigger"
      ],
      "properties": {
        "category": {
          "type": "string",
          "enum": [
            "audit_trail",
            "consent_history",
            "statutory_record",
            "backup",
            "tombstone",
            "other"
          ]
        },
        "reason": {
          "type": "string",
          "enum": [
            "regulatory_audit",
            "withdrawal_evidence",
            "statutory_retention",
            "backup_window",
            "lawful_basis_other"
          ]
        },
        "lawful_basis": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "retention_until": {
          "oneOf": [
            {
              "type": "string",
              "format": "date-time"
            },
            {
              "type": "null"
            }
          ]
        },
        "decision_status": {
          "type": "string",
          "enum": [
            "owner_decision_required",
            "approved"
          ]
        },
        "restrictions": {
          "type": "string",
          "enum": [
            "no_personal_values",
            "read_only",
            "access_role_restriction"
          ]
        },
        "owner": {
          "type": "string"
        },
        "deletion_trigger": {
          "type": "string",
          "enum": [
            "legal_retention_expiry",
            "backup_expiry",
            "owner_decision"
          ]
        }
      }
    },
    "error": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "code",
        "message",
        "retryable"
      ],
      "properties": {
        "code": {
          "type": "string",
          "enum": [
            "upstream_timeout",
            "upstream_unavailable",
            "upstream_error",
            "upstream_malformed",
            "rate_limited",
            "auth_invalid",
            "init_data_expired",
            "subject_mismatch",
            "confirmation_expired",
            "replay_detected",
            "cross_tenant_violation",
            "schema_mismatch",
            "contract_violation",
            "internal_error"
          ]
        },
        "message": {
          "type": "string"
        },
        "retryable": {
          "type": "boolean"
        }
      }
    }
  },
  "type": "object",
  "additionalProperties": false,
  "required": [
    "operation_id",
    "status",
    "format_version",
    "error"
  ],
  "properties": {
    "operation_id": {
      "oneOf": [
        {
          "type": "string",
          "format": "uuid"
        },
        {
          "type": "null"
        }
      ]
    },
    "status": {
      "type": "string",
      "enum": [
        "failed"
      ]
    },
    "format_version": {
      "type": "string",
      "enum": [
        "1.0"
      ]
    },
    "error": {
      "$ref": "#/$defs/error"
    }
  }
}
```
### 5.5 Delete success schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$defs": {
    "subject": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "ayla_user_id",
        "bot_user_id"
      ],
      "properties": {
        "ayla_user_id": {
          "oneOf": [
            {
              "type": "string",
              "format": "uuid"
            },
            {
              "type": "null"
            }
          ]
        },
        "bot_user_id": {
          "type": "string",
          "format": "uuid"
        }
      }
    },
    "perStepResults": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "ayla_delete",
        "memory_delete",
        "consent_withdraw"
      ],
      "properties": {
        "ayla_delete": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "ok",
            "detail"
          ],
          "properties": {
            "ok": {
              "type": "boolean"
            },
            "detail": {
              "type": "string",
              "enum": [
                "deleted",
                "already_deleted",
                "subject_gone",
                "not_linked"
              ]
            }
          }
        },
        "memory_delete": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "ok",
            "detail"
          ],
          "properties": {
            "ok": {
              "type": "boolean"
            },
            "detail": {
              "type": "string",
              "enum": [
                "deleted",
                "already_deleted",
                "not_linked"
              ]
            }
          }
        },
        "consent_withdraw": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "ok",
            "detail"
          ],
          "properties": {
            "ok": {
              "type": "boolean"
            },
            "detail": {
              "type": "string",
              "enum": [
                "withdrawn",
                "already_withdrawn",
                "not_linked"
              ]
            }
          }
        }
      }
    },
    "retainedItem": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "category",
        "reason",
        "lawful_basis",
        "retention_until",
        "decision_status",
        "restrictions",
        "owner",
        "deletion_trigger"
      ],
      "properties": {
        "category": {
          "type": "string",
          "enum": [
            "audit_trail",
            "consent_history",
            "statutory_record",
            "backup",
            "tombstone",
            "other"
          ]
        },
        "reason": {
          "type": "string",
          "enum": [
            "regulatory_audit",
            "withdrawal_evidence",
            "statutory_retention",
            "backup_window",
            "lawful_basis_other"
          ]
        },
        "lawful_basis": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "retention_until": {
          "oneOf": [
            {
              "type": "string",
              "format": "date-time"
            },
            {
              "type": "null"
            }
          ]
        },
        "decision_status": {
          "type": "string",
          "enum": [
            "owner_decision_required",
            "approved"
          ]
        },
        "restrictions": {
          "type": "string",
          "enum": [
            "no_personal_values",
            "read_only",
            "access_role_restriction"
          ]
        },
        "owner": {
          "type": "string"
        },
        "deletion_trigger": {
          "type": "string",
          "enum": [
            "legal_retention_expiry",
            "backup_expiry",
            "owner_decision"
          ]
        }
      }
    },
    "error": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "code",
        "message",
        "retryable"
      ],
      "properties": {
        "code": {
          "type": "string",
          "enum": [
            "upstream_timeout",
            "upstream_unavailable",
            "upstream_error",
            "upstream_malformed",
            "rate_limited",
            "auth_invalid",
            "init_data_expired",
            "subject_mismatch",
            "confirmation_expired",
            "replay_detected",
            "cross_tenant_violation",
            "schema_mismatch",
            "contract_violation",
            "internal_error"
          ]
        },
        "message": {
          "type": "string"
        },
        "retryable": {
          "type": "boolean"
        }
      }
    }
  },
  "type": "object",
  "additionalProperties": false,
  "required": [
    "operation_id",
    "status",
    "format_version",
    "subject",
    "completed_at",
    "per_step_results",
    "deleted",
    "retained"
  ],
  "properties": {
    "operation_id": {
      "type": "string",
      "format": "uuid"
    },
    "status": {
      "type": "string",
      "enum": [
        "completed"
      ]
    },
    "format_version": {
      "type": "string",
      "enum": [
        "1.0"
      ]
    },
    "subject": {
      "$ref": "#/$defs/subject"
    },
    "completed_at": {
      "type": "string",
      "format": "date-time"
    },
    "per_step_results": {
      "$ref": "#/$defs/perStepResults"
    },
    "deleted": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "ayla_personal_context",
          "memory_green"
        ]
      }
    },
    "retained": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/retainedItem"
      }
    }
  }
}
```
### 5.6 Delete partial schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$defs": {
    "subject": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "ayla_user_id",
        "bot_user_id"
      ],
      "properties": {
        "ayla_user_id": {
          "oneOf": [
            {
              "type": "string",
              "format": "uuid"
            },
            {
              "type": "null"
            }
          ]
        },
        "bot_user_id": {
          "type": "string",
          "format": "uuid"
        }
      }
    },
    "perStepResults": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "ayla_delete",
        "memory_delete",
        "consent_withdraw"
      ],
      "properties": {
        "ayla_delete": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "ok",
            "detail"
          ],
          "properties": {
            "ok": {
              "type": "boolean"
            },
            "detail": {
              "type": "string",
              "enum": [
                "deleted",
                "already_deleted",
                "subject_gone",
                "not_linked"
              ]
            }
          }
        },
        "memory_delete": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "ok",
            "detail"
          ],
          "properties": {
            "ok": {
              "type": "boolean"
            },
            "detail": {
              "type": "string",
              "enum": [
                "deleted",
                "already_deleted",
                "not_linked"
              ]
            }
          }
        },
        "consent_withdraw": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "ok",
            "detail"
          ],
          "properties": {
            "ok": {
              "type": "boolean"
            },
            "detail": {
              "type": "string",
              "enum": [
                "withdrawn",
                "already_withdrawn",
                "not_linked"
              ]
            }
          }
        }
      }
    },
    "retainedItem": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "category",
        "reason",
        "lawful_basis",
        "retention_until",
        "decision_status",
        "restrictions",
        "owner",
        "deletion_trigger"
      ],
      "properties": {
        "category": {
          "type": "string",
          "enum": [
            "audit_trail",
            "consent_history",
            "statutory_record",
            "backup",
            "tombstone",
            "other"
          ]
        },
        "reason": {
          "type": "string",
          "enum": [
            "regulatory_audit",
            "withdrawal_evidence",
            "statutory_retention",
            "backup_window",
            "lawful_basis_other"
          ]
        },
        "lawful_basis": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "retention_until": {
          "oneOf": [
            {
              "type": "string",
              "format": "date-time"
            },
            {
              "type": "null"
            }
          ]
        },
        "decision_status": {
          "type": "string",
          "enum": [
            "owner_decision_required",
            "approved"
          ]
        },
        "restrictions": {
          "type": "string",
          "enum": [
            "no_personal_values",
            "read_only",
            "access_role_restriction"
          ]
        },
        "owner": {
          "type": "string"
        },
        "deletion_trigger": {
          "type": "string",
          "enum": [
            "legal_retention_expiry",
            "backup_expiry",
            "owner_decision"
          ]
        }
      }
    },
    "error": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "code",
        "message",
        "retryable"
      ],
      "properties": {
        "code": {
          "type": "string",
          "enum": [
            "upstream_timeout",
            "upstream_unavailable",
            "upstream_error",
            "upstream_malformed",
            "rate_limited",
            "auth_invalid",
            "init_data_expired",
            "subject_mismatch",
            "confirmation_expired",
            "replay_detected",
            "cross_tenant_violation",
            "schema_mismatch",
            "contract_violation",
            "internal_error"
          ]
        },
        "message": {
          "type": "string"
        },
        "retryable": {
          "type": "boolean"
        }
      }
    }
  },
  "type": "object",
  "additionalProperties": false,
  "required": [
    "operation_id",
    "status",
    "format_version",
    "subject",
    "completed_at",
    "per_step_results",
    "completed_steps",
    "failed_steps",
    "retryable",
    "request_attempt",
    "execution_attempt",
    "retained",
    "next_action"
  ],
  "properties": {
    "operation_id": {
      "type": "string",
      "format": "uuid"
    },
    "status": {
      "type": "string",
      "enum": [
        "partial"
      ]
    },
    "format_version": {
      "type": "string",
      "enum": [
        "1.0"
      ]
    },
    "subject": {
      "$ref": "#/$defs/subject"
    },
    "completed_at": {
      "type": "string",
      "format": "date-time"
    },
    "per_step_results": {
      "$ref": "#/$defs/perStepResults"
    },
    "completed_steps": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "ayla_delete",
          "memory_delete",
          "consent_withdraw"
        ]
      }
    },
    "failed_steps": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "ayla_delete",
          "memory_delete",
          "consent_withdraw"
        ]
      }
    },
    "retryable": {
      "type": "boolean"
    },
    "request_attempt": {
      "type": "integer",
      "minimum": 1
    },
    "execution_attempt": {
      "type": "integer",
      "minimum": 1
    },
    "retained": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/retainedItem"
      }
    },
    "next_action": {
      "type": "string",
      "enum": [
        "retry_by_user",
        "contact_support"
      ]
    }
  }
}
```
### 5.7 Delete failure schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$defs": {
    "subject": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "ayla_user_id",
        "bot_user_id"
      ],
      "properties": {
        "ayla_user_id": {
          "oneOf": [
            {
              "type": "string",
              "format": "uuid"
            },
            {
              "type": "null"
            }
          ]
        },
        "bot_user_id": {
          "type": "string",
          "format": "uuid"
        }
      }
    },
    "perStepResults": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "ayla_delete",
        "memory_delete",
        "consent_withdraw"
      ],
      "properties": {
        "ayla_delete": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "ok",
            "detail"
          ],
          "properties": {
            "ok": {
              "type": "boolean"
            },
            "detail": {
              "type": "string",
              "enum": [
                "deleted",
                "already_deleted",
                "subject_gone",
                "not_linked"
              ]
            }
          }
        },
        "memory_delete": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "ok",
            "detail"
          ],
          "properties": {
            "ok": {
              "type": "boolean"
            },
            "detail": {
              "type": "string",
              "enum": [
                "deleted",
                "already_deleted",
                "not_linked"
              ]
            }
          }
        },
        "consent_withdraw": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "ok",
            "detail"
          ],
          "properties": {
            "ok": {
              "type": "boolean"
            },
            "detail": {
              "type": "string",
              "enum": [
                "withdrawn",
                "already_withdrawn",
                "not_linked"
              ]
            }
          }
        }
      }
    },
    "retainedItem": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "category",
        "reason",
        "lawful_basis",
        "retention_until",
        "decision_status",
        "restrictions",
        "owner",
        "deletion_trigger"
      ],
      "properties": {
        "category": {
          "type": "string",
          "enum": [
            "audit_trail",
            "consent_history",
            "statutory_record",
            "backup",
            "tombstone",
            "other"
          ]
        },
        "reason": {
          "type": "string",
          "enum": [
            "regulatory_audit",
            "withdrawal_evidence",
            "statutory_retention",
            "backup_window",
            "lawful_basis_other"
          ]
        },
        "lawful_basis": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "retention_until": {
          "oneOf": [
            {
              "type": "string",
              "format": "date-time"
            },
            {
              "type": "null"
            }
          ]
        },
        "decision_status": {
          "type": "string",
          "enum": [
            "owner_decision_required",
            "approved"
          ]
        },
        "restrictions": {
          "type": "string",
          "enum": [
            "no_personal_values",
            "read_only",
            "access_role_restriction"
          ]
        },
        "owner": {
          "type": "string"
        },
        "deletion_trigger": {
          "type": "string",
          "enum": [
            "legal_retention_expiry",
            "backup_expiry",
            "owner_decision"
          ]
        }
      }
    },
    "error": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "code",
        "message",
        "retryable"
      ],
      "properties": {
        "code": {
          "type": "string",
          "enum": [
            "upstream_timeout",
            "upstream_unavailable",
            "upstream_error",
            "upstream_malformed",
            "rate_limited",
            "auth_invalid",
            "init_data_expired",
            "subject_mismatch",
            "confirmation_expired",
            "replay_detected",
            "cross_tenant_violation",
            "schema_mismatch",
            "contract_violation",
            "internal_error"
          ]
        },
        "message": {
          "type": "string"
        },
        "retryable": {
          "type": "boolean"
        }
      }
    }
  },
  "type": "object",
  "additionalProperties": false,
  "required": [
    "operation_id",
    "status",
    "format_version",
    "error"
  ],
  "properties": {
    "operation_id": {
      "oneOf": [
        {
          "type": "string",
          "format": "uuid"
        },
        {
          "type": "null"
        }
      ]
    },
    "status": {
      "type": "string",
      "enum": [
        "failed"
      ]
    },
    "format_version": {
      "type": "string",
      "enum": [
        "1.0"
      ]
    },
    "error": {
      "$ref": "#/$defs/error"
    }
  }
}
```
### 5.8 Error taxonomy

| Error class | External HTTP | External body `code` | Internal classification | Retryable | When |
|---|---|---|---|---|---|
| timeout | 504 | `upstream_timeout` | `upstream_timeout` | yes | upstream deadline exceeded |
| upstream network error | 502 | `upstream_unavailable` | `upstream_unavailable` | yes | transport-level failure |
| upstream 5xx | 502 | `upstream_error` | `upstream_error` | yes | upstream returned 5xx |
| upstream malformed response | 502 | `upstream_malformed` | `upstream_malformed` | yes | upstream body does not match contract |
| invalid internal credential | 500 | `internal_error` | `security_incident:internal_credential_failure` | no (alert first) | bearer/permission failure; triggers security alert |
| invalid init data signature | 401 | `auth_invalid` | `auth_invalid` | no | MaxInitData signature/tamper check failed |
| init data expired | 401 | `init_data_expired` | `init_data_expired` | no | MaxInitData older than `max_init_data_age` |
| subject mismatch | 403 | `subject_mismatch` | `subject_mismatch` | no | request subject ≠ authenticated subject |
| schema mismatch | 500 | `schema_mismatch` | `schema_mismatch` | no | contract version/schema conflict |
| contract violation | 500 | `contract_violation` | `contract_violation` | no | invariant broken |
| cross-tenant violation | 403 | `cross_tenant_violation` | `cross_tenant_violation` | no | subject accessed from wrong tenant context |
| replay | 409 | `replay_detected` | `replay_detected` | no | reused nonce/idempotency key with different scope |
| rate limit | 429 | `rate_limited` | `rate_limited` | yes | too many requests |
| confirmation expired | 403 | `confirmation_expired` | `confirmation_expired` | no | step-up challenge TTL exceeded |

**Norm:** запрещено правило «любая upstream-ошибка → 502» без
machine-readable `code`, и запрещено раскрытие внешнему клиенту деталей
внутренних security-инцидентов.

---

## 6. subject_gone

- **Implemented fact:** W2 endpoint `DELETE /api/v1/internal/users/{ayla_user_id}/personal-data/`
  currently returns HTTP 404 with body `{"code":"NOT_FOUND","message":"User not found."}`
  (`users/personal_data_api.py:53-58`).
- **Proposed norm:** after amendment W2 must return HTTP 404 with the closed body
  below when the subject is missing or soft-deleted:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": false,
  "required": ["code", "subject"],
  "properties": {
    "code": {"type": "string", "enum": ["subject_gone"]},
    "subject": {
      "type": "object",
      "additionalProperties": false,
      "required": ["ayla_user_id", "bot_user_id"],
      "properties": {
        "ayla_user_id": {"oneOf": [{"type": "string", "format": "uuid"}, {"type": "null"}]},
        "bot_user_id": {"type": "string", "format": "uuid"}
      }
    }
  }
}
```

- `subject_gone` is a **semantic success code**, not an `error.code`. It means the
  subject has no personal context to delete.
- W3 maps `subject_gone` to `per_step_results.ayla_delete.ok=true` with
  `detail="subject_gone"` and returns a completed delete response with empty
  `deleted[]`.
- A bare HTTP 404 is **not** treated as semantic success. It is classified as
  `upstream_error` / `contract_violation` and remains retryable.
- W3 validates `subject` correlation before treating the response as gone.
- `subject_gone` is idempotent: repeated requests return the same code.
- Implementation delta: AMD020-DEL-005.

---

## 7. Retention Manifest

Delete-ответ содержит `retained[]`. Каждый элемент:

| Field | Type | Meaning |
|---|---|---|
| `category` | string | audit_trail, consent_history, statutory_record, backup, tombstone, other |
| `reason` | string | regulatory_audit, withdrawal_evidence, statutory_retention, backup_window, lawful_basis_other |
| `lawful_basis` | string\|null | основание по 152-ФЗ, если утверждено |
| `retention_until` | string\|null | ISO timestamp; `null` если TBD |
| `decision_status` | string | `owner_decision_required` или `approved` |
| `restrictions` | string | no_personal_values, read_only, access_role_restriction |
| `owner` | string | владелец класса данных |
| `deletion_trigger` | string | legal_retention_expiry, backup_expiry, owner_decision |

**Retained items for pilot:**

1. Bot-audit records (`privacy.personal_data_exported`,
   `privacy.personal_data_deleted`) — retention TBD; `decision_status: owner_decision_required`.
2. Ayla-audit records (`AnalyticsEvent`) — retention TBD; `decision_status: owner_decision_required`.
3. Tombstones (`MemoryEntry` soft-deleted rows) — until `primary_purge_deadline`;
   `decision_status: owner_decision_required` until Legal confirms retention.
4. Consent records — retained as withdrawal evidence; retention TBD;
   `decision_status: owner_decision_required`.

**Example (non-normative placeholder):**

```json
{
  "category": "audit_trail",
  "reason": "regulatory_audit",
  "lawful_basis": null,
  "retention_until": null,
  "decision_status": "owner_decision_required",
  "restrictions": "no_personal_values",
  "owner": "Legal/Privacy",
  "deletion_trigger": "legal_retention_expiry"
}
```

---

## 8. Auth, Replay Protection and Step-up

### 8.1 Three separate mechanisms

| Mechanism | Purpose | Layer |
|---|---|---|
| `Idempotency-Key` | Application-level guarantee: одинаковые клиентские retry не приводят к повторной destructive execution | Request handling |
| `nonce` / confirmation challenge | Security replay protection: одноразовый токен подтверждения destructive операции | Step-up authentication |
| `correlation_id` | Observability and cross-system tracing; не является защитой | Logging/audit |

### 8.2 Controls

| Control | Proposed value | Status |
|---|---|---|
| `max_init_data_age` | 5 minutes | owner_decision_required |
| `step-up authentication` | destructive operation requires explicit confirmation challenge | implementation_delta |
| `confirmation challenge TTL` | 5 minutes | owner_decision_required |
| `destructive nonce` | one-time token for delete confirmation | implementation_delta |
| `rate limit` | 5 delete attempts / 15 min / subject; 20 export / 15 min / subject | owner_decision_required |
| `session/device binding` | operation tied to current `BotUser` + channel session | implementation_delta |
| `relink behavior` | delete operation aborted if `ayla_user_id` changes mid-flight; retry after relink uses new subject correlation | implementation_delta |
| `cross-user / cross-tenant checks` | subject from auth must match requested resource; tenant scoping enforced | implementation_delta |
| `PII in URL/query string/logs/metrics/traces` | forbidden; acceptance test required | implementation_delta |
| `secure export file delivery` | JSON attachment with `Content-Disposition`; no persistent URL | implemented_fact (headers); implementation_delta (filename pattern) |

**Fail-closed rule:** если step-up authentication отключён, недоступен или
misconfigured, destructive endpoint недоступен. Запрещён fallback на
аутентификацию только по MaxInitData. Feature flag может отключить весь endpoint,
но не может ослабить обязательную защиту endpoint.

### 8.3 PII-in-URL rule

- **Public W4/W3 endpoints:** subject identifier не передаётся в URL; субъект
  определяется из аутентификации (`request.bot_user`).
- **Internal W3→W2 endpoint:** текущий контракт использует `{ayla_user_id}` в
  пути (`/api/v1/internal/users/{ayla_user_id}/personal-data/`). Это
  implementation gap AMD020-DEL-009: либо заменить на opaque request-scoped
  token, либо применить строгую санитизацию access logs/traces и ограничить
  доступ по internal network.
- **Query string:** передача ПД в query string запрещена.
- **Access logs / traces:** subject IDs sanitized или заменены HMAC-дайджестом.

### 8.4 Safe logging rule

Разрешено логировать:

- `operation_id`;
- `correlation_id`;
- технический `result_code` / `error_code`;
- псевдонимизированный subject reference (например, HMAC-дайджест), только если
  operational correlation необходим.

Запрещено логировать:

- `ayla_user_id` в plaintext;
- `bot_user_id` в plaintext;
- phone, email, name, `MemoryEntry.content`, `ConsentRecord` payload;
- полный export response body.

### 8.5 Secure export file delivery

- **Implemented fact:** W3 view `personal_data_export` (`apps/miniapp_api/views.py:1618-1640`)
  возвращает `JsonResponse(payload)` с заголовком
  `Content-Disposition: attachment; filename="personal-data-export.json"`.
  The response is generated on demand; no persistent download URL is created.
- **Implementation delta:** filename must include only the generation date and
  must not contain the subject identifier (e.g. `ayla-personal-data-{YYYY-MM-DD}.json`).
  Current code uses a generic filename without a date.

### 8.6 Export authentication policy

Export is privacy-sensitive but **not destructive**. Therefore the required
authentication assurance is lower than for delete:

| Control | Export | Delete |
|---|---|---|
| `MaxInitData` freshness | required | required |
| Session/device binding | required | required |
| Cross-user/cross-tenant checks | required | required |
| Step-up confirmation challenge | **not required** by default | required |
| Destructive nonce | not applicable | required |
| Rate limit | required (separate value) | required |

- First export and repeated exports both require fresh `MaxInitData` and a valid
  session; the operation is authorized for the authenticated subject only.
- An owner MAY configure step-up for export via feature flag, but this is not
  the default pilot behavior.
- Export after a completed delete must return empty personal-context data
  (`ayla.personal_context: null`, `memory: []`).

---

## 9. Audit Retention

| audit_event | purpose | contains_personal_data | pseudonymization | access_roles | deletion_exception | owner | current_status |
|---|---|---|---|---|---|---|---|
| `privacy.personal_data_exported` | record export request and scope | yes (subject reference) | HMAC token (direct internal identifier only where operational correlation is required and access is restricted) | W3 ops, Legal/Privacy | statutory request | Legal/Privacy | owner_decision_required |
| `privacy.personal_data_deleted` | record delete request, steps, outcome | yes (subject reference; values excluded) | HMAC token (direct internal identifier only where operational correlation is required and access is restricted) | W3 ops, Legal/Privacy | statutory request | Legal/Privacy | owner_decision_required |
| `memory.forget_entry` | per-entry deletion | yes (user_id reference) | HMAC token (direct internal identifier only where operational correlation is required and access is restricted) | W3 ops | statutory request | W3 | owner_decision_required |
| `memory.forget_all_requested` | mass-erasure intent | yes (user_id reference) | HMAC token (direct internal identifier only where operational correlation is required and access is restricted) | W3 ops | statutory request | W3 | owner_decision_required |
| `AnalyticsEvent` (Ayla) | W2 internal deletion audit | yes (user_id reference) | HMAC token (direct internal identifier only where operational correlation is required and access is restricted) | W2 ops | statutory request | W2 | owner_decision_required |

**Norm:** `user_id`/`bot_user_id` являются персональными/псевдонимизированными
данными и не могут считаться безопасной неперсональной metadata. До утверждения
Legal/Privacy retention и lawful basis readiness gate считается незакрытым.

### 9.1 Legacy audit cleanup

The retention policy applies to **all** audit rows, including legacy rows
written before activation of AMD-020 v0.6.

| Aspect | Required behavior |
|---|---|
| Scope | All audit tables listed above; rows without `retention_until` or classification must be backfilled or marked `owner_decision_required`. |
| Retention start | For legacy rows use `created_at` if present; rows without `created_at` require manual inventory and owner decision before cleanup. |
| Statutory hold | Rows under statutory hold are exempt from deletion; hold list is maintained by Legal/Privacy and must be loaded into the cleanup job. |
| Dry-run mode | Every cleanup job run starts with `dry_run=true`; the report lists rows that would be deleted and held rows preserved. |
| Execution approval | Transition from dry-run to real deletion requires written approval from Legal/Privacy and a logged approval ticket. |
| Batch limits | Each deletion batch is bounded (default 1000 rows) and resumes from a persisted cursor. |
| Idempotency | Re-running the cleanup with the same cursor and parameters is idempotent; already-deleted rows are skipped. |
| Evidence | W6 scenario 38 validates both dry-run and execution phases. |

---

## 10. Consent History in Export

### 10.1 Implemented fact

Существующие поля `ConsentRecord` (подтверждено кодом
`apps/identity/services/privacy.py:148-157`):

```json
{
  "consent_type": "<string>",
  "granted": "<bool>",
  "document_version": "<string>",
  "source": "<string>",
  "captured_at": "<timestamp>",
  "withdrawn_at": "<timestamp|null>"
}
```

### 10.2 Proposed contract

Для соответствия ст. 9 152-ФЗ (конкретное, предметное, информированное,
сознательное, однозначное согласие) export должен содержать:

| Field | Status | Source |
|---|---|---|
| `purpose` | implementation_delta | not present in current model |
| `data_categories` | implementation_delta | not present |
| `operator` | implementation_delta | not present |
| `recipients` | implementation_delta | not present |
| `term` | implementation_delta | not present |
| `lawful_basis` | implementation_delta | not present |
| `document_version` | implemented_fact | present |
| `identification_method` | implementation_delta | not present |

**Legacy record policy:** Before activation, every existing `ConsentRecord` row
must be backfilled with the expanded fields. If source data is unavailable, use
sentinel values:

| Field | Sentinel value for legacy rows |
|---|---|
| `purpose` | `"pre_amd020_legacy"` |
| `data_categories` | `[]` |
| `operator` | `"unknown"` |
| `recipients` | `[]` |
| `term` | `"unknown"` |
| `lawful_basis` | `null` |
| `identification_method` | `"unknown"` |

A boolean `legacy_record` flag may be stored to distinguish pre-amendment rows.
`enforcement_status: Effective` is blocked until the backfill migration is
verified and the export schema's `required` fields are satisfied for 100% of
rows. W6 scenario 39 validates the backfill.

### 10.3 ConsentRecord delete semantics (AMD020-CONSENT-001)

**Status:** `proposed_norm_pending_owner_confirmation`. The withdrawal semantics
below are architecturally fixed, but physical retention, pseudonymization method,
lawful basis and cleanup of legacy rows require Legal/Privacy/Security decisions.

- **Withdrawal:** при delete все активные `ConsentRecord` для person получают
  `withdrawn_at` timestamp. Row **не удаляется** физически.
- **Retained fields:** `consent_type`, `granted`, `document_version`, `source`,
  `captured_at`, `withdrawn_at`, псевдонимизированный subject reference.
- **Removed fields:** нет отдельного payload для удаления; сама запись является
  audit trail.
- **Physical deletion:** governed by the separate audit-retention policy; cannot
  be implemented until Legal approves retention period, lawful basis and
  pseudonymization method.
- **Relink:** consent history привязана к `BotUser`; при relink новые
  `BotUser` получают новую историю, старая остаётся у прежнего `BotUser` и
  удаляется в рамках удаления того persona.

---

## 11. Acceptance №6

Пользователь может самостоятельно экспортировать и удалить данные, входящие в
утверждённый Personal Context pilot scope. Операция проверяется end-to-end.
Она не является полным удалением аккаунта, исчерпывающим удалением всех
персональных данных Ayla или формальным ответом на запрос субъекта по статье 14
152-ФЗ.

---

## 12. Implementation Readiness Gate

До `enforcement_status: Effective` запрещено заявлять соответствие endpoint
требованиям AMD-020 v0.6.

| # | Gate item | Normative status | Implementation status | Evidence owner | Activation blocker |
|---|---|---|---|---|---|
| 1 | Delete barrier | proposed_norm | not implemented | W3 | yes |
| 2 | Block new records during operation | proposed_norm | not implemented | W3 | yes |
| 3 | Block inference/derived writes during operation | proposed_norm | not implemented | W3 | yes |
| 4 | Stable operation_id | proposed_norm | not implemented | W3 | yes |
| 5 | scope_hash | proposed_norm | not implemented | W3 | yes |
| 6 | Idempotency key handling | proposed_norm | not implemented | W3 | yes |
| 7 | Concurrent delete joins active operation | proposed_norm | not implemented | W3 | yes |
| 8 | Replay / lost-response handling | proposed_norm | not implemented | W3 | yes |
| 9 | W2 returns subject_gone code | proposed_norm | not implemented | W2 | yes |
| 10 | Closed response schemas (JSON Schema) | proposed_norm | not implemented | W2/W3 | yes |
| 11 | Upstream timeouts + error taxonomy | proposed_norm | partially implemented | W2/W3 | yes |
| 12 | Soft-delete → purge → hard-delete SLA | proposed_norm | not implemented | W3 | yes |
| 13 | Postgres cleanup | proposed_norm | partially implemented (soft-delete exists) | W3 | yes |
| 14 | Redis cleanup | proposed_norm | not applicable_pending_inventory_evidence | W3 | no |
| 15 | Derived cleanup | proposed_norm | partially implemented (read-gate) | W3 | yes |
| 16 | Step-up authentication | proposed_norm | not implemented | W4/W3 | yes |
| 17 | Destructive nonce | proposed_norm | not implemented | W3 | yes |
| 18 | Challenge TTL | proposed_norm | not implemented | W3 | yes |
| 19 | Replay protection | proposed_norm | not implemented | W3 | yes |
| 20 | Audit retention approved | owner_decision_required | pending Legal | Legal/Privacy | yes |
| 21 | W6 acceptance battery passed | proposed_norm | pending W6 | W6 | yes |
| 22 | Code version recorded | proposed_norm | pending | W3 | yes |
| 23 | Export filename pattern | proposed_norm | implementation_delta | W3 | no |
| 24 | Export operation/auth/schema/failure handling | proposed_norm | not implemented | W3 | yes |
| 25 | ConsentRecord expanded-field backfill verified | implementation_delta | not implemented | W3 | yes |

Effective разрешается только после:

- `implementation_status: Verified`;
- полного W6 evidence;
- фиксации версии кода;
- owner activation decision;
- установки `effective_from`.

---

## 13. W6 Acceptance Battery

**Status definitions:**

- `SPECIFIED` — test case documented, preconditions/action/expected result are unambiguous, but implementation and execution are pending.
- `IMPLEMENTED` — test automation exists, but has not been executed against the current build.
- `EXECUTED_PASS` — test executed and passed.
- `EXECUTED_FAIL` — test executed and failed.
- `BLOCKED` — test cannot be implemented/executed until an external decision (owner/Legal/Privacy/Security) or a code delta is available.
- `NOT_APPLICABLE` — test does not apply to the current pilot scope; reason recorded.

| # | Test ID | Scenario | Expected result | Evidence owner | Status | Blocker / note |
|---|---|---|---|---|---|---|
| 1 | AMD020-W6-001 | Concurrent delete | Second request joins the active operation and receives the same `operation_id`; no second destructive execution is created | W6 | SPECIFIED | — |
| 2 | AMD020-W6-002 | Retry after lost success-response | Repeat with same `idempotency_key` returns the final completed/partial status without a new `execution_attempt` | W6 | SPECIFIED | — |
| 3 | AMD020-W6-003 | W2 ayla_delete step failure | HTTP 502 with `status: partial`; `failed_steps` contains `ayla_delete`; `memory_delete` and `consent_withdraw` completed | W6 | SPECIFIED | — |
| 4 | AMD020-W6-004 | Overall deadline between steps | HTTP 504 with `error.code: upstream_timeout`; no partial success returned to client | W6 | SPECIFIED | — |
| 5 | AMD020-W6-005 | Schema mismatch | HTTP 500 with `error.code: schema_mismatch` | W6 | SPECIFIED | — |
| 6 | AMD020-W6-006 | Malformed upstream response | HTTP 502 with `error.code: upstream_malformed` | W6 | SPECIFIED | — |
| 7 | AMD020-W6-007 | Relinking during deletion | Operation is aborted with `error.code: subject_mismatch`; a new operation is required after relink | W6 | SPECIFIED | — |
| 8 | AMD020-W6-008 | Cross-tenant access | HTTP 403 with `error.code: cross_tenant_violation` | W6 | SPECIFIED | — |
| 9 | AMD020-W6-009 | Write UserPersonalContext after barrier | New W2 `UserPersonalContext` row is rejected while the delete operation is active | W6 | SPECIFIED | — |
| 10 | AMD020-W6-010 | Write MemoryEntry after barrier | New green `MemoryEntry` is rejected while the delete operation is active | W6 | SPECIFIED | — |
| 11 | AMD020-W6-011 | Create ConsentRecord after barrier | New `ConsentRecord` is rejected while the delete operation is active | W6 | SPECIFIED | — |
| 12 | AMD020-W6-012 | Inference job after barrier | Inference job that would create green `MemoryEntry` is blocked while the delete operation is active | W6 | SPECIFIED | — |
| 13 | AMD020-W6-013 | Hard purge MemoryEntry | Soft-deleted `MemoryEntry` row is physically removed after `soft_delete_retention` | W6 | BLOCKED | Legal/Privacy must confirm `soft_delete_retention` and hard-delete deadline |
| 14 | AMD020-W6-014 | Physical wipe UserPersonalContext | `UserPersonalContext` row is removed from W2 primary store immediately on delete | W6 | BLOCKED | Owner/Legal must confirm physical wipe as canonical semantics |
| 15 | AMD020-W6-015 | ConsentRecord withdrawal and retention | Active consents receive `withdrawn_at`; rows remain as audit trail | W6 | BLOCKED | Legal/Privacy must confirm retention period, lawful basis, and pseudonymization method |
| 16 | AMD020-W6-016 | Redis cleanup | No Redis keys for included classes are found in read/write path; Redis inventory is documented | W6 | NOT_APPLICABLE | No Redis usage in included-class read/write path per §2.1 inventory |
| 17 | AMD020-W6-017 | Derived/cache/index cleanup | In-memory prompt block no longer surfaces deleted facts | W6 | SPECIFIED | — |
| 18 | AMD020-W6-018 | Retained manifest | Delete response `retained[]` lists every retained category with reason and `decision_status` | W6 | SPECIFIED | — |
| 19 | AMD020-W6-019 | Audit correlation | All audit rows for the operation share `operation_id` and `correlation_id` | W6 | SPECIFIED | — |
| 20 | AMD020-W6-020 | PII in URL/logs/metrics/traces | No plaintext `ayla_user_id`, `bot_user_id`, phone, email, name, `MemoryEntry.content`, or export body in inspected sinks | W6 | SPECIFIED | Internal W3→W2 URL decision (AMD020-DEL-009) may affect evidence |
| 21 | AMD020-W6-021 | Export of another user | HTTP 403 with `error.code: subject_mismatch` | W6 | SPECIFIED | — |
| 22 | AMD020-W6-022 | Stale initData | HTTP 401 with `error.code: init_data_expired` | W6 | SPECIFIED | — |
| 23 | AMD020-W6-023 | Expired confirmation challenge | HTTP 403 with `error.code: confirmation_expired` | W6 | SPECIFIED | — |
| 24 | AMD020-W6-024 | Nonce reuse | HTTP 409 with `error.code: replay_detected` | W6 | SPECIFIED | — |
| 25 | AMD020-W6-025 | Export after delete | Export returns `ayla.personal_context: null` and `memory: []`; `consents` contains only withdrawn history | W6 | SPECIFIED | — |
| 26 | AMD020-W6-026 | Repeat delete after completion | HTTP 200 delete success response with `status: completed`, empty `deleted[]`, `retained[]` listing audit/consent items, and `per_step_results` showing `already_deleted` / `already_withdrawn` detail codes | W6 | SPECIFIED | — |
| 27 | AMD020-W6-027 | Partial recovery | Retry after upstream recovery completes all remaining steps and returns HTTP 200 `status: completed` | W6 | SPECIFIED | — |
| 28 | AMD020-W6-028 | Backup expiry | After `backup_expiry`, backups no longer contain deleted primary data | W6 | BLOCKED | SRE/Legal must confirm backup retention SLA |
| 29a | AMD020-W6-029a | Operation recovery after process crash — resumable | Operation resumes from last persisted state and completes all remaining steps | W6 | SPECIFIED | — |
| 29b | AMD020-W6-029b | Operation recovery after process crash — unrecoverable | Operation transitions to terminal `failed` state; barrier is released only after terminal state and incident record; subsequent idempotent request returns HTTP 502 `status: failed` with `failed_steps` listing incomplete steps | W6 | SPECIFIED | — |
| 30 | AMD020-W6-030 | Stuck operation — authorized terminal abort | Two authorized operators (W3 on-call + Security) approve abort with reason code and incident ticket; operation moves to terminal `aborted`; barrier released only after terminal state; audit event `privacy.delete_aborted` is written | W6 | SPECIFIED | — |
| 31 | AMD020-W6-031 | Scope mismatch with same idempotency key | HTTP 409 with `error.code: replay_detected` | W6 | SPECIFIED | — |
| 32 | AMD020-W6-032 | Different idempotency keys for same active operation | Both requests join the same `operation_id`; no second destructive execution | W6 | SPECIFIED | — |
| 33 | AMD020-W6-033 | Export delivery headers | HTTP 200 with `Content-Disposition: attachment; filename="ayla-personal-data-YYYY-MM-DD.json"` where `YYYY-MM-DD` is the generation date in UTC; no persistent URL | W6 | SPECIFIED | — |
| 34 | AMD020-W6-034 | No subject ID in access logs | No plaintext `ayla_user_id`, `bot_user_id`, phone, email, or name in access logs, traces, or metrics for the operation; pseudonymization uses HMAC digest if present | W6 | SPECIFIED | Internal W3→W2 URL decision (AMD020-DEL-009) may affect evidence |
| 35 | AMD020-W6-035 | Export schema versioning — producer | W3 rejects a response that contains unknown top-level fields for `format_version: "1.0"` | W6 | SPECIFIED | — |
| 36 | AMD020-W6-036 | Partial export failure | HTTP 502 with `error.code: upstream_unavailable`; no partial JSON body is returned | W6 | SPECIFIED | — |
| 37 | AMD020-W6-037 | Fail-closed step-up unavailable | Delete is rejected with HTTP 500 `error.code: internal_error`; no fallback to MaxInitData-only auth | W6 | BLOCKED | Security/owner must confirm fail-closed policy and alert severity before execution |
| 38a | AMD020-W6-038a | Legacy audit cleanup — dry-run | Retention cleanup job in `dry_run=true` mode reports expired rows that would be deleted and held rows preserved; no rows are deleted | W6 | BLOCKED | Legal/Privacy must approve dry-run report format and retention schedule |
| 38b | AMD020-W6-038b | Legacy audit cleanup — execution | After Legal/Privacy approval, retention cleanup job deletes expired rows and preserves rows under statutory hold; idempotent re-run deletes no additional rows | W6 | BLOCKED | Legal/Privacy written approval required before execution |
| 39 | AMD020-W6-039 | Expanded consent history in export | After backfill, export `consents[]` includes `purpose`, `data_categories`, `operator`, `recipients`, `term`, `lawful_basis`, and `identification_method` for every record; legacy rows use sentinel values defined in §10.2 | W6 | BLOCKED | Legal must approve consent text/lawful basis; W3 must verify backfill before execution |
| 40 | AMD020-W6-040 | Green MemoryEntry delete step failure | HTTP 502 with `status: partial`; `failed_steps` contains `memory_delete`; `ayla_delete` and `consent_withdraw` completed | W6 | SPECIFIED | — |
| 41 | AMD020-W6-041 | ConsentRecord withdraw step failure | HTTP 502 with `status: partial`; `failed_steps` contains `consent_withdraw`; `ayla_delete` and `memory_delete` completed | W6 | SPECIFIED | — |

**Battery summary:** 43 scenario rows; 0 implemented; 0 executed; 7 blocked; 1 not applicable; 35 specified. No scenario is claimed as passing.

---

## 14. Open Questions and Known Conflicts

**Удалена фраза «конфликтов не обнаружено».**

| issue | source | impact | classification | owner | required decision | blocks document approval? | blocks operational activation? |
|---|---|---|---|---|---|---|---|
| UserPersonalContext delete semantics | Owner feedback v0.3; code inspection W2 | Physical wipe is implemented, but owner confirmation and backup tracking are pending | `proposed_norm_pending_owner_confirmation` | W2/Product/Legal | Confirm physical wipe as canonical semantics; approve backup tracking | yes | yes |
| ConsentRecord retention/redaction/pseudonymization | Owner feedback v0.3; code inspection W3 | Withdrawal is implemented; physical retention policy is missing | `proposed_norm_pending_owner_confirmation` | Legal/Privacy/Security | Retention period, lawful basis, pseudonymization method, key management, legacy cleanup, statutory hold handling | yes | yes |
| Operator/processor roles | P1.6 | formal 152-ФЗ roles | `owner_decision_required` | Legal | operator/processor designation | yes | yes |
| Retention audit-records | P1.8 | lawful_basis and retention_until TBD | `owner_decision_required` | Legal/Privacy | retention table + lawful basis; legacy cleanup; dry-run policy | no | yes |
| Hard-delete deadline | P0.4 | 30-day proposal needs Legal confirmation | `owner_decision_required` | Legal/Privacy | confirm/reject 30d | no | yes |
| Backup expiry | P0.4 | depends on backup policy | `owner_decision_required` | SRE/Legal | backup retention SLA | no | yes |
| Timeout values | v0.1 §3.8 | 10s/25s design candidates | `owner_decision_required` | W3/SRE | confirm timeouts | no | yes |
| Consent history fields | P1.7 | purpose/recipients/term/etc. | `implementation_delta` | W3/Legal | schema + lawful basis text | no | yes |
| Step-up/auth values | P0.6 | max_init_data_age, challenge TTL, rate limits | `owner_decision_required` | W4/W3/Security | confirm values; fail-closed policy | no | yes |
| HMAC/pseudonymization method | Owner feedback v0.3 | audit subject references | `implementation_delta` | W3/Security | choose HMAC/key management | no | yes |
| Internal W3→W2 URL with ayla_user_id | Owner feedback v0.3 | PII in URL | `implementation_delta` | W2/W3 | AMD020-DEL-009: opaque token or sanitization | no | yes |
| Handoff scope conflicts | 16 handoff files (§1.4) | OP6 / account-deletion promises exceed AMD-020 pilot boundary | `owner_decision_required` | Owner / Product / Legal / OP6 track | Reconcile customer-facing «delete all my data» copy with narrow AMD-020 scope | yes | no |
| Formal Article 14 response | P0.2 | excluded from AMD-020; separate post-pilot track | `external_obligation` | Product/Legal | scope decision in separate track | no | no |
| Full account deletion | P0.1 | excluded from AMD-020; separate post-pilot track | `external_obligation` | Product Architecture | separate track | no | no |

---

## 15. Traceability

| Norm / fix | Source requirement | AMD-020 section | Implementation Amendment norm ID | Evidence |
|---|---|---|---|---|
| Narrow pilot scope + 4 disclaimers | Owner ruling (Режим 2+), P0.1 | Title, §0, §1 | — | owner_verdict_amd020_v01_2026-07-23.md §2 |
| Included registry | Owner ruling, P0.1 | §1.1 | — | owner_verdict_amd020_v01_2026-07-23.md §2 |
| Excluded registry to handoffs | Owner feedback v0.3 | §1.2, §1.3 | — | `2026-05-17-conversations-handoff.md` §7; `2026-05-18-customer-first-time-handoff.md` §12 F4; `2026-05-18-loyalty-system-handoff.md` §14; `2026-05-18-marketing-campaigns-handoff.md` §6; `2026-05-18-master-mobile-handoff.md` §13 E17; `2026-05-19-master-admin-internal-chat-handoff.md` §2.1, §8.5; `2026-05-19-master-device-reauth-handoff.md` §9.1; `2026-05-19-master-offboarding-handoff.md` §2.4, §6.4; `2026-05-19-master-reviews-feedback-handoff.md` §2.10, §7.1, §7.2; `2026-05-19-wellness-sleep-handoff.md` §11.4; architecture maps used only as supplementary index |
| Derived boundary all 3 classes | Owner ruling, P0.4 | §2 | AMD020-DER-001 | code inspection SHA `3697034f` |
| UserPersonalContext delete semantics | Owner feedback v0.3 | §3.2, §3.4 | AMD020-DEL-008 | `users/personal_data_api.py:147-152`, `users/models.py:425-544` |
| ConsentRecord retention semantics | Owner feedback v0.3 | §10.3 | AMD020-CONSENT-001 | `apps/consent/models.py:56-183` |
| Operation vs per-class state | Owner feedback v0.3 | §3.1, §3.2 | AMD020-DEL-001 | owner feedback 2026-07-23 |
| Delete barrier | Owner ruling, P0.5 | §3.3 | AMD020-DEL-001 | owner_verdict_amd020_v01_2026-07-23.md §2 |
| Hard-delete lifecycle | Owner ruling, P0.4 | §3.4 | AMD020-DEL-002 | owner_verdict_amd020_v01_2026-07-23.md §2 |
| operation_id | Owner ruling, P1.3 | §4.1 | AMD020-DEL-003 | owner_verdict_amd020_v01_2026-07-23.md §2 |
| scope_hash | Owner feedback v0.3 | §4.2 | AMD020-DEL-003 | owner feedback 2026-07-23 |
| Idempotency mechanics | Owner ruling, P1.4 | §4.3 | AMD020-DEL-003 | owner_verdict_amd020_v01_2026-07-23.md §2 |
| Concurrent delete joins | Owner feedback v0.3 | §4.3 | AMD020-DEL-003 | owner feedback 2026-07-23 |
| Relink abort | Owner ruling | §4.3 | AMD020-DEL-003 | owner_verdict_amd020_v01_2026-07-23.md §2 |
| Closed response schemas | Owner ruling, P1.2; owner feedback v0.3 | §5 | AMD020-DEL-004 | owner_verdict_amd020_v01_2026-07-23.md §2; owner feedback 2026-07-23 |
| Error taxonomy | Owner ruling, P1.1; owner feedback v0.3 | §5.6 | AMD020-DEL-004 | owner_verdict_amd020_v01_2026-07-23.md §2; owner feedback 2026-07-23 |
| subject_gone | Owner ruling, P1.5 | §6 | AMD020-DEL-005 | owner_verdict_amd020_v01_2026-07-23.md §2 |
| Retention manifest | Owner ruling, P0.3 | §7 | AMD020-DEL-006 | owner_verdict_amd020_v01_2026-07-23.md §2 |
| Auth/replay/step-up | Owner ruling, P0.6 | §8 | AMD020-DEL-007 | owner_verdict_amd020_v01_2026-07-23.md §2 |
| Separate idempotency/nonce/correlation | Owner feedback v0.3 | §8.1 | AMD020-DEL-007 | owner feedback 2026-07-23 |
| PII-in-URL rule | Owner feedback v0.3 | §8.3 | AMD020-DEL-009 | owner feedback 2026-07-23 |
| Secure export delivery evidence | Owner feedback v0.3 | §8.5 | — | `apps/miniapp_api/views.py:1618-1640` |
| Audit retention table | Owner ruling, P1.8 | §9 | AMD020-AUD-001 | owner_verdict_amd020_v01_2026-07-23.md §2 |
| Consent history split | Owner ruling, P1.7 | §10 | AMD020-EXP-001 | owner_verdict_amd020_v01_2026-07-23.md §2 |
| Acceptance №6 wording | Owner ruling | §11 | — | owner_verdict_amd020_v01_2026-07-23.md §2 |
| Readiness Gate | Owner ruling | §12 | — | owner_verdict_amd020_v01_2026-07-23.md §2 |
| W6 battery | Owner ruling, P1.10; owner feedback v0.3 | §13 | — | owner_verdict_amd020_v01_2026-07-23.md §2; owner feedback 2026-07-23 |
| Remove «no conflicts» | Owner verdict | §14 | — | owner_verdict_amd020_v01_2026-07-23.md §1 |
| Post-pilot tracks as external obligation | Owner feedback v0.2 | §14 | — | owner feedback 2026-07-23 |

---

## 16. Differences v0.1 → v0.2 → v0.3 → v0.4 → v0.5

| area | v0.1 | v0.2 | v0.3 | v0.4 | v0.5 | reason |
|---|---|---|---|---|---|---|
| Title | «C5 Personal Data Export/Delete (152-ФЗ)» | «C5 Pilot Personal Context Export/Forget Contract» | same | same | same | Honest scope boundary |
| Disclaimers | absent | 4 explicit | same | same | same | Prevent overclaim |
| Scope registry | implicit | included + excluded tables | same | split implementation status per class | excluded sources replaced with exact 16 handoff files; conflicts table added | Owner feedback v0.4 review |
| Derived boundary | not covered | MemoryEntry only | all 3 classes | all 3 classes + evidence queries | same + stronger evidence note | Owner feedback v0.3 |
| UserPersonalContext delete semantics | physical wipe stated | mixed with tombstone | mixed with tombstone | explicit per-class physical wipe + backup tracking | marked `proposed_norm_pending_owner_confirmation`; lifecycle clarified | v0.4 review |
| ConsentRecord semantics | withdraw retained | same | same | explicit AMD020-CONSENT-001 with retention/redaction | marked `proposed_norm_pending_owner_confirmation`; retention decisions open | v0.4 review |
| Operation vs per-class state | not defined | 6 states mixed | 6 states mixed | separate operation state + per-class state | `accepted` redefined as internal pre-commit; first observable state is `blocked` | v0.4 review |
| Concurrent delete | not defined | queue | queue | joins active operation | same | Owner feedback v0.3 |
| scope_hash | not defined | not defined | BotUser.id + idempotency_key | subject_ref + tenant_ref + included_classes + contract_version + link_generation | same | Owner feedback v0.3 |
| Response schemas | partial | examples with `...` | examples with `...` | JSON Schema 2020-12 with additionalProperties:false | Self-contained root schemas; local `$ref` resolvable; `profile` removed; `subject_gone` formalized | v0.5/v0.6 review |
| subject_gone | 404 interpreted | contradiction | implemented/proposed split | explicit fact + proposed norm | same; code fence fixed | v0.4 review |
| Retention manifest | absent | `retained[]` | fake date example | `null` + `owner_decision_required` | same | Owner feedback v0.2/v0.3 |
| Auth/step-up | MaxInitData only | full controls | same | separate idempotency/nonce/correlation | fail-closed rule added; feature flag cannot weaken auth | v0.4 review |
| PII-in-URL | not covered | forbidden but allowed ayla_user_id logging | forbidden but internal URL gap | explicit public/internal rule + DEL-009 | same | Owner feedback v0.3 |
| Audit retention | TBD | structured table | contains_personal_data: no | contains_personal_data: yes + HMAC note | same | Owner feedback v0.3 |
| Error taxonomy | basic | machine codes | internal credential as auth_invalid | internal credential as security incident + safe external code | `init_data_expired` added; upstream codes in failure schema | v0.4 review |
| Idempotency | conceptual | request/execution attempt | request/execution attempt | scope_hash + join behavior | same | Owner feedback v0.3 |
| Readiness gate | minimal | 21 items | 21 items (claimed 13) | 22 items, correctly counted | 25 items; synchronized between AMD-020 and Amendment; export and backfill gates added | v0.5/v0.6 review |
| W6 battery | minimal | 23 scenarios | same | 39 scenarios | 43 scenario rows; ambiguous cases split; one expected result per scenario; Test ID + Status columns added | v0.5/v0.6 review |
| Quality Bar table | absent | absent | absent | included in document | re-graded with honest PASS/FAIL/BLOCKED; no PASS as Draft | v0.4 review |

---

## 17. Document Quality Bar Self-Review

| bar item | PASS/FAIL/BLOCKED/PARTIAL | evidence | document section | unresolved action |
|---|---|---|---|---|
| A1 Честность scope | PASS | Title matches scope; included/excluded/handoff analysis tables; `profile` removed from export; split implementation status; conflicts table | §0, §1, §1.3, §1.4 | — |
| A2 «полный/complete» | PASS | Title changed; 4 explicit disclaimers | §0 | — |
| A3 «конфликтов не обнаружено» | PASS | Removed; replaced with issues/conflicts tables | §14 | — |
| A4 Норма = факт или design candidate | PASS | Implemented/proposed/owner_decision labels; no overclaim | all | — |
| B1 Статьи замаплены | PASS | ст. 14, 21, 9; Article 14 explicitly excluded | §0, §1.2, §10 | — |
| B2 Portability ≠ formal response | PASS | Explicit distinction | §0, §1.2 | — |
| B3 Оператор/обработчик | **FAIL** | Left as owner decision | §14 | Legal must designate before canonicalization |
| B4 Retained-классы | PARTIAL | Retention manifest + audit table; several `retention_until: null` pending Legal | §7, §9 | Legal/Privacy must approve retention periods |
| C1 Auth/replay/step-up | **BLOCKED** | Fail-closed rule added, but numerical values and production readiness require Security/owner decision | §8.2 | Security/owner must confirm step-up is fail-closed and values |
| C2 Error taxonomy | PASS | Machine codes; security incident internal; `init_data_expired` separated from `auth_invalid` | §5.6, §5.8 | — |
| C3 ПД в URL/logs/metrics/traces | PARTIAL | Safe-logging rule + PII-in-URL rule; internal W3→W2 URL still an implementation gap | §8.3, §8.4 | DEL-009: choose opaque token or sanitization |
| C4 404 ≠ semantic success | **PASS** | `subject_gone` code defined; generic 404 is treated as `upstream_error`/`contract_violation` in both AMD-020 §6 and Amendment §3/DEL-005 | §6; Amendment DEL-005 | — |
| D1 Гонки / barrier | **BLOCKED** | Barrier + concurrent join defined; atomic operation creation is `implementation_delta` | §3.1, §3.3, §4.3 | Implement single-transaction operation+lock+barrier before activation |
| D2 Идемпотентность механика | PASS | scope_hash, request/execution attempt, replay read | §4 | — |
| D3 Полный lifecycle | **BLOCKED** | UPC physical wipe and ConsentRecord retention are `proposed_norm_pending_owner_confirmation` | §3.2, §3.4, §10.3 | Owner/Legal must confirm UPC wipe and consent retention |
| D4 Retention manifest | PASS | `retained[]` with `decision_status` | §7 | — |
| E1 Closed schemas | **PASS** | Schemas use `$defs`; recursive `$ref` fixed; failure enum matches taxonomy; `personal_context` and `MemoryEntry.content` are intentionally declared `opaque_payload`; producer/consumer contract is explicit | §5.1, §5.3 | — |
| E2 operation_id/correlation | PASS | Defined; scope_hash added | §4 | — |
| F1 Acceptance battery | PARTIAL | 43 scenario rows; Test ID + Status columns (SPECIFIED/BLOCKED/NOT_APPLICABLE) added; no false PASS; previously ambiguous cases split; each scenario has one expected result; some scenarios still depend on unresolved decisions | §13 | Finalize decisions blocking C1/D3 before W6 run |
| G1 Нет открытых decisions при сдаче | **FAIL** | Multiple owner/legal/security decisions remain open | §14 | Resolve blocker decisions before final approval |
| G2 Validation | PASS | Repository validator: 0 errors, warnings ≤ baseline | — | Re-run after edits |
| G3 Отчёт по форме | PASS | This section + final agent report | §17 | — |
| H Cross-document consistency | **PASS** | Amendment v0.6 synchronized: 25 readiness-gate items match; generic 404 fallback removed; step-up fail-closed; export backlog added; atomic operation creation and `aborted` state aligned; open questions cleaned | AMD-020 §6, §8.2, §12; Amendment §2, §3, DEL-005, DEL-007, EXP-002…EXP-005 | — |
| I Implementation evidence | PARTIAL | Pinned commit SHAs and reproducible grep commands added for Redis/cache/derived inventory; code evidence cited for key facts; backup evidence and full W6 evidence still pending | §2.1, §2.2, §8.5 | Collect W6 evidence and backup inventory after implementation |
| J Writing precision | **PARTIAL** | Code-fence issue fixed; most ambiguous W6 results corrected; `subject_gone` formalized; remaining precision depends on owner decisions and final implementation evidence | §5, §6, §13 | Finalize owner decisions and re-verify after implementation |

**Итог Quality Bar:** FAIL/BLOCKED по пунктам B3, C1, D1, D3, G1; PARTIAL по B4, C3, F1, I, J.
Документ остаётся Draft/Proposed/Blocked. После v0.6 пакет готов к
**техническому повторному ревью**, но **не** к structured owner decision review,
final owner approval, canonicalization или operational activation.

---

## 18. Change Log

### v0.6 — 2026-07-23

- Добавлена §1.4 — полная handoff scope analysis по всем 16 файлам.
- JSON Schema исправлена: каждая root schema самодостаточна, `$ref` разрешаются
  локально; `profile` удалён из export (вне pilot scope).
- `subject_gone` формализован как отдельная закрытая schema.
- Operation state machine дополнен terminal state `aborted`; добавлено explicit
  mapping `partially_completed` → external `status: partial`.
- Barrier release разрешён только после terminal state; break-glass procedure
  определена.
- Relink lifecycle и судьба старой persona описаны в §4.4.
- ConsentRecord legacy backfill policy и sentinel values определены в §10.2.
- Readiness gates синхронизированы между AMD-020 и Amendment (25 items).
- Open Questions очищены от уже выполненных decomposition tasks.
- Legacy audit cleanup specification расширена (§9.1).
- W6 battery дополнена: однозначные expected results, сценарии 38a/38b, 40, 41; добавлены Test ID и Status (SPECIFIED/BLOCKED/NOT_APPLICABLE) без ложных PASS.
- Export authentication policy выделена отдельно (§8.6).
- Physical/derived inventory дополнена воспроизводимыми командами и результатами.
- Quality Bar пересчитана; document status остаётся Draft/Proposed/Blocked.

### v0.5 — 2026-07-23

- Excluded scope registry переписана с точными ссылками на 16 handoff-файлов;
  добавлена таблица известных конфликтов с OP6/account-deletion scope.
- Исправлено противоречие между `accepted` и atomic barrier creation:
  `accepted` — внутреннее состояние, первое внешнее состояние — `blocked`.
- UserPersonalContext delete semantics и ConsentRecord retention помечены как
  `proposed_norm_pending_owner_confirmation`.
- JSON Schema переписана через `$defs`; исправлены рекурсивные `$ref`;
  добавлен export failure schema; failure enum синхронизирован с taxonomy;
  `personal_context` и `MemoryEntry.content` явно объявлены `opaque_payload`.
- Добавлен fail-closed rule для step-up authentication.
- W6 battery: неоднозначные сценарии разделены/исправлены; ожидаемые результаты
  стали однозначными.
- Quality Bar self-review пересчитана честно: FAIL/BLOCKED по открытым решениям
  и несинхронизированным местам.
- Implementation Amendment v0.5 синхронизирован (generic 404 fallback удалён,
  step-up fail-closed, export backlog дополнен).

### v0.4 — 2026-07-23

- Исправлена единая delete-семантика UserPersonalContext (physical wipe + backup
  tracking, AMD020-DEL-008).
- Добавлена отдельная норма ConsentRecord withdrawal/retention
  (AMD020-CONSENT-001).
- Разделены operation state и per-class state.
- Concurrent delete: queue → join active operation.
- Добавлен канонический `scope_hash`.
- Response schemas переписаны как JSON Schema 2020-12 с
  `additionalProperties: false`.
- Разделены idempotency, nonce replay protection и correlation.
- Добавлен explicit PII-in-URL rule с DEL-009 для internal W3→W2 endpoint.
- Добавлены evidence для secure export delivery.
- Исправлена audit inventory: `contains_personal_data: yes`.
- Расширен derived inventory evidence для всех трёх классов.
- Scope Registry: split implementation status.
- W6 battery расширена до 38 сценариев.
- Добавлена таблица отличий v0.1→v0.2→v0.3→v0.4.
- Добавлена построчная Quality Bar self-review в документ.

### v0.3 — 2026-07-23

- Исправлены критические замечания v0.2.

### v0.2 — 2026-07-23

- Первая переработка после owner verdict.

### v0.1 — 2026-07-23

- Initial draft (rejected; see owner verdict).

---

**Конец документа — AMD-020 v0.6 (Draft, pending owner approval)**
