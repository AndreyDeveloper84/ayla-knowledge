---
node_id: ayla.governance.data-inventory-matrix
title: Data Inventory Matrix
type: data-inventory-matrix
status: draft
version: "0.1"
owner: Product Architecture
priority: P0
knowledge_area:
  - safety-governance
domain:
  - user-context
  - consent
  - wellness
  - memory
concerns:
  - privacy
  - safety
  - governance
  - data-ownership
system_owner:
  - ayla-user-context
  - ayla-consent
  - ayla-wellness
source_repository: ayla-knowledge
created: 2026-07-24
updated: 2026-07-24
source_kind: canonical
classification: internal
data_sensitivity: high
data_categories:
  - user-profile
  - consent
  - wellness
  - semantic-memory
security_sensitivity: high
ai_indexing: allowed
export_policy: restricted
tags:
  - ayla
  - ayla/governance
  - ayla/data-inventory
  - type/data-inventory-matrix
  - priority/p0
implements:
  - "[[Ayla Constitution]]"
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Glossary]]"
  - "[[ADR-0012 Dynamic User Model]]"
related:
  - "[[Ayla Knowledge Architecture Specification]]"
  - "[[Ayla Domain and Metadata Registry]]"
review_cycle: event-driven
---

# Data Inventory Matrix

## Назначение

Этот документ фиксирует единый словарь владения данными для всех классов пользовательских данных в Ayla. Он является источником истины для:

- нормативного domain ownership;
- физического custodian;
- source of truth для каждого класса данных;
- разрешённых consumers и write authority;
- consent/purpose требований;
- retention и deletion orchestrator;
- правил временных projections.

Этот документ не определяет API, модели данных или runtime-поведение. Он фиксирует policy-границы, которые должны соблюдаться всеми implementation documents.

## Модель владения

### Термины

| Термин | Определение |
|---|---|
| **Data subject** | Пользователь (end user) — физическое лицо, которому принадлежат персональные данные. |
| **Normative domain owner** | Нормативный владелец домена — bounded context, определяющий семантику и policy для класса данных. |
| **Physical custodian** | Технический хранитель — система, которая физически хранит и оперирует данными в runtime. |
| **Source of truth** | Источник истины — система или домен, который авторизован создавать и обновлять данные этого класса. |
| **Authorized consumers** | Разрешённые потребители — системы или компоненты, которые могут читать данные этого класса. |
| **Write authority** | Право записи — кто может создавать, обновлять или удалять данные этого класса. |
| **Consent / Purpose** | Требования к согласию и целям обработки для этого класса данных. |
| **Retention & deletion orchestrator** | Система, ответственная за orchestration retention и deletion lifecycle. |
| **Temporary projections** | Временные производные представления — read-only проекции для конкретных use case, не создающие параллельного хранения. |

### Принципы

1. **Один владелец на класс данных.** Каждый класс данных имеет ровно один нормативный domain owner.
2. **Custodian ≠ Owner.** Технический хранитель (W3 / Memory & Identity) не становится владельцем данных только потому, что хранит их.
3. **W2 — владелец профиля и operational preferences, но не semantic memory.** W2 User/Profile Domain владеет account/profile и operational preferences, но не параллельной semantic memory.
4. **Wellness Domain — источник истины для raw wellness events.** Сырые wellness-события остаются в Wellness Domain.
5. **Consent Domain — источник истины для согласий.** Все согласия управляются через Consent Domain.
6. **Получатели temporary projections — только consumers без прав владения или прямой записи.** Projections не создают параллельного хранения.
7. **Semantic memory — отдельный класс данных с собственным lifecycle.** Память не привязана к master_id, не передаётся при offboarding и не удаляется автоматически.

## Матрица классов данных

| Класс данных | Data subject | Normative domain owner | Physical custodian | Source of truth | Authorized consumers | Write authority | Consent / Purpose | Retention & deletion orchestrator | Temporary projections rules |
|---|---|---|---|---|---|---|---|---|---|
| **Account / Profile** | User | W2 User/Profile Domain | W2 Identity System | W2 Identity System | W3 Memory, Wellness, Consent, Notification | W2 Identity System only | Account creation TOS; profile update requires user action | W2 Identity System (account closure) | Profile fields may be projected to memory only via explicit memory proposal gate; no automatic sync |
| **Operational Preferences** (notification, language, timezone) | User | W2 Notification Preferences Domain | W2 Preferences API | W2 Preferences API | W3 Memory (read-only for context), Notification Service | W2 Preferences API only | Implied by account usage; opt-out via preferences UI | W2 Preferences API (account closure) | Preferences may inform memory context but cannot be stored as MemoryEntry without separate proposal |
| **Consent Records** | User | W2 Consent/Communication Preferences Domain | W2 Consent API | W2 Consent API | W3 Memory (for consent state checks), Wellness, Booking | W2 Consent API only | Explicit consent required per purpose; withdrawable at any time | W2 Consent API (consent withdrawal or account closure) | Consent state may be projected for gating decisions; no persistent copy outside Consent Domain |
| **Semantic Memory** (MemoryEntry, verified facts, learned patterns) | User | W3 Memory & Identity Domain | W3 Memory Service | W3 Memory Service (via memory proposal gate) | W2 Profile (read-only for display), Wellness (read-only for correlation), Booking (purpose-limited) | W3 Memory Service only (via proposal/consent/purpose gate) | Requires explicit consent per memory category; purpose-limited | W3 Privacy Flow (user-initiated privacy request only) | No parallel copies; projections must be ephemeral and purpose-bound |
| **Raw Wellness History** (sleep events, activity logs, measurements) | User | Wellness Domain | Wellness Data Store | Wellness Data Store | W3 Memory (for derived patterns), Dashboards, Analytics | Wellness Data Store only (user input or device sync) | Wellness TOS; separate consent for memory derivation | Wellness Domain (user deletion request or retention expiry) | Raw history never equals memory; only aggregated/derived patterns may enter memory via gate |
| **Wellness-Derived Memory** (patterns, insights, personalization from wellness data) | User | W3 Memory & Identity Domain | W3 Memory Service | W3 Memory Service (via memory gate) | Dashboards, Analytics, Coaching | W3 Memory Service only (via wellness-to-memory proposal gate) | Requires separate consent for wellness-to-memory derivation; purpose-limited to wellness personalization | W3 Privacy Flow (user-initiated privacy request only) | Derived memory is independent of raw wellness retention; deletion does not cascade to raw history |
| **Purpose-Limited Projections** (booking-specific views, substitute access, dashboard summaries) | User | N/A (projection, not owned class) | Consumer-specific | Source class (memory, wellness, profile) | Specific consumer only (e.g., substitute, master, dashboard) | None (read-only projection) | Inherited from source class; additional purpose limitation applies | N/A (ephemeral; no independent retention) | Must be ephemeral; no persistence beyond session or specific booking lifecycle; no copying or export |

## Детализация по классам

### Account / Profile

**Описание:** Базовая учётная запись пользователя, профильные поля (имя, контактные данные, идентификаторы).

**Границы:**
- W2 Identity System является единственным источником истины.
- W3 может читать профиль для обогащения контекста памяти, но не может изменять его.
- Профильные поля не становятся памятью автоматически. Создание MemoryEntry из профиля требует отдельного memory proposal gate.

**Запрещено:**
- Синхронизация профиля в память без явного proposal gate.
- Использование профиля как параллельного хранилища semantic memory.

### Operational Preferences

**Описание:** Настройки уведомлений, язык, часовой пояс, другие операционные предпочтения.

**Границы:**
- W2 Notification Preferences Domain владеет этими данными.
- W3 может читать preferences для контекста, но не хранит их как MemoryEntry.
- Preferences API не является хранилищем semantic memory.

**Запрещено:**
- Обход memory proposal, consent и purpose gates через Preferences API.
- Хранение operational preferences в W3 как независимой памяти.

### Consent Records

**Описание:** Записи о согласиях пользователя на обработку данных, отзыв согласий.

**Границы:**
- Consent Domain является единственным источником истины для всех согласий.
- W3 проверяет состояние согласий для gating решений, но не хранит независимые копии.
- Отзыв согласия немедленно влияет на все dependent systems через event propagation.

**Запрещено:**
- Кэширование consent state за пределами Consent Domain без TTL и invalidation.
- Принятие решений о памяти без проверки актуального consent state.

### Semantic Memory

**Описание:** Верифицированные факты о пользователе, выученные паттерны, персонализированные выводы.

**Границы:**
- W3 Memory & Identity является техническим custodian semantic memory.
- Создание MemoryEntry возможно только через W3 proposal/consent/purpose gate.
- Память не привязана к master_id; она принадлежит data subject (пользователю).

**Запрещено:**
- Привязка памяти к master_id или staff-профилю.
- Передача, копирование или изменение памяти мастером (substitute).
- Автоматическое создание памяти из conversations, internal chat или raw events без gate.
- Удаление памяти при offboarding мастера; удаление только через user privacy request.

### Raw Wellness History

**Описание:** Сырые измерения wellness (сон, активность, физиологические показатели).

**Границы:**
- Wellness Domain является источником истины для raw events.
- Raw history остаётся в Wellness Domain независимо от памяти.
- Dashboards и API views являются производными projections.

**Запрещено:**
- Формулировка «sleep data is Ayla's memory» или аналогичные.
- Прямое преобразование raw events в память без memory gate.

### Wellness-Derived Memory

**Описание:** Паттерны, инсайты и персонализация, выведенные из raw wellness data.

**Границы:**
-Derived memory становится semantic memory только после прохождения memory gate.
- W3 является custodian derived memory.
- Deletion derived memory не каскадируется на raw wellness history.

**Запрещено:**
- Модель «Wellness Profile целиком равен Ayla Memory».
- Игнорирование separate consent requirement для wellness-to-memory derivation.

### Purpose-Limited Projections

**Описание:** Временные представления данных для конкретных use case (booking, substitute access, dashboards).

**Границы:**
- Projections не являются самостоятельным классом данных с владельцем.
- Projection наследует consent/purpose от source class.
- Projection должна быть ephemeral (сессия, booking lifecycle).

**Запрещено:**
- Персистентное хранение projections за пределами session/booking.
- Экспорт или копирование projections вне approved consumer.
- Использование projection как обхода memory gating.

## Связь с другими документами

| Документ | Связь |
|---|---|
| [[ADR-0012 Dynamic User Model]] | ADR-0012 определяет proposed архитектурную модель; эта матрица фиксирует конкретные классы данных и ownership. |
| [[Ayla Constitution]] | Конституция определяет фундаментальные права пользователя; эта матрица реализует их для конкретных классов данных. |
| [[Ayla Glossary]] | Глоссарий определяет терминологию; эта матрица использует её для consistency. |
| AMD-020 Pilot Scope Registry | AMD-020 должен быть обновлён для отражения ownership из этой матрицы (после завершения текущего AMD-020-батча). |
| ayla-memory-and-personalization.md (ai-bot-platform) | Этот документ является implementation policy, который должен ссылаться на данную матрицу. |
| core-wellness-profile.md (ai-bot-platform) | Должен разделять raw wellness records и derived memory согласно этой матрице. |

## Проверка соответствия

Перед публикацией любого handoff- или policy-документа необходимо проверить отсутствие следующих запрещённых утверждений:

- ❌ «memory attached to master_id»
- ❌ «raw sleep history equals memory»
- ❌ «W2 owns all UserPersonalContext»
- ❌ «offboarding transfers or deletes memory»
- ❌ «conversations/internal chat automatically produce memory»
- ❌ «Wellness Profile целиком равен Ayla Memory»
- ❌ «Preferences API является хранилищем semantic memory»

## Change Log

### v0.1 — 2026-07-24

- Первоначальная версия Data Inventory Matrix.
- Зафиксированы 7 классов данных: Account/Profile, Operational Preferences, Consent Records, Semantic Memory, Raw Wellness History, Wellness-Derived Memory, Purpose-Limited Projections.
- Определены нормативные владельцы, custodians, sources of truth, authorized consumers, write authority, consent/purpose, retention/deletion orchestrator, projection rules.
- Добавлены запреты на распространённые анти-паттерны владения памятью.

## Approval

**Status:** Draft — Pending Review

**Owner:** Product Architecture

**Review required from:**
- User Context Domain
- Privacy and Safety
- Wellness Domain Owner
- Consent Domain Owner

**Approval date:** __________________

**Decision reference:** __________________
