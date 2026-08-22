---
node_id: ayla.strategy.mvp-scope-release-contract
title: Ayla MVP Scope and Release Contract
type: specification
status: draft
decision_status: proposed
canonical_status: candidate
version: "0.4"
owner: Product Owner
priority: P0
knowledge_area:
  - strategy
  - product
domain:
  - cross-domain
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
updated: 2026-08-17
review_cycle: monthly
depends_on:
  - "[[Ayla Product Essence]]"
  - "[[Ayla Living Digital Twin Manifesto]]"
  - "[[Ayla — Product Vision]]"
  - "[[Ayla MVP Product Thesis]]"
  - "[[Ayla Product Principles]]"
  - "[[Ayla Constitution]]"
  - "[[Ayla Decision Log]]"
  - "[[Ayla MVP Documentation Roadmap]]"
related:
  - "[[Killer PRD]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Consent Scope Registry]]"
  - "[[AMD-020 Pilot Scope Registry]]"
  - "[[Ayla MVP User Journey Specification]]"
supersedes: []
---

# Ayla MVP Scope and Release Contract v0.4

**Статус:** DRAFT / proposed / canonical candidate
**Версия:** 0.4
**Положение:** Foundation document №4 (Vision → Thesis → Principles →
**MVP Scope** → User Journey)
**Владелец:** Product Owner
**Revision mode:** TARGETED_AMENDMENT_FROM_OWNER_DECISIONS (OD-MVP-1…4)
**Artifact path and node identity:** preserved
(`02 Strategy/Ayla MVP Scope and Release Contract.md`,
`ayla.strategy.mvp-scope-release-contract`)
**Основание:** Owner Decisions OD-MVP-1…4 (`Ayla MVP v2 — Owner
Decisions`); Ayla Product Essence v1.2, Ayla — Product Vision v2.1, Ayla
MVP Product Thesis v0.6, Ayla Product Principles v0.2 (все candidates,
пока не прошли Product Owner Final Review)

> v0.3 не был canonical (draft/proposed/candidate). v0.4 — targeted
> amendment: обязательный Living Digital Twin critical path заменён на
> representation-neutral release composition (Goal → Everyday Signal →
> Context → Recommendation → Action → Memory → Progress); Food
> Intelligence и Memory Foundation введены как явные release capabilities.
> Artifact identity, path и history сохранены. Downstream-ссылки на
> разделы v0.3 (в т.ч. MVP User Journey Specification v1.2 §6.4
> MUST_HAVE-ссылки) **не считаются выровненными автоматически** — см. §14
> и итоговый отчёт канонизации. Документ не становится CANONICAL до
> internal consistency review, migration readiness review и отдельного
> owner approval.

## 1. Purpose and Release Contract Role

Этот документ отвечает на вопрос **«что входит в первый релиз»**: какие
capabilities и пользовательские результаты обязаны работать в MVP пилота,
а что явно отложено или исключено. Это release contract, а не roadmap:
он фиксирует границу релиза, а не план работ во времени.

Положение в потоке документов: MVP Scope работает между
[[Ayla MVP Product Thesis]] / [[Ayla Product Principles]] (проверяемая
гипотеза и неизменные нормы) и [[Ayla MVP User Journey Specification]]
(детализация пути пользователя). Он выбирает релизный состав в пределах
Principles и под составную гипотезу Thesis.

Этот документ **не** определяет:

- долгосрочное видение — [[Ayla — Product Vision]];
- проверяемую гипотезу и критерии её подтверждения — [[Ayla MVP Product Thesis]];
- неизменные продуктовые нормы — [[Ayla Product Principles]];
- пользовательский путь и состояния — [[Ayla MVP User Journey Specification]];
- техническую архитектуру, доменные схемы и API — Architecture/Domain-документы;
- UX-решения — UX-документы;
- числовые пороги и метрики — Measurement Framework (planned).

MVP Scope не доказывает Thesis целиком: он фиксирует минимальный релиз,
достаточный для её проверки (§3).

**Граница с AMD-020 (факт, AYLA-DEC-0014):** [[AMD-020 Pilot Scope Registry]]
владеет pilot/memory ownership (какие данные и память допустимы в пилоте);
настоящий документ владеет release scope capabilities (какие способности
продукта входят в релиз). Пересечения разрешаются в пользу более строгого
ограничения; изменение границы — через Change Control (§13).

## 2. Position in Canon

```text
Ayla Product Essence v1.2 (candidate) — высший продуктовый источник
├── Living Digital Twin Manifesto v1.0 — sibling / согласующий input (LDT-темы)
├── Product Vision v2.1 (candidate) — sibling
├── Product Thesis v0.6 (candidate) — sibling
├── Product Principles v0.2 (candidate) — sibling
└── MVP Scope (этот документ)
      ↓
User Journey → Domain → UX → Architecture → Engineering
```

- **[[Ayla Constitution]]** — hard constraints и боковой якорь; её статьи
  здесь не переписываются, а применяются как обязательные ограничения.
- **[[Ayla Product Essence]]** — высший продуктовый источник; при любом
  конфликте побеждает Essence.
- **[[Ayla Product Principles]]** — стабильные правила продуктовых решений;
  релизный состав выбирается в их пределах.
- **MVP Scope** — точная релизная граница первого выпуска.
- **[[Ayla MVP User Journey Specification]]** — downstream: раскрывает путь
  пользователя внутри утверждённого scope.
- **[[Killer PRD]]** — legacy reference only (CANON_INDEX): не является
  нормативным источником этого документа и не основа его структуры.

Этот документ не создаёт новую иерархию и находится ниже Essence v1.2;
Manifesto v1.1 — authoritative input для его LDT-положений, не родитель.

## 3. MVP Product Boundary

> **Изменено (v0.4, OD-MVP-1…4).** Composite formula заменена на
> representation-neutral value loop. Living Digital Twin baseline/
> recognition убраны из обязательного состава; Everyday Signal (Food
> Intelligence) и Memory Foundation введены как явные обязательные
> элементы.

MVP — минимальный релиз, который проверяет **составную продуктовую
ценность** ([[Ayla MVP Product Thesis]] §4.3):

```text
Transformation Goal
+
Everyday Signal (Food Intelligence — первая реализация)
+
Context Understanding
+
Explainable Recommendation
+
Realistic Action
+
Memory Continuity
+
Goal-relative Progress
```

Ни один элемент отдельно не является целью релиза; проверяется их
сочетание. Память — механизм continuity внутри составного пути, а не
центр продукта и не самостоятельная цель MVP. Living Digital Twin не
входит в обязательный состав (OD-MVP-1): если он включён в конкретный
релиз, он усиливает `Context / State / Progress` как опциональный
representation layer (§6.4).

Явные границы:

- MVP — **не booking flow**: запись — одно из downstream-действий плана
  ([[Ayla Product Essence]] §20; [[Ayla Product Principles]] 4.7);
- **не набор disconnected trackers**: питание, вода, сон, активность —
  инструменты пути к цели, не самостоятельные центры продукта; Food
  Intelligence — первая реализация `Everyday Signal`, не self-contained
  calorie-tracking продукт (OD-MVP-2);
- **не полный marketplace**: только seed-контур пилотных провайдеров;
- **не обязателен Living Digital Twin**: LDT — опциональная стратегическая
  capability (OD-MVP-1; §6.4); если включён — проверяется его
  жизнеспособность (viability), не полная модель;
- **не medical product**: медицинская диагностика и выводы о здоровье
  запрещены ([[Ayla Constitution]] Ст. XII); food/behavioral-сигналы не
  становятся медицинским фактом (Observation ≠ Fact; Principles 4.4, 4.12);
- **не long-term personalization platform**: Memory Foundation входит в
  MVP с начала, но проверяется минимально полезная continuity через
  progressive lifecycle (working context → memory candidate → policy/
  consent gate → persistent memory), а не полная платформа персонализации
  (OD-MVP-3; Principles 4.5);
- **«ничего не делать» — валидный outcome** рекомендации
  ([[Ayla — Product Vision]] §19; Principles 4.6);
- **economic neutrality обязательна**: коммерческий статус, тариф или
  платёж провайдера никогда не влияют на персональные рекомендации
  (Constitution Ст. IV; Principles 4.10).

**Пилотная граница (факт, без дублирования Thesis):** территория пилота —
Пенза (дата пилота — AYLA-DEC-0003); клиентская сторона — пользователи в
предметной области [[Ayla Constitution]] Ст. I, находящиеся в зоне охвата
пилотных провайдеров ([[Ayla MVP Product Thesis]] §5); начальный
provider-профиль — соло-мастер и малый салон до 3 мастеров; персоны пилота
— по owner direction 2026-07-27 (клиент, ищущий услугу или специалиста;
соло-мастер; малый салон до трёх мастеров): новые персоны не вводятся,
детальные нарративы персон здесь не пересказываются.

## 4. Primary End-to-End Journey

> **Изменено (v0.4, OD-MVP-1, OD-MVP-2).** Twin baseline/recognition
> переведены из OBLIGATORY в CONDITIONAL (только если LDT включён в
> релиз). Добавлен обязательный шаг Everyday Signal / Food Intelligence.

Единственный обязательный сквозной сценарий MVP — путь вокруг цели и
видимого прогресса, а не цепочка «запрос → запись»:

```text
1.  Пользователь формулирует или уточняет Transformation Goal   — OBLIGATORY
2.  Пользователь предоставляет минимальные разрешённые inputs   — OBLIGATORY
2a. Ayla получает Everyday Signal (Food Intelligence — первая
    реализация) и связывает его с контекстом цели                — OBLIGATORY
3.  Ayla создаёт или подтверждает Twin baseline                 — CONDITIONAL (только если LDT включён в релиз)
4.  Пользователь узнаёт себя или исправляет Twin                — CONDITIONAL (только если LDT включён в релиз)
5.  Ayla интерпретирует intent в контексте                      — OBLIGATORY
6.  Ayla формирует объяснимую рекомендацию                      — OBLIGATORY
7.  Пользователь выбирает реалистичный следующий шаг             — OBLIGATORY
8.  Запись может произойти как одна из downstream-опций         — OPTIONAL
9.  Результат / follow-up становится continuity input           — PARTIAL
10. Пользователь видит прогресс или следующее состояние         — OBLIGATORY (минимальная форма)
```

Обязательные условия сценария:

- **Consent gates** действуют на входных данных (шаг 2), Signal-данных
  (шаг 2a), media при включённом LDT (шаг 3) и персистентной памяти
  (шаг 9) — по [[Consent Scope Registry]] §10;
- **Observation ≠ confirmed fact** (шаг 2a): Food/Signal-наблюдение не
  становится автоматически подтверждённым или медицинским фактом
  (Principles 4.4, 4.12);
- **recognition point обязательна только при включённом LDT** (шаг 4):
  если Twin включён в релиз, сигнал «это не похоже на меня» и
  исправление/перестроение Twin — часть сценария, не опция; если Twin не
  включён, шаги 3–4 не применяются и не блокируют сценарий;
- **Phase 1 — session-only memory**; **Phase 2 — opt-in persistent
  memory**; Phase 2 не является условием релиза Phase 1;
- **booking optional** (шаг 8): сценарий не обязан завершаться записью;
  отказ от действия — допустимый исход (шаг 7);
- **journey заканчивается прогрессом / следующим состоянием** (шаг 10),
  а не подтверждением записи.

Детализация сценария до этапов, негативных веток и owning capability —
задача MVP User Journey, не этого документа.

## 5. In-Scope User Outcomes

> **Изменено (v0.4, OD-MVP-1, OD-MVP-2).** Twin baseline/recognition
> переведены в conditional outcome (только при включённом LDT); добавлен
> обязательный outcome для Everyday Signal.

MVP обязан обеспечить следующие пользовательские результаты
(outcome-level, без CAP-first framing и без числовых порогов):

1. личная Transformation Goal установлена или уточнена;
2. Everyday Signal получен и связан с контекстом цели (Food Intelligence —
   первая реализация; observation отделено от подтверждённого факта);
3. intent понят в контексте пользователя;
4. рекомендация объяснена (что, почему, на каких данных, с какой
   неопределённостью);
5. реалистичный следующий шаг выбран — включая обоснованное «ничего не
   делать»;
6. booking возможен как downstream action;
7. прогресс / следующее состояние видимы (сравнение состояний во времени
   или другое понятное representation);
8. разрешённый continuity context сохраняется через progressive memory
   lifecycle и используется в повторном пути;
9. user control реализуем на практике: просмотр, исправление, удаление,
   отзыв согласия.

**Conditional (только если Living Digital Twin включён в релиз):**

10. Twin baseline создан на разрешённых данных;
11. пользователь узнаёт себя в Twin или исправляет его.

## 6. In-Scope Capabilities

Маппинг на Capability ID ([[Ayla Domain Capability Registry]] §6) остаётся
**proposal** до перевода записей реестра в MVP-active (волна 2,
AYLA-DEC-0014) и не является canonical activation. Новые области
(Transformation Goal, Living Digital Twin) получают CAP-маппинг только
через ту же волну 2, не этим документом.

### 6.1 Client-facing

> **Изменено (v0.4, OD-MVP-1, OD-MVP-2, OD-MVP-3).** Twin baseline/
> recognition/correction переведены в CONDITIONAL блок. Food Intelligence
> introduction и Memory Foundation добавлены как явные IN_SCOPE
> capabilities.

- Transformation Goal creation / refinement (минимальная структура цели;
  детальная модель — Domain);
- минимальные разрешённые inputs (progressive profiling, Constitution
  Ст. VI);
- **Food Intelligence (OD-MVP-2)** — приём food input, включая фото;
  распознавание; пользовательская коррекция существенной ошибки
  распознавания; связывание наблюдения с Transformation Goal как
  разрешённого контекста рекомендаций; наблюдение может стать memory
  candidate. Не входит автоматически: полноценный дневник питания, точный
  calorie tracking, обязательный подсчёт БЖУ, диетические программы,
  медицинские выводы (Observation ≠ medical fact);
- **Memory Foundation (OD-MVP-3)** — working/session context; различие
  observation и confirmed fact; memory candidates; policy/consent gate;
  Phase 2 opt-in persistent memory; explainability сохранённого контекста,
  влияющего на рекомендацию (детали — §6.3);
- intent conversation (минимальный набор intent types, proposal CAP-003);
- объяснимая рекомендация (proposal CAP-004 + CAP-005);
- выбор следующего действия;
- booking / reschedule / cancel как опция (proposal CAP-011): same-ID
  time-only reschedule (Wave 1, Simple Reschedule) — accepted
  (AYLA-DEC-0022 п. 9, Domain Event Registry v0.4, `appointment.rescheduled`
  registered); полная cancellation journey, replacement, change
  specialist/service, re-offer — остаются deferred (AYLA-DEC-0022,
  owner ruling 2026-07-28, вариант Б);
- транзакционные уведомления (proposal CAP-021);
- видимый прогресс относительно цели (сравнение состояний во времени или
  другое понятное representation — §6.4);
- контроль данных, memory и персонализации.

**Conditional (только если Living Digital Twin включён в релиз, OD-MVP-1):**

- управляемая фотофиксация и Twin baseline;
- recognition / correction Twin.

**Канальное распределение (факт, AYLA-DEC-0027):** client-facing
capabilities распределяются по owning channels: **Mobile App** —
primary/full experience для Living Digital Twin, photo capture, прогресса,
истории, контроля данных и longitudinal interaction; **MAX Mini App** —
lightweight embedded experience для статуса цели, рекомендации, booking,
быстрого check-in и продолжения пути; **MAX Bot** — диалог, уточнения,
объяснения, напоминания, транзакционные уведомления, быстрые действия и
маршрутизация. Полная feature parity между каналами не требуется;
capability обязана быть доступна в назначенном owning channel (§8).
Полная channel capability matrix принадлежит execution/UX-документам и
здесь не фиксируется.

**Wellness inputs — статусы:**

| Input | Статус |
|---|---|
| food | IN_SCOPE (v0.4, OD-MVP-2) — первая конкретная реализация Everyday Signal: приём input/фото, распознавание, пользовательская коррекция, связывание с Transformation Goal как разрешённого контекста рекомендаций; dedicated full food diary/точный calorie tracking — DEFERRED; один из равнозначных trigger-сценариев (Vision §10, AYLA-DEC-0028) |
| water | DEFERRED |
| sleep | DEFERRED |
| mood | DEFERRED; без inferred mental state (Constitution Ст. X) |
| symptoms | OUT_OF_SCOPE |
| activity / body signals | DEFERRED |
| photos | CONDITIONAL (v0.4) — управляемая фотофиксация для Twin baseline только если LDT включён в релиз (OD-MVP-1); особо чувствительный input, где применяется — Manifesto §12 |
| manual notes | CONDITIONAL (минимальный пользовательский ввод фактов — whitelist personal context) |
| conversation-derived context | IN_SCOPE в пределах consent; с разделением классов достоверности |

Медицинские выводы (medical inference) не вводятся ни для одного input.

### 6.2 Provider-facing

- минимальный профиль провайдера (proposal CAP-009);
- пилотные профили: соло-мастер и малый салон до 3 мастеров
  ([[Ayla MVP Product Thesis]] §5);
- актуальные слоты availability (proposal CAP-010);
- provider-side monetary boundary (§7 не активирует полный Payment);
- eligibility gate;
- подтверждение записи;
- минимальная reconciliation с платёжным провайдером.

Не включать: глубокую верификацию провайдеров, payouts, крупные сети и
франшизы, сложное управление персоналом.

### 6.3 AI / Orchestration / Memory

- intent understanding;
- recommendation formation (primary + alternatives; без продвинутого ML
  ranking);
- explanation — обязательно (Constitution Ст. VII);
- минимальная tool orchestration сквозного сценария (proposal CAP-018);
- session memory (Phase 1);
- opt-in persistent memory — только после Phase 2 gate (Consent Scope
  Registry §10);
- model/provider fallback — как NFR (§10);
- prompt/tool version traceability;
- attribution — IN_SCOPE как минимальный direct linkage: `recommendation_id`
  → выбранное действие; `booking_id` / `appointment_id` привязываются только
  если booking произошёл (proposal CAP-013). Assisted attribution, cohort
  models, multi-touch attribution и advanced windows — DEFERRED,
  Measurement Framework (§11).

Memory-first framing запрещён: память поддерживает составной путь
(memory supports composite journey); объём сохранённых фактов не является
целью и не admission metric ([[Ayla MVP Product Thesis]] §8.2).

### 6.4 Living Digital Twin

> **Изменено (v0.4, OD-MVP-1).** Living Digital Twin переведён из
> обязательной MVP capability в опциональную/DEFERRED-по-умолчанию
> capability. MVP как таковой не обязан проверять жизнеспособность LDT.
> Если Product Owner отдельным решением включает LDT в конкретный релиз,
> действуют требования ниже без ослаблений — они остаются
> нормативными для этого сценария.

Living Digital Twin **не входит в обязательный состав первого MVP**
(Essence v1.2 §18; Thesis v0.6 §6; Principles v0.2 4.3, 4.14). Если LDT
включён в релиз отдельным решением, MVP обязан обеспечить минимально
достаточный контроль и доверие ([[Ayla Living Digital Twin Manifesto]]
§14):

| Класс | Состав |
|---|---|
| MUST_HAVE, если LDT включён | управляемая фотофиксация; baseline; recognition («это я»); сигнал «это не похоже на меня»; исправление/перестроение модели; сохранение идентичности между версиями (identity drift — дефект); сравнение состояний во времени; разделение факта, реконструкции, прогноза и цели; body dignity и anti-shaming; удаление исходных и производных данных |
| SHOULD_HAVE, если LDT включён | отображение уверенности в поддерживаемой форме (не обязательные проценты); объяснение ограничений модели |
| CONDITIONAL | видео — только при подтверждённой необходимости для качества модели, и только если LDT включён |
| DEFERRED (по умолчанию, v0.4) | включение Living Digital Twin в MVP как таковое остаётся deferred до отдельного owner decision (OD-MVP-1: критерий возвращения — доказуемое улучшение понимания пользователя, рекомендаций или прогресса); более богатая Living Timeline; более глубокая персонализация; более объяснимые прогнозы (Manifesto §15) — если/когда LDT включён |
| OUT_OF_SCOPE | full morphing engine; идеализированное будущее тело; medical simulation; medical-grade reconstruction; неподдержанный/гарантированный прогноз (в т.ч. 30/60/90 дней); произвольная генерация аватаров; точный состав тела по камере; автоматическое обновление Twin после каждого действия |

### 6.5 Safety / Consent / Control

- детерминированные safety gates ко всем product capabilities
  (mandatory cross-cutting, proposal CAP-014);
- consent management — только scopes, необходимые Phase 1/2
  (proposal CAP-002; [[Consent Scope Registry]] §10);
- purpose limitation: данные используются только для информированных
  целей;
- session-only default до Phase 2 gate;
- просмотр, исправление, удаление, отзыв согласия пользователем;
- удаление исходных и производных данных;
- аудит критических событий (consent, authorization, booking, safety —
  proposal CAP-026);
- запрет автономных действий без подтверждения пользователя;
- запрет скрытой медицинской диагностики (Constitution Ст. X);
- body dignity / anti-shaming (Manifesto §13).

### 6.6 Enabling / Operations

Сохраняются валидные enabling capabilities v0.2 (AYLA-DEC-0015):

- AI Orchestration and Tool Execution (proposal CAP-018,
  `user_visible_capability: false`, `mvp_scope: required`);
- Audit and Observability (proposal CAP-026, `mandatory-cross-cutting`);
- Identity and Access — ограниченный срез Master MVP (auth/session/tenant
  + authority/permission policy; CAP-019 MVP-active; AYLA-DEC-0016;
  AYLA-DEC-0017 п. 11; [[Ayla Master MVP Auth and Authority Contract]]);
- минимальный provider monetary integration (CAP-022 MVP-active только в
  части §7 monetary boundary);
- backend как SoR для каталога, провайдеров, availability, записей,
  consent и context facts;
- поддержка seed catalog / provider / availability.

## 7. Explicitly Out of Scope / Deferred

**OUT_OF_SCOPE (исключено из MVP):**

- клиентская онлайн-оплата услуг;
- wallet и внутренний баланс;
- payouts;
- refunds;
- chargebacks;
- универсальный split settlement;
- полноценный financial ledger;
- полный marketplace и расширенный marketplace search (CAP-024);
- multi-tenant customization (CAP-020);
- medical/health inference и автоматические выводы о здоровье
  (CAP-006 в этой части);
- admin tooling;
- Telegram как канал (AYLA-DEC-0004);
- поддержка крупных сетей и франшиз;
- полный LDT morphing и гарантированный прогноз будущей внешности (§6.4).

**DEFERRED (отложено, не исключено навсегда):**

- полноценный Payment Processing (CAP-023; в MVP — только provider-side
  monetary boundary ниже);
- полноценный Billing сверх monetary boundary;
- advanced Outcome Learning (CAP-007);
- сложная Experimentation Platform (CAP-025);
- продвинутый ML ranking;
- dedicated wellness-трекеры (food/water/sleep/activity — §6.1);
- глубокая provider verification;
- внутренний баланс провайдера с выводом T+24ч (эпик этапа 2,
  AYLA-DEC-0008);
- richer Living Timeline, advanced forecasts, deeper personalization
  (Manifesto §15);
- **Living Digital Twin как обязательная MVP capability (v0.4, OD-MVP-1)**
  — deferred до отдельного owner decision о включении в конкретный релиз;
  не удалён из продукта и не признан ошибочной концепцией (Essence v1.2
  §6, §18).

**MVP Provider Monetary Boundary (факт, AYLA-DEC-0015):** в MVP входит
ограниченный денежный контур провайдера — списание подписки; списание
booking fee 90 ₽; обработка результата попытки списания; обновление
billing status; применение eligibility gate; минимальная reconciliation с
YooKassa. Этот контур **не означает активацию CAP-023 Payment Processing**
и не создаёт универсальный payment domain.

## 8. Channels and Deployment Boundary

**Required MVP channel set (факт, AYLA-DEC-0027):**

1. **Mobile App** — REQUIRED / primary product experience: полная визуальная
   и longitudinal experience (Living Digital Twin, photo capture, прогресс,
   история, контроль данных);
2. **MAX Mini App** — REQUIRED / lightweight embedded companion;
3. **MAX Bot** — REQUIRED / conversational, notification and routing
   companion.

Обязательные условия:

- три канала — один продукт, а не три отдельных продукта; все три работают
  поверх единого backend и domain model;
- едины identity, consent, safety, recommendation state, memory boundary,
  attribution и analytics;
- **feature parity across channels — NOT_REQUIRED**; capability обязана
  быть доступна в назначенном owning channel;
- **shared product state — REQUIRED**; cross-channel continuity обязательна;
- реальный pilot release требует доступности всех трёх required channels;
  internal smoke test может использовать pre-release/internal distribution;
- **Telegram** — вне пилотного scope (AYLA-DEC-0004, Thesis §7);
- универсальная multi-channel спецификация не требуется для MVP.

## 9. Dependencies and External Systems

- **MAX platform** — канал пилота (AYLA-DEC-0004);
- **Backend API** — SoR для каталога, провайдеров, availability, записей,
  consent и context facts;
- **ayla-ai-core** — библиотека reusable AI logic; **ai-bot-platform** —
  runtime/channel consumer (рекомендуемая MVP-композиция; backend
  допустим как модульный монолит);
- **LLM provider** — через provider abstraction ayla-ai-core; определён
  model/provider fallback;
- **YooKassa** — обязательная интеграция только для provider-side
  monetary flow (§7); клиентская оплата и полноценный Payment Processing
  остаются вне MVP (AYLA-DEC-0015);
- **LDT media pipeline (CONDITIONAL, v0.4)** — downstream architecture
  dependency для Twin baseline и фотофиксации, применяется только если
  LDT включён в релиз (§6.4, OD-MVP-1); техническая граница реализации
  определяется в Architecture-документах и здесь не фиксируется (§15);
- **Mobile application distribution infrastructure** — internal testing /
  closed distribution / store publication path; конкретный mobile store не
  фиксируется как единственный канал распространения (AYLA-DEC-0027);
- **Deep links / universal links** — обязательны для channel routing, где
  поддерживаются платформой;
- **Push notifications** — mobile dependency для mobile-owned уведомлений;
- **Cross-channel account linking** — обязательная зависимость единой
  идентичности пользователя между Mobile App, MAX Mini App и MAX Bot;
- **Shared API contract** — единый контракт для всех трёх required channels;
  channel-specific backend rules не создаются.

## 10. Non-Functional Requirements

Минимум, обязательный к релизу:

- **Security:** access control; tenant isolation; управление secrets;
  логирование без PII; rate limits; audit; backup;
- **Privacy:** по умолчанию режим [[Consent Scope Registry]] §10 — session
  context only, no proactive recommendations, no cross-domain
  personalization, no persistent inferred signals, no persistent
  preference storage — до выполнения gate Phase 2;
- **AI:** закреплённые версии prompt; совместимые tool schemas; token
  budget; протестированные hallucination-сценарии; определённый
  model/provider fallback; prompt/tool version traceability;
- **Everyday Signal / Memory (v0.4):** observation отделено от
  подтверждённого факта; food-сигнал не становится медицинским выводом;
  memory candidate проходит policy/consent gate перед persistent записью;
- **Living Digital Twin (CONDITIONAL — только если включён в релиз,
  OD-MVP-1):** recognition/correction поддерживаются продуктово; identity
  preservation между версиями; честное разделение факта, реконструкции,
  оценки, прогноза и цели; body dignity; удаление исходных и производных
  данных;
- **Explainability:** существенная рекомендация объяснима и трассируема к
  структурированным причинам (Constitution Ст. VII);
- **Operations:** monitoring; alerts; support process; назначенный
  incident owner; возможность rollback; feature flags;
- **Product:** primary journey (§4) работает end-to-end; fallback
  существует; критических тупиков нет;
- **Channels (AYLA-DEC-0027):** cross-channel identity consistency;
  cross-channel consent consistency; shared recommendation state;
  отсутствие дублированной автономной business logic в клиентах; deep-link
  fallback; channel-aware observability; mobile crash/error telemetry;
  rollback и feature flags по каналам; secure local storage для mobile;
  media permission handling.

Числовые SLA и пороги производительности в этом документе не
устанавливаются. Implementation details определяются в
Architecture/Engineering-документах.

## 11. Measurement and Release Evidence

MVP Scope фиксирует только **release evidence** — какие факты должны быть
наблюдаемы в пилоте, чтобы составная ценность (§3) считалась проверенной
качественно. Числовые пороги, cohorts, retention-аналитика и advanced
attribution принадлежат Measurement Framework (planned) и здесь не
вводятся (Thesis §8.1: пороги — design candidates).

> **Изменено (v0.4, OD-MVP-1, OD-MVP-2).** Twin baseline/recognition
> переведены в conditional evidence; добавлен обязательный Everyday
> Signal evidence.

Release evidence минимум:

- goal established — пользователь сформулировал/уточнил Transformation
  Goal;
- everyday signal captured — Food Intelligence input получен, распознан и
  при необходимости скорректирован пользователем; наблюдение связано с
  Transformation Goal;
- recommendation explained;
- next action accepted/rejected — включая валидный исход «ничего не
  делать»;
- booking — **secondary downstream evidence** (conversion/completion
  фиксируются, но не являются центральной метрикой MVP);
- continuity retained where consented — повторное обращение без повторного
  объяснения контекста (в пределах Phase 1/2 режима);
- user control exercised — просмотр/исправление/удаление/отзыв;
- safety blocks; tool failures; usefulness feedback;
- channel continuity (AYLA-DEC-0027) — account linking completed;
  cross-channel state preserved; consent state consistent;
  recommendation/result continuity preserved; channel source captured;
  deep-link/route outcome captured; mobile-owned progress path observable
  (LDT/photo path observable дополнительно, только если LDT включён в
  релиз); bot/Mini App companion path observable.

Диагностический минимум пилота (resolved intents, clarification rate,
recommendation shown/acceptance rate, rejection reasons, unsafe block
rate, tool failure rate, median response time) сохраняется из v0.2 как
техническая телеметрия релиза; критерии подтверждения/опровержения
гипотезы — [[Ayla MVP Product Thesis]] §8.1/§8.2 и Product Thesis
Validation Gate §8.4.

## 12. Release Gates and Blockers

| Элемент | Статус |
|---|---|
| OD-K11 (`canonical_status` в schema) | RESOLVED / NOT_A_BLOCKER |
| Data Inventory Matrix | RESOLVED / NOT_A_BLOCKER (exists draft v1.0; зависимость AMD-020 разрешена — Thesis §9) |
| Killer PRD | LEGACY_REFERENCE_ONLY / NOT_A_BLOCKER (его canonical approval заблокирован ADR-0012 OD-1/OD-2 — это блокер downstream approvals самого Killer PRD, не этого документа) |
| Consent Scope Registry §10 gates | ACTIVE — Phase 1: scopes `intent_understanding` и `provider_selection` approved, persistent memory технически отключена; Phase 2 gate — по Registry §10.2 |
| Safety/privacy review | ACTIVE — обязателен при approval этого документа |
| LDT media pipeline feasibility | NOT_A_BLOCKER_FOR_MVP (v0.4, OD-MVP-1) — применяется только если LDT отдельно включён в релиз; тогда REQUIRES_REVALIDATION на этапе Architecture (§9, §15) |
| Recognition quality bar | NOT_A_BLOCKER_FOR_MVP (v0.4, OD-MVP-1) — применяется только если LDT отдельно включён в релиз |
| Provider supply readiness | OPERATIONS_DEPENDENCY / NOT_DOCUMENT_BLOCKER (операционный трек пилота, AYLA-DEC-0003) |
| User Journey v1.2 alignment с OD-MVP-1…4 | ACTIVE / REQUIRED — Journey v1.2 содержит MUST_HAVE-ссылки на §6.4 Twin-требования этого документа (её собственные AYLA-DEC-0037…0054), которые устаревают после v0.4; alignment pass зарегистрирован как отдельный follow-up gate (см. итоговый отчёт канонизации), не блокирует канонизацию этого документа, но блокирует downstream-согласованность до выполнения |
| Mobile channel readiness | ACTIVE / REQUIRED (AYLA-DEC-0027) — internal/closed mobile distribution validated; account linking; deep links; push path where required; crash monitoring; privacy/safety review для camera/media/local storage; store review/publication timing отслеживается как operational dependency и не является абсолютным blocker для internal testing |

Resolved-элементы не сохраняются в статусе blockers. Governance Exit фазы
MVP (Thesis §8.4): решение о переходе фазы принимает Product Owner и не
является автоматическим.

**Предусловия approval и канонизации:** до Product Owner approval и
канонизации этого документа обязательны: (1) Internal Consistency Review;
(2) Migration Readiness Review; (3) Product Architecture review —
подтверждение scope-to-capability alignment и proposal CAP-маппинга;
(4) Privacy/Safety review — подтверждение активных gates; (5) завершённая
обязательная downstream migration (§14); (6) Product Owner Final Review.

## 13. Admission and Change Control

**Admission test (составной, заменяет memory-first фильтр v0.2):**
функция входит в MVP, только если она:

1. вносит проверяемый вклад в составную гипотезу (Thesis §4.3);
2. не нарушает [[Ayla Product Principles]] (4.1–4.11);
3. необходима именно для релиза (release necessity, а не «полезна
   вообще»);
4. сохраняет объяснимость (Constitution Ст. VII);
5. сохраняет user control и consent boundaries;
6. не нарушает economic neutrality (Constitution Ст. IV);
7. корректно позиционирована (booking и транзакции — downstream, не
   центр);
8. имеет измеримый release evidence (§11).

Функция, нарушающая любую строку таблицы MVP-принципов Thesis §8.3, не
проходит admission независимо от пункта 1 (автоматический отказ).

**Критическое правило (дословно, Roadmap §1.4 и AYLA-DEC-0014):** после
approval любое расширение Included Scope требует owner decision с
указанием:

- зачем оно нужно до MVP;
- какой срок добавляет;
- какую текущую задачу вытесняет.

Сокращение Included Scope или уточнение формулировок без расширения
фиксируется записью в Change Log этого документа и записью в
[[Ayla Decision Log]].

## 14. Downstream Migration Contract

По owner decision OD-MS-3 (PATH_STABILITY_WITH_COORDINATED_MIGRATION):

- artifact path, title, node identity и version history сохранены;
- нумерация и семантика разделов v0.3 могут отличаться от v0.2, где это
  требуется текущим каноном;
- downstream-ссылки на разделы v0.2 **не считаются выровненными
  автоматически**;
- coordinated migration **обязательна** и должна завершиться до
  канонизации этого документа;
- owner review следует после structured revision и migration readiness
  review.

Migration matrix (миграция выполняется отдельными pass, не этим
документом):

```text
Ayla MVP User Journey Specification   — ссылки на §3/§4/§11 v0.2; Foundation №5, LDT-alignment
Ayla Intent Model Specification       — ссылки на §3/§4.1/§4.2/§5 v0.2
Ayla Core Domain Model Specification  — ссылки на §4/§5/§11 v0.2 (включая change control)
Ayla MVP Recommendation Contract      — depends_on и scope-якорь
ADR-0013 Recommendation Snapshot      — ссылки на §4.1 п. 9, 11 v0.2
UX MVP source index                   — ссылка на «v0.3» и неканонический path
draft privacy-consent mapping         — ссылки на «v0.3» §8/§10
recommendation UX addendum            — ссылки на §4.1 п. 2, 9, 11 v0.2
SCR-CUST-004                          — ссылка на §4.1 п. 9 v0.2
intent-registry.yaml                  — comment-ссылка на §4 v0.2 (non-normative)
Ayla.md MOC                           — статусная таблица (v0.2)
mobile navigation specification       — TO_BE_CREATED (downstream migration item, AYLA-DEC-0027)
mobile deep-link contract             — TO_BE_CREATED (downstream migration item, AYLA-DEC-0027)
mobile authentication/account-linking flow — TO_BE_CREATED (downstream migration item, AYLA-DEC-0027)
push notification contract            — TO_BE_CREATED (downstream migration item, AYLA-DEC-0027)
mobile privacy/media consent mapping  — TO_BE_CREATED (downstream migration item, AYLA-DEC-0027)
channel capability matrix             — TO_BE_CREATED (execution/UX artifact, AYLA-DEC-0027)
mobile UX source index                — TO_BE_CREATED (downstream migration item, AYLA-DEC-0027)
Ayla Single-Provider Technical Pilot Execution Scope — CREATED / EDITORIAL_CLEANUP_COMPLETE / TARGETED_REVIEW_REQUIRED
Ayla Multi-Provider Product Validation Execution Scope — CREATED / EDITORIAL_CLEANUP_COMPLETE / TARGETED_REVIEW_REQUIRED
```

Артефакты, помеченные TO_BE_CREATED, не существуют в репозитории на момент
этой ревизии и зарегистрированы как downstream migration items по
AYLA-DEC-0027; их создание — часть coordinated migration и execution/UX
работ, не этого документа.

## 15. Open Questions

Только реальные non-blocking вопросы; новые owner decisions этот документ
не создаёт:

- **CAP mapping для Transformation Goal и LDT (KEEP_NON_BLOCKING).**
  Новые области получают Capability-маппинг в волне 2 перевода Registry в
  MVP-active (AYLA-DEC-0014), а не в этом документе.
- **Exact recognition quality bar (KEEP_NON_BLOCKING, CONDITIONAL v0.4).**
  Применяется только если LDT включён в релиз (OD-MVP-1). Принцип
  узнаваемости канонизирован (Manifesto §5); измерение — downstream
  AI/Measurement.
- **Exact LDT media pipeline implementation boundary (KEEP_NON_BLOCKING,
  CONDITIONAL v0.4).** Применяется только если LDT включён в релиз.
  Architecture topic; здесь зафиксирована только зависимость (§9).
- **Living Digital Twin re-admission to MVP (NEW, v0.4, KEEP_NON_BLOCKING).**
  Owner decision о включении LDT в конкретный релиз может быть принят
  отдельно по мере появления доказательств (OD-MVP-1: критерий
  возвращения). Не блокирует канонизацию этого документа.
- **Числовые пороги release evidence (KEEP_NON_BLOCKING).** Принадлежат
  Measurement Framework (Thesis §8.1, §10).
- **Post-MVP wellness trackers (KEEP_NON_BLOCKING).** Возврат dedicated
  food/water/sleep/activity трекеров — отдельное scope-решение после
  пилота.
- **Exact mobile distribution route for pilot (KEEP_NON_BLOCKING).**
  Маршрут распространения (internal testing / closed distribution / store
  publication) определяется операционно; store как единственный канал не
  фиксируется (§9).
- **Exact store publication timing (KEEP_NON_BLOCKING).** Release
  dependency, отслеживается как operational dependency (§12); не blocker
  для internal testing.
- **Exact feature ownership details by channel (KEEP_NON_BLOCKING).**
  Детальная channel capability matrix принадлежит execution/UX-документам
  (§6.1, §14); implementation-level вопрос, нового owner decision не
  требует.
- **Exact deep-link fallback behavior (KEEP_NON_BLOCKING).**
  Implementation-level поведение определяется в Architecture/UX-документах;
  требование fallback зафиксировано как NFR (§10).

## Change Log

> Этот журнал отражает историю изменений документа и не является
> нормативной частью спецификации. Нормативным считается текущее состояние
> разделов 1–15, а не записи ниже.

### v0.4 (2026-08-07) — Targeted amendment: release composition per OD-MVP-1…4

Выполнено как часть канонизации Owner Decisions OD-MVP-1…4 (`Ayla MVP v2 —
Owner Decisions`), после Product Essence v1.2, Product Vision v2.1, Product
Thesis v0.6 и Product Principles v0.2 (все candidates). Amendment plans
Essence/Thesis/Principles рекомендуют этот шаг как следующий в
canonization sequence.

- **OD-MVP-1 (Living Digital Twin):** LDT переведён из обязательной MVP
  capability в опциональную/DEFERRED-по-умолчанию. §3 composite formula,
  §4 Primary Journey (шаги 3–4), §5 User Outcomes (10–11), §6.1, §6.4, §10
  NFR, §11 release evidence и §12 gates (LDT media pipeline feasibility,
  Recognition quality bar) переведены в CONDITIONAL — применяются только
  если LDT отдельно включён в релиз owner decision. LDT-требования
  (Manifesto, Essence §18) не ослаблены для сценария, когда LDT включён.
- **OD-MVP-2 (Food Intelligence):** введён как явная IN_SCOPE capability
  §6.1 «Food Intelligence»; wellness inputs таблица (§6.1) обновлена: food
  — IN_SCOPE вместо CONDITIONAL. §3, §4 (новый шаг 2a), §5 (новый outcome
  2), §11 (новое release evidence) обновлены.
- **OD-MVP-3 (Memory Foundation):** введена как явная IN_SCOPE capability
  §6.1 «Memory Foundation» с progressive lifecycle (working context →
  memory candidate → policy/consent gate → persistent memory). §10 NFR
  дополнен Everyday Signal/Memory блоком.
- **OD-MVP-4 (MVP hypothesis):** §3 composite formula заменена на
  representation-neutral `Goal → Everyday Signal → Context →
  Recommendation → Action → Memory → Progress`, согласованную с Thesis
  v0.6 §4.3.
- **§2** — обновлены версии parent-документов (Essence v1.2, Vision v2.1,
  Thesis v0.6, Principles v0.2).
- **§7** — добавлена явная DEFERRED-запись для LDT как обязательной MVP
  capability.
- **§15** — LDT-specific open questions переведены в CONDITIONAL; добавлен
  вопрос о будущем re-admission LDT.
- **MUST_UPDATE_NOW downstream finding (не выполняется этим документом):**
  `Ayla MVP User Journey Specification v1.2` §6.3, §6.4-ссылки и Event
  Usage Summary содержат MUST_HAVE-привязки к прежнему §6.4 этого
  документа (Twin baseline/recognition как обязательные experience
  points) и собственный набор owner decisions AYLA-DEC-0037…0054
  (2026-08-04). Эти привязки требуют alignment pass с OD-MVP-1…4; pass
  зарегистрирован как отдельный follow-up gate (см. итоговый отчёт
  канонизации), а не выполнен в рамках этого amendment — редактирование
  документа с собственным недавним owner decision session без отдельного
  рассмотрения было признано избыточным риском для этой канонизации.
- **Не изменено:** §6.2 (Provider-facing), §6.3 (AI/Orchestration —
  memory-first framing уже был запрещён в v0.3), §6.5, §6.6, §8, §9, §13,
  §14 сохранены без стилистической правки; монетизация, каналы (AYLA-DEC-
  0027), geography/provider-профиль пилота не затронуты.
- **Metadata:** version 0.3 → 0.4; updated 2026-08-02 → 2026-08-07.
  `decision_status: proposed` и `canonical_status: candidate` сохранены
  (документ не был CANONICAL и до этого amendment).
- **Next gate:** Internal Consistency Review, Migration Readiness Review
  (§14, дополненный User Journey alignment finding выше), Product Owner
  Final Review.

### v0.3 (2026-08-02) — Wave 1 Simple Reschedule §6.1 alignment

Targeted editorial sync: no scope change, no owner decision, no version
bump, no canonical status change.

- **§6.1** — уточнена формулировка "booking / reschedule / cancel как
  опция": same-ID time-only reschedule (Wave 1, Simple Reschedule) —
  accepted (AYLA-DEC-0022 п. 9, DER v0.4); полная cancellation journey,
  replacement, change specialist/service, re-offer — deferred. Устранена
  асимметрия детализации с [[Ayla MVP User Journey Specification]] §16 и
  [[Ayla MVP Appointment Contract]] §14, где это разграничение уже было
  зафиксировано.

### v0.3 (2026-07-31) — Execution scope artifacts added to migration matrix

Выполнено в Two-Phase Pilot Scope Reconciliation Window по промпту
`TWO_PHASE_PILOT_COMBINED_EDITORIAL_CLEANUP_PROMPT.md` (finding CD-P3-03).

- **§14** — migration matrix дополнена двумя созданными downstream
  execution artifacts: Ayla Single-Provider Technical Pilot Execution Scope
  и Ayla Multi-Provider Product Validation Execution Scope — со статусами
  CREATED / EDITORIAL_CLEANUP_COMPLETE / TARGETED_REVIEW_REQUIRED. Они не
  объявляются canonical или finally approved; обязательность coordinated
  downstream migration не изменена.
- **Editorial only:** no scope change, no owner decision, no version bump,
  no canonical status change.

### v0.3 (2026-07-31) — Mobile Channel Amendment (AYLA-DEC-0027)

Targeted material revision по owner ruling AYLA-DEC-0027 (OD-CH-1 —
Required MVP Channel Set, OWNER_DECISION_REGISTER) в Two-Phase Pilot Scope
Reconciliation Window. Это targeted owner-directed correction до
канонизации, а не новый release scope generation; версия сохранена 0.3.

- **Mobile App добавлен как REQUIRED / primary product experience**;
  **MAX Mini App и MAX Bot сохранены как required companion channels**
  (§8); feature parity across channels — NOT_REQUIRED; shared
  backend/state/consent/safety/analytics — REQUIRED; cross-channel
  continuity обязательна.
- **§6.1** — добавлено канальное распределение client-facing capabilities
  по owning channels (без полной channel capability matrix — она
  принадлежит execution/UX-документам).
- **§8** — устаревшая норма «MAX-бот + MAX Mini App — единственные
  обязательные каналы MVP» заменена на required three-channel set;
  Telegram остаётся вне scope (AYLA-DEC-0004 уточнён, не отменён).
- **§9** — добавлены mobile distribution infrastructure, deep/universal
  links, push notifications, cross-channel account linking, shared API
  contract.
- **§10** — добавлены channel-specific NFR (identity/consent consistency,
  shared recommendation state, deep-link fallback, channel-aware
  observability, mobile telemetry, per-channel rollback/feature flags,
  secure local storage, media permissions).
- **§11** — добавлено channel continuity release evidence (без числовых
  порогов).
- **§12** — добавлен gate Mobile channel readiness (ACTIVE / REQUIRED);
  store approval не является абсолютным blocker для internal testing.
- **§14** — migration matrix расширена mobile/channel downstream
  artifacts; все они зарегистрированы как TO_BE_CREATED (не существуют на
  момент ревизии, без выдуманных owners).
- **§15** — добавлены channel open questions (distribution route, store
  timing, feature ownership details, deep-link fallback) — все
  KEEP_NON_BLOCKING, implementation-level.
- **Не изменены:** составная продуктовая гипотеза, product boundary,
  primary journey, provider monetary boundary, wellness statuses, LDT
  boundary, booking downstream, economic neutrality, admission test,
  география и provider-профиль пилота, metadata (version/status/owner/
  created/updated).
- Документ остаётся **draft / proposed / candidate**; Product Owner Final
  Review остаётся deferred до execution-scope revisions и обязательных
  reviews (§12).

### v0.3 (2026-07-31) — Structured revision for current product canon

Выполнено в MVP Scope Canon Window по owner decision
APPROVE_STRUCTURED_REVISION_ROUTE (OD-MS-1: STRUCTURED_REVISION_SAME_PATH;
OD-MS-2: V0_3_CANDIDATE_SAME_PATH; OD-MS-3:
PATH_STABILITY_WITH_COORDINATED_MIGRATION). Основание: Ayla Product
Essence v1.1, Living Digital Twin Manifesto v1.0, Ayla Product Vision
v2.0, Ayla MVP Product Thesis v0.5, Ayla Product Principles v0.1,
AYLA-DEC-0026; действующие решения AYLA-DEC-0014/0015 сохранены.

- **Artifact identity:** path, title, node_id, owner и Git history
  сохранены; `supersedes` на v0.2 не добавляется — тот же artifact,
  lineage через Git history и этот журнал.
- **Memory-first framing удалён:** MVP Goal, admission filter и §9
  метрики переписаны под составную гипотезу (Thesis §4.3); память —
  continuity внутри составного пути.
- **Transformation Goal и Living Digital Twin включены** в release
  boundary (§3, §4, §6.1, §6.4); LDT MVP boundary задан по Essence §18 и
  Manifesto §14–15.
- **Booking — downstream:** primary journey (§4) завершается прогрессом,
  а не записью; «ничего не делать» — валидный исход.
- **Структура перестроена:** 15 разделов + Change Log; добавлены §2
  Position in Canon, §3 Product Boundary, §5 User Outcomes, §14 Downstream
  Migration Contract, §15 Open Questions.
- **Blockers актуализированы (§12):** OD-K11 — RESOLVED; Data Inventory
  Matrix — RESOLVED; Killer PRD — LEGACY_REFERENCE_ONLY; добавлены LDT
  media pipeline feasibility и recognition quality bar
  (REQUIRES_REVALIDATION).
- **Killer PRD переведён в legacy reference:** удалён из `depends_on`,
  оставлен в `related`; нормативных ссылок на Killer PRD в тексте нет.
- **Wellness inputs определены явно** (§6.1); medical inference не
  введён.
- **Admission filter заменён** на составной 8-точечный тест (§13);
  owner-decision правило расширения scope (AYLA-DEC-0014) сохранено
  дословно.
- **Metadata:** version 0.2 → 0.3; добавлен `canonical_status:
  candidate`; `depends_on` приведён к Essence / Manifesto / Vision /
  Thesis / Principles / Constitution / Decision Log / Documentation
  Roadmap; `related` актуализирован (MVP User Journey Specification).
- **Документ не объявляется CANONICAL:** статус CANONICAL присваивается
  только после internal consistency review, migration readiness review и
  owner approval. Owner re-review after revision — REQUIRED.
- **Downstream migration обязательна (§14)** до канонизации; downstream
  references не считаются aligned автоматически.

### v0.2 (2026-07-27) — Применено AYLA-DEC-0015 (MVP Monetary Boundary)

- **§5.1** добавлен: MVP Provider Monetary Boundary (provider-side charge
  flow: подписка, booking fee 90 ₽, charge result, billing status,
  eligibility gate, минимальная reconciliation) — без активации CAP-023.
- **§5** строка Payment Processing переписана по AYLA-DEC-0015; строка
  Billing уточнена: CAP-022 MVP-active только в части §5.1.
- **§6** добавлена обязательная интеграция YooKassa (только provider-side
  charge flow); статус proposal снят.
- **§4** разделён на §4.1 Product capabilities (12 user-visible) и §4.2
  Mandatory enabling capabilities: CAP-014 (`mandatory-cross-cutting`,
  `mvp_scope: required`), CAP-018 (`enabling-technical-capability`,
  `mvp_scope: required`), CAP-026, минимальный provider monetary integration
  (CAP-022).
- **§2** зафиксировано owner decision по персонам пилота (клиент, ищущий
  услугу/специалиста; соло-мастер; малый салон до трёх мастеров); остальные
  персоны Vision §11 — стратегические, не release blockers.
- Закрыты открытые вопросы v0.1: денежный контур, статус CAP-014/CAP-018,
  персоны пилота, интеграция YooKassa — по AYLA-DEC-0015 / owner decision
  2026-07-27. Остаются открытыми: маппинг CAP-ID до волны 2 (§4) и правило
  сокращения scope (§11).

### v0.1 (2026-07-27) — Initial draft

- Документ создан по AYLA-DEC-0014 и [[Ayla MVP Documentation Roadmap]] §1.4.
- Included/Deferred списки перенесены дословно из Roadmap §1.4; маппинг на
  CAP-ID выполнен по [[Ayla Domain Capability Registry]] §6 и помечен как
  proposal (Registry §9 — `undetermined` для всех записей, кроме CAP-023).
- Зафиксирована граница с [[AMD-020 Pilot Scope Registry]] (pilot/memory
  ownership ≠ release scope) по AYLA-DEC-0014.
- Открытые вопросы: применимость персон к пилоту (§2); статус CAP-014/CAP-018
  (§4); расхождение Thesis §6 и OD-CAP-4 по денежному контуру (§5);
  интеграция YooKassa (§6); правило сокращения scope (§11).
