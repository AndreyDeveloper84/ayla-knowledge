---
node_id: ayla.architecture.goal-desired-outcome-contract
title: Ayla Goal and Desired Outcome Contract
type: specification
status: review
decision_status: proposed
canonical_status: candidate
version: "0.1"
owner: Product Architecture
priority: P0
knowledge_area:
  - architecture
domain:
  - user-context
  - wellness
  - cross-domain
concerns:
  - privacy
  - safety
  - explainability
system_owner:
  - ayla-platform
  - ayla-user-context
  - ayla-mini-app
  - ayla-conversation
source_repository: ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: high
data_categories:
  - pii
  - health
security_sensitivity: high
ai_indexing: metadata-only
export_policy: metadata-only
created: 2026-09-21
updated: 2026-09-21
review_cycle: before-major-change
depends_on:
  - "[[Ayla Constitution]]"
  - "[[OWNER_DECISION_REGISTER]]"
  - "[[Ayla Intent Model Specification]]"
  - "[[Ayla MVP User Journey Specification]]"
  - "[[Consent Scope Registry]]"
  - "[[Ayla Memory Domain Contract]]"
  - "[[Ayla Context Resolution Contract]]"
related:
  - "[[Ayla Personal Plan Contract]]"
  - "[[Ayla Decision Policy Contract]]"
  - "[[Ayla Diary and Water Contract]]"
  - "[[Ayla Dietitian Capability Contract]]"
  - "[[Ayla Goal Outcome Semantic Model Working Design]]"
  - "[[Ayla Domain Event Registry]]"
  - "[[AMD-001 C5 Pilot Personal Context Export-Forget Contract]]"
  - "[[Data Inventory Matrix]]"
  - "[[Ayla Decision Log]]"
  - "[[Ayla MVP Reset Roadmap]]"
  - "[[Ayla MVP Recommendation Contract]]"
  - "[[Ayla Glossary]]"
---

# Ayla Goal and Desired Outcome Contract

> Черновик этапа C (DRF-2261). Основание — решения владельца `AYLA-DEC-0087`, `AYLA-DEC-0090`, `AYLA-DEC-0094` и связанные (партия регистрации 2026-09-21, [[OWNER_DECISION_REGISTER]]). Документ не вводит новых сущностей, хранилищ, частот и полей: источник истины — существующие runtime-объекты. Предлагаемые имена событий помечены как предложение.

**Снимки, на которых проверен runtime:**
- `cat:` — каталог (`beautygo_backend`, рабочая копия `djangoproject`), `refs/prm/dev` = `cca8a914` (21.09 16:52 MSK); `bot:` — `ai-bot-platform`, `refs/prm/dev` = `808ca79d` (21.09 18:23 MSK). Ссылки, перепроверенные на этих SHA, помечены `@cca8a914` / `@808ca79d` или «слито #NNN». Прочие `путь:строка` сняты на прежних снимках `cat@4dbff523` / `bot@0e2c0100` и не перепроверялись. В файлах, изменённых после них, номера строк могли сдвинуться: каталог — `nutrition/services/{ai_comment,nutrition_summary,nutrition_profile,profile_upsert,manual_targets}_service.py`, `nutrition/services/targets_state.py`, `nutrition/signals.py`, `wellness/migrations/0007_*`; бот — `apps/nutrition_proactive/render.py`, `apps/orchestrator/{concierge,pipeline,personal_surface,shadow_turn}.py`, `apps/orchestrator/safety/*`, `apps/miniapp_api/{views,health_gate,views_last_topic}.py`, `apps/consent/{customer,services}.py`, `apps/skills/welcome/skill.py`, `apps/channels/max/global_onboarding.py`, `docs/OPEN_DECISIONS.md`.
- Прокси целей `apps/miniapp_api/views.py` пересверен на `bot@808ca79d`: по смыслу не менялся, номера строк сдвинулись на +10 (#1957, DRF-2230, правка выше по файлу); ссылки ниже даны на новые строки.
- «ТЗ» — `docs/PROMPT-ORCHESTRATOR-GOAL.md` (рабочее дерево Ayla, вне git); «инв. N» — его §7; «E2E N» — его §10.

## Назначение (Purpose)

Контракт определяет:

1. **Цель (Goal)** — необязательный сквозной контекст пользователя (`AYLA-DEC-0087`): что хранится, кто её создаёт и меняет, какие переходы допустимы, кто и как её читает, что она не блокирует.
2. **Desired Outcome** — обездвиженную в первом релизе модель желаемого результата (`AYLA-DEC-0094`): что существует в схеме, что запрещено, какие носители «желаемого результата» живые.
3. **Смену цели** как доменный факт и обязанность спросить человека о судьбе активного плана (`AYLA-DEC-0090`). Сам переход плана (`superseded`, `superseded_by`, пометка «собран под прошлую цель») определяет [[Ayla Personal Plan Contract]]; здесь — событие-источник и обязанность.

Цель описывает желаемое направление пути человека; она не является текущим intent, KPI, прогнозом или обещанием результата ([[Ayla MVP User Journey Specification]] v1.2 §Сквозные концепции; [[Ayla Intent Model Specification]] v1.0 §Transformation Goal and Intent). Пользователь управляет своими целями ([[Ayla Constitution]], Термины; Ст. III «Роли»).

## Владение (Ownership)

| Что | Владелец | Основание |
|---|---|---|
| Смысл цели, право сформулировать, изменить, отложить, завершить, архивировать | человек | Constitution Ст. III; Journey v1.2 §Сквозные концепции; `AYLA-DEC-0039` |
| Хранение цели и анкеты цели, таблица переходов | домен User Context; runtime — каталог `beautygo_backend`, приложение `goals` | `cat:goals/models.py:71-288`; `cat:goals/lifecycle.py:1-135` |
| Курируемый словарь ключей цели (`GoalOption`) и связь «цель → категории» | каталог (данные, правка в админке) | `cat:goals/resolution.py:1-23` |
| Семантическая связь intent ↔ Goal | [[Ayla Intent Model Specification]] (только правило связи, не хранение) | Intent Model v1.0 §Lifecycle and Ownership; `AYLA-DEC-0043` |
| Реакция плана на смену цели | [[Ayla Personal Plan Contract]] | `AYLA-DEC-0090` |
| Выбор следующего шага при наличии/отсутствии цели | [[Ayla Decision Policy Contract]] | `AYLA-DEC-0097` |
| Desired Outcome / PlanOutcomeLink / ProgressObservation | домен Wellness; runtime — каталог, приложение `wellness`; **писателей нет** | `AYLA-DEC-0094`; `cat:wellness/services.py:70-137` |
| Поверхности ввода | Mini App (экран выбора цели и анкета); бот — только чтение и кнопка перехода в Mini App | `bot@808ca79d:apps/miniapp_api/views.py:5637-5721`; `bot:apps/skills/welcome/skill.py:190,1282` |

LLM и Ayla как система **не являются** владельцами цели: у модели нет инструмента записи цели (см. «Граница API / runtime»).

Отображение хранилища `ClientGoal` на репозиторий в [[Ayla Repository Responsibility Matrix]] не задано — см. «Открытые вопросы», OQ-10. До решения хранилище в каталоге обозначено в frontmatter как `system_owner: ayla-platform` — так же, как во всех пяти контрактах этапа C.

## Источник истины (Source of truth)

| Понятие | Единственный источник истины | Не является источником истины |
|---|---|---|
| Цель | строка `goals.ClientGoal` (`cat:goals/models.py:71-171`) | документ состояния `decision-context` (эфемерная проекция, `cat:goals/api.py:280-294`); `PersonalPlan.goal_key` (снимок); AnalyticsEvent `goal_selected` |
| Дословная формулировка цели | `ClientGoal.goal_text` — хранится дословно, не нормализуется (`cat:goals/models.py:106-112`) | подпись чипа; пересказ модели |
| Курируемый ключ цели | `ClientGoal.goal_key` — ставится только выбором человека (чип или вариант анкеты) (`cat:goals/api.py:340-345,547-557`) | вывод резолвера по тексту (он ключ не пишет — `cat:goals/resolution.py:55-88`) |
| Ответы анкеты цели | `GoalAnketaRun` / `GoalAnketaAnswer` (`cat:goals/models.py:174-288`) | — |
| Срок цели | `ClientGoal.target_date` (`cat:goals/models.py:133-142`) | Desired Outcome (обездвижен) |
| Цель питания | `NutritionProfile.goal` (`cat:nutrition/models.py:453,492`) — отдельный носитель, **связан, не слит** (`AYLA-DEC-0089`). Это цель, **названная** человеком: расчётная цель после ступени `bmr_floor` больше не пишется в это поле ни при пересчёте, ни при подтверждении — так (слито #536, `cca8a914`, DRF-2241; `cat@cca8a914:nutrition/services/profile_upsert_service.py:291-302`, `:705-706`) | `ClientGoal`; подсказка `PlanTemplate.nutrition_goal_hint` (`cat:wellness/models.py:505-515`) |
| Желаемый результат | в первом релизе **нет**; живые носители — только `ClientGoal.target_date` и `NutritionProfile.goal` (`AYLA-DEC-0094`) | `DesiredOutcome` (схема без писателей) |

Новый источник истины для «желаемого результата» создавать запрещено (`AYLA-DEC-0094`). Документ состояния и снимок `goal_key` в плане — производные; при расхождении прав `ClientGoal`.

## Сущности

### Goal — `ClientGoal`

Поля (факт кода, `cat:goals/models.py:91-144`):

| Поле | Смысл | Норма |
|---|---|---|
| `id` | UUID цели | адрес для переходов |
| `client` | человек (FK на пользователя, `PROTECT`) | салона на цели нет — решение DRF-1472 (`cat:goals/models.py:13-19`) |
| `goal_key` | ключ курируемой цели (`GoalOption.key`) или `NULL` | ставится только выбором человека; `NULL` — свободный текст без сопоставления |
| `goal_text` | дословный ввод человека или `NULL` | не нормализуется; хранится и при распознанном ключе |
| — | CheckConstraint: заполнено хотя бы одно из `goal_key` / `goal_text` | `cat:goals/models.py:149-155` |
| `selected_at`, `source_channel` (`bot` / `miniapp`) | момент и канал выбора | канал — provenance, не семантика |
| `state`, `state_changed_at` | состояние жизненного цикла и момент перехода | `NULL` у legacy-строк: момент не выдумывается |
| `target_date` | срок, названный человеком, или `NULL` | напоминаний, процентов «прошло времени» и пересчёта плана по сроку нет (`cat:goals/models.py:133-137`) |

Кардинальность: у человека **0..N** целей, из них **не более одной `ACTIVE`** (partial unique `clientgoal_one_active_per_client`, `cat:goals/models.py:156-160`). Прочие — в `PAUSED` и терминальных состояниях. Цель может отсутствовать вовсе.

**Норма до пилота — одна активная цель** (решение владельца 21.09, журнал главного окна CD §72 п.17 (вне git)): у человека не более одной `ACTIVE` цели; несколько одновременно активных целей не вводятся. Ограничение схемы `clientgoal_one_active_per_client` совпадает с этой нормой.

### Анкета цели — `GoalAnketaRun`, `GoalAnketaAnswer`

- Проход анкеты — факт; незакрытый проход у человека не более одного (`cat:goals/models.py:208-216`). `goal` прохода — цель, которой он завершился, или `NULL` (проход брошен — разрешённый выход, «анкета не ворота»).
- Ответ на шаг хранится дословно (`answer_text`) или ключом варианта; собирается **только цель** — контактов и профильных полей нет (`cat:goals/models.py:229-240`).
- Шаги: `goal` (первый), `area`, `feeling`, `deadline` (`cat:goals/anketa.py:68,329-412`).

### Desired Outcome — `DesiredOutcome`, `PlanOutcomeLink`, `ProgressObservation`

Схема существует (`cat:wellness/models.py:23-90,160-340`) и **обездвижена** (`AYLA-DEC-0094`):
- `DesiredOutcome` — `target`, дословный `statement_text`, `direction` / `desired_state_numeric`, `status` ∈ {`open`, `closed_by_user`};
- `PlanOutcomeLink` — связь плана и результата;
- `ProgressObservation` — наблюдения тела.

Состояний `ACHIEVED` / `FAILED` в перечислениях нет: система физически не может объявить результат достигнутым или проваленным (`cat:wellness/models.py:10-12`). Контракт не описывает семантику этих моделей сверх факта схемы: она определяется после утверждения Goal/Outcome Taxonomy (OQ-GO-6 в [[Ayla Goal Outcome Semantic Model Working Design]]).

### Связанные носители (не сущности этого контракта)

- `PersonalPlan.goal` (FK `SET_NULL`) и снимок `PersonalPlan.goal_key` (`cat:wellness/models.py:115-134`) — владелец [[Ayla Personal Plan Contract]].
- `NutritionProfile.goal` (`lose` / `maintain` / `gain`) — владелец [[Ayla Diary and Water Contract]] / [[Ayla Dietitian Capability Contract]]; связь с `ClientGoal` — только подсказка `nutrition_goal_hint` в документе состояния, без предвыбора (`cat:goals/decision_context.py:196-200`).

## Состояния и переходы

### Цель

Состояния (`cat:goals/models.py:78-89`): `ACTIVE`, `PAUSED`, `ACHIEVED`, `ARCHIVED`, `SUPERSEDED`, `LEGACY_INACTIVE_REASON_UNKNOWN`.

Таблица переходов (`cat:goals/lifecycle.py:49-56`):

```text
(нет)    → ACTIVE                      выбор цели человеком (новая строка)
ACTIVE   → PAUSED · ACHIEVED · ARCHIVED  явное действие человека
PAUSED   → ACTIVE · ACHIEVED · ARCHIVED  явное действие человека
ACTIVE   → SUPERSEDED                  только как следствие выбора новой цели
ACHIEVED, ARCHIVED, SUPERSEDED, LEGACY_INACTIVE_REASON_UNKNOWN — терминальны
```

Нормы:
1. Из каждого нетерминального состояния есть выход, и ни один выход не требует замещающей цели (`cat:goals/lifecycle.py:1-7`).
2. `ACHIEVED` и `ARCHIVED` — только слово человека. Бездействие, завершённая бронь и завершённый план цель в `ACHIEVED` не переводят. Автоматических писателей терминальных состояний нет (`cat:goals/models.py:50-52`).
3. `SUPERSEDED` пишет только выбор новой цели (`cat:goals/lifecycle.py:126-135`, вызывается из `cat:goals/api.py:249-259`). Это не `ARCHIVED`: человек не говорил, что старую цель вести не хочет.
4. `PAUSED`-цели при выборе новой остаются на паузе (`cat:goals/lifecycle.py:130-131`).
5. Снятие с паузы при другой `ACTIVE` — отказ `GOAL_ANOTHER_ACTIVE`, а не молчаливое закрытие соседней (`cat:goals/lifecycle.py:29-33,103-109`).
6. `LEGACY_INACTIVE_REASON_UNKNOWN` не переводится никуда кодом: его смысл неизвестен и не угадывается (`cat:goals/lifecycle.py:21-23`).
7. Повторный запрос того же состояния — идемпотентен, `state_changed_at` не сдвигается (`cat:goals/lifecycle.py:86-91`).
8. Возврат `ARCHIVED` / `ACHIEVED` → `ACTIVE` владелец не постановлял; выход — выбрать цель заново (новая строка) (`cat:goals/lifecycle.py:17-19`). См. OQ-7.

### Смена цели при активном плане (`AYLA-DEC-0090`)

«Смена цели» — переход `ACTIVE → SUPERSEDED` старой цели с созданием новой `ACTIVE` в одной транзакции (`cat:goals/api.py:249-259`). При этом:
- план **не закрывается молча** и не меняется этим переходом;
- Ayla **обязана спросить** человека: «Обновить план под новую цель» или «Оставить текущий» (формулировка `AYLA-DEC-0090`);
- до явного подтверждения нового плана кнопкой старый план остаётся активным;
- переходы плана (`superseded`, `superseded_by`, пометка «собран под прошлую цель») — [[Ayla Personal Plan Contract]].

Пауза, архив и «достигнута» при активном плане решением `AYLA-DEC-0090` не охвачены — см. OQ-9.

### Desired Outcome

Переходов в первом релизе нет: писатели отказывают (`cat:wellness/services.py:106-137`). Состояния схемы (`open` / `closed_by_user`) не используются.

## Команды

Существующие команды (runtime). Все — от имени человека, по его явному действию.

| Команда | Вход | Эффект | Отказы | Источник |
|---|---|---|---|---|
| `SelectGoal` | `POST /api/v1/internal/me/goals/select/` с ровно одним из `goal_key` (чип) / `goal_text` (свободный ввод) и `source_channel` | `SUPERSEDED` прежней `ACTIVE` + новая `ACTIVE`; закрытие открытого прохода анкеты; AnalyticsEvent `goal_selected` | 400 — форма тела | `cat:goals/api.py:160-196,312-355` |
| `DeclareNeedGuidance` | тот же вход, `intent=need_guidance` | цель **не создаётся**, событие не пишется; документ с ведущим вопросом | — | `cat:goals/api.py:317-324` |
| `StartGoalAnketa` | `intent=start_anketa` | открыть (или переиспользовать) проход; активная цель **не трогается** | — | `cat:goals/api.py:326-331,359-375` |
| `AnswerGoalAnketaStep` | `answer` = `{step, option_key \| option_keys \| text \| confirm, revise?}` | запись ответа; ответ на шаг `goal` создаёт цель так же, как `SelectGoal`; шаг `deadline` ставит `target_date` | 409 `ANKETA_STEP_MISMATCH`; 400 — чужой вариант, текст где он не допускается, непонятый срок | `cat:goals/api.py:426-592` |
| `ChangeGoalState` | `POST /api/v1/internal/me/goals/state/` с `goal_id`, `state` ∈ {`active`, `paused`, `achieved`, `archived`} | переход по таблице | 404 — чужая или несуществующая цель; 409 `GOAL_TRANSITION_NOT_ALLOWED` / `GOAL_ANOTHER_ACTIVE` | `cat:goals/api.py:199-210,595-659` |
| `ForgetAll` (чужая команда, эффект на цель) | пути «забудь всё» каталога | стирание всех целей и анкеты человека (см. «Приватность») | откат всей транзакции | `cat:users/forget_all_catalog.py:77-158` |

Команды, которых нет и которые этот контракт **не вводит**:
- записи Desired Outcome (`record_outcome`, `record_observation` всегда отказывают — `AYLA-DEC-0094`);
- записи цели моделью (LLM) или по выводу из разговора (инв. 1–2);
- «предложить сопоставление текста с ключом с последующим подтверждением» — такого шага в runtime нет; сопоставление = выбор чипа или варианта человеком (см. OQ-2).

## События

Сейчас в runtime есть только AnalyticsEvent `goal_selected` (`cat:analytics/event_catalogue.py:94-101`; эмиссия `cat:goals/api.py:213-227`): payload `goal_key`, `has_text`, `source_channel`, **без** `goal_text`. Доменных событий цели в [[Ayla Domain Event Registry]] нет.

Предлагаются к регистрации в Domain Event Registry (KB-E) по правилу имён `<domain>.<entity>.<fact>` / `<entity>.<fact>` (DER §3, `AYLA-DEC-0025`):

| Событие | Когда | Минимальное содержание | Потребители | Статус |
|---|---|---|---|---|
| `goal.selected` | создана новая `ACTIVE` цель (`SelectGoal` или шаг `goal` анкеты) | идентификатор цели, `goal_key` или его отсутствие, признак наличия текста, `source_channel`, время. **Без** `goal_text` — как у текущего `goal_selected` | аналитика; [[Ayla Decision Policy Contract]] | **предлагается к регистрации в Domain Event Registry (KB-E)**; `goal_selected` — кандидат в legacy alias |
| `goal.state_changed` | переход по `ChangeGoalState` (`PAUSED`, `ACHIEVED`, `ARCHIVED`, снятие с паузы) | идентификатор цели, `from_state`, `to_state`, время | [[Ayla Personal Plan Contract]] (см. OQ-9); аналитика | **предлагается к регистрации в Domain Event Registry (KB-E)** |
| `goal.superseded` | прежняя `ACTIVE` закрыта выбором новой | идентификатор закрытой цели, идентификатор новой цели, время | [[Ayla Personal Plan Contract]] — источник обязанности спросить (`AYLA-DEC-0090`) | **предлагается к регистрации в Domain Event Registry (KB-E)** |

Нормы:
- события — факты в прошедшем времени, не команды;
- ни одно событие цели не несёт дословный `goal_text` и ответы анкеты;
- `goal.superseded` при наличии активного плана обязан привести к вопросу человеку (`AYLA-DEC-0090`); само событие план не меняет;
- связь «старая цель → новая» в хранилище сейчас не записывается (у `ClientGoal` нет поля ссылки); окончательный состав полей — решение поправки DER (OQ-6).

Desired Outcome событий в первом релизе не имеет.

## Входы и выходы

**Входы:**
- явное действие человека в Mini App: чип, свободный текст, вариант анкеты, ответ на шаг срока, кнопки жизненного цикла (последние — путь исполнения DRF-2228);
- свободный текст цели в Mini App проходит safety-вход до записи (`bot@808ca79d:apps/miniapp_api/views.py:5672-5678`, `bot:apps/miniapp_api/health_gate.py:1-46`).

Не являются входом: реплики в чате (цель из разговора не создаётся), вывод резолвера intent, догадка модели.

**Выходы (читатели цели):**
- документ состояния `decision-context`: скаляр `known.goal` (активная) и список `known.goals` (`ACTIVE` + `PAUSED`) с `id`, `state`, `goal_key`, `goal_text`, `label`, `target_date`, `target_date_passed`, `nutrition_goal_hint` (`cat:goals/decision_context.py:162-205,423-444`);
- фильтр рекомендаций по категориям цели — только при `GOAL_RESOLUTION_ENABLED` (по умолчанию `false`, `cat:djangoProject/settings/base.py:528-530`); при невозможности разрешить цель фильтр не применяется, выдача прежняя (`cat:goals/wiring.py:12-24`);
- план: `PersonalPlan.goal` / `goal_key` (владелец — Personal Plan Contract);
- бот: читатель активной цели для коуча питания, fail-closed — сбой неотличим от «цели нет» (`bot:apps/nutrition_coach/goals.py:1-26`);
- главный экран, карточка личности, источник рекомендаций (`cat:users/home_api.py`, `cat:users/identity_card.py`, `cat:users/recommendation_source.py` — перепись импортов `goals`).

**Выход Desired Outcome:** `wellness-context` отдаёт `outcomes: []` — писателей нет (`cat:wellness/context_read.py:85-86`).

Intent Resolution Output 0.5 поля цели не содержит и не получает (Intent Model v1.0 §Recommendation Input Boundary); в `bot:apps/orchestrator/intent_resolution.py` слово `goal` не встречается (git grep на `0e2c0100`).

## Инварианты

| # | Инвариант | Основание | Инв. ТЗ |
|---|---|---|---|
| G-INV-1 | Ayla и LLM не создают цель и не меняют её состояние. Цель создаётся только явным действием человека. | `AYLA-DEC-0087`; Intent Model v1.0 «resolver не создаёт Goal из догадки» | инв. 1, 7 |
| G-INV-2 | Ayla не выдумывает связь Intent → Goal: при неизвестной связи она остаётся `unknown/not_established`. | `AYLA-DEC-0043`; Intent Model v1.0 §Transformation Goal and Intent | инв. 2 |
| G-INV-3 | Сопоставление «текст → курируемый ключ» подтверждается человеком (выбор чипа или варианта). Свободный текст без такого выбора хранится с `goal_key = NULL`; отсутствие сопоставления ничего не блокирует и не заменяется ближайшим ключом. | `AYLA-DEC-0087`; ТЗ §6 «Goal»; `cat:goals/models.py:97-99` | инв. 2, 5, 6 |
| G-INV-4 | Дословная формулировка сохраняется без нормализации; подпись чипа не подделывается под слова человека. | `cat:goals/models.py:106-112`; ТЗ §6 «Goal» | инв. 6 |
| G-INV-5 | Целей 0..N, `ACTIVE` — не более одной: одна активная цель до пилота. | решение владельца 21.09, журнал главного окна CD §72 п.17 (вне git); runtime `cat:goals/models.py:156-160`; `AYLA-DEC-0090` (формулировка «смена цели») | — |
| G-INV-6 | Отсутствие цели не блокирует дневник, воду, вопросы, запись и явно выбранные действия. | `AYLA-DEC-0087`, `AYLA-DEC-0091`; Journey N1.4 | — |
| G-INV-7 | Выход из цели не требует замещающей цели; терминальные состояния пишет только человек (или выбор новой цели для `SUPERSEDED`). | `cat:goals/lifecycle.py:1-7`; Journey «пользователь может изменить или отложить цель в любой момент» | инв. 7 |
| G-INV-8 | Смена цели при активном плане — событие; план не закрывается молча; Ayla спрашивает; новый план — только после явного подтверждения кнопкой. | `AYLA-DEC-0090` | инв. 7, 8, 9, 10 |
| G-INV-9 | Desired Outcome, PlanOutcomeLink, ProgressObservation — писателей 0; гейты D/O fail-closed; новый источник истины «желаемого результата» не создаётся. | `AYLA-DEC-0094`, `AYLA-DEC-0088` | инв. 3, 6 |
| G-INV-10 | Цель и цель питания связаны, не слиты: ни один носитель не пишется из другого, подсказка не предвыбирает. | `AYLA-DEC-0089`, `AYLA-DEC-0094` | инв. 3 |
| G-INV-11 | Цель не является медицинским или телесным параметром; система не объявляет цель достигнутой или проваленной. | `AYLA-DEC-0094`; `cat:wellness/models.py:10-12`; `cat:goals/models.py:50-52` | инв. 3 |
| G-INV-12 | «Забудь всё» стирает все цели и анкету цели в той же транзакции «всё или ничего», что план и профиль питания. | ТЗ инв. 21; бриф T-6; `AYLA-DEC-0101` (та же транзакция) | инв. 21 |
| G-INV-13 | Safety имеет приоритет над целью: опасный текст цели не записывается до прохождения safety-входа. | `AYLA-DEC-0096` | инв. 22 |
| G-INV-14 | Каждое изменение цели объяснимо: кто, когда, через какой канал, из какого состояния в какое. | ТЗ §7 | инв. 25 |

## Согласие (Consent)

- **Факт runtime.** На пути записи цели (прокси `customer_goal_select`, декоратор `require_init_data`, `cat:goals/api.py`) проверки согласия нет: в прочитанных участках (`bot@808ca79d:apps/miniapp_api/views.py:147-215,5637-5721`; git grep `consent` в `cat:goals/*.py` вне тестов — 0 вхождений).
- **Канон.** [[Consent Scope Registry]] v1.4 §4 регистрирует категорию `explicit_goal` («Разрешается только по scope») и честно оставляет открытым её владельца и маппинг на поля (§4, §4.1). Отдельного scope хранения цели нет; scope `goal_memory` для постоянной записи намерения в Desired Outcome не утверждён — гейт D отказывает (`cat:wellness/services.py:70-85`).
- Этот контракт **не выбирает** правовое основание хранения `ClientGoal` — это решение Privacy/владельца (OQ-3).
- Desired Outcome: гейты D и O fail-closed для `purpose=processing` даже с валидной attestation; права субъекта (`purpose=subject_rights`: просмотр, экспорт, исправление, удаление) не блокируются (`cat:wellness/services.py:18-21,81-103`).
- Отзыв согласия на хранение ведёт к «забудь всё» на стороне каталога (`cat:users/personal_data_api.py:348-355` — комментарий о вызывающих; сам путь бота не перепроверялся).

## Приватность (Privacy)

**Классы данных цели:** дословный `goal_text`, свободные ответы анкеты (`answer_text`), `target_date`, история состояний. Это персональные данные, введённые человеком; свободный текст может случайно содержать сведения о здоровье — отсюда safety-вход (см. «Безопасность»).

**«Забудь всё» (`AYLA-DEC-0101`, инв. 21).** Факт на `4dbff523`:
- все три пути «забудь всё» каталога зовут `erase_remembered_catalog`: приложение (`cat:users/personal_context_views.py:200`), бот C5.2 (`cat:users/personal_data_api.py:357-364`), `DELETE …/personal-context/` (`cat:users/internal_personal_context_api.py:220`);
- функция стирает `PlanOutcomeLink`, `PlanAction`, `PersonalPlan`, `DesiredOutcome`, `ProgressObservation`, `GoalAnketaRun` (ответы — каскадом), `ClientGoal`, затем профиль питания и дневник с фото (`cat:users/forget_all_catalog.py:116-150`);
- транзакция «всё или ничего» — у вызывающего (`cat:users/personal_data_api.py:357`; `cat:users/forget_all_catalog.py:63-68`);
- покрыто тестом `cat:users/tests/test_forget_all_catalog_2214.py` (дословные слова цели и анкеты исчезают — :210-218; повтор безвреден — :267; сбой откатывает всё — :293).

Это слито PR #526 (`cf2e99a7`) и #530 (`33eddecc`) в DRF-2214.

**Остаточные пробелы (путь исполнения — DRF-2214):**
- **Экспорт C5.1 целей не отдаёт**: ответ содержит `profile`, `personal_context`, `specialist_profile`, `linked_identities` (`cat:users/personal_data_api.py:289-296`); в `bot:apps/identity/export_coverage.py` слово `goal` не встречается. Экспорт обязан нести цели (включая `goal_text`, состояния, `target_date`) и ответы анкеты.
- Ответ C5.2 в `deleted` по-прежнему называет только персональный контекст (`cat:users/personal_data_api.py:327`); readback C5.3 проверяет только строку профиля (`cat:users/personal_data_api.py:409-432`). Смена формы — DRF-2214 PR-3 (по докстрингу `cat:users/forget_all_catalog.py:63-68`).
- `Recommendation.target_outcomes` держит UUID стёртых `DesiredOutcome` (`cat:users/forget_all_catalog.py:42-47`) — при обездвиженном Desired Outcome строк нет, но пробел назван.
- Судьба строк AnalyticsEvent `goal_selected` (с `actor` и `goal_key`) при «забудь всё» — **UNKNOWN** (в `erase_remembered_catalog` не входят) — OQ-5.

**Внешняя LLM.** По докстрингу `bot:apps/nutrition_coach/goals.py:22-26` `goal_text` идёт в промпт LLM после очистки и обрезки. Флаги здоровья во внешнюю модель не передаются (`AYLA-DEC-0098`); применимость этого запрета к свободному тексту цели — OQ-11.

**Аналитика.** `goal_text` в BI не попадает (`cat:analytics/event_catalogue.py:95-97`); предлагаемые события `goal.*` сохраняют это правило.

## Безопасность (Safety)

- **Порядок.** Safety выполняется раньше функций цели (`AYLA-DEC-0096`, инв. 22). Минимальный входной детектор и расширенная оценка — [[Ayla Decision Policy Contract]].
- **Вход свободного текста цели (Mini App).** До записи `goal_text` и `answer.text` проходят `screen_goal_body` (`bot@808ca79d:apps/miniapp_api/views.py:5672-5678`): кризис и блок — ответы чата; красный флаг — медицинский текст неотложки; медицинский вердикт гейта (MEDICAL, 103 / 112) сводится к тому же красному флагу — так (слито #1956, `557f0238`, DRF-2000; `bot@808ca79d:apps/miniapp_api/health_gate.py:235-249`); мягкий сигнал и `CLARIFY` — признание и уточняющие вопросы. При сигнале цель **не создаётся**, документ не меняется; ответ на уточнение классифицируется и не хранится (`bot:apps/miniapp_api/health_gate.py:1-46`). Названный предел: память «вопросы заданы» чата и Mini App не объединены (`bot:apps/miniapp_api/health_gate.py:52-59`).
- **Цель не медицинская цель.** Цель не несёт телесных параметров; числовые телесные результаты (`desired_state_numeric`, `ProgressObservation`) обездвижены (`AYLA-DEC-0094`, `AYLA-DEC-0088`).
- **Нет давления.** Цель не спрашивается как обязательный шаг; «не понимаю, чего хочу» — состояние ведения, не цель (`cat:goals/api.py:317-324`; Journey N1.4).
- **Срок.** `target_date` не порождает напоминаний и не пересчитывает план (`cat:goals/models.py:133-137`).

## Наблюдаемость (Observability)

Есть (runtime):
- журнал каталога: `goals.selected`, `goals.anketa_goal_chosen`, `goals.anketa_completed`, `goals.need_guidance`, `goals.state_changed`, `goals.state_refused` с кодом (`cat:goals/api.py:321,350-354,561-564,588-591,638-652`); `goal.state_changed` в `lifecycle.transition` (`cat:goals/lifecycle.py:119-122`);
- AnalyticsEvent `goal_selected` на каждый выбор, включая повторный выбор той же цели (`cat:goals/api.py:213-227`);
- журнал «забудь всё» со счётом строк по моделям без значений (`cat:users/forget_all_catalog.py:152-157`);
- печать состояния флагов `GOAL_RESOLUTION_ENABLED`, `GOAL_ANKETA_ENABLED` командой `surface_state` (`cat:core/management/commands/surface_state.py:82-86`);
- при включённом резолвере — отдельная строка журнала для цели без связей и для пустой полки (`cat:goals/wiring.py:32-49`).

Нет (расхождение):
- `supersede_active` не пишет ни строки журнала, ни события (`cat:goals/lifecycle.py:126-135`): факт «цель закрыта выбором новой» восстанавливается только по `state` / `state_changed_at`;
- доменных событий `goal.*` нет (см. «События»).

## Поведение при сбоях (Failure behavior)

| Сбой | Поведение | Источник |
|---|---|---|
| Каталог недоступен при выборе цели | прокси — 502 `ayla_unavailable`; при ошибке конфигурации — 503; запись не выполняется | `bot@808ca79d:apps/miniapp_api/views.py:5685-5706` |
| Отказ каталога 4xx | прокси — 400 с телом и исходным статусом `ayla_status` (экран отличает «сказал словами» от «документ протух») | `bot@808ca79d:apps/miniapp_api/views.py:5688-5703` |
| Протухший документ / ответ не на тот шаг | 409 `ANKETA_STEP_MISMATCH`, проход не создаётся (проверки до записи) | `cat:goals/api.py:441-487` |
| Гонка двух вызывающих (бот и Mini App) при переходе | условный `UPDATE … WHERE state=from`; проигравший получает честный отказ, чужой переход не перезаписывается | `cat:goals/lifecycle.py:98-115` |
| Нарушение «одна ACTIVE» при снятии с паузы | 409 `GOAL_ANOTHER_ACTIVE`, соседняя цель не трогается | `cat:goals/lifecycle.py:103-109` |
| Чужой `goal_id` | 404, существование чужой цели не раскрывается | `cat:goals/api.py:626-633` |
| Читатель цели в боте при сбое | fail-closed: сбой = «цели нет», проактив молчит | `bot:apps/nutrition_coach/goals.py:8-20` |
| Резолвер не может разрешить цель | фильтр не применяется, выдача прежняя; угадывания нет | `cat:goals/wiring.py:12-24` |
| Сбой «забудь всё» на любом шаге | откат всей транзакции; файл фото, не снятый с носителя, — `IncompleteErasure` | `cat:users/forget_all_catalog.py:58-61,80-81` |
| Попытка записать Desired Outcome | отказ гейта с `reason_code` (`scope_not_approved` / `blocked_pending_privacy_legal`), записи нет | `cat:wellness/services.py:83-84,101-102` |
| Safety-сигнал в тексте цели | запись не выполняется, человеку — ответ safety | `bot@808ca79d:apps/miniapp_api/views.py:5676-5678` |

## Граница API / runtime

| Норма | Целевое поведение | Текущий runtime | Расхождение → лист |
|---|---|---|---|
| Цель необязательна (G-INV-6) | ни дневник, ни вода, ни вопрос, ни запись, ни явно выбранное действие не требуют цели | в `cat:nutrition/` и `cat:appointments/` импорта `goals` нет (git grep на `4dbff523`); фильтр рекомендаций без цели не применяется (`cat:goals/wiring.py:18-20`); **но** создание плана без `ACTIVE`-цели — 404 `no_active_goal` (`cat:wellness/plan_lite.py:172-175`), бот при отсутствии цели ведёт на выбор цели (`bot:apps/orchestrator/plan_lite_card.py:13`) | план без цели — [[Ayla Personal Plan Contract]] (`AYLA-DEC-0091`); лист исполнения — UNKNOWN (не назначен в правилах этапа C) |
| LLM цель не пишет (G-INV-1) | у модели нет инструмента записи цели | инструменты консьержа: `show_masters`, `start_booking`, `ask_clarification`, `confirm_said_fact`, `show_salons`, `show_services`, `show_my_records`, `health_screening`, `log_water`, `clarify_food_entry`, `start_nutrition_anketa` (`bot:apps/orchestrator/concierge.py:723-732`; `bot:apps/orchestrator/nutrition_global.py:100-161`; `bot:apps/orchestrator/discovery.py:281-461`; `bot:apps/orchestrator/personal_surface.py:148`) — инструмента цели нет; единственный вызывающий `post_goal_select` — прокси Mini App (`bot@808ca79d:apps/miniapp_api/views.py:5681`) | нет |
| Intent без поля цели (G-INV-2) | Output Contract 0.5 без полей цели | `bot:apps/orchestrator/intent_resolution.py` — 0 вхождений `goal` | нет |
| Сопоставление подтверждает человек (G-INV-3) | ключ — только выбором чипа / варианта | `goal_key` пишется только из тела `goal_key` или `option_key` анкеты (`cat:goals/api.py:340-345,552-557`); свободный текст — `goal_key = NULL`; резолвер при `GOAL_RESOLUTION_ENABLED` сопоставляет текст с подписью `GoalOption` только при точном совпадении без учёта регистра, ключ не пишет, только фильтрует категории (`cat:goals/resolution.py:76-86`); флаг по умолчанию выключен (`cat:djangoProject/settings/base.py:528-530`) | квалификация точного совпадения как «подтверждения» — OQ-2 |
| 0..N, ≤1 ACTIVE (G-INV-5) | как runtime | partial unique (`cat:goals/models.py:156-160`); список `known.goals` для открытых целей (`cat:goals/decision_context.py:423-441`) | runtime соответствует норме (CD §72 п.17). Реестр бота §97 OD-GOAL-E и ТЗ §6 допускают больше — их выравнивание вне этого контракта |
| Жизненный цикл из UI (T-10) | кнопки «пауза / архив / достигнута» в Mini App | ручка есть (`cat:goals/api.py:595-653`, маршрут `cat:goals/state_urls.py:7`); прокси `goals/state` в боте нет (git grep `goals/state` в `bot:apps/` — 0 на `0e2c0100`, `eec1ded5` и `808ca79d`) | **DRF-2228** (после G-1) |
| Смена цели → вопрос о плане (G-INV-8) | событие `goal.superseded`, вопрос «Обновить / Оставить» | `supersede_active` план не трогает, событие не пишется, вопроса нет; предложение плана зовут только при отсутствии плана (`bot:apps/orchestrator/plan_lite_card.py:484-487`) | событие — этот контракт + поправка DER (KB-E); вопрос и переход плана — [[Ayla Personal Plan Contract]]; лист исполнения — UNKNOWN |
| Desired Outcome обездвижен (G-INV-9) | писателей 0; сторож-перепись | ORM-создание `DesiredOutcome` / `PlanOutcomeLink` / `ProgressObservation` вне тестов и миграций — 0 (git grep на `4dbff523`); гейты отказывают, покрыто `cat:wellness/tests/test_fail_closed.py:60-101`; Plan Lite не импортирует наблюдения тела — `cat:wellness/tests/test_plan_lite_2101.py:107-160` | **сторож-перепись «писателей вне тестов — 0»** (из брифа D-1) в каталоге не найден поиском по `*/tests/*`; лист — не назначен (предлагается завести) |
| «Забудь всё» (G-INV-12) | цели и анкета стираются вместе с планом и профилем питания | выполнено (`cat:users/forget_all_catalog.py:116-129`) | экспорт целей отсутствует — **DRF-2214** (PR-2); форма ответа и readback — DRF-2214 PR-3 |
| События `goal.*` | зарегистрированы и эмитятся | только AnalyticsEvent `goal_selected` | поправка DER (KB-E) + эмиссия (лист — UNKNOWN) |
| Наблюдаемость `SUPERSEDED` | журнал / событие перехода | нет | вместе с `goal.superseded` |

## Не входит (Non-goals)

- Семантика и таксономия Goal / Outcome (OQ-GO-6, `DesiredChangeSpecification`) — после пилота, отдельным решением.
- Активация Desired Outcome, хранение веса и наблюдений тела (`AYLA-DEC-0094`, `AYLA-DEC-0088`).
- Прогресс по цели и автоматическое `ACHIEVED` — отсутствуют намеренно; прогресс плана — только «N из M» ([[Ayla Personal Plan Contract]]).
- Переходы и состав плана, шаблоны «цель → план», частоты `PLAN_CADENCE` — [[Ayla Personal Plan Contract]] (`AYLA-DEC-0089`, `AYLA-DEC-0093`).
- Выбор следующего шага по цели, NBA — [[Ayla Decision Policy Contract]] (`AYLA-DEC-0097`).
- Цель питания и ориентиры — [[Ayla Diary and Water Contract]], [[Ayla Dietitian Capability Contract]].
- Несколько одновременно `ACTIVE` целей и Goal Relevance Resolver — не вводятся до пилота (CD §72 п.17).
- Извлечение `GoalCandidate` из разговора и политика продвижения кандидата в цель — не вводятся.
- Салон на цели (снят решением DRF-1472).
- Напоминания по сроку цели.

## Открытые вопросы

| ID | Вопрос | Кому | Почему не решено здесь |
|---|---|---|---|
| OQ-1 | Закрыт решением владельца CD §72 п.17 → раздел «Сущности» (кардинальность), инвариант G-INV-5. | — | — |
| OQ-2 | Считается ли точное совпадение свободного текста с подписью чипа (`cat:goals/resolution.py:76-86`, за выключенным флагом) подтверждённым человеком сопоставлением, или перед фильтрацией нужен явный выбор? | владелец / Product Architecture | инв. 2 и норма «сопоставление подтверждает человек» допускают оба чтения |
| OQ-3 | Правовое основание и scope хранения `ClientGoal.goal_text` и ответов анкеты: на пути записи проверки согласия нет; CSR v1.4 держит `explicit_goal` «только по scope» без владельца и маппинга | Privacy / владелец | решение Privacy; поправка CSR — отдельный документ |
| OQ-4 | Состав экспорта цели по ст. 14: все состояния и история, `goal_text`, `target_date`, ответы анкеты, legacy-строки | Privacy; исполнение DRF-2214 | не решение владельца, если принимается «экспортируется всё, что стирается» |
| OQ-5 | Стираются ли строки AnalyticsEvent `goal_selected` (`actor`, `goal_key`) при «забудь всё» | Privacy | не измерено |
| OQ-6 | Поля `goal.superseded`: хранить ли ссылку «старая → новая» в `ClientGoal` (аддитивная миграция) или только в событии; `goal_selected` — legacy alias или отдельное аналитическое событие | Product Architecture (поправка DER, KB-E) | новое поле не вводится без решения |
| OQ-7 | Возврат `ARCHIVED` / `ACHIEVED` → `ACTIVE` | владелец | не постановлялось (`cat:goals/lifecycle.py:17-19`) |
| OQ-8 | Управляемая сверка строк `LEGACY_INACTIVE_REASON_UNKNOWN` (докстринг называет 33 строки, `cat:goals/models.py:45-48`; на стенде не измерено) | владелец / главное окно | состояние не угадывается |
| OQ-9 | Что делать с активным планом при паузе, архиве или «достигнута» цели, под которую он собран (`AYLA-DEC-0090` говорит только о смене цели). Влияет на DRF-2228 | владелец | решение не принималось |
| OQ-10 | Отображение хранилища цели (`beautygo_backend`, приложение `goals`) и домена User Context в [[Ayla Repository Responsibility Matrix]] | Product Architecture | RRM его не называет |
| OQ-11 | Распространяется ли запрет `AYLA-DEC-0098` (или иное правило) на свободный `goal_text`, уходящий в промпт внешней LLM (`bot:apps/nutrition_coach/goals.py:22-26`) | Privacy / владелец | DT-1 сформулирован для флагов здоровья |

## Критерии приёмки

| # | Критерий (проверяемый) | E2E ТЗ §10 |
|---|---|---|
| AC-1 | Человек без цели записывает еду и воду, задаёт вопрос и записывается на услугу; ни один из этих путей не возвращает отказ по причине отсутствия цели. | E2E 1 |
| AC-2 | Свободный текст цели без совпадения с чипом сохраняется дословно с `goal_key = NULL`; выдача не фильтруется по цели; никакой ключ не подставлен. | E2E 2 |
| AC-3 | Выбор чипа создаёт цель с `goal_key` чипа; `goal_text` не подделан подписью чипа. | E2E 3 |
| AC-4 | Отказ от предложенного сопоставления (человек не выбрал чип и ввёл свой текст) оставляет `goal_key = NULL`; повторный показ подсказок не меняет цель. | E2E 4 (в runtime шаг «предложить сопоставление» отсутствует — см. OQ-2) |
| AC-5 | Выбор новой цели при активном плане: старая цель — `SUPERSEDED`, план остаётся `active`, эмитится `goal.superseded`, человеку показан вопрос «Обновить план под новую цель» / «Оставить текущий». | E2E 8 |
| AC-6 | Закрытие вопроса AC-5 без ответа оставляет старый план активным. | E2E 8 |
| AC-7 | Цель можно поставить на паузу, архивировать и отметить «достигнута» из Mini App без выбора замещающей (после DRF-2228). | — |
| AC-8 | Снятие с паузы при другой `ACTIVE` — 409 `GOAL_ANOTHER_ACTIVE`; другая цель не изменилась. | — |
| AC-9 | В коде модели нет инструмента записи цели; перепись инструментов консьержа не содержит goal-инструмента (сторож). | E2E 6 (по смыслу: предложение ничего не создаёт) |
| AC-10 | Сторож-перепись: ORM-создание `DesiredOutcome` / `PlanOutcomeLink` / `ProgressObservation` вне тестов и миграций — 0; `record_outcome` / `record_observation` отказывают с валидной attestation. | E2E 9 |
| AC-11 | «Забудь всё» (бот и приложение) стирает все `ClientGoal`, `GoalAnketaRun`, `GoalAnketaAnswer` человека и всех его связанных личностей в одной транзакции с планом и профилем питания; сбой откатывает всё. | E2E 21 |
| AC-12 | Экспорт персональных данных содержит цели и ответы анкеты (после DRF-2214 PR-2). | E2E 21 |
| AC-13 | Текст цели с кризисным или медицинским сигналом не создаёт `ClientGoal`; человек получает safety-ответ. | E2E 19 |
| AC-14 | Ни одно событие `goal.*` и AnalyticsEvent не содержит `goal_text` и ответов анкеты. | — |

## Влияние на миграции (Migration impact)

- **Схема цели:** контракт в редакции 0.1 изменений схемы `ClientGoal`, `GoalAnketa*` не требует. Если по OQ-6 будет решено хранить ссылку «старая → новая», это аддитивная миграция каталога (поле со значением `NULL` у существующих строк; значения задним числом не выдумываются).
- **Desired Outcome:** миграций нет; модели не удаляются (`AYLA-DEC-0094`, вариант (в) отвергнут).
- **Legacy-строки:** `LEGACY_INACTIVE_REASON_UNKNOWN` не мигрируются кодом (OQ-8).
- **События:** регистрация `goal.*` — поправка [[Ayla Domain Event Registry]] (KB-E); эмиссия — код без миграции схемы.
- **Жизненный цикл из UI (DRF-2228):** только прокси бота и экран Mini App; схема не меняется.
- **Экспорт (DRF-2214):** изменение формы ответа C5.1 — согласовать с потребителем бота (форма сообщается отдельно, не тихой сменой).
- **Откат:** `GOAL_RESOLUTION_ENABLED` (по умолчанию выкл.) и `GOAL_ANKETA_ENABLED` (по умолчанию вкл., рубильник отката к документу DRF-1190 — `cat:djangoProject/settings/base.py:532-547`).

## Трассировка

**DEC → раздел**

| Решение | Разделы |
|---|---|
| `AYLA-DEC-0087` (Goal необязательна) | Назначение; Источник истины; Инварианты G-INV-1, G-INV-6; Граница API; AC-1 |
| `AYLA-DEC-0088` (Plan Lite без веса) | Сущности (Desired Outcome); Инварианты G-INV-9; Безопасность |
| `AYLA-DEC-0089` (цель → план; связать, не слить) | Источник истины; Инварианты G-INV-10; Не входит |
| `AYLA-DEC-0090` (смена цели при активном плане) | Состояния и переходы; События (`goal.superseded`); Инварианты G-INV-8; Граница API; AC-5, AC-6 |
| `AYLA-DEC-0091` (план без цели) | Инварианты G-INV-6; Граница API |
| `AYLA-DEC-0094` (Desired Outcome не активируется) | Источник истины; Сущности; Состояния; Инварианты G-INV-9, G-INV-11; Миграции; AC-10 |
| `AYLA-DEC-0096` (safety → consent) | Безопасность; Инварианты G-INV-13 |
| `AYLA-DEC-0097` (минимальный Decision Engine) | Владение; Не входит |
| `AYLA-DEC-0098` (флаги здоровья не во внешнюю LLM) | Приватность; OQ-11 |
| `AYLA-DEC-0101` («забудь всё» — одна транзакция) | Приватность; Инварианты G-INV-12; AC-11 |
| `AYLA-DEC-0039`, `AYLA-DEC-0043` (Goal — сквозная концепция; Goal ≠ intent) | Назначение; Владение; Инварианты G-INV-2 |
| Решение владельца 21.09, журнал главного окна CD §72 п.17 (вне git) — одна активная цель до пилота | Сущности (кардинальность); Инварианты G-INV-5; Граница API (0..N, ≤1 ACTIVE); Не входит; OQ-1 (закрыт) |

**Инвариант ТЗ §7 → раздел**

| Инв. | Разделы |
|---|---|
| 1 | G-INV-1; Граница API (инструменты модели); AC-9 |
| 2 | G-INV-2, G-INV-3; Граница API (intent_resolution, резолвер); AC-2, AC-4 |
| 3 | G-INV-9, G-INV-10, G-INV-11 |
| 5, 6 | G-INV-3, G-INV-4; Сбои (резолвер без угадывания) |
| 7, 8, 9, 10 | G-INV-1, G-INV-7, G-INV-8; AC-5, AC-6 |
| 21 | G-INV-12; Приватность; AC-11, AC-12 |
| 22 | G-INV-13; Безопасность; AC-13 |
| 25 | G-INV-14; Наблюдаемость; События |

## Change Log

### v0.1 — 2026-09-21 — первичная редакция (DRF-2261)

- Первичная редакция по `AYLA-DEC-0087`, `AYLA-DEC-0090`, `AYLA-DEC-0094` и связанным решениям партии 2026-09-21.
- Runtime сверен с каталогом `4dbff523` и ботом `0e2c0100`. Отличие от отчёта этапа A: «забудь всё» каталога теперь стирает цели и анкету цели (#526, #530, DRF-2214); экспорт целей по-прежнему отсутствует.
- Предложены события `goal.selected`, `goal.state_changed`, `goal.superseded` — к регистрации в Domain Event Registry (KB-E).

### v0.1 — правки по рецензии (DRF-2261)

- `system_owner`: добавлен `ayla-platform` для хранилища в каталоге (единое соответствие во всех пяти контрактах); OQ-10 остаётся открытым.
- G-INV-12: основание — ТЗ инв. 21; бриф T-6; `AYLA-DEC-0101` (та же транзакция).
- Runtime пересверен на `cat@cca8a914` / `bot@808ca79d`: строки прокси целей (+10, #1957); медицинский вердикт гейта в safety-входе цели (#1956, DRF-2000). Прочие ссылки — на прежних снимках (шапка). Прокси `goals/state` по-прежнему нет (DRF-2228 открыт).

### v0.1 — решения владельца CD §72 п.17 вписаны (DRF-2261)

- Одна активная цель до пилота (CD §72 п.17, вне git): норма в «Сущности» и G-INV-5; OQ-1 закрыт; строка трассировки.
