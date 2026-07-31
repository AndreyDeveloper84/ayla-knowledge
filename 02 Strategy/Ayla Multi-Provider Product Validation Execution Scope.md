---
node_id: ayla.strategy.multi-provider-product-validation-execution-scope
title: Ayla Multi-Provider Product Validation Execution Scope
type: specification
status: draft
decision_status: proposed
canonical_status: draft
version: "0.2"
owner: Product Owner
knowledge_area:
  - strategy
system_owner:
  - ayla-knowledge
source_repository: ayla-knowledge
source_kind: product-requirements
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
created: 2026-07-31
updated: 2026-07-31
review_cycle: monthly
depends_on:
  - "[[Ayla MVP Scope and Release Contract]]"
  - "[[Ayla Single-Provider Technical Pilot Execution Scope]]"
  - "[[Ayla MVP Product Thesis]]"
  - "[[Consent Scope Registry]]"
related:
  - "[[AMD-020 Pilot Scope Registry]]"
  - "[[OWNER_DECISION_REGISTER]]"
---

# Ayla Multi-Provider Product Validation Execution Scope v0.2

**Статус:** DRAFT / proposed / non-canonical execution scope
**Версия:** 0.2
**Владелец:** Product Owner
**Upstream:** [[Ayla MVP Scope and Release Contract]] v0.3
(draft / proposed / candidate) и
[[Ayla Single-Provider Technical Pilot Execution Scope]] v0.3
(draft / proposed / INTERNALLY_APPROVED)
**Источник ревизии:** Ayla Multi-Provider Product Validation Scope v0.1
(внешний docx, structured revision)

> **Роль документа (факт):** это **post-A2 execution scope** — staged
> multi-provider repeatability и product/business validation после
> успешного завершения A2. Документ не является canonical Foundation
> artifact, не владеет MVP release boundary и не создаёт конкурирующий
> MVP scope anchor. Схема репозитория не поддерживает значение
> `canonical_status: non-canonical`; использовано валидное значение
> `draft`, а execution-level / non-foundation роль зафиксирована здесь и
> в §1–§2.

## 1. Purpose and Document Role

Этот документ отвечает на вопрос **«как поэтапно проверяется
переносимость продукта на независимых провайдеров и продуктово-бизнесовая
ценность после single-provider пилота»**: какие фазы, какой состав
провайдеров и когорт, какие capabilities активируются, какие gates
отделяют фазы и какие доказательства собираются.

This document:

- is a post-A2 execution scope;
- defines B0 repeatability and B1 product/business validation;
- is downstream of MVP Scope v0.3 and Single-Provider Execution Scope v0.3;
- does not redefine MVP release scope;
- does not activate full marketplace;
- does not activate CAP-020, CAP-023 or CAP-024;
- does not create paid placement;
- does not prove Product Thesis automatically.

Название **Product Validation Scope** без execution qualifier не
используется: оно размывает execution-роль документа и создаёт
конкурирующий scope anchor. Единственный владелец MVP release boundary —
MVP Scope v0.3.

## 2. Relationship to MVP Scope and Single-Provider Execution Scope

```text
Ayla MVP Scope and Release Contract v0.3 — release boundary (что входит в релиз)
└── Ayla Single-Provider Technical Pilot Execution Scope v0.3
      — staged execution на одном провайдере (фазы A0/A1/A2)
      └── Ayla Multi-Provider Product Validation Execution Scope v0.2 (этот документ)
            — staged multi-provider execution (фазы B0/B1)
```

- Этот документ **reference, а не дублирует** канонические продуктовые
  нормы: release scope, product boundary, LDT boundary, channel set,
  wellness statuses и monetary boundary определены в MVP Scope v0.3 и
  здесь не пересматриваются.
- Все ссылки на «Ayla MVP Scope v0.1» из v0.1 заменены на
  [[Ayla MVP Scope and Release Contract]] v0.3.
- Фазовая модель B0/B1 принадлежит execution-уровню: MVP Scope v0.3 фаз
  не содержит и не содержит обязанности их содержать.
- Конфликт между этим документом и MVP Scope v0.3 разрешается в пользу
  MVP Scope v0.3; конфликт с [[Ayla Product Essence]] — в пользу Essence.
- Переход A2 → B0 регулируется exit-критериями
  [[Ayla Single-Provider Technical Pilot Execution Scope]] (§10, §20) и
  preconditions §3 этого документа.

Применённые owner decisions (OWNER_DECISION_REGISTER, DECIDED
2026-07-31): **AYLA-DEC-0027** (required three-channel set),
**AYLA-DEC-0028** (Food Scanner — один из равнозначных триггеров),
**AYLA-DEC-0029** (28-day cycle — A2 exit evidence, precondition B0),
**AYLA-DEC-0030** (provider mix B0/B1), **AYLA-DEC-0031** (cold
acquisition — только B1), **AYLA-DEC-0032** (порядок monetization
validation), **AYLA-DEC-0033** (статус числовых порогов),
**AYLA-DEC-0034** (без formal RCT в initial beta).

## 3. Preconditions from A2

B0 не стартует, пока не выполнены preconditions (B0 entry gates):

- Single-Provider A2 exit completed
  ([[Ayla Single-Provider Technical Pilot Execution Scope]] §10);
- 28-day evidence available (AYLA-DEC-0029: достаточная, явно определённая
  доля A2-когорты завершила 28-дневный путь);
- technical/safety gates passed (hard gates = 0 нарушений);
- основной пользовательский цикл работает без критических ошибок;
- safety, consent, attribution и удаление данных проверены;
- provider/tenant не зашиты в код (добавляются конфигурацией);
- ServiceOffering отделено от CanonicalService;
- booking adapter readiness (интеграция через адаптер);
- runbook подключения провайдера и обработки исключений готов;
- onboarding owner нового провайдера назначен;
- tenant/provider/cohort analytics available (аналитика различает
  tenant / provider / cohort / manual intervention).

## 4. What B0 Validates

B0 подтверждает **переносимость и операционную повторяемость** продукта
на независимых провайдерах:

1. подключение провайдера повторяемо по runbook без разработчика;
2. каталоги разных провайдеров нормализуются по единым правилам
   (CanonicalService / ServiceOffering);
3. eligibility и safety работают единообразно для всех tenant;
4. deterministic ranking и explanation работают при нескольких допустимых
   кандидатах;
5. booking через adapter работает более чем у одного провайдера;
6. direct attribution сохраняется и аудируема в multi-provider контуре;
7. provider workspace minimum покрывает типовую работу провайдера;
8. consent-limited client context соблюдается на стороне провайдера;
9. cost-to-serve и источники ручной работы измеримы;
10. qualitative independent retention signal наблюдаем вне «Формулы тела»;
11. три required канала работают поверх единого backend для всех
    провайдеров с сохранением identity, consent и state.

## 5. What B0 Does Not Validate

- product-market fit Ayla;
- willingness to pay и любую monetization hypothesis;
- cold acquisition и удержание холодной аудитории;
- количественный независимый retention (только qualitative signal);
- нейтральность выбора при масштабном marketplace;
- причинную атрибуцию вклада Twin (AYLA-DEC-0034);
- memory-dependent claims (Phase 1 — session-only;
  [[Ayla Single-Provider Technical Pilot Execution Scope]] §14);
- готовность к массовому запуску.

```text
B0 does not validate PMF or willingness to pay.
```

## 6. What B1 Validates

B1 подтверждает **продуктовую и бизнес-гипотезу** на нескольких
независимых провайдерах.

**Основная гипотеза (из v0.1, сохранена):** пользователь возвращается в
Ayla не из-за связи с конкретным салоном, а потому что Ayla понимает его
цель, связывает ежедневные наблюдения с персональным планом и помогает
выбрать уместное домашнее действие или реальную услугу у подходящего
провайдера.

**Вторичные гипотезы:**

| Сторона | Проверяемая гипотеза |
|---|---|
| Пользователь | Ayla даёт регулярную полезность, вызывает доверие и приводит к meaningful actions |
| Мастер | Ayla приводит более подготовленного клиента и снижает стоимость консультации и повторного контакта |
| Салон | Ayla увеличивает конверсию в запись и повторные визиты без чрезмерной нагрузки на администратора |
| Платформа | Каталоги, availability, matching и attribution работают для разных провайдеров по единым правилам |
| Бизнес | Провайдеры видят измеримую ценность и демонстрируют готовность платить (AYLA-DEC-0032) |

Предмет валидации B1:

- независимый retention вне контролируемой среды «Формулы тела»;
- provider value (интервью, continuation, WTP-сигналы);
- monetization hypothesis в порядке AYLA-DEC-0032 (§20);
- активация и поведение отдельной cold acquisition когорты (§21);
- business metrics и reason-coded refusals;
- cross-channel cohort analysis.

## 7. What B1 Does Not Validate

- готовность к массовому федеральному запуску;
- полный self-service marketplace и marketplace search (CAP-024 — OUT);
- модель крупного салона (DEFERRED, отдельное owner decision);
- причинную атрибуцию вклада Twin (formal controlled experiment —
  DEFERRED, AYLA-DEC-0034);
- клиентские платежи (клиент не платит — AYLA-DEC-0032, Constitution
  Ст. IV);
- memory-dependent claims (требуют Phase 2 evidence, §26);
- Product Thesis автоматически (§26);
- полноценный billing сверх canonical provider-side monetary boundary
  (MVP Scope §7).

## 8. Three-Channel Delivery Model

Применяется **AYLA-DEC-0027** (Required MVP Channel Set):

```text
Mobile App:      REQUIRED / PRIMARY PRODUCT EXPERIENCE
MAX Mini App:    REQUIRED / LIGHTWEIGHT EMBEDDED COMPANION
MAX Bot:         REQUIRED / CONVERSATIONAL, NOTIFICATION AND ROUTING COMPANION
Feature parity:  NOT_REQUIRED
Shared backend/domain/state/consent/safety/recommendation/memory/
attribution/analytics: REQUIRED
```

Для B0/B1 дополнительно:

- provider expansion не создаёт channel-specific backend rules: единый
  shared API contract для всех провайдеров и всех трёх каналов;
- ranking/recommendation едины между каналами: один и тот же candidate
  set, ordering и explanation независимо от канала;
- retention считается cross-channel: пользователь — один, когорта
  определяется acquisition source и provider origin, а не каналом;
- entry channel и acquisition source фиксируются в событиях (§19);
- mobile installation не обязательна для первой активации через MAX
  (Mini App / Bot);
- переход MAX → Mobile должен быть измерим (deep-link/route outcome).

Полная feature parity не требуется; отсутствие второстепенной функции в
Mini App или Bot не блокирует фазу, если capability доступна в
назначенном owning channel (MVP Scope §8).

## 9. Phase Model Overview

| Фаза | Провайдеры | Пользователи | Длительность | Цель |
|---|---|---|---|---|
| B0 — Multi-Provider Repeatability | 2–3: «Формула тела» + 1–2 независимых | warm users + пользователи новых провайдеров; ≥1 не-клиентская когорта; без cold | 6–8 недель | Переносимость и операционная повторяемость |
| B1 — Product Validation Beta | 3–5 салонов + 5–10 соло-мастеров | 150–300 activated users, включая отдельную cold cohort | не менее 6–8 недель | Независимый retention, provider value, monetization hypothesis |

Клиентский цикл single-provider пилота сохраняется; multi-provider фазы
добавляют только функции, необходимые для переноса на несколько
провайдеров и честной проверки рынка:

```text
Transformation Goal и Living Digital Twin
→ trigger-сценарии (food — один из равнозначных, AYLA-DEC-0028) и daily check-in
→ weekly plan
→ eligibility и Safety Gate
→ provider candidates
→ объяснимый выбор и альтернативы
→ booking у выбранного провайдера
→ appointment и feedback
→ weekly review
```

## 10. Phase B0 — Multi-Provider Repeatability

**Purpose:** проверить переносимость и операционную повторяемость.

**Entry gates:** §3 полностью (A2 exit, 28-day evidence,
technical/safety gates, provider not hardcoded, booking adapter
readiness, runbook, onboarding owner, tenant/provider/cohort analytics).

**Provider mix (AYLA-DEC-0030):**

```text
2–3 providers total:
«Формула тела» + 1–2 independent providers

Allowed:
solo specialist
small salon up to 3 specialists

Large salon:
OUT / DEFERRED (отдельное owner decision и отдельная когорта)
```

**Users:**

- warm users исходного салона;
- пользователи вновь подключённых провайдеров;
- минимум одна когорта, не являющаяся клиентами «Формулы тела»
  (AYLA-DEC-0031);
- no paid cold acquisition (cold — OUT в B0, §21).

**Duration:** 6–8 недель.

### MUST

- provider onboarding through runbook;
- CanonicalService / ServiceOffering normalization;
- manual taxonomy review;
- eligibility gate before ranking (§15);
- multiple eligible provider candidates where possible;
- deterministic ranking (§16);
- stored ranking reasons;
- explainable recommendation;
- alternatives;
- booking adapters (§17);
- provider workspace minimum (§18);
- tenant/provider/cohort analytics;
- consent-limited client context;
- attribution completeness (§19);
- three-channel continuity (§8).

### SHOULD

- second booking adapter;
- minimal provider analytics;
- reduced manual onboarding.

### DEFERRED

- monetization validation (B1, §20);
- formal RCT (AYLA-DEC-0034);
- large salon (AYLA-DEC-0030);
- assisted attribution except diagnostic (§19).

### OUT

- cold acquisition — B0 OUT; activates only in B1 after B0 exit (§21);
- paid placement;
- marketplace search (CAP-024);
- multi-tenant customization (CAP-020);
- client payments;
- autonomous procedure assignment;
- full CRM.

### Exit

- repeatable onboarding without developer;
- ranking/explanation works with multiple candidates;
- safety/consent consistent across tenants;
- attribution stable;
- cost-to-serve understood;
- independent retention signal observed qualitatively;
- manual work sources understood.

```text
B0 does not validate PMF or willingness to pay.
```

## 11. Phase B1 — Product Validation Beta

**Purpose:** проверить продуктовую и бизнес-гипотезу (§6) на
независимых провайдерах.

**Entry:**

- B0 exit полностью;
- owner-approved B1 thresholds (final go/no-go утверждается Product
  Owner до B1 launch, §23);
- acquisition channels defined;
- monetization interview design ready;
- provider mix confirmed;
- safety/consent stable.

**Provider mix (AYLA-DEC-0030):**

```text
3–5 салонов
+
5–10 соло-мастеров
```

Провайдеры различаются по размеру, каталогу, зрелости процессов и типу
специалистов. Крупный салон остаётся отдельным кейсом и требует
отдельного owner decision и отдельной когорты.

**Users:**

```text
150–300 activated users
```

Включая отдельную cold acquisition cohort (§21).

**Duration:** не менее 6–8 недель пользовательского наблюдения.

### MUST

- все B0 capabilities;
- cold acquisition cohort (§21);
- independent retention measurement;
- provider-value interviews;
- monetization offers (§20);
- provider continuation/WTP signals;
- business metrics (§23);
- reason-coded refusals;
- cross-channel cohort analysis.

### SHOULD

- combined monetization model interview;
- trust/diagnostic surveys.

### DEFERRED

- full billing beyond canonical monetary boundary (MVP Scope §7);
- large salon cohort;
- formal controlled Twin experiment (AYLA-DEC-0034);
- marketplace self-service.

### OUT

- mass launch;
- paid placement;
- ad auction;
- customer payments;
- CAP-023 expansion;
- CAP-024 marketplace search;
- CAP-020 customization;
- full CRM.

### Exit

- есть независимый retention-сигнал вне «Формулы тела»;
- есть повторяемая процедура подключения провайдера;
- ranking и объяснение работают для нескольких кандидатов;
- safety и consent единообразны для всех tenant;
- booking attribution и appointment feedback стабильны;
- определена жизнеспособная monetization hypothesis;
- понятны cost-to-serve и основные источники ручной работы;
- сформировано предложение следующего scope (публичный MVP, ограниченный
  marketplace или provider SaaS); решение — Product Owner, не
  автоматический триггер (§26).

## 12. Provider Mix and Cohort Design

Применяются **AYLA-DEC-0030**, **AYLA-DEC-0031**, **AYLA-DEC-0034**:

```text
B0: repeatability cohorts
B1: product/business validation cohorts
Cold acquisition: B1 only
No formal RCT required in initial beta.
Observational cohort comparison is required.
Causal claims are prohibited.
```

**Когорты:**

- existing warm users — клиенты уже подключённых провайдеров;
- new provider users — клиенты независимых мастеров и салонов;
- cold acquisition users — новые пользователи из внешнего канала
  (только B1);
- provider comparison cohorts — пользователи, которым доступно более
  одного допустимого провайдера.

**Обязательное разделение данных:**

- метрики считаются отдельно по cohort, tenant, provider type и
  acquisition source;
- данные «Формулы тела» не объединяются с независимыми провайдерами без
  отдельного среза;
- ручное сопровождение маркируется и анализируется отдельно (§24);
- retention считается от Behavioral Activation.

**Измерения сравнения (observational):** provider origin, acquisition
source, channel entry, Twin engagement depth, recommendation usage,
booking outcome и retention period. Сравнение — наблюдательное; явное
заявление об ограничениях обязательно (Honest Representation,
[[Ayla Product Principles]] 4.5).

## 13. Provider Onboarding Boundary

Onboarding каждого провайдера обязан включать (MUST):

- создание Tenant, Provider, Location и рабочих ролей;
- контактные данные, график, правила отмены и сервисные условия;
- catalog import или manual entry;
- ServiceOffering → CanonicalService mapping;
- booking adapter или governed fallback-процесс;
- readiness check перед публикацией;
- onboarding runbook и назначенный onboarding owner.

Full self-service onboarding — OUT: onboarding выполняется по runbook с
участием оператора; совершенная автоматизация onboarding всех типов
провайдеров не требуется.

## 14. Catalog Normalization Boundary

- CanonicalService описывает единый тип услуги в канонической
  таксономии; ServiceOffering хранит коммерческое предложение конкретного
  провайдера;
- название, длительность, цена, location, specialist eligibility и
  availability принадлежат провайдеру (ServiceOffering);
- текстовое совпадение названий не используется как единственное
  основание matching;
- unresolved items → manual taxonomy review (§24);
- canonical taxonomy не поглощает коммерческую презентацию провайдера.

## 15. Eligibility and Safety Before Ranking

```text
Eligibility first
Ranking second
```

Eligibility включает: safety, consent, service applicability, возрастные
ограничения и известные противопоказания, availability, operational
eligibility и geography where applicable. До ranking недопустимые услуги
и провайдеры исключаются из candidate set.

- safety-правила едины для всех провайдеров и не могут быть ослаблены
  коммерческими настройками;
- спорные случаи эскалируются на ручную проверку (§24);
- **commercial status cannot bypass eligibility** — коммерческий статус,
  тариф или платёж не влияют на прохождение eligibility gate
  (Constitution Ст. IV).

## 16. Deterministic Ranking and Explainability

**Allowed factors:**

- Transformation Goal relevance;
- user preference;
- availability;
- geography/distance;
- provider data completeness/quality;
- explicit constraints.

**Forbidden factors:**

- provider tariff;
- subscription level;
- payment;
- commission;
- advertising budget;
- commercial relationship.

```text
LLM may explain.
LLM must not own ranking.
```

Candidate set, factors и reasons сохраняются и доступны для аудита.
Advanced ML ranking — DEFERRED (MVP Scope §7).

**Paid relationship correction:** формулировка v0.1 «платные или
партнёрские отношения раскрываются, если влияют на представление
вариантов» заменена нормой:

```text
Paid relationship must not influence eligibility, candidate generation,
ranking, recommendation or presentation order in B0/B1.
```

Paid placement — OUT (§10, §11). Это inherited constitutional guardrail
(Constitution Ст. IV), а не дисклеймер: раскрытие paid relationship не
делает влияние допустимым.

**Пользовательский выбор:** пользователь видит, почему предложена
конкретная услуга или provider; получает один основной вариант и
альтернативы по запросу или причине отказа; может выбрать альтернативу,
отказаться и указать причину (reason-coded refusal). Нельзя создавать
впечатление медицинского назначения (Constitution Ст. X, XII).

## 17. Booking Adapter Boundary

Один внутренний booking contract:

```text
create
confirm
cancel
reschedule
status
```

- внешние booking-системы подключаются только через adapter; поддерживается
  более одного booking-контура (разные провайдеры — разные системы);
- создание, подтверждение, отмена, перенос и appointment status
  нормализуются к внутреннему контракту;
- deep-link fallback разрешён только если attribution и route outcome
  сохраняются и результат фиксируется, где это возможно;
- Yclients не является канонической зависимостью — только текущая
  реализация/пример провайдерской booking-системы (как и в
  [[Ayla Single-Provider Technical Pilot Execution Scope]] §21).

## 18. Provider Workspace Minimum

Минимум рабочего места провайдера:

- входящие Ayla-рекомендации и bookings;
- booking/appointment statuses;
- exception handling и запросы на уточнение;
- minimal provider analytics (показы, переходы, записи, визиты, повторные
  действия);
- consent-limited client context: контекст клиента только в объёме,
  разрешённом consent scope ([[Consent Scope Registry]];
  [[AMD-020 Pilot Scope Registry]] — provider не получает сведений о
  взаимодействии пользователя с другими провайдерами, Constitution
  Ст. V).

Это execution-level enabling operations surface для B0/B1: он **не
модифицирует** canonical MVP release boundary (MVP Scope §6.2
provider-facing) и **не активирует** новую user-facing MVP capability.
Полная CRM, финансовый учёт и программа лояльности — OUT.

**Minimal provider analytics:** SHOULD в B0, MUST в B1 — provider workspace
minimum в B0 остаётся MUST, но analytics-компонент внутри него — SHOULD до
B1 (синхронно с §22).

## 19. Attribution and Outcome Boundary

MUST-состав direct attribution:

```text
recommendation_id
candidate_set
provider_id
service_offering_id
selected action
booking_id when applicable
appointment_id when applicable
channel source
cohort source
```

- attribution chain сохраняется и аудируема для всех провайдеров и
  каналов; attribution completeness — working validation threshold (§23);
- assisted / multi-touch attribution — DEFERRED; при исследовании —
  DIAGNOSTIC only;
- post-procedure feedback сохраняется отдельно от объективного
  медицинского эффекта; медицинские выводы запрещены (Constitution
  Ст. X, XII);
- повторная запись связывается с исходным или новым recommendation
  context.

## 20. Monetization Validation Boundary

Применяется **AYLA-DEC-0032** — порядок проверки моделей:

```text
1. Solo subscription — 690 ₽ (интервью и оффер самостоятельному мастеру)
2. Salon subscription — 990 ₽ (интервью и оффер салону)
3. Completed booking fee — 90 ₽ (проверка fee за состоявшуюся запись)
4. Combined model (проверка допустимости комбинированной модели)
```

B1 валидирует: willingness to pay, preferred model, refusal reasons,
provider value и cost-to-serve. Beta не обязана запускать полноценный
billing.

- отказы фиксируются reason-coded: цена, отсутствие ценности, риск,
  сложность, отсутствие доверия;
- **клиент Ayla не платит** (Constitution Ст. IV): customer
  willingness-to-pay не является monetization target; вместо неё
  измеряются willingness to use, share permitted data, follow
  recommendations and book through Ayla;
- не активируются: client payments, новые transaction fees сверх
  canonical 90 ₽ booking fee, revenue share, billing сверх canonical
  provider-side monetary boundary (MVP Scope §7 — подписка, booking fee
  90 ₽, charge result, billing status, eligibility gate, минимальная
  reconciliation).

## 21. Cold Acquisition Boundary

Применяется **AYLA-DEC-0031**:

```text
B0: OUT
B1: MUST as separate cohort
```

- acquisition source фиксируется для каждого пользователя (§19);
- cold-метрики считаются отдельно от warm/new-provider когорт (§12);
- скрытая ручная помощь cold-когорте запрещена (§24): вся ручная работа
  логируется и маркируется;
- слабая cold activation (cold-трафик не проходит onboarding или не
  достигает Behavioral Activation) — stop signal для paid acquisition и
  сигнал эскалации (§28), а не основание увеличивать ручное
  сопровождение.

## 22. Capability Activation Matrix

| Capability | B0 | B1 |
|---|---|---|
| Provider onboarding (runbook + owner) | MUST | MUST |
| Catalog normalization + manual taxonomy review | MUST | MUST |
| Eligibility gate before ranking | MUST | MUST |
| Multiple eligible candidates | MUST (where possible) | MUST |
| Deterministic ranking + stored reasons | MUST | MUST |
| Explainable recommendation + alternatives | MUST | MUST |
| Reason-coded refusals | MUST | MUST |
| Booking adapter (internal contract) | MUST | MUST |
| Second booking adapter | SHOULD | MUST (более одного контура) |
| Provider workspace minimum | MUST | MUST |
| Minimal provider analytics | SHOULD | MUST |
| Tenant/provider/cohort analytics | MUST | MUST |
| Consent-limited client context | MUST | MUST |
| Direct attribution (полный состав §19) | MUST | MUST |
| Three-channel continuity | MUST | MUST |
| Cross-channel cohort analysis | SHOULD | MUST |
| Independent retention measurement | QUALITATIVE | MUST |
| Cold acquisition cohort | OUT | MUST |
| Provider-value interviews | DEFERRED | MUST |
| Monetization offers (порядок §20) | DEFERRED | MUST |
| Provider continuation/WTP signals | DEFERRED | MUST |
| Combined monetization model interview | DEFERRED | SHOULD |
| Trust/diagnostic surveys | DEFERRED | SHOULD |
| Reduced manual onboarding | SHOULD | SHOULD |
| Assisted/multi-touch attribution | DEFERRED (diag.) | DEFERRED (diag.) |
| Formal RCT / controlled Twin experiment | DEFERRED | DEFERRED |
| Large salon cohort | OUT | DEFERRED (separate owner decision) |
| Full billing beyond monetary boundary | OUT | DEFERRED |
| Marketplace self-service / search (CAP-024) | OUT | OUT |
| Paid placement / ad auction | OUT | OUT |
| Client payments | OUT | OUT |
| CAP-020 customization | OUT | OUT |
| CAP-023 expansion | OUT | OUT |
| Full CRM | OUT | OUT |

## 23. Metrics and Threshold Status

Применяется **AYLA-DEC-0033**.

### REQUIRED HARD GATES

- user data loss = 0;
- critical safety incidents = 0;
- consent bypass = 0;
- economic influence on recommendation or candidate ordering = 0 —
  inherited constitutional guardrail (Constitution Ст. IV): commercial
  status, tariff, payment or provider economics must not influence
  eligibility, candidate generation, ranking, recommendation or
  presentation order;
- eligibility-before-ranking preserved (§15) = 0 нарушений;
- direct attribution chain technically available and auditable.

### WORKING VALIDATION THRESHOLDS

Все процентные цели из v0.1 — рабочие пороги валидации, **не
канонические нормы**; утверждаются Product Owner до B1 launch после
определения каналов привлечения и модели монетизации:

- D28 Meaningful Retention у независимых провайдеров — не ниже 20–25%;
- повторное использование trigger-сценариев (trigger-agnostic, ≥50%
  активированных; заменяет v0.1 «повторное использование Food Scanner»
  по AYLA-DEC-0028);
- Weekly Review Completion — не менее 35–40%;
- recommendation-to-booking conversion — не менее 12–15% для допустимых
  рекомендаций;
- booking-to-completed appointment — не менее 70%;
- provider continuation — не менее 50% провайдеров хотят продолжить
  после beta;
- provider WTP — не менее 30% провайдеров подтверждают готовность
  платить по одной из моделей §20;
- attribution completeness — не менее 95%;
- manual intervention and cost-to-serve are measured as a qualitative
  working validation threshold; exact acceptable cost-to-serve and unit
  economics criteria are defined by the Measurement Framework and approved
  by Product Owner before B1 launch.

FINAL GO/NO-GO утверждается Product Owner до B1 launch после B0 evidence
и Measurement Framework; здесь не канонизируется.

### DIAGNOSTIC

- candidate coverage;
- onboarding time;
- catalog error rate;
- manual intervention rate;
- cost-to-serve;
- trust score (до формального определения — open question §29);
- assisted conversion;
- Twin engagement depth;
- Food Scanner usage (DIAGNOSTIC, AYLA-DEC-0028 — как и в
  [[Ayla Single-Provider Technical Pilot Execution Scope]] §13/§19).

## 24. Manual Operations Policy

**Allowed:**

- manual taxonomy review;
- onboarding assistance;
- fallback booking;
- provider data correction;
- safety escalation;
- consent/deletion handling.

**Log каждого вмешательства:**

```text
type
reason
operator
duration
result
provider
cohort
channel
```

**Forbidden:**

- hidden ranking change;
- hidden recommendation override;
- commercial preference;
- unlogged provider intervention;
- manual user facts (создание оператором пользовательских фактов);
- safety bypass.

Функциональность, регулярно выполняемая вручную, не считается
автоматизированной; ручное сопровождение маркируется и анализируется
отдельно (§12).

## 25. Architecture Readiness Boundary

Сохраняются только execution-level readiness statements:

- `tenant_id` и `provider_id` в релевантных записях и событиях;
- provider isolation (один провайдер не получает данных другого,
  Constitution Ст. V);
- shared API contract для всех трёх каналов и всех провайдеров;
- adapter contracts (booking — §17);
- deterministic ranking service с сохранёнными candidate set, factors и
  reasons;
- ranking audit;
- provider workspace boundary (§18);
- channel clients не владеют business logic.

Детальные entity/model/API definitions — включая minimal multi-tenant
entity set v0.1 (Tenant, Provider, Location, Specialist,
CanonicalService, ServiceOffering, Availability, ProviderCandidate,
Recommendation, Booking, Appointment) — принадлежат
Architecture/Domain-документам и здесь не дублируются.

Техническая multi-tenant readiness **не означает** активацию CAP-020
(multi-tenant customization — OUT_OF_SCOPE в MVP Scope §7).

## 26. Product Validation Boundary

```text
B0 validates repeatability.
B1 validates independent retention, provider value and monetization hypothesis.
Neither automatically validates Product Thesis.
Product Owner closes Product Thesis Validation.
```

- Product Thesis Validation — отдельный governance act Product Owner по
  [[Ayla MVP Product Thesis]] §8.4; evidence B0/B1 — вход для него, а не
  его замена;
- memory-dependent claims требуют Phase 2 evidence
  ([[Consent Scope Registry]] §10.2 gate, AYLA-DEC-0018): Phase 1 —
  session-only memory, memory-dependent claims не входят в exit evidence
  B0/B1;
- booking conversion — не North Star продукта (MVP Scope §11: booking —
  secondary downstream evidence).

## 27. Disallowed Interpretations

```text
B0 success does not prove PMF.
B0 retention does not prove monetization.
B1 thresholds are not canonical norms.
Provider WTP does not justify commercial ranking.
Booking conversion is not Ayla's North Star.
Cold traffic failure does not prove technical failure.
Warm retention is not independent retention.
Observational Twin engagement is not causal proof.
Multi-provider readiness is not full marketplace activation.
Three channels are not three products.
```

## 28. Risks and Stop Conditions

Немедленная остановка фазы (stop condition):

- любая потеря пользовательских данных;
- любой critical safety incident;
- любой consent bypass;
- любое экономическое влияние на eligibility, candidate generation,
  ranking, recommendation или presentation order;
- любой обход eligibility-before-ranking;
- потеря attribution chain без возможности восстановления;
- рассинхронизация identity/consent между каналами или tenant.

Риски, требующие эскалации к Product Owner (без автоматической
остановки):

- retention держится только у тёплых клиентов исходного салона;
- пользователи не возвращаются ни к одному trigger-сценарию после первого
  использования;
- рекомендации процедур вызывают недоверие или воспринимаются как
  реклама;
- независимые провайдеры требуют постоянного ручного сопровождения;
- каталоги невозможно стабильно нормализовать без разработчика;
- booking attribution регулярно теряется;
- провайдеры не видят влияния на записи или повторные визиты;
- cold-когорта не проходит onboarding или не достигает Behavioral
  Activation (stop signal для paid acquisition, §21).

## 29. Open Questions

Только реальные non-blocking вопросы; решённые AYLA-DEC-0030…0034
вопросы не переоткрываются:

- exact B1 thresholds (owner approval до B1 launch, §23);
- exact trust score definition;
- exact acquisition channels;
- exact provider interview script;
- exact cost-to-serve target;
- exact large-salon experiment timing;
- exact formal experiment design after beta (AYLA-DEC-0034).

Вопросы для review из v0.1 закрыты этой ревизией или переведены выше:

- достаточность состава провайдеров — закрыто AYLA-DEC-0030 (§10–§12);
- включение холодного трафика — закрыто AYLA-DEC-0031 (§21);
- допустимые/запрещённые факторы ranking — закрыто §16;
- первая модель монетизации — закрыто AYLA-DEC-0032 (§20);
- данные provider о пользователе — consent-limited client context (§18),
  [[Consent Scope Registry]], [[AMD-020 Pilot Scope Registry]];
- go/no-go пороги — статусы AYLA-DEC-0033 (§23), финальные пороги —
  owner approval + Measurement Framework;
- контрольная группа — закрыто AYLA-DEC-0034 (§12);
- следующий продуктовый этап при частичном подтверждении — предложение
  формируется как B1 exit evidence (§11), решение — Product Owner (§26).

## 30. Change Log

> Журнал отражает историю изменений и не является нормативной частью.
> Нормативно — текущее состояние разделов 1–29.

### v0.2 (2026-07-31) — Provider analytics, cold acquisition, large salon and cost-to-serve wording normalized

Выполнено в Two-Phase Pilot Scope Reconciliation Window по промпту
`TWO_PHASE_PILOT_COMBINED_EDITORIAL_CLEANUP_PROMPT.md` (findings CD-P3-02,
MP-ICR-P3-01, MP-ICR-P3-02, MP-ICR-P3-03, MP-ICR-P3-04).

- **§18** — boundary-формулировка уточнена: execution-level enabling
  operations surface, не модифицирует canonical MVP release boundary и не
  активирует user-facing MVP capability; minimal provider analytics явно
  SHOULD в B0 / MUST в B1 (CD-P3-02, MP-ICR-P3-01).
- **§10** — cold acquisition перенесён из DEFERRED в OUT («B0 OUT;
  activates only in B1 after B0 exit»), согласовано с §21 и §22
  (MP-ICR-P3-02).
- **§22** — composite-статус large salon `OUT/DEFERRED` разделён: B0 —
  OUT, B1 — DEFERRED (separate owner decision) (MP-ICR-P3-03).
- **§23** — расплывчатая строка про unit economics заменена qualitative
  working validation threshold с отсылкой к Measurement Framework и owner
  approval до B1 launch; числовой порог не создан (MP-ICR-P3-04).
- **Editorial only:** no scope change, no owner decision, no version bump,
  no canonical status change.

### v0.2 (2026-07-31) — Structured revision after Two-Phase Pilot Scope Reconciliation

Выполнено в Two-Phase Pilot Scope Reconciliation Window по промпту
`MULTI_PROVIDER_PRODUCT_VALIDATION_EXECUTION_SCOPE_V0_2_REVISION_PROMPT.md`
после Repeat Internal Consistency Review Single-Provider Execution Scope
v0.3 (verdict: APPROVED_FOR_MULTI_PROVIDER_SCOPE_REVISION). Источник:
внешний docx «Ayla Multi-Provider Product Validation Scope v0.1».

- **Переименован** из «Product Validation Scope» в «Product Validation
  Execution Scope»: устранён конкурирующий scope anchor; execution role
  зафиксирован (§1–§2); документ не является canonical Foundation
  artifact.
- **Материализован в репозитории** как Markdown
  (`02 Strategy/Ayla Multi-Provider Product Validation Execution Scope.md`);
  исходный docx остаётся внешним pre-canon artifact.
- **B0/B1 split:** единая «beta» v0.1 разделена на Phase B0
  (repeatability, 2–3 провайдера, 6–8 недель) и Phase B1 (product/business
  validation, 3–5 салонов + 5–10 соло, 150–300 пользователей, ≥6–8
  недель).
- **Provider mix** по AYLA-DEC-0030: B0 — «Формула тела» + 1–2
  независимых (соло / малый салон до 3 специалистов); группа D v0.1
  (более крупный салон) — DEFERRED, отдельное owner decision; норма
  v0.1 «салон 2–4 специалиста» приведена к каноническому «до 3».
- **Cold acquisition** по AYLA-DEC-0031: OUT в B0; отдельная обязательная
  когорта в B1; в B0 обязательна минимум одна когорта не-клиентов
  «Формулы тела».
- **Monetization order** по AYLA-DEC-0032: 690 ₽ соло → 990 ₽ салон →
  90 ₽ booking fee → combined; клиент не платит; customer WTP (v0.1
  §11/§14) удалён как target и заменён на willingness to use / share /
  follow / book.
- **Threshold classification** по AYLA-DEC-0033: все процентные цели
  v0.1 §12 переведены в WORKING VALIDATION THRESHOLDS; REQUIRED HARD
  GATES и DIAGNOSTIC выделены; final go/no-go — owner approval до B1
  launch.
- **Food Scanner de-centered** по AYLA-DEC-0028: «≥50% повторно
  используют Food Scanner» заменён trigger-agnostic порогом; food usage —
  DIAGNOSTIC; цепочка §9 использует trigger-agnostic формулировку.
- **Ranking neutrality и eligibility:** deterministic ranking с явными
  allowed/forbidden factors (§16); eligibility-before-ranking — hard
  gate (§15, §23); «LLM may explain, must not own ranking».
- **Paid influence removed:** формулировка v0.1 «платные отношения
  раскрываются, если влияют» заменена запретом влияния paid relationship
  на eligibility, candidate generation, ranking, recommendation и
  presentation order (§16); paid placement — OUT.
- **RCT deferred** по AYLA-DEC-0034: formal controlled experiment —
  DEFERRED; observational cohort comparison обязателен; causal claims
  запрещены (§12).
- **Three-channel model** добавлена по AYLA-DEC-0027 (§8): Mobile
  REQUIRED/PRIMARY, Mini App/Bot REQUIRED companion, parity NOT_REQUIRED;
  cross-channel retention, MAX-first activation, измеримый переход
  MAX → Mobile.
- **A2 preconditions** формализованы (§3) по Single-Provider Execution
  Scope §10/§20 и AYLA-DEC-0029.
- **Stale references удалены:** «Ayla MVP Scope v0.1» →
  [[Ayla MVP Scope and Release Contract]] v0.3 (wikilink); добавлена
  ссылка на [[Ayla Single-Provider Technical Pilot Execution Scope]] v0.3.
- Применённые owner decisions: AYLA-DEC-0027…0034 (все восемь).
- **Не изменены по существу (invariants):** основная гипотеза v0.1 §3,
  вторичные гипотезы (стороны пользователь/мастер/салон/платформа),
  состав onboarding/catalog/eligibility/booking/provider
  workspace/attribution границ, negative signals как risk-контур, exit
  criteria beta как B1 exit.

### Migration note — v0.1 (pre-canon, внешний docx)

Сохраняется как история, не как активные нормы:

- v0.1 «Ayla Multi-Provider Product Validation Scope» (16 разделов +
  вопросы для review, 220 параграфов) — заменён этой ревизией; исходный
  docx остаётся внешним artifact;
- единый формат beta v0.1 (§5) — разделён на B0/B1 (§9–§11);
- provider groups A–D v0.1 (§6) — группа A/B/C отражены в provider mix
  B0/B1, группа D (крупный салон) — DEFERRED (AYLA-DEC-0030);
- Core Product Scope и Multi-Provider Expansion v0.1 (§7–§8) —
  перераспределены в §9, §13–§19;
- minimal multi-tenant model v0.1 (§9) — перенесена как reference в
  Architecture boundary (§25), entity detail не дублируется;
- экспериментальный дизайн v0.1 (§10) — §12 с поправкой AYLA-DEC-0031/
  0034;
- метрики и Primary Success Criteria v0.1 (§11–§12) — статусы §23;
- negative signals v0.1 (§13) — §28;
- Monetization Validation v0.1 (§14) — §20 с порядком AYLA-DEC-0032;
- Out of Scope v0.1 (§15) — §10/§11 OUT + MVP Scope §7;
- Exit Criteria v0.1 (§16) — B1 exit (§11);
- вопросы для review v0.1 — закрыты или переведены в §29.
