---
node_id: ayla.foundation.repository-responsibility-matrix
title: Ayla Repository Responsibility Matrix
type: architecture-specification
status: draft
decision_status: proposed
version: "1.0-draft"
owner: Platform Architecture
owners:
  - Product Owner
  - Platform Architecture
knowledge_area:
  - foundation
  - architecture
system_owner:
  - shared
source_kind: canonical
classification: internal
data_sensitivity: none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
updated: 2026-08-14
review_cycle: quarterly
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Ayla Glossary]]"
  - "[[Ayla Decision Log]]"
  - "[[Ayla MVP Scope and Release Contract]]"
  - "[[Consent Scope Registry]]"
  - "[[Data Inventory Matrix]]"
supersedes:
  - "Ayla Repository Responsibility Matrix v0.1"
superseded_by: []
---

# Ayla Repository Responsibility Matrix

## 1. Purpose

Этот документ задаёт единый контракт ответственности между доменами, репозиториями, приложениями и runtime-компонентами Ayla.

Он предотвращает:

- появление нескольких источников истины для одного бизнес-состояния;
- ошибочное отождествление домена с репозиторием или Django-приложением;
- запись бизнес-фактов из AI runtime, каналов, provider applications или knowledge vault;
- прямой доступ к чужим ORM-моделям и общей базе данных;
- публикацию событий потребителем вместо владельца факта;
- смешение канонической политики, implementation contract и runtime projection.

Документ находится в `00 Foundation` и является архитектурным основанием для:

1. `Ayla MVP Appointment Contract`;
2. `Ayla Domain Event Registry`;
3. `Salon Operations MVP - Product - Interaction Contract`;
4. `Screen Data Contracts`.

Документ фиксирует архитектурные границы. Он не утверждает неподтверждённые product decisions: такие места имеют статус `Proposed`, `Pending owner decision` или `Open question`.

## 2. Architectural Principles

### 2.1. Single Source of Truth

Для каждого authoritative business state существует один владелец домена и один назначенный System of Record. Репозиторий может реализовывать состояние, но сам факт существования кода не доказывает domain ownership.

Если ownership не подтверждён источниками, в этом документе не создаётся второй владелец: состояние маркируется `Proposed` или `Open question`.

### 2.2. Consumer Cannot Become Owner

Чтение данных, использование DTO, проекции, кэша, зеркала, event consumer или AI context envelope не создаёт ownership. Consumer может хранить техническую копию для своего runtime, но не может изменять её как каноническое бизнес-состояние.

### 2.3. AI Is Not Source of Truth

AI может:

- понимать пользовательский запрос;
- формировать предложение или recommendation;
- создать command request;
- вызвать approved tool;
- использовать approved, purpose-limited context.

AI не может владеть `Appointment`, `Availability`, `Payment`, `Consent`, provider state или иным transactional business fact. AI output не становится фактом без принятия команды владельцем домена.

### 2.4. Conversation Is Not Domain State

Conversation, message history, session state и delivery state — runtime-состояния канала/оркестрации. Они не являются автоматически:

- `Appointment`;
- `Consent`;
- acceptance recommendation;
- business fact;
- semantic memory.

Факт из разговора может быть создан только отдельным domain command и соответствующим policy/consent gate.

### 2.5. Domain, Repository, Physical Implementation, Runtime Storage

Эти четыре уровня разделяются:

| Уровень | Вопрос |
|---|---|
| Domain ownership | Кто отвечает за смысл, lifecycle и invariants состояния? |
| Repository ownership | Где поддерживается implementation contract и release? |
| Physical implementation | В каком приложении, модуле, сервисе или provider adapter это реализовано? |
| Runtime storage | Где конкретный deployment временно хранит state, cache или projection? |

`beautygo_backend` может быть реализацией transactional state, но это утверждение должно быть отдельно от утверждения, что весь booking domain совпадает с одним Django app или репозиторием.

## 3. Repository Inventory

### 3.1. `ayla-knowledge`

- **Purpose:** нормативный knowledge hub и canonical documentation repository.
- **Responsibility:** product/domain semantics, cross-system architecture, policy, consent and safety rules, terminology, ownership contracts and decision traceability.
- **Owned state:** normative documents and their governance metadata.
- **Consumed data:** approved decisions, domain evidence, implementation findings and repository contracts.
- **Forbidden ownership:** production transactional state, appointments, availability, payments, provider state, user PII, conversation runtime and AI-generated business facts.

### 3.2. `beautygo_backend`

- **Purpose:** transactional backend and current candidate implementation boundary for Ayla business state.
- **Responsibility:** backend API, transactional invariants, provider integrations, booking/appointment operations and enforcement at the data boundary where this is confirmed by contracts.
- **Owned state:** `Proposed` as operational transactional SoR for user/profile, provider/specialist, availability, appointment and payment state; see OD-RRM-1.
- **Consumed data:** provider integration data, authorized commands, policy and consent decisions, channel-originated requests.
- **Forbidden ownership:** conversation runtime, channel transport, prompt registry, shared AI mechanics, normative canon and global product semantics.

### 3.3. `ai-bot-platform`

- **Purpose:** conversation, channel and AI application runtime.
- **Responsibility:** webhook/channel adapters, conversation and session orchestration, retrieval boundary, tool invocation, event consumption, delivery and runtime observability.
- **Owned state:** runtime conversation/session/delivery state is the documented implementation mapping; domain ownership of these runtime concerns is `Proposed` under OD-RRM-2.
- **Consumed data:** backend APIs, approved projections, event contracts, consent decisions at retrieval boundary, AI-core APIs and channel inputs.
- **Forbidden ownership:** Appointment, Availability, Payment, Consent records, provider state, durable semantic memory and canonical PII.

### 3.4. `ayla-ai-core`

- **Purpose:** reusable AI mechanics and public Python/API boundary for multiple consumers.
- **Responsibility:** model/provider adaptation, prompt/context rendering mechanics, tool-loop primitives and safety-oriented rendering guards where contractually assigned.
- **Owned state:** reusable library code and provider adapter protocol; no direct domain storage ownership under OD-RRM-3 (`Proposed`).
- **Consumed data:** filtered context envelopes and approved tool contracts.
- **Forbidden ownership:** domain storage, Appointment, Availability, Payment, Consent persistence, provider state, raw PII and business transaction lifecycle.

### 3.5. `formula_tela`

- **Purpose:** pilot provider application and legacy/local salon runtime.
- **Responsibility:** provider-specific operations and legacy MAX/site functionality until an explicit cutover.
- **Owned state:** provider-local state and legacy implementation state only; global Ayla operational SoR status is not assigned.
- **Consumed data:** provider-local inputs and approved Ayla integration contracts.
- **Forbidden ownership:** global Ayla Appointment, global Availability, cross-provider memory, global Consent, global Recommendation or global business transactions.

### 3.6. Mobile App

- **Purpose:** primary product channel in the MVP release model where confirmed by the MVP scope decision.
- **Responsibility:** user-facing presentation, navigation, local interaction state and calls through public contracts.
- **Owned state:** channel-local UI/session state only; exact repository and persistent storage are `Open question`.
- **Consumed data:** screen DTOs, public API responses, approved events and command outcomes.
- **Forbidden ownership:** domain lifecycle, backend transactional state, consent records, provider state and AI canonical memory.

### 3.7. MAX Mini App

- **Purpose:** companion product surface.
- **Responsibility:** presentation and user interaction through approved API/tool contracts.
- **Owned state:** screen/session state only; physical implementation boundary is `Open question`.
- **Consumed data:** screen DTOs, availability/appointment projections and command outcomes.
- **Forbidden ownership:** Appointment, Availability, Payment, Consent, provider state or independent booking truth.

### 3.8. MAX Bot

- **Purpose:** companion conversational channel.
- **Responsibility:** channel interaction through the target conversation runtime; current legacy implementation may remain in `formula_tela` until cutover.
- **Owned state:** conversation/session/delivery state only in the target runtime; exact cutover and physical owner are `Open question`.
- **Consumed data:** channel events, approved context, domain API responses and command outcomes.
- **Forbidden ownership:** domain business facts, independent appointment state, consent records and provider state.

## 4. Responsibility Matrix

The matrix distinguishes confirmed/documented mapping from proposed target ownership. `O` = owner of the stated responsibility; `C` = consumer/implementer; `P` = projection or runtime copy; `—` = must not own.

| System | Owns | May Write | Consumes | Must Not Own |
|---|---|---|---|---|
| `ayla-knowledge` | Normative canon, shared semantics, policy and responsibility contract | Canonical documents and governance metadata | Decisions, evidence, implementation contracts | Transactional state, PII, AI/runtime state |
| `beautygo_backend` | **Proposed:** operational transactional SoR for Appointment, Availability, Provider/Specialist and Payment | Domain commands accepted by owning backend contracts | Authorized requests, provider data, policy/consent inputs | Conversation, prompts, channel transport, global canon |
| `ai-bot-platform` | **Proposed:** conversation/orchestration runtime; documented current mapping for channel and delivery runtime | Conversation/session/delivery state; tool requests and runtime metadata | Backend APIs, projections, events, filtered context, channel input | Appointment, Availability, Payment, Consent, provider state |
| `ayla-ai-core` | Reusable AI mechanics and provider adapter protocol | Library/runtime-local artifacts only | Approved context envelopes and tool contracts | Direct domain storage and business facts |
| `formula_tela` | Provider-local/legacy implementation only | Provider-local state within its contract | Provider inputs and approved integration contracts | Global Ayla operational SoR |
| Mobile App | **Proposed:** presentation/client runtime only | Local UI/session state through platform rules | Public APIs, DTOs, command outcomes | Domain state and independent cache-as-truth |
| MAX Mini App | **Proposed:** presentation/client runtime only | Local UI/session state through platform rules | Public APIs, DTOs, command outcomes | Domain state and independent booking truth |
| MAX Bot | **Proposed:** channel runtime only | Channel/session state through platform owner | Events, APIs, context and command outcomes | Domain state, Consent and provider state |

### 4.1. State ownership baseline

| Business state | Domain owner | Current/target SoR | Write authority | Status |
|---|---|---|---|---|
| Appointment lifecycle | Appointment Domain | `beautygo_backend` | Appointment domain command handler | `Proposed` under OD-RRM-1; domain capability is documented |
| Availability and slots | Availability Domain | `beautygo_backend` | Availability domain owner | `Proposed` implementation mapping |
| Provider/specialist profile and status | Provider and Specialist Domain | `beautygo_backend` | Provider domain owner | `Proposed` implementation mapping |
| Payment state | Payment/Billing Domain | `beautygo_backend` | Payment domain/integration owner | `Proposed` implementation mapping |
| Consent records and scope | Consent Domain | Consent Service/domain boundary | Consent owner only | Service/repository placement `Pending owner decision`; ownership is normative |
| Semantic memory | Memory/User Context Domain | Memory service/domain boundary | Approved memory flow only | Physical placement not assigned by this matrix |
| Conversation state | Conversation/Runtime Domain | `ai-bot-platform` target runtime | Conversation runtime | `Proposed` under OD-RRM-2 |
| Channel delivery state | Notification/Channel Runtime | `ai-bot-platform` target runtime | Channel runtime | Current mapping documented; final ownership `Proposed` |
| Provider-local state | Provider Integration/Provider application | `formula_tela` for pilot-local state | Provider application contract | Provider-specific, not global Ayla SoR |

## 5. Write Authority Model

Every cross-system operation is classified as one of four levels:

| Level | Meaning | Can change authoritative business state? |
|---|---|---|
| `READ` | Retrieve an approved fact or projection | No |
| `PROPOSE` | Produce a candidate, recommendation or suggested change | No |
| `COMMAND` | Request a business operation with validated intent and parameters | No by itself |
| `WRITE` | Validate invariants and commit the authoritative state transition | Yes, owner only |

Example: user says «перенеси запись».

1. AI/runtime understands intent (`PROPOSE`/interpretation).
2. AI/runtime creates `reschedule_appointment` command request (`COMMAND`).
3. Appointment domain validates ownership, status, slot and policy.
4. Appointment owner writes Appointment (`WRITE`).
5. Appointment owner publishes `appointment.rescheduled` after committed state.
6. AI/channel renders the result; rendering does not create the fact.

AI tool invocation is never equivalent to `WRITE`. A successful tool transport response is not proof that the business transaction committed.

## 6. Public Contract Ownership

Cross-repository communication MUST use explicit public contracts:

- API contracts;
- domain event contracts;
- tool contracts;
- SDK/library contracts;
- versioned DTO and screen data contracts.

The following are prohibited:

- direct access to another repository's ORM models;
- imports of internal Django models across repository boundaries;
- shared database ownership;
- writes to another system's tables;
- undocumented reliance on provider-specific storage;
- treating a mirror or cache as canonical.

A mirror may be read-only and must identify its source, version and freshness. Implementation repositories own their implementation contracts; `ayla-knowledge` owns shared semantics and normative cross-system meaning, unless an approved decision says otherwise.

## 7. API Ownership

A business operation belongs to the domain owner, not to the channel, AI tool or UI.

Example: `Reschedule Appointment` belongs to Appointment Domain. `reschedule_appointment()` in `ai-bot-platform` is an adapter that:

- validates input shape at the boundary;
- carries identity, tenant and consent context;
- calls the Appointment public contract;
- returns a typed outcome;
- does not implement or redefine Appointment invariants.

The backend/domain owner owns the transactional API contract and status semantics. The tool owner owns the adapter schema and runtime ergonomics. The shared meaning of the operation is documented in the domain contract.

## 8. Tool Ownership

Tool responsibility has three layers:

| Layer | Owner | Responsibility |
|---|---|---|
| Domain Command | Domain owner | Meaning, invariants, authorization, state transition and outcome |
| Backend Contract | Transactional implementation owner | API/wire contract, validation boundary, idempotency and persistence |
| AI Tool Schema | AI/channel runtime owner | Model-facing schema, argument extraction, retries and presentation mapping |

The AI tool schema is not a source of business rules. It cannot grant permissions, confirm a booking, infer consent or publish a domain event.

## 9. Event Ownership

- An event is created only by the owner of the fact it describes.
- A consumer does not become a producer by observing or reacting to an event.
- Tool invocation is not an event.
- A delivery receipt is not a business success.
- Event payload contracts must identify producer, version, event identity, occurred time, entity identity and causation/correlation identifiers.

Correct flow:

```text
beautygo_backend
  validates and commits Appointment
  publishes appointment.created

ai-bot-platform
  consumes appointment.created
  updates runtime/projection state
  informs the user through the channel
```

Incorrect flow:

```text
ai-bot-platform
  calls a tool
  publishes appointment.created
```

The latter can only publish a technical command/result signal, never an authoritative domain event.

## 10. Projection and Cache Rules

A projection is a read model, DTO, cache, screen model or AI context envelope. It is not domain state.

Every projection MUST declare:

| Field | Requirement |
|---|---|
| `source_system` | System that owns the source fact |
| `source_entity` | Entity or contract being projected |
| `source_version` | Version/event/API revision used |
| `freshness` | TTL or freshness expectation |
| `purpose` | Why this consumer receives it |
| `consent_scope` | Applicable privacy/consent basis where relevant |
| `failure_behavior` | What happens if freshness or source availability fails |

Projections are read-only from the consumer's domain perspective. A cache miss, stale projection or unavailable source must not be silently interpreted as a new business fact.

## 11. Failure Semantics

Integration success and business success are different outcomes.

| Integration outcome | Business interpretation |
|---|---|
| Timeout while creating appointment | Appointment status `unknown` until authoritative read/reconciliation; never `confirmed` |
| Provider API timeout | Provider result unknown; do not create a second independent Appointment truth |
| HTTP `201` returned but confirmation screen absent | Backend fact must be checked; UI silence is not failure or success by itself |
| Consent lookup unavailable | Fail closed; do not interpret absence as consent granted |
| Event delivery delayed | Domain fact remains in source SoR; consumer state is stale/pending |
| Tool call succeeded | Only command transport succeeded; authoritative write still requires domain outcome |

No integration failure may be reported as a successful business operation. Recovery requires idempotency, authoritative reread, reconciliation or an explicit `unknown/pending` outcome.

## 12. Provider Boundary

`formula_tela` is a **pilot provider application / provider integration boundary**. It is not the global Ayla operational System of Record.

The architecture MUST NOT create two independent truths such as:

```text
Formula Tela Appointment
Ayla Appointment
```

For the pilot, provider-specific state may remain in the provider application, but the Ayla-facing Appointment/Availability/Provider contracts must identify which system is authoritative for each fact. If a provider system remains authoritative for a provider-owned fact, Ayla stores an integration reference or normalized projection rather than inventing a competing lifecycle.

The mapping of provider-local appointment state to the Ayla Appointment Contract is `Open question` where the sources do not settle the direction of authority.

## 13. Data Privacy Boundary

A provider or master receives only a purpose-limited operational projection required for the current operational task.

Provider/master access MUST NOT include:

- semantic memory;
- AI hypotheses or inferred signals;
- data belonging to other providers;
- hidden recommendation reasons or internal ranking factors;
- complete memory or conversation context;
- unnecessary PII;
- consent records beyond the minimum authorization result required for the operation.

Purpose-limited projections inherit the source domain's privacy and retention rules. They do not become provider-owned memory, a new source of truth or a permission to write the source state.

## 14. Owner Decisions

| ID | Decision | Status |
|---|---|---|
| OD-RRM-1 | `beautygo_backend` is the operational transactional SoR for the Ayla business states covered by Appointment, Availability, Provider/Specialist and Payment contracts. This does not mean the repository owns every related domain or every provider-local fact. | `Proposed` |
| OD-RRM-2 | `ai-bot-platform` owns conversation runtime and orchestration runtime, but not Appointment, Availability, Payment, Consent or Provider state. | `Proposed` |
| OD-RRM-3 | `ayla-ai-core` has no direct access to domain storage; it receives approved context and uses public contracts/tools. | `Proposed` |
| OD-RRM-4 | `formula_tela` is a provider integration/pilot application and is not the Ayla operational SoR. | `Proposed` |
| OD-RRM-5 | Mobile App, MAX Mini App and MAX Bot are product/channel surfaces and do not own Ayla business state. | `Proposed` |
| OD-RRM-6 | Consent ownership is a domain responsibility separate from channel/runtime ownership; physical Consent Service placement remains pending. | `Proposed` |
| OD-RRM-7 | A domain event is published only by the owner of the committed fact; semantic event meaning is governed canonically, while producer wire details remain with the producer contract owner. | `Proposed` |

## 15. Open Questions

1. Кто является named owner и физическим SoR для Consent Records: отдельный Consent Service, `beautygo_backend` или иной компонент?
2. Какой точный provider boundary действует в Controlled Pilot: provider system как authoritative scheduler или `beautygo_backend` как normalized transactional SoR?
3. Где физически реализованы Mobile App, MAX Mini App и MAX Bot, и какой runtime является целевым после MAX legacy cutover?
4. Как соотносятся `Booking`, `Appointment` и provider-local visit state в следующем Appointment Contract?
5. Кто является named owner для Availability Domain и Payment/Billing Domain?
6. Какой event registry является wire-contract owner для producer payload: producer repository, `ayla-knowledge` или двухслойная модель semantic canon + producer schema?
7. Какой exact API/tool contract используется для command outcome `unknown`, reconciliation и idempotency?
8. Какие provider/master operational projections разрешены для каждого pilot operation и с какой freshness?
9. Какова окончательная retention/deletion orchestration для runtime conversation/delivery state?
10. Какой cutover criterion переводит MAX Bot из `formula_tela` legacy runtime в `ai-bot-platform`?

## 16. Source and Evidence Notes

Подтвержденные основания для этого документа:

- `Ayla Constitution` — normative product, privacy, safety, autonomy and provenance boundaries.
- `Ayla Domain Capability Registry` — distinction between capability, context and repository; repository boundary does not equal domain boundary.
- `Ayla Glossary` — canonical terminology.
- `Ayla Decision Log` — approved and pending cross-system/product decisions.
- `Ayla MVP Scope and Release Contract` — MVP channel and scope constraints.
- `Ayla Single-Provider Technical Pilot Execution Scope` — pilot/provider integration constraints.
- `Ayla Multi-Provider Product Validation Execution Scope` — multi-provider normalization and adapter boundary.
- `Ayla Domain Context Map` — context/SoR identification rules and implementation mapping discipline.
- `Ayla Core Domain Model Specification` — domain entities and invariants.
- `Ayla MVP Appointment Contract` — appointment lifecycle authority and contract dependency.
- `Ayla Domain Event Registry` — event ownership/registration boundary.
- `Consent Scope Registry` — purpose-limited access, fail-closed behavior and consent enforcement boundaries.
- `Data Inventory Matrix` — source-of-truth, physical custodian, permitted consumers, write authority and projection rules.

The existence of a module, table, API route or legacy implementation is evidence of physical implementation only. It is not by itself evidence of domain ownership.

## 17. Change Control

Изменение этого документа, которое затрагивает SoR, domain ownership, public contract, event ownership, privacy boundary или write authority, является cross-repository architectural change и требует:

1. owner decision или ADR;
2. impact analysis;
3. списка затронутых consumers;
4. migration/compatibility plan;
5. обновления зависимых контрактов;
6. conformance/validation evidence.

Мелкие редакторские исправления не должны менять смысл ownership или write authority.

## Change Log

| Version | Date | Change |
|---|---|---|
| 1.0-draft | 2026-08-14 | Replaced previous mixed draft with explicit domain/repository/implementation/runtime responsibility model; added channel inventory, write authority, contract, event, projection, failure, provider and privacy boundaries. |