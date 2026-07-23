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
version: "0.5"
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
| Version | 0.5 (2026-07-23) |
| Review status | pending_owner_approval |

**Owner ruling:** Режим 2+ — двухступенчатая канонизация. Настоящий документ
подготовлен для повторного owner review. Самостоятельный перевод в
Canonical/Accepted запрещён.

**What this document IS:** нормативный контракт self-service экспорта и
удаления (forget) данных, входящих в утверждённый Personal Context pilot scope,
для пилота 2026-08-15.

**What this document IS NOT (дословные дисклеймеры):**

- AMD-020 v0.5 не является полным механизмом реализации прав субъекта по 152-ФЗ.
- AMD-020 v0.5 не является формальным ответом по статье 14 152-ФЗ.
- AMD-020 v0.5 не является удалением аккаунта.
- AMD-020 v0.5 не является исчерпывающим удалением всех персональных данных Ayla.

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
boundary. These conflicts are **not resolved** in v0.5; they are recorded here
and in §14 for owner decision:

| Conflict | Handoff source | AMD-020 position | Resolution authority |
|---|---|---|---|
| Wellness/sleep export and deletion cascades with OP6 | `2026-05-19-wellness-sleep-handoff.md` §11.4 | Excluded from pilot scope (§1.2) | Owner / Legal / Privacy / OP6 track |
| Loyalty data erased on account deletion | `2026-05-18-loyalty-system-handoff.md` §14 | Loyalty records excluded; AMD-020 not account deletion | Owner / OP6 track |
| Reviews have 30-day customer hard-delete window | `2026-05-19-master-reviews-feedback-handoff.md` §2.10, §7.1, §7.2 | Reviews excluded from pilot scope | Owner / Gamma Reviews Owner |
| Conversations hidden/exported on customer deletion | `2026-05-17-conversations-handoff.md` §7; `2026-05-18-master-mobile-handoff.md` §13 E17; `2026-05-19-master-admin-internal-chat-handoff.md` §8.5 | Conversations/messages excluded from pilot scope | Owner / W5 Conversation Owner |
| Customer profile button «Удалить все мои данные» triggers OP6 | `2026-05-18-customer-first-time-handoff.md` §12 F4 | AMD-020 is not exhaustive deletion / account deletion | Owner / Product / Legal |
| Account-lock state machine includes `DELETED` | `2026-05-19-master-device-reauth-handoff.md` §9.1 | Account deletion excluded from pilot scope | Owner / OP6 track |

---

## 2. Derived Boundary

### 2.1 Physical-store inventory for all included classes

| Included class | Postgres | Redis/cache | Embeddings/vector | Prompt snapshots | Audit/events | Queues | Analytics | Logs/traces | Backups | Derived attributes | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UserPersonalContext (W2) | `users_userpersonalcontext` | none found in read/write path | none found | none found | `AnalyticsEvent` via `emit_personal_data_deleted` | none found | none found | `user_id` in structured logs; query: `grep -n 'user_id' users/personal_data_api.py` | Postgres backups | none found | `users/personal_data_api.py`, `users/personal_context_events.py`, `users/models.py:425-544` |
| Green MemoryEntry (W3) | `identity_memoryentry` | none found in read/write path | none found (ChromaDB only in `apps/kb/`) | none found | `write_audit("memory.forget_entry")`, `write_audit("memory.forget_all_requested")` | none found | none found | `user_id` in structured logs; query: `grep -n 'user_id' apps/identity/services/memory_*.py` | Postgres backups | in-memory prompt block | `apps/identity/models.py:621-838`, `apps/identity/services/memory_deleter.py`, `apps/identity/services/memory_reader.py`, `apps/orchestrator/memory_block.py` |
| ConsentRecord (W3) | `consent_consentrecord` | none found in read/write path | none found | none found | `write_audit("privacy.personal_data_deleted")`; `ConsentRecord` itself is audit trail | none found | none found | `bot_user_id` in audit payload | Postgres backups | none found | `apps/consent/models.py:56-183`, `apps/identity/services/privacy.py:143-157`, `apps/identity/services/privacy.py:229-233` |

### 2.2 Evidence statement

- **ChromaDB:** dependency present in `.venv`, but production code using ChromaDB
  lives only in `apps/kb/` (knowledge-base retrieval). No call path from any
  included class to ChromaDB was found.
- **Redis/Django cache:** general cache usage exists in the repo (eventbus,
  catalog sync, etc.), but none of the three included-class read/write paths use
  cache. Status: `not_applicable_pending_inventory_evidence` for pilot.
- **Prompt snapshots:** `build_concierge_memory_block` constructs the block and
  returns it to the orchestrator; no intermediate persistence was found.
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
- `partially_completed` — каскад завершён с одним или более failed steps;
  retryable.
- `completed` — каскад завершён успешно; все included-классы обработаны.
- `failed` — каскад завершён с не-retryable ошибкой.

**Atomicity requirement:** operation record + scope lock + barrier activation
are created in a single database transaction. If the transaction fails, the
client receives an error and no `operation_id`. There is no externally
observable window between `operation_id` issuance and barrier activation.

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
  ├──► partially_completed  ← есть failed steps
  │      │
  │      ▼ retry
  │   processing
  │
  └──► completed  ← все шаги успешны
         │
         └──► per-class lifecycle продолжается независимо:
                UserPersonalContext: deleted → backup_expired
                MemoryEntry: soft_deleted → primary_purged → backup_expired
                ConsentRecord: withdrawn → retained_under_other_basis
```

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
- Retry после потери success-response: клиент повторяет с тем же
  `idempotency_key`; W3 возвращает финальный результат из idempotency store
  (replay read), не запуская новое execution.
- Срок хранения idempotency record: proposed 7 days after operation completion
  (`owner_decision_required`).
- После завершённой операции повторный запрос возвращает `completed_at` и
  финальный `status` без увеличения `execution_attempt`.

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

### 5.2 Common definitions (`$defs`)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$defs": {
    "subject": {
      "type": "object",
      "additionalProperties": false,
      "required": ["ayla_user_id", "bot_user_id"],
      "properties": {
        "ayla_user_id": {"oneOf": [{"type": "string", "format": "uuid"}, {"type": "null"}]},
        "bot_user_id": {"type": "string", "format": "uuid"}
      }
    },
    "perStepResults": {
      "type": "object",
      "additionalProperties": false,
      "required": ["ayla_delete", "memory_delete", "consent_withdraw"],
      "properties": {
        "ayla_delete": {
          "type": "object",
          "additionalProperties": false,
          "required": ["ok", "detail"],
          "properties": {
            "ok": {"type": "boolean"},
            "detail": {"type": "string", "enum": ["deleted", "already_deleted", "not_linked"]}
          }
        },
        "memory_delete": {
          "type": "object",
          "additionalProperties": false,
          "required": ["ok", "detail"],
          "properties": {
            "ok": {"type": "boolean"},
            "detail": {"type": "string", "enum": ["deleted", "already_deleted", "not_linked"]}
          }
        },
        "consent_withdraw": {
          "type": "object",
          "additionalProperties": false,
          "required": ["ok", "detail"],
          "properties": {
            "ok": {"type": "boolean"},
            "detail": {"type": "string", "enum": ["withdrawn", "already_withdrawn", "not_linked"]}
          }
        }
      }
    },
    "retainedItem": {
      "type": "object",
      "additionalProperties": false,
      "required": ["category", "reason", "lawful_basis", "retention_until", "decision_status", "restrictions", "owner", "deletion_trigger"],
      "properties": {
        "category": {"type": "string", "enum": ["audit_trail", "consent_history", "statutory_record", "backup", "tombstone", "other"]},
        "reason": {"type": "string", "enum": ["regulatory_audit", "withdrawal_evidence", "statutory_retention", "backup_window", "lawful_basis_other"]},
        "lawful_basis": {"oneOf": [{"type": "string"}, {"type": "null"}]},
        "retention_until": {"oneOf": [{"type": "string", "format": "date-time"}, {"type": "null"}]},
        "decision_status": {"type": "string", "enum": ["owner_decision_required", "approved"]},
        "restrictions": {"type": "string", "enum": ["no_personal_values", "read_only", "access_role_restriction"]},
        "owner": {"type": "string"},
        "deletion_trigger": {"type": "string", "enum": ["legal_retention_expiry", "backup_expiry", "owner_decision"]}
      }
    },
    "error": {
      "type": "object",
      "additionalProperties": false,
      "required": ["code", "message", "retryable"],
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
        "message": {"type": "string"},
        "retryable": {"type": "boolean"}
      }
    }
  }
}
```

### 5.3 Export success schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": false,
  "required": ["operation_id", "status", "generated_at", "subject", "format_version", "ayla", "memory", "consents"],
  "properties": {
    "operation_id": {"type": "string", "format": "uuid"},
    "status": {"type": "string", "enum": ["completed"]},
    "generated_at": {"type": "string", "format": "date-time"},
    "subject": {"$ref": "#/$defs/subject"},
    "format_version": {"type": "string", "enum": ["1.0"]},
    "ayla": {
      "oneOf": [
        {"type": "null"},
        {
          "type": "object",
          "additionalProperties": false,
          "required": ["user_id", "exported_at", "profile", "personal_context"],
          "properties": {
            "user_id": {"type": "string", "format": "uuid"},
            "exported_at": {"type": "string", "format": "date-time"},
            "profile": {
              "type": "object",
              "additionalProperties": false,
              "required": ["phone", "email", "full_name", "bio", "city"],
              "properties": {
                "phone": {"oneOf": [{"type": "string"}, {"type": "null"}]},
                "email": {"oneOf": [{"type": "string"}, {"type": "null"}]},
                "full_name": {"oneOf": [{"type": "string"}, {"type": "null"}]},
                "bio": {"oneOf": [{"type": "string"}, {"type": "null"}]},
                "city": {"oneOf": [{"type": "string"}, {"type": "null"}]}
              }
            },
            "personal_context": {
              "description": "opaque_payload: structure governed by UserPersonalContextSerializer; not closed by this schema",
              "oneOf": [{"type": "object", "additionalProperties": true}, {"type": "null"}]
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
        "required": ["id", "kind", "source", "content", "last_inferred_at", "created_at"],
        "properties": {
          "id": {"type": "string", "format": "uuid"},
          "kind": {"type": "string"},
          "source": {"type": "string", "enum": ["explicit", "inferred", "signal"]},
          "content": {
            "description": "opaque_payload: MemoryEntry content structure; not closed by this schema",
            "type": "object",
            "additionalProperties": true
          },
          "last_inferred_at": {"oneOf": [{"type": "string", "format": "date-time"}, {"type": "null"}]},
          "created_at": {"type": "string", "format": "date-time"}
        }
      }
    },
    "consents": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["consent_type", "granted", "document_version", "source", "captured_at", "withdrawn_at", "purpose", "data_categories", "operator", "recipients", "term", "lawful_basis", "identification_method"],
        "properties": {
          "consent_type": {"type": "string"},
          "granted": {"type": "boolean"},
          "document_version": {"type": "string"},
          "source": {"type": "string"},
          "captured_at": {"type": "string", "format": "date-time"},
          "withdrawn_at": {"oneOf": [{"type": "string", "format": "date-time"}, {"type": "null"}]},
          "purpose": {"type": "string"},
          "data_categories": {"type": "array", "items": {"type": "string"}},
          "operator": {"type": "string"},
          "recipients": {"type": "array", "items": {"type": "string"}},
          "term": {"type": "string"},
          "lawful_basis": {"oneOf": [{"type": "string"}, {"type": "null"}]},
          "identification_method": {"type": "string"}
        }
      }
    }
  }
}
```

### 5.4 Export failure schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": false,
  "required": ["operation_id", "status", "format_version", "error"],
  "properties": {
    "operation_id": {"oneOf": [{"type": "string", "format": "uuid"}, {"type": "null"}]},
    "status": {"type": "string", "enum": ["failed"]},
    "format_version": {"type": "string", "enum": ["1.0"]},
    "error": {"$ref": "#/$defs/error"}
  }
}
```

*(Export is all-or-nothing; there is no partial export response in the pilot
contract. Any upstream failure yields the failure schema with HTTP 502/504.)*

### 5.5 Delete success schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": false,
  "required": ["operation_id", "status", "format_version", "subject", "completed_at", "per_step_results", "deleted", "retained"],
  "properties": {
    "operation_id": {"type": "string", "format": "uuid"},
    "status": {"type": "string", "enum": ["completed"]},
    "format_version": {"type": "string", "enum": ["1.0"]},
    "subject": {"$ref": "#/$defs/subject"},
    "completed_at": {"type": "string", "format": "date-time"},
    "per_step_results": {"$ref": "#/$defs/perStepResults"},
    "deleted": {
      "type": "array",
      "items": {"type": "string", "enum": ["ayla_personal_context", "memory_green"]}
    },
    "retained": {
      "type": "array",
      "items": {"$ref": "#/$defs/retainedItem"}
    }
  }
}
```

### 5.6 Delete partial schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": false,
  "required": ["operation_id", "status", "format_version", "subject", "completed_at", "per_step_results", "completed_steps", "failed_steps", "retryable", "request_attempt", "execution_attempt", "retained", "next_action"],
  "properties": {
    "operation_id": {"type": "string", "format": "uuid"},
    "status": {"type": "string", "enum": ["partial"]},
    "format_version": {"type": "string", "enum": ["1.0"]},
    "subject": {"$ref": "#/$defs/subject"},
    "completed_at": {"type": "string", "format": "date-time"},
    "per_step_results": {"$ref": "#/$defs/perStepResults"},
    "completed_steps": {"type": "array", "items": {"type": "string", "enum": ["ayla_delete", "memory_delete", "consent_withdraw"]}},
    "failed_steps": {"type": "array", "items": {"type": "string", "enum": ["ayla_delete", "memory_delete", "consent_withdraw"]}},
    "retryable": {"type": "boolean"},
    "request_attempt": {"type": "integer", "minimum": 1},
    "execution_attempt": {"type": "integer", "minimum": 1},
    "retained": {"type": "array", "items": {"$ref": "#/$defs/retainedItem"}},
    "next_action": {"type": "string", "enum": ["retry_by_user", "contact_support"]}
  }
}
```

### 5.7 Delete failure schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": false,
  "required": ["operation_id", "status", "format_version", "error"],
  "properties": {
    "operation_id": {"oneOf": [{"type": "string", "format": "uuid"}, {"type": "null"}]},
    "status": {"type": "string", "enum": ["failed"]},
    "format_version": {"type": "string", "enum": ["1.0"]},
    "error": {"$ref": "#/$defs/error"}
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
  сейчас возвращает HTTP 404 с телом `{"code":"NOT_FOUND","message":"User not found."}`
  (`users/personal_data_api.py:53-58`).
- **Proposed norm:** после amendment W2 обязан возвращать машинный код
  `subject_gone` в теле ответа для отсутствующего или soft-deleted пользователя:

```json
{
  "code": "subject_gone",
  "subject": { "ayla_user_id": "<uuid>" }
}
```

- Голый HTTP 404 не трактуется W3 как успешное удаление без машинного кода и
  подтверждённой subject correlation.
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
требованиям AMD-020 v0.5.

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

Effective разрешается только после:

- `implementation_status: Verified`;
- полного W6 evidence;
- фиксации версии кода;
- owner activation decision;
- установки `effective_from`.

---

## 13. W6 Acceptance Battery

| # | Scenario | Expected result | Evidence owner |
|---|---|---|---|
| 1 | Concurrent delete | Second request joins the active operation and receives the same `operation_id`; no second destructive execution is created | W6 |
| 2 | Retry after lost success-response | Repeat with same `idempotency_key` returns the final completed/partial status without a new `execution_attempt` | W6 |
| 3 | Failure of each individual step | HTTP 502 with `status: partial`, correct `failed_steps`, and all other steps completed | W6 |
| 4 | Overall deadline between steps | HTTP 504 with `error.code: upstream_timeout`; no partial success returned to client | W6 |
| 5 | Schema mismatch | HTTP 500 with `error.code: schema_mismatch` | W6 |
| 6 | Malformed upstream response | HTTP 502 with `error.code: upstream_malformed` | W6 |
| 7 | Relinking during deletion | Operation is aborted with `error.code: subject_mismatch`; a new operation is required after relink | W6 |
| 8 | Cross-tenant access | HTTP 403 with `error.code: cross_tenant_violation` | W6 |
| 9 | Write UserPersonalContext after barrier | New W2 `UserPersonalContext` row is rejected while the delete operation is active | W6 |
| 10 | Write MemoryEntry after barrier | New green `MemoryEntry` is rejected while the delete operation is active | W6 |
| 11 | Create ConsentRecord after barrier | New `ConsentRecord` is rejected while the delete operation is active | W6 |
| 12 | Inference job after barrier | Inference job that would create green `MemoryEntry` is blocked while the delete operation is active | W6 |
| 13 | Hard purge MemoryEntry | Soft-deleted `MemoryEntry` row is physically removed after `soft_delete_retention` | W6 |
| 14 | Physical wipe UserPersonalContext | `UserPersonalContext` row is removed from W2 primary store immediately on delete | W6 |
| 15 | ConsentRecord withdrawal and retention | Active consents receive `withdrawn_at`; rows remain as audit trail | W6 |
| 16 | Redis cleanup | No Redis keys for included classes are found in read/write path; Redis inventory is documented | W6 |
| 17 | Derived/cache/index cleanup | In-memory prompt block no longer surfaces deleted facts | W6 |
| 18 | Retained manifest | Delete response `retained[]` lists every retained category with reason and `decision_status` | W6 |
| 19 | Audit correlation | All audit rows for the operation share `operation_id` and `correlation_id` | W6 |
| 20 | PII in URL/logs/metrics/traces | No plaintext `ayla_user_id`, `bot_user_id`, phone, email, name, `MemoryEntry.content`, or export body in inspected sinks | W6 |
| 21 | Export of another user | HTTP 403 with `error.code: subject_mismatch` | W6 |
| 22 | Stale initData | HTTP 401 with `error.code: init_data_expired` | W6 |
| 23 | Expired confirmation challenge | HTTP 403 with `error.code: confirmation_expired` | W6 |
| 24 | Nonce reuse | HTTP 409 with `error.code: replay_detected` | W6 |
| 25 | Export after delete | Export returns `ayla.personal_context: null` and `memory: []`; `consents` contains only withdrawn history | W6 |
| 26 | Repeat delete after completion | HTTP 200 delete success response with `status: completed`, empty `deleted[]`, `retained[]` listing audit/consent items, and `per_step_results` showing `already_deleted` / `already_withdrawn` detail codes | W6 |
| 27 | Partial recovery | Retry after upstream recovery completes all remaining steps and returns HTTP 200 `status: completed` | W6 |
| 28 | Backup expiry | After `backup_expiry`, backups no longer contain deleted primary data | W6 |
| 29a | Operation recovery after process crash — resumable | Operation resumes from last persisted state and completes all remaining steps | W6 |
| 29b | Operation recovery after process crash — unrecoverable | Operation returns HTTP 502 `status: partial`; watchdog releases barrier after timeout | W6 |
| 30 | Stuck processing_blocked | Monitoring alert fires; break-glass release requires two authorized operators (W3 on-call + Security) and is audit-logged | W6 |
| 31 | Scope mismatch with same idempotency key | HTTP 409 with `error.code: replay_detected` | W6 |
| 32 | Different idempotency keys for same active operation | Both requests join the same `operation_id`; no second destructive execution | W6 |
| 33 | Export delivery headers | HTTP 200 with `Content-Disposition: attachment; filename="ayla-personal-data-{date}.json"`; no persistent URL | W6 |
| 34 | No subject ID in access logs | No plaintext `ayla_user_id`, `bot_user_id`, phone, email, or name in access logs, traces, or metrics for the operation; pseudonymization uses HMAC digest if present | W6 |
| 35 | Export schema versioning — producer | W3 rejects a response that contains unknown top-level fields for `format_version: "1.0"` | W6 |
| 36 | Partial export failure | HTTP 502 with `error.code: upstream_unavailable`; no partial JSON body is returned | W6 |
| 37 | Fail-closed step-up unavailable | Delete is rejected with HTTP 500 `error.code: internal_error`; no fallback to MaxInitData-only auth | W6 |
| 38 | Legacy audit cleanup | Retention cleanup job removes expired audit rows and preserves rows under statutory hold; dry-run mode first | W6 |
| 39 | Expanded consent history in export | Export `consents[]` includes `purpose`, `data_categories`, `operator`, `recipients`, `term`, `lawful_basis`, and `identification_method` for every record | W6 |

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
| Export delivery filename | Owner feedback v0.3 | filename should not contain subject ID | `implementation_delta` | W3 | update filename pattern | no | yes |
| Export implementation backlog | Owner feedback v0.3/v0.4 review | Export orchestration, serializers, failure/retry, post-forget semantics not fully decomposed | `implementation_delta` | W3 | Add EXP-002…EXP-005 deltas to Implementation Amendment | no | yes |
| Response schema closure | v0.4 review | `personal_context`/`content` are opaque; failure enum was incomplete | `implementation_delta` | W3/Knowledge | Adopt $defs-based schemas; decide opaque payload contract | no | yes |
| Atomic operation creation | v0.4 review | `accepted` state contradicted atomic barrier creation | `proposed_norm` | W3 | Implement single-transaction operation+lock+barrier | no | yes |
| Handoff scope conflicts | 16 handoff files | OP6 / account-deletion promises exceed AMD-020 pilot boundary | `owner_decision_required` | Owner / Product / Legal / OP6 track | Reconcile customer-facing «delete all my data» copy with narrow AMD-020 scope | yes | no |
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
| Response schemas | partial | examples with `...` | examples with `...` | JSON Schema 2020-12 with additionalProperties:false | $defs-based schemas; opaque_payload noted; full error enum; export failure schema added | v0.4 review |
| subject_gone | 404 interpreted | contradiction | implemented/proposed split | explicit fact + proposed norm | same; code fence fixed | v0.4 review |
| Retention manifest | absent | `retained[]` | fake date example | `null` + `owner_decision_required` | same | Owner feedback v0.2/v0.3 |
| Auth/step-up | MaxInitData only | full controls | same | separate idempotency/nonce/correlation | fail-closed rule added; feature flag cannot weaken auth | v0.4 review |
| PII-in-URL | not covered | forbidden but allowed ayla_user_id logging | forbidden but internal URL gap | explicit public/internal rule + DEL-009 | same | Owner feedback v0.3 |
| Audit retention | TBD | structured table | contains_personal_data: no | contains_personal_data: yes + HMAC note | same | Owner feedback v0.3 |
| Error taxonomy | basic | machine codes | internal credential as auth_invalid | internal credential as security incident + safe external code | `init_data_expired` added; upstream codes in failure schema | v0.4 review |
| Idempotency | conceptual | request/execution attempt | request/execution attempt | scope_hash + join behavior | same | Owner feedback v0.3 |
| Readiness gate | minimal | 21 items | 21 items (claimed 13) | 22 items, correctly counted | statuses corrected where v0.4 overclaimed | v0.4 review |
| W6 battery | minimal | 23 scenarios | same | 39 scenarios | ambiguous scenarios split/fixed; expected results made unambiguous | v0.4 review |
| Quality Bar table | absent | absent | absent | included in document | re-graded with honest PASS/FAIL/BLOCKED; no PASS as Draft | v0.4 review |

---

## 17. Document Quality Bar Self-Review

| bar item | PASS/FAIL/BLOCKED/PARTIAL | evidence | document section | unresolved action |
|---|---|---|---|---|
| A1 Честность scope | PASS | Title matches scope; included/excluded tables; split implementation status; conflicts table | §0, §1, §1.3 | — |
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
| F1 Acceptance battery | PARTIAL | 38 scenarios, ambiguous cases split; some scenarios still depend on unresolved decisions | §13 | Finalize decisions blocking C1/D3 before W6 run |
| G1 Нет открытых decisions при сдаче | **FAIL** | Multiple owner/legal/security decisions remain open | §14 | Resolve blocker decisions before final approval |
| G2 Validation | PASS | Repository validator: 0 errors, warnings ≤ baseline | — | Re-run after edits |
| G3 Отчёт по форме | PASS | This section + final agent report | §17 | — |
| H Cross-document consistency | **PASS** | Amendment v0.5 synchronized: generic 404 fallback removed, step-up fail-closed, export backlog added, atomic operation creation aligned | AMD-020 §6, §8.2; Amendment §3, DEL-005, DEL-007, EXP-002…EXP-005 | — |
| I Implementation evidence | PARTIAL | Code evidence cited for key facts; derived inventory, Redis, backup evidence still pending | §2, §8.5 | Collect W6 evidence and inventory after implementation |
| J Writing precision | **PASS** | Code-fence issue fixed; ambiguous W6 results corrected; no placeholders or vague expected results remain | §5, §6, §13 | — |

**Итог Quality Bar:** FAIL/BLOCKED по пунктам B3, C1, D1, D3, G1.
Документ остаётся Draft/Proposed; готов к structured owner decision review, но
**не** к final owner approval, canonicalization или operational activation.

---

## 18. Change Log

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

**Конец документа — AMD-020 v0.5 (Draft, pending owner approval)**
