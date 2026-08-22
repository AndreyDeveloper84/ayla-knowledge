---
node_id: ayla.product.salon-operations-mvp-contract
title: Ayla Salon Operations MVP Contract
type: specification
status: draft
decision_status: proposed
canonical_status: candidate
version: "0.1"
created: 2026-08-14
updated: 2026-08-17
owner: Product Owner
knowledge_area:
  - product
  - operations
domain:
  - booking
system_owner:
  - ayla-knowledge
source_repository: ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: medium
data_categories:
  - pii
security_sensitivity: medium
ai_indexing: allowed
export_policy: sanitized
review_cycle: monthly
tags: [product, salon-operations, mvp, appointment, operations]
depends_on:
  - "[[Ayla MVP Customer Resolution Contract]]"
  - "[[Ayla Master MVP Auth and Authority Contract]]"
related:
  - "[[Ayla Constitution]]"
  - "[[Ayla Repository Responsibility Matrix]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Ayla Glossary]]"
  - "[[Ayla Decision Log]]"
  - "[[Ayla MVP Appointment Contract]]"
  - "[[Ayla Domain Event Registry]]"
  - "[[Ayla Core Domain Model Specification]]"
  - "[[Ayla Domain Context Map]]"
  - "[[Ayla MVP User Journey Specification]]"
  - "[[Ayla MVP Scope and Release Contract]]"
  - "[[Ayla Single-Provider Technical Pilot Execution Scope]]"
  - "[[Ayla MVP Recommendation Contract]]"
  - "[[Consent Scope Registry]]"
  - "[[Data Inventory Matrix]]"
---

# Ayla Salon Operations MVP Contract

## 1. Purpose and position in the canon

Этот документ описывает ежедневную операционную модель салона, мастера,
администратора, владельца салона и клиента. Он отвечает на вопрос, **какая
операция должна быть поддержана и кто отвечает за её результат**.

Документ не является UX/UI-спецификацией, API-документацией, моделью экранов
или описанием технической реализации. Экран, бот или AI-диалог — только
интерфейс к уже определённой операции.

Порядок проектирования:

```text
Business Process
  -> Domain Capability
  -> Command
  -> Event
  -> Projection
  -> Screen requirement
```

Статус документа — `draft / proposed / canonical candidate`. Если источник не
подтверждает решение, оно помечено `Proposed`, `Pending owner decision` или
`Open question`.

## 2. Operating Model Overview

```text
Customer <-> Ayla <-> Salon Operations <-> Master
                         |
                  Service Delivery
```

| Участник | Цель | Нужные capabilities |
| --- | --- | --- |
| Customer | Найти подходящую услугу, выбрать исполнителя, получить и посетить запись | Discovery, availability read, appointment lifecycle, notifications, permitted follow-up |
| Ayla | Понять намерение, объяснить варианты, подготовить действие и показать разрешённый контекст | Intent understanding, recommendation, purpose-limited context, command preparation, explanation |
| Salon Operations | Поддерживать расписание, записи, клиентов и исключения | Appointment management, schedule/availability, customer operations, notifications |
| Master | Выполнить услугу и зафиксировать операционный результат | Schedule read, appointment context, service delivery, operational notes, completion |
| Service Delivery | Превратить подтверждённую запись в фактически оказанную услугу | Appointment lifecycle, service outcome capture; exact MVP semantics are `Open question` where not defined by Appointment Contract |

### 2.1 Business operation to domain model

| Business operation | Domain capability | Command | Event | Projection | Screen requirement |
| --- | --- | --- | --- | --- | --- |
| Клиент хочет записаться | Appointment Management + Availability | `CreateAppointment` | `appointment.created`, затем `appointment.confirmed` только после authoritative confirmation | Customer Appointment Projection | Показать статус записи и следующий допустимый шаг |
| Мастер начинает рабочий день | Schedule Management | `RequestOperationalContext` — `Proposed` | Не создаёт бизнес-событие сам по себе | Master Day Projection | Показать расписание, клиентов и разрешённые исключения |
| Клиент просит перенос | Appointment Management | `RescheduleAppointment` | `appointment.rescheduled` после committed change | Updated Appointment Projection | Показать old/new time и результат операции |
| Normal visit after scheduled end | Service Delivery / Appointment lifecycle | No mandatory manual command | appointment.completed only after authoritative three-hour resolution window and no exception before deadline | Visit Outcome Projection | Show normal zero-action waiting state, then authoritative completion/readback |
| Возник конфликт | Conflict Resolution — `Proposed` | `ResolveSchedulingConflict` — `Proposed` | Только после committed operational decision | Exception Projection | Показать конфликт, владельца решения и допустимые варианты |

`Command` выражает намерение изменить state. `Event` выражает уже случившийся
факт. Вызов кнопки, API, AI tool, timeout или notification delivery не является
доменным событием.

## 3. Roles and Responsibilities

| Role | Responsibilities | Allowed actions | Cannot do |
| --- | --- | --- | --- |
| Customer | Искать услугу, выбирать мастера, управлять своими визитами, сообщать об изменениях | Читать разрешённые offerings/availability; инициировать create/reschedule/cancel в пределах Appointment Contract; подтвердить предложенное действие | Изменять чужую запись, расписание салона, цену или provider state |
| Master | Работать по расписанию, проводить услугу, фиксировать разрешённые operational notes, завершать визит | Читать своё operational schedule и purpose-limited customer context; выполнять разрешённые service operations; инициировать operational correction через установленную команду | Читать semantic memory напрямую; менять глобальную цену/каталог; подтверждать факт за другого мастера без полномочия |
| Administrator | Управлять записями и расписанием, помогать клиентам, разрешать конфликты | Выполнять authorized appointment/schedule commands; эскалировать provider conflicts; отправлять operational notifications | Подменять Appointment/Availability owner или создавать второй источник истины |
| Salon Owner | Управлять бизнесом и контролировать операционные процессы | Читать разрешённые operational projections и управленческие показатели; принимать owner decisions, если они определены governance | Получать semantic memory или скрытые AI hypotheses без purpose/consent; менять канонический доменный state обходом владельца |
| Ayla AI Assistant | Помогать, рекомендовать, готовить действия, объяснять разрешённую информацию | Понять intent; показать варианты; подготовить command; вызвать approved tool; показать purpose-limited context | Самостоятельно создавать business fact, подтверждать appointment, менять цену/расписание, решать за мастера, диагностировать или делать медицинские выводы |

Роль в этой таблице не равна repository ownership. Физический исполнитель
команды может быть backend application, но authoritative domain owner определяется
Appointment/Availability contract, а не названием приложения. Role authority и
допустимость действий, включая schedule writes, определяются
[[Ayla Master MVP Auth and Authority Contract]].

## 4. Master Operating Journey

### 4.1 Start Day

**Business process:** мастер начинает рабочий день и получает контекст текущей
операционной работы.

**Нужные данные:** подтверждённые записи, время, offering и snapshots записи,
клиентский идентификатор, разрешённые booking-specific notes, исключения,
операционные задачи и freshness projection.

**Ayla может:** подготовить краткий operational context, обратить внимание на
ближайшую запись и показать разрешённые исключения.

**Ayla не может:** выводить скрытые причины рекомендаций, читать semantic
memory, угадывать отсутствие клиента или изменять расписание.

**Действия:** мастер читает расписание; при конфликте инициируется
`ResolveSchedulingConflict` или эскалация администратору. Само чтение не создаёт
доменного события.

**Projection:** `Master Day Projection`, источник — Appointment/Schedule source,
freshness и version обязательны. Это не новый System of Record.

### 4.2 Before Appointment

Мастер получает только необходимый operational context:

- время и текущий appointment status;
- услугу и исторические snapshots, зафиксированные в записи;
- идентификатор/разрешённое представление клиента;
- purpose-limited operational notes;
- разрешённые provider/booking-specific ограничения.

Мастер не получает semantic memory, полный conversation context, AI hypotheses,
данные других providers или скрытые recommendation reasons. Data Inventory Matrix
запрещает мастеру прямой доступ к semantic memory; provider получает только
purpose-limited operational projection.

### 4.3 During Service

**Business process:** мастер начинает оказание услуги, выполняет работу,
фиксирует операционные заметки и сообщает об исключениях.

`StartService` и модель service-delivery state — `Proposed`, пока они не
определены в Appointment Contract. Операционная заметка не становится memory
entry и не является медицинским заключением. Данные должны быть минимальными,
purpose-limited и видимыми только authorized consumers.

Если возникла проблема, мастер не исправляет канонический appointment прямым
редактированием. Он инициирует предусмотренную команду или передаёт ситуацию
администратору; результат должен быть подтверждён authoritative owner.

### 4.4 Complete Appointment

Нормальное завершение визита утверждено и автоматическое: по `scheduled_end`
authoritative backend completion mechanism Appointment Domain открывает
трёхчасовое post-visit resolution window; при отсутствии зарегистрированного
lifecycle exception до дедлайна публикуется `appointment.completed` (zero-action
happy path — обязательное действие мастера не требуется). Семантику определяет
Appointment Contract §5B (Authoritative Completion Runtime). Успешная отправка
команды, закрытие чата, timeout или notification delivery не означают
service completed.

`CompleteAppointment` остаётся только опциональным owner-authorized
correction/exception path: исправление ошибочно завершённой записи выполняется
исключительно через authorized correction path с audit, без dispute/support
subsystem. Открытыми остаются exception-path evidence и role authority
(`OQ-AC-3`/`OQ-AC-7`) и customer-side exception (`OQ-AC-17`, Deferred) — см.
`OQ-SO-1`.

## 5. Administrator Operating Journey

### 5.1 Booking Creation

```text
Customer request
  -> Availability read
  -> Appointment command
  -> authoritative validation
  -> appointment.created
  -> confirmation decision
  -> appointment.confirmed (только если подтверждено)
```

Запрос клиента, предложение AI и наличие слота не являются созданной записью.
`appointment.created` означает persisted appointment в допустимом статусе по
Appointment Contract. `appointment.confirmed` означает authoritative
confirmation. Administrator может помогать клиенту и выполнять authorized
command, но не становится отдельным producer событий.

### 5.2 Reschedule

Для MVP отдельно различаются:

1. **Same-ID reschedule:** изменяется время существующей записи; применяется к
   accepted Simple Reschedule и сохраняется тот же `appointment_id`.
2. **Replacement appointment:** старая запись и новая запись имеют отдельные
   идентификаторы; это требует отдельной семантики связи, уведомлений и
   cancellation/re-offer. Полный replacement flow — `Deferred / Open question`,
   если не активирован owner decision.

`RescheduleAppointment` может подготовить Ayla, но committed change и
`appointment.rescheduled` принадлежат Appointment owner. Нельзя считать вызов
AI tool или отправленное уведомление переносом.

### 5.3 Cancellation

Уполномоченный customer, master или administrator может **инициировать**
cancellation только в пределах Appointment Contract и role policy. Кто имеет
право окончательно подтвердить отмену, обязательные причины, последствия для
availability, re-offer и уведомлений требуют явной policy; неподтверждённые
части имеют статус `Proposed / OQ-SO-2`.

После authoritative commit публикуется `appointment.cancelled`. Сбой
уведомления не отменяет и не подтверждает бизнес-операцию; notification worker
обрабатывает delivery отдельно.

### 5.4 Conflict Resolution

| Конфликт | Операционная реакция | Кто принимает решение |
| --- | --- | --- |
| Мастер занят | Заблокировать неподтверждённое обещание; предложить другой слот/мастера; не подтверждать без authoritative availability | Appointment/Availability owner или authorized administrator; exact policy `Proposed` |
| Двойная запись | Выявить collision; сохранить один authoritative state; эскалировать affected appointments, не создавать второй факт | Appointment/Availability owner; resolution command `Proposed` |
| Изменение графика | Пересчитать affected availability и предложить допустимые варианты; не переписывать историю silently | Schedule owner + authorized administrator; policy `Proposed` |
| Отсутствие мастера | Не считать запись выполненной; запустить reassign/cancel/escalation flow только по policy | Administrator/provider operations; reassign semantics `Deferred` |
| Необходимость переназначения | Подготовить candidate replacement, получить required confirmation, сохранить связь старой и новой записи | Appointment owner; replacement model `Open question` |

Ни Ayla, ни notification system не могут молча выбрать победителя конфликта.

## 6. Customer Operating Journey

### 6.1 Discovery

Клиент начинает с цели или потребности, а не с конкретного экрана. Ayla может
объяснить услугу, уточнить минимально необходимый контекст и предложить
допустимые варианты. Recommendation не является appointment и не гарантирует
доступность, цену или результат.

### 6.2 Booking

Клиент выбирает offering, мастера/assignment и слот из разрешённой availability
projection. Ayla подготавливает `CreateAppointment`; backend/domain owner
валидирует команду и фиксирует запись. Клиент должен видеть различие между
`requested`, `created` и `confirmed`, если эти состояния доступны контракту.

### 6.3 Confirmation

Клиент понимает, что запись подтверждена, только по authoritative appointment
state/confirmation projection. Экран, сообщение AI или notification без такого
state не может обещать подтверждение.

### 6.4 Reschedule

Клиент инициирует перенос, получает допустимые варианты и подтверждает command.
Для accepted Simple Reschedule меняется время той же записи. Replacement
вариант не должен имитироваться как same-ID изменение; его использование
остаётся deferred до отдельного решения.

### 6.5 Cancellation

Клиент запрашивает отмену, видит последствия и подтверждает действие, если это
требует policy. Ayla готовит command; authoritative owner валидирует права,
причину и state transition. Отмена считается фактом только после
`appointment.cancelled`.

### 6.6 Visit

Клиент приходит на подтверждённую запись, получает услугу и может сообщить о
проблеме. Визит не считается завершённым из-за времени, уведомления или
предположения AI. Нормальный факт completion создаётся authoritative backend
completion mechanism Appointment Domain без обязательного действия человека
(см. Appointment Contract §5B); authorized operational actor требуется только
для exception/correction path по правилам Appointment Contract.

### 6.7 Follow-up

После услуги Ayla может показать подтверждённый operational outcome, предложить
следующий безопасный шаг или запросить feedback, если соответствующая capability
активна и purpose/consent позволяют. Она не должна превращать feedback в
медицинский вывод, скрытую память или автоматическое обещание результата.

## 7. Ayla AI Role Boundary

### 7.1 Ayla CAN

- объяснить услугу и известные ограничения;
- помочь выбрать среди разрешённых вариантов;
- предложить варианты слота, мастера или следующего шага;
- показать purpose-limited operational context;
- подготовить command и передать его authorized owner;
- помочь мастеру ориентироваться в расписании и разрешённых notes;
- объяснить результат authoritative operation и обозначить неопределённость.

### 7.2 Ayla CANNOT

- самостоятельно создать business fact;
- самостоятельно подтвердить запись;
- изменить цену или исторический snapshot;
- изменить расписание без authorized command;
- принять решение вместо мастера, администратора или владельца домена;
- считать tool invocation, timeout или message delivery событием;
- читать или распространять semantic memory без purpose/consent gate;
- делать медицинские выводы или диагнозы.

Правило:

```text
AI suggestion != Business action
AI-prepared command != Committed domain state
Committed domain state -> authoritative event -> projection
```

## 8. Operational Capabilities MVP

`MVP` здесь означает операционный scope этого контракта, а не утверждение,
что capability уже активирована во всех репозиториях. Capability Registry и MVP
Scope остаются источниками activation status.

| Capability | MVP | Owner | Notes |
| --- | --- | --- | --- |
| Appointment Management | MVP operational slice / Proposed | Appointment Domain | Create/confirm и accepted same-ID Simple Reschedule; full cancellation, replacement, re-offer — Deferred/decision-dependent |
| Schedule Management | Proposed MVP support | Schedule/Availability Domain — owner not fully resolved | Read operational schedule and apply authorized changes; no second schedule SoR |
| Customer Management | Proposed MVP support | Customer/User Context owner — exact salon ownership Open question | Booking-specific customer projection allowed; not semantic memory |
| Service Management | Pilot seed / Proposed | Provider/Service Offering owner — exact domain owner Open question | Offerings, assignment and snapshots needed for appointment; full catalog governance not established here |
| Operational Notes | Proposed, constrained | Appointment/Service Delivery owner — Pending owner decision | Purpose-limited notes only; not memory, diagnosis or unrestricted chat history |
| Notifications | Proposed MVP support | Notification Domain | Delivery is a projection/side effect; notification success is not business success |
| Availability | Proposed MVP support | Availability Domain — Pending owner decision | Availability is read/validated by Appointment owner; provider sync semantics remain bounded |
| Reviews/Feedback | Deferred | Pending owner decision | Follow-up may be prepared as a proposal; review state and publication policy are not canonical |
| Earnings | Deferred | Pending owner decision | No MVP earnings SoR or calculation policy is defined by current sources |

## 9. Master ↔ Ayla Interaction Model

```text
Appointment approaching
  -> Ayla prepares allowed operational context
  -> Master reviews context
  -> Master decides / executes authorized operation
  -> Domain owner commits state
  -> Domain event is published
  -> Ayla and screens consume a projection
```

Ayla помогает мастеру уменьшить operational cognitive load, но не заменяет его
профессиональную или operational responsibility. Пример: Ayla может показать
время, услугу и разрешённые notes; мастер решает, как проводить услугу и когда
сообщить об исключении; только owner contract определяет, какой факт записан.

## 10. Automation Boundary

| Может быть автоматизировано | Требует authorized human/domain decision |
| --- | --- |
| Сбор intent, подготовка вариантов, чтение projections, напоминание, маршрутизация исключения, нормальное service completion (утверждённый automated authoritative domain outcome, Appointment Contract §5B) | Confirmation, price change, schedule change, reassignment, cancellation policy exception, service completion correction |
| Дедупликация delivery и retry уведомлений | Определение, что appointment создан/подтверждён/завершён |
| Формирование operational context с freshness/version | Медицинское заключение, скрытая inference или решение за мастера |

Автоматизация может вызвать command только с установленной authorization,
idempotency и проверкой актуального state. Она не получает право владеть
доменным фактом.

## 11. Provider Boundary and Pilot

`formula_tela` рассматривается как pilot provider integration, а не как
глобальный Ayla operational System of Record. Provider может быть источником
операционного сигнала в рамках интеграционного контракта, но Ayla не создаёт
параллельные независимые `Formula Tela Appointment` и `Ayla Appointment` для
одного факта.

Provider/master получает только purpose-limited operational projection. Нельзя
передавать semantic memory, AI hypotheses, сведения других providers, скрытые
recommendation reasons или полный conversation context.

## 12. Failure Semantics

Интеграционный или коммуникационный неуспех не является успехом бизнес-
операции:

| Наблюдение | Что оно означает | Чего оно не означает |
| --- | --- | --- |
| Timeout при CreateAppointment | Неизвестный результат; нужен reconciliation/readback или escalation | `appointment.confirmed` |
| Уведомление доставлено | Communication side effect | Appointment created/confirmed |
| Provider sync failed | Интеграционная ошибка и stale/unknown context | Appointment cancelled или completed |
| Команда принята в AI runtime | Intent/command preparation | Domain write |
| `appointment.confirmed` committed | Authoritative confirmation fact | Услуга оказана |

Неопределённый результат должен быть обозначен пользователю и операционному
участнику; повтор команды должен быть idempotent и не создавать второй факт.

## 13. Screen and Interaction Consequences

Этот раздел не задаёт экраны. Он задаёт минимальные данные, без которых любой
экран/бот/mini app не может быть корректным:

- source of truth и статус appointment;
- actor, permitted action и authorization result;
- availability freshness/version;
- old/new values для same-ID reschedule;
- distinction между suggestion, command accepted и committed event;
- conflict state, owner of resolution и next allowed action;
- purpose-limited customer context и privacy boundary.

Экран не может самостоятельно вычислять подтверждение, completion, cancellation
или ownership из локальной projection.

## 14. Owner Decisions and Open Questions

| ID | Decision / Question | Status |
| --- | --- | --- |
| OD-SO-1 | Зафиксировать этот документ как канонический operating contract и определить его Product Owner | Proposed |
| OD-SO-2 | Назначить authoritative owner для Schedule/Availability и границу между provider schedule и Ayla projection | Pending owner decision |
| OD-SO-3 | Утвердить, кто может окончательно подтвердить cancellation и какие причины/уведомления обязательны | Open question |
| OQ-SO-1 | Remaining producer/evidence/correction rules after the approved three-hour window and separation from no_show | Duration and zero-action rule approved; remaining semantics open | Open question |
| OQ-SO-2 | Входит ли cancellation в ближайший MVP slice или остаётся deferred согласно MVP Scope/AYLA-DEC-0022? | Open question |
| OQ-SO-3 | Нужен ли replacement appointment для pilot; если да, как связать old/new appointment и события? | Open question |
| OQ-SO-4 | Кто владеет customer profile и salon-specific operational customer projection? Booking-time customer resolution (search/dedup/creation) закреплена в [[Ayla MVP Customer Resolution Contract]]; owner decision остаётся открытым | Open question |
| OQ-SO-5 | Какой минимальный набор operational notes разрешён мастеру и каков retention/correction policy? | Open question |
| OQ-SO-6 | Активируется ли Reviews/Feedback в MVP и кто владеет feedback state? | Open question |
| OQ-SO-7 | Нужна ли Earnings capability в provider pilot; если да, кто владеет расчётом? | Open question |

- [x] Normal visit completion is a zero-action path after the approved three-hour window; feedback/review does not change lifecycle outcome.
- [x] Customer-arrived/non-delivery remains unresolved and is not mapped to no_show, completed, or a new status/event/command.

## 15. Validation Checklist

- [x] Business process отделён от capability, command, event, projection и screen.
- [x] AI не назначен владельцем Appointment, Availability, Consent, Payment или Provider state.
- [x] Чтение projection не создаёт ownership и не становится вторым SoR.
- [x] `appointment.created`, `appointment.confirmed`, `appointment.rescheduled`, `appointment.cancelled` и `appointment.completed` трактуются как committed facts, а не UI/API/tool signals.
- [x] Same-ID reschedule отделён от replacement appointment.
- [x] `no_show` не смешан с `cancelled`; его operational authority вынесена в Open Questions через Event Registry/Appointment Contract.
- [x] Provider boundary и purpose-limited privacy projection зафиксированы.
- [x] Timeout, delivery failure и provider sync failure не объявляются успехом бизнес-операции.
- [x] Неподтверждённые решения явно отмечены статусами `Proposed`, `Pending owner decision` или `Open question`.
- [ ] Owner review и canonical activation не выполнены.

## 16. Change Log

| Version | Date | Change |
| --- | --- | --- |
| 0.1 | 2026-08-14 | Initial proposed Salon Operations MVP Contract |
