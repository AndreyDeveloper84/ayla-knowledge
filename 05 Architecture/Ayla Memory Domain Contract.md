---
node_id: ayla.architecture.memory-domain-contract
title: Ayla Memory Domain Contract
type: specification
status: approved
decision_status: accepted
canonical_status: approved
version: "1.1"
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
updated: 2026-09-21
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
  - "[[OWNER_DECISION_REGISTER]]"
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
- Для `kind=allergy` AYLA-DEC-0100 определяет, как хранится запись
  (§12.1). Условия activation gate на 21.09.2026 выполнены частично
  (4 из 24, §12.1); запись аллергий не активируется, пока не выполнены
  все, либо пока владелец явно не примет предел. До этого fail-closed
  по пункту выше действует и для аллергий.

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

### 12.1 `kind=allergy` — red-хранение по AYLA-DEC-0100 и состояние условий активации

**Норма.** AYLA-DEC-0100 определяет, **как** хранится аллергия: категория
`allergy` и scope `allergy_safety_filter` по [[Consent Scope Registry]]
v1.5 §4 и §5.9, зона `red`, правила записи ниже. Решение исходило из
того, что условия §12 (OR-MEM-6) для этого вида записи выполнены
(«Для kind=allergy условия MDC §12 объявляются выполненными»). Сверка
кода `ai-bot-platform@0e2c0100` эту посылку не подтвердила: из 24
условий таблицы ниже механизмом выполнены 4, ещё 6 — частично, одно
есть в схеме, но не действует (п. 7), 12 не выполнены, одно открыто
(п. 24). Решение этим не отменяется: срок включения записи определяют
условия, а не решение. Расхождение показано владельцу (тело PR KB-D).

- аллергия хранится в зоне `red` (перекрывает `yellow` из ADR-0012 для
  этого вида записи — [[Consent Scope Registry]] §11.1);
- все прочие yellow/red записи — по §12 без изменений, fail-closed
  сохраняется;
- **запись аллергий не активируется, пока не выполнены все условия
  таблицы, либо пока владелец явно не примет предел.** Большая часть
  невыполненных условий — работа DRF-2132; п. 7 — переход на
  не-суперпользовательскую роль БД `ayla_app` (ADR-0011 §16, фаза 2,
  шаг 5). Правило «активация только по завершении DRF-2132» следует из
  §12 v1.0 и остаётся до подтверждения владельцем в PR. Статус
  DRF-2132 по брифу ред. 2 — Backlog; в Linear не проверялся.

**Правила записи аллергии** (AYLA-DEC-0100; подробности — бриф ред. 2,
M-1):

- фраза распознаётся только как кандидат; Ayla показывает распознанную
  формулировку и спрашивает отдельное явное согласие на эту запись;
- до сохранения человек один раз называет дату рождения. Это
  самодекларация; запись разрешена только при статусе
  `adult_eligibility_asserted`. Без даты или при возрасте младше 18
  запись не создаётся. Норма — [[Consent Scope Registry]] §2 п. 11;
- provenance — только `user_stated`: опора — §4 (provenance) и
  AYLA-DEC-0100 «фраза распознаётся только как кандидат; Ayla
  показывает распознанную формулировку» — из этого `inferred` без
  подтверждения исключён; второй источник — журнал главного окна §52
  «Что не меняется». Выведенное (`inferred`) аллергией не записывается;
- для обработки аллергию читают ровно двое: фильтр состава в
  рекомендациях и предупреждение сканера. Кроме них — только права
  субъекта над собственной записью: показ («Что Ayla помнит»), экспорт,
  удаление; каждое такое чтение тоже журналируется
  (`memory.allergy.accessed`). В текст для модели аллергия не попадает,
  во внешнюю LLM не передаётся;
- результат фильтра при неизвестном или неполном составе — `UNKNOWN`.
  Гарантий безопасности по одному отсутствию найденного аллергена нет;
- каждое чтение и каждый отказ журналируются
  (`memory.allergy.accessed`, `memory.allergy.access_denied`); запись и
  удаление — `memory.allergy.recorded` / `memory.allergy.forgotten`.
  Содержания в событиях нет. Имена предлагаются к регистрации в
  [[Ayla Domain Event Registry]] (KB-E, DRF-2263);
- «Забудь аллергии» и «Забудь всё» удаляют запись (§10); экспорт её
  отдаёт;
- срок хранения — без TTL (журнал главного окна §52 В1: «без TTL (kind
  без срока)»; бриф ред. 2, M-1 вариант (а)).

**Условия §12 и дополнительные условия AYLA-DEC-0100 для `kind=allergy`.**
Ссылки — `ai-bot-platform@0e2c0100`, если не указано иное.

| # | Условие | Механизм runtime | Состояние |
|---|---|---|---|
| 1 | Sensitivity gate: зона записи | `MemoryEntry.sensitivity_zone` с `red` — `apps/identity/models.py:833-840, 939-945` | **Выполнено механизмом** |
| 2 | Вид записи `allergy` | В `MemoryEntry.KIND_CHOICES` значения для аллергии нет: `preference`, `contraindication`, `symptom`, `lifestyle`, `relationship`, `financial`, `other` — `apps/identity/models.py:851-859` | **Требует DRF-2132** (выбрать или добавить `kind`) |
| 3 | Consent check на запись red | DB CHECK `memory_entry_yellow_red_requires_consent`: живая red-строка обязана иметь `consent_at` — `apps/identity/migrations/0007_user_personal_context.py:84-96`; поле `apps/identity/models.py:1000-1009` | **Частично**: БД не даёт создать живую red-строку без метки `consent_at` — это наличие метки, а не проверка согласия. Проверки согласия по scope `allergy_safety_filter` (связи с `ConsentRecord`) и отзыва нет: отзыв «NOT modeled as setting consent_at=NULL on a live row» (`models.py:1000-1009`) — **не выполнено → требует DRF-2132** (`CSR-OD-15`) |
| 4 | Показ формулировки и отдельное per-entry согласие в диалоге | Сбора согласия на аллергию нет; извлечение фразы выбрасывается — `apps/persona/memory_extract.py:425-437` (`allergy_clause_dropped`) | **Требует DRF-2132** |
| 5 | Защита несовершеннолетних, fail-closed | `write_entry` для yellow/red: `minor_lock` → отказ; `_check_minor_protection` → отказ и строка `write_rejected_dob_lookup` — `apps/identity/services/memory_writer.py:168-183`; тот же гейт на `promote_zone` — `:263-293`; `minor_lock` — `apps/identity/models.py:786` | **Fail-closed выполнено механизмом** |
| 6 | Разрешающая ветка возраста: `adult_eligibility_asserted` из даты рождения | Заглушка `_check_minor_protection` всегда бросает (`apps/identity/services/memory_writer.py:66-87`, #597) — любая red-запись отклоняется. Даты рождения в каталоге нет: `git grep -iE "date_of_birth|birth_date|\bdob\b"` по `*.py` вне тестов @`4dbff523` — 0 вхождений. Есть только `NutritionProfile.age` — `djangoproject:nutrition/models.py:481` | **Требует DRF-2132 и работы по дате рождения.** По брифу — «плюс 2–3 SP возраст»; лист не назван |
| 7 | Изоляция чтения red на уровне БД | RLS-политика `memory_entry_non_red_visible` (`AS RESTRICTIVE FOR SELECT`, видимость red только при UUID в GUC) + `FORCE ROW LEVEL SECURITY` — `apps/identity/migrations/0008_red_zone_db_security.py:162-194`; безопасное представление для ops без red — `:150-158`, `:225` | **Механизм в схеме есть, не действует.** Приложение подключается суперпользователем контейнера `platform`, и RLS обходится: «Сегодня приложение ходит под ``platform`` — суперпользователем контейнера, он RLS обходит» — `apps/identity/services/memory_deleter.py:135-137`; `POSTGRES_USER: platform` — `docker-compose.yml:44`, `docker-compose.staging.yml:41`. **Не выполнено → переход на не-суперпользовательскую роль БД `ayla_app` (ADR-0011 §16, фаза 2, шаг 5)**; см. примечание 1 |
| 8 | Единственный санкционированный читатель | `RedZoneReader.read` — GUC, проверка владельца, cross-tenant, audit-строка в той же транзакции — `apps/identity/services/red_zone_reader.py:81-185`; экран субъекта — `list_live_for_subject` `:192`, `soft_delete_for_subject` `:248` | **Частично**: механизм есть (GUC, проверка владельца, аудит в одной транзакции). Строка выбирается `MemoryEntry.objects.get(id=entry_id, user_id=user_id)` (`red_zone_reader.py:149`) — без фильтра `soft_deleted_at`/`status` и без проверки `consent_at`; проверка тенанта — только если вызывающий передал `expected_source_tenant_id` (`:155`). Забытая или отозванная запись читается (см. п. 12, п. 20) — **не выполнено → требует DRF-2132** |
| 9 | CI-сторож прямых запросов к red | `tools/lint/red_zone_guard.py:1-40` (allowlist: reader, writer, deleter); запуск в CI — `.github/workflows/ci.yml:482` | **Выполнено механизмом** (литеральные запросы; пределы — раздел KNOWN LIMITATIONS в docstring сторожа: `.exclude(...)`, переменные, raw SQL, `**{}` не ловятся. Утверждение docstring о действии RLS на суперпользователя неверно — см. п. 7) |
| 10 | Audit чтения | `RedZoneAccessLog` — INSERT-only, 7 лет: `apps/identity/models.py:1183-1189`; права только `SELECT, INSERT` — `0008_red_zone_db_security.py:220-221`; строка `read` — `red_zone_reader.py:163-173` | **Частично**: журнал есть (`RedZoneAccessLog`, INSERT-only). Ролей читателя `recommendations` / `scanner` в `ACCESSOR_ROLE_CHOICES` нет (`ayla_llm`, `system_job`, `ops_admin`, `data_subject` — `models.py:1201-1213`); события `memory.allergy.accessed` нет (см. п. 12) — **не выполнено → требует DRF-2132** |
| 11 | Audit записи | `ACCESS_WRITE` объявлен (`apps/identity/models.py:1216, 1224`), но в production-коде его никто не пишет: `git grep ACCESS_WRITE\b` вне tests/migrations — только объявление. Пишется лишь отказ `write_rejected_dob_lookup` (`memory_writer.py:95-120`) | **Требует DRF-2132** |
| 12 | Audit отказа (`memory.allergy.access_denied`) | Отказ в `RedZoneReader.read` откатывает транзакцию без audit-строки — по замыслу «no orphan log», `red_zone_reader.py:19-25, 145-148`. Значения `access_type` для отказа нет — `apps/identity/models.py:1215-1232`. Событий `memory.allergy.*` в коде нет (`git grep` — 0) | **Требует DRF-2132** |
| 13 | Purpose-based authorization: для обработки читают только рекомендации и сканер; кроме них — доступ субъекта (показ, экспорт, удаление) с журналом | `purpose` в `RedZoneReader.read` — свободная строка, не проверяется (`red_zone_reader.py:92, 105`). Runtime authorization layer из [[Consent Scope Registry]] §6 в боте отсутствует (`git grep -E "resolve_context|scope_id"` вне tests — 0 соответствий) | **Требует DRF-2132**: закрытый перечень purpose (`recommendations`, `scanner` + доступ субъекта к своей записи) с отказом и журналом |
| 14 | В текст для модели не попадает | Роль `ayla_llm` («Ayla LLM prompt construction») разрешена для чтения red — `apps/identity/models.py:1201, 1209`; запрета для аллергий нет | **Требует DRF-2132** (запрет и сторож) |
| 15 | Единый retrieval boundary (OR-MEM-5) | `resolve_context` в боте отсутствует (см. п. 13) | Для аллергии узкий эквивалент — п. 8 + п. 13 (**требует DRF-2132**). Требуется ли общий `resolve_context` — открытый вопрос, см. ниже |
| 16 | Provenance policy (§4) | `write_entry` ставит `provenance=user_stated` и `status=active` для explicit-записи — `apps/identity/services/memory_writer.py:185-204`; поле — `apps/identity/models.py:1128-1139` | **Частично**: explicit-запись получает `user_stated`. `write_entry` принимает `source="inferred"` для любой зоны, включая red; гейт red (`memory_writer.py:169-183`) проверяет только возраст. Запрет inferred/signal для `allergy` — **не выполнено → требует DRF-2132** |
| 17 | Lifecycle (§5) | Поле `status` — `apps/identity/models.py:1042-1050`; soft delete с причиной — `:861-880, 1010-1031` | **Частично**: поле и soft delete есть; код поле не читает — help-text «runtime logic does not read it yet» (`models.py:1048-1049`), читатель статус не учитывает (п. 8) — **не выполнено → требует DRF-2132** |
| 18 | Conflict/supersession (§6) | `supersede_entries` — `apps/identity/services/memory_writer.py:221-260`. Ключа аллергии в реестре §6.2 нет; кардинальность не решена | **Частично**: механизм есть; **регистрация ключа — требует DRF-2132**, кардинальность — открытый вопрос |
| 19 | Срок хранения без TTL | `ttl_days` передаёт вызывающий (`memory_writer.py:162, 216`); по описанию модели red по умолчанию — 90 дней (`apps/identity/models.py:819-822, 994-999`). Вызывающего для аллергии нет | **Требует DRF-2132** |
| 20 | «Забудь всё» удаляет аллергию | `soft_delete_all_zones_for_forget_all` охватывает red с журналом — `apps/identity/services/memory_deleter.py:110-247`; надгробие и журнал `delete` в одной транзакции — `:171-196` | **Выполнено механизмом** (надгробие + журнал; физическая очистка через 30 дней — `models.py:1019-1021`; в эти 30 дней строку достаёт читатель — п. 8) |
| 21 | «Забудь аллергии» | Команды нет: `git grep -i "забудь аллерг"` — 0 | **Требует DRF-2132** |
| 22 | Экспорт отдаёт аллергию | Red-зона сейчас исключена из выгрузки: «Добавление её в выгрузку — отдельное решение владельца» — `apps/identity/export_coverage.py:196-201` | Решение дано AYLA-DEC-0100; **в коде не сделано** — DRF-2132 / DRF-2214, лист уточнить |
| 23 | Фильтр `CONFLICT` / `NO_CONFLICT_FOUND` / `UNKNOWN` и предупреждение сканера | `git grep NO_CONFLICT_FOUND` — 0 в боте @`0e2c0100` и в каталоге @`4dbff523` | **Требует DRF-2132** |
| 24 | Каталожный вход `allergies` / `allergies_vague` без согласия и возраста | `djangoproject:nutrition/serializers.py:503-510` @`4dbff523` | Не закрыт; открытый вопрос `CSR-OD-12` [[Consent Scope Registry]] |

**Примечание 1 (п. 7).**

- В спецификации механизм назывался «BEFORE SELECT trigger». В Postgres
  такого нет; реализовано RLS-политикой с эквивалентной семантикой —
  `0008_red_zone_db_security.py:36-49`.
- На SQLite миграция — no-op (`:67-68`).
- RLS не действует для суперпользователя и ролей с `BYPASSRLS`. Код
  сам называет роль: «Сегодня приложение ходит под ``platform`` —
  суперпользователем контейнера, он RLS обходит» —
  `apps/identity/services/memory_deleter.py:135-137` @`0e2c0100`;
  `POSTGRES_USER: platform` — `docker-compose.yml:44`,
  `docker-compose.staging.yml:41`. Значит, изоляция п. 7 сегодня не
  действует; она заработает только после перехода на
  не-суперпользовательскую роль `ayla_app` (ADR-0011 §16, фаза 2,
  шаг 5). Роль на стенде пилота этап не читал (вне полномочий); ссылки
  выше — из кода и compose.

**Итог.** Для `kind=allergy` условия активации red на 21.09.2026
выполнены частично (**4 из 24**); запись аллергий не активируется, пока
не выполнены все, либо пока владелец явно не примет предел.

- Выполнены механизмом (4): 1, 5 (fail-closed), 9, 20.
- Частично (6): 3, 8, 10, 16, 17, 18 — недостающая часть требует
  DRF-2132.
- Механизм в схеме есть, не действует (1): 7 — переход на `ayla_app`
  (ADR-0011 §16, фаза 2, шаг 5).
- Не выполнены, требуют DRF-2132 (12): 2, 4, 6 (и работа по дате
  рождения), 11–15, 19, 21–23.
- Открыт (1): 24 (`CSR-OD-12`).

**Открытые вопросы (не решены AYLA-DEC-0100).**

- Нужен ли общий `resolve_context` (OR-MEM-5) для аллергии, или
  достаточно узкого читателя с закрытым перечнем purpose (п. 15).
- Кардинальность ключа аллергии (single / multi-value) в реестре §6.2.
- `MemoryEntry` глобальна по человеку, а [[Consent Scope Registry]] §6
  держит global scope в `blocked` — `CSR-OD-10`.
- Закрытый словарь `reason_code` результата фильтра
  (`allergy-filter-result.schema.json`) — `CSR-OD-17`.

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
- v1.1: AYLA-DEC-0100 ([[OWNER_DECISION_REGISTER]], партия DRF-2259,
  2026-09-21); [[Consent Scope Registry]] v1.5 §4, §5.9, §2 п. 11;
  runtime-ссылки §12.1 — `ai-bot-platform@0e2c0100`,
  `djangoproject@4dbff523`.

## 15. Change Log

### v1.1 — 2026-09-21 — Amendment §12: red-активация для kind=allergy (AYLA-DEC-0100)

- §12.1 (новый): AYLA-DEC-0100 определяет, как хранится аллергия
  (red, категория `allergy`, scope `allergy_safety_filter`). Правила
  записи аллергии: кандидат → показ формулировки → отдельное per-entry
  согласие → дата рождения (самодекларация, `adult_eligibility_asserted`);
  только `user_stated`; для обработки читают только фильтр рекомендаций
  и сканер, плюс доступ субъекта (показ, экспорт, удаление) с журналом;
  не в текст модели; `UNKNOWN` при неполном составе; журнал
  `memory.allergy.*`; «Забудь аллергии» / «Забудь всё»; экспорт; без TTL.
- §12.1: перечень 24 условий с механизмами runtime
  (`repo:путь:строка`). Посылка решения «условия выполнены» сверкой кода
  @`0e2c0100` не подтвердилась: выполнено механизмом 4 из 24, частично
  6, п. 7 (RLS) в схеме есть, но не действует — приложение ходит
  суперпользователем `platform`. Запись аллергий не активируется, пока
  не выполнены все условия, либо пока владелец явно не примет предел.
- §9: ссылка на §12.1. Прочие yellow/red — без изменений; fail-closed
  сохраняется.
- Статус документа не изменён (approved / accepted / approved).

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

**Amendment v1.1 (2026-09-21):** AYLA-DEC-0100 — для `kind=allergy`
определено red-хранение (§12.1); условия активации выполнены частично
(4 из 24), запись не активируется, пока не выполнены все, либо пока
владелец явно не примет предел. Для прочих yellow/red activation
по-прежнему не разрешён.
