---
node_id: ayla.strategy.mvp-documentation-roadmap
title: Ayla MVP Documentation Roadmap
type: specification
status: approved
decision_status: accepted
version: "1.1"
owner: Founder / Product Architecture
priority: P0
knowledge_area:
  - strategy
system_owner:
  - ayla-knowledge
source_repository: ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
created: 2026-07-27
updated: 2026-07-28
review_cycle: monthly
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Decision Log]]"
related:
  - "[[Ayla MVP Product Thesis]]"
  - "[[Killer PRD]]"
  - "[[Ayla Domain Capability Registry]]"
---

# Ayla MVP Documentation Roadmap

Нормативный статус зафиксирован записью AYLA-DEC-0014 в [[Ayla Decision Log]].

Роадмап документов Ayla к максимально быстрому MVP

Главный принцип: документация должна уменьшать неопределённость разработки, а не становиться отдельным проектом.

Для запуска MVP не нужно сначала канонизировать всю будущую экосистему Ayla. Нужно зафиксировать только те решения, без которых разработчики:

реализуют один бизнес-процесс по-разному;
создадут несовместимые модели данных;
нарушат privacy или safety;
не смогут интегрировать AI, backend и канал;
не смогут проверить, что MVP действительно работает.
1. Целевая цепочка документов
Constitution
    ↓
Product Vision
    ↓
MVP Product Thesis
    ↓
Killer PRD
    ↓
MVP Scope and Release Contract
    ↓
MVP User Journey
    ↓
Intent Model
    ↓
Domain Capability Registry
    ↓
MVP Context Map
    ↓
Core Domain Model
    ↓
MVP Architecture
    ↓
API / Event / Tool Contracts
    ↓
Data / Consent / Safety Contracts
    ↓
Delivery Roadmap and Backlog
    ↓
Release Readiness

При этом документы не обязательно делать строго последовательно. После фиксации MVP scope несколько потоков можно вести параллельно.

Phase 0. Зафиксировать фундамент и прекратить расширение scope
0.1. Ayla Constitution

Статус: уже существует.

Документ фиксирует ограничения, которые нельзя нарушать ради ускорения разработки:

пользователь контролирует персональный контекст;
AI не является источником истины;
inference отделяется от fact;
recommendation отделяется от action;
sensitive data обрабатываются по правилам;
экономические интересы не должны скрыто искажать organic recommendation;
критические решения должны быть прослеживаемы.
Для MVP нужно проверить

Не требуется переписывать документ. Нужно только убедиться, что в нём нет открытых положений, блокирующих MVP.

Результат
Constitution usable for MVP: yes/no
Blocking constitutional questions: list
0.2. Ayla Decision Log

Статус: существует, включает DEC-0011 и DEC-0012.

До начала следующей волны разработки Decision Log должен содержать решения по:

порядку канонизации документов;
владельцу capability registry;
единой классификации;
MVP scope Payment;
границе AI core и consumers;
владельцам public contracts;
breaking changes между репозиториями.
Правило

Не создавать новый большой документ, когда достаточно короткой записи в Decision Log.

Phase 1. Заморозить продуктовый MVP

Это самая приоритетная стадия. До неё нельзя уверенно проектировать архитектуру.

1.1. Ayla Product Vision

Статус: существует.

Для MVP из документа нужно извлечь
для кого запускается продукт;
какую проблему решает;
чем отличается от каталога и обычного чат-бота;
какой долгосрочный scope не входит в первую версию.
Не делать сейчас
не расширять Vision новыми вертикалями;
не детализировать будущую международную платформу;
не описывать весь продукт на несколько лет.
1.2. Ayla MVP Product Thesis

Приоритет: P0.

Документ должен уместиться примерно в 5–10 страниц и однозначно ответить:

Целевая аудитория MVP

Например:

существующие клиенты салона;
новые пользователи beauty/wellness;
самостоятельные специалисты;
один пилотный салон;
конкретный город или ограниченная территория.
Главная проблема

Что именно пользователь не может удобно сделать без Ayla.

Главное обещание

Например:

Ayla понимает запрос пользователя, учитывает разрешённый контекст, предлагает один понятный следующий шаг и помогает выполнить его.

Основной сценарий

Для максимально быстрого MVP лучше выбрать один end-to-end сценарий, а остальные оставить как совместимые, но не обязательные.

Рекомендуемый сквозной сценарий:

Пользователь выражает потребность
→ Ayla уточняет intent
→ подбирает услугу или действие
→ объясняет рекомендацию
→ пользователь подтверждает
→ Ayla создаёт запись
→ пользователь получает подтверждение
Out of scope

Обязательно перечислить:

полноценные платежи;
сложную программу лояльности;
весь marketplace;
автоматические медицинские выводы;
продвинутые ML-модели;
автономные действия без подтверждения;
несколько стран;
сложную multi-tenant тарификацию;
полноценное outcome learning, если оно не требуется для пилота.
Exit criteria

Документ должен определить, при каких условиях MVP считается проверенным.

1.3. Killer PRD

Статус: существует.

Его не надо расширять до описания всей платформы.

Для MVP оставить
killer moment;
trigger-сценарии;
primary recommendation;
alternatives;
recommendation_id;
qualified action;
direct и assisted attribution;
economic neutrality;
consent requirements;
safety ограничения;
основные продуктовые метрики.
Для MVP отложить
сложные модели обучения;
долгосрочные cohort mechanics;
расширенные автоматические сценарии;
глубокую оптимизацию ranking;
сложную monetization attribution.
1.4. MVP Scope and Release Contract

Приоритет: P0.
Новый обязательный документ.

Это должен быть главный документ против разрастания проекта.

Структура
# Ayla MVP Scope and Release Contract

## 1. MVP Goal
## 2. Target Users
## 3. Primary End-to-End Scenario
## 4. Included Capabilities
## 5. Deferred Capabilities
## 6. Required Integrations
## 7. Required Channels
## 8. Non-Functional Minimum
## 9. Release Metrics
## 10. Release Blockers
## 11. Change Control
Included capabilities

Для первого релиза я бы ограничил обязательный набор:

Conversation Experience.
Intent Understanding.
Consent Management — минимальный scope.
Personal Context — ограниченный набор фактов.
Service Catalog.
Provider Management — минимальный профиль.
Availability.
Recommendation Formation.
Explanation.
Appointment Management.
Notification.
Attribution — минимальный direct linkage.
Audit — только критические события.
Deferred capabilities
Payment Processing;
полноценный Billing;
advanced Outcome Learning;
сложная Experimentation Platform;
расширенный Marketplace Search;
cross-product tenant customization;
глубокая provider verification;
автоматическая обработка health outcomes.
Критическое правило

После approval любое расширение Included Scope требует owner decision с указанием:

зачем оно нужно до MVP;
какой срок добавляет;
какую текущую задачу вытесняет.
Phase 2. Зафиксировать пользовательский поток
2.1. MVP User Journey Specification

Приоритет: P0.

Не нужно описывать все будущие journeys. Нужна только сквозная цепочка MVP.

Обязательные этапы
1. Entry
2. First interaction
3. Consent request
4. Intent detection
5. Clarification
6. Context retrieval
7. Recommendation
8. Explanation
9. User confirmation
10. Availability selection
11. Booking creation
12. Booking confirmation
13. Notification
14. Outcome or feedback prompt

Для каждого шага:

actor;
trigger;
пользовательская цель;
системное действие;
отображаемое состояние;
ошибка;
fallback;
analytics event;
owning capability.
Ключевые негативные сценарии

Обязательно описать:

Ayla не поняла запрос;
отсутствует consent;
нет подходящей услуги;
нет свободных слотов;
специалист недоступен;
запись не подтверждена;
tool или LLM недоступен;
рекомендация заблокирована safety gate;
пользователь отказывается от предложения.
2.2. MVP UX State Contract

Приоритет: P1.

Это не полный UI-kit. Это перечень обязательных продуктовых состояний:

loading;
clarification required;
recommendation ready;
no recommendation;
consent required;
slot unavailable;
booking pending;
booking confirmed;
booking failed;
retry;
human handoff.

Документ не должен описывать пиксели. Его задача — не дать frontend и backend по-разному трактовать состояния.

Phase 3. Зафиксировать смысл AI
3.1. Ayla Intent Model Specification

Приоритет: P0.
Критический predecessor по DEC-0011.

Без этого документа нельзя корректно завершить Context Map и стабильный AI contract.

Для MVP определить
поддерживаемые intent types;
required и optional slots;
confidence levels;
clarification rules;
multi-intent handling;
correction;
supersession;
expiry;
unsupported intent;
safety-sensitive intent;
контракт результата intent resolution.
Минимальный набор intent types

Не надо сразу описывать сотни намерений.

Например:

DISCOVER_SERVICE
FIND_SPECIALIST
BOOK_APPOINTMENT
RESCHEDULE_APPOINTMENT
CANCEL_APPOINTMENT
ASK_ABOUT_SERVICE
ASK_ABOUT_PRICE
ASK_ABOUT_AVAILABILITY
PROVIDE_CONTEXT
CORRECT_CONTEXT
REVOKE_CONSENT
UNKNOWN
Обязательный output contract
intent_id:
intent_type:
status:
confidence:
slots:
missing_required_slots:
evidence:
requires_clarification:
clarification_question:
safety_flags:
3.2. MVP Recommendation Contract

Приоритет: P0.

Это должен быть отдельный короткий документ, даже если Recommendation подробно будет описана позднее.

Определить
что является candidate;
обязательные gates;
ranking inputs;
primary recommendation;
alternatives;
explanation;
recommendation_id;
expiry;
invalidation;
accept/reject;
связь с booking;
economic-neutrality rule.
Минимальная последовательность
Intent resolved
→ consent checked
→ context selected
→ candidates collected
→ eligibility checked
→ safety checked
→ availability checked
→ ranked
→ primary composed
→ explanation generated
→ recommendation persisted
→ shown
Не детализировать сейчас
продвинутый ML ranking;
сложные коэффициенты;
полноценный experimentation framework;
долгосрочный personalization learning.
3.3. Prompt Canon and Runtime Prompt Assembly Boundary

Приоритет: P0 для AI-реализации.

Документ должен быть коротким — 3–6 страниц.

Зафиксировать

Knowledge владеет:

фундаментальными safety rules;
brand principles;
product policies;
canonical prompt fragments;
versioning и approval.

ayla-ai-core владеет:

reusable message construction;
prompt composition protocol;
token budgeting;
memory rendering interface;
grounding and injection guards;
provider abstraction.

consumer владеет:

channel-specific context;
tenant/product configuration;
доступными tools;
runtime facts;
delivery formatting.
Главный результат

Ни один consumer не должен собирать системный prompt по собственной неподконтрольной схеме.

3.4. MVP Memory Pipeline Contract

Приоритет: P0, если в MVP используется память.

Backend facts
→ consent/purpose filter
→ platform retrieval
→ core memory rendering
→ model context
→ trace reference
Зафиксировать
какие факты доступны;
кто их владелец;
как проверяется consent;
как выбирается relevant context;
что попадает в prompt;
provenance;
token limit;
redaction;
удаление и отзыв согласия;
запрет превращать transcript в authoritative fact.
Для быстрого MVP

Разрешить только небольшой whitelist персональных фактов. Например:

предпочтительный способ общения;
интересующие категории услуг;
предпочтение времени;
предыдущая подтверждённая услуга;
явно подтверждённые ограничения;
согласие на персонализацию.

> **AYLA-DEC-0023 (2026-07-28, accepted):** плоский whitelist этого
> раздела заменяется категориальной формой — категории со статусом
> allowed / requires dedicated consent / forbidden, наследованием
> политики полями и красной зоной default deny. Позиция «согласие на
> персонализацию» как персональный факт вытесняется: consent state —
> authorization metadata, не Context Fact (см. также AYLA-DEC-0024,
> MemoryEntry хранит только ссылку `consent_scope`). **Список выше —
> superseded, non-normative historical reference** и не является вторым
> нормативным источником; нормативна категориальная форма AYLA-DEC-0023
> (+ MemoryCategoryPolicy, AYLA-DEC-0024 п. 7). Редакционное приведение
> списка — pending.
> Именование событий §6.4 этого документа приводится к конвенции
> AYLA-DEC-0025 (dot-separated past-tense) при создании Domain Event
> Registry.

Phase 4. Завершить доменные границы только для MVP
4.1. Ayla Domain Capability Registry

Статус: draft v1.1.

Не нужно доводить все 27 записей до одинаковой глубины перед началом MVP.

Для MVP сделать две группы
MVP-active

Полностью проверить evidence и mapping для capabilities, включённых в Scope Contract.

Deferred

Оставить identified/deferred с кратким evidence.

Цель

Registry должен отвечать:

capability нужна MVP или нет;
какой у неё candidate context;
кто downstream consumer;
какой документ обязан определить детали.
4.2. Ayla MVP Domain Context Map

Приоритет: P0.

Не обязательно сразу канонизировать окончательную Context Map всей экосистемы.

Можно создать MVP-focused view внутри основной Context Map или отдельное приложение.

Для MVP достаточно подтвердить
Intent
Personal Context
Consent
Recommendation
Catalog
Provider
Availability
Appointment
Conversation/Application
Notification
Safety Policy
Для каждого контекста
purpose;
owned concepts;
SoR;
upstream/downstream;
published contracts;
repository owner;
MVP status;
deferred responsibilities.
Не нужно сейчас
идеально разделять все 27 capabilities;
проектировать будущие микросервисы;
выделять отдельный сервис на каждый context;
закрывать deferred Payment и advanced Learning.
4.3. Ayla Core Domain Model Specification

Приоритет: P0, но только MVP slice.**

Нужны модели
User;
Consent;
Context Fact;
Intent;
Service;
Provider/Specialist;
Service Offering;
Availability Slot;
Recommendation;
Appointment;
Attribution Link.
Для каждой
stable ID;
owner;
state;
lifecycle;
invariants;
commands;
events;
ссылки между моделями.
Не нужно

Полностью моделировать будущую платформу, биллинг, платежи, сложное обучение и multi-country compliance.

Phase 5. Сформировать архитектурный контракт MVP
5.1. Ayla MVP Architecture

Приоритет: P0.

Это должен быть практический документ для разработчиков.

Обязательные разделы
## 1. System Context
## 2. MVP Components
## 3. Repository Responsibilities
## 4. Runtime Request Flow
## 5. Data Ownership
## 6. Integration Boundaries
## 7. Synchronous Calls
## 8. Events and Background Jobs
## 9. Failure Handling
## 10. Security and Tenant Isolation
## 11. Deployment Topology
## 12. Deferred Architecture
Рекомендуемая MVP-композиция

Не начинать с большого набора микросервисов.

Client / MAX bot / mobile
        ↓
ai-bot-platform
        ↓
ayla-ai-core
        ↓
Backend API
        ↓
PostgreSQL
        +
Redis/Celery при необходимости

Backend может оставаться модульным монолитом.

ayla-ai-core — библиотека reusable AI logic.

ai-bot-platform — runtime/channel consumer.

5.2. Repository Responsibility Matrix

Приоритет: P0.

Responsibility	ayla-knowledge	ayla-ai-core	ai-bot-platform	backend	frontend
Canonical product rules	Owner	Read	Read	Read	Read
Prompt canon	Owner	Consume/assemble	Configure	—	—
Intent engine contract	Define	Implement reusable logic	Invoke	Provide facts	Present
Personal facts	Policy	Render abstraction	Retrieve/orchestrate	SoR	Manage UI
Recommendation	Define policy	Core algorithm	Orchestrate	Candidates/facts	Present
Appointment	Contract	Tool schema	Tool invocation	SoR	UI
Consent	Policy	Gate interface	Runtime check	SoR	Consent UX

Это снимет основные P0-пробелы между репозиториями.

5.3. Supported Consumer Matrix

Приоритет: P0.

Для ayla-ai-core:

Consumer	Supported version	Required features	Pin owner	Test suite
ai-bot-platform	...	orchestration, memory, tools	...	...
backend consumer	...	recommendation, replay	...	...
Обязательно определить
кто обновляет pin;
синхронное обновление двух consumers;
compatibility window;
deprecation period;
rollback;
release sequence.
5.4. Cross-Repository Change Policy

Приоритет: P0.

Короткий нормативный документ:

additive change;
backward-compatible change;
breaking change;
required ADR/Decision;
consumer impact review;
coordinated PR order;
test matrix;
release and rollback;
emergency exception.
Phase 6. Зафиксировать контракты реализации
6.1. Public API Registry

Приоритет: P0.

Для ayla-ai-core нужен один список публичного Python API.

Например:

AIConcierge
OrchestrationRequest
OrchestrationResult
IntentResult
RecommendationRequest
RecommendationResult
MemoryBlock
ToolDefinition
ToolDispatcher
ModelProvider
ReplayContext

Всё, что не включено в public API, считается internal.

6.2. Backend API Contract

Приоритет: P0.

Документировать только endpoints MVP:

current user;
consent;
context facts;
service search;
provider candidates;
availability;
appointment create;
appointment update/cancel;
recommendation persistence;
attribution;
feedback.

Лучше использовать OpenAPI как исполняемый контракт, а Markdown оставить для бизнес-семантики и ошибок.

6.3. Tool Schema Registry

Приоритет: P0.

Для каждого AI tool:

tool_name:
owner_context:
schema_owner:
side_effect:
idempotency:
authorization:
input_schema:
output_schema:
error_codes:
timeout:
retry_policy:
audit_events:

Минимальные tools:

search_services
find_providers
get_availability
create_appointment
reschedule_appointment
cancel_appointment
read_user_context
update_user_context
read_consent
6.4. Domain Event Registry

Приоритет: P1.

Только события MVP:

ConsentGranted;
ConsentRevoked;
IntentResolved;
RecommendationShown;
RecommendationAccepted;
AppointmentCreated;
AppointmentConfirmed;
AppointmentCancelled;
AppointmentCompleted;
QualifiedActionAttributed;
ContextFactCorrected.

Для каждого:

producer;
consumers;
schema;
version;
idempotency;
ordering;
retention;
PII classification.
6.5. Error and Reason Code Registry

Приоритет: P0.

Общий перечень стабильных кодов:

CONSENT_REQUIRED
INTENT_UNRESOLVED
NO_CANDIDATES
NO_AVAILABLE_SLOTS
PROVIDER_INELIGIBLE
APPOINTMENT_CONFLICT
APPOINTMENT_NOT_CONFIRMED
SAFETY_BLOCKED
TOOL_TIMEOUT
MODEL_UNAVAILABLE
CONTEXT_NOT_ALLOWED

Frontend, backend и AI platform не должны придумывать разные значения одной ошибки.

Phase 7. Privacy, safety и data minimum
7.1. MVP Consent Scope Registry

Приоритет: P0.

Для каждого scope:

identifier;
purpose;
data categories;
optional/required;
UI wording;
retention;
downstream uses;
revocation effect;
legal review status.

Минимальные scopes:

service_delivery
personalized_recommendations
persistent_context
transactional_notifications
product_analytics
7.2. MVP Data Classification and Retention Policy

Приоритет: P0.

Зафиксировать:

ordinary personal data;
sensitive self-care/health-adjacent data;
conversation data;
inferred data;
appointment data;
audit data;
analytics events.

Для каждой категории:

SoR;
retention;
deletion;
logging rules;
prompt eligibility;
analytics eligibility.
7.3. MVP Safety Policy

Приоритет: P0.

Не надо сразу писать универсальную энциклопедию безопасности.

Зафиксировать минимум:

запрещённые медицинские diagnosis/inference;
ситуации обязательного отказа;
unsafe service recommendations;
health-check triggers;
red flags;
human escalation;
допустимые формулировки;
mandatory deterministic gates;
разделение knowledge/core/consumer rules.
7.4. Threat Model Lite

Приоритет: P1, но до внешнего пилота.**

Проверить:

prompt injection;
tool abuse;
unauthorized appointment modification;
cross-tenant leakage;
replay attacks;
webhook spoofing;
PII in logs;
consent bypass;
model hallucination;
duplicate side effects.

Формат — компактная таблица:

Threat	Asset	Scenario	Prevention	Detection	Owner
Phase 8. Превратить документы в план разработки
8.1. MVP Delivery Roadmap

Приоритет: P0.

Разбить реализацию вертикальными срезами.

Slice 1 — базовый каталог и запись
Catalog
→ Provider
→ Availability
→ Appointment
Slice 2 — conversation и intent
Message
→ Intent
→ Clarification
→ Structured request
Slice 3 — recommendation
Intent
→ Candidates
→ Gates
→ Primary recommendation
→ Explanation
Slice 4 — consent и memory
Consent
→ Context facts
→ Retrieval
→ Memory block
Slice 5 — end-to-end AI booking
Conversation
→ Recommendation
→ User confirmation
→ Tool call
→ Appointment confirmation
Slice 6 — measurement and pilot
recommendation_id
→ qualified action
→ attribution
→ dashboard
→ feedback
8.2. MVP Backlog Decomposition Rules

Каждая задача должна иметь:

business_outcome:
owning_context:
source_document:
acceptance_criteria:
api_or_event_contract:
data_changes:
privacy_impact:
safety_impact:
tests:
out_of_scope:

Задача без owning context и acceptance criteria не должна уходить агенту.

8.3. Definition of Done

Для каждой функции:

contract implemented;
tests passed;
audit events added;
error states covered;
consent checked;
safety checked;
metrics emitted;
docs updated;
rollback possible.
Phase 9. Подготовка пилота и релиза
9.1. MVP Release Readiness Checklist

Приоритет: P0 перед пилотом.**

Product
primary journey работает end-to-end;
понятны ограничения;
нет критических тупиков;
recommendation объяснима;
fallback существует.
Data
seed catalog готов;
provider profiles проверены;
availability актуальна;
тестовые пользователи подготовлены.
AI
prompt versions закреплены;
tool schemas совместимы;
token budget установлен;
hallucination scenarios протестированы;
model/provider fallback определён.
Security
access control;
tenant isolation;
secrets;
logs;
rate limits;
audit;
backup.
Operations
monitoring;
alerts;
support process;
incident owner;
rollback;
feature flags.
9.2. Pilot Measurement Plan

Приоритет: P0.

Минимальные метрики:

доля resolved intents;
clarification rate;
recommendation shown rate;
recommendation acceptance rate;
booking conversion;
booking completion;
attributed qualified actions;
recommendation rejection reasons;
unsafe block rate;
tool failure rate;
median response time;
пользовательская оценка полезности.

Главная метрика MVP должна проверять не количество сообщений, а переход:

осмысленный запрос
→ полезная рекомендация
→ подтверждённое действие
9.3. Pilot Operations Runbook

Приоритет: P1.**

Зафиксировать:

кто следит за пилотом;
что делать при ошибке записи;
как отключить AI;
как перевести пользователя на человека;
как исправить каталог;
как отозвать ranking release;
как обрабатывать privacy request;
как расследовать safety incident;
как уведомлять пользователей о сбое.
Практический порядок выполнения
Волна 1 — блокирующие продуктовые документы
MVP Product Thesis.
MVP Scope and Release Contract.
Проверка Killer PRD на соответствие MVP.
MVP User Journey.
Intent Model Specification.

Результат: команда точно знает, что строит.

Волна 2 — блокирующие доменные документы
Обновление MVP-active записей Capability Registry.
MVP Context Boundary Review.
MVP Domain Context Map.
MVP Core Domain Model.
Consent Scope Registry.
MVP Safety Policy.

Результат: команда знает, кто чем владеет и какие правила нельзя нарушать.

Волна 3 — блокирующие технические контракты
MVP Architecture.
Repository Responsibility Matrix.
Prompt Canon / Runtime Assembly Boundary.
Memory Pipeline Contract.
Public API Registry.
Backend OpenAPI.
Tool Schema Registry.
Error and Reason Code Registry.
Cross-Repository Change Policy.
Supported Consumer Matrix.

Результат: разработчики могут работать параллельно без расхождения контрактов.

Волна 4 — доставка
MVP Delivery Roadmap.
Backlog с вертикальными slices.
Definition of Done.
Threat Model Lite.
Release Readiness Checklist.
Pilot Measurement Plan.
Operations Runbook.

Результат: продукт можно реализовать, выпустить и проверить на реальных пользователях.

Что не должно блокировать MVP

Следующие документы можно оставить draft или отложить:

полная Context Map всей будущей экосистемы;
детальная Payment Processing Specification;
расширенная Billing Specification;
полноценная Outcome Learning Specification;
advanced Experimentation Framework;
полный Event Catalog платформы;
multi-country legal model;
сложная monetization architecture;
отдельный микросервисный decomposition plan;
подробная data warehouse architecture;
масштабная ML training architecture;
универсальная multi-channel specification;
исчерпывающая taxonomy всех будущих услуг.
Минимальный комплект документов для старта разработки

Если резать максимально жёстко, достаточно следующих 12 артефактов:

Constitution.
Product Vision.
MVP Product Thesis.
Killer PRD.
MVP Scope and Release Contract.
MVP User Journey.
Intent Model Specification.
MVP Context Map.
MVP Core Domain Model.
MVP Architecture.
API + Tool Contracts.
Consent and Safety Contract.

Остальные документы можно дополнять параллельно с разработкой.

Рекомендуемая последовательность прямо сейчас

С учётом уже выполненной работы:

1. Обновить Root MOC
2. Зафиксировать текущий пакет отдельным коммитом
3. Завершить Ayla Intent Model Specification
4. Создать MVP Scope and Release Contract
5. Сжать User Journey до MVP end-to-end flow
6. Пометить MVP-active capabilities в Registry
7. Провести MVP Context Boundary Review
8. Завершить MVP Context Map
9. Сформировать MVP Core Domain Model slice
10. Написать MVP Architecture
11. Зафиксировать API, tool и repository contracts
12. Декомпозировать реализацию на вертикальные slices

Самый важный следующий документ — MVP Scope and Release Contract. Он должен стать жёсткой границей, которая не позволит архитектурной работе снова расшириться до всей будущей платформы.