---
node_id: ayla.architecture.mvp-appointment-contract
title: Ayla MVP Appointment Contract
type: specification
status: draft
decision_status: proposed
version: "0.2"
owner: Product Architecture
priority: P0
knowledge_area:
  - architecture
domain:
  - booking
concerns:
  - governance
  - audit
  - observability
system_owner:
  - ayla-booking
source_repository: ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
created: 2026-07-29
updated: 2026-08-02
review_cycle: monthly
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Decision Log]]"
  - "[[Ayla Core Domain Model Specification]]"
  - "[[Ayla MVP Scope and Release Contract]]"
  - "[[Ayla Domain Event Registry]]"
related:
  - "[[Ayla MVP Recommendation Contract]]"
  - "[[Ayla MVP User Journey Specification]]"
  - "[[Killer PRD]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Consent Scope Registry]]"
---

# Ayla MVP Appointment Contract

> **Статус:** Draft v0.1 — proposed. Это не канонизация: документ
> определяет доменный контракт Appointment для MVP и подлежит полному
> архитектурному review и owner rulings (прежде всего — по completion
> authority, OQ-A1). Основания: [[Ayla Domain Event Registry]] v0.3
> (§6.3, OQ-E3), [[Ayla MVP Recommendation Contract]] v0.3 (§18, §22),
> [[Ayla MVP User Journey Specification]] v1.1 (этапы 10–14),
> [[Ayla Core Domain Model Specification]] (§7.10–§7.12, Appointment
> Revision, Reschedule Proposal), [[Ayla MVP Scope and Release Contract]]
> (§6), [[Killer PRD]] (§6), AYLA-DEC-0020 (Offering/Membership),
> AYLA-DEC-0021 (Availability and Slot Model), AYLA-DEC-0022 (Reschedule
> and Replacement Model), AYLA-DEC-0025 (event rules).
>
> Документ **не** изменяет Domain Event Registry, **не** изменяет Journey
> Specification и Recommendation Contract, **не** регистрирует новые
> события (§14 — только кандидаты), **не** закрывает OQ-E3 реестра и
> **не** снимает `semantic_status: incomplete` с `appointment.completed`
> до owner ruling по OQ-A1. `appointment_completed` остаётся candidate
> qualified action в Recommendation Contract v0.3 §18 до принятия этого
> контракта.

## 1. Purpose and Scope

Документ отвечает на вопросы:

- Что является Appointment aggregate и где его authoritative System of
  Record?
- Что означают `appointment.created`, `appointment.confirmed`,
  `appointment.completed` — и чем локальное создание отличается от
  внешнего подтверждения?
- Кто имеет право объявить каждый доменный факт, в первую очередь —
  completion?
- Как моделируются cancellation, rejection, no-show?
- Исправим ли ошибочный terminal state и как?
- Как Appointment связан с Booking Flow, Recommendation и Attribution?
- Какие события — domain, integration, technical?

В scope: жизненный цикл записи MVP primary-booking journey (этапы 10–14
[[Ayla MVP User Journey Specification]]), синхронизация с внешним booking
authority, связь со slot hold (AYLA-DEC-0021) и reschedule/replacement
(AYLA-DEC-0022). Вне scope: reschedule-операции как таковые (канон —
AYLA-DEC-0022 и CDM §7.12, здесь только стыки), payment processing
(AYLA-DEC-0015, MVP Monetary Boundary), модель availability
(AYLA-DEC-0021), measurement/attribution policy (Killer PRD §6,
Measurement Framework — planned).

## 2. Terminology

- **Appointment** — authoritative запись о намерении и факте оказания
  услуги конкретному subject у конкретного исполнителя в конкретное
  время; aggregate и SoR статуса записи (CDM §7.12, инвариант 4).
- **Booking Flow** — пользовательский и оркестрационный процесс от
  выбора слота до результата (Journey, этапы 10–12); **не** является
  состоянием Appointment.
- **Booking authority (external)** — внешняя система записи провайдера
  (в MVP — YClients, AYLA-DEC-0021 п. 2), принимающая или отклоняющая
  запись и являющаяся primary календарём в режиме `external_primary`
  (AYLA-DEC-0022 п. 8).
- **Slot Hold** — временное удержание интервала (lifecycle
  `held → confirmed | expired | released`, TTL 15 минут — платформенный
  параметр, AYLA-DEC-0021 п. 3); предшественник Appointment, не часть
  его state model.
- **Completion** — доменный факт «услуга оказана»; требует authoritative
  источника (§9).
- **No-show** — доменный факт неявки одной из сторон при действующей
  `confirmed` записи (§10).
- **Lineage** — цепочка reschedule/replacement через `reschedule_of` и
  `root_appointment_id` (AYLA-DEC-0022 п. 3).
- **Appointment Revision** — иммутабельная версия изменения Appointment
  (CDM §7.12, AYLA-DEC-0022 п. 1).

**Разграничение состояний (нормативное):** не смешиваются —

1. **appointment state** — статус aggregate (§4);
2. **booking command state** — результат операции/команды (success,
   failed, timeout); `failed` — **не** состояние Appointment;
3. **integration synchronization state** — `sync_status` внешней
   синхронизации (например `uncertain`, `stale`, `quarantined`,
   AYLA-DEC-0021 п. 7);
4. **payment state** — вне этого контракта (AYLA-DEC-0015);
5. **attendance state** — фактическая явка/оказание; отражается в
   appointment state только через authoritative completion или
   no-show, не напрямую.

## 3. Aggregate and Ownership

**Appointment — aggregate и единственный SoR статуса записи** (CDM
§7.12, инвариант 4). System of Record: Appointment → Appointment
Management, CAP-011 (AYLA-DEC-0021 п. 2); физически — Backend API
(beautygo_backend) как SoR для записей
([[Ayla MVP Scope and Release Contract]] §6). Внешняя запись YClients —
внешняя система, не SoR статуса Ayla Appointment.

Состав aggregate (факт — CDM §7.12, выборочно): `appointment_id`,
`tenant_id`, `subject_id`, `specialist_assignment_id`,
`service_offering_id`, `price_snapshot`,
`effective_duration_snapshot`, `status`, `scheduled_at`, `created_at`,
`confirmed_at`, `cancelled_at`, `completed_at`, `version` (монотонно),
`reschedule_of`, `root_appointment_id`, `reschedule_count`,
`external_ref` (nullable: system, external_id, source timestamps, sync
metadata), `origin` + условный `recommendation_id` (§13).

Правила ownership (нормативные):

- единственный producer доменных событий `appointment.*` — CAP-011
  (AYLA-DEC-0022 п. 9; DER v0.3 §8);
- LLM/AI Runtime **не** объявляет запись созданной без backend result
  (CDM §7.12, инвариант 5; KM-IM-1: AI Runtime не SoR для Appointment
  и completed action);
- UI, Notification, Analytics, Recommendation и LLM provider не
  создают authoritative `appointment_id` и не изменяют статус;
- история изменений — иммутабельные Appointment Revision; запись не
  переписывается при изменении прайса и исторических данных
  (AYLA-DEC-0020 п. 8).

## 4. State Model

Канонический lifecycle (факт — CDM §7.12, AYLA-DEC-0022 п. 1):

```text
requested → pending_confirmation → confirmed → completed
    ↘ rejected          ↘ expired       ↘ cancelled / no_show
```

Соответствие рабочей модели ревью (справочно, не второй канон):
`requested` ≈ «pending», `pending_confirmation` ≈
«awaiting_external_confirmation».

Нормативные правила:

- **стартовое состояние** при `appointment.created` — `requested`
  (CDM). *Расхождение источников:* DER v0.3 §6.3 называет стартовое
  состояние `pending` — терминологический gap, OQ-A4;
- `requested → rejected` — отказ до передачи/принятия (например,
  валидация, политика); `requested → expired` — истечение ожидания без
  подтверждения (см. technical candidate `pending_appointment.expired`,
  §14);
- `no_show` — **только** из действующей `confirmed` (AYLA-DEC-0022
  п. 9);
- terminal states: `completed`, `cancelled`, `rejected`, `expired`,
  `no_show`; reschedule/replacement из terminal state запрещены
  (AYLA-DEC-0022 п. 2);
- **reschedule — не статус**, а версионируемая операция (same-ID
  Revision или replacement, AYLA-DEC-0022 п. 1–3); статус
  `rescheduled` не вводится;
- `failed` **не вводится** как состояние Appointment: сбой команды или
  интеграции — booking command state / integration sync state (§2);
  timeout внешнего подтверждения сам по себе не переводит Appointment
  в `cancelled` (§6).

## 5. Create Semantics

`appointment.created` (DER v0.3 §6.3, proposed) — **успешное создание
authoritative Appointment aggregate в локальном SoR** со стартовым
состоянием. Разделение фактов (нормативное):

```text
request submitted ≠ aggregate persisted ≠ external booking accepted
≠ appointment confirmed
```

- создание выполняется **одной транзакцией** с подтверждением hold
  (факт — AYLA-DEC-0021 п. 3): блокировать hold → проверить статус и
  серверный TTL → повторно проверить актуальные Rule/Block/external
  busy → создать Appointment → перевести hold в `confirmed` →
  зафиксировать идемпотентный результат;
- истёкший hold не подтверждается; нарушение занятости → `SLOT_TAKEN`
  (это ошибка команды, не состояние Appointment);
- `appointment.created` **не означает** принятие записи внешним booking
  authority и не означает подтверждение (DER v0.3 §6.3);
- Create Appointment идемпотентен (CDM §7.12, инвариант 3); ключ
  идемпотентности события — `appointment_id` (DER);
- защита от двойной записи — DB-enforced по интервалам (exclusion
  constraint / Time Reservation ledger, AYLA-DEC-0021 п. 4);
- overlap-защита и запрет подтверждения на занятый интервал (CDM §7.12,
  инварианты 1–2).

## 6. External Authority Synchronization

MVP работает в calendar mode `external_primary` (факт — AYLA-DEC-0022
п. 8; несинхронизированный dual-source запрещён, AYLA-DEC-0021 п. 7):

- внешний booking authority (YClients) — primary календарь; локальная
  проекция external busy — Schedule Block с `source`, `external_ref`,
  `source_updated_at`, `observed_at`, `sync_status` и идемпотентным
  обновлением (дубли от повторных webhook запрещены);
- конфликт версий — **в пользу подтверждённой внешней версии**; stale
  синхронизация → degraded mode;
- freshness сверх лимита → Ayla не подтверждает автоматически либо
  требует синхронной проверки внешней системы; если проверка
  невозможна — отдельный временный reason code (**не** `SLOT_TAKEN`);
  точный SLA — в integration contract (AYLA-DEC-0021 п. 7);
- неизвестный `staff_id` — quarantined + уведомление.

**Нормативно:** рассинхронизация — это **integration synchronization
state**, а не appointment state (§2). External confirmation timeout не
означает автоматически `appointment.cancelled`; допустимое состояние
проекции — `sync_status = uncertain`, требующее reconciliation job и
мониторинга расхождений (AYLA-DEC-0021 п. 7). Внешние изменения
нормализуются по матрице операций AYLA-DEC-0022 п. 2 (время-only →
same-ID Revision с `actor = external_system`; Offering/цена/
длительность/consent/payment → replacement); запись внешних изменений
как Revision без разбора запрещена (AYLA-DEC-0022 п. 8).

## 7. Confirmation

`appointment.confirmed` (DER v0.3 §6.3, proposed) — booking authority
подтвердил переход в authoritative `confirmed` state (полная UJS,
Stage 5). Нормативно:

- user-facing confirmation показывается **только после** этого факта
  (полная UJS, Stage 5 Success Criteria: «Ayla подтвердила только
  фактически достигнутое состояние»; Journey v1.1, этап 12);
- payload: `appointment_id` + опционально `confirmed_by`,
  `recommendation_id` (DER); бизнес-время `confirmed_at` хранится в
  aggregate (CDM);
- provider eligibility проверяется до подтверждения (CDM §7.12,
  инвариант 9);
- подтверждение — не completion: между `confirmed` и `completed`
  находятся attendance, cancellation и no-show (§9, §10).

## 8. Cancellation and Rejection

`appointment.cancelled` (DER v0.3 §6.3, proposed) — запись отменена;
история не удаляется (CAP-011 invariant). Нормативно:

- cancellation имеет **actor и reason** (CDM §7.12, инвариант 7);
  payload: `cancelled_by`, `cancellation_reason_ref` (DER);
- допустимые выходы в cancellation: из `requested`,
  `pending_confirmation`, `confirmed` (§4); при replacement старая
  запись → `cancelled` с `cancellation_reason =
  replaced_by_reschedule` (AYLA-DEC-0022 п. 3);
- отмена не удаляет ранее выданные или сохранённые attribution
  evidence; downstream-обработка отмены — Recommendation/Attribution
  правила (Killer PRD §6.3 «Отмена записи», DER v0.3 §6.3);
- отмена после подтверждения — тот же доменный факт
  `appointment.cancelled` с соответствующими actor/reason; refund и
  поздняя отмена — вне этого контракта (payment boundary,
  AYLA-DEC-0015; late-window правила — AYLA-DEC-0022 п. 5).

**Rejection** — отказ booking authority принять запись (или
policy-отказ до передачи): выход `requested | pending_confirmation →
rejected`. Событие `appointment.rejected` — candidate (§14), CDM §11
перечисляет `AppointmentRejected`; детальная семантика (источник
отказа, reason codes, отличие от cancellation пользователем) — OQ-A5.
Rejection не является cancellation: cancelled предполагает ранее
существовавшее обязательство, rejected — отказ на входе.

## 9. Completion

Самая значимая часть контракта. `appointment.completed` (DER v0.3 §6.3,
`semantic_status: incomplete`, OQ-E3) — **услуга подтверждённо
оказана** (authoritative completion).

### 9.1 Варианты authoritative completion source

| Вариант | Источник | Плюсы | Минусы |
|---|---|---|---|
| A — специалист/салон | Явная отметка исполнителя | Простой MVP; соответствует операционному процессу | Ошибки; недобросовестная отметка; нужен dispute/correction flow (§11) |
| B — booking authority | Внешняя система объявляет completion | Единый источник | Внешняя система может не иметь такого статуса; семантика провайдера ≠ семантика Ayla |
| C — projection Ayla | `confirmed` + время прошло + нет cancellation/no_show | Не требует интеграции | **Недопустим:** отсутствие отмены не доказывает оказание услуги |

### 9.2 Рекомендация для MVP (proposal, до owner ruling OQ-A1)

`appointment.completed` публикуется **только после явного
authoritative подтверждения** выполнения услуги со стороны специалиста,
салона или поддерживаемого booking authority (варианты A/B; выбор и
приоритет — OQ-A1). При этом:

- прохождение scheduled time **не является** доказательством completion
  (нормативный запрет; Journey v1.1, этап 14: «время записи прошло» —
  UX-триггер prompt, не доменный факт);
- наступление времени услуги без authoritative подтверждения может
  создавать только **internal signal** `completion_confirmation_due`
  (technical/observability, не доменное событие, не публикуется вне
  Appointment context; §14);
- `completed_at` заполняется только вместе с completion evidence;
  payload события: `appointment_id` + `completion_evidence_ref` (DER);
- capability внешней системы по completion (есть ли статус вообще) —
  integration discovery, OQ-A6.

## 10. No-show

Нормативное различение (обязательно, не опционально):

- **`customer_no_show`** — клиент не явился на действующую `confirmed`
  запись;
- **`provider_no_show`** — исполнитель/салон не принял клиента.

Стороны имеют разные ответственность, refund-последствия, метрики,
Product Thesis interpretation и возможность повторной записи — сводить
их в одно значение без `party` запрещено.

Правила:

- `no_show` — только из действующей `confirmed` (AYLA-DEC-0022 п. 9);
- кандидат события `appointment.no_show` с обязательным payload
  (proposal): `party: customer | provider`, `declared_by`,
  `declared_at`, `evidence_refs`;
- регистрация события — **после owner decision** (OQ-A2); до этого
  статус в state model существует (CDM), canonical event — нет;
- provider_no_show как повод к substitute/re-offer — reschedule-контур
  (AYLA-DEC-0022 п. 4, Reschedule Proposal), не этот контракт.

## 11. Corrections and Disputes

Принцип (нормативный): **доменный факт не удаляется и не
переписывается**; ошибочная фиксация исправляется отдельным
compensating event и новой projection — с audit trail (CDM §7.12,
инвариант 10).

- простой переход `completed → confirmed` как обычная мутация **без
  audit trail запрещён**;
- кандидаты compensating events (proposal, **не регистрировать** до
  решения, кто и по каким основаниям выполняет correction — OQ-A3):
  `appointment.completion_corrected`, `appointment.status_corrected`;
- correction event должен ссылаться на исправляемый факт
  (`corrects_event_id` / `corrects_state`), actor, reason и evidence;
  исходный факт остаётся в истории;
- dispute (клиент оспаривает completion/no-show или исполнитель —
  отмену) — отдельный flow с человеческим разбором **(proposal)**;
  автоматическое опровержение authoritative completion по одностороннему
  сигналу не допускается;
- последствия correction для attribution и thesis-метрик — Measurement
  Framework; исторические attribution facts не переписываются (RC v0.3
  §18–§19, prospective-only правила).

## 12. Idempotency and Concurrency

Факты и нормативные требования:

- Create Appointment идемпотентен; повторный confirm hold идемпотентен
  (CDM §7.12 инв. 3; AYLA-DEC-0021 п. 3);
- подтверждение hold — одна транзакция с блокировкой и повторной
  проверкой Rule/Block/external busy (AYLA-DEC-0021 п. 3);
- reschedule acceptance — атомарная 7-шаговая транзакция с
  `expected_version` и повторной проверкой freshness; при любом отказе
  старая запись и reservation без изменений (AYLA-DEC-0022 п. 4, п. 10);
- двойная запись исключается DB-enforced exclusion constraint по
  `tstzrange` либо единым Time Reservation ledger с общей locking
  boundary (AYLA-DEC-0021 п. 4);
- webhook-события внешней системы идемпотентны; дубли запрещены
  (AYLA-DEC-0021 п. 2);
- consumers доменных событий идемпотентны (at-least-once delivery —
  DER v0.3 §10); ordering — только в пределах `appointment_id`.

## 13. Recommendation and Attribution Links

Нормативно:

- Appointment принимает **опциональные** ссылки
  `source_recommendation_id`, `source_recommendation_set_id` (и
  `recommendation_id` в payload событий, DER §6.3). **Не каждая запись
  создаётся из Recommendation:** ручная запись, повторная запись,
  внешний импорт, действие администратора, прямой booking — Appointment
  **не зависит** от существования Recommendation;
- `origin` (CDM §7.12, enum 7 значений) фиксирует фактическое
  происхождение; `recommendation_id` обязателен iff
  `origin = ai_recommendation` (CDM §7.12, инвариант 8);
- **Appointment не объявляет себя результатом Recommendation** —
  атрибуция выполняется отдельным Attribution / Measurement context
  через `qualified_action.attributed` (DER v0.3 §6.6; RC v0.3 §15,
  §18); типизированные action types — `appointment_created`,
  `appointment_confirmed` (transaction, qualified),
  `appointment_completed` (**candidate outcome до принятия этого
  контракта**, RC v0.3 §18);
- lineage и attribution: при переносе той же услуги attribution
  продолжается по lineage; при другой услуге `recommendation_id`
  наследуется только после проверки исполнения той же Recommendation;
  Attribution Link не переписывается (AYLA-DEC-0022 п. 7); при
  replacement, не исполняющем исходную Recommendation, новая запись
  `recommendation_id` не получает (CDM §7.12);
- после начала booking flow ownership availability/price — у Booking/
  Appointment context; истечение Recommendation не отменяет начатый
  flow; invalidated Recommendation блокирует действие (owner ruling
  OQ-R6, RC v0.3 §22) — настоящий контракт реализует соответствующую
  повторную валидацию при create/confirm (§5).

## 14. Event Candidates

Этот документ **не изменяет** Domain Event Registry напрямую; для
большинства перечисленных событий регистрация остаётся отдельным change
set после review и owner rulings. Исключение — `appointment.rescheduled`:
уже зарегистрирован в DER v0.4 по AYLA-DEC-0022 п. 9 (accepted); этот
контракт лишь фиксирует ссылку на уже состоявшуюся регистрацию, не
дублирует и не заменяет её. Текущее состояние (registered/candidate) по
каждому событию:

| Event | Статус в DER | Позиция контракта |
|---|---|---|
| `appointment.created` | proposed, defined | Семантика подтверждена (§5); стартовое состояние — OQ-A4 |
| `appointment.confirmed` | proposed, defined | Семантика подтверждена (§7) |
| `appointment.completed` | proposed, **incomplete** (OQ-E3) | Остаётся incomplete до owner ruling OQ-A1 (§9) |
| `appointment.cancelled` | proposed, defined | Семантика подтверждена (§8) |
| `appointment.rejected` | candidate | Предлагается к определению (§8) — OQ-A5 |
| `appointment.rescheduled` | **registered (DER v0.4)** | Семантика — AYLA-DEC-0022 п. 9 (same-ID); зарегистрировано (Domain Event Registry §6.3, `registration_status: registered`); Wave 1 Simple Reschedule — owner decision (Decision Log, AYLA-DEC-0022, accepted 2026-07-28) |
| `appointment.no_show` | candidate | Предлагается с обязательным `party` (§10) — после OQ-A2 |
| `appointment.completion_corrected` / `appointment.status_corrected` | нет | Не регистрировать до OQ-A3 (§11) |
| `pending_appointment.expired` | technical candidate | Technical signal для `requested/pending_confirmation → expired`; доменным фактом не является **(proposal)** |
| `completion_confirmation_due` | нет | Internal signal (§9.2); **не** доменное событие, за пределы Appointment context не публикуется **(proposal)** |

Publication scope существующих записей — `cross_repository` (DER §6.3:
v0.3 для proposed-записей, v0.4 для зарегистрированного
`appointment.rescheduled`): Appointment — интеграционная граница с
Backend/YClients-контуром.

### 14.1 Legacy Schema Compatibility (temporary, non-canonical)

Для Wave 1 Simple Reschedule runtime/legacy интеграция (YClients-контур,
`ai-bot-platform-booking`) местами всё ещё использует плоские поля,
предшествующие Offering/Assignment модели (AYLA-DEC-0020). Временное
соответствие для чтения legacy-полей при интеграции — **не переопределяет
CDM и не вводит новые SoR-атрибуты**:

| Legacy поле | Приблизительное соответствие в каноне |
|---|---|
| `service_id` (плоский, до Offering/Assignment split) | ≈ Service Offering ref (`offering_id`) — не Catalog Service `service_id` (CDM §7.9 / §12) |
| `(specialist_id, service_id)` | ≈ Specialist Offering Assignment ref (`specialist_offering_assignment_id`, CDM §7.9) |

Это соответствие — **не канон**: оно не отменяет запрет `specialist_id`
как SoR-атрибута Appointment (AYLA-DEC-0020 п. 8, CDM §21 инв. 11) и не
переопределяет `service_id` Catalog Service (CDM §7.9). Оно существует
только как temporary мостик для чтения legacy runtime payload при
Simple Reschedule до миграции интеграции на канонические
`offering_id`/`specialist_offering_assignment_id`. Мостик подлежит
удалению при закрытии миграции; canonical write commands обязаны
использовать `specialist_offering_assignment_id` (AYLA-DEC-0022 п. 9,
`appointment.rescheduled` payload).

## 15. Privacy and Audit

- payload событий — псевдонимизированные идентификаторы
  (`pseudonymous_identifiers_only`), sensitive значения не включаются
  (DER v0.3 §4 п. 3; наследует CSR §9.1);
- side effects имеют audit trail (CDM §7.12, инвариант 10); cancellation
  — с actor и reason (инвариант 7); correction — со ссылкой на
  исправляемый факт (§11);
- внешние изменения фиксируются с `actor = external_system` и
  `external_ref` (AYLA-DEC-0022 п. 8);
- retention event log и audit — OQ-E5 реестра (вне этого контракта);
- appointment history не удаляется при cancellation (CAP-011);
  удаление по privacy request — через deletion pipeline и retention
  policy (AMD-001 C5 / CSR), не через доменные события этого контракта.

## 16. Open Questions

- **OQ-A1 (главный owner decision).** Authoritative completion source:
  вариант A (специалист/салон), B (booking authority) или их
  сочетание с приоритетом? Рекомендация §9.2: A и/или B, явное
  подтверждение обязательно; вариант C (projection по времени)
  отклонён. До ruling `appointment.completed` остаётся
  `semantic_status: incomplete` (OQ-E3 реестра не закрывается).
- **OQ-A2.** Регистрировать ли `appointment.no_show` как canonical
  event в MVP и с каким обязательным payload (предложение §10)?
- **OQ-A3.** Кто и по каким основаниям выполняет correction;
  регистрировать ли `appointment.completion_corrected` /
  `appointment.status_corrected` (§11)?
- **OQ-A4.** Терминологический gap: CDM §7.12 — стартовое состояние
  `requested`, DER v0.3 §6.3 — `pending`. Требуется выравнивание при
  ближайшем change set реестра (предложение: канон CDM — `requested`).
- **OQ-A5.** Семантика `appointment.rejected`: источники отказа,
  reason codes, граница с cancellation (§8).
- **OQ-A6.** Имеет ли внешний booking authority (YClients) completion
  статус и какова его семантика — integration discovery перед owner
  ruling OQ-A1 (вариант B).
- **OQ-A7.** Критерии `requested | pending_confirmation → expired`:
  таймауты ожидания внешнего подтверждения, связь с
  `pending_appointment.expired` (technical) и sync `uncertain` (§4, §6).

## 17. Acceptance Criteria

- [ ] Документ создан в `05 Architecture`, version 0.1, draft / proposed.
- [ ] Appointment aggregate и SoR определены (CAP-011, CDM §7.12).
- [ ] State model соответствует CDM; `failed` и `rescheduled` не
      введены как состояния.
- [ ] `appointment.created` отделён от external acceptance и
      confirmation.
- [ ] Completion требует authoritative источника; прохождение времени
      не является completion.
- [ ] No-show различает `customer` / `provider` с обязательным `party`.
- [ ] Correction — compensating event, не мутация; `completed →
      confirmed` без audit trail запрещён.
- [ ] Рассинхронизация с booking authority — integration state, не
      appointment state; timeout ≠ cancelled.
- [ ] Связь с Recommendation — опциональные ссылки; Appointment не
      объявляет себя результатом Recommendation.
- [ ] События раздела 14 — кандидаты, кроме `appointment.rescheduled`
      (зарегистрирован отдельным решением, AYLA-DEC-0022 п. 9, DER v0.4);
      Domain Event Registry этим документом не изменён.
- [ ] OQ-E3 не закрыт; `appointment.completed` не объявлен fully
      defined; `appointment_completed` остаётся candidate thesis action
      в Recommendation Contract.
- [ ] Journey Spec, Recommendation Contract, memory.* не затронуты.
- [ ] Validator = 0 errors (по этому файлу).

## 18. Change Log

### v0.2 (2026-08-02) — Wave 1 Simple Reschedule canon alignment

- **§14:** статус `appointment.rescheduled` обновлён на **registered**
  (Domain Event Registry v0.4, `registration_status: registered`) —
  регистрация нормативно предписана AYLA-DEC-0022 п. 9 (accepted
  2026-07-28); добавлен §14.1 Legacy Schema Compatibility (temporary,
  non-canonical) — мэппинг legacy runtime-полей `service_id` и
  `(specialist_id, service_id)` на Offering/Assignment ref для
  YClients-контура и `ai-bot-platform-booking`; мэппинг не переопределяет
  AYLA-DEC-0020 и подлежит удалению при закрытии миграции интеграции.
- **§14 intro, §17:** уточнено, что `appointment.rescheduled` —
  единственное исключение из общего правила «события раздела —
  кандидаты»; убрана ссылка на служебный prompt-файл в позиции
  контракта, заменена на каноническую атрибуцию (Decision Log,
  AYLA-DEC-0022).
- `status`/`decision_status` не менялись — изменение point-in-scope,
  без отдельного owner decision сверх уже принятого AYLA-DEC-0022.

### v0.1 (2026-07-29) — Initial draft

- Документ создан по owner direction после закрытия цепочки
  Recommendation Contract v0.3 → Domain Event Registry v0.3 →
  MVP User Journey v1.1: Appointment aggregate и SoR (CAP-011),
  state model по CDM §7.12 (AYLA-DEC-0020/0021/0022), create /
  confirmation / cancellation semantics по DER v0.3 §6.3.
- Completion: три варианта authoritative source, рекомендация MVP —
  явное подтверждение (специалист/салон или booking authority);
  прохождение времени — только internal signal
  `completion_confirmation_due`; вариант C (projection) отклонён;
  OQ-A1 — главный owner decision.
- No-show с обязательным `party` (customer | provider); corrections —
  compensating events без переписывания фактов; external
  synchronization как отдельный integration state (timeout ≠
  cancelled).
- Связь с Recommendation/Attribution: опциональные
  `source_recommendation_id` / `source_recommendation_set_id`;
  attribution — отдельный контекст; `appointment_completed` остаётся
  candidate outcome.
- События предложены как кандидаты без изменения Domain Event
  Registry; OQ-E3 не закрыт; Open Questions OQ-A1..A7. Статус:
  draft / proposed.
