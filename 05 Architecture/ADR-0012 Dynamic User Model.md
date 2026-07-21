---
node_id: ayla.architecture.adr-0012-dynamic-user-model
title: ADR-0012 Dynamic User Model
aliases:
  - ADR-0012
  - ADR-0012 Dynamic User Model
  - Dynamic User Model
adr_id: ADR-0012
type: adr
status: draft
decision_status: proposed
revision: 1
version: "0.2"
amendments: []
superseded_by: null
owner: Product Architecture
priority: P0
knowledge_area:
  - architecture
domain:
  - user-context
  - cross-domain
concerns:
  - privacy
  - safety
  - governance
  - explainability
  - audit
system_owner:
  - ayla-user-context
source_repository: ayla-knowledge
created: 2026-07-21
updated: 2026-07-21
source_kind: canonical
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
tags:
  - ayla
  - ayla/architecture
  - ayla/adr
  - adr/0012
  - type/adr
  - priority/p0
implements:
  - "[[Ayla Constitution]]"
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Glossary]]"
  - "[[Ayla Decision Log]]"
  - "[[Ayla User Journey Specification]]"
related:
  - "[[Ayla Knowledge Architecture Specification]]"
review_cycle: event-driven
---

# ADR-0012 Dynamic User Model

## Статус

**Статус документа:** Draft (pending legal and cross-functional rulings)
**Статус решения:** Proposed — owner directions recorded; canonical approval pending.
**Версия:** 0.2 (2026-07-21)

Этот документ — Draft v0.2, подготовленный Knowledge/Canon Architect (W7) по
GO владельца от 2026-07-21 и review оркестратора. Owner rulings по
OD-1…OD-10 зафиксированы. Канонизация заблокирована до legal review по OD-1,
совместного Privacy/Safety/Legal решения и amendment ADR-0011 по OD-2. До
канонизации нормативными остаются [[Ayla Constitution]] (v2.2), целевые
положения [[Ayla User Journey Specification]] (v1.2, Review) и действующие
контракты пилота.

**Владельцы документа:**

- Владелец решения (GO/NO-GO): Founder / Product Architecture.
- Владелец документа (draft): Knowledge/Canon Architect (W7).
- Профильные владельцы сверки: User Context Domain, Privacy and Safety,
  Safety Owner.

## Контекст

Память — центр killer-сценария Ayla («Ayla помнит и понимает меня»,
AYLA-DEC-0002). При этом знания о пользователе сегодня описаны двумя
разными словарями, которые без сводящего решения рискуют стать двумя
несовместимыми моделями памяти:

1. **Sensitivity-зоны** (`green` / `yellow` / `red`) — канон приватности и
   хранения из ADR-0011 (`ai-bot-platform`
   `docs/adr/ADR-0011-user-personal-context-privacy.md`): основания согласия,
   шифрование, retention, аудит доступа, кросс-тенантные границы.
2. **Классы знаний Journey v1.2** (`verified_identity`, `persistent_safety`,
   `time_bounded_safety`, `stable`, `ephemeral`, `hypothesis`) — draft-таблица
   [[Ayla User Journey Specification]] §5 «What Ayla Remembers», помеченная как
   `Proposed классы знаний (planned source: ADR-0012)` вместе с MVP Memory
   Heuristic и Proactive Readiness Gate.

Draft-классы Journey смешивают разные оси в одном списке: `verified_identity`
кодирует способ подтверждения, `persistent_safety` — предмет и срок,
`stable` — срок, `ephemeral` — срок, `hypothesis` — степень достоверности.
Из-за этого невозможно выразить простые состояния без новых классов:
«подтверждённая гипотеза», «временный safety-факт от провайдера»,
«устойчивое, но неподтверждённое предпочтение».

Дополнительные факторы контекста:

- Конституция (Ст. V, VI, VII, IX, X, XIV) требует различать источник, цель
  использования, надёжность, актуальность и допустимую область доступа каждого
  знания, отделять гипотезы от фактов и не превращать прошлое пользователя в
  вечный застывший профиль.
- Реализация пилота уже работает: bot-side `MemoryEntry` (зоны, `source`
  `explicit`/`inferred`/`signal`, `kind`), Ayla-side 12 declared-полей по
  frozen-контракту v1.0, consent-гейт `memory_green`. Модель обязана
  мигрировать из этого состояния, а не игнорировать его.
- Владелец прямо запретил вводить вторую модель памяти параллельно ADR-0011
  и потребовал ортогональные измерения вместо списка классов.

## Решение

### Принцип: одна модель, ортогональные измерения

В системе существует **одна модель памяти**. Каждая Memory Entry описывается
точкой в декартовом произведении независимых осей:

- **sensitivity_zone** (`green` / `yellow` / `red`) — ось приватности и
  хранения. Канон — ADR-0011; настоящий ADR её не изменяет (норма N-10).
- **Измерения знания** (вводятся настоящим ADR): `knowledge_class`,
  `confidence`, `lifetime`, `provenance`.
- **Атрибуты состояния** записи: `memory_status`, `storage_scope`,
  `consent_scope`.

Зоны и измерения ортогональны: зона отвечает на вопрос «насколько
чувствительно содержимое и каковы правила согласия, шифрования, retention и
доступа», измерения — «что это за знание, насколько оно подтверждено, как
долго актуально и откуда взялось». Ни одно измерение не назначает зону; зона
назначается по содержимому записи per ADR-0011 §4. Ни одна зона не заменяет
измерения: `green`-запись может быть гипотезой, `red`-запись — подтверждённым
persistent-фактом.

Подтверждённая гипотеза — **не новый класс**, а комбинация измерений, например:
`knowledge_class=preference`, `confidence=declared`,
`provenance=confirmed_proposal`.

### Измерение 1: `knowledge_class` — о чём знание

| Значение | Семантика | Примеры |
|---|---|---|
| `identity` | Атрибуты идентичности и связанные идентификаторы. Исправляемые; `verified` не означает «истина навсегда» | Дата рождения, связанный channel ID |
| `safety` | Safety-critical сведения: ошибка, игнорирование или преждевременное забывание создаёт риск здоровью/безопасности | Подтверждённая аллергия, беременность, приём лекарств, safety-наблюдение провайдера (Конституция Ст. III.4) |
| `preference` | Устойчивые предпочтения, влияющие на подбор и персонализацию | Любимый Specialist, предпочтительное время, район, бюджет, диета как предпочтение |
| `context` | Ситуативный контекст, релевантный ограниченное время | «Завал на работе», «в отпуске», временные семейные обстоятельства |
| `unclassified` | Техническое состояние, когда предмет знания ещё не определён. Не допускается как постоянный класс; должен быть уточнён при подтверждении | Начальный proposal, из которого система ещё не вывела предмет |

### Измерение 2: `confidence` — насколько знание подтверждено

| Значение | Семантика |
|---|---|
| `verified` | Подтверждено определённым методом верификации помимо слов пользователя (системный linkage, профессиональное подтверждение). Метод верификации обязателен в provenance-метаданных записи; реестр допустимых методов — open question (OQ-1), до его утверждения `verified` применяется только к identity-linkage |
| `declared` | Прямо сообщено пользователем или подтверждено им (включая подтверждение Memory Proposal) |
| `inferred` | Выведено системой из сообщений, поведения или событий; не подтверждено пользователем |

Инвариант: `knowledge_class` не хранит эпистемическое состояние. Неподтверждённое
предположение о предпочтении выражается как `knowledge_class=preference`,
`confidence=inferred`, `memory_status=proposed`. Подтверждение меняет
`confidence`, `provenance` и `memory_status`, но не предмет знания (N-05).

### Измерение 3: `lifetime` — как долго знание актуально

| Значение | Семантика |
|---|---|
| `until_changed` | Актуально до исправления, отзыва или замены; подлежит переподтверждению по N-06/N-09. **Не отменяет zone retention cap** (N-10): эпистемическая устойчивость ≠ бессрочное хранение |
| `time_bounded` | Имеет ожидаемый срок актуальности; к границе срока — переподтверждение или прекращение использования. Временные состояния не сохраняются бесконечно без перепроверки (Конституция Ст. IX) |
| `ephemeral` | Короткий ситуативный контекст (design candidate: 14–30 дней, Journey §5). Не становится основанием долгосрочных выводов о пользователе |

`lifetime` — ось релевантности (когда переспрашивать и прекращать
использование), а не ось удаления. Удаление регулируется зоной (ADR-0011 §5)
и правами пользователя (ADR-0011 §8, контракт C5).

### Измерение 4: `provenance` — откуда знание возникло

| Значение | Семантика | Соответствие существующих словарей |
|---|---|---|
| `explicit_answer` | Прямой ответ или сообщение пользователя | `MemoryEntry.source=explicit`; contract sources `explicit`, `conversational` |
| `imported` | Импорт из внешней или смежной системы на явном основании (устройства, миграции, cross-system import). Основание импорта фиксируется в provenance-метаданных | Резерв для Phase 1+ (wearables, внешние источники — Конституция Ст. VI: подключаются отдельно и добровольно) |
| `observed_event` | Наблюдаемое событие, надёжно зафиксированное системой: запись к специалисту, отмена, поведение в приложении, safety-наблюдение провайдера (Ст. III.4). Набор событий может служить `evidence_refs`, но их интерпретация как паттерна/предпочтения — это `model_inference`. Само по себе событие не объясняет мотивов | `MemoryEntry.source=signal`; contract sources `behavioral`, `transactional` |
| `model_inference` | Вывод Ayla из одного или нескольких `observed_event` с помощью модели/правила. Обязательны ссылки на `evidence_refs` и `derivation_method` | `MemoryEntry.source=inferred` |
| `confirmed_proposal` | Memory Proposal, подтверждённый пользователем. Исходное provenance сохраняется в истории записи (N-05) | Состояние `confirmed` из Journey Stage 6 |

Бывший плоский `source=inferred` (код, Glossary «Memory Source») на уровне
модели разлагается: вывод Ayla — это `confidence=inferred` +
`knowledge_class=<предмет>` + `provenance=model_inference`, основанный на
`observed_event` (событиях). Кодовый enum `source` остаётся без изменений до
миграции схемы (§«Миграция от текущей реализации»); конфликта моделей нет,
есть отображение.

Для `model_inference` обязательны метаданные:
- `evidence_refs` — события/сообщения, на которых основан вывод;
- `derivation_method` — правило или модель, сформировавшая гипотезу.
Это требование N-13 (объяснимость) и N-02 (audit trail для inferred-записей).

### Атрибуты состояния записи

Не являются измерениями содержания — описывают положение записи в её
жизненном цикле (канонизация полей из Journey Stage 6 «Memory Proposal»):

- `memory_status`: `proposed` → `confirmed` | `confirmation_required`
  (устаревание/противоречие, N-06/N-09) | `superseded` (замещён исправлением
  или более новым значением, N-12).
- **Decision record (proposal rejection):** когда пользователь отклоняет
  proposal, сама Memory Entry не создаётся. Создаётся минимальный
  `ProposalDecision`/`ConsentDecision` без персонального значения:
  тема/purpose, решение (`rejected`), timestamp, cooldown-метаданные.
  Это обеспечивает anti-spam, audit согласия и право пользователя видеть
  историю отказов (ADR-0011 §8). Повторный вопрос по той же теме подчиняется
  правилам ask-eligibility (frozen-контракт, cooldown 24ч, skip×2 → пауза).
- `storage_scope`: `session` (только Session Context текущего взаимодействия)
  / `persistent` (Persistent Memory). Исход Consent Check по N-02.
- `consent_scope`: набор purpose-ключей из **versioned consent-scope registry**,
  в пределах которых запись может использоваться (пример:
  `provider_selection`). Использование вне `consent_scope` запрещено (N-07).
  Конкретный список purpose-ключей утверждается отдельным контрактом; до
  утверждения registry реализацию `consent_scope` начинать нельзя.

### Пример жизненного цикла (нормативная иллюстрация)

1. Пользователь трижды записывается на вечер → создаётся **только** Memory
   Proposal: `knowledge_class=preference`, `confidence=inferred`,
   `lifetime=time_bounded`, `provenance=model_inference`
   (на основе `observed_event`: три записи), `memory_status=proposed`,
   `storage_scope=session` (N-02).
2. Ayla уточняет: «Похоже, тебе удобнее вечером. Сохранить это для будущих
   подборок?» Пользователь подтверждает → запись становится
   `knowledge_class=preference`, `confidence=declared`,
   `lifetime=until_changed`, `provenance=confirmed_proposal` (исходный
   `model_inference` и `evidence_refs` сохранены в истории),
   `memory_status=confirmed`, `storage_scope=persistent`,
   `consent_scope=[provider_selection]`, `sensitivity_zone=green` (N-05).
3. Год спустя перед существенным использованием устаревшего факта Ayla
   переспрашивает (N-09). Пользователь: «теперь мне удобнее утром» →
   исправление: старая запись `superseded`, новая — `declared` /
   `explicit_answer` (N-12).
4. Если бы пользователь не подтвердил proposal на шаге 2 — Persistent Memory
   не создавалась бы; молчание не трактовалось бы как согласие (N-03).

### Нормы

Каждая норма содержит формулировку, источник (traceability), где проверяется
и пару «разрешено / запрещено». Проверки, помеченные *design candidate*, —
предлагаемые acceptance-сценарии; они вводятся вместе с канонизацией этого
ADR, а не существуют сегодня.

#### N-01. Единая модель памяти

Зоны ADR-0011 и измерения ADR-0012 — ортогональные оси **одной** Memory Entry.
Запрещено вводить параллельные модели, профили или классификации памяти, не
сводимые к этим осям.

- **Источник:** решение владельца 2026-07-21 (бриф W7); ADR-0011 §4;
  Конституция Ст. V (федеративная модель пользователя).
- **Проверка:** *design candidate* — schema review при реализации §«Миграция»;
  любой новый документ/код, вводящий классификацию памяти, обязан ссылаться на
  этот ADR.
- ✅ Разрешено: запись с `sensitivity_zone=yellow`,
  `knowledge_class=preference`, `confidence=declared`,
  `lifetime=until_changed`, `provenance=explicit_answer` — один набор осей над
  одной записью.
- ⛔ Запрещено: отдельный «профиль предпочтений» с собственной шкалой
  надёжности, не маппируемой на `confidence`, или отдельный «граф знаний»,
  не маппируемый на зоны и измерения.

#### N-02. Proposal-first: только Memory Proposal входит в память

Любое сообщение, событие или вывод сначала создаёт **только** Memory Proposal.
Persistent Memory создаётся, только если пройдены Sensitivity Check, Purpose
Check и Consent Check. Explicit save request («запомни, что мне удобно утром»)
также проходит состояние `proposed`, но может быть подтверждён в том же
сообщении пользователя, не требуя дополнительного вопроса. Session Context
only (`storage_scope=session`) допустим, но не отменяет Sensitivity, Purpose,
access и lawful-basis checks (запрещено «облегчённое» согласие для yellow/red
только из-за кратковременности или ephemeral-статуса).

- **Источник:** Journey §5 «When Memory is Created» (обязательный flow),
  Journey Stage 6 «Memory Proposal»; Конституция Ст. VI (минимально
  необходимые знания), Ст. XIV (разделение согласий).
- **Проверка:** acceptance-сценарий пилота №7 «вопрос → ответ сохранён →
  следующая рекомендация учла (consent-гейт)» (PILOT_CONTRACTS §10);
  consent-гейт `memory_green` (PERSONAL_CONTEXT contract, блок «Аутентификация»).
- ✅ Разрешено: «я веган» → proposal (`provenance=explicit_answer`) → проверки
  пройдены → `storage_scope=persistent`, `consent_scope=[provider_selection]`.
- ✅ Разрешено: «запомни, что мне удобно утром» → proposal
  (`provenance=explicit_answer`) → то же сообщение подтверждает →
  `memory_status=confirmed` после checks.
- ⛔ Запрещено: сигнал «3 вечерние записи подряд» записывается напрямую в
  Persistent Memory, минуя proposal и Consent Check.
- ⛔ Запрещено: чувствительная yellow/red-гипотеза сохраняется в Session Context
  без sensitivity/purpose/lawful-basis checks, только потому что
  `lifetime=ephemeral`.

#### N-03. Молчание ≠ согласие

Молчание, бездействие, продолжение диалога, отмена или выбор другого варианта
не трактуются как согласие на профилирование, сохранение гипотез, отказ от
цели или изменение устойчивого предпочтения. Согласие на историю сообщений не
является согласием на память.

- **Источник:** Journey §5 «When Memory is Created», Stage 6 «Learning
  Signals» (неявные сигналы); Конституция Ст. VII (Неявные сигналы),
  Ст. XIV; Glossary «Consent».
- **Проверка:** acceptance пилота №7 (только явный ответ сохраняется);
  поведение skip/abandon в `apps/orchestrator/memory_ask.py` (W5): явный skip
  → `/skip/`, неразобранный ответ → тихий abandone без записи.
- ✅ Разрешено: пользователь не ответил на feedback-вопрос → релевантность
  гипотезы не меняется, новых выводов не создаётся.
- ⛔ Запрещено: отсутствие ответа на «Сохранить как предпочтение?» трактовать
  как «да» и персистить запись.

#### N-04. `inferred` и `signal` — не самостоятельное основание Substantial Recommendation

Записи с `confidence=inferred` и/или `provenance=model_inference` не могут
быть единственным основанием Substantial Recommendation. Допустимо: несущественная
персонализация с вероятностным языком и уточнением; для существенного —
требуется `declared`/`verified` корроборация или подтверждение пользователя.

- **Источник:** Journey §5, MVP Memory Heuristic п.4; Конституция Ст. VII
  (гипотезы, вероятностный язык), Ст. V (гипотезы отделены от фактов);
  Glossary «Substantial Recommendation».
- **Проверка:** *design candidate* — acceptance «объяснение существенной
  рекомендации не опирается только на inferred/signal» (Recommendation
  Explanation contract, Phase 1).
- ✅ Разрешено: «Похоже, тебе удобнее вечером — показать вечерние слоты?»
  (несущественная персонализация с уточнением).
- ⛔ Запрещено: предложить курс процедур (существенная рекомендация) только
  потому, что из поведения выведено «кожа в порядке» или «бюджет позволяет».

#### N-05. Подтверждённая гипотеза трансформируется с сохранением provenance

При подтверждении пользователем гипотезы предмет знания не меняется:
`knowledge_class=preference` (или `safety`/`context`). Изменяются
`confidence: inferred → declared`, `provenance: model_inference →
confirmed_proposal`, `memory_status: proposed → confirmed`. Исходные значения
`model_inference`, `evidence_refs` и `derivation_method` сохраняются в истории
записи.

- **Источник:** Journey §5, MVP Memory Heuristic п.5; Journey Stage 6
  (yaml `provenance_preserved: true`); решение владельца 2026-07-21 (бриф 2.1).
- **Проверка:** acceptance пилота №7 (flow «ответ → сохранено → учтено»);
  *design candidate* — тест трансформации состояния в `memory_writer`.
- ✅ Разрешено: proposal о вечернем предпочтении (`preference/inferred/
  model_inference`) → подтверждена → `preference/declared/confirmed_proposal`,
  исходный `model_inference` и evidence — в истории записи.
- ⛔ Запрещено: менять `knowledge_class` при подтверждении (например, с
  `hypothesis` на `preference`) или стирать след того, что знание было выводом
  модели.

#### N-06. Safety-critical сведения не удаляются по давности

Записи `knowledge_class=safety` не удаляются автоматически только из-за
давности. Устаревание переводит их в `memory_status=confirmation_required`;
перед существенным использованием — переподтверждение. При ручном удалении
Ayla объясняет последствия, после чего сведения прекращают использоваться.
Коллизия этой нормы с red-zone TTL (90 дней, ADR-0011 §5) не разрешена в этом
ADR и вынесена в «Owner decision required» (OD-2).

- **Источник:** Конституция Ст. IX (Safety-critical сведения); Journey §5,
  MVP Memory Heuristic п.2–3; Glossary «Safety-Critical Information».
- **Проверка:** *design candidate* — acceptance «safety-запись с истёкшим
  сроком → confirmation_required + переспрос, а не молчаливое удаление».
- ✅ Разрешено: подтверждённая аллергия не использовалась 6 месяцев →
  `confirmation_required`, уточнение при следующем релевантном действии.
- ⛔ Запрещено: sweep-job удаляет подтверждённую аллергию только потому, что
  прошло N дней без событий (для red-зоны — нерешённая коллизия, OD-2).

#### N-07. Использование только в пределах purpose и consent

Persistent Memory используется только в пределах `consent_scope` и цели, для
которых запись сохранена: персонализация рекомендаций (Stage 4), понимание
намерения (Stage 3), пропуск повторяющихся вопросов (Stage 2). Новая цель
требует нового основания.

- **Источник:** Journey §5 «When Memory is Used»; Конституция Ст. V (цель
  использования), Ст. VI (новая цель — новое основание), Ст. XIV.
- **Проверка:** `consent_scope` в Memory Proposal (Journey Stage 6);
  *design candidate* — аудит-записи использования памяти содержат purpose.
- ✅ Разрешено: предпочтение времени, сохранённое с
  `consent_scope=[provider_selection]`, фильтрует слоты при подборе.
- ⛔ Запрещено: использовать то же предпочтение для маркетинговой рассылки
  или новой цели без отдельного основания.

#### N-08. Минимально необходимое покрытие, а не накопление

Цель памяти — **минимально необходимое покрытие релевантного контекста**,
достаточное для безопасной и полезной помощи. Накопление фактов не является
продуктовой или инженерной целью; сбор «на будущее» без понятной цели
запрещён. Детальные KPI — отдельный Measurement Framework, не этот ADR
(§«Принцип метрик»).

- **Источник:** решение владельца 2026-07-21 (бриф 2.4); Конституция Ст. VI;
  Journey §5 «What Ayla Remembers»; AYLA-DEC-0002 (moat — понимание, а не
  объём сбора).
- **Проверка:** Measurement Framework (отдельный документ, вне scope).
- ✅ Разрешено: перед созданием proposal — проверка «нужен ли этот факт для
  текущей или предвидимой помощи»; отказ от сохранения при отрицательном
  ответе.
- ⛔ Запрещено: цель вида «число записей памяти на пользователя» или
  «полнота профиля %» как метрика успеха команды.

#### N-09. Вопрошание памяти; decay engine отложен с критерием включения

Канонизируются триггеры переподтверждения из Journey §5 «When Memory Must be
Questioned»: противоречие; истёк срок актуальности; факт временный,
изменяемый или safety-critical и используется для существенного решения.
Числовые пороги `current_relevance` (< 0.3 — переспрос; < 0.2 — подавление
проактивности, Journey §5/§6) — **design candidates** из draft-источника.
Автоматический decay engine (вычисление `current_relevance`, авто-TTL по
классам) — **deferred**. Критерий включения: GO владельца + Measurement
Framework + расширение схемы MemoryEntry + baseline данных пилота. Единственные
действующие числовые TTL — zone retention caps ADR-0011 §5 (green: нет
auto-TTL; yellow: 365 дней; red: 90 дней).

- **Источник:** Journey §5 (MVP Memory Heuristic п.6, «When Memory Must be
  Questioned»), §6 (Proactive Suppression Rules); Конституция Ст. IX.
- **Проверка:** *design candidate* — acceptance «временный факт перед
  существенным решением → переспрос»; пороги — после Measurement Framework.
- ✅ Разрешено: «Ты сказал "я веган" два года назад — это всё ещё так?»
  перед диетологической рекомендацией.
- ⛔ Запрещено: автоматический purge по вычисленному `current_relevance` до
  выполнения критерия включения; использование порогов 0.3/0.2 как
  утверждённых констант.

#### N-10. Канон ADR-0011 не изменяется

Зоны, основания согласия (`consent_at`), шифрование at-rest, retention caps,
`RedZoneAccessLog`, защита несовершеннолетних, запрет авто-повышения зоны и
кросс-тенантные правила ADR-0011 остаются в силе без изменений. Любая
коллизия измерений с зонами — стоп и «Owner decision required», а не
молчаливое разрешение (зафиксированные коллизии: OD-1, OD-2).

- **Источник:** ADR-0011 §4–§11; решение владельца 2026-07-21 (бриф 5).
- **Проверка:** acceptance gate ADR-0011 (`memory-entry-schema.md` §13 в
  `ai-bot-platform`).
- ✅ Разрешено: yellow-запись любого `knowledge_class` по-прежнему требует
  `consent_at`, шифруется и живёт ≤ 365 дней от последнего использования.
- ⛔ Запрещено: «переопределить» retention или consent-семантику зоны,
  ссылаясь на `lifetime` или `knowledge_class` из этого ADR.
- ⛔ Запрещено: рассматривать `storage_scope=session` или `lifetime=ephemeral`
  как основание не применять sensitivity, purpose, access и lawful-basis
  checks.

#### N-11. Proactive Readiness Gate (memory-часть)

Перед проактивным предложением, опирающимся на память, проверяются факторы
подавления Journey §6: `explicit_do_not_disturb` (жёсткая блокировка),
`topic_cooldown_active` (< 14 дней — значение из Journey §6),
`high_workload_context` (эмпатия без CTA), `quiet_hours`,
`proactivity_consent_missing`, `low_relevance` (порог 0.2 — design candidate).
Заблокированная проактивность не подменяется substitute offer; допустимы
молчание или нейтральное acknowledgement без CTA. Канонизируется только
memory-часть gate; канальные и тайминговые правила остаются в Journey и
профильных спецификациях.

- **Источник:** Journey §6 «Recommendation and Proactivity Gates», Stage 4 и
  Stage 7; Конституция Ст. X; Glossary «Proactive Readiness Gate» (planned
  source: ADR-0012).
- **Проверка:** Helpful Restraint Acceptance Rate (Journey §13, baseline в
  пилоте); *design candidate* — acceptance «блокировка gate → нет substitute
  offer».
- ✅ Разрешено: похожее предложение отклонено 5 дней назад → Ayla не
  инициирует тему и не предлагает замену.
- ⛔ Запрещено: при срабатывании `low_relevance` предложить «тогда другой
  массаж?» или продолжить тему вопросом.

#### N-12. Контроль пользователя над памятью

Пользователь видит, что учитывает Ayla, знает provenance записи, может
исправить, удалить, ограничить использование или отозвать согласие. Явная
обратная связь имеет приоритет над поведенческой гипотезой. Исправление
оформляется как `superseded` старой версии с сохранением истории.

- **Источник:** Конституция Ст. IX (Контроль пользователя), Ст. VII (вето и
  исправление), Ст. XIV; ADR-0011 §8 (subject rights endpoints); контракт C5
  (PILOT_CONTRACTS §6).
- **Проверка:** acceptance пилота №6 (export/delete из miniapp, dual-system
  проверка, PILOT_CONTRACTS §10); memory transparency UI (#236 в follow-ups
  ADR-0011).
- ✅ Разрешено: пользователь исправил «вечер» на «утро» → старая запись
  `superseded`, новая — `declared`/`explicit_answer`; рекомендации
  немедленно учитывают исправление.
- ⛔ Запрещено: скрывать использование записи (Journey anti-pattern 4 «Ayla
  скрывает работу памяти») или продолжать использовать поведенческую гипотезу
  после явной коррекции пользователя.

#### N-13. Объяснимость и аудит памяти

Существенное решение, использовавшее память, имеет структурированный след:
какие записи повлияли, их provenance и confidence, версия правил. Объяснение
не создаётся LLM постфактум. Гипотезы озвучиваются вероятностным языком
(«возможно», «похоже»); несущественные персонализации не превращаются в
бюрократические дисклеймеры.

- **Источник:** Конституция Ст. V (Ответственность за синтез), Ст. VII
  (Право на объяснение, Аудит); ADR-0011 §8 (право знать об автоматической
  обработке).
- **Проверка:** memory transparency (source per entry, #236); аудит-след
  существенных решений (Constitution-mandated, проверяется safety/audit
  review).
- ✅ Разрешено: «Предлагаю вечерний слот, потому что ты подтвердила, что
  вечер удобнее, и у Анны есть окно в четверг».
- ⛔ Запрещено: выдать гипотезу как факт без вероятностного языка или
  сгенерировать правдоподобное объяснение без зафиксированных причин.

#### N-14. Экономическая нейтральность памяти

Память не используется для коммерческого приоритета: тариф, комиссия, выручка
или рекламный бюджет провайдера не влияют на то, какие записи создаются, как
они используются в ranking и объяснениях.

- **Источник:** Конституция Ст. IV; Journey §9 «Monetization Neutrality»;
  AYLA-DEC-0001.
- **Проверка:** Journey §13 «Правило приоритета» и запрет оптимизации на
  GMV/Booking Fee; *design candidate* — regression-контроль ranking на
  коммерческие признаки (ADR-0009: Recommendation получает данные через
  allowlist).
- ✅ Разрешено: память персонализирует время, район, бюджет и формат
  предложения.
- ⛔ Запрещено: усиливать кандидата в ranking, потому что провайдер платит
  больше, или создавать записи памяти с коммерческими ярлыками (запрещено и
  для провайдеров — Конституция Ст. III.4).

### Proactive Readiness Gate — сводная памятная политика

Для памяти, управляющей проактивностью, действует совокупность: N-03
(молчание), N-09 (вопрошание, `low_relevance`), N-11 (факторы подавления),
N-14 (нейтральность). Полная политика gate (каналы, частота, UX) — Journey §6
и профильные спецификации; этот ADR фиксирует только её памятный контур,
исполняя роль planned source по Glossary.

### Принцип метрик

Раздел метрик этого ADR фиксирует один принцип и ноль KPI:

> Успех памяти — **минимально необходимое покрытие релевантного контекста**:
> нужный факт доступен в момент решения, при минимальном объёме хранимого и
> полной управляемости пользователем. Рост числа записей, «полнота профиля»
> и частота использования памяти сами по себе не являются успехом.

Детальные KPI (precision/recall релевантности, доля переподтверждений,
доля отзывов, качество покрытия) — предмет отдельного Measurement Framework,
который также задаёт критерии включения decay engine (N-09). Существующие
Journey-метрики (§13: Feedback Response Rate, Helpful Restraint Acceptance
Rate и др.) остаются в ведении Journey и не дублируются здесь.

## Маппинг draft-классов Journey v1.2 на многомерную модель

Draft-классы Journey §5 раскладываются на оси (имена классов — deprecated
aliases; в код и документы они не переносятся):

| Draft-класс (Journey v1.2) | `knowledge_class` | `confidence` | `lifetime` | `provenance` | TTL draft-класса → статус |
|---|---|---|---|---|---|
| `verified_identity` | `identity` | `declared` (дата рождения, введённая пользователем) / `verified` (только при наличии утверждённого `verification_method`) | `until_changed` | `explicit_answer` (дата рождения), `imported` (связанный channel ID) | «по identity/retention policy» → без изменений; identity живёт преимущественно в canonical User identity (ADR-0009), не в Memory Entry |
| `persistent_safety` | `safety` | `declared` (user-stated) / `verified` (профессионально подтверждено) | `until_changed` | `explicit_answer` / `confirmed_proposal` | «без авто-удаления по возрасту, с переподтверждением» → норма N-06; коллизия с red TTL 90d → OD-2 |
| `time_bounded_safety` | `safety` | `declared` / `inferred` | `time_bounded` | `explicit_answer` / `observed_event` (safety-наблюдение провайдера, Ст. III.4) | «по утверждённой safety/retention policy» → OD-5 (число не подтверждено источниками) |
| `stable` | `preference` | `declared` | `until_changed` | `explicit_answer` / `confirmed_proposal` / `imported` | candidate 365d → совпадает с yellow zone cap ADR-0011 §5; для green — без auto-TTL; итог — OD-5 |
| `ephemeral` | `context` | `declared` / `inferred` | `ephemeral` | `explicit_answer` / `model_inference` | candidate 14–30d → design candidate (OD-5) |
| `hypothesis` | `preference` / `safety` / `context` (по предмету) | `inferred` | `time_bounded` | `model_inference` | candidate 30d → design candidate (OD-5); `knowledge_class=hypothesis` не вводится |

Числовые TTL из таблицы Journey §5 являются design candidates (само Journey
это фиксирует): до решений OD-2/OD-5 они не разрешают ни автоматическое
удаление safety-critical сведений, ни бессрочное хранение персональных данных.

### Примирение с sensitivity-зонами ADR-0011

- Зоны и измерения **ортогональны** (N-01): зона назначается по содержимому
  записи per ADR-0011 §4, а не по `knowledge_class`.
  `knowledge_class=preference`, `confidence=inferred`, `provenance=model_inference`
  о вечерних слотах — `green` (содержимое нечувствительно);
  та же ось о ценовой чувствительности — `yellow`;
  подтверждённая беременность — `red`.
- Типичные (ненормативные) корреляции: `safety` → обычно `yellow`/`red`;
  `preference` → обычно `green`/`yellow`; `identity` → преимущественно вне
  Memory Entry (canonical User identity). Это ориентир для реализации, а не
  правило: нормативна только ADR-0011 §4.
- В системе **одна** модель памяти: `MemoryEntry` несёт и зону, и измерения
  (после миграции); 12 declared-полей Ayla-side отображаются на те же оси
  (§«Миграция»). Две коллизии словарей обнаружены и **не разрешены молча** —
  вынесены в «Owner decision required» (OD-1, OD-2) по стоп-условию брифа.

## Сверка норм Journey v1.2: подтверждено / изменено

| # | Норма Journey v1.2 | Решение ADR-0012 | Обоснование |
|---|---|---|---|
| 1 | Memory Proposal flow: Signal/Explicit → Proposal → Sensitivity+Purpose Check → Consent Check → Persistent / Session only | **Подтверждено** (N-02); оформлено через атрибуты `memory_status`/`storage_scope`/`consent_scope` | Прямая канонизация draft-источника; атрибуты взяты из Journey Stage 6 yaml, новой семантики не добавлено |
| 2 | Источники proposal: `explicit` / `signal` / `inferred` | **Подтверждено с перекодировкой**: `inferred` раскладывается в `confidence=inferred` + `provenance=model_inference` (на основе `observed_event`); предмет (`knowledge_class`) определяется отдельно | Требование владельца — ортогональные измерения; плоский `source` не вмещает «подтверждённую гипотезу»; кодовый enum сохраняется до миграции |
| 3 | Молчание ≠ согласие на профилирование и сохранение гипотез | **Подтверждено** (N-03) | Конституция Ст. VII/XIV; совпадает с реализацией W5 (`memory_ask` skip/abandon) |
| 4 | Heuristic п.1: `explicit` — только в исходной purpose | **Подтверждено** (N-07) | Конституция Ст. V/VI |
| 5 | Heuristic п.2: временные/изменяемые факты — переподтверждение перед существенным использованием | **Подтверждено** (N-06, N-09) | Конституция Ст. IX |
| 6 | Heuristic п.3: safety-critical не удаляется по давности → `confirmation_required` | **Подтверждено** (N-06); коллизия с red TTL 90d → **OD-2** | Норма прямо из Конституции Ст. IX; разрешить коллизию с ADR-0011 §5 в этом draft — вне полномочий |
| 7 | Heuristic п.4: `inferred`/`signal` — не самостоятельное основание Substantial Recommendation | **Подтверждено** (N-04) | Конституция Ст. VII |
| 8 | Heuristic п.5: подтверждённая гипотеза → declared/confirmed с сохранением provenance | **Подтверждено и формализовано** измерениями (N-05): предмет не меняется, меняются `confidence`, `provenance`, `memory_status` | Пример владельца канонизирован как комбинация осей |
| 9 | Heuristic п.6: TTL/decay/`current_relevance` отложены до ADR-0012 | **Изменено сознательно**: поведенческие триггеры вопрошания канонизированы (N-09); числовые пороги 0.3/0.2 — design candidates; автоматический decay engine — deferred с явным критерием включения | Критерий владельца «либо норма, либо явно deferred с критерием»: выбран вариант «норма поведения сейчас + автоматика позже»; числа вне источников не вводятся |
| 10 | Классы знаний (6 draft-классов) | **Изменено**: заменены ортогональными измерениями; `hypothesis` убран из `knowledge_class`; маппинг — §«Маппинг»; имена классов — deprecated aliases | Прямое требование владельца (бриф 2.1): draft-классы смешивают оси |
| 11 | Proactive Readiness Gate (planned source: ADR-0012) | **Подтверждено в memory-части** (N-11); каналы/тайминг остаются в Journey | Glossary и Journey §6 называют ADR-0012 planned source; scope-ограничение брифа (без UX-политик) |
| 12 | «What Ayla Remembers»: запоминается только необходимое для помощи | **Подтверждено** (N-08) | Конституция Ст. VI; бриф 2.4 |
| 13 | Learning Signals: явный feedback меняет `current_relevance`, неявный — нет | **Подтверждено как направление** (N-03, N-12); числовая механика — deferred (N-09) | Числа — design candidates до Measurement Framework |

## Миграция от текущей реализации

Принцип: модель накладывается на существующие хранилища **аддитивно**; ни один
действующий контракт, consent-гейт или retention-mеханизм не меняется этим
ADR. Все шаги миграции — после канонизации и решений OD.

### MemoryEntry (`ai-bot-platform`, apps/identity)

| Существующее поле | Роль в модели | Действие |
|---|---|---|
| `sensitivity_zone` | Ось зон (ADR-0011) | Без изменений (N-10) |
| `kind` (`preference`/`contraindication`/`symptom`/`lifestyle`/`relationship`/`financial`/`other`) | Частичная проекция `knowledge_class`: `contraindication`,`symptom` → `safety`; `preference`,`lifestyle`,`financial` → `preference`; `relationship` → `context`; `other` → `context`. `identity` в `kind` отсутствует; гипотезы кодируются `source=inferred` и проецируются на `knowledge_class` по предмету (например, `preference`) с `confidence=inferred` | Сохранить; добавить `knowledge_class` аддитивно с backfill по этому маппингу (правила backfill — design candidate, утверждает OD-4) |
| `source` (`explicit`/`inferred`/`signal`) | Проекция `provenance` + `confidence`:
  `explicit` → `explicit_answer`+`declared`;
  `signal` → `observed_event`+`inferred`;
  `inferred` → `model_inference`+`inferred` (на основе `observed_event` в
  `evidence_refs`). | Сохранить enum; добавить измерения аддитивно;
  `confirmed_proposal` — новое значение, появляется только при подтверждении
  proposal. Также contract sources `behavioral`/`transactional` →
  `observed_event`+`inferred`, а не `declared`. |
| `consent_at`, `last_inferred_at`, `last_used_at/count`, `ttl_days`, `delete_*`, `deletion_reason` | Слой приватности и аудита ADR-0011 | Без изменений (N-10) |
| — (отсутствуют) | `confidence`, `lifetime`, `provenance`, `memory_status`, `storage_scope`, `consent_scope` | Аддитивное расширение схемы — владелец реализации №1 (ниже); backfill-правила — design candidate (OD-4) |

### Consent-зоны и гейты

`memory_green` (PERSONAL_DATA welcome consent), per-entry `consent_at` для
yellow/red, fail-closed minor protection, запрет авто-повышения зоны,
`CONCIERGE_MEMORY_ENABLED` rollback — **без изменений**. Модель не вводит
новых consent-типов и не меняет основания зон.

### 12 declared-полей Ayla-side (frozen-контракт v1.0)

Все поля: `confidence=declared` для источников `explicit`/`conversational`
(однозначное утверждение пользователя); `confidence=inferred` для источников
`behavioral`/`transactional`; `provenance=explicit_answer` или
`observed_event` соответственно; `lifetime=until_changed`; зона — по контракту
`green` (см. OD-1 по двум полям):

| Поле контракта | `knowledge_class` | Примечание |
|---|---|---|
| `preferred_districts`, `workplace_district`, `home_district` | `preference` | Где удобно получать услугу |
| `preferred_time_slots`, `busy_days` | `preference` | Когда удобно / когда занят |
| `price_range_min`, `price_range_max` | `preference` | Бюджет как предпочтение (inferred price floor — отдельная запись `preference`/`inferred`/`model_inference`, `yellow`) |
| `diet_type` | `preference` | Диета как предпочтение; зона — OD-1 (ADR-0011 §4.2 относит vegan/keto/allergies к `yellow`; halal/kosher косвенно затрагивают религиозную принадлежность — требуется ruling владельца/legal) |
| `skin_sensitivities` | `safety` | User-stated, не клинический диагноз (контракт); зона — OD-1 (контракт: `green`; ADR-0011 §4.2: `yellow`) |
| `prefers_flexible_cancellation` | `preference` | |
| `favorite_masters` | `preference` | |
| `min_rating_preference` | `preference` | |

Эволюция контракта (persist per-field confidence/измерений Ayla-side) —
только аддитивно, по «Договору совместимости» frozen-контракта (plug-in A1b /
MemoryFact), и не входит в пилотный scope.

### Числовой confidence рендеринга (W5)

Текущее отображение в `apps/orchestrator/memory_block.py` (declared → 1.0,
inferred → 0.6; пороги ai-core `>=0.8` assert / `<0.4` clarify) — **implementation
mapping** enum-измерения в вербализацию, а не вторая модель. Оно сохраняется;
нормативен enum `confidence`, числа — производные для prompt-слоя.

### C5 (export/delete)

Не затрагивается: экспорт и удаление работают на уровне хранилищ (зоны,
MemoryEntry, declared prefs, consents). Добавление измерений в export-payload
— post-pilot follow-up, не этого ADR (бриф, scope).

## Последствия

### Положительные

- Один словарь памяти для Journey, ADR-0011, контрактов и кода; draft-классы
  Journey канонизируются без потери выразительности (подтверждённая гипотеза,
  safety-наблюдение провайдера, ephemeral-контекст выражаются комбинациями осей).
- AYLA-DEC-0002 получает нормативную модель moat: понимание пользователя как
  управляемые измерения, а не непрозрачный рост профиля (N-08).
- Миграция аддитивна: пилотные контракты и consent-гейты не ломаются.
- Точки конфликта существующих канонов (зоны vs классы, red TTL vs safety)
  явно локализованы и переданы владельцу, а не замаскированы.

### Издержки

- Расширение схемы `MemoryEntry` (+5 атрибутов) и backfill; правила backfill
  требуют отдельного утверждения (OD-4).
- Два словаря (`kind`/`source` в коде и измерения в модели) сосуществуют до
  завершения миграции — требуется дисциплина маппинга (N-01 запрещает
  расхождение без ADR).
- Glossary требует amendments (11 терминов/уточнений) — отдельный reviewed-батч
  после OD-7.

### Риски

- Реализация миграции до решений OD-1/OD-2 закрепит спорные зоны
  (diet/sensitivities) в коде — митигация: явный статус Draft и
  стоп-условие в N-10.
- «verified» без реестра методов верификации может деградировать в
  самоназначаемый ярлык — митигация: до OQ-1 `verified` только для
  identity-linkage.

## Consistency review

Постатейная сверка Draft v0.2 с действующими канонами. Вывод: конфликтов,
препятствующих продолжению review Draft, нет. Канонизация и реализация
затронутых частей заблокированы до решений OD-1 и OD-2. OD-1 требует legal
review (особенно для религиозных выводов, health/safety), OD-2 — совместного
Privacy/Safety/Legal ruling и amendment ADR-0011. Две коллизии не разрешены
в тексте ADR.

### Конституция v2.2

| Статья | Сверка | Вывод |
|---|---|---|
| III (Роли; safety-наблюдения) | Наблюдение провайдера — `safety`/`inferred`/`time_bounded`/`observed_event`; до подтверждения — только соразмерное временное ограничение; запрет провайдерских «предпочтений» и ярлыков — N-02, N-14 | Совместимо |
| IV (Экономическая нейтральность) | N-14 | Совместимо |
| V (Происхождение знаний) | Модель прямо реализует «источник, цель, надёжность, актуальность, область доступа»: `provenance`/`consent_scope`/`confidence`/`lifetime`+N-09/зона; гипотезы отделены (`confidence=inferred`, `memory_status=proposed`); синтез и аудит — N-13 | Совместимо |
| VI (Постепенное доверие) | N-02, N-07, N-08 | Совместимо |
| VII (Объяснение, вето, неявные сигналы) | N-03, N-04, N-05, N-12, N-13 | Совместимо |
| IX (Жизненный цикл знаний) | N-06, N-09, N-12; коллизия «safety не удаляется по давности» vs red TTL 90d (ADR-0011 §5) → OD-2, не разрешена здесь | Совместимо с одной зафиксированной коллизией |
| X (Уместность) | N-11; запрет скрытой диагностики не расширяется: inferred-запись о состоянии не создаётся по косвенным признакам здоровья (красная зона — только user-stated/explicit consent per ADR-0011 §4.3) | Совместимо |
| XI (Честное отражение) | Измерение/оценка/заключение/гипотеза различаются `confidence` и `knowledge_class`; импорт мультимодальных данных → `imported` + отдельные политики (вне scope) | Совместимо |
| XIV (Автономия, согласия) | N-03, N-07, N-12; отказ от памяти/персонализации (ADR-0011 §8, §13.3) не изменён | Совместимо |

### Decision Log

- **AYLA-DEC-0001** (монетизация): память не монетизируется; N-14. Совместимо.
- **AYLA-DEC-0002** (память = moat): ADR-0012 — нормативная модель этого
  решения; N-08 фиксирует, что moat — качество понимания, не объём сбора.
  Совместимо.
- **AYLA-DEC-0004** (канал MAX): ортогонально модели памяти. Совместимо.

### Wave 0 (PILOT_CONTRACTS_2026-08-15)

- **C1–C4, R1:** не пересекаются с моделью памяти. Совместимо.
- **C5 (export/delete):** не изменён (§«Миграция»); acceptance №6 остаётся
  проверкой N-12. Совместимо.
- **Acceptance №7 (память):** подтверждён как проверка N-02/N-03/N-05.
  Совместимо.
- **§9 (границы пилота):** ADR не требует post-pilot модулей; все
  реализационные шаги — после канонизации. Совместимо.

### ADR-0011 (ai-bot-platform)

- Зоны, consent-семантика, retention, шифрование, аудит, minor protection —
  без изменений (N-10). «Одна модель» достигается ортогональностью, а не
  заменой зон. Совместимо, кроме двух зафиксированных коллизий, которые
  блокируют канонизацию/реализацию затронутых частей до owner decisions:
  - **OD-1** — зона `diet_type`/`skin_sensitivities`: ADR-0011 §4.2 (`yellow`)
    vs frozen-контракт (все 12 полей `green`). Требуется legal review
    (особенно halal/kosher и health/safety).
  - **OD-2** — red TTL 90d purge vs safety-critical persistence (Ст. IX,
    Journey `persistent_safety`). Требуется Privacy/Safety/Legal ruling и
    amendment ADR-0011.

### ADR-0009 (ayla-knowledge, статус Review)

Границы владения памятью не затронуты: модель задаёт семантику записей внутри
существующих контуров (core memory — bot-side; declared prefs — Ayla-side;
provider-specific history — per-tenant, вне Memory Entry). Ownership не
переносится. Совместимо; отмечено, что ADR-0009 сам пока в Review.

### Glossary v2.1

Конфликтов нет: все использованные термины существуют (User Model, Dynamic
User Model — planned source: этот ADR; Memory Entry, Memory Source, Memory
Proposal, Consent, Sensitivity Zone, Hypothesis, Proactive Readiness Gate и
др.). 11 терминов/уточнений предложены в §«Предлагаемые дополнения в
Glossary»; сам Glossary этим ADR не изменяется (отдельный reviewed-батч).

## Владельцы реализации

Назначения — предложение draft; утверждает владелец (OD-8). Пилотные роли
(W-потоки) — по PILOT_CONTRACTS §6/§8.

1. **`ai-bot-platform` (system: `ayla-user-context`)** — аддитивное
   расширение `MemoryEntry` (`knowledge_class`, `confidence`, `lifetime`,
   `provenance`, `memory_status`, `storage_scope`, `consent_scope`), backfill
   по §«Миграция», обновление `memory_writer`/`memory_reader`, тесты
   трансформации N-05. **Scope:** post-pilot / separate amendment; пилотный W3
   не меняет frozen схему и контракты.
2. **`beautygo_backend` (пилотный W2)** — без изменений по frozen-контракту
   v1.0; аддитивная эволюция (A1b MemoryFact, persist измерений) — только
   новой версией контракта с уведомлением оркестратора, post-pilot.
3. **`ayla-ai-core`** — отображение enum `confidence` в вербализацию memory
   block (пороги assert/clarify), без изменения контракта `build_memory_block`.
4. **`ayla-knowledge` (W7)** — этот ADR; amendments Glossary (после OD-7);
   актуализация Journey §5 (ссылки на канонизированные нормы) — отдельными
   reviewed-батчами.
5. **QA / W6** — acceptance-расширения: №7 (состояния proposal,
   confirmation_required), dual-system smoke по миграции. **Scope:** post-pilot /
   separate amendment после канонизации ADR и решений OD-1/OD-2.
6. **Tech lead (владелец ADR-0011)** — amendments ADR-0011 по исходам
   OD-1/OD-2.

## Owner decision required

Решения владельца записаны ниже. Draft остаётся в статусе Proposed до
завершения legal review по OD-1 и совместного Privacy/Safety/Legal решения с
amendment ADR-0011 по OD-2. До этих условий канонизация и реализация
затронутых частей заблокированы.

- **OD-1. Зона `diet_type` и `skin_sensitivities`.** ADR-0011 §4.2 относит
  user-stated diet (vegan/keto/allergies) и skin sensitivities к `yellow`;
  frozen-контракт v1.0 объявляет все 12 declared-полей `green`. Дополнительно:
  `diet_type=halal/kosher` может косвенно раскрывать религиозную
  принадлежность (спецкатегория 152-ФЗ §10). Варианты: (a) закрепить `green`
  по pivot-решению 2026-07-09 и скорректировать примеры ADR-0011 при ближайшей
  ревизии; (b) расщепить: диета-предпочтение `green`, аллергии/сенситивности
  `yellow`; (c) иное.
  - **Решение владельца:** утвердить направление **(b)** — расщепить.
    Обычная диета-предпочтение остаётся `green`; аллергии, health-related diet
    и `skin_sensitivities` — `yellow`. `halal`/`kosher` нельзя использовать для
    вывода религиозной принадлежности. **Условие:** окончательное нормативное
    решение — после legal review по ADR-0011 §15; пилотный frozen-контракт v1.0
    в рамках пилота не меняется.
- **OD-2. Red TTL 90 дней vs safety-critical persistence.** Sweep ADR-0011 §5
  удаляет red-записи после 90 дней неиспользования; Конституция Ст. IX и
  Journey `persistent_safety` запрещают удаление safety-critical только по
  давности. Варианты: (a) для `knowledge_class=safety` на границе TTL —
  переход в `confirmation_required` + переспрос вместо молчаливого purge
  (требует amendment ADR-0011); (b) продлённый TTL для safety-kind; (c)
  принять purge как privacy-first с повторным сбором при следующем контакте.
  - **Решение владельца:** утвердить направление **(a)** — safety-critical
    запись на границе TTL переводится в `confirmation_required`, исключается
    из обычного использования и переподтверждается. **Условие:** требуется
    amendment ADR-0011; до него действующий red retention не меняется.
- **OD-3. Утверждение enum измерений** (`knowledge_class`, `confidence`,
  `lifetime`, `provenance` и их значений) как канонических — или правки.
  Предварительные условия review (убрать `hypothesis` из `knowledge_class`,
  добавить `observed_event`/`model_inference` в provenance) выполнены в v0.2.
  - **Решение владельца:** **APPROVE** — enum четырёх измерений утверждается
    как целевая модель.
- **OD-4A. Утверждение маппинга** Journey-классов и правил backfill
  (§«Миграция», design candidate). Backfill должен быть source-aware:
  `behavioral`/`transactional` → `confidence=inferred`/`provenance=observed_event`,
  не `declared`.
  - **Решение владельца:** **APPROVE AS DESIGN CANDIDATE** — source-aware
    mapping верен; окончательные backfill-правила должны пройти dry-run на
    реальных данных.
- **OD-4B. Реестр методов верификации** для `confidence=verified`: что qualifies
  (профессиональное подтверждение, документ, системный linkage). До появления
  утверждённого allowlist `verified` запрещено для данных, введённых только
  пользователем (например, дата рождения).
  - **Решение владельца:** **APPROVE REQUIREMENT, REGISTRY PENDING** — без
    allowlist и `verification_method` использовать `verified` запрещено, кроме
    отдельно уже подтверждённого identity-linkage.
- **OD-5. Числовые TTL** (ephemeral 14–30d, hypothesis 30d, stable 365d —
  кандидаты Journey): утвердить как design candidates для экспериментов или
  отложить до Measurement Framework. Zone caps ADR-0011 остаются единственными
  действующими числами.
  - **Решение владельца:** **DEFER** — числовые TTL пока не канонизировать;
    оставить design candidates до Measurement Framework.
- **OD-6. Пороги `current_relevance`** (0.3 переспрос / 0.2 подавление):
  утвердить как design candidates; критерий включения decay engine (N-09) —
  подтвердить или изменить.
  - **Решение владельца:** **DEFER NUMBERS / APPROVE BEHAVIOR** — триггеры
    переспроса утверждаются, пороги 0.3/0.2 и decay engine — позже.
- **OD-7. Дополнения Glossary** (§ниже): утвердить список терминов для
  отдельного reviewed-батча.
  - **Решение владельца:** **APPROVE** — подготовить отдельный Glossary batch
    после редакционной сверки терминов.
- **OD-8. Владельцы реализации** (§выше): подтвердить назначения и очередь
  (после канонизации ADR). Реализация заблокирована до OD-1–OD-4.
  - **Решение владельца:** **APPROVE WITH SCOPE CONDITION** — владельцев
    подтвердить, но реализацию схемы и backfill не начинать в рамках
    замороженного пилота без отдельного amendment.
- **OD-9. Canonical consent-scope registry:** утвердить versioned список
  purpose-ключей (`provider_selection`, `intent_understanding`,
  `question_suppression`, `proactive_recommendation` и др.) и владельца registry
  до начала реализации `consent_scope`.
  - **Решение владельца:** **APPROVE REQUIREMENT** — нужен отдельный versioned
    consent-scope registry с владельцем; до него поле нельзя внедрять как
    рабочий контракт.
- **OD-10. Формат decision record для rejected proposal:** утвердить минимальный
  набор полей (`topic`/`purpose`, `decision`, `timestamp`, `cooldown`), срок
  хранения и доступ пользователя к истории отказов (ADR-0011 §8).
  - **Решение владельца:** **APPROVE CONCEPT / SPEC REQUIRED** — Decision
    Record не содержит отклонённого персонального значения; срок хранения,
    доступ и чувствительность `topic` определить отдельным контрактом.

## Open questions

- **OQ-1.** Реестр методов верификации для `confidence=verified`: что
  qualifies (профессиональное подтверждение, документ, системный linkage)?
  Владелец: User Context Domain + Safety Owner.
- **OQ-2.** Формат хранения истории provenance (при трансформациях N-05/N-12):
  отдельная таблица событий записи vs поле `provenance_history`. Схемный
  вопрос реализации №1.
- **OQ-3.** Входы `current_relevance` (возраст, использование, feedback,
  противоречия) и его диапазон — предмет decay engine spec после N-09
  критерия.
- **OQ-4.** Включение измерений в C5 export-payload (post-pilot): состав и
  формат — отдельным изменением C5 по amendment procedure.
- **OQ-5.** Consent-семантика `imported` (wearables, внешние источники):
  какое согласие покрывает импорт и производные гипотезы — Phase 1+, legal
  review (ADR-0011 §15).
- **OQ-6.** UX-паттерн переспроса (`confirmation_required`): владелец —
  Conversation Design; связь с anti-spam правилами ask-eligibility.
- **OQ-7.** Подтверждение маппинга safety-наблюдений провайдера (Ст. III.4)
  на `safety`/`inferred`/`time_bounded`/`observed_event` — с Safety Owner.

## Предлагаемые дополнения в Glossary

Не применяются этим ADR; отдельный reviewed-батч после OD-7. Формат —
сокращённые карточки по шаблону Glossary §1.3 (Status: `proposed`, Planned
source: ADR-0012, Owner: User Context Domain, если не указано иное).
Предложено 11 терминов/уточнений:

- **Knowledge Class** (`knowledge_class`) — измерение Memory Entry: предметная
  категория знания (`identity`/`safety`/`preference`/`context`), плюс
  техническое `unclassified` для начального proposal без выявленного предмета.
- **Memory Confidence** — измерение Memory Entry: степень подтверждённости
  записи (`verified`/`declared`/`inferred`). Не равно `Confidence` (надёжность
  структурированного вывода): disambiguation обязательна по Glossary §2.1.
- **Lifetime (memory)** — измерение Memory Entry: ожидаемый срок актуальности
  (`until_changed`/`time_bounded`/`ephemeral`). Не заменяет Retention Policy
  (зоны).
- **Provenance Category** — измерение Memory Entry: категория происхождения
  (`explicit_answer`/`imported`/`observed_event`/`model_inference`/
  `confirmed_proposal`). Уточняет существующий термин Provenance, не заменяя
  его.
- **Memory Status** (`memory_status`) — состояние записи в жизненном цикле
  (`proposed`/`confirmed`/`confirmation_required`/`superseded`). Отклонённый
  proposal не порождает Memory Entry; решение фиксируется Decision Record.
- **Storage Scope** — область хранения записи (`session`/`persistent`).
- **Confirmation Required** — состояние записи, при котором использование для
  существенных решений требует переподтверждения. Owner: Safety Owner.
- **Decision Record** — минимальная audit-запись без персонального значения,
  фиксирующая отклонение proposal (`topic`/`purpose`, `decision`, `timestamp`,
  `cooldown`). Owner: User Context Domain + Privacy.
- **Consent Scope Registry** — versioned реестр purpose-ключей
  (`consent_scope`), в пределах которых может использоваться запись памяти.
  Owner: User Context Domain + Privacy.
- **Current Relevance** — планируемая оценка актуальности записи; числовая
  механика deferred (N-09). Status: `planned`.
- **Memory Decay** — планируемый механизм затухания актуальности; критерий
  включения — N-09. Status: `planned`.

## Вне scope

- Measurement Framework и KPI памяти (принцип — §«Принцип метрик»; числа —
  отдельный документ).
- Killer moment / WOW-спецификация (Journey §10, отдельная работа).
- Phase 1.5 и любые post-pilot эпики.
- Контракт C5 и его эволюция (только OQ-4 как вопрос).
- Изменения ADR-0011, frozen-контракта, Конституции, Decision Log, Glossary —
  только отдельными reviewed-документами после решений владельца.
- Политики фото/мультимодальных данных (Ст. XI), wearables-импорты (OQ-5).

## Источники и provenance

Draft подготовлен по брифу владельца (GO 2026-07-21, роль W7) на основании:

1. [[Ayla Constitution]] v2.2 (`ayla-knowledge`, Approved) — Ст. III–VII,
   IX–XI, XIV.
2. [[Ayla Glossary]] v2.1 (`ayla-knowledge`) — §5–§9, термины памяти и
   Cross-Provider Memory.
3. [[Ayla Decision Log]] v0.2 (`ayla-knowledge`) — AYLA-DEC-0001/0002/0004.
4. [[Ayla User Journey Specification]] v1.2 (`ayla-knowledge`, Review) — §5
   Memory Interaction, Stage 6, §6, §13 — draft-источник канонизируемых норм.
5. `djangoproject/docs/PERSONAL_CONTEXT_INTERNAL_API_CONTRACT.md` v1.0
   (FROZEN) — 12 green-полей, contract sources, consent-гейт `memory_green`.
6. `djangoproject/docs/PILOT_CONTRACTS_2026-08-15.md` — §6 C5, §10 acceptance.
7. `ai-bot-platform-s1/docs/adr/ADR-0011-user-personal-context-privacy.md`
   (Proposed, refactored 2026-05-22) — зоны GREEN/YELLOW/RED, retention,
   consent-семантика.
8. Реализация (grounding, без изменений): `apps/consent/memory.py`,
   `apps/orchestrator/memory_block.py`, `apps/orchestrator/memory_ask.py`,
   `apps/identity/services/memory_writer.py`, `apps/identity/models.py`
   (`MemoryEntry` enums).
9. `ADR-0009 Ayla Split-Domain Architecture` (`ayla-knowledge`, Review) —
   границы владения памятью (формат и frontmatter-конвенции также взяты из
   этого ADR).

## Change Log

### v0.2 — 2026-07-21

- Правки по review оркестратора:
  - `hypothesis` убран из `knowledge_class`; неподтверждённая гипотеза —
    комбинация `knowledge_class=<предмет>`, `confidence=inferred`,
    `memory_status=proposed`.
  - Provenance разведено на `observed_event` (факт) и `model_inference`
    (вывод); для `model_inference` обязательны `evidence_refs` и
    `derivation_method`.
  - Исправлен mapping confidence: `behavioral`/`transactional` → `inferred` +
    `observed_event`.
  - `verified_identity` уточнено: `verified` только при наличии утверждённого
    `verification_method`; просто введённая дата рождения — `declared`.
  - `lifetime=persistent` переименовано в `until_changed`.
  - `memory_status=rejected` убран из Memory Entry; отклонённые proposal
    фиксируются Decision Record без персонального значения.
  - N-02 уточнено: explicit save request проходит `proposed`, session/ephemeral
    не ослабляют sensitivity/legal checks.
  - Consistency review переформулирован: канонизация/реализация заблокированы
    до OD-1 (legal review) и OD-2 (Privacy/Safety/Legal ruling + amendment
    ADR-0011).
  - Добавлены OD-4A/OD-4B, OD-9 (consent-scope registry), OD-10 (decision
    record формат); прежний OQ-6 (ephemeral/согласие) удалён как отдельный
    вопрос, последующие вопросы перенумерованы.
  - Glossary proposals обновлены: 11 терминов, включая Decision Record и
    Consent Scope Registry.
- Владельческие решения по OD-1…OD-10 зафиксированы в §«Owner decision
  required» (2026-07-21). Draft остаётся Proposed до legal review OD-1 и
  Privacy/Safety/Legal решения с amendment ADR-0011 по OD-2.
- Редакционные правки: число пунктов приведено к фактическим 11 (OD-1…OD-10
  с OD-4A/OD-4B), определение `observed_event` уточнено (событие vs паттерн),
  scope реализации явно помечен post-pilot / separate amendment.

### v0.1 — 2026-07-21

- Первый draft по GO владельца: многомерная модель (4 измерения + атрибуты
  состояния), 14 норм с traceability и примерами, маппинг draft-классов
  Journey v1.2, примирение с зонами ADR-0011, миграция от текущей
  реализации, consistency review, 8 owner decisions, 8 open questions,
  9 предложений в Glossary.

## Approval

Owner rulings по OD-1…OD-10 зафиксированы 2026-07-21. Канонизация заблокирована
до legal ruling по OD-1 и совместного Privacy/Safety/Legal решения с amendment
ADR-0011 по OD-2.
`approved_by`: — · `approval_date`: —
