---
node_id: ayla.ux.master-app-information-architecture
title: Ayla Master App Information Architecture
type: specification
status: draft
canonical_status: candidate
version: "0.1"
owner: UX Architecture
owners:
  - UX Architecture
  - Product Operations
knowledge_area: design
system_owner:
  - ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: medium
data_categories:
  - pii
security_sensitivity: medium
ai_indexing: allowed
export_policy: sanitized
domain: booking
updated: 2026-08-17
review_cycle: monthly
depends_on:
  - "[[Ayla Master System and Recovery UX Contract]]"
  - "[[Ayla Knowledge Area Taxonomy]]"
  - "[[Ayla Repository Responsibility Matrix]]"
  - "[[Ayla Constitution]]"
  - "[[Ayla Glossary]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Ayla Decision Log]]"
  - "[[Ayla MVP Appointment Contract]]"
  - "[[Ayla Domain Event Registry]]"
  - "[[Ayla Domain Context Map]]"
  - "[[Ayla Core Domain Model Specification]]"
  - "[[Ayla Salon Operations MVP Contract]]"
  - "[[Ayla Master Operations Screen Contract]]"
---

# Ayla Master App Information Architecture

> Канонический связующий контракт между Product Operations и отдельными Screen
> Contracts мобильного приложения мастера.

Документ определяет структуру приложения, карту экранов, ответственность,
навигацию, projection flow и зависимости между экранными контрактами. Он не
является UI-дизайном, набором макетов, React Native-описанием, API-документом
или технической реализацией.

## 1. Purpose

Information Architecture нужна, чтобы определить приложение мастера до создания
отдельных экранов и не допустить набора несвязанных Screen Contracts.

Она решает следующие проблемы:

- неясно, где находится рабочий центр мастера;
- одна и та же операционная ответственность повторяется на нескольких экранах;
- экран пытается одновременно быть календарём, CRM, админ-панелью и AI-ассистентом;
- navigation flow начинает определять бизнес-логику;
- Screen Contracts создаются без общей модели capabilities, projections и boundaries;
- MVP и deferred-функции смешиваются в одной поверхности.

Приложение проектируется в следующем порядке:

```text
Master Goals
  -> Operational Capabilities
  -> Information Architecture
  -> Screen Responsibilities
  -> Screen Contracts
  -> UI Implementation
```

Экран не является владельцем бизнес-логики:

```text
Screen State != Domain State
Projection != Source of Truth
```

Нумерация и физическое расположение будущих документов не означают миграцию
существующих UX MVP-файлов. Handoff-документы не являются canonical dependencies
этого IA-контракта.

## 2. Master App Product Context

### 2.1 Primary User

**Primary User:** Master.

Мастер использует приложение в рамках своего authorized tenant/provider scope.
Приложение поддерживает service delivery и операционную работу, но не заменяет
Salon Operations, Appointment Domain или административное управление бизнесом.

### 2.2 Master Goals

Мастер должен иметь возможность:

- видеть рабочий день;
- понимать следующую рабочую задачу;
- работать с разрешённым контекстом конкретного клиента;
- выполнять услугу;
- фиксировать результат через разрешённую команду;
- получать помощь Ayla в пределах доступной projection.

### 2.3 Product Context Boundaries

Приложение мастера — operational surface для service delivery. Оно не является:

- полным CRM;
- системой управления салоном;
- источником истины для Appointment, Availability, Consent или Payment;
- интерфейсом доступа к semantic memory;
- заменой администратора при конфликте, переназначении или policy decision.

## 3. Master App Capability Map

| Capability area | Operational problem | App responsibility | Canonical owner / source |
| --- | --- | --- | --- |
| `Daily Operations` | Мастеру нужно понимать текущий рабочий день | Собрать разрешённый day context, next appointment, tasks и exceptions | `Ayla Salon Operations MVP Contract`; `Master Operations Screen Contract` |
| `Appointment Management` | Нужно работать с конкретной записью | Показать appointment context и передать разрешённые commands | `Ayla MVP Appointment Contract` |
| `Customer Context` | Нужно подготовиться к услуге без лишнего раскрытия данных | Показать minimum necessary operational context | `Consent Scope Registry`; `Data Inventory Matrix`; Appointment projection |
| `Schedule Awareness` | Изменения расписания влияют на рабочий день | Показать schedule projection, freshness и изменения; инициировать разрешённые write intents, routed to canonical commands | Schedule/Operational Projection; `Ayla Master Schedule UX Contract` |
| `Ayla Assistant` | Мастеру нужна объяснимая помощь | Объяснить разрешённый контекст и подготовить следующий шаг | Repository Responsibility Matrix; Master Operations Screen Contract |
| `Profile and Settings` | Нужны личные настройки и управление доступом | Отдельная future surface, не смешанная с service delivery | Product Operations / Governance decision pending |

Capability Map не создаёт новых CAP-ID, ownership или permission rules.

## 4. Screen Map

### 4.1 Proposed Logical Screen Set

| Screen Name | Purpose | Primary User Goal | Responsible Capability | Input Data | Output / Actions | Related Screens | Not Responsible For |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Operations Home` | Рабочий центр текущего дня | Понять, что происходит сейчас и что делать дальше | Daily Operations | `Master Day Projection`, Today Summary, exceptions, task projection | Open appointment, refresh, report exception, access assistant | Appointment Detail, Schedule View, Notifications | Domain rules, catalog, users, full CRM |
| `Appointment Detail` | Контекст и действия по одной записи | Подготовиться к визиту и выполнить разрешённый outcome flow | Appointment Management / Service Delivery | `Appointment Operational Projection`, permitted Customer Context | View, complete, no-show or request change only when authorized | Operations Home, Customer Context | Appointment ownership, direct editing, policy decisions |
| `Customer Context` | Purpose-limited context клиента | Получить минимум информации для текущей услуги | Customer Context | `Customer Operational Context Projection` | Read context, add authorized operational note if capability exists | Appointment Detail, Operations Home | Semantic memory, full history, medical inference |
| `Schedule View` | Планирование и availability management | Проверить и управлять day/week schedule where scope permits | Schedule Awareness | Schedule Projection, appointment projections | Read, refresh, navigate to appointment, initiate permitted write intents routed to canonical commands | Operations Home, Appointment Detail | Creating policy, assigning masters, directly rewriting availability/domain state |
| `Notifications` | Транзакционные и operational updates | Понять изменения, требующие внимания | Notifications / Operations | Notification projection derived from approved events | Open related context, mark read if policy allows | Operations Home, Appointment Detail | Becoming a second event source or chat inbox by default |
| `Profile / Settings` | Личные настройки и session/access controls | Управлять собственными настройками | Profile and Settings | Authorized profile/settings projection | Change permitted personal settings | Operations Home | Customer data, salon administration, domain state |

### 4.2 IA Decision

`Operations Home` является рабочим центром приложения. `Appointment Detail`
является точкой работы с конкретной записью. `Customer Context` пока
определён как отдельная logical responsibility; будет ли он самостоятельным
экраном или sub-surface Appointment Detail, остаётся Open Question.

`Schedule View` является утверждённой P0-поверхностью (planning + availability
management) и входит в глобальную навигацию `Today | Schedule | Ayla`.
`Notifications` и `Profile / Settings` не являются обязательными P0 destinations;
они не должны автоматически появляться как обязательные tabs или navigation
destinations без подтверждения capabilities, owner и release scope.

## 5. Screen Responsibility Boundaries

### 5.1 Operations Home

Делает:

- показывает рабочий день;
- показывает ближайшие записи;
- показывает operational exceptions и разрешённые tasks;
- направляет мастера к следующему допустимому действию.

Не делает:

- не изменяет доменные правила;
- не управляет услугами, каталогом или пользователями;
- не редактирует Appointment напрямую;
- не становится CRM или admin dashboard.

### 5.2 Appointment Detail

Делает:

- показывает authoritative appointment projection через разрешённый read model;
- показывает service/customer context в пределах purpose и role;
- запускает authorized command flow;
- отражает result event только после authoritative update.

Не делает:

- не владеет Appointment lifecycle;
- не создаёт новые event names;
- не принимает решения о permissions, ownership или reassignment;
- не показывает скрытую AI memory.

### 5.3 Customer Context

Делает:

- показывает только minimum necessary customer context для текущей услуги;
- отделяет operational notes от semantic memory;
- применяет authorization, consent и purpose limitation.

Не делает:

- не является full customer profile;
- не показывает данные других клиентов/providers;
- не показывает AI inference, medical conclusions или полный conversation history;
- не становится владельцем customer data.

### 5.4 Schedule View

Делает:

- показывает schedule projection (planning + availability management) в
  разрешённом scope;
- инициирует разрешённые write intents (booking, Time Off, availability),
  которые направляются в canonical authoritative commands.

Не делает:

- не является domain source of truth и не изменяет domain state напрямую;
- не создаёт policy, не назначает мастеров, не разрешает конфликты и не
  переписывает Appointment state вне canonical commands.

### 5.5 Notifications and Profile / Settings

`Notifications` только доставляет/показывает derived operational updates.
`Profile / Settings` только управляет разрешёнными личными настройками. Ни один
из этих экранов не создаёт второй источник истины для domain events или user state.

## 6. Navigation Model

### 6.1 Entry

```text
Application open
  -> authorization and projection freshness check
  -> Operations Home
```

Если projection недоступна, приложение остаётся в `Offline`, `Loading` или
`Exception` state и не подменяет отсутствие данных пустым рабочим днём.

### 6.2 Before Appointment

```text
Operations Home
  -> Appointment Detail
  -> Customer Context (if separately authorized/available)
  -> return to Appointment Detail
  -> Operations Home
```

### 6.3 Service Completion and Post-Visit Resolution

```text
Operations Home
  -> Appointment Detail
  -> authoritative scheduled_end
  -> 3-hour post-visit resolution window
  -> no lifecycle exception before deadline
  -> authoritative normal completion/readback
  -> updated projection
  -> Operations Home refresh
```

### 6.4 Problem and Change Flow

```text
Any operational screen
  -> Operational Exceptions
  -> refresh / retry / authorized Request Change / admin escalation
  -> updated projection or explicit unresolved state
  -> Operations Home
```

Navigation does not decide whether `Request Change` is a command, proposal or
admin workflow. That meaning must come from the responsible canonical contract.

The normal visit path is zero-action after scheduled_end; Appointment Detail does not require a manual completion ceremony. Exception actions remain subject to the Appointment Contract and canonical authority/evidence rules.

## 7. MVP Screen Scope

| Screen | Purpose | MVP Status | Priority | Dependencies |
| --- | --- | --- | --- | --- |
| `Operations Home` | Daily operational work center | Included in MVP | P0 | Master Operations Screen Contract; Master Day Projection; appointment/schedule sources |
| `Appointment Detail` | Work with one appointment | Included in MVP; P0 UX frozen for implementation | P0 | Appointment Contract; Domain Event Registry; Operations Contract |
| `Customer Context` | Purpose-limited customer context | Proposed / scope decision required | P1 | Consent Scope Registry; Data Inventory Matrix; Appointment Detail |
| `Schedule View` | Planning + availability management | Included in MVP (approved P0 surface) | P0 | Schedule Projection; availability/permission policy; Master Schedule UX Contract |
| `Notifications` | Operational notification inbox | Deferred | P1 | Notification projection and event consumer policy |
| `Profile / Settings` | Personal settings/access controls | Future | P2 | Profile/settings capability and governance decision |

MVP inclusion means a capability is supported by approved scope and owner
contracts. It does not imply that every listed action is already implemented.

## 8. Data Flow Between Screens

| Screen | Required Projection | Domain Source | Events Affecting Update |
| --- | --- | --- | --- |
| Operations Home | `Master Day Projection`, Today Summary, Exception Projection | Appointment Domain + Schedule/Operational Projection | `appointment.created`, `appointment.confirmed`, `appointment.completed`, `appointment.cancelled`, `appointment.rescheduled`, and other registered events according to Domain Event Registry |
| Appointment Detail | `Appointment Operational Projection` | Appointment Domain | Registered `appointment.*` events relevant to the record; exact status checked in registry |
| Customer Context | `Customer Operational Context Projection` | Authorized customer/appointment sources | Approved operational note or consent/authorization updates; no AI hypothesis event |
| Schedule View | Schedule Projection | Schedule/Availability owner | Registered availability/schedule integration events, when defined |
| Notifications | Notification Projection | Event consumers / notification system | Derived notification events; notification is not a substitute for domain fact |
| Profile / Settings | Profile/Settings Projection | Authorized profile/settings owner | Approved settings or authorization events, when defined |

Projection updates never make the consuming screen a Source of Truth. Each event
name, semantic status, producer and consumer must be verified in
`Ayla Domain Event Registry`.

## 9. Ayla AI Placement

### 9.1 Placement Decision

The primary Ayla Assistant surface is an approved standalone global
conversational surface and P0 destination, reachable through the global
navigation `Today | Schedule | Ayla`, with additional contextual entries from
`Operations Home` and `Appointment Detail`. It is not a separate operational
authority.

The standalone placement is approved; it is not an Open Question. Contextual
entries keep AI adjacent to the current operational projection while preserving
screen responsibility boundaries, and do not replace the standalone surface.

### 9.2 Ayla CAN

Ayla can:

- explain the permitted operational context;
- remind the master about an appointment based on authoritative projection;
- explain a service using approved information;
- prepare information for the next step;
- propose or prepare an action for explicit user confirmation.

### 9.3 Ayla CANNOT

Ayla cannot:

- change domain state without an authorized command;
- complete a service instead of the master;
- make decisions for the master, administrator or domain owner;
- create or confirm business facts from inference;
- make medical conclusions;
- show hidden memory, unauthorized PII or data outside role/purpose scope.

`AI suggestion != Business action`.

## 10. Privacy Boundary

| Actor | Accessible in Master App context | Excluded from this IA surface |
| --- | --- | --- |
| Master | Own operational day, permitted appointment data, minimum customer context and authorized operational notes | Semantic memory, hidden inference, other clients/providers, unnecessary history and full conversations |
| Customer | Own customer-facing appointment/communication projections through customer surfaces | Master operational projections, internal notes, other customers and provider operations |
| Administrator | Authorized operational projections and exception context in assigned scope | Data outside role/purpose/consent scope and hidden AI hypotheses |
| Ayla | Only the projection and context explicitly passed through an authorized boundary | Direct write authority, semantic memory without approval, unauthorized PII and unapproved sensitive data |

Access follows `Consent Scope Registry`, `Data Inventory Matrix`, role
authorization and purpose limitation. Missing or uncertain scope is handled
fail-closed.

## 11. Relationship With Screen Contracts

The document hierarchy is:

```text
Information Architecture
  -> Screen Contracts
  -> UI Design / Implementation
```

Information Architecture owns application structure and screen responsibility.
Screen Contracts own the data, states, actions and boundaries of one screen.
UI Design translates an accepted Screen Contract into interaction and visual
decisions. None of these layers owns domain state.

Canonical Screen Contracts:

- `07 UX/Ayla Master Operations Screen Contract.md` — existing;
- `07 UX/Ayla Appointment Detail Screen Contract.md` — existing; P0 UX frozen for implementation;
- `07 UX/Ayla Customer Context Screen Contract.md` — future if separate screen is approved;
- `07 UX/Ayla Master Schedule UX Contract.md` — existing; Schedule View is an approved P0 surface.

Handoff documents may inform historical context but are not dependencies or
sources of truth for this IA contract.

## 12. Open Questions

| ID | Question | Status |
| --- | --- | --- |
| IA-MASTER-OQ-01 | Нужен ли отдельный календарь мастера или достаточно day projection на Operations Home? | Resolved: Schedule View — approved P0 surface (planning + availability management); see `Ayla Master Schedule UX Contract` |
| IA-MASTER-OQ-02 | Нужен ли отдельный экран клиента или Customer Context должен оставаться частью Appointment Detail? | Owner decision required |
| IA-MASTER-OQ-03 | Где должен размещаться Ayla Assistant: внутри Operations Home, в Appointment Detail или отдельной surface? | Resolved: standalone Ayla — approved global conversational surface (P0 destination); contextual entries from Home/Detail remain |
| IA-MASTER-OQ-04 | Нужен ли отдельный inbox уведомлений? | Deferred; capability and event-consumer decision required |
| IA-MASTER-OQ-05 | Какие экраны обязательны для MVP? | Resolved: Operations Home (Today), Schedule и Ayla — P0; Customers/Profile/Create/More не являются обязательными P0 destinations |
| IA-MASTER-OQ-06 | Какие действия доступны мастеру без администратора? | Role policy / Appointment Contract owner decision required |
| IA-MASTER-OQ-07 | Является ли `Request Change` command, proposal или admin workflow? | Open; no decision created here |
| IA-MASTER-OQ-08 | Разрешён ли `MarkNoShow` мастеру и какие evidence требуются? | Open; follow Appointment/Event contracts |

Open Question не является разрешением на реализацию. До решения владельца
соответствующая capability должна быть deferred, ограничена read-only или
направлена в admin escalation.

## 13. Validation Checklist

### Architecture

- [x] Domain boundaries и Appointment ownership не изменены.
- [x] Ни один screen не объявлен Source of Truth.
- [x] Projection используется как read model, а не как domain state.
- [x] Events берутся из `Ayla Domain Event Registry`; новые события не созданы.
- [x] Handoff-документы не включены в `depends_on`.

### Product

- [x] Screen Map выведена из Master operating model и capabilities.
- [x] Каждый экран имеет одну основную ответственность.
- [x] MVP, Deferred и Future scope разделены.
- [x] Рабочий центр, appointment context, customer context, schedule и settings разделены по responsibility.

### UX

- [x] Описана navigation model для открытия, подготовки, завершения и исключений.
- [x] Data flow между screens связан с projections и canonical sources.
- [x] Existing Master Operations Screen Contract сохранён и использован как dependency.
- [x] UI mockups, component details и API specifications не создавались.

### AI

- [x] AI не получил WRITE authority.
- [x] `AI suggestion != Business action` зафиксировано.
- [x] AI ограничен переданным разрешённым context.

### Privacy

- [x] Разделены доступы Master, Customer, Administrator и Ayla.
- [x] Использованы `Consent Scope Registry` и `Data Inventory Matrix`.
- [x] Semantic memory, hidden inference и unauthorized PII исключены.


## 13A. Shared System and Recovery UX

All Master surfaces use the shared [[Ayla Master System and Recovery UX Contract]] for system/recovery presentation. This does not add a destination: global navigation remains Today | Schedule | Ayla, while contextual Manual Booking remains an action.

## 14. Source and Non-Override Rule

Canonical dependency chain:

```text
Repository Responsibility Matrix
  -> Appointment Contract
  -> Domain Event Registry
  -> Salon Operations MVP Contract
  -> Master Operations Screen Contract
  -> Master App Information Architecture
```

Foundation, domain context, core model, privacy — release documents provide
constraints and context. Этот документ не переопределяет их ownership,
permissions, event semantics, data access rules или AI boundary.

При конфликте вопрос передаётся владельцу соответствующей области и фиксируется
через governance decision. Существующие документы и папки не перемещаются,
не переименовываются и не изменяются.
