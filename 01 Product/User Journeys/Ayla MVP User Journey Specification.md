---
node_id: ayla.product.mvp-user-journey
title: Ayla MVP User Journey Specification
type: user-journey-specification
status: approved
decision_status: accepted
canonical_status: approved
version: "1.2"
owner: Product Owner
priority: P0
knowledge_area:
  - product
domain:
  - cross-domain
concerns:
  - privacy
  - safety
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
updated: 2026-08-08
review_cycle: monthly
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Product Essence]]"
  - "[[Ayla Product Vision]]"
  - "[[Ayla MVP Product Thesis]]"
  - "[[Ayla Product Principles]]"
  - "[[Ayla MVP Scope and Release Contract]]"
  - "[[Ayla Living Digital Twin Manifesto]]"
  - "[[Ayla User Journey Specification]]"
  - "[[Ayla MVP Documentation Roadmap]]"
  - "[[Ayla Intent Model Specification]]"
related:
  - "[[Consent Scope Registry]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Ayla Domain Event Registry]]"
  - "[[Ayla MVP Recommendation Contract]]"
  - "[[Killer PRD]]"
---

# Ayla MVP User Journey Specification

> **Статус:** Approved v1.2 (2026-08-08, Product Owner). Эволюция
> owner-approved v1.1 (2026-07-29) по итогам архитектурной Owner Decision
> Session (решения OD-1…OD-18, подтверждены Product Owner 2026-08-04), с
> финальным alignment pass по AYLA-DEC-0063…AYLA-DEC-0066 (OD-MVP-1…4,
> 2026-08-07). Состояние: approved / accepted / canonical. Положения
> имеют нормативную силу в границах MVP. OD-1…OD-18 зарегистрированы как
> AYLA-DEC-0037…AYLA-DEC-0054; OD-MVP-1…OD-MVP-4 зарегистрированы как
> AYLA-DEC-0063…AYLA-DEC-0066 в [[OWNER_DECISION_REGISTER]].
>
> **Canon Lineage.** v1.2 — Active Canon revision Knowledge Node
> `ayla.product.mvp-user-journey`, основанная на owner-approved MVP Journey
> v1.1 (2026-07-29), выборочных улучшениях draft-линии v1.1
> (2026-07-31 / 2026-08-03) и owner rulings OD-1…OD-18. Формула редакции:
> Approved v1.1 + явно принятые owner decisions + выборочные улучшения из
> draft + синхронизация с актуальным каноном. С owner approval v1.2
> предыдущая approved revision v1.1 переведена в статус `superseded`
> (`approved_v1_1.md`, 2026-08-08); историческая редакция сохраняется в
> Git history и snapshot-файле. Active Canon uniqueness по Variant C
> соблюдена: только одна revision узла находится в active canonical
> статусе.
>
> **Соглашение о метках.** Утверждения, дословно или близко следующие из
> канонических источников, помечены как *(факт — источник §)*. Положения,
> принятые Product Owner в Owner Decision Session 2026-08-04, помечены как
> *(owner decision OD-N)*. Предложения, не зафиксированные в источниках и
> не принятые владельцем, помечены **(proposal)** и подлежат review.
> Незакрытые вопросы собраны в Open Questions с классификацией по
> влиянию (A–E); вопросов, блокирующих approval этой редакции, нет.
>
> **Терминология событий (owner decision OD-15).** Различаются четыре
> понятия: *canonical event name* (имя по конвенции AYLA-DEC-0025),
> *registration status* (`registered` / `registration proposed` — статус
> записи), *registry status* (редакция реестра) и *legacy alias*
> (compatibility mapping §11 реестра, не per-event регистрация).
> Единственный источник истины по статусу событий —
> [[Ayla Domain Event Registry]] v0.4. Этот документ не создаёт новых
> domain events и не повышает их статус.

## Purpose

Назначение документа (основание — [[Ayla MVP Documentation Roadmap]] §2.1;
сохранено из approved v1.1, расширено по OD-1):

- зафиксировать нормативный сквозной пользовательский путь MVP
  ([[Ayla MVP Scope and Release Contract]] v0.3 §4) в виде 14 этапов с
  полями actor, trigger, пользовательская цель, системное действие,
  отображаемое состояние, ошибка, fallback, события, capability reference;
- описать обязательные негативные и recovery-сценарии и их поведение
  (шесть классов — owner decision OD-11);
- связать каждый этап с consent-правилами ([[Consent Scope Registry]]);
  capability mapping — исключительно как reference (owner decision OD-16);
- дать продуктовой, AI-, backend/frontend-командам и QA одну трактовку
  пользовательского потока, чтобы они не реализовывали один бизнес-процесс
  по-разному (Roadmap, вводная часть);
- **(owner decision OD-1)** зафиксировать путь вокруг Transformation Goal:
  философия journey — lifecycle approved v1.1 `Conversation →
  Understanding → Recommendation → Execution → Learning`, расширенный
  целевым якорем (Transformation Goal) и Living Digital Twin как
  непрерывным представлением контекста, состояния и прогресса; booking —
  опциональное downstream-действие; терминал journey — progress / next
  state, а не подтверждение записи;
- **(owner decision OD-2)** зафиксировать продуктовый lifecycle разговора
  (Conversation Lifecycle) как продуктовую логику, которую позже
  реализует Conversation Runtime;
- **(proposal, v0.2 — сохранено)** определить, как Ayla извлекает,
  проверяет и применяет разрешённый персональный контекст на протяжении
  всего journey, а не только на этапе 6;
- **(proposal, v0.2 — сохранено)** обеспечить, чтобы повторное
  взаимодействие становилось полезнее первого, не создавая скрытого
  profiling, устаревшей персонализации, cross-tenant contamination или
  lock-in на прошлые решения;
- определить Product Thesis Validation Scenario (см. Memory Interaction),
  без которого основная продуктовая гипотеза Ayla не считается
  проверенной. Статус этого критерия определён решением AYLA-DEC-0018
  (accepted, Option C): он не является release gate Phase 1 — Product
  Thesis Validation остаётся открытой до Phase 2.

Документ **не** описывает все будущие journeys: долгосрочные состояния
(S7 Long-term), доменные journeys (Nutrition Guidance), проактивные
сценарии и полная state machine остаются в
[[Ayla User Journey Specification]] и здесь не дублируются (см. Non-goals).

Целевая аудитория: продуктовая команда, AI-команда, backend/frontend
разработчики, QA.

## Canonical Position

- Документ — нормативный MVP-срез [[Ayla User Journey Specification]]
  (производный по AYLA-DEC-0014) и downstream от
  [[Ayla MVP Scope and Release Contract]] v0.3: релизный состав и границы
  определяет MVP Scope, этот документ их не переопределяет и не дублирует
  (owner decision OD-14).
- Выше документа: [[Ayla Constitution]], [[Ayla Product Essence]] v1.1,
  [[Ayla Product Vision]] v2.0, [[Ayla MVP Product Thesis]] v0.5,
  [[Ayla Product Principles]] v0.1; по темам Living Digital Twin
  authoritative input — [[Ayla Living Digital Twin Manifesto]] v1.0.
- Действующие owner decisions в scope этого документа: AYLA-DEC-0026
  (LDT — главный визуальный интерфейс; Transformation Goal — центральная
  доменная сущность), AYLA-DEC-0027 (три required channels), AYLA-DEC-0028
  (четыре равнозначных trigger-сценария), AYLA-DEC-0029 (28-day cycle —
  A2 exit evidence), AYLA-DEC-0033 (статус числовых порогов),
  AYLA-DEC-0034 (NO_FORMAL_RCT в initial beta), AYLA-DEC-0036 (Simple
  Reschedule — same-ID time-only), а также решения OD-1…OD-18 Owner
  Decision Session 2026-08-04 (зарегистрированы как AYLA-DEC-0037…AYLA-DEC-0054
  в [[OWNER_DECISION_REGISTER]]).
- Consent, memory phases и authorization — по [[Consent Scope Registry]]
  (факт — CSR §2, §5, §8, §10); intent types и output contract — по
  [[Ayla Intent Model Specification]] (approved v0.9.2 — действующий
  runtime-канон, Output Contract 0.5; v1.0 — draft / proposed /
  candidate, owner decision OD-7).
- Этот документ — продуктовый фундамент, а не центр синхронизации
  остальных документов: downstream документы синхронизируются относительно
  Journey, а не наоборот (owner decision OD-18).

## Terminology

Канонические продуктовые термины (owner decision OD-17). Термины не
являются взаимозаменяемыми; технические определения (storage, runtime)
этим разделом не задаются.

| Термин | Продуктовое определение |
|---|---|
| **Dialogue Turn** | Один обмен: сообщение пользователя и ответ Ayla внутри interaction. Наименьшая продуктовая единица разговора. |
| **Interaction** | Эпизод взаимодействия по одному поводу (одна потребность, один flow) внутри session или conversation; состоит из dialogue turns. |
| **Session** | Непрерывный период активности пользователя в одном канале в пределах подтверждённой identity boundary. Session context существует только внутри session (факт — CSR §10.1). |
| **Conversation** | Продуктовая рамка диалога пользователя с Ayla, в которой развивается понимание запроса, рекомендация и действие; может охватывать несколько interactions и — в пределах consent и identity boundary — продолжаться между sessions и каналами (owner decision OD-13). Conversation ≠ Session: session — технически ограниченный интервал активности, conversation — продуктовая непрерывность диалога. |
| **Transformation Goal** | Центральная доменная сущность продукта; принадлежит пользователю; желаемое направление пути (факт — AYLA-DEC-0026; Product Essence). Не текущий intent, не KPI продукта, не прогноз и не обещание результата. |
| **Living Digital Twin (LDT)** | Центральное пользовательское представление контекста, состояния и прогресса; главный визуальный интерфейс ключевых сценариев (факт — AYLA-DEC-0026; редакция owner decision OD-4: не самостоятельный Source of Truth и не единственный центр продукта). |
| **ControlAction** | Owner-approved product concept (owner decision OD-8): типизированная категория управляющих действий пользователя — управление memory, consent, personalization и conversation ownership. **Не** ProductIntent и не расширение Product Intent Registry. Пока **не** canonical registry entity: использование термина не подразумевает существования отдельного registry, capability, runtime contract или implementation — это отдельный downstream workstream. |
| **appointment** | Канонический термин для записи (создание, подтверждение, перенос); события `appointment.*` (факт — AYLA-DEC-0025). |
| **booking** | Legacy alias для appointment (факт — Domain Event Registry §11); сохраняется в канонических идентификаторах этапов «Booking creation» / «Booking confirmation» (owner ruling 2026-07-28, v0.3-final) и в UX-state tokens Roadmap §2.2 как legacy-цитата. |

Иерархия единиц разговора: **Dialogue Turn → Interaction → Session →
Conversation**. Session является channel-scoped: переход между каналами
не означает продолжение той же Session — в другом канале начинается
новая Session. Conversation может охватывать несколько Sessions и
несколько каналов (в пределах consent и identity boundary); между
Sessions переносится только разрешённая context projection, а не сама
Session и не UI state (открытый экран, локальная навигация, widget
state). Conversation ownership между каналами автоматически не
переносится (owner decision OD-13; см. Cross-channel Experience).

Терминология событий — см. баннер статуса и раздел Stage Specifications
(owner decision OD-15): *canonical event name*, *registration status*,
*registry status*, *legacy alias* — разные понятия; «canonical event» не
используется как синоним «registered domain event».

## Journey Operating Model

Принципы пути (факт — [[Ayla Product Principles]] v0.1 §4; приняты как
философия journey — owner decision OD-1):

- **Human First** — главный герой продукта — человек, не Twin и не Ayla.
- **Goal at the Center** — путь строится вокруг Transformation Goal.
- **The Path Is Visible** — пользователь видит состояние, прогресс и
  движение к цели.
- **Identity Continuity** — Twin сохраняет узнаваемую идентичность между
  версиями и состояниями.
- **Honest Representation** — факт, реконструкция, оценка, прогноз и цель
  не смешиваются и не выдаются друг за друга.
- **Memory as Continuity** — память поддерживает составной путь; объём
  сохранённых фактов не является целью (memory-first framing запрещён —
  факт, MVP Scope v0.3 §6.3; Thesis §8.2).
- **Explainable Next Step** — рекомендация объяснима и трассируема
  (Constitution Ст. VII).
- **Booking Is Downstream** — запись — downstream-действие пути, не центр
  продукта и не терминал journey.
- **User in Control** — явное подтверждение действий, управление данными,
  отказ без давления.
- **Progress Without Pressure** — прогресс без стыда, давления и
  манипуляции страхом (Manifesto §13).
- **Value on Both Sides, Neutral by Default** — экономическая
  нейтральность рекомендаций (Killer PRD §5.3; Конституция).

Базовый lifecycle journey (сохранён из approved v1.1 — owner decision
OD-1):

```text
Conversation → Understanding → Recommendation → Execution → Learning
```

Действующие ограничения operating model (факты — сохранены из approved
v1.1):

- **Один сквозной сценарий:** пользователь формулирует или уточняет
  Transformation Goal → Ayla понимает потребность и intent → подбирает
  услугу или действие → объясняет рекомендацию → пользователь подтверждает
  → Ayla выполняет подтверждённое действие → пользователь видит прогресс
  или следующее состояние (факт — MVP Scope v0.4 §4; owner decision OD-1).
- **Три required channels — один продукт:** Mobile App, MAX Mini App,
  MAX Bot — разные поверхности одной продуктовой системы, а не три
  независимых продукта (факт — AYLA-DEC-0027; MVP Scope v0.3 §8; см.
  Cross-channel Experience).
- **Два activation gate** (факт — [[Consent Scope Registry]] §10): MVP
  Phase 1 — session-only vertical slice без персистентной памяти; MVP
  Phase 2 — opt-in persistent preferences. Phase 2 не является условием
  релиза Phase 1 (AYLA-DEC-0018, accepted, Option C).
- **Автономные действия без подтверждения пользователя запрещены** (факт —
  Конституция; MVP Scope v0.3 §6.5).
- **Fail-closed по умолчанию** (факт — CSR §2): неизвестный, отсутствующий,
  просроченный или неутверждённый scope обрабатывается как запрет;
  отсутствие consent record не интерпретируется как согласие.
- **Один primary recommendation**, до двух alternatives — только по запросу
  или после отклонения primary, каждая с собственным `recommendation_id`
  (факт — [[Killer PRD]] §5.1).
- **Journey не строго линейна**: пользователь может уточнять intent и
  менять решение; обратные переходы (уточнение, «давай другую опцию»)
  допустимы (факт — полная UJS, State Transitions). Нумерация этапов
  отражает пользовательскую ответственность, а не обязательный
  однопроходный порядок исполнения: intent detection, context retrieval и
  clarification могут итерироваться.
- **Journey является trigger-agnostic** (факт — AYLA-DEC-0028): ни один
  trigger-сценарий (питание, восстановление, подготовка к событию, история
  посещений) не является центром продукта.
- **Рекомендация может завершиться без downstream action** — это
  полноценное успешное завершение journey; Goal не эквивалентен Booking
  (owner decision, план v1.2 п. 5).

Принципы operating model, добавленные в v0.2 (**proposal** — сохранены):

- **Personal Context Management — сквозная роль** всего journey наряду со
  сквозными CAP-014 (Safety), CAP-018 (Orchestration) и CAP-026 (Audit)
  (capability reference — owner decision OD-16), а не только owning
  capability этапа 6. Этап 6 фиксирует обязательную recommendation-time
  проверку контекста, но не является единственной точкой извлечения.
- **Контекст может извлекаться на нескольких точках:** session context
  bootstrap (этап 2), intent disambiguation (этап 4), clarification
  suppression — не спрашивать известное повторно (этап 5),
  recommendation-time retrieval (этап 6), execution context (этапы 10–11),
  outcome interpretation (этап 14).
- **Каждое использование контекста — в пределах активного scope** (факт —
  CSR §2); сквозная роль памяти не расширяет разрешённый доступ: принцип —
  максимально полезное использование минимально необходимого разрешённого
  контекста.

Роли (actors) в сценарии:

| Actor | Описание |
|---|---|
| User | Клиент пилота — человек с beauty/wellness-потребностью и личной Transformation Goal (персона пилота, Thesis §5) |
| Ayla (AI) | Диалоговая логика и оркестрация пути: ai-bot-platform (runtime/channel consumer) + ayla-ai-core (reusable AI logic) — рекомендуемая MVP-композиция (факт — MVP Scope v0.3 §9) |
| Backend | SoR для каталога, провайдеров, availability, записей, consent, context facts (факт — MVP Scope v0.3 §9) |
| Provider | Соло-мастер или малый салон (≤3 специалистов), подтверждающий запись (пилотные профили — Thesis §5) |

### Conversation Lifecycle

Продуктовый жизненный цикл разговора (owner decision OD-2). Описывает
исключительно пользовательскую динамику разговора — продуктовую логику,
которую позже реализует Conversation Runtime. Это **не** Conversation
Runtime, **не** Conversation FSM, **не** Conversation Storage Model и
**не** Conversation Database Schema; внутренняя реализация Conversation
Engine здесь не описывается (owner decision, план v1.2 п. 3).

Десять элементов продуктового lifecycle:

| # | Элемент | Пользовательская динамика | Связь с этапами |
|---|---|---|---|
| 1 | Начало / возобновление conversation | Пользователь открывает диалог или возвращается; известное не переспрашивается | этапы 1–2; N5.1 |
| 2 | Понимание текущего запроса | Ayla понимает, чего пользователь хочет достичь, а не только что написал | этап 4 |
| 3 | Clarification | Минимально необходимые вопросы; отказ отвечать не блокирует путь | этап 5 |
| 4 | Recommendation | Один понятный следующий шаг с объяснением | этапы 7–8 |
| 5 | Confirmation | Ничего с внешним эффектом не происходит без явного подтверждения | этап 9 |
| 6 | Transactional execution | Подтверждённое действие исполняется; подтверждение показывается только по фактически достигнутому состоянию | этапы 10–12 |
| 7 | Follow-up | Транзакционное сообщение или согласованный check-in; не скрытая рекомендация | этап 13 |
| 8 | Learning | Outcome и feedback становятся Memory Proposal; persistent write — только Phase 2 после consent и eligibility | этап 14; Memory Interaction |
| 9 | Human handoff | Передача человеку как пользовательский исход при повторных сбоях **(proposal — пороги вне Journey, см. Open Question №2)** | N6.1 |
| 10 | Завершение / приостановка flow | Завершение с прогрессом / next state — в том числе без downstream action; приостановка с возможностью возобновления | Progress and next state; N5.1 |

### Сквозные концепции: Transformation Goal, Living Digital Twin, Progress

Transformation Goal, Living Digital Twin и Progress **не являются
обязательными линейными стадиями journey** и не превращаются в
обязательные последовательные остановки каждого сценария (owner decision,
план v1.2 п. 2). Это сквозные концепции, сопровождающие пользовательский
путь. Их присутствие на конкретных этапах описано в Stage Specifications;
фазовая доступность — по MVP Scope v0.3 и разделу Scope and Deferred.

**Transformation Goal (сквозной якорь).** Центральная доменная сущность;
принадлежит пользователю (факт — AYLA-DEC-0026). Нормативные положения:

- цель принадлежит пользователю — Ayla помогает сформулировать, но не
  назначает;
- цель — не KPI продукта и не измеримый бизнес-показатель;
- цель — не прогноз: желаемое состояние не подменяется оценкой возможного
  (факт — Manifesto §7 «Цель не равна прогнозу»);
- цель — не обещание результата;
- цель связывает recommendation, action, booking, progress и Twin в
  единый путь;
- пользователь может изменить или отложить цель в любой момент;
- отсутствие готовой цели не блокирует безопасное продолжение journey:
  Ayla может помочь уточнить цель или продолжить с минимальным рабочим
  намерением (см. Negative Scenarios, N1.4);
- Transformation Goal ≠ текущий intent: intent — текущее структурированное
  намерение; связь intent с целью может быть `unknown/not_established` и
  не выдумывается (owner decision OD-7; Intent Model v1.0, candidate);
- минимальная структура цели — in scope (факт — MVP Scope v0.3 §6.1);
  детальная доменная модель цели определяется Domain-документами и здесь
  не вводится.

**Living Digital Twin (сквозное представление).** Центральное
пользовательское представление контекста, состояния и прогресса; главный
визуальный интерфейс ключевых сценариев (факт — AYLA-DEC-0026); не
самостоятельный Source of Truth и не единственный центр продукта (owner
decision OD-4). Living Digital Twin — strategic / conditional
representation capability: он не является обязательным critical-path
элементом первого MVP (AYLA-DEC-0063 / OD-MVP-1). Положения:

- Twin — долгоживущее цифровое представление пользователя, а не разовая
  генерация изображения (факт — Manifesto §3);
- Twin — key visual interface, **not mandatory on every screen** (факт —
  Manifesto §4; Product Essence §9);
- Twin объединяет восприятие состояния, прогресса и данных из разных
  областей, но не владеет доменами и не подменяет их (факт — Manifesto §3);
- Twin ≠ memory: Twin baseline и media-артефакты — authoritative backend
  domain data с собственным media consent, не persistent semantic memory
  (owner decision OD-4; разграничение сущностей — Memory Interaction);
- если конкретный релиз включает LDT, обязательные experience points
  (факт — MVP Scope v0.4 §6.4 MUST_HAVE, если LDT включён; Manifesto §14):
  baseline; управляемая фотофиксация; recognition «это я»; сигнал «это
  не похоже на меня»; correction / rebuild; identity continuity;
  comparison over time; state-class distinction; deletion / user control.
  Если LDT не включён, эти experience points не являются обязательными
  для MVP (AYLA-DEC-0063). Owning channel для визуально-зависимых
  experience — Mobile App (факт — AYLA-DEC-0027);
- классы достоверности (факт — Manifesto §9): user-entered fact, observed
  fact, reconstructed representation (включая сам Twin), inferred state,
  predicted scenario, desired outcome (Transformation Goal) — не
  смешиваются и не выдаются друг за друга;
- запрещено (факт — MVP Scope v0.3 §6.4 OUT_OF_SCOPE; Manifesto §4, §13):
  automatic idealization и универсальный body ideal; body shaming и
  манипуляция страхом; medical simulation и скрытая медицинская
  диагностика; guaranteed transformation и неподдержанный прогноз;
  identity drift; произвольная генерация аватаров; автоматическое
  обновление Twin после каждого действия;
- target image — CONDITIONAL, выражение желаемого результата (не прогноз,
  не обещание); видео — CONDITIONAL, только при подтверждённой
  необходимости для качества модели (факт — MVP Scope v0.3 §6.4).

**Progress and next state (терминальная концепция).** Journey завершается
прогрессом / следующим состоянием, а не подтверждением записи (факт — MVP
Scope v0.3 §4 шаг 10; owner decision OD-1):

- пользователь видит сравнение состояний во времени через поддерживаемые
  представления, включая Twin, если он включён в релиз;
- прогресс показывается без давления и стыда (факт — Principles 4.10;
  Manifesto §13);
- следующее состояние формулируется честно: что наблюдаемо, что оценено,
  что является целью (state-class distinction);
- отсутствие видимого изменения — тоже объяснимое состояние (факт —
  Manifesto §10);
- прогресс и next state доступны независимо от того, произошёл ли booking
  (owner decision, план v1.2 п. 5).

## Journey Overview

14 обязательных этапов (порядок и состав сохранены из approved v1.1 —
owner decision OD-3: все KEEP, с EXTEND-изменениями). Маппинг на
состояния полной UJS приведён для трассируемости и не расширяет scope.
Сквозные концепции (Transformation Goal, Living Digital Twin, Progress)
сопровождают этапы и не являются дополнительными обязательными остановками
(owner decision, план v1.2 п. 2).

| # | Этап | Соответствие полной UJS | Capability reference (proposal) |
|---|---|---|---|
| 1 | Entry | S0 Acquisition → S1 First Contact | CAP-016 |
| 2 | First interaction | S1 First Contact | CAP-016 |
| 3 | Consent request | Consent-шаги S1–S6 | CAP-002 |
| 4 | Intent detection | S3 Intent Understanding | CAP-003 |
| 5 | Clarification | S2 Discovery / S3 | CAP-003 |
| 6 | Context retrieval | S2/S3 Memory Lookup | CAP-001 |
| 7 | Recommendation | S4 Recommendation Layer | CAP-004 |
| 8 | Explanation | S4 (Explanation) | CAP-005 |
| 9 | User confirmation | S4 → S5 переход | CAP-004 |
| 10 | Availability selection | S5 Execution (slots) | CAP-010 |
| 11 | Booking creation | S5 Execution (Booking) | CAP-011 |
| 12 | Booking confirmation | S5 Confirmation | CAP-011 |
| 13 | Notification | S5/S6 уведомления | CAP-021 |
| 14 | Outcome or feedback prompt | S6 Feedback Loop | CAP-006 |

> Capability mapping — исключительно reference и **proposal** (owner
> decision OD-16; MVP Scope v0.3 §6): этот документ описывает только
> product availability и не зависит от существования CAP-ID. Capability
> mapping will be assigned during Capability Registry Wave 2
> (AYLA-DEC-0014). Enabling capabilities CAP-014 (Safety Policy
> Enforcement), CAP-018 (AI Orchestration and Tool Execution) и CAP-026
> (Audit and Observability) действуют сквозным образом на всех этапах
> (факт — Scope Contract §4.2) и не дублируются в каждой строке.

Сквозная цепочка (пользовательский слой):

```text
Entry → First interaction → Consent request → Intent detection
→ Clarification → Context retrieval → Recommendation → Explanation
→ User confirmation → Availability selection → Booking creation
→ Booking confirmation → Notification → Outcome or feedback prompt
```

Этап 3 (Consent request) — не обязательно отдельный экран: в Phase 1
обработка текущего сообщения выполняется по `service_necessity` без
consent record (факт — [[Consent Scope Registry]] §3 «Разграничение
session use и persistent consent»); явный запрос согласия требуется для
persistence, media capture, проактивности и передачи данных для другой
цели.

**Booking — опциональная downstream-ветка** (owner decision OD-3, OD-9;
факт — MVP Scope v0.3 §4): этапы 10–12 выполняются, только если
пользователь выбрал booking как next action; сценарий не обязан
завершаться записью; отказ от действия и обоснованное «ничего не делать»
— валидные исходы; journey завершается прогрессом / следующим состоянием
в обоих случаях.

Сквозной memory loop (**proposal**, v0.2 — детали в Memory Interaction):

```text
Session context bootstrap
→ Targeted retrieval
→ Context sufficiency check
→ Recommendation-time application
→ Explanation of context use
→ Outcome capture
→ Memory Proposal
→ User confirmation
→ Context Fact create / correct / supersede
→ Next journey
```

## Stage Specifications

Формат полей каждого этапа — по Roadmap §2.1: actor, trigger,
пользовательская цель, системное действие, отображаемое состояние, ошибка,
fallback, capability reference и события. «Отображаемое состояние»
использует терминологию продуктовых состояний MVP UX State Contract
(Roadmap §2.2, P1, planned): loading, clarification required,
recommendation ready, no recommendation, consent required, slot
unavailable, booking pending, booking confirmed, booking failed, retry,
human handoff. Коды ошибок — по перечню Error and Reason Code Registry
(Roadmap §6.5, planned).

Поле событий разделено на **три класса с разными владельцами контрактов**
(v0.1.1; не в каждом этапе присутствуют все три):

- **domain event** — изменение authoritative business state; единственный
  источник истины по статусу событий — [[Ayla Domain Event Registry]] v0.4
  (owner decision OD-15);
- **analytics event** — измерение поведения и funnel; рабочие имена,
  **NOT_DEFINED** до Measurement Framework (owner decision OD-15;
  informative — CSR §9.2);
- **audit event** — consent, authorization и policy checks; канонический
  перечень — [[Consent Scope Registry]] §9.1; audit — проекция/consumer
  доменных событий, не конкурирующая форма канона (AYLA-DEC-0025); как
  domain events — **NOT_DEFINED** (owner decision OD-15).

Именование и статусы событий (owner decision OD-15): различаются
*canonical event name* (конвенция AYLA-DEC-0025), *registration status*
(`registered` / `registration proposed`), *registry status* (актуальная
редакция — Domain Event Registry v0.4) и *legacy alias* (§11 Migration
Mapping — только compatibility mapping). «Canonical event» не
используется как синоним «registered domain event». Этот документ не
создаёт новых domain events и не повышает их статус. Wildcard-имена
семейств ниже — только названия семейств, а не доказательство per-event
статуса; статус каждого события проверяется по реестру отдельно.
Классификация используемых семейств (Domain Event Registry v0.4):

- `registered`: `recommendation.created`, `recommendation.superseded`,
  `recommendation.expired`, `recommendation.invalidated`,
  `recommendation.presented`, `recommendation.accepted`,
  `recommendation.declined` (§6.5), `qualified_action.attributed` (§6.6),
  `appointment.rescheduled` (§6.3; AYLA-DEC-0022 п. 9);
- `registration proposed` (CANDIDATE): `intent.*`, `consent.*`, остальные
  `appointment.*` (включая `appointment.completed` — `semantic_status:
  incomplete` до Appointment Contract, OQ-E3); `memory.*` — строго
  per-event по §6.4, без группового повышения статуса семейства:
  `registration proposed` — `memory.proposal_created`,
  `memory.proposal_confirmed`, `memory.proposal_rejected`,
  `memory.entry_created`, `memory.entry_superseded`,
  `memory.entry_expired`, `memory.entry_revoked`; candidate —
  `memory.proposal_expired`; NOT_DEFINED — `memory.entry_deleted`
  (не регистрируется; tombstone — Deletion Pipeline, OQ-E4);
- `LEGACY_ALIAS` (Domain Event Registry §11 — только справочно):
  `booking.rescheduled` → legacy alias для `appointment.rescheduled`;
  `booking.confirmed` → legacy name для `appointment.confirmed` (§6.3);
  `booking.created` — legacy alias (§1, §11); wildcard-строка `booking.*`
  существует в §11 только как compatibility adapter и не является
  per-event регистрацией; исторические migration aliases — по §11;
- `NOT_DEFINED`: отсутствующие memory events, внутренние analytics names,
  audit projections, implementation events — не выдумываются.

### Этап 1. Entry

| Поле | Значение |
|---|---|
| actor | User |
| trigger | Пользователь открывает MAX Bot (DM), переходит по deep link в MAX Mini App или запускает Mobile App (факт — AYLA-DEC-0027; journey един независимо от entry channel) |
| пользовательская цель | Получить помощь с beauty/wellness-потребностью без поиска по каталогу |
| системное действие | Показать приветствие с выбором категории состояния и возможностью свободного ввода (факт — полная UJS, Stage 1 First Message). Progressive profiling — минимальные разрешённые inputs (факт — MVP Scope v0.3 §6.1; Constitution Ст. VI) |
| отображаемое состояние | Приветственное сообщение + кнопки категорий + поле ввода (форма зависит от канала — Cross-channel Experience) |
| ошибка | Канал недоставляет сообщение / сбой платформы |
| fallback | Повторная доставка при следующем открытии; пользователь может продолжить в другом из трёх каналов (факт — AYLA-DEC-0027) **(proposal)** |
| analytics event | `session_started` **(proposal — рабочее имя, NOT_DEFINED до Measurement Framework)** |
| capability reference | CAP-016 — Conversation Experience (reference, proposal — OD-16) |

Ограничения (факт — полная UJS, Stage 1 Forbidden Behavior): не запрашивать
имя, возраст, вес при первом контакте; не начинать с анкеты; не продавать.
Trigger model: четыре равнозначных trigger-сценария — входы в путь, а не
отдельные продукты (факт — AYLA-DEC-0028; Vision §10); Food Scanner —
CONDITIONAL trigger, не центр пути.

### Этап 2. First interaction

| Поле | Значение |
|---|---|
| actor | User → Ayla |
| trigger | Пользователь выбрал категорию или написал свободный запрос |
| пользовательская цель | Выразить потребность своими словами и быть понятым |
| системное действие | Принять сообщение; подтвердить получение; начать обработку в session-only режиме. **(proposal, v0.2)** Session context bootstrap: поднять контекст текущей сессии и — при активном `preference_memory` (Phase 2) — проверить наличие релевантных актуальных фактов до ответа, не показывая их без необходимости. При необходимости Ayla помогает сформулировать или уточнить Transformation Goal (сквозная концепция — Journey Operating Model; не обязательная остановка — owner decision, план v1.2 п. 2) |
| отображаемое состояние | loading → первый содержательный ответ Ayla |
| ошибка | `MODEL_UNAVAILABLE` — LLM-провайдер недоступен |
| fallback | model/provider fallback, определённый в Release Readiness (факт — Roadmap §9.1); при полной недоступности — честное сообщение о сбое и предложение вернуться позже (факт — полная UJS, Error Recovery 3) |
| analytics event | `first_message_received` **(proposal — рабочее имя, NOT_DEFINED)** |
| capability reference | CAP-016 — Conversation Experience (reference, proposal — OD-16) |

### Этап 3. Consent request

| Поле | Значение |
|---|---|
| actor | Ayla → User |
| trigger | Наступление операции, требующей согласия: сохранение предпочтения между сессиями (Phase 2, scope `preference_memory`), media capture для Twin baseline, иное использование за пределами текущей сессии (факт — [[Consent Scope Registry]] §3, §5.7; MVP Scope v0.3 §4 consent gates) |
| пользовательская цель | Понять, зачем запрашиваются данные, и сохранить контроль |
| системное действие | Запросить согласие с указанием цели (scope), а не факта «сохранить данные»; дать возможность отклонить без прерывания диалога (факт — CSR §8 UX Requirements). Управление согласиями и памятью доступно пользователю как ControlAction — owner-approved product concept (owner decision OD-8): просмотр активных согласий, отзыв scope, отключение persistent personalization, «Что Ayla знает обо мне», удаление memory fact, «Забыть это» (факт команд — CSR §8); термин не подразумевает отдельного registry/contract/capability |
| отображаемое состояние | consent required |
| ошибка | Отсутствие, отказ или отзыв consent → **fail-closed**: операция не выполняется (факт — CSR §2) |
| fallback | Session-only обработка без сохранения (факт — CSR §5.7); сценарий продолжается |
| audit event | `consent_granted` / `consent_denied` / `consent_revoked` (факт — CSR §9.1; audit — проекция/consumer доменных событий consent, не конкурирующая форма канона — AYLA-DEC-0025) |
| domain event | `consent.granted` / `consent.revoked` (canonical event name — AYLA-DEC-0025 / Domain Event Registry v0.4 §6.2; `registration proposed`; legacy: `ConsentGranted`, `ConsentRevoked`) |
| capability reference | CAP-002 — Consent Management (reference, proposal — OD-16) |

В Phase 1 этот этап не показывает диалог согласия для понимания текущего
запроса: `intent_understanding` и `provider_selection` работают по
`service_necessity` в пределах сессии (факт — CSR §5.1/§5.2). Persistent
memory в Phase 1 технически отключена (факт — CSR §10.1).

### Этап 4. Intent detection

| Поле | Значение |
|---|---|
| actor | Ayla |
| trigger | Получено пользовательское сообщение с потребностью |
| пользовательская цель | Чтобы Ayla поняла, чего пользователь хочет достичь, а не только что написал (Query vs Intent — факт, полная UJS Stage 3) |
| системное действие | Извлечь intent и slots из сообщения; определить confidence; проверить safety constraints до перехода к рекомендации (факт — полная UJS, Stage 3 Intent Extraction / Safety Check). Поддерживаемые intent types, required/optional slots и confidence levels определяет [[Ayla Intent Model Specification]] v0.9.2 (approved/accepted — действующий runtime-канон, owner decision OD-7: 11 продуктовых intent types + sentinel `UNKNOWN`) и её machine-readable contracts — `03 AI System/Contracts/intent-registry.yaml`, `slot-registry.yaml`, `intent-output.schema.json` (contract_version 0.5) (факт — Intent Model § Intent Types, § Output Contract). Intent интерпретируется в контексте Transformation Goal и разрешённых данных; связь intent с целью читается из canonical concept source Transformation Goal, а не из intent output; если связь неизвестна, она не выдумывается (owner decision OD-7; Intent Model v1.0, candidate). **(proposal, v0.2)** Для разрешения ссылок на прошлый опыт («как в прошлый раз», «к ней», «снова») допускается targeted memory retrieval до окончательного разрешения intent — в пределах активного scope |
| отображаемое состояние | Формулировка понимания с уровнем уверенности через язык (факт — полная UJS, Stage 3 Confidence) |
| ошибка | `INTENT_UNRESOLVED` — intent не распознан или confidence ниже порога (соответствует `intent_type = UNKNOWN` со `status = unresolved` / `needs_clarification`; `UNKNOWN` — resolver sentinel, execution по нему запрещён — факт, Intent Model § Intent Types, § Output Contract) |
| fallback | Переход к этапу 5 (Clarification); при повторной неудаче — см. Negative Scenarios N1.1 |
| domain event | `intent.resolution_produced` (canonical event name — AYLA-DEC-0025 / Domain Event Registry v0.4 §6.1; `registration proposed`; результат — в payload `resolution_status`; legacy: `IntentResolved`) |
| capability reference | CAP-003 — Intent Understanding (reference, proposal — OD-16) |

Минимальный набор intent types (факт — [[Ayla Intent Model Specification]]
§ Intent Types / intent-registry.yaml; первичное требование — Roadmap §3.1):
DISCOVER_SERVICE,
FIND_SPECIALIST, BOOK_APPOINTMENT, RESCHEDULE_APPOINTMENT,
CANCEL_APPOINTMENT, ASK_ABOUT_SERVICE, ASK_ABOUT_PRICE,
ASK_ABOUT_AVAILABILITY, PROVIDE_CONTEXT, CORRECT_CONTEXT, REVOKE_CONSENT,
UNKNOWN.

Публичный Product Intent Registry не расширяется (owner decision OD-8):
управляющие команды пользователя — ControlAction, не ProductIntent;
скрытый второй intent registry в prompt или orchestration-коде запрещён.

### Этап 5. Clarification

| Поле | Значение |
|---|---|
| actor | Ayla ↔ User |
| trigger | `requires_clarification`: недостаточно обязательных слотов или низкий confidence (факт — [[Ayla Intent Model Specification]] § Output Contract / § Confidence and Clarification: поле `requires_clarification` и пять случаев его установки; полная UJS, Context Sufficiency Gate) |
| пользовательская цель | Ответить на минимум вопросов и получить решение, а не анкету |
| системное действие | Задать минимально необходимый вопрос; не более 5 вопросов за сессию Discovery (факт — полная UJS, Stage 2 Maximum Questions); при отказе отвечать — продолжить с имеющимся контекстом, обозначив неопределённость (факт — полная UJS, Handling Incomplete Answers). **(proposal, v0.2)** Clarification suppression: не задавать вопрос, ответ на который уже содержится в актуальном разрешённом факте; устаревший или конфликтующий факт не заменяет уточнение (см. Memory Interaction, Context Sufficiency Model) |
| отображаемое состояние | clarification required |
| ошибка | Пользователь не отвечает / отвечает односложно / противоречиво |
| fallback | Переформулировать вопрос с примерами; fast path «просто запиши меня» не обходит safety evaluation и явное подтверждение действия (факт — полная UJS, Context Sufficiency Gate) |
| analytics event | `clarification_requested` **(proposal — рабочее имя, NOT_DEFINED)**; вклад в clarification rate (факт — Roadmap §9.2) |
| capability reference | CAP-003 — Intent Understanding (reference, proposal — OD-16) |

Два независимых ограничения уточняющих вопросов (ремарка F2, v1.0): **UX
Discovery** — не более 5 вопросов за всю discovery-сессию (факт — полная
UJS, Stage 2 Maximum Questions): правило пользовательского взаимодействия,
ограничивает суммарное число вопросов к пользователю; **Intent
Resolution** — не более 2 последовательных clarification-подходов по
одному intent, после чего resolver обязан вернуть `intent_type = UNKNOWN`,
`status = unresolved` (факт — [[Ayla Intent Model Specification]]
§ Confidence and Clarification): правило AI runtime, ограничивает цикл
уточнения одного intent. Правила действуют на разных уровнях: первое
ограничивает UX-сессию в целом, второе — разрешение конкретного intent;
одно не заменяет и не отменяет другое.

### Этап 6. Context retrieval

| Поле | Значение |
|---|---|
| actor | Ayla (ai-bot-platform → Backend) |
| trigger | Intent resolved; требуется контекст для подбора. **(proposal, v0.2)** Это обязательная recommendation-time проверка контекста, но не единственная точка извлечения — см. Journey Operating Model |
| пользовательская цель | Чтобы Ayla учитывала только то, что пользователь разрешил |
| системное действие | Получить разрешённый контекст: в Phase 1 — только session context текущего диалога; в Phase 2 — дополнительно persistent preferences при активном `preference_memory` consent (факт — CSR §5.1/§5.2/§5.7, §10). В prompt передаются только данные, разрешённые активным scope и необходимые для конкретного запроса (факт — CSR §2 п. 8). Используемые сущности контекста различаются и не являются подмножествами друг друга (owner decision, план v1.2 п. 4 — см. Memory Interaction: backend facts, session context, persistent semantic memory и др.). **(proposal, v0.2)** Результат оформляется как Context Sufficiency Summary (см. Memory Interaction) |
| отображаемое состояние | Не отображается напрямую; результат виден в объяснении рекомендации (этап 8) |
| ошибка | `CONTEXT_NOT_ALLOWED` — запрошенный контекст не разрешён scope (fail-closed deny, факт — CSR §2) |
| fallback | Session-only режим без persistent контекста; рекомендация формируется только по текущему диалогу (факт — CSR §5.7 fallback); при недоступности памяти — см. Negative Scenarios N4.3 |
| audit event | `authorization_scope_checked`, `context_read_allowed` / `context_read_denied`, `memory_fact_used` (факт — CSR §9.1) |
| capability reference | CAP-001 — Personal Context Management (reference, proposal — OD-16) |

Whitelist допустимых персональных фактов: каноническая форма — категориальный
whitelist AYLA-DEC-0023 (категории со статусом allowed / requires dedicated
consent / forbidden, наследование политики полями, расширение — только owner
decision). Плоский список Roadmap §3.4 = Scope Contract §4.1 п. 8 —
**superseded, non-normative historical reference** (Change Control
2026-07-28); позиция «согласие на персонализацию» из него исключена
(Consent state ≠ Context Fact — см. Memory Interaction). Inferred signals не
сохраняются и не используются как самостоятельное основание рекомендации
(факт — CSR §5.7 Prohibited; полная UJS, MVP Memory Heuristic; единственный
pipeline inference → confirmation → persist — факт, AYLA-DEC-0023 п. 2).

### Этап 7. Recommendation

| Поле | Значение |
|---|---|
| actor | Ayla (ayla-ai-core Recommendation Composer) |
| trigger | Intent resolved + разрешённый контекст получен |
| пользовательская цель | Получить один понятный следующий шаг, а не каталог |
| системное действие | Выполнить decision pipeline: consent/privacy gate → safety gate → eligibility/availability → relevance → preference boost → economic-neutrality check → primary output (факт — [[Killer PRD]] §5.1). Сформировать одну primary recommendation с `recommendation_id`; кандидат, исключённый на любом этапе, не возвращается (факт — там же). Recommendation привязана к Transformation Goal, если связь установлена (owner decision OD-9). **LLM не является ranking authority** (owner decision OD-9): LLM может понимать запрос, участвовать в clarification и формировать explanation, но admissible set, ranking constraints, eligibility и authoritative ordering определяются каноническими правилами, registries и authoritative backend data. `no_action` (обоснованное «ничего не делать») — полноценный объяснимый результат (owner decision OD-9; факт — MVP Scope v0.4 §5 п. 6). **(proposal, v0.2)** Роль памяти не сводится к preference boost — см. Recommendation and Proactivity Gates, «Memory influence model» |
| отображаемое состояние | recommendation ready (одна карточка primary); no recommendation — если кандидатов не осталось |
| ошибка | `NO_CANDIDATES`; `SAFETY_BLOCKED`; `ranking_economic_neutrality_alert` (внутренний policy/observability alert, не user-facing ошибка: блокирует выдачу до разбора — факт, Killer PRD §5.2/§5.3) |
| fallback | При `NO_CANDIDATES` — честное состояние no recommendation + обычный поиск/запись без персонализированной primary (факт — Killer PRD §5.3 Fallback); при safety-блокировке — Boundary Handling (см. Negative Scenarios N4.5) |
| domain event | `recommendation.created` (Domain Event Registry v0.4 §6.5, `registered`; публикуется после persistence immutable decision record — [[Ayla MVP Recommendation Contract]] v0.3 §15; legacy: `RecommendationCreated`) и `recommendation.presented` (там же, `registered`; доставка каналу, owner Channel Delivery / Interaction, `presented ≠ viewed`; legacy: `RecommendationShown`) |
| analytics event | `recommendation_created` (рабочее имя, NOT_DEFINED — owner decision OD-15; informative — CSR §9.2, владелец схемы — Killer PRD) |
| capability reference | CAP-004 — Recommendation Formation (reference, proposal — OD-16) |

Персистентность рекомендации, lifecycle (projection: active / superseded /
expired / invalidated) и expiry/invalidation определяются
[[Ayla MVP Recommendation Contract]] v0.3 (§3, §14, §22). Recommendation
intent — system-owned структурированная цель recommendation pass: она не
изменяет user intent и не выдаётся за выбор пользователя, не даёт права на
side effect (owner decision OD-7; Intent Model v1.0, candidate).

### Этап 8. Explanation

| Поле | Значение |
|---|---|
| actor | Ayla → User |
| trigger | Primary recommendation сформирована |
| пользовательская цель | Понять, почему предложено именно это |
| системное действие | Показать объяснение «почему эта рекомендация» и какой разрешённый контекст применён (факт — Scope Contract §4.1 п. 9; Конституция Ст. VII). Объяснение соответствует фактически использованному контексту, не заявляет неиспользованные факты и не раскрывает sensitive context (факт — Capability Registry §6.5, key invariants CAP-005). Уровень уверенности показывается в поддерживаемой продуктом форме — не обязательные проценты (факт — Manifesto §10). **(proposal, v0.2)** Персонализация, которую Ayla не может объяснить пользователю, недопустима (см. Non-goals) |
| отображаемое состояние | Карточка рекомендации с объяснением (inline attribution применённого контекста — факт, Killer PRD §6.1 п. 3) |
| ошибка | Объяснение не может быть сформировано без раскрытия запрещённого контекста |
| fallback | Редактированное (redacted) объяснение только по разрешённым фактам; правило «без объяснения рекомендация не показывается» — **(proposal, не утверждено; открыто до сверки с будущим Explanation Contract — owner decision OD-9, см. Open Question №4)** |
| analytics event | `recommendation_explanation_rendered` (рабочее имя, NOT_DEFINED; informative — CSR §9.2) |
| capability reference | CAP-005 — Explanation and Context Attribution (reference, proposal — OD-16) |

### Этап 9. User confirmation

| Поле | Значение |
|---|---|
| actor | User → Ayla |
| trigger | Пользователю показана рекомендация с объяснением |
| пользовательская цель | Контролировать действие: ничего не происходит без явного согласия |
| системное действие | Ожидать явное подтверждение; без него не создавать запись и не выполнять side effect (факт — Конституция; MVP Scope v0.3 §6.5; owner decision OD-10). Пользователь выбирает реалистичный следующий шаг: self-care action, check-in, plan update, information, booking или no action — обоснованное «ничего не делать» как валидный исход (owner decision OD-9; факт — MVP Scope v0.3 §5). Acceptance recommendation не означает booking; booking — один из downstream actions, а не цель journey (owner decision OD-9). После первого отклонения primary — зафиксировать `rerank_reason` и предложить alternative в пределах установленного лимита (одновременно не более одной primary и до двух alternative — факт, Killer PRD §5.1). После повторного или явно жёсткого отказа дальнейшие предложения подавляются: принять отказ без давления (факт — полная UJS, Proactive Suppression Rules / User Communication) |
| отображаемое состояние | recommendation ready + CTA подтверждения; после отказа — нейтральное acknowledgement |
| ошибка | Пользователь отклоняет или игнорирует предложение |
| fallback | Отказ — валидный исход: после окончательного (повторного или жёсткого) отказа Ayla не предлагает новых вариантов и не инициирует повторное (факт — полная UJS, User Communication); см. Negative Scenarios N2.5 |
| domain event | `recommendation.accepted` при явном выборе варианта (Domain Event Registry v0.4 §6.5, `registered`; acceptance ≠ booking completion, `acceptance_action` обязателен — [[Ayla MVP Recommendation Contract]] v0.3 §17; legacy: `RecommendationAccepted`) / `recommendation.declined` при явном отказе (там же, `registered`; бездействие ≠ decline) |
| analytics event | `recommendation_dismissed` (рабочее имя, NOT_DEFINED; informative — CSR §9.2) |
| capability reference | CAP-004 — Recommendation Formation (reference, proposal — OD-16; acceptance как часть lifecycle рекомендации; доставка UX — CAP-016) |

### Этап 10. Availability selection

| Поле | Значение |
|---|---|
| actor | User ↔ Ayla ↔ Backend |
| trigger | Пользователь подтвердил рекомендацию и выбрал booking как next action |
| пользовательская цель | Выбрать удобное время |
| системное действие | Запросить актуальные слоты у Backend (SoR availability, факт — Scope Contract §6); показать доступные варианты. Displayed slot не является reservation; slot проверяется при commit booking (факт — Capability Registry §6.10, key invariants CAP-010). **(proposal, v0.2)** Execution context: при показе слотов учитывать актуальные разрешённые факты (предпочтение времени, прошлый мастер), не скрывая альтернатив (anti-lock-in, см. Memory Interaction). **Slot hold (факт — AYLA-DEC-0021 п. 3, v0.3-final):** при выборе слота пользователем выполняется цепочка «slot selected → hold acquired → confirmation in progress»; hold создаётся с серверным `expires_at` (TTL 15 минут — платформенный параметр); hold не показывается пользователю до его фактического создания; внутренние термины (ledger, locking, reservation boundary) пользователю не отображаются |
| отображаемое состояние | Список слотов; slot unavailable — если слотов нет; после выбора — «Слот временно закреплён за вами до HH:MM. Завершите запись в течение 15 минут» (время — серверный `expires_at`, факт — AYLA-DEC-0021) |
| ошибка | `NO_AVAILABLE_SLOTS` |
| fallback | Предложить альтернативу: другой мастер или другое время (факт — полная UJS, Error Recovery 1); см. Negative Scenarios N2.4 |
| analytics event | `availability_requested` / `slots_shown` **(proposal — рабочие имена, NOT_DEFINED)** |
| capability reference | CAP-010 — Availability Management (reference, proposal — OD-16) |

### Этап 11. Booking creation

| Поле | Значение |
|---|---|
| actor | Ayla → Backend |
| trigger | Пользователь выбрал слот |
| пользовательская цель | Чтобы запись была создана ровно одна и на выбранных условиях |
| системное действие | Вызвать tool `create_appointment` (минимальный набор tools — факт, Roadmap §6.3); Backend создаёт Appointment и возвращает фактическое состояние; Booking Request, Booking Created и Confirmed Booking не взаимозаменяемы (legacy-цитата — полная UJS, Stage 5 Booking). **Подтверждение hold (факт — AYLA-DEC-0021 п. 3, v0.3-final):** цепочка «slot selected → hold acquired → confirmation in progress» завершается одной транзакцией — заблокировать hold, проверить статус и серверный TTL, повторно проверить актуальные Rule/Block/external busy, создать Appointment, перевести hold в `confirmed`. **Simple Reschedule (owner decision OD-14; факт — AYLA-DEC-0022 п. 1, п. 9; AYLA-DEC-0036):** same-ID time-only перенос в пределах того же Offering — тот же `appointment_id`, монотонная `version`, AppointmentRevision, одна атомарная операция, событие `appointment.rescheduled`; механика `cancel_then_create_new_booking` для переноса запрещена. Смена услуги/мастера, replacement, re-offer, cross-tenant перенос, изменение цены/длительности — deferred (AYLA-DEC-0022; см. Scope and Deferred) |
| отображаемое состояние | booking pending (confirmation in progress; hold-индикатор из этапа 10 остаётся до результата) |
| ошибка | `APPOINTMENT_CONFLICT`, `TOOL_TIMEOUT`, `APPOINTMENT_NOT_CONFIRMED`, `SLOT_TAKEN` (факт — AYLA-DEC-0021 п. 3), hold expired (истёкший hold не подтверждается — факт, там же); stale state / version conflict — отказ без изменений исходной записи (факт — AYLA-DEC-0022 п. 10) |
| fallback | После expiry hold — отключить подтверждение и предложить повторную проверку доступности (факт — AYLA-DEC-0021); при нарушении занятости — понятный пользователю `SLOT_TAKEN` без внутренних терминов; показать booking failed с честным описанием и recovery path: повторить, выбрать другой слот, записаться позже (факт — полная UJS, Error Recovery 3; Success Criteria — «пользователь получил честное описание ошибки и Recovery path»); см. Negative Scenarios N3.1–N3.3 |
| domain event | `appointment.created` (canonical event name — AYLA-DEC-0025 / Domain Event Registry v0.4 §6.3; `registration proposed`; legacy: `AppointmentCreated`, `booking.created` — legacy alias, Domain Event Registry §11); при Simple Reschedule — `appointment.rescheduled` (Domain Event Registry v0.4 §6.3, `registered`; AYLA-DEC-0022 п. 9) |
| capability reference | CAP-011 — Appointment Management (reference, proposal — OD-16) |

### Этап 12. Booking confirmation

| Поле | Значение |
|---|---|
| actor | Backend / Provider → Ayla → User |
| trigger | Backend подтвердил переход Appointment в authoritative `confirmed` state (hold → `confirmed`, факт — AYLA-DEC-0021 п. 3) |
| пользовательская цель | Получить достоверное подтверждение (кто, когда, где) |
| системное действие | Показать user-facing confirmation только после получения authoritative confirmed state (факт — полная UJS, Stage 5 Booking); подтвердить детали и предложить напоминание (факт — полная UJS, Confirmation) |
| отображаемое состояние | booking confirmed |
| ошибка | Провайдер не подтверждает / отклоняет запись → `APPOINTMENT_NOT_CONFIRMED`; задержка authoritative подтверждения — подтверждение не показывается до фактического состояния (см. Negative Scenarios N3.3) |
| fallback | Не показывать подтверждение неподтверждённой записи (факт — полная UJS, Success Criteria: «Ayla подтвердила только фактически достигнутое состояние»); предложить альтернативный слот/мастера **(proposal)**; см. Negative Scenarios N3.1 |
| domain event | `appointment.confirmed` (canonical event name — AYLA-DEC-0025 / Domain Event Registry v0.4 §6.3; `registration proposed`; legacy: `AppointmentConfirmed`, `booking.confirmed` — legacy alias, Domain Event Registry §6.3/§11); при соблюдении условий — `qualified_action.attributed` с `recommendation_id` (Domain Event Registry v0.4 §6.6, `registered`; owner Attribution / Measurement, правила атрибуции — Killer PRD §6.2 и [[Ayla MVP Recommendation Contract]] v0.3 §18; legacy: `QualifiedActionAttributed`) |
| analytics event | `booking_confirmation_shown` **(proposal — legacy-маркер; NOT_DEFINED: канонического analytics event в Domain Event Registry v0.4 нет, registry gap — Open Question №8 approved v1.1)** |
| capability reference | CAP-011 — Appointment Management (reference, proposal — OD-16) |

Подтверждённая запись в пределах attribution window может составить
`killer_moment` при выполнении всех пяти условий (факт — Killer PRD §6.1);
последующая отмена не удаляет историческое событие (факт — Killer PRD §6.3
«Отмена записи»). Attribution осуществляется через `recommendation_id` —
минимальный direct linkage (owner decision OD-9; факт — MVP Scope v0.3
§6.3).

### Этап 13. Notification

| Поле | Значение |
|---|---|
| actor | Ayla → User |
| trigger | Подтверждение записи; приближение времени записи (напоминание, если пользователь его запросил на этапе 12) |
| пользовательская цель | Не забыть о записи; иметь детали под рукой |
| системное действие | Отправить транзакционное уведомление по записи (факт — MVP Scope v0.3 §6.1: Notification — транзакционные уведомления по записи). Follow-up после услуги — транзакционное сообщение либо согласованный check-in; follow-up не превращается в скрытую recommendation (owner decision OD-13) |
| отображаемое состояние | Уведомление в канале пользователя (MAX Bot — conversational/notification companion; Mobile App / MAX Mini App — по channel capability, см. Cross-channel Experience) |
| ошибка | Недоставка уведомления |
| fallback | Детали записи доступны по запросу в диалоге и в Mini App **(proposal)**; повторная отправка уведомления по запросу пользователя **(proposal)** |
| analytics event | `notification_sent` / `notification_failed` **(proposal — рабочие имена, NOT_DEFINED)** |
| capability reference | CAP-021 — Notification Coordination (reference, proposal — OD-16) |

Проактивные уведомления вне транзакционного контура записи в MVP не
выполняются: Phase 1 работает в режиме no proactive recommendations
(факт — CSR §10); persistent memory сама по себе не открывает proactive
behavior (owner decision OD-10).

### Этап 14. Outcome or feedback prompt

| Поле | Значение |
|---|---|
| actor | Ayla → User |
| trigger | Время записи прошло (запись состоялась или завершилась) либо завершён иной подтверждённый next action; надёжный доменный триггер — см. Open Question №8 (OQ-E3) |
| пользовательская цель | Быстро оценить результат одним действием |
| системное действие | Спросить, как прошло, с прогрессивным раскрытием (базовая оценка → при негативе уточнение причины) (факт — полная UJS, Stage 6 Feedback Collection). Результат и follow-up становятся continuity input (факт — MVP Scope v0.4 §4 шаг 9, PARTIAL). Feedback создаёт только Memory Proposal — предложение сохранить знание, допускается уже в Phase 1; Memory Proposal не является persistent write, не требует публикации незарегистрированных `memory.*` events и не изменяет долгосрочную память (owner decision OD-12). Persistent memory обновляется только после consent, purpose validation, eligibility и Phase 2 rollout (owner decision OD-12; факт — CSR §10.2). **(proposal, v0.2)** Этап 14 — не конец journey, а вход в Memory Evaluation and Update (см. Memory Interaction): outcome интерпретируется, классифицируется и — после подтверждения пользователя — становится входом следующего journey |
| отображаемое состояние | Сообщение с вариантами оценки; путь продолжается к progress / next state независимо от исхода booking (Journey Operating Model) |
| ошибка | Пользователь не отвечает — молчание не интерпретируется как согласие или отрицание (факт — полная UJS, Learning Signals) |
| fallback | Не повторять prompt навязчиво; feedback остаётся опциональным **(proposal)**; задержка доменного события завершения не блокирует пользовательский путь (см. Negative Scenarios N3.3) |
| domain event | `appointment.completed` (canonical event name — AYLA-DEC-0025 / Domain Event Registry v0.4 §6.3; `registration proposed`, `semantic_status: incomplete` до Appointment Contract, OQ-E3) — входной доменный триггер этапа, не событие самого feedback prompt; `memory.entry_superseded` — candidate mapping для `ContextFactCorrected` (AYLA-DEC-0024 п. 4; `registration proposed`, per-event — owner decision OD-15) |
| analytics event | `feedback_received` **(proposal — рабочее имя, NOT_DEFINED)** |
| capability reference | CAP-006 — Outcome Capture (reference, proposal — OD-16; в MVP — только простой feedback prompt; advanced outcome learning deferred — факт, Scope Contract §5) |

## Negative Scenarios

Состав обязателен (факт — Roadmap §2.1). Сценарии организованы в **шесть
классов** (owner decision OD-11); содержание сценариев approved v1.1
(N1–N9) сохранено и дополнено сценариями, закрывающими принятые owner
decisions. Journey фиксирует пользовательский outcome; runtime mechanics
(retry, reconciliation, locking, idempotency и аналогичные механизмы)
остаются за пределами этого документа (owner decision OD-11). Для каждого
сценария: триггер, поведение системы, пользовательское состояние /
outcome, capability reference.

### Класс 1. Understanding / Interaction

**N1.1. Ayla не поняла запрос (misunderstanding).**

- **Триггер:** `INTENT_UNRESOLVED` — intent не распознан или confidence
  ниже порога после этапов 4–5.
- **Поведение системы:** честно признать неопределённость, не имитировать
  понимание; уточнить несколько деталей или помочь найти специалиста
  (факт — полная UJS, Edge Case 3); low-confidence не маскируется как
  определённый intent (факт — Capability Registry §6.3, key invariants
  CAP-003).
- **Пользовательский outcome:** clarification required; после повторной
  неудачи — human handoff **(proposal)**.
- **Capability reference:** CAP-003 (reference, proposal — OD-16).

**N1.2. Clarification loop.**

- **Триггер:** повторные clarification-подходы по одному intent.
- **Поведение системы:** действуют два независимых лимита (этап 5, ремарка
  F2): не более 2 последовательных подходов по одному intent — resolver
  возвращает `UNKNOWN` / `unresolved` (факт — Intent Model § Confidence
  and Clarification); не более 5 вопросов за discovery-сессию (факт —
  полная UJS). После исчерпания — продолжение с обозначенной
  неопределённостью или честное завершение ветки.
- **Пользовательский outcome:** путь не зацикливается; пользователь не
  получает анкету.
- **Capability reference:** CAP-003 (reference, proposal — OD-16).

**N1.3. Invalid structured output.**

- **Триггер:** результат AI-обработки не проходит проверку output contract
  (факт существования контракта — Intent Model § Output Contract,
  contract_version 0.5).
- **Поведение системы:** невалидный результат не исполняется и не
  показывается как понимание; трактуется как сбой класса N1.1/N3.4:
  clarification или честное сообщение о сбое.
- **Пользовательский outcome:** пользователь не видит некорректную
  интерпретацию; путь продолжается с валидного состояния.
- **Capability reference:** CAP-018 (reference, proposal — OD-16).

**N1.4. Transformation Goal не сформулирована (unresolved goal).**

- **Триггер:** пользователь не может или не хочет формулировать
  Transformation Goal.
- **Поведение системы:** Ayla предлагает помощь в уточнении цели
  минимальными вопросами или продолжение с минимальным рабочим намерением;
  давление запрещено (owner decision OD-3; draft v1.1 N1).
- **Пользовательский outcome:** отложить цель; изменить её позже;
  продолжить без цели — путь продолжается с явно обозначенной
  неопределённостью; Twin baseline и рекомендации не блокируются.
- **Capability reference:** capability mapping will be assigned during
  Capability Registry Wave 2 (owner decision OD-16).

### Класс 2. Recommendation / Availability

**N2.1. Нет подходящей рекомендации (no recommendation).**

- **Триггер:** `NO_CANDIDATES` — все кандидаты исключены на этапах
  eligibility/relevance.
- **Поведение системы:** показать честное состояние no recommendation, не
  выдумывать рекомендацию (факт — Killer PRD §5.3 Fallback).
- **Пользовательский outcome:** no recommendation + вариант обычного
  поиска; альтернативный next action (self-care, information, check-in).
- **Capability reference:** CAP-004, CAP-008 (reference, proposal — OD-16).

**N2.2. Нет подходящей услуги (no service).**

- **Триггер:** запрошенная услуга отсутствует в seed-каталоге пилота
  (ограничен — факт, MVP Scope v0.3; approved v1.1 N3).
- **Поведение системы:** честно сообщить об ограничении каталога; не
  подменять отсутствующую услугу нерелевантной.
- **Пользовательский outcome:** изменить запрос, уточнить ограничения,
  выбрать «ничего не делать».
- **Capability reference:** CAP-008 (reference, proposal — OD-16).

**N2.3. Специалист / провайдер недоступен (no provider).**

- **Триггер:** `PROVIDER_INELIGIBLE` — провайдер/специалист не принимает
  запись (факт — Capability Registry §6.9, key invariants CAP-009).
- **Поведение системы:** исключить кандидата до показа primary; если
  недоступность выявлена после показа — честно сообщить и предложить
  alternative (факт — Killer PRD §5.1: eligibility до ranking).
- **Пользовательский outcome:** альтернативная рекомендация с объяснением
  замены **(proposal)**.
- **Capability reference:** CAP-009 (reference, proposal — OD-16).

**N2.4. Нет свободных слотов (no slot).**

- **Триггер:** `NO_AVAILABLE_SLOTS` на этапе 10.
- **Поведение системы:** предложить альтернативу — другой мастер или
  другое время (факт — полная UJS, Error Recovery 1); повторный прогон
  Recommendation Composer с уточнённым constraint, alternative получает
  собственный `recommendation_id` (факт — Killer PRD §5.1).
- **Пользовательский outcome:** slot unavailable + альтернативные варианты;
  путь не обрывается на отсутствии слотов.
- **Capability reference:** CAP-010 (reference, proposal — OD-16).

**N2.5. Пользователь отклоняет предложение (recommendation rejected).**

- **Триггер:** пользователь отклоняет primary recommendation на этапе 9.
- **Поведение системы:** после первого отклонения — зафиксировать
  `rerank_reason`, повторно пройти Composer с уточнённым constraint и
  предложить alternative в пределах лимита (не более двух) (факт — Killer
  PRD §5.1). После повторного или явно жёсткого отказа дальнейшие
  предложения подавляются: жёсткий отказ («не напоминай») — блокировка без
  `reconsider_after`, мягкий — нейтральное acknowledgement без CTA (факт —
  полная UJS, Proactive Suppression Rules / User Communication).
  Отклонённая рекомендация не получает атрибуцию (факт — Killer PRD §6.2).
- **Пользовательский outcome:** альтернатива с объяснением либо спокойное
  завершение без давления (факт — полная UJS, Anti-pattern 3 «Ayla давит»).
- **Capability reference:** CAP-004 (rerank), CAP-016 (поведение диалога)
  (reference, proposal — OD-16).

**N2.6. Обоснованное «ничего не делать» (no_action).**

- **Триггер:** по совокупности контекста оптимальное действие — отсутствие
  действия.
- **Поведение системы:** Ayla объясняет, почему «ничего не делать» —
  обоснованный следующий шаг (owner decision OD-9; факт — MVP Scope v0.3
  §5 п. 6). Рекомендация не навязывается.
- **Пользовательский outcome:** принять, отклонить, запросить альтернативу;
  завершение без downstream action — полноценный успешный исход journey
  (owner decision, план v1.2 п. 5); путь продолжается к check-in /
  progress.
- **Capability reference:** CAP-004 (reference, proposal — OD-16).

### Класс 3. Transactional

**N3.1. Запись не подтверждена (booking failure).**

- **Триггер:** `APPOINTMENT_NOT_CONFIRMED` или `APPOINTMENT_CONFLICT` —
  backend/provider не перевёл Appointment в `confirmed`.
- **Поведение системы:** не показывать подтверждение неподтверждённой
  записи (факт — полная UJS, Stage 5 Success Criteria); сообщить
  фактическое состояние и предложить recovery: другой слот, другой
  мастер, повторить позже (факт — полная UJS, Error Recovery).
- **Пользовательский outcome:** booking failed + recovery path; прогресс /
  next state не зависят от успеха booking.
- **Capability reference:** CAP-011 (reference, proposal — OD-16).

**N3.2. Stale state / version conflict.**

- **Триггер:** состояние, на котором основан выбор пользователя, устарело:
  `SLOT_TAKEN`, hold expired, конфликт версий при подтверждении (факт —
  AYLA-DEC-0021 п. 3; AYLA-DEC-0022 п. 10).
- **Поведение системы:** истёкший hold не подтверждается; при конфликте
  исходная запись и reservation остаются без изменений; предложить
  повторную проверку доступности (факт — AYLA-DEC-0021; AYLA-DEC-0022).
- **Пользовательский outcome:** понятный `SLOT_TAKEN` без внутренних
  терминов; пользователь повторяет выбор на актуальных данных.
- **Capability reference:** CAP-010, CAP-011 (reference, proposal — OD-16).

**N3.3. Authoritative confirmation delay (domain-event delay).**

- **Триггер:** задержка authoritative состояния или доменного события
  (подтверждение записи, завершение услуги; `appointment.completed` —
  `semantic_status: incomplete`, OQ-E3).
- **Поведение системы:** подтверждение показывается только по фактически
  достигнутому состоянию (факт — полная UJS, Success Criteria); follow-up
  и пользовательский путь не блокируются ожиданием события.
- **Пользовательский outcome:** честное промежуточное состояние без
  имитации завершённости.
- **Capability reference:** CAP-011, CAP-021 (reference, proposal — OD-16).

**N3.4. Tool или LLM недоступен (tool failure).**

- **Триггер:** `TOOL_TIMEOUT` / `MODEL_UNAVAILABLE` на любом этапе,
  использующем tool call или LLM.
- **Поведение системы:** применить model/provider fallback (факт — Roadmap
  §9.1); при недоступности — извиниться и предложить альтернативу:
  записаться позже или дать контакты мастера для прямой записи (факт —
  полная UJS, Error Recovery 3); дублирование side effects при retry
  недопустимо (идемпотентность tool calls — факт, Roadmap §6.3; runtime
  mechanics — вне этого документа, owner decision OD-11).
- **Пользовательский outcome:** retry; при повторном сбое — human handoff
  **(proposal)**.
- **Capability reference:** CAP-018 (reference, proposal — OD-16).

### Класс 4. Consent / Memory / Safety

**N4.1. Отсутствует consent (no consent).**

- **Триггер:** операция требует scope, по которому нет effective consent
  record (отсутствует, `denied`, `revoked`, `expired`) — `CONSENT_REQUIRED`.
- **Поведение системы:** fail-closed deny (факт — CSR §2 п. 2; §7
  «отсутствие consent record не интерпретируется как согласие»); предложить
  session-only продолжение либо явный запрос согласия с названием цели;
  negative test «отсутствие consent → deny» обязателен к Phase 2 (факт —
  CSR §10.2).
- **Пользовательский outcome:** consent required; диалог не прерывается
  при отказе (факт — CSR §8 UX Requirements).
- **Capability reference:** CAP-002 (reference, proposal — OD-16).

**N4.2. Отзыв consent (consent revoked).**

- **Триггер:** пользователь отзывает scope или отключает persistent
  personalization (ControlAction — owner decision OD-8).
- **Поведение системы:** fail-closed: новое использование прекращается
  немедленно; сохранённые предпочтения помечаются `revoked` и перестают
  использоваться в `provider_selection`/`intent_understanding`;
  подтверждение пользователю, что именно изменилось (факт — CSR §2, §5.7,
  §7, §8).
- **Пользовательский outcome:** отзыв одной командой; путь продолжается в
  session-only режиме; несвязанная функциональность сохраняется.
- **Capability reference:** CAP-002 (reference, proposal — OD-16).

**N4.3. Память недоступна или не разрешена (memory unavailable).**

- **Триггер:** persistent memory отключена (Phase 1), отозвана или
  недоступна для текущей операции (owner decision OD-11; факт — CSR §10).
- **Поведение системы:** session-only продолжение без имитации памяти;
  Ayla не заявляет знание, к которому не имеет права или доступа;
  управление памятью — через ControlAction (owner decision OD-8).
- **Пользовательский outcome:** путь продолжается по текущему диалогу;
  ограничение честно объясняется при необходимости.
- **Capability reference:** CAP-001 (reference, proposal — OD-16).

**N4.4. Запрос на удаление (deletion request).**

- **Триггер:** пользователь запрашивает удаление данных: «Забыть это»,
  удаление memory fact, удаление исходных и производных Twin-данных
  (ControlAction — owner decision OD-8; факт команд — CSR §8).
- **Поведение системы:** удаление выполняется с подтверждением, что именно
  удалено; производные данные рассматриваются как чувствительные
  соразмерно исходным (факт — Manifesto §11/§12; CSR §8); до завершения
  удаления данные не используются в новых решениях **(proposal)**.
- **Пользовательский outcome:** выборочное или полное удаление с просмотром
  перед удалением; путь продолжается без удалённых данных.
- **Capability reference:** CAP-001, CAP-002 (reference, proposal — OD-16).

**N4.5. Рекомендация заблокирована safety gate (safety block).**

- **Триггер:** `SAFETY_BLOCKED` — safety gate Recommendation Composer
  обнаружил конфликт с safety-critical контекстом или competence boundary
  (факт — Killer PRD §5.1 этап 2; полная UJS, Stage 3 Safety Check).
- **Поведение системы:** остановить обработку и перейти в S8 Boundary
  Handling: не подтверждать и не продолжать небезопасный путь; задать
  только минимальные вопросы о срочности и red flags; предложить безопасный
  следующий шаг или направление к квалифицированному специалисту (факт —
  полная UJS, Edge Case 2; при явно сообщённом срочном симптоме —
  safety-routing flow, факт — Killer PRD §4.1 OD-K6).
- **Пользовательский outcome:** boundary message без CTA на заблокированную
  услугу; безопасная альтернатива — только после Boundary Handling (факт —
  полная UJS, State Transitions S8).
- **Capability reference:** CAP-014 (reference, proposal — OD-16).

### Класс 5. Continuity / Channel

**N5.1. Пользователь прерывает и возобновляет путь (abandon / resume).**

- **Триггер:** пользователь прерывает путь на любом этапе и возвращается
  позже — в том же или другом канале.
- **Поведение системы:** путь возобновляется с сохранённого состояния; в
  Phase 1 — в пределах подтверждённой identity boundary: в том же канале —
  продолжение той же Session при непрерывной активности, в другом канале —
  новая Session с разрешённой context projection (Session не продолжается
  между каналами); при активном Phase 2
  consent — с persistent continuity; известное не переспрашивается
  (owner decision OD-13; факт — CSR §10; clarification suppression,
  proposal).
- **Пользовательский outcome:** продолжить, начать заново, удалить
  сохранённое; при отсутствии consent на continuity — новый вход без
  повторного использования прошлых данных.
- **Capability reference:** CAP-016, CAP-001 (reference, proposal — OD-16).

**N5.2. Прерывание канала / degraded mode (interrupted channel).**

- **Триггер:** потеря сети или деградация канала (особенно Mobile App).
- **Поведение системы:** честное сообщение о деградации; уже полученные
  состояния (цель, прогресс, детали записи) остаются видимыми из последнего
  известного состояния; действия, требующие backend, не имитируются
  **(proposal — draft v1.1 N11)**.
- **Пользовательский outcome:** read-only просмотр последнего
  синхронизированного состояния; без скрытых offline-записей действий;
  путь возобновляется после восстановления связи.
- **Capability reference:** CAP-016 (reference, proposal — OD-16).

**N5.3. Конфликт аккаунтов между каналами (account linking conflict).**

- **Триггер:** при account linking обнаружены два разных аккаунта или
  конфликт идентичности между каналами.
- **Поведение системы:** конфликт не разрешается молча; пользователю
  показывается, какие идентичности конфликтуют, и предлагается явный
  выбор; до разрешения cross-channel continuity для конфликтующих
  аккаунтов не активируется **(proposal — draft v1.1 N10; условия
  continuity — owner decision OD-13)**.
- **Пользовательский outcome:** подтвердить связку, оставить аккаунты
  раздельными, запросить удаление лишнего; каждый канал продолжает работать
  со своей сессией без слияния данных.
- **Capability reference:** capability mapping will be assigned during
  Capability Registry Wave 2 (owner decision OD-16).

### Класс 6. Human / Operations

**N6.1. Human handoff.**

- **Триггер:** повторные сбои понимания или исполнения (N1.1, N3.4);
  пользователь явно просит человека.
- **Поведение системы:** handoff — валидный пользовательский исход, а не
  скрытый тупик **(proposal — пороги и процедура не определены в
  источниках; требуется решение в Pilot Operations Runbook, Roadmap §9.3,
  P1 — см. Open Question №2)**.
- **Пользовательский outcome:** пользователь получает понятный статус
  передачи и дальнейшие ожидания.
- **Capability reference:** CAP-016 (reference, proposal — OD-16).

**N6.2. Видимая ручная интервенция (manual intervention).**

- **Триггер:** повторяющаяся ручная операционная интервенция (manual
  operations пилота) становится видимой пользователю.
- **Поведение системы:** честная коммуникация ограничения пилота без
  имитации автоматики; ручное вмешательство не выдаётся за автоматическое
  действие системы **(proposal — draft v1.1 N16)**.
- **Пользовательский outcome:** действие завершается с явным статусом;
  путь не блокируется.
- **Capability reference:** capability mapping will be assigned during
  Capability Registry Wave 2 (owner decision OD-16).

## Memory Interaction

MVP-срез правил памяти полной UJS (What Ayla Remembers / When Memory is
Created / When Memory is Used); полная модель — в UJS и ADR-0012. Раздел
сохраняет approved-содержание (v0.2 proposal-слой с метками) и усилен
явным разграничением сущностей (owner decision, план v1.2 п. 4).

### Независимость сущностей контекста и памяти

Следующие сущности **независимы, имеют собственных владельцев и жизненные
циклы; ни одна не является подмножеством другой** (owner decision, план
v1.2 п. 4). Этот документ не отождествляет их: LDT ≠ Memory, Session ≠
Memory, Backend Facts ≠ Memory и т.п.

| Сущность | Что это | Владелец / lifecycle | Persistence |
|---|---|---|---|
| **backend facts** | Authoritative доменные данные: appointments, каталог, consent records, Twin media-артефакты | Backend — SoR (факт — MVP Scope v0.3 §9); доменный lifecycle | Да, доменно |
| **session context** | Содержимое текущего диалога в пределах session | Conversation-уровень; живёт внутри session (факт — CSR §10.1) | Нет (сессия) |
| **Conversation Flow State** | Состояние активного flow (active-flow slots) текущего пути | Conversation-уровень; ≠ Persistent Memory (факт — AYLA-DEC-0023) | Нет (сессия) |
| **persistent semantic memory** | MemoryEntry: типизированное `value`, `provenance`, `consent_scope`, `purpose_tags`, `effective_from`, `superseded_by`, `expires_at` (факт — AYLA-DEC-0024) | User Context Domain / backend; создаётся только через pipeline proposal → confirmation → whitelist check → persist (факт — AYLA-DEC-0023) | Да, opt-in Phase 2 |
| **consent record** | Authorization metadata о согласии пользователя; **не Context Fact** и не значение MemoryEntry (факт — AYLA-DEC-0023/0024) | Consent Management / [[Consent Scope Registry]] | Да (Consent Management) |
| **purpose-limited projection** | Проекция persistent memory, доступная для конкретной цели: retrieval допустим только в пределах declared `purpose_tags` (факт — AYLA-DEC-0024 п. 1) | Memory-владелец; runtime | Runtime |
| **rendered memory block** | Рендер разрешённых фактов, передаваемый в prompt: только данные, разрешённые активным scope и необходимые для конкретного запроса (факт — CSR §2 п. 8) | Runtime; не хранится | Нет |
| **Living Digital Twin** | Центральное пользовательское представление контекста, состояния и прогресса; reconstructed representation / интерфейс восприятия, не memory store (owner decision OD-4; факт — Manifesto §3, §9) | Twin-артефакты — backend facts с media consent; обновление при достаточных основаниях (факт — Manifesto §3) | Артефакты — как backend facts |

### Фазы памяти (target state и rollout)

Full/Target Journey — архитектура долгосрочного персонализированного опыта;
MVP rollout — ограничения доступности по фазам (owner decision OD-6; факт —
CSR §10; AYLA-DEC-0018, Option C):

```text
Phase 1:
session context + active-flow slots + authoritative backend facts
persistent memory disabled; отсутствие автоматического persistent write
(факт — CSR §10.1)

Phase 2:
opt-in persistent memory после Consent Scope Registry gate:
consent, purpose limitation, provenance, correction, revocation,
deletion, retention/expiry, supersession
(факт — CSR §10.2; AYLA-DEC-0023/0024)
```

### Learning levels

Learning разделяется на независимые уровни (owner decision OD-12);
формулировка «Ayla учится» без указания конкретного уровня не
используется:

| Уровень | Статус |
|---|---|
| Session Learning | MVP (Phase 1) |
| Outcome Learning | MVP (простой feedback, этап 14) |
| Recommendation Analytics | MVP (диагностическая телеметрия — MVP Scope v0.3 §11) |
| Personalized Learning | Phase 2 (после consent и persistent memory) |
| Persistent Memory Learning | Phase 2 |
| Adaptive Recommendation Optimization | Future Phase |
| Model Training (fine-tuning, RLHF, DPO, SFT и аналогичные механизмы) | Deferred / Out of MVP |

Цепочка обучения, отражаемая в journey (owner decision OD-12):

```text
Outcome
→ Feedback
→ Optional Memory Proposal
→ Phase 2 Consent & Eligibility
→ Persistent Memory Write
```

**Memory Proposal** допускается уже в Phase 1 и означает только предложение
сохранить знание (owner decision OD-12): не является persistent write; не
требует publication незарегистрированных `memory.*` events; не изменяет
долгосрочную память. Persistent write возможен только после: consent;
purpose validation; eligibility; Phase 2 rollout.

### Факты из источников (сохранены из approved v1.1)

- **Whitelist фактов MVP:** каноническая форма — категориальный whitelist
  AYLA-DEC-0023 (статусы категорий allowed / requires dedicated consent /
  forbidden; красная зона — default deny; расширение — только owner
  decision с проверками product_value / privacy_review / retention_policy /
  deletion_behavior). Плоский список Roadmap §3.4 = Scope Contract §4.1
  п. 8 — superseded, non-normative historical reference (Change Control
  2026-07-28). Ничего сверх whitelist в MVP не сохраняется.
- **Memory Proposal flow** (полная UJS, When Memory is Created): сообщение
  или событие создаёт только proposal; persistent memory — после
  sensitivity/purpose check и consent check. Молчание и продолжение диалога
  не являются согласием.
- **Revocation** (CSR §2 п. 6, §5.7, §7): отзыв прекращает новое
  использование, становится видимым runtime без новой сессии; сохранённые
  предпочтения помечаются `revoked` и перестают использоваться в
  `provider_selection`/`intent_understanding`.
- **Перепроверка памяти** (полная UJS, When Memory Must be Questioned /
  MVP Memory Heuristic): Ayla переспрашивает при низкой актуальности факта,
  истечении TTL, противоречии, а также когда временный, изменяемый или
  safety-critical факт используется для существенного решения; подтверждённая
  пользователем гипотеза преобразуется в confirmed context с сохранением
  provenance.
- **Consent state ≠ Context Fact** (факт — AYLA-DEC-0023/0024): согласие —
  authorization metadata в Consent Management, не факт памяти; MemoryEntry
  хранит только ссылку `consent_scope`.

### Memory Learning Loop **(proposal, v0.2 — сохранён)**

```text
Observe (сообщение, событие, outcome)
→ Propose (Memory Proposal: candidate fact + source + purpose + confidence)
→ Verify (sensitivity/purpose check + подтверждение пользователя)
→ Store (Context Fact с provenance, только при активном scope)
→ Retrieve (targeted, в пределах scope и релевантности)
→ Apply (recommendation, clarification suppression, execution context)
→ Measure outcome (feedback, acceptance, correction)
→ Correct (confirm / supersede / expire / delete)
```

Поля Memory Proposal **(proposal)**: `candidate_fact`, `fact_type`,
`source`, `proposal_confidence`, `sensitivity`, `purpose`,
`confirmation_requirement`, `conflict_with_existing`, `persistence_result`,
`review_after` / `expires_at`, `audit_events`.

> Поле `proposal_confidence` (v0.3, по AYLA-DEC-0024 п. 1): допустимо у
> MemoryProposal и в audit metadata, но **не переходит в canonical
> MemoryEntry** — там `confidence` запрещён и не влияет на использование
> факта. После подтверждения создаётся MemoryEntry без confidence. Состав
> MemoryEntry и статусы MemoryProposal (`pending_confirmation | accepted |
> rejected | expired`) определяются AYLA-DEC-0024.

Кандидатные lifecycle-события цикла **(proposal — все имена CANDIDATE,
`registration proposed` per-event по Domain Event Registry v0.4 §6.4 —
owner decision OD-15; конвенция и producer правила — AYLA-DEC-0025)**:
`memory.proposal_created`, `memory.proposal_confirmed`,
`memory.proposal_rejected`, `memory.entry_created`,
`memory.entry_superseded` (resolved mapping для `ContextFactCorrected` —
AYLA-DEC-0024 п. 4), `memory.entry_expired`, `memory.entry_revoked`.
`memory.proposal_expired` — candidate (TTL proposal — AYLA-DEC-0024
п. 2; не `registration proposed`). `memory.entry_deleted` — NOT_DEFINED
(не регистрируется; tombstone — Deletion Pipeline, OQ-E4). `ContextFactUsed` — classification unresolved
(v0.2.1): вероятнее audit-событие `memory_fact_used` (факт — CSR §9.1) или
recommendation evidence record, а не lifecycle domain event; как domain
event — NOT_DEFINED.

Не каждый feedback становится памятью **(proposal)**: оценка специалиста,
оценка услуги, достижение цели, временная реакция и safety signal —
разные interpretation candidates; Ayla не выбирает значение автоматически,
а предлагает сохранить конкретный факт («Запомнить, что предпочитаете более
мягкую интенсивность?»).

### Memory taxonomy **(proposal, v0.2 — сохранена)**

Вместо плоского списка — типизированные классы фактов, каждый со своими
purpose, sensitivity, source, confidence, сроком актуальности, способом
подтверждения и допустимым влиянием на решение:

| Тип факта | Пример | Влияние на решение |
|---|---|---|
| Preference Fact | предпочтение времени, стиля общения | preference weighting |
| Constraint Fact | явно подтверждённый отказ от интенсивных процедур | constraint / exclusion, не boost |
| Historical Action Fact | предыдущая подтверждённая услуга, мастер | candidate generation, disambiguation |
| Outcome Fact | прошлая услуга не дала ожидаемого результата | смена стратегии рекомендации |
| Communication Preference | краткие или подробные объяснения | explanation style |
| Temporary Context | событие через две недели, период восстановления | time-bounded relevance + expiry |
| User-confirmed Correction | исправление ранее сохранённого факта | supersede с приоритетом над старым фактом |

**Temporary Context — session-only класс (owner ruling 2026-07-28):**
существует только в активной сессии; не сохраняется в долговременную
память по умолчанию; не извлекается в будущих сессиях; не становится
User Fact автоматически; перевод в persistent memory — только через
Memory Proposal по AYLA-DEC-0024 (pipeline: proposal → confirmation →
whitelist check → persist); внутри сессии используется в пределах
`purpose_tags` (AYLA-DEC-0024 п. 1).

> **Normative guard (v0.2.1).** Данная taxonomy **не расширяет** approved
> persistent-memory whitelist (факт — Roadmap §3.4 = Scope Contract §4.1).
> Класс факта может использоваться для session context, runtime
> classification или proposal generation, но persistent сохранение
> разрешено только для типов, явно включённых в действующий whitelist,
> допустимый purpose и активный consent scope. Расширение whitelist —
> только owner decision с четырьмя проверками (факт — AYLA-DEC-0023 п. 5).

Outcome Fact несёт источник и статус подтверждения **(proposal, v0.2.1)**:
`reported` (сообщён пользователем), `confirmed` (подтверждён допустимым
authoritative source), `inferred` (вычислен системой — не может
автоматически становиться persistent Context Fact), `disputed` (оспорен
пользователем), `superseded` (заменён более актуальным фактом).

Кто может создавать факты **(proposal)**: пользователь (explicit) и Ayla
(proposal на подтверждение). Provider-authored данные могут быть
authoritative operational facts в пределах owning domain, но не становятся
фактами о предпочтениях, намерениях или субъективном результате
пользователя без подтверждения самого пользователя (v0.2.1).

### Context Sufficiency Model

Общий принцип достаточности контекста — **факт**, унаследован из полной
UJS (Context Sufficiency Gate): sufficiency определяется обязательным
набором данных для конкретных Intent Type, Action Class и Risk Level, а не
количеством заполненных слотов.

Формальная структура сводки — **proposal (v0.2)**, не утверждённая часть
полной UJS (v0.2.1):

```yaml
context_summary:
  applicable_facts: []
  uncertain_facts: []
  conflicting_facts: []
  stale_facts: []
  missing_required_context: []
  authorization_scope:
  sufficiency: sufficient | partial | insufficient
```

Правила **(proposal)**: память не заменяет уточнение, если релевантный факт
устарел, конфликтует, недостаточно подтверждён или неоднозначно применим к
текущей ситуации; конфликтующие факты не применяются одновременно —
запрашивается пользовательское разрешение конфликта (согласуется с фактом —
полная UJS, When Memory Must be Questioned).

### Freshness, expiry и supersession **(proposal — сохранено)**

Каждый факт несёт временную модель: `observed_at`, `confirmed_at`,
`effective_from`, `expires_at`, `review_after`, `supersedes_fact_id`.
Временные и изменяемые факты перед существенным использованием требуют
повторного подтверждения (факт — полная UJS, MVP Memory Heuristic п. 2;
числовые TTL — design candidates до ADR-0012, факт — полная UJS, What Ayla
Remembers). Пользовательские сценарии актуализации: «Это всё ещё
актуально?», «Оставить это предпочтение?», «Использовать только сегодня»,
«Забыть это» (последнее — факт, CSR §8).

### Anti-lock-in и novelty guard **(proposal — сохранено)**

- История пользователя — не безусловный приказ повторить прошлый выбор:
  высокая повторяемость прошлого решения может означать filter bubble, а не
  качество.
- Preference boost не обходит safety, eligibility и economic-neutrality
  (факт в части gates — Killer PRD §5.1/§5.3).
- Негативный outcome снижает повторение прошлого решения, но не создаёт
  автоматически sensitive inference (согласуется с фактом — CSR §5.7
  Prohibited; полная UJS, Learning Signals).
- Система сохраняет разумную возможность исследования alternatives; Ayla
  может спросить: «Повторить знакомый вариант или посмотреть что-то
  новое?» — вместо скрытого решения за пользователя.

### User memory controls (ControlAction)

Факты (CSR §8): просмотр активных согласий по scope; отзыв scope одной
командой; отключение всей persistent personalization; «Что Ayla знает обо
мне»; удаление выбранного memory fact; «Забыть это»; подтверждение
пользователю, что именно изменилось после отзыва.

Эти команды — ControlAction (owner decision OD-8): управляющие действия
пользователя над memory, consent, personalization и conversation
ownership; не ProductIntent и не расширение Product Intent Registry.
Термин не подразумевает существования отдельного registry, capability,
runtime contract или implementation — это отдельный downstream workstream
(owner decision OD-17). Routing-правило **(proposal — Intent Model v1.0
§ Does not own, candidate)**: выделенные UI-элементы обращаются к
владеющим областям напрямую, минуя intent resolution; разговорные
формулировки тех же команд распознаются orchestration как
management-запрос и маршрутизируются к владеющей области без расширения
замороженного реестра из 11 продуктовых intent types + sentinel `UNKNOWN`
и без изменения Output Contract 0.5.

Дополнения **(proposal)**: «Почему это сохранено» и «Где это использовалось»
(provenance disclosure); ограничение использования факта — через модель
`purpose_tags` (AYLA-DEC-0024: retrieval допустим только в пределах
declared purpose; отдельный fact-level opt-out «не использовать для
рекомендаций» не канонизируется); «Не спрашивать снова»; «Сохранить только
на эту сессию»; explanation CTA из карточки рекомендации к управлению
памятью (чат-команда или экран — по channel capability, Cross-channel
Experience).

> Ограничение контроля «Не спрашивать снова» (v0.2.1): применяется только к
> необязательным повторным вопросам и Memory Proposal prompts. Не отключает
> обязательные safety checks, authorization checks, consent revalidation,
> freshness verification и legal/policy-required confirmations.

### Product Thesis Validation Scenario **(proposal — сохранён)**

Сценарий проверки memory-first тезиса на пилоте (переименован в v0.2.1;
ранее «Memory proof scenario»). Статус определён решением AYLA-DEC-0018
(accepted, Option C): Phase 1 session-only остаётся самостоятельным
техническим release gate (факт — CSR §10), а Product Thesis Validation
закрывается только после Phase 2 и успешного прохождения этого сценария.

**Первый визит.** Пользователь сообщает цель, удобное время и важное
ограничение. Ayla использует их в текущей сессии, предлагает сохранить
допустимые предпочтения, получает согласие, сохраняет подтверждённые факты.

**Повторный визит.** Пользователь: «Хочу снова записаться на этой неделе».
Ayla извлекает релевантные актуальные факты, не повторяет известные
вопросы, уточняет только изменяемое, учитывает прошлый outcome, предлагает
решение, объясняет использование памяти и даёт возможность его исправить.

**Acceptance criterion:** повторный journey короче, точнее и персональнее
первого; при этом Ayla использует минимум один релевантный подтверждённый
факт, показывает его влияние на решение, позволяет исправить или отключить
его и не использует нерелевантные или отозванные данные.

## Recommendation and Proactivity Gates

MVP-срез; полные правила — полная UJS §6 и [[Killer PRD]] §5. Раздел
сохранён из approved v1.1 с одним EXTEND-уточнением (owner decision
OD-10).

Факты:

- **User-Initiated Recommendation Gate** (полная UJS §6): ответ на явный
  запрос проверяет safety, eligibility, Context Sufficiency, competence
  boundary и explicit current refusal. **В MVP существуют только
  user-initiated рекомендации** (owner decision OD-10).
- **Proactive Readiness Gate — неактивен в MVP:** Phase 1 работает в режиме
  no proactive recommendations (CSR §10); scope `proactive_recommendation`
  не входит в обязательные Phase 1/2 и может оставаться `blocked` (факт —
  CSR §5.7 примечание). **Persistent memory сама по себе не открывает
  proactive behavior: Phase 2 gate открывает только `preference_memory`;
  любые proactive recommendations требуют отдельного Product/Privacy owner
  decision (owner decision OD-10; факт — CSR §5.3/§5.4: `MVP status:
  blocked`, требуется отдельное Privacy/Legal approval CSR-OD-3).**
  Этап 13 допускает только транзакционные уведомления по записи.
- **Обязательный порядок gates** для любой рекомендации (Killer PRD §5.1):
  consent/privacy → safety → eligibility/availability → relevance →
  preference boost → economic-neutrality → primary output.
- **Recommendation никогда не выполняет side effect автоматически;** любое
  действие с внешним эффектом требует явного подтверждения пользователя
  (owner decision OD-10; факт — Конституция; MVP Scope v0.3 §6.5).
- **Economic neutrality** (Killer PRD §5.3; Конституция): комиссия, booking
  fee и коммерческий статус провайдера не влияют на organic ranking;
  нарушение блокирует выдачу и переводит ranking release в `quarantined`.
- **LLM не ranking authority** (owner decision OD-9): admissible set,
  ranking constraints, eligibility и authoritative ordering определяются
  каноническими правилами, registries и authoritative backend data; LLM
  понимает запрос, участвует в clarification и формирует explanation.

**Memory influence model (proposal, v0.2 — сохранена):** влияние памяти не
сводится к одному preference boost на этапе ranking. Разные типы фактов
(таксономия — Memory Interaction) работают на разных этапах решения:
интерпретация intent, hard constraints и exclusions, формирование
candidate set, outcome-informed relevance, preference weighting,
novelty/diversity guard, выбор explanation и уровня уверенности, решение
«предложить действие или продолжить уточнение». Канонический pipeline
Killer PRD §5.1 этим не отменяется — порядок gates сохраняется; контракт
«как тип факта влияет на решение» определён в
[[Ayla MVP Recommendation Contract]] v0.3 (§6, §7): consent/safety задают
admissible set для всей обработки; внутри него действует приоритет
источников (current explicit request → session context → confirmed
persistent memory → historical inferred signals — последние не участвуют в
ranking как факт до Memory Learning Loop); memory используется через
immutable `memory_snapshot_ref` (`memory_version`, `value_digest`); заднее
число переписывания recommendation запрещено (OQ №11 approved v1.1 —
закрыт).

## Cross-channel Experience

Применение AYLA-DEC-0027 и owner decisions OD-5/OD-13 на уровне journey.

**Required MVP channel set (факт — AYLA-DEC-0027; MVP Scope v0.3 §8):**

| Channel | Роль в journey |
|---|---|
| **Mobile App** | REQUIRED / primary product experience: полная визуальная и longitudinal experience — photo capture, прогресс, история, контроль данных; Living Digital Twin — conditional representation capability, доступный, если включён в релиз отдельным owner decision (AYLA-DEC-0063 / OD-MVP-1) |
| **MAX Mini App** | REQUIRED / lightweight embedded companion: статус цели, рекомендация, booking, быстрый check-in, продолжение пути |
| **MAX Bot** | REQUIRED / conversational, notification and routing companion: диалог, уточнения, объяснения, напоминания, транзакционные уведомления, быстрые действия, маршрутизация |

Правила единой Journey (owner decision OD-5; факт — AYLA-DEC-0027):

- **одна Journey с тремя UI-поверхностями**, а не три отдельных продукта;
  единые identity, consent, safety, recommendation state, memory boundary,
  attribution и analytics; channel-specific business logic запрещена;
- **feature parity across channels — NOT_REQUIRED** (факт — AYLA-DEC-0027);
  полная функциональная симметрия трёх каналов — не часть MVP, относится к
  phased rollout / target state (owner decision OD-14);
- intents могут инициироваться в поддерживаемых каналах, но **доступность
  конкретных действий определяется channel capability matrix, UX contract
  и rollout phase** (owner decision OD-5); capability обязана быть доступна
  в назначенном owning channel; отсутствие второстепенной функции в Mini
  App или Bot не блокирует путь;
- диалоговые и транзакционные действия (диалог, уточнения, объяснения,
  check-in, транзакционные уведомления, быстрые действия) доступны во всех
  каналах; визуально-зависимые experience (Twin baseline/recognition/
  comparison, photo capture, прогресс/история, контроль данных) —
  owning channel Mobile App;
- **Telegram** — вне пилотного scope (AYLA-DEC-0004; MVP Scope v0.3 §8).

Cross-channel continuity (owner decision OD-13) допускается только при
выполнении **всех** условий:

- подтверждённая identity;
- account linking (выполняется один раз и прозрачно; конфликт — только
  явное разрешение, см. N5.3);
- допустимый purpose;
- consent;
- channel capability;
- отсутствие privacy restrictions.

**Conversation ownership не переносится автоматически между каналами**
(owner decision, план v1.2 п. 6): переносится только подтверждённое
пользовательское состояние, а не техническое состояние UI, экранов,
виджетов или локальной навигации. Session является channel-scoped:
переход в другой канал начинает новую Session, а не продолжает прежнюю;
session-only контекст переносится между каналами только как разрешённая
context projection внутри подтверждённой identity boundary и при
выполнении условий continuity выше (owner decision OD-13).

Recommendation state сохраняется между каналами: рекомендация, полученная
в одном канале, доступна и объяснима в другом (в пределах условий выше).
Deep links / universal links используются для channel routing, где
поддерживаются платформой (факт — MVP Scope v0.3 §9).

Screen-level navigation, формулировки cross-channel handoff и channel
capability matrix этим документом не определяются — они принадлежат
execution/UX-документам (см. Non-goals; Open Question №1).

## Business Alignment

- Путь «цель → понимание → объяснимая рекомендация → следующий шаг →
  прогресс» реализует составную ценность MVP (факт — MVP Scope v0.3 §3);
  booking — secondary downstream evidence, не центральная метрика MVP
  (факт — MVP Scope v0.3 §11).
- Этапы 7–12 реализуют конверсионную цепочку «осмысленный запрос →
  полезная рекомендация → подтверждённое действие» (факт — Roadmap §9.2 =
  Scope Contract §9), при этом завершение без downstream action —
  полноценный успешный исход (owner decision, план v1.2 п. 5).
- Этап 12 связывает запись с `recommendation_id`, обеспечивая минимальный
  direct linkage атрибуции (факт — Scope Contract §4.1 п. 11; Killer PRD
  §6); attribution осуществляется через `recommendation_id` (owner
  decision OD-9).
- Экономическая нейтральность рекомендации (этап 7) защищает доверие как
  актив пилота (факт — Killer PRD §5.3; полная UJS, Monetization
  Neutrality).
- Проверяемый тезис MVP: накопленное и объяснимое понимание пользователя, а
  не сама функция записи, создаёт преимущество (факт — Scope Contract §1,
  AYLA-DEC-0002). Этапы 4–8 и сквозные концепции (Goal, Twin, Progress) —
  носители этого тезиса в journey.
- **(proposal, v0.2)** Product Thesis Validation Scenario (Memory
  Interaction) — продуктовый критерий проверки тезиса AYLA-DEC-0002 на
  уровне journey; статус — AYLA-DEC-0018 (Option C): не release gate
  Phase 1.

## Metrics

Journey фиксирует, **что** измеряется, но не определяет, **как** именно
измеряется (owner decision, план v1.2 п. 7). Этот документ не содержит
KPI, thresholds, численные показатели и алгоритмы расчёта — они
определяются отдельным Measurement Framework (статус порогов — факт,
AYLA-DEC-0033: процентные цели — working validation thresholds, final
go/no-go — после B0 evidence и Measurement Framework).

Метрики этапов привязаны к минимальному набору метрик пилота (факт —
Roadmap §9.2 = Scope Contract §9) — состав сохранён из approved v1.1:

| Метрика пилота (факт — Roadmap §9.2) | Этапы данного документа |
|---|---|
| доля resolved intents | 4–5 |
| clarification rate | 5 |
| recommendation shown rate | 7–8 |
| recommendation acceptance rate | 9 |
| booking conversion | 9–12 |
| booking completion | 11–13 |
| attributed qualified actions | 12 |
| recommendation rejection reasons | 9, N2.5 |
| unsafe block rate | N4.5 |
| tool failure rate | N3.4 |
| median response time | все |
| пользовательская оценка полезности | 14 |

Journey-level evidence points (owner decision OD-11/OD-14; имена событий —
NOT_DEFINED до Measurement Framework, owner decision OD-15):

| Evidence point | Этапы / сценарии |
|---|---|
| goal established/updated | сквозная концепция Goal (этапы 2, 4, 9) |
| baseline created | Twin experience points (owning channel Mobile) |
| recognition accepted/corrected | Twin experience points (recognition «это я»; сигнал «это не похоже на меня»; correction/rebuild) |
| recommendation explained | 8 |
| action accepted/rejected | 9 |
| booking selected/not selected | 10–12 |
| cross-channel continuation | Cross-channel Experience; N5.1 |
| check-in/result | 14 |
| progress viewed | Progress / next state |
| user control exercised | 3, 9, Consent/Memory controls |
| deletion/consent change | 3, N4.2, N4.4 |
| safety block | N4.5 |
| recovery completed | Negative Scenarios (все классы) |

Целевые ориентиры полной UJS (Journey Quality Metrics — First Contact
Completion Rate, Discovery Completion Rate, Intent Recognition Accuracy,
Booking Success Rate, Feedback Response Rate и др.) остаются справочными для
пилота и не переопределяются этим документом. Диагностическая телеметрия
релиза (resolved intents, clarification rate, recommendation
shown/acceptance, rejection reasons, unsafe block rate, tool failure rate,
median response time) сохраняется как техническая телеметрия (факт — MVP
Scope v0.3 §11).

**Memory-quality метрики (proposal, v0.2 — сохранены):** без них команда
может оптимизировать booking conversion и считать продукт успешным, даже
если память не влияет на решения. Кандидаты (measurement method и baseline —
pending Measurement Framework, v0.2.1):

| Группа | Метрика-кандидат | Что измеряет |
|---|---|---|
| Retrieval quality | context retrieval precision / recall | доля извлечённых фактов, релевантных запросу; доля найденных релевантных фактов |
| Retrieval quality | stale fact rate | доля использованных фактов, потерявших актуальность |
| Retrieval quality | contradictory fact rate | доля решений с конфликтующими фактами |
| Пользовательская полезность | repeated-question rate | как часто Ayla спрашивает уже известное |
| Пользовательская полезность | context correction rate | как часто пользователь исправляет применённую память |
| Пользовательская полезность | recommendation acceptance uplift | прирост принятия при корректном использовании контекста |
| Пользовательская полезность | repeat-journey value uplift | насколько второй journey полезнее первого |
| Безопасность | unauthorized context use rate = 0 | использование контекста вне scope |
| Безопасность | unexplained memory use rate | использование памяти без объяснения |
| Безопасность | sensitive inference persistence rate = 0 | сохранение inferred sensitive signals |
| Безопасность | cross-tenant memory contamination rate = 0 | утечка контекста между tenant |
| Безопасность | revoked fact use rate = 0 | использование отозванных данных |
| Анти-lock-in | incumbent repetition rate / novelty exposure rate | подавление новых вариантов историей |

Фиксированные нулевые значения safety-метрик — не настраиваемые
бизнес-пороги, а мониторинг действующих hard invariants (fail-closed,
revocation, запрет sensitive inference — факты CSR §2/§5.7).

## Constitutional Traceability

Матрица MVP-среза; полная матрица — [[Ayla User Journey Specification]] §14.

| Принцип Конституции | Этапы / разделы | Реализация в MVP-срезе |
|---|---|---|
| Ст. I (предметная область) | 1–2 | Journey начинается с потребности человека и его цели, не с каталога |
| Ст. VI (доверие расходуется вопросами) | 5 | Не более 5 вопросов Discovery (полная UJS, Maximum Questions); clarification suppression (proposal) |
| Ст. VII (объяснимость) | 8 | Объяснение рекомендации обязательно (Scope Contract §4.1 п. 9); unexplained memory use недопустимо (proposal) |
| Ст. X (уместность прежде действия) | 3, 9, 13, N4.5 | Явное подтверждение перед записью; отказ без прерывания диалога; никакой проактивности в Phase 1; Boundary Handling |
| Пользователь контролирует персональный контекст | 3, 6, 14, Memory Interaction | Fail-closed consent; whitelist фактов; revocation; ControlAction (owner decision OD-8); user memory controls (proposal) |
| AI не является источником истины | 4, 7, 11–12 | Backend — SoR; подтверждение только фактически достигнутого состояния; LLM не ranking authority (owner decision OD-9); inference не становится фактом без подтверждения (полная UJS, Memory Proposal) |
| Recommendation отделяется от action | 7, 9, 11 | Рекомендация не создаёт запись без явного подтверждения; acceptance ≠ booking (owner decision OD-9) |
| Экономическая нейтральность | 7 | Economic-neutrality check до показа primary (Killer PRD §5.3) |
| Критические решения прослеживаемы | все | Audit events CSR §9.1; `recommendation_id` сквозная связь; provenance фактов памяти (proposal) |

## Relationship to A0–B1 Execution

Journey document не описывает execution plans. Компактная привязка (факт —
execution scopes; сохранена из draft v1.1 как выборочное улучшение — см.
Canon Lineage):

| Фаза | Назначение | Journey relevance |
|---|---|---|
| A0 — Internal Technical Spine | technical spine | путь проходится внутренне end-to-end |
| A1 — Controlled Salon Alpha | controlled real-user journey | первый реальный пользовательский путь |
| A2 — Full Single-Provider Pilot | full 28-day single-provider cycle | полный цикл как A2 exit evidence (факт — AYLA-DEC-0029) |
| B0 — Multi-Provider Repeatability | multi-provider repeatability | путь воспроизводится у нескольких провайдеров |
| B1 — Product Validation Beta | independent product/business validation | путь валидируется как продукт |

Детали фаз, gates и runbook-процедуры — в
[[Ayla Single-Provider Technical Pilot Execution Scope]] и
[[Ayla Multi-Provider Product Validation Execution Scope]]; provider
counts, detailed gates, rollout-подробности и operational procedures в этот
документ не переносятся (owner decision OD-14).

## Scope and Deferred

Явная классификация возможностей (owner decision OD-14). Этот раздел не
дублирует [[Ayla MVP Scope and Release Contract]] — релизный состав
определяет MVP Scope; здесь фиксируется только отражение классификации в
пользовательском пути. Детали реализации, платежные варианты и
rollout-подробности, не влияющие непосредственно на пользовательский путь,
в Journey не переносятся (owner decision OD-14).

**IN_SCOPE (MVP, Phase 1):**

- сквозной путь: Transformation Goal → понимание → объяснимая рекомендация
  → next action → progress / next state;
- три required channels (Mobile App, MAX Mini App, MAX Bot) as MVP
  journey surfaces — трёхканальная Journey является частью MVP (owner
  decision OD-14; факт — AYLA-DEC-0027); это не означает одинаковую
  доступность всех функций во всех каналах: доступность конкретного
  действия определяется channel capability matrix, UX contract и rollout
  phase (owner decision OD-5);
- Living Digital Twin — conditional / deferred-by-default representation
  capability; Twin baseline и связанные experience points обязательны
  только если LDT включён в конкретный релиз отдельным owner decision
  (факт — MVP Scope v0.4 §6.4; AYLA-DEC-0063 / OD-MVP-1);
- session context, active-flow slots, authoritative backend facts;
- простой feedback (этап 14); Memory Proposal (Phase 1, без persistent
  write — owner decision OD-12);
- транзакционные уведомления по записи;
- booking как опциональная downstream-ветка (owner decision OD-3/OD-9);
- **Simple Reschedule** — same-ID time-only в пределах того же Offering
  (owner decision OD-14; факт — AYLA-DEC-0022 п. 1, п. 9; AYLA-DEC-0036;
  `appointment.rescheduled` — `registered`, Domain Event Registry v0.4);
- Session Learning, Outcome Learning, Recommendation Analytics (owner
  decision OD-12).

**PHASED (Phase 2):**

- opt-in persistent memory (`preference_memory`): consent, purpose
  limitation, provenance, correction, revocation, deletion,
  retention/expiry, supersession (owner decision OD-6; факт — CSR §10.2);
- Personalized Learning и Persistent Memory Learning (owner decision OD-12);
- полная функциональная симметрия трёх каналов (owner decision OD-14);
- Product Thesis Validation Scenario как закрытие продуктовой гипотезы
  (AYLA-DEC-0018, Option C).

**DEFERRED:**

- полная Cancellation Journey, Replacement, Advanced Reschedule (смена
  услуги/мастера, re-offer, substitute, late-window, cross-tenant перенос,
  изменение цены/длительности), расширенные transactional flows (owner
  decision OD-14; факт — AYLA-DEC-0022, owner ruling 2026-07-28, вариант Б);

> **Deferred branches — reconciliation / traceability (сохранено из
> approved v1.1, owner ruling 2026-07-28, вариант Б; актуализировано по
> AYLA-DEC-0022 accepted и AYLA-DEC-0036).** Доменная семантика веток
> определяется AYLA-DEC-0022 (accepted, действует) —
> `99 Archive/proposals/decision-brief-appointment-reschedule-model.md`
> (матрица операций — §4, сценарии — §2): reschedule записи (S1, S2, S6,
> S7, S8), cancel записи (S1–S3, S13), late-window изменения (§10, S6),
> substitute / отказ от замещения (S12), YClients reschedule /
> sync-конфликты (S5, §12) — deferred beyond MVP primary-booking journey.
> Единственное исключение из deferral — Simple Reschedule (same-ID
> time-only, см. IN_SCOPE и этап 11). Проверка отсутствия конфликтов: в
> этапах 1–14 и негативных сценариях нет статусов, событий или операций
> deferred-веток, кроме явно разрешённого Simple Reschedule; intent types
> RESCHEDULE_APPOINTMENT / CANCEL_APPOINTMENT упоминаются как элементы
> реестра Roadmap §3.1 (этап 4) без операциональной семантики
> deferred-веток.
- Advanced Twin evolution, advanced personalization, persistent continuity
  сверх Phase 2 модели (owner decision OD-14; Manifesto §15);
- Adaptive Recommendation Optimization (owner decision OD-12 — Future
  Phase);
- Model Training (fine-tuning, RLHF, DPO, SFT и аналогичные механизмы) —
  Deferred / Out of MVP (owner decision OD-12);
- advanced Outcome Learning (CAP-007 — факт, MVP Scope v0.3 §7);
- полная proactive architecture: proactive recommendations и cross-domain
  personalization — `blocked`, отдельное Product/Privacy owner decision
  (owner decision OD-10/OD-14; факт — CSR §5.3/§5.4);
- dedicated wellness-трекеры (food/water/sleep/activity — факт, MVP Scope
  v0.3 §6.1);
- видео для Twin — CONDITIONAL, только при подтверждённой необходимости
  (факт — MVP Scope v0.3 §6.4).

**TARGET_STATE_ONLY (описываются как target state, не как доступные MVP
функции):**

- долгосрочный персонализированный опыт полной памяти (Full/Target
  Journey — owner decision OD-6);
- richer Living Timeline, advanced forecasts, deeper personalization (факт —
  Manifesto §15);
- channel-agnostic expansion beyond the three MVP channels и additional
  future channels — универсальная multi-channel спецификация (факт — MVP
  Scope v0.3 §8); не путать с трёхканальной MVP Journey, которая IN_SCOPE
  (см. выше);
- долгосрочные состояния и доменные journeys полной UJS (S7 Long-term,
  Nutrition Guidance, re-engagement).

## Non-goals

Этот документ не определяет (сохранено из approved v1.1 и draft v1.1):

- screens, visual layouts, component library, navigation spec;
- API/DTO, domain schema, ML architecture;
- Conversation Runtime, Conversation FSM, Conversation Storage Model,
  Conversation Database Schema и внутреннюю реализацию Conversation Engine
  (owner decision, план v1.2 п. 3);
- Memory Runtime целиком (owner decision OD-6);
- ControlAction contract / registry / capability / implementation —
  отдельный downstream workstream (owner decision OD-17);
- channel capability matrix и формулировки cross-channel handoff —
  execution/UX-документы (owner decision OD-5);
- provider ranking algorithm, final analytics thresholds, operations
  runbook, monetization implementation, store distribution, full
  marketplace journey.

**Stop List (owner decision, план v1.2 п. 9).** Journey запрещается
описывать:

- внутренние prompt pipelines;
- внутренний orchestration graph;
- внутренние prompt assembly mechanics;
- внутренние runtime chains.

Journey остаётся продуктовым документом.

Ложные трактовки памяти, запрещённые в MVP (факты — CSR §5.7 Prohibited,
CSR §2, полная UJS Memory Proposal; остальное — **proposal**, v0.2):

- скрытое сохранение inferred traits без подтверждения пользователя (факт);
- использование отозванного или неразрешённого контекста (факт);
- построение sensitive attributes из поведения (факт — CSR §5.7,
  `inferred_signal` prohibited);
- бессрочное использование предпочтений без проверки актуальности
  **(proposal)**;
- использование provider-authored данных как пользовательских предпочтений
  без маркировки источника и подтверждения **(proposal)**;
- автоматическое повторение прошлого выбора только на основании истории
  **(proposal)**;
- персонализация, которую Ayla не может объяснить пользователю
  **(proposal)**;
- оптимизация рекомендаций только по booking conversion (факт — полная UJS,
  Business Metrics «Правило приоритета» / «Запрещено»);
- отождествление сущностей: LDT = Memory, Session = Memory, Backend Facts =
  Memory и иные подобные упрощения (owner decision, план v1.2 п. 4).

## Open Questions

Принятые owner decisions (OD-1…OD-18, AYLA-DEC-0026…0036) не
переоткрываются. Каждый открытый вопрос классифицирован по влиянию
(owner decision — metadata discipline v1.2):

- **A.** Non-blocking editorial/contract follow-up;
- **B.** Deferred product decision;
- **C.** Implementation dependency;
- **D.** Blocking before capability rollout — не блокирует approval
  Journey, но блокирует rollout конкретной capability;
- **E.** Blocking before Journey approval.

Вопросы категории E в этом списке отсутствуют.

1. **(A — non-blocking editorial/contract follow-up). Exact wording of
   cross-channel handoff** — формулировки перехода
   между каналами (Bot → Mobile, Mini App → Mobile) и channel capability
   matrix определяются execution/UX-документами (owner decision OD-5).
2. **(D — blocking before capability rollout: human handoff). Human
   handoff.** Порог перехода к оператору/человеку (N6.1) и сама
   процедура не определены в источниках; требуется решение в Pilot
   Operations Runbook (Roadmap §9.3, P1). Approval Journey не блокирует;
   rollout human handoff как capability блокирует — сохранён из approved
   v1.1.
3. **(B — deferred product decision). Поведение этапа 12 при отклонении
   записи провайдером.** Предложение
   «альтернативный слот/мастер» помечено (proposal); требуется подтверждение
   продуктового решения — сохранён из approved v1.1.
4. **(A — non-blocking contract follow-up: Explanation Contract).
   Fallback этапа 8.** Правило «без объяснения рекомендация не
   показывается» — (proposal), не утверждено (owner decision OD-9);
   требует сверки с будущим Explanation Contract.
5. **(B — deferred product decision). Ветки переноса/отмены записи.**
   Simple Reschedule (same-ID time-only)
   — in scope (AYLA-DEC-0022/0036); включение остальных веток
   (cancellation journey, replacement, re-offer) в следующие версии
   MVP-среза — открыто (Scope and Deferred).
6. **(D — blocking before capability rollout: Outcome Capture). Статус
   CAP-006 в MVP.** Этап 14 отнесён к Outcome Capture, но в
   Included Capabilities Scope Contract §4.1 прямой записи нет (advanced
   outcome learning deferred); кандидат-решение из review: разделить Basic
   Feedback Capture (MVP-active) и Advanced Outcome Learning (deferred) —
   решается в Capability Registry Wave 2 (owner decision OD-16;
   AYLA-DEC-0014). Approval Journey не блокирует; rollout Outcome
   Capture capability блокирует — сохранён из approved v1.1.
7. **(ЗАКРЫТ — v1.0, 2026-07-29). Зависимость от Ayla Intent Model
   Specification.** Документ материализован и утверждён:
   [[Ayla Intent Model Specification]] v0.9.2 (status approved,
   decision_status accepted) + machine-readable contracts
   `03 AI System/Contracts/` (intent-registry.yaml и slot-registry.yaml —
   registry_version 1.0, compatible_contract_version 0.5;
   intent-output.schema.json — contract_version 0.5). Сверка этапов 4–5 с
   утверждённым Output Contract выполнена — противоречий не выявлено
   (подробности — Change Log approved v1.1). Owner decision OD-7:
   v0.9.2 остаётся runtime-каноном; границы v1.0 (Transformation Goal ≠
   intent, recommendation intent — system-owned, orchestration state ≠
   product intent, downstream action — не только LLM) приняты как
   journey-level нормативный язык; v1.0 — candidate до отдельного owner
   review.
8. **(ЧАСТИЧНО РЕШЁН — v1.1; обновлено v1.2 по OD-15).** Domain Event
   Registry — актуальная редакция v0.4, единственный источник истины по
   статусу событий (owner decision OD-15). `registered`:
   `recommendation.created`, `recommendation.superseded`,
   `recommendation.expired`, `recommendation.invalidated`,
   `recommendation.presented`, `recommendation.accepted`,
   `recommendation.declined` (§6.5), `qualified_action.attributed` (§6.6),
   `appointment.rescheduled` (§6.3). `registration proposed`: `consent.*`,
   `intent.*`, остальные `appointment.*`, `memory.*` (per-event: 7 записей
   §6.4; `memory.proposal_expired` — candidate; `memory.entry_deleted` —
   NOT_DEFINED, OQ-E4). Открытыми остаются: финальные
   payload и owner для этапа 14 (**C — implementation dependency:**
   OQ-E3, до Appointment Contract;
   `appointment.completed` — `semantic_status: incomplete`); deletion
   events (**D — blocking before capability rollout: memory deletion,**
   OQ-E4). **Registry gap (A — non-blocking contract follow-up:
   Measurement Framework):** канонический analytics event для
   `booking_confirmation_shown` (этап 12) в реестре отсутствует —
   NOT_DEFINED до Measurement Framework.
9. **(ЗАКРЫТ для draft metadata — v1.2, 2026-08-05; остаток: A —
   non-blocking schema backlog). Canon Lineage metadata.** Поле
   `derived_from` отсутствует в relationship semantics
   [[Ayla Domain and Metadata Registry]] v1.0 §7 и удалено из frontmatter
   (resolved by removal from draft metadata); `supersedes` на текущий
   узел удалён как self-reference и как преждевременный до owner
   approval. Каноническая линия зафиксирована в текстовом блоке Canon
   Lineage и Change Log. Открытый остаток — backlog: введение versioned
   lineage-поля в schema отдельным изменением
   [[Ayla Domain and Metadata Registry]] (не в этом документе).
10. **(ЗАКРЫТ — AYLA-DEC-0018, accepted 2026-07-28, Option C). Статус
    Phase 2 как product-validation gate.** Phase 1 (session-only) —
    самостоятельный технический release gate; Product Thesis Validation
    открыта до Phase 2 и успешного Product Thesis Validation Scenario.
11. **(ЗАКРЫТ — AYLA-DEC-0023, accepted 2026-07-28). Достаточность memory
    whitelist.** Категориальная форма; расширение — только owner decision.
12. **(ЗАКРЫТ — AYLA-DEC-0023/0024, accepted 2026-07-28). «Согласие на
    персонализацию» в whitelist.** Consent state — authorization metadata,
    не Context Fact и не значение MemoryEntry.
13. **(ЗАКРЫТ — v1.1, [[Ayla MVP Recommendation Contract]] v0.3). Роль
    памяти в recommendation pipeline.** Нормативная модель влияния memory
    определена Recommendation Contract v0.3 (§6, §7); канонический порядок
    gates Killer PRD §5.1 подтверждён без изменений.
14. **(A — non-blocking backlog; cross-document, deferred). Naming-дрейф
    полной UJS и
    термин «substitute» (2026-07-28).** Полная
    [[Ayla User Journey Specification]] v1.2 использует `booking.created` /
    `booking.confirmed` — расхождение с каноном AYLA-DEC-0025
    (`appointment.*`). Отдельный backlog-пункт: аменда полной UJS к канону
    имён или сознательный deferral (owner decision OD-18 — naming
    alignment). Терминологическое пересечение: «substitute offer» в полной
    UJS (Proactive Readiness Gate) ≠ substitute-исполнитель (S12
    decision-brief-appointment-reschedule-model); в этом документе
    «substitute» используется только во втором значении (deferral-ветка).

## Change Log

Historical Change Log не переписывается (Canon Preservation Rules).
Записи v0.1…v1.1 сохранены как точная история.

### v1.2 (2026-08-04) — Эволюция approved v1.1 по итогам Owner Decision Session (OD-1…OD-18)

- **Фундамент сохранён (approved v1.1 — основание редакции, см. Canon
  Lineage):** структура 14 этапов approved
  v1.1, негативные сценарии (содержание N1–N9), Memory Interaction
  (proposal-слой), Recommendation and Proactivity Gates, Metrics —
  сохранены; принцип EXTEND, не REWRITE.
- **OD-1 (Journey Philosophy):** lifecycle approved v1.1 сохранён и
  расширен целевым якорем Transformation Goal и Living Digital Twin как
  непрерывным представлением; booking — опциональное downstream-действие;
  терминал — progress / next state.
- **OD-2 (Conversation Lifecycle):** добавлен подраздел в Journey
  Operating Model — 10 элементов продуктового lifecycle разговора; не
  Conversation Runtime/FSM/Storage/Schema (owner decision, план v1.2 п. 3).
- **OD-3 (Journey Stages):** все 14 этапов KEEP/EXTEND; Goal, LDT и
  Progress оформлены как сквозные концепции, а не обязательные линейные
  стадии (owner decision, план v1.2 п. 2); booking-этапы 10–12 —
  опциональная ветка.
- **OD-4 (LDT):** роль Twin зафиксирована в редакции владельца: центральное
  пользовательское представление контекста и прогресса, не SoT, не
  единственный центр; Twin baseline/media — backend domain data, не
  persistent semantic memory.
- **OD-5 (Три канала):** раздел Cross-channel Experience приведён к
  AYLA-DEC-0027; доступность действий — по channel capability matrix, UX
  contract и rollout phase.
- **OD-6 (Memory Target State):** модель «target state + phase rollout»;
  восьмичленное разграничение сущностей — независимы, с собственными
  владельцами и lifecycle (owner decision, план v1.2 п. 4).
- **OD-7 (Intent Boundary):** границы Intent Model v1.0 приняты как
  journey-level язык; runtime-канон — v0.9.2 / Output Contract 0.5.
- **OD-8 (ControlAction):** управляющие команды пользователя оформлены как
  ControlAction — owner-approved product concept, не ProductIntent, без
  подразумеваемого registry/contract/capability (owner decision OD-17).
- **OD-9 (Recommendation Model):** approved lifecycle сохранён; goal-
  anchor, `no_action`, LLM не ranking authority, acceptance ≠ booking,
  attribution через `recommendation_id`.
- **OD-10 (Gates):** EXTEND-уточнение — proactive остаётся blocked и после
  Phase 2 (отдельное Product/Privacy owner decision).
- **OD-11 (Negative Scenarios):** реорганизация в 6 классов; добавлены
  сценарии invalid structured output, unresolved goal, stale state/version
  conflict, authoritative confirmation delay, memory unavailable, consent
  revoked, deletion request, abandon/resume, interrupted channel, account
  linking conflict, human handoff, manual intervention, no_action; runtime
  mechanics вынесены за пределы документа.
- **OD-12 (Learning Loop):** уровни learning зафиксированы; Memory
  Proposal допускается в Phase 1 без persistent write и без публикации
  `memory.*`; цепочка Outcome → Feedback → Optional Memory Proposal →
  Phase 2 Consent & Eligibility → Persistent Memory Write.
- **OD-13 (Follow-up and Continuity):** follow-up — транзакционное
  сообщение или согласованный check-in; условия cross-channel continuity;
  conversation ownership не переносится автоматически (owner decision,
  план v1.2 п. 6).
- **OD-14 (Scope and Deferred):** добавлен раздел с классификацией
  IN_SCOPE / PHASED / DEFERRED / TARGET_STATE_ONLY; Journey не дублирует
  Release Contract.
- **OD-15 (Event Consistency):** все события приведены к Domain Event
  Registry v0.4 с точным registration status (`registered` / `registration
  proposed` / NOT_DEFINED / LEGACY_ALIAS); терминология canonical event
  name / registration status / registry status разведена; ссылки на
  реестр обновлены до v0.4.
- **OD-16 (Capability Consistency):** поле «owning capability» заменено на
  «capability reference»; Journey описывает только product availability;
  формулировка «Capability mapping will be assigned during Capability
  Registry Wave 2».
- **OD-17 (Metadata and Domain Consistency):** добавлены раздел
  Terminology (appointment, booking
  как legacy alias, Transformation Goal, Living Digital Twin, Conversation,
  Session, Interaction, Dialogue Turn, ControlAction); обязательные
  разделы типа сохранены. Canon Lineage зафиксирована в текстовом блоке
  (см. правку 2026-08-05 ниже).
- **OD-18 (Downstream Updates):** downstream scope зафиксирован в
  Canonical Position; Journey — продуктовый фундамент, не центр
  синхронизации.
- **Draft v1.1 как источник выборочных улучшений (см. Canon Lineage):**
  перенесены —
  Canonical Position, Actors-таблица с тремя каналами, Relationship to
  A0–B1 Execution, evidence points, trigger model (AYLA-DEC-0028),
  сценарии N1/N2/N3/N4/N6/N10/N11/N14/N15/N16 (в адаптированном виде в
  классах 1–6). Не перенесены — перегруппировка этапов в 7 блоков,
  12-шаговая структура, booking-optional замена структуры (заменено
  опциональной веткой).
- **Frontmatter:** version 1.1 → 1.2; depends_on дополнен
  Foundation-документами; статус: draft / proposed /
  candidate — pending review и owner approval.

**Targeted governance and consistency fixes (2026-08-05, pre-review
pass; архитектура и принятые решения не менялись):**

- **FIX-1 (Canon Lineage):** из frontmatter удалены `supersedes`
  (self-reference на текущий узел; преждевременный до owner approval) и
  `derived_from` (отсутствует в relationship semantics
  [[Ayla Domain and Metadata Registry]] v1.0 §7 и в `.knowledge/schema.yaml`).
  Каноническая линия сохранена в текстовом блоке Canon Lineage и в этой
  записи Change Log: v1.2 — новая candidate-редакция, основанная на
  approved v1.1, выборочных улучшениях draft-линии и owner rulings
  OD-1…OD-18; до owner approval v1.2 не supersede approved v1.1.
- **FIX-2 (Owner rulings status):** в статусный блок добавлено «Owner
  directions OD-1…OD-18 applied to draft. Formal registration and
  canonical approval remain pending.»; удалены ссылки на внутрисессионные
  идентификаторы AD-001…AD-012 (не существуют как артефакты репозитория)
  — заменены ссылками на OD-8/OD-14 и Canon Lineage; фиктивные AYLA-DEC
  ID не добавлялись; регистрация решений в Owner Decision Register
  выполнена как AYLA-DEC-0037…AYLA-DEC-0054 (2026-08-05).
- **FIX-3 (Event classification):** wildcard-статусы заменены точными
  per-event перечислениями по Domain Event Registry v0.4: registered
  `recommendation.*` перечислены поимённо (7 событий §6.5); legacy aliases
  — `booking.rescheduled`, `booking.confirmed`, `booking.created` (§11,
  §6.3, §1), wildcard `booking.*` помечен как compatibility adapter;
  `memory.*` разведены на `registration proposed` (7 записей §6.4),
  candidate (`memory.proposal_expired`) и NOT_DEFINED
  (`memory.entry_deleted`); терминология дополнена понятием legacy alias.
- **FIX-4 (Session / cross-channel):** зафиксирована иерархия Dialogue
  Turn → Interaction → Session → Conversation; Session объявлена
  channel-scoped (переход между каналами начинает новую Session); между
  Sessions переносится только разрешённая context projection; фраза о
  «продолжении» session-only контекста между каналами переписана в
  N5.1 и Cross-channel Experience.
- **FIX-5 (Open Questions):** введена классификация A–E по влиянию;
  вопросы human handoff, CAP-006 и memory deletion events помечены как
  блокирующие rollout конкретных capabilities, но не approval Journey;
  OQ по `derived_from` закрыт как resolved by removal from draft
  metadata (остаток — non-blocking schema backlog).
- **FIX-6 (Three-channel scope):** разведены IN_SCOPE (три канала как
  MVP journey surfaces, без обещания функциональной симметрии) и
  TARGET_STATE_ONLY (channel-agnostic expansion beyond the three MVP
  channels и additional future channels).

**Final closure alignment (2026-08-07, WINDOW-01 Journey v1.2 / OD-MVP-1…4):**

- **AYLA-DEC-0063 / OD-MVP-1 (LDT):** Living Digital Twin переведён из
  обязательного critical-path элемента первого MVP в strategic /
  conditional representation capability. Сквозные концепции,
  Cross-channel Experience и Scope and Deferred приведены в соответствие
  с MVP Scope v0.4 §6.4: LDT обязателен только если включён в конкретный
  релиз; долгосрочная модель LDT, его strategic role и требования
  honesty / recognizability / identity continuity / correction /
  user-control (при включении) сохранены. LDT не удалён, не deprecated.
- **AYLA-DEC-0064 / OD-MVP-2 (Everyday Signal / Food Intelligence):**
  проверено, что Food Scanner остаётся first concrete MVP implementation
  of Everyday Signal, но не центральной сущностью, не единственным
  сигналом, не calorie-tracking продуктом, не медицинским inference
  source и не permanent identity of Ayla; материальных изменений не
  потребовалось (de-centered framing уже действует).
- **AYLA-DEC-0065 / OD-MVP-3 (Memory Foundation):** проверено, что
  progressive memory model (Working Context → Memory Candidate → Policy /
  Consent Gate → Persistent Memory) уже отражена в Memory Interaction;
  формулировки «Phase 1 = no memory» отсутствуют; persistent memory
  остаётся отключённой в Phase 1, но Memory Proposal допускается.
- **AYLA-DEC-0066 / OD-MVP-4 (MVP value loop):** проверено, что Journey
  совместим со сквозным циклом Goal → Signal → Context → Recommendation
  → Action → Memory → Progress; существующая структура
  Conversation → Understanding → Recommendation → Execution → Learning /
  Continuity сохранена; booking остаётся одним из возможных downstream
  Action, а не terminal product value.
- **Metadata:** `updated` обновлён на 2026-08-07; статус остаётся draft /
  proposed / candidate — pending final owner review. Упоминания pending
  alignment с AYLA-DEC-0063…0066 удалены из статусного баннера.

**Final owner approval (2026-08-08):**

- Статус переведён в `approved` / `accepted` / `canonical`.
- Предыдущая approved revision v1.1 (`approved_v1_1.md`) переведена в
  `superseded`; историческая редакция сохранена.
- Journey v1.2 — Active Canon revision узла `ayla.product.mvp-user-journey`.

### v1.1 (2026-08-03) — D1 Product/Journey consistency repair

- Stale [[Ayla Intent Model Specification]] references (§2 Canonical
  Position, §6.4 Intent Understanding) corrected: removed hard-coded
  `v0.9.2 (approved/accepted)`; now cite `v1.0, draft / proposed /
  candidate`, matching the current Intent Model status banner.
- Memory/consent controls (§6.1 Entry and Context, §10 Memory Interaction)
  clarified: dedicated UI controls route directly to CAP-001 (Personal
  Context Management) / CAP-002 (Consent Management), bypassing intent
  resolution; conversational equivalents are recognized by orchestration as
  management requests and routed to the same capabilities without
  extending the frozen 11 product intent types + `UNKNOWN` registry.
- No new intents, slots, scope, or owner decisions introduced; version,
  status and canonical_status unchanged; historical Change Log entries
  (including the `v0.9.2` references under `### v1.0 (2026-07-29)`) left
  untouched as accurate history. Status remains candidate.

### v1.1 (2026-07-31) — Structured revision for MVP Scope v0.3 downstream migration (Wave D1)

- **LDT and Transformation Goal added:** Transformation Goal — центральный
  шаг пути (§6.2); Living Digital Twin baseline, recognition, correction,
  identity continuity, comparison over time и state-class distinction —
  обязательные experience points (§6.3) по AYLA-DEC-0026, Product Essence
  v1.1, LDT Manifesto v1.0 и MVP Scope v0.3 §4/§6.4.
- **Booking moved to optional downstream action:** booking — OPTIONAL на
  уровне journey (§6.6); technical execution coverage сохраняется в A1/A2;
  booking-terminal framing снят.
- **Progress/next state terminal:** journey завершается прогрессом /
  следующим состоянием (шаг 12, §6.7), а не подтверждением записи.
- **Three-channel journey:** применён AYLA-DEC-0027 — Mobile App
  (primary), MAX Mini App и MAX Bot (companions); feature parity
  NOT_REQUIRED; единый journey, account linking, consent continuity,
  сохранение recommendation state (§4, §6.1, §7); MAX-only wording
  удалён.
- **Food Scanner de-centered:** применён AYLA-DEC-0028 — четыре
  равнозначных trigger-сценария (Vision §10) как входы; Food Scanner —
  CONDITIONAL trigger (§6.1); food-centered framing снят.
- **Memory phases aligned:** Phase 1 session-only / Phase 2 opt-in
  persistent по CSR §10 (§6.1, §10); memory loop, Consent state ≠
  Context Fact и user controls сохранены в сжатом виде; memory-first
  framing запрещён (MVP Scope v0.3 §6.3).
- **Negative/recovery scenarios expanded:** N1–N16 с обязательными полями
  trigger / system behavior / user control / safe fallback / journey
  continuation / analytics evidence (§8).
- **Stale references migrated:** ссылки на MVP Scope v0.2 (§3, §4.1, §5,
  §7, §9) переведены на актуальные разделы v0.3 (§4, §5, §6, §7, §8, §11);
  старые execution document titles заменены на актуальные execution
  scopes; booking-terminal wording заменён progress/next state terminal.
- **No UX/architecture implementation added:** документ не определяет
  screens, layouts, components, navigation, API/DTO, domain schema, ML
  architecture (§16).
- **Structure:** обязательные normative sections типа
  user-journey-specification сохранены (Purpose, Journey Operating Model,
  Journey Overview, Stage Specifications, Memory Interaction,
  Recommendation and Proactivity Gates, Cross-channel Experience,
  Business Alignment, Metrics, Constitutional Traceability, Change Log).
- **Metadata:** version 1.0 → 1.1; status draft / decision_status
  proposed / canonical_status candidate; depends_on дополнен
  [[Ayla Product Essence]], [[Ayla Product Vision]],
  [[Ayla MVP Product Thesis]], [[Ayla Product Principles]],
  [[Ayla Living Digital Twin Manifesto]]; документ остаётся candidate
  pending review и owner approval.

### v1.1 (2026-07-29) — Conforming amendment: регистрация recommendation.* / qualified_action.attributed, закрытие OQ №11

- **Миграция имён событий завершена для зарегистрированных семейств**
  ([[Ayla Domain Event Registry]] v0.3, §6.5/§6.6, `registered`;
  семантика — [[Ayla MVP Recommendation Contract]] v0.3, architecture
  review APPROVED): этап 7 — `recommendation.created` +
  `recommendation.presented` (legacy `RecommendationShown`); этап 9 —
  `recommendation.accepted` / `recommendation.declined` (legacy
  `RecommendationAccepted`); этап 12 — `qualified_action.attributed`
  (legacy `QualifiedActionAttributed`). Ссылки на реестр обновлены до
  v0.3 во всех этапах. `memory.*` остаются немигрированными (candidate
  mappings); отсутствующие события не выдуманы.
- **Open Question №11 закрыт:** нормативная модель влияния memory на
  candidate generation / ranking / explanation / alternatives определена
  Recommendation Contract v0.3 (§6, §7): consent/safety — admissible
  set; приоритет источников внутри него; inferred signals не участвуют в
  ranking как факт до Memory Learning Loop; immutable
  `memory_snapshot_ref`; канонический порядок gates Killer PRD §5.1
  подтверждён без изменений.
- **Open Question №8 обновлён (частично решён):** OQ-E1 реестра закрыт;
  открыты — candidate mappings `memory.*`, финальные payload/owner
  этапа 14 (OQ-E3), registry gap `booking_confirmation_shown`.
- Ссылки «MVP Recommendation Contract (planned)» заменены на
  [[Ayla MVP Recommendation Contract]] v0.3 (этап 7, Memory Interaction,
  Recommendation and Proactivity Gates, OQ №4).
- Conforming amendment: бизнес-логика этапов, scope, негативные
  сценарии и metrics не изменены. Статус не изменён: approved/accepted.

### v1.0 (2026-07-29) — Approval: синхронизация с Intent Model (F1), ремарка о лимитах clarification (F2)

- **F1 (обязательное замечание owner review):** этап 4 — ссылка на
  «Ayla Intent Model Specification (planned, в разработке)» заменена на
  утверждённую [[Ayla Intent Model Specification]] v0.9.2
  (approved/accepted) и machine-readable contracts
  `03 AI System/Contracts/` (intent-registry.yaml, slot-registry.yaml,
  intent-output.schema.json, contract_version 0.5); триггер этапа 5
  перепривязан от Roadmap §3.1 к Output Contract Intent Model; ошибка
  этапа 4 `INTENT_UNRESOLVED` связана с `UNKNOWN` sentinel.
- **Open Question №7 закрыт** с задокументированным результатом сверки
  этапов 4–5 с утверждённым Output Contract (`requires_clarification`,
  `UNKNOWN`/`INTENT_UNRESOLVED`, confidence через язык, граница
  clarification vs execution readiness) — противоречий не выявлено.
- **F2:** этап 5 — добавлена ремарка о двух независимых ограничениях:
  не более 5 вопросов за discovery-сессию (UX-правило, полная UJS Stage 2)
  и не более 2 последовательных clarification-подходов по одному intent
  (AI runtime, Intent Model § Confidence and Clarification).
- Frontmatter: depends_on дополнен [[Ayla Intent Model Specification]].
- **Статус повышен: draft/proposed → approved/accepted** (Product Owner,
  2026-07-29; вердикт review — accept после устранения F1). Остальные
  Open Questions остаются в трекинге своих целевых артефактов.

### v0.3-final (2026-07-28) — Owner rulings 2026-07-28 (финализация MVP primary-booking journey)

- **Deferral (вариант Б):** ветки reschedule / cancel / late-window /
  substitute / YClients reschedule закреплены в Non-goals; добавлена
  Deferred branches reconciliation/traceability table со ссылкой на
  `99 Archive/proposals/decision-brief-appointment-reschedule-model.md`
  (planned AYLA-DEC-0022, draft до Journey-reconciliation). Проверено:
  конфликтующих статусов, событий и операций в этапах 1–14 и N1–N9 нет.
- **Slot hold (AYLA-DEC-0021):** этапы 10–11 дополнены цепочкой
  «slot selected → hold acquired → confirmation in progress»;
  UX-формулировка «Слот временно закреплён за вами до HH:MM…» с
  серверным `expires_at` (TTL 15 минут); hold не показывается до
  фактического создания; после expiry — повторная проверка доступности;
  `SLOT_TAKEN` добавлен в ошибки этапа 11; внутренние термины (ledger,
  locking, reservation boundary) пользователю не отображаются.
- **Миграция имён событий — только active canonical:** `consent.granted /
  consent.revoked` (этап 3), `intent.resolution_produced` (этап 4),
  `appointment.created / appointment.confirmed / appointment.completed`
  (этапы 11, 12, 14). Pending-семейства (`recommendation.*`,
  `qualified_action.*`, `memory.*`) не мигрированы; отсутствующие события
  не выдуманы. `booking_confirmation_shown` (этап 12) оставлен
  legacy-маркером — канонического analytics event в реестре нет.
- **Temporary Context** зафиксирован как session-only класс (без
  persistence по умолчанию, перевод в persistent — только через
  Memory Proposal по AYLA-DEC-0024, использование в сессии — в пределах
  `purpose_tags`).
- **Терминология этапов 11–12:** существительное Booking заменено на
  Appointment (создание и подтверждение записи, переход в `confirmed`);
  имена этапов сохранены дословно по Roadmap §2.1 как канонические
  идентификаторы; цитаты полной UJS («Booking Request / Booking Created /
  Confirmed Booking», «Stage 5 Booking») и UX-state tokens Roadmap §2.2
  (booking pending/confirmed/failed) оставлены как legacy-цитаты.
- Баннер статуса синхронизирован: Draft v0.3-final. Статус документа не
  изменён: draft / proposed.
- **Дополнено при приёмке (2026-07-28):** добавлен Open Question
  (cross-document backlog): naming-дрейф полной UJS v1.2
  (`booking.created/confirmed` → канон `appointment.*` — отдельная аменда
  или deferral) и терминологическое пересечение «substitute offer»
  (полная UJS, proactive gate) vs substitute-исполнитель (S12
  decision-brief-appointment-reschedule-model) — на сверку при
  reconciliation DEC-0022.

### v0.3 (2026-07-28) — Приведение к AYLA-DEC-0023/0024/0025 (cross-decision сверка)

- **OQ (whitelist) закрыт** (AYLA-DEC-0023/0024): whitelist — категориальная
  форма, наследование политики от категории, красная зона default deny,
  session state ≠ Persistent Memory, единственный pipeline
  inference → confirmation → persist, model-derived medical facts
  запрещены, расширение — только owner decision.
- **OQ (consent как факт) закрыт** (AYLA-DEC-0023/0024): consent state —
  authorization metadata, не Context Fact и не значение MemoryEntry;
  MemoryEntry ссылается на `consent_scope`, но согласие не персистируется
  как память.
- **OQ (events) — partially resolved** (AYLA-DEC-0025): решены конвенция
  имён, классификация, ownership, семантика intent- и consent-событий;
  открыты — регистрация `recommendation.*`, `qualified_action.attributed`,
  создание канонического Domain Event Registry, финальные payload/owner
  для этапа 14.
- **Memory Interaction приведён к решениям:** поле переименовано в
  `proposal_confidence`; упоминания whitelist переведены на категориальную
  форму.
- Статус не повышён: draft/proposed.

### v0.2.2 (2026-07-28) — OQ по Phase 2 закрыт по AYLA-DEC-0018 (accepted, Option C)

- **Open Question (Phase 2 gate) закрыт** ссылкой на [[Ayla Decision Log]]
  (AYLA-DEC-0018, accepted 2026-07-28): Phase 1 (session-only) —
  самостоятельный технический release gate; Product Thesis Validation
  открыта до Phase 2 и успешного Product Thesis Validation Scenario;
  активация Phase 2 сама по себе validation не закрывает.
- Статус не повышён: draft/proposed.

### v0.2.1 (2026-07-27) — Memory layer review fixes (по итогам review v0.2)

- Кандидатные event names явно помечены candidate/non-stable;
  `ContextFactUsed` переклассифицирован (classification unresolved).
- Memory taxonomy: normative guard — taxonomy не расширяет approved
  whitelist; добавлены статусы Outcome Fact.
- «Memory proof scenario» переименован в **Product Thesis Validation
  Scenario**.
- Metrics: оговорка — measurement method и baseline pending Measurement
  Framework.
- Статус не повышен: draft/proposed.

### v0.2 (2026-07-27) — Memory-first proposal layer (по итогам review)

- Purpose дополнен целями memory loop и memory proof **(proposal)**.
- Journey Operating Model: Personal Context Management обозначена сквозной
  ролью всего journey **(proposal)**.
- Memory Interaction расширен: Memory Learning Loop, memory taxonomy,
  Context Sufficiency Model, freshness/expiry/supersession, anti-lock-in,
  user memory controls — всё **(proposal)**.
- Recommendation and Proactivity Gates: Memory influence model
  **(proposal)** — память не сводится к preference boost.
- Статус не повышен: draft/proposed.

### v0.1.1 (2026-07-27) — Event namespace clarification (по итогам review)

- Поле событий этапов разделено на три класса: **domain event**,
  **analytics event**, **audit event**.
- Уточнено поведение при отказе от рекомендации: первый отказ →
  alternative в пределах лимита; повторный или жёсткий отказ →
  suppression.
- Статус не повышен: draft/proposed.

### v0.1 (2026-07-27) — Initial draft

- Документ создан по AYLA-DEC-0014 как производный MVP-срез
  [[Ayla User Journey Specification]] (Roadmap §2.1): 14 обязательных
  этапов и 9 обязательных негативных сценариев.
- Границы MVP зафиксированы по [[Ayla MVP Scope and Release Contract]]
  v0.2; consent-шаги и fail-closed поведение — по
  [[Consent Scope Registry]].
