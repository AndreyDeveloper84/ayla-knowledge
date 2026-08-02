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
version: "0.8"
canonical_status: draft
review_status: pending_technical_re_review
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
updated: 2026-07-24
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
| Version | 0.8 (2026-07-24) |
| Review status | pending_technical_re_review |

**Owner ruling:** Режим 2+ — двухступенчатая канонизация. Настоящий документ
подготовлен для повторного технического ревью. Перевод в structured owner
decision review, final owner approval, Canonical/Accepted или operational
activation до прохождения технического ревью запрещён.

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
  отображается как `status: "partial"`. Barrier остаётся активным; automatic
  release запрещён.
- `completed` — каскад завершён успешно; все included-классы обработаны.
  Barrier может быть снят, т.к. per-class lifecycle (soft-delete → purge,
  withdrawal → retention) продолжается под контролем отдельных state machines.
- `failed` — каскад завершён с не-retryable ошибкой; terminal operation state.
  **Barrier НЕ снимается автоматически.** Система обязана либо достичь
  `deletion_converged`, либо создать и успешно завершить
  `recovery_purge_operation`, либо установить `subject_suppression` до снятия
  barrier.
- `aborted` — операция прервана авторизованным break-glass, relink или
  неисправимым сбоем; terminal operation state. **Barrier НЕ снимается
  автоматически.** Применяются те же convergence/recovery/suppression правила,
  что и для `failed`.
- `deletion_converged` — **внутреннее состояние достижения безопасности**:
  для каждого included-класса подтверждено, что он находится в целевом
  терминальном per-class состоянии (`deleted`, `primary_purged`, `withdrawn`)
  либо явно перечислен в `retained[]` с корректным `decision_status`. Это
  состояние является **единственным основанием** для безопасного снятия barrier.
- `recovery_pending` — **внутреннее состояние**: принято решение о необходимости
  recovery; barrier активен; идёт подготовка (allocating `operation_id`, lease,
  authorization) к запуску `recovery_purge_operation`.
- `recovery_processing` — **внутреннее состояние**: recovery purge operation
  выполняет оставшиеся destructive шаги; barrier активен.
- `recovery_failed` — **внутреннее состояние**: recovery operation завершилась
  terminal `failed`. Barrier **сохраняется**; `deletion_converged` **не**
  устанавливается. Система обязана запустить bounded retry / новую recovery
  operation или эскалировать инцидент. Снятие barrier без достижения
  `deletion_converged` запрещено.
- `subject_suppression` — **внутреннее состояние**: установлена persistent
  subject-level tombstone, которая блокирует создание новых included-записей
  для данного субъекта до достижения `deletion_converged`. Может использоваться
  как временная мера, если recovery операция не может быть запущена немедленно.
  См. формальный контракт в §3.7.

**State-to-response mapping:**

| Internal operation state | External response `status` | HTTP |
|---|---|---|
| `blocked` | `accepted` (or `blocked` in status read) | 202 |
| `processing` | `processing` | 202 |
| `partially_completed` | `partial` | 502 |
| `completed` | `completed` | 200 |
| `failed` | `failed` | 502/504/500 |
| `aborted` | `failed` or `aborted`* | 502/500 |
| `recovery_pending` / `recovery_processing` / `recovery_failed` | `failed` or `aborted` | 502/500 |
| `subject_suppression` | `failed` or `aborted` | 502/500 |

`*` `aborted` may be exposed as a dedicated external `status` only after owner
approval of the break-glass/relink semantics. Until then, external responses use
`failed` with `error.code: subject_mismatch` / `internal_error`.

**Atomicity requirement:** operation record + scope lock + barrier activation
are created in a single database transaction. If the transaction fails, the
client receives an error and no `operation_id`. There is no externally
observable window between `operation_id` issuance and barrier activation.

**Safe-outcome invariant (barrier release rule):**

```text
safe_outcome ⇔ (
    operation.state == completed
) OR (
    recovery_operation.state == completed
    AND post_recovery_inventory_sweep == clean
    AND every_included_class ∈ {deleted, primary_purged, withdrawn} ∪ retained[]
    AND deletion_converged == true
)
```

- Barrier снимается **только после** `deletion_converged`.
- Для `completed` безопасный исход наступает сразу (per-class lifecycle
  управляется отдельно).
- Для `failed`/`aborted` система обязана:
  1. Выполнить inventory sweep.
  2. Если остатков нет — установить `deletion_converged` и снять barrier.
  3. Если остатки есть — создать `recovery_purge_operation`, перевести parent
     operation в `recovery_processing`; barrier остаётся активным.
  4. Если recovery завершилась `failed` — оставаться в `recovery_failed`,
     сохранить barrier, запустить bounded retry / новую recovery или
     эскалировать инцидент; `deletion_converged` не устанавливать.
  5. Если recovery не может быть запущена немедленно — установить
     `subject_suppression` tombstone (§3.7) и запланировать recovery с
     отслеживаемым deadline; barrier остаётся активным.
- Automatic release after partial, failed recovery, or unrecoverable failure
  without `deletion_converged` is **prohibited**.
- Повторный failure recovery operation должен иметь определённый lifecycle:
  bounded retry count, exponential backoff with cap, incident escalation after
  max retries, mandatory human review before any manual barrier release.

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
  ├──► partially_completed  ← есть failed steps; retryable; barrier active
  │      │
  │      ├──► retry  → processing
  │      │
  │      └──► max retries / unrecoverable → failed  (terminal operation)
  │
  ├──► completed  ← все шаги успешны (terminal operation)
  │         │
  │         └──► per-class lifecycle продолжается независимо:
  │                UserPersonalContext: deleted → backup_expired
  │                MemoryEntry: soft_deleted → primary_purged → backup_expired
  │                ConsentRecord: withdrawn → retained_under_other_basis
  │         │
  │         └──► barrier released (safe outcome: completed)
  │
  └──► aborted  ← break-glass / relink / authorized terminal abort
            │     (terminal operation; barrier stays)
            ▼
      convergence gate (barrier still active)
            │
            ├──► inventory sweep clean
            │         │
            │         └──► deletion_converged ──► barrier released
            │
            ├──► residual data found
            │         │
            │         ├──► recovery_pending
            │         │         │
            │         │         ▼
            │         ├──► recovery_processing
            │         │         │
            │         │         ├──► recovery completed + post-recovery sweep clean
            │         │         │         │
            │         │         │         └──► deletion_converged ──► barrier released
            │         │         │
            │         │         └──► recovery_failed
            │         │                   │
            │         │                   ├──► bounded retry → recovery_pending
            │         │                   │
            │         │                   └──► max retries / incident escalation
            │         │                         (barrier stays; deletion_converged false)
            │         │
            │         └──► if recovery cannot start immediately:
            │                   subject_suppression tombstone installed
            │                   (barrier stays or atomically handed off)
            │                   └──► recovery_pending when ready
            │
            └──► subject_suppression tombstone as interim guard
                      └──► recovery_pending when recovery becomes possible

Barrier is released only after `deletion_converged`:
- `completed`, or
- `failed`/`aborted` followed by clean inventory sweep, or
- `failed`/`aborted` followed by recovery_purge_operation `completed` AND clean
  post-recovery inventory sweep.

`recovery_failed` is NOT a safe outcome. Barrier stays active until a
subsequent recovery reaches `completed` and a clean sweep confirms
`deletion_converged`, or until incident-driven manual recovery proves
convergence via a documented, two-operator, audited procedure.
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
- Move operation to `aborted` **without releasing the barrier**.
- Do **not** auto-retry the original `aborted` operation; the client must start
  a new delete operation with a new `idempotency_key` after convergence.
- Preserve evidence of completed steps; already-deleted classes remain deleted.
- Immediately enter the **convergence gate** (§3.1):
  - Run an inventory sweep of all included classes and derived stores.
  - If no residual personal-context data is found, transition to
    `deletion_converged` and release the barrier.
  - If residual data is found, create a `recovery_purge_operation` with the
    same `scope_hash` and a new `operation_id`; parent operation enters
    `recovery_processing`; keep the barrier until recovery reaches `completed`
    **and** a post-recovery sweep confirms `deletion_converged`.
  - If recovery completes but the post-recovery sweep finds residual data,
    create a new `recovery_purge_operation`; do not set `deletion_converged`.
  - If recovery fails, transition parent operation to `recovery_failed`;
    barrier stays; trigger bounded retry or incident escalation. A failed
    recovery is never a safe outcome.
  - If recovery cannot start immediately, install a `subject_suppression`
    tombstone (§3.7) that blocks new writes of included classes for the subject
    and schedule recovery with a tracked deadline.
- After abort and before barrier release, **no new write** of any included
  class for the subject is permitted.
- A fresh inventory sweep is mandatory before any new operation on the same
  `scope_hash`.

---

### 3.7 Subject suppression contract

`subject_suppression` — persistent subject-level guard that blocks creation of
new included-class records for a semantic subject when the delete barrier
cannot be held (for example, after a terminal abort, an unrecoverable crash,
or while waiting for a recovery purge operation to start).

#### 3.7.1 Semantics

| Attribute | Normative rule | Deployment decision |
|---|---|---|
| Authoritative storage | Must be a durable, strongly-consistent store shared by all write paths; proposed W3 Postgres table `identity_subject_suppression` | `BLOCKED` — final physical store and owner must be approved by W3/SRE/Security |
| Canonical subject key | Stable `subject_ref` (§4.2) plus `tenant_ref` | derived |
| Tenant boundary | Suppression is scoped per tenant; cross-tenant suppression is prohibited | derived |
| Persona / `link_generation` | Suppression is bound to the current `link_generation`; old `link_generation` values keep their own suppression records | derived |
| Stable identity | Suppression follows the semantic subject, not the technical `scope_hash`; HMAC rotation does not create a new subject | §4.2 |

#### 3.7.2 Lifecycle

1. **Creation:** suppression tombstone is created only from a safe state
   transition: either atomically when handing off from an active barrier, or
   explicitly by incident command after a terminal abort/crash.
2. **Atomic handoff `barrier → suppression`:** when a terminal `aborted`/`failed`
   operation cannot keep the in-process barrier (for example, process crash),
   the system must atomically install a suppression tombstone **before**
   releasing the barrier. There must be no observable window in which neither
   guard is active.
3. **Producer enforcement:** every write path for included classes (W2
   `UserPersonalContext`, W3 `MemoryEntry` writer/inference, W3
   `ConsentRecord`) must check suppression **before** commit. A suppressed
   subject receives `409 Conflict` / `503 Service Unavailable` with audit event
   `privacy.write_blocked_by_suppression`.
4. **Fail-closed on suppression store unavailability:** if the suppression store
   is unreachable, write attempts for included classes must be rejected with
   `503 Service Unavailable` until the store recovers. The system must not
   accept writes without confirming suppression state.
5. **Removal:** suppression is removed only after `deletion_converged` is
   confirmed by an inventory sweep. Removal is itself an audited operation
   `privacy.subject_suppression_removed`.
6. **Relink:** if the subject relinks while suppression is active, the
   suppression record remains tied to the old `link_generation` and old persona.
   The new persona starts with no suppression. The old persona’s suppression
   continues to block writes against the old identity scope until convergence.
7. **HMAC rotation:** because suppression uses stable `subject_ref` and
   `tenant_ref`, key rotation does not change the suppression record. The
   key-ring must resolve the same `subject_ref` for all active key versions
   (§4.2).

#### 3.7.3 Audit events

| Event | When |
|---|---|
| `privacy.subject_suppression_set` | Tombstone installed |
| `privacy.subject_suppression_handoff` | Barrier atomically replaced by suppression |
| `privacy.write_blocked_by_suppression` | Write attempt rejected while suppressed |
| `privacy.subject_suppression_removed` | Tombstone removed after `deletion_converged` |
| `privacy.subject_suppression_store_unavailable` | Suppression store unreachable (incident) |

#### 3.7.4 Incident escalation

If suppression cannot be installed during a required handoff, or if the
suppression store remains unavailable beyond a bounded timeout, the system must:

- emit `security_incident.subject_suppression_failure`;
- page the incident commander and W3/SRE on-call;
- keep the operation/barrier in a safe state (do not release);
- record the incident ticket in the operation record.

---

## 4. operation_id, scope_hash, stable identity and Idempotency

### 4.1 Identifiers

| Field | Purpose | Source | Stability |
|---|---|---|---|
| `operation_id` | Stable end-to-end identifier of one delete/export operation | Generated by W3 at request acceptance | Unique per operation |
| `subject_ref` | Stable pseudonymized semantic subject identifier | HMAC-SHA-256 over normalized (`ayla_user_id`, `bot_user_id`) using a versioned HMAC key | Stable across HMAC key rotations when key-ring resolves old keys |
| `scope_hash` | Technical operation-scope identifier | SHA-256 over canonical JSON of (`subject_ref`, `tenant_ref`, `operation_type`, `included_classes`, `contract_version`, `link_generation`, `hmac_key_version`) | Changes on relink, contract version bump, class-set change, or HMAC key rotation |
| `idempotency_key` | Client-supplied key for safe retry | Miniapp request header (proposed: `Idempotency-Key`) | Client-supplied |
| `correlation_id` | Traces request across W4 → W3 → W2 and audit | Carried in request headers and logs | Per request |
| `request_attempt` | Ordinal of the client HTTP retry | Incremented by W3 for each request with same `idempotency_key` | Per request replay |
| `execution_attempt` | Ordinal of actual execution | Incremented only when a new execution is attempted | Per execution |
| `link_generation` | Monotonic version of BotUser ↔ AylaUser link | Incremented on every relink; never reused | Per persona mapping |
| `hmac_key_version` | Version of the HMAC key used for `subject_ref` | Managed by W3 Security | Key-rotation epoch |

### 4.2 Stable identity vs. technical scope

#### 4.2.1 `subject_ref` — stable semantic identity

`subject_ref` identifies the **semantic subject** (the natural person represented
by the current BotUser↔AylaUser link) independently of technical scope changes.

| Property | Rule |
|---|---|
| Input | Normalized `ayla_user_id` (UUID, lowercase, no braces) + `bot_user_id` (UUID, lowercase, no braces) + `tenant_ref` |
| Algorithm | HMAC-SHA-256 over the canonical concatenation `tenant_ref + ":" + ayla_user_id + ":" + bot_user_id` |
| Output | Lowercase hex string |
| Key version | Explicit `hmac_key_version` recorded with every `subject_ref` |
| Key-ring | W3 Security maintains a key-ring of active and recently retired HMAC keys. The same input must resolve to the same `subject_ref` for all key versions in the ring. |
| Audit use | Only the HMAC digest may be logged; the key must not be derivable from digest or logs. |

#### 4.2.2 `scope_hash` — technical operation scope

`scope_hash` is the technical identifier of an operation scope. It **must not**
be confused with stable identity. Components:

- `subject_ref` — stable HMAC digest (§4.2.1);
- `tenant_ref` — canonical tenant identifier (UUID or normalized slug);
- `operation_type` — `"export"` or `"delete"`;
- `included_classes` — sorted lexicographically canonical class names;
- `contract_version` — AMD-020 version string (e.g., `"0.8"`);
- `link_generation` — current monotonic link generation;
- `hmac_key_version` — key version used for `subject_ref`.

**Canonical serialization (no whitespace, UTF-8, keys sorted):**

```json
{
  "contract_version": "0.8",
  "hmac_key_version": "k3",
  "included_classes": ["ConsentRecord", "MemoryEntry_green", "UserPersonalContext"],
  "link_generation": 3,
  "operation_type": "delete",
  "subject_ref": "<hmac_hex>",
  "tenant_ref": "<tenant_id>"
}
```

**Hash algorithm:**

- Serialize the canonical JSON object with keys sorted lexicographically,
  UTF-8 encoding, no whitespace.
- Compute `SHA-256(serialized_bytes)`.
- Represent the hash as lowercase hexadecimal.

#### 4.2.3 HMAC key rotation

Rotation creates a new `hmac_key_version` and therefore a new `subject_ref` and
`scope_hash`. The following rules prevent two active scopes for the same
semantic subject:

1. **Key-ring lookup:** before accepting a new delete/export request, W3 resolves
   `subject_ref` using all active key versions. If an active operation, barrier,
   or suppression exists for the same semantic subject under any key version,
   the new request must join or be rejected; parallel destructive operations are
   prohibited.
2. **Alias mapping:** idempotency records store the `hmac_key_version` used at
   creation. A lookup by new `scope_hash` must also search aliases generated
   from old key versions for the same semantic subject.
3. **No automatic re-scope:** HMAC rotation does **not** cancel or orphan an
   active operation. The operation continues under its original `scope_hash`;
   new requests for the same subject are routed to it via key-ring resolution.
4. **Old key retirement:** a retired key version may be removed from the ring
   only after all operations scoped with that version have reached a terminal
   state and `deletion_converged`; retention period for old keys is
   `owner_decision_required`.
5. **Fail-closed:** if a request arrives with a key version not present in the
   ring and no alias can be resolved, the request is rejected with
   `internal_error` and a security incident is raised.

#### 4.2.4 Parallel operation prohibition

Only **one active delete operation** may exist for a given semantic subject at a
time. Concurrent requests with equivalent or aliased `scope_hash` join the same
operation. Requests with a different `scope_hash` that resolve to the same
subject (e.g., after HMAC rotation or relink) are handled as follows:

- **Same `link_generation`, different `hmac_key_version`:** join active operation
  (alias match).
- **Higher `link_generation`:** old operation is `aborted` if still active; new
  operation uses new `scope_hash` (§4.4).
- **Lower or reused `link_generation`:** rejected as `replay_detected` /
  `subject_mismatch`.

### 4.3 Idempotency rules

- **Idempotency key scope:** idempotency records are keyed by
  `(scope_hash, idempotency_key)`.
- **Alias lookup:** because HMAC rotation changes `scope_hash`, W3 must also
  search idempotency records by `subject_ref` + `tenant_ref` + `operation_type` +
  `link_generation` across all active key versions. A request with a new
  `scope_hash` but matching semantic subject and `link_generation` joins the
  existing operation; it does not create a second destructive execution.
- **Повторный запрос с тем же `idempotency_key` и эквивалентным `scope_hash`**
  возвращает результат текущего/предыдущего состояния операции.
- **Concurrent delete:** concurrent request с другим `idempotency_key`, но
  совпадающим `scope_hash` (or aliased scope), **joins** активную операцию и
  получает тот же `operation_id`. Вторая destructive execution не создаётся и не
  queued.
- **Relink during deletion:** операция **aborted**; клиент получает
  `subject_mismatch` и должен инициировать новую операцию после relink.
  Полный lifecycle relink описан в §4.4.
- **Retry после потери success-response:** клиент повторяет с тем же
  `idempotency_key`; W3 возвращает финальный результат из idempotency store
  (replay read), не запуская новое execution.
- **Срок хранения idempotency record:** proposed 7 days after operation completion
  (`owner_decision_required`).
- **После завершённой операции:** повторный запрос возвращает `completed_at` и
  финальный `status` без увеличения `execution_attempt`.
- **HMAC rotation during active operation:** the operation continues under its
  original `scope_hash`. New requests for the same subject after rotation are
  resolved via the key-ring and alias mapping and join the active operation.

### 4.4 Relink lifecycle

`scope_hash` включает `link_generation`. `link_generation` — **монотонно
возрастающее** целое число; при каждом relink оно увеличивается. Предыдущие
значения `link_generation` и прежние `scope_hash` никогда не
восстанавливаются, даже если пользователь позже relink'ается обратно на тот
же `Ayla User`. Это предотвращает replay, ошибочное присоединение к старой
операции и смешение idempotency records.

Если связь BotUser ↔ Ayla User меняется во время активной операции:

1. Текущая операция немедленно переходит в terminal state `aborted`.
2. Внешний ответ: `failed` (или `aborted` после owner approval) с
   `error.code: subject_mismatch`.
3. Уже выполненные шаги остаются выполненными; незавершённые шаги отменяются.
4. Barrier **не снимается** автоматически. Система входит в convergence gate
   (§3.1): для старой persona должна быть доказана `deletion_converged`, либо
   создана `recovery_purge_operation`, либо установлена `subject_suppression`
   tombstone.
5. Клиент должен инициировать **новую** операцию с новым `idempotency_key`;
   новый `scope_hash` будет содержать новое (большее) `link_generation`.

**Fate of the old persona:**

- Старая persona (`BotUser` + связанный `Ayla User`) продолжает существовать в
  системе со своей историей согласий, памяти и аудита.
- Пользователь **не теряет** прав на экспорт/удаление данных старой persona.
- Доступ к старой persona и её операциям осуществляется без необходимости
  relink'аться обратно. Нормативный контракт old-persona authorization и
  иллюстративный API path описаны в §4.5. Доступ через OP6 / account-deletion
  track — дополнительная альтернатива, а не единственный путь.
- `ConsentRecord`, `MemoryEntry` и `UserPersonalContext` старой persona не
  мигрируют к новой persona автоматически.
- Если старая persona имеет активное или частично выполненное delete-операцию,
  она **обязана** завершиться до безопасного исхода (§3.1). Orphaned partially
  deleted persona недопустима.

**Relink at each destructive step:**

- `link_generation` проверяется **перед каждым destructive шагом** (ayla_delete,
  memory_delete, consent_withdraw) и **перед каждой derived-write блокировкой**.
- Mismatch на любом шаге немедленно переводит операцию в `aborted` и
  convergence gate.
- Уже выполненные шаги фиксируются в `per_step_results`; незавершённые
  отменяются.

**Export after relink:**

- An in-flight export operation is aborted if relink occurs; the client must
  retry after relink.
- Export, созданный до relink, привязан к старому `scope_hash` и содержит
  данные старой persona.
- Новый export возвращает данные только для текущей persona.
- Старый export artifact не обновляется и не пересоздаётся автоматически;
  retention / deletion старых artifacts определяется отдельной policy.

---

### 4.5 Old-persona authorization contract

After relink, the previous persona (old `BotUser` ↔ old `AylaUser` link) remains
a distinct privacy subject. The user must be able to complete export/delete for
that old persona without reversing the relink.

#### 4.5.1 Normative behavior

| Aspect | Rule | Deployment decision |
|---|---|---|
| Ownership mapping | W3 maintains a durable mapping `current_subject_ref → list[(old_scope_hash, old_link_generation, old_subject_ref)]` | `BLOCKED` — physical schema and retention period must be approved by W3/Security/Legal |
| Authoritative owner | The authenticated owner of the current persona is authorized to access old personas that derive from the same natural person | derived |
| Access without reverse relink | The system must provide at least one mechanism (illustrative API or OP6 track) to list old personas and initiate export/delete for each | derived |
| Cross-tenant isolation | Old persona access is rejected if the current authenticated subject belongs to a different tenant | derived |
| Enumeration protection | Old persona endpoints must not allow enumeration of other users’ personas; responses are scoped to the authenticated owner | derived |
| Consent history | Old persona consent history remains tied to the old `BotUser`; new persona starts with empty consent history | derived |
| Data migration | No automatic migration of `MemoryEntry`, `ConsentRecord`, or `UserPersonalContext` from old to new persona | derived |
| Mapping retention | Ownership mapping retention period is `owner_decision_required`; it must survive at least until all old persona operations reach `deletion_converged` | owner_decision_required |
| HMAC rotation | Mapping stores stable `subject_ref` and `scope_hash`; key-ring resolution (§4.2.3) applies to old persona lookups | derived |
| Revocation | The user may revoke access to an old persona export artifact; revocation does not delete the old persona data | derived |
| Audit | Every old-persona access emits `privacy.old_persona_accessed` with `old_scope_hash`, `old_link_generation`, current `operation_id`, and authorization outcome | derived |

#### 4.5.2 Illustrative API (non-normative path)

```text
GET  /privacy/v1/personas                    # list personas owned by caller
GET  /privacy/v1/personas/{old_scope_hash}/export
POST /privacy/v1/personas/{old_scope_hash}/delete
GET  /privacy/v1/personas/{old_scope_hash}/operations/{operation_id}
```

The exact path is an implementation detail. The normative requirement is that
old persona operations use the same `scope_hash`, `link_generation`, barrier,
suppression, recovery, and schema contracts as current-persona operations.

#### 4.5.3 Errors

| Condition | Response | Audit event |
|---|---|---|
| Old persona not owned by caller | 403 `subject_mismatch` / `cross_tenant_violation` | `privacy.old_persona_access_denied` |
| Old persona mapping corrupted/missing | 500 `internal_error`; incident ticket required | `security_incident.old_persona_mapping_failure` |
| Old persona operation still active after new relink | 409 `operation_in_progress`; caller must wait or abort per §3.6 | `privacy.old_persona_operation_conflict` |

#### 4.5.4 Lifecycle of old persona operations

- An old persona delete operation follows §3.1–§3.7 with the old `scope_hash`.
- It is not blocked by operations on the new persona, and vice versa, except
  that they share the same natural person and therefore must not leak data
  across personas.
- After old persona operation reaches `deletion_converged`, the old barrier /
  suppression may be released; the ownership mapping may be retained per
  retention policy.

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

- Each root schema in §5.3–§5.8 is a self-contained JSON Schema 2020-12 document.
- Shared structures (`subject`, `perStepResults`, `retainedItem`, `error`) are duplicated in every root schema so that all `$ref` resolve within the same document.
- `additionalProperties: false` is enforced at every closed level.
- `personal_context` and `MemoryEntry.content` are intentionally declared `opaque_payload` and are not closed by this contract.
- `subject_gone` is formalized as a separate closed schema in §6.

### 5.3 Export success schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://ayla.knowledge/architecture/amd020/schemas/export-success/1.0",
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
          "identification_method",
          "legacy_record",
          "schema_complete",
          "semantic_complete",
          "legal_validity_status"
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
          },
          "legacy_record": {
            "type": "boolean",
            "description": "true if this record was backfilled from pre-AMD020 storage and may carry sentinel values"
          },
          "schema_complete": {
            "type": "boolean",
            "description": "true if all schema-required fields are populated with non-sentinel values"
          },
          "semantic_complete": {
            "type": "boolean",
            "description": "true if the record's values reflect actual captured consent metadata, not sentinels"
          },
          "legal_validity_status": {
            "type": "string",
            "enum": ["approved", "owner_decision_required", "legacy_unknown"],
            "description": "Legal review status of the consent record; schema-completeness does not imply legal validity"
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
  "$id": "https://ayla.knowledge/architecture/amd020/schemas/export-failure/1.0",
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
  "$id": "https://ayla.knowledge/architecture/amd020/schemas/delete-success/1.0",
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
  "$id": "https://ayla.knowledge/architecture/amd020/schemas/delete-partial/1.0",
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
  "$id": "https://ayla.knowledge/architecture/amd020/schemas/delete-failure/1.0",
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

### 5.8 Operation status-read schema

Status read returns the durable state of an operation. It is the authoritative
source of truth after a timeout, crash, or lost HTTP response.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://ayla.knowledge/architecture/amd020/schemas/operation-status-read/1.0",
  "$defs": {
    "step": {
      "type": "string",
      "enum": ["ayla_delete", "memory_delete", "consent_withdraw"]
    },
    "perStepResult": {
      "type": "object",
      "additionalProperties": false,
      "required": ["ok", "detail"],
      "properties": {
        "ok": {"type": "boolean"},
        "detail": {"type": "string"}
      }
    },
    "error": {
      "type": "object",
      "additionalProperties": false,
      "required": ["code", "message", "retryable"],
      "properties": {
        "code": {"type": "string"},
        "message": {"type": "string"},
        "retryable": {"type": "boolean"}
      }
    }
  },
  "type": "object",
  "additionalProperties": false,
  "required": [
    "operation_id",
    "status",
    "format_version",
    "subject_ref",
    "tenant_ref",
    "link_generation",
    "operation_type",
    "included_classes",
    "barrier_state",
    "suppression_state",
    "deletion_converged",
    "retryable",
    "created_at",
    "updated_at",
    "audit_correlation"
  ],
  "properties": {
    "operation_id": {
      "type": "string",
      "format": "uuid"
    },
    "status": {
      "type": "string",
      "enum": [
        "accepted",
        "blocked",
        "processing",
        "partially_completed",
        "completed",
        "failed",
        "aborted",
        "recovery_pending",
        "recovery_processing",
        "recovery_failed",
        "deletion_converged"
      ]
    },
    "format_version": {
      "type": "string",
      "enum": ["1.0"]
    },
    "subject_ref": {
      "type": "string",
      "description": "HMAC digest of the semantic subject; no plaintext identifiers"
    },
    "tenant_ref": {
      "type": "string"
    },
    "link_generation": {
      "type": "integer",
      "minimum": 0
    },
    "hmac_key_version": {
      "type": "string"
    },
    "operation_type": {
      "type": "string",
      "enum": ["export", "delete"]
    },
    "included_classes": {
      "type": "array",
      "items": {"type": "string"}
    },
    "completed_steps": {
      "type": "array",
      "items": {"$ref": "#/$defs/step"}
    },
    "failed_steps": {
      "type": "array",
      "items": {"$ref": "#/$defs/step"}
    },
    "pending_steps": {
      "type": "array",
      "items": {"$ref": "#/$defs/step"}
    },
    "per_step_results": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "ayla_delete": {"$ref": "#/$defs/perStepResult"},
        "memory_delete": {"$ref": "#/$defs/perStepResult"},
        "consent_withdraw": {"$ref": "#/$defs/perStepResult"}
      }
    },
    "barrier_state": {
      "type": "string",
      "enum": ["active", "released", "handoff_to_suppression", "suppressed"]
    },
    "suppression_state": {
      "type": "string",
      "enum": ["none", "pending", "active"]
    },
    "recovery_operation_id": {
      "oneOf": [
        {"type": "string", "format": "uuid"},
        {"type": "null"}
      ]
    },
    "recovery_state": {
      "oneOf": [
        {
          "type": "string",
          "enum": ["pending", "processing", "completed", "failed"]
        },
        {"type": "null"}
      ]
    },
    "deletion_converged": {
      "type": "boolean"
    },
    "retryable": {
      "type": "boolean"
    },
    "next_action": {
      "type": "string",
      "enum": [
        "wait",
        "retry_by_user",
        "contact_support",
        "start_recovery",
        "none"
      ]
    },
    "created_at": {
      "type": "string",
      "format": "date-time"
    },
    "updated_at": {
      "type": "string",
      "format": "date-time"
    },
    "completed_at": {
      "oneOf": [
        {"type": "string", "format": "date-time"},
        {"type": "null"}
      ]
    },
    "error": {
      "oneOf": [
        {"$ref": "#/$defs/error"},
        {"type": "null"}
      ]
    },
    "audit_correlation": {
      "type": "object",
      "additionalProperties": false,
      "required": ["correlation_id"],
      "properties": {
        "correlation_id": {"type": "string"},
        "parent_operation_id": {
          "oneOf": [
            {"type": "string", "format": "uuid"},
            {"type": "null"}
          ]
        }
      }
    }
  }
}
```

**Semantics:**

- `status` reflects the durable operation state; `accepted` is exposed only in
  status read, not in the initial HTTP response.
- `barrier_state` and `suppression_state` together describe the current guard
  protecting the subject from new writes.
- `deletion_converged` is `true` only when the safe-outcome invariant (§3.1) is
  satisfied.
- `next_action` is advisory; the client may retry only when `retryable` is
  `true`.
- For a recovery operation, `recovery_operation_id` and `recovery_state` are
  populated; the parent operation remains in `recovery_processing` or
  `recovery_failed` until recovery completes and a clean sweep confirms
  convergence.

### 5.9 Error taxonomy

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
  below when the subject is missing or soft-deleted.

W2 is authoritative for `AylaUser`, but it is **not** authoritative for
`BotUser`. Therefore the `subject_gone` response must not require W2 to return
`bot_user_id`; doing so would create a contract that W2 cannot reliably
implement. W3 already knows the requested `bot_user_id` from authentication and
validates correlation.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://ayla.knowledge/architecture/amd020/schemas/subject-gone/1.0",
  "type": "object",
  "additionalProperties": false,
  "required": ["code", "format_version", "subject"],
  "properties": {
    "code": {"type": "string", "enum": ["subject_gone"]},
    "format_version": {"type": "string", "enum": ["1.0"]},
    "subject": {
      "type": "object",
      "additionalProperties": false,
      "required": ["ayla_user_id"],
      "properties": {
        "ayla_user_id": {"oneOf": [{"type": "string", "format": "uuid"}, {"type": "null"}]}
      }
    },
    "correlation_id": {"type": "string"},
    "retryable": {"type": "boolean", "enum": [false]}
  }
}
```

- `subject_gone` is a **semantic success code**, not an `error.code`. It means the
  subject has no personal context to delete.
- `operation_id` is intentionally **not** present: the upstream W2 call is one
  step of a W3-managed operation; `operation_id` is assigned and validated by W3.
- W3 maps `subject_gone` to `per_step_results.ayla_delete.ok=true` with
  `detail="subject_gone"` and returns a completed delete response with empty
  `deleted[]`.
- A bare HTTP 404 is **not** treated as semantic success. It is classified as
  `upstream_error` / `contract_violation` and remains retryable.
- W3 validates `subject.ayla_user_id` correlation before treating the response as
  gone; mismatch returns `subject_mismatch` / `contract_violation`.
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

Export is privacy-sensitive but **not destructive**. The default pilot policy
below is a **proposed technical clarification**, not an approved security
ruling. The final decision (step-up required or not) is `owner_decision_required`
and blocks activation until recorded.

| Control | Export (proposed) | Delete |
|---|---|---|
| `MaxInitData` freshness | required | required |
| Session/device binding | required | required |
| Cross-user/cross-tenant checks | required | required |
| Step-up confirmation challenge | **owner_decision_required** | required |
| Destructive nonce | not applicable | required |
| Rate limit | required (separate value) | required |

- First export and repeated exports both require fresh `MaxInitData` and a valid
  session; the operation is authorized for the authenticated subject only.
- The default pilot behavior **proposes** no step-up for export, but Security/Owner
  must approve this before activation. If approval is denied, export requires the
  same step-up challenge as delete and the export endpoint remains blocked until
  the control is implemented.
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
| `legacy_record` | implementation_delta | not present |
| `schema_complete` | implementation_delta | computed |
| `semantic_complete` | implementation_delta | computed |
| `legal_validity_status` | owner_decision_required | computed |

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

The boolean `legacy_record` flag is **required** for every exported consent
row. It is set to `true` for pre-amendment rows and `false` for rows captured
after activation. `schema_complete: true` means all schema-required fields are
populated with non-sentinel values. `semantic_complete: true` means the values
reflect actual captured consent metadata, not sentinels. `legal_validity_status`
is one of `approved`, `owner_decision_required`, `legacy_unknown` and is set by
Legal/Privacy review, not derived from schema completeness.

`schema_complete: true` does **not** imply legal validity. A legacy row with
sentinel values satisfies the export schema but remains `legacy_record: true`,
`semantic_complete: false`, `legal_validity_status: legacy_unknown`.

`enforcement_status: Effective` is blocked until:

1. The backfill migration is verified;
2. The export schema's `required` fields are satisfied for 100% of rows;
3. A Legal/Privacy review report classifies every row by `legal_validity_status`.

W6 scenario 39 validates the backfill and completeness flags.

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
требованиям AMD-020 v0.8.

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

| # | Test ID | Requirement / defect ref | Scenario | Preconditions | Action | Expected HTTP result | Expected persisted state | Expected barrier state | Expected suppression state | Expected recovery state | Expected audit event | Retryability | Privacy/security invariant | Evidence type | Implementation status | Execution status | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | AMD020-W6-001 | — | Concurrent delete joins active operation | Active delete operation exists for the subject; second request arrives with different idempotency_key but equivalent scope_hash. | Send second delete request. | 202 Accepted (or current operation status). | Single operation record; both requests recorded under same operation_id; execution_attempt unchanged. | Active and unchanged; no second destructive execution created. | N/A | N/A | `privacy.operation_joined` with correlation_id of second request linked to existing operation_id. | yes (idempotent replay) | No concurrent destructive execution for the same scope_hash. | HTTP trace + operation-state query | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 2 | AMD020-W6-002 | — | Retry after lost success-response | Delete operation completed successfully; client did not receive success response. | Repeat request with same idempotency_key and scope_hash. | 200 OK with status `completed`; no new execution_attempt. | operation state remains `completed`; execution_attempt not incremented. | Released (operation reached safe outcome `completed`). | N/A | N/A | Idempotency replay logged; no new `privacy.personal_data_deleted` event. | yes | Identical idempotency_key + scope_hash never triggers second destructive execution. | Replay request + operation log | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 3 | AMD020-W6-003 | — | W2 ayla_delete step failure | Delete operation in `processing`; W2 ayla_delete step fails with upstream 5xx. | Process deletion cascade. | 502 Bad Gateway, status `partial`. | Operation internal state `partially_completed`; failed_steps=[`ayla_delete`]; completed_steps=[`memory_delete`,`consent_withdraw`] (continue-on-error policy: remaining independent steps may complete). | Active; operation is retryable. | N/A | N/A | `privacy.personal_data_deleted` partial event; per-step error code logged. | yes (transient upstream failure) | Partial failure does not release barrier; already-completed steps remain completed. | HTTP response + operation-state query + per-step audit | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 4 | AMD020-W6-004 | — | Overall deadline between steps | Delete operation in `processing`; overall deadline expires before all steps complete. | Process deletion cascade until deadline. | 504 Gateway Timeout, `error.code: upstream_timeout`; no partial body returned. | Operation transitions to terminal `failed`; any completed steps recorded; uncompleted steps marked failed. | Remains active; convergence gate entered (recovery purge or subject suppression required before release). | N/A | N/A | `privacy.personal_data_deleted` failed event with `upstream_timeout`. | yes (after upstream recovery / recovery purge) | Deadline expiry does not leave subject unprotected; barrier stays until safe outcome. | HTTP response + operation-state query + barrier probe | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 5 | AMD020-W6-005 | — | Schema mismatch | Producer generates response violating contract schema. | Return producer response through W3 validation layer. | 500 Internal Server Error, `error.code: schema_mismatch`. | Operation terminal `failed`; no partial success persisted to client. | Remains active; convergence gate entered. | N/A | N/A | `privacy.schema_mismatch` event. | no | Malformed contract response is never exposed to client as success. | Producer output + W3 validation log | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 6 | AMD020-W6-006 | — | Malformed upstream response | W2 returns non-JSON or missing required fields. | W3 parses upstream response. | 502 Bad Gateway, `error.code: upstream_malformed`. | Operation terminal `failed` (or `partially_completed` if other steps completed). | Active; convergence gate entered if terminal failed. | N/A | N/A | `privacy.upstream_malformed` event. | yes (after upstream fix) | Upstream contract violation is not treated as semantic success. | Upstream raw body + error log | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 7 | AMD020-W6-007 | — | Relinking during deletion | Delete operation in `processing`; BotUser relinks to different AylaUser mid-flight. | System detects link_generation change. | 502/500, `error.code: subject_mismatch` (external status `failed`/`aborted`). | Operation terminal `aborted`; completed steps remain; uncompleted steps cancelled; new link_generation recorded. | Remains active for old scope_hash until convergence gate resolves old persona. | N/A | N/A | `privacy.delete_aborted` with reason `relink`; old persona marked for mandatory purge/resolution. | no for old operation; new operation required with new scope_hash. | Old persona cannot be orphaned in partially-deleted state; new persona cannot inherit old data. | Operation log + old-persona state query + barrier probe | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 8 | AMD020-W6-008 | — | Cross-tenant access | Authenticated subject belongs to tenant A; request targets tenant B subject. | Send export/delete request. | 403 Forbidden, `error.code: cross_tenant_violation`. | No operation record created. | Not created. | N/A | N/A | `privacy.cross_tenant_violation` event. | no | Tenant boundary cannot be crossed by personal-context operations. | HTTP response + audit log | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 9 | AMD020-W6-009 | — | Write UserPersonalContext after barrier | Delete operation active; barrier set for subject. | Attempt to create/update UserPersonalContext row for subject. | 409 Conflict or 503 Service Unavailable (W2/W3 internal rejection). | No new/modified UserPersonalContext row. | Active; write rejected. | N/A | N/A | `privacy.write_blocked_by_barrier` event. | yes (after operation completes) | Personal context cannot be recreated while deletion is in flight. | Write attempt + database query + barrier metric | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 10 | AMD020-W6-010 | — | Write MemoryEntry after barrier | Delete operation active; barrier set for subject. | Attempt to create green MemoryEntry for subject. | 409/503 rejection. | No new MemoryEntry row. | Active; write rejected. | N/A | N/A | `privacy.write_blocked_by_barrier` event. | yes (after operation completes) | Memory cannot be recreated while deletion is in flight. | Write attempt + memory table query + barrier metric | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 11 | AMD020-W6-011 | — | Create ConsentRecord after barrier | Delete operation active; barrier set for subject. | Attempt to create ConsentRecord for subject. | 409/503 rejection. | No new ConsentRecord row. | Active; write rejected. | N/A | N/A | `privacy.write_blocked_by_barrier` event. | yes (after operation completes) | Consent cannot be recreated while deletion is in flight. | Write attempt + consent table query + barrier metric | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 12 | AMD020-W6-012 | — | Inference job after barrier | Delete operation active; inference job would create green MemoryEntry. | Trigger inference job. | N/A (background job rejected). | No inferred MemoryEntry created. | Active; inference blocked. | N/A | N/A | `privacy.inference_blocked_by_barrier` event. | yes (after operation completes) | Inferred memory cannot bypass deletion barrier. | Celery/job log + memory table query | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 13 | AMD020-W6-013 | — | Hard purge MemoryEntry | Green MemoryEntry row soft-deleted at time T; `soft_delete_retention` elapsed. | Run daily purge job. | N/A. | Row physically removed from primary store; audit `memory.purged_rows`. | N/A (operation already completed). | N/A | N/A | `memory.purge_run` with row count. | yes (cron is idempotent) | Soft-deleted memory is physically purged after approved retention. | Cron log + database query before/after | NOT_IMPLEMENTED | NOT_EXECUTED | BLOCKED |
| 14 | AMD020-W6-014 | — | Physical wipe UserPersonalContext | Delete operation reaches ayla_delete step. | Execute W2 physical delete. | N/A (internal step). | UserPersonalContext row removed from W2 primary store; per_step_results.ayla_delete.ok=true. | Active during step; retained for operation duration. | N/A | N/A | `privacy.ayla_upc_deleted`. | yes (transient upstream failure) | Primary UPC data is removed on delete if physical wipe is canonical. | Database query + per_step_results + audit | NOT_IMPLEMENTED | NOT_EXECUTED | BLOCKED |
| 15 | AMD020-W6-015 | — | ConsentRecord withdrawal and retention | Active ConsentRecord exists for subject. | Execute consent_withdraw step. | N/A. | `withdrawn_at` timestamp set; row retained as audit trail; pseudonymization applied if configured. | Active during step. | N/A | N/A | `privacy.consent_withdrawn`. | yes | Consent withdrawal is recorded and retained only under approved lawful basis/retention. | Database query + audit log | NOT_IMPLEMENTED | NOT_EXECUTED | BLOCKED |
| 16 | AMD020-W6-016 | — | Redis cleanup | Pilot scope includes only Postgres-backed classes. | Inspect Redis/cache read/write paths for included classes. | N/A. | No Redis keys for included classes. | N/A. | N/A | N/A | Inventory report. | N/A | No persistent derived cache of included classes exists outside Postgres in pilot. | Repository grep + SHA + command output | NOT_IMPLEMENTED | NOT_EXECUTED | NOT_APPLICABLE |
| 17 | AMD020-W6-017 | — | Derived/cache/index cleanup | Memory entries deleted; in-memory prompt block may still surface deleted facts. | Query memory through read-gate / prompt block builder. | N/A. | Deleted facts not returned. | N/A. | N/A | N/A | Read-gate log. | N/A | Derived in-memory representations cannot resurrect deleted primary data. | Read-gate test + prompt block inspection | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 18 | AMD020-W6-018 | — | Retained manifest | Delete operation completed. | Inspect delete response retained[]. | 200 OK. | retained[] lists every retained item with category, reason, decision_status, owner, deletion_trigger. | Released (safe outcome `completed`). | N/A | N/A | `privacy.personal_data_deleted` includes retained count. | N/A | User receives transparent list of retained data and legal basis. | Response body + audit payload | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 19 | AMD020-W6-019 | — | Audit correlation | Delete/export operation executed. | Collect all audit events for the operation. | N/A. | All audit rows share operation_id and correlation_id. | N/A. | N/A | N/A | Correlated events: created, barrier_set, per-step results, completion/failure. | N/A | Full audit trail is reconstructible by operation_id. | Audit store query by operation_id | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 20 | AMD020-W6-020 | — | PII in URL/logs/metrics/traces | Operation executed; sinks inspected. | Search access logs, traces, metrics, query strings for plaintext identifiers/values. | N/A. | No plaintext ayla_user_id, bot_user_id, phone, email, name, MemoryEntry.content, export body in sinks. | N/A. | N/A | N/A | Security audit sample. | N/A | PII is not leaked to observability sinks; internal URL PII gap (DEL-009) must be closed before activation. | Log/metric/trace queries + sanitization config | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 21 | AMD020-W6-021 | — | Export of another user | Authenticated subject A; request targets subject B. | Send export request for subject B. | 403 Forbidden, `error.code: subject_mismatch`. | No export operation created. | Not created. | N/A | N/A | `privacy.subject_mismatch` event. | no | Cross-user export is impossible. | HTTP response + audit log | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 22 | AMD020-W6-022 | — | Stale initData | MaxInitData older than `max_init_data_age`. | Send export/delete request. | 401 Unauthorized, `error.code: init_data_expired`. | No operation created. | Not created. | N/A | N/A | `privacy.init_data_expired` event. | yes (with fresh initData) | Stale authentication cannot authorize privacy operations. | HTTP response + auth log | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 23 | AMD020-W6-023 | — | Expired confirmation challenge | Delete step-up challenge issued; TTL elapsed. | Submit delete confirmation with expired challenge. | 403 Forbidden, `error.code: confirmation_expired`. | No operation created or operation rejected. | Not created. | N/A | N/A | `privacy.confirmation_expired` event. | yes (new challenge) | Expired destructive confirmation cannot be replayed. | HTTP response + challenge store query | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 24 | AMD020-W6-024 | — | Nonce reuse | Delete confirmation nonce already consumed. | Submit same nonce again. | 409 Conflict, `error.code: replay_detected`. | No second destructive execution. | Unchanged if operation exists. | N/A | N/A | `privacy.replay_detected` event. | no (nonce is one-time) | Destructive nonce cannot be reused. | HTTP response + nonce store query | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 25 | AMD020-W6-025 | — | Export after delete | Delete operation completed for subject. | Send export request for same subject. | 200 OK. | Export operation `completed`; ayla.personal_context=null; memory=[]; consents contain only withdrawn history. | Released (delete reached safe outcome). | N/A | N/A | `privacy.personal_data_exported` after delete. | yes (idempotent) | Post-delete export cannot resurrect deleted primary data. | Export response + primary-store query | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 26 | AMD020-W6-026 | — | Repeat delete after completion | Delete operation already completed. | Send new delete request (new idempotency_key). | 200 OK, status `completed`; empty deleted[]; retained[] lists audit/consent items; per_step_results show already_deleted/withdrawn. | New operation record `completed`; no new destructive execution of already-deleted classes. | Released immediately for new operation (safe outcome). | N/A | N/A | `privacy.personal_data_deleted` idempotent repeat event. | yes | Repeat delete is safe and does not corrupt state. | HTTP response + state query + audit | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 27 | AMD020-W6-027 | — | Partial recovery | Operation in `partially_completed`; upstream failure resolved. | Retry operation (same idempotency_key). | 200 OK, status `completed` after all steps succeed. | Operation transitions to `completed`; all steps recorded ok. | Released after `completed`. | N/A | see scenario | Retry and completion events logged. | yes | Transient partial state is recoverable without data loss or recreation. | Retry request + final state query | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 28 | AMD020-W6-028 | — | Backup expiry | Primary data deleted; `backup_expiry` elapsed. | Verify backup contents no longer contain deleted primary data. | N/A. | Backup lifecycle state `backup_expired`. | N/A. | N/A | N/A | Backup retention report. | N/A | Deleted primary data does not survive backup retention window. | Backup scan report | NOT_IMPLEMENTED | NOT_EXECUTED | BLOCKED |
| 29 | AMD020-W6-029a | — | Process crash — resumable | Operation in `processing`; worker process crashes. | Restart worker; client performs status read with operation_id. | Status read returns current state; operation resumes and eventually `completed`. | Operation state recovered from durable store; execution_attempt incremented on resume. | Active throughout; not released during crash. | N/A | N/A | `privacy.operation_resumed` event. | yes | Process crash does not lose operation state or release barrier. | Crash injection + status read + final state | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 30 | AMD020-W6-029b | — | Process crash — unrecoverable | Operation in `processing`; worker process crashes and cannot resume safely. | Incident commander records terminal abort; system enters convergence gate. | Status read returns `failed`; barrier remains active until convergence/recovery. | Operation terminal `failed`; convergence gate entered; recovery_purge_operation created or subject_suppression installed. | Remains active until deletion_converged / recovery completed / suppression active. | N/A | see scenario | `privacy.delete_aborted` + `privacy.recovery_purge_created` or `privacy.subject_suppression_set`. | no for old operation; new operation after convergence with new idempotency_key. | Unrecoverable crash does not auto-release barrier; subject remains protected. | Crash injection + status reads + barrier probe + convergence log | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 31 | AMD020-W6-030 | — | Stuck operation — authorized terminal abort | Operation stuck in `partially_completed` and cannot resume. | Two authorized operators approve abort with reason code and incident ticket. | Operation status becomes `aborted` (externally `failed`/`aborted`). | Operation terminal `aborted`; convergence gate entered; recovery_purge_operation or subject_suppression created. | Remains active until convergence/recovery/suppression. | N/A | see scenario | `privacy.delete_aborted` with operator identities, reason, incident ticket. | no for old operation; new operation only after convergence. | Manual abort cannot leave subject unprotected; new writes blocked until safe outcome. | Abort action + operation log + barrier probe + recovery audit | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 32 | AMD020-W6-031 | — | Scope mismatch with same idempotency key | Previous request used idempotency_key K with scope_hash S1. | Send new request with same K but different scope_hash S2. | 409 Conflict, `error.code: replay_detected`. | No new operation; idempotency record unchanged. | Unchanged. | N/A | N/A | `privacy.replay_detected` event. | no (new idempotency_key required) | Idempotency key cannot be reused across different scopes. | HTTP response + idempotency store query | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 33 | AMD020-W6-032 | — | Different idempotency keys for same active operation | Active operation with scope_hash S. | Send two requests with different idempotency_keys but same S. | Both join same operation (202/200 with same operation_id). | Single operation record; both idempotency_keys mapped to same operation_id. | Active; no second execution. | N/A | N/A | Two `privacy.operation_joined` events. | yes | Concurrent deletes for same scope do not create parallel executions. | Two requests + operation-state query | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 34 | AMD020-W6-033 | — | Export delivery headers | Export operation completed at UTC date D. | Send export request. | 200 OK; Content-Disposition: attachment; filename="ayla-personal-data-YYYY-MM-DD.json" where YYYY-MM-DD equals D in UTC; regex validated. | Export operation `completed`; no persistent download URL. | N/A. | N/A | N/A | `privacy.personal_data_exported` with filename and format_version. | yes | Export filename contains only date, no subject identifier; no persistent URL. | HTTP headers + regex check + URL persistence check | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 35 | AMD020-W6-034 | — | No subject ID in access logs | Operation executed. | Inspect access logs/traces/metrics. | N/A. | No plaintext ayla_user_id/bot_user_id/phone/email/name in sinks. | N/A. | N/A | N/A | Sanitization config audit. | N/A | Subject identifiers are pseudonymized in observability sinks. | Log/metric/trace queries + HMAC digest verification | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 36 | AMD020-W6-035 | — | Export schema versioning — producer | Producer generates response with unknown top-level field for format_version 1.0. | W3 validates response against closed schema. | 500 Internal Server Error, `error.code: schema_mismatch`. | Operation terminal `failed`; no malformed response sent to client. | N/A for export. | N/A | N/A | `privacy.schema_mismatch` event. | no | Producer cannot extend closed schema without version bump. | Producer output + validation log | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 37 | AMD020-W6-036 | — | Partial export failure | Export operation in progress; upstream unavailable. | Process export. | 502 Bad Gateway, `error.code: upstream_unavailable`; no partial JSON body. | Operation terminal `failed`. | N/A for export. | N/A | N/A | `privacy.export.failed.upstream_unavailable` event. | yes (transient upstream) | Partial export result is never returned to client. | HTTP response + body inspection | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 38 | AMD020-W6-037 | — | Fail-closed step-up unavailable | Step-up provider misconfigured or unavailable. | Send delete request. | 500 Internal Server Error, `error.code: internal_error`; no fallback to MaxInitData-only auth. | No operation created; internal security incident recorded. | Not created. | N/A | N/A | `security_incident.internal_credential_failure` with severity and alert; `privacy.step_up_unavailable`. | no until step-up restored; endpoint may be disabled via circuit breaker. | Misconfigured step-up cannot weaken authentication; client receives no config details. | HTTP response + security incident + alert log | NOT_IMPLEMENTED | NOT_EXECUTED | BLOCKED |
| 39 | AMD020-W6-038a | — | Legacy audit cleanup — dry-run | Audit table contains expired, held, and non-expired rows. | Run retention cleanup job with `dry_run=true`. | N/A. | No rows deleted; report lists rows that would be deleted and held rows preserved. | N/A. | N/A | N/A | `audit.retention_cleanup.dry_run` report. | yes | Dry-run must not mutate data. | Report + table row counts before/after | NOT_IMPLEMENTED | NOT_EXECUTED | BLOCKED |
| 40 | AMD020-W6-038b | — | Legacy audit cleanup — execution | Legal/Privacy approved dry-run report. | Run retention cleanup job with `dry_run=false`. | N/A. | Expired rows deleted; held rows preserved; non-expired rows retained; idempotent re-run deletes no additional rows. | N/A. | N/A | N/A | `audit.retention_cleanup.executed` with counts. | yes (idempotent) | Statutory holds are honored; deletion is bounded and resumable. | Execution report + table query + re-run verification | NOT_IMPLEMENTED | NOT_EXECUTED | BLOCKED |
| 41 | AMD020-W6-039 | — | Expanded consent history in export | Backfill migration completed; legacy and new rows exist. | Send export request. | 200 OK. | Every consents[] row contains required expanded fields; legacy rows carry sentinel values and flags: legacy_record=true, schema_complete, semantic_complete, legal_validity_status. | N/A. | N/A | N/A | `privacy.personal_data_exported`. | yes | Schema completeness is distinguishable from legal validity; legacy rows are explicitly flagged. | Export response + database query for flags | NOT_IMPLEMENTED | NOT_EXECUTED | BLOCKED |
| 42 | AMD020-W6-040 | — | Green MemoryEntry delete step failure | Delete operation in `processing`; memory_delete step fails. | Process cascade. | 502 Bad Gateway, status `partial`; failed_steps=[`memory_delete`]. | Operation `partially_completed`; ayla_delete and consent_withdraw completed if independent. | Active; retryable. | N/A | N/A | Partial event with memory_delete error. | yes | Per-step failure is isolated; barrier prevents recreation. | HTTP response + per_step_results + audit | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 43 | AMD020-W6-041 | — | ConsentRecord withdraw step failure | Delete operation in `processing`; consent_withdraw step fails. | Process cascade. | 502 Bad Gateway, status `partial`; failed_steps=[`consent_withdraw`]. | Operation `partially_completed`; ayla_delete and memory_delete completed if independent. | Active; retryable. | N/A | N/A | Partial event with consent_withdraw error. | yes | Per-step failure is isolated; barrier prevents recreation. | HTTP response + per_step_results + audit | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 44 | AMD020-W6-042 | — | Mandatory recovery after terminal abort | Operation terminal `failed`/`aborted` with completed and uncompleted steps. | System enters convergence gate. | Status read returns `failed`/`aborted`; barrier remains active. | recovery_purge_operation created OR subject_suppression tombstone installed; old operation linked to recovery. | Active until recovery reaches safe outcome. | N/A | see scenario | `privacy.recovery_purge_created` or `privacy.subject_suppression_set`. | yes for recovery operation | Terminal failure does not leave subject unprotected; new writes blocked until convergence. | Abort + status reads + recovery audit + barrier probe | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 45 | AMD020-W6-043 | — | Old scope_hash cannot be restored after double relink | Subject relinked from AylaUser1 to AylaUser2; then back to AylaUser1. | Attempt operations using old scope_hash from first link_generation. | 409 Conflict, `error.code: replay_detected` or `subject_mismatch`. | Idempotency records keyed by old scope_hash remain linked to old operation; new operations use strictly greater link_generation. | Old barrier managed by old operation lifecycle; new operations use new scope_hash. | N/A | N/A | `privacy.replay_detected` for old scope_hash reuse attempt. | no | link_generation is monotonic; previous scope_hash values are never reused. | Relink sequence + idempotency store + operation logs | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 46 | AMD020-W6-044 | AMD020 v0.8 §3.1 recovery failure | Recovery purge operation fails | Parent operation terminal failed/aborted; recovery_purge_operation created and reaches failed | Recovery purge executes and fails | 502/500 status failed/aborted | Parent operation state recovery_failed; recovery_operation state failed; barrier_state active; deletion_converged false | Active | none | failed | privacy.recovery_failed + security incident if max retries exceeded | no for original; bounded retry for recovery | Failed recovery does not release barrier or mark convergence | Operation-state query + recovery log + barrier probe | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 47 | AMD020-W6-045 | AMD020 v0.8 §3.1 repeated recovery failure | Second recovery purge also fails | First recovery failed; system creates second recovery; second also fails | Second recovery executes and fails | 502/500 status failed/aborted | Parent operation recovery_failed; retry count exhausted; incident ticket created | Active | none | failed | privacy.recovery_failed; security_incident.recovery_max_retries | no until manual incident resolution | Repeated failed recovery escalates; barrier stays | Recovery logs + incident ticket | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 48 | AMD020-W6-046 | AMD020 v0.8 §3.1 recovery + dirty sweep | Recovery completes but inventory sweep finds residual data | Recovery purge reached completed | Post-recovery inventory sweep detects residue | 502/500 status failed/aborted | Parent operation remains recovery_failed; new recovery_purge_operation created; deletion_converged false | Active | none | completed then failed-dirty-sweep | privacy.recovery_completed + privacy.recovery_sweep_dirty + privacy.recovery_purge_created | yes for new recovery | Recovery alone is not a safe outcome; clean sweep required | Recovery audit + inventory sweep report | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 49 | AMD020-W6-047 | AMD020 v0.8 §3.1 safe recovery outcome | Recovery completes and post-recovery sweep is clean | Recovery purge reached completed | Post-recovery inventory sweep confirms no residue | 200/202 status transitions to deletion_converged then completed | Parent operation deletion_converged; barrier_state released; recovery_state completed | Released | none | completed + clean sweep | privacy.recovery_completed + privacy.deletion_converged + privacy.barrier_released | N/A | Only completed recovery + clean sweep releases barrier | Recovery audit + inventory sweep report + barrier probe | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 50 | AMD020-W6-048 | AMD020 v0.8 §3.7 barrier→suppression handoff | Process crash requires handoff to suppression | Operation terminal aborted; process about to crash | Crash occurs; worker restarts and performs handoff | Status read returns failed/aborted; barrier_state handoff_to_suppression then suppressed | Suppression tombstone installed; barrier released only after suppression active; no data recreated | handoff_to_suppression → suppressed | active | N/A | privacy.subject_suppression_handoff + privacy.subject_suppression_set | no for original; recovery scheduled | No window without guard during crash recovery | Crash injection + status reads + suppression probe + write attempt | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 51 | AMD020-W6-049 | AMD020 v0.8 §3.7 handoff failure | Suppression tombstone cannot be installed during handoff | Operation terminal aborted; suppression store rejects write | System attempts barrier→suppression handoff | 500 internal_error; barrier remains active | Handoff fails; barrier stays; incident created; suppression_state pending | Active | pending | N/A | privacy.subject_suppression_handoff + security_incident.subject_suppression_failure | no until incident resolved | Failed handoff does not release barrier | Handoff failure injection + incident log | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 52 | AMD020-W6-050 | AMD020 v0.8 §3.7 suppression store unavailable | Suppression store is unreachable | Suppression tombstone active or store unavailable | Attempt any included-class write | 503 Service Unavailable | No new row created; write rejected | N/A | active/unavailable | N/A | privacy.write_blocked_by_suppression or privacy.subject_suppression_store_unavailable | yes after store recovery | Writes fail closed when suppression store unavailable | Write attempt + suppression store failure injection | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 53 | AMD020-W6-051 | AMD020 v0.8 §3.7 write under suppression | Included-class write attempted while suppression active | Suppression tombstone active for subject | Create UserPersonalContext / MemoryEntry / ConsentRecord | 409 Conflict or 503 Service Unavailable | No new row created | N/A | active | N/A | privacy.write_blocked_by_suppression | yes after convergence | Suppression blocks recreation of included data | Write attempt + suppression probe | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 54 | AMD020-W6-052 | AMD020 v0.8 §3.7 relink under suppression | Subject relinks while old persona is suppressed | Old persona has active suppression tombstone | Relink BotUser to new AylaUser | Old persona suppression stays active; new persona unaffected | Old scope_hash remains suppressed; new scope_hash has no suppression; old operation continues convergence | N/A | old active; new none | N/A | privacy.relink + privacy.subject_suppression_set (old) | no for old operation; new operation possible | Suppression is tied to old link_generation, not subject globally | Relink sequence + suppression probe + operation logs | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 55 | AMD020-W6-053 | AMD020 v0.8 §3.7 suppression removal | Suppression removed after clean sweep | Suppression active; recovery completed; sweep clean | System removes suppression tombstone | N/A | Suppression record removed; deletion_converged true; barrier released | Released | removed | completed + clean sweep | privacy.subject_suppression_removed + privacy.deletion_converged | N/A | Suppression removed only after proven convergence | Suppression store query + audit | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 56 | AMD020-W6-054 | AMD020 v0.8 §4.2.3 HMAC rotation during active delete | HMAC key rotates while delete operation is active | Active delete operation with old hmac_key_version | Key rotation occurs; new request arrives for same subject | New request joins active operation via alias mapping; 202/200 | Single operation continues; idempotency alias resolves old scope_hash; no parallel operation created | Active | none | N/A | privacy.operation_joined (alias) | yes | HMAC rotation does not orphan or duplicate active operation | Key rotation + alias lookup + operation-state query | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 57 | AMD020-W6-055 | AMD020 v0.8 §4.2.3 rotation with active barrier | HMAC rotation with active barrier and no operation | Barrier active for subject under old key version | New request after rotation | New request resolved via key-ring; joins active scope or returns current status | Barrier/barrier alias found; no second barrier | Active | none | N/A | privacy.operation_joined / privacy.barrier_active | yes | Barrier state discoverable across key versions | Key rotation + barrier probe + status read | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 58 | AMD020-W6-056 | AMD020 v0.8 §3.7/§4.2.3 suppression stable across rotation | HMAC rotation with active suppression | Suppression tombstone active under old key version | New request after rotation | Suppression resolved via stable subject_ref; write rejected | Suppression remains active for semantic subject | N/A | active | N/A | privacy.write_blocked_by_suppression | yes after convergence | Suppression follows stable identity, not scope_hash | Key rotation + suppression probe + write attempt | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 59 | AMD020-W6-057 | AMD020 v0.8 §4.2/§4.4 double relink + rotation | Double relink and HMAC rotation do not restore old scope_hash | Subject relinked twice; HMAC rotated | Attempt operation using old scope_hash/old link_generation | 409 replay_detected / subject_mismatch | Old scope_hash not reused; idempotency records remain tied to old operation | N/A | none | N/A | privacy.replay_detected | no | Old scope_hash and link_generation never reused | Relink sequence + rotation + idempotency store query | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 60 | AMD020-W6-058 | AMD020 v0.8 §5.8 status read after timeout | Timeout after partial destructive execution | Operation partially completed some steps; overall deadline expires | Client performs status read | 200 OK with status partially_completed / failed | Status read returns completed_steps, failed_steps, pending_steps, per_step_results, barrier_state active, recovery_state if any | Active | none | N/A or pending | privacy.personal_data_deleted failed event + status read audit | yes after recovery | Partial destructive results are durable and discoverable | Timeout + status read + schema validation | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 61 | AMD020-W6-059 | AMD020 v0.8 §5.8 status read recovery_failed | Status read for recovery_failed operation | Parent operation in recovery_failed after recovery failure | Client performs status read | 200 OK status failed/aborted externally; internally recovery_failed | Response shows recovery_operation_id, recovery_state failed, barrier_state active, deletion_converged false | Active | none | failed | privacy.status_read + privacy.recovery_failed | yes for status read; no for recovery until escalation | Status read exposes true durable state | Status read call + schema validation | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 62 | AMD020-W6-060 | AMD020 v0.8 §5.8 status read deletion_converged | Status read after safe convergence | Operation reached deletion_converged | Client performs status read | 200 OK status completed | Response shows deletion_converged true, barrier_state released, suppression_state none | Released | none | N/A | privacy.deletion_converged + privacy.status_read | yes | Status read confirms safe outcome | Status read + schema validation | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 63 | AMD020-W6-061 | AMD020 v0.8 §4.5 old-persona access after rotation | User accesses old persona after HMAC rotation | Ownership mapping exists; HMAC rotated | Authenticated owner requests old persona export/delete | 200/202 authorized | Old persona operation created/listed; cross-tenant check passes | N/A | none | N/A | privacy.old_persona_accessed | yes | Old persona accessible without reverse relink | Old-persona API call + key-ring resolution + audit | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 64 | AMD020-W6-062 | AMD020 v0.8 §4.5 old-persona access after double relink | User accesses old persona after two relinks | Ownership mapping exists after double relink | Authenticated owner requests old persona export/delete | 200/202 authorized | Old persona operation tied to old scope_hash/link_generation | N/A | none | N/A | privacy.old_persona_accessed | yes | Double relink preserves old persona ownership mapping | Relink sequence + old-persona API call + audit | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 65 | AMD020-W6-063 | AMD020 v0.8 §4.5 old-persona cross-tenant denial | Post-relink user tries to access old persona of another tenant | User authenticated in tenant A; targets old persona in tenant B | Request old persona operation | 403 cross_tenant_violation / subject_mismatch | No operation created; access denied | N/A | none | N/A | privacy.old_persona_access_denied | no | Old persona access is tenant-scoped | Old-persona API call + tenant boundary check | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 66 | AMD020-W6-064 | AMD020 v0.8 §4.2.4 parallel operation via new hash | Attempt to create parallel operation after HMAC rotation | Active operation exists under old scope_hash; new scope_hash after rotation | Send new delete request with new scope_hash | 202/200 joins active operation OR 409 operation_in_progress | No second destructive execution; alias mapping resolves to active operation | Active | none | N/A | privacy.operation_joined (alias) or privacy.operation_conflict | yes | Parallel destructive operations for same subject are prohibited | Rotation + new request + operation-state query | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |
| 67 | AMD020-W6-065 | AMD020 v0.8 §5.8 status-read schema validation | Status-read response conforms to operation-status-read schema | Any operation exists | Perform status read | 200 OK | Response validates against operation-status-read/1.0 schema; additionalProperties rejected | N/A | none | N/A | privacy.status_read | yes | Status read contract is machine-enforceable | Schema validation script + HTTP response | NOT_IMPLEMENTED | NOT_EXECUTED | SPECIFIED |

**Battery summary:** 67 scenario rows; 0 implemented; 0 executed; 8 blocked; 1 not applicable; 58 specified. No scenario is claimed as passing.

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
| Step-up/auth values (delete) | P0.6 | max_init_data_age, challenge TTL, rate limits | `owner_decision_required` | W4/W3/Security | confirm values; fail-closed policy | no | yes |
| Step-up/auth values (export) | v0.7 review | whether export requires step-up challenge | `owner_decision_required` | Security/Owner | approve export step-up policy before activation | no | yes |
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
| C1 Auth/replay/step-up | **BLOCKED** | Delete fail-closed rule added; export step-up now marked `owner_decision_required` instead of assumed default; numerical values and production readiness require Security/owner decision | §8.2, §8.6 | Security/owner must confirm delete step-up values and export step-up policy |
| C2 Error taxonomy | PASS | Machine codes; security incident internal; `init_data_expired` separated from `auth_invalid` | §5.6, §5.8 | — |
| C3 ПД в URL/logs/metrics/traces | PARTIAL | Safe-logging rule + PII-in-URL rule; internal W3→W2 URL still an implementation gap | §8.3, §8.4 | DEL-009: choose opaque token or sanitization |
| C4 404 ≠ semantic success | **PASS** | `subject_gone` code defined; generic 404 is treated as `upstream_error`/`contract_violation` in both AMD-020 §6 and Amendment §3/DEL-005 | §6; Amendment DEL-005 | — |
| D1 Гонки / barrier | **BLOCKED** | Barrier + concurrent join defined; atomic operation creation is `implementation_delta` | §3.1, §3.3, §4.3 | Implement single-transaction operation+lock+barrier before activation |
| D2 Идемпотентность механика | PASS | scope_hash, request/execution attempt, replay read | §4 | — |
| D3 Полный lifecycle | **BLOCKED** | UPC physical wipe and ConsentRecord retention are `proposed_norm_pending_owner_confirmation` | §3.2, §3.4, §10.3 | Owner/Legal must confirm UPC wipe and consent retention |
| D4 Retention manifest | PASS | `retained[]` with `decision_status` | §7 | — |
| E1 Closed schemas | **PASS** | All root schemas now have `$id`; `$defs` duplicated per schema; recursive `$ref` fixed; failure enum matches taxonomy; `personal_context` and `MemoryEntry.content` declared `opaque_payload`; producer/consumer contract explicit; runnable validator script committed | §5.1–§5.7, §6; `scripts/validate_amd020_schemas.py` | — |
| E2 operation_id/correlation | PASS | Defined; scope_hash added | §4 | — |
| F1 Acceptance battery | PARTIAL | 45 scenario rows; full test-case format (preconditions, action, HTTP, persisted state, barrier state, audit event, retryability, invariant, evidence type, status); counts corrected to 36 specified / 8 blocked / 1 N/A; mandatory recovery and scope_hash monotonicity tests added; not executed | §13 | Finalize decisions blocking C1/D3 before W6 run |
| G1 Нет открытых decisions при сдаче | **FAIL** | Multiple owner/legal/security decisions remain open | §14 | Resolve blocker decisions before final approval |
| G2 Validation | PASS | Repository validator: 0 errors, warnings ≤ baseline | — | Re-run after edits |
| G3 Отчёт по форме | PASS | This section + final agent report | §17 | — |
| H Cross-document consistency | **PARTIAL** | Contract v0.7 changed barrier lifecycle, relink, subject_gone, scope_hash, consent flags, export auth, W6 battery; Amendment v0.7 not yet synchronized; readiness gate count still 25 but normative content diverges | AMD-020 §3.1, §4.2, §4.4, §6, §8.6, §10.2, §13; Amendment | Synchronize Amendment v0.7 before claiming PASS |
| I Implementation evidence | PARTIAL | Pinned commit SHAs and reproducible grep commands added for Redis/cache/derived inventory; code evidence cited for key facts; backup evidence and full W6 evidence still pending | §2.1, §2.2, §8.5 | Collect W6 evidence and backup inventory after implementation |
| J Writing precision | **PARTIAL** | Code-fence issue fixed; W6 battery rewritten as full test cases with preconditions/persisted state/barrier/audit/invariants; `subject_gone` redesigned for W2 implementability; scope_hash serialization formalized; remaining precision depends on owner decisions and final implementation evidence | §4.2, §5, §6, §13 | Finalize owner decisions and re-verify after implementation |

**Итог Quality Bar:** FAIL/BLOCKED по пунктам B3, C1, D1, D3, G1; PARTIAL по B4, C3, F1, H, I, J.
Документ остаётся Draft/Proposed/Blocked с `review_status: pending_technical_re_review`.
Пакет подготовлен для **повторного технического ревью**, но **не** к structured
owner decision review, final owner approval, canonicalization или operational
activation.

---

## 18. Change Log

### v0.7 — 2026-07-23

- `review_status` изменён на `pending_technical_re_review`; owner approval запрещён
  до прохождения технического ревью.
- Barrier lifecycle перепроектирован: `failed`/`aborted` не снимают barrier
  автоматически; введены `deletion_converged`, `recovery_purge_operation`,
  `subject_suppression` как обязательные безопасные исходы.
- Relink lifecycle перепроектирован: `link_generation` монотонно возрастающий;
  запрещено восстановление прежнего `scope_hash`; старая persona получает
  обязательный путь завершения удаления без зависимости от OP6.
- `scope_hash` формализован: canonical JSON serialization, HMAC-SHA-256,
  sorted keys, key version management.
- `subject_gone` перепроектирован: W2 не обязан возвращать `bot_user_id`;
  добавлены `format_version`, `correlation_id`, `retryable`; `operation_id`
  объяснено отсутствие.
- Все root JSON Schemas получили `$id`; добавлен запускаемый
  `scripts/validate_amd020_schemas.py`.
- ConsentRecord export schema: `legacy_record`, `schema_complete`,
  `semantic_complete`, `legal_validity_status` — required; разделена schema
  completeness и legal validity.
- Export step-up политика помечена как `owner_decision_required`.
- W6 acceptance battery переписана в полноценном формате тест-кейсов с
  preconditions, persisted state, barrier state, audit event, invariant,
  evidence type; добавлены сценарии mandatory recovery и scope_hash monotonicity;
  counts исправлены (36 specified / 8 blocked / 1 N/A).
- Quality Bar обновлена: удалены ложные PASS; `H Cross-document consistency`
  понижен до PARTIAL из-за необходимости синхронизации Amendment.
- Implementation Amendment ещё не синхронизирован с v0.7 Contract.

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

**Конец документа — AMD-020 v0.8 (Draft, pending technical re-review)**