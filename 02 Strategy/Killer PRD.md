---
node_id: ayla.strategy.killer-prd
title: Killer PRD v1.3.1 — Сценарий с памятью в основе
type: specification
status: draft
decision_status: proposed
version: "1.3.1"
owner: Product Owner
priority: P0
knowledge_area:
  - strategy
domain:
  - recommendation
  - user-context
concerns:
  - privacy
  - safety
  - explainability
  - governance
system_owner:
  - ayla-recommendation
  - ayla-user-context
  - ayla-conversation
source_kind: canonical
classification: internal
data_sensitivity: high
data_categories:
  - pii
  - health
security_sensitivity: medium
ai_indexing: allowed
export_policy: full
created: 2026-07-21
updated: 2026-07-22
review_cycle: before-major-change
depends_on:
  - "[[Ayla Decision Log]]"
  - "[[ADR-0012 Dynamic User Model]]"
  - "[[Ayla User Journey Specification]]"
  - "[[Ayla Constitution]]"
required_dependencies:
  - Consent Scope Registry (User Context Domain Owner + Privacy Owner) — blocks implementation and pilot
  - Operational handling contract for ranking_economic_neutrality_alert — blocks pilot/production traffic
---

# Killer PRD v1.3.1 — Сценарий с памятью в основе

> Product Requirements Document. Переработка `PRD_Ayla_Killer_Scenario_v1.0.md` в соответствии с AYLA-DEC-0002.

| | |
|---|---|
| **Статус** | Draft (ожидает cross-functional review) |
| **Статус решения** | Proposed — направление владельца зафиксировано; canonical approval ожидается |
| **Версия** | 1.3.1 |
| **Владелец** | Product Owner / W7 (Canon Architect) |
| **Заинтересованные стороны** | Recommendation Engine Owner, Privacy/Safety Owner, Conversation Design Owner |
| **Блокеры канонизации** | ADR-0012 OD-1, OD-2; отсутствие утверждённого Consent Scope Registry (OD-K9). |
| **Блокеры pilot / production** | OD-1, OD-2, OD-K9, OD-K10 (operational handling contract для economic-neutrality alerts). |

> **Примечание о `source_kind`:** схема `.knowledge/schema.yaml` требует значения `canonical` для внутренних нормативных документов, но не предоставляет отдельного значения для `canonical candidate`. Поэтому документ зарегистрирован как `canonical` со статусом `Draft / Proposed`, что семантически означает *canonical candidate*. Требуется amendment схемы: добавить `source_kind: canonical-candidate` (или `proposal`) для Draft-нормативных документов. До этого момента интерпретация `canonical` + `status: draft` зафиксирована в данном примечании.

---

## 1. Статус и решение

Этот документ имеет статус **Draft**. Направление владельца по центральному продуктовому тезису — память как основа killer scenario, где food→beauty является одним из нескольких равноправных triggers, — зафиксировано в §2 и §4. Canonical approval и реализация остаются заблокированными до получения cross-functional rulings, перечисленных во frontmatter и §12.

**Решение владельца зафиксировано (2026-07-21):**
> Сценарий «еда → рекомендация в сфере beauty/wellness» закреплён как один из нескольких равноправных контекстных triggers. Он может использоваться как основной демонстрационный пример в маркетинговых и onboarding-материалах, но не определяет центр продукта, domain model или приоритет реализации. Основой продукта остаётся memory-first персонализация на базе явно предоставленных данных, подтверждённых предпочтений, истории взаимодействий и текущего контекста.

---

## 2. Контекст и тезис

### 2.1 Проблема

Ayla работает на рынке, где сама по себе запись является commodity, а универсальная AI memory уже доступна на крупных платформах. Единственная устойчивая дифференциация — **контекстная персонализация, которой доверяют пользователи**: Ayla помнит важное, объясняет, как использует память, и преобразует эту память в полезный следующий шаг без скрытой коммерческой предвзятости.

### 2.2 Тезис (AYLA-DEC-0002)

**Память — основа killer scenario.** Food logging, wellness-сигналы, история посещений и явно заданные предпочтения являются **входными данными** для памяти, а не центром продукта. Killer moment возникает, когда Ayla использует законно сохранённый и ограниченный конкретной целью контекст, чтобы сформировать **одну основную** объяснимую и безопасную рекомендацию, после которой пользователь совершает связанное с ней подтверждаемое полезное действие. Пользователь может запросить альтернативы; каждая альтернатива должна независимо пройти те же privacy, safety, eligibility, relevance и economic-neutrality gates.

### 2.3 Проверка тезиса результатами исследования

Сводные результаты исследований (`00-SYNTHESIS.md`, `02-value-prop-validation.md`, `05-competitive.md`) подтверждают:

- Запись — commodity; YClients/DIKIDI/Alice AI уже покрывают transaction layer.
- «AI, который помнит» становится commodity-функцией (межсессионная память ChatGPT, «Моя память» Алисы).
- Защищаемая ценность заключается в **покрытии + междоменной связности + прозрачности**, а не в количестве сохранённых фактов.
- Окно для создания switching cost за счёт памяти составляет **12–18 месяцев**.

Этот PRD сужает обещание pilot с «food-first superapp» до **memory-first и privacy-visible опыта рекомендаций**, где еда выступает одним из демонстрационных triggers.

---

## 3. Определения

| Термин | Определение |
|---|---|
| **Killer moment** | Формальное атрибутированное событие, в рамках которого Ayla выдаёт одну **основную** рекомендацию с использованием разрешённой сохранённой памяти, показывает пользователю применённый контекст, а пользователь выполняет `qualified_action` в пределах применимого `attribution_window`. Альтернатива, сформированная после уточнения причины отказа и повторно прошедшая все gates, получает собственный `recommendation_id` и может породить отдельный `killer_moment`. Исходная отклонённая рекомендация не считается источником `qualified_action`. |
| **Active user** | Пользователь, у которого было хотя бы одно содержательное взаимодействие с Ayla за скользящие 7 дней, предшествующие событию. Незначительные взаимодействия (например, единственное проигнорированное приветствие) не учитываются. |
| **Intent action** | Пользовательская реакция на рекомендацию, которая ещё не доказывает полученную ценность: открыть, сохранить на потом, запросить альтернативу, уточнить детали. |
| **Qualified action** | Инициированный пользователем и подтверждаемый полезный результат, связанный с рекомендацией: подтверждённая запись по primary или alternative recommendation, принятая и начатая инструкция/план, подтверждённое выполнение определённого первого полезного шага. Само принятие альтернативы является `intent_action`, а не `qualified_action`. Простые клики, просмотры и `save for later` не являются `qualified_action`. |
| **Completed outcome** | Завершённый цикл ценности: запись состоялась, guidance выполнен, пользователь подтвердил пользу. |
| **Attribution window** | Допустимый период между показом рекомендации и связанным с ней `qualified_action`. Зависит от `scenario_type` и типа атрибуции (`direct` / `assisted`). Время само по себе не доказывает attribution; необходима связь с `recommendation_id`. |
| **Direct attribution** | `qualified_action` совершён внутри прямого окна для данного `scenario_type` и связан с `recommendation_id`. |
| **Assisted attribution** | `qualified_action` совершён позже прямого окна, но пользователь явно вернулся к сохранённой рекомендации (`save_for_later`, повторный показ карточки, переход по ссылке), и связь с `recommendation_id` подтверждена. |
| **Unattributed action** | Действие произошло без связи с `recommendation_id`; не является killer moment. |
| **Recommendation role** | Роль рекомендации в диалоге: `primary` — основная, выбранная системой; `alternative` — сформированная после уточнения причины отказа от primary или по запросу пользователя. |
| **Parent recommendation** | Для `alternative` — `recommendation_id` рекомендации, которая предшествовала ей и привела к rerank. |
| **Rerank reason** | Причина, по которой primary recommendation не подошла: цена, время, мастер, локация, стиль услуги, другое. Используется для повторного прохождения Composer с уточнённым constraint. |
| **Substantial Recommendation** | Рекомендация, которая существенно влияет на выбор пользователя, его здоровье, безопасность, privacy или расходы. Для неё необходимы **одновременно**: (а) контекст уровня `declared` или `verified`; (б) допустимость конкретной цели использования согласно действующему `consent_scope`; (в) применимый `lawful basis`. Inferred/signal memory сама по себе не может служить достаточным основанием независимо от разрешения на их обработку. |
| **Useful memory coverage** | Доля active users, имеющих минимально необходимый разрешённый контекст для конкретного сценария, среди active users, **потенциально подходящих** для этого сценария. Пользователи, сознательно выбравшие session-only режим, не считаются «неполными». Измеряет готовность, а не созданную ценность. |
| **Memory fact count** | Диагностическое количество сохранённых записей памяти. Не должно использоваться как цель оптимизации или командный KPI. |

### Разрешённые и запрещённые примеры

- ✅ «Пользователь явно сохранил предпочтение вечерних слотов → Ayla предлагает вечернее окно и объясняет, почему».
- ⛔ «Ayla накопила 50 фактов о пользователе за неделю → это считается успехом продукта».
- ✅ «Пользователь задал правило о поздних ужинах; Ayla использует это правило для планирования времени процедуры, не делая медицинских выводов».
- ⛔ «Ayla вывела дефицит витамина D из фото еды → автоматически рекомендует косметолога без объяснения и без возможности отказа».
- ⛔ «Пользователь отклонил Top-1; Ayla автоматически показывает Top-2 без уточнения причины отказа».

---

## 4. Trigger-сценарии

Food→beauty — **один из четырёх равноправных trigger-сценариев**. В маркетинге и onboarding он может демонстрироваться первым, поскольку является ярким и неожиданным; в архитектуре и реализации он не имеет приоритета перед остальными.

### 4.1 Food interaction с допустимым переходом к отдельному wellness-контексту

**Что может использовать Ayla:** явно предоставленные диетические предпочтения, подтверждённые аллергии, недавний контекст food scan, переданный Ayla для рекомендаций по питанию, а также явно заданные пользовательские правила, связывающие питание и планирование процедур.

**Принцип:** food scan не является самостоятельным основанием для beauty-рекомендации. Сначала Ayla отвечает на непосредственный food intent. Cross-domain влияние допустимо только при наличии явной пользовательской цели, подтверждённого правила или иной объяснимой связи. Простое совпадение по времени не считается релевантностью.

**Пример 1 — явное пользовательское правило с подтверждением inference:**
- Пользователь ранее задал правило: «После поздних плотных ужинов не предлагай мне ранние утренние процедуры».
- Пользователь сканирует поздний ужин.
- Ayla: «Похоже, ужин получился плотным. Применить правило «не ранние утренние процедуры после плотного ужина»?»
- Пользователь подтверждает: «Да».
- Ayla: «Тогда я не предлагаю ранний слот. Хочешь, подберу подходящее время после 12:00?»
- Пользователь соглашается и записывается.

**Пример 2 — сначала food intent:**
- Пользователь сканирует ужин.
- Ayla: «Я сохранила этот ужин. Хочешь посмотреть состав или подобрать более лёгкий завтрак на завтра?»
- Только если пользователь явно переключается на wellness-контекст, Ayla может использовать разрешённую память для подбора процедуры.

### 4.2 Контекст усталости/восстановления → подходящий уход

**Что может использовать Ayla:** явно сообщённое состояние («устала», «болит спина»), подтверждённое предпочтение восстановительных процедур, история принятых рекомендаций по восстановлению.

**Пример:**
- Пользователь говорит: «Опять устала после работы».
- Ayla: «Раньше тебе помогал массаж шеи и спины. Рядом есть окно у Анны сегодня в 19:00. Записать?»

> **Safety/Legal note:** если пользователь сообщает о боли (например, «болит спина»), Ayla сначала проходит boundary check: уточняет признаки, исключает необходимость медицинской помощи и только после этого предлагает немедицинскую wellness-процедуру. Точная формулировка и критерии escalation в S8 должны быть утверждены Safety/Legal до пилота.

### 4.3 Подготовка к событию → расписание процедур

**Что может использовать Ayla:** явно сообщённую дату события, подтверждённые beauty/wellness-предпочтения, историю посещений и их сроки.

**Пример:**
- Пользователь говорит: «Через две недели свадьба подруги».
- Ayla: «До события осталось 14 дней. Если хочешь, могу предложить план процедур с учётом твоих предпочтений и доступных слотов».

### 4.4 История посещений и предпочтения → повторная запись или подбор мастера

**Что может использовать Ayla:** подтверждённого любимого мастера, предпочитаемое время, подтверждённый тип услуги, историю записей.

**Пример:**
- Пользователь говорит: «Хочу записаться к мастеру».
- Ayla: «Ты раньше ходила к Марии на маникюр по четвергам. У неё есть окно в четверг в 18:00. Записать?»

---

## 5. Recommendation Composer

Recommendation Composer — нормативный decision pipeline для любой рекомендации Ayla, использующей сохранённую память. Этапы должны выполняться в указанном ниже порядке. Candidate, исключённый на любом этапе, не может быть возвращён последующими этапами.

### 5.1 Порядок этапов

1. **Consent / privacy gate** — сохранена ли требуемая память в рамках `consent_scope`, охватывающего данную цель? Совместима ли sensitivity zone с этой рекомендацией? Если нет — использовать session-only fallback или запросить разрешение.
2. **Safety gate** — противоречит ли рекомендация safety-critical памяти (аллергии, противопоказания, медицинские ограничения)? Если да — остановить обработку и перейти к S8 Boundary Handling.
3. **Eligibility / availability** — доступен ли provider/service в запрошенное время и в нужной локации? Если нет — исключить.
4. **Relevance** — соответствует ли candidate текущему intent и контексту? Если нет — исключить.
5. **Preference boost** — применить подтверждённые предпочтения (время, мастер, стиль услуги). Предпочтение не должно возвращать candidate, уже исключённый по safety, eligibility или relevance.
6. **Economic-neutrality check** — убедиться, что organic ranking не зависит от коммерческой выгоды Ayla.
7. **Primary output** — выбрать и объяснить **одну основную** рекомендацию. Если пользователь отклоняет primary или запрашивает альтернативу, Ayla фиксирует `rerank_reason`, повторно проходит Composer с уточнённым constraint и формирует `alternative` recommendation с собственным `recommendation_id` и ссылкой на `parent_recommendation`. Система не показывает альтернативы как равноправный каталог по умолчанию; одновременно доступна не более одной primary и до двух alternative рекомендаций.

### 5.2 Примеры исключения на каждом этапе

| Этап | Candidate | Результат |
|---|---|---|
| Consent/privacy | Рекомендация на основе inferred пищевого предпочтения, когда пользователь не дал consent для scope `proactive_recommendation` | Исключён; память не использовать |
| Safety | Рекомендация скраба с моллюсками пользователю с подтверждённой аллергией на моллюсков | Исключён; переход к S8 |
| Eligibility | Рекомендация мастера, у которого нет свободных слотов на этой неделе | Исключён |
| Relevance | Рекомендация услуги для ногтей при intent «боль в спине» | Исключён |
| Preference boost | Два одинаково релевантных мастера; пользователь предпочитает вечер → побеждает вечерний слот | Разрешён |
| Economic-neutrality | Изменение комиссии меняет organic ranking при прочих равных | Генерируется `ranking_economic_neutrality_alert`; выдача блокируется до разбора |

### 5.3 Economic-neutrality check (проверяемое правило)

- Комиссия, маржа, расходы на рекламу или коммерческий статус provider **не должны влиять** на organic recommendation score, порядок кандидатов или выбор primary recommendation.
- Sponsored placement, если оно будет введено позднее, рассчитывается отдельно, явно маркируется и **не заменяет** organic primary recommendation.
- Цена может показываться и использоваться как пользовательский budget filter, но не как скрытый коммерческий ranking signal.
- При равенстве основных оценок применяется утверждённый нейтральный tie-breaker в фиксированном порядке: (1) лучшее соответствие подтверждённым предпочтениям; (2) ближайшее подходящее время; (3) меньшее расстояние; (4) стабильный технический идентификатор provider. Tie-breaker должен быть задокументирован в Recommendation Engine Specification и не должен зависеть от экономических параметров Ayla.

**Counterfactual acceptance test:** Система должна поддерживать воспроизводимый economic-neutrality check: при одинаковом наборе допустимых кандидатов и неизменных пользовательских сигналах изменение только экономического параметра (комиссия, маржа, рекламная оплата, коммерческий статус) не должно менять organic primary recommendation. Проверка может выполняться через online deterministic assertion, shadow evaluation, sampled counterfactual checks или полный прогон в CI / pre-release audit. Двойной синхронный прогон для каждого production-запроса не является обязательным требованием.

**Observability:** Если изменение или удаление экономического параметра меняет organic primary recommendation, система генерирует событие `ranking_economic_neutrality_alert` в observability-контур, определённый ADR-0009. Событие содержит `recommendation_id`, `ranking_model_version`, идентификаторы сравниваемых кандидатов, redacted score breakdown, изменившийся параметр и результаты обоих прогонов. Sensitive user context в событие не включается.

**Operational handling contract (required before pilot):** До запуска pilot должны быть утверждены: severity alert (минимум SEV-1/P0), получатели и SLA подтверждения, разрешённый fallback, механизм приостановки ranking model version, критерии восстановления и обязательный regression test. Recommendation Engine не допускается к production/pilot traffic до утверждения этого контракта.

**Реакция:** Если расхождение обнаружено до показа рекомендации, выдача блокируется и применяется нейтральный fallback. Если влияние обнаружено после показа, инцидент классифицируется как блокирующий для соответствующей версии ranking model; её дальнейшее использование приостанавливается до разбора Architecture Owner и Safety Owner.

---

## 6. Killer Moment

### 6.1 Формальное определение

`killer_moment` — событие, которое одновременно удовлетворяет **всем пяти** условиям:

1. Ayla выдаёт **одну основную рекомендацию** для текущего пользовательского intent.
2. Рекомендация использует **разрешённую сохранённую память/контекст** в рамках применимого `consent_scope`.
3. Ayla **показывает пользователю, какой контекст был применён** (явное объяснение или inline attribution).
4. Пользователь выполняет связанный с рекомендацией `qualified_action`.
5. Действие совершается в пределах применимого `attribution_window`, связано с конкретным `recommendation_id` и классифицируется как `direct` или `assisted` attribution. Для `alternative` рекомендаций событие дополнительно содержит `parent_recommendation_id`, `recommendation_role=alternative` и `rerank_reason`.

### 6.2 Правила атрибуции

- Временная близость сама по себе недостаточна. `qualified_action` должен ссылаться на `recommendation_id` или на принятое дочернее действие, производное от него.
- `attribution_type` принимает значения:
  - `direct` — действие внутри прямого окна для данного `scenario_type`;
  - `assisted` — действие за пределами прямого окна, но с подтверждённой связью к сохранённой рекомендации (`save_for_later`, повторный показ карточки, переход по ссылке);
  - `unattributed` — действие без связи с `recommendation_id`; не является killer moment.
- Если пользователь позднее записывается на ту же услугу, не воспользовавшись рекомендацией, это `unattributed`.
- Если пользователь отклоняет рекомендацию, но позднее самостоятельно возвращается к тому же provider, это `unattributed`.

### 6.3 Attribution window по scenario_type

Начальные значения для pilot (гипотезы, уточняются в Measurement Framework):

| `scenario_type` | Direct window | Assisted limit | Формула direct window |
|---|---|---|---|
| `immediate_slot` / `repeat_booking` | 24 часа | до 7 дней | `recommendation_shown_at + 24h` |
| `recovery_wellness` | 72 часа | до 7 дней | `recommendation_shown_at + 72h` |
| `event_preparation` | до даты события, но не более 14 дней | до даты события | `min(recommendation_shown_at + 14 days, event_at)` |

**Правило `save_for_later`:** `save_for_later` — это не `scenario_type`, а механизм assisted attribution. Он позволяет квалифицировать последующее действие как `assisted`, но **не изменяет** начало и предел attribution window. Предел рассчитывается от `recommendation_shown_at` согласно `scenario_type`. Для `event_preparation` общий максимальный предел assisted attribution — `event_at`, но не более 90 дней от `recommendation_shown_at`.

Действие за пределами direct window может учитываться как `assisted` attribution, только если сохраняется подтверждаемая связь с `recommendation_id`. Временная близость без такой связи недостаточна для attribution.

### 6.4 Повторные killer moments

Для недельной метрики на пользователя повторные killer moments одного `scenario_type` учитываются **не более одного раза за скользящие 7 дней**. Продукту **не запрещается** создавать дополнительные полезные моменты; ограничивается только метрика, чтобы предотвратить gaming.

### 6.5 Пример

- Ayla: «Ты упоминала, что предпочитаешь вечер, и раньше довольна была расслабляющим массажем у Марии. У неё есть окно сегодня в 19:00. Записать?»
- Пользователь: «Да» → запись подтверждена в течение 24 часов.
- Зарегистрировано событие `killer_moment` с `recommendation_id`, `scenario_type=repeat_booking`, `context_used=[preferred_time, favorite_master, service_type]`, `attribution_type=direct`.

---

## 7. Метрики

### 7.1 Иерархия метрик

| Роль | Метрика | Определение | Целевое значение |
|---|---|---|---|
| **Killer Outcome Metric** | `% active users with ≥1 attributed killer moment / rolling 7 days` | Доля active users, которые испытали хотя бы один killer moment за последние 7 дней | ≥ 25% через 60 дней после запуска (гипотеза; требуется baseline pilot) |
| **Leading Product Metric** | `useful_memory_coverage_by_scenario` | Доля active users, имеющих минимально необходимый разрешённый контекст для сценария, среди active users, потенциально подходящих для этого сценария | Определить baseline в pilot; цель роста установить после Measurement Framework |
| **Diagnostic** | `memory_fact_count` | Количество сохранённых записей памяти | Не является целью; используется только для debugging и capacity planning |
| **Diagnostic** | `proposal_conversion_rate` | Подтверждённые пользователем предложения / общее количество показанных предложений | Определить baseline в pilot |
| **Diagnostic** | `rejected_decision_rate` | Отклонённые пользователем предложения / общее количество показанных предложений | Определить baseline в pilot; использовать для настройки anti-spam и cooldown |
| **Diagnostic** | `intent_action_rate` | Доля рекомендаций, вызвавших `intent_action` (сохранить, уточнить, запросить альтернативу) | Baseline в pilot |

### 7.2 Guardrails для killer outcome metric

Цель ≥25% не должна достигаться за счёт доверия. Обязательные guardrail-метрики (Measurement Framework должен детализировать numerator, denominator, eligibility population, event source, deduplication и measurement window):

| Метрика | Numerator | Denominator |
|---|---|---|
| `recommendation_dismissal_rate` | Рекомендации, явно отклонённые пользователем | Все показанные рекомендации, использовавшие persistent memory |
| `memory_disable_rate` | Пользователи, отключившие персонализацию за окно | Active users, у которых была включена персонализация в начале окна |
| `incorrect_context_rate` | Рекомендации с указанием пользователя, что контекст применён неверно | Все показанные рекомендации, использовавшие persistent memory |
| `safety_escalation_rate` | Переходы в S8 Boundary Handling в течение 1 часа после показа рекомендации | Все показанные рекомендации, использовавшие persistent memory |
| `post_recommendation_cancellation_rate` | Подтверждённые записи, отменённые пользователем | Все записи, совершённые после attributed recommendation |
| `why_explanation_dissatisfaction_rate` | Обращения «почему?», по которым пользователь явно выразил недовольство | Все обращения «почему?» по рекомендациям, использовавшим persistent memory |

Если любой guardrail показывает ухудшение, рост killer outcome metric не считается успехом.

### 7.3 Запрещённые формулировки

- ⛔ «Memory enrichment rate: новые факты в неделю» как командный KPI или метрика успеха.
- ⛔ Целевые значения `fill rate`, стимулирующие сбор большего количества фактов, чем минимально необходимо.
- ⛔ Считать `intent_action` (`save_for_later`) завершённым killer moment.

### 7.4 Руководящий принцип

> `useful_memory_coverage_by_scenario` измеряет наличие у пользователя минимального разрешённого релевантного контекста для конкретного сценария. Это показатель готовности к персонализации, **а не** доказательство созданной ценности и **не** искусственный lock-in. Покрытие без полезных рекомендаций — failure mode, а не успех. Пользователи, сознательно выбравшие session-only режим, не считаются «неполными».

---

## 8. Safety, Privacy и прозрачность по 152-ФЗ

### 8.1 152-ФЗ как видимая функция

Прозрачность — не ссылка в footer, а первоклассная поверхность продукта:

- «Что Ayla знает обо мне» — просмотр сохранённой памяти по категориям и consent scope в одно нажатие.
- «Забыть это» — немедленное прекращение использования контекста в рекомендациях и инициирование удаления из active memory одной командой.
- «Почему ты мне это предложила?» — объяснение контекста, использованного для любой рекомендации.

**Уровни удаления:**

| Уровень | Что происходит | Срок |
|---|---|---|
| Немедленное прекращение использования | Контекст исключается из recommendation pipeline | Мгновенно |
| Удаление из active memory | Personal payload удаляется или криптографически уничтожается в соответствии с active-memory deletion policy. Допускается хранение минимального tombstone без исходного значения, если он необходим для предотвращения восстановления, повторного импорта или воспроизведения audit trail. | В рамках policy active memory |
| Backups / logs | Обезличенное/audit-хранение согласно retention policy; логи, содержащие sensitive value, подлежат срокам очистки | Согласно отдельному retention policy |
| Legally retained data | Сохраняется только если это требуется законом или audit obligations | Согласно legal retention |

Пользовательский UX обещает «удалить одной командой» использование и active-memory запись. Технические ограничения backups/legally retained data объясняются прозрачно, но не используются как отказ от удаления.

### 8.2 Совместимость с ADR-0012 v0.2

| Правило ADR-0012 | Следствие для PRD |
|---|---|
| `consent_scope` из versioned registry | Каждая рекомендация должна проверять `consent_scope` (например, `provider_selection`, `intent_understanding`, `question_suppression`, `proactive_recommendation`). Произвольные строки scope запрещены. |
| Inferred/signal memory не является основанием для Substantial Recommendation | Рекомендация food scan → beauty должна формулироваться как мягкое предложение, а не как медицинский или косметологический вывод. |
| Отклонённые предложения создают Decision Record | Отклонение сохраняется как `ProposalDecision` с ограниченным набором полей (topic/purpose, decision, timestamp, cooldown), без восстановления исходного sensitive value. Decision Record сам по себе является персональным данным и подпадает под retention/access/deletion policy. |

### 8.3 Правило безопасности для наблюдений о еде

Наблюдение о еде не должно автоматически превращаться в вывод о здоровье, дерматологический или психологический вывод. Рекомендация должна:

- представляться как мягкое предложение;
- содержать контекст, который её вызвал;
- предлагать явную возможность отказа;
- позволять пользователю исправить контекст;
- позволять пользователю запретить дальнейшее использование этого сигнала.

### 8.4 Типы отказов и их последствия

| Тип отказа | Смысл | Последствие |
|---|---|---|
| «Не сейчас» | Временная неготовность | Cooldown по topic, повторное предложение возможно позже |
| «Покажи другой вариант» | Не устраивает primary, но контекст релевантен | Rerank с уточнённым constraint; показ альтернативы |
| «Мне это не подходит» | Контекст или предположение неверны | Коррекция/удаление контекста; Decision Record |
| «Не используй эти данные» | Отзыв consent для сигнала | Прекращение использования сигнала; удаление применимо |
| «Никогда больше не предлагай эту тему» | Жёсткий отказ | Блокировка topic без повторных предложений; audit |

---

## 9. Вне scope

Следующее явно не входит в scope данного PRD:

- Подробные спецификации реализации Phase 1.5.
- Конкретная реализация Recommendation Composer или слоя хранения Memory.
- Числовые значения TTL/decay (отложены до Measurement Framework и ADR-0012).
- Полные детали governance каталога или trust model providers.
- Медицинская диагностика или рекомендации по лечению.
- Автоматическое определение состояний здоровья по сигналам питания/wellness.
- Финальные формулировки lawful basis, тексты consent и сроки хранения до закрытия соответствующих решений Legal/Privacy (ADR-0012 OD-1, OD-2).

---

## 10. Traceability и acceptance

| Норма PRD | Источник | Acceptance check |
|---|---|---|
| Память — основа; food→beauty — один из triggers | AYLA-DEC-0002 | Review документа; примеры сценариев в PRD |
| Четыре равноправных trigger-сценария | Решение владельца (2026-07-21) | В §4 PRD перечислены четыре сценария с равным статусом |
| Killer moment: одна основная рекомендация + допустимые альтернативы | Ревью v1.1 | UX flow; acceptance test на альтернативы после отказа |
| `qualified_action` не включает `save_for_later` | Ревью v1.1 | Event taxonomy; metric definitions |
| `direct` / `assisted` / `unattributed` attribution | Ревью v1.1 | Event schema; analytics contract |
| Scenario-dependent attribution window | Ревью v1.1 | Measurement Framework; pilot analysis |
| Counterfactual economic-neutrality check | Ревью v1.1 | Ranking audit; `ranking_economic_neutrality_alert` event |
| Consent Scope Registry — required dependency | Ревью v1.1 | Наличие утверждённого registry до использования persistent context |
| Food scan сначала отвечает на food intent | Ревью v1.1 | Red-team cases; conversation QA |
| `useful_memory_coverage_by_scenario` с корректным знаменателем | Ревью v1.1 | Metric definition; dashboard review |
| Guardrails для killer outcome metric | Ревью v1.1 | Dashboard; incident review process |
| Уровни удаления и legally retained data | Ревью v1.1 | Privacy review; deletion test |
| Decision Record как personal data | Ревью v1.1 | Privacy audit; retention/access policy |
| Типы отказов и cooldown | Ревью v1.1 | Conversation design; QA scenarios |
| Inferred не является основанием для Substantial Recommendation | ADR-0012 N-04; Journey §5 | QA red-team cases; ranking audit |
| Decision Record для отклонённых предложений | ADR-0012 OD-10 | Review схемы; privacy audit |
| `consent_scope` из registry | ADR-0012 OD-9 | Consent-scope registry существует до release функции |
| Прозрачность по 152-ФЗ как видимая функция | Constitution Ст. VI, VII; сводка исследований | Review UX-макета; тест удаления одной командой |
| Правило безопасности наблюдений о еде | Решение владельца; Constitution Ст. VIII, XII | Red-team cases; medical/safety review |
| Альтернатива получает собственный `recommendation_id` и может породить killer moment | Ревью v1.2 | Event schema; UX flow; acceptance test |
| Substantial Recommendation требует declared/verified AND consent/lawful basis | Ревью v1.2 | Ranking audit; QA red-team |
| Food interaction — отдельный wellness-контекст или явное пользовательское правило | Ревью v1.2 | Conversation QA; red-team |
| `save_for_later` — механизм assisted attribution, не scenario_type | Ревью v1.2 | Event taxonomy; analytics contract |
| Формула `event_preparation` direct window: `min(recommendation_shown_at + 14 days, event_at)` | Ревью v1.2 | Analytics implementation; pilot validation |
| Утверждённый нейтральный tie-breaker | Ревью v1.2 | Recommendation Engine Specification |
| Operational handling contract для economic-neutrality alerts | Ревью v1.2 | Operational Playbook; pre-pilot checklist |
| Personal payload удаляется/уничтожается; tombstone без исходного значения | Ревью v1.2 | Privacy review; deletion test |
| Decision Record — personal data с retention/access/deletion | Ревью v1.2 | Privacy audit |
| Типология отказов и разные cooldown/consequences | Ревью v1.2 | Conversation design; QA scenarios |

---

## 11. Проверка согласованности

### 11.1 С Ayla Constitution v2.2

- **Ст. IV (economic neutrality):** Composer включает явный counterfactual economic-neutrality check и observability event. ✅
- **Ст. VI (минимально необходимые знания):** метрики сосредоточены на useful coverage, а не на накоплении фактов. ✅
- **Ст. VII (объяснение и veto):** killer moment требует объяснения использованного контекста; прозрачность по 152-ФЗ обеспечивает удаление одной командой. ✅
- **Ст. X (уместность):** proactive recommendations используют consent_scope и cooldowns сценариев. ✅
- **Ст. XIV (автономия):** пользователь может отказаться, исправить или запретить любой сигнал. ✅

### 11.2 С Ayla Decision Log

- **AYLA-DEC-0002:** память — основа; food→beauty — один из triggers. ✅
- **AYLA-DEC-0001 / AYLA-DEC-0004:** конфликтов нет; privacy-first design сохранён. ✅

### 11.3 С Ayla User Journey Specification v1.2

- **§5 Memory Interaction:** согласовано с Memory Proposal flow; inferred/signal не является основанием для Substantial Recommendation. ✅
- **§6 Proactivity:** Proactive Readiness Gate соблюдён; требуется consent_scope. ✅
- **§13 Metrics:** `useful_memory_coverage` заменяет любые цели по количеству фактов. ✅

### 11.4 С ADR-0012 v0.2

- Multi-dimensional memory model является целевой reference architecture. ✅
- Требование к registry `consent_scope` учтено (OD-9). ✅
- Decision Record для отклонённых предложений учтён (OD-10). ✅
- OD-1 и OD-2 перечислены как блокеры канонизации и не обходятся. ✅

### 11.5 С Wave 0 / pilot contracts

- Этот PRD не изменяет frozen pilot contracts или контракт 12 green fields.
- Реализация новой схемы или backfill помечена как post-pilot / отдельный amendment. ✅

### 11.6 Вывод

Новых неразрешённых конфликтов, кроме перечисленных блокеров, не обнаружено. Канонизация PRD заблокирована до закрытия OD-1, OD-2 и утверждения Consent Scope Registry (OD-K9). Реализация и pilot дополнительно заблокированы до утверждения operational handling contract для economic-neutrality alerts (OD-K10).

---

## 12. Требуемые решения владельца и зависимости

| ID | Вопрос | Направление владельца зафиксировано? | Блокер канонизации? |
|---|---|---|---|
| OD-K1 | Приоритет сценариев: B — четыре равноправных triggers, food→beauty как демонстрационный пример | ✅ Да | Нет |
| OD-K2 | Атрибуция killer moment требует связи через `recommendation_id` | ✅ Да | Нет |
| OD-K3 | Economic-neutrality check как проверяемое правило ranking | ✅ Да | Нет |
| OD-K4 | `useful_memory_coverage` — leading metric, а не North Star | ✅ Да | Нет |
| OD-K5 | Прозрачность по 152-ФЗ как видимая функция | ✅ Да | Нет |
| OD-K6 | Медицинские/health inference из пищевых сигналов находятся вне scope | ✅ Да | Нет |
| OD-K7 | Primary recommendation ≠ единственная; альтернативы по запросу/причине отказа | ✅ Да | Нет |
| OD-K8 | Scenario-dependent attribution window (direct/assisted) | ✅ Да | Нет |
| OD-K9 | Consent Scope Registry — required dependency до использования persistent context | ✅ Да | **Да (канонизация + реализация + pilot)** |
| OD-K10 | Operational handling contract для `ranking_economic_neutrality_alert` — required before pilot | ✅ Да | **Да (только pilot / production traffic)** |
| OD-K11 | Amendment `.knowledge/schema.yaml` для `source_kind: canonical-candidate` | ✅ Да | Нет |
| OD-1 (ADR-0012) | Legal ruling о разделении чувствительности данных о диете/религии | ⏳ Ожидает legal review | **Да (канонизация + реализация)** |
| OD-2 (ADR-0012) | Решение Privacy/Safety/Legal + amendment ADR-0011 по хранению safety-critical данных | ⏳ Ожидает cross-functional ruling | **Да (канонизация + реализация)** |

### 12.1 Required dependency: Consent Scope Registry

До начала реализации Recommendation Composer с использованием реального пользовательского контекста **User Context Domain Owner совместно с Privacy Owner** должны создать и утвердить versioned `consent-scope-registry.md`.

Initial registry должен как минимум определить scopes для:

- `provider_selection`;
- `proactive_recommendation`;
- `intent_understanding`.

Для каждого scope должны быть определены:

- стабильный машинный идентификатор;
- понятное пользователю описание цели;
- разрешённые категории данных;
- допустимые consumers и операции;
- запрещённые способы использования;
- срок действия и правила повторного подтверждения;
- правила отзыва consent;
- влияние отзыва на active memory и future recommendations;
- совместимость и миграция версий;
- audit events;
- владелец scope.

Recommendation Composer не может использовать persistent user context, если требуемый scope отсутствует в утверждённой версии registry, отозван, истёк либо не покрывает конкретную цель обработки. В таком случае применяется session-only или no-personalization fallback.

### 12.2 Required dependency: Operational handling contract for economic-neutrality alerts

До запуска pilot **Recommendation Engine Owner совместно with Architecture Owner и Safety Owner** должны утвердить operational handling contract для `ranking_economic_neutrality_alert`, включающий:

- severity (минимум SEV-1/P0);
- получателей alert и канал доставки;
- SLA подтверждения и разбора;
- разрешённый fallback при блокировке выдачи;
- механизм приостановки и восстановления ranking model version;
- обязательный regression test после исправления;
- владельца закрытия инцидента.

Recommendation Engine не допускается к production/pilot traffic до утверждения этого контракта.

---

## 13. Открытые вопросы

1. **Baseline-значения pilot:** каковы baseline для `useful_memory_coverage_by_scenario`, `proposal_conversion_rate` и доли killer moments до установки числовых целей? *(Отложено до получения данных pilot и Measurement Framework.)*
2. **Таксономия scenario type:** следует ли уже сейчас формализовать trigger-сценарии как enum в analytics schema или отложить это до Recommendation Engine Specification? *(Предложение: определить enum в analytics schema, сохранив возможность уточнения.)*
3. **Граница sponsored placement:** если sponsored placement появится после pilot, какой документ будет владеть правилом, запрещающим ему заменять organic primary recommendation? *(Предложение: отдельный Commercial Policy ADR.)*
4. **`source_kind` для Draft-нормативных документов:** требуется amendment `.knowledge/schema.yaml`, чтобы добавить значение `canonical-candidate` (или `proposal`) и разрешить машинно проверяемое различие между действующим каноном и Draft-кандадатом. *(Owner: Knowledge Architecture / W7.)*

---

## 14. Change Log

### v1.3.1 — 2026-07-22

- Удалено «принятая безопасная альтернатива» из `qualified_action`; принятие альтернативы — `intent_action`, killer moment требует квалифицированного действия по альтернативе.
- Уточнена формула Substantial Recommendation: `declared`/`verified` AND valid processing purpose AND applicable `lawful basis`.
- Исправлен food-trigger: inference о «плотном ужине» подтверждается пользователем перед применением правила.
- Уточнено правило `save_for_later`: оно не продлевает attribution window; предел рассчитывается от `recommendation_shown_at` по `scenario_type`.
- Согласованы статусы блокеров во frontmatter, §11.6 и §12: OD-K9 — канонизация + реализация + pilot; OD-K10 — только pilot/production; OD-K11 — не блокер.
- Guardrail-метрики дополнены таблицей numerator/denominator.
- Добавлен Safety/Legal note к примеру с болью/массажем.
- Обновлены traceability и change log.

### v1.3 — 2026-07-22

- Устранено противоречие вокруг альтернатив: альтернатива, сформированная после уточнения причины отказа и повторно прошедшая все gates, получает собственный `recommendation_id` и может породить отдельный `killer_moment`.
- Введены поля `recommendation_role`, `parent_recommendation_id`, `rerank_reason`.
- Исправлено условие Substantial Recommendation: требуется `declared`/`verified` контекст **AND** действующий `consent_scope`/lawful basis; consent сам по себе не легитимизирует inferred memory.
- Переименован сценарий §4.1 и исправлены примеры: food scan не является основанием для beauty-рекомендации; cross-domain влияние допустимо только через явное пользовательское правило.
- Разделены `scenario_type` и `save_for_later`: `save_for_later` — механизм assisted attribution, а не сценарий.
- Добавлена вычислимая формула для `event_preparation` attribution window.
- Уточнён tie-breaker: фиксированный утверждённый порядок вместо примеров.
- Economic-neutrality check дополнен operational handling contract как required dependency before pilot.
- Уточнено удаление из active memory: personal payload удаляется/уничтожается, допускается tombstone без исходного значения.
- Уточнены guardrail-метрики: знаменатели и измеримые сигналы.
- Добавлены OD-K10 и OD-K11; source_kind schema conflict зафиксирован как требующий amendment схемы.
- Обновлены traceability, acceptance checks, open questions и consistency review.

### v1.2 — 2026-07-21

- Исправлено смешение понятий: введено разделение между primary recommendation (UX), Top-1 (ranking engine) и single recommendation (единственный вариант).
- Добавлено правило: Ayla показывает одну основную рекомендацию, но до двух альтернатив доступны по запросу пользователя или после уточнения причины отказа.
- Переработана атрибуция killer moment: введены `direct`, `assisted` и `unattributed` attribution; attribution window стало зависимым от `scenario_type`.
- Исправлен пример food→beauty: Ayla сначала отвечает на food intent; cross-domain предложение допустимо только при реальной объяснимой связи.
- Уточнён economic-neutrality check: введён counterfactual test, observability event `ranking_economic_neutrality_alert` и блокировка при обнаружении влияния.
- Разделены `intent_action`, `qualified_action` и `completed_outcome`; `save_for_later` исключён из `qualified_action`.
- Добавлены guardrail-метрики для killer outcome metric.
- Уточнён `useful_memory_coverage_by_scenario` с корректным знаменателем.
- Добавлены уровни удаления памяти (immediate stop, active memory, backups, legally retained).
- Уточнено, что Decision Record сам по себе является персональным данным.
- Добавлена типология отказов и их последствий.
- Consent Scope Registry повышен из Open Question до required dependency.
- Обновлены traceability, acceptance checks, owner decisions и open questions.
- `data_sensitivity` повышено до `high`, добавлена категория `health`, `security_sensitivity` повышено до `medium`.

### v1.1 — 2026-07-21

- Документ переработан из `PRD_Ayla_Killer_Scenario_v1.0.md` в соответствии с AYLA-DEC-0002.
- Память закреплена как основа; food→beauty понижен до одного из четырёх равноправных trigger-сценариев.
- `memory_enrichment_rate` удалён из целевых KPI.
- Добавлено формальное определение `killer_moment` из 5 условий с атрибуцией по `recommendation_id`.
- Метрики разделены на Killer Outcome Metric, Leading Product Metric и diagnostics.
- Добавлен нормативный порядок этапов Recommendation Composer с примерами исключения.
- Economic-neutrality check сделан проверяемым.
- Прозрачность по 152-ФЗ добавлена как видимая функция.
- Выполнено согласование с ADR-0012 v0.2: registry `consent_scope`, правило inferred-not-basis, Decision Record для отклонённых предложений.
- Явно добавлено в out of scope: медицинская диагностика, health inference из пищевых сигналов, финальные lawful basis/consent/retention до решений Legal/Privacy.
- Добавлены traceability, проверка согласованности, решения владельца и открытые вопросы.

---

**Конец документа — Killer PRD v1.3.1**
