---
node_id: ayla.architecture.memory-domain-contract
title: Ayla Memory Domain Contract
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
concerns:
  - privacy
  - governance
  - audit
system_owner:
  - ayla-user-context
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
  - "[[Ayla Memory Model Specification]]"
  - "[[Consent Scope Registry]]"
related:
  - "[[AMD-020 Pilot Scope Registry]]"
  - "[[Data Inventory Matrix]]"
  - "[[Ayla Context Resolution Contract]]"
  - "[[ADR-0012 Dynamic User Model]]"
  - "[[Ayla Domain Event Registry]]"
---

# Ayla Memory Domain Contract

## 1. Назначение и нормативность

Этот контракт отвечает на вопрос:

> **Что Ayla знает о пользователе, откуда это взялось, насколько этому
> можно доверять, как это меняется и что считается актуальным?**

Он определяет **физический и логический контракт хранения** persistent
memory: канонический состав `MemoryEntry`, сущности `MemoryProposal` и
`DecisionRecord`, provenance, lifecycle/status, conflict/supersession
rules, cardinality policy, write ownership и delete/revoke semantics.

Граница с соседним каноном:

| Документ | Владеет | Этот контракт |
|---|---|---|
| [[Ayla Memory Model Specification]] (v1.0, approved) | Концептуальная семантика: Proposal ≠ Entry, эпистемика, ownership boundary | Не дублирует; материализует её в поля и состояния |
| AYLA-DEC-0023 ([[Ayla Decision Log]]) | Категориальный whitelist persistent memory | Не расширяет и не пересматривает |
| AYLA-DEC-0024 ([[Ayla Decision Log]]) | Memory Contract на уровне решения: состав полей, retrieval, revocation, supersession, MemoryCategoryPolicy | Этот документ — его storage-level материализация; при расхождении DEC-0024 имеет приоритет до отдельного owner decision |
| [[Consent Scope Registry]] | «Можно ли использовать эти данные этим consumer для этой цели?» | Этот контракт НЕ владеет authorization, consent lifecycle, scopes |
| [[Ayla Context Resolution Contract]] | «Какой разрешённый, актуальный и минимальный context envelope получает consumer?» | Этот контракт НЕ владеет retrieval pipeline |

Этот контракт **не владеет**: consent lifecycle; физическим владением
данными других доменов (booking, nutrition); session/conversation state;
semantic recall (вне MVP).

Статус: approved / accepted / canonical по AYLA-DEC-0081 (2026-08-20) —
см. §16 Approval.

## 2. Owner rulings — входные ограничения

Зафиксированы владельцем 2026-08-19, не переоткрываются:

- **OR-MEM-1.** `MemoryEntry` — канонический source of truth persistent
  memory. Параллельный persistent-memory store не создаётся. Эволюция
  схемы `MemoryEntry` допускается.
- **OR-MEM-2.** `UserPersonalContext` перестаёт быть source of truth
  памяти. Целевая роль: `MemoryEntry → materialization/read model →
  UserPersonalContext` (read model, materialized profile, API/UI
  projection, cache-like representation). Не место, где смешиваются
  declared и inferred values.
- **OR-MEM-3.** Declared и inferred — один Memory Domain, разные записи.
  Различимость canonical entries обеспечивается `provenance`,
  `evidence_refs`, `derivation_method` и lifecycle/status — **без
  `confidence` в MemoryEntry**: после OD-MEM-1 `confidence` существует
  только на уровне MemoryProposal и audit metadata, и это удовлетворяет
  OR-MEM-3. Граница
  «declared = Ayla backend, inferred = ai-bot-platform» — НЕ доменная
  граница. Producers могут физически жить в разных репозиториях;
  canonical persistent memory имеет единый domain contract.
- **OR-MEM-4.** Взаимоисключающие факты не существуют одновременно как
  active бесконечно. Conflict/supersession lifecycle обязателен. Нет
  автоматического supersede для всех новых данных. Минимум три режима:
  explicit correction → supersession; inference vs confirmed/declared →
  proposal/conflict, не молчаливая замена; multi-value key →
  coexistence. Conflict policy — schema/key-aware.
- **OR-MEM-5.** Все consumers persistent memory переводятся на единый
  retrieval boundary `resolve_context(..., purpose)`. Authorization и
  resolution — разные функции (см. [[Ayla Context Resolution Contract]]).
- **OR-MEM-6.** Yellow/red persistent memory не активируется, пока
  одновременно не работают: purpose-based authorization; consent check;
  sensitivity gate; audit; единый retrieval boundary;
  provenance/confidence policy; lifecycle/conflict policy. Исправление
  age lookup само по себе не основание для активации (§12).

## 3. Канонические сущности

### 3.1 MemoryEntry (source of truth, OR-MEM-1)

Каноническая запись persistent memory. Иммутабельна: изменение значения
— только через supersession (§6), никакого update-in-place
(AYLA-DEC-0024).

**Целевой состав полей** и их отображение на текущую runtime-модель
`identity.MemoryEntry` (ai-bot-platform, `apps/identity/models.py`,
проверено 2026-08-19):

| Поле (канон) | Назначение / инвариант | Текущее runtime-соответствие | Gap / миграция |
|---|---|---|---|
| `memory_id` | Стабильный ID записи | `id` (UUID) | — |
| `subject_id` | Субъект данных | `user_id` (UUID, денормализованный) | — |
| `tenant_id` | Тенант-изоляция; `null` = global (blocked по CSR-OD-8) | `source_tenant_id` (nullable) | Семантика source vs scope уточняется при миграции |
| `category` | Категория из whitelist AYLA-DEC-0023; определяет MemoryCategoryPolicy | `kind` (7 choices) + `content.key` | Требуется mapping `kind`/`key` → whitelist category; часть schema-compatible addition |
| `value` | Typed payload: `type`, `payload`, `display_text`; свободный текст как единственная форма запрещён | `content` (EncryptedJSONField `{key, value}`) | Типизация payload — эволюция content schema, backward-compatible (JSON) |
| `sensitivity_zone` | `green | yellow | red` (ADR-0011) | `sensitivity_zone` | — |
| `provenance` | Ровно `user_stated | user_confirmed_inference` (AYLA-DEC-0024) | `source`: `explicit | inferred | signal` | Mapping: `explicit → user_stated`; `inferred`/`signal` не допускаются к persistent write без confirmation (см. §4); legacy-строки — по migration plan |
| `consent_scope` | Scope из CSR, **авторизовавший persistence/write** этой записи (для MVP persistent preferences — `preference_memory`); атрибут записи, НЕ переписывается при read/use | отсутствует; внешние гейты `PERSONAL_DATA` (write) и `memory_green` (read) — оба **legacy** (OD-MEM-4, 2026-08-19): `memory_green` deprecated, `personal_data` не является purpose authorization persistent memory | **Новое поле**, nullable на переходный период; backfill по migration plan |
| `purpose_tags` | Допустимые цели использования (ограничение retrieval) | отсутствует в записи (purpose-теги только в write-path: `discovery:explicit_green_fact`) | **Новое поле**, default `[]` = наследовать от category policy |
| `status` | Lifecycle: `active | superseded | expired | deletion_pending | deleted` | производное: `soft_deleted_at` + `deletion_reason` + `delete_requested_at` | **Новое поле**; backfill: `soft_deleted_at IS NULL → active`; `delete_requested_at NOT NULL → deletion_pending`; `soft_deleted_at NOT NULL → deleted` |
| `created_at` | Время записи | `created_at` | — |
| `updated_at` | Время последнего state transition | отсутствует (`last_used_at` — другое: usage tracking) | **Новое поле**, default = `created_at` |
| `effective_from` | Начало действия факта | отсутствует | **Новое поле**, default = `created_at` |
| `expires_at` | Абсолютный срок действия; обязателен для категорий с TTL | `ttl_days` (относительный) | Вычисляется при backfill: `created_at + ttl_days`; `ttl_days` сохраняется как policy input |
| `superseded_by` | Ссылка на запись-замену | отсутствует | **Новое поле**, nullable |
| `supersession_reason` | `corrected | changed | consolidated | policy_migration` | отсутствует | **Новое поле**, nullable; обязателен при status=superseded |
| `source_event_id` | Идемпотентность записи (unique) | отсутствует | **Новое поле**, nullable; unique где NOT NULL |
| `evidence_refs` | Ссылки на observations (сообщения, события), из которых подтверждён факт | отсутствует | **Новое поле** (JSON list), default `[]` |
| `derivation_method` | Как получен факт (для confirmed inference) | отсутствует | **Новое поле**, nullable; NULL для `user_stated` |
| `deletion metadata` | `delete_requested_at`, `soft_deleted_at`, `deletion_reason` + tombstone по DEC-0024 | есть (`delete_requested_at`, `soft_deleted_at`, `deletion_reason` — 6 choices) | Добавить reason `superseded`? — НЕТ: supersession ≠ deletion (§6); расширение choices — отдельный шаг при вводе `status` |

**Разделение write authorization scope и runtime read purpose.**
`consent_scope` фиксирует, каким scope была авторизована *запись*
(MVP: `preference_memory`), и не меняется в течение жизни записи.
Текущий *read/use purpose* в запись не пишется: он передаётся в
`resolve_context(..., purpose)` и проверяется по CSR на каждом
обращении ([[Ayla Context Resolution Contract]] §5, шаг 3).
Допустимые purposes использования записи ограничиваются
`purpose_tags` и category policy (MemoryCategoryPolicy,
AYLA-DEC-0024) — тремя разными механизмами, которые не смешиваются
в одном поле.

Поля, которые **не добавляются**, и почему:

- `confidence` — **запрещён в canonical MemoryEntry** (AYLA-DEC-0024;
  подтверждено owner ruling OD-MEM-1, 2026-08-19).
  Уверенность — свойство предложения и процесса подтверждения, а не
  подтверждённого факта. Различимость declared/inferred по OR-MEM-3
  обеспечивается `provenance` + `derivation_method` + `evidence_refs`;
  `confidence` живёт в `MemoryProposal` (§3.2) и audit metadata.
  Текущее runtime-расхождение (сериализатор внутреннего API принимает
  `confidence` и молча отбрасывает — `users/internal_personal_context_api.py:70-72,117-121`
  в beautygo_backend) устраняется при миграции внутреннего API на этот
  контракт.
- `valid_until` отдельным от `expires_at` — один механизм истечения,
  не два.
- `storage_scope` / `memory_scope` (`person | tenant | provider`) —
  выводится из category policy (AYLA-DEC-0024), не хранится дублирующим
  полем.

Сохраняемые runtime-механизмы (подтверждены аудитом, соответствуют
контракту): зоны; Fernet-шифрование payload; TTL; soft delete с
причиной; три CHECK-ограничения; RLS для red zone; RedZoneAccessLog
(7 лет).

### 3.2 MemoryProposal

Кандидат на запись. **Единственный путь, которым inference может стать
памятью** (AYLA-DEC-0023 п.2): `user message → model inference →
assistant asks confirmation → explicit user confirmation → proposal →
whitelist check → persist`.

Поля: `proposal_id`, `subject_id`, `tenant_id`, `category`,
`value` (typed, как у MemoryEntry), `provenance: model_inference |
observed_event | imported`, `confidence` (0..1, **здесь допустим**),
`evidence_refs`, `derivation_method`, `status: pending_confirmation |
accepted | rejected | expired`, `expires_at` (TTL предложения; истекает
не позднее завершения сессии), `created_at`, `resolved_at`,
`resulting_memory_id`.

Инварианты: proposal ≠ entry; accepted proposal — новая запись, не
редактирование; молчание ≠ согласие; rejected/expired proposals не
участвуют в retrieval, но хранятся для аудита.

Runtime-статус: **не реализован** (подтверждено аудитом 2026-08-19).

### 3.3 DecisionRecord

Запись решения субъекта о своей памяти: подтверждение, отклонение,
коррекция, запрос удаления, отзыв согласия на scope (ссылка, не
дублирование consent state).

Поля: `decision_id`, `subject_id`, `tenant_id`, `kind: confirm |
reject | correct | delete | revoke_scope | reconfirm`, `target_refs`
(proposal/entry/scope), `channel`, `created_at`, `evidence_ref`
(сообщение/событие, в котором принято решение).

Назначение: доказательная база provenance `user_stated` /
`user_confirmed_inference` и reconfirmation safety constraints
(AYLA-DEC-0024 п.8). Это НЕ telemetry: текущие счётчики пропусков
вопросов и analytics-события DecisionRecord не заменяют.

Runtime-статус: **не реализован**.

## 4. Provenance и различимость declared/inferred (OR-MEM-3)

- Persistent `MemoryEntry` существует только в двух provenance:
  `user_stated` (пользователь сообщил явно) и `user_confirmed_inference`
  (вывод модели, явно подтверждённый пользователем через proposal flow).
- `model_inference`, `observed_event`, `imported` — provenance
  **предложений и session-обработки**, не persistent записей.
- Declared и inferred живут в одном домене, одной таблице, одном
  контракте — различимы по `provenance` (+ `derivation_method`,
  `evidence_refs`). Физическое расположение producers (ai-bot-platform,
  beautygo_backend) не создаёт доменной границы.
- Текущее runtime-расхождение (устраняется по migration plan):
  - `identity.MemoryEntry.source` имеет значения `inferred`/`signal` для
    persistent записей — допустимо только как legacy, новые writes таких
    значений без proposal flow запрещаются;
  - `users.UserPersonalContext` смешивает declared и inferred в одних
    колонках, `data_sources` перезаписывается поключево без истории —
    нарушение OR-MEM-2/3, переводится в read model (§8).

## 5. Lifecycle

```
MemoryProposal: pending_confirmation → accepted | rejected | expired
MemoryEntry:    active → superseded | expired | deletion_pending → deleted
```

- State transitions выполняет только Memory Service (write authority,
  §9). Consumers не меняют состояния.
- `superseded`, `expired`, `deletion_pending`, `deleted` — различные
  терминальные/предтерминальные состояния, не взаимозаменяемы
  (Memory Model Spec, Wave 3 invariants).
- `deletion_pending` — обязательная фаза перед физическим удалением:
  запись уже исключена из retrieval, но удаление идёт по revocation
  pipeline (§10).
- Текущее runtime-соответствие: `active` = `soft_deleted_at IS NULL`;
  `deletion_pending` ≈ `delete_requested_at NOT NULL`;
  `deleted` = `soft_deleted_at NOT NULL` + `deletion_reason`.
  `superseded` и `expired` сегодня не представимы — вводятся полем
  `status` (§3.1) как schema-compatible addition.

## 6. Conflict / supersession (OR-MEM-4)

### 6.1 Правила

1. **Explicit correction.** Пользователь явно исправляет факт
   single-value ключа → атомарно: старая запись → `superseded`
   (`superseded_by`, `supersession_reason: corrected|changed`), новая →
   `active`. Update-in-place запрещён (иммутабельность + история).
2. **Inference vs confirmed/declared.** Вывод модели, конфликтующий с
   active записью, НЕ заменяет её молча: создаётся `MemoryProposal`
   (status `pending_confirmation`), конфликт фиксируется; замена —
   только после explicit confirmation, тогда это п.1.
3. **Multi-value keys.** Допустимые множественные значения сосуществуют
   как независимые active записи; удаление одного значения — обычный
   delete flow, не supersession.

### 6.2 Key/cardinality policy (schema/key-aware)

Машиночитаемый реестр, дополняющий MemoryCategoryPolicy
(AYLA-DEC-0024). Реализация — модуль в Memory Service (не YAML-файл
обязателен; минимальная форма, совместимая с проектом).

Начальный реестр (по фактически существующим ключам, код проверен
2026-08-19):

| `memory_key` | cardinality | При explicit correction | При inferred conflict | Комментарий |
|---|---|---|---|---|
| `diet` | single | supersede | proposal/conflict | Единственный продовый ключ (`apps/persona/memory_extract.py`) |
| (default для незарегистрированных) | single | supersede | proposal/conflict | Консервативный default: не допускаем молчаливых противоречий |

Ключи declared-профиля Ayla (`preferred_time_slots`, `favorite_masters`,
`busy_days`, …) регистрируются при включении в Memory Domain по
migration plan; `favorite_masters` — кандидат в multi-value (coexist).

### 6.3 Retrieval-time гарантия

Resolver НИКОГДА не возвращает одновременно взаимоисключающие active
факты одного single-value ключа (инвариант
[[Ayla Context Resolution Contract]]). До появления поля `status`
действует переходное deterministic правило выборки: приоритет
`explicit > inferred/signal`, затем самый свежий `created_at`,
стабильный tiebreak — реализовано read-side fix 2026-08-19
(ai-bot-platform), задокументировано как interim, не целевое поведение.

## 7. Session vs persistent

- Session memory (Redis-окно сообщений, TTL, аудит без тела) — НЕ
  persistent memory и не регулируется этим контрактом; граница —
  Conversation Domain ([[Ayla Conversation Model Specification]]).
- Запрещены: batch promotion session → persistent, auto-summarization в
  persistent, background copying (AYLA-DEC-0024 п.6). Persistent запись
  — только через §3.1/§3.2 flow.

## 8. UserPersonalContext — целевая роль read model (OR-MEM-2)

- `users.UserPersonalContext` (beautygo_backend) — **materialized read
  model / API/UI projection**, пересобираемая из канонических источников
  (MemoryEntry + declared profile owning domain). Не source of truth.
- В projection каждое поле обязано нести provenance своего источника;
  смешение declared и inferred в одной ячейке без различимого
  provenance запрещено.
- Публичный REST-контракт, внутренний API, мобильный клиент и фронт
  продолжают работать с projection — migration plan сохраняет их
  совместимость (трансформация под ними, не big-bang).
- До миграции документ фиксирует как известное нарушение: перезапись на
  месте без истории; поключевая перезапись `data_sources`;
  детерминированная inference-эвристика (`favorite_masters`,
  `busy_days`, nightly Celery) пишет в те же колонки, что и человек
  (отказ трогать explicit — частичная митигация, не решение).

## 9. Write ownership

- **Memory Service** (логический W3; физически — `apps/identity` в
  ai-bot-platform) — единственный write authority для persistent memory:
  все state transitions, supersession, deletion.
- **ayla-ai-core** — может производить только `MemoryProposal`
  candidates (через ответ orchestrator'у); никакого прямого
  read/write/delete persistent storage (подтверждено: библиотека не
  имеет storage I/O).
- **ai-bot-platform** — orchestration: принимает решения пользователя,
  создаёт proposals, вызывает Memory Service write API.
- **beautygo_backend и другие owning domains** — source of truth своих
  domain facts (booking и т.д.); их факты НЕ становятся persistent
  semantic memory автоматически; в Memory Domain попадают только через
  approved contract (proposal/import с provenance `imported`).
- Запись в yellow/red зоны остаётся fail-closed (текущее поведение
  `_check_minor_protection` — безусловный reject) до activation gate
  §12.

## 10. Delete / revoke semantics

- Удаление по запросу пользователя: `deletion_pending` → distributed
  deletion всех копий и derived artifacts → content-free tombstone
  (4-слойная revocation модель AYLA-DEC-0024 п.5). Повторное согласие
  НЕ восстанавливает записи.
- Отзыв consent по scope: немедленный read gate + тот же pipeline для
  записей этого `consent_scope`. Consent lifecycle сам по себе —
  [[Consent Scope Registry]], здесь не дублируется.
- Forget-all: каскад по всем записям субъекта (существующий 152-ФЗ
  export/forget path — соответствует, сохраняется).
- Удаление memory fact НИКОГДА не удаляет и не изменяет backend source
  of truth (booking и пр.) — и обратное удаление booking-факта не
  трогает память автоматически.
- Self-shot protection: команда стирания не должна на том же ходу
  порождать повторное извлечение того же факта (существующая защита в
  write path — норма для всех будущих extractors).

## 11. Что НЕ является Memory Fact

- Consent state / ConsentRecord — Consent Domain, authorization metadata
  (CSR §10.3); хранение consent как MemoryEntry запрещено.
- Session/conversation state и сами сообщения (`conversations.Message`,
  `ai.Message`) — observations; на них ссылаются `evidence_refs`, они не
  записи памяти.
- Domain facts owning backends (booking, payments, catalog).
- Analytics/telemetry события, счётчики пропусков вопросов.
- `NutritionProfile` — доменные данные nutrition; **не является Memory
  Fact и не переносится в MemoryEntry** (OD-MEM-2, approved direction
  2026-08-19): `NutritionProfile` остаётся source of truth Nutrition
  Domain. Его sensitive-поля (пол, возраст, вес, health flags включая
  беременность/РПП — сегодня без шифрования, зоны и consent) требуют
  отдельного Privacy/Legal perimeter (classification, encryption,
  authorization, permitted purposes, retention, audit) — это follow-up
  вне Memory Domain, а не unresolved memory-architecture decision. До
  отдельного решения sensitive nutrition/health данные **запрещено
  передавать как persistent AI context**.

## 12. Yellow/red activation gate (OR-MEM-6)

Полноценная активация yellow/red persistent memory запрещена, пока
одновременно не работают: purpose-based authorization (CSR runtime);
consent check; sensitivity gate; audit на запись и чтение; единый
retrieval boundary ([[Ayla Context Resolution Contract]]);
provenance policy (§4); lifecycle/conflict policy (§5–§6). До этого —
текущее fail-closed поведение сохраняется и является нормой, а не
багом. Исправление age lookup (#597) — необходимое, но не достаточное
условие.

## 13. Решения владельца (2026-08-19) — закрытые вопросы

Открытых memory-architecture решений не остаётся. Закрыты:

| ID | Решение |
|---|---|
| OD-MEM-1 | **Approved.** `confidence` — свойство MemoryProposal и audit metadata; canonical MemoryEntry числового confidence не содержит (AYLA-DEC-0024). Различимость declared/inferred: `provenance` + `derivation_method` + `evidence_refs` (§3.1, §4) |
| OD-MEM-2 | **Approved direction.** `NutritionProfile` остаётся source of truth Nutrition Domain, в MemoryEntry не переносится; sensitive-поля — отдельный Privacy/Legal perimeter (см. §11); до решения запрещены как persistent AI context. Follow-up вне Memory Domain |
| OD-MEM-3 (= CSR-OD-5) | **Approved.** Canonical owner Consent Records — логический Consent Domain; MVP physical custodian — ai-bot-platform; отдельный consent microservice не создаётся; второй Consent SoT в beautygo_backend запрещён; при необходимости backend получает read-only projection/cache через approved contract |
| OD-MEM-4 | **Approved.** `memory_green` — legacy/deprecated; `personal_data` — только базовый privacy/legal consent, не purpose authorization. Целевая модель: persistent preference write → CSR `preference_memory`; persistent read/use → purpose scope; sensitivity green/yellow/red — отдельная ось. Миграция backward-compatible и fail-closed; legacy gates не удаляются до перевода consumers и write paths |

## 14. Traceability

- Owner rulings: OR-MEM-1…6 (2026-08-19, prompt владельца).
- Канон: AYLA-DEC-0023, AYLA-DEC-0024 ([[Ayla Decision Log]]);
  [[Ayla Memory Model Specification]] v1.0; [[Consent Scope Registry]]
  v1.2+; ADR-0011 (зоны — через [[ADR-0012 Dynamic User Model]], draft,
  словарь ADR-0012 несовместим с этим контрактом по `confidence` —
  нормативен DEC-0024).
- Runtime-факты: `C:/Users/user/PycharmProjects/Ayla/docs/AUDIT_MEMORY_DOMAIN.md`
  (2026-08-19), перепроверены по коду ai-bot-platform
  (`apps/identity`, `apps/consent`, `apps/persona`, `orchestrator`) и
  beautygo_backend (`users`, `ai`, `nutrition`) в тот же день.
- Retrieval boundary: [[Ayla Context Resolution Contract]].

## 15. Change Log

### v1.0 — 2026-08-20 — Канонизация

- status: approved / decision_status: accepted / canonical_status:
  approved по CANONIZATION RULING — Memory Domain package (2026-08-20),
  AYLA-DEC-0081; прецедент версии canonical-релиза — AYLA-DEC-0080.
- Содержательных изменений относительно v0.2 нет.

### v0.2 — 2026-08-19 — Reconciliation по owner rulings

- Применены и закрыты OD-MEM-1…4 (§13): confidence — только
  proposal/audit; NutritionProfile — Nutrition Domain SoT + отдельный
  Privacy/Legal follow-up; Consent Domain — canonical owner consent
  records (CSR-OD-5); целевая purpose-based consent-модель,
  `memory_green` — legacy/deprecated.
- §3.1: поле `consent_scope` — целевое значение CSR scope
  (`preference_memory` для write), legacy-гейты помечены.
- Открытых memory-architecture решений не остаётся; yellow/red
  activation gate (§12) остаётся закрытым.

### v0.1 — 2026-08-19 — Initial candidate

- Первая материализация Memory Domain Contract: канонический состав
  MemoryEntry с runtime-mapping и gap-анализом; MemoryProposal и
  DecisionRecord как целевые сущности; provenance model по DEC-0024;
  lifecycle; key-aware conflict/supersession policy с начальным
  реестром; read model роль UserPersonalContext; write ownership;
  delete/revoke semantics; yellow/red activation gate; OD-MEM-1…4.
- Основание: owner rulings OR-MEM-1…6; аудит памяти 2026-08-19
  (перепроверен по коду); AYLA-DEC-0023/0024; Memory Model Spec v1.0.
- Статус: draft/candidate — требует Product Owner review, НЕ канон.

## 16. Approval

**Status:** Approved

**Owner:** Founder / Product Owner

**Approval date:** 2026-08-20

**Decision reference:** CANONIZATION RULING — Memory Domain package,
2026-08-20; зарегистрировано как AYLA-DEC-0081 ([[Ayla Decision Log]],
OWNER_DECISION_REGISTER). Подтверждены owner rulings OR-MEM-1…6 и
закрытые решения OD-MEM-1…4 / CSR-OD-5. Yellow/red persistent memory
activation этим ruling НЕ разрешён (OR-MEM-6, §12).
