---
node_id: ayla.domain.core-domain-model

title: Ayla Core Domain Model Specification
title_ru: Спецификация основной доменной модели Ayla

type: domain-specification
status: draft
decision_status: proposed
version: "1.3"

owner: Domain Architecture
owners:
  - Product Owner
  - Domain Architecture

reviewers:
  - Backend Architecture
  - AI Architecture
  - Product Design
  - Privacy and Safety

knowledge_area:
  - domain-model
  - product
  - architecture

system_owner:
  - ayla-platform

system_scope:
  - all Ayla production systems

source_kind: canonical

classification: internal
data_sensitivity: none
security_sensitivity: low

ai_indexing: allowed
export_policy: full

depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Product Vision]]"
  - "[[Ayla Repository Responsibility Matrix]]"
  - "[[Ayla Glossary]]"
  - "[[Ayla MVP Scope and Release Contract]]"
  - "[[Ayla MVP Documentation Roadmap]]"
  - "[[Ayla Intent Model Specification]]"
  - "[[Consent Scope Registry]]"
  - "[[AMD-020 Pilot Scope Registry]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Ayla Decision Log]]"

related_documents:
  - Ayla Intent Model Specification
  - Ayla User Journey Specification
  - Ayla Killer PRD
  - Ayla Repository Responsibility Matrix
  - Ayla Glossary



supersedes: []
superseded_by: []

updated: 2026-07-28
review_cycle: quarterly
---

# Ayla Core Domain Model Specification

## 1. Статус и назначение

Документ определяет каноническую доменную модель Ayla: ключевые бизнес-понятия, их идентичность, владение состоянием, жизненные циклы, инварианты, команды и доменные события.

Он описывает бизнес-смысл системы, а не конкретную реализацию в Django, PostgreSQL, REST API, Python-классах, LLM prompts или пользовательском интерфейсе.

### Readiness

| Гейт | Статус |
|---|---|
| Ready for technical review | No |
| Ready for owner review | No |
| Ready for approval | No |
| Ready for canonicalization | No |

Текущий статус: **Draft / Proposed — substantively developed, internally incomplete**. Снято с блокирующих (v1.3): identity foundation (AYLA-DEC-0016), tenancy — Tenant/Membership/Roles (AYLA-DEC-0017), Offering owner и lifecycle (AYLA-DEC-0020), availability и scheduling (AYLA-DEC-0021), Appointment reschedule/replacement (AYLA-DEC-0022), memory lifecycle (AYLA-DEC-0023/0024), event конвенция (AYLA-DEC-0025). Остаются блокирующими: lifecycle completeness (CDM-AC-04), Handoff Coverage Matrix, SoR owners для Recommendation и Attribution Link (§22), Domain Event Registry semantic review (§11; §24, Governance п. 6), согласование с Safety Policy (CDM-AC-09), mapping commands с API/tool contracts (CDM-AC-06).

## 2. Scope

### 2.1. MVP-значимые доменные объекты

Identity (AYLA-DEC-0016, AYLA-DEC-0017):

1. Subject
2. User
3. Account
4. Identity Reference
5. Tenant
6. Provider
7. Provider Membership
8. Role Assignment
9. Specialist Profile

Персональный контур:

10. Consent
11. Context Fact (Persistent Memory Entry — AYLA-DEC-0024)
12. MemoryProposal (AYLA-DEC-0024)
13. Inference
14. Intent

Коммерческий и операционный контур:

15. Catalog Service
16. Service Offering
17. Specialist Offering Assignment (AYLA-DEC-0020)
18. Availability Calendar / Availability Rule / Schedule Block / Slot Hold (AYLA-DEC-0021)
19. Bookable Slot — вычисляемая проекция, не доменная сущность (§7.10)
20. Recommendation
21. Appointment
22. Appointment Revision (AYLA-DEC-0022)
23. Reschedule Proposal (AYLA-DEC-0022)
24. Attribution Link
25. Feedback (deferred / proposal — см. §7.14, §17)
26. Outcome

### 2.2. Вне полного scope этой версии

- универсальный payment domain;
- wallet, payouts, chargebacks;
- полноценный financial ledger;
- advanced outcome learning;
- многосторонний marketplace settlement;
- multi-country compliance;
- полная микросервисная декомпозиция;
- substitute workflow и time-boxed доступ (deferred — AYLA-DEC-0017 п. 9);
- полная авто-синхронизация внешних календарей и произвольный RRULE (deferred — AYLA-DEC-0021 п. 7, 10);
- merge Subjects, multi-account UI, дополнительные identity-каналы (deferred — AYLA-DEC-0016 п. 8).

Исключение из пункта «универсальный payment domain»: в MVP разрешён ограниченный provider-side monetary flow по AYLA-DEC-0015 ([[Ayla Decision Log]]) — списание подписки, списание booking fee 90 ₽, обработка результата списания, обновление billing status, применение provider eligibility и минимальная reconciliation с YooKassa. Всё остальное (клиентская онлайн-оплата, wallet, payouts, refunds, chargebacks, split-payment, полноценный payment lifecycle, financial ledger) остаётся deferred.

### 2.3. Normative Force

`source_kind: canonical` описывает происхождение (место источника истины), а не нормативную зрелость; нормативная сила наступает только при `status: approved` (см. AYLA-DEC-0013, отклонение `canonical-candidate`).

После получения статуса `approved` настоящий документ становится нормативным источником описания доменной модели Ayla.

Документы более низкого уровня, включая PRD, ADR, API Specifications, Data Models, Event Specifications, Prompt Specifications и техническую документацию, не должны переопределять канонический смысл доменных понятий, определённых настоящим документом.

Изменение канонического значения доменного понятия допускается только посредством внесения изменений в настоящий документ с последующим обновлением зависимой документации.

Терминология, канонические определения и правила использования альтернативных наименований определяются [[Ayla Glossary]] (§3.10), который является нормативным источником терминологического управления. Настоящий документ использует эти определения и не переопределяет их.

## 3. Нормативные принципы

### 3.1. Domain before implementation

Сначала определяется бизнес-смысл объекта, затем таблица, ORM-модель, API, event schema, tool schema и UI.

### 3.2. Technical representations

Доменная Entity не тождественна:

- строке базы данных;
- ORM-модели;
- API DTO;
- UI-компоненту;
- LLM output;
- runtime artifact.

Все технические представления (домен → ORM → API → UI) должны иметь явное сопоставление с канонической доменной моделью. Наличие таблицы, класса или контракта не создаёт отдельную доменную сущность.

### 3.3. Stable identity

Ключевые объекты имеют стабильные идентификаторы:

```text
subject_id
user_id
account_id
identity_ref_id
tenant_id
membership_id
role_assignment_id
specialist_profile_id
consent_id
context_fact_id
proposal_id
inference_id
intent_id
service_id
provider_id
offering_id
assignment_id
calendar_id
rule_id
block_id
hold_id
recommendation_id
appointment_id
revision_id
reschedule_proposal_id
attribution_id
outcome_id
```

ID не меняется при переименовании, смене статуса, миграции и повторной обработке.

Bookable Slot не имеет persistent `slot_id`: ключ проекции — `(specialist_offering_assignment_id, starts_at)` (AYLA-DEC-0021 п. 1, §7.10). Унификация идентификаторов на `user_id` запрещена: `user_id`, `subject_id`, `account_id`, `identity_ref_id` — раздельные идентификаторы с раздельными System of Record (AYLA-DEC-0016 п. 3).

### 3.4. Aggregate consistency

Изменения состояния выполняются только через владельца агрегата, с проверкой инвариантов, авторизации, idempotency и аудита.

### 3.5. AI is never source of truth

LLM может интерпретировать, классифицировать, объяснять и предлагать. LLM не является authoritative source для consent, appointment, price, availability, payment result, profile status или подтвержденных пользовательских фактов.

### 3.6. Facts, inferences and actions are distinct

```text
Fact
Inference
Action
```

Inference не становится Fact автоматически.

### 3.7. Conversation is not System of Record

```text
Transcript ≠ Consent
Transcript ≠ Appointment
Transcript ≠ Context Fact
LLM output ≠ Recommendation record
Tool request ≠ completed action
```

### 3.8. Commands and Events

Command выражает намерение изменить состояние. Event фиксирует уже произошедший факт.

### 3.9. Semantic evolution

- patch — уточнение без изменения смысла;
- minor — совместимое расширение;
- major — breaking change.

### 3.10. One Canonical Meaning

Каждое самостоятельное доменное понятие должно иметь одно каноническое значение и одно каноническое наименование.

Правила регистрации, классификации и использования альтернативных наименований определяются исключительно [[Ayla Glossary]] — единственным авторитетным источником терминологии.

### 3.11. Historical Consistency

Изменение текущего состояния системы не должно изменять исторические бизнес-факты.

Доменная модель должна обеспечивать сохранение исторической информации, необходимой для аудита, аналитики, разрешения споров и соблюдения нормативных требований.

## 4. Ubiquitous Language

> [[Ayla Glossary]] — единственный авторитетный источник терминологии (§3.10). Данный раздел — прикладная таблица терминов доменных объектов; при расхождении приоритет имеет Glossary. Полные определения, правила альтернативных наименований и запрещённые термины фиксируются в Glossary и здесь не переопределяются.

| Термин | Каноническое значение |
|---|---|
| Subject | Субъект персональных данных, consent и memory |
| User | Человек в бизнес-модели |
| Account | Учётная запись входа |
| Identity Reference | Внешний идентификатор (MAX / Telegram / phone / email) |
| Tenant | Граница изоляции и доступа организации |
| Provider | Организация или самостоятельный поставщик услуг |
| Provider Membership | Связь User с tenant |
| Role Assignment | Назначение роли внутри active Membership |
| Specialist Profile | Профессиональный профиль исполнителя, привязанный к User |
| Catalog Service | Каноническое описание типа услуги |
| Service Offering | Коммерческое предложение Provider |
| Specialist Offering Assignment | Назначение Specialist Membership на Service Offering |
| Availability Calendar | Календарь доступности (в MVP один на tenant) |
| Availability Rule | Версионируемое recurring-правило доступности |
| Schedule Block | Блокировка интервала (time-off, external busy, exception) |
| Slot Hold | Временное удержание интервала (TTL 15 минут) |
| Bookable Slot | Вычисляемая проекция доступного интервала, не сущность |
| Intent | Структурированная цель пользователя |
| Context Fact | Подтвержденный факт персистентной памяти (Memory Entry) |
| MemoryProposal | Кандидат в память до подтверждения пользователя |
| Inference | Вывод системы |
| Recommendation | Структурированное предложение следующего действия |
| Appointment | Authoritative запись на услугу |
| Appointment Revision | Иммутабельная версия изменения Appointment |
| Reschedule Proposal | Предложение переноса до принятия |
| Consent | Разрешение на конкретную обработку данных |
| Attribution Link | Связь рекомендации с действием |
| Outcome | Зафиксированный результат |
| Feedback | Явная оценка пользователя |
| System of Record | Авторитетный владелец состояния |
| Aggregate | Граница согласованного изменения |
| Invariant | Правило, которое нельзя нарушить |

## 5. Identity and Ownership

Каждый доменный объект обязан иметь:

- стабильный ID;
- owning context;
- System of Record;
- статус;
- provenance;
- timestamps;
- правила архивирования или удаления.

Контексты ссылаются друг на друга по идентификаторам. Копирование поля не переносит ownership.

## 6. Facts, Inferences and Actions

### 6.1. Fact

```yaml
fact_id:
subject_id:
fact_type:
value:
source:
verification_status:
consent_scope:
valid_from:
valid_until:
status:
```

Fact имеет источник, назначение, актуальность и статус подтверждения.

Persistent Context Fact (Memory Entry) дополнительно подчиняется Memory Contract (AYLA-DEC-0024, §7.3): иммутабельность, типизированное value, purpose_tags, provenance, source_event_id, статусы включая `deletion_pending`.

### 6.2. Inference

```yaml
inference_id:
subject_id:
inference_type:
value:
confidence:
evidence_refs:
model_version:
purpose:
created_at:
expires_at:
status:
```

Inference отделен от Fact, имеет confidence, evidence, purpose и срок действия.

### 6.3. Action

```yaml
action_id:
action_type:
subject_id:
actor_id:
result:
source_command_id:
created_at:
```

Action является результатом выполненной команды.

## 7. Core Domain Objects

### 7.1. Identity: Subject, User, Account, Identity Reference

Каноническая identity-модель — четыре разделённые сущности (AYLA-DEC-0016; пятая — Provider Membership, §7.8).

#### Subject

Субъект персональных данных, consent и memory.

```yaml
subject_id:
status:          # active | merged | anonymized
created_at:
updated_at:
```

Инварианты:

1. `subject_id` во всех доменных объектах ссылается на Subject и никогда не переписывается в исторических записях.
2. В нормальном активном состоянии один Subject имеет не более одного active User; исторические, merged и anonymized записи сохраняются и не обязаны поддерживать физическую симметрию 1:1.
3. SoR: Memory & Identity Domain (AYLA-DEC-0016 п. 10).

#### User

Человек в бизнес-модели.

```yaml
user_id:
subject_id:
status:
created_at:
updated_at:
```

Инварианты:

1. User принадлежит ровно одному Subject.
2. User не зависит от канала.
3. User не равен Account, Specialist Profile или Provider.
4. Удаление или деактивация User не каскадирует в удаление Subject; юридически или договорно обязательные записи не удаляются автоматически, а минимизируются, обезличиваются или сохраняются на установленный срок (retention manifest — отдельный privacy/legal артефакт, AYLA-DEC-0016 п. 7).
5. SoR: Identity and Access (CAP-019).

#### Account

Учётная запись входа.

```yaml
account_id:
user_id:
channel:
status:
created_at:
updated_at:
```

Инварианты:

1. User 1—0..N Account; в MVP — один Account-канал (MAX) (AYLA-DEC-0016 п. 8).
2. Унификация идентификаторов на `user_id` запрещена (§3.3).
3. SoR: Identity and Access (CAP-019).

#### Identity Reference

Внешний идентификатор.

```yaml
identity_ref_id:
account_id:
ref_type:        # max_user_id | phone | telegram | email
ref_value:
status:          # pending | verified | revoked
created_at:
updated_at:
```

Инварианты:

1. Account 1—0..N Identity Reference.
2. Relink допустим только для reference в состоянии `verified` (AYLA-DEC-0016 п. 6).
3. SoR: Identity and Access (CAP-019).

Операции уровня person (AYLA-DEC-0016 п. 4): merge, relink и person-wide deletion — отдельные управляемые операции с audit events (`subject_merged`, `identity_ref_relinked`, `subject_anonymized`), actor и reason. Автоматический merge запрещён; merge инициирует только уполномоченная support/privacy-функция по подтверждённому запросу пользователя; до реализации consent resolver merge запрещён. Consent records при merge не сливаются и не переписываются, сохраняют исходный `subject_id` (AYLA-DEC-0016 п. 5). `ayla_user_id → subject_id` и BotUser — interim mapping / runtime representation, не канонический эквивалент какой-либо одной сущности (AYLA-DEC-0016 п. 9).

### 7.2. Consent

The normative structure, identifiers, allowed scopes, purposes and policy bindings for Consent are defined by the [[Consent Scope Registry]]. This document defines only the domain role, ownership, lifecycle and invariants of Consent.

Разделение нормативного владения: [[Consent Scope Registry]] нормативно владеет scope, purpose, policy bindings и lifecycle Consent; [[Ayla Domain Event Registry]] нормативно владеет именами событий, envelope, payload schema, версиями событий и authoritative producer (AYLA-DEC-0025). Ниже — сводка для чтения модели.

Consent имеет стабильный `consent_id`, привязан к `subject_id` и фиксирует состояние разрешения в рамках scope, зарегистрированного в [[Consent Scope Registry]]. Собственная схема полей Consent в настоящем документе не определяется.

Lifecycle (состояния — дословно по CSR §7; `not_requested` — отсутствие consent record):

```text
not_requested → granted
not_requested → denied

granted → revoked
granted → expired

denied  → granted  ┐
revoked → granted  ├─ создаёт новую consent record
expired → granted  ┘
```

Правило повторного согласия (CSR §7): переход к `granted` после терминального состояния (`denied` / `revoked` / `expired`) создаёт новую consent record (`previous_consent_record_id` + `transition_reason`); прежняя запись остаётся в своём терминальном статусе и не возвращается в `granted`. Переходы `granted → revoked` и `granted → expired` изменяют статус той же записи, не создавая новую. Для комбинации `subject_id` + `tenant_id` + `scope_id` существует не более одного effective (`granted`) состояния одновременно.

Инварианты:

1. Consent имеет scope и purpose.
2. Consent может быть отозван.
3. Отсутствие Consent нельзя компенсировать inference (отсутствие consent record не интерпретируется как согласие — CSR §7).
4. Новая версия политики не расширяет старое согласие автоматически.

Commands:

```text
GrantConsent
DenyConsent
RevokeConsent
ExpireConsent
```

Events (доменные факты lifecycle): grant, deny, revoke, expire. Канонические имена — `consent.granted`, `consent.denied`, `consent.revoked`, `consent.expired` (owner ruling P1-1: приоритет AYLA-DEC-0025 и [[Ayla Domain Event Registry]]); snake_case (`consent_granted`, …) — только legacy aliases либо внутренние audit codes, не второй канон; новые producers/consumers используют только `consent.*`; требуется amendment CSR §9.1 и migration plan (§24, Governance п. 6).

### 7.3. Context Fact (Persistent Memory Entry)

Подтверждённый факт персистентной памяти. Контракт жизненного цикла — AYLA-DEC-0024; whitelist категорий — AYLA-DEC-0023 (поле не может существовать вне категории; каждая категория имеет статус allowed / requires dedicated consent / forbidden и scope из [[Consent Scope Registry]]).

```yaml
context_fact_id:        # memory_id
subject_id:
tenant_id:
category:               # из whitelist (AYLA-DEC-0023)
value:                  # типизированное {type, payload, display_text}; свободный текст как единственная форма запрещён
provenance:             # user_stated | user_confirmed_inference
consent_scope:
purpose_tags:
status:                 # active | superseded | expired | deletion_pending | deleted
created_at:
updated_at:
effective_from:
superseded_by:
expires_at:
source_event_id:        # уникален — идемпотентность подтверждения
deletion_due_at:
```

Lifecycle:

```text
active → superseded | expired | deletion_pending → deleted
```

Инварианты:

1. Запись иммутабельна; update-in-place запрещён. Смена active entry атомарна: old → `superseded` (`superseded_by = new_id`), new → `active`; обязателен `supersession_reason` (`corrected | changed | consolidated | policy_migration`). Удаление без замены — не supersession: запись переходит в `deletion_pending`.
2. `confidence` в canonical записи запрещён (допустим у MemoryProposal и в audit metadata, не влияет на использование факта).
3. Fact имеет provenance; Fact не создаётся только из LLM output — единственный pipeline: user message → model inference → assistant asks for confirmation → explicit user confirmation → memory candidate → whitelist check → persist (AYLA-DEC-0023 п. 2).
4. Retrieval — только purpose-limited (`MemoryRetrievalRequest` с declared purpose); retrieval без purpose и API вида `get_all_memory` запрещены; retrieval аудируется (AYLA-DEC-0024 п. 3).
5. User-stated safety constraints хранятся как утверждение пользователя (`user_stated`: «Пользователь сообщил, что…»), а не как medical facts; model-derived medical facts запрещены к сохранению всегда (AYLA-DEC-0023 п. 3).
6. Отзыв consent: записи немедленно становятся unreadable (read gate по актуальному consent state), переводятся в `deletion_pending`; distributed deletion охватывает все readable и derived representations (кэши, индексы, embeddings, projections); после удаления — только content-free tombstone. Повторное согласие не восстанавливает старые записи (AYLA-DEC-0024 п. 5).
7. `expires_at` обязателен для категорий с TTL; expired запись не читается; expiration ≠ deletion — далее действует retention policy. User-stated safety constraints подлежат периодическому reconfirmation (AYLA-DEC-0024 п. 8).
8. Memory Service — единственный владелец state transitions; consumers могут только submit proposal, confirm proposal, request correction, request deletion, retrieve by purpose (AYLA-DEC-0024 п. 10).

#### MemoryProposal

Кандидат в память до подтверждения пользователя (AYLA-DEC-0024 п. 2).

```yaml
proposal_id:
subject_id:
tenant_id:
category:
value:
confidence:             # допустим здесь; не влияет на использование факта
status:                 # pending_confirmation | accepted | rejected | expired
created_at:
expires_at:             # TTL; истекает при завершении сессии
```

Инварианты:

1. До подтверждения proposal — не память.
2. Завершение сессии не создаёт память, не является implicit consent и не подтверждает pending proposals.
3. Цепочка: `proposal.pending_confirmation → accepted → entry.active`; superseded и expired переходят в `deletion_pending`, если retention policy требует физического удаления.

Temporary Context (состояние сессии, временные намерения, контекст разговора) — не долговременная сущность CDM: относится к Conversation State (session-scoped, короткий TTL, недоступен через Memory Retrieval API; batch promotion, automatic summarization и background copying в Persistent Memory запрещены — AYLA-DEC-0024 п. 6) и здесь не моделируется.

### 7.4. Inference

```yaml
inference_id:
subject_id:
inference_type:
value:
confidence:
evidence_refs:
model_version:
purpose:
status:
created_at:
expires_at:
```

Lifecycle:

```text
generated → active → superseded / expired / deleted
```

Инварианты:

1. Inference не является Fact.
2. Inference имеет confidence и provenance.
3. Inference имеет срок действия.
4. Inference не меняет authoritative state напрямую.
5. Запрещенные sensitive inference не создаются; model-derived medical facts запрещены к сохранению всегда (AYLA-DEC-0023 п. 3).
6. Inference никогда не становится persistent memory самостоятельно: единственный pipeline — через explicit user confirmation и whitelist check (AYLA-DEC-0023 п. 2); неподтверждённый inference живёт только в сессии.

### 7.5. Intent

```yaml
intent_id:
subject_id:
intent_type:
status:
confidence:
slots:
missing_required_slots:
evidence_refs:
safety_flags:
created_at:
resolved_at:
superseded_by:
```

Нормативный состав runtime output, intent types, slot requirements и инварианты контракта определяются [[Ayla Intent Model Specification]] (Output Contract); настоящий раздел определяет доменную роль, границу lifecycle и владение состоянием Intent.

#### Internal resolution processing ≠ Intent status

Обработка resolution проходит внутренние состояния:

```text
received → detected → resolving → first output produced
```

Эти состояния — не значения `Intent.status`: они не сериализуются, не являются orchestration state, не означают intent-level или execution readiness и не запускают downstream processing или side effects. Они существуют только для traces, logs, metrics, recovery и replay.

`detected` — внутреннее lifecycle-состояние процесса resolution (owner ruling KM-IM-1). Оно **не отображается в `unresolved`**: отсутствие output ≠ status `unresolved`.

`intent_id` создаётся при начале resolution, но `status` присваивается только после завершения первого resolution pass; до первого output объект недоступен business consumers. Запрещён default `status = unresolved` для NOT NULL поля (ложная семантика); допустимые реализационные варианты — отдельный processing state, nullable `status` или создание aggregate после первого pass — конкретный вариант не предписывается.

#### Published Intent status

Поле `status` принимает только значения Output Contract [[Ayla Intent Model Specification]]:

```text
resolved | needs_clarification | unresolved | superseded | expired | blocked_safety
```

`unresolved` — consumer-meaningful результат **завершённого** resolution pass (resolver завершил проход без результата), а не признак того, что resolver ещё работает.

Первый публикуемый output создаётся после первого resolution pass и принимает одно из: `resolved`, `needs_clarification`, `unresolved`, `blocked_safety`. Значения `superseded` и `expired` — не результаты resolution pass, а последующие lifecycle-переходы уже опубликованного Intent.

Lifecycle опубликованного Intent (transition matrix по [[Ayla Intent Model Specification]]; семантика переходных событий — pending Domain Event Registry reconciliation, §24, Governance п. 6):

```text
needs_clarification → resolved | unresolved | expired | superseded
resolved            → superseded | expired
unresolved          → superseded | expired
blocked_safety      → superseded
```

#### Intent-level readiness

`resolved` означает только intent-level readiness (распознанность типа по Output Contract) и ничего более:

```text
resolved ≠ action authorized ≠ action confirmed ≠ action executed ≠ action succeeded
```

Выполнение действия фиксируется owning downstream capability (Appointment/Action); Intent не меняет свой `status` по факту выполнения.

#### Events

- `IntentDetected` — internal technical/observability event: не integration contract, не запускает capabilities, не используется для attribution, не равен `IntentResolved`.
- `IntentFulfilled` — производная корреляционная проекция от authoritative downstream event (например, `AppointmentCompleted`), а не самостоятельный факт выполнения.
- Семантика `IntentResolved`, `IntentAbandoned`, `IntentFulfilled`, `IntentSuperseded`, `IntentExpired` — pending Domain Event Registry reconciliation (§24, Governance п. 6); `IntentResolved` как универсальное событие не использовать до этого решения.

Инварианты:

1. Intent имеет стабильный `intent_id`.
2. Query ≠ Intent: Intent не равен сообщению.
3. Intent имеет evidence.
4. Низкая уверенность требует clarification.
5. Required slots заполняются до irreversible action.
6. Sensitive Intent проходит safety policy.
7. `detected` ∉ `Intent.status` и `detected` ↛ `unresolved`: внутреннее состояние resolver не отображается в контрактное значение.
8. `unresolved` присваивается только после завершённого resolution pass.
9. Output соответствует Output Contract [[Ayla Intent Model Specification]].
10. `resolved` = intent-level readiness только.
11. Intent не выполняет side effects и не создаёт Appointment напрямую; выполнение подтверждает owning downstream.
12. Supersession сохраняет историю.
13. Blocking safety предотвращает запуск downstream pipeline.
14. Internal telemetry ≠ публичный контракт.

### 7.6. Catalog Service

Каноническое описание типа услуги (бывш. Service; CAP-008 владеет только каноническим Catalog Service — AYLA-DEC-0020 п. 14).

```yaml
service_id:
canonical_name:
category_id:
description:
constraints:
safety_profile:
status:
version:
```

Инварианты:

1. Catalog Service не содержит конкретную цену исполнителя.
2. Catalog Service не равен Service Offering.
3. Смена названия не меняет service_id.
4. Деактивированная услуга не предлагается.
5. SoR: Service Catalog (CAP-008).

### 7.7. Provider

Организация или самостоятельный поставщик услуг — владелец коммерческих предложений (AYLA-DEC-0020 п. 2).

```yaml
provider_id:
provider_type:
legal_name:
display_name:
tenant_id:
status:          # active | suspended | closed
created_at:
updated_at:
```

Инварианты:

1. В MVP один Provider связан ровно с одним Tenant, но Provider и Tenant — не синонимы; изменение кардинальности Provider↔Tenant после MVP не должно требовать переопределения identity и authorization contracts (AYLA-DEC-0017 п. 2).
2. У Provider всегда не менее одного active Membership с ролью `owner`, пока Provider не `closed` (AYLA-DEC-0017 п. 10).
3. Provider status влияет на коммерческие действия.
4. Provider не владеет каноническим Catalog Service; Provider владеет Service Offering (AYLA-DEC-0020 п. 2).
5. Самозанятый — вырожденный случай: один User, один Tenant, один Provider, один Membership с ролями `owner` + `specialist`; отдельного доменного контура соло не существует (AYLA-DEC-0017 п. 10, AYLA-DEC-0020 п. 2).
6. SoR: Provider Management (CAP-009, business truth).

### 7.8. Tenant, Provider Membership, Role Assignment, Specialist Profile

Модель доступа персонала (AYLA-DEC-0017): профессиональный профиль, доступ к салону и связь с tenant — три независимых факта.

#### Tenant

Граница изоляции и доступа.

```yaml
tenant_id:
default_timezone:    # IANA; наследуется Availability Calendar (AYLA-DEC-0021 п. 5)
status:
created_at:
```

Инварианты:

1. Tenant — самостоятельная сущность, не синоним Provider.
2. SoR: Identity and Access (CAP-019) (AYLA-DEC-0017 п. 11).

#### Provider Membership

Связь User с tenant. Создаёт owner tenant'а или уполномоченный platform operator; самостоятельная заявка мастера создаёт только invitation/request в состоянии `requested` без доступа до подтверждения owner.

```yaml
membership_id:
user_id:
provider_id:
tenant_id:
status:
created_at:
suspended_at:
revoked_at:
```

Lifecycle:

```text
requested / invited → active ⇄ suspended → revoked
```

Инварианты:

1. Revoke/expiry — терминальные, не удаляющие: Membership, история Appointment, Offering и Specialist Profile сохраняются; реанимация revoked запрещена, повторный найм создаёт новый Membership.
2. Revoke немедленно прекращает доступ и автоматически не изменяет Appointment: для каждой будущей активной записи создаётся обязательный remediation item `needs_resolution` (операционная задача, не статус Appointment), уведомление owner/admin и явное решение (сохранить / переназначить / перенести / отменить) с actor, reason и уведомлением клиента (AYLA-DEC-0017 п. 7).
3. Доступ персонала требует active Membership с подходящей Role Assignment; ни одна tenant-роль не даёт доступа к memory, context и consent клиентов.
4. SoR: Provider Management (CAP-009) владеет business truth; Identity and Access (CAP-019) владеет enforcement и хранит только авторизационную проекцию Membership/roles (AYLA-DEC-0017 п. 11).

#### Role Assignment

Назначение роли внутри active Membership.

```yaml
role_assignment_id:
membership_id:
role:            # owner | admin | specialist
granted_at:
expires_at:      # nullable; time-boxed assignment — модель допускает (substitute deferred)
```

Инварианты:

1. Role Assignment действует только внутри active Membership.
2. Роли MVP: `owner`, `admin`, `specialist`. Минимальный `admin`: создание/изменение offline-записей, работа с расписанием, операционные данные своего tenant, клиентские обращения в пределах политики. Запрещено: управление ownership, billing/legal settings, доступ к memory/wellness/consent клиента, назначение owner. Все действия `admin` с чужими Appointment аудируются (AYLA-DEC-0017 п. 6).
3. Substitute workflow — deferred; модель допускает time-boxed Role Assignment, scoped access, один tenant, только назначенные Appointment и автоматическое expiry (AYLA-DEC-0017 п. 9).
4. SoR: Provider Management (CAP-009, business truth); CAP-019 — enforcement-проекция.

#### Specialist Profile

Профессиональный профиль исполнителя; привязан к User и не содержит `provider_id` (AYLA-DEC-0017 п. 3–4).

```yaml
specialist_profile_id:
user_id:
display_name:
profile_status:
qualification_refs:
created_at:
updated_at:
```

Инварианты:

1. Прямая привязка `Specialist.provider_id` отменяется; один Specialist Profile допускает любое число активных Membership в разных Provider.
2. Specialist Profile ≠ доступ (Role Assignment) ≠ связь с tenant (Provider Membership).
3. Qualification data имеет provenance.
4. Specialist оказывает услугу через Specialist Offering Assignment → Membership (AYLA-DEC-0020 п. 1).
5. SoR: Provider Management (CAP-009, business truth).

### 7.9. Service Offering

Конкретное коммерческое предложение Provider (AYLA-DEC-0020).

```yaml
offering_id:
service_id:        # → Catalog Service
provider_id:
tenant_id:         # граница изоляции и доступа; Tenant — не владелец прайса
title:
duration_minutes:  # base_duration
price:             # base_price
currency:
status:
created_at:
updated_at:
```

Lifecycle:

```text
draft → active ⇄ paused → archived
```

Инварианты:

1. Offering принадлежит Provider как организации-владельцу коммерческого предложения и ссылается на существующий Catalog Service.
2. Поле `specialist_id` в Offering упразднено: исполнители разрешаются через Specialist Offering Assignment.
3. Неактивное Offering не участвует в подборе; `paused` — новые записи запрещены, assignments сохраняются; `archived` не удаляется при наличии записей.
4. Offering не ослабляет глобальные safety rules.
5. Активация Offering соло-организации невозможна без active Assignment на единственный eligible Specialist Membership; draft Offering без assignment допустим; команда создания с немедленной активацией создаёт обе сущности атомарно, асинхронное создание assignment запрещено (AYLA-DEC-0020 п. 4).
6. Offering price — Commerce / Catalog Management, не Platform Billing (тариф подписки, комиссия Ayla, реквизиты) (AYLA-DEC-0020 п. 6).
7. SoR: Provider Management (CAP-009, business truth); формулировка `Provider/Catalog boundary` упразднена (AYLA-DEC-0020 п. 14).

#### Specialist Offering Assignment

Назначение Specialist Membership на Service Offering (AYLA-DEC-0020 п. 3).

```yaml
assignment_id:
offering_id:
specialist_membership_id:   # модель assignment.specialist_id запрещена
price_override:             # nullable
duration_override:          # nullable
booking_enabled:
qualification_status:
qualification_evidence_ref:
status:
created_at:
updated_at:
```

Effective values: `effective_price = price_override ?? base_price`; `effective_duration = duration_override ?? base_duration`. `booking_allowed` — результат domain policy evaluation (offering active AND offering booking enabled AND assignment active AND assignment booking enabled AND membership active AND availability decision = available AND qualification/safety requirements satisfied), а не поле Assignment; assignment не является доказательством квалификации.

Lifecycle (AYLA-DEC-0020 п. 11):

```text
pending → active | archived
active → self_disabled | organization_disabled | suspended | archived
self_disabled → active | organization_disabled | suspended | archived
organization_disabled → active | suspended | archived
suspended → active | archived
archived → ∅
```

Инварианты:

1. `organization_disabled` — коммерческое решение организации; `suspended` — принудительное ограничение (compliance, qualification, safety, platform enforcement).
2. Specialist управляет собственной доступностью (`active → self_disabled`); возврат — owner/admin, для safety-sensitive услуг — только с подтверждением специалиста (AYLA-DEC-0020 п. 5).
3. Membership terminated → assignments not bookable, сохраняются для истории.
4. Клиентский каталог — derived projection (offering один раз; «от X» = min effective_price активных assignments), не SoR (AYLA-DEC-0020 п. 12).
5. SoR: Provider Management (CAP-009, business truth).

### 7.10. Availability и Bookable Slot

Bookable Slot — **вычисляемая проекция без System of Record** (AYLA-DEC-0021 п. 1), не доменная сущность. Ключ слота — `(specialist_offering_assignment_id, starts_at)`; assignment_id однозначно определяет tenant, membership, offering, effective_duration и buffers (AYLA-DEC-0020). Постоянный `slot_id` доменной сущности не вводится; для API допустим подписанный projection token с версией входных данных — transport-артефакт, не SoR. Модель «slot as stored entity per offering» отменяется. Кэш проекции — non-authoritative optimization, не порождает доменных событий. Слот рассчитывается от `effective_duration` конкретного assignment (AYLA-DEC-0020 п. 9). Горизонт проекции — 30 дней (tenant-configurable параметр чтения); произвольный RRULE — deferred (AYLA-DEC-0021 п. 10).

Инварианты проекции:

1. starts_at < ends_at.
2. Отображаемый слот не является reservation и не гарантирует Appointment.
3. Защита от двойной записи — DB-enforced по интервалам: PostgreSQL exclusion constraint по `tstzrange` ЛИБО единый Time Reservation ledger (`reservation_kind = hold | appointment`) с exclusion constraint для активных reservation одного ресурса; если Hold и Appointment — разные таблицы, обязательна общая locking boundary для всех путей занятия интервала. Конкретная реализация не предписывается (AYLA-DEC-0021 п. 4).
4. События «слот исчез» не существует (AYLA-DEC-0021 п. 6).

Доменные сущности контура (SoR: Availability Management, CAP-010 — AYLA-DEC-0021 п. 2):

#### Availability Calendar

```yaml
calendar_id:
tenant_id:          # в MVP один календарь на tenant
timezone:           # IANA; наследует Tenant.default_timezone
status:
```

#### Availability Rule

Recurring weekly rules (MVP-шаблон: день недели × интервалы), версионируемые.

```yaml
rule_id:
calendar_id:
specialist_membership_id:
weekday:
intervals:
effective_from:
effective_until:    # изменение будущего pattern создаёт новую версию, историческая не переписывается
status:
```

#### Schedule Block

Блокировка интервала: time-off, sick_day, external busy, date exceptions.

```yaml
block_id:
calendar_id:
specialist_membership_id:
starts_at:
ends_at:
block_type:         # time_off | sick_day | external_busy | date_exception | override
source:             # manual | self_service | external_sync
external_ref:       # nullable: {system, external_id}
source_updated_at:
observed_at:
sync_status:
```

Инварианты:

1. Хранение UTC; recurring rules — local wall time + IANA timezone календаря; границы дня — в timezone календаря; клиенту — время места оказания услуги с явной зоной; timezone устройства — только display-проекция (AYLA-DEC-0021 п. 5).
2. Локальная проекция external busy идемпотентно обновляет существующий блок — дубли от повторных webhook запрещены (AYLA-DEC-0021 п. 2).
3. Создание Schedule Block или изменение Availability Rule немедленно переводит конфликтующие активные hold в `released` с reason `AVAILABILITY_CHANGED` + audit + уведомление активной booking session; Appointment автоматически не изменяются — обязательные remediation items `needs_resolution` (AYLA-DEC-0021 п. 6, AYLA-DEC-0017 п. 7).
4. Self-service мастера: SICK_DAY — немедленный эффективный Block `sick_day` + audit + уведомление admin; vacation/planned leave/recurring change — через approval workflow; свободный редактор расписания — deferred (AYLA-DEC-0021 п. 9).

#### Slot Hold

Временное удержание интервала; TTL 15 минут — платформенный параметр.

```yaml
hold_id:
specialist_offering_assignment_id:
starts_at:
ends_at:
status:             # held | confirmed | expired | released
created_at:
expires_at:
```

Lifecycle:

```text
held → confirmed | expired | released
```

Инварианты:

1. Hold имеет TTL; истёкший hold не подтверждается; повторный confirm идемпотентен; нарушение занятости → `SLOT_TAKEN` (AYLA-DEC-0021 п. 3).
2. ConfirmAppointment — одна транзакция: блокировать hold/reservation → проверить статус и TTL → повторно проверить актуальные Rule/Block/external busy → создать Appointment → перевести hold в `confirmed` → зафиксировать идемпотентный результат.
3. Offline/admin-записи создаются без hold, с обязательным audit и теми же overlap-проверками в той же locking boundary; запись вне Availability Rule — явная override-команда с actor и reason; пересечение с другой Appointment запрещено даже override (политика parallel capacity не введена) (AYLA-DEC-0021 п. 8).
4. Физическое удаление терминальных hold запрещено, если это разрушает аудит; конкретные сроки хранения не установлены (DEC-0021 Q7, §24).
5. Calendar Sync: несинхронизированный dual-source запрещён; freshness сверх лимита → Ayla не подтверждает автоматически либо требует синхронной проверки внешней системы; если проверка невозможна — отдельный временный reason code, не `SLOT_TAKEN` (AYLA-DEC-0021 п. 7; SLA — integration contract, §24).

### 7.11. Recommendation

```yaml
recommendation_id:
subject_id:
intent_id:
primary_candidate:
alternative_candidates:
ranking_inputs:
gating_results:
explanation:
status:
created_at:
presented_at:
expires_at:
accepted_at:
rejected_at:
```

Lifecycle:

```text
draft → validated → presented → accepted → acted_upon
         ↘ blocked        ↘ rejected / expired
```

Инварианты:

1. Recommendation имеет recommendation_id.
2. Recommendation связана с resolved Intent.
3. Primary recommendation не означает единственный вариант.
4. Recommendation проходит eligibility и safety gates.
5. Explanation не содержит неподтвержденные факты.
6. Экономический интерес не искажает organic ranking скрыто.
7. Recommendation имеет expiry.
8. Recommendation не равна Appointment.
9. Accepted Recommendation не означает выполненное действие.
10. Для attribution сохраняется recommendation_id.

### 7.12. Appointment

Authoritative запись на услугу (AYLA-DEC-0020 п. 8, AYLA-DEC-0022).

```yaml
appointment_id:
subject_id:
tenant_id:                      # иммутабелен
provider_id:
service_offering_id:
specialist_assignment_id:
specialist_membership_id:
origin:                         # ai_recommendation | direct_catalog | provider_created | admin_created | external_import | campaign | rebooking
recommendation_id:              # условно: обязателен iff origin = ai_recommendation
price_snapshot:                 # {amount, currency}
effective_duration_snapshot:
offering_title_snapshot:
reschedule_of:                  # nullable → appointment_id; непосредственный предок, только replacement
root_appointment_id:            # корень lineage
reschedule_count:               # наследуется +1 по lineage (успешные переносы)
external_ref:                   # nullable: {system, external_id, source_timestamps, sync_metadata}
status:
scheduled_at:
created_at:
confirmed_at:
cancelled_at:
completed_at:
version:                        # монотонно, +1 на same-ID reschedule
```

Канонический `specialist_id` как SoR-атрибут Appointment запрещён: исполнитель определяется через `specialist_membership_id`, глобальный профиль — через Membership → Specialist Profile. Денормализованный `specialist_id` допустим только в read models, search indexes и analytics как derived-поле: не принимается в write commands и не участвует в доменных инвариантах (AYLA-DEC-0020 п. 8).

Lifecycle (статус `rescheduled` не вводится — AYLA-DEC-0022 п. 1):

```text
requested → pending_confirmation → confirmed → completed
    ↘ rejected          ↘ expired       ↘ cancelled / no_show
```

Reschedule — не статус, а версионируемая операция. Same-ID (сохранение `appointment_id`, монотонная `version`, иммутабельная Appointment Revision на каждое изменение) допустим только при: тот же tenant; тот же `service_offering_id`; неизменные цена и длительность; тот же payment/consent scope; не terminal state. Матрица операций (AYLA-DEC-0022 п. 2): дата/время → same-ID; специалист в том же Offering при неизменной цене/длительности и явном согласии клиента → same-ID (reschedule acceptance, не новый Consent); небизнесовые метаданные → same-ID при неизменных сумме, способе/статусе оплаты и доходе мастера; другая услуга/Offering, изменение клиентской цены (всегда, включая снижение), изменение длительности, изменение payment boundary, новый юридический/медицинский/информационный Consent → replacement (в любом статусе, включая `requested`); другой tenant → cancel + новый booking flow без cross-tenant lineage; terminal state → запрещено.

Replacement: старая запись → `cancelled` с `cancellation_reason = replaced_by_reschedule`; новая запись несёт `reschedule_of` (непосредственный предок, ациклично, тот же tenant), `root_appointment_id`, `reschedule_count` (наследуется +1) (AYLA-DEC-0022 п. 3).

Origin и `recommendation_id` при replacement: если replacement больше не исполняет исходную Recommendation, новая Appointment **не** получает `recommendation_id`, а её `origin` отражает фактическое происхождение новой записи (например `rebooking`). История происхождения сохраняется через lineage и неизменяемую исходную Appointment. `origin = ai_recommendation` допускается только вместе с валидным `recommendation_id`.

Инварианты:

1. Нельзя подтвердить запись на занятый интервал; истёкший hold не подтверждается (§7.10).
2. Нельзя создать конфликтующую запись (overlap-защита DB-enforced, §7.10).
3. Create Appointment идемпотентен.
4. Appointment — SoR статуса записи.
5. LLM не объявляет запись созданной без backend result.
6. История изменений сохраняется как иммутабельные Appointment Revision; историческая запись не изменяется при изменении прайса (AYLA-DEC-0020 п. 8).
7. Cancellation имеет actor и reason.
8. `recommendation_id` сохраняется и обязателен iff `origin = ai_recommendation`; origin/provenance сохраняются всегда; Attribution Link не переписывается — при переносе той же услуги attribution продолжается по lineage, при другой услуге `recommendation_id` наследуется только после проверки исполнения той же Recommendation (без слепого наследования); attribution eligibility — явное решение (AYLA-DEC-0022 п. 7).
9. Provider eligibility проверяется до подтверждения.
10. Side effects имеют audit trail.
11. Инвариант цепочки (AYLA-DEC-0020 п. 8): `service_offering_id` и `specialist_membership_id` в Appointment обязаны совпадать с Offering и Membership, на которые ссылается `specialist_assignment_id`; все три сущности принадлежат одному tenant.
12. Cross-tenant lineage запрещён (AYLA-DEC-0022 п. 2–3).
13. Billing: reschedule не создаёт charge; replacement может породить charge после собственного завершения; один completed outcome в lineage → не более одного booking fee; billing проверяет lineage по `root_appointment_id` (AYLA-DEC-0022 п. 7, AYLA-DEC-0010).
14. `no_show` — только из действующей `confirmed` (AYLA-DEC-0022 п. 9).
15. Calendar mode tenant: `ayla_primary | external_primary`; несинхронизированный dual-source запрещён. В `external_primary` (MVP) перенос выполняется во внешней системе; Ayla импортирует результат с `external_ref`; конфликт — в пользу подтверждённой внешней версии; stale → degraded mode (AYLA-DEC-0021); внешние изменения нормализуются по матрице операций (время-only → same-ID Revision с actor=external_system; Offering/цена/длительность/consent/payment → replacement); запись внешних изменений как Revision без разбора запрещена (AYLA-DEC-0022 п. 8).
16. Лимит переносов — policy, не инвариант: MVP default 3 успешных self-service reschedule на lineage; далее — owner/admin review с actor/reason; запись не блокируется и не отменяется (AYLA-DEC-0022 п. 6).

#### Appointment Revision

Иммутабельная версия изменения Appointment (владеет Appointment Aggregate, AYLA-DEC-0022 п. 1).

```yaml
revision_id:
appointment_id:
version:              # версия записи после изменения
changed_fields:       # [{field, old, new}]
actor:                # user | specialist | admin | owner | system | external_system
reason:
command_id:           # + idempotency_key
created_at:
```

#### Reschedule Proposal

Предложение переноса до принятия (AYLA-DEC-0022 п. 4). Обязательна для смены мастера, master re-offer, substitute-предложений, late-window и сверх-лимитных запросов.

```yaml
reschedule_proposal_id:
appointment_id:
proposed_assignment_id:    # nullable (если меняется только время)
proposed_starts_at:
proposed_price_snapshot:
actor:
reason:
status:                    # pending | accepted | declined | expired | withdrawn
created_at:
expires_at:
```

Инварианты:

1. Pending proposal не изменяет Appointment: исходная запись действующая, старое время занято, новая Reservation с ограниченным TTL, `appointment.rescheduled` не публикуется.
2. Принятие — атомарная транзакция с hold (AYLA-DEC-0021), `expected_version`, повторной проверкой Rule/Block/external freshness; при любом отказе старая запись и reservation без изменений (AYLA-DEC-0022 п. 10).
3. Отказ/expiry — исходная запись неизменна.
4. Late-window запрос (позднее чем за 1 час до `starts_at`) — manual reschedule request через proposal, решение owner/admin вручную; порог — product default MVP, не доменный инвариант (AYLA-DEC-0022 п. 5).

### 7.13. Attribution Link

```yaml
attribution_id:
recommendation_id:
action_type:
action_id:
attribution_type:
window_type:
created_at:
```

Типы:

```text
direct
assisted
unattributed
```

Инварианты:

1. Direct attribution требует recommendation_id.
2. Assisted attribution имеет формализованное окно.
3. Attribution не создается без Action.
4. Одно действие не получает конфликтующие direct attribution records.
5. Версия attribution rule прослеживаема.

### 7.14. Feedback (deferred / proposal)

**Статус: deferred / proposal.** Feedback не входит в Included Capabilities [[Ayla MVP Scope and Release Contract]] §4 и не перечислен среди моделей [[Ayla MVP Documentation Roadmap]] §4.3. Активация Feedback в MVP допускается только через change control Scope Contract §11 (owner decision). Определение ниже — proposal и не является основанием для реализации.

```yaml
feedback_id:
subject_id:
target_type:
target_id:
value:
comment:
source:
created_at:
```

Инварианты (proposal):

1. Feedback — пользовательский ввод, не inference.
2. Feedback не равен Outcome.
3. Изменения Feedback аудируются.
4. Свободный текст проходит privacy и safety обработку.

### 7.15. Outcome

```yaml
outcome_id:
subject_id:
appointment_id:
recommendation_id:
outcome_type:
value:
source:
status:
recorded_at:
```

Инварианты:

1. Outcome имеет источник.
2. Feedback и Outcome не смешиваются.
3. Inferred Outcome маркируется отдельно.
4. Health-related Outcome не превращается в диагноз.
5. Outcome Learning не меняет исторические факты.

## 8. Aggregate Boundaries

### 8.1. Consent Aggregate

Root: `Consent`.

Владеет состоянием согласия: grant, revoke, expiry. Нормативная структура scope, purpose и policy bindings определяется [[Consent Scope Registry]] (§7.2) и здесь не дублируется.

### 8.2. Personal Context Aggregate

Root: `Context Subject`.

Владеет Context Facts, correction history и usage metadata. Не владеет Consent, но проверяет его. State transitions Memory Entry и MemoryProposal выполняет только Memory Service (AYLA-DEC-0024 п. 10); запись иммутабельна, история — через supersession (§7.3).

### 8.3. Intent Aggregate

Root: `Intent`.

Владеет slots, missing slots, evidence refs, clarification state и supersession.

### 8.4. Recommendation Aggregate

Root: `Recommendation`.

Владеет primary candidate, alternatives, explanation, gating results, status и expiry.

### 8.5. Appointment Aggregate

Root: `Appointment`.

Владеет selected offering reference, selected assignment reference, participants, status transitions и Appointment Revision history (AYLA-DEC-0022).

### 8.6. Recommendation Aggregate: owns / references / does-not-own

Owns:

- выбор кандидатов (primary candidate, alternative candidates — как ссылки, §7.11);
- Explanation;
- Ranking Result (ranking inputs, gating results);
- Presentation State (status, presented_at, expiry).

References (по идентификаторам, §5, §13):

- Intent (`intent_id`);
- кандидаты: Service Offering / Specialist Offering Assignment (Bookable Slot — projection key, §7.10);
- Provider.

Does not own:

- Appointment (создаётся downstream после accepted Recommendation — §7.11, инвариант 8);
- Specialist Profile;
- Catalog Service;
- Service Offering и Specialist Offering Assignment как объекты каталога и прайса.

### 8.7. Appointment Aggregate: owns / references / does-not-own

Owns:

- status transitions (lifecycle §7.12);
- Timeline (scheduled_at, confirmed_at, cancelled_at, completed_at);
- Booking Metadata (participants, `version`, actor и reason изменений);
- Appointment Revision history и lineage (`reschedule_of`, `root_appointment_id`, `reschedule_count`);
- snapshots (`price_snapshot`, `effective_duration_snapshot`, `offering_title_snapshot`).

References (по идентификаторам, §5, §13):

- Service Offering (`service_offering_id`);
- Specialist Offering Assignment (`specialist_assignment_id`) и Provider Membership (`specialist_membership_id`);
- Bookable Slot — только projection key `(specialist_offering_assignment_id, starts_at)`, не ссылка на сущность (§7.10);
- Recommendation (`recommendation_id` — условно, iff `origin = ai_recommendation`, §7.12);
- Provider (`provider_id`).

Does not own:

- Specialist Profile, Provider, Catalog Service;
- Service Offering и его price (`price_snapshot` — исторический snapshot, §13);
- Availability Calendar / Rule / Schedule Block / Slot Hold как объекты расписания.

## 9. Lifecycle Rules

Каждый lifecycle должен:

- иметь допустимые состояния;
- запрещать недопустимые переходы;
- фиксировать actor и reason;
- публиковать событие;
- поддерживать idempotency;
- сохранять audit trail.

Статусы являются стабильными enum-значениями, а не свободным текстом.

## 10. Commands

Общий контракт:

```yaml
command_id:
command_type:
actor_id:
subject_id:
aggregate_id:
idempotency_key:
payload:
issued_at:
correlation_id:
causation_id:
```

MVP commands (группировка по превалирующему actor; классификация не меняет состав реестра и контракт команд):

User commands:

```text
GrantConsent
DenyConsent
RevokeConsent
ConfirmContextFact
CorrectContextFact
DeleteContextFact
AcceptRecommendation
RejectRecommendation
RequestAppointment
RescheduleAppointment
CancelAppointment
```

System commands:

```text
RecordContextFact
SupersedeIntent
AbandonIntent
ExpireRecommendation
CompleteAppointment
MarkAppointmentNoShow
CreateAttribution
RecordOutcome
```

AI commands:

```text
RequestIntentClarification
ResolveIntent
CreateRecommendation
ValidateRecommendation
PresentRecommendation
```

Administrative commands:

```text
ConfirmAppointment
RejectAppointment
```

Deferred (активация через change control [[Ayla MVP Scope and Release Contract]] §11 — см. §7.14):

```text
SubmitFeedback
```

Примечание: `DetectIntent` исключён из реестра команд (KM-IM-1): `detected` — внутренний этап обработки `ResolveIntent`, а не создание опубликованного результата (§7.5).

## 11. Domain Events

Нормативные имена событий, payload schema и envelope принадлежат [[Ayla Domain Event Registry]] (AYLA-DEC-0025) и в настоящем документе не дублируются. PascalCase-имена и прежний envelope (v1.2.x) упразднены как источник контракта (OQ-1 реестра).

Действующая конвенция (AYLA-DEC-0025):

1. Имя — lowercase dot-separated past-tense fact: `<domain>.<entity>.<fact>` (`appointment.created`, `consent.revoked`, `memory.deleted`). Смешение форм запрещено — одна каноническая форма; событие — факт, не команда. `appointment.*` — canonical, `booking.*` — legacy (compatibility adapter `booking_id` → `appointment_id`). Legacy aliases — временный compatibility mapping, не второе полноценное событие.
2. Envelope — единый, определяется реестром: `event_id`, `event_name`, `event_version`, `occurred_at`, `published_at`, `producer {service, bounded_context, instance_id}`, `subject {entity_type, entity_id}`, `tenant_id`, `correlation_id`, `causation_id`, `idempotency_key`, `data`, `metadata`.
3. Классификация — две независимые оси: `semantic_class` (`domain_fact | technical_signal`) и `publication_scope` (`internal | cross_context | cross_repository | external`). Technical signals запрещены как основание для доменных действий, изменения состояния и side effects; разрешены для observability (logs, tracing, metrics, monitoring, debugging, replay diagnostics).
4. Ровно один authoritative producer на событие: `appointment.*` → Appointment context (CAP-011), `consent.*` → Consent Domain, `intent.*` → Intent Resolution owner, `memory.*` → Memory Service. Вторичные семантические producer'ы запрещены; transport relays (outbox publisher, broker adapter, CDC) допустимы, но не становятся владельцами и сохраняют canonical name, producer identity, event_id, payload version, occurred_at.
5. Event immutable; consumer idempotent; PII classification обязательна; event не содержит лишние sensitive data. Additive change обратно совместим; breaking payload change — major `event_version`; переименование — новое canonical имя + legacy alias + deprecation window.

Установленные расхождения (AYLA-DEC-0025 п. 7): Consent — канон `consent.granted` / `consent.revoked` (legacy: `ConsentGranted`, `consent_granted`); Intent — общее событие завершения resolution pass `intent.resolution_produced` (результат — в payload `resolution_status`); `intent.resolved` как общее событие не используется; `intent.detected` — `technical_signal`, `internal`, не integration contract, не основание для доменных действий (KM-IM-1); Appointment — same-ID reschedule публикует `appointment.rescheduled`, replacement — канонические lifecycle-события старой и новой записи, единственный producer — CAP-011 (AYLA-DEC-0022 п. 9).

Инвентарь доменных фактов MVP (прежние списки Business/Technical/Integration v1.2.x) упразднён как источник имён: первый срез событий проходит семантический review в [[Ayla Domain Event Registry]] (AYLA-DEC-0025 п. 8) — не механическое переименование. До завершения review семантика `IntentAbandoned`, `IntentFulfilled` и семейств `recommendation.*` / `qualified_action.attributed` остаётся pending (§24, Governance п. 6–7). `FeedbackSubmitted` — deferred (активация через change control [[Ayla MVP Scope and Release Contract]] §11, §7.14).

## 12. Systems of Record

| Объект | System of Record | Caching allowed | Snapshot allowed | Replicated |
|---|---|---|---|---|
| Subject | Memory & Identity Domain (AYLA-DEC-0016 п. 10) | proposal | proposal | proposal |
| User | Identity and Access (CAP-019) | proposal | proposal | proposal |
| Account | Identity and Access (CAP-019) | proposal | proposal | proposal |
| Identity Reference | Identity and Access (CAP-019) | proposal | proposal | proposal |
| Tenant | Identity and Access (CAP-019, AYLA-DEC-0017 п. 11) | proposal | proposal | proposal |
| Consent | Consent Management | YES (purpose-bound authoritative cache с freshness, TTL и invalidation — [[AMD-020 Pilot Scope Registry]], [[Consent Scope Registry]]) | NO | NO |
| Context Fact (Memory Entry) | Memory & Identity Domain (W3 Memory Service — AYLA-DEC-0024 п. 10) | proposal | NO (иммутабельность; после удаления — только tombstone) | NO (derived copies подлежат distributed deletion, не SoR) |
| MemoryProposal | Memory & Identity Domain (W3 Memory Service) | proposal | proposal | NO |
| Inference (persistent) | Memory & Identity Domain | proposal | proposal | proposal |
| Intent aggregate (lifecycle/persistence) | Core Domain owner | proposal | proposal | proposal |
| Intent Resolution Output Contract | Intent Model / AI Architecture | proposal | proposal | proposal |
| Internal resolver processing state | AI Runtime (internal telemetry, без публичного контракта — §7.5) | proposal | proposal | NO |
| Authoritative execution result | owning downstream capability | proposal | proposal | proposal |
| Cross-intent attribution | Attribution / analytics | proposal | proposal | proposal |
| Catalog Service | Service Catalog (CAP-008) | proposal | proposal | proposal |
| Provider | Provider Management (CAP-009) | proposal | proposal | proposal |
| Provider Membership | Provider Management (CAP-009, business truth; CAP-019 — авторизационная проекция) | proposal | NO (revoke терминален, не удаляющий) | proposal |
| Role Assignment | Provider Management (CAP-009, business truth; CAP-019 — авторизационная проекция) | proposal | proposal | proposal |
| Specialist Profile | Provider Management (CAP-009) | proposal | proposal | proposal |
| Service Offering | Provider Management (CAP-009, AYLA-DEC-0020 п. 14) | proposal | proposal | proposal |
| Specialist Offering Assignment | Provider Management (CAP-009, AYLA-DEC-0020 п. 14) | proposal | proposal | proposal |
| Availability Calendar / Rule / Schedule Block / Slot Hold | Availability Management (CAP-010, AYLA-DEC-0021 п. 2) | proposal | NO (Rule версионируется, история не переписывается) | proposal |
| Bookable Slot | нет SoR — вычисляемая проекция (AYLA-DEC-0021 п. 1) | YES (non-authoritative cache, не порождает событий) | NO | NO |
| Recommendation | Recommendation | proposal | proposal | proposal |
| Appointment | Appointment Management (CAP-011) | proposal | YES (price/duration/title snapshots — §7.12, §13) | proposal |
| Appointment Revision | Appointment Management (CAP-011, AYLA-DEC-0022) | proposal | NO (иммутабельна) | proposal |
| Reschedule Proposal | Appointment Management (CAP-011, AYLA-DEC-0022) | proposal | proposal | proposal |
| Attribution Link | Attribution | proposal | proposal | proposal |
| Feedback | Feedback Collection (deferred / proposal — §7.14) | proposal | proposal | proposal |
| Outcome | Outcome Learning / Backend facts | proposal | proposal | proposal |
| Conversation transcript | Conversation Experience | proposal | proposal | proposal |
| Conversation State (temporary context) | Conversation Experience (session-scoped, не Persistent Memory — AYLA-DEC-0024 п. 6) | proposal | NO | NO |
| Billing eligibility | owning capability defined outside this document (граница по AYLA-DEC-0015, CAP-022 Billing Eligibility — см. §2.2, §17) | proposal | proposal | proposal |
| Payment result | external deferred (ограниченный контур по AYLA-DEC-0015 — см. §2.2, §17) | proposal | proposal | proposal |

Разграничение ролей для Inference: AI Runtime — producer/processor, который генерирует Inference, но не становится его System of Record. Persistent Inference хранится в Memory & Identity Domain ([[AMD-020 Pilot Scope Registry]], Ownership Summary: Semantic Memory → Memory & Identity Domain). Ephemeral Inference (session-scoped) не имеет persistent System of Record и не переживает сессию.

Разграничение ролей для Intent (KM-IM-1, §7.5): AI Runtime производит resolution, но не становится SoR для Appointment или completed action; authoritative execution result фиксирует owning downstream capability. Internal resolver processing state — внутренняя телеметрия AI Runtime и не является публичным доменным состоянием.

Смысл колонок: Caching allowed — допускается ли кэширование состояния вне SoR; Snapshot allowed — допускается ли snapshot по правилам §13; Replicated — допускается ли реплика состояния в другом контуре. Пометка `proposal` означает, что значение не зафиксировано нормативным источником и требует решения владельца (§24).

## 13. Cross-Context References

Контекст хранит чужие идентификаторы, а не копии чужих агрегатов.

Snapshot допускается, когда он нужен для исторической целостности, имеет timestamp и не используется как новая authoritative версия.

```text
Appointment.price_snapshot
не делает Appointment владельцем Offering price.
```

## 14. AI Interaction Rules

### 14.1. Input boundary

AI получает только разрешенные facts, допустимые inferences, минимальную историю, tool definitions, policy constraints и provenance references.

### 14.2. Output boundary

LLM output считается proposal, classification, explanation, candidate result или draft text.

LLM output не считается completed action, confirmed fact, consent, booking result, payment result или authoritative status.

### 14.3. Tool execution

```text
LLM proposes tool call
→ runtime validates schema
→ authorization check
→ consent check
→ safety check
→ backend executes command
→ backend returns result
→ runtime renders result
```

### 14.4. Side effects

Side effect требует explicit command, authorization, idempotency, audit, deterministic validation и authoritative backend result.

### 14.5. Grounding

Утверждения о цене, доступности, статусе, записи, специалисте, услуге и согласии опираются на структурированный источник.

### 14.6. Safety

Safety не существует только в prompt. Нужны deterministic gates, policy checks, tool restrictions, schema validation, audit events и block reasons.

## 15. Error and Reason Codes

```text
CONSENT_REQUIRED
CONSENT_REVOKED
CONTEXT_NOT_ALLOWED
CONTEXT_FACT_EXPIRED
INTENT_UNRESOLVED
INTENT_CLARIFICATION_REQUIRED
UNSUPPORTED_INTENT
NO_CANDIDATES
RECOMMENDATION_BLOCKED
SAFETY_BLOCKED
NO_AVAILABLE_SLOTS
SLOT_EXPIRED
SLOT_CONFLICT
SLOT_TAKEN
PROVIDER_INELIGIBLE
APPOINTMENT_CONFLICT
APPOINTMENT_NOT_CONFIRMED
APPOINTMENT_ALREADY_CANCELLED
TOOL_TIMEOUT
MODEL_UNAVAILABLE
DEPENDENCY_UNAVAILABLE
IDEMPOTENCY_CONFLICT
UNAUTHORIZED
FORBIDDEN
VALIDATION_FAILED
```

## 16. Versioning and Evolution

Breaking change включает:

- удаление поля;
- изменение смысла поля;
- изменение enum semantics;
- изменение ownership;
- изменение lifecycle;
- изменение aggregate boundary;
- изменение required field;
- изменение event interpretation.

Stable ID удаленного типа не переиспользуется.

Lifecycle контракта:

```text
active → deprecated → retired
```

Cross-repository breaking change требует Decision Log entry, impact analysis, consumer matrix update, migration plan, rollback plan и coordinated release.

## 17. MVP Alignment

Состав capabilities и правила активации — по [[Ayla MVP Scope and Release Contract]]; перечень сущностей приведён к AYLA-DEC-0016/0017/0020/0021/0022/0024 (v1.3).

MVP-active:

```text
Subject / User / Account / Identity Reference (ограниченный срез — AYLA-DEC-0016 п. 8)
Tenant / Provider / Provider Membership / Role Assignment / Specialist Profile
Consent
Context Fact (Memory Entry)
Intent
Catalog Service
Service Offering / Specialist Offering Assignment
Availability Calendar / Availability Rule / Schedule Block / Slot Hold
Recommendation
Appointment / Appointment Revision
Attribution Link
```

Ограниченный MVP scope:

```text
Inference
Outcome
MemoryProposal
Reschedule Proposal
Bookable Slot (вычисляемая проекция, не сущность — §7.10)
```

Deferred / proposal:

- Feedback — активация только через change control [[Ayla MVP Scope and Release Contract]] §11 (owner decision), см. §7.14;
- substitute workflow и time-boxed доступ (AYLA-DEC-0017 п. 9);
- merge Subjects, multi-account UI, дополнительные identity-каналы (AYLA-DEC-0016 п. 8);
- полная авто-синхронизация внешних календарей, произвольный RRULE (AYLA-DEC-0021);
- full payment aggregate;
- refund lifecycle;
- payout lifecycle;
- advanced outcome learning;
- provider settlement;
- universal ledger;
- multi-country compliance model.

**Cross-source contradiction record (P1-5): Feedback.** Core Scope: Feedback deferred ([[Ayla MVP Scope and Release Contract]] §5). Внешний источник (master-reviews-feedback handoff): production-blocking. Resolution owner: Product Owner. Activation prohibited until scope change через change control §11. См. §24 (Product, п. 6).

Ограниченный monetary contour по AYLA-DEC-0015 ([[Ayla Decision Log]]): списание подписки, списание booking fee 90 ₽, обработка результата списания, обновление billing status, применение provider eligibility, минимальная reconciliation с YooKassa. Этот контур не считается активацией полной Payment Processing capability и не создаёт универсальный payment domain (§2.2).

## 18. Acceptance Criteria

Документ готов к approval, когда все критерии в статусе PASSED:

| ID | Criterion | Status | Evidence | Blocker |
|---|---|---|---|---|
| CDM-AC-01 | Все MVP-active objects имеют owner | PARTIAL | §22 (v1.3: Offering → CAP-009, Availability → CAP-010 — закрыто AYLA-DEC-0020/0021; остаются Recommendation, Attribution Link) | Yes |
| CDM-AC-02 | Все объекты имеют stable ID | PASSED | §3.3 | No |
| CDM-AC-03 | Aggregate roots подтверждены | PARTIAL | §8 (roots определены, не подтверждены владельцем) | Yes |
| CDM-AC-04 | Lifecycles не конфликтуют с Intent Model и MVP Scope | PARTIAL | §7.5 (Intent — конфликт устранён); coverage расширено v1.3, неполно — см. примечание ниже | Yes |
| CDM-AC-05 | Systems of Record согласованы | PARTIAL | §12 (v1.3 — SoR по AYLA-DEC-0016/0017/0020/0021/0022/0024), §22 | Yes |
| CDM-AC-06 | Commands сопоставлены с API/tool contracts | FAILED | §10 (сопоставление не выполнено) | Yes |
| CDM-AC-07 | Events сопоставлены с Event Registry | PARTIAL | §11 (конвенция AYLA-DEC-0025 принята; семантический review первого среза pending — §24, Governance п. 6) | Yes |
| CDM-AC-08 | Consent rules согласованы с Consent Scope Registry | PASSED | §7.2 (v1.2.1, KM-CDM-6) | No |
| CDM-AC-09 | Safety rules согласованы с Safety Policy | FAILED | §24, Safety (открытые вопросы) | Yes |
| CDM-AC-10 | Recommendation и Appointment связаны через recommendation_id | PASSED | §7.11, §7.12 (условная связь iff `origin = ai_recommendation` — AYLA-DEC-0022) | No |
| CDM-AC-11 | Нет скрытого ownership между contexts | PARTIAL | §8.6–§8.7, §13, §22 | Yes |
| CDM-AC-12 | Open questions закрыты или оформлены решениями | FAILED | §24 (решённые закрыты v1.3; backlog открыт) | Yes |

Текущий статус по критерию CDM-AC-04: Intent lifecycle приведён к status-enum Output Contract [[Ayla Intent Model Specification]] (§7.5) — конфликт устранён, критерий в части Intent выполнен.

Полнота покрытия lifecycle и per-object commands/events по [[Ayla MVP Documentation Roadmap]] §4.3 на текущей версии выполнена **частично**: lifecycle определён для Consent, Context Fact (Memory Entry), MemoryProposal, Inference, Intent, Provider Membership, Service Offering, Specialist Offering Assignment, Slot Hold, Recommendation, Appointment и Reschedule Proposal; для Subject, User, Account, Identity Reference, Tenant, Catalog Service, Attribution Link и Outcome lifecycle и per-object commands/events не определены — см. §24 (Architecture, п. 3).

## 19. Entity Relationship Diagram

```text
                                   ┌─────────┐
                                   │ Subject │──► User ──► Account ──► Identity Reference
                                   └────┬────┘
              grants                    │        owns
   ┌────────────────────────────────────┼────────────────────────┐
   ▼                                    ▼                        │
┌─────────┐               ┌────────────────────────┐ derived from │
│ Consent │               │ Context Fact           │◄───────────┐ │
└────┬────┘               │ (Memory Entry)         │            │ │
     │                    │ ◄── MemoryProposal     │            │ │
     │ gates              └───────────┬────────────┘            │ │
     │ (consent-gated only)           │ evidence                │ │
     │                                ▼                         │ │
     │                         ┌──────────┐           ┌───────────┐
     │                         │  Intent  │◄──────────│ Inference │
     │                         └────┬─────┘ evidence  └───────────┘
     │                              │ resolved (intent-level readiness)
     │                              ▼
     │                      ┌─────────────────┐  candidates: Service Offering /
     └─────────────────────►│  Recommendation │  Specialist Offering Assignment
                            │ (recommendation │
                            │      _id)       │
                            └───────┬─────────┘
                                    │ accepted
                                    ▼
                            ┌──────────────┐  revisions ┌─────────────────────┐
                            │ Appointment  │───────────►│ Appointment Revision│
                            └──────┬───────┘            └─────────────────────┘
                                   │ lineage (reschedule_of / root_appointment_id)
                                   ├──► Reschedule Proposal (pending не изменяет Appointment)
                                   ▼
                            ┌──────────┐        ┌──────────────┐
                            │ Outcome  │        │   Feedback   │ (deferred / proposal — §7.14)
                            └──────────┘        └──────────────┘

Коммерческая цепочка (AYLA-DEC-0020):

Catalog Service ◄── Service Offering ◄── Specialist Offering Assignment ──► Provider Membership ──► Specialist Profile

Доступность (AYLA-DEC-0021):

Availability Calendar / Rule / Schedule Block / Slot Hold ──(вычисление)──► Bookable Slot (проекция, без SoR) ──► Appointment
```

Дополнительные связи, не показанные на схеме: Appointment хранит `recommendation_id` (условно, iff `origin = ai_recommendation` — §7.12); Outcome ссылается на `appointment_id` и `recommendation_id` (§7.15); Attribution Link связывает Recommendation с Action через `recommendation_id` (§7.13); Consent ограничивает (gates) обработку Context Fact и Inference только для consent-gated обработки (§7.3, §7.4, §20).

Граница resolver (KM-IM-1): Intent Resolver processing (internal, §7.5) → produces → Intent Resolution Result / aggregate state; внутренние состояния resolver (`received`, `detected`, `resolving`) на схеме не отображаются и не являются доменными объектами.

## 20. Domain Dependency Graph

```text
Consent ──► Context Fact ──► Intent ──► Recommendation ──► Appointment ──► Outcome
  │             ▲                ▲             │                 │
  │             │                │             ▼                 ▼
  │          Inference ──────────┘      Attribution Link    Appointment Revision
  │                                        ──► Action      (same-ID) / lineage
  │                                                         (replacement,
  └── ребро Consent → Context Fact действует только          reschedule_of)
      для consent-gated facts (persistent context,         Reschedule Proposal ─┘
      personalization по [[Consent Scope Registry]])      (pending не изменяет Appointment)

Catalog Service ──► Service Offering ──► Specialist Offering Assignment ──► Provider Membership ──► Specialist Profile

Availability Calendar / Rule / Schedule Block / Slot Hold ──► Bookable Slot (проекция, без SoR) ──► Appointment
```

Правила чтения графа:

1. Consent не зависит ни от одного объекта. Consent гейтует только обработку на основании согласия — persistent context и personalization по [[Consent Scope Registry]]; факты service delivery обрабатываются на договорном основании и не требуют Consent.
2. Inference является производной от Context Fact и не создаёт обратной зависимости. Граница: Intent Resolver processing (internal, §7.5) → produces → Intent Resolution Result / aggregate state; internal processing states в граф зависимостей не входят.
3. Recommendation зависит от resolved Intent; Appointment зависит от Service Offering и Specialist Offering Assignment и — для `origin = ai_recommendation` — от Recommendation (`recommendation_id`, AYLA-DEC-0022 п. 11); Outcome зависит от Appointment.
4. Bookable Slot — вычисляемая проекция от Availability Calendar/Rule/Schedule Block/Slot Hold и `effective_duration` assignment; не сущность и не создаёт зависимости владения (AYLA-DEC-0021 п. 1).
5. Обратных (циклических) зависимостей владения не допускается (§5, §8).

## 21. Global Domain Invariants

Сквозные инварианты уровня всей доменной модели. Дополняют per-object инварианты §7 и принципы §3, не заменяя их.

1. Recommendation не существует без Intent: каждая Recommendation ссылается на resolved Intent (дополняет §7.11, инвариант 2).
2. Appointment не существует без Service Offering и Specialist Offering Assignment: Appointment всегда ссылается на конкретные Offering и Assignment, принадлежащие одному tenant (дополняет §7.12, инвариант 11).
3. Service Offering не существует без Catalog Service (дополняет §7.9, инвариант 1); Specialist Offering Assignment не существует без Offering и Specialist Membership (AYLA-DEC-0020).
4. Consent никогда не выводится из поведения: ни поведение пользователя, ни Inference, ни отсутствие возражений не создают и не расширяют Consent; допустимы только явные переходы lifecycle Consent (§7.2) по структуре [[Consent Scope Registry]].
5. Inference никогда не становится Fact автоматически (§3.6): переход Inference → подтверждённый Context Fact возможен только через явное подтверждение (user confirmation / verification) с фиксацией provenance и whitelist check (§7.3, AYLA-DEC-0023 п. 2).
6. Копирование поля не переносит ownership (§5); snapshot не становится новой authoritative версией (§13).
7. LLM output не создаёт authoritative state ни для одного объекта модели (§3.5, §14.2).
8. Internal processing state ≠ published domain state: внутренние состояния обработки (resolver, runtime) не входят в публичные контракты и не запускают downstream (§7.5, KM-IM-1).
9. Readiness одного слоя не означает readiness downstream: `resolved` Intent — только intent-level readiness, не execution readiness (§7.5).
10. Ни один internal resolver state не может быть представлен публичным контрактным значением с иным бизнес-смыслом (нарушение §3.10 One Canonical Meaning).
11. Исполнитель Appointment разрешается только через цепочку Specialist Offering Assignment → Provider Membership → Specialist Profile; прямые `Specialist.provider_id` и канонический `specialist_id` как SoR-атрибуты запрещены (AYLA-DEC-0017 п. 4, AYLA-DEC-0020 п. 8).
12. Bookable Slot не имеет собственного состояния: доступность вычисляется и не может быть изменена иначе как через Availability Calendar / Rule / Schedule Block / Slot Hold или Appointment (AYLA-DEC-0021).
13. Ни одна операция не создаёт cross-tenant lineage Appointment (AYLA-DEC-0022 п. 2–3).
14. Один completed outcome в lineage → не более одного booking fee; billing проверяет lineage по `root_appointment_id` (AYLA-DEC-0010, AYLA-DEC-0022 п. 7).

## 22. Bounded Context Ownership Matrix

Матрица владения доменными объектами. Сводит §7, §8 и §12; при расхождении приоритет имеет §12.

Статусы: `confirmed` — владение подтверждено нормативным источником вне настоящего документа ([[AMD-020 Pilot Scope Registry]], [[Ayla Domain Capability Registry]]); `proposal` — владение зафиксировано настоящим документом и ожидает подтверждения владельца; `unresolved` — открытый вопрос (§24).

| Domain Object | Owner Context | Статус |
|---|---|---|
| Subject | Memory & Identity Domain | confirmed (AYLA-DEC-0016 п. 10) |
| User | Identity and Access (CAP-019) | confirmed (AYLA-DEC-0016 п. 10) |
| Account | Identity and Access (CAP-019) | confirmed (AYLA-DEC-0016 п. 10) |
| Identity Reference | Identity and Access (CAP-019) | confirmed (AYLA-DEC-0016 п. 10) |
| Tenant | Identity and Access (CAP-019) | confirmed (AYLA-DEC-0017 п. 11) |
| Provider | Provider Management (CAP-009) | confirmed (AYLA-DEC-0017 п. 11) |
| Provider Membership | Provider Management (CAP-009, business truth; CAP-019 — enforcement projection) | confirmed (AYLA-DEC-0017 п. 11) |
| Role Assignment | Provider Management (CAP-009, business truth; CAP-019 — enforcement projection) | confirmed (AYLA-DEC-0017 п. 11) |
| Specialist Profile | Provider Management (CAP-009) | confirmed (AYLA-DEC-0017 п. 11) |
| Consent | Consent Management | confirmed (AMD-020: Consent Records → Consent Domain; CAP-002) |
| Context Fact (Memory Entry) | Memory & Identity Domain (W3 Memory Service) | confirmed (AMD-020; AYLA-DEC-0024 п. 10) |
| MemoryProposal | Memory & Identity Domain (W3 Memory Service) | confirmed (AYLA-DEC-0024 п. 2, 10) |
| Inference (persistent) | Memory & Identity Domain | confirmed (AMD-020, Ownership Summary: Semantic Memory → Memory & Identity Domain) |
| Intent | Intent Understanding (разделение владения: aggregate lifecycle/persistence vs Output Contract vs AI Runtime — §12, KM-IM-1) | proposal |
| Catalog Service | Service Catalog (CAP-008) | confirmed (AYLA-DEC-0020 п. 14) |
| Service Offering | Provider Management (CAP-009) | confirmed (AYLA-DEC-0020 п. 14) |
| Specialist Offering Assignment | Provider Management (CAP-009) | confirmed (AYLA-DEC-0020 п. 14) |
| Availability Calendar / Rule / Schedule Block / Slot Hold | Availability Management (CAP-010) | confirmed (AYLA-DEC-0021 п. 2) |
| Bookable Slot | нет owner context — вычисляемая проекция без SoR | confirmed (AYLA-DEC-0021 п. 1) |
| Recommendation | Recommendation | unresolved (§24, Architecture п. 1) |
| Appointment | Appointment Management (CAP-011) | confirmed (CAP-011 authoritative_responsibility; AYLA-DEC-0022) |
| Appointment Revision | Appointment Management (CAP-011) | confirmed (AYLA-DEC-0022) |
| Reschedule Proposal | Appointment Management (CAP-011) | confirmed (AYLA-DEC-0022) |
| Attribution Link | Attribution | unresolved (§24, Architecture п. 2) |
| Feedback (deferred / proposal — §7.14) | Feedback Collection | proposal |
| Outcome | Outcome Learning / Backend facts | proposal |

## 23. Domain Object ↔ Capability Mapping

Сопоставление доменных объектов с capability из [[Ayla Domain Capability Registry]]. Статусы: `confirmed` — объект входит в `owned_concepts` соответствующей capability; `proposal` — маппинг не зафиксирован нормативным решением и требует подтверждения владельца (§24); `unresolved` — маппинг затрагивает открытый вопрос (§24).

| Domain Object | CAP-ID | Capability (canonical_name) | Статус маппинга |
|---|---|---|---|
| Subject | CAP-019 / CAP-001 | Identity and Access / Personal Context Management (граница — Memory & Identity Domain SoR по AYLA-DEC-0016 п. 10) | proposal |
| User | CAP-019 | Identity and Access | confirmed (AYLA-DEC-0016 п. 10) |
| Account | CAP-019 | Identity and Access | confirmed (AYLA-DEC-0016 п. 10) |
| Identity Reference | CAP-019 | Identity and Access | confirmed (AYLA-DEC-0016 п. 10) |
| Tenant | CAP-019 | Identity and Access | confirmed (AYLA-DEC-0017 п. 11) |
| Consent | CAP-002 | Consent Management | confirmed |
| Context Fact (Memory Entry) | CAP-001 | Personal Context Management | confirmed (AYLA-DEC-0023/0024) |
| MemoryProposal | CAP-001 | Personal Context Management | confirmed (AYLA-DEC-0024) |
| Inference | CAP-001 | Personal Context Management | proposal |
| Intent | CAP-003 | Intent Understanding | confirmed |
| Catalog Service | CAP-008 | Service Catalog Management | confirmed (AYLA-DEC-0020 п. 14) |
| Provider | CAP-009 | Provider and Specialist Management | confirmed |
| Provider Membership | CAP-009 | Provider and Specialist Management (business truth; CAP-019 — enforcement) | confirmed (AYLA-DEC-0017 п. 11) |
| Role Assignment | CAP-009 | Provider and Specialist Management (business truth; CAP-019 — enforcement) | confirmed (AYLA-DEC-0017 п. 11) |
| Specialist Profile | CAP-009 | Provider and Specialist Management | confirmed (AYLA-DEC-0017) |
| Service Offering | CAP-009 | Provider and Specialist Management | confirmed (AYLA-DEC-0020 п. 14) |
| Specialist Offering Assignment | CAP-009 | Provider and Specialist Management | confirmed (AYLA-DEC-0020) |
| Availability Calendar / Rule / Schedule Block / Slot Hold | CAP-010 | Availability Management | confirmed (AYLA-DEC-0021 п. 2) |
| Bookable Slot | CAP-010 | Availability Management (вычисляемая проекция, не сущность) | confirmed (AYLA-DEC-0021 п. 1) |
| Recommendation | CAP-004 | Recommendation Formation | confirmed |
| Appointment | CAP-011 | Appointment Management | confirmed |
| Appointment Revision | CAP-011 | Appointment Management | confirmed (AYLA-DEC-0022) |
| Reschedule Proposal | CAP-011 | Appointment Management | confirmed (AYLA-DEC-0022) |
| Attribution Link | CAP-013 | Recommendation Attribution | confirmed |
| Feedback | CAP-012 | Feedback Collection (deferred / proposal — §7.14) | proposal |
| Outcome | CAP-006 | Outcome Capture | confirmed |
| Billing eligibility | CAP-022 | Billing Eligibility | confirmed (контур AYLA-DEC-0015) |
| Payment result | CAP-023 | Payment Processing | confirmed (external deferred, контур AYLA-DEC-0015) |

## 24. Open Questions

### Закрытые (v1.3, со ссылками на решения)

1. ~~Граница Provider Management и Service Catalog для Offering~~ — AYLA-DEC-0020 п. 2, 14: Service Offering и Specialist Offering Assignment → Provider Management (CAP-009, business truth); CAP-008 владеет только каноническим Catalog Service; формулировка `Provider/Catalog boundary` упразднена.
2. ~~Owner Availability Slot~~ — AYLA-DEC-0021 п. 1–2: Bookable Slot — вычисляемая проекция без SoR; контур Availability (Calendar/Rule/Schedule Block/Slot Hold) → CAP-010.
3. ~~Нужен ли отдельный Personal Context aggregate root~~ — AYLA-DEC-0024 п. 10: Memory Service — единственный владелец state transitions; Memory Entry иммутабельна, история через supersession (§7.3, §8.2).
4. ~~Двойная семантика `Intent.status = unresolved`~~ — KM-IM-1 (§7.5; бывш. Architecture п. 8).
5. ~~`recommendation_id` обязателен для всех Appointment или только recommendation-originated~~ — AYLA-DEC-0022 п. 11: условная связь, обязателен iff `origin = ai_recommendation` (бывш. Architecture п. 9).
6. ~~Финальный владелец Service Offering~~ — AYLA-DEC-0020 (бывш. Architecture п. 11).
7. ~~Формализация Appointment reschedule lifecycle~~ — AYLA-DEC-0022: reschedule — версионируемая операция (same-ID Revision / replacement lineage), статус `rescheduled` не вводится (бывш. Architecture п. 12).

### Architecture (backlog)

1. Где хранится authoritative Recommendation record.
2. Нужен ли отдельный Attribution context в MVP.
3. Lifecycle и per-object commands/events не определены для Subject, User, Account, Identity Reference, Tenant, Catalog Service, Attribution Link и Outcome — требуется дополнение до соответствия [[Ayla MVP Documentation Roadmap]] §4.3 (см. §18, CDM-AC-04).
4. Action — полноценный доменный объект или generic `action_id` подлежит удалению из модели (§6.3, §7.13) (требует owner decision).
5. Провенанс записи Change Log v1.1 («восстановленная MVP-aligned версия после удаления предыдущего файла») требует подтверждения владельца документа.
6. Retention терминальных Slot Hold (AYLA-DEC-0021 Q7): сроки не установлены; физическое удаление, разрушающее аудит, запрещено.
7. Calendar Sync SLA (AYLA-DEC-0021 Q9): числовые значения — в обязательный integration contract, не в доменный DEC.
8. Маппинг Subject на capability: CAP-019 vs CAP-001 при SoR Memory & Identity Domain (§23) (требует owner decision).

### Product (backlog)

1. Какие intent types входят в release.
2. Какие alternatives обязательны.
3. Какое окно assisted attribution использовать.
4. Какие feedback types входят в пилот (только после активации Feedback через Scope Contract §11 — см. §7.14).
5. Active Outcome slice: какие outcome types фиксируются в MVP и через какой источник (§7.15, §17) (требует owner decision).
6. Cross-source contradiction P1-5: Feedback deferred по Scope Contract §5 vs production-blocking по master-reviews-feedback handoff — resolution owner Product Owner, активация только через change control §11 (см. §17) (требует owner decision).
7. Подтвердить product defaults: late-window порог 1 час (AYLA-DEC-0022 п. 5), лимит 3 self-service reschedule на lineage (п. 6), TTL Slot Hold 15 минут (AYLA-DEC-0021 п. 3), горизонт проекции 30 дней (п. 10).
8. Какие user facts разрешены для persistent context — частично закрыто whitelist AYLA-DEC-0023; расширение whitelist — только owner decision с проверками product_value / privacy_review / retention_policy / deletion_behavior (п. 5 DEC).

### Privacy (backlog)

1. Mapping whitelist-категорий на consent scope — согласование с [[Consent Scope Registry]] (AYLA-DEC-0023 п. 1).
2. Какие inferred preferences разрешены — pipeline AYLA-DEC-0023 п. 2; красная зона default deny (п. 4).
3. Retention transcript и Recommendation.
4. Какие данные запрещено передавать в LLM.
5. Retention manifest (AYLA-DEC-0016 п. 7) — отдельный privacy/legal артефакт, не создан.

### Safety (backlog)

1. Полный список health-sensitive triggers.
2. Какие рекомендации требуют deterministic block.
3. Где требуется human escalation.
4. Какие категории запрещены без health check.
5. Периодичность reconfirmation user-stated safety constraints (AYLA-DEC-0024 п. 8).

### Governance (backlog)

1. Кто owner public domain schemas.
2. Кто утверждает lifecycle changes.
3. Кто owner tool schemas при конфликте consumers.
4. Как синхронно обновляются pins consumers.
5. Какой документ canonical для enum values.
6. Семантический review первого среза событий в [[Ayla Domain Event Registry]] (AYLA-DEC-0025 п. 8): `intent.resolved` как общее событие не использовать; семантика `IntentResolved`/`IntentAbandoned`/`IntentFulfilled`, семейств `recommendation.*` и `qualified_action.attributed` — pending. **P1-1 — решён owner ruling:** DEC-0025 и Domain Event Registry имеют приоритет в именовании событий; канонические события — `consent.granted` / `consent.denied` / `consent.revoked` / `consent.expired`; snake_case (`consent_granted` и т.д.) — только legacy aliases либо внутренние audit codes, не второй канон; новые producers/consumers используют только `consent.*`; временный compatibility mapping допустим на период миграции; envelope, payload version и producer определяются Domain Event Registry; CSR не создаёт собственную event naming convention. Требуется amendment CSR §9.1 и migration plan для legacy snake_case aliases.
7. `IntentAbandoned` — доменное событие vs analytics/session/derived label (KM-IM-1, §7.5, §11) (требует owner decision).
8. **P1-2 — решён owner ruling:** `needs_reconfirmation` НЕ добавляется в lifecycle Consent как статус; это результат consent resolution/remediation при merge (`consent_resolution = needs_reconfirmation`), а не состояние Consent наряду с `granted`/`denied`/`revoked`/`expired`. Merge запрещён до реализации consent resolver (AYLA-DEC-0016 п. 4); вопрос не блокирует CDM и закрывается до активации Subject merge.

## 25. Approval

| Роль | Статус | Имя | Дата |
|---|---|---|---|
| Product Owner | Pending |  |  |
| Domain Architecture | Pending |  |  |
| Backend Owner | Pending |  |  |
| AI Platform Owner | Pending |  |  |
| Privacy/Safety Owner | Pending |  |  |

## 26. Change Log

| Версия | Дата | Изменение | Автор |
|---|---|---|---|
| 1.1 | 2026-07-28 | Восстановленная MVP-aligned версия после удаления предыдущего файла (провенанс требует подтверждения владельца — см. §24, Architecture п. 7) | Ayla Architecture |
| 1.1.1 | 2026-07-28 | Слияние с vault-версией 1.0: перенесены §2.3 Normative Force, §3.2 Technical Representations, §3.10 One Canonical Meaning, §3.11 Historical Consistency; Intent lifecycle (§7.5) приведён к status-enum Output Contract [[Ayla Intent Model Specification]] с маппинг-таблицей состояний потока; §4 подчинён [[Ayla Glossary]] (нормативная оговорка); Feedback переведён в deferred / proposal (§7.14, §17) — активация только через Scope Contract §11; `client_id` унифицирован к `subject_id` (§7.12); строки Billing eligibility / Payment result в §12 помечены как ограниченный контур по AYLA-DEC-0015; frontmatter приведён к schema v1.12 | Domain Architecture |
| 1.2 | 2026-07-28 | Пакет доработок по результатам независимого ревью. A: §7.2 и §8.1 — собственная схема полей Consent заменена ссылкой на [[Consent Scope Registry]] (нормативная структура scope/purpose/policy bindings выведена из документа); §12 — Inference SoR разделён на producer/processor (AI Runtime) и persistent storage (Memory & Identity Domain по [[AMD-020 Pilot Scope Registry]], Ownership Summary), добавлено пояснение про ephemeral Inference; строки Billing eligibility / Payment result приведены к «owning capability defined outside this document» (CAP-022) и «external deferred» без введения новых bounded contexts. B: добавлены §19 Entity Relationship Diagram, §20 Domain Dependency Graph, §21 Global Domain Invariants, §22 Bounded Context Ownership Matrix, §23 Domain Object ↔ Capability Mapping, §8.6–§8.7 Aggregate owns/references/does-not-own для Recommendation и Appointment; §10 Commands сгруппированы (User/System/AI/Administrative) и §11 Events сгруппированы (Business/Technical/Integration) без изменения состава; §12 дополнен колонками Caching allowed / Snapshot allowed / Replicated; бывшие §19–§21 перенумерованы в §24–§26 | Domain Architecture |
| 1.2.1 | 2026-07-28 | Пакет «внутренние противоречия» + KM-CDM-6. (1) §7.2 — lifecycle/commands/events Consent приведены к актуальной модели [[Consent Scope Registry]] (состояния not_requested/granted/denied/revoked/expired, правило повторного согласия через новую consent record, добавлены DenyConsent/ConsentDenied), делегирование CSR усилено (lifecycle/commands/events нормативно в CSR §7–§9, здесь — сводка); (2) §20 правило 1 — Consent гейтует только обработку на основании согласия (persistent context, personalization), факты service delivery — на договорном основании; ASCII-схема помечена «consent-gated facts only»; (3) §20 правило 3 — зависимость Appointment от Recommendation смягчена до recommendation-originated, универсальность `recommendation_id` вынесена в §24 (Architecture п. 9); (4) §26 — вторая запись 1.1 переименована в 1.1.1, broken reference «§19» исправлена на «§24»; (5) §22 и §23 — добавлены статусы строк confirmed / proposal / unresolved с легендой; (6) §10/§11 — SubmitFeedback и FeedbackSubmitted вынесены в подраздел Deferred (активация через Scope Contract §11), состав сохранён; в §10/§11 добавлены DenyConsent/ConsentDenied для согласованности с §7.2; (7) §24 — добавлены пункты v1.3: двойная семантика Intent.status unresolved, обязательность `recommendation_id`, статус Action, владелец Service Offering, reschedule lifecycle Appointment (Architecture п. 8–12), active Outcome slice (Product п. 6), согласование event names (Governance п. 6) | Domain Architecture |
| 1.2.2 | 2026-07-28 | Governance repair (без доменных решений): (1) §1 — добавлен Readiness-блок (все гейты No; статус Draft / Proposed — substantively developed, internally incomplete; блокирующие области: identity foundation, scheduling и Appointment, lifecycle completeness, Handoff Coverage Matrix, SoR owners); (2) §2.3 — пояснение `source_kind: canonical` (происхождение, не нормативная зрелость; нормативная сила только при `status: approved` — AYLA-DEC-0013, отклонение `canonical-candidate`); (3) frontmatter `depends_on` дополнен нормативными ссылками ([[Ayla MVP Scope and Release Contract]], [[Ayla MVP Documentation Roadmap]], [[Ayla Intent Model Specification]], [[Consent Scope Registry]], [[AMD-020 Pilot Scope Registry]], [[Ayla Domain Capability Registry]], [[Ayla Decision Log]]); (4) §17 — зарегистрирован cross-source contradiction P1-5 по Feedback (deferred по Scope Contract §5 vs production-blocking по master-reviews-feedback handoff; resolution owner Product Owner), пункт в §24 (Product п. 7); (5) §18 — Acceptance Criteria формализованы в таблицу CDM-AC-01…12 (Criterion / Status / Evidence / Blocker) без изменения содержания критериев | Domain Architecture |
| 1.2.3 | 2026-07-28 | KM-IM-1 Intent lifecycle boundary (owner ruling, ACCEPTED): (1) §7.5 переработан — разделены internal resolution processing (`received → detected → resolving → first output produced`, не сериализуется, не orchestration/readiness) и published Intent status (6 значений Output Contract [[Ayla Intent Model Specification]]; `unresolved` — только результат завершённого pass; переход «detected → unresolved» и «unresolved (interim)» удалены; guard против default `status = unresolved` для NOT NULL); добавлены подразделы Intent-level readiness (`resolved` ≠ action authorized/confirmed/executed/succeeded) и Events; инварианты пересобраны (14); (2) §11 — `IntentDetected` переведён в technical/observability, `IntentResolved`/`IntentAbandoned` — semantics pending Domain Event Registry, `IntentFulfilled` — derived projection; (3) §10 — `DetectIntent` исключён (detected = внутренний этап `ResolveIntent`); (4) §12 — владение Intent разделено (aggregate lifecycle/persistence, Output Contract, internal resolver state, execution result, cross-intent attribution), AI Runtime не SoR для completed action; (5) §21 — добавлены инварианты 8–10 (internal ≠ published, readiness послойно, запрет подмены бизнес-смысла); (6) §19/§20 — зафиксирована граница Intent Resolver processing → produces → Intent Resolution Result; (7) §24 — Architecture п. 8 закрыт (KM-IM-1), Governance п. 6 дополнен, добавлен Governance п. 7 (`IntentAbandoned`). Статус документа и readiness-блокеры не изменены | Domain Architecture |

| 1.3 | 2026-07-28 | Канонический update: интеграция принятых AYLA-DEC-0016/0017/0020/0021/0022/0023/0024/0025 (traceability — Appendix A). §7.1 — identity-модель Subject/User/Account/Identity Reference с кардинальностью и неизменным `subject_id` (DEC-0016); §7.8 — Tenant/Provider Membership/Role Assignment/Specialist Profile, отмена `Specialist.provider_id`, lifecycle Membership (DEC-0017); §7.6 — Service → Catalog Service; §7.9 — Offering принадлежит Provider, `specialist_id` упразднён, добавлена Specialist Offering Assignment с effective values и lifecycle (DEC-0020); §7.10 — Bookable Slot как вычисляемая проекция без SoR, сущности Availability Calendar/Rule/Schedule Block/Slot Hold → CAP-010 (DEC-0021); §7.12 — Appointment: `origin` (7 значений), snapshots, `version`, lineage (`reschedule_of`/`root_appointment_id`/`reschedule_count`), `external_ref`, условный `recommendation_id`, Appointment Revision, Reschedule Proposal; статус `rescheduled` упразднён (DEC-0022); §7.3 — Context Fact приведён к Memory Contract (иммутабельность, typed value, purpose_tags, provenance, source_event_id, `deletion_pending`) + MemoryProposal; Temporary Context → Conversation State (DEC-0023/0024); §11 — PascalCase-имена и прежний envelope упразднены, нормативные имена/payload делегированы [[Ayla Domain Event Registry]] (DEC-0025); §2/§3.3/§4/§8/§12/§15/§17/§18/§19–§23 синхронизированы; §24 — решённые вопросы закрыты со ссылками на DEC, остальные собраны в backlog; §1 Readiness — сняты области identity foundation, tenancy, offering, availability, appointment. Статус документа не изменён | Domain Architecture |
| 1.3 | 2026-07-28 | Owner review amendments (точечные): (1) §7.2 — явное разделение нормативного владения: CSR владеет scope/purpose/policy bindings/lifecycle Consent, Domain Event Registry — именами событий, envelope, payload schema, версиями и authoritative producer; (2) §7.12 — ID Reschedule Proposal приведён к канону `reschedule_proposal_id` (`proposal_id` сохранён только у MemoryProposal, §3.3); (3) §7.12 — добавлена норма: replacement, не исполняющий исходную Recommendation, не получает `recommendation_id`, `origin` отражает фактическое происхождение (например `rebooking`), `origin = ai_recommendation` — только с валидным `recommendation_id`; (4) §24 Governance п. 6 — P1-1 решён owner ruling: приоритет DEC-0025/Domain Event Registry в именовании событий, snake_case — legacy aliases/audit codes, требуется amendment CSR §9.1 и migration plan; (5) §24 Governance п. 8 — P1-2 решён owner ruling: `needs_reconfirmation` — результат consent resolution при merge, не статус lifecycle Consent | Domain Architecture |

## Appendix A. DEC Traceability Matrix (v1.3)

Таблица трассировки интегрированных решений: DEC → принятое правило → раздел CDM → изменение → проверка. Источник: [[Ayla Decision Log]].

| DEC | Принятое правило | Раздел CDM | Изменение | Проверка |
|---|---|---|---|---|
| AYLA-DEC-0016 п. 1–2 | Пять разделённых identity-сущностей; кардинальность; не-каскадное удаление; `subject_id` неизменен | §7.1, §21 | §7.1 (User) заменён на группу Subject/User/Account/Identity Reference с инвариантами | grep: схема §7.1 содержит `subject_id`/`user_id`/`account_id`/`identity_ref_id` |
| AYLA-DEC-0016 п. 3 | Запрет унификации идентификаторов на `user_id` | §3.3 | Список stable ID пересобран, запрет зафиксирован | grep §3.3 |
| AYLA-DEC-0016 п. 4–8 | Merge/relink/person-wide deletion — управляемые операции; merge запрещён до consent resolver; MVP-срез identity | §7.1 (операции), §2.2, §17 | Добавлено; deferred-пункты в §2.2/§17 | Ручная сверка с DEC |
| AYLA-DEC-0016 п. 10 | SoR: Subject → Memory & Identity Domain; User/Account/Identity Reference → CAP-019 | §12, §22, §23 | Новые строки SoR и статусы confirmed | Таблицы §12/§22/§23 |
| AYLA-DEC-0017 п. 1–4 | Профиль ≠ доступ ≠ tenant; отмена `Specialist.provider_id`; Membership — единственная связь с tenant | §7.8 | §7.8 (Specialist) заменён на Tenant/Provider Membership/Role Assignment/Specialist Profile | grep `provider_id` в Specialist Profile — только упоминание отмены |
| AYLA-DEC-0017 п. 5–8, 10 | Lifecycle Membership `requested/invited → active ⇄ suspended → revoked`; revoke не удаляющий + remediation `needs_resolution`; роли MVP; ≥1 active owner Membership | §7.8 | Добавлено | Ручная сверка с DEC |
| AYLA-DEC-0017 п. 11 | SoR: CAP-009 business truth, CAP-019 enforcement projection; Tenant → CAP-019 | §12, §22 | Строки Membership/Role Assignment/Tenant | Таблицы §12/§22 |
| AYLA-DEC-0020 п. 1–2, 14 | Catalog Service → Service Offering → Specialist Offering Assignment; Offering принадлежит Provider; `Provider/Catalog boundary` упразднена | §7.6, §7.9, §12, §22 | §7.6 → Catalog Service; §7.9 переписан; SoR Offering/Assignment → CAP-009 | grep `Provider/Catalog boundary` — только changelog |
| AYLA-DEC-0020 п. 3–5, 11 | `assignment.specialist_id` запрещён; effective values; `booking_allowed` — policy evaluation; lifecycle Offering и Assignment | §7.9 | Добавлены Assignment, effective values, оба lifecycle | grep `specialist_id` в §7.9 — только запрет |
| AYLA-DEC-0020 п. 8 | Appointment: `service_offering_id`/`specialist_assignment_id`/`specialist_membership_id` + snapshots; канонический `specialist_id` запрещён; инвариант цепочки | §7.12, §21 (инв. 11) | §7.12 переписан | grep §7.12: `price_snapshot`, `effective_duration_snapshot`, `offering_title_snapshot` |
| AYLA-DEC-0021 п. 1 | Bookable Slot — вычисляемая проекция без SoR; ключ `(specialist_offering_assignment_id, starts_at)`; `slot_id` не вводится | §7.10, §3.3, §12, §22 | §7.10 (Availability Slot) заменён проекцией + сущностями контура | grep: Slot как entity с SoR — 0 |
| AYLA-DEC-0021 п. 2–6 | Calendar/Rule/Schedule Block/Slot Hold → CAP-010; Hold lifecycle `held → confirmed \| expired \| released`, TTL 15 мин; DB-enforced overlap (constraint ЛИБО ledger, без выбора); release holds при `AVAILABILITY_CHANGED`; timezone IANA/wall time/UTC | §7.10 | Добавлено | Ручная сверка с DEC |
| AYLA-DEC-0021 п. 7–9 | Несинхронизированный dual-source запрещён; offline/admin-записи без hold с override-аудитом; self-service SICK_DAY | §7.10, §7.12 (инв. 15) | Добавлено | — |
| AYLA-DEC-0022 п. 1–3 | Reschedule — операция, не статус; same-ID/replacement матрица; старая запись → `cancelled` + `replaced_by_reschedule`; lineage-поля | §7.12 | Lifecycle исправлен, статус `rescheduled` удалён, матрица и lineage добавлены | grep `rescheduled` как статус — только цитаты/changelog/`appointment.rescheduled` |
| AYLA-DEC-0022 п. 4–6, 11 | `origin` (7 значений); условный `recommendation_id`; Reschedule Proposal (`pending \| accepted \| declined \| expired \| withdrawn`); pending не изменяет Appointment; late-window/лимиты — policy | §7.12, §20, §24 (closed п. 5) | Добавлено; §24 Architecture п. 9 закрыт | grep §7.12: `origin`/`reschedule_of`/`root_appointment_id`/`reschedule_count`/`external_ref`/`version` |
| AYLA-DEC-0022 п. 7–8 | Billing: один completed outcome в lineage → ≤1 booking fee, проверка по `root_appointment_id`; calendar modes `ayla_primary \| external_primary` | §7.12 (инв. 13, 15), §21 (инв. 13–14) | Добавлено | — |
| AYLA-DEC-0023 | Whitelist по категориям; inference→memory единственный pipeline; user-stated safety constraints (не medical facts); красная зона default deny; Persistent Memory ≠ состояние разговора | §7.3, §7.4 (инв. 5–6), §21 (инв. 5) | Добавлено | — |
| AYLA-DEC-0024 | MemoryEntry иммутабельна, статусы `active \| superseded \| expired \| deletion_pending \| deleted`, typed value, purpose_tags, provenance, `source_event_id`; MemoryProposal; Conversation State ≠ Persistent Memory; Memory Service — единственный владелец transitions | §7.3, §8.2, §12 | §7.3 переписан; MemoryProposal добавлен; Temporary Context вынесен из CDM | grep `deletion_pending` в §7.3 |
| AYLA-DEC-0025 | Конвенция `<domain>.<entity>.<fact>`; единый envelope; оси `semantic_class` × `publication_scope`; один authoritative producer; `appointment.*` canonical, `booking.*` legacy; нормативные имена/payload → Event Registry | §11 | §11 переписан ссылочно; PascalCase-имена и прежний envelope удалены | grep `booking.` — только legacy-пометка; PascalCase-имена событий — только legacy/pending-пометки и changelog |
