---
node_id: ayla.foundation.repository-responsibility-matrix
title: Ayla Repository Responsibility Matrix
type: architecture-specification
status: draft
decision_status: proposed
version: "0.1"
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
updated: 2026-07-25
review_cycle: quarterly
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla]]"
  - "[[Ayla Knowledge Architecture Specification]]"
supersedes: []
superseded_by: []
---

# Ayla Repository Responsibility Matrix

## 1. Статус документа

**Статус документа:** Draft  
**Статус решения:** Proposed — требует утверждения владельцем продукта и архитектурными владельцами репозиториев.

Документ становится каноническим после:

- утверждения владельцем продукта;
- проверки фактических границ всех пяти репозиториев;
- устранения открытых вопросов, перечисленных в разделе 16;
- внесения ссылок на локальные архитектурные документы;
- прохождения проверки метаданных `ayla-knowledge`.

После утверждения документ используется как обязательная основа для:

- создания новых модулей;
- выбора репозитория для нового кода;
- размещения документации;
- определения источника истины;
- создания cross-repository contracts;
- согласования breaking changes;
- миграции legacy-компонентов;
- настройки mirrors в `ayla-knowledge`.

---

## 2. Назначение документа

Экосистема Ayla разделена между пятью репозиториями:

```text
ayla-knowledge
beautygo_backend
ai-bot-platform
ayla-ai-core
formula_tela
```

Без формального распределения ответственности возникают следующие риски:

- один бизнес-процесс реализуется сразу в нескольких репозиториях;
- разные репозитории считают себя System of Record;
- API и event contracts меняются несинхронно;
- prompts и safety rules расходятся между consumers;
- одна и та же AI-логика копируется в разные приложения;
- legacy-код продолжает развиваться параллельно новой платформе;
- документация противоречит фактическому коду;
- невозможно определить владельца ошибки или архитектурного решения.

Документ устанавливает:

1. роль каждого репозитория;
2. области исключительного владения;
3. области совместного владения;
4. допустимые зависимости;
5. место хранения канонических документов;
6. порядок разрешения конфликтов;
7. правила переноса функциональности между репозиториями.

---

## 3. Основные термины

### 3.1. Repository owner

Репозиторий, отвечающий за реализацию, тестирование, выпуск и поддержку конкретного компонента или контракта.

### 3.2. System of Record — SoR

Система, в которой находится каноническое текущее состояние бизнес-сущности.

Пример:

```text
Appointment хранится в beautygo_backend.
```

Следовательно, бот не должен поддерживать независимую каноническую копию записи.

### 3.3. Normative canon

Утверждённое описание того:

- что означает сущность;
- какие правила она обязана соблюдать;
- какие ограничения действуют во всей системе;
- какое решение имеет приоритет при конфликте.

Normative canon хранится преимущественно в `ayla-knowledge`.

### 3.4. Implementation contract

Точный технический контракт конкретной реализации:

- Python API;
- HTTP API;
- event payload;
- модель базы данных;
- tool schema;
- deployment procedure;
- migration;
- feature flag.

Implementation contract хранится в репозитории, который владеет реализацией.

### 3.5. Mirror

Автоматически синхронизируемая read-only копия документа из owning repository в `ayla-knowledge`.

Mirror не становится новым источником истины.

### 3.6. Consumer

Репозиторий или приложение, использующее API, библиотеку, событие или данные другого репозитория.

### 3.7. Legacy source

Существующая реализация, используемая как источник поведения, данных или миграционного знания, но не получающая новую общеплатформенную ответственность.

---

## 4. Архитектурный принцип разделения

Высокоуровневая модель экосистемы:

```text
ayla-knowledge
определяет смысл, продуктовые правила и общесистемные ограничения

beautygo_backend
хранит бизнес-факты и выполняет транзакции

ai-bot-platform
управляет каналами, разговорами и AI-сценариями

ayla-ai-core
предоставляет общий исполняемый AI-механизм

formula_tela
обслуживает сайт салона и сохраняет legacy-наработки
```

В сокращённом виде:

```text
Knowledge → Meaning and policy
Backend   → Facts and transactions
Platform  → Runtime and channels
Core      → Shared AI mechanics
Formula   → Local product and legacy
```

---

## 5. Реестр репозиториев

### 5.1. `ayla-knowledge`

#### Роль

Центральный нормативный и навигационный knowledge hub Ayla.

#### Владеет

- Конституцией Ayla;
- Product Thesis;
- общесистемной терминологией;
- Product Strategy;
- User Journeys;
- общими domain definitions;
- cross-system architecture;
- repository responsibility;
- data ownership;
- safety policy;
- privacy policy;
- consent policy;
- business rules;
- общими metrics;
- Decision Log;
- ADR Index;
- governance;
- documentation coverage;
- knowledge lifecycle;
- mirrors implementation-документов.

#### Не владеет

- production-кодом;
- точными Django models;
- HTTP handlers;
- runtime prompts конкретного deployment;
- Python signatures библиотеки;
- инфраструктурой приложений;
- database migrations;
- локальными runbooks конкретного сервиса.

#### Критерий размещения

Документ относится в `ayla-knowledge`, когда он отвечает на вопрос:

> Что должно быть истинно и обязательно для всей системы Ayla?

---

### 5.2. `beautygo_backend`

#### Роль

Главный transactional backend и System of Record для бизнес-данных Ayla.

#### Владеет

- пользователями;
- PII;
- профилями;
- specialists/providers;
- tenant relationships;
- каталогом услуг;
- Service Templates;
- Salon Services;
- Specialist Services;
- расписанием;
- availability;
- external busy intervals;
- appointments;
- состояниями appointments;
- payments;
- refunds;
- reviews;
- durable personal context;
- provenance пользовательских фактов;
- consent enforcement на стороне данных;
- внутренними REST API;
- публичными REST API;
- OpenAPI backend-контрактом;
- transactional outbox;
- producer-стороной domain events;
- YClients intake;
- YClients calendar integration;
- YooKassa integration;
- backend safety enforcement;
- backend operational runbooks.

#### Не владеет

- диалоговым состоянием AI-каналов;
- MAX/Telegram transport;
- prompt registry;
- AI skill routing;
- общим AI orchestration kernel;
- общей продуктовой стратегией;
- нормативной терминологией;
- legacy-сайтом салона.

#### Критерий размещения

Функциональность относится в `beautygo_backend`, когда она:

- изменяет бизнес-состояние;
- требует транзакционной целостности;
- хранит долгоживущие факты;
- требует database constraints;
- определяет availability;
- управляет деньгами;
- является каноническим состоянием пользователя, исполнителя или appointment.

---

### 5.3. `ai-bot-platform`

#### Роль

Conversation, channel and AI application runtime платформы Ayla.

#### Владеет

- webhook ingress каналов;
- MAX adapter;
- Telegram adapter;
- Web Chat transport;
- conversation state;
- session state;
- channel identity mapping;
- skills;
- scenario routing;
- runtime orchestration shell;
- tool implementations, обращающимися к внешним системам;
- интеграционными clients к `beautygo_backend`;
- retrieval пользовательского контекста;
- prompt registry;
- выбором runtime prompt version;
- model routing;
- AI provider runtime configuration;
- event consumers;
- deduplication входящих событий;
- replay infrastructure;
- experiments;
- shadow mode;
- canary mode;
- human handoff;
- runtime observability;
- bot analytics;
- delivery ответов пользователю.

#### Не владеет

- каноническими appointments;
- payments;
- каталогом как бизнес-источником;
- PII как System of Record;
- долгоживущими personal facts;
- общими AI primitives, нужными нескольким consumers;
- продуктовым определением Intent;
- нормативными safety rules;
- сайтом салона.

#### Критерий размещения

Функциональность относится в `ai-bot-platform`, когда она отвечает на вопрос:

> Как принять запрос из канала, собрать контекст, выполнить AI-сценарий и доставить результат?

---

### 5.4. `ayla-ai-core`

#### Роль

Общая исполняемая Python-библиотека AI-оркестрации для нескольких consumers.

#### Владеет

- `AIConcierge`;
- циклом model/tool orchestration;
- построением model messages;
- общими prompt composition primitives;
- `BrandVoiceConfig`;
- candidate context abstractions;
- `CandidateContext`;
- `SpecialistContext`;
- общими tool schemas;
- tool dispatch protocol;
- Dependency Injection interface для consumer tool dispatcher;
- provider adapter protocol;
- OpenAI adapter;
- Anthropic adapter;
- token budgeting;
- history truncation;
- tenant propagation внутри AI-вызова;
- tenant-aware library observability;
- deterministic replay helpers;
- memory block rendering;
- anti-injection guards;
- grounding guards;
- стабильным публичным Python API;
- package versioning;
- compatibility policy;
- release policy.

#### Не владеет

- HTTP;
- Django views;
- Django models;
- PostgreSQL;
- channel webhooks;
- session persistence;
- user identity resolution;
- tenant authorization через базу данных;
- booking transactions;
- payment processing;
- consent persistence;
- YClients;
- YooKassa;
- конкретными channel responses;
- deployment конкретного consumer.

#### Критерий размещения

Функциональность относится в `ayla-ai-core`, если одновременно выполняются условия:

1. она нужна более чем одному consumer;
2. она не зависит от конкретного transport;
3. она не зависит от конкретной базы данных;
4. она может быть выражена через Python abstractions;
5. она не определяет бизнес-состояние;
6. она может тестироваться как библиотека.

---

### 5.5. `formula_tela`

#### Роль

Продуктовый репозиторий салона «Формула тела», сайт и источник legacy AI-реализации.

#### Владеет

- публичным сайтом салона;
- SEO;
- маркетинговыми страницами;
- локальным каталогом отображения сайта;
- salon-specific content;
- формами и локальными заявками;
- локальными интеграциями сайта;
- салонными operational workflows;
- legacy MAX bot до завершения cutover;
- legacy MCP;
- миграционными исходниками;
- historical implementation evidence.

#### Не владеет

- общеплатформенным AI runtime;
- shared AI orchestration;
- канонической моделью marketplace;
- booking SoR Ayla;
- общими product definitions;
- новой cross-product функциональностью;
- общими tool schemas после их переноса;
- новым persistent memory pipeline.

#### Критерий размещения

Функциональность остаётся в `formula_tela`, если она:

- относится только к сайту или бизнесу салона;
- не нужна платформе Ayla;
- является legacy-компонентом до миграции;
- служит источником поведения для extraction;
- должна быть выведена из эксплуатации после cutover.

---

## 6. Матрица владения верхнего уровня

Условные обозначения:

- **O** — Owner;
- **C** — Consumer;
- **N** — Normative canon;
- **M** — Mirror;
- **L** — Legacy source;
- **—** — не участвует.

| Область | `ayla-knowledge` | `beautygo_backend` | `ai-bot-platform` | `ayla-ai-core` | `formula_tela` |
|---|---:|---:|---:|---:|---:|
| Product mission | N/O | C | C | C | C |
| Product strategy | N/O | C | C | C | C |
| Repository governance | N/O | C | C | C | C |
| Identity | N | O | C | — | L |
| PII | N | O | C через API | — | локально |
| Tenant relationships | N | O | C | tenant context only | L |
| Provider profiles | N | O | C | context abstraction | L |
| Canonical Service Catalog | N | O | C/M | context abstraction | L |
| Availability | N | O | C | — | L |
| Appointments | N | O | C | — | L |
| Payments | N | O | C | — | локально |
| Reviews | N | O | C | — | локально |
| Durable personal context | N | O | C/retrieval | rendering | L |
| Conversation state | N | — | O | stateless processing | L |
| Channel adapters | N | — | O | — | L |
| Skills | N | — | O | shared primitives only | L |
| AI orchestration | N | C | O application shell | O kernel | L |
| Prompt policy | N/O | C | runtime owner | composition owner | L |
| Prompt registry | N | — | O | C | — |
| Brand voice | N | config consumer | config consumer | abstraction owner | legacy config |
| Tool schemas | N | business endpoints | runtime selection | shared protocol | legacy |
| Tool implementation | N | business operations | O для AI tools | dispatcher interface | legacy |
| Model adapters | N | — | runtime config | O | L |
| Model routing | N | — | O | adapter support | — |
| Event producer | N | O | C | — | — |
| Event consumer | N | producer client | O | — | — |
| Runtime replay | N | event/outbox evidence | O | deterministic helpers | — |
| Safety policy | N/O | enforcement | enforcement | guards | legacy |
| Consent policy | N/O | durable enforcement | runtime enforcement | context constraints | legacy |
| Website/SEO | N | — | — | — | O |
| Legacy MAX bot | N | — | target runtime | extracted kernel | L/O до cutover |
| Knowledge mirrors | O | source | source | source | source |

---

## 7. Детальная матрица систем истины

### 7.1. Бизнес-данные

| Сущность | System of Record | Разрешённые копии |
|---|---|---|
| User | `beautygo_backend` | channel identity mapping |
| User PII | `beautygo_backend` | минимизированный runtime context |
| Tenant | `beautygo_backend` | bot runtime mirror |
| TenantUserRelationship | `beautygo_backend` | derived access cache |
| SpecialistProfile | `beautygo_backend` | discovery/runtime mirror |
| ServiceTemplate | `beautygo_backend` | search/recommendation mirror |
| SalonService | `beautygo_backend` | bot catalog mirror |
| SpecialistService | `beautygo_backend` | bot booking mirror |
| Availability | `beautygo_backend` | short-lived cache |
| ExternalBusyInterval | `beautygo_backend` | без независимого SoR |
| Appointment | `beautygo_backend` | bot projection |
| Payment | `beautygo_backend` | read-only status projection |
| Review | `beautygo_backend` | search projection |
| Durable memory fact | `beautygo_backend` | runtime retrieval cache |
| Conversation | `ai-bot-platform` | analytics projection |
| Channel message delivery state | `ai-bot-platform` | provider-side delivery ID |
| Prompt version assignment | `ai-bot-platform` | experiment logs |
| AI library version | package/release в `ayla-ai-core` | pins в consumers |

### 7.2. Документы

| Тип документа | Каноническое место |
|---|---|
| Product policy | `ayla-knowledge` |
| Cross-product domain semantics | `ayla-knowledge` |
| Cross-system architecture | `ayla-knowledge` |
| HTTP API contract | owning service |
| Python API contract | `ayla-ai-core` |
| Event payload producer contract | `beautygo_backend` |
| Event consumption mapping | `ai-bot-platform` |
| Shared event semantics | `ayla-knowledge` |
| Database model invariants | `beautygo_backend` |
| Prompt composition API | `ayla-ai-core` |
| Prompt deployment registry | `ai-bot-platform` |
| Channel protocol | `ai-bot-platform` |
| Site/SEO implementation | `formula_tela` |
| Migration plan | target owning repository |
| Operational runbook | репозиторий, где выполняется операция |
| Legacy evidence | `formula_tela` или `90 Sources` |

---

## 8. Разрешённые направления зависимостей

### 8.1. Основной dependency graph

```text
ayla-knowledge
не является runtime dependency

formula_tela ───────────────┐
                            ▼
                      ayla-ai-core
                            ▲
                            │
beautygo_backend ───────────┼──────── ai-bot-platform
       ▲                    │                │
       └──── REST/events ───┴────────────────┘
```

Более точно:

```text
beautygo_backend
  imports ayla-ai-core только для локального AI consumer, пока он существует

ai-bot-platform
  imports ayla-ai-core
  calls beautygo_backend via internal API
  consumes beautygo_backend events

formula_tela
  imports ayla-ai-core для legacy runtime до cutover

ayla-ai-core
  не импортирует consumer repositories

ayla-knowledge
  не импортируется production-кодом как runtime package
```

### 8.2. Запрещённые зависимости

Запрещаются следующие направления:

```text
ayla-ai-core → beautygo_backend
ayla-ai-core → ai-bot-platform
ayla-ai-core → formula_tela
```

Также запрещается:

- импортировать Django models в `ayla-ai-core`;
- обращаться к базе данных из `ayla-ai-core`;
- выполнять HTTP-запросы к Ayla backend из общего AI core;
- хранить booking state в `ai-bot-platform`;
- дублировать payment state machine в боте;
- помещать channel adapter в `ayla-ai-core`;
- переносить общеплатформенную AI-логику обратно в `formula_tela`;
- использовать `ayla-knowledge` как runtime configuration database без отдельного утверждённого механизма экспорта.

---

## 9. Правила совместного владения

Некоторые области нельзя назначить только одному репозиторию. Для них ответственность разделяется по слоям.

### 9.1. Prompts

| Слой | Владелец |
|---|---|
| Product principles | `ayla-knowledge` |
| Safety requirements | `ayla-knowledge` |
| Shared prompt composition | `ayla-ai-core` |
| Brand voice abstraction | `ayla-ai-core` |
| Brand voice values | consumer |
| Runtime prompt version | `ai-bot-platform` |
| Experiment assignment | `ai-bot-platform` |
| Channel-specific instructions | consumer |
| Business data injected into prompt | owning data service через consumer |

### 9.2. Tools

| Слой | Владелец |
|---|---|
| Product meaning of tool | `ayla-knowledge` |
| Shared tool-call protocol | `ayla-ai-core` |
| Runtime tool registration | `ai-bot-platform` |
| Tool implementation | consumer |
| Business transaction | `beautygo_backend` |
| Authorization | owning service |
| Tool execution audit | `ai-bot-platform` и backend |
| Legacy tool | `formula_tela` до миграции |

### 9.3. Memory

| Слой | Владелец |
|---|---|
| Memory semantics | `ayla-knowledge` |
| Consent policy | `ayla-knowledge` |
| Durable facts | `beautygo_backend` |
| Fact provenance | `beautygo_backend` |
| Runtime retrieval | `ai-bot-platform` |
| Session memory | `ai-bot-platform` |
| Rendering into prompt | `ayla-ai-core` |
| Confidence-aware wording | `ayla-ai-core` |
| Data access enforcement | backend + platform |
| Final safety filtering | core + consumer |

### 9.4. Safety

| Слой | Владелец |
|---|---|
| Normative safety boundary | `ayla-knowledge` |
| Data validation | `beautygo_backend` |
| Runtime scenario gate | `ai-bot-platform` |
| Prompt/injection guards | `ayla-ai-core` |
| Channel presentation | `ai-bot-platform` |
| Legacy enforcement | `formula_tela` до cutover |

---

## 10. Изменения и breaking changes

### 10.1. Локальное изменение

Изменение считается локальным, если оно:

- не меняет публичный контракт;
- не влияет на другой репозиторий;
- не меняет продуктовый инвариант;
- не требует синхронного consumer update.

Такое изменение утверждается владельцем owning repository.

### 10.2. Cross-repository change

Изменение считается cross-repository, если оно затрагивает:

- internal REST API;
- event schema;
- публичный API `ayla-ai-core`;
- tool schema;
- prompt contract;
- memory contract;
- tenant propagation;
- identifier semantics;
- status taxonomy;
- authentication;
- authorization;
- shared configuration.

Такое изменение требует:

1. owner proposal;
2. impact analysis;
3. списка affected consumers;
4. migration strategy;
5. compatibility window;
6. conformance tests;
7. синхронного или поэтапного обновления consumers;
8. записи в Decision Log или ADR;
9. обновления mirrors после слияния.

### 10.3. Изменение `ayla-ai-core`

Breaking change библиотеки не может выпускаться только по решению разработчика библиотеки.

Требуются:

- проверка всех активных consumers;
- Consumer Matrix;
- Migration Guide;
- обновление pins;
- consumer compatibility checks в CI;
- Release Notes;
- rollback target.

---

## 11. Правило размещения новой функциональности

Перед созданием новой функции необходимо пройти следующий выбор.

### Шаг 1. Функция меняет каноническое бизнес-состояние?

Да → `beautygo_backend`.

Примеры:

- создать appointment;
- отменить appointment;
- изменить payment;
- сохранить факт пользователя;
- изменить availability специалиста.

### Шаг 2. Функция относится к каналу, сессии или сценарию?

Да → `ai-bot-platform`.

Примеры:

- принять MAX webhook;
- сохранить conversation state;
- выбрать skill;
- повторить tool call;
- переключить human handoff.

### Шаг 3. Функция является общей AI-механикой для нескольких consumers?

Да → `ayla-ai-core`.

Примеры:

- собрать messages;
- сократить history;
- адаптировать provider response;
- отрендерить memory block;
- выполнить общий tool loop.

### Шаг 4. Функция относится только к сайту салона?

Да → `formula_tela`.

### Шаг 5. Это правило, определение или решение всей экосистемы?

Да → `ayla-knowledge`.

---

## 12. Правила документации

Каждый implementation repository должен иметь локальный MOC или Documentation Index.

Минимальный набор:

```text
README.md
docs/README.md или DOCUMENTATION_INDEX.md
docs/architecture/
docs/contracts/
docs/runbooks/
docs/adr/ при наличии локальных ADR
```

Каждый значимый документ должен указывать:

- authority;
- owner;
- lifecycle;
- статус реализации;
- связанные contracts;
- `supersedes`;
- `superseded_by`;
- canonical source;
- affected repositories.

В `ayla-knowledge` импортируются только allowlisted документы.

Запрещается:

- зеркалировать весь `docs/**` без классификации;
- вручную редактировать generated mirrors;
- считать mirror новым canon;
- переносить PR description без нормализации;
- канонизировать исторический план как действующую архитектуру.

---

## 13. Правила legacy и миграции

`formula_tela/mysite/maxbot` остаётся legacy source до завершения cutover.

Для каждого legacy-компонента должен быть определён один статус:

```text
active-legacy
frozen
shadowed
migration-source
deprecated
decommissioned
archived
```

Новая общеплатформенная функциональность не создаётся в legacy runtime.

Допустимые изменения legacy-кода:

- критическое исправление production;
- security fix;
- migration instrumentation;
- compatibility adapter;
- cutover support;
- data export;
- observability, необходимая для сравнения.

После успешного cutover:

- channel runtime переходит в `ai-bot-platform`;
- shared AI logic находится в `ayla-ai-core`;
- business transactions остаются в `beautygo_backend`;
- legacy implementation архивируется;
- historical evidence сохраняется.

---

## 14. Разрешение конфликтов

При конфликте решений применяется следующий приоритет:

1. Ayla Constitution;
2. утверждённый Decision Log;
3. утверждённая cross-system policy;
4. принятый ADR;
5. утверждённая domain specification;
6. implementation contract owning repository;
7. код и conformance tests;
8. рабочие планы и PR descriptions;
9. legacy implementation;
10. historical sources.

Если код противоречит утверждённому нормативному документу:

- код не становится автоматически новым canon;
- создаётся discrepancy;
- определяется, ошибочен код или устарел документ;
- решение фиксируется явно;
- изменения выполняются синхронно.

---

## 15. Владение конфликтами

| Тип конфликта | Финальный владелец решения |
|---|---|
| Product meaning | Product Owner |
| Repository boundary | Platform Architecture |
| Data ownership | Backend Architecture + Privacy |
| AI Core boundary | AI Architecture |
| Safety rule | Safety/Privacy + Product Owner |
| Payment behavior | Backend/Payments Owner |
| Booking invariant | Booking Domain Owner |
| Prompt behavior | AI Architecture при соблюдении canon |
| Tool schema | AI Architecture + owning transaction service |
| Channel UX | Conversation Product Owner |
| Legacy migration | Migration Owner + target owner |
| Legal compliance | Legal/Privacy ruling |

---

## 16. Открытые решения владельца

Для утверждения версии `1.0` необходимо закрыть следующие вопросы.

### OD-R1. Веточная модель `beautygo_backend`

Необходимо зафиксировать фактическую модель:

```text
dev = integration branch
master = production/default branch
```

или утвердить другую модель.

Также необходимо решить, какую ветку использует mirror pipeline.

**Рекомендация:** рабочие mirrors — с `dev`; утверждённые release mirrors — с immutable tag или commit SHA.

### OD-R2. Статус AI внутри `beautygo_backend`

Необходимо определить:

- остаётся ли backend долгосрочным consumer `ayla-ai-core`;
- переезжает ли весь conversational AI в `ai-bot-platform`;
- сохраняет ли backend только ограниченные внутренние AI-функции.

**Рекомендация:** conversational runtime переносится в `ai-bot-platform`; backend использует core только для backend-owned offline/internal AI use cases.

### OD-R3. Tool schemas

Необходимо определить, кто утверждает shared tool schema при различиях между consumers.

**Рекомендация:**

- общий protocol — `ayla-ai-core`;
- business meaning — `ayla-knowledge`;
- concrete runtime schemas — `ai-bot-platform`;
- transaction contract — `beautygo_backend`.

### OD-R4. Prompt canon

Необходимо определить, какие prompt-тексты являются:

- нормативными;
- библиотечными;
- runtime;
- experimental;
- channel-specific.

**Рекомендация:** использовать четырёхслойную модель из раздела 9.1.

### OD-R5. `formula_tela` после cutover

Необходимо утвердить, остаются ли в репозитории:

- только сайт и SEO;
- salon-local integrations;
- MCP;
- какие-либо AI-функции.

**Рекомендация:** AI runtime удаляется или архивируется; сайт и локальный бизнес остаются.

### OD-R6. Владелец `ayla-ai-core`

Необходимо назначить:

- Code Owner;
- Release Owner;
- API Compatibility Owner;
- Security Reviewer;
- Consumer Representatives.

### OD-R7. Canonical event contract

Необходимо выбрать модель владения event contract:

- единый contract в `ayla-knowledge`;
- единый contract в implementation repository;
- разделение semantic canon и wire contract.

**Рекомендация:**

- event semantics — `ayla-knowledge`;
- точный producer wire contract — `beautygo_backend`;
- consumer mapping — `ai-bot-platform`.

---

## 17. Критерии утверждения

Документ может получить статус `approved`, когда:

- утверждены роли всех пяти репозиториев;
- закрыты OD-R1–OD-R7;
- назначены owners;
- создана Data Ownership Matrix;
- создана AI Component Ownership Matrix;
- добавлены ссылки на локальные MOC;
- проверены реальные зависимости;
- установлен процесс cross-repository breaking changes;
- обновлён `sources-manifest.yaml`;
- документ проходит knowledge validation.

---

## 18. Предлагаемое решение

Предлагается утвердить следующую базовую формулировку:

> `ayla-knowledge` владеет нормативным знанием и общесистемными правилами.  
> `beautygo_backend` владеет каноническими бизнес-данными и транзакциями.  
> `ai-bot-platform` владеет каналами, разговорами и исполнением AI-сценариев.  
> `ayla-ai-core` владеет общей переиспользуемой AI-механикой и публичным Python API.  
> `formula_tela` владеет сайтом салона и остаётся legacy/migration source для вынесенных компонентов.
