---
node_id: ayla.architecture.domain-event-registry
title: Ayla Domain Event Registry
type: specification
status: draft
decision_status: accepted
version: "0.1"
owner: Architecture / Event Governance
priority: P0
knowledge_area:
  - architecture
domain:
  - cross-domain
concerns:
  - observability
  - governance
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
created: 2026-07-28
updated: 2026-07-28
review_cycle: monthly
depends_on:
  - "[[Ayla Decision Log]]"
  - "[[Ayla MVP Documentation Roadmap]]"
  - "[[Ayla Core Domain Model Specification]]"
related:
  - "[[Ayla Intent Model Specification]]"
  - "[[Consent Scope Registry]]"
  - "[[Killer PRD]]"
---

# Ayla Domain Event Registry

> **Статус документа: draft (v0.1).** Формат реестра, конвенция имён,
> классификация, ownership, envelope и правила версионирования приняты
> решением **AYLA-DEC-0025** ([[Ayla Decision Log]]) и являются
> нормативными. Содержимое Event Catalog (§7) — **не канонизировано**:
> каждое событие имеет честный `semantics_status` (`confirmed` /
> `pending definition`). Записи `pending definition` не являются
> контрактами и не могут использоваться как основание для реализации.

## 1. Purpose and Authority

Этот реестр — **единственный canonical источник имён и контрактов
событий** платформы Ayla (AYLA-DEC-0025 п. 1). Любое событие,
публикуемое любым компонентом, регистрируется здесь до использования;
имена и payload schema, не прошедшие через реестр, не являются
контрактом.

Размещение — `05 Architecture`, а не domain models: реестр задаёт
cross-domain и cross-repository контракт.

Governance (AYLA-DEC-0025 п. 1):

- **Architecture / Event Governance** владеет форматом реестра и
  глобальными правилами (этот документ).
- **Bounded context** владеет семантикой своего события (какой факт
  произошёл и что он означает).
- **Authoritative producer** владеет payload schema события.
- **Breaking change** любого события требует cross-repository review
  (см. §6, §9).

Отношение к другим документам: [[Ayla Core Domain Model Specification]]
§11 и [[Consent Scope Registry]] §9 перечисляют события своих доменов;
при расхождении имён и envelope с этим реестром canonical — данный
реестр (выравнивание этих документов зафиксировано в §10 Open
Questions). Реестр не отменяет ownership Consent Scope Registry над
audit-семантикой consent-домена и Killer PRD — над recommendation/
attribution-семантикой.

## 2. Naming Convention

Единая конвенция имён (AYLA-DEC-0025 п. 2):

- Формат: **lowercase dot-separated past-tense fact** —
  `<domain>.<entity>.<fact>` (или `<entity>.<fact>` для малого домена).
  Примеры: `appointment.created`, `consent.revoked`, `memory.deleted`.
- Событие — **факт в прошедшем времени**, не команда:
  `CompleteAppointment` (команда) ≠ `appointment.completed` (факт).
  Команды в реестр событий не включаются и не именуются по этой
  конвенции.
- **Смешение форм запрещено**: `ConsentGranted`, `consent_granted`,
  `consent.granted` — это не три допустимых варианта, а одна
  каноническая форма (`consent.granted`) плюс legacy aliases (§8).
  Одновременное существование нескольких форм одного факта в новых
  контрактах не допускается.
- Legacy alias — временный compatibility mapping, а не второе
  полноценное событие (§6, §8).
- Список событий роадмапа ([[Ayla MVP Documentation Roadmap]] §6.4)
  приводится к конвенции через семантический review, а не механическое
  переименование (§7).

## 3. Classification

Две **независимые оси** (не одно взаимоисключающее поле) —
AYLA-DEC-0025 п. 3:

**`semantic_class`:**

- `domain_fact` — произошедший факт доменного lifecycle, на который
  consumers вправе опираться как на основание для действий.
- `technical_signal` — сигнал инфраструктурного/наблюдаемого характера.

**`publication_scope`:**

- `internal` — внутри одного bounded context / сервиса.
- `cross_context` — между bounded contexts одного репозитория.
- `cross_repository` — интеграционный контракт между репозиториями.
- `external` — публикуется внешним потребителям платформы.

Оси комбинируются свободно: бизнес-факт может одновременно быть
интеграционным контрактом (`appointment.completed` = `domain_fact` +
`cross_repository`).

**Правило technical_signal:** technical signals **запрещены** как
основание для доменных действий, изменений состояния и side effects
(`domain_trigger_allowed: false`); **разрешены** для observability —
logs, tracing, metrics, monitoring, debugging, replay diagnostics.
Пример: `intent.detected` (§7) — technical_signal, internal, не
integration contract (KM-IM-1, [[Ayla Intent Model Specification]]).

## 4. Ownership

Правила владения (AYLA-DEC-0025 п. 4):

- **Ровно один authoritative producer** на событие — компонент,
  владеющий фактом: `appointment.*` → Appointment context;
  `consent.*` → Consent Domain; `intent.*` → Intent Resolution owner;
  `memory.*` → Memory Service.
- **Вторичные семантические producer'ы запрещены**: consumer не вправе
  сам решить, что факт произошёл, и опубликовать его от своего имени
  (аналитика не вправе сама решить, что запись завершена).
- **Transport relays** (outbox publisher, broker adapter, integration
  relay, CDC) допустимы, но **не становятся владельцами** события и
  обязаны сохранять без изменений: canonical name, producer identity,
  `event_id`, payload version, `occurred_at`.

## 5. Envelope

Единый envelope всех событий (AYLA-DEC-0025 п. 5). Обязательные поля:

```yaml
event_id:          # уникальный идентификатор события (UUID)
event_name:        # canonical имя по §2 (lowercase dot-separated)
event_version:     # целочисленная major wire-версия payload (см. §6)
occurred_at:       # время, когда факт произошёл (доменное время)
published_at:      # время публикации события
producer:
  service:         # сервис — authoritative producer (§4)
  bounded_context: # bounded context producer'а
  instance_id:     # экземпляр producer'а
subject:
  entity_type:     # тип сущности, к которой относится факт
  entity_id:       # идентификатор сущности
tenant_id:         # tenant scope события
correlation_id:    # сквозная корреляция запроса/потока
causation_id:      # событие/команда — непосредственная причина
idempotency_key:   # ключ идемпотентной обработки consumers
data:              # payload события (schema владеет producer, §4)
metadata:          # технические метаданные (без доменной семантики)
```

Правила payload (по [[Ayla Core Domain Model Specification]] §11):
событие immutable; consumer idempotent; PII classification обязательна
(колонка `pii_class` в §7); событие не содержит лишних sensitive data.

> **Расхождение:** envelope Core Domain Model §11 (`event_type`,
> `aggregate_version`, `schema_version`) отличается от настоящего.
> Canonical — envelope этого раздела; выравнивание — OQ-1 (§10).

## 6. Versioning and Deprecation

Правила (AYLA-DEC-0025 п. 6):

- **Canonical event name стабилен.** Переименование без необходимости
  запрещено.
- **Additive change** (новое необязательное поле payload) — обратно
  совместим; имя и `event_version` прежние.
- **Breaking payload change** — major version (`event_version: 1 → 2`);
  имя может сохраниться. Требует cross-repository review (§1).
- **Изменение семантики факта** — это не версия, а новое событие или
  раздельные факты (`recommendation.dispatched` ≠
  `recommendation.displayed`).
- **Переименование** = новое canonical имя + legacy alias +
  deprecation window. Доменный producer публикует **только canonical**;
  legacy consumers обслуживает compatibility layer.
- **Deprecation window** — период, в течение которого alias
  действует; конкретный срок фиксируется при регистрации alias (§8).
- **Удаление alias** — только после миграции всех зарегистрированных
  consumers этого alias.

## 7. Event Catalog — MVP-срез

Исходный список — [[Ayla MVP Documentation Roadmap]] §6.4 (11
событий), приведённый к конвенции §2 и прошедший семантический review
по AYLA-DEC-0025 п. 8 (какой факт произошёл; кто единственный
producer; в какой точке транзакции возникает; что значит «доставлено»
и «обработано»; какие consumers вправе опираться).

`semantics_status`:

- **confirmed** — семантика подтверждена AYLA-DEC-0025 / связанными
  каноническими документами; пять проверочных ответов приведены.
- **pending definition** — семантика НЕ подтверждена; событие не
  является контрактом до закрытия соответствующего вопроса (§10).

### 7.1 Catalog table

| event_name | semantic_class | publication_scope | authoritative_producer | consumers | payload summary | event_version | pii_class | semantics_status |
|---|---|---|---|---|---|---|---|---|
| `consent.granted` | domain_fact | cross_repository | Consent Domain | Memory Service, User Context, AI platform (retrieval gates), audit | `subject_id`, `scope_id`, `scope_version`, `granted_at`, channel | 1 | pii | confirmed |
| `consent.revoked` | domain_fact | cross_repository | Consent Domain | Memory Service (revocation, 4 слоя DEC-0024 п. 5), User Context, AI platform, audit | `subject_id`, `scope_id`, `revoked_at`, `revocation_event_id` | 1 | pii | confirmed |
| `intent.resolution_produced` | domain_fact | cross_context | Intent Resolution owner | Orchestrator / execution layer, clarification flow, analytics | output contract [[Ayla Intent Model Specification]] § Output Contract; `resolution_status`: resolved / needs_clarification / unresolved / blocked_safety | 1 | low | confirmed |
| `intent.detected` | technical_signal | internal | Intent Resolution owner | Observability only (logs, tracing, metrics) | `intent_id` (pre-resolution), signal metadata; **domain_trigger_allowed: false** | 1 | low | confirmed |
| `appointment.created` | domain_fact | cross_repository | Appointment context | Notification, analytics, recommendation (attribution linkage) | `appointment_id`, `subject_id`, `provider_id`, `service_id`, `slot`, `created_at` | 1 | pii | confirmed |
| `appointment.confirmed` | domain_fact | cross_repository | Appointment context | Notification, analytics, recommendation (qualified_action candidate) | `appointment_id`, `confirmed_at`, confirmation actor | 1 | pii | confirmed |
| `appointment.cancelled` | domain_fact | cross_repository | Appointment context | Notification, analytics, recommendation (`post_recommendation_cancellation`) | `appointment_id`, `cancelled_at`, cancellation actor, reason code | 1 | pii | confirmed |
| `appointment.completed` | domain_fact | cross_repository | Appointment context | Analytics, recommendation (outcome / qualified_action evidence), billing | `appointment_id`, `completed_at`, outcome reference | 1 | pii | confirmed |
| `recommendation.dispatched` | domain_fact (предварительно) | cross_context (предварительно) | Recommendation context (предварительно) | TBD | TBD: факт передачи рекомендации в канал доставки (`recommendation_id`) | — | TBD | **pending definition** |
| `recommendation.displayed` | domain_fact (предварительно) | cross_context (предварительно) | Recommendation context / presentation layer — не решено | TBD | TBD: факт фактического показа пользователю; якорь `recommendation_shown_at` для attribution window ([[Killer PRD]]) | — | TBD | **pending definition** |
| `recommendation.accepted` | domain_fact (предварительно) | cross_context (предварительно) | TBD (producer принятия — не решено) | TBD | TBD: факт принятия рекомендации пользователем; `linkage_type` по Killer PRD | — | TBD | **pending definition** |
| `qualified_action.attributed` | TBD: domain fact vs analytics projection — не решено | TBD | TBD (analytics ≠ вторичный producer факта, §4) | TBD | TBD: `recommendation_id`, `attribution_type`, `attribution_window_registry_version` | — | TBD | **pending definition** |
| `context_fact.corrected` | domain_fact (предварительно) | internal / cross_context — не решено | Memory Service (по DEC-0024 п. 10) | TBD | TBD: `memory_id`, `superseded_by`, `supersession_reason=corrected` (DEC-0024 п. 4) | — | TBD | **pending definition** |

### 7.2 Confirmed events — пять проверочных ответов

**`consent.granted`**

1. Факт: пользователь предоставил согласие на конкретный scope
   ([[Consent Scope Registry]] §7 lifecycle).
2. Producer: Consent Domain — единственный (DEC-0025 п. 7).
3. Точка транзакции: после атомарной фиксации consent record в Consent
   Domain; событие — результат commit, не намерение.
4. Доставлено ≠ обработано: доставка события не означает, что consumers
   применили scope; runtime gates обязаны проверять актуальное consent
   state, а не полагаться на потреблённое событие (DEC-0024 п. 5а).
5. Consumers: Memory Service (write gate `preference_memory`),
   User Context, AI platform retrieval boundary, audit
   ([[Consent Scope Registry]] §9.1, legacy `consent_granted` → §8).

**`consent.revoked`**

1. Факт: пользователь отозвал согласие по scope.
2. Producer: Consent Domain — единственный.
3. Точка транзакции: после фиксации revocation в Consent Domain;
   немедленный runtime effect наступает через read gate независимо от
   доставки события (DEC-0024 п. 5а).
4. Доставлено ≠ обработано: distributed deletion (кэши, индексы,
   derived artifacts — DEC-0024 п. 5в) асинхронен с дедлайном по
   retention manifest; событие фиксирует факт отзыва, не завершение
   удаления.
5. Consumers: Memory Service (deletion pipeline), User Context,
   AI platform, audit (legacy `consent_revoked`, `ConsentRevoked` → §8).

**`intent.resolution_produced`**

1. Факт: завершён resolution pass и создан первый consumer-meaningful
   output (DEC-0025 п. 7; KM-IM-1).
2. Producer: Intent Resolution owner — единственный.
3. Точка транзакции: после первого resolution pass; результат — одно из
   публикуемых состояний `resolution_status` (resolved /
   needs_clarification / unresolved / blocked_safety), достаточное для
   следующего решения consumer. `intent.resolved` как общее событие не
   используется — двусмысленно (DEC-0025 п. 7).
4. Доставлено ≠ обработано: получение output orchestrator'ом не
   означает начало execution; readiness определяется output contract,
   не фактом доставки.
5. Consumers: orchestrator / execution layer, clarification flow,
   analytics (output contract — [[Ayla Intent Model Specification]]
   § Output Contract; legacy `IntentResolved` → §8).

**`intent.detected`**

1. Факт: технический сигнал о внутреннем pre-resolution состоянии
   Intent; **не доменный факт** (KM-IM-1).
2. Producer: Intent Resolution owner.
3. Точка транзакции: внутри resolution pipeline, до первого
   consumer-meaningful output.
4. Доставлено ≠ обработано: неприменимо как trigger —
   `domain_trigger_allowed: false`; запрещён как основание для доменных
   действий, изменений состояния и side effects (§3).
5. Consumers: только observability (logs, tracing, metrics, monitoring,
   debugging, replay diagnostics). Internal scope; не integration
   contract.

**`appointment.created` / `appointment.confirmed` / `appointment.cancelled` / `appointment.completed`**

1. Факты: соответствующие переходы lifecycle записи (создание,
   подтверждение, отмена, завершение).
2. Producer: Appointment context — единственный для всего семейства
   (DEC-0025 п. 4); analytics не вправе сама решить, что запись
   завершена.
3. Точка транзакции: после commit соответствующего state transition в
   Appointment context; событие публикуется из факта перехода, не из
   намерения (команда `CompleteAppointment` ≠ факт
   `appointment.completed`).
4. Доставлено ≠ обработано: доставка в notification/analytics не
   меняет состояние записи; consumers идемпотентны по
   `idempotency_key`. Отмена после атрибуции не удаляет историческое
   событие — фиксируется `post_recommendation_cancellation=true`
   ([[Killer PRD]]).
5. Consumers: notification, analytics, recommendation (attribution
   linkage и outcome evidence). Канон `appointment.*`; `booking.*` —
   legacy, включая payload-адаптер `booking_id` → `appointment_id`
   (§8).

### 7.3 Pending events — явный статус

**`recommendation.dispatched` / `recommendation.displayed` / `recommendation.accepted`** — разложены из roadmap-событий
`RecommendationShown` и `RecommendationAccepted` (DEC-0025 п. 8:
семейство `recommendation.*` требует предварительной дефиниции до
включения). **Показано ≠ доставлено ≠ принято** — три разных факта с
разными producer'ами и точками транзакции. Связь с [[Killer PRD]]:
`recommendation_shown_at` — якорь attribution window; `accepted` —
это `intent_action` по Killer PRD, а не `qualified_action`; Consent
Scope Registry §9.2 упоминает snake_case-варианты
(`recommendation_created/shown/accepted/dismissed`, `booking_linked`)
как informative и прямо отказывается от владения их schema. До
дефиниции семантики (OQ-3) события **не контракты**.

**`qualified_action.attributed`** — НЕ подтверждено. Открытые вопросы
(OQ-4): что такое QualifiedAction как доменный факт (Killer PRD
определяет через `recommendation_id` + `attribution_window` +
`direct/assisted` + single-winner); preliminary vs final attribution
(переклассификация при новых данных?); является ли атрибуция доменным
фактом или analytics projection — если projection, то правило §4
запрещает analytics быть producer'ом доменного факта.

**`context_fact.corrected`** — частично определено, не подтверждено.
Producer — Memory Service (DEC-0024 п. 10: единственный владелец всех
state transitions; correction — атомарная supersession,
`supersession_reason=corrected`, DEC-0024 п. 4). Не решено (OQ-5):
соотношение с семейством `memory.*` (DEC-0025 п. 2/4 приводит
`memory.deleted` как пример канонического имени и Memory Service как
producer `memory.*`); является ли `context_fact.corrected` тем же
фактом, что `memory.entry_superseded` с reason `corrected`, и как
соотносится с audit-событиями Consent Scope Registry §9.1
(`memory_fact_written` / `memory_fact_deleted`).

## 8. Legacy Alias Registry

Compatibility mapping (AYLA-DEC-0025 п. 2, п. 6, п. 7). Доменные
producer'ы публикуют только canonical имена; legacy consumers
обслуживает compatibility layer. Alias удаляется только после миграции
всех зарегистрированных consumers (§6).

| Legacy | Canonical | Вид | Источник расхождения | Статус |
|---|---|---|---|---|
| `ConsentGranted` | `consent.granted` | event name alias | [[Ayla Core Domain Model Specification]] §11 | active alias |
| `ConsentRevoked` | `consent.revoked` | event name alias | Core Domain Model §11 | active alias |
| `consent_granted` | `consent.granted` | event name alias | [[Consent Scope Registry]] §9.1 (snake_case audit events) | active alias |
| `booking.rescheduled` | `appointment.rescheduled` | event name alias | legacy booking-домен; `appointment.rescheduled` не входит в MVP-срез §7 | active alias |
| `booking_id` → `appointment_id` | payload adapter | **payload field adapter, не имя события** | DEC-0025 п. 7 | active alias |
| `IntentResolved` | `intent.resolution_produced` | event name alias | Roadmap §6.4, Core Domain Model §11 | active alias |

Примечание: snake_case-события Consent Scope Registry §9.1
(`consent_denied`, `consent_expired`, `authorization_scope_checked` и
др.) — полный canonical список audit-событий consent-домена; их
приведение к dot-separated конвенции и регистрация в §7 — отдельный
расширительный review (OQ-2), в MVP-срез не входит.

## 9. Rules for New Events

Процесс добавления и изменения событий:

1. **Регистрация до использования.** Новое событие сначала вносится в
   §7 со всеми обязательными полями каталога, затем реализуется.
2. **Семантический review обязателен.** Пять проверочных вопросов §7
   (факт, единственный producer, точка транзакции, доставлено vs
   обработано, consumers) отвечаются до получения
   `semantics_status: confirmed`. Механическое переименование без
   review запрещено (DEC-0025 п. 8).
3. **Ownership согласуется по §4:** один authoritative producer;
   проверка, что событие не дублирует факт существующего (One
   Canonical Meaning, Core Domain Model §3.10).
4. **Изменение существующего события** идёт по §6: additive — через
   producer + уведомление Event Governance; breaking — major version +
   cross-repository review; смена семантики — новое событие.
5. **Approval flow:** изменения реестра (форма) — Architecture /
   Event Governance; семантика события — owning bounded context;
   payload schema — authoritative producer. Статус документа при этом
   остаётся предметом стандартного lifecycle схемы знаний.
6. **PII classification** обязательна для каждого события (Core Domain
   Model §11, правило 5).

## 10. Open Questions

- **OQ-1. Envelope Core Domain Model §11 vs §5.** CDM §11 фиксирует
  другой envelope (`event_type`, `aggregate_id`, `aggregate_version`,
  `schema_version`) и PascalCase-имена. Canonical — этот реестр;
  требуется amendment CDM §11. Owner: Architecture / Event Governance.
- **OQ-2. Приведение audit-событий Consent Scope Registry §9.1.**
  Snake_case список (16 событий) — canonical для своего домена, но
  нарушает §2. Нужен маппинг на dot-separated имена и включение
  расширенного consent-набора (`consent.denied`, `consent.expired`, …)
  в каталог отдельным review, с сохранением ownership Consent Scope
  Registry над audit-семантикой.
- **OQ-3. Семантика `recommendation.*`.** Определить факты и
  producer'ов для `dispatched` / `displayed` / `accepted`: кто владеет
  фактом показа (Recommendation context или presentation layer), что
  является точкой транзакции для `recommendation_shown_at` (якорь
  attribution window, [[Killer PRD]]), соотношение с informative
  snake_case-событиями Consent Scope Registry §9.2. До закрытия —
  все три события `pending definition`.
- **OQ-4. `qualified_action.attributed`.** Не решено: (а) QualifiedAction
  как доменный факт vs analytics projection — §4 запрещает analytics
  быть producer'ом доменного факта; (б) preliminary vs final
  attribution и возможность переклассификации (Killer PRD: historical
  события не переклассифицируются при смене Attribution Window
  Registry, но допустима ли коррекция при новых linkage-данных?);
  (в) producer и publication_scope. Источник семантики — [[Killer PRD]]
  (qualified action, attribution window, single-winner), но событие
  атрибуции там не определено как доменный контракт.
- **OQ-5. `context_fact.corrected` vs семейство `memory.*`.**
  DEC-0024 определяет correction как supersession (`supersession_reason=
  corrected`, producer Memory Service), DEC-0025 использует
  `memory.deleted` как пример canonical имени. Нужно единое семейство
  `memory.*` (created / superseded / expired / deleted) и решение,
  является ли `context_fact.corrected` alias на
  `memory.entry_superseded{reason=corrected}` или отдельным событием;
  увязка с audit-событиями Consent Scope Registry §9.1
  (`memory_fact_*`).
- **OQ-6. `appointment.rescheduled` в MVP-срезе.** Alias
  `booking.rescheduled` зарегистрирован (§8), но canonical
  `appointment.rescheduled` отсутствует в §6.4 роадмапа и §7. Добавить
  в каталог или подтвердить post-MVP — отдельное решение.

## 11. Change Log

### v0.1 — 2026-07-28

- Initial draft по AYLA-DEC-0025: назначение и governance (§1),
  конвенция имён (§2), две оси классификации (§3), ownership (§4),
  единый envelope (§5), versioning/deprecation (§6).
- Event Catalog (§7): 13 записей из 11 событий роадмапа §6.4 —
  8 confirmed (`consent.granted`, `consent.revoked`,
  `intent.resolution_produced`, `intent.detected`, `appointment.created`,
  `appointment.confirmed`, `appointment.cancelled`,
  `appointment.completed`), 5 pending definition
  (`recommendation.dispatched`, `recommendation.displayed`,
  `recommendation.accepted`, `qualified_action.attributed`,
  `context_fact.corrected`).
- Legacy Alias Registry (§8): 6 mapping'ов, включая payload-адаптер
  `booking_id` → `appointment_id`.
- Rules for New Events (§9), Open Questions OQ-1…OQ-6 (§10).
