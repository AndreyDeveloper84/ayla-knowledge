---
node_id: ayla.architecture.memory-context-migration-plan
title: Ayla Memory and Context Migration Plan
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
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
created: 2026-08-19
updated: 2026-08-20
review_cycle: before-major-change
depends_on:
  - "[[Ayla Memory Domain Contract]]"
  - "[[Ayla Context Resolution Contract]]"
  - "[[Consent Scope Registry]]"
related:
  - "[[Ayla Decision Log]]"
  - "[[Ayla Memory Model Specification]]"
---

# Ayla Memory and Context Migration Plan

## 1. Назначение

План перехода от текущего runtime-состояния (аудит 2026-08-19,
перепроверен) к целевой архитектуре [[Ayla Memory Domain Contract]] и
[[Ayla Context Resolution Contract]]. Без big-bang rewrite; каждый шаг —
обратимый, тестируемый, наблюдаемый. Порядок шагов обязателен: шаг N
не начинается, пока шаг N−1 не в эксплуатации (исключения помечены).

Принцип аудита, принятый как норма плана: **строить поверх слоя,
который не исполняется, значит закрепить его нерабочим** — сначала
оживляем/чиним существующее, потом новые сущности.

## 2. Шаги

### Шаг 1 — Live conflict bug (ВЫПОЛНЕН 2026-08-19)

Read-side детерминированный fix в ai-bot-platform: key-policy реестр
(cardinality), выборка актуального факта `explicit > inferred`, затем
latest `created_at`; применён в `orchestrator/memory_block.py` и
`apps/persona/memory_surface.py`. Write path не менялся, миграций нет.

- Rollback: revert diff (изменения изолированы в read path).
- Tests: 5 regression-тестов (explicit correction; inferred не
  вытесняет explicit; multi-value coexist; отсутствие противоречий;
  детерминизм legacy rows).
- Observability: существующие логи write path; метрика отсеянных
  конфликтом строк — при появлении resolver (шаг 5).
- Compatibility: полная; существующий write-тест (2 живые строки
  vegan→keto) сохранён.

### Шаг 2 — Schema-compatible additions (MemoryEntry)

Добавить в `identity.MemoryEntry` nullable/default-поля по
[[Ayla Memory Domain Contract]] §3.1: `status` (default по backfill-правилу),
`updated_at`, `effective_from`, `expires_at`, `superseded_by`,
`supersession_reason`, `source_event_id` (unique где NOT NULL),
`evidence_refs` (JSON, default `[]`), `derivation_method`,
`consent_scope` (nullable), `purpose_tags` (JSON, default `[]`).
Никаких изменений существующих полей и constraints.

- Rollback: миграция обратима (drop columns); read/write path полей не
  требует до шага 3.
- Tests: migration tests (apply/rollback на копии pilot-схемы);
  invariant: существующие строки читаются без изменений поведения.
- Observability: migration duration; count строк по backfill-правилам.
- Compatibility: полная — все поля nullable/с default, код не обязан их
  писать.

### Шаг 3 — Legacy backfill

`status`: `soft_deleted_at IS NULL AND delete_requested_at IS NULL →
active`; `delete_requested_at NOT NULL → deletion_pending`;
`soft_deleted_at NOT NULL → deleted`. `expires_at = created_at +
ttl_days` где задан. `provenance`: `explicit → user_stated`; строки
`inferred`/`signal` — НЕ молчаливая конвертация в
`user_confirmed_inference` (запрещено owner ruling): помечаются
отдельным отчётом, решение по каждой категории — через owner
(в pilot их количество замеряется, ожидается ~0 вне тестов).
`effective_from = created_at`, `updated_at = created_at`.

- Rollback: backfill идемпотентен и ограничен новыми полями; исходные
  поля не трогаются — повторный прогон безопасен.
- Tests: fixture-наборы всех комбинаций legacy-состояний; запрет
  silent migration inferred → confirmed покрыт тестом.
- Observability: отчёт backfill (counts по правилам, anomaly list).
- Compatibility: read path продолжает работать на старых полях до шага 5.

### Шаг 4 — UserPersonalContext → read model

`users.UserPersonalContext` переводится в materialized projection:
источник истины — MemoryEntry (после шага 3) + owning domains;
provenance per field в projection обязателен. Публичный REST, internal
API, мобильный клиент, фронт — без изменений контрактов (трансформация
под ними). Nightly inference-эвристика переводится на запись
proposals/отдельных inferred-записей, не в declared-колонки.
Внутренний API перестаёт принимать `confidence` молча — либо сохраняет
в proposal, либо отклоняет явно.

- Rollback: переключение materialization source за feature flag;
  прежняя таблица сохраняется до конца шага 5.
- Tests: parity-тесты projection vs legacy-таблицы на pilot-данных;
  контрактные тесты внутреннего API.
- Observability: расхождения parity-прогонов (метрика + отчёт).
- Compatibility: внешние контракты неизменны; флаг отката.

### Шаг 5 — Consumer migration на resolve_context

Реализация resolver'а (modular boundary в ai-bot-platform, Context
Resolution Contract §9) и перевод четырёх legacy read paths (§8
контракта) по одному: (2) concierge memory block → (1)
read_personal_context → (4) Ayla personal context hint → (3)
coordinator persistent-часть.

- Rollback: каждый consumer за отдельным flag; resolver read-only
  additive до включения consumers.
- Tests: golden-тесты envelope для каждого consumer; инвариант «нет
  противоречий в envelope»; parity со старым read path на pilot-наборе.
- Observability: retrieval audit events (шаг 11 pipeline) с первого
  включения; latency budget resolver'а.
- Compatibility: старые пути не удаляются до шага 6.

### Шаг 6 — Direct-read prohibition

AST-linter guard (расширение существующего AST-линтера): прямой ORM
`MemoryEntry` вне Memory Service/resolver = ошибка CI. Deprecation
warnings → enforcement. Удаление legacy read path кода.

- Rollback: linter rule отключается конфигом; код legacy paths
  восстанавливается из git.
- Tests: linter fixtures (разрешённые/запрещённые паттерны).
- Observability: нарушения guard в CI (метрика = 0 после миграции).
- Compatibility: требует завершения шага 5 для всех consumers.

### Шаг 7 — Consent integration

Перевод persistent memory на purpose-based authorization по целевой
модели (OD-MEM-4, approved 2026-08-19):

- persistent preference **write** → consent под CSR scope
  `preference_memory` (явное согласие, CSR §5.7);
- persistent **read/use** → соответствующий purpose scope
  (`provider_selection`, `intent_understanding`, …) через authorization
  шаг resolver'а (CSR §6);
- `consent_scope` записывается в MemoryEntry при write;
- sensitivity (green/yellow/red) остаётся отдельной осью и НЕ заменяет
  purpose authorization.

Legacy: `memory_green` — **deprecated**, не выдаётся и не начинает
выдаваться; `personal_data` остаётся базовым privacy/legal consent, где
нормативно требуется, но не purpose authorization. **Legacy gates не
удаляются** до полного перевода consumers и write paths — миграция
backward-compatible и fail-closed (неизвестный/отсутствующий scope →
deny). Реестр согласий остаётся в Consent Domain; physical custodian в
MVP — ai-bot-platform DB (CSR-OD-5, решено 2026-08-19); второй Consent
SoT в beautygo_backend не создаётся.

- Rollback: gate переключается обратно на legacy-поведение флагом;
  consent records append-only, откат не требуется.
- Tests: consent-gated write/read матрица (granted/revoked/missing ×
  zone); revoke → немедленный read gate.
- Observability: authorization deny rate по scope (ожидаемый всплеск
  при включении — baseline до включения).
- Compatibility: legacy gates сохраняются до завершения перевода
  consumers (fail-closed, backward-compatible); тексты согласия
  `preference_memory` не придумываются — Legal/Product input.

### Шаг 8 — Green persistent preference activation

Активация `preference_memory` (CSR §5.7, MVP Phase 2 / §10.2):
proposal-first запись явно подтверждённых предпочтений через полный
pipeline resolver'а. Расширение key/cardinality реестра на
declared-ключи (`preferred_time_slots`, `favorite_masters` — multi,
и пр.) после их регистрации в Memory Domain.

- Rollback: scope остаётся `proposed`/deactivated; записанные факты
  остаются active, но не используются (read gate).
- Tests: end-to-end proposal → confirmation → entry → envelope;
  MemoryCategoryPolicy enforcement.
- Observability: funnel proposal acceptance; retrieval audit coverage.
- Compatibility: требует шагов 5–7; не блокирует MVP Phase 1 (CSR §10.1).

### Шаг 9 — Yellow/red activation gate

НЕ выполняется до одновременной готовности (OR-MEM-6 / Memory Domain
Contract §12): purpose-based authorization (шаг 7), consent check,
sensitivity gate, audit на read+write (шаг 5), единый retrieval
boundary (шаг 5–6), provenance policy (шаг 3–4), lifecycle/conflict
policy (шаг 2–3) — плюс age lookup (#597) и отдельное owner decision.
Исправление age lookup само по себе активацию не открывает.

- Rollback: н/д — шаг является включением, fail-closed остаётся нормой
  до явного решения.
- Tests: полный activation-gate checklist как тестовая матрица.
- Observability: RedZoneAccessLog coverage = 100% red reads/writes.
- Compatibility: green-поведение не затрагивается.

## 3. Зависимости и блокеры вне плана

| Блокер | Шаг | Тип решения |
|---|---|---|
| UX/Legal тексты согласия для `preference_memory` | 7–8 | Legal/Product |
| Age lookup #597 | 9 | Engineering + owner acceptance |

Canonization prerequisite satisfied 2026-08-20 (AYLA-DEC-0081).

Решено 2026-08-19 (не блокеры): OD-MEM-1 (confidence — proposal/audit),
OD-MEM-4 (целевая consent-модель, `memory_green` deprecated), CSR-OD-5
(Consent Domain — canonical owner; physical custodian ai-bot-platform).

Отдельный follow-up вне этого плана (не memory-architecture decision):
sensitive-поля `NutritionProfile` требуют собственного Privacy/Legal
perimeter (classification, encryption, authorization, purposes,
retention, audit); до отдельного решения они запрещены к передаче как
persistent AI context (OD-MEM-2, approved direction 2026-08-19).

## 4. Change Log

### v1.0.3 — 2026-08-20 — Bookkeeping note (non-semantic)

- Step 4 (UserPersonalContext → materialized read model) выполнен в
  beautygo_backend: projection builder с per-field provenance, минимальная
  `PersonalContextProposal` (MDC §3.2), nightly inference отделён от
  declared-колонок (flag `PERSONAL_CONTEXT_INFERENCE_TARGET`, default
  legacy), confidence в internal API — observable deprecation,
  feature flag `PERSONAL_CONTEXT_PROJECTION_SOURCE` (default legacy),
  parity-инструмент. Публичные контракты не изменены.
- Зафиксированные зависимости для Step 5 (не архитектурные решения):
  отсутствует cross-service read-контракт на MemoryEntry
  (ai-bot-platform → beautygo_backend); confirmation flow для proposals
  не реализован; pilot-замеры/parity на pilot-БД не выполнялись (нет
  доступа).
- Каноническая архитектура не изменялась; новых owner decisions не
  вводилось.

### v1.0.2 — 2026-08-20 — Bookkeeping note (non-semantic)

- Step 3.5 = canonical write compatibility выполнен: `write_entry`
  (ai-bot-platform) штампует explicit-записи каноническими полями
  (`status=active`, `provenance=user_stated`, единый write timestamp,
  `expires_at` от `ttl_days`); активных inferred/signal writers нет
  (`record_inferred_green_facts` — 0 prod callers, помечен deprecated);
  schema-миграций не потребовалось; тесты зелёные (1295 passed).
- Каноническая архитектура не изменялась; новых owner decisions не
  вводилось.

### v1.0.1 — 2026-08-20 — Bookkeeping note (non-semantic)

- Step 2.5 provenance schema correction performed because canonical
  provenance field was omitted from initial Step 2 additive migration.
- Execution status: шаг 1 (conflict bug fix), шаг 2 (0015), шаг 2.5
  (0017 `provenance`), шаг 3A (0016 lifecycle/time backfill) и шаг 3B
  (0018 provenance backfill) выполнены в ai-bot-platform; тесты зелёные.
- Каноническая архитектура не изменялась; новых owner decisions не
  вводилось (реализационная коррекция в рамках AYLA-DEC-0081).

### v1.0 — 2026-08-20 — Канонизация

- status: approved / decision_status: accepted / canonical_status:
  approved по CANONIZATION RULING — Memory Domain package (2026-08-20),
  AYLA-DEC-0081; прецедент версии canonical-релиза — AYLA-DEC-0080.
- Содержательных изменений относительно v0.2 нет.

### v0.2 — 2026-08-19 — Reconciliation по owner rulings

- Шаг 7 переписан под approved OD-MEM-4: write → `preference_memory`,
  read/use → purpose scopes; `memory_green` deprecated и не начинает
  выдаваться; legacy gates сохраняются до перевода consumers
  (backward-compatible, fail-closed).
- CSR-OD-5 применён: Consent Domain — canonical owner, physical
  custodian ai-bot-platform, без второго SoT в beautygo_backend.
- §3: OD-MEM-1/OD-MEM-4/CSR-OD-5 убраны из блокеров (решены);
  NutritionProfile perimeter вынесен в отдельный Privacy/Legal
  follow-up (OD-MEM-2), не блокер memory migration.
- Описание текущего legacy runtime сохранено — оно необходимо шагам
  2–5 миграции.

### v0.1 — 2026-08-19 — Initial candidate

- 9 шагов миграции с rollback/tests/observability/compatibility;
  шаг 1 выполнен в день составления; внешние блокеры вынесены в §3.
- Статус: draft/candidate — требует Product Owner review, НЕ канон.

## 5. Approval

**Status:** Approved

**Owner:** Founder / Product Owner

**Approval date:** 2026-08-20

**Decision reference:** CANONIZATION RULING — Memory Domain package,
2026-08-20; зарегистрировано как AYLA-DEC-0081 ([[Ayla Decision Log]],
OWNER_DECISION_REGISTER). Канонизация не является разрешением на
yellow/red activation (OR-MEM-6) и не отменяет follow-up:
UX/Legal тексты `preference_memory`, age lookup #597, NutritionProfile
Privacy/Legal perimeter.
