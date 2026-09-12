---
node_id: ayla.architecture.goal-outcome-semantic-model-working-design
title: Ayla Goal Outcome Semantic Model Working Design
type: specification
status: draft
decision_status: proposed
canonical_status: draft
version: "0.9"
owner: Product Architecture
priority: P1
knowledge_area:
  - architecture
domain:
  - recommendation
  - intent
concerns:
  - governance
  - explainability
  - safety
system_owner:
  - ayla-recommendation
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
created: 2026-08-20
updated: 2026-08-22
review_cycle: before-major-change
depends_on:
  - "[[Ayla Intent Model Specification]]"
  - "[[Ayla MVP Recommendation Contract]]"
  - "[[Ayla Glossary]]"
related:
  - "[[Ayla MVP User Journey Specification]]"
  - "[[Ayla Decision Log]]"
  - "[[OWNER_DECISION_REGISTER]]"
  - "[[BOT-001 First Contact Specification]]"
  - "[[Ayla MVP C01 C02 UX Inventory]]"
---

# Ayla Goal Outcome Semantic Model Working Design

> **Статус:** Draft v0.9 — Working Design checkpoint. **Non-canonical.**
>
> **2026-09-12 (PROPOSED — awaiting owner approval; Final Reconciliation v1.0
> §6.2 A1, §6.3):** дельты §20 (D-1…D-7, D-9, D-10) **применены amendment A1**
> к [[Ayla MVP Recommendation Contract]] v1.0 (proposed); D-8 закрыт пакетом 2
> B9 — семейства `ADDRESS / SUPPORT / RECOVER / OBSERVE` provisional для
> Controlled Pilot (вариант `INTERVENE / SUPPORT / OBSERVE` не принят).
> Документ остаётся non-canonical evidence base для Goal/Outcome Taxonomy
> Design (§23); текст ниже не менялся.
> Документ фиксирует архитектурный checkpoint по семантике Goal / Outcome /
> Recommendation перед проектированием Goal/Outcome Taxonomy и подготовкой
> amendment к [[Ayla MVP Recommendation Contract]].
>
> Документ разделяет четыре класса утверждений и не смешивает их:
>
> 1. **Established Canon** — подтверждено действующими approved-документами
>    и зафиксированными owner-решениями.
> 2. **Owner directions** — направления, принятые владельцем в рабочем разборе
>    и зафиксированные этим документом; их governance-статус этим документом
>    не повышается.
> 3. **Working model / proposal** — рабочие гипотезы, не являющиеся каноном.
> 4. **Open questions** — нерешённые вопросы, не закрываемые по умолчанию.
>
> **Дата checkpoint:** 2026-08-22.

---

## 1. Status / purpose

- `status: draft`, `decision_status: proposed`, `canonical_status: draft`.
- Назначение: сохранить уже установленный канон, принятые owner directions,
  текущие рабочие гипотезы и открытые вопросы вокруг семантики
  Goal / Outcome / Recommendation, чтобы дальнейшая архитектурная работа не
  восстанавливала эти решения из истории обсуждений.
- Документ не является Goal/Outcome Taxonomy и не вводит новый канонический
  registry.

## 2. Why this Working Design exists

Рабочий разбор границы между User Intent, Transformation Goal, желаемыми
результатами пользователя, контекстом и Canonical Recommendation выявил
ограничения и направления, которые не зафиксированы ни в одном действующем
документе как единая картина:

- [[Ayla Intent Model Specification]] v1.0 (Active Canon) фиксирует границу
  Intent ↔ Transformation Goal, но не моделирует желаемые результаты.
- [[Ayla MVP Recommendation Contract]] v0.4 (`status: draft`,
  `decision_status: proposed`) содержит §27–§33 о Goal Resolution, Outcome
  Resolution и NBA Taxonomy, но сам является предложенным, а не утверждённым
  каноном, и предполагает линейную цепочку `Goal → Outcome`, которая в
  рабочем разборе поставлена под вопрос.

Этот документ — checkpoint, а не замена существующего канона.

## 3. Authority and non-goals

### 3.1. Authority

- Канонические утверждения опираются только на документы репозитория
  (см. §4 и §24). Рабочий разбор и обсуждения не являются каноническим
  авторитетом.
- Там, где owner direction существует только в рабочем разборе, он помечен
  как «owner direction, зафиксированное этим Working Design», а не как
  существующий канон.

### 3.2. Non-goals

Эта задача и этот документ **не**:

- создают каноническую Goal Taxonomy;
- создают каноническую Outcome Taxonomy;
- создают Subject/Factor/Target Registry;
- изменяют Intent Output Contract ([[Ayla Intent Model Specification]],
  Output Contract 0.5);
- изменяют [[Ayla MVP Recommendation Contract]] (возможные amendments —
  только как список в §20);
- изменяют C01/C02 designer tasks и UX-спецификации;
- изменяют runtime code, DB/API schemas;
- вводят safety rules или medical/health semantics;
- канонизируют `INTERVENE / SUPPORT / OBSERVE` или любой другой набор
  NBA families;
- создают новые Decision IDs — governance этого не требовал, а owner
  authority для новых решений здесь не оформлялась;
- создают registry, storage, JSON Schema, Pydantic- или DB-модель для
  `SemanticResolutionResult` — OD-SR-1…6 (§5) фиксируют только
  working/conceptual shape (§11.2).

## 4. Established canonical constraints

Подтверждено действующим каноном (approved-документы и реестр owner-решений).

### 4.1. Intent ≠ Transformation Goal

[[Ayla Intent Model Specification]] v1.0 (`status: approved`,
`canonical_status: approved`, Active Canon, 2026-08-08), раздел
«Transformation Goal and Intent»:

- User Intent — «текущее структурированное представление того, что
  пользователь пытается изменить, понять, выбрать или сделать сейчас».
- Transformation Goal — «canonical product concept, принадлежащий
  пользователю… описывает желаемое направление пути»; отдельный Domain
  Aggregate для Transformation Goal этим документом не вводится.
- «Intent не владеет Transformation Goal и не заменяет её». Intent может
  поддерживать Goal, уточнять её, временно не иметь с ней явной связи.

Owner-решение: AYLA-DEC-0043 (OD-7, Intent Boundary, 2026-08-04,
[[OWNER_DECISION_REGISTER]]): «Transformation Goal ≠ intent».

### 4.2. Связь Intent ↔ Goal может быть не установлена

[[Ayla Intent Model Specification]] v1.0, § Transformation Goal and Intent
и § Inputs:

- если связь с целью неизвестна, resolver не выдумывает её: связь остаётся
  `unknown/not_established`, а Ayla либо задаёт минимальный вопрос, либо
  продолжает с минимальным рабочим намерением;
- «resolver не создаёт Goal из догадки».

Owner-решения: AYLA-DEC-0043 (OD-7) — неизвестная связь intent↔goal не
выдумывается; AYLA-DEC-0045 (OD-9, Recommendation Model) — «рекомендация
привязана к Transformation Goal, **если связь установлена**».

### 4.3. Goal не входит в Intent Resolution Output

[[Ayla Intent Model Specification]] v1.0, § Recommendation Input Boundary:

- Intent Resolution Output 0.5 остаётся единственным выходом resolver'а;
  новые поля (`goal_id`, `goal_ref`, `goal_relationship` и т.п.) в него не
  вводятся;
- downstream Recommendation/orchestration имеет два логически раздельных
  входа: Intent Resolution Output и разрешённый runtime context, собранный
  вне output resolver'а (Transformation Goal relationship — если установлена,
  authorization/consent state, результат safety evaluation).

### 4.4. Intent Slot Registry не является Goal/Outcome semantic model

[[Ayla Intent Model Specification]] v1.0, § Slots: реестр слотов
(`service_interest`, `service_ref`, `service_category`,
`provider_preference`, `budget`, `context_fact`, `consent_scope` и др.)
служит intent resolution и capability routing. Слотов `subject`, `factor`,
`target`, `desired_outcome` в реестре нет; их нельзя добавлять только для
решения Goal/Outcome задачи.

### 4.5. Goal — доменная семантика, не услуга и не действие

[[Ayla Glossary]]: Goal — «желаемый результат на уровне изменения
состояния… не является услугой или действием». Transformation Goal
провозглашён центральной доменной сущностью (AYLA-DEC-0026,
[[OWNER_DECISION_REGISTER]]); SoT для Transformation Goal — canonical
product concept / Journey, для Recommendation — Recommendation Contract
(AYLA-DEC-0062).

### 4.6. Goal — сквозная концепция, а не обязательная линейная стадия

AYLA-DEC-0039 (OD-3, Journey Stages, 2026-08-04): «Goal, LDT и Progress
оформлены как сквозные концепции, а не обязательные линейные стадии»;
этапы booking — опциональная ветка. AYLA-DEC-0037 (OD-1, Journey
Philosophy): lifecycle `Conversation → Understanding → Recommendation →
Execution → Learning` расширен якорем Transformation Goal.

Важно: это решения о нелинейности journey-стадий. Решения «journey или
рекомендация могут существовать вообще без установленного Goal» в
репозитории как owner decision **не зафиксировано** (см. OD-GO-1, §5).

### 4.7. `no_action` — валидный результат; safety — гейт

- AYLA-DEC-0045 (OD-9): `no_action` — полноценный объяснимый результат;
  LLM не ranking authority; acceptance ≠ booking.
- [[Ayla MVP Recommendation Contract]] v0.4, §23 (R-NBA-5): «Safety — это
  gate, а не Recommendation family»; §32: `SAFETY_BOUNDARY` —
  RecommendationResult (runtime-имя `SAFETY_BLOCKED`), не является NBA.

Статусная оговорка: сам Recommendation Contract v0.4 — `status: draft`,
`decision_status: proposed`; его содержимое — текущий proposed contract,
а не approved canon. Owner-решение AYLA-DEC-0045 при этом зафиксировано
независимо и является DECIDED.

### 4.8. Outcome используется downstream как post-action результат

[[Ayla Intent Model Specification]] v1.0, § Orchestration Intent Model:
«→ confirmed downstream action or no_action → outcome / continuity input →
progress / next state». То есть слово `outcome` в действующем каноне уже
занято для результата **после** действия, питающего continuity/progress
(см. также AYLA-DEC-0048, OD-12, Learning Loop: `Outcome → Feedback →
Optional Memory Proposal → …`).

## 5. Owner directions captured

Направления, принятые владельцем в рабочем разборе и зафиксированные этим
Working Design. Если иное не указано, в репозитории отдельной записи об
этих решениях нет; их governance-статус — «owner direction, captured by
this Working Design», не canon.

### OD-GO-1. Goal не является обязательным родителем Outcome

Не использовать модель `Intent → Goal REQUIRED → Outcome`. Допускается
journey, в котором пользователь достаточно ясно выразил желаемое изменение
без отдельного установленного Goal:

```text
«Хочу убрать отёчность»
↓
normalized desired outcome REDUCE(PUFFINESS)
↓
Goal может оставаться not_established,
если Decision Policy не требует его уточнения.
```

Совместимость с каноном: §4.2 и §4.6 (unknown/not_established допустимо;
стадии нелинейны). Смежные решения существуют, но сама формулировка
«Goal optional для recommendation journey» как owner decision в репозитории
ранее не записана.

### OD-GO-2. Не спрашивать Goal ради заполнения схемы

Если имеющихся Outcomes + разрешённого Context достаточно для
Recommendation Decision, Ayla не должна задавать дополнительный вопрос
только для получения Goal. Goal уточняется только когда его отсутствие
действительно влияет на решение, приоритет, допустимость или требуемое
объяснение.

### OD-GO-3. C01 option не обязана быть 1:1 Domain Goal

C01 остаётся human-facing intent entry layer. Варианты C01 могут
резолвиться в разные semantic outputs: Domain Goal; Outcome discovery
cluster; Journey Mode; resolution/discovery state; комбинацию этих
объектов. UX C01 не нужно переделывать только потому, что внутренняя
semantic model становится точнее.

### OD-GO-4. C02 поддерживает 1..N результатов

C02 (включая UX-режим, обозначавшийся «C02.4») должен позволять
пользователю подтвердить несколько подходящих
интерпретаций/результатов через multi-select, когда несколько вариантов
действительно соответствуют его словам. Semantic Resolution должен уметь
вернуть `1..N` нормализованных desired outcomes.

Связь с репозиторием: [[Ayla MVP Recommendation Contract]] v0.4 §28 уже
допускает `outcomes[1..N]` и называет «явная таксономия / multi-select»
одним из источников Outcomes; но multi-select как поведение этапа C02
отдельным решением не зафиксирован (см. delta D-6, §20).

Уточнение (v0.5, OD-CI-1): multi-select применяется только к unresolved
candidate interpretations; несколько уже resolved Desired Outcomes идут
по resolved path (`RESOLVED → SKIP`) и не требуют `CHOOSE_MANY` (§11.3).

Это направление формализовано как OD-CLAR-1 (§5): «C02.4» — UX/design label
режима `CHOOSE_MANY` внутри единого `Adaptive Clarification`, а не отдельная
semantic/domain стадия.

### OD-GO-5. Recommendation target не получает независимую taxonomy без необходимости

Не создавать отдельный `Recommendation Target Registry`, пока не проверено,
может ли Recommendation target ссылаться на общие нормализованные domain
concepts, используемые также Outcome/Context слоями (см. §14).

### OD-GO-6. Execution route не является частью semantic core NBA

Рабочая граница:

```text
C04 — Canonical Recommendation — WHAT + WHY
──────── execution boundary ────────
C05 — Execution Mapping — HOW
```

Если `action_type` означает способ исполнения (`SERVICE_PATH` и т.п.), он
должен находиться downstream от Canonical Recommendation. Связь с текущим
контрактом — см. delta D-7, §20.

### OD-C01-1. C01 = Hybrid First Contact

C01 — Hybrid First Contact: free text — primary input; Quick Actions —
contextual UX assistance, а не Goal/Outcome taxonomy.

Canon-опора: [[BOT-001 First Contact Specification]] v1.0 (`approved`,
2026-08-12) — hybrid entry surface (free text + contextual Quick Actions);
owner-решение A-BOT-001-Q4 (APPROVED, 2026-08-12). Inventory-опора:
[[Ayla MVP C01 C02 UX Inventory]] — канонизированного фиксированного набора
C01 labels нет; free text является primary.

### OD-C01-2. Одновременно 3–5 contextual Quick Actions

На C01 одновременно показывается 3–5 contextual Quick Actions. Конкретный
user-facing copy не является canonical semantic taxonomy и может зависеть от
greeting/user state. Quick Action labels не объявляются каноническими
Domain Goal codes (согласуется с OD-GO-3).

### OD-C01-3. Единый semantic-resolution pipeline

Quick Action и эквивалентная natural-language формулировка проходят через
один semantic-resolution pipeline. Не допускается отдельный hardcoded путь
Quick Action → Goal/Outcome: выбор Quick Action порождает user expression,
которая резолвится тем же путём, что и free text.

### OD-CLAR-1. «C02.4» — UX/design label режима CHOOSE_MANY

`C02.4` не является отдельным semantic/domain stage. Это UX/design label
для режима `CHOOSE_MANY` внутри единого `Adaptive Clarification`
(OD-CLAR-2). Если `C02.4` уже используется как screen identifier в
UX/Linear, немедленное переименование не требуется — зафиксирована только
архитектурная граница.

### OD-CLAR-2. Четыре режима Adaptive Clarification

Adaptive Clarification концептуально поддерживает минимум четыре режима:

- `SKIP` — semantic state достаточен, clarification UI не нужен;
- `CONFIRM_ONE` — одна вероятная интерпретация требует подтверждения;
- `CHOOSE_MANY` — несколько одновременно допустимых интерпретаций;
  пользователь может подтвердить несколько;
- `ASK_CONTEXT` — данных недостаточно для полезного набора интерпретаций;
  задаётся один наиболее информативный вопрос.

Примерный UX copy этим направлением не канонизируется.

### OD-CLAR-3. Совместимость интерпретаций определяет semantic layer

Multi-select не является универсальным UI-правилом. Совместимость
интерпретаций и `single/multiple` selection mode определяет semantic layer;
UI только отображает разрешённое поведение. Compatibility
algorithm/schema/registry этим документом не проектируются (см. OQ-GO-12,
§22).

### OD-CLAR-4. Minimization и re-resolution

Clarification запускается только при недостаточности, неоднозначности или
необходимости подтверждения semantic state. За один conversational turn
показывается один набор интерпретаций либо задаётся один наиболее
информативный вопрос. После ответа выполняется semantic re-resolution.
Новые confidence thresholds, information-gain formulas и clarification
limits этим документом не вводятся (существующие пороги — runtime config
Intent Model, §19).

### OD-SR-1. SemanticResolutionResult — отдельный downstream semantic object

`SemanticResolutionResult` — отдельный downstream semantic object. Он не
расширяет и не заменяет Intent Resolution Output 0.5
([[Ayla Intent Model Specification]], §4.3). Граница:

```text
Intent Resolution Output 0.5
+ User Expression
+ allowed Context
        ↓
Goal / Outcome Semantic Resolution
        ↓
SemanticResolutionResult
```

Intent остаётся во владении Intent Resolution и не дублируется в
`SemanticResolutionResult` без canonical requirement.

### OD-SR-2. Четыре состояния resolution_status

```text
RESOLVED
NEEDS_CONFIRMATION
AMBIGUOUS
INSUFFICIENT
```

- `RESOLVED` — нет blocking semantic uncertainty; это **не** означает
  decision sufficiency (OD-SR-6).
- `NEEDS_CONFIRMATION` → обычно `CONFIRM_ONE`.
- `AMBIGUOUS` → `CHOOSE_MANY` только когда semantic layer подтвердил
  совместимость интерпретаций (OD-CLAR-3); не любой `AMBIGUOUS` является
  `CHOOSE_MANY` — правила зафиксированы OD-CI-1…10 (§11.3).
- `INSUFFICIENT` → обычно `ASK_CONTEXT`.

Thresholds и classifier этим направлением не проектируются
(OQ-GO-13, §22).

### OD-SR-3. Goal optional при любом resolution_status

`goal = not_established` совместим с `resolution_status = RESOLVED`.
Отсутствие Transformation Goal само по себе не делает resolution
недостаточным — согласуется с OD-GO-1/OD-GO-2 и §4.2. Goal не
синтезируется ради заполнения схемы.

### OD-SR-4. Resolution и readiness — разные оси

Наряду с `resolution_status` вводится working distinction:

```text
semantic_readiness:
  READY_FOR_DECISION
  DISCOVERY_REQUIRED
```

Пример:

```text
«Не знаю, с чего начать — помоги»
resolution_status  = RESOLVED
semantic_readiness = DISCOVERY_REQUIRED
```

Discovery — не semantic failure. Если `journey_mode` существует отдельно,
он автоматически не схлопывается с `semantic_readiness`.

### OD-SR-5. Минимум один Desired Outcome для READY_FOR_DECISION

`READY_FOR_DECISION` требует минимум один sufficiently resolved Desired
Outcome:

```text
READY_FOR_DECISION ⇒ desired_outcomes count >= 1
```

При `DISCOVERY_REQUIRED` Desired Outcome может отсутствовать: на уровне
объекта `desired_outcomes[]` допускает `0..N`, но recommendation-ready
state требует `>= 1`. Финальная DesiredOutcome schema и формальная функция
sufficiently resolved здесь не определяются (OQ-GO-10, OQ-GO-13, §22).

### OD-SR-6. Semantic Sufficiency ≠ Decision Sufficiency

- **Semantic Sufficiency** — достаточно ли Ayla поняла, чего пользователь
  хочет / в каком semantic journey state он находится.
- **Decision Sufficiency** — достаточно ли разрешённых decision-relevant
  context facts для Recommendation Decision Policy
  ([[Ayla MVP Recommendation Contract]] §30, proposed).

RecommendationContext gap не переводит уже `RESOLVED` semantic result в
`INSUFFICIENT`.

### OD-CI-1. Resolved plurality ≠ clarification plurality

Несколько уже resolved Desired Outcomes не требуют `CHOOSE_MANY`. Если
пользователь явно выразил несколько Outcomes и ambiguity отсутствует,
допустим путь `RESOLVED → SKIP`:

```text
MULTIPLE RESOLVED OUTCOMES != CHOOSE_MANY
```

`CHOOSE_MANY` применяется к unresolved candidate interpretations,
требующим подтверждения, а не к множественности уже разрешённых
результатов.

### OD-CI-2. Одна InterpretationGroup = одна semantic ambiguity

Candidates одной `InterpretationGroup` являются вариантами разрешения
одной конкретной неоднозначности. Не смешивать в одной selection group
Goal, Desired Outcome, Journey Mode, Context и другие semantic dimensions
только потому, что они обнаружены одновременно.

### OD-CI-3. selection_mode принадлежит semantic layer

```text
selection_mode = ONE | MANY
```

- `ONE` — одновременно принять несколько candidates нельзя;
- `MANY` — можно подтвердить более одного candidate.

UI не вычисляет compatibility/selection mode, а только отображает
разрешённое semantic layer поведение (развивает OD-CLAR-3).

### OD-CI-4. Compatibility относится к полной interpretation

Compatibility нельзя определять только по Outcome/target code.
Учитываются direction, target, scope и релевантные semantic qualifiers.
Глобальный compatibility registry не создаётся.

### OD-CI-5. MVP без сложного compatibility graph

Для `MANY` любое непустое подмножество candidates должно быть допустимо.
Pairwise matrix, graph, mutual exclusions и conditional subset constraints
не проектируются. Если нужны сложные комбинационные ограничения —
resolver перестраивает clarification: разделяет ambiguity или запрашивает
context (один наиболее полезный clarification за turn, OD-CLAR-4). Это
MVP simplification.

### OD-CI-6. CandidateInterpretation = proposal

`CandidateInterpretation` — гипотеза semantic meaning для подтверждения,
а не final Desired Outcome / Goal / Journey Mode /
SemanticResolutionResult.

### OD-CI-7. Presentation ≠ semantic identity

Концептуально:

```text
CandidateInterpretation
├── temporary/current-cycle identity
├── presentation
└── proposed_semantic_payload
```

User-facing copy не является canonical semantic identity и не
канонизируется.

### OD-CI-8. Selection всегда ведёт к Semantic Re-resolution

Нельзя напрямую мутировать `desired_outcomes[]`, Goal или Journey Mode
выбранным candidate:

```text
original semantic state
+ user selection / confirmation evidence
        ↓
Semantic Re-resolution
        ↓
new SemanticResolutionResult
```

### OD-CI-9. non-selection ≠ durable rejection

Для `CHOOSE_MANY` минимум различаются концептуальные состояния `selected`
и `not_selected`. `not_selected` означает отсутствие подтверждения только
в текущем clarification cycle и не становится durable negative
preference, memory или rejection. Explicit rejection требует отдельного
явного сигнала/контракта; этим документом не проектируется.

### OD-CI-10. Metadata не определяет semantic identity

Confidence, ranking, provenance, evidence refs могут быть
resolution/audit metadata, но не semantic identity candidate. Их runtime
representation этим документом не решается (OQ-GO-14, §22). Confidence
thresholds не вводятся.

### OD-DC-1. Minimal Desired Change Model (2026-08-22)

Минимальная архитектурная композиция DesiredOutcome (owner direction, не
canon):

```text
DesiredOutcome =
VALID(
  typed target,
  DesiredChangeSpecification,
  optional intrinsic scope
)

DesiredChangeSpecification:
  direction?             0..1
  desired_state/value?   0..1

Invariant:
  at least one of direction / desired_state/value must be established.
```

- Валидны три базовые формы: только direction; только desired
  state/value; direction + desired state/value.
- Если установлены и direction, и desired state/value, они не должны
  образовывать известное семантическое противоречие при наличии
  применимого baseline/Actual State. Compatibility
  algorithm/matrix/registry этим документом не проектируются; Actual State
  не становится обязательным полем DesiredOutcome или
  DesiredChangeSpecification: при неизвестном baseline explicit desired
  state/value остаётся валидным.
- Direction может быть explicit, derived (`Actual State + Desired State →
  derived Direction`) или not_established. Direction provenance
  (explicit/derived/inferred) — resolution/evidence metadata, а не часть
  semantic identity: обязательное поле вида `direction_source` в canonical
  semantic shape не вводится; если такая информация нужна runtime для
  explainability/audit/replay, она проектируется отдельно.
- `desired_state/value` описывает желаемое состояние самого typed target;
  архитектурно это не обязательно число, enum, строка, единица измерения
  или threshold. Exact value model/type system — отдельный будущий
  taxonomy/runtime вопрос; Value Registry, Unit Registry, Measurement
  Schema, JSON Schema, Pydantic- и DB-модели не создаются.
- External temporal, comparative и execution constraints (deadline, event
  date, time-to-effect, persistence expectation, comparative
  reference/baseline, execution cadence, service/provider preference,
  price/budget, availability, execution route) автоматически не входят в
  DesiredChangeSpecification (подтверждает GO2-W13, §13.1).
- Несколько независимых изменений одного пользовательского запроса
  представляются по возможности несколькими DesiredOutcome, а не одним
  перегруженным DesiredChangeSpecification; `1..N` directions и `1..N`
  desired states не вводятся без фактического контрпримера.

Structural gate OQ-GO-2: по пяти stress-test группам (§13.1) не найдено
случая, не представимого через `typed target + DesiredChangeSpecification
+ optional intrinsic scope` без добавления ещё одного обязательного
semantic dimension:

```text
NO ADDITIONAL REQUIRED DIMENSION IDENTIFIED
```

Это закрывает **архитектурную часть** OQ-GO-2 (§22). Закрытие не означает
готовности Direction Taxonomy, Target Type Taxonomy, Target Registry,
value model, scope schema, direction-target validity registry, runtime
schema, parser/classifier, inference algorithm, safety semantics или
amendment к Recommendation Contract.

Статус OD-C01-1…3, OD-CLAR-1…4, OD-SR-1…6, OD-CI-1…10 и OD-DC-1: принятые
owner directions (OD-C01/OD-CLAR — 2026-08-20; OD-SR и OD-CI — 2026-08-21;
OD-DC — 2026-08-22), зафиксированы этим Working Design; governance-статус
этим документом не повышается, они не являются canon и не создают
глобальных AYLA-DEC IDs.

## 6. Problem statement

Действующий канон разводит Intent и Transformation Goal (§4.1–§4.3), но не
отвечает на вопросы:

1. Чем является «то, какое изменение хочет пользователь» как нормализованный
   semantic object — и обязан ли он подчиняться уже установленному Goal?
2. Как UX-входы C01/C02 отображаются на внутреннюю семантику, не становясь
   автоматически каноническими Domain Goal codes?
3. Из чего состоит semantic identity Canonical Recommendation и где проходит
   граница между ней и маршрутом исполнения?
4. Как избежать дублирующих vocabularies target/subject/factor между
   Outcome-, Context- и Recommendation-слоями?

Текущий proposed Recommendation Contract v0.4 предполагает линейную
цепочку `Intent Resolution → Goal Resolution → Outcome Resolution` и вход
Outcome Resolution = `goal + user expression` (§27–§28), что конфликтует с
owner directions OD-GO-1/OD-GO-2 (см. §20).

## 7. Terminology

| Термин | Статус | Значение |
|---|---|---|
| User Intent | canon ([[Ayla Intent Model Specification]] v1.0) | Что пользователь пытается изменить/понять/выбрать/сделать **сейчас** |
| Transformation Goal | canon (product concept; AYLA-DEC-0026, AYLA-DEC-0062) | Долгоживущее желаемое направление пути пользователя; не Domain Aggregate по Intent Model |
| Domain Goal | working | Decision-relevant кодифицированный Goal; состав не утверждён |
| Desired Outcome | **proposed terminology** | Желаемое изменение/сохранение состояния **до** Recommendation/action |
| Actual Outcome | working name для canon-понятия `outcome` (§4.8) | Фактический результат **после** action; continuity/progress input |
| Semantic Resolution | **proposed architectural layer** | Слой разрешения Goal?/Outcomes/Journey Mode?; не утверждён |
| Journey Mode | **proposed entity** | Режим journey (event preparation, maintenance, discovery); не утверждён |
| Canonical NBA | proposed contract ([[Ayla MVP Recommendation Contract]] v0.4) | Canonical Next Best Action — «что сделать» |
| Adaptive Clarification | owner direction (OD-CLAR-1…4) / working mechanism | Единый слой уточнения: `SKIP / CONFIRM_ONE / CHOOSE_MANY / ASK_CONTEXT`; «C02.4» — UX/design label режима `CHOOSE_MANY` |
| SemanticResolutionResult | owner direction (OD-SR-1…6) / conceptual shape | Отдельный downstream semantic object результата Goal/Outcome Semantic Resolution; не заменяет Intent Resolution Output 0.5; не canonical runtime schema |
| resolution_status | owner direction (OD-SR-2) | `RESOLVED / NEEDS_CONFIRMATION / AMBIGUOUS / INSUFFICIENT` |
| semantic_readiness | owner direction (OD-SR-4) / working distinction | `READY_FOR_DECISION / DISCOVERY_REQUIRED`; ось, ортогональная `resolution_status` |
| Semantic Sufficiency | owner direction (OD-SR-6) | Достаточность понимания, чего хочет пользователь / в каком semantic journey state он находится |
| Decision Sufficiency | proposed contract ([[Ayla MVP Recommendation Contract]] v0.4 §30) + owner direction на разделение (OD-SR-6) | Достаточность разрешённых decision-relevant context facts для Recommendation Decision Policy |
| C01–C05 | рабочие коды этапов, введённые Recommendation Contract v0.4 §34 | Маппинг на этапы Journey «подлежит подтверждению» |
| CandidateInterpretation | owner direction (OD-CI-6…7) / conceptual | Гипотеза semantic meaning для подтверждения; не final Outcome/Goal/Journey Mode; `presentation` отделена от `proposed_semantic_payload` |
| InterpretationGroup | owner direction (OD-CI-2…3) / conceptual | Набор candidates одной semantic ambiguity + `selection_mode` |
| selection_mode | owner direction (OD-CI-3) | `ONE | MANY`; задаётся semantic layer, UI только отображает |
| not_selected | owner direction (OD-CI-9) / conceptual | Отсутствие подтверждения в текущем clarification cycle; не durable rejection |
| DesiredChangeSpecification | owner direction (OD-DC-1) / conceptual shape | Минимальная semantic shape желаемого изменения typed target: `direction?` 0..1 + `desired_state/value?` 0..1, минимум один установлен; direction provenance (explicit/derived) — resolution/evidence metadata; не runtime schema |

## 8. Intent / Goal boundary

Канон (§4.1–§4.3): Intent отвечает на вопрос «что пользователь пытается
сделать сейчас»; Transformation Goal — отдельный, более долгоживущий
смысловой объект; связь может быть `unknown/not_established`; resolver не
выдумывает Goal.

Запрещённая модель (не принятая архитектура):

```text
Intent → mandatory Goal → Outcome
```

Текущее рабочее направление (working, не canon):

```text
First Contact (C01)
        |
        v
User Expression (free text или Quick Action — один pipeline, OD-C01-3)
        |
        v
Intent Resolution
        |
        v
Goal/Outcome Semantic Resolution (proposed)
        |
        v
Adaptive Clarification (owner direction, OD-CLAR-1…4)
        +--> SKIP          — semantic state достаточен
        +--> CONFIRM_ONE   — подтверждение одной интерпретации
        +--> CHOOSE_MANY   — выбор нескольких совместимых («C02.4» = UX label)
        +--> ASK_CONTEXT   — один наиболее информативный вопрос
        |
        v
Semantic Re-Resolution (OD-CLAR-4)
        |
        v
SemanticResolutionResult (OD-SR-1…6; conceptual shape — §11.2)
        +-- resolution_status:  RESOLVED / NEEDS_CONFIRMATION /
        |                       AMBIGUOUS / INSUFFICIENT
        +-- semantic_readiness: READY_FOR_DECISION /
        |                       DISCOVERY_REQUIRED
        |
   +----+----+
   |         |
   v         v
DISCOVERY_REQUIRED        READY_FOR_DECISION
(Desired Outcomes могут   (требует >= 1 sufficiently
ещё отсутствовать,        resolved Desired Outcome,
OD-SR-3…5)                OD-SR-5)
   |                         |
   v                         v
Outcome discovery            RecommendationContext (вне объекта, OD-SR-6)
   |                         |
   v                         v
semantic re-resolution       Decision Sufficiency
                                  |
                                  v
                             Decision Policy
                                  |
                                  v
                             Canonical Recommendation
```

`READY_FOR_DECISION` не гарантирует рекомендацию: downstream policy может
иметь недостаточный context (`INSUFFICIENT_CONTEXT`) или вернуть допустимый
`no_action` (§4.7, OD-SR-6).

`Semantic Resolution` как именованный слой/aggregate и точные кардинальности
— рабочий дизайн до сверки с каноническими контрактами (см. OQ-GO-2, §22).

### Рабочая роль Goal (working)

Goal отвечает на вопрос «зачем пользователю это изменение в текущем
journey?» и является semantic framing / user priority context, но не должен
самостоятельно определять Recommendation и не должен override'ить safety,
eligibility, exclusions, consent, evidence, context sufficiency.

Рабочий принцип (не canon):

> **Goal informs; Outcome anchors; Context differentiates; Policy decides.**

## 9. Desired Outcome vs actual Outcome

Обнаруженное семантическое различие, которое документ обязан сохранить:

```text
Desired / pre-action outcome  !=  Actual / post-action outcome
```

- Первое описывает, какое изменение/результат пользователь хочет получить.
- Второе описывает, что произошло после действия, и питает
  continuity/progress (canon-использование, §4.8).

Термин `Desired Outcome` — **proposed terminology**: канонического имени
для pre-action желаемого результата пока нет. Канонические поля этим
документом не переименовываются. Финальные canonical names — OQ-GO-1 (§22).

## 10. C01 semantic role

C01 — **human intent entry surface**, а не обязательно 1:1 селектор Domain
Goal (OD-GO-3).

UX-варианты C01 могут оставаться: better appearance; better wellbeing;
relax/recover; self-care; event preparation; maintain result; discovery /
«не знаю, с чего начать» — без автоматического объявления их каноническими
Domain Goal codes.

По [[Ayla MVP Recommendation Contract]] v0.4 §34, C01 определён как
«вход/выбор цели (этапы 1–3 Journey v0.3)», причём сам маппинг кодов на
этапы Journey помечен как подлежащий подтверждению. Этот Working Design не
меняет UX-задачу C01; семантическая роль C01 уточняется здесь только на
архитектурном уровне.

Принятые owner directions (OD-C01-1…3, §5):

- C01 — Hybrid First Contact: free text — primary input, Quick Actions —
  contextual UX assistance, а не Goal/Outcome taxonomy (canon-опора:
  [[BOT-001 First Contact Specification]] v1.0, approved 2026-08-12,
  A-BOT-001-Q4);
- одновременно показывается 3–5 contextual Quick Actions; их user-facing
  copy — не canonical semantic taxonomy и может зависеть от greeting/user
  state;
- Quick Action и natural-language формулировка идут одним
  semantic-resolution pipeline; hardcoded путь Quick Action → Goal/Outcome
  запрещён.

Provenance по [[Ayla MVP C01 C02 UX Inventory]] (draft, не canon): набор
C01 labels не канонизирован (SCR-CUST-001 A3: состав категорий не
зафиксирован); финальный user-facing copy — предмет отдельной follow-up
задачи и здесь не фиксируется.

## 11. C02 semantic role

C02 остаётся intent detection / clarification (см.
[[Ayla MVP Recommendation Contract]] v0.4 §34 — proposed). Owner direction
OD-GO-4 (§5): C02 разрешает, что пользователь на самом деле хочет
изменить/достичь; может быть подтверждено `1..N` outcomes/интерпретаций;
clarification может предлагать несколько правдоподобных интерпретаций;
нормализованные semantic outputs отделяются от user-facing формулировок.

Уточнение OD-CI-1 (§5, §11.3): множественность уже resolved Desired
Outcomes сама по себе не требует `CHOOSE_MANY` — multi-select применяется
только к unresolved candidate interpretations, а `1..N` явно выраженных и
непротиворечивых Outcomes допускает путь `RESOLVED → SKIP`.

Multi-select из OD-GO-4 формализован owner direction OD-CLAR-1 (§5): «C02.4»
— не отдельная semantic/domain стадия, а UX/design label режима
`CHOOSE_MANY` внутри единого `Adaptive Clarification` (§11.1). Если `C02.4`
используется как screen identifier в UX/Linear, немедленное переименование
не требуется — зафиксирована только архитектурная граница.

Provenance по [[Ayla MVP C01 C02 UX Inventory]] (draft, не canon): C02 —
dynamic clarification; фиксированного canonical option inventory для C02
нет; формальной канонической спецификации «C02.4» нет; multi-select находится
в owner-direction/proposed layer.

Расхождение с текущим proposed contract: v0.4 §34 определяет C02 как
«Intent detection», а Outcome Resolution — отдельный этап 4. Предлагаемая
роль C02 как outcome/interpretation resolution — рабочее направление,
требующее синхронизации (delta D-6, §20). Этот документ — архитектурный
checkpoint, не redesign ticket для UX.

### 11.1. Adaptive Clarification — единый рабочий механизм

Owner directions OD-CLAR-1…4 (§5) определяют единый слой уточнения с
четырьмя режимами:

```text
ADAPTIVE CLARIFICATION
  ├── SKIP          — semantic state достаточен, clarification UI не нужен
  ├── CONFIRM_ONE   — одна вероятная интерпретация требует подтверждения
  ├── CHOOSE_MANY   — несколько одновременно допустимых интерпретаций;
  │                   пользователь может подтвердить несколько
  │                   («C02.4» — UX/design label этого режима)
  └── ASK_CONTEXT   — данных недостаточно для полезного набора
                      интерпретаций; задаётся один наиболее
                      информативный вопрос
```

Рабочие правила (owner directions, не canon):

- **Semantic-layer compatibility (OD-CLAR-3).** Совместимость интерпретаций
  и `single/multiple` selection mode определяет semantic layer; UI только
  отображает разрешённое поведение. Multi-select не является универсальным
  UI-правилом. Compatibility algorithm/schema/registry здесь не
  проектируются (OQ-GO-12, §22).
- **Minimization + re-resolution (OD-CLAR-4).** Clarification запускается
  только при недостаточности, неоднозначности или необходимости
  подтверждения semantic state; за один conversational turn — один набор
  интерпретаций ИЛИ один наиболее информативный вопрос; после ответа
  выполняется semantic re-resolution. Новые thresholds/limits не вводятся.
- **UX copy не канонизируется** (OD-CLAR-2): примерные формулировки
  clarification — UX-задача, не canonical semantic taxonomy.

Совместимость с [[Ayla Intent Model Specification]] v1.0 (reconcile, §19):

- existing single-confirm behavior Intent Model (medium confidence 0.5–0.8 —
  одна подтверждающая формулировка, подтверждение обязательно перед
  side-effect; ровно один `clarification_question`) является **частным
  случаем** режима `CONFIRM_ONE` единого Adaptive Clarification. Пороги
  0.5/0.8 остаются runtime config Intent Model и здесь не переопределяются.
- `CHOOSE_MANY` (подтверждение нескольких интерпретаций) Intent Model v1.0
  не поддерживает — это **known delta / future amendment** к Intent Model,
  а не Existing Canon; Intent Model этим документом не изменяется.

### 11.2. SemanticResolutionResult — conceptual shape (working, не canonical schema)

Owner directions OD-SR-1…6 (§5) фиксируют `SemanticResolutionResult` как
отдельный downstream semantic object. Ниже — **только working/conceptual
shape, не canonical runtime schema**: registry, storage, JSON Schema,
Pydantic- и DB-модели этим документом не создаются (§3.2).

```text
SemanticResolutionResult
├── resolved semantics
│   ├── goal?                 optional / may be not_established (OD-SR-3)
│   └── desired_outcomes[]    0..N at object level (OD-SR-5)
├── resolution_status           (OD-SR-2)
│   ├── RESOLVED
│   ├── NEEDS_CONFIRMATION
│   ├── AMBIGUOUS
│   └── INSUFFICIENT
├── semantic_readiness          (OD-SR-4)
│   ├── READY_FOR_DECISION    ⇒ desired_outcomes count >= 1 (OD-SR-5)
│   └── DISCOVERY_REQUIRED    — Desired Outcome может отсутствовать
└── unresolved interpretation groups?   working/proposed (OD-CI-2; §11.3)
```

Resolved semantics и unresolved candidates разведены (OD-CI-6): candidates
не являются частью resolved `goal?` / `desired_outcomes[]`. Exact
cardinality/storage schema unresolved groups этим документом не
фиксируется (OQ-GO-14, §22).

Маппинг на Adaptive Clarification (согласовано с OD-CLAR-1…4):

```text
RESOLVED           → SKIP
NEEDS_CONFIRMATION → CONFIRM_ONE
AMBIGUOUS          → CHOOSE_MANY when compatible
INSUFFICIENT       → ASK_CONTEXT
```

Не утверждается, что любой `AMBIGUOUS` — это `CHOOSE_MANY`: совместимость
интерпретаций подтверждает semantic layer (OD-CLAR-3; архитектурная часть
OQ-GO-12 закрыта — OD-CI-1…10, §11.3). После ответа пользователя всегда
выполняется semantic re-resolution (OD-CLAR-4, OD-CI-8); «C02.4» не
возвращается как отдельный semantic/domain stage (OD-CLAR-1).

**Context boundary (OD-SR-6).** RecommendationContext не переносится
внутрь `SemanticResolutionResult`. Downstream-вход Decision Policy:

```text
Intent Resolution Output
+ SemanticResolutionResult
+ RecommendationContext
        ↓
Decision Sufficiency
        ↓
Recommendation Decision Policy
```

В `SemanticResolutionResult` не добавляются `recommendation_family`,
`recommended_action`, `action_type`, `service`, `provider`, `price`,
`availability`, `ranking`, `reason_codes`, `execution_route` и booking
data.

**Две оси sufficiency (OD-SR-6).** Semantic Sufficiency — достаточно ли
Ayla поняла, чего пользователь хочет / в каком semantic journey state он
находится. Decision Sufficiency — достаточно ли разрешённых
decision-relevant context facts для Recommendation Decision Policy
([[Ayla MVP Recommendation Contract]] §30, proposed). RecommendationContext
gap не переводит уже `RESOLVED` semantic result в `INSUFFICIENT`;
`READY_FOR_DECISION` не гарантирует рекомендацию — downstream policy может
иметь недостаточный context или вернуть допустимый `no_action` (§4.7).

Целевой pipeline (заменяет представление `SUFFICIENT SEMANTIC STATE` как
единой булевой двери):

```text
Semantic Resolution
        ↓
SemanticResolutionResult
        ├── resolution_status
        └── semantic_readiness
                 │
        ┌────────┴─────────┐
        ↓                  ↓
DISCOVERY_REQUIRED   READY_FOR_DECISION
        ↓                  ↓
Outcome discovery    RecommendationContext
        ↓                  ↓
re-resolution        Decision Sufficiency
                           ↓
                  Recommendation Decision Policy
```

### 11.3. Candidate Interpretations и InterpretationGroup — conceptual model (working, не canonical schema)

Owner directions OD-CI-1…10 (§5) закрывают архитектурную часть OQ-GO-12 —
представление совместимости интерпретаций и `single/multiple` selection
mode в semantic layer. Ниже — **только working/conceptual model, не
canonical runtime schema**: registry, storage, JSON Schema, Pydantic- и
DB-модели, API/storage format и global candidate IDs этим документом не
создаются (§3.2). Candidate identity, где упоминается, scoped к текущему
resolution/clarification cycle; runtime-форма остаётся открытой
(OQ-GO-14, §22).

```text
InterpretationGroup
├── candidates[]
│   └── CandidateInterpretation
│       ├── temporary/current-cycle identity
│       ├── presentation
│       └── proposed_semantic_payload
└── selection_mode
    ├── ONE
    └── MANY
```

Ключевые правила (owner directions, не canon):

- **Resolved plurality ≠ clarification plurality (OD-CI-1).** Несколько
  уже resolved Desired Outcomes — это не clarification plurality: такой
  state идёт по resolved path (`RESOLVED → SKIP`). `CHOOSE_MANY`
  применяется только к unresolved candidate interpretations.
- **Одна group = одна ambiguity (OD-CI-2).** Semantic state может
  концептуально иметь несколько unresolved ambiguities (несколько groups),
  но UI не обязан показывать их вместе: clarification policy выбирает
  один наиболее полезный clarification за turn (OD-CLAR-4), затем
  re-resolution. Алгоритм выбора наиболее полезного clarification этим
  документом не проектируется.
- **selection_mode принадлежит semantic layer (OD-CI-3).** `ONE | MANY`
  вычисляет semantic layer; UI только отображает разрешённое поведение
  (развивает OD-CLAR-3).
- **Compatibility по полной interpretation (OD-CI-4).** Учитываются
  direction, target, scope и релевантные semantic qualifiers, а не только
  Outcome/target code; глобальный compatibility registry не создаётся.
- **MVP без сложного compatibility graph (OD-CI-5).** Для `MANY` любое
  непустое подмножество candidates допустимо; сложные комбинационные
  ограничения разрешаются перестройкой clarification (разделить ambiguity
  или запросить context), а не pairwise matrix/graph.
- **Candidate = proposal (OD-CI-6); presentation ≠ identity (OD-CI-7).**
  `CandidateInterpretation` — гипотеза для подтверждения; user-facing
  copy не канонизируется и не является semantic identity.
- **Selection → re-resolution (OD-CI-8).** Выбранный candidate никогда не
  мутирует напрямую `desired_outcomes[]`, Goal или Journey Mode.
- **non-selection ≠ durable rejection (OD-CI-9).** `not_selected` —
  отсутствие подтверждения в текущем cycle, не negative preference /
  memory / rejection; explicit rejection требует отдельного контракта.
- **Metadata вне semantic identity (OD-CI-10).** Confidence, ranking,
  provenance, evidence refs — resolution/audit metadata; их runtime
  representation открыта (OQ-GO-14); confidence thresholds не вводятся.

Целевая цепочка Adaptive Clarification (согласована с OD-CLAR-1…4):

```text
Semantic Resolution
  ↓
SemanticResolutionResult
  ↓
blocking ambiguity?
  ├── no → resolved path / SKIP
  └── yes
       ↓
  InterpretationGroup
  ├── candidates[]
  └── selection_mode ONE | MANY
       ↓
  Adaptive Clarification
       ↓
  User Selection
       ↓
  confirmation evidence
       ↓
  Semantic Re-resolution
       ↓
  new SemanticResolutionResult
```

«C02.4» не возвращается как отдельный semantic/domain stage (OD-CLAR-1);
minimization сохраняется: один максимально полезный clarification за turn
(OD-CLAR-4).

**Проверка CONFIRM_ONE.** Не утверждается автоматически, что
`InterpretationGroup` с `selection_mode = ONE` эквивалентна `CONFIRM_ONE`:
текущая формулировка (OD-CLAR-2 и canon-опора
[[Ayla Intent Model Specification]] v1.0 — ровно один
`clarification_question`, одна подтверждающая формулировка) определяет
`CONFIRM_ONE` как подтверждение одной наиболее вероятной интерпретации.
Single-selection между несколькими alternatives создаёт
терминологическую дельту — она зафиксирована как known delta / future
amendment (§19), новый режим не вводится, canon silently не
переписывается.

**Граница терминов.** `CandidateInterpretation` — semantic meaning
candidate upstream от Recommendation и не смешивается с
recommendation/service/provider/ranking candidates
([[Ayla MVP Recommendation Contract]] v0.4 — proposed).

Illustrative examples (не canonical taxonomy; коды — из рабочей модели
§12–§15):

1. **Несколько resolved Outcomes → SKIP.** «Хочу убрать отёчность и
   снять напряжение в шее» → `REDUCE(PUFFINESS)` +
   `REDUCE(MUSCLE_TENSION)` с `scope.body_area = NECK` разрешаются без
   ambiguity → `RESOLVED → SKIP`, не `CHOOSE_MANY` (OD-CI-1).
2. **Compatible unresolved candidates → MANY.** «После праздников лицо
   какое-то уставшее» → compatible candidates `IMPROVE(FRESH_APPEARANCE)`
   и `REDUCE(PUFFINESS)` → `InterpretationGroup`, `selection_mode = MANY`
   → `CHOOSE_MANY` → пользователь подтверждает оба → confirmation
   evidence → Semantic Re-resolution → новый SemanticResolutionResult
   (OD-CI-3…5, OD-CI-8).
3. **Alternative interpretations → ONE.** «Хочу выглядеть свежее» может
   означать perceived-result outcome или maintenance framing одной
   ambiguity → `selection_mode = ONE` → single-selection clarification
   (см. дельту с `CONFIRM_ONE` выше).
4. **Scope меняет compatibility.** Два candidates с одинаковым target
   code `MUSCLE_TENSION`, но разными `scope.body_area` (`NECK` vs `BACK`)
   оцениваются по полной interpretation (OD-CI-4): совпадение target
   code само по себе не определяет совместимость.

## 12. Goal decomposition working matrix

Рабочая декомпозиция C01 options (**working design, не canon**):

| C01 UX entry | Рабочая классификация | Типичные semantic outputs |
|---|---|---|
| `LOOK_BETTER` | сильный кандидат на Domain Goal | — (Goal остаётся optional) |
| `FEEL_BETTER` | сильный кандидат на Domain Goal | — (Goal остаётся optional) |
| `RELAX_RECOVER` | UX entry / Outcome discovery cluster | `IMPROVE(RELAXATION)`, `IMPROVE(RECOVERY_STATE)`, `REDUCE(MUSCLE_TENSION)`; иногда дополнительно `goal = FEEL_BETTER`, но не синтезируется автоматически |
| `SELF_CARE` | UX/motivation framing; может резолвиться без отдельного Goal | `ESTABLISH(SELF_CARE_ROUTINE)` |
| `EVENT_PREPARATION` | Journey Mode / contextual framing | `IMPROVE(FRESH_APPEARANCE)`, `REDUCE(PUFFINESS)` и др.; `event_type`, `event_date`, `time_to_event` — context/runtime semantics |
| `MAINTAIN_RESULT` | maintenance mode / UX shortcut | `MAINTAIN(SKIN_CONDITION)`, `MAINTAIN(FRESH_APPEARANCE)`, `MAINTAIN(BODY_COMFORT)`; восстановление прежнего target из Memory — только при соблюдении consent/provenance/freshness правил |
| `UNKNOWN` / «не знаю, с чего начать» | resolution/discovery state, **не Goal** | запускает Goal/Outcome discovery; не превращается в фиктивный `goal=UNKNOWN` |

## 13. Outcome semantic model — working hypothesis

Рабочая композиционная модель (не canon):

```yaml
Outcome:
  direction:
  target:
    type:
    code:
  scope:
```

Уточнение (v0.6, GO2-W2, §13.1): `direction × target` — не произвольный
Cartesian product; композиция должна быть семантически валидной (например,
`MAINTAIN(PUFFINESS)` — misleading/invalid). Точное представление
direction-target validity остаётся открытым (§22).

Уточнение (v0.8, GO2-W11/W14, §13.1): исходная композиция
`direction + typed target + optional intrinsic scope` поддержана для
directional outcomes, но **не универсально достаточна**: quantitative
desired state/value («Хочу весить 85 кг») теряется при нормализации
только в direction. Generalized working candidate (не canon):

```text
DesiredOutcome =
VALID(
  typed target,
  desired change specification,
  optional intrinsic scope
)
```

Уточнение (v0.9, OD-DC-1, §13.1): разбор Minimal Desired Change Model
завершён; generalized candidate принят как owner direction и
**архитектурная часть OQ-GO-2 закрыта** (§22):

```text
DesiredOutcome =
VALID(
  typed target,
  DesiredChangeSpecification,
  optional intrinsic scope
)

DesiredChangeSpecification:
  direction?             0..1
  desired_state/value?   0..1

Invariant: at least one of direction / desired_state/value
must be established.
```

`direction` перестала быть обязательным универсальным носителем изменения;
explicit desired state/value поддерживается; direction и desired
state/value могут сосуществовать при семантической совместимости
(OD-DC-1); intrinsic scope остаётся optional. `DesiredChangeSpecification`
— НЕ canonical entity/schema: exact value model, validation, storage, API
и runtime representation не утверждаются (OQ-GO-15, §22); illustrative
codes/values не канонизируются.

Кандидаты direction (не заморожены): `REDUCE`, `IMPROVE`, `INCREASE`,
`MAINTAIN`, `ESTABLISH`.

Кандидаты target types (не заморожены): `STATE`, `PERCEIVED_RESULT`,
`BEHAVIOR`. Примеры: STATE — `PUFFINESS`, `MUSCLE_TENSION`,
`SKIN_CONDITION`, `ENERGY_LEVEL`, `RECOVERY_STATE`, `RELAXATION`;
PERCEIVED_RESULT — `FRESH_APPEARANCE`, `GROOMED_APPEARANCE`; BEHAVIOR —
`SELF_CARE_ROUTINE`.

Примеры композиции:

```text
REDUCE + PUFFINESS + FACE
IMPROVE + SKIN_CONDITION
MAINTAIN + BODY_COMFORT
ESTABLISH + SELF_CARE_ROUTINE
```

Рабочее правило:

> Не создавать классификации, которые не меняют поведение системы.

Рабочая cardinality (подлежит валидации будущим контрактом):

```text
Transformation Goal?    0..1 (optional при любом resolution_status, OD-SR-3)
Desired Outcomes        0..N на уровне объекта (OD-SR-5);
                        READY_FOR_DECISION требует >= 1 sufficiently
                        resolved Desired Outcome
Journey Mode?           0..1
Context Facts           0..N
```

Для discovery journey (`semantic_readiness = DISCOVERY_REQUIRED`, OD-SR-4)
`Desired Outcomes` могут ещё отсутствовать: состояние
`RESOLVED + DISCOVERY_REQUIRED + desired_outcomes = []` валидно
(OD-SR-3…5). Формальная DesiredOutcome schema и функция sufficiently
resolved остаются открытыми (OQ-GO-10, OQ-GO-13, §22).

### 13.1. OQ-GO-2 stress-test checkpoints и финальный разбор (v0.6, расширен v0.7–v0.8; архитектурное закрытие v0.9)

Зафиксированы stress-test checkpoints OQ-GO-2 (§22) по пяти группам
желаемых изменений: **Appearance / LOOK_BETTER**; **Body / Recovery /
Physical State**; **Maintenance / Habit / Prevention** (v0.6); **Behavior /
Lifestyle / Continuity** (v0.7); **Comparative / Quantitative / Temporal**
(v0.8); и финальный owner-level разбор **Minimal Desired Change Model**
(v0.9, OD-DC-1, §5). Итог: **архитектурная часть OQ-GO-2 закрыта (v0.9)** —
минимальная composition shape DesiredOutcome определена; canon, taxonomy
и AYLA-DEC этим документом не создаются.

#### GO2-W1 — базовая композиция пока выдерживает stress-test

После четырёх групп не найдено случая, доказывающего необходимость
четвёртого обязательного semantic dimension:

```text
DesiredOutcome =
direction
+ typed target
+ optional intrinsic scope
```

Статус (на момент v0.6–v0.7; см. уточнения v0.8/v0.9 ниже): working
hypothesis supported by current stress-test evidence (четыре группы); не
canon.

Уточнение (v0.8): stress-test Comparative / Quantitative / Temporal дал
контрпример к *universal sufficiency* direction-композиции (GO2-W11,
GO2-W14). Четвёртый универсальный dimension (общий `qualifier`) по-прежнему
не доказан (GO2-W10), но сам состав композиции требует обобщения:
`direction` → `desired change specification` (GO2-W14).

Уточнение (v0.9): generalized composition `typed target +
DesiredChangeSpecification + optional intrinsic scope` принята как owner
direction OD-DC-1 (§5); structural gate пройден — `NO ADDITIONAL REQUIRED
DIMENSION IDENTIFIED`; архитектурная часть OQ-GO-2 закрыта (§22).

#### GO2-W2 — композиция должна быть семантически валидной

`direction × target` не является произвольным Cartesian product.
Концептуально:

```text
DesiredOutcome =
VALID composition(
  direction,
  typed target,
  optional intrinsic scope
)
```

Illustrative evidence (коды и directions — illustrative, не canon):

```text
REDUCE(PUFFINESS)             → plausible
PREVENT(PUFFINESS)            → candidate/plausible
MAINTAIN(PUFFINESS)           → misleading/invalid

IMPROVE(SKIN_CONDITION)       → plausible
MAINTAIN(SKIN_CONDITION)      → plausible

ESTABLISH(SELF_CARE_ROUTINE)  → plausible candidate
ESTABLISH(PUFFINESS)          → invalid
```

Illustrative codes/directions не канонизируются; compatibility
registry/schema не создаются (согласуется с OD-CI-4: compatibility
оценивается по полной interpretation, §11.3).

#### GO2-W3 — общий qualifier пока не доказан

Stress-test дал temporal/recurrence evidence:

- «хочу быстрее восстанавливаться»;
- «хочу, чтобы отёки не возвращались»;
- «хочу делать это раз в месяц».

Этого недостаточно для общего/обязательного `qualifier` в DesiredOutcome.
Текущая интерпретация (working, не canon):

- prevention может потребовать direction semantics (`PREVENT` — candidate,
  не canon);
- cadence конкретной услуги («раз в месяц») относится downstream к
  execution/planning;
- «быстрее» остаётся evidence possible qualifier gap, но не основанием для
  нового dimension.

Qualifier taxonomy/schema/field не создаются. Comparative/quantitative/
temporal expressions — предмет следующего обязательного stress-test
(см. конец §13.1).

#### GO2-W4 — Service/Action не становится Outcome target автоматически

Фраза «Хочу регулярно делать массаж» не должна автоматически превращаться в
`ESTABLISH(MASSAGE_ROUTINE)` как Desired Outcome. Сохраняется граница
(согласуется с OD-GO-6, §17):

```text
Desired Outcome
→ Recommendation / NBA
→ Execution Mapping
→ Service / Provider / Booking
```

Конкретная услуга может быть execution preference, пользовательской
гипотезой способа или context, но не transformation target автоматически.

Behavioral target вроде условного `SELF_CARE_ROUTINE` получил
дополнительное evidence в stress-test Behavior / Lifestyle / Continuity
как допустимый кандидат Outcome target при изменении поведения
пользователя (GO2-W5), но остаётся working hypothesis, не canon
(GO2-W7, OQ-GO-5 open).

#### GO2-W5 — behavioral change может быть DesiredOutcome (v0.7)

Изменение поведения пользователя может быть представлено тем же классом
`DesiredOutcome`, если объектом изменения является само поведение
пользователя, а не конкретная услуга/способ исполнения.

Illustrative (working example, не canonical code/taxonomy):

```text
«Хочу начать регулярно заботиться о себе»

direction   = ESTABLISH
target.type = BEHAVIOR
target      = SELF_CARE_ROUTINE
```

#### GO2-W6 — repeated Service/Action != behavioral DesiredOutcome automatically (v0.7)

Фраза «Хочу регулярно делать массаж» не должна автоматически превращаться
в `ESTABLISH(MASSAGE_ROUTINE)`. Разводка (working, не canon):

- desired state/behavior change;
- execution preference / user hypothesis;
- external instruction/context.

Примеры:

```text
«...чтобы меньше забивалась спина»
→ Desired Outcome может быть REDUCE(MUSCLE_TENSION)
→ massage regularly = execution preference/hypothesis

«Хочу сделать уход за собой регулярной частью жизни»
→ possible behavioral DesiredOutcome: ESTABLISH(SELF_CARE_ROUTINE)
```

Зафиксировано:

```text
Repeated Service/Action
!=
Behavioral DesiredOutcome automatically
```

`MASSAGE_ROUTINE` не становится Outcome target; условный код использован
только как negative illustrative example (см. также GO2-W4, §21).

#### GO2-W7 — BEHAVIOR получает дополнительное evidence (v0.7)

Stress-test Behavior / Lifestyle / Continuity поддерживает `BEHAVIOR` как
viable candidate Target Type наряду с:

```text
STATE
PERCEIVED_RESULT
BEHAVIOR
```

Это evidence, не canon: **OQ-GO-5 остаётся open**; `BEHAVIOR` не
утверждается как canonical target type; registry/type taxonomy не
создаются.

#### GO2-W8 — continuity выявляет возможный Direction gap (v0.7)

Сценарий: «Раньше регулярно занимался собой, потом забросил. Хочу
вернуться». `ESTABLISH` может быть недостаточно точным: behavior уже
существовал ранее.

Candidate directions (не canon, не accepted):

```text
RESUME?
RESTORE?
```

Это evidence для OQ-GO-4 (наряду с `INCREASE?` / `ACHIEVE?` / `PREVENT?`).
Новый direction vocabulary не утверждается; отдельный continuity
object/entity только из-за этого примера не создаётся.

#### GO2-W9 — broad lifestyle aspiration может оставаться DISCOVERY_REQUIRED (v0.7)

Фразы вида:

```text
«Хочу больше заботиться о себе»
«Хочу больше времени уделять себе»
«Хочу не запускать себя»
```

не должны автоматически создавать generic DesiredOutcome вроде
`IMPROVE(SELF_CARE)`. Допустимо (согласуется с OD-SR-3…5, §11.2):

```text
resolution_status  = RESOLVED
semantic_readiness = DISCOVERY_REQUIRED
desired_outcomes   = []
```

Зафиксировано:

```text
Broad lifestyle aspiration
!=
generic behavioral DesiredOutcome
```

#### GO2-W10 — quantitative/temporal semantics heterogeneous (v0.8)

Stress-test Comparative / Quantitative / Temporal показал: эти смыслы не
сводятся к одному общему `qualifier` (усиливает GO2-W3). Разводка
conceptual meanings (working, не canon):

- intrinsic desired state/value;
- deadline/event context;
- desired time-to-effect;
- persistence expectation;
- execution cadence;
- comparative reference/baseline.

Общий qualifier model/field по-прежнему не создаётся.

#### GO2-W11 — direction not universally sufficient (v0.8)

Evidence:

```text
«Хочу похудеть»             vs «Хочу весить 85 кг»  vs «Хочу похудеть до 85 кг»
«Хочу меньше уставать»      vs «Хочу уровень энергии 8/10»
«Хочу уменьшить отёчность»  vs «Хочу, чтобы отёчности почти не было»
```

Direction alone может быть lossy: «Хочу весить 85 кг» имеет
`target = BODY_WEIGHT`, `desired_state/value = 85 kg`; direction зависит от
Actual State и может быть derived, а нормализация только в
`REDUCE`/`INCREASE` теряет `85 kg`. Illustrative codes/values не
канонизируются.

#### GO2-W12 — direction may be derived (v0.8)

```text
Actual State + Desired State → derived Direction
```

Direction может быть explicit, derived/inferred или пока отсутствовать.
Алгоритм derivation не проектируется; runtime fields не создаются.

#### GO2-W13 — intrinsic Desired State != external constraint (v0.8)

Working criterion: intrinsic Desired State/Value описывает желаемое
состояние самого semantic target:

```text
BODY_WEIGHT → 85 kg          intrinsic candidate
ENERGY_LEVEL → 8/10          intrinsic candidate
PUFFINESS → near_absent      intrinsic candidate

deadline = Saturday          context/constraint
time_to_effect = faster      decision expectation/constraint
persistence >= 7 days        persistence expectation
massage <= 2/month           execution constraint
```

Runtime fields/schema не создаются; illustrative codes/values не canon.

#### GO2-W14 — original composition requires revision (v0.8)

Зафиксировано:

```text
ORIGINAL COMPOSITION HYPOTHESIS:
SUPPORTED FOR DIRECTIONAL OUTCOMES
NOT UNIVERSALLY SUFFICIENT

GENERALIZED CANDIDATE:
DesiredOutcome =
VALID(
  typed target,
  desired change specification,
  optional intrinsic scope
)
```

`desired change specification` — conceptual placeholder, НЕ canonical
entity/schema. Working candidate для следующего разбора:

```text
DesiredChangeSpecification
├── direction?
└── desired_state/value?
```

Exact cardinality/validation/storage/API не утверждаются. Уточнение
(v0.9): разбор Minimal Desired Change Model выполнен (см. ниже); рабочий
кандидат принят как owner direction OD-DC-1 (§5); архитектурная часть
OQ-GO-2 закрыта (§22).

#### Финальный разбор — Minimal Desired Change Model (v0.9)

Выполнен последний узкий owner-level разбор OQ-GO-2. Reconcile с
[[Ayla Intent Model Specification]] v1.0 (граница Intent ↔ Transformation
Goal; Output Contract 0.5; confidence/clarification; evidence) и
[[Ayla MVP Recommendation Contract]] v0.4 (§27 Goal Resolution, §28 Outcome
Resolution, §29 RecommendationContext, §30 Context Sufficiency, §31
Decision Policy, §25 evidence/replay) противоречий минимальной модели не
выявил; upstream/downstream документы не изменены.

Принятая минимальная модель (owner direction OD-DC-1, §5; не canon):

```text
DesiredOutcome =
VALID(
  typed target,
  DesiredChangeSpecification,
  optional intrinsic scope
)

DesiredChangeSpecification:
  direction?             0..1
  desired_state/value?   0..1

Invariant:
  at least one of direction / desired_state/value
  must be established.
```

Валидны три базовые формы (illustrative; коды/значения не canon):

```text
A. Direction only
   «Хочу похудеть»
   target = BODY_WEIGHT
   desired_change: direction = REDUCE

B. Desired state/value only
   «Хочу весить 85 кг»
   target = BODY_WEIGHT
   desired_change: desired_state/value = 85 kg

C. Direction + desired state/value
   «Хочу похудеть до 85 кг»
   target = BODY_WEIGHT
   desired_change: direction = REDUCE; desired_state/value = 85 kg
```

Зафиксированные свойства:

- **Direction semantics.** `direction` может быть `explicit`, `derived`
  (`Actual State + Desired State → derived Direction`) или
  `not_established`. Provenance direction не является частью semantic
  identity: поле вида `direction_source = explicit | derived | inferred`
  в canonical semantic shape не вводится; для explainability/audit/replay
  это resolution/evidence metadata, проектируемое отдельно (согласуется с
  OD-CI-10 и с различием источников `source`/`confirmed` в Recommendation
  Contract §27/§29). Derived direction не выдаётся за explicit user
  statement. Exact runtime representation не проектируется.
- **Semantic invariant.** Если установлены и `direction`, и
  `desired_state/value`, они не должны образовывать известное
  семантическое противоречие при наличии применимого baseline/Actual
  State. Illustrative: `actual = 95 kg; direction = REDUCE;
  desired_state = 85 kg` — compatible; `actual = 95 kg; direction =
  INCREASE; desired_state = 85 kg` — contradictory. Compatibility
  algorithm, compatibility matrix/registry и numerical comparison engine
  НЕ проектируются. Actual State не входит в DesiredChangeSpecification и
  не становится обязательным полем DesiredOutcome: при неизвестном
  baseline невозможность вывести/проверить direction сама по себе не
  инвалидирует explicit desired state/value.
- **Граница с temporal/comparative/execution semantics** (подтверждает
  GO2-W13). `desired_state/value` описывает желаемое состояние самого
  typed target и не смешивается с внешними ограничениями:
  `desired_state/value != deadline`; `desired_state/value != comparative
  baseline`; `desired_state/value != execution constraint`. Deadline,
  event date, time-to-effect/speed, persistence expectation, comparative
  reference/baseline, execution cadence, service/provider preference,
  price/budget, availability и execution route автоматически не входят в
  DesiredChangeSpecification (каждое остаётся в своём слое: context /
  decision expectation / execution semantics).
- **Не универсальный scalar.** `desired_state/value` архитектурно не
  предполагается числом, enum, строкой, единицей измерения или threshold;
  illustrative `85 kg`, `8/10`, `near_absent` не канонизируются. Value
  Registry, Unit Registry, Measurement Schema, JSON Schema, Pydantic- и
  DB-модели не создаются — отдельный будущий taxonomy/runtime вопрос
  (OQ-GO-15, §22).
- **Cardinality.** `direction: 0..1`, `desired_state/value: 0..1` с
  constraint «минимум один установлен». `1..N` directions и `1..N`
  desired states не вводятся без фактического контрпримера: несколько
  независимых изменений одного запроса представляются по возможности
  несколькими DesiredOutcome, а не одним перегруженным
  DesiredChangeSpecification.

Structural gate (последний structural gate OQ-GO-2): по уже собранным
пяти stress-test группам не найдено случая, который нельзя представить
через `typed target + DesiredChangeSpecification + optional intrinsic
scope` без добавления ещё одного обязательного semantic dimension:

```text
NO ADDITIONAL REQUIRED DIMENSION IDENTIFIED
```

Это не означает завершения taxonomy — только то, что минимальная
архитектурная композиция DesiredOutcome достаточно определена:
**архитектурная часть OQ-GO-2 закрыта** (§22). Дальнейший поиск
дополнительных dimensions DesiredOutcome прекращён; возврат к composition
— только при конкретном MVP counterexample, не представимом принятой
минимальной моделью (§23).

#### Evidence stress-test групп (кратко)

**Appearance / LOOK_BETTER:**

- broad aspiration («Хочу лучше выглядеть») может разрешаться как Goal +
  `desired_outcomes=[]` + `DISCOVERY_REQUIRED` (согласуется с OD-SR-3…5,
  §11.2); generic `IMPROVE(APPEARANCE)` не создаётся;
- scope предотвращает target proliferation: `REDUCE(PUFFINESS) + FACE`
  предпочтительнее отдельного `FACE_PUFFINESS`, пока downstream semantics
  не докажет обратного (согласуется с §14);
- Actual/Reported State ≠ explicit Desired Outcome;
- event/Journey Mode («к свадьбе») ≠ Desired Outcome.

**Body / Recovery / Physical State:**

- subjective state может быть semantic target без causal diagnosis;
  `Desired Outcome != causal diagnosis`;
- direction vocabulary имеет evidence gaps (`RELAXATION → ACHIEVE?`,
  `ENERGY_LEVEL → INCREASE?`) — это предмет OQ-GO-4; ничего не утверждается;
- semantic validity Outcome ортогональна Safety Gate; health-like examples
  не канонизируются, Safety Policy не меняется (см. §4.7, OQ-GO-8).

**Maintenance / Habit / Prevention:**

- `MAINTAIN` выявляет direction-target compatibility (GO2-W2);
- `PREVENT` — сильный candidate direction (например «чтобы отёки не
  возвращались», «не доводить спину до такого состояния»), но не canon
  (предмет OQ-GO-4);
- recurrence конкретной услуги ≠ intrinsic recurrence DesiredOutcome.

**Behavior / Lifestyle / Continuity (v0.7):**

- behavioral change может быть тем же классом DesiredOutcome, если объект
  изменения — поведение пользователя, а не услуга/способ исполнения
  (GO2-W5);
- repeated Service/Action ≠ behavioral DesiredOutcome automatically;
  execution preference/hypothesis разводится с desired state/behavior
  change (GO2-W6);
- `BEHAVIOR` получил дополнительное evidence как candidate Target Type;
  OQ-GO-5 остаётся open (GO2-W7);
- continuity-сценарий («забросил — хочу вернуться») выявляет possible
  Direction gap: `RESUME?` / `RESTORE?` — evidence для OQ-GO-4, не canon
  (GO2-W8);
- broad lifestyle aspiration ≠ generic behavioral DesiredOutcome;
  допустимо `RESOLVED + DISCOVERY_REQUIRED + desired_outcomes=[]`
  (GO2-W9).

**Comparative / Quantitative / Temporal (v0.8):**

- quantitative/temporal semantics heterogeneous; общий `qualifier` не
  создан (GO2-W10);
- direction alone lossy для quantitative desired state/value
  (GO2-W11);
- direction может быть derived из Actual State + Desired State
  (GO2-W12);
- intrinsic Desired State/Value разведён с deadline, time-to-effect,
  persistence и execution constraints (GO2-W13);
- исходная композиция требует ревизии; generalized candidate —
  `typed target + desired change specification + optional intrinsic
  scope` (GO2-W14);
- deadline/event не превращает broad aspiration в resolved Outcome;
- exact duration без known target не делает semantic state sufficient;
- service cadence остаётся execution-level;
- comparative reference может ссылаться на previous Actual
  Outcome/baseline, не становясь target;
- user-stated quantitative target не становится автоматически
  нормативной целью Ayla/safety/policy.

#### Остаётся открытым

Архитектурная часть OQ-GO-2 закрыта (v0.9, OD-DC-1, §5); этот документ не
закрывает: OQ-GO-4 (Direction vocabulary, включая candidates `INCREASE?` /
`ACHIEVE?` / `PREVENT?` / `RESUME?` / `RESTORE?`); OQ-GO-5 (Target Types,
включая статус `BEHAVIOR`); Goal Taxonomy; Outcome Taxonomy; shared
Target/Subject/Factor representation (OQ-GO-3); exact direction-target
validity representation; qualifier model; behavioral target semantics
(evidence есть, canon нет); value model / exact representation
`desired_state/value`; runtime representation
`DesiredChangeSpecification` (OQ-GO-15, §22); safety treatment конкретных
health-like targets; runtime schema (OQ-GO-13/OQ-GO-14).

#### Minimal Desired Change Model — разбор выполнен (v0.9)

Последний узкий owner-level разбор OQ-GO-2 выполнен (см. выше): принята
минимальная модель `direction?` 0..1 + `desired_state/value?` 0..1 с
invariant «минимум один установлен» (OD-DC-1, §5); structural gate пройден
— дополнительный обязательный dimension не выявлен (`NO ADDITIONAL
REQUIRED DIMENSION IDENTIFIED`). Следующий этап — Goal/Outcome Semantic
Taxonomy Design (§23), а не дальнейший composition research.

## 14. Target / Subject / Factor problem

Design requirement (OD-GO-5):

> Outcome и Recommendation не должны независимо определять дублирующие
> vocabularies для одного и того же domain concept.

Коды вида `PUFFINESS`, `MUSCLE_TENSION`, `SKIN_CONDITION` должны в
перспективе происходить из общей нормализованной domain semantics, если
будущая taxonomy подтвердит эту модель.

Отдельный `RecommendationTargetRegistry` или `SubjectRegistry` в рамках
этой задачи **не создаётся**. Физическая форма — один общий Domain Concept
Registry, несколько typed registries или иная структура — остаётся открытой
(OQ-GO-3, §22).

Запрет на дублирующие сущности (working): не создавать
`REDUCE_FACE_PUFFINESS`, `FACE_PUFFINESS`, `PUFFINESS_TARGET` как три
независимые сущности, если это выразимо композицией `direction = REDUCE`,
`target = PUFFINESS`, `scope.body_area = FACE`.

## 15. Scope vs Context

Рабочее правило:

```text
Scope != Context
```

- `scope` описывает, к чему непосредственно относится желаемое изменение;
- `context` описывает факты ситуации, используемые при принятии решения.

Пример:

```text
Desired Outcome: REDUCE(MUSCLE_TENSION), scope.body_area = NECK
Context:         tension is reported after prolonged desk work
```

`NECK` — часть предмета желаемого изменения (предпочтительнее
пролиферации кодов вида `NECK_TENSION`, когда семантика позволяет
композицию); факт «напряжение после длительной работы за столом» —
контекст, остаётся Context, а не Outcome Scope (канонический Context Fact
code здесь намеренно не вводится).

## 16. Recommendation semantic core

### 16.1. Текущее состояние репозитория (proposed contract)

[[Ayla MVP Recommendation Contract]] v0.4, §33:

- NBA задаётся композиционно: `family + target + action_type`;
- `target` — «целевой объект действия в терминах домена» (§3,
  `decision_subject`); `target_outcomes[]` — коды Outcomes, на которые
  направлен NBA (§28);
- candidate families: `ADDRESS`, `SUPPORT`, `RECOVER`, `OBSERVE` — «семейства
  — кандидаты, не финальный канон до валидации против полной MVP
  Goal/Outcome таксономии (OQ-R11)»;
- safety — гейт, не family (§23, R-NBA-5); `no_action` — валидный
  объяснимый результат, размещение в таксономии отложено до валидации
  (§32, OQ-R11).

### 16.2. Рабочая гипотеза этого checkpoint (не canon)

```text
Canonical NBA semantic identity ≈ family + target
```

с metadata/evidence вокруг. Рабочие family candidates рабочего разбора:
`INTERVENE`, `SUPPORT`, `OBSERVE`.

**Зафиксированное расхождение:** код `INTERVENE` в репозитории отсутствует;
текущий proposed contract использует `ADDRESS` и включает `RECOVER`.
Предложение рабочего разбора — заменить `ADDRESS` на `INTERVENE` и убрать
`RECOVER` как family — является **рабочей гипотезой**, не подтверждённой
контрактом, и подлежит валидации на полном MVP scenario inventory вместе с
OQ-R11. Рабочие аргументы разбора (не решения): `RECOVER`, вероятно,
выражается через Outcome/target semantics и не нужен как отдельная family;
`NO_ACTION` — RecommendationResult, не family (согласуется с §32 и
AYLA-DEC-0045); safety/no-action — результаты/гейты, не families
(согласуется с §23); `ASSESS / SEEK_HELP` остаётся открытым и не
добавляется без проверки MVP scope и Safety Policy.

### 16.3. Target Recommendation не обязан совпадать с target Desired Outcome (working)

```text
Desired Outcome:          IMPROVE(FRESH_APPEARANCE)
Context:                  PUFFINESS_PRESENT
Canonical Recommendation: INTERVENE(PUFFINESS)   # working family name
Relation:                 Recommendation targets_outcome → IMPROVE(FRESH_APPEARANCE)
```

Это обосновывает сохранение `target_outcomes[]` в Recommendation semantics
(поле существует в v0.4 §3).

## 17. Recommendation vs Execution boundary

Критическое design direction (OD-GO-6). Semantic identity Canonical
Recommendation не должна зависеть от execution routes (`SERVICE_PATH`,
`SELF_CARE_PATH`, `OBSERVATION_PATH` или эквивалентов).

```text
C04 = WHAT + WHY
---------------- execution boundary ----------------
C05 = HOW
```

Концептуально:

```text
Canonical Recommendation
        |
        v
Execution Mapping
        |
        +--> routes/options
        +--> feasibility
        |
        v
Service / other capability
        |
        v
Provider Ranking / Booking where applicable
```

Совместимость с текущим contract: v0.4 §34 уже фиксирует `C04 = WHAT +
WHY` / `C05 = HOW` и относит execution options (`SERVICE_PATH | self-care |
observe | …`) к Execution Mapping; при этом `SERVICE_PATH` «означает
"реализуемо через услуги Ayla" и не идентифицирует конкретную услугу».

Availability, price, provider inventory и route capability не должны молча
переопределять уже выбранную semantic recommendation; действующая
каноническая policy (v0.4: Recommendation Suitability ≠ Execution
Feasibility, экономическая нейтральность) это направление поддерживает.

Открытая неоднозначность: `action_type` в v0.4 входит в композицию
Canonical NBA (`family + target + action_type`, §33). Если `action_type`
означает маршрут исполнения, это конфликтует с OD-GO-6 и подлежит
уточнению при amendment (delta D-7, §20).

## 18. Working end-to-end pipeline

Рабочая (не каноническая) сквозная картина:

```text
      FIRST CONTACT (C01)
             |
             v
      USER EXPRESSION
      (free text или Quick Action — один pipeline, OD-C01-3)
             |
             v
      INTENT RESOLUTION
             |
             v
      GOAL / OUTCOME SEMANTIC RESOLUTION   (proposed layer)
             |
             v
      ADAPTIVE CLARIFICATION               (owner direction, OD-CLAR-1…4)
             +-- SKIP
             +-- CONFIRM_ONE
             +-- CHOOSE_MANY        («C02.4» — UX/design label)
             +-- ASK_CONTEXT
             |
             v
      SEMANTIC RE-RESOLUTION               (OD-CLAR-4)
             |
             v
      SEMANTIC RESOLUTION RESULT   (OD-SR-1…6; conceptual — §11.2)
        resolution_status + semantic_readiness
             |
   +---------+---------+
   |                   |
   v                   v
 DISCOVERY_REQUIRED   READY_FOR_DECISION
 (Desired Outcomes    (>= 1 sufficiently
  могут отсутствовать, resolved Desired
  OD-SR-3…5)          Outcome, OD-SR-5)
   |                   |
   v                   v
 OUTCOME DISCOVERY    ADAPTIVE CONTEXT
   |                   |
   v                   v
 SEMANTIC            CONTEXT SUFFICIENCY
 RE-RESOLUTION       (Decision Sufficiency — OD-SR-6;
                      RecommendationContext gap не понижает
                      RESOLVED в INSUFFICIENT)
                          |
                          v
                      DECISION / SAFETY
             |
             v
      CANONICAL NBA
             |
           C04
        WHAT + WHY
-------- execution boundary --------
             |
             v
     EXECUTION MAPPING
             |
           C05
           HOW
```

Нормативное положение Safety gate в pipeline должно быть синхронизировано с
действующими safety/Recommendation contracts; этот документ его не
переопределяет (OQ-GO-8, §22).

## 19. Compatibility with current Intent Model

Совместимо без изменений [[Ayla Intent Model Specification]]:

- граница Intent ↔ Transformation Goal сохраняется (§4.1–§4.2);
- Intent Resolution Output 0.5 не расширяется Goal/Outcome-полями (§4.3) —
  Goal/Outcome semantics живёт downstream от resolver'а;
- Intent Slot Registry не пополняется `subject`/`factor`/`target`/
  `desired_outcome` (§4.4);
- post-action `outcome` (continuity/progress) не переименовывается (§4.8);
  pre-action терминология решается отдельно (OQ-GO-1).

Следствие: базовая модель этого Working Design не требует amendment к
Intent Model. Одно известное расхождение: режим `CHOOSE_MANY` единого
Adaptive Clarification (подтверждение нескольких интерпретаций, OD-CLAR-2)
Intent Model v1.0 не поддерживает — это known delta / future amendment
(§11.1), зафиксированное здесь без изменения Intent Model. Остальные
потенциальные amendments относятся к Recommendation Contract (§20) и
будущей Goal/Outcome Taxonomy.

Второе уточнение (v0.5, OD-CI-1…10): `InterpretationGroup` с
`selection_mode = ONE` (single-selection между несколькими alternatives,
§11.3) автоматически не приравнивается к `CONFIRM_ONE` — действующий
canon и OD-CLAR-2 определяют `CONFIRM_ONE` как подтверждение одной
наиболее вероятной интерпретации. Это known terminological delta /
future amendment; новый clarification mode этим документом не вводится,
Intent Model не изменяется.

## 20. Known deltas against Recommendation Contract

Impact hypothesis для будущего amendment к
[[Ayla MVP Recommendation Contract]] v0.4. **Сам контракт этим документом не
изменяется.**

| ID | Тема | Текущее состояние v0.4 | Рабочее направление |
|---|---|---|---|
| D-1 | Pipeline | Линейный порядок этапов: Intent Resolution (1) → Goal Resolution (3) → Outcome Resolution (4) (§5) | Semantic Resolution, допускающий optional Goal |
| D-2 | Goal Resolution | Этап 3, выход `goal + source + confirmed` (§27) | Явно поддержать `Goal = 0..1` и запрет искусственного Goal synthesis |
| D-3 | Outcome Resolution | Вход = `goal + user expression`; «к Goal относится 1..N Outcomes» (§28) | Outcome Resolution не должен требовать уже существующего Goal |
| D-4 | RecommendationContext | Поле `goal` присутствует; кардинальность явно не специфицирована (§29) | `goal` — optional; отсутствие Goal само по себе не `INSUFFICIENT_CONTEXT` |
| D-5 | Context Sufficiency | §30 оперирует missing/needs-confirmation фактами; missing Goal отдельно не обрабатывается | Goal уточняется только если конкретное правило Decision Policy требует его для текущего решения |
| D-6 | C01/C02 mapping | §34: C01 = вход/выбор цели; C02 = Intent detection; маппинг «подлежит подтверждению» | C01 = Hybrid First Contact (free text primary + contextual Quick Actions, OD-C01-1…3); C02 = desired outcome discovery/resolution с единым Adaptive Clarification (`SKIP / CONFIRM_ONE / CHOOSE_MANY / ASK_CONTEXT`, OD-CLAR-1…4); «C02.4» — не отдельная стадия, а UX/design label режима `CHOOSE_MANY`; C03 = adaptive missing-context clarification; C04 = WHAT+WHY; C05 = HOW. Точная нумерация этапов остаётся открытой (§22) |
| D-7 | `action_type` | Входит в композицию Canonical NBA `family + target + action_type` (§33); execution routes отнесены к C05 (§34) | Если `action_type` — маршрут исполнения, перенести downstream; уточнить семантику поля |
| D-8 | NBA families | Кандидаты `ADDRESS / SUPPORT / RECOVER / OBSERVE` (§33, OQ-R11) | Кандидаты разбора `INTERVENE / SUPPORT / OBSERVE`; `RECOVER` — вероятно избыточен как family. Обе версии — кандидаты; валидация на полном MVP inventory |
| D-9 | Decision Policy | Goal участвует через context fit (§31) | Goal может участвовать в controlled priority/alignment, но не override'ит safety, eligibility, exclusions, consent, evidence, context fit |
| D-10 | Semantic vs Decision Sufficiency | §30 «Context Sufficiency» оценивает достаточность context facts для Decision Policy; отдельного semantic sufficiency объекта нет; `INSUFFICIENT_CONTEXT` — исход RecommendationResult (§32) | Ввести upstream `SemanticResolutionResult` с осями `resolution_status` + `semantic_readiness` (OD-SR-1…6, §11.2); Context Sufficiency остаётся decision-level: RecommendationContext gap не переводит `RESOLVED` semantic result в `INSUFFICIENT` |

## 21. Explicitly rejected / deferred designs

Отклонено или отложено (не фиксируется как канон):

1. `Intent → mandatory Goal → Outcome` — отклонено (OD-GO-1, OD-GO-2).
2. Искусственный Goal synthesis ради заполнения схемы — отклонено (§4.2,
   OD-GO-2).
3. Декларация C01 UX options как 1:1 канонических Domain Goal codes —
   отклонено (OD-GO-3).
4. Фиктивный `goal = UNKNOWN` для discovery-входа — отклонено (§12).
5. Отдельный `RecommendationTargetRegistry` / `SubjectRegistry` — отложено
   до проверки shared domain concepts (OD-GO-5, §14).
6. Дублирующие коды вида `REDUCE_FACE_PUFFINESS` — отклонены при
   достаточности композиции (§14).
7. Зависимость semantic identity NBA от execution route — отклонено
   (OD-GO-6, §17).
8. Safety и no-action как Recommendation families — отклонено; это
   гейты/результаты (§4.7, §16).
9. Канонизация любого набора NBA families — отложено до валидации (§16,
   OQ-R11 / OQ-GO-9).
10. «C02.4» как отдельная semantic/domain stage — отклонено; это UX/design
    label режима `CHOOSE_MANY` внутри единого Adaptive Clarification
    (OD-CLAR-1, §5, §11).
11. Отдельный hardcoded путь Quick Action → Goal/Outcome в обход общего
    semantic-resolution pipeline — отклонено (OD-C01-3, §5, §10).
12. Multi-select как универсальное UI-правило — отклонено; selection mode
    определяет semantic layer, UI только отображает (OD-CLAR-3, §5, §11).
13. `SUFFICIENT SEMANTIC STATE` как единая булева дверь — заменено двумя
    осями `resolution_status` + `semantic_readiness` (OD-SR-2, OD-SR-4,
    §8, §11.2, §18).
14. Перенос RecommendationContext внутрь `SemanticResolutionResult` —
    отклонено (OD-SR-6, §11.2).
15. Понижение `RESOLVED` в `INSUFFICIENT` из-за RecommendationContext
    gap — отклонено (OD-SR-6, §11.2).
16. Автоматический `CHOOSE_MANY` из множественности уже resolved Desired
    Outcomes — отклонено; `CHOOSE_MANY` применяется только к unresolved
    candidate interpretations (OD-CI-1, §11.3).
17. Смешение разных semantic dimensions (Goal, Desired Outcome, Journey
    Mode, Context) в одной selection group — отклонено (OD-CI-2, §11.3).
18. Сложный compatibility graph/matrix, mutual exclusions, conditional
    subset constraints — отложены как MVP simplification; вместо
    комбинаторных ограничений resolver перестраивает clarification
    (OD-CI-5, §11.3).
19. Прямая мутация `desired_outcomes[]`, Goal или Journey Mode выбранным
    candidate без Semantic Re-resolution — отклонено (OD-CI-8, §11.3).
20. `not_selected` как durable negative preference / memory / rejection —
    отклонено; explicit rejection требует отдельного явного
    сигнала/контракта (OD-CI-9, §11.3).
21. Confidence/ranking/provenance/evidence как semantic identity
    candidate — отклонено; это resolution/audit metadata
    (OD-CI-10, §11.3).
22. Generic `IMPROVE(APPEARANCE)` для broad aspiration «Хочу лучше
    выглядеть» — отклонено; broad aspiration может разрешаться как Goal +
    `desired_outcomes=[]` + `DISCOVERY_REQUIRED` (GO2-W1, §13.1).
23. Автоматическое превращение Service/Action (например «Хочу регулярно
    делать массаж») в Desired Outcome target — отклонено; конкретная услуга
    может быть execution preference, пользовательской гипотезой способа или
    context, но не transformation target автоматически (GO2-W4, §13.1).
24. Общий/обязательный `qualifier` в DesiredOutcome — отложено:
    temporal/recurrence evidence есть, но недостаточно для нового
    dimension; qualifier taxonomy/schema не создаются (GO2-W3, §13.1).
25. Автоматическое превращение repeated Service/Action («Хочу регулярно
    делать массаж») в behavioral DesiredOutcome (`ESTABLISH(MASSAGE_ROUTINE)`)
    — отклонено; desired state/behavior change разводится с execution
    preference / user hypothesis и external instruction/context
    (GO2-W6, §13.1).
26. Generic `IMPROVE(SELF_CARE)` для broad lifestyle aspiration («Хочу
    больше заботиться о себе» и т.п.) — отклонено; допустимо
    `RESOLVED + DISCOVERY_REQUIRED + desired_outcomes=[]`
    (GO2-W9, §13.1).
27. Нормализация quantitative desired target только в direction
    (`REDUCE`/`INCREASE`) — отклонено: теряет intrinsic desired
    state/value («Хочу весить 85 кг» → `85 kg`) (GO2-W11, GO2-W14, §13.1).
28. Общий `qualifier` для quantitative/temporal semantics — повторно
    отклонено/отложено: meanings heterogeneous (intrinsic desired
    state/value; deadline/event context; time-to-effect; persistence;
    execution cadence; comparative reference) (GO2-W10, §13.1; см. также
    п. 24, GO2-W3).
29. User-stated quantitative target как автоматическая нормативная цель
    Ayla / safety / policy — отклонено: это user-stated desired
    state/value, не норматив (§13.1, evidence v0.8).
30. `direction` как universally required dimension DesiredOutcome —
    отклонено: минимальная модель допускает explicit desired state/value
    без direction и их сосуществование (OD-DC-1, GO2-W11, §13.1).
31. `direction_source = explicit | derived | inferred` как обязательное
    поле semantic identity — отклонено: direction provenance —
    resolution/evidence metadata, проектируемая отдельно (OD-DC-1, §13.1).
32. Actual State как обязательное поле DesiredOutcome /
    DesiredChangeSpecification — отклонено: при неизвестном baseline
    explicit desired state/value остаётся валидным; compatibility
    invariant применяется только при наличии применимого baseline
    (OD-DC-1, §13.1).
33. `1..N` directions / `1..N` desired states в одном
    DesiredChangeSpecification — не введено без фактического контрпримера:
    несколько независимых изменений представляются несколькими
    DesiredOutcome (OD-DC-1, §13.1).
34. Value Registry / Unit Registry / Measurement Schema для
    `desired_state/value` — отложено: exact value model — будущий
    taxonomy/runtime вопрос (OD-DC-1, OQ-GO-15, §22).

Не утверждены на текущем этапе: финальная Goal Taxonomy; финальная Outcome
Taxonomy; название `Desired Outcome`; отдельная сущность/aggregate
`Semantic Resolution`; `Subject Registry`; `Factor Registry`; финальный
набор target types; финальный набор directions (включая `PREVENT`,
`ACHIEVE`, `INCREASE`, `RESUME`, `RESTORE`); exact direction-target validity representation;
qualifier model; behavioral target semantics; canonical/runtime форма
`DesiredChangeSpecification` (минимальная архитектурная shape зафиксирована
owner direction OD-DC-1; exact value model, schema, validation, storage и
representation explicit/derived direction evidence не утверждены —
OQ-GO-15, §22); физическая форма registry;
`Journey Mode Registry`; финальный NBA family registry;
`ASSESS / SEEK_HELP` semantics.

## 22. Open questions

| ID | Вопрос |
|---|---|
| OQ-GO-1 | Canonical terminology для желаемого результата: как назвать объект так, чтобы он не конфликтовал с downstream `Outcome` после action? Кандидаты проверяются против Journey, Progress, Analytics и Recommendation документов. |
| OQ-GO-2 | **Архитектурная часть закрыта (v0.9, OD-DC-1, §5, §13.1):** принята Minimal Desired Change Model — `DesiredOutcome = VALID(typed target, DesiredChangeSpecification, optional intrinsic scope)`, где `DesiredChangeSpecification` = `direction?` 0..1 + `desired_state/value?` 0..1 с invariant «минимум один установлен»; direction перестала быть обязательным универсальным носителем изменения; explicit desired state/value поддерживается; direction + desired state/value могут сосуществовать при семантической совместимости; intrinsic scope остаётся optional; structural gate по пяти stress-test группам: `NO ADDITIONAL REQUIRED DIMENSION IDENTIFIED`. Закрытие не означает готовности Direction Taxonomy, Target Type Taxonomy, Target Registry, value model, scope schema, direction-target validity registry, runtime schema, parser/classifier, inference algorithm, safety semantics или amendment к Recommendation Contract. Остатки распределены: direction vocabulary → OQ-GO-4; target types → OQ-GO-5; shared concepts/registry → OQ-GO-3; runtime `SemanticResolutionResult` → OQ-GO-13; candidate interpretation runtime → OQ-GO-14; runtime representation `DesiredChangeSpecification` → OQ-GO-15. Полный MVP C02 inventory остаётся обязательным для taxonomy validation (§23), но не для повторного открытия composition research без нового контрпримера. |
| OQ-GO-3 | Нужен ли общий semantic vocabulary для Outcome/Context/Recommendation target и какова его минимальная структура. Registry не создавать до проверки полного inventory. |
| OQ-GO-4 | Direction vocabulary: проверить необходимость и различия `REDUCE / IMPROVE / INCREASE / MAINTAIN / ESTABLISH`. **Additional evidence (v0.7, §13.1):** continuity-сценарий («забросил — хочу вернуться») выявляет possible gap — `ESTABLISH` может быть недостаточно точным, если behavior существовал ранее; candidates `RESUME?` / `RESTORE?` добавлены к ранее зафиксированным `INCREASE?` / `ACHIEVE?` / `PREVENT?`. Ничего не канонизировано; вопрос **остаётся открытым**. |
| OQ-GO-5 | Target types: проверить полный MVP набор; текущие кандидаты `STATE / PERCEIVED_RESULT / BEHAVIOR`. **Additional evidence (v0.7, §13.1):** stress-test Behavior / Lifestyle / Continuity поддерживает `BEHAVIOR` как viable candidate Target Type (GO2-W5, GO2-W7); `BEHAVIOR` не утверждён как canonical, registry/type taxonomy не создаются; вопрос **остаётся открытым**. |
| OQ-GO-6 | Goal taxonomy: достаточно ли для MVP decision-relevant goals `LOOK_BETTER / FEEL_BETTER`; существуют ли реальные MVP-сценарии, требующие третьего самостоятельного Goal. |
| OQ-GO-7 | Journey Mode: проверить существующий канон на эквиваленты для `EVENT_PREPARATION / MAINTENANCE / DISCOVERY` до создания нового registry. |
| OQ-GO-8 | Safety ordering: синхронизировать рабочую pipeline diagram (§18) с нормативным порядком safety gates. Этот документ не меняет существующую safety authority. |
| OQ-GO-9 | Recommendation family registry: после Goal/Outcome semantic model валидировать family-кандидатов (обе версии, D-8) на полном MVP scenario inventory, совместно с OQ-R11 контракта. |
| OQ-GO-10 | **Частично разрешён (v0.4):** состояние `RESOLVED + DISCOVERY_REQUIRED + desired_outcomes = []` валидно (OD-SR-3…5, §11.2, §13). Открытый остаток: формальное определение поведения discovery journey — механизм outcome discovery не проектировался. |
| OQ-GO-11 | **Архитектурная часть закрыта (v0.4, OD-SR-1…6):** boundary `SemanticResolutionResult` (отдельный downstream semantic object, не заменяет Intent Resolution Output 0.5), состояния `resolution_status`, optional Goal, разделение resolution/readiness, минимум один Desired Outcome для `READY_FOR_DECISION`, разделение Semantic Sufficiency и Decision Sufficiency (§5, §11.2). Runtime-schema/algorithm остаток выделен в OQ-GO-13. |
| OQ-GO-12 | **Архитектурная часть закрыта (v0.5, OD-CI-1…10):** resolved plurality ≠ clarification plurality; одна `InterpretationGroup` = одна semantic ambiguity; `selection_mode = ONE \| MANY` принадлежит semantic layer; compatibility оценивается по полной interpretation; MVP без сложного compatibility graph; `CandidateInterpretation` = proposal; presentation отделена от payload; selection всегда ведёт к Semantic Re-resolution; `not_selected` ≠ durable rejection; metadata вне semantic identity (§5, §11.3). Runtime-schema остаток выделен в OQ-GO-14; алгоритм выбора наиболее полезного clarification этим документом не проектировался. |
| OQ-GO-13 | Runtime-форма `SemanticResolutionResult`: runtime schema, thresholds/classifier для `resolution_status`, формальная функция sufficiently resolved для Desired Outcome (остаток OQ-GO-11). Не проектировать до отдельного owner-level разбора. |
| OQ-GO-14 | Runtime-форма `CandidateInterpretation` / `InterpretationGroup` (остаток OQ-GO-12): exact schema, lifecycle temporary/current-cycle identity, representation provenance/evidence refs и resolution/audit metadata (confidence, ranking). Не проектировать до отдельного owner-level разбора; registry, JSON/DB/API и global candidate IDs не создавать. |
| OQ-GO-15 | Runtime representation `DesiredChangeSpecification` (остаток OQ-GO-2, v0.9): exact schema/value representation `desired_state/value`, explicit/derived direction evidence, validation и serialization. Не проектировать до отдельного owner-level разбора; Value Registry, Unit Registry, Measurement Schema, JSON Schema, Pydantic- и DB-модели не создавать (OD-DC-1, §13.1). |

## 23. Next validation work

Разбор **Minimal Desired Change Model** выполнен (v0.9, §13.1): принята
минимальная semantic shape `DesiredChangeSpecification` (`direction?`
0..1 + `desired_state/value?` 0..1, минимум один установлен; OD-DC-1, §5),
представляющая explicit direction, explicit desired state/value или оба,
без смешения с deadline, speed, persistence, comparative reference и
execution constraints. Два этапа разведены:

```text
OQ-GO-2 composition architecture
→ CLOSED (architectural part, v0.9)

Goal/Outcome Semantic Taxonomy Design
→ NEXT PHASE
```

Принцип (зафиксирован этим Working Design):

> Не продолжать расширять DesiredOutcome semantic shape speculative
> dimensions. Возвращаться к composition только при обнаружении
> конкретного MVP counterexample, не представимого принятой минимальной
> моделью.

Полный MVP C02 inventory остаётся обязательным для taxonomy validation,
но **не** для повторного открытия composition research без нового
контрпримера.

Следующий рабочий этап — **Goal/Outcome Semantic Taxonomy Design**, но
начинать не со списка кодов. Порядок:

1. Собрать фактический MVP C02 outcome inventory.
2. Разложить каждый вариант в матрицу: `C01 entry → UI label / user
   expression → proposed direction → target type → target code → intrinsic
   scope → required context → ambiguity / collision`.
3. Найти дубли и неразложимые случаи.
4. Проверить shared domain concepts (OQ-GO-3).
5. Определить минимальную Goal/Outcome semantic schema.
6. Только затем формировать registry/taxonomy.
7. После стабилизации — подготовить amendment к Recommendation Contract
   v0.4 (дельты §20) и связанные Journey/UX документы.

## 24. Change log / provenance

### Evidence base

- [[Ayla Intent Model Specification]] v1.0 — Active Canon (approved,
  2026-08-08): граница Intent ↔ Transformation Goal, `unknown/not_established`,
  Recommendation Input Boundary, Slot Registry, downstream `outcome`.
- [[Ayla MVP Recommendation Contract]] v0.4 — proposed contract (draft):
  pipeline §5, Goal Resolution §27, Outcome Resolution §28,
  RecommendationContext §29, Context Sufficiency §30, Decision Policy §31,
  Results §32, NBA Taxonomy §33, граница C04/C05 §34, OQ-R11.
- [[Ayla Glossary]] — Goal, Outcome, Next Best Action.
- [[OWNER_DECISION_REGISTER]] — AYLA-DEC-0026, AYLA-DEC-0037, AYLA-DEC-0039,
  AYLA-DEC-0043, AYLA-DEC-0045, AYLA-DEC-0046, AYLA-DEC-0048, AYLA-DEC-0055,
  AYLA-DEC-0062, AYLA-DEC-0078.
- [[Ayla MVP User Journey Specification]] — этапы Journey, на которые
  ссылается маппинг C01–C05 (v0.4 §34).
- [[BOT-001 First Contact Specification]] v1.0 (approved, 2026-08-12) и
  owner-решение A-BOT-001-Q4 (APPROVED, 2026-08-12) — canon-опора для
  Hybrid First Contact: free text — primary input, Quick Actions —
  contextual UX assistance (OD-C01-1…2).
- [[Ayla MVP C01 C02 UX Inventory]] v0.1 (draft, 2026-08-20) — provenance
  по C01/C02: отсутствие канонизированного набора C01 labels и fixed C02
  option inventory, отсутствие формальной спецификации «C02.4», коллизии
  COL-01…COL-10; использован только как evidence, сам не изменён.
- Рабочий разбор Goal/Outcome семантики (2026-08-20) — источник owner
  directions OD-GO-1…OD-GO-6 и рабочих гипотез; не является каноническим
  авторитетом.

### Change Log

#### v0.9 — 2026-08-22

- выполнен последний узкий owner-level разбор OQ-GO-2 — **Minimal Desired
  Change Model** (§13.1); reconcile с [[Ayla Intent Model Specification]]
  v1.0 (граница Intent ↔ Transformation Goal, Output Contract 0.5,
  confidence/clarification, evidence) и [[Ayla MVP Recommendation Contract]]
  v0.4 (§27–§31, §25) противоречий минимальной модели не выявил;
  upstream/downstream документы не изменены;
- записан принятый owner direction OD-DC-1 (§5): минимальная
  архитектурная композиция `DesiredOutcome = VALID(typed target,
  DesiredChangeSpecification, optional intrinsic scope)`;
  `DesiredChangeSpecification` = `direction?` 0..1 +
  `desired_state/value?` 0..1 с invariant «минимум один установлен»;
  валидны три базовые формы (direction only; desired state/value only;
  direction + desired state/value); при совместной установке —
  архитектурный compatibility invariant при наличии применимого
  baseline/Actual State (без проектирования algorithm/matrix/registry);
  direction может быть explicit / derived / not_established, при этом
  provenance — resolution/evidence metadata, не semantic identity;
  external temporal/comparative/execution constraints автоматически не
  входят в DesiredChangeSpecification;
- structural gate пройден: по пяти stress-test группам `NO ADDITIONAL
  REQUIRED DIMENSION IDENTIFIED`; **архитектурная часть OQ-GO-2 закрыта**
  (§22);
- §7: добавлен термин `DesiredChangeSpecification`;
- §13: generalized composition финализирована как owner direction OD-DC-1;
  `direction` больше не обязательный универсальный носитель изменения;
- §13.1: записан финальный checkpoint Minimal Desired Change Model; список
  «Остаётся открытым» приведён к post-closure состоянию;
- §21: добавлены отклонённые/отложенные дизайны 30–34 (`direction` как
  universally required; `direction_source` в semantic identity; Actual
  State как обязательное поле; `1..N` directions / `1..N` desired states;
  Value/Unit registry для desired_state/value);
- §22: OQ-GO-2 — архитектурная часть закрыта, остатки распределены
  (OQ-GO-3/4/5/13/14); добавлен OQ-GO-15 — runtime representation
  `DesiredChangeSpecification` (не решать сейчас); OQ-GO-3, OQ-GO-4 и
  OQ-GO-5 остаются открытыми без изменений;
- §23: переход от composition research к Goal/Outcome Semantic Taxonomy
  Design; зафиксирован принцип «не расширять DesiredOutcome semantic shape
  speculative dimensions; возврат к composition только при конкретном MVP
  counterexample»;
- не канонизировано: `DesiredChangeSpecification` как canonical
  entity/schema, illustrative codes/values (`BODY_WEIGHT`, `85 kg`,
  `8/10`, `near_absent`, `REDUCE`, `INCREASE`), value model, runtime
  fields/schema; Intent Model, Recommendation Contract, Safety Policy и
  Journey/UX документы не изменены, AYLA-DEC не созданы.

#### v0.8 — 2026-08-21

- записан interim stress-test checkpoint OQ-GO-2 (не закрытие) по пятой
  группе — Comparative / Quantitative / Temporal; coverage расширен до
  пяти групп (§13.1);
- зафиксированы working findings GO2-W10…W14: quantitative/temporal
  semantics heterogeneous (общий `qualifier` не создан); direction alone
  lossy для quantitative desired state/value («Хочу весить 85 кг»);
  direction может быть explicit / derived из Actual State + Desired State
  / отсутствовать; intrinsic Desired State/Value разведён с deadline,
  time-to-effect, persistence и execution constraints; исходная
  композиция требует ревизии;
- ревизия гипотезы (§13, §13.1): исходная композиция
  `direction + typed target + optional intrinsic scope` — supported for
  directional outcomes, **not universally sufficient**; generalized
  working candidate — `typed target + desired change specification +
  optional intrinsic scope`; `DesiredChangeSpecification` (working
  candidate `direction?` + `desired_state/value?`) — conceptual
  placeholder, НЕ canonical entity/schema, cardinality/validation/
  storage/API не утверждены;
- дополнительные findings (§13.1): deadline/event не превращает broad
  aspiration в resolved Outcome; exact duration без known target не делает
  semantic state sufficient; service cadence остаётся execution-level;
  comparative reference может ссылаться на previous Actual
  Outcome/baseline, не становясь target; user-stated quantitative target
  не становится нормативной целью Ayla/safety/policy;
- §21: добавлены отклонённые дизайны 27–29 (нормализация quantitative
  target только в direction; общий qualifier для quantitative/temporal;
  user-stated quantitative target как норматив); canonical форма
  `DesiredChangeSpecification` добавлена в список не утверждённых;
- §22: OQ-GO-2 дополнен checkpoint v0.8 и **остаётся открытым**; OQ-GO-4
  и OQ-GO-5 остаются открытыми без изменений;
- §23: следующий и последний узкий owner-level разбор перед попыткой
  закрыть OQ-GO-2 — Minimal Desired Change Model (этим документом не
  выполняется);
- не канонизировано: `DesiredChangeSpecification`, illustrative
  codes/values (`BODY_WEIGHT`, `85 kg`, `8/10`, `near_absent`), qualifier
  model, comparative/temporal schema, runtime fields; canonical
  upstream/downstream docs не изменены, AYLA-DEC не созданы.

#### v0.7 — 2026-08-21

- записан interim stress-test checkpoint OQ-GO-2 (не закрытие) по четвёртой
  группе — Behavior / Lifestyle / Continuity; coverage расширен до четырёх
  групп (§13.1);
- зафиксированы working findings GO2-W5…W9: behavioral change может быть
  тем же классом DesiredOutcome (объект изменения — поведение пользователя,
  не услуга); repeated Service/Action ≠ behavioral DesiredOutcome
  automatically; `BEHAVIOR` получил дополнительное evidence как candidate
  Target Type; continuity-сценарий выявляет possible Direction gap
  (`RESUME?` / `RESTORE?` — evidence для OQ-GO-4); broad lifestyle
  aspiration ≠ generic behavioral DesiredOutcome, допустимо
  `RESOLVED + DISCOVERY_REQUIRED + desired_outcomes=[]`;
- после четырёх stress-test групп не найдено контрпримера, требующего
  четвёртого обязательного semantic dimension; composition hypothesis
  `VALID composition(direction, typed target, optional intrinsic scope)`
  остаётся working/non-canonical, OQ-GO-2 **остаётся открытым**;
- §21: добавлены отклонённые дизайны 25–26 (repeated Service/Action как
  behavioral DesiredOutcome; generic `IMPROVE(SELF_CARE)` для broad
  lifestyle aspiration); `RESUME` / `RESTORE` добавлены в список не
  утверждённых directions;
- §22: OQ-GO-2 дополнен checkpoint v0.7 и **остаётся открытым**; OQ-GO-4 и
  OQ-GO-5 получили additional evidence без закрытия;
- §23: следующий обязательный validation step — stress-test
  Comparative / Quantitative / Temporal Desired Outcomes (этим документом
  не выполняется);
- не канонизировано: `BEHAVIOR` как Target Type, `RESUME` / `RESTORE` /
  `PREVENT` / `ACHIEVE` / `INCREASE`, `SELF_CARE_ROUTINE` и другие
  illustrative codes, behavioral/continuity registry, qualifier и
  comparative/temporal model, runtime schema; canonical
  upstream/downstream docs не изменены, AYLA-DEC не созданы.

#### v0.6 — 2026-08-21

- записан interim stress-test checkpoint OQ-GO-2 (не закрытие) по трём
  группам — Appearance / LOOK_BETTER; Body / Recovery / Physical State;
  Maintenance / Habit / Prevention (§13.1);
- зафиксированы working findings GO2-W1…W4: базовая композиция
  `direction + typed target + optional intrinsic scope` поддержана текущим
  stress-test evidence как working hypothesis; композиция должна быть
  семантически валидной (`direction × target` ≠ произвольный Cartesian
  product); общий/обязательный `qualifier` не доказан; Service/Action не
  становится Outcome target автоматически;
- §13: композиция Outcome дополнена требованием семантической валидности
  (GO2-W2);
- §21: добавлены отклонённые/отложенные дизайны 22–24 (generic
  `IMPROVE(APPEARANCE)` для broad aspiration; автоматический Service/Action
  как Outcome target; общий обязательный `qualifier`);
- §22: OQ-GO-2 дополнен interim checkpoint status и **остаётся открытым**;
  следующий обязательный stress-test — Behavior / Lifestyle / Continuity
  (этим документом не выполняется);
- не канонизировано: `PREVENT` / `ACHIEVE` / `INCREASE`, illustrative
  codes/directions, qualifier model, behavioral target semantics, exact
  direction-target validity representation, runtime schema; canonical
  upstream/downstream docs не изменены, AYLA-DEC не созданы.

#### v0.5 — 2026-08-21

- записаны принятые owner directions OD-CI-1…10 по Candidate
  Interpretations и `CHOOSE_MANY` (§5): resolved plurality ≠
  clarification plurality; одна `InterpretationGroup` = одна semantic
  ambiguity; `selection_mode = ONE | MANY` принадлежит semantic layer;
  compatibility по полной interpretation; MVP без сложного compatibility
  graph; `CandidateInterpretation` = proposal; presentation ≠ semantic
  identity; selection → Semantic Re-resolution; `not_selected` ≠ durable
  rejection; metadata вне semantic identity;
- добавлена §11.3 — conceptual model `InterpretationGroup` /
  `CandidateInterpretation` (working, не canonical runtime schema),
  целевая цепочка Adaptive Clarification, multiple unresolved groups,
  дельта `InterpretationGroup(ONE)` vs `CONFIRM_ONE`, illustrative
  examples;
- §11.2: conceptual shape `SemanticResolutionResult` приведён к разводке
  resolved semantics / unresolved interpretation groups (OD-CI-2,
  OD-CI-6);
- §7: добавлены термины `CandidateInterpretation`, `InterpretationGroup`,
  `selection_mode`, `not_selected`;
- §11: уточнено, что множественность resolved Desired Outcomes не
  требует `CHOOSE_MANY` (OD-CI-1);
- §19: зафиксирована known terminological delta — single-selection между
  несколькими alternatives (`selection_mode = ONE`) не приравнивается к
  `CONFIRM_ONE`; Intent Model не изменён;
- §21: добавлены отклонённые/отложенные дизайны 16–21;
- §22: OQ-GO-12 закрыт в архитектурной части; runtime-остаток выделен в
  новый OQ-GO-14; OQ-GO-13 не перегружен и не изменён.

#### v0.4 — 2026-08-21

- записаны принятые owner directions OD-SR-1…6 по Semantic Resolution &
  Sufficiency (§5): `SemanticResolutionResult` как отдельный downstream
  semantic object, не расширяющий и не заменяющий Intent Resolution
  Output 0.5; четыре состояния `resolution_status`; optional Goal при
  `RESOLVED`; разделение осей `resolution_status` / `semantic_readiness`;
  минимум один sufficiently resolved Desired Outcome для
  `READY_FOR_DECISION`; разделение Semantic Sufficiency и Decision
  Sufficiency;
- добавлена §11.2 — conceptual shape `SemanticResolutionResult`
  (working, не canonical runtime schema), маппинг на Adaptive
  Clarification, context boundary и целевой pipeline;
- pipeline-диаграммы §8 и §18: представление `SUFFICIENT SEMANTIC STATE`
  как единой булевой двери заменено двумя осями `resolution_status` +
  `semantic_readiness` с ветвлением `DISCOVERY_REQUIRED` /
  `READY_FOR_DECISION`;
- рабочая cardinality §13 приведена к OD-SR-3/OD-SR-5
  (`desired_outcomes` — `0..N` на уровне объекта);
- §20: добавлена дельта D-10 (Semantic vs Decision Sufficiency) к будущему
  amendment Recommendation Contract; сам контракт не изменён;
- §21: зафиксированы отклонённые/заменённые дизайны — единая булева дверь
  sufficiency; RecommendationContext внутри `SemanticResolutionResult`;
  понижение `RESOLVED` из-за RecommendationContext gap;
- §22: OQ-GO-11 закрыт в архитектурной части, runtime-остаток выделен в
  OQ-GO-13; OQ-GO-10 частично разрешён (`RESOLVED + DISCOVERY_REQUIRED +
  desired_outcomes = []` валидно); OQ-GO-12 не затронут — следующий
  owner-level разбор.

#### v0.3 — 2026-08-20

- записаны принятые owner directions по C01 (OD-C01-1…3: Hybrid First
  Contact; 3–5 contextual Quick Actions; единый semantic-resolution
  pipeline без hardcoded пути Quick Action → Goal/Outcome) и по Adaptive
  Clarification (OD-CLAR-1…4: четыре режима `SKIP / CONFIRM_ONE /
  CHOOSE_MANY / ASK_CONTEXT`; semantic-layer compatibility; minimization +
  re-resolution) — §5, §10, §11, §11.1;
- «C02.4» переопределён: не отдельная semantic/domain стадия, а UX/design
  label режима `CHOOSE_MANY` (OD-CLAR-1); соответствующие места §8, §11,
  §18, §20 (D-6), §21 приведены к этой границе;
- pipeline-диаграммы §8 и §18 обновлены: добавлены First Contact → User
  Expression, Adaptive Clarification с четырьмя режимами, Semantic
  Re-Resolution, Sufficient Semantic State (критерий открыт — OQ-GO-11);
- reconcile с [[Ayla Intent Model Specification]] v1.0: existing
  single-confirm behavior зафиксирован как частный случай `CONFIRM_ONE`;
  `CHOOSE_MANY` Intent Model не поддерживает — known delta / future
  amendment, не canon (§11.1);
- добавлены OQ-GO-11 (схема Semantic Resolution Result и критерий
  sufficient) и OQ-GO-12 (представление совместимости интерпретаций) — §22;
- evidence base дополнена [[BOT-001 First Contact Specification]] v1.0 /
  A-BOT-001-Q4 и [[Ayla MVP C01 C02 UX Inventory]] — §24.

#### v0.2 — 2026-08-20

- targeted repair: пример §15 заменён на семантически очевидный
  (`REDUCE(MUSCLE_TENSION)`, `scope.body_area = NECK` + свободная
  формулировка контекста без выдуманного Context Fact code);
- проверены и оставлены без изменений: `source_kind: canonical`
  (совместим с `canonical_status: draft` — source kind отделён от
  canonical maturity со schema 1.11) и ссылка на AYLA-DEC-0026 в §4.5
  (каноническая запись решения в [[OWNER_DECISION_REGISTER]] явно
  провозглашает Transformation Goal центральной доменной сущностью).

#### v0.1 — 2026-08-20

- создан Working Design checkpoint по семантике Goal / Outcome /
  Recommendation;
- зафиксированы established canon (§4), owner directions OD-GO-1…OD-GO-6
  (§5), рабочие модели (§8–§18), дельты к Recommendation Contract v0.4
  D-1…D-9 (§20), открытые вопросы OQ-GO-1…OQ-GO-10 (§22);
- зафиксировано расхождение рабочего разбора с proposed contract по NBA
  families (`INTERVENE` отсутствует в репозитории; v0.4 §33 использует
  `ADDRESS / SUPPORT / RECOVER / OBSERVE` как кандидатов) — оставлено
  открытым (D-8, OQ-GO-9);
- документ размещён в `05 Architecture/` рядом с документом, владеющим
  Goal/Outcome/Recommendation semantics ([[Ayla MVP Recommendation Contract]]),
  согласно [[Ayla Knowledge Area Taxonomy]].
