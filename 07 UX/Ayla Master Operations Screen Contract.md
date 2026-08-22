---
node_id: ayla.ux.master-operations-screen-contract
title: Ayla Master Operations Screen Contract
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
updated: 2026-08-14
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
  - "[[Ayla MVP Scope and Release Contract]]"
  - "[[Ayla MVP User Journey Specification]]"
  - "[[Consent Scope Registry]]"
  - "[[Data Inventory Matrix]]"
---

# Ayla Master Operations Screen Contract

> Первый канонический Screen Contract UX-слоя Ayla. Документ определяет смысл,
> данные, состояния, действия и границы рабочего экрана мастера. Он не является
> UI-макетом, визуальным дизайном, API-спецификацией или техническим планом
> реализации.

## 1. Purpose

`Master Operations Screen` — рабочий центр мастера для управления текущим
рабочим днём через разрешённое operational context.

Экран решает одну ежедневную задачу: помочь мастеру понять, какие подтверждённые
визиты требуют внимания, подготовиться к ближайшему клиенту, выполнить
разрешённую операционную работу и зафиксировать результат через authoritative
command.

Экран используется в последовательности:

```text
Start day
  -> review today's operational projection
  -> prepare for the next appointment
  -> perform the service
  -> initiate an allowed outcome command
  -> observe the updated authoritative projection
```

Экран не является:

- CRM или полной карточкой клиента;
- аналитической панелью салона;
- инструментом управления бизнесом, каталогом, ценами или расписанием;
- источником истины для Appointment, Availability, Consent или Payment;
- интерфейсом доступа к semantic memory или полному conversation context;
- AI-ассистентом с правом самостоятельно изменять business state.

Его контрактная позиция:

```text
Business Operation
  -> Operational Capability
  -> Projection
  -> Screen Data Contract
  -> User Action
  -> Command
  -> Domain Event
  -> Updated Projection
```

`Screen State != Domain State`. `Projection != Source of Truth`.

## 2. Contract Position and Responsibilities

Документ является контрактом между Product Operations, Architecture, Backend,
Mobile App — UX/UI.

| Участник | Ответственность в рамках экрана |
| --- | --- |
| Product Operations | Определяет операционную задачу мастера и допустимый workflow. |
| Architecture | Определяет доменные границы, ownership, commands, events и source of truth. |
| Backend | Предоставляет авторизованные projections и исполняет команды по доменным контрактам. |
| Mobile App | Представляет projection, состояния загрузки/ошибки и результаты команд. |
| UX/UI | Определяет понятное взаимодействие и recovery без изменения доменной семантики. |
| Ayla AI | Может объяснять разрешённый контекст и подготовить действие; не владеет business state. |

Физическое расположение этого документа в `07 UX` означает UX-ответственность
за screen contract, но не переносит сюда ownership Appointment, Availability,
events, permissions или transactional state.

## 3. User Context

### 3.1 Primary User

**Primary User:** Master.

Мастер работает в пределах tenant/provider scope и видит только тот
operational context, который разрешён его ролью, purpose и policy.

### 3.2 Goals

Мастер должен иметь возможность:

1. понять расписание и ближайшую рабочую задачу;
2. увидеть подготовленный для него минимум контекста по визиту;
3. выполнить услугу и сообщить об операционном результате;
4. распознать изменение, конфликт или неопределённость;
5. инициировать разрешённую команду либо быстро передать ситуацию администратору;
6. увидеть, подтверждён ли результат authoritative owner.

### 3.3 Pain Points

Экран должен снижать следующие операционные проблемы:

- неизвестно, кто следующий клиент и какая запись требует внимания;
- у мастера нет контекста, необходимого для подготовки к визиту;
- сложно обработать изменения, конфликты и исключения в рабочем дне;
- слишком много информации приходится собирать и проверять вручную;
- смешение appointment status, transaction status и UI status;
- риск принять AI-подсказку или локальное состояние за подтверждённый факт;
- отсутствие понятного recovery при stale projection, конфликте или неуспешной команде;
- показ мастеру лишних клиентских данных, истории или скрытого AI-контекста.

### 3.4 Role and Privacy Boundary

Мастер может читать своё расписание и purpose-limited customer context,
выполнять разрешённые service operations и инициировать разрешённые
операционные действия. Роль мастера не даёт права:

- читать semantic memory, полный conversation context или AI hypotheses;
- видеть данные других providers или клиентов вне operational need;
- менять глобальные цены, каталог, расписание или provider state;
- подтверждать факт за другого мастера без отдельного полномочия;
- обходить consent, authorization или Appointment ownership.

Минимальный набор персональных данных определяется `Consent Scope Registry` и
`Data Inventory Matrix`. Если purpose, scope или authorization неизвестны,
экран применяет fail-closed поведение: данные не показываются.

### 3.5 User Context Decisions to Confirm

Следующие вопросы не решаются этим Screen Contract и требуют product/owner
решения:

| ID | Вопрос | Статус |
| --- | --- | --- |
| UX-MOS-OQ-01 | Нужен ли мастеру полный список клиентов дня или только записи в его operational scope? | Open question |
| UX-MOS-OQ-02 | Допустима ли история предыдущих визитов, и в каком purpose-limited объёме? | Open question; privacy review required |
| UX-MOS-OQ-03 | Нужна ли отдельная операция `StartService`? | Proposed in Product Operations; domain semantics pending |
| UX-MOS-OQ-04 | Нужен ли мастеру check-in, и чей domain owner подтверждает его значение? | Open question |
| UX-MOS-OQ-05 | Authoritative producer, evidence, and correction policy after the approved three-hour window | Duration and zero-action rule approved; remaining semantics open | Appointment Owner / Product Owner |
| UX-MOS-OQ-06 | Какие действия мастер может выполнять без администратора? | Role policy / owner decision required |

До закрытия вопросов экран не должен превращать предположение в обязательную
capability или UI action.

## 4. Screen Responsibility Boundary

### 4.1 What the Screen Does

Master Operations Screen:

- показывает рабочий день и его разрешённый operational context;
- предоставляет доступ к разрешённым операционным действиям мастера;
- показывает minimum necessary context по ближайшему и текущему визиту;
- показывает изменения, исключения, freshness и следующий допустимый шаг;
- отражает результат команды только после authoritative validation/commit.

### 4.2 What the Screen Does Not Do

Экран:

- не управляет бизнесом, каталогом, ценами или глобальным расписанием;
- не меняет правила записи и не создаёт собственную appointment policy;
- не принимает решения вместо Appointment Domain, Availability owner или policy owner;
- не заменяет Appointment Domain и не становится владельцем Appointment;
- не превращает projection, локальное состояние или AI output в business fact.

Экран — это представление операционного процесса и boundary для действий, а не
место, где определяется доменная бизнес-логика.

## 5. Information Architecture

Ниже определены логические блоки экрана. Это не описание layout, визуальных
компонентов или порядка размещения элементов.

| Logical block | Цель | Зачем нужен мастеру | Источник данных |
| --- | --- | --- | --- |
| `Master Operations Home` | Дать единый operational entry point | Быстро понять состояние рабочего дня и доступные следующие действия | `Master Day Projection`, authorization/policy projection |
| `Today Context` | Определить рамки текущего рабочего дня | Проверить дату, timezone, рабочий scope, freshness и наличие изменений | Schedule/operational projection |
| `Next Appointment` | Выделить ближайшую задачу | Понять, кто следующий, когда визит, какая услуга и какой минимум подготовки нужен | `Appointment Operational Projection`, permitted customer context |
| `Day Timeline` | Представить все разрешённые рабочие записи в контексте дня | Планировать последовательность работы и заметить gaps/conflicts | `Master Day Projection`, Appointment/Schedule sources |
| `Operational Exceptions` | Сделать неопределённости и изменения явными | Понять, что требует refresh, retry, escalation или решения администратора | `Exception Projection`, command results, registered event consumers |
| `Tasks` | Показать разрешённые операционные follow-ups | Не держать ручные напоминания вне системы и завершать рабочие шаги | Product Operations task projection; exact capability pending |
| `Ayla Assistant Context` | Дать безопасную помощь поверх уже разрешённого контекста | Получить объяснение, summary или следующий допустимый шаг без доступа к скрытым данным | Current screen projection only; no direct semantic memory |

Каждый блок является consumer-ом projection. Ни один блок не является отдельным
источником истины. `Ayla Assistant Context` не получает более широких прав, чем
сам экран и роль мастера.
## 6. Business Operation

### 6.1 Operational Problem

Бизнес-операция экрана — `Master Daily Service Delivery`:

> Мастер получает разрешённый контекст текущего рабочего дня, выполняет
> назначенные услуги и фиксирует только те результаты, для которых существует
> authorized command — authoritative confirmation path.

Экран поддерживает service delivery, но не владеет расписанием и не принимает
решения за Appointment Domain или Salon Operations.

### 6.2 Daily Operating Cycle

| Шаг | Операционная потребность | Экранный результат |
| --- | --- | --- |
| Start day | Получить актуальный operational context | `Master Day Projection` загружена или показана причина недоступности |
| Before appointment | Подготовиться к ближайшему визиту | Показан minimum necessary appointment context |
| During service | Выполнить услугу и при необходимости сообщить исключение | Доступны только разрешённые actions; notes не становятся memory |
| Post-visit outcome | Show normal waiting state or permitted exception | Ordinary visit requires no manual completion; completed only after authoritative readback |
| Exception | Разобраться с конфликтом или неопределённостью | Показан owner/next allowed step; silent overwrite запрещён |

### 6.3 Non-goals

В этот экран не входят:

- управление расписанием салона, staff assignment и каталогом;
- редактирование канонической Appointment напрямую;
- полноценная CRM-история и customer profile;
- финансовые операции и payment management;
- аналитика производительности мастера;
- автоматическое распределение клиентов или переназначение мастеров;
- медицинские выводы, диагностика или скрытое профилирование;
- новые domain rules, event names или permission policies.

## 7. Operational Capability

Ниже capability указаны как ссылки на существующую операционную модель. Новые
CAP-ID этим документом не создаются.

| Capability / operation | Для чего экран её потребляет | Contract status |
| --- | --- | --- |
| Schedule Management / operational context read | Показать рабочий день и ближайшие записи | Existing; `RequestOperationalContext` proposed |
| Appointment Management | Показать appointment projection и разрешённые transitions | Existing; owner — Appointment Domain |
| Service Delivery | Поддержать выполнение услуги и outcome capture | Existing in operations model; exact completion semantics open |
| Conflict Resolution | Показать exception и передать решение authorized owner | Proposed |
| Operational Notes | Сохранить минимальную purpose-limited note, если capability активирована | Policy and persistence contract required |

Доменная capability определяет бизнес-смысл. Screen Contract только определяет,
какая часть результата capability нужна мастеру и как она отображается.

## 8. Projection Model

### 8.1 Primary Projection

Основная projection экрана — `Master Day Projection`.

Она является read model, собранной из разрешённых источников Appointment/Schedule
и связанных operational projections. Она должна иметь freshness/version metadata
и не становится новым System of Record.

| Projection | Назначение | Source of truth |
| --- | --- | --- |
| `Master Day Projection` | Список рабочего контекста, ближайшие записи, исключения и freshness | Appointment/Schedule authoritative sources; exact repository is implementation decision |
| `Appointment Operational Projection` | Разрешённые поля конкретного визита и его display status | Appointment Domain / authoritative Appointment state |
| `Customer Operational Context Projection` | Минимум данных, необходимый для данной услуги и роли мастера | Authorized backend/domain sources; not semantic memory |
| `Exception Projection` | Конфликт, stale state, failed command или требуемая эскалация | Authoritative operation result / registered event consumers |
| `Updated Appointment Projection` | Результат после принятой команды | Authoritative Appointment state after commit |

### 8.2 Projection Invariants

- Projection не определяет Appointment lifecycle.
- `loading`, `stale`, `error`, `unknown` — UI/projection states, не domain facts.
- `HTTP success`, local optimistic state, AI acknowledgement или notification
  delivery не подтверждают appointment transition.
- При конфликте версий экран не молча перезаписывает состояние; он показывает
  stale/unknown и предлагает refresh, retry или escalation.
- Каждое поле должно иметь source, purpose и role authorization.
- Отсутствующее или неразрешённое поле не заполняется догадкой.

## 9. Screen Data Contract

Это логический контракт данных, а не API schema. Имена полей являются
семантическими placeholders; точный DTO/endpoint остаётся Engineering/API
ответственностью.

### 9.1 Data Block Contract

Каждый логический блок экрана обязан иметь собственные `Data`, `Source`, `Owner`
и `Refresh` правила. Эти поля описывают ответственность и жизненный цикл данных,
а не конкретный API DTO.

#### Today Summary

| Field | Contract |
| --- | --- |
| Purpose | Дать мастеру целостное понимание текущего рабочего дня до начала работы.
| Data | Рабочий день, количество разрешённых записей, текущий operational status, freshness/version. |
| Source | `Schedule/Operational Projection`. |
| Owner | Schedule / Product Operations owner; точный repository owner не определяется UX. |
| Refresh | При открытии рабочего дня, user request, изменении версии projection или возвращении из background. При stale/unknown экран не делает вывод о пустом дне. |

#### Appointment Card

| Field | Contract |
| --- | --- |
| Purpose | Дать мастеру контекст ближайшего визита и безопасный доступ к допустимым действиям.
| Data | `appointment_id`, время, услуга, длительность, разрешённое представление клиента, appointment status, доступные действия и причины недоступности. |
| Source | `Appointment Operational Projection`. |
| Owner | `Appointment Domain`. |
| Refresh | После открытия карточки, изменения appointment version/event, command result и обнаружения stale projection. Команда не считается успешной до updated authoritative projection. |

`appointment_id` является стабильной идентичностью записи, но не даёт экрану
права изменять её. Время не вычисляет статус, а duration/service являются
snapshot-данными согласно Appointment Contract.

#### Customer Context

| Field | Contract |
| --- | --- |
| Purpose | Помочь мастеру подготовиться к услуге без раскрытия лишних персональных данных.
| Data | Только minimum necessary context для текущей услуги и operational purpose: имя или разрешённый display label, предыдущие operational notes если они authorized, и иная явно разрешённая информация. |
| Source | `Customer Operational Context Projection`, построенная из authorized backend/domain sources. |
| Owner | Соответствующий customer/consent/data owner; Screen Contract не создаёт владельца данных. |
| Refresh | При открытии appointment context, изменении authorization/consent scope, обновлении operational note или версии projection. При отсутствии доказанного scope данные скрываются. |

Мастеру запрещено показывать:

- скрытую AI memory и memory candidates;
- AI inference, hypotheses или не подтверждённые выводы;
- данные других клиентов;
- данные других providers/tenants;
- полный conversation context, если он не является отдельно approved operational projection;
- медицинские выводы и чувствительные inference.

#### Exceptions

| Field | Contract |
| --- | --- |
| Purpose | Сделать изменения и исключения явными и показать, кто принимает следующее решение.
| Data | Customer late, master issue, reassignment, provider sync issue, stale/failed command, owner of next decision и разрешённый next step. |
| Source | `Operational Exception Model` / `Exception Projection`. |
| Owner | Соответствующий operational, Appointment, provider или administrator owner; exact ownership определяется existing contracts. |
| Refresh | После provider/integration update, registered event consumer update, command result, retry или escalation result. Исключение не закрывается локальным dismiss без authoritative resolution. |

#### Refresh Contract

`Refresh` — это read/update projection operation, а не доменная команда. Refresh:

- не меняет Appointment или Schedule;
- не создаёт domain event;
- должен возвращать новую version/freshness либо объяснимый failure;
- не должен скрывать расхождение между локальным состоянием и источником;
- после изменения source должен обновлять только разрешённые блоки.
### 9.2 Required Data

| Data group | Minimum meaning | Source | Display constraint |
| --- | --- | --- | --- |
| Day context | date, timezone, scope, projection freshness/version | Schedule/operational projection | Показывать только в operational scope |
| Appointment identity | stable `appointment_id`, status, version | Appointment projection | ID не является заменой display authorization |
| Time | start/end/timezone and relative urgency | Appointment projection | Не вычислять бизнес-статус из времени |
| Service snapshot | offering/service name, duration/price snapshot only where permitted | Appointment Contract projection | Snapshot не редактируется экраном |
| Assignment | assigned specialist/master reference | Appointment/assignment projection | Не разрешает менять ownership |
| Customer context | minimum identity/display label and booking-specific context | Authorized operational projection | No full profile, semantic memory or hidden hypotheses |
| Operational notes | purpose-limited notes if authorized | Approved operational notes source | Не считать memory entry или medical record |
| Exception state | conflict, stale, blocked, escalation reason and next allowed step | Operation result/exception projection | Не скрывать uncertainty |
| Action availability | allowed action, reason unavailable, confirmation requirement | Authorization/policy result | Permission failure is not a UI accident |

### 9.3 Explicitly Excluded Data

Экран не имеет права показывать без отдельного approved purpose, scope и policy:

- semantic memory — memory candidates;
- полный conversation history или AI reasoning;
- скрытые recommendation reasons и AI hypotheses;
- данные других клиентов, мастеров, providers или tenants;
- медицинские выводы, диагнозы и чувствительные inference;
- payment details, если они не нужны текущей operational action;
- consent records сверх минимального authorization/result signal;
- данные, полученные только из технического event, analytics или notification.

### 9.4 Data Freshness and Failure

Экран должен различать:

| State | Meaning | Allowed UX consequence |
| --- | --- | --- |
| `fresh` | Projection соответствует известной версии источника | Можно показать разрешённый контекст |
| `stale` | Данные устарели или требуют refresh | Не обещать актуальность; refresh/retry/escalation |
| `unknown` | Невозможно доказать состояние | Не разрешать рискованное действие без повторной проверки |
| `loading` | Read operation ещё не завершена | Не считать отсутствие данных пустым расписанием |
| `error` | Read operation неуспешна | Объяснить ограничение и recovery path |

## 10. User Actions, Commands and Events

### 10.1 Master Action Contract Format

Каждое действие мастера описывается в формате:

```text
Action
  -> Preconditions
  -> Authorization
  -> Command
  -> Result
  -> Domain Event (only after commit)
  -> Updated Projection
  -> Refresh / Recovery
```

| Action | Preconditions | Authorization | Command | Result / event | Refresh / recovery |
| --- | --- | --- | --- | --- | --- |
| Open Today Summary | Identity and master scope valid | Master read access | `RequestOperationalContext` | `Master Day Projection`; no domain event | Refresh on stale/error |
| Open Appointment Card | Appointment belongs to allowed scope | Master read access | Read projection | Appointment context; no state change | Reload by appointment version |
| Refresh | Projection stale, unknown, changed or user requested | Master read access | Read/refresh request | New projection version or explicit failure | Retry, stale explanation or escalation |
| Start Service | Capability and policy approved; appointment is actionable | Master permission pending owner decision | `StartService` — proposed | Service state/event semantics pending | Pending → updated projection or blocked |
| Post-visit resolution | scheduled_end passed and projection is current | No manual action for normal visit; exception only if canonical authority permits | No local command; permitted exception command only | Authoritative completed or exception projection | Readback; pending/unknown remains explicit |
| Report Exception | Exception type and operational scope known | Master may report; resolution owner differs | Exception/report command — proposed | Exception projection or escalation | Show owner and next permitted step |
| Cancel / Reschedule | Appointment policy, state and required reason allow action | Role policy from Appointment Contract | `CancelAppointment` / `RescheduleAppointment` | Registered event only after commit | Refresh appointment and day projection |
| Add Operational Note | Approved purpose, scope, retention and note capability exist | Master note permission pending | Note command — exact contract pending | Operational note result; not memory | Refresh authorized context or show rejection |

No action may be inferred from a visible block alone. The backend/domain boundary
revalidates authorization, version and preconditions before committing a change.
### 10.2 Action Contract

Каждое действие экрана должно иметь precondition, authorized actor, command,
результат и recovery. Нажатие, API request, AI tool call или timeout сами по
себе не являются domain event.

| User action | Preconditions | Command / intent | Expected result |
| --- | --- | --- | --- |
| Открыть рабочий день | Identity and role authorized | `RequestOperationalContext` — proposed | `Master Day Projection` или read error; domain event не создаётся |
| Открыть визит | Appointment принадлежит разрешённому scope | Read appointment projection | Context loaded; state не изменяется |
| Обновить контекст | Projection stale/unknown или user request | Refresh/read request | New projection version или explicit failure |
| Начать услугу | Только если policy и domain contract активируют capability | `StartService` — proposed | Service-delivery state; event semantics pending |
| Обычный визит | After scheduled_end and before deadline show that nothing is required; after deadline follow authoritative projection | No mandatory command; exception only under canonical policy | completed only after authoritative readback; pending/unknown remains explicit |
| Инициировать отмену | Role policy, Appointment state и required reason | `CancelAppointment` — по Appointment Contract | `appointment.cancelled` только после authoritative commit |
| Инициировать перенос | Role policy и accepted reschedule rules | `RescheduleAppointment` | Для same-ID time-only: updated appointment и `appointment.rescheduled` после commit |
| Зафиксировать operational note | Approved purpose, scope и note capability | Note command — exact contract pending | Persisted operational note или rejected; не memory event |
| Передать администратору | Exception или недостаток полномочий | Escalation command — proposed | Exception/escalation projection; no silent domain mutation |

### 10.3 Result Event Scenarios

#### View Appointment

`View Appointment` — только чтение. Оно загружает разрешённую Appointment
Operational Projection и не создаёт command, domain event или изменение
Appointment state.

#### Post-Visit Resolution and Completion

Normal visit
  -> authoritative scheduled_end
  -> 3-hour resolution window
  -> no lifecycle exception before deadline
  -> authoritative normal completion
  -> updated Appointment Projection
  -> screen refresh

No manual CompleteAppointment is required for the normal path. Any exception or
correction command remains subject to canonical authority and evidence. Local
time, closing the screen, request submission, timeout, or AI acknowledgement do
not establish completed state. The screen shows completed only after authoritative
projection/readback.
#### No Show

```text
Master action
  -> MarkNoShow command
  -> domain validation
  -> appointment.no_show event
  -> updated Appointment Projection
  -> screen refresh
```

`MarkNoShow` и право мастера его выполнять не считаются утверждёнными новым
решением этого документа. Событие и его семантика должны использоваться только
в статусе, указанном `Ayla Domain Event Registry` и Appointment Contract.

#### Request Change

`Request Change` не получает собственной семантики без источника. В зависимости
от существующего authoritative contract это может быть:

- command;
- proposal для authorized owner;
- admin workflow / escalation.

Screen Contract не выбирает вариант автоматически. До owner decision экран должен
показывать request как pending/proposed или направлять мастера к администратору,
но не менять Appointment напрямую.
### 10.4 Confirmation Rules

Подтверждение пользователя требуется для действий с внешним эффектом, если это
предписано Appointment Contract, role policy или Consent Scope Registry. Экран
не должен показывать success до authoritative result.

Команда должна быть повторяемой безопасно: при retry используется version или
идемпотентный business key, если это определено backend/domain contract.

### 10.5 Updated Projection

После команды экран следует цепочке:

```text
User Action
  -> authorization and precondition check
  -> command request
  -> authoritative validation
  -> committed state change or rejection
  -> registered domain event, when applicable
  -> updated projection
```

Если команда принята к обработке, отображается `pending`, а не утверждение
успеха. `appointment.completed` отображается только после подтверждённого
authoritative state change. Сбой notification не изменяет доменный результат.

## 11. State Model

### 11.1 Screen States

Screen state описывает доступность projection и взаимодействия:

```text
uninitialized
  -> loading
  -> ready
  -> stale
  -> action_pending
  -> ready (after updated projection)

loading -> error -> retrying -> loading
ready/stale -> blocked_or_escalation
```

Screen state не равен Appointment lifecycle. Например, `ready` не означает
`confirmed`, `action_pending` не означает `completed`, а `error` не означает
`cancelled`.

### 11.2 Required Screen States

| State | Meaning | Required behavior |
| --- | --- | --- |
| `Normal` | Есть разрешённые записи и актуальная projection | Показать рабочий день, next appointment, timeline и доступные actions. |
| `Empty Day` | В operational scope нет записей | Явно показать отсутствие записей; не трактовать отсутствие projection как empty day. |
| `Offline` | Нет соединения или read/write boundary недоступен | Показать последний безопасный context только с freshness; не обещать актуальность и не подтверждать commands. |
| `Changed Appointment` | Запись изменилась после открытия экрана | Инвалидировать stale context, показать изменение и запросить refresh; не отправлять действие поверх неизвестной версии. |
| `Exception State` | Есть operational problem: late, issue, reassignment или provider sync problem | Показать exception, owner/next permitted step и recovery; не скрывать проблему локальным dismiss. |

`Normal` — screen state, а не гарантия appointment status. `Empty Day`,
`Offline`, `Changed Appointment` и `Exception State` не создают domain events.

### 11.3 Appointment State Display

Названия и переходы берутся из `Ayla MVP Appointment Contract` и
`Ayla Domain Event Registry`. Экран может отобразить `requested`,
`pending_confirmation`, `confirmed`, `cancelled`, `completed`, 
o_show`,
`rejected` или `expired` только когда это значение доступно из разрешённой
authoritative projection. Экран не выводит эти состояния из времени, кнопки,
локального флага или AI-ответа.

## 12. Backend Capabilities Required

Ниже перечислены потребности UX-контракта, а не API endpoints.

Backend должен обеспечить:

1. авторизованное чтение `Master Day Projection` в tenant/provider scope;
2. stable identity, version и freshness для appointment projections;
3. role/policy-aware filtering customer context;
4. командный boundary для разрешённых service/appointment operations;
5. authoritative validation до подтверждения внешнего эффекта;
6. idempotency/concurrency handling для повторной отправки команды;
7. различение committed, pending, rejected, failed и unknown результатов;
8. публикацию только зарегистрированных domain events;
9. обновление projection после committed event/state change;
10. audit/authorization trace без раскрытия лишних персональных данных;
11. recovery/error reason, достаточный для refresh, retry или escalation;
12. возможность безопасно отозвать или ограничить доступ при изменении policy.

Exact API shape, endpoint names, DTOs, database models и deployment остаются
вне этого документа.

## 13. AI Boundary

### 13.1 Allowed AI Behavior

Ayla AI может:

- кратко объяснить разрешённый operational context;
- помочь найти ближайшую запись в уже выданной projection;
- подсветить явное исключение, stale state или отсутствие данных;
- предложить следующий разрешённый шаг;
- подготовить command request для явного подтверждения и backend validation;
- сообщить результат только по authoritative projection.

### 13.2 Forbidden AI Behavior

Ayla AI не может:

- самостоятельно создать, подтвердить, отменить, перенести или завершить запись;
- получить write authority над Appointment, Availability, Payment, Consent или provider state;
- принять решение за мастера или администратора;
- превращать hypothesis, recommendation, inference или summary в business fact;
- расширять customer context за пределы role/purpose/consent;
- читать или показывать semantic memory, если это не разрешено отдельным каноном;
- диагностировать, делать медицинские выводы или скрыто профилировать клиента.

AI output всегда остаётся предложением или presentation layer. Business fact
возникает только после authorized command, authoritative validation и commit.

### 13.3 Ayla CAN / CANNOT

**Ayla CAN:**

- показать разрешённый operational context;
- напомнить о записи по authoritative projection;
- объяснить услугу на основе разрешённых данных;
- подготовить информацию для мастера;
- предложить действие или подготовить command request для явного подтверждения.

**Ayla CANNOT:**

- завершить услугу вместо мастера;
- изменить запись без authorized command и backend/domain validation;
- принимать решения за мастера, администратора или domain owner;
- делать медицинские выводы;
- показывать скрытую информацию, AI memory, inference или данные вне scope.

Главное правило: `AI suggestion != Business action`.
## 14. Privacy Boundary

| Actor | May see | Must not receive through this screen | Authority boundary |
| --- | --- | --- | --- |
| Master | Свой operational day, разрешённые appointment details и minimum customer context | Hidden AI memory, inference, other customers/providers, full conversation context | Не владеет Appointment или provider state |
| Administrator | Разрешённые operational projections и exception context в своей scope | Данные вне role/purpose/consent scope и скрытые AI hypotheses | Может выполнить только authorized admin command |
| Customer | Только собственные customer-facing appointment/communication projections | Данные мастера, других клиентов, internal exceptions и internal notes | Не получает master operational screen projection |
| Ayla AI | Только переданный разрешённый screen context | Semantic memory, hidden context, unauthorized PII, unapproved sensitive data | No write authority; suggestion only |

Доступ регулируется `Consent Scope Registry`, `Data Inventory Matrix`, role
authorization и purpose limitation. Отсутствие доказанного scope трактуется как
запрет.

## 15. Event Relationship

Новые события этим Screen Contract не создаются. Имена и семантика берутся только
из `Ayla Domain Event Registry`.

```text
User Action
  -> Command
  -> Domain validation
  -> Event (only after committed fact)
  -> Projection Update
  -> Screen Refresh
```

- `User Action` — намерение мастера в screen layer.
- `Command` — запрос изменить state, проходящий authorization и validation.
- `Event` — уже произошедший authoritative fact.
- `Projection Update` — read model, обновлённая после committed state/event.
- `Screen Refresh` — получение новой projection; не является event.

View/read actions останавливаются на projection read и не создают domain event.

## 16. Open Questions and Proposed Decisions

| ID | Question | Status | Owner |
| --- | --- | --- | --- |
| UX-MOS-OQ-01 | Полный список клиентов дня или только assigned/authorized scope? | Proposed: minimum operational scope | Product Operations + Privacy |
| UX-MOS-OQ-02 | Разрешённый объём previous visit history | Not included by default | Privacy / Product Owner |
| UX-MOS-OQ-03 | Семантика `StartService` и event | Proposed only; no new event created here | Appointment / Domain Architecture |
| UX-MOS-OQ-04 | Check-in capability — authoritative owner | Not specified | Product Operations + Architecture |
| UX-MOS-OQ-05 | Authoritative producer, evidence, and correction policy after the approved three-hour window | Duration and zero-action rule approved; remaining semantics open | Appointment Owner / Product Owner |
| UX-MOS-OQ-06 | Права мастера на cancel/reschedule и required confirmation | Follow existing Appointment Contract; exact policy pending | Product Operations + Governance |
| UX-MOS-OQ-07 | Operational notes: persistence, retention and visibility | No write assumed until contract exists | Privacy + Architecture |
| UX-MOS-OQ-08 | Exact backend projection/API boundary | Capability requirement only in this document | Backend Architecture |
| UX-MOS-OQ-09 | Canonical path of `Ayla MVP User Journey Specification` | Existing file found under `01 Product/User Journeys/`; supplied path was absent | Documentation Governance |
| UX-MOS-OQ-10 | Is `Request Change` a command, proposal or admin workflow? | No decision created; source/owner required | Product Operations + Architecture |
| UX-MOS-OQ-11 | Is `MarkNoShow` available to Master and what evidence is required? | Existing event semantics only; permission pending | Appointment Owner / Product Operations |

Open Question не является разрешением реализовать функцию. До owner decision
соответствующее действие должно быть скрыто, disabled с объяснением или заменено
эскалацией.

### 16A. Post-Visit Presentation Rule

The scheduled_end to scheduled_end + 3 hours interval is normal post-visit
resolution, not ATTENTION/error or a forgotten task. Real authoritative
exceptions, stale results, conflicts, and other issues may still use attention or
Exception State. The screen never computes completed locally.
## 17. Validation Checklist

### Architecture

- [x] Screen Contract не стал доменной моделью.
- [x] `Screen State != Domain State` зафиксировано.
- [x] Projection не объявлена Source of Truth.
- [x] Appointment ownership сохранён за Appointment Domain.
- [x] Domain Event Registry остаётся единственным источником event names/semantics.
- [x] Новые domain events и permission policies не созданы.

### UX

- [x] Определён ежедневный рабочий цикл мастера.
- [x] Определены Screen Responsibility Boundary и Information Architecture.
- [x] Для Data Blocks указаны Purpose, Data, Source, Owner и Refresh.
- [x] Для действий указаны Preconditions, Authorization, Command, Result/Event и recovery.
- [x] View Appointment определён как read-only.
- [x] Normal, Empty Day, Offline, Changed Appointment и Exception State описаны.
- [x] UI layout, colors, sizes и component implementation не описываются.

### AI

- [x] AI не получил WRITE authority.
- [x] `AI suggestion != Business action` зафиксировано.
- [x] AI ограничен разрешённой projection и purpose-limited context.
- [x] AI не завершает услугу, не меняет запись и не принимает решения.

### Privacy

- [x] Разделены видимость для Master, Administrator, Customer и Ayla AI.
- [x] Данные ограничены ролью, purpose, tenant/provider scope и consent.
- [x] Semantic memory, full conversation context и hidden hypotheses исключены.
- [x] Privacy boundary связан с `Consent Scope Registry` и `Data Inventory Matrix`.

### Governance

- [x] Обязательные Foundation, Architecture, Product и UX-источники изучены.
- [x] Существующие UX MVP, handoff и interaction documents не заменены.
- [x] Existing domain/operations contracts не изменены.
- [x] Не создана API specification и не создан UI mockup.
- [x] Все неопределённости отмечены `Proposed` или `Open question`.


## 17A. Shared System and Recovery UX

Loading, Empty, Offline, Stale, Error, Permission, Pending/Unknown, and Conflict use the shared [[Ayla Master System and Recovery UX Contract]]. This screen keeps its Today-specific execution, attention, and next-action semantics; it does not redefine shared trust or recovery meanings. The normal post-visit resolution window remains a domain/Appointment Detail projection, not a system error.

## 18. Source and Non-Override Rule

Этот документ использует, но не переопределяет:

- `Ayla Knowledge Area Taxonomy` — ответственность UX Screen Contract;
- `Ayla Repository Responsibility Matrix` — repository/domain ownership и AI boundary;
- `Ayla Constitution` — hard constraints и права пользователя;
- `Ayla MVP Appointment Contract` — Appointment lifecycle, ownership и command semantics;
- `Ayla Domain Event Registry` — event names, semantics, producers и consumers;
- `Ayla Domain Context Map` и `Ayla Core Domain Model Specification` — bounded contexts и domain model;
- `Ayla Salon Operations MVP Contract` — Master journey, role boundaries и operational capability chain;
- `Ayla MVP Scope and Release Contract` и `Ayla MVP User Journey Specification` — release/journey scope;
- `Consent Scope Registry` и `Data Inventory Matrix` — privacy, consent and data access.

При конфликте Screen Contract не создаёт вторую истину. Вопрос передаётся
владельцу соответствующей области и фиксируется через governance decision.