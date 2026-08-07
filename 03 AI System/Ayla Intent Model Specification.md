---
node_id: ayla.ai.intent-model
title: Ayla Intent Model Specification
type: ai-specification
status: draft
decision_status: proposed
canonical_status: candidate
version: "1.0"
owner: AI Architecture
priority: P0
knowledge_area:
  - ai-system
domain:
  - intent
concerns:
  - safety
  - explainability
system_owner:
  - ayla-ai-core
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
updated: 2026-08-05
review_cycle: monthly
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Product Essence]]"
  - "[[Ayla Product Vision]]"
  - "[[Ayla MVP Product Thesis]]"
  - "[[Ayla Product Principles]]"
  - "[[Ayla MVP Scope and Release Contract]]"
  - "[[Ayla Decision Log]]"
related:
  - "[[Ayla MVP User Journey Specification]]"
  - "[[Consent Scope Registry]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Killer PRD]]"
---

# Ayla Intent Model Specification

> **Статус:** Draft v1.0 / proposed / canonical candidate — structured
> revision в Two-Phase Pilot Scope Reconciliation Window. Документ приведён
> к текущей продуктовой основе: [[Ayla Product Essence]] v1.1,
> [[Ayla Product Vision]] v2.0, [[Ayla MVP Product Thesis]] v0.5,
> [[Ayla Product Principles]] v0.1, [[Ayla MVP Scope and Release Contract]]
> v0.3 и [[Ayla MVP User Journey Specification]] v1.1. Редакция не наследует
> approval v0.9.2 автоматически и ожидает review и Product Owner approval.
> Runtime Intent Resolution Output Contract сохраняет `contract_version:
> "0.5"`; его поля и machine-readable appendix этой ревизией не меняются.
>
> **Соглашение о пометках.** Положения, прямо подтверждённые источниками,
> помечены «Факт — <источник>». Положения, впервые предложенные этим
> документом, помечены «Proposal»; с момента approval они действуют как
> нормы MVP-среза, а их изменение подчиняется change control.

## Purpose

Документ предлагает нормативную MVP-модель intent для review и
последующей канонизации: как текущее намерение пользователя связано с
принадлежащей пользователю Transformation Goal, как
оно распознаётся и проходит lifecycle, как из него формируется
recommendation intent и как orchestration переводит подтверждённый выбор в
downstream action. Внутри этой модели документ сохраняет точный контракт
Intent Understanding (CAP-003): intent types, slots, clarification,
supersession/expiry и результат intent resolution.

Задача документа — устранить неопределённость, при которой AI, backend и
канал реализовали бы intent handling несовместимо (принцип
[[Ayla MVP Documentation Roadmap]] вводная часть). Документ не описывает
реализацию классификатора (модель, prompt, код) — это зона ayla-ai-core и
Prompt Canon (Roadmap §3.3).

Проверяемая цель: intent layer помогает пройти составной путь MVP
«Transformation Goal → понятный intent → объяснимая рекомендация →
подтверждённый следующий шаг → progress / next state» (факт — MVP Scope
v0.3 §3–§5; MVP User Journey v1.1 §5). `resolved intents` и
`clarification rate` остаются диагностической телеметрией, а не центром
продукта (факт — MVP Scope v0.3 §11).

## Responsibility

Intent Model отвечает за каноническую связь между пользовательской целью,
текущим intent, recommendation intent и orchestration decision. Resolver
часть модели превращает текущее пользовательское сообщение (query) в
структурированное намерение со слотами, оценкой уверенности и
safety-пометками — ровно в объёме, достаточном для следующего решения
Recommendation и orchestration (факт — MVP Scope v0.3 §3–§6; MVP User
Journey v1.1 §6.4–§6.6):

```text
Пользователь формулирует Transformation Goal или рабочее намерение
→ Ayla распознаёт и уточняет user intent       ← resolver contract
→ связывает intent с целью и разрешённым контекстом
→ формирует объяснимый recommendation intent  ← relationship contract
→ пользователь принимает, отклоняет или уточняет следующий шаг
→ orchestration исполняет только подтверждённое downstream action
→ результат становится continuity input
→ пользователь видит progress / next state
```

Факт — [[Ayla Glossary]]: Intent — структурированное представление того, что
человек пытается изменить, понять, выбрать или сделать; Intent не является
ключевым словом, названием услуги или буквальным повторением сообщения. Query —
нормализованное содержимое текущего обращения, само по себе не достоверный
факт и не Intent.

## Canonical Intent Relationships

### Transformation Goal and Intent

**Transformation Goal** — центральная доменная сущность и принадлежит
пользователю (факт — Product Essence §20; Product Principles 4.2). Она
описывает желаемое направление пути и может жить дольше отдельной сессии в
пределах соответствующего consent и доменного lifecycle.

> **Note.** Transformation Goal — продуктовая концепция, используемая
> несколькими canonical документами (в т.ч. этим). Её определение находится
> вне Domain Model; этот документ не вводит и не предполагает существование
> отдельного Domain Aggregate для Transformation Goal.

**User Intent** — текущее структурированное представление того, что
пользователь пытается изменить, понять, выбрать или сделать сейчас. Intent
может поддерживать Transformation Goal, уточнять её, временно не иметь с ней
явной связи или выражать управление самим journey (например,
`REVOKE_CONSENT`). Intent не владеет Transformation Goal и не заменяет её.
Если связь с целью неизвестна, resolver не выдумывает её: связь остаётся
`unknown/not_established`, а Ayla либо задаёт минимальный вопрос, либо
продолжает с минимальным рабочим намерением (факт — MVP User Journey v1.1
§6.2, N1).

**Transformation intent** — роль user intent в изменении состояния на пути к
Transformation Goal. Это не новый runtime `intent_type` и не отдельная
сущность: роль связывает распознанный intent с целью и ожидаемым изменением,
если такая связь подтверждена. Она не превращает прогноз в цель и не обещает
результат.

### Recommendation Intent

**Recommendation intent** — system-owned структурированная цель текущего
recommendation pass: какой объяснимый следующий шаг Ayla намерена предложить
в ответ на resolved user intent, с какой связью с Transformation Goal,
какими gates и каким допустимым классом действия. Это relationship boundary,
а не redesign Recommendation architecture и не новое поле Intent Resolution
Output Contract.

Recommendation intent:

- формируется только после intent-level resolution и обязательных gates;
- не изменяет user intent и не выдаётся за выбор пользователя;
- может быть `no_action`, если действие неуместно;
- не даёт права на side effect: действие требует отдельного явного
  подтверждения пользователя;
- принадлежит Recommendation/orchestration layer; Intent Model владеет
  только правилами связи с user intent.

### Recommendation Input Boundary

Intent Resolution Output 0.5 — единственный выход resolver'а, но не
единственный вход Recommendation/orchestration (Proposal, нормативно).
Recommendation/orchestration получает как минимум два логически раздельных
входа:

1. Intent Resolution Output 0.5 (§ Output Contract) — без изменений;
2. разрешённый runtime context, собранный вне output resolver'а:
   Transformation Goal relationship (если установлена), authorization/
   consent state, результат safety evaluation и прочий допустимый контекст.

Нормативные правила:

- Intent Resolution Output 0.5 остаётся единственным выходом resolver'а;
  этой правкой Output Contract не меняется, новые поля (`goal_id`,
  `goal_ref`, `goal_relationship`, `transformation_goal_ref` и т.п.) в него
  не вводятся;
- Goal context не копируется в output resolver'а молча: связь intent с
  целью читается orchestration/Recommendation из canonical concept source
  Transformation Goal, а не из Intent Output;
- Intent Model владеет только семантической связью intent↔Goal
  (§ Transformation Goal and Intent), а не persistence Goal и не сборкой
  входа Recommendation — это ответственность Recommendation/orchestration
  layer;
- machine-readable appendix (`intent-registry.yaml`, `slot-registry.yaml`,
  `intent-output.schema.json`) этой правкой не меняется.

### Orchestration Intent Model

Orchestration использует следующий нейтральный к каналу порядок:

```text
entry trigger
→ query + permitted context
→ user intent resolution
→ Transformation Goal relationship (known | unknown)
→ recommendation intent
→ explanation + user decision
→ confirmed downstream action or no_action
→ outcome / continuity input
→ progress / next state
```

Intent resolution не вызывает tools и не создаёт side effects.
Recommendation не является действием. Orchestration исполняет action только
после подтверждения пользователя и доменных authorization/safety checks.
Booking — одна из опций downstream action и не является terminal intent или
terminal journey state (факт — Product Principles 4.8; MVP Scope v0.3 §4;
MVP User Journey v1.1 §5, §6.6–§6.7).

### Living Digital Twin Relationship

Living Digital Twin — главный визуальный интерфейс ключевых сценариев и не
самостоятельный субъект продукта (факт — AYLA-DEC-0026: «главный визуальный
интерфейс Ayla и долгоживущее цифровое отражение самого пользователя»;
Product Essence §7: «не сам пользователь и не самостоятельный субъект
продукта»). Normative interpretation derived from AYLA-DEC-0026 и Product
Essence §6–§9 (Proposal; источники не используют эту формулировку дословно):
Twin не является classifier и не является источником intent. Intent Model:

- может использовать только разрешённые user-entered/observed facts и
  явно маркированные reconstructed/inferred representations;
- не выводит intent из внешности или Twin без пользовательского сигнала;
- не смешивает intent, Transformation Goal, prediction и observed state;
- передаёт подтверждённую связь intent с целью/следующим шагом в
  orchestration, чтобы owning channel мог показать её через Twin или другую
  подходящую поверхность;
- не требует Twin на каждом экране и не обновляет Twin автоматически после
  каждого intent/action.

Recognition «это я» относится к принятию Twin-представления пользователем,
а intent recognition — к пониманию текущего намерения. Эти два recognition
flow независимы и не должны смешиваться.

## Recognition Flow and Intent Lifecycle

### Recognition Flow

Четыре равнозначных trigger-сценария — питание, восстановление, подготовка к
событию, история посещений/предпочтений — являются только entry context
(факт — AYLA-DEC-0028: FOUR_EQUAL_TRIGGER_MODEL, ни один trigger не
обязателен и не является центром MVP; Product Vision §10: сценарий
food→beauty «не определяет центр продукта, доменную модель или приоритет
реализации»). Normative interpretation derived from этого принципа
(Proposal; источники не используют термин «intent type»): ни один trigger,
включая Food Scanner, не определяет **intent type** — тип intent
распознаётся resolver'ом по содержанию сообщения (§ Intent Types), а не по
entry trigger; trigger также не получает приоритет по умолчанию в
orchestration.

```text
trigger/context received
→ query normalized without treating it as fact
→ permitted session context assembled
→ candidate user intent(s) detected internally
→ type/slots/confidence/safety resolved
→ clarification when required
→ first consumer-meaningful result published
```

`detected` остаётся внутренним non-runtime lifecycle state по
AYLA-DEC-0019; первый публикуемый result имеет один из статусов Output
Contract. Explainability обеспечивается `evidence` и структурированной
связью с использованным контекстом; правдоподобное объяснение post factum
запрещено.

### Lifecycle and Ownership

- Пользователь владеет намерением в смысле права сформулировать, уточнить,
  изменить, отменить или отвергнуть интерпретацию Ayla.
- Intent resolver владеет resolution result, confidence, slots и lifecycle
  опубликованного результата в пределах этого контракта.
- Transformation Goal принадлежит пользователю и своему domain owner;
  смена intent не изменяет Goal молча.
- Recommendation layer владеет recommendation intent и candidates;
  orchestration владеет sequencing и execution decision; domain capability
  владеет фактическим результатом действия.
- `resolved` означает распознанность user intent, а не принятие
  рекомендации, не execution readiness и не достижение Goal.
- `superseded`/`expired` применяются к intent resolution; они не делают
  Transformation Goal, память или доменный action автоматически
  superseded/expired.

Lifecycle одного user intent:

```text
detected (internal)
→ resolving
→ resolved | needs_clarification | unresolved | blocked_safety
→ superseded | expired                    # только после публикации
```

Повторная сессия создаёт новый intent resolution. Phase 2 persistent memory
может дать разрешённый контекст новому resolution, но не делает прежний
session intent активным и не превращает историю intent в пользовательский
факт.

**Разделение lifecycle ownership (Proposal, нормативно; не создаёт нового
owner decision).** Intent Model и [[Ayla Core Domain Model Specification]]
не определяют конкурирующие lifecycle-модели: они описывают разные слои
одного и того же lifecycle intent.

Intent Model владеет:

- семантикой intent-level состояний (`resolved`, `needs_clarification`,
  `unresolved`, `blocked_safety`, `superseded`, `expired`) и допустимыми
  переходами между ними (см. выше);
- recognition/resolution поведением;
- semantics supersession и expiry (§ Supersession and Expiry);
- представлением состояния в Output Contract (§ Output Contract).

Core Domain Model владеет:

- представлением Intent как доменной сущности (aggregate);
- persistence и стабильным `intent_id`;
- временными метками и техническими transition events;
- storage lifecycle и SoR доменной записи Intent.

## Owns

- Канонические различия и связи между Transformation Goal, user intent,
  transformation role, recommendation intent и orchestration action
  (§ Canonical Intent Relationships) без владения downstream entities.
- Recognition flow и семантический lifecycle user intent (значения
  состояний и допустимые переходы между ними, § Lifecycle and Ownership),
  включая ownership boundaries и отделение session resolution от persistent
  memory; доменное представление, persistence и техническая реализация
  lifecycle принадлежат Core Domain Model (см. ниже, § Does not own).
- Реестр MVP intent types, их slot requirements (`all_of`/`any_of`/
  `conditional`) и правила детерминированного disambiguation между типами
  (§ Intent Types, § Disambiguation and Precedence). Имена слотов, типы и
  правила заполнения; владение значениями слотов (SoR) — у доменных
  capabilities, см. § Slots «Владение значениями».
- Lifecycle значения слота в пределах сессии (§ Slot Lifecycle): состояния,
  события изменения и правило единственного активного значения.
- Правила confidence, clarification, multi-intent, correction, supersession,
  expiry (соответствующие разделы).
- Output contract результата intent resolution (§ Output Contract) —
  обязательный минимум по Roadmap §3.1 плюс additive-поля, помеченные
  Proposal; поля этого контракта являются единственными, которые downstream
  consumers вправе требовать от intent resolver в MVP.
- Правило разметки safety-sensitive intents, форму поля `safety_flags` в
  Output Contract, место blocking-решения в результате, разделение safety
  signal / blocking decision и инвариант `blocked_safety`
  (§ Safety-sensitive Intents). Состав blocking-кодов, их семантика, условия
  срабатывания, fallback-поведение и тексты безопасных ответов принадлежат
  MVP Safety Policy (Roadmap §7.3, CAP-014, ещё не материализована — см.
  OQ-7); текущие три кода — стартовый MVP-набор до её материализации.

## Does not own

- **Transformation Goal lifecycle и persistence** — goal принадлежит
  пользователю и соответствующему Domain owner; Intent Model только
  определяет связь текущего intent с целью.
- **Living Digital Twin representation, media pipeline и recognition
  quality** — Intent Model определяет только границу взаимодействия; Twin
  не является источником intent.
- **Recommendation, ranking, candidates** — MVP Recommendation Contract
  (Roadmap §3.2) и [[Killer PRD]]; Intent Model только поставляет resolved
  intent на вход recommendation pipeline.
- **Consent policy и runtime authorization** — [[Consent Scope Registry]]
  (owner: User Context Domain Owner / Privacy Owner). Intent Model читает
  результат authorization check и отражает его в `status_reason`, но не
  определяет scopes, не хранит consent и не выполняет отзыв consent records —
  отзыв исполняет Consent Management (§ Confidence and Clarification п. 5).
  Authorization deny на уровне execution capability остаётся в
  orchestration/capability layer и не изменяет статус распознанного intent.
- **Safety policy** — детерминированные gates, red flags, competence boundary
  определяются MVP Safety Policy (Roadmap §7.3) и CAP-014; этот документ
  определяет только, как их результат отражается в intent resolution.
- **Доменное представление Intent как сущности**: stable ID, persistence,
  технические transition events, storage lifecycle и SoR (доменный/
  технический слой lifecycle, не семантика intent-level состояний) —
  [[Ayla Core Domain Model Specification]] (MVP slice, Roadmap §4.3).
  Семантический lifecycle intent-level состояний остаётся у Intent Model
  (§ Lifecycle and Ownership).
- **Prompt assembly, tool schemas, provider abstraction** — ayla-ai-core по
  Prompt Canon (Roadmap §3.3) и Tool Schema Registry (Roadmap §6.3).
- **Коммуникативная таксономия** Intent Type (`goal`, `action`, `information`,
  `management`, `feedback`, `correction`) и Goal Category — определены в
  [[Ayla Glossary]] и [[Ayla User Journey Specification]] (legacy full
  journey; historical/non-normative для реестра intent types, поскольку
  маппинг MVP уже зафиксирован закрытым OQ-4); их связь с реестром intent
  types зафиксирована закрытым OQ-4 и machine-readable Intent Registry,
  здесь не переопределяется и не используется как orchestration state.
- **Значения слотов и их SoR** — `service_ref`/`service_category` принадлежат
  Service Catalog Management (CAP-008), `provider_name`/`provider_preference`
  — Provider and Specialist Management (CAP-009),
  `time_slot`/`new_time_slot`/`time_window` — Availability Management
  (CAP-010), `appointment_ref` — Appointment Management (CAP-011),
  `context_fact` — Personal Context Management (CAP-001), `consent_scope` —
  [[Consent Scope Registry]]. Intent Model владеет только именами слотов,
  их типами и правилами заполнения, не данными.
- **Memory view/delete/explain операции** (например, «покажи, что известно
  обо мне», «удали этот факт», «почему это сохранено», «где это
  использовалось») — точный командный словарь и operation contract
  принадлежат CAP-001 (Personal Context Management) и CAP-002 (Consent
  Management) и их UX/operation contracts, не этому документу. Выделенные
  UI-элементы (dedicated settings controls) могут обращаться к этим
  capability напрямую, минуя intent resolution. Разговорные формулировки
  тех же команд могут распознаваться intent resolution как management
  speech act исключительно для маршрутизации orchestration к владеющей
  capability — это не создаёт нового публичного product intent type, не
  расширяет замороженный реестр из 11 типов + sentinel `UNKNOWN`, не
  добавляет runtime-поле и не меняет Output Contract `0.5` **(Proposal)**.
  Interim rule до отдельного owner decision: прямые UI-действия разрешены;
  разговорные команды маршрутизируются к CAP-001/CAP-002 через
  orchestration; новый публичный intent type не вводится.

## Non-goals

Явно вне объёма MVP (Факт — основания: Roadmap §1.2 out of scope, §3.1
«не надо сразу описывать сотни намерений», §3.2 «не детализировать»):

- продвинутые ML-модели классификации и обучение на истории диалогов;
- расширение реестра сверх 11 продуктовых intent types + sentinel `UNKNOWN`
  (замороженный список из 12 значений, Roadmap §3.1);
- долгосрочное персонализационное обучение по intent-паттернам (advanced
  Outcome Learning — deferred, [[Ayla MVP Scope and Release Contract]]
  v0.3 §7);
- proactive recommendations и cross-domain personalization — выключены в
  MVP (факт — [[Consent Scope Registry]] §5.3, §5.4: `MVP status: blocked`,
  требуется отдельное Privacy/Legal approval и решение CSR-OD-3; это не
  автоматически снимается выполнением Phase 2 gate §10.2, который относится
  к `preference_memory`); дополнительно, до выполнения §10.2 любая
  persistent-зависимая персонализация недоступна независимо от статуса этих
  scopes (факт — CSR §10.1–§10.2);
- persistence самого session intent как personal memory; Phase 1 использует
  session-only context, Phase 2 может читать только разрешённые persistent
  preferences для нового resolution (факт — CSR §5.1/§5.2, §10);
- screen-level и channel-specific UX: Intent Model cross-channel neutral;
  required MVP surfaces — Mobile App, MAX Mini App и MAX Bot, feature parity
  не требуется (факт — AYLA-DEC-0027; MVP Scope v0.3 §8);
- автоматические медицинские выводы из intent (запрещено — Roadmap §1.2,
  [[Killer PRD]] §9);
- contract-test fixtures и исполняемые contract tests — не часть этого
  документа; они принадлежат реализации ayla-ai-core (OQ-9);
- machine-readable Intent Registry, Slot Registry и Output Schema —
  канонические appendix этой спецификации в `03 AI System/Contracts/`
  (OQ-9), не содержимое этого Markdown-документа.

## Inputs

Вход intent resolution (Факт — состав данных ограничен scope
`intent_understanding`, [[Consent Scope Registry]] §5.1):

- **User Message / Query** — текущее сообщение пользователя из любого
  required owning channel: Mobile App, MAX Mini App или MAX Bot. Канал не
  изменяет семантику intent и фиксируется только как provenance/routing
  context.
- **Transformation Goal relationship** — подтверждённая текущая Goal или
  явное состояние `unknown/not_established`; resolver не создаёт Goal из
  догадки.
- **Session context** — только разрешённые категории: `explicit_goal`,
  `service_preference`, `provider_preference`, `session_signal`. Persistent
  context этим scope не разрешён; чтение persistent preferences требует
  активного consent на `preference_memory` (required authorization, Phase 2).
- **Authorization state** — результат runtime authorization contract
  ([[Consent Scope Registry]] §6): какие категории данных доступны resolver'у
  в этой сессии. Отсутствие consent → deny (fail-closed).
- **Контекст взаимодействия сессии** — предыдущие сообщения/действия и
  подтверждённые слоты текущей сессии независимо от канала (нужны для
  multi-intent, correction, supersession и cross-channel continuation).
- **Safety evaluation input** — red-zone факты и сигналы риска, доступные в
  сессии, для передачи в deterministic safety gates (CAP-014).

Ограничение (Факт — [[Consent Scope Registry]] §5.1): scope
`intent_understanding` имеет validity «текущая сессия», authorization basis
`service_necessity`, запрещает `write`/`delete` и persistence
`inferred_signal`. Intent resolver не вправе сохранять что-либо о пользователе
— сохранение фактов выполняется только через PROVIDE_CONTEXT/CORRECT_CONTEXT
и владельца Personal Context (CAP-001) по своим правилам.

Нормативное правило authorization (Proposal): неавторизованные **необязательные**
категории данных исключаются из входа fail-closed, но сами по себе **не
блокируют** intent resolution. Intent-level authorization blocking допустим
**только** тогда, когда после исключения неавторизованных категорий
невозможно определить intent type. Если intent type определён,
невозможность downstream execution не меняет его `status` и обрабатывается
orchestration/capability layer — см. § Safety-sensitive Intents,
«Authorization ≠ Safety».

## Outputs

Единственный выход — результат intent resolution по Output Contract
(§ Output Contract): структурированный объект, которого достаточно, чтобы:

- Recommendation Formation (CAP-004) собрала candidates для actionable
  intents;
- канал задал пользователю ровно один уточняющий вопрос, когда
  `requires_clarification = true`;
- safety gate заблокировал дальнейший pipeline при blocking safety decision;
- audit/attribution могли связать последующее действие с конкретным
  `intent_id` (событие `IntentResolved` — MVP event, Roadmap §6.4);
- orchestration восстановила очередь secondary intents без повторного
  анализа сообщения (поле `secondary_intents`).

Intent Model не вызывает tools и не создаёт side effects: запись, перенос и
отмена выполняются только после подтверждения пользователя соответствующими
capabilities (Факт — автономные действия без подтверждения запрещены:
Roadmap §1.2, [[Ayla Constitution]]).

## Intent Types

Минимальный набор MVP (Факт — дословно Roadmap §3.1; не расширяется):
**11 продуктовых intent types + `UNKNOWN` как resolver sentinel** (не
пользовательский intent, см. примечания). Все 11 продуктовых типов
MVP-critical. Это vocabulary **user intent resolution**, а не перечень
Transformation Goal types, recommendation intents или orchestration states.
Каждый тип прямо обслуживает сквозной сценарий
([[Ayla MVP Scope and Release Contract]] v0.3 §4), in-scope capabilities
(факт — MVP Scope §6.1: booking/reschedule/cancel как опция; §6.5: consent
management scopes; Proposal — маппинг на имена
[[Ayla Domain Capability Registry]], не canonical activation до волны 2,
MVP Scope §6: Appointment Management CAP-011 — создание, подтверждение,
перенос, отмена; Consent Management CAP-002; Personal Context Management
CAP-001, whitelist-ограниченный ввод факта) или обязательный негативный
сценарий «Ayla не поняла запрос» (Roadmap §2.1, обработан через `UNKNOWN`).

Требования к слотам показаны в трёх непересекающихся категориях: слот в
`any_of`-группе покрывает своё требование самостоятельно и не дублируется
в «Дополнительные опциональные слоты» (иначе создаётся ложное впечатление,
что тот же слот одновременно и требуется через `any_of`, и опционален
независимо от неё).

| Intent type | Description | Обязательные (`all_of`) | Обязательные (`any_of`) | Дополнительные опциональные слоты | Safety-sensitive | MVP-critical |
|---|---|---|---|---|---|---|
| `DISCOVER_SERVICE` | Пользователь выражает потребность и ищет подходящую услугу без конкретного исполнителя («устала, хочу расслабиться») | `service_interest` | — | `time_preference`, `budget`, `provider_preference` | yes | yes |
| `FIND_SPECIALIST` | Просит найти, показать, сравнить или проверить специалиста; создание записи не запрошено («найди Анну», «кто делает лимфодренажный массаж?») | — | `specialist_selector` (`provider_name` \| `service_category`, minimum_present 1) | — | no | yes |
| `BOOK_APPOINTMENT` | Прямо просит создать запись, даже если часть параметров отсутствует («запиши меня к Анне») | `service_ref`, `time_slot` | — | `provider_name`, `comment` | no | yes |
| `RESCHEDULE_APPOINTMENT` | Перенести существующую запись | `appointment_ref`, `new_time_slot` | — | `reason` | no | yes |
| `CANCEL_APPOINTMENT` | Отменить существующую запись | `appointment_ref` | — | `reason` | no | yes |
| `ASK_ABOUT_SERVICE` | Вопрос о содержании, длительности, подготовке, противопоказаниях услуги | `service_ref` | — | — | yes | yes |
| `ASK_ABOUT_PRICE` | Вопрос о стоимости услуги или booking fee | `service_ref` | — | `provider_name` | no | yes |
| `ASK_ABOUT_AVAILABILITY` | Вопрос о свободных слотах услуги или специалиста | — | `availability_subject` (`service_ref` \| `provider_name`, minimum_present 1) | `time_window` | no | yes |
| `PROVIDE_CONTEXT` | Пользователь добровольно сообщает факт о себе (предпочтение, ограничение) | `context_fact` | — | `fact_category` | yes | yes |
| `CORRECT_CONTEXT` | Пользователь исправляет факт текущей сессии (исправление persistent memory — через memory correction contract, Phase 2) | `context_fact_ref`, `context_fact` | — | — | yes | yes |
| `REVOKE_CONSENT` | Пользователь отзывает согласие на использование данных | — (conditional: см. ниже) | — | `consent_scope`, `revocation_mode` | no | yes |
| `UNKNOWN` | Sentinel resolver'а: намерение не распознано или вне реестра MVP | — | — | — | no | yes |

### Slot Requirements

Требования к слотам материализованы машинно-проверяемо (канонический
machine-readable вид — `03 AI System/Contracts/intent-registry.yaml`,
OQ-9):

- `all_of` — все перечисленные слоты обязаны удовлетворять порогу
  подтверждения; нарушение отражается в `missing_required_slots`.
- `any_of` — минимум `minimum_present` слотов из группы обязаны
  удовлетворять порогу подтверждения; нарушение отражается в
  `unmet_slot_requirements`.
- `conditional` — требование, активируемое значением слота режима; нарушение
  активированного требования отражается так же, как нарушение `all_of`/
  `any_of` соответственно.

Порог подтверждения зависит от класса действия (Proposal):

```yaml
requirement_satisfaction:
  read_only:
    non_reference_slots: filled      # минимум filled
    reference_slots: entity_resolved # однозначный entity_ref обязателен всегда
  side_effect:
    all_required_slots: confirmed    # пользовательское подтверждение значений
```

Так read-only execution (ответ о цене) не требует от пользователя
подтверждать распознанную услугу, но ссылочные слоты (`service_ref`,
`appointment_ref`, `time_slot`) всегда требуют однозначного разрешения в
сущность. `missing_required_slots` и `unmet_slot_requirements`
вычисляются относительно порога, соответствующего intent type
(informational → read_only; side-effect intents → side_effect).

```yaml
slot_requirements:
  DISCOVER_SERVICE:
    all_of: [service_interest]
    any_of: []
  FIND_SPECIALIST:
    all_of: []
    any_of:
      - group_id: specialist_selector
        slots: [provider_name, service_category]
        minimum_present: 1
  BOOK_APPOINTMENT:
    all_of: [service_ref, time_slot]
    any_of: []
  RESCHEDULE_APPOINTMENT:
    all_of: [appointment_ref, new_time_slot]
    any_of: []
  CANCEL_APPOINTMENT:
    all_of: [appointment_ref]
    any_of: []
  ASK_ABOUT_SERVICE:
    all_of: [service_ref]
    any_of: []
  ASK_ABOUT_PRICE:
    all_of: [service_ref]
    any_of: []
  ASK_ABOUT_AVAILABILITY:
    all_of: []
    any_of:
      - group_id: availability_subject
        slots: [service_ref, provider_name]
        minimum_present: 1
  PROVIDE_CONTEXT:
    all_of: [context_fact]
    any_of: []
  CORRECT_CONTEXT:
    all_of: [context_fact_ref, context_fact]
    any_of: []
  REVOKE_CONSENT:
    all_of: []
    any_of: []
    conditional:
      - when: {revocation_mode: consent_record_revocation}
        all_of: [consent_scope]
  UNKNOWN:
    all_of: []
    any_of: []
```

### Disambiguation and Precedence

Одно surface form не может нормативно относиться к двум intent types. Тип
определяется по **speech act / requested outcome**, а не по объекту запроса
(Proposal):

- `FIND_SPECIALIST` — пользователь просит **найти, показать, сравнить или
  проверить** специалиста; создание записи не запрошено.
- `BOOK_APPOINTMENT` — пользователь **прямо просит создать запись**, даже
  если часть параметров отсутствует.

```yaml
intent_precedence:
  - when: {requested_side_effect: create_appointment}
    resolve_as: BOOK_APPOINTMENT
  - when: {requested_outcome: find_or_compare_provider}
    resolve_as: FIND_SPECIALIST
```

Примеры:

- «Найди Анну» → `FIND_SPECIALIST`;
- «Кто делает лимфодренажный массаж?» → `FIND_SPECIALIST`;
- «Запиши меня к Анне» → `BOOK_APPOINTMENT` (с дозапросом `service_ref`,
  `time_slot` через clarification);
- «Хочу попасть к Анне» → `BOOK_APPOINTMENT` при однозначном чтении как
  намерения записаться; при неоднозначной формулировке — clarification
  (записаться или найти?), а не молчаливый выбор типа.

При конфликте измерений приоритет у запрошенного side effect: сообщение,
содержащее запрос на создание записи, никогда не разрешается как
`FIND_SPECIALIST`.

Примечания (Proposal, если не указано иное):

- `safety-sensitive = yes` — это **не** утверждение, что intent опасен, и не
  свойство типа само по себе. Колонка означает только одно: resolution этого
  типа обязан проходить обязательную safety evaluation до перехода к
  recommendation/answer, потому что тип *может* нести health-adjacent или
  red-zone контекст (факт — [[Ayla MVP User Journey Specification]] v1.1
  §6.4: safety constraints проверяются перед рекомендацией; §8 N13: Boundary
  Handling при конфликте с safety-critical контекстом; red-zone факты —
  аллергии, противопоказания, конфликт целей — иллюстративные примеры этого
  документа, Proposal, не дословная формулировка Journey).
  Решение о блокировке принимает
  deterministic safety gate **по контексту** (конкретные red-zone факты,
  competence boundary), а не по типу intent: `DISCOVER_SERVICE` без red-zone
  контекста проходит evaluation с пустым результатом и не блокируется.
  Тип определяет обязательность проверки; контекст определяет её исход
  (§ Safety-sensitive Intents; MVP User Journey v1.1 §6.4, §8).
- `ASK_ABOUT_SERVICE` помечен safety-sensitive, потому что ответ может
  касаться противопоказаний; запрещённые медицинские выводы контролируются
  Safety Policy, а не этим документом.
- `REVOKE_CONSENT` не safety-sensitive, но governance-critical: обработка по
  § Multi-intent and Correction и [[Consent Scope Registry]] §8; режимы
  отзыва — § Confidence and Clarification п. 5.
- `UNKNOWN` — **не пользовательское намерение, а sentinel-состояние
  resolver'а**: «намерение не распознано или вне реестра MVP». Тип сохранён в
  реестре, потому что состав реестра заморожен Roadmap §3.1, но downstream
  **запрещено** обрабатывать `UNKNOWN` как настоящий intent: он никогда не
  передаётся в recommendation pipeline и не может инициировать tool
  execution. Причина фиксируется в поле `status_reason` (§ Output Contract).
  Resolver обязан вернуть `UNKNOWN` вместо угадывания, когда confidence ниже
  порога (§ Confidence and Clarification). `UNKNOWN` не входит в метрики как
  успешно обработанный intent type и не является продуктовой функцией при
  расширении реестра.

## Slots

Slot — именованная единица контекста, которая может быть заполнена,
отсутствовать, конфликтовать или требовать подтверждения (Факт —
[[Ayla Glossary]], Context Slot).

MVP slot registry (Proposal; категории данных согласованы с разрешёнными
категориями scope `intent_understanding` — Факт, [[Consent Scope Registry]]
§5.1):

| Slot | Тип значения | Источник значения | Data category |
|---|---|---|---|
| `service_interest` | Категория услуги seed catalog или свободная формулировка потребности | сообщение пользователя | `explicit_goal` / `service_preference` |
| `service_ref` | Идентификатор или однозначное название услуги | сообщение + каталог (CAP-008) | `service_preference` |
| `service_category` | Категория из seed catalog | сообщение + каталог | `service_preference` |
| `provider_name` | Имя специалиста/салона как сказал пользователь | сообщение | `provider_preference` |
| `provider_preference` | Критерий выбора исполнителя | сообщение | `provider_preference` |
| `time_preference` | Свободное выражение времени («в пятницу вечером») | сообщение | `session_signal` |
| `time_window` | Интервал времени для availability-запроса | сообщение | `session_signal` |
| `time_slot` | Конкретный слот или однозначное время записи | сообщение + Availability Management (CAP-010) | `session_signal` |
| `new_time_slot` | Новое время при переносе | сообщение + Availability Management | `session_signal` |
| `appointment_ref` | Ссылка на запись: ID или однозначное описание («моя запись в пятницу») | сообщение + Appointment Management (CAP-011) | `session_signal` |
| `budget` | Бюджет пользователя в свободной форме | сообщение | `explicit_goal` |
| `comment` | Произвольный комментарий к записи | сообщение | `session_signal` |
| `reason` | Причина переноса/отмены | сообщение | `session_signal` |
| `context_fact` | Факт о пользователе (текст) | сообщение | зависит от содержания; persistence — только whitelist Roadmap §3.4 через CAP-001 |
| `context_fact_ref` | Ссылка на исправляемый факт текущей сессии | диалог сессии | как `context_fact` |
| `fact_category` | Категория факта из whitelist | классификация | control metadata |
| `consent_scope` | Scope из [[Consent Scope Registry]] §5 | сообщение | control metadata |
| `revocation_mode` | `session_personalization_stop` \| `consent_record_revocation` | сообщение (классификация) | control metadata |

Control metadata (Proposal): `fact_category`, `consent_scope`,
`revocation_mode` — технические метаданные resolution, а не пользовательские
context facts; они не относятся к user-context data categories
[[Consent Scope Registry]] §4. Они **могут извлекаться или
классифицироваться из текущего пользовательского сообщения**, но не
добавляются в personal memory, не persistence'ятся независимо от результата
resolution и подчиняются общему session retention результата resolution.
`consent_scope` в этом слоте — **requested scope selector** (какой scope
пользователь хочет отозвать), а не consent record metadata и не
доказательство наличия активного consent: наличие самого согласия проверяет
Consent Management по [[Consent Scope Registry]], а не resolver.

Владение значениями (маппинг CAP — proposal по
[[Ayla MVP Scope and Release Contract]] v0.3 §6): Intent Model владеет реестром
имён слотов и правилами их заполнения, но **не** значениями. Разрешение
значения в сущность и его SoR принадлежат доменным capabilities:
`service_ref`/`service_category` → Service Catalog Management (CAP-008);
`provider_name`/`provider_preference` → Provider and Specialist Management
(CAP-009); `time_slot`/`new_time_slot`/`time_window` → Availability
Management (CAP-010); `appointment_ref` → Appointment Management (CAP-011);
`context_fact` → Personal Context Management (CAP-001); `consent_scope` →
[[Consent Scope Registry]].
Если слоты станут общими для нескольких документов (Consent, Capability,
Journey), реестр выносится в отдельный документ — OQ-10.

Правила (Proposal):

- Slot заполняется только из текущей сессии; автоматическая подстановка
  persistent значений запрещена до Phase 2 (Факт — [[Consent Scope Registry]]
  §10.1).
- Slot, заполненный и подтверждённый, повторно не спрашивается, пока он
  релевантен текущему intent, совместим с purpose и не противоречит новому
  сигналу (факт — [[Ayla MVP User Journey Specification]] v1.1 §6.4,
  clarification suppression и allowed context retrieval).
- Конфликтующие значения одного slot (старое и новое в одной сессии)
  разрешаются через CORRECT_CONTEXT или clarification — не молчаливым
  перезаписыванием.
- `appointment_ref` и `service_ref` считаются заполненными только при
  однозначном разрешении в сущность backend (`entity_ref` в slot envelope);
  неоднозначность → clarification.
- Значение слота передаётся downstream только в стабильном envelope
  (§ Output Contract): `raw_value`, `normalized_value`, `entity_ref`,
  `confirmation_status`, `evidence_refs`. Свободные scalar-значения в
  `slots` запрещены.

## Slot Lifecycle

Lifecycle intent определён в § Supersession and Expiry; этот раздел
определяет lifecycle **значения слота** в пределах одной сессии (Proposal).
Состояние и событие изменения разделены.

Состояние значения — два независимых измерения:

```yaml
value_status:        # active | superseded | expired
confirmation_status: # filled | confirmed
```

- **active / superseded** — активным (`active`) считается ровно одно
  последнее значение слота; вытесненное значение (`superseded`) не
  удаляется из audit-следа, но недоступно resolver'у и execution.
- **expired** — любое значение недействительно за пределами сессии
  (Факт — validity scope `intent_understanding` = текущая сессия,
  [[Consent Scope Registry]] §5.1); перенос значений между сессиями запрещён
  до Phase 2.
- **filled** — значение извлечено из сообщения, но не подтверждено
  пользователем и (для ссылочных слотов) не разрешено в сущность backend.
- **confirmed** — значение подтверждено пользователем (явно или принятием
  уточняющей формулировки) и, для ссылочных слотов (`service_ref`,
  `appointment_ref`, `time_slot`), однозначно разрешено в сущность
  (`entity_ref ≠ null`). Только confirmed-значения доступны side-effect
  execution.

Сериализация (Proposal, нормативно): `value_status` — атрибут внутренней
lifecycle/audit-модели значения и **не входит** в active slot envelope
output contract. Любое значение, присутствующее в `output.slots`, имплицитно
имеет `value_status = active`; superseded- и expired-значения доступны
только через lifecycle/audit representation, не через runtime output.

Событие изменения (фиксируется в audit-следе, не является состоянием):

```yaml
change_reason: # initial_fill | user_correction | intent_shift | clarification_answer
```

Переходы:

- **Initial fill:** новое значение → `active` + `filled`,
  `change_reason = initial_fill`.
- **Confirmation:** `filled → confirmed` (`clarification_answer` либо явное
  подтверждение).
- **Correction (CORRECT_CONTEXT):** старое значение → `superseded`; новое
  значение → `active` + `filled`, `change_reason = user_correction`; после
  подтверждения → `confirmed`. Исправление red-zone релевантного значения
  запускает повторную safety evaluation (§ Multi-intent and Correction).
  Состояния `corrected` не существует: correction — это событие, порождающее
  supersession старого значения и fill нового.
- **Intent shift:** значения, нерелевантные новому intent, несовместимые с
  purpose или противоречащие новому сигналу, → `superseded`,
  `change_reason = intent_shift`; автоматический перенос запрещён (Факт —
  [[Ayla MVP User Journey Specification]] v1.1 §3, §6.4).
- **Session end:** все значения → `expired`.

Пример («Хочу к Анне» → «Нет, я имел в виду Марию»):

| Шаг | Значение | value_status | confirmation_status | change_reason |
|---|---|---|---|---|
| «Хочу к Анне» | `Анна` | active | confirmed | initial_fill → confirmation |
| «Нет, к Марии» | `Анна` | superseded | confirmed | user_correction |
| «Нет, к Марии» | `Мария` | active | filled → confirmed | user_correction |

Правило конфликта: два одновременно активных значения одного слота
невозможны — новое значение либо supersede'ит старое, либо инициирует
clarification при противоречии (§ Confidence and Clarification). Молчаливая
перезапись confirmed-значения без сигнала пользователя запрещена.

## Confidence and Clarification

Confidence — оценка надёжности конкретного структурированного вывода, не
доказательство истинности (Факт — [[Ayla Glossary]]).

Уровни уверенности (факт — [[Ayla MVP User Journey Specification]] v1.1
§6.4,
заданы для формулировок в диалоге; числовые пороги — стартовая runtime
configuration ayla-ai-core по закрытому OQ-1, семантика уровней
канонична):

- **high (> 0.8):** intent считается распознанным; clarification не
  требуется, если выполнены slot requirements.
- **medium (0.5–0.8):** допустимо продолжать с подтверждающей формулировкой
  («Возможно, ты хочешь…»); подтверждение пользователя обязательно перед
  side-effect execution.
- **low (< 0.5):** resolver обязан вернуть `requires_clarification = true`
  либо `intent_type = UNKNOWN` со `status_reason = low_confidence`;
  угадывание запрещено.

Resolution vs Action readiness (Proposal): **распознанность intent и полнота
действия — два разных измерения.** `status = resolved` означает, что тип
intent распознан с достаточной confidence; он **не** требует полноты слотов.
Полнота выражается отдельно через `missing_required_slots` (нарушения
`all_of` и активированных `conditional`) и `unmet_slot_requirements`
(нарушения `any_of`): intent может быть `resolved` и одновременно
action-incomplete («Запиши меня к Анне» → `BOOK_APPOINTMENT`, `resolved`,
`missing_required_slots = [service_ref, time_slot]`).

Готовность различается по классу действия (Proposal):

- **Read-only capability execution** (informational intents: `ASK_*`,
  `DISCOVER_SERVICE`, `FIND_SPECIALIST`; ответ, поиск, формирование
  recommendation): `status = resolved` ∧ slot requirements выполнены на
  уровне read-only (§ Slot Requirements: non-reference слоты — минимум
  `filled`, reference слоты — однозначный `entity_ref`) ∧
  `safety_flags = []` ∧ intent-level authorization пройдена. Отдельное
  подтверждение пользователя не требуется; confirmation gate действует
  позже — перед записью, а не перед формированием рекомендации.
- **Side-effect execution** (создание/перенос/отмена записи, отзыв consent
  records): slot requirements выполнены на уровне side-effect (обязательные
  слоты `confirmed`) + `status = resolved` + `safety_flags = []`.

**Граница контракта (Proposal, нормативно):** Intent Resolution Output
Contract — это **не** полный authorization или execution contract. Он
однозначно определяет только **intent-level readiness** для конкретного
downstream action: распознан ли intent, выполнены ли slot requirements,
подтверждены ли необходимые значения и отсутствует ли intent-level safety
block. Поля `authorization_status` и `user_action_confirmation` в контракт
**не входят**: authorization decision и подтверждение side effect
принадлежат orchestration/capability layer (§ Does not own). **Полная
execution readiness** вычисляется orchestration/capability layer:
intent-level readiness + authorization decision + required user
confirmation + доменные предусловия capability. Два runtime-состояния с
одинаковым intent output могут отличаться execution readiness — это
нормально и не является противоречием контракта.

Action readiness оценивается **для конкретного downstream action**, а не
только для intent type: у одного intent type может быть несколько действий
с разными требованиями (см. REVOKE_CONSENT, п. 5 ниже). Статус
`needs_clarification` зарезервирован для случаев, когда неопределён **сам
intent** (low confidence) или значения конфликтуют, — но не для обычного
дозапроса слотов при распознанном типе.

Тип уточнения (Proposal): additive-поле `clarification_reason` различает
маршруты уточнения — intent-level clarification (уточнение самого намерения),
slot-level clarification (дозапрос параметров при распознанном типе) и
governance-level clarification (уточнение дополнительного downstream action).
Additive-поле `clarification_effect` фиксирует влияние уточнения на текущее
действие: `blocks_current_action` (действие не может быть выполнено до
ответа) или `allows_immediate_safe_action` (уточнение **не блокирует**
выполнение текущего безопасного действия; ответ нужен для дополнительного
действия). Нормативно: `allows_immediate_safe_action` — это разрешение
перейти к действию, а **не** подтверждение, что действие уже исполнено;
resolver не выполняет действий, и факт завершения подтверждается отдельным
execution result/event orchestration/capability layer вне Intent Output
Contract. Нормативная формула:

- `status = needs_clarification` ⇒ intent-level clarification,
  `clarification_reason ∈ {intent_low_confidence, conflicting_slot}`,
  `clarification_effect = blocks_current_action`;
- `status = resolved` ∧ `requires_clarification = true` ⇒ slot-level
  clarification, `clarification_reason ∈ {missing_required_slot,
  unmet_any_of_requirement}`, `clarification_effect = blocks_current_action`;
- исключение — `REVOKE_CONSENT` с готовым безопасным действием:
  `clarification_reason = consent_scope_selection`,
  `clarification_effect = allows_immediate_safe_action` (п. 5 ниже).

Clarification rules (Proposal, если не указано иное):

1. `requires_clarification = true` устанавливается ровно в пяти случаях
   (с соответствующим `clarification_reason`): confidence low
   (`intent_low_confidence`); конфликт значений слота (`conflicting_slot`);
   нарушено требование `all_of`/`conditional` (`missing_required_slot`);
   нарушено требование `any_of` (`unmet_any_of_requirement`); требуется
   выбор scope для отзыва consent records при уже готовом безопасном
   действии (`consent_scope_selection`, только REVOKE_CONSENT). Первые два
   случая переводят результат в `status = needs_clarification`; нарушения
   slot requirements и `consent_scope_selection` оставляют
   `status = resolved`, если тип распознан.
2. `clarification_question` — ровно один конкретный вопрос о недостающих
   слотах, невыполненной группе `any_of` или конфликте; вопрос обязан
   ссылаться на то, что уже сказал пользователь (не общий «что вы хотите?»).
3. Не более 2 clarification-подходов подряд по одному intent; далее
   `intent_type = UNKNOWN`, `status = unresolved`,
   `status_reason = max_clarification_exceeded` и fallback по негативному
   сценарию «Ayla не поняла запрос» (Факт — существование сценария: Roadmap
   §2.1; предел 2 — Proposal).
4. Ответ пользователя на clarification обрабатывается как новый вход того же
   intent (тот же `intent_id`), а не как новый intent — Proposal.
5. `REVOKE_CONSENT` имеет два режима результата (слот `revocation_mode`):
   - `session_personalization_stop` — немедленное прекращение использования
     persistent personalization в текущей сессии (fail-closed). Не требует
     `consent_scope`; исполняется немедленно, без clarification-циклов.
   - `consent_record_revocation` — отзыв конкретных consent records.
     Требует confirmed `consent_scope` (conditional requirement);
     исполняется не resolver'ом, а Consent Management, и только по
     подтверждённому набору scopes.
   Resolver **не выбирает scope самостоятельно и не выполняет отзыв по
   догадке**. При неоднозначном запросе («не используй больше мои данные»)
   `revocation_mode` по умолчанию = `session_personalization_stop`
   (единственное безопасное действие, не требующее выбора) — результат
   готов к его немедленному исполнению orchestration'ом; одновременно
   задаётся один уточняющий вопрос о scope с
   `clarification_reason = consent_scope_selection` и
   `clarification_effect = allows_immediate_safe_action`: вопрос касается
   дополнительного действия (отзыва records) и не блокирует текущее
   безопасное действие. Фактическое завершение session stop подтверждается
   отдельным execution result Consent Management/orchestration, а не этим
   output. REVOKE_CONSENT без confirmed `consent_scope` никогда не является
   готовым к отзыву consent records.
   Деструктивный fallback («отозвать все затронутые scopes») спецификацией
   не устанавливается — поведение открыто до решения Privacy Owner (OQ-5).

## Multi-intent and Correction

Multi-intent — ситуация, когда одно сообщение содержит несколько значимых
Intent; Primary Intent наиболее существенно определяет следующий шаг,
Secondary — дополнительный (Факт — [[Ayla Glossary]]).

Правила MVP (Proposal):

1. Один результат intent resolution = один Primary Intent. Secondary intents
   из того же сообщения материализуются в additive-поле `secondary_intents`
   (тип, `evidence_refs`, `message_position`) — так очередь восстанавливается
   downstream детерминированно, без повторной классификации intent type.
   Secondary intents обрабатываются последовательными resolution-циклами
   после Primary, а не параллельно. Материализация следующего цикла
   (Proposal): orchestration передаёт resolver'у `message_id`, выбранный
   элемент `secondary_intents` и его `evidence_refs`; resolver выполняет
   отдельный slot-resolution pass **без повторной классификации типа** и
   формирует новый полноценный output с новым `intent_id`. Дескриптор
   secondary intent сам по себе не является executable output (не содержит
   slots, confidence, status). Evidence при материализации: resolver
   копирует только указанные элементы evidence в `evidence` нового output;
   `evidence_id` сохраняется (стабильный идентификатор, не индекс), поэтому
   `evidence_refs` дескриптора остаются валидными и после копирования;
   происхождение фиксируется через `message_id`, а не через позицию в
   родительском массиве.
2. Deterministic ordering — порядок определяется правилами, а не выбором
   модели:
   - governance/safety intents, требующие немедленного изменения прав
     (`REVOKE_CONSENT`), обрабатываются первыми независимо от позиции в
     сообщении;
   - иначе Primary = **первый intent в порядке следования в сообщении**
     (message order);
   - informational intent (`ASK_*`) выносится перед actionable только тогда,
     когда его результат — prerequisite для информированного подтверждения
     этого действия: «Запиши меня на массаж и скажи цену» → Primary =
     BOOK_APPOINTMENT, но ответ о цене даётся до запроса подтверждения;
     «Отмени запись и скажи, сколько с меня удержат» → Primary =
     CANCEL_APPOINTMENT (message order), вопрос об удержании — prerequisite
     информированного подтверждения;
   - side effects выполняются только после подтверждения пользователя,
     независимо от ordering (Факт — запрет автономных действий: Roadmap
     §1.2);
   - два actionable в одном сообщении («Перенеси запись и отмени вторую») →
     Primary = первый по message order (RESCHEDULE), второй — Secondary и
     обрабатывается отдельным циклом только после завершения Primary;
     никогда одновременно и никогда в обратном порядке.
3. Правила учёта multi-intent в метрике resolved intents (denominator,
   exclusion rules) принадлежат Measurement Framework; Journey фиксирует
   только evidence points без финальных порогов (факт —
   [[Ayla MVP User Journey Specification]] v1.1 §13) — Open Question OQ-3.

Correction:

1. `CORRECT_CONTEXT` заменяет значение факта в пределах текущей сессии по
   правилам § Slot Lifecycle (старое → `superseded`, новое → `active` +
   `filled`); новое значение не считается подтверждённым, пока пользователь
   не подтвердил исправление — Proposal.
2. Исправление факта, влияющего на safety (red-zone), обязано запускать
   повторную safety evaluation до продолжения actionable pipeline (Факт —
   аналог Safety Re-evaluation при Intent Shift,
   [[Ayla MVP User Journey Specification]] v1.1 §3, §6.4).
3. Событие `ContextFactCorrected` входит в MVP event set (Факт — Roadmap
   §6.4); persistence исправлений — зона CAP-001 Personal Context и Phase 2
   gates, не этого документа.

## Supersession and Expiry

Supersession (смена намерения внутри сессии). Факт —
[[Ayla MVP User Journey Specification]] v1.1 §3, §6.4: пользователь
может менять намерение в рамках одной сессии; при сдвиге Ayla:

1. фиксирует Intent Shift;
2. передаёт в Incremental Discovery только разрешённый к повторному
   использованию контекст;
3. перезапускает Safety Re-evaluation для нового intent;
4. обновляет Recommendation Layer;
5. **не продолжает execution по старому intent без нового подтверждения
   пользователя.**

Proposal (операционализация для output contract): сменившийся intent получает
новый `intent_id`; прежний результат получает `status = superseded` со
`status_reason = intent_shift` и недоступен для execution. Связь «новый
вытесняет старый» фиксируется в audit-следе события `IntentResolved`, а не в
полях output contract (состав обязательных полей заморожен Roadmap §3.1 —
см. OQ-6).

Expiry. Факт — [[Consent Scope Registry]] §5.1: validity scope
`intent_understanding` — текущая сессия; следовательно, resolved intent
действителен только в пределах сессии и не переносится между сессиями.
Proposal: intent, оставшийся без завершения к концу сессии, получает
`status = expired` со `status_reason = session_expired`; таймаут внутри
активной сессии в MVP не устанавливается (OQ-2; при введении —
`status_reason = clarification_timeout`).

## Safety-sensitive Intents

Механика (факт — [[Ayla MVP User Journey Specification]] v1.1 §6.4: safety
constraints проверяются перед переходом к рекомендации; §8 N13: при
конфликте с safety-critical контекстом или competence boundary Ayla
останавливает обработку и переходит в Boundary Handling): перед переходом к
recommendation resolver проверяет red-zone факты (Proposal — иллюстративные
примеры этого документа, не дословная формулировка Journey: аллергии,
противопоказания), конфликты целей и риск вреда; при высоком риске или
competence boundary Ayla не подтверждает и не продолжает небезопасный путь, а
переходит к Boundary Handling; безопасная альтернатива предлагается только
после него. Детерминированные safety gates обязательны для всех product
capabilities (факт — [[Ayla MVP Scope and Release Contract]] v0.3 §6.5,
proposal CAP-014).

Safety signals ≠ blocking decisions (Proposal, нормативно):

- **Safety signal** — детектированный контекст, запускающий обязательную
  safety evaluation: `red_zone_context` (обнаружен red-zone факт — аллергия,
  противопоказание, хроническое состояние, ограничение). Сигнал фиксируется
  во входе safety evaluator'а и в audit metadata; он **не** является полем
  blocking-результата и сам по себе ничего не блокирует. Наличие red-zone
  контекста запускает обязательную safety evaluation, но не является
  blocking result: «У меня аллергия на масло. Какие виды массажа можно
  рассмотреть?» — evaluation может исключить несовместимые варианты, дать
  немедицинское пояснение и продолжить безопасный pipeline без блокировки.
- **`safety_flags`** — список машиночитаемых кодов **только blocking
  decisions** детерминированного safety gate:
  - `red_zone_conflict` — запрошенная услуга или путь конфликтует с
    конкретным red-zone фактом;
  - `competence_boundary` — запрос выходит за границы компетенции Ayla
    ([[Ayla Constitution]] Ст. XII);
  - `unsafe_service_request` — запрошенная услуга конфликтует с известными
    ограничениями.

Отражение в intent resolution (Proposal):

- Непустой `safety_flags` → `status = blocked_safety` со
  `status_reason = safety_gate_blocked`, recommendation pipeline не
  запускается; downstream код ошибки — `SAFETY_BLOCKED` (Факт — стабильный
  код: Roadmap §6.5). `blocked_safety` устанавливается **только** по
  blocking decision детерминированного gate, никогда — по одному факту
  детекции сигнала.
- Safety gates детерминированы: LLM не может «переубедить» gate снятием
  флага; снятие возможно только новым пользовательским вводом, изменяющим
  оценку (например, CORRECT_CONTEXT убрал red-zone факт) — Proposal.
- `unsafe block rate` — обязательная метрика пилота (Факт — Roadmap §9.2);
  частота срабатывания signal-only evaluation (без блокировки) измеряется
  отдельно, чтобы не смешивать detection с deny (Proposal).

### Authorization ≠ Safety

Отсутствие consent — не safety-проблема: намерение пользователя от этого не
становится небезопасным. Safety gate и authorization layer независимы
(Proposal, нормативные правила):

1. Неавторизованные **необязательные** категории данных исключаются из входа
   resolver'а fail-closed, но **не блокируют** intent resolution:
   session-only flow Phase 1 обязан работать без persistent preferences
   (Факт — [[Consent Scope Registry]] §10.1: persistent memory отключена до
   Phase 2, vertical slice функционален без неё).
2. `status = unresolved` со `status_reason = required_context_not_authorized`
   применяется **только** когда после минимизации разрешённого входа
   **невозможно определить intent type**. Downstream код в этом случае —
   `CONSENT_REQUIRED` (Факт — стабильный код: Roadmap §6.5); `safety_flags`
   остаётся пустым, `blocked_safety` не устанавливается.
3. Если intent распознан, но **execution** невозможен из-за недоступной
   категории («подбери того же мастера, что в прошлый раз» →
   `FIND_SPECIALIST`, `resolved`, но история записей неавторизована) —
   intent остаётся `resolved`; authorization deny на уровне execution
   принимает orchestration/capability layer (см. § Does not own), а не
   intent contract. Перевод результата в `unresolved` в этом случае
   запрещён: это ложное утверждение, что intent не распознан.
4. Если session-only данных достаточно, resolution продолжается с
   ограниченным контекстом; запрос дополнительного consent — решение
   Consent Management и UX, а не intent resolver'а.

### Economic Neutrality and Attribution

Intent resolution и его связь с recommendation intent экономически
нейтральны (факт — Constitution Ст. IV; Product Principles 4.11; MVP Scope
v0.3 §3, §13):

- provider revenue, тариф, booking fee, advertising spend, paid placement и
  вероятность тарифицируемого действия не могут влиять на `intent_type`,
  confidence, slots, primary/secondary ordering или clarification;
- intent resolver не получает коммерческий приоритет как evidence;
- recommendation intent не подменяется booking intent ради конверсии;
- цена может быть пользовательским constraint (`budget`) и объяснимым
  фактом, но не скрытым коммерческим весом;
- `intent_id` обеспечивает direct attribution к `recommendation_id` и
  выбранному action; `booking_id` / `appointment_id` добавляется только если
  booking действительно произошёл (факт — MVP Scope v0.3 §6.3; MVP User
  Journey v1.1 §12).

Attribution описывает связь решений и результата, но не изменяет ownership:
наличие booking не делает intent «более истинным», а отсутствие booking не
делает resolved intent неуспешным. Journey может завершиться `no_action` или
другим полезным next step и всё равно перейти к progress / next state.

### Cross-channel Neutrality

Один intent resolution contract действует для Mobile App, MAX Mini App и
MAX Bot (факт — AYLA-DEC-0027). `channel` может присутствовать в transport,
provenance и analytics metadata, но не меняет intent semantics, thresholds,
safety/consent rules или Output Contract. Cross-channel continuation
использует общие identity, consent, recommendation state и memory boundary;
канал не создаёт новый intent автоматически, если пользователь продолжает
тот же подтверждённый resolution flow. При новом сообщении или изменении
намерения применяется обычный lifecycle/supersession.

Минимальные семантические правила session/channel boundary (Proposal,
нормативно; точные тайминги и transport-механика — вне этого документа, см.
новый OQ-12 ниже):

- **channel handoff** — переключение канала само по себе не создаёт новый
  intent resolution: тот же подтверждённый resolution flow продолжается,
  если сохранены общая identity и активное resolution state;
- **new message в рамках того же active resolution** — не создаёт новый
  intent автоматически, если сообщение отвечает на clarification или
  продолжает тот же ещё не завершённый resolution flow
  (§ Confidence and Clarification п. 4);
- **intent shift** — подтверждённая смена намерения создаёт новый intent
  resolution и supersede'ит прежний (§ Supersession and Expiry), независимо
  от канала;
- **session termination / abandoned-flow expiry** — завершение сессии или
  истечение незавершённого flow переводит intent в `expired`
  (§ Supersession and Expiry); возврат пользователя после этого создаёт
  новый resolution, а не продолжение прежнего;
- **new session** — создаёт новый intent resolution (см. § Lifecycle and
  Ownership); Phase 2 persistent memory может дать новому resolution
  разрешённый контекст, но не реактивирует прежний session intent.

Точные транспортные и session-механики (что технически означает «активное
resolution state сохранено» между каналами, длительность abandoned-flow до
expiry, техническая синхронизация state между Mobile App/MAX Mini App/MAX
Bot) этим документом не устанавливаются — не путать с уже закрытым OQ-1 или
с OQ-2 (clarification timeout внутри одной активной сессии); см. новый
OQ-12.

## Output Contract

Обязательный контракт результата intent resolution. Десять полей —
дословно Roadmap §3.1 (Факт, состав заморожен); типы и семантика — Proposal.
Additive-поля (`unmet_slot_requirements`, `contract_version`,
`status_reason`, `clarification_reason`, `clarification_effect`,
`secondary_intents`) — Proposal, добавлены по правилу additive change:

```yaml
intent_id:                # стабильный ID результата resolution в пределах сессии (UUID)
intent_type:              # одно из 12 значений реестра § Intent Types
status:                   # resolved | needs_clarification | unresolved | superseded | expired | blocked_safety
confidence:               # число 0.0–1.0; уровни по § Confidence and Clarification
slots:                    # {slot_name: slot envelope}; только активные значения
missing_required_slots:   # имена слотов all_of/conditional, не удовлетворяющих порогу intent type
evidence:                 # runtime evidence: список {evidence_id, message_id, fragment}
requires_clarification:   # boolean; true ровно в случаях § Confidence and Clarification п. 1
clarification_question:   # string | null; обязателен, когда requires_clarification = true
safety_flags:             # только blocking decisions § Safety-sensitive Intents; [] при отсутствии
unmet_slot_requirements:  # additive: невыполненные any_of-требования (см. ниже); [] при отсутствии
contract_version:         # additive: версия runtime-контракта ("0.5", pre-release); обязательна
status_reason:            # additive: причина статуса (enum ниже); null для resolved
clarification_reason:     # additive: intent_low_confidence | conflicting_slot | missing_required_slot |
                          # unmet_any_of_requirement | consent_scope_selection; null, если requires_clarification = false
clarification_effect:     # additive: blocks_current_action | allows_immediate_safe_action;
                          # null, если requires_clarification = false
secondary_intents:        # additive: очередь secondary intents из того же сообщения; [] при отсутствии
```

**Состояние `detected` (owner ruling 2026-07-27, KM-IM-1):** промежуточное
состояние доменной сущности Intent до первого resolution pass является
внутренним non-runtime lifecycle-состоянием Core Domain Model и в
сериализуемый output-контракт не входит. Оно не используется как
orchestration state, не означает intent-level readiness или execution
readiness и не может служить consumers основанием для действия. Первый
публикуемый output создаётся после первого resolution pass и несёт одно из
публикуемых intent-level состояний, достаточных для следующего решения
consumer (первое consumer-meaningful состояние): `resolved`,
`needs_clarification`, `unresolved`, `blocked_safety`. Значения `superseded`
и `expired` — не результаты resolution pass, а последующие
lifecycle-переходы уже опубликованного результата (§ Supersession and
Expiry).

Slot envelope — стабильная форма значения слота (Proposal):

```yaml
slots:
  provider_name:
    raw_value: "к Анне"              # дословная форма из сообщения
    normalized_value: "Анна"         # нормализованная форма (или null)
    entity_ref: "provider:uuid"      # ссылка на сущность backend или null
    confirmation_status: filled      # filled | confirmed
    evidence_refs: ["ev-1"]          # evidence_id элементов evidence
  budget:
    raw_value: "до трёх тысяч"
    normalized_value: {amount_max: 3000, currency: RUB}
    entity_ref: null
    confirmation_status: filled
    evidence_refs: ["ev-2"]
```

Не все поля обязательны для каждого слота, но shape стабилен; `entity_ref`
обязателен для ссылочных слотов в состоянии `confirmed`. `value_status` в
envelope не сериализуется: присутствие значения в `slots` имплицитно означает
`active` (§ Slot Lifecycle). Superseded-значения в `slots` не включаются.

`unmet_slot_requirements` — элемент (Proposal):

```yaml
- requirement_id: specialist_selector   # group_id из § Slot Requirements
  requirement_type: any_of
  candidate_slots: [provider_name, service_category]
  minimum_present: 1
```

`secondary_intents` — элемент (Proposal):

```yaml
- intent_type: ASK_ABOUT_PRICE   # тип secondary intent из реестра
  evidence_refs: ["ev-2"]        # evidence_id элементов evidence этого intent
  message_position: 2            # порядковая позиция в сообщении (1-based)
```

`status_reason` — enum (Proposal): `low_confidence` | `out_of_scope` |
`conflicting_slots` | `max_clarification_exceeded` | `intent_shift` |
`session_expired` | `clarification_timeout` | `safety_gate_blocked` |
`required_context_not_authorized`.

`contract_version` — версия **runtime output contract**, независимая от
версии этого документа: редакционные изменения спецификации (пояснения,
Open Questions, Change Log) не меняют `contract_version`. Пока контракт не
заморожен первой реализацией (consumers отсутствуют), используется
pre-release нумерация `0.x` (текущая — `"0.5"`, пятая редакция
контракта): изменения фиксируются minor-шагами внутри `0.x`. Первая
замороженная JSON Schema с реальным consumer получает `"1.0"`; далее:
additive-поле → minor; удаление/переименование поля или изменение семантики
→ major и change control по Roadmap §5.4.

`evidence` — runtime-форма (Proposal):

```yaml
- evidence_id: "ev-1"   # стабильный ID элемента в пределах сессии (не индекс массива)
  message_id:           # идентификатор сообщения сессии (выдаёт runtime/channel)
  fragment:             # дословная цитата фрагмента, обосновывающего тип или слот
```

`evidence_id` стабилен при копировании элемента в новый output (secondary
materialization, § Multi-intent and Correction): ссылки `evidence_refs`
остаются валидными, происхождение фиксируется через `message_id`.

Дословный `fragment` может содержать чувствительные данные (здоровье,
противопоказания, персональные обстоятельства), поэтому действует
нормативное правило (Proposal): **runtime evidence живёт только в пределах
разрешённой session retention и не переносится в долгосрочный
audit/attribution автоматически.** Для persistence используется отдельная
форма без дословного текста:

```yaml
audit_evidence:
  - message_id:
    evidence_type:    # intent_type | slot
    slot_name:        # или null
    fragment_hash:    # хэш для проверки целостности, не исходный текст
```

Persistence `audit_evidence` требует отдельной data classification,
retention policy и authorization basis (Roadmap §7.2, Data Inventory
Matrix) — см. OQ-8.

Инварианты (Proposal):

- `intent_type = UNKNOWN` ⇒ `status ∈ {needs_clarification, unresolved}`,
  `status_reason ≠ null`; результат не передаётся в recommendation pipeline
  и не может инициировать execution (UNKNOWN — sentinel, не intent).
- `status_reason ≠ null` обязателен для `status ∈ {unresolved, superseded,
  expired, blocked_safety}` и допустим для `needs_clarification`; для
  `resolved` — `null`.
- `requires_clarification = true` ⇒ `clarification_question ≠ null` ∧
  `clarification_reason ≠ null` ∧ `clarification_effect ≠ null`.
- `status = needs_clarification` ⇒ `requires_clarification = true` ∧
  `clarification_reason ∈ {intent_low_confidence, conflicting_slot}` ∧
  `clarification_effect = blocks_current_action`.
- `clarification_reason = consent_scope_selection` ⇒
  `clarification_effect = allows_immediate_safe_action` ∧
  `intent_type = REVOKE_CONSENT` ∧ `status = resolved`; уточняется
  дополнительное действие, текущее безопасное действие разрешено к
  немедленному исполнению orchestration'ом (но его завершение этим output
  не подтверждается).
- `intent_type = UNKNOWN` ∧ `status = needs_clarification` ⇒
  `clarification_reason = intent_low_confidence`.
- `intent_type = UNKNOWN` ∧ `status = unresolved` ⇒
  `status_reason ∈ {out_of_scope, max_clarification_exceeded,
  required_context_not_authorized}`.
- `status = resolved` означает распознанность типа и **не** требует
  `missing_required_slots = []` или `unmet_slot_requirements = []`
  (resolution ≠ action readiness).
- Output однозначно определяет **intent-level readiness** для конкретного
  downstream action: read-only — `status = resolved` ∧
  `missing_required_slots = []` ∧ `unmet_slot_requirements = []` ∧
  `safety_flags = []` (порог слотов — по § Slot Requirements); side-effect
  — дополнительно обязательные слоты `confirmed`. Полная execution
  readiness (authorization decision, подтверждение пользователя, доменные
  предусловия) этим контрактом не выражается и вычисляется
  orchestration/capability layer.
- `REVOKE_CONSENT` готов к отзыву consent records только при
  `revocation_mode = consent_record_revocation` ∧ confirmed `consent_scope`;
  без confirmed `consent_scope` результат разрешает только
  `session_personalization_stop` и передачу управления Consent Management.
- `status = blocked_safety` ⇔ `safety_flags ≠ []` ∧
  `status_reason = safety_gate_blocked`; результат не передаётся в
  recommendation pipeline. Обратно: `status ≠ blocked_safety` ⇒
  `safety_flags = []`. `safety_flags` содержит только blocking-коды;
  детекция safety signal без blocking decision не меняет `status`.
  Authorization denial никогда не порождает `blocked_safety`
  (§ Authorization ≠ Safety).
- `status = unresolved` со `status_reason = required_context_not_authorized`
  допустим только при невозможности определить intent type после
  минимизации разрешённого входа.
- `secondary_intents` содержит каждый значимый intent сообщения, не
  выбранный Primary; каждый элемент ссылается на собственные
  `evidence_refs` по стабильным `evidence_id`; при материализации secondary
  intent указанные элементы evidence копируются в новый output с
  сохранением `evidence_id`.
- `evidence` не пуст для `status = resolved`: каждый resolved intent обязан
  быть прослеживаем к пользовательскому вводу (Факт — принцип
  прослеживаемости критических решений: [[Ayla Constitution]]; explainability
  — обязательное требование MVP, [[Ayla MVP Scope and Release Contract]]
  v0.3 §10; [[Ayla MVP User Journey Specification]] v1.1 §6.5).
- `contract_version` присутствует в каждом результате и равна версии
  runtime-контракта, по которой сформирован результат.
- Контракт additive-расширяем: новые поля допускаются только через change
  control и совместимость с consumers (Roadmap §5.4); удаление/переименование
  полей — breaking change.

## Open Questions

- **OQ-1 (ЗАКРЫТ — owner ruling 2026-07-28). Владелец числовых порогов
  confidence.** Семантика confidence bands (high/medium/low) принадлежит
  Intent Model и остаётся канонической; конкретные числовые пороги — не
  неизменяемая часть публичного runtime-контракта, а versioned runtime
  configuration ayla-ai-core. Стартовые значения MVP: 0.8 (high) / 0.5
  (medium). Настройка порогов по fixtures и пилотным данным —
  configuration change; изменение смысла уровней — architecture change,
  требующее отдельного решения.
- **OQ-2. Таймаут expiry внутри активной сессии** для intent в статусе
  `needs_clarification` (сейчас: только конец сессии,
  `status_reason = session_expired`). Требуется решение Product Owner
  совместно с MVP UX State Contract (Roadmap §2.2); при введении таймаута
  задействуется `status_reason = clarification_timeout`.
- **OQ-3. Правила метрики resolved intents:** denominator, exclusion rules,
  resolution window, учёт multi-intent, различие user-confirmed/inferred —
  обязательны по Journey (Intent Resolution Types), но нигде не зафиксированы.
  Кандидат на фиксацию: Pilot Measurement Plan (Roadmap §9.2). `UNKNOWN`
  (sentinel) не входит в denominator как обработанный intent type.
- **OQ-4 (ЗАКРЫТ — owner ruling 2026-07-28). Связь реестра intent types с
  коммуникативной таксономией** Journey Stage 3
  (`goal`/`action`/`information`/`management`/`feedback`/`correction`).
  Решение: это ортогональные измерения. Intent Type используется для
  resolution и capability routing; Communicative Class — для Journey, UX и
  аналитики. Маппинг Intent Type → Communicative Class хранится в
  machine-readable Intent Registry (OQ-9) и не заменяет `intent_type` в
  resolver output. Маппинг MVP (норма с v0.9): DISCOVER_SERVICE →
  goal; BOOK_APPOINTMENT → action; RESCHEDULE/CANCEL_APPOINTMENT →
  management; ASK_* → information; PROVIDE_CONTEXT → feedback;
  CORRECT_CONTEXT → correction; REVOKE_CONSENT → management;
  FIND_SPECIALIST → information (owner ruling 2026-07-28: «найди/покажи/
  кто делает» — запрос информации о специалистах).
- **OQ-5. Поведение при неоднозначном REVOKE_CONSENT.** Спецификация
  устанавливает безопасный минимум: неоднозначный запрос →
  `revocation_mode = session_personalization_stop` + один уточняющий вопрос
  о scope; отзыв records — только через Consent Management по подтверждённому
  набору scopes. Машинное определение «затронутых scopes» и финальное
  поведение при повторной неоднозначности требуют решения Privacy Owner и
  согласования с [[Consent Scope Registry]] §8 (команды пользователя).
- **OQ-6. Представление supersession-связи** (новый intent вытесняет старый):
  audit-след события `IntentResolved` vs дополнительное поле контракта.
  Текущее решение — audit-след, чтобы не расширять замороженный контракт.
- **OQ-7 (ЗАКРЫТ — owner ruling 2026-07-28). Владение safety-кодами.**
  Intent Model владеет формой safety-интеграции: структурой `safety_flags`,
  правилом signal ≠ blocking decision и инвариантом `blocked_safety`.
  Составом blocking-кодов, условиями срабатывания, fallback-поведением и
  текстами безопасных ответов владеет MVP Safety Policy (Roadmap §7.3). До
  её материализации текущие три кода (`red_zone_conflict`,
  `competence_boundary`, `unsafe_service_request`) — стартовый MVP-набор;
  расширение набора — additive, изменение семантики существующего кода —
  change control.
- **OQ-8. Persistence `intent_id` и `audit_evidence`** для связки с
  attribution (`recommendation_id` → qualified action, [[Killer PRD]] §6):
  хранится ли intent result в backend или живёт только в сессии — решить в
  MVP Architecture (Roadmap §5.1). Дословный `fragment` persistence'у не
  подлежит; форма `audit_evidence` требует data classification и retention
  policy (Roadmap §7.2).
- **OQ-9. Machine-readable Intent Registry и contract-test fixtures.**
  Канонические machine-readable appendix этого документа (материализованы
  в v0.9.1; версии реестров независимы — `registry_version`, совместимость
  с контрактом указывается через `compatible_contract_version`):
  - `03 AI System/Contracts/intent-registry.yaml` — реестр intent types,
    slot requirements, execution class, маппинг Communicative Class
    (закрытый OQ-4) и downstream capability, `intent_precedence`;
  - `03 AI System/Contracts/slot-registry.yaml` — реестр слотов, data
    categories, control metadata, SoR-владение;
  - `03 AI System/Contracts/intent-output.schema.json` — JSON Schema
    (draft 2020-12) output contract с инвариантами `allOf`.
  Изменение реестров — через change control ayla-knowledge; при
  расхождении нормативным является текст этого документа, реестры
  синхронизируются с ним. Contract-test fixtures и исполняемые тесты —
  implementation-owned артефакты ayla-ai-core (волна 3, AYLA-DEC-0014):
  проверяют соответствие кода каноническим реестрам и схеме.
- **OQ-10 (ЧАСТИЧНО ЗАКРЫТ). Slot Registry.** Machine-readable Slot
  Registry материализован в `03 AI System/Contracts/slot-registry.yaml`
  (v0.9.1+). Отложенным остаётся только вопрос о выделении
  самостоятельной narrative-спецификации слотов — до появления
  cross-document ownership и lifecycle semantics (слоты, общие для
  Consent, Capability, Journey). Во избежание коллизий нумерации:
  «OQ-10» этого документа — всегда про Slot Registry; вопрос Memory
  Whitelist относится к Core Domain Model / Memory policy, не к этому
  документу.
- **OQ-11 (ЗАКРЫТ — owner ruling 2026-07-27, KM-IM-1). Состояние `detected`
  доменной сущности Intent.** Решение: `detected` зафиксирован как
  внутреннее non-runtime lifecycle-состояние Core Domain Model. Оно не
  входит в сериализуемый output-контракт Intent Model, не используется как
  orchestration state, не означает intent-level readiness и execution
  readiness и не должно использоваться consumers как основание для действия.
  В публичном контракте остаются только публикуемые intent-level состояния,
  достаточные для следующего решения consumer (первое consumer-meaningful
  состояние): `resolved`, `needs_clarification`, `unresolved`,
  `blocked_safety`; значения `superseded` и `expired` — последующие
  lifecycle-переходы уже опубликованного результата (§ Supersession and
  Expiry). Первый contract output создаётся после первого resolution pass.
  Impact: intent model — no_change; Core Domain Model — `detected` помечен
  как internal non-runtime state (применено в v1.2.2 §7.5). Решение
  зарегистрировано записью AYLA-DEC-0019 ([[Ayla Decision Log]],
  регистрация 2026-07-28; исправлена ошибочная ссылка на AYLA-DEC-0016 —
  Subject Identity Model).
- **OQ-12. Session/Conversation State Contract для cross-channel session
  boundary.** Точные транспортные и session-механики — что технически
  означает «активное resolution state сохранено» между каналами,
  длительность abandoned-flow до expiry вне текущей сессии, синхронизация
  state между Mobile App/MAX Mini App/MAX Bot — не определены этим
  документом и требуют отдельного Session/Conversation State Contract или
  UX State Contract (смежный, но отдельный вопрос от OQ-2, который про
  clarification timeout внутри одной активной сессии). До его появления
  действуют только минимальные семантические правила
  § Cross-channel Neutrality.

## Authoring Self-Check

Раздел фиксирует **полноту авторской проработки** документа относительно
требований Roadmap и предыдущих ревью — не готовность к implementation, не
internal/Product Owner approval и не canonical status (Proposal,
нормативно). Отмеченные `[x]` пункты означают только то, что
соответствующий аспект специфицирован в тексте документа; они не отменяют
требований review, approval gates (см. status banner в начале документа) и
не подменяют findings Internal Consistency Review. Готовность к
implementation candidate определяется отдельно — через review, targeted
repair (этот проход) и Product Owner Final Review.

Пункты чек-листа (авторская проработка):

- [x] Определены 11 продуктовых intent types из Roadmap §3.1 с description,
      slot requirements, optional slots, разметкой safety-sensitive и
      MVP-critical, плюс `UNKNOWN` как resolver sentinel; ни одного типа
      сверх замороженного списка из 12 значений.
- [x] Для каждого intent type существует машинно-проверяемое slot
      requirement (`all_of` / `any_of` с `minimum_present` / `conditional`).
- [x] Disambiguation детерминирован: тип определяется по speech act /
      requested outcome; для известных пересечений типов установлены
      deterministic precedence или обязательная clarification; resolver не
      делает молчаливый выбор при неустранимой неоднозначности
      (FIND_SPECIALIST vs BOOK_APPOINTMENT разведены).
- [x] Output contract содержит все 10 обязательных полей Roadmap §3.1;
      additive-поля помечены; каждый инвариант выразим как автоматический
      тест.
- [x] Любой output однозначно определяет **intent-level readiness** для
      конкретного downstream action, включая режимы REVOKE_CONSENT
      (`session_personalization_stop` без `consent_scope`;
      `consent_record_revocation` — только с confirmed `consent_scope`).
      Полная execution readiness (authorization decision, user
      confirmation, доменные предусловия) контрактом не выражается и
      вычисляется orchestration/capability layer; поля
      `authorization_status`/`user_action_confirmation` в контракте
      отсутствуют намеренно.
- [x] Пороги подтверждения слотов разведены по классу действия: read-only —
      non-reference слоты `filled`, reference слоты — однозначный
      `entity_ref`; side-effect — обязательные слоты `confirmed`.
- [x] Governance-level clarification выразима контрактом: неоднозначный
      REVOKE_CONSENT = готовность к немедленному session stop +
      `clarification_reason = consent_scope_selection` +
      `clarification_effect = allows_immediate_safe_action`; поле не
      утверждает факт исполнения действия — завершение подтверждается
      отдельным execution result вне контракта; ни один нормативно
      требуемый кейс не нарушает инварианты.
- [x] `contract_version` версионирует runtime-контракт и независима от
      версии документа; до первой замороженной реализации действует
      pre-release нумерация `0.x`, `"1.0"` присваивается первой замороженной
      JSON Schema с consumer.
- [x] Для каждого терминального/блочного status определена допустимая
      `status_reason`; enum покрывает все значения status; комбинации
      `UNKNOWN` × status × reason зафиксированы.
- [x] Slot lifecycle разделяет состояние (`value_status` ×
      `confirmation_status`) и событие (`change_reason`); correction имеет
      однозначный state transition; правило единственного активного значения
      зафиксировано; `value_status` не сериализуется в output (присутствие в
      `slots` имплицитно = `active`).
- [x] Slot envelope фиксирует `raw_value` / `normalized_value` /
      `entity_ref` / `confirmation_status` / `evidence_refs`; scalar-значения
      запрещены; control metadata отделены от user-context data categories.
- [x] Safety deny и authorization deny представлены раздельно; detection
      (safety signal) отделён от blocking decision: `blocked_safety` ⇔
      непустые blocking-коды (`status ≠ blocked_safety` ⇒
      `safety_flags = []`); authorization blocking — только
      `unresolved` + `required_context_not_authorized` при невозможности
      определить intent; ни один optional context denial не блокирует
      session-only flow; execution-level authorization deny не меняет
      статус распознанного intent.
- [x] `UNKNOWN` формализован как sentinel resolver'а; execution по нему
      запрещён; в метрики как обработанный intent type не входит.
- [x] Evidence разделён на runtime-форму (`{evidence_id, message_id,
      fragment}`) и audit-форму без дословного текста (`fragment_hash`);
      дословный fragment не persist'ится автоматически; `evidence_id`
      стабилен при secondary materialization.
- [x] Secondary intents восстанавливаются из output детерминированно
      (`secondary_intents`: тип, `evidence_refs` по `evidence_id`,
      `message_position`); материализация — slot-resolution pass без
      повторной классификации, с новым `intent_id` и копированием evidence.
- [x] Multi-intent имеет deterministic ordering: governance-приоритет →
      message order; informational выносится вперёд только как prerequisite
      информированного подтверждения; side effects — только после
      подтверждения.
- [x] Правила clarification задают исчерпывающие условия
      `requires_clarification = true`, тип уточнения (`clarification_reason`)
      и верхнюю границу числа уточнений; «угадывание» при low confidence
      исключено; REVOKE_CONSENT не содержит destructive fallback.
- [x] Supersession и expiry опираются на зафиксированные в источниках
      механики (Dynamic Intent Transition, session validity) и не вводят
      перенос intent между сессиями.
- [x] Все положения, не подтверждённые источниками, помечены Proposal; все
      незакрытые решения собраны в Open Questions и не подменены выдуманными
      значениями.
- [x] Содержимое не выходит за MVP-границы
      [[Ayla MVP Scope and Release Contract]] v0.3 §6/§7 и consent-режим Phase 1
      ([[Consent Scope Registry]] §10.1).
- [x] `python scripts/validate_knowledge.py` — 0 errors по этому документу.

## Change Log

> Журнал отражает историю изменений документа и не является нормативной частью
> спецификации.

### v1.0 (2026-08-05) — WINDOW-02 targeted alignment

- **§ Recommendation Input Boundary:** формулировка «владеющий доменный
  источник Transformation Goal» заменена на «canonical concept source»,
  чтобы не подразумевать существование отдельного Domain Aggregate для
  Transformation Goal в Core Domain Model. Семантика правила не изменена.
- **§ Transformation Goal and Intent дополнен Note:** Transformation Goal —
  продуктовая концепция, используемая несколькими canonical документами; её
  определение находится вне Domain Model.
- **Будущая синхронизация:** после approval Ayla Domain Event Registry
  (текущая версия 0.4, § Migration Mapping) события `IntentResolved` и
  `ContextFactCorrected`, используемые в этом документе, потребуют
  синхронизации с их каноническими кандидатами (`intent.resolution_produced`,
  `memory.entry_superseded`). До approval реестра переименование не
  выполняется (консистентно с правилом реестра о том, что миграция
  потребителей не выполняется до approval).
- 11 продуктовых intent types + sentinel `UNKNOWN`, 18 слотов, Output
  Contract `0.5` и machine-readable appendix не изменены. Status остаётся
  candidate. CANON_INDEX не затронут (отдельное окно).

### v1.0 (2026-08-03) — D1 Product/Journey boundary clarification

- **§ Does not own дополнен:** memory view/delete/explain операции
  («покажи, что известно обо мне», «удали этот факт», «почему это
  сохранено», «где это использовалось») явно закреплены за CAP-001
  (Personal Context Management) и CAP-002 (Consent Management) и их
  UX/operation contracts. Выделенные UI-элементы могут обращаться к этим
  capability напрямую, минуя intent resolution; разговорные формулировки
  могут распознаваться только для маршрутизации orchestration, без
  создания нового публичного product intent type.
- Interim rule зафиксировано: прямые UI-действия разрешены; разговорные
  команды маршрутизируются к CAP-001/CAP-002 через orchestration; новый
  публичный intent type не вводится до отдельного owner decision.
- 11 продуктовых intent types + sentinel `UNKNOWN`, 18 слотов, OQ-9, OQ-10
  и Output Contract `0.5` не изменены; machine-readable appendix не
  затронут; никакое новое runtime-поле не добавлено. Status остаётся
  candidate.

### v1.0 (2026-08-03) — Governance and machine-readable synchronization pass

- Governance synchronization после repeat Internal Consistency Review
  (read-only) следующей за targeted material repair. Не redesign и не новая
  structured revision: `version`, `status`, `decision_status`,
  `canonical_status`, `contract_version`, Output Contract, intent types,
  slot IDs и owner decisions не изменены.
- **P3 normalization (residual):** нормализованы два оставшихся сокращённых
  имени capability в таблице § Slots («Availability»/«Appointment» →
  «Availability Management»/«Appointment Management», CAP-010/CAP-011),
  пропущенные предыдущим normalization pass.
- **Machine-readable metadata sync:** `intent-registry.yaml` и
  `slot-registry.yaml` (`source_version`, `status`, `updated`, header
  comment) и `intent-output.schema.json` (description) обновлены для
  отражения текущего состояния документа (v1.0, draft / proposed /
  candidate) вместо устаревшего v0.9.2/approved; `registry_version`,
  `compatible_contract_version`, `contract_version`, intent/slot IDs,
  execution/communicative classes и JSON Schema `allOf`-инварианты не
  изменены.
- **`any_of` presentation harmonization:** `optional_slots` в
  `intent-registry.yaml` для `FIND_SPECIALIST` и `ASK_ABOUT_AVAILABILITY`
  приведён в соответствие с prose-таблицей Intent Types (не дублирует
  члены `any_of`-группы как «дополнительные опциональные»); `any_of`
  requirements не изменены.
- **Migration Plan correction:** `Ayla MVP v0.3 Downstream Migration Plan`
  (I-02) скорректирован — требование «добавить новые intent types» для
  Goal/LDT/check-in/weekly-review/trigger-сценариев заменено на требование
  semantic coverage через Goal relationship/Context/Orchestration (уже
  введено § Recommendation Input Boundary v1.0); новые intent types не
  вводятся ни в этом документе, ни в Migration Plan.
- Governance-находки предыдущей ревизии, не входящие в mandate этой
  синхронизации (workstream authorization; `approved`→`draft` lifecycle
  transition отсутствует в `schema.yaml`), остаются открытыми как
  Governance Gap и не закрываются этим проходом.

### v1.0 (2026-08-03) — Targeted material repair after Internal Consistency Review

- Пройден targeted material repair пакета findings Internal Consistency
  Review (read-only review этой же ревизии v1.0). Правка не является новой
  structured revision и не меняет `version`, `status`, `decision_status`,
  `canonical_status` или `contract_version`.
- **Goal context vs Intent Output Contract:** добавлен § Recommendation
  Input Boundary — Recommendation/orchestration получает Intent Resolution
  Output 0.5 и отдельно permitted runtime context (включая Transformation
  Goal relationship); Output Contract 0.5 не изменён, новые Goal-поля не
  введены.
- **Lifecycle ownership:** разведены семантический lifecycle intent-level
  состояний (Intent Model) и доменное представление/persistence/технический
  lifecycle (Core Domain Model); § Owns и § Does not own синхронизированы.
- **Cross-channel/session boundary:** добавлены минимальные семантические
  правила (channel handoff, new message, intent shift, session termination,
  new session); точная transport/session-механика вынесена в новый узкий
  OQ-12, existing OQ-1/OQ-4/OQ-7/OQ-11 не переоткрыты.
- **`any_of` slot presentation:** таблица Intent Types переведена на три
  явные категории (`all_of` / `any_of` / дополнительные опциональные слоты)
  без изменения фактических slot requirements и без расхождения с YAML
  `slot_requirements`.
- **Fact/Proposal/source attribution:** исправлены пять случаев
  избыточно-широкой атрибуции «Факт» (Living Digital Twin/AYLA-DEC-0026;
  trigger model/AYLA-DEC-0028 и Product Vision §10; Consent Scope Registry
  §10 vs §5.3/§5.4; MVP Scope §6 capability wording; red-zone facts Journey
  references) — переразмечены как Proposal/normative interpretation с
  точной ссылкой на источник.
- **`safety_flags` ownership:** § Owns уточнён — Intent Model владеет формой
  поля и разделением signal/blocking decision; состав и семантика
  blocking-кодов остаются за MVP Safety Policy (OQ-7).
- **Acceptance Criteria:** раздел переименован в § Authoring Self-Check с
  явным пояснением, что отметки `[x]` — авторская полнота, не approval и не
  canonical status.
- Применены связанные editorial-исправления: вводная формулировка Purpose
  («предлагает нормативную модель» вместо «определяет каноническую»),
  wikilink legacy [[Ayla User Journey Specification]], нормализация имён
  capability против [[Ayla Domain Capability Registry]] (Provider and
  Specialist Management, Service Catalog Management, Availability
  Management, Personal Context Management, Appointment Management, Consent
  Management).
- Не изменены: Output Contract 0.5; machine-readable appendix
  (`intent-registry.yaml`, `slot-registry.yaml`,
  `intent-output.schema.json`); MVP scope; owner decisions не создавались;
  candidate status не изменён.

### v1.0 (2026-08-03) — Structured revision to current product foundation

- **Canonical role expanded:** документ больше не сводит intent model к
  classifier/output contract; зафиксированы связи Transformation Goal →
  user intent → transformation role → recommendation intent → confirmed
  downstream action → progress / next state без redesign Recommendation или
  Domain Model.
- **Transformation Goal:** цель закреплена как центральная доменная сущность,
  принадлежащая пользователю; session intent не владеет целью, не изменяет её
  молча и не подменяет её прогнозом.
- **Living Digital Twin:** определена граница взаимодействия с главным
  визуальным интерфейсом; Twin не является источником intent, classifier или
  самостоятельным субъектом; Twin recognition и intent recognition разведены.
- **Lifecycle and ownership:** добавлены recognition flow, ownership
  boundaries и полный intent lifecycle от internal `detected` до публикуемых
  states и последующих `superseded`/`expired`; persistent memory не продлевает
  session intent.
- **Journey alignment:** booking закреплён как optional downstream action;
  terminal journey state — progress / next state; `no_action` допустим.
- **Trigger model:** четыре сценария AYLA-DEC-0028 равнозначны; Food Scanner
  не определяет тип intent и не является центром пути.
- **Channels:** применена модель AYLA-DEC-0027 — Mobile App, MAX Mini App и
  MAX Bot поверх общего intent contract; channel-specific semantics и
  MAX-only assumptions удалены.
- **Memory and consent:** Phase 1 session-only отделён от Phase 2 opt-in
  persistent context; прежний intent не становится persistent user fact;
  fail-closed и execution authorization остаются вне resolver ownership.
- **Economic neutrality and attribution:** коммерческие признаки запрещены
  как вход classification/ordering; intent attribution отделена от booking
  conversion и не меняет ownership или resolution truth.
- **Reference migration:** нормативные ссылки переведены на MVP Scope v0.3 и
  MVP User Journey v1.1; metadata дополнена текущими Foundation inputs.
- **Runtime compatibility:** 11 product intent types + `UNKNOWN`, slots,
  Output Contract `0.5` и machine-readable appendix не изменены.
- **Status:** v1.0 — draft / proposed / canonical candidate; approval v0.9.2
  не унаследован автоматически. Product Owner Final Review required.

### v0.9.2 (2026-07-28) — Targeted fixes пакета OQ-9 по приёмке (accept with targeted fixes)

- **Provenance:** `source_version` обновлён до `"0.9.2"` в обоих YAML;
  описания артефактов синхронизированы с версией спецификации.
- **Non-goals:** устранено противоречие с OQ-9 — machine-readable
  реестры объявлены каноническими appendix; в Non-goals остались только
  contract-test fixtures и исполняемые тесты (ayla-ai-core).
- **OQ-10:** частично закрыт — machine-readable Slot Registry
  материализован; отложена только самостоятельная narrative-спецификация
  слотов.
- **OQ-4:** Communicative Class FIND_SPECIALIST финализирован —
  `information` (owner ruling 2026-07-28); двойственность
  «goal/information» устранена в спецификации и реестре; маппинг принят
  как норма (пометка Proposal снята).
- **Versioning реестров:** правило «registry_version всегда равна
  contract_version» отменено; введены независимый `registry_version:
  "1.0"` и `compatible_contract_version: "0.5"` в обоих YAML;
  `contract_version` output contract не изменён.
- **JSON Schema усилена:** `propertyNames` slots ограничены 18 именами
  Slot Registry (`$defs/slot_name`); `missing_required_slots` и
  `candidate_slots` ограничены тем же enum; `secondary_intents[].intent_type`
  ограничен 11 продуктовыми типами (без UNKNOWN); для confirmed
  reference-slots (`service_ref`, `time_slot`, `new_time_slot`,
  `appointment_ref`) требуется непустой `entity_ref`; `evidence_refs` —
  `minItems: 1` + `uniqueItems`; `evidence` — `uniqueItems`.
- **Slot Registry:** `sor_owner` нормализован в `resolution_owner`
  (единый namespace CAP-ID); для `consent_scope`/`revocation_mode`
  добавлен `value_registry: consent-scope-registry`; `context_fact_ref`
  ограничен фактами текущей сессии — исправление persistent memory
  вынесено в memory correction contract Phase 2 (описание
  CORRECT_CONTEXT сужено синхронно в спецификации и реестре).
- Cross-file и смысловые проверки (существование evidence_refs,
  уникальность evidence_id, соответствие slots intent type, пороги
  подтверждения) осознанно оставлены contract tests ayla-ai-core —
  JSON Schema отвечает за форму, тесты — за смысловые связи.
- Статус документа не изменён (approved / accepted).

### v0.9.1 (2026-07-28) — Материализация OQ-9: machine-readable appendix

- Созданы канонические machine-readable артефакты в
  `03 AI System/Contracts/` (canonical source — ayla-knowledge; валидатор
  знаний их не проверяет, т.к. проверяет только `.md`):
  - `intent-registry.yaml` — 11 продуктовых типов + UNKNOWN sentinel,
    slot requirements (`all_of`/`any_of`/`conditional`), execution class,
    Communicative Class (закрытый OQ-4), downstream capability,
    `intent_precedence`;
  - `slot-registry.yaml` — 18 слотов: типы, источники, data categories,
    control metadata, SoR-владение, reference-признак;
  - `intent-output.schema.json` — JSON Schema draft 2020-12 output
    contract: все поля, enums и 9 инвариантов `allOf` (UNKNOWN-комбинации,
    blocked_safety ⇔ blocking-коды, clarification consistency,
    consent_scope_selection).
- Версии реестров привязаны к контракту: `registry_version =
  contract_version = "0.5"`; изменение — через change control; при
  расхождении нормативен текст спецификации.
- OQ-9 обновлён: реестры объявлены machine-readable appendix; fixtures и
  contract tests — implementation-owned артефакты ayla-ai-core (канон
  уходит в ai-core только после приёмки здесь).
- Статус документа не изменён (approved / accepted).

### v0.9 (2026-07-28) — Owner approval и закрытие governance-вопросов

- **OQ-1 закрыт (owner ruling):** семантика confidence bands канонична и
  принадлежит Intent Model; числовые пороги — versioned runtime
  configuration ayla-ai-core, стартовые значения 0.8 / 0.5; настройка —
  configuration change, изменение смысла уровней — architecture change.
  Текст § Confidence and Clarification синхронизирован.
- **OQ-4 закрыт (owner ruling):** Intent Type и Journey Communicative
  Class — ортогональные измерения (resolution/routing vs Journey/UX/
  аналитика); маппинг хранится в machine-readable Intent Registry (OQ-9);
  стартовый маппинг MVP зафиксирован как Proposal.
- **OQ-7 закрыт (owner ruling):** Intent Model владеет формой
  safety-интеграции (`safety_flags`, signal ≠ blocking, инвариант
  `blocked_safety`); составом и семантикой кодов владеет MVP Safety Policy;
  текущие три кода — стартовый MVP-набор, расширение additive.
- OQ-10 дополнен disambiguation: «OQ-10» этого документа — Slot Registry;
  Memory Whitelist относится к Core Domain Model / Memory policy.
- **Статус:** review → **approved**, decision_status: proposed →
  **accepted** (owner approval 2026-07-28). Документ принят как
  implementation candidate; положения получают нормативную силу в объёме
  MVP-среза, дальнейшие изменения — через change control.
- Не закрыты и не блокируют реализацию Phase 1: OQ-2 (timeout — UX-
  настройка), OQ-3 (метрики — Pilot Measurement Plan), OQ-5 (fail-closed
  поведение уже безопасно; финал — Privacy Owner), OQ-6 (audit-след
  достаточен), OQ-8 (persistence — MVP Architecture/Data Inventory),
  OQ-9/OQ-10 (машинные артефакты — следующий этап).
- `contract_version` без изменений (`"0.5"`): сериализуемый output contract
  не менялся.

### v0.8.2 (2026-07-28) — Decision reference correction (KM-IM-1)

- Исправлена ошибочная ссылка KM-IM-1: `AYLA-DEC-0016` заменён на
  `AYLA-DEC-0019` (Intent Detected Lifecycle Boundary, accepted) во всех
  местах документа (OQ-11, Change Log v0.7, v0.8, v0.8.1). AYLA-DEC-0016 —
  Subject Identity Model, не изменялся; collision идентификатора устранена.
- OQ-11 остаётся закрытым: `detected` — internal lifecycle state Intent
  Resolution, resolved by AYLA-DEC-0019.
- Runtime Intent Resolution Output Contract не изменён: `detected` (и
  иные interim/processing состояния) в публичные statuses не добавлялись.
- `contract_version` без изменений (`"0.5"`). Статус документа не изменён
  (review / proposed).

### v0.8.1 (2026-07-28) — Унификация терминологии состояний (editorial)

- Формулировка «итоговые состояния» заменена на «публикуемые intent-level
  состояния, достаточные для следующего решения consumer (первое
  consumer-meaningful состояние)» в § Output Contract (пояснение о
  `detected`) и в тексте закрытия OQ-11: `needs_clarification` — итог
  первого resolution pass, а не всей обработки intent, поэтому термин
  «итоговые» был неточен. Смысл решения KM-IM-1 / AYLA-DEC-0019 не
  изменён; набор публикуемых состояний прежний (`resolved`,
  `needs_clarification`, `unresolved`, `blocked_safety`).
- Историческая запись v0.7 сохранена в исходной редакции.
- `contract_version` без изменений (`"0.5"`). Статус документа не изменён
  (review / proposed).

### v0.8 (2026-07-28) — Регистрация AYLA-DEC-0019 (KM-IM-1)

- OQ-11: ссылка на Decision Log обновлена — решение зарегистрировано
  записью **AYLA-DEC-0019** ([[Ayla Decision Log]], дата решения
  2026-07-27, регистрация 2026-07-28): `detected` — внутреннее non-runtime
  lifecycle-состояние; не входит в `Intent.status`, не сериализуется, не
  отображается в `unresolved`; внутреннее `IntentDetected` не является
  integration contract.
- Impact подтверждён применением: Intent Model v0.7 (этот документ);
  [[Ayla Core Domain Model Specification]] v1.2.2 §7.5; в Core Domain Model
  закрывается устаревший Open Question Architecture №8 о двойной семантике
  `unresolved`.
- `contract_version` без изменений (`"0.5"`): сериализуемая схема не
  менялась. Статус документа не изменён (review / proposed).

### v0.7 (2026-07-27) — Owner ruling KM-IM-1 (OQ-11 закрыт)

- **OQ-11 закрыт owner ruling (2026-07-27):** `detected` зафиксирован как
  внутреннее non-runtime lifecycle-состояние Core Domain Model. Оно не
  входит в сериализуемый output-контракт Intent Model, не используется как
  orchestration state, не означает intent-level readiness или execution
  readiness и не должно использоваться consumers как основание для действия.
  Публичный контракт: итоговые состояния resolution pass — `resolved`,
  `needs_clarification`, `unresolved`, `blocked_safety`; `superseded` и
  `expired` — последующие lifecycle-переходы уже опубликованного результата
  (§ Supersession and Expiry). Первый contract output создаётся после
  первого resolution pass.
- § Output Contract дополнен нормативным пояснением о `detected`; Open
  Questions — OQ-11 переведён в закрытые с текстом решения.
- `contract_version` без изменений (`"0.5"`): сам контракт не менялся,
  правка редакционная (impact: intent_model — no_change; core_domain_model —
  пометить `detected` как internal non-runtime state при канонизации).
- Запись в [[Ayla Decision Log]] на момент v0.7 не создана: оформляется
  отдельной предлагаемой задачей (зарегистрирована как AYLA-DEC-0019,
  2026-07-28 — см. v0.8).
- Статус документа не изменён (review / proposed).

### v0.6 (2026-07-27) — Правки по ревью v0.5 (граница с execution)

- **P0-1:** зафиксирована граница контракта: output однозначно определяет
  только **intent-level readiness**; полная execution readiness
  (authorization decision, user confirmation, доменные предусловия)
  вычисляется orchestration/capability layer. Поля
  `authorization_status`/`user_action_confirmation` в контракт намеренно
  не добавлены. Acceptance Criteria и инварианты переформулированы.
- **P0-2:** значение `clarification_effect` переименовано:
  `follows_completed_safe_action` → `allows_immediate_safe_action`;
  нормативно зафиксировано, что поле разрешает немедленное безопасное
  действие, но не подтверждает его исполнение — завершение подтверждается
  отдельным execution result/event вне Intent Output Contract.
- **P1-1:** пороги подтверждения слотов разведены по классу действия
  (`requirement_satisfaction`): read-only — non-reference `filled`,
  reference — однозначный `entity_ref` всегда; side-effect — `confirmed`.
- **P1-2:** `value_status` объявлен несериализуемым атрибутом
  lifecycle/audit-модели: присутствие значения в `output.slots` имплицитно
  означает `active`.
- **P1-3:** элементы evidence получили стабильный `evidence_id`;
  `evidence_refs` (slots, secondary_intents) ссылаются по ID, не по
  индексу; при secondary materialization элементы копируются с сохранением
  `evidence_id`, происхождение — через `message_id`.
- **P1-4:** инвариант blocked_safety заменён на эквивалентность:
  `blocked_safety` ⇔ `safety_flags ≠ []` ∧ `status_reason =
  safety_gate_blocked`; `status ≠ blocked_safety` ⇒ `safety_flags = []`.
- **P1-5:** зафиксированы допустимые комбинации UNKNOWN: `UNKNOWN` +
  `needs_clarification` ⇒ `clarification_reason = intent_low_confidence`;
  `UNKNOWN` + `unresolved` ⇒ `status_reason ∈ {out_of_scope,
  max_clarification_exceeded, required_context_not_authorized}`.
- **OQ-11 (KM-IM-1):** ревью рекомендует принять owner ruling (без
  изменений для intent model; Core Domain Model помечает `detected` как
  internal non-runtime state) — ожидает owner decision.
- `contract_version` → `"0.5"` (pre-release minor: `evidence_id`,
  переименование значения `clarification_effect`, пороги подтверждения).
- Статус документа не изменён (review / proposed).

### v0.5 (2026-07-27) — Правки по ревью v0.4 (синхронизация перед заморозкой)

- **P0-1:** закрыто внутреннее противоречие REVOKE_CONSENT: enum
  `clarification_reason` расширен значением `consent_scope_selection`;
  добавлено additive-поле `clarification_effect` (`blocks_current_action` |
  `allows_immediate_safe_action`). Неоднозначный запрос теперь выразим без
  нарушения инвариантов: немедленный `session_personalization_stop` +
  уточнение дополнительного governance action. Нормативная формула типа
  уточнения дополнена третьим (governance-level) случаем.
- **P1-1:** формулировка authorization blocking в § Inputs синхронизирована
  с § Authorization ≠ Safety: intent-level blocking — только при
  невозможности определить intent type; невозможность execution не меняет
  `status`.
- **P1-2:** нумерация `contract_version` исправлена: до первой замороженной
  реализации — pre-release `0.x` (текущая `"0.4"`); `"1.0"` — первая
  замороженная JSON Schema с consumer; major/minor правила действуют с
  этого момента.
- **P1-3:** материализация secondary intent определена: orchestration
  передаёт `message_id` + выбранный дескриптор + `evidence_refs`; resolver
  выполняет slot-resolution pass без повторной классификации типа и создаёт
  новый `intent_id`; дескриптор не является executable output.
- **P1-4:** control metadata: формулировка исправлена — извлекаются/
  классифицируются из пользовательского сообщения, но не являются personal
  context facts и не persistence'ятся независимо; `consent_scope` определён
  как requested scope selector, не доказательство активного consent.
- **P2-1:** критерий disambiguation переформулирован реалистично:
  deterministic precedence или обязательная clarification для известных
  пересечений; запрет молчаливого выбора при неустранимой неоднозначности.
- **P2-2:** action readiness разделена на read-only capability execution
  (без подтверждения) и side-effect execution (confirmed slots + явное
  подтверждение); инварианты и Acceptance Criteria обновлены.
- **OQ-11 (KM-IM-1):** оформлен кандидат на owner ruling с impact mapping
  (`intent_model: no_change`; `core_domain_model:
  remove_or_mark_non-runtime interim mapping`).
- Статус документа не изменён (review / proposed).

### v0.4 (2026-07-27) — Правки по ревью v0.3 (детерминированность контракта)

- **P0-1:** FIND_SPECIALIST и BOOK_APPOINTMENT разведены по speech act /
  requested outcome; пример «запишите к Анне» удалён из FIND_SPECIALIST;
  добавлен подраздел «Disambiguation and Precedence» с машинно-проверяемым
  `intent_precedence`; при конфликте измерений приоритет у запрошенного
  side effect.
- **P0-2:** REVOKE_CONSENT получил слот `revocation_mode`
  (`session_personalization_stop` | `consent_record_revocation`) и
  conditional slot requirement: отзыв records требует confirmed
  `consent_scope`. Нормативно: без confirmed `consent_scope` результат
  готов только к session stop; action readiness оценивается для конкретного
  downstream action.
- **P0-3:** `red_zone_context` выведен из `safety_flags` и переопределён
  как safety signal (вход evaluator'а, audit metadata); `safety_flags`
  содержит только blocking decisions (`red_zone_conflict`,
  `competence_boundary`, `unsafe_service_request`); нормативно: detection
  запускает обязательную evaluation, но не является blocking result.
- **P1-1:** secondary intents материализованы в additive-поле
  `secondary_intents` (`intent_type`, `evidence_refs`, `message_position`) —
  очередь восстанавливается downstream детерминированно.
- **P1-2:** `required_context_not_authorized` сужен: `unresolved` только
  при невозможности определить intent type после минимизации входа;
  execution-level authorization deny остаётся в orchestration/capability
  layer и не меняет `resolved`.
- **P1-3:** добавлено additive-поле `clarification_reason`; нормативная
  формула: `needs_clarification` ⇒ intent-level, `resolved` +
  `requires_clarification` ⇒ slot-level.
- **P1-4:** `fact_category`, `consent_scope`, `revocation_mode` определены
  как control metadata — не user-context data categories, не persistence
  персональных данных.
- **P2-1:** формулировка «12 intent types» заменена на «11 продуктовых
  типов + UNKNOWN sentinel»; UNKNOWN исключён из метрик как обработанный
  тип.
- **P2-2:** Acceptance Criteria переписаны с учётом режимов REVOKE_CONSENT
  и downstream-action readiness.
- **KM-IM-1:** добавлен OQ-11 с рекомендуемой owner-формулировкой:
  `detected` — внутреннее состояние доменной сущности Intent (Core Domain
  Model), отдельного представления в Output Contract не имеет; первый
  публикуемый output — после первого resolution pass. Требует owner
  decision.
- `contract_version` → `"1.1"` (additive-поля `clarification_reason`,
  `secondary_intents`, уточнение семантики `safety_flags`; consumers
  отсутствуют, major-нумерация — с первой замороженной реализации).
- Статус документа не изменён (review / proposed).

### v0.3 (2026-07-27) — Правки по ревью v0.2 (контрактные проблемы)

- **P0-1:** slot requirements материализованы (`all_of` / `any_of` с
  `group_id` и `minimum_present`) для всех 12 типов; в Output Contract
  добавлено additive-поле `unmet_slot_requirements`; action readiness =
  `missing_required_slots = []` ∧ `unmet_slot_requirements = []`;
  clarification rule 1 расширено нарушением `any_of`; таблица Intent Types
  переведена на ссылки на slot requirements.
- **P0-2:** Slot Lifecycle переписан: состояние (`value_status:
  active|superseded|expired` × `confirmation_status: filled|confirmed`)
  отделено от события (`change_reason: initial_fill | user_correction |
  intent_shift | clarification_answer`); псевдосостояние `corrected`
  удалено; correction = supersession старого значения + fill нового;
  пример «Анна → Мария» формализован таблицей переходов. В `slots` введён
  стабильный envelope с `confirmation_status` и `evidence_refs` — статус
  подтверждения виден downstream.
- **P0-3:** `consent_scope_missing` удалён из `safety_flags`; новый
  подраздел «Authorization ≠ Safety»: необязательные неавторизованные
  категории исключаются fail-closed без блокировки resolution;
  authorization blocking — только `unresolved` +
  `status_reason = required_context_not_authorized` (downstream
  `CONSENT_REQUIRED`); `SAFETY_BLOCKED` отделён от `CONSENT_REQUIRED`.
- **P1-1:** `contract_version` отделена от версии документа: runtime
  output contract получил собственную версию `"1.0"`; редакционные
  изменения спецификации её не меняют.
- **P1-2:** деструктивный fallback REVOKE_CONSENT («отозвать все затронутые
  scopes») удалён из нормативного текста; зафиксирован безопасный минимум
  (fail-closed в сессии + отзыв только через Consent Management по
  подтверждённому набору scopes); финальное поведение оставлено в OQ-5.
- **P1-3:** `resolution_reason` переименован в `status_reason` и расширен
  до покрытия всех терминальных/блочных статусов (`intent_shift`,
  `session_expired`, `clarification_timeout`, `safety_gate_blocked`,
  `required_context_not_authorized`); инвариант обязательности для
  terminal statuses.
- **P1-4:** ordering multi-intent пересмотрен: governance-приоритет
  (REVOKE_CONSENT) → message order; informational выносится перед
  actionable только как prerequisite информированного подтверждения; слепой
  приоритет класса ASK_* отменён.
- **P1-5:** evidence разделён на runtime-форму (`{message_id, fragment}`)
  и audit-форму (`{message_id, evidence_type, slot_name, fragment_hash}`);
  нормативно запрещён автоматический перенос дословного fragment в
  долгосрочный audit/attribution.
- **P1-6:** определён единый slot value envelope (`raw_value`,
  `normalized_value`, `entity_ref`, `confirmation_status`,
  `evidence_refs`); scalar-значения в `slots` запрещены.
- **P2-1:** ссылки на номера замечаний прошлых ревью удалены из
  нормативного текста (история — только в Change Log).
- **P2-2:** Acceptance Criteria переписаны как проверки исполнимости
  модели (slot requirements, action readiness, status reasons, раздельные
  deny, однозначный correction transition, неблокирующий optional denial).
- **P2-3:** пакет fixtures/реестров (intent-registry, slot-registry,
  JSON Schema, test cases) зафиксирован как следующий шаг в OQ-9 — вне
  содержимого этого документа.
- Статус документа переведён draft → review (owner decision 2026-07-27,
  после закрытия P0 ревью v0.2); decision_status остаётся `proposed` —
  канонизация не выполнялась.

### v0.2 (2026-07-27) — Правки по ревью v0.1 (requires_changes)

- **P0-1:** добавлено additive-поле `contract_version` в Output Contract;
  инвариант обязательности; правило версионирования (additive = minor,
  breaking = major + change control).
- **P0-2:** новый раздел § Slot Lifecycle: состояния
  `filled → confirmed → corrected → superseded` / `expired`, правило
  единственного активного значения, связь с CORRECT_CONTEXT и session-only
  expiry.
- **P1-1:** разделены resolution и action readiness: `status = resolved`
  больше не требует полноты слотов; явный список условий actionable
  execution; `needs_clarification` зарезервирован для неопределённости
  самого intent и конфликтов.
- **P1-2:** зафиксировано владение значениями слотов (SoR — доменные
  capabilities; Intent Model владеет только именами и правилами заполнения);
  отражено в § Owns / § Does not own / § Slots.
- **P1-3:** `UNKNOWN` переформулирован как sentinel-состояние resolver'а
  (тип сохранён — реестр заморожен Roadmap §3.1); добавлено additive-поле
  `resolution_reason`; execution по UNKNOWN запрещён инвариантом.
- **P1-4:** семантика колонки safety-sensitive уточнена: тип определяет
  обязательность safety evaluation, контекст — её исход; блокировка только
  по непустым `safety_flags`.
- **P1-5:** `evidence` формализован: элемент `{message_id, fragment}`;
  offsets отложены, persistence `message_id` присоединена к OQ-8.
- **P1-6:** multi-intent получил deterministic ordering: informational →
  actionable, внутри класса — message order; actionable — строго
  последовательно и только с подтверждением.
- **P2:** Acceptance Criteria переведены в чек-лист (P2-3);
  machine-readable Intent Registry и вынос Slot Registry зафиксированы как
  OQ-9/OQ-10 (P2-1, P2-2) — без расширения MVP scope.
- Статус документа не изменён (draft / proposed); перевод в review — после
  owner review. Рекомендация ревью «Implementation Candidate → contract
  tests → прогон на реальных диалогах» относится к следующим шагам и в
  статусной модели schema v1.12 отдельного значения не имеет.

### v0.1 (2026-07-27) — Initial draft

- Документ создан как критический predecessor по AYLA-DEC-0011 в объёме
  MVP-среза (AYLA-DEC-0014, Roadmap §3.1).
- Реестр intent types и состав output contract перенесены дословно из
  Roadmap §3.1 без расширения.
- MVP slot registry, пороги confidence как runtime-пороги, лимит
  clarification, правила multi-intent/correction, операционализация
  supersession/expiry и состав `safety_flags` оформлены как Proposal.
- Открытые вопросы OQ-1…OQ-8 зафиксированы без подмены решений.
