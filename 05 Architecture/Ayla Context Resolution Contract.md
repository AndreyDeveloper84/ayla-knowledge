---
node_id: ayla.architecture.context-resolution-contract
title: Ayla Context Resolution Contract
type: specification
status: approved
decision_status: accepted
canonical_status: approved
version: "1.0"
owner: Product Architecture
priority: P0
knowledge_area:
  - architecture
domain:
  - user-context
  - cross-domain
concerns:
  - privacy
  - governance
  - audit
system_owner:
  - ayla-platform
source_repository: ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: high
data_categories:
  - pii
security_sensitivity: high
ai_indexing: metadata-only
export_policy: metadata-only
created: 2026-08-19
updated: 2026-08-20
review_cycle: before-major-change
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Decision Log]]"
  - "[[Consent Scope Registry]]"
  - "[[Ayla Memory Domain Contract]]"
related:
  - "[[Ayla Memory Model Specification]]"
  - "[[Ayla Conversation Model Specification]]"
  - "[[ADR-0013 Recommendation Snapshot]]"
  - "[[ADR-0014 Conversation Context ID]]"
  - "[[Ayla Domain Event Registry]]"
---

# Ayla Context Resolution Contract

## 1. Назначение и нормативность

Этот контракт отвечает на вопрос:

> **Какой именно разрешённый, актуальный и минимальный context envelope
> consumer получает прямо сейчас?**

Он определяет единый retrieval boundary для persistent memory:

```
resolve_context(subject_id, tenant_id, consumer, purpose, ...) -> ContextEnvelope
```

После завершения миграции прямое чтение persistent memory
consumer-компонентами запрещено архитектурно (OR-MEM-5). До завершения
миграции этот документ — целевой контракт; текущие четыре read paths
(§8) признаны legacy и подлежат переводу.

Граница владения:

| Функция | Владелец |
|---|---|
| «Разрешено ли использование?» (authorization) | [[Consent Scope Registry]] + Consent Domain |
| «Что хранится и что актуально?» (storage, lifecycle) | [[Ayla Memory Domain Contract]] |
| «Какой минимизированный envelope вернуть?» (resolution) | **этот контракт** |
| Session/conversation context | [[Ayla Conversation Model Specification]] (§28–30 Context Projection), [[ADR-0014 Conversation Context ID]] |

Статус: approved / accepted / canonical по AYLA-DEC-0081 (2026-08-20) —
см. §12 Approval.

## 2. Разделение authorization и resolution (OR-MEM-5)

`resolve_context()` и authorization check — НЕ одно и то же:

- **Authorization** отвечает: «разрешено ли использование этих данных
  этим consumer для этой цели и этой операции?» — бинарное решение по
  CSR (fail-closed).
- **Resolver** отвечает: «какой именно минимизированный, актуальный,
  непротиворечивый контекст вернуть?» — выборка, фильтрация,
  conflict resolution, minimization.

Resolver вызывает authorization как шаг pipeline (§5), но не
подменяет его и не дублирует его правила локально. Runtime-компоненты не
могут расширять категории/consumers/операции локальной конфигурацией
(CSR §2 п.7 — распространяется и на resolver).

## 3. Интерфейс

### 3.1 Запрос

Базируется на `MemoryRetrievalRequest` (AYLA-DEC-0024 п.3):

```yaml
subject_id: "<user-id>"            # обязателен
tenant_id: "<tenant-id>"           # обязателен; null (global) — blocked по CSR-OD-8
consumer: ai-bot-platform | beautygo_backend | ayla-ai-core | ayla-analytics
consumer_component: "<optional>"   # информативно
purpose: "<scope_id из CSR>"       # обязателен; неизвестный scope — fail-closed
scope_version: "1.0"
operation: read | model_transfer
requested_categories: [...]        # опционально; пересекается с allowed-for-purpose
session_id: "<optional>"
correlation_id: "<обязателен для аудита>"
```

`purpose` — обязательный параметр первого класса. Вызов без purpose
невозможен по сигнатуре, а не только по политике. `get_all_memory(subject_id)`
запрещён (AYLA-DEC-0024) — API не предоставляет такой операции.

### 3.2 Ответ — ContextEnvelope

```yaml
envelope_id: "<uuid>"
subject_id: "<user-id>"
tenant_id: "<tenant-id>"
purpose: "<scope_id>"
resolved_at: "<timestamp>"
facts:
  - memory_id: "<uuid>"
    category: "<whitelist category>"
    key: "<memory_key>"
    value: { type: ..., payload: ..., display_text: ... }
    provenance: user_stated | user_confirmed_inference
    sensitivity_zone: green | yellow | red
    effective_from: ...
    expires_at: ...
authorization:
  decision: allow | deny
  evaluated_scopes: [...]
  failed_scope_id: "<при deny>"
resolution:
  conflicts_resolved: <int>        # сколько записей отсеяно conflict policy
  filtered_by_status: <int>
  filtered_by_consent: <int>
  filtered_by_freshness: <int>
  minimized_from: <int>            # кандидатов до минимизации
audit_ref: "<retrieval audit event id>"
```

Принципы envelope: только `active`, непротиворечивые, разрешённые,
свежие, минимально необходимые для purpose факты; provenance сохраняется
для consumer; никаких сырых записей хранилища, tombstone'ов,
`deletion_pending`, proposals. Deny — атомарный (partial read не
поддерживается в MVP, CSR §6 Edge Cases): при deny envelope фактов не
содержит.

## 4. Инварианты

1. **Fail-closed**: любая ошибка authorization, неизвестный
   scope/purpose, сбой sensitivity gate → deny, а не частичный ответ.
2. **Нет противоречий**: envelope никогда не содержит одновременно
   взаимоисключающие active факты одного single-value ключа
   ([[Ayla Memory Domain Contract]] §6).
3. **Provenance прозрачен**: consumer видит provenance каждого факта;
   inference-derived данные не маскируются под declared.
4. **Минимизация**: возвращается только необходимое для purpose
   (CSR §2 п.8).
5. **Аудируемость**: каждый retrieval — audit event (§7), включая deny.
6. **Детерминизм**: одинаковый запрос на одинаковом состоянии даёт
   одинаковый envelope (стабильные tiebreaks).
7. **Нет обхода**: `ayla-ai-core` получает ТОЛЬКО готовый
   ContextEnvelope (`model_transfer`) и не обращается к persistent
   storage ни напрямую, ни через обходные вызовы (CSR §3 `operation`).

## 5. Pipeline (12 шагов)

Каждый вызов `resolve_context` выполняет:

1. **Validate subject/tenant/request** — обязательные поля, tenant
   isolation, global scope blocked (CSR-OD-8).
2. **Determine purpose/scope** — resolve `purpose` → scope из CSR;
   неизвестный/просроченный/неутверждённый → deny (fail-closed).
3. **Authorization check** — вызов authorization по CSR §6 (включая
   dependent scopes при `context_mode: persistent`).
4. **Sensitivity check** — zone gate: green — по scope; yellow/red —
   только если activation gate Memory Domain Contract §12 пройден
   (сейчас — fail-closed норма).
5. **Retrieve candidates** — чтение MemoryEntry через Memory Service
   (единственная точка ORM-доступа), отсекая physically deleted.
6. **Filter by memory status** — только `active` (после введения поля
   `status`; сейчас — `soft_deleted_at IS NULL AND delete_requested_at
   IS NULL`).
7. **Resolve conflicts/supersession** — key-aware policy
   (Memory Domain Contract §6): single-value → один актуальный факт;
   multi-value → coexistence; детерминированные tiebreaks.
8. **Apply provenance rules** — приоритет
   `user_stated > user_confirmed_inference` при коллизиях; provenance
   сохраняется в envelope. Resolver работает с canonical MemoryEntry и
   не использует числовой `confidence` — его нет в MemoryEntry
   (AYLA-DEC-0024 / OD-MEM-1); confidence не добавляется в envelope.
9. **Apply freshness/validity** — `effective_from <= now`, не истёк
   `expires_at`/TTL.
10. **Apply relevance/minimization** — пересечение requested ∩
    allowed-for-purpose ∩ необходимое для purpose.
11. **Audit decision/use** — retrieval audit event (§7) до возврата.
12. **Return ContextEnvelope** (§3.2).

Шаги 3–4 выполняются ДО чтения кандидатов (данные не читаются без
разрешения); шаги 5–10 — чистые функции над кандидатами; шаг 11
обязателен при любом исходе.

## 6. Consumer matrix

| Consumer | Доступ | Механизм |
|---|---|---|
| `ai-bot-platform` (orchestration) | `read` — вызывает resolve_context, строит и минимизирует envelope | Retrieval boundary размещается здесь (modular boundary, не отдельный микросервис) |
| `beautygo_backend` | `read` — через resolve_context для своих сценариев; declared profile отдаёт по approved internal API до миграции | Internal API с Bearer (существующий), переводится на envelope по migration plan |
| `ayla-ai-core` | `model_transfer` — только готовый ContextEnvelope | Библиотека без storage I/O (подтверждено кодом); получает envelope аргументом |
| `ayla-analytics` | по scope `recommendation_measurement` | `blocked` (CSR-OD-1/9) |

`RedZoneReader` (ai-bot-platform, `apps/identity/services/red_zone_reader.py`)
— действующий прототип этого контракта для red zone: обязательные
purpose, subject, request id, атомарный аудит, RLS-GUC. Единый resolver
обобщает эту модель на все зоны, а не заменяет её параллельным
механизмом.

## 7. Audit

Каждый retrieval порождает audit event с: `correlation_id`, subject,
tenant, consumer, purpose, decision, счётчики фильтрации (без содержимого
фактов), `envelope_id`. Именование событий — lowercase dot-separated по
AYLA-DEC-0025 и [[Ayla Domain Event Registry]]; конкретные имена
(`memory.context_resolved` / `memory.context_resolution_denied` или
эквивалент) регистрируются в DER при реализации — этот контракт не
узурпирует владение DER.

Текущий gap (фиксируется, закрывается migration plan): чтение green
zone сегодня не аудируется вообще; аудит существует только для red zone
(RedZoneAccessLog) и записей.

## 8. Legacy read paths (подлежат переводу)

Подтверждены аудитом 2026-08-19, ни один не принимает purpose:

| # | Путь | Расположение | Целевое состояние |
|---|---|---|---|
| 1 | `read_personal_context()` | ai-bot-platform, `apps/identity/services/memory_reader.py` (прямой ORM) | Внутренность шага 5 resolver'а |
| 2 | `build_concierge_memory_block()` | ai-bot-platform, `orchestrator/memory_block.py` (HTTP в Ayla + MemoryEntry) | Consumer resolve_context |
| 3 | `coordinator.load_snapshot()` | ai-bot-platform, `orchestrator/memory/coordinator.py` (Redis + profile + slots; про MemoryEntry не знает) | Session-часть остаётся в Conversation Domain; persistent-часть — через resolve_context |
| 4 | `ChatService._build_personal_context_hint()` | beautygo_backend, `ai/application/services/chat_service.py` (прямой ORM) | Consumer envelope |

Запрет прямого чтения вводится после миграции consumers: сначала
deprecation + linter/AST-guard (расширение существующего AST-линтера),
затем enforcement. Big-bang запрет без миграции consumers запрещён.

## 9. Размещение

Единый resolver — **modular boundary внутри ai-bot-platform** (рядом с
Memory Service / `apps/identity`), не отдельный микросервис. Extraction
в отдельный сервис — только при доказанной необходимости (нагрузка,
границы деплоя), отдельным решением.

## 10. Traceability

- OR-MEM-5, OR-MEM-6 (owner rulings 2026-08-19).
- AYLA-DEC-0024 п.3 (MemoryRetrievalRequest, запрет get_all_memory,
  аудируемость), AYLA-DEC-0025 (именование событий) — [[Ayla Decision Log]].
- [[Consent Scope Registry]] §3 (`operation`, read vs model_transfer),
  §5–6 (authorization contract, dependent scopes, edge cases).
- [[Ayla Memory Domain Contract]] (status, conflicts, provenance,
  freshness — правила шагов 6–10).
- [[Ayla Conversation Model Specification]] §28–30 (Context Projection —
  концептуальная рамка), [[ADR-0013 Recommendation Snapshot]],
  [[ADR-0014 Conversation Context ID]] (session-scoped resolve, не
  дублируется).
- Runtime-факты: AUDIT_MEMORY_DOMAIN.md (2026-08-19), перепроверен.

## 11. Change Log

### v1.0 — 2026-08-20 — Канонизация

- status: approved / decision_status: accepted / canonical_status:
  approved по CANONIZATION RULING — Memory Domain package (2026-08-20),
  AYLA-DEC-0081; прецедент версии canonical-релиза — AYLA-DEC-0080.
- Содержательных изменений относительно v0.2 нет.

### v0.2 — 2026-08-19 — Reconciliation по owner rulings

- Применены owner rulings 2026-08-19: OD-MEM-1 (confidence — только
  proposal/audit), CSR-OD-5 (Consent Domain — canonical owner consent
  records; physical custodian в MVP — ai-bot-platform; без второго SoT в
  beautygo_backend), OD-MEM-4 (purpose-based authorization;
  `memory_green` — legacy/deprecated). Нормативных изменений контракта
  не потребовалось — он уже соответствовал rulings; проверена
  терминология и граница authorization (CSR) vs resolution (этот
  документ): дублирования нет.
- Yellow/red activation gate остаётся закрытым (OR-MEM-6).

### v0.1 — 2026-08-19 — Initial candidate

- Единый retrieval boundary `resolve_context(..., purpose)`: интерфейс,
  ContextEnvelope, 7 инвариантов, 12-шаговый pipeline, consumer matrix,
  audit, реестр legacy read paths, размещение (modular boundary).
- Основание: OR-MEM-5/6; AYLA-DEC-0024; CSR v1.2; RedZoneReader как
  прототип; аудит 2026-08-19 (перепроверен).
- Статус: draft/candidate — требует Product Owner review, НЕ канон.

## 12. Approval

**Status:** Approved

**Owner:** Founder / Product Owner

**Approval date:** 2026-08-20

**Decision reference:** CANONIZATION RULING — Memory Domain package,
2026-08-20; зарегистрировано как AYLA-DEC-0081 ([[Ayla Decision Log]],
OWNER_DECISION_REGISTER). Подтверждены owner rulings OR-MEM-1…6,
включая OR-MEM-5 (единый retrieval boundary) и OR-MEM-6 (yellow/red
остаются fail-closed до полного activation gate).
