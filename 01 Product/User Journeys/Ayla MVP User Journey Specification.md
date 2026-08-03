---
node_id: ayla.product.mvp-user-journey
title: Ayla MVP User Journey Specification
type: user-journey-specification
status: draft
decision_status: proposed
canonical_status: candidate
version: "1.1"
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
updated: 2026-07-31
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
  - "[[Ayla Intent Model Specification]]"
related:
  - "[[Consent Scope Registry]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Killer PRD]]"
  - "[[Ayla MVP Documentation Roadmap]]"
  - "[[Ayla Single-Provider Technical Pilot Execution Scope]]"
  - "[[Ayla Multi-Provider Product Validation Execution Scope]]"
---

# Ayla MVP User Journey Specification

> **Статус:** Draft v1.1 (2026-07-31) — structured revision в рамках
> Migration Wave D1 (Product/Journey Alignment) по
> [[Ayla MVP v0.3 Downstream Migration Plan]]. Документ приведён к
> [[Ayla MVP Scope and Release Contract]] v0.3, Living Digital Twin canon
> ([[Ayla Product Essence]] v1.1, [[Ayla Living Digital Twin Manifesto]]
> v1.0, AYLA-DEC-0026), [[Ayla MVP Product Thesis]] v0.5,
> [[Ayla Product Principles]] v0.1 и трёхканальной модели AYLA-DEC-0027.
> Состояние: draft / proposed / candidate — pending review и owner
> approval; документ **не** объявляется canonical. Предыдущая approved
> редакция — v1.0 (2026-07-29); история — в Change Log.
>
> **Соглашение о метках.** Утверждения, дословно или близко следующие из
> канонических источников, помечены как *(факт — источник §)*. Предложения,
> не зафиксированные в источниках, помечены **(proposal)** и подлежат
> review. Незакрытые вопросы собраны в Open Questions и являются
> non-blocking.

## 1. Purpose

This document:

- owns the normative MVP user journey;
- translates MVP Scope into user experience sequence;
- does not define screen layouts;
- does not define component composition;
- does not define APIs, DTOs or architecture;
- does not define release backlog;
- does not redefine MVP Scope;
- is an authoritative downstream input for Intent, Recommendation, UX and
  Measurement documents after approval.

Назначение документа:

- зафиксировать нормативный сквозной пользовательский путь MVP
  ([[Ayla MVP Scope and Release Contract]] v0.3 §4) в виде
  последовательности шагов с обязательными и опциональными элементами;
- описать обязательные негативные и recovery-сценарии и их поведение;
- связать путь с consent-правилами ([[Consent Scope Registry]]), Living
  Digital Twin canon и трёхканальной моделью (AYLA-DEC-0027);
- дать продуктовой, AI-, backend/frontend-командам и QA одну трактовку
  пользовательского потока;
- зафиксировать, как Ayla извлекает, проверяет и применяет разрешённый
  персональный контекст на протяжении всего journey **(proposal)**;
- определить Product Thesis Validation Scenario (см. Memory Interaction),
  без которого основная продуктовая гипотеза Ayla не считается
  проверенной; его статус определён решением AYLA-DEC-0018 (accepted,
  Option C): он не является release gate Phase 1 — Product Thesis
  Validation остаётся открытой до Phase 2.

Документ **не** описывает все будущие journeys: долгосрочные состояния,
доменные journeys, проактивные сценарии и полная state machine остаются в
[[Ayla User Journey Specification]] и здесь не дублируются (см. Non-goals).

Целевая аудитория: продуктовая команда, AI-команда, backend/frontend
разработчики, QA.

## 2. Canonical Position

- Документ — нормативный MVP-срез [[Ayla User Journey Specification]]
  (производный по AYLA-DEC-0014) и downstream от
  [[Ayla MVP Scope and Release Contract]] v0.3: релизный состав и границы
  определяет MVP Scope, этот документ их не переопределяет.
- Выше документа: [[Ayla Constitution]], [[Ayla Product Essence]] v1.1,
  [[Ayla Product Vision]] v2.0, [[Ayla MVP Product Thesis]] v0.5,
  [[Ayla Product Principles]] v0.1; по темам Living Digital Twin
  authoritative input — [[Ayla Living Digital Twin Manifesto]] v1.0
  (Manifesto §18).
- Обязательные owner decisions в scope этого документа: AYLA-DEC-0026
  (LDT — главный визуальный интерфейс; Transformation Goal — центральная
  доменная сущность), AYLA-DEC-0027 (три required channels),
  AYLA-DEC-0028 (четыре равнозначных trigger-сценария), AYLA-DEC-0029
  (28-day cycle — A2 exit evidence), AYLA-DEC-0033 (статус числовых
  порогов), AYLA-DEC-0034 (NO_FORMAL_RCT в initial beta).
- Consent, memory phases и authorization — по [[Consent Scope Registry]]
  (факт — CSR §2, §5, §8, §10); intent types и output contract — по
  [[Ayla Intent Model Specification]] v0.9.2 (approved/accepted).
- Исполнение пилота (фазы A0–B1) описывается execution scopes; этот
  документ задаёт только journey-логику (см. Relationship to A0–B1
  Execution).

## 3. Journey Operating Model

Принципы пути (факт — [[Ayla Product Principles]] v0.1 §4):

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

Действующие ограничения operating model:

- **Автономные действия без подтверждения пользователя запрещены** (факт —
  Конституция; MVP Scope v0.3 §6.5).
- **Fail-closed по умолчанию** (факт — [[Consent Scope Registry]] §2):
  неизвестный, отсутствующий, просроченный или неутверждённый scope
  обрабатывается как запрет; отсутствие consent record не
  интерпретируется как согласие.
- **Два activation gate** (факт — CSR §10): Phase 1 — session-only без
  персистентной памяти; Phase 2 — opt-in persistent memory. Phase 2 не
  является условием релиза Phase 1 (AYLA-DEC-0018, accepted, Option C).
- **Journey не строго линейна**: пользователь может уточнять intent,
  менять решение и возвращаться к предыдущим шагам (факт — полная UJS,
  State Transitions). Нумерация шагов отражает пользовательскую
  ответственность, а не обязательный однопроходный порядок исполнения:
  intent detection, context retrieval и clarification могут итерироваться
  **(proposal)**.
- Journey является **trigger-agnostic** (факт — AYLA-DEC-0028): ни один
  trigger-сценарий не является центром продукта.
- **Одна primary recommendation**, до двух alternatives — только по
  запросу или после отклонения primary, каждая с собственным
  `recommendation_id` (факт — [[Killer PRD]] §5.1).

## 4. Actors and Channels

Роли (actors) в сценарии:

| Actor | Описание |
|---|---|
| User | Клиент пилота — человек с beauty/wellness-потребностью и личной Transformation Goal (персона пилота, Thesis §5) |
| Ayla (AI) | Диалоговая логика и оркестрация пути: ai-bot-platform (runtime/channel consumer) + ayla-ai-core (reusable AI logic) — рекомендуемая MVP-композиция (факт — MVP Scope v0.3 §9) |
| Backend | SoR для каталога, провайдеров, availability, записей, consent, context facts (факт — MVP Scope v0.3 §9) |
| Provider | Соло-мастер или малый салон (≤3 специалистов), подтверждающий запись (пилотные профили — Thesis §5) |

**Required MVP channel set (факт — AYLA-DEC-0027; MVP Scope v0.3 §8):**

| Channel | Роль в journey |
|---|---|
| **Mobile App** | REQUIRED / primary product experience: полная визуальная и longitudinal experience — Living Digital Twin, photo capture, прогресс, история, контроль данных |
| **MAX Mini App** | REQUIRED / lightweight embedded companion: статус цели, рекомендация, booking, быстрый check-in, продолжение пути |
| **MAX Bot** | REQUIRED / conversational, notification and routing companion: диалог, уточнения, объяснения, напоминания, транзакционные уведомления, быстрые действия, маршрутизация |

Обязательные условия (факт — AYLA-DEC-0027; MVP Scope v0.3 §8):

- три канала — один продукт; единые identity, consent, safety,
  recommendation state, memory boundary, attribution и analytics;
- **feature parity across channels — NOT_REQUIRED**; capability обязана
  быть доступна в назначенном owning channel;
- journey является единым независимо от entry channel; пользователь может
  начать в MAX и продолжить в Mobile (см. Cross-channel Experience);
- channel-specific business logic запрещена;
- Telegram — вне пилотного scope (AYLA-DEC-0004; MVP Scope v0.3 §8).

## 5. Journey Overview

Нормативный backbone пути (детализация
[[Ayla MVP Scope and Release Contract]] v0.3 §4 до journey-уровня;
разметка OBLIGATORY / OPTIONAL / PARTIAL сохранена из §4):

```text
1.  Entry and recognition of context            — OBLIGATORY
2.  Identity / account continuity               — OBLIGATORY
3.  Consent and allowed inputs                  — OBLIGATORY
4.  Transformation Goal                         — OBLIGATORY
5.  Baseline and Living Digital Twin            — OBLIGATORY
6.  Recognition / «это я» / correction          — OBLIGATORY
7.  Intent understanding                        — OBLIGATORY
8.  Explainable recommendation                  — OBLIGATORY
9.  Next action                                 — OBLIGATORY
10. Optional booking or another action          — OPTIONAL
11. Continuity input / check-in / result        — PARTIAL
12. Progress and next state                     — OBLIGATORY (минимальная форма)
```

Главные свойства пути (факт — MVP Scope v0.3 §4):

```text
Journey terminal:
progress / next state (шаг 12), а не подтверждение записи

Booking:
OPTIONAL downstream action (шаг 10); отказ от действия — допустимый исход

Food Scanner:
CONDITIONAL trigger — один из равнозначных входов, не центр пути

Living Digital Twin:
key visual interface, not mandatory on every screen
```

Обязательные условия сценария (факт — MVP Scope v0.3 §4):

- consent gates действуют на входных данных, media и персистентной памяти
  — по [[Consent Scope Registry]] §10;
- recognition point обязательна (шаг 6): сигнал «это не похоже на меня» и
  исправление/перестроение Twin — часть сценария, не опция;
- Phase 1 — session-only memory; Phase 2 — opt-in persistent memory;
  Phase 2 не является условием релиза Phase 1;
- booking optional: сценарий не обязан завершаться записью;
- journey заканчивается прогрессом / следующим состоянием.

## 6. Stage Specifications

Формат: каждый шаг описан на journey-уровне — actor, trigger,
пользовательская цель, системное поведение, контроль пользователя,
fallback. Этот документ не определяет экраны, layouts, компоненты и
навигацию (см. Non-goals). События: canonical domain events используются
только там, где они утверждены (Domain Event Registry v0.2,
AYLA-DEC-0025); имена journey-level analytics events — TO_BE_DEFINED by
Measurement Framework (см. Metrics).

### 6.1 Entry and Context (шаги 1–3)

**Entry points и первый контакт.** Пользователь входит в journey через
любой из трёх required channels (§4): открывает MAX Bot (DM), переходит
по deep link в MAX Mini App или запускает Mobile App. Journey един
независимо от entry channel (факт — AYLA-DEC-0027). Ограничения первого
контакта (факт — полная UJS, Stage 1 Forbidden Behavior): не запрашивать
имя, возраст, вес при первом контакте; не начинать с анкеты; не
продавать. Progressive profiling — минимальные разрешённые inputs (факт —
MVP Scope v0.3 §6.1; Constitution Ст. VI).

**Trigger model (факт — AYLA-DEC-0028; Vision §10).** Четыре
равнозначных trigger-сценария — входы в путь, а не отдельные продукты
(канонические формулировки — [[Ayla Product Vision]] v2.0 §10;
safety/eligibility правила — [[Killer PRD]] §4):

1. контекст питания → рекомендация в beauty/wellness;
2. усталость или восстановление → подходящая забота;
3. подготовка к событию → план процедур;
4. история посещений и предпочтения → повторная запись или подбор
   специалиста.

```text
Food Scanner:
CONDITIONAL — один из равнозначных trigger-сценариев;
not required for every user;
not central daily loop;
not product center
```

Journey остаётся trigger-agnostic: сценарий food → beauty может
использоваться как демонстрационный пример в onboarding, но не определяет
центр продукта, доменную модель или приоритет реализации (факт —
AYLA-DEC-0002; Vision §10). Food-specific metrics — DIAGNOSTIC; primary
metrics — TRIGGER_AGNOSTIC (факт — AYLA-DEC-0028).

**Recognition of context.** Ayla принимает потребность своими словами и
подтверждает понимание контекста обращения; session context bootstrap
**(proposal)**: поднять контекст текущей сессии и — при активном
`preference_memory` (Phase 2) — проверить наличие релевантных актуальных
фактов до ответа, не показывая их без необходимости. Для возвращающегося
пользователя вход включает continuity: известный контекст не
переспрашивается (clarification suppression — см. §6.5).

**Identity and account continuity.** Единая идентичность пользователя
между Mobile App, MAX Mini App и MAX Bot обязательна (факт —
AYLA-DEC-0027; MVP Scope v0.3 §9 cross-channel account linking). Account
linking выполняется один раз и прозрачно; конфликт аккаунтов разрешается
явно с участием пользователя (см. Negative Scenarios, N10). Consent
continuity: состояние согласий едино во всех каналах (факт —
AYLA-DEC-0027; NFR — MVP Scope v0.3 §10).

**Consent and allowed inputs.** Consent request — не обязательно
отдельный экран: обработка текущего сообщения выполняется по
`service_necessity` без consent record (факт — [[Consent Scope Registry]]
§3); явный запрос согласия требуется для persistence, media capture,
проактивности и передачи данных для другой цели. Правила (факты — CSR §2,
§5.7, §8, §10):

- запрос согласия — с указанием цели (scope), а не факта «сохранить
  данные»; отказ не прерывает диалог;
- fail-closed: отсутствие, отказ или отзыв consent → операция не
  выполняется; session-only продолжение сохраняется;
- в Phase 1 `intent_understanding` и `provider_selection` работают по
  `service_necessity` в пределах сессии; persistent memory технически
  отключена;
- пользовательские команды: просмотр активных согласий; отзыв отдельного
  scope; отключение всей persistent personalization; «Что Ayla знает обо
  мне»; удаление выбранного memory fact; «Забыть это»;
- фото, видео и body-related data — особо чувствительные входы
  (факт — Manifesto §12).

Audit-события consent и authorization — канонический перечень CSR §9.1;
доменные события `consent.granted` / `consent.revoked` — канон
AYLA-DEC-0025 / Domain Event Registry v0.2.

### 6.2 Transformation Goal (шаг 4)

Transformation Goal — центральная доменная сущность продукта (факт —
AYLA-DEC-0026; Product Essence; Manifesto §2). На этом шаге пользователь
формулирует или подтверждает свою цель.

Нормативные положения:

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
  Ayla может помочь уточнить цель или продолжить с минимальным
  рабочим намерением (см. Negative Scenarios, N1).

Минимальная структура цели — in scope (факт — MVP Scope v0.3 §6.1);
детальная доменная модель цели определяется Domain-документами и здесь не
вводится.

### 6.3 Living Digital Twin Baseline and Recognition (шаги 5–6)

Living Digital Twin — главный визуальный интерфейс ключевых сценариев и
долгоживущее цифровое отражение самого пользователя (факт — AYLA-DEC-0026;
Manifesto §3). Twin — key visual interface, **not mandatory on every
screen** (факт — Manifesto §4; Product Essence §9).

**Обязательные experience points** (факт — MVP Scope v0.3 §6.4 MUST_HAVE;
Manifesto §14):

- **baseline** — сохранение исходного состояния;
- **controlled photo/media capture** — управляемая фотофиксация на
  разрешённых данных;
- **recognition «это я»** — пользователь мгновенно узнаёт себя
  (факт — Manifesto §5);
- **«это не похоже на меня»** — обязательный сигнал отклонения неверного
  представления;
- **correction / rebuild** — исправление или повторное построение модели;
- **identity continuity** — сохранение узнаваемой идентичности между
  версиями и состояниями (identity drift — недопустимый класс дефекта,
  факт — Manifesto §6);
- **comparison over time** — сравнение состояний во времени;
- **state-class distinction** — видимое различение классов достоверности;
- **deletion / user control** — удаление исходных и производных данных.

Recognition point — обязательная часть сценария, не опция (факт — MVP
Scope v0.3 §4): сигнал «это не похоже на меня» и исправление/перестроение
Twin включены в путь (см. Negative Scenarios, N3).

**Классы достоверности** (факт — Manifesto §9; Essence §8) — journey
обязан явно разделять и не смешивать:

- user-entered fact (введённый пользователем факт);
- observed fact (наблюдаемое, реально зафиксированное);
- reconstructed representation (реконструкция, включая сам Twin);
- inferred state (оценённое состояние);
- predicted scenario (прогноз);
- desired outcome (желаемый результат — Transformation Goal).

Реконструкция не выдаётся за факт; прогноз — за наблюдение; оценка — за
измерение; цель — за вероятный результат.

**Target image и video:**

```text
Target image:
CONDITIONAL
desired outcome only — выражение цели пользователя
not forecast
not promise

Video:
CONDITIONAL — только при подтверждённой необходимости для качества модели
(факт — MVP Scope v0.3 §6.4; Manifesto §14)
```

**Запрещено** (факт — MVP Scope v0.3 §6.4 OUT_OF_SCOPE; Manifesto §4,
§13):

- automatic idealization и универсальный body ideal;
- body shaming, давление, манипуляция страхом;
- medical simulation, medical-grade reconstruction, скрытая медицинская
  диагностика;
- guaranteed transformation и неподдержанный прогноз (в т.ч. 30/60/90
  дней);
- identity drift между версиями;
- arbitrary avatar replacement и произвольная генерация аватаров;
- автоматическое обновление Twin после каждого действия — визуальное
  обновление происходит при достаточных основаниях (факт — Manifesto §3).

### 6.4 Intent Understanding (шаг 7)

Ayla извлекает intent и slots из сообщения, определяет confidence и
проверяет safety constraints до перехода к рекомендации (факт — полная
UJS, Stage 3). Поддерживаемые intent types, required/optional slots и
confidence levels определяет [[Ayla Intent Model Specification]] v0.9.2
(approved/accepted: 11 продуктовых intent types + sentinel `UNKNOWN`) и
машиночитаемые contracts `03 AI System/Contracts/`
(intent-registry.yaml, slot-registry.yaml, intent-output.schema.json,
contract_version 0.5). `UNKNOWN` — resolver sentinel: execution по нему
запрещён; доменное событие `intent.resolution_produced` — канон
AYLA-DEC-0025 / Domain Event Registry v0.2.

Цель пользователя — чтобы Ayla поняла, чего он хочет достичь, а не только
что написал (Query vs Intent — факт, полная UJS Stage 3); intent
интерпретируется в контексте цели и разрешённых данных (факт — MVP Scope
v0.3 §4 шаг 5). Для разрешения ссылок на прошлый опыт («как в прошлый
раз») допускается targeted memory retrieval в пределах активного scope
**(proposal)**.

**Clarification.** При `requires_clarification` (недостаточно
обязательных слотов или низкий confidence — факт, Intent Model § Output
Contract) Ayla задаёт минимально необходимый вопрос; при отказе отвечать —
продолжает с имеющимся контекстом, обозначив неопределённость (факт —
полная UJS, Handling Incomplete Answers). Два независимых ограничения
(факт — v1.0, ремарка F2): **UX Discovery** — не более 5 вопросов за
discovery-сессию (полная UJS, Stage 2 Maximum Questions); **Intent
Resolution** — не более 2 последовательных clarification-подходов по
одному intent, после чего resolver возвращает `UNKNOWN` / `unresolved`
(Intent Model § Confidence and Clarification). **Clarification
suppression (proposal):** не задавать вопрос, ответ на который уже
содержится в актуальном разрешённом факте; устаревший или конфликтующий
факт не заменяет уточнение.

**Allowed context retrieval.** Personal Context Management — сквозная
capability всего journey **(proposal)**: контекст может извлекаться на
нескольких точках (session bootstrap, intent disambiguation,
clarification suppression, recommendation-time, execution, outcome
interpretation). Каждое использование контекста — в пределах активного
scope (факт — CSR §2): принцип — максимально полезное использование
минимально необходимого разрешённого контекста. В Phase 1 — только
session context; в Phase 2 — дополнительно persistent preferences при
активном `preference_memory` (факт — CSR §5.1/§5.2/§5.7, §10).
`CONTEXT_NOT_ALLOWED` — fail-closed deny; fallback — session-only режим.

Whitelist допустимых персональных фактов — категориальная форма
AYLA-DEC-0023 (allowed / requires dedicated consent / forbidden;
расширение — только owner decision). Inferred signals не сохраняются и не
используются как самостоятельное основание рекомендации; единственный
pipeline — inference → confirmation → whitelist check → persist (факт —
AYLA-DEC-0023/0024; CSR §5.7).

### 6.5 Recommendation and Explainability (шаг 8)

Recommendation исходит из Transformation Goal + разрешённого контекста и
формируется decision pipeline с обязательным порядком gates (см.
Recommendation and Proactivity Gates). Recommendation не зависит от
коммерческого статуса провайдера; LLM не является ranking authority —
ranking определяется детерминированными gates и eligibility, модель
работает в пределах их ограничений **(proposal)**.

**Explainability.** Объяснение обязательно (факт — MVP Scope v0.3 §6.3;
Конституция Ст. VII) и показывает:

- reason — почему предложено именно это, и какой разрешённый контекст
  применён (inline attribution — факт, Killer PRD §6.1);
- confidence class — уровень уверенности в поддерживаемой продуктом форме
  (не обязательные проценты — факт, Manifesto §10; числовой confidence
  остаётся внутри output contract, пользователю показывается
  вербализованная уверенность).

Объяснение соответствует фактически использованному контексту, не
заявляет неиспользованные факты и не раскрывает sensitive context
(факт — Capability Registry §6.5, key invariants CAP-005).
Персонализация, которую Ayla не может объяснить пользователю,
недопустима **(proposal)**; без объяснения рекомендация не показывается
**(proposal)**.

**User decision.** Пользователь может принять, отклонить или уточнить
рекомендацию; поддерживается обоснованное «ничего не делать» как
валидный исход (факт — MVP Scope v0.3 §5). После первого отклонения
primary — фиксируется `rerank_reason` и предлагается alternative в
пределах лимита; после повторного или явно жёсткого отказа дальнейшие
предложения подавляются: отказ принимается без давления (факт — Killer
PRD §5.1; полная UJS, Proactive Suppression Rules). Ничего не происходит
без явного подтверждения пользователя (факт — Конституция; MVP Scope
v0.3 §6.5).

### 6.6 Next Action and Optional Booking (шаги 9–10)

**Next action.** Пользователь выбирает реалистичный следующий шаг (факт —
MVP Scope v0.3 §4 шаг 7). Next action может быть:

- self-care action;
- check-in;
- plan update;
- information;
- booking;
- no action — обоснованное «ничего не делать» (валидный исход).

**Booking boundary:**

```text
Journey-level booking:
OPTIONAL — одна из downstream-опций пути (факт — MVP Scope v0.3 §4 шаг 8;
Principles 4.8 Booking Is Downstream)

Technical execution coverage:
MUST in A1/A2 where adapter is tested
(факт — Single-Provider Execution Scope)
```

Booking journey включает:

- booking как downstream action после выбора пользователя, с явным
  подтверждением перед созданием записи;
- alternatives before booking — пользователь видит, что запись — одна из
  опций, а не единственный исход;
- consent-limited provider context — провайдеру передаётся только
  контекст, разрешённый соответствующим scope (факт — CSR §2);
- attribution: `recommendation_id` → выбранное действие →
  `booking_id` / `appointment_id` — только если booking произошёл
  (факт — MVP Scope v0.3 §6.3, минимальный direct linkage);
- cancel / status: intent type CANCEL_APPOINTMENT поддерживается моделью
  intent; полноценная ветка cancel journey остаётся deferred beyond MVP
  primary-booking journey (owner ruling 2026-07-28, вариант Б — см.
  Non-goals);
- reschedule (Wave 1, owner decision — Simple Reschedule): same-ID
  перенос времени/даты в пределах того же Offering (без смены
  услуги/мастера) — **in scope**; выполняется через intent
  `RESCHEDULE_APPOINTMENT` и публикует `appointment.rescheduled`
  (канон — AYLA-DEC-0022 п. 1, п. 9; Domain Event Registry §6.3,
  `registered`, v0.4). Смена услуги/мастера, replacement, re-offer,
  cross-tenant перенос, изменение цены/длительности — остаются deferred
  (AYLA-DEC-0022 — полная ветка replacement; см. Non-goals);
- fallback при external booking failure — честное состояние booking
  failed с recovery path: повторить, выбрать другой слот, записаться
  позже (см. Negative Scenarios, N7–N9);
- progress / next state после appointment или после отказа — путь
  продолжается к шагу 12 в обоих исходах.

Slot hold (факт — AYLA-DEC-0021): при выборе слота — цепочка «slot
selected → hold acquired → confirmation in progress» с серверным
`expires_at` (TTL 15 минут); user-facing подтверждение — только после
authoritative `confirmed` state; `SLOT_TAKEN` без внутренних терминов.
Внешний booking provider не канонизируется: Yclients — пилотный
integration adapter, не canonical элемент journey **(proposal)**.

Проактивные уведомления вне транзакционного контура записи не
выполняются: Phase 1 — no proactive recommendations (факт — CSR §10);
допустимы только транзакционные уведомления по записи (факт — MVP Scope
v0.3 §6.1). Доменные события `appointment.created` /
`appointment.confirmed` / `appointment.completed` — канон AYLA-DEC-0025
/ Domain Event Registry v0.2.

### 6.7 Continuity, Check-ins and Progress (шаги 11–12)

**Continuity input / check-in / result.** Результат и follow-up
становятся continuity input (PARTIAL — факт, MVP Scope v0.3 §4 шаг 9).
Check-in — короткое действие: пользователь сообщает состояние, результат
или факт; feedback создаёт только Memory Proposal; persistent memory
обновляется после sensitivity/purpose check и проверки применимого
consent (факт — полная UJS, Memory Proposal). Молчание не
интерпретируется как согласие или отрицание (факт — полная UJS, Learning
Signals). Быстрые check-ins поддерживаются во всех каналах, с
conversational вводом в MAX Bot (см. Cross-channel Experience). Правила
памяти — в Memory Interaction.

**Progress and next state (journey terminal).** Journey завершается
прогрессом / следующим состоянием (OBLIGATORY, минимальная форма — факт,
MVP Scope v0.3 §4 шаг 10):

- пользователь видит сравнение состояний во времени (comparison over
  time) через Twin и/или поддерживаемые представления;
- прогресс показывается без давления и стыда (факт — Principles 4.10;
  Manifesto §13);
- следующее состояние формулируется честно: что наблюдаемо, что
  оценено, что является целью (state-class distinction, §6.3);
- отсутствие видимого изменения — тоже объяснимое состояние (факт —
  Manifesto §10);
- прогресс и next state доступны независимо от того, произошёл ли
  booking.

## 7. Cross-channel Experience

Применение AYLA-DEC-0027 на уровне journey:

- journey является единым независимо от entry channel; пользователь может
  начать в MAX Bot или Mini App и продолжить в Mobile App — и наоборот;
- account linking и consent continuity обязательны до cross-channel
  продолжения (факт — MVP Scope v0.3 §8/§9);
- recommendation state сохраняется между каналами: рекомендация,
  полученная в одном канале, доступна и объяснима в другом;
- channel-specific business logic запрещена; каналы — поверхности одного
  продукта поверх единого backend и domain model;
- **Mobile App** владеет full LDT / photo capture / progress / history /
  data-control experience;
- **MAX Mini App** даёт lightweight continuation: статус цели,
  рекомендация, booking, быстрый check-in;
- **MAX Bot** объясняет, напоминает, маршрутизирует и поддерживает быстрые
  check-ins и транзакционные уведомления;
- deep links / universal links используются для channel routing, где
  поддерживаются платформой (факт — MVP Scope v0.3 §9);
- отсутствие второстепенной функции в Mini App или Bot не блокирует путь,
  если capability доступна в назначенном owning channel (факт —
  AYLA-DEC-0027);
- универсальная multi-channel спецификация для MVP не требуется (факт —
  MVP Scope v0.3 §8).

Screen-level navigation и handoff UX этим документом не описываются
(см. Non-goals; Open Question №1).

## 8. Negative Scenarios

Для каждого сценария: trigger, system behavior, user control, safe
fallback, journey continuation, analytics evidence. Сценарии описывают
поведение пути, не operational runbook.

### N1. Пользователь не готов сформулировать цель

- **Trigger:** пользователь не может или не хочет формулировать
  Transformation Goal на шаге 4.
- **System behavior:** Ayla предлагает помощь в уточнении цели
  минимальными вопросами или продолжение с минимальным рабочим
  намерением; давление запрещено.
- **User control:** отложить цель; изменить её позже; продолжить без
  цели.
- **Safe fallback:** путь продолжается с явно обозначенной
  неопределённостью; Twin baseline и рекомендации не блокируются.
- **Journey continuation:** шаг 5; цель может быть установлена на любом
  последующем шаге.
- **Analytics evidence:** goal deferred / goal established later —
  evidence point «goal established/updated» (Metrics).

### N2. Отказ от фото

- **Trigger:** пользователь отказывается от фотофиксации или media
  capture на шаге 5.
- **System behavior:** отказ принимается без давления; честно объясняется,
  какие Twin-функции станут ограниченными (факт — Manifesto §11).
- **User control:** отказаться от конкретных входных данных без потери
  доступа к несвязанной функциональности.
- **Safe fallback:** journey продолжается на не-media inputs; Twin
  baseline откладывается; несвязанные capabilities сохраняются.
- **Journey continuation:** шаги 7–9 без визуального baseline; baseline
  возможен позже.
- **Analytics evidence:** media consent declined; baseline deferred.

### N3. «Это не похоже на меня»

- **Trigger:** пользователь отклоняет Twin-представление на recognition
  point (шаг 6).
- **System behavior:** сигнал принимается как обязательная часть модели
  контроля (факт — Manifesto §5/§11); предлагается исправление или
  повторное построение модели; объясняются ограничения качества входных
  материалов.
- **User control:** отклонить, исправить, перестроить Twin; удалить
  исходные и производные данные.
- **Safe fallback:** correction/rebuild flow; путь не продолжается с
  отвергнутым представлением как с валидным.
- **Journey continuation:** повторная recognition после исправления;
  далее шаг 7.
- **Analytics evidence:** recognition rejected; correction completed —
  evidence point «recognition accepted/corrected» (Metrics).

### N4. Отзыв consent

- **Trigger:** пользователь отзывает scope или отключает persistent
  personalization.
- **System behavior:** fail-closed: новое использование прекращается
  немедленно; сохранённые предпочтения помечаются `revoked` и перестают
  использоваться; подтверждение пользователю, что именно изменилось
  (факт — CSR §2, §5.7, §7, §8).
- **User control:** отзыв одной командой; отключение всей persistent
  personalization; «Что Ayla знает обо мне».
- **Safe fallback:** session-only продолжение; несвязанная
  функциональность сохраняется.
- **Journey continuation:** путь продолжается в session-only режиме.
- **Analytics evidence:** consent revoked — audit события CSR §9.1;
  доменное `consent.revoked` (канон AYLA-DEC-0025).

### N5. Отсутствие подходящей рекомендации

- **Trigger:** `NO_CANDIDATES` — все кандидаты исключены на этапах
  eligibility/relevance.
- **System behavior:** честное состояние no recommendation; Ayla не
  выдумывает рекомендацию (факт — Killer PRD §5.3 Fallback).
- **User control:** изменить запрос, уточнить ограничения, выбрать
  «ничего не делать».
- **Safe fallback:** обычный поиск/запись без персонализированной primary;
  альтернативный next action (self-care, information, check-in).
- **Journey continuation:** шаг 9 с альтернативным действием; шаг 12.
- **Analytics evidence:** no recommendation shown; fallback action
  selected.

### N6. Безопасная рекомендация «ничего не делать»

- **Trigger:** по совокупности контекста оптимальное действие — отсутствие
  действия.
- **System behavior:** Ayla объясняет, почему «ничего не делать» —
  обоснованный следующий шаг (факт — MVP Scope v0.3 §5 п. 6; Vision:
  «отказ от действия тоже может быть корректной рекомендацией»).
- **User control:** принять, отклонить, запросить альтернативу.
- **Safe fallback:** рекомендация не навязывается; отказ — валидный исход
  без давления.
- **Journey continuation:** check-in / continuity input; шаг 12.
- **Analytics evidence:** «no action» accepted — evidence point
  «action accepted/rejected» (Metrics).

### N7. Booking unavailable

- **Trigger:** `NO_AVAILABLE_SLOTS` — нет свободных слотов у выбранного
  провайдера.
- **System behavior:** предложить альтернативу — другой мастер или другое
  время (факт — полная UJS, Error Recovery 1); повторный прогон
  recommendation с уточнённым constraint и собственным
  `recommendation_id` (факт — Killer PRD §5.1).
- **User control:** выбрать альтернативу, записаться позже, отказаться от
  booking.
- **Safe fallback:** slot unavailable + альтернативные варианты; путь не
  обрывается на отсутствии слотов.
- **Journey continuation:** шаг 10 с альтернативой или шаги 11–12 без
  booking.
- **Analytics evidence:** slots unavailable; alternative offered/accepted.

### N8. Provider unavailable

- **Trigger:** `PROVIDER_INELIGIBLE` — провайдер не принимает запись
  (факт — Capability Registry §6.9, key invariants CAP-009).
- **System behavior:** кандидат исключается до показа primary; если
  недоступность выявлена после показа — честное сообщение и alternative
  (факт — Killer PRD §5.1: eligibility до ranking).
- **User control:** принять альтернативу или отказаться.
- **Safe fallback:** альтернативная рекомендация с объяснением замены
  **(proposal)**.
- **Journey continuation:** шаги 8–9 с альтернативой.
- **Analytics evidence:** provider ineligible; replacement shown.

### N9. External booking failure

- **Trigger:** `APPOINTMENT_NOT_CONFIRMED`, `APPOINTMENT_CONFLICT`,
  `SLOT_TAKEN`, hold expired, `TOOL_TIMEOUT` при создании записи через
  внешний adapter.
- **System behavior:** не показывать подтверждение неподтверждённой
  записи (факт — полная UJS, Stage 5 Success Criteria); после expiry
  hold — повторная проверка доступности (факт — AYLA-DEC-0021);
  дублирование side effects при retry недопустимо (идемпотентность —
  факт, Roadmap §6.3).
- **User control:** повторить, выбрать другой слот, записаться позже.
- **Safe fallback:** booking failed с честным описанием и recovery path;
  детали доступны по запросу в диалоге.
- **Journey continuation:** повтор шага 10 или переход к шагам 11–12 без
  booking; прогресс/next state не зависят от успеха booking.
- **Analytics evidence:** booking failed; recovery completed — evidence
  point «recovery completed» (Metrics).

### N10. Cross-channel account conflict

- **Trigger:** при account linking обнаружены два разных аккаунта или
  конфликт идентичности между каналами.
- **System behavior:** конфликт не разрешается молча; пользователю
  показывается, какие идентичности конфликтуют, и предлагается явный
  выбор; до разрешения cross-channel continuity для конфликтующих
  аккаунтов не активируется **(proposal)**.
- **User control:** подтвердить связку, оставить аккаунты раздельными,
  запросить удаление лишнего.
- **Safe fallback:** каждый канал продолжает работать со своей сессией без
  слияния данных.
- **Journey continuation:** путь продолжается в текущем канале; linking
  повторяется позже.
- **Analytics evidence:** account conflict detected; linking
  resolved/deferred — evidence point «cross-channel continuation»
  (Metrics).

### N11. Offline / degraded mode

- **Trigger:** потеря сети или деградация канала (особенно Mobile App).
- **System behavior:** честное сообщение о деградации; уже полученные
  состояния (цель, прогресс, детали записи) остаются видимыми из
  последнего известного состояния; действия, требующие backend, не
  имитируются **(proposal)**.
- **User control:** повторить позже; продолжить просмотр доступного
  состояния.
- **Safe fallback:** read-only просмотр последнего синхронизированного
  состояния; без скрытых offline-записей действий.
- **Journey continuation:** путь возобновляется с сохранённого состояния
  после восстановления связи.
- **Analytics evidence:** degraded mode entered; session resumed.

### N12. Tool / model failure

- **Trigger:** `TOOL_TIMEOUT` / `MODEL_UNAVAILABLE` на любом шаге,
  использующем tool call или LLM.
- **System behavior:** model/provider fallback (факт — MVP Scope v0.3
  §10); при полной недоступности — честное сообщение о сбое и предложение
  вернуться позже (факт — полная UJS, Error Recovery 3).
- **User control:** повторить; продолжить позже; выбрать действие без
  AI-обработки, где применимо.
- **Safe fallback:** retry; при повторном сбое — human handoff
  **(proposal)**.
- **Journey continuation:** путь возобновляется с последнего валидного
  состояния.
- **Analytics evidence:** tool failure — диагностическая телеметрия
  (MVP Scope v0.3 §11).

### N13. Unsafe or medical-like request

- **Trigger:** `SAFETY_BLOCKED` — запрос конфликтует с safety-critical
  контекстом или competence boundary (медицинская диагностика, скрытый
  medical inference).
- **System behavior:** остановить обработку и перейти в Boundary
  Handling: не подтверждать и не продолжать небезопасный путь; задать
  только минимальные вопросы о срочности и red flags; предложить
  безопасный следующий шаг или направление к квалифицированному
  специалисту (факт — полная UJS, Edge Case 2; Killer PRD §4.1 OD-K6).
- **User control:** получить безопасную альтернативу; отказаться.
- **Safe fallback:** boundary message без CTA на заблокированную услугу;
  безопасная альтернатива — только после Boundary Handling (факт — полная
  UJS, S8).
- **Journey continuation:** путь продолжается вне заблокированной ветки.
- **Analytics evidence:** safety block — evidence point (Metrics);
  unsafe block rate — диагностическая телеметрия.

### N14. User abandons and later resumes

- **Trigger:** пользователь прерывает путь на любом шаге и возвращается
  позже — в том же или другом канале.
- **System behavior:** путь возобновляется с сохранённого состояния; в
  Phase 1 — в пределах session; при активном Phase 2 consent — с
  persistent continuity; известное не переспрашивается (факт — CSR §10;
  clarification suppression, proposal).
- **User control:** продолжить, начать заново, удалить сохранённое.
- **Safe fallback:** при отсутствии consent на continuity — новый вход
  без повторного использования прошлых данных.
- **Journey continuation:** возврат на прерванный шаг или к шагу 12
  (progress/next state).
- **Analytics evidence:** session resumed; cross-channel continuation —
  evidence point (Metrics).

### N15. Deletion request

- **Trigger:** пользователь запрашивает удаление данных: «Забыть это»,
  удаление memory fact, удаление исходных и производных Twin-данных.
- **System behavior:** удаление выполняется с подтверждением, что именно
  удалено; производные данные рассматриваются как чувствительные
  соразмерно исходным (факт — Manifesto §11/§12; CSR §8).
- **User control:** выборочное удаление; полное удаление; просмотр перед
  удалением.
- **Safe fallback:** до завершения удаления данные не используются в
  новых решениях **(proposal)**.
- **Journey continuation:** путь продолжается без удалённых данных; Twin
  baseline при удалении media перестраивается или откладывается.
- **Analytics evidence:** deletion/consent change — evidence point
  (Metrics).

### N16. Repeated manual intervention visible as pilot limitation

- **Trigger:** повторяющаяся ручная операционная интервенция
  (manual operations пилота) становится видимой пользователю.
- **System behavior:** честная коммуникация ограничения пилота без
  имитации автоматики; ручное вмешательство не выдаётся за
  автоматическое действие системы **(proposal)**.
- **User control:** принять limitation, отложить действие, отказаться.
- **Safe fallback:** действие завершается вручную с явным статусом; путь
  не блокируется.
- **Journey continuation:** путь продолжается после завершения ручного
  шага.
- **Analytics evidence:** manual intervention completed — видимая
  limitation фиксируется как pilot evidence, не как дефект journey
  **(proposal)**.

## 9. Safety, Privacy and Dignity

- **Safety gates** — детерминированные, обязательные cross-cutting ко
  всем product capabilities (факт — MVP Scope v0.3 §6.5); safety
  evaluation не обходится ни одним fast path (факт — полная UJS, Context
  Sufficiency Gate).
- **Competence boundary:** запрет скрытой медицинской диагностики
  (факт — Конституция Ст. X; MVP Scope v0.3 §6.5); unsafe или
  medical-like request → Boundary Handling (Negative Scenarios, N13).
- **Privacy:** fail-closed consent; purpose limitation; минимизация;
  session-only default до Phase 2 gate; отсутствие consent record ≠
  согласие (факт — CSR §2, §10).
- **Body dignity и anti-shaming:** нейтральный поддерживающий язык; запрет
  стыда, давления, ранжирования внешности и манипуляции страхом
  (факт — Manifesto §13; Principles 4.10).
- **Honest Representation:** разделение классов достоверности во всех
  объяснениях и представлениях (§6.3); запрет deceptive precision
  (факт — Manifesto §16 AI/ML).
- **User control:** просмотр, исправление, удаление, отзыв согласия
  реализуемы на практике (факт — MVP Scope v0.3 §5 п. 10).
- **Audit:** критические события (consent, authorization, booking,
  safety) аудируются (факт — MVP Scope v0.3 §6.5; CSR §9.1).

## 10. Memory Interaction

MVP-срез правил памяти полной UJS; полная модель — в UJS и ADR-0012.

```text
Phase 1:
session-only memory
persistent memory disabled (факт — CSR §10.1)

Phase 2:
opt-in persistent memory after Consent Scope Registry gate (факт — CSR §10.2)
```

Journey обязан:

- объяснять, что запоминается, и показывать влияние памяти на решение;
- позволять не давать persistent consent без потери несвязанной
  функциональности;
- поддерживать deletion («Забыть это», удаление выбранного memory fact —
  факт, CSR §8);
- не делать Phase 1 evidence доказательством memory-dependent claims
  (факт — AYLA-DEC-0018; Single-Provider Execution Scope §14).

**Memory Learning Loop (proposal):** Observe → Propose → Verify → Store →
Retrieve → Apply → Measure outcome → Correct. Memory Proposal flow
(факт — полная UJS, When Memory is Created): сообщение или событие
создаёт только proposal; persistent memory — после sensitivity/purpose
check и consent check; молчание и продолжение диалога не являются
согласием. Поле `proposal_confidence` допустимо у MemoryProposal и в
audit, но не переходит в canonical MemoryEntry (факт — AYLA-DEC-0024).
Статусы MemoryProposal и состав MemoryEntry определяются AYLA-DEC-0024;
имена событий `memory.*` — candidate до регистрации в Domain Event
Registry (AYLA-DEC-0025) и здесь не канонизируются.

**Consent state ≠ Context Fact** (факт — AYLA-DEC-0023/0024): согласие —
authorization metadata в Consent Management, не факт памяти; MemoryEntry
хранит только ссылку `consent_scope`.

**Перепроверка памяти** (факт — полная UJS, When Memory Must be
Questioned): Ayla переспрашивает при низкой актуальности факта, истечении
TTL, противоречии, а также когда временный, изменяемый или
safety-critical факт используется для существенного решения.

**Anti-lock-in и novelty guard (proposal):** история пользователя — не
безусловный приказ повторить прошлый выбор; preference boost не обходит
safety, eligibility и economic-neutrality; система сохраняет разумную
возможность исследования alternatives.

**User memory controls** (факты — CSR §8; дополнения — **proposal**):
просмотр активных согласий; отзыв scope; отключение всей persistent
personalization; «Что Ayla знает обо мне»; удаление выбранного memory
fact; «Забыть это»; подтверждение, что именно изменилось после отзыва;
«Почему это сохранено» и «Где это использовалось» (provenance disclosure,
proposal); ограничение использования факта — через модель `purpose_tags`
(факт — AYLA-DEC-0024). Правило «Не спрашивать снова» применяется только
к необязательным повторным вопросам и Memory Proposal prompts и не
отключает обязательные safety/authorization/consent/freshness/legal
проверки (v1.0).

### Product Thesis Validation Scenario **(proposal)**

Статус определён AYLA-DEC-0018 (accepted, Option C): Phase 1
(session-only) — самостоятельный технический release gate; Product Thesis
Validation открыта до Phase 2 и успешного прохождения этого сценария.

**Первый визит.** Пользователь сообщает цель, удобное время и важное
ограничение. Ayla использует их в текущей сессии, предлагает сохранить
допустимые предпочтения, получает согласие, сохраняет подтверждённые
факты.

**Повторный визит.** Пользователь: «Хочу снова записаться на этой
неделе». Ayla извлекает релевантные актуальные факты, не повторяет
известные вопросы, уточняет только изменяемое, учитывает прошлый
outcome, предлагает решение, объясняет использование памяти и даёт
возможность его исправить.

**Acceptance criterion:** повторный journey короче, точнее и персональнее
первого; Ayla использует минимум один релевантный подтверждённый факт,
показывает его влияние на решение, позволяет исправить или отключить его
и не использует нерелевантные или отозванные данные.

## 11. Recommendation and Proactivity Gates

MVP-срез; полные правила — полная UJS §6 и [[Killer PRD]] §5.

- **User-Initiated Recommendation Gate** (факт — полная UJS §6): ответ на
  явный запрос проверяет safety, eligibility, Context Sufficiency,
  competence boundary и explicit current refusal. В MVP существуют только
  user-initiated рекомендации.
- **Proactive Readiness Gate — неактивен в MVP:** Phase 1 работает в
  режиме no proactive recommendations (факт — CSR §10); допустимы только
  транзакционные уведомления по записи (§6.6).
- **Обязательный порядок gates** для любой рекомендации (факт — Killer
  PRD §5.1): consent/privacy → safety → eligibility/availability →
  relevance → preference boost → economic-neutrality → primary output.
- **Economic neutrality** (факт — Killer PRD §5.3; Конституция):
  комиссия, booking fee и коммерческий статус провайдера не влияют на
  organic ranking; нарушение блокирует выдачу.
- **LLM не ranking authority:** ranking определяется детерминированными
  gates и eligibility (§6.5, proposal).

**Memory influence model (proposal):** влияние памяти не сводится к
одному preference boost на этапе ranking. Разные типы фактов работают на
разных этапах решения: интерпретация intent, hard constraints и
exclusions, формирование candidate set, outcome-informed relevance,
preference weighting, novelty/diversity guard, выбор explanation и
уровня уверенности. Канонический pipeline Killer PRD §5.1 этим не
отменяется — порядок gates сохраняется; уточнение контракта «как тип
факта влияет на решение» — предмет MVP Recommendation Contract.

## 12. Business Alignment

- Путь «цель → понимание → объяснимая рекомендация → следующий шаг →
  прогресс» реализует составную ценность MVP (факт — MVP Scope v0.3 §3);
  booking — secondary downstream evidence, не центральная метрика MVP
  (факт — MVP Scope v0.3 §11).
- Attribution: минимальный direct linkage `recommendation_id` → выбранное
  действие → `booking_id` / `appointment_id` при фактическом booking
  (факт — MVP Scope v0.3 §6.3; Killer PRD §6).
- Экономическая нейтральность рекомендации (§11) защищает доверие как
  актив пилота (факт — Killer PRD §5.3; полная UJS, Monetization
  Neutrality).
- Проверяемый тезис MVP: накопленное и объяснимое понимание пользователя,
  а не сама функция записи, создаёт преимущество (факт — Thesis;
  AYLA-DEC-0002). Шаги 4–8 — носители этого тезиса в journey.
- **(proposal)** Product Thesis Validation Scenario (Memory Interaction) —
  продуктовый критерий проверки тезиса на уровне journey: повторная
  рекомендация доказуемо полезнее благодаря разрешённой памяти; статус —
  AYLA-DEC-0018 (Option C): не release gate Phase 1.

## 13. Metrics

Journey-level evidence points (без числовых порогов; статус порогов —
факт, AYLA-DEC-0033: процентные цели — working validation thresholds,
final go/no-go — после B0 evidence и Measurement Framework):

| Evidence point | Шаги / сценарии |
|---|---|
| goal established/updated | 4 |
| baseline created | 5 |
| recognition accepted/corrected | 6 |
| recommendation explained | 8 |
| action accepted/rejected | 9 |
| booking selected/not selected | 10 |
| cross-channel continuation | 2, Cross-channel Experience |
| check-in/result | 11 |
| progress viewed | 12 |
| user control exercised | 3, 9, Safety/Privacy |
| deletion/consent change | 3, N4, N15 |
| safety block | N13 |
| recovery completed | N1–N16 |

```text
Event names:
TO_BE_DEFINED by Measurement Framework / analytics registry
```

Canonical domain events, где они уже утверждены, используются по Domain
Event Registry v0.2 (`consent.*`, `intent.resolution_produced`,
`appointment.*` — канон AYLA-DEC-0025); новые канонические имена для
journey evidence этим документом не выдумываются. Диагностическая
телеметрия релиза (resolved intents, clarification rate, recommendation
shown/acceptance, rejection reasons, unsafe block rate, tool failure
rate, median response time) сохраняется как техническая телеметрия
(факт — MVP Scope v0.3 §11). Measurement method и baseline — pending
Measurement Framework (v1.0).

## 14. Constitutional Traceability

| Принцип Конституции | Шаги / разделы | Реализация в MVP-срезе |
|---|---|---|
| Ст. I (предметная область) | 1 | Journey начинается с потребности человека и его цели, не с каталога |
| Ст. VI (доверие расходуется вопросами) | 7 | Не более 5 вопросов Discovery (полная UJS); clarification suppression (proposal) |
| Ст. VII (объяснимость) | 8 | Объяснение рекомендации обязательно (MVP Scope v0.3 §6.3); unexplained memory use недопустимо (proposal) |
| Ст. X (уместность прежде действия; запрет скрытой мед. диагностики) | 3, 9, N13 | Явное подтверждение перед действием; отказ без прерывания; Boundary Handling; никакой проактивности в Phase 1 |
| Пользователь контролирует персональный контекст | 3, Memory Interaction | Fail-closed consent; whitelist фактов; revocation; команды CSR §8; deletion |
| AI не является источником истины | 7, 10 | Backend — SoR; подтверждение только фактически достигнутого состояния; inference не становится фактом без подтверждения |
| Recommendation отделяется от action | 8–10 | Рекомендация не создаёт запись без явного подтверждения |
| Экономическая нейтральность | 8, Gates | Economic-neutrality check до показа primary (Killer PRD §5.3) |
| Критические решения прослеживаемы | все | Audit events CSR §9.1; `recommendation_id` сквозная связь; provenance фактов памяти (proposal) |

## 15. Relationship to A0–B1 Execution

Journey document не описывает execution plans. Компактная привязка
(факт — execution scopes):

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
counts, detailed gates и operational procedures в этот документ не
переносятся.

## 16. Non-goals

Этот документ не определяет:

- screens;
- visual layouts;
- component library;
- navigation spec;
- API/DTO;
- domain schema;
- ML architecture;
- final analytics thresholds;
- provider ranking algorithm;
- operations runbook;
- monetization implementation;
- store distribution;
- full marketplace journey.

Не входит в данный MVP-срез (основания указаны):

- все состояния и journeys полной [[Ayla User Journey Specification]] за
  пределами сквозного сценария (S7 Long-term, доменные journeys, полная
  state machine, re-engagement);
- проактивные рекомендации и Proactive Readiness Gate в действии
  (deferred — CSR §10);
- платежи пользователя в journey (факт — MVP Scope v0.3 §7; клиент Ayla
  не платит — AYLA-DEC-0032);
- отмена записи как полноценная ветка journey, late-window, substitute и
  reschedule sync-конфликты — **deferred (вариант Б, owner ruling
  2026-07-28)**: intent type CANCEL_APPOINTMENT поддерживается моделью
  intent, операциональная семантика полной ветки определяется AYLA-DEC-0022
  (accepted, действует —
  `99 Archive/proposals/decision-brief-appointment-reschedule-model.md`);
  в шагах 1–12 и N1–N16 нет статусов, событий или операций этих веток;
- **Simple Reschedule — исключение из вышеуказанного deferral (Wave 1,
  owner decision).** Same-ID перенос времени/даты в пределах того же
  Offering — in scope: intent `RESCHEDULE_APPOINTMENT`, событие
  `appointment.rescheduled` (канон — AYLA-DEC-0022 п. 1, п. 9; Domain
  Event Registry §6.3, `registered`, v0.4). Остаются deferred: смена
  услуги/мастера, replacement, re-offer, cross-tenant перенос, изменение
  цены/длительности (полная replacement-ветка AYLA-DEC-0022);
- Telegram и любые каналы кроме трёх required (факт — MVP Scope v0.3 §8;
  AYLA-DEC-0004/0027);
- программа лояльности, marketplace-сценарии, несколько стран (факт —
  MVP Scope v0.3 §7).

Ложные трактовки памяти, запрещённые в MVP (факты — CSR §5.7 Prohibited,
§2; полная UJS Memory Proposal; остальное — **proposal**):

- скрытое сохранение inferred traits без подтверждения пользователя (факт);
- использование отозванного или неразрешённого контекста (факт);
- построение sensitive attributes из поведения (факт);
- бессрочное использование предпочтений без проверки актуальности
  **(proposal)**;
- использование provider-authored данных как пользовательских
  предпочтений без маркировки источника и подтверждения **(proposal)**;
- автоматическое повторение прошлого выбора только на основании истории
  **(proposal)**;
- персонализация, которую Ayla не может объяснить пользователю
  **(proposal)**;
- оптимизация рекомендаций только по booking conversion (факт — полная
  UJS, Business Metrics).

## 17. Open Questions

Только non-blocking вопросы; AYLA-DEC-0027…0034 не переоткрываются.

1. **Exact wording of cross-channel handoff** — формулировки перехода
   между каналами (Bot → Mobile, Mini App → Mobile) определяются
   UX-документами.
2. **Exact event names** — имена analytics events для journey evidence
   points (Metrics) — TO_BE_DEFINED by Measurement Framework / analytics
   registry.
3. **Exact recognition quality threshold** — качественный порог
   recognition Twin; принцип Recognition (Manifesto §5) не вводит числовой
   similarity score.
4. **Exact offline fallback UX** — детали read-only поведения в degraded
   mode (N11) — UX-документы.
5. **Exact first-run media permission timing** — момент запроса media
   permission при первом запуске Mobile App — UX/platform-документы.

## 18. Change Log

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
  persistence по умолчанию, перевод в persistent — только через Memory
  Proposal по AYLA-DEC-0024, использование в сессии — в пределах
  `purpose_tags`).
- **Терминология этапов 11–12:** существительное Booking заменено на
  Appointment (создание и подтверждение записи, переход в `confirmed`);
  имена этапов сохранены дословно по Roadmap §2.1 как канонические
  идентификаторы.
- Баннер статуса синхронизирован: Draft v0.3-final. Статус документа не
  изменён: draft / proposed.

### v0.3 (2026-07-28) — Приведение к AYLA-DEC-0023/0024/0025 (cross-decision сверка)

- **OQ №10 закрыт** (AYLA-DEC-0023/0024): whitelist — категориальная
  форма, наследование политики от категории, красная зона default deny,
  session state ≠ Persistent Memory, единственный pipeline
  inference → confirmation → persist, model-derived medical facts
  запрещены, расширение — только owner decision.
- **OQ №12 закрыт** (AYLA-DEC-0023/0024): consent state — authorization
  metadata, не Context Fact и не значение MemoryEntry; MemoryEntry
  ссылается на `consent_scope`, но согласие не персистируется как память.
- **OQ №8 — partially resolved** (AYLA-DEC-0025): решены конвенция
  имён, классификация, ownership, семантика intent- и consent-событий;
  открыты — регистрация `recommendation.*`, `qualified_action.attributed`,
  создание канонического Domain Event Registry, финальные payload/owner
  для этапа 14.
- **Memory Interaction приведён к решениям:** поле переименовано в
  `proposal_confidence`; упоминания whitelist переведены на категориальную
  форму.
- Статус не повышён: draft/proposed.

### v0.2.2 (2026-07-28) — OQ №9 закрыт по AYLA-DEC-0018 (accepted, Option C)

- **Open Question №9 закрыт** ссылкой на [[Ayla Decision Log]] (AYLA-DEC-0018,
  accepted 2026-07-28): Phase 1 (session-only) — самостоятельный технический
  release gate; Product Thesis Validation открыта до Phase 2 и успешного
  Product Thesis Validation Scenario; активация Phase 2 сама по себе
  validation не закрывает.
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
- Статус не повышён: draft/proposed.

### v0.2 (2026-07-27) — Memory-first proposal layer (по итогам review)

- Purpose дополнен целями memory loop и memory proof **(proposal)**.
- Journey Operating Model: CAP-001 обозначена сквозной capability всего
  journey **(proposal)**.
- Memory Interaction расширен: Memory Learning Loop, memory taxonomy,
  Context Sufficiency Model, freshness/expiry/supersession, anti-lock-in,
  user memory controls — всё **(proposal)**.
- Recommendation and Proactivity Gates: Memory influence model
  **(proposal)** — память не сводится к preference boost.
- Статус не повышён: draft/proposed.

### v0.1.1 (2026-07-27) — Event namespace clarification (по итогам review)

- Поле событий этапов разделено на три класса: **domain event**,
  **analytics event**, **audit event**.
- Уточнено поведение при отказе от рекомендации: первый отказ →
  alternative в пределах лимита; повторный или жёсткий отказ →
  suppression.
- Статус не повышён: draft/proposed.

### v0.1 (2026-07-27) — Initial draft

- Документ создан по AYLA-DEC-0014 как производный MVP-срез
  [[Ayla User Journey Specification]] (Roadmap §2.1): 14 обязательных
  этапов и 9 обязательных негативных сценариев.
- Границы MVP зафиксированы по [[Ayla MVP Scope and Release Contract]]
  v0.2; consent-шаги и fail-closed поведение — по
  [[Consent Scope Registry]].
