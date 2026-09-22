---
node_id: ayla.architecture.personal-plan-contract
title: Ayla Personal Plan Contract
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
  - wellness
  - booking
  - cross-domain
concerns:
  - privacy
  - safety
  - explainability
system_owner:
  - ayla-platform
  - ayla-conversation
  - ayla-mini-app
source_repository: ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: high
data_categories:
  - pii
security_sensitivity: high
ai_indexing: metadata-only
export_policy: metadata-only
created: 2026-09-21
updated: 2026-09-21
review_cycle: before-major-change
depends_on:
  - "[[Ayla Constitution]]"
  - "[[OWNER_DECISION_REGISTER]]"
  - "[[Ayla MVP User Journey Specification]]"
  - "[[Ayla Memory Domain Contract]]"
  - "[[Consent Scope Registry]]"
  - "[[AMD-001 C5 Pilot Personal Context Export-Forget Contract]]"
  - "[[Ayla Domain Event Registry]]"
related:
  - "[[Ayla Goal and Desired Outcome Contract]]"
  - "[[Ayla Diary and Water Contract]]"
  - "[[Ayla Decision Policy Contract]]"
  - "[[Ayla Dietitian Capability Contract]]"
  - "[[Data Inventory Matrix]]"
  - "[[ADR-0012 Dynamic User Model]]"
  - "[[Ayla MVP Reset Roadmap]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Ayla Glossary]]"
---

# Ayla Personal Plan Contract

Машиночитаемое приложение: `03 AI System/Contracts/plan-action.schema.json` (`contract_version` major 1, форма `^1\.[0-9]+$`) — версия действия плана.

**Снимки runtime.** `cat:` — каталог (`beautygo_backend`, рабочая копия `djangoproject`), `refs/prm/dev` = `cca8a914` (21.09 16:52 MSK); `bot:` — `ai-bot-platform`, `refs/prm/dev` = `808ca79d` (21.09 18:23 MSK). Ссылки, перепроверенные на этих SHA, помечены `@cca8a914` / `@808ca79d` или «слито #NNN». Прочие `путь:строка` сняты на прежних снимках `cat@4dbff523` / `bot@0e2c0100` и не перепроверялись. В файлах, изменённых после них, номера строк могли сдвинуться: каталог — `nutrition/services/{ai_comment,nutrition_summary,nutrition_profile,profile_upsert,manual_targets}_service.py`, `nutrition/services/targets_state.py`, `nutrition/signals.py`, `wellness/migrations/0007_*`; бот — `apps/nutrition_proactive/render.py`, `apps/orchestrator/{concierge,pipeline,personal_surface,shadow_turn}.py`, `apps/orchestrator/safety/*`, `apps/miniapp_api/{views,health_gate,views_last_topic}.py`, `apps/consent/{customer,services}.py`, `apps/skills/welcome/skill.py`, `apps/channels/max/global_onboarding.py`, `docs/OPEN_DECISIONS.md`.

«ТЗ» — `docs/PROMPT-ORCHESTRATOR-GOAL.md`: инварианты §7, E2E §10. «CD §N» — журнал главного окна `docs/CURRENT_DECISIONS_2026-09-16.md`. Это отдельная нумерация, не DEC.

## Назначение (Purpose)

1. Контракт задаёт персональный план человека в первом релизе — **Plan Lite без веса** (AYLA-DEC-0088):
   - от 1 до 3 обязательств-действий трёх типов: `book_service`, `log_food`, `log_water`;
   - прогресс выражается только как «N из M действий»;
   - наблюдений тела нет.
2. Контракт фиксирует:
   - как план предлагается (таблица «цель → план» как данные, AYLA-DEC-0089);
   - как план подтверждается, закрывается и заменяется при смене цели (AYLA-DEC-0090);
   - как собирается план без цели (AYLA-DEC-0091);
   - как хранится провенанс каждого действия и что участвует в расчётах (AYLA-DEC-0092);
   - какой смысл несут частоты (AYLA-DEC-0093);
   - что план отдаёт Decision Engine (AYLA-DEC-0097).
3. Контракт заменяет в части плана §2, §5 Sprint 1–4 и §7 документа [[Ayla MVP Reset Roadmap]] (AYLA-DEC-0087, K-1).

## Владение (Ownership)

| Что | Владелец | Основание |
|---|---|---|
| Семантика плана, состояния, провенанс | Product Architecture (этот контракт) | AYLA-DEC-0088…0093 |
| Хранение и писатель плана (`PersonalPlan`, `PlanAction`) | каталог, приложение `wellness` (`ayla-platform`) | `cat:wellness/models.py:93-157`, `:390-452`; `cat:wellness/plan_lite.py:151-217` |
| Шаблоны «цель → план» (`PlanTemplate`) — **данные владельца**, правка в админке | владелец продукта; носитель — каталог | AYLA-DEC-0089; `cat:wellness/models.py:477-535`; `cat:wellness/admin.py:15-16` |
| Смысл частот (`PLAN_CADENCE`) | владелец; реестр правил планирования | AYLA-DEC-0093 |
| Предложение и подтверждение в чате | бот, `ayla-conversation` | `bot:apps/orchestrator/plan_lite_card.py` |
| Экран «Мой план» | Mini App, `ayla-mini-app` | `bot:apps/miniapp/src/screens/PlanLiteScreen.tsx`; прокси `bot:apps/miniapp_api/views_plan_lite.py` |
| Факты выполнения | поставщики фактов доменов Nutrition и Booking; решение «выполнено» — только домен плана | `cat:wellness/fact_providers.py:1-10` |
| Выбор следующего действия плана | [[Ayla Decision Policy Contract]] | AYLA-DEC-0097 |

- `PlanTemplate` — **носитель** утверждённой таблицы §51 (AYLA-DEC-0089, AYLA-DEC-0093).
- `PlanTemplate` **не является** Plan Composer: он ничего не составляет и не выводит (ТЗ §6 «Plan»).
- Сущности Plan Composer в этом контракте нет.

## Источник истины (Source of truth)

1. **План и его действия** — строки каталога `PersonalPlan` и `PlanAction`. Единственный источник.
   - Бот и Mini App копий не хранят и читают план через:
     - поле `plan_lite` документа wellness-context (`cat:wellness/context_read.py:75`, `:82`, `:92`);
     - прокси (`bot:apps/miniapp_api/views_plan_lite.py:153-158`).
   - Маркер «Не сейчас» `skill_state["plan_lite"].plan_proposal_declined_at` (`bot:apps/orchestrator/plan_lite_card.py:108-110`, `:637-644`) — состояние разговора, не плана.
2. **Актуальное состояние действия** — единственная версия со `status = active` (AYLA-DEC-0092).
   - Второго источника, например изменяемой строки плюс журнала, не вводится (вариант (б) P-2 отвергнут).
3. **Частоты и тексты «почему»**:
   - в каталоге — активная версия `PlanTemplate` по `goal_key`;
   - в KB — тип `PLAN_CADENCE` реестра `planning-rules-registry.yaml` (AYLA-DEC-0093; поправка — отдельный PR);
   - сид — дословная копия таблицы CD §51 (`cat:wellness/plan_lite_templates.py:54-88`).
4. **Цель плана**:
   - ссылка `PersonalPlan.goal` → `goals.ClientGoal`, `SET_NULL` (`cat:wellness/models.py:122-128`);
   - снимок `goal_key` (`:129-134`).
   - Семантика цели — в [[Ayla Goal and Desired Outcome Contract]].
   - Desired Outcome плану не источник (AYLA-DEC-0094): `PlanOutcomeLink` у Plan Lite не создаётся (`cat:wellness/plan_lite.py:18-19`).
5. **Факты выполнения** — журналы доменов: `FoodLog`, `WaterEntry`, `Appointment`. Итог «N из M» — производная, не хранится (`cat:wellness/plan_lite.py:312-337`).
6. **Предложение плана** — эфемерно:
   - вычисляется на каждый запрос (`cat:wellness/plan_lite.py:223-248`);
   - не хранится и источником истины не является.

## Сущности

### PersonalPlan

| Поле | Сейчас (`cat:wellness/models.py`) | Цель контракта |
|---|---|---|
| `id` | UUID, `:104` | без изменений |
| `user` | FK, `PROTECT`, `:105-109` | без изменений |
| `status` | `active` \| `closed_by_user`, `:100-102` | + `superseded` (AYLA-DEC-0090) |
| `superseded_by` | нет | новое: ссылка на план, сменивший этот; обязательна при `superseded`, иначе `null` (AYLA-DEC-0090) |
| `goal` | FK `ClientGoal`, nullable, `SET_NULL`, `:122-128` | `null` допустим (AYLA-DEC-0091) |
| `goal_key` | снимок, `:129-134` | без изменений; пустой у плана без цели |
| `source` | `manual` \| `template:<goal_key>:v<N>`, `:138-142` | без изменений; у плана без цели — только `manual` (AYLA-DEC-0091) |
| `created_at`, `closed_at` | `:143-144` | без изменений; для `superseded` — момент замены (см. открытый вопрос 6) |

- Ограничение «не более одного `active` на человека» — `personalplan_one_active_per_user` (`:148-154`). Сохраняется.
- Состояние «пауза» **не вводится**: паузы плана до пилота нет (решение владельца 21.09, журнал главного окна CD §72 п.26 (вне git)). Человеку доступны «изменить» и «новый план».

### PlanAction — версия действия

Одна строка — одна **неизменяемая версия** действия (AYLA-DEC-0092). Форма — `plan-action.schema.json`.

| Поле | Сейчас (`cat:wellness/models.py:390-452`) | Цель |
|---|---|---|
| `action_id` (`id`) | UUID | без изменений; идентификатор версии |
| `plan_id` | FK `PROTECT` | без изменений |
| `action_type` | `book_service` \| `log_food` \| `log_water`, `:406-412` | без изменений; расширение — только решением владельца |
| `cadence` | `per_day` \| `per_week` \| `per_2_weeks`, `:414-419` | без изменений; смысл — `PLAN_CADENCE` (AYLA-DEC-0093) |
| `target_count` | 1…14: модель допускает любое положительное, предел в писателе `cat:wellness/plan_lite.py:58`, `:125` | 1…14 |
| `status` | нет | `active` \| `superseded` \| `removed` |
| `source` | нет | `template` \| `user_selected` \| `user_edited` \| `specialist` \| `ayla_proposal_accepted` |
| `source_ref`, `source_version` | нет; провенанс только у плана | ссылка и версия источника. У `template` — ключ и версия шаблона. У `user_edited` — ссылка и версия исходного шаблона, если правлена строка шаблона; иначе `null` / `null` |
| `changed_by` | нет | `user` \| `specialist` \| `system` |
| `changed_at` | есть только `created_at` | время создания версии |
| `reason_code` | нет | `initial` \| `user_edit` \| `goal_changed` \| `plan_rebuilt` \| `action_removed` \| `specialist_change` — закрытый список |
| `supersedes_action_id` | нет | `null` только при `reason_code = initial` |
| время действия | нет | слот дня `утро` / `день` / `вечер` + дни недели (решение владельца 21.09, журнал главного окна CD §72 п.18 (вне git)). Точный час — после пилота. Имя и форма поля — при миграции (см. «Влияние на миграции» п. 11); в `plan-action.schema.json` поле в этой редакции не вводится |

**Время действия** (CD §72 п.18). Время действия плана задаётся только слотом дня (`утро` / `день` / `вечер`) и днями недели. Точного часа до пилота нет. Этим контракт не вводит напоминаний и их форм: время — атрибут обязательства, по которому Decision Engine узнаёт «действие на текущее время» ([[Ayla Decision Policy Contract]], ступень 4).

**Идентичность действия.** Писатель допускает не более одного действия каждого `action_type` на план (`cat:wellness/plan_lite.py:128-129`). Поэтому логическое действие в Plan Lite — пара (`plan_id`, `action_type`), а его версии связаны цепочкой `supersedes_action_id`.

**Категория `book_service`.**
- Сейчас у действия категории нет. Для плана с целью она выводится из цели:
  - `goal_key → GoalOptionCategory` (`cat:wellness/fact_providers.py:70-79`);
  - комментарий `cat:wellness/models.py:489-490`.
- Для плана без цели AYLA-DEC-0091 требует считать запись «только по категории, которую человек выбрал сам». Носителя такой категории в коде нет.
- **Норма** (решение владельца 21.09, журнал главного окна CD §72 п.19 (вне git)): в плане без цели человек сам выбирает категорию услуг (например, «массаж») **из списка категорий каталога**. Действие `book_service` такого плана несёт **ссылку на категорию каталога**; свободный текст категории и категория, выведенная системой, не допускаются.
- Имя поля — **предложение**: `service_category_ref` (ссылка на категорию каталога). В `plan-action.schema.json` поле в этой редакции не вводится; добавление — при миграции (см. «Влияние на миграции» п. 12).

### PlanTemplate — носитель таблицы «цель → план»

- Поля: `goal_key`, `actions` (1–3 действия в форме `PlanAction`), `why_text`, `nutrition_goal_hint`, `version`, `is_active` (`cat:wellness/models.py:493-518`).
- Ограничения: одна активная версия на `goal_key`; пара (`goal_key`, `version`) уникальна (`:520-532`).
- Версии не удаляются: на них ссылаются планы (`:482-484`).
- `nutrition_goal_hint` — **подсказка** анкете питания (связать, не слить; AYLA-DEC-0089). В план она не пишется и ничего не предвыбирает (`:505-515`).
- Персональных данных нет (`:486-487`).

### PlanProposal — предложение (не сущность хранения)

- Вычисляемый документ `{goal_key, why, template_version, actions}` по активной цели из активного шаблона (`cat:wellness/plan_lite.py:223-248`).
- Не хранится.
- Без активной цели не строится: Ayla без цели план не предлагает (AYLA-DEC-0091). Решение владельца 21.09 (CD §71 п.3): «Без цели Ayla не предлагает и не создаёт план по своей инициативе. Такой план может собрать только сам пользователь. Это правило P-1 имеет приоритет». Явный запрос плана без цели открывает ручной конструктор (`ComposeManual`), а не предложение.

### Производные (не хранятся)

- `done_count` — «N» за текущее ведро каденса (`cat:wellness/plan_lite.py:276-291`).
- `within_target_count` у `log_food` — «в ориентире N» (`:294-309`).
- `bucket` — границы ведра (`:256-269`):
  - `per_day` — календарный день;
  - `per_week` — неделя с понедельника по воскресенье;
  - `per_2_weeks` — 14 дней от даты создания плана.
- **Норма пояса ведра.** Ведро `per_day` / `per_week` считается по **локальной дате человека** — по цепочке пояса AYLA-DEC-0095 ([[Ayla Diary and Water Contract]], I-3; `local_date` DiaryDay). Так «в ориентире N» плана и «день завершён» дневника читают одни сутки. Текущий runtime считает по поясу сервера — расхождение, «Граница API» R-18.

## Состояния и переходы

### План

| Из | В | Триггер | Условие |
|---|---|---|---|
| — | `active` | подтверждение предложения **кнопкой** (чат `cb:plan:accept:<v>`, экран «Подтвердить план») или «Составить план» в конструкторе | нет другого `active`; для плана из шаблона — активная цель; для ручного плана цель не требуется (AYLA-DEC-0091) |
| `active` | `closed_by_user` | человек закрыл план | — |
| `active` | `superseded` | человек при смене цели выбрал «Обновить план» **и** подтвердил новый план кнопкой (AYLA-DEC-0090) | в одной транзакции: старый → `superseded`, `superseded_by` = новый; новый → `active` |
| `active` | `active` (без изменения) | смена цели и «Оставить текущий» или отказ от подтверждения нового (AYLA-DEC-0090) | план помечается, под какую цель он собран |
| `closed_by_user`, `superseded` | — | терминальные | история; не пересчитываются |

Запрещённые переходы:
- любой переход без действия человека (инв. ТЗ 7–9);
- `active → superseded` до подтверждения нового плана (AYLA-DEC-0090);
- возврат из терминальных состояний.

### Версия действия

| Из | В | Триггер |
|---|---|---|
| — | `active` | создание плана (`reason_code = initial`) |
| `active` | `superseded` | создана следующая версия того же действия (`user_edit`, `specialist_change`, `goal_changed`, `plan_rebuilt`) |
| `active` | `superseded` плюс новая версия `removed` | удаление действия (`action_removed`) |

Правила переходов версии:
- Переход — всегда вставка новой строки. Прежняя версия меняет только `status`, её содержимое неизменно (AYLA-DEC-0092).
- Версия `removed` терминальна для логического действия: с этого момента оно не входит в «M» (AYLA-DEC-0092).
- Версии закрытого или заменённого плана не меняются.

## Команды

Все команды выполняет только человек через кнопку или экран. Специалист план клиента не меняет: он только предлагает изменение, клиент подтверждает кнопкой (решение владельца 21.09, журнал главного окна CD §72 п.20 (вне git); команды `ProposeSpecialistChange` / `ConfirmSpecialistChange`). **LLM ни одной команды не вызывает** (инв. ТЗ 7, 8).

| Команда | Канал | Эффект | Сейчас |
|---|---|---|---|
| `ProposePlan` | чат, Mini App | только чтение; предложение из активного шаблона активной цели | `GET …/plan-lite/proposal/` (`cat:wellness/plan_lite_api.py:144-180`) |
| `ConfirmProposal(template_version, actions)` | кнопка чата `cb:plan:accept:<v>`; кнопка экрана | создаёт `active` план. Строки, принятые без правки, — `source = template` (ссылка и версия шаблона). Строки, изменённые человеком до подтверждения, — `source = user_edited`. Все — `reason_code = initial`. Снятые строки не создаются | `POST …/plan-lite/` (`cat:wellness/plan_lite.py:151-199`); провенанс действий теряется — см. «Граница API» |
| `ComposeManual(actions)` | конструктор Mini App | план `source = manual`, действия `source = user_selected`, `reason_code = initial`; цель не требуется (AYLA-DEC-0091) | сейчас требует активной цели: 404 `no_active_goal` (`cat:wellness/plan_lite.py:172-175`) |
| `ReviseAction(action_type, cadence?, target_count?)` | Mini App | новая версия `source = user_edited`, `reason_code = user_edit`, `supersedes_action_id` = прежняя; прежняя → `superseded` | нет; «Изменить план» = закрыть и составить заново (`bot:apps/miniapp/src/screens/PlanLiteScreen.tsx:28`, `:353-369`) |
| `RemoveAction(action_type)` | Mini App | новая версия `status = removed`, `reason_code = action_removed`; прежняя → `superseded` | нет |
| `AddAction(action_type, cadence, target_count)` | Mini App | новая версия `source = user_selected`, `reason_code = initial`, пока в плане меньше 3 активных действий и тип не повторяется | нет; порядок допуска — открытый вопрос 7 |
| `ClosePlan` | чат, Mini App | `active → closed_by_user` | `DELETE …/plan-lite/` (`cat:wellness/plan_lite.py:202-217`) |
| `ResolveGoalChange(choice)` | вопрос в чате и та же развилка на экране цели; триггер вопроса — событие `goal.superseded` (предлагаемое, «Входы») при активном плане | `keep` — план остаётся `active` с пометкой цели; `update` — показывается `ProposePlan` по новой цели, план не меняется до `ConfirmSupersession` | нет (`cat:goals/lifecycle.py:126-135` план не трогает) |
| `ConfirmSupersession(template_version, actions)` | кнопка | одна транзакция: новый план `active`, старый `superseded` + `superseded_by`. `reason_code` действий нового плана — по открытому вопросу 5 | нет |
| `ProposeSpecialistChange(action_type, cadence?, target_count?)` | поверхность специалиста (какая — открытый вопрос 14) | **только предложение**: план и версии действий не меняются; клиенту показывается предложение с кнопкой подтверждения (CD §72 п.20) | нет (пути записи специалистом нет) |
| `ConfirmSpecialistChange` | кнопка клиента | новая версия `source = specialist`, `changed_by = specialist`, `reason_code = specialist_change`, `supersedes_action_id` = прежняя; прежняя → `superseded`. Без кнопки клиента ничего не меняется | нет |
| `ExportPlan` / `ForgetPlan` | «Забудь всё», экспорт ст. 14 | см. «Приватность» | стирание — есть, экспорт — нет |

Правила подтверждения:
- Текст «да», «подтверждаю», «ок» подтверждением не является (инв. ТЗ 10). Сторож: `bot:apps/orchestrator/tests/test_plan_chat_2125.py:292-315` `TestConfirmOnlyByButton`.
- Набранная вручную строка вида `cb:plan:…` — не тап (`bot:apps/orchestrator/plan_lite_card.py:100`).
- Если версия шаблона изменилась, пока карточка лежала в чате, план не создаётся. Показывается новая карточка (`bot:apps/orchestrator/plan_lite_card.py:517-527`).

## События

Все события ниже **предлагаются к регистрации (KB-E)** в [[Ayla Domain Event Registry]] со статусом `registration_status: proposed`. В runtime их нет (`git grep` по обоим репозиториям на указанных SHA: 0 вхождений).

| Событие | Когда | Полезная нагрузка (без персональных значений) |
|---|---|---|
| `plan.created` | план стал `active` | `plan_id`, `source` (`manual` \| `template`), `template_version` \| null, `has_goal` (bool), число действий |
| `plan.closed` | `active → closed_by_user` | `plan_id` |
| `plan.superseded` | `active → superseded` | `plan_id`, `superseded_by` |
| `plan.action.revised` | создана версия действия, кроме `initial` | `plan_id`, `action_id`, `supersedes_action_id`, `action_type`, `reason_code`, `changed_by`, `status` |

- В событиях нет `goal_text`, фактов дневника, калорий или текста «почему».
- Вместо событий сейчас пишутся логи без тел:
  - `orchestrator.plan_lite.accepted` и др. (`bot:apps/orchestrator/plan_lite_card.py:554-560`);
  - `customer_plan_lite.created` (`bot:apps/miniapp_api/views_plan_lite.py:202-207`).

## Входы и выходы

**Входы:**
- активная цель (`ClientGoal`, state `ACTIVE`) — не обязательна (AYLA-DEC-0091);
- событие `goal.superseded` (предлагаемое, [[Ayla Goal and Desired Outcome Contract]]) — триггер `ResolveGoalChange` при активном плане (AYLA-DEC-0090);
- событие `goal.state_changed` (предлагаемое) — **не потребляется** до решения GOAL OQ-9 (что делать с планом при паузе, архиве, «достигнута»);
- активный `PlanTemplate` по `goal_key`;
- команды человека (раздел «Команды»);
- факты:
  - `FoodLog.logged_at`;
  - `WaterEntry.ts` без мягко удалённых;
  - `Appointment` — целевое правило в инварианте I-9;
- для `within_target_count` — действующий подтверждённый калорийный ориентир (`cat:nutrition/services/plan_facts.py:31-51`).

**Выходы:**
- Документ `plan_lite` (`cat:wellness/plan_lite.py:312-337`): `{plan_id, goal_key, actions:[{action_type, cadence, target_count, done_count, bucket, within_target_count?}]}`.
  - Только форма и факты; процентов, «достигнуто» и шкалы нет (AYLA-DEC-0088).
  - Цель: по одной **актуальной** версии на логическое действие (AYLA-DEC-0092).
  - Добавляются провенанс для показа «почему это действие» и пометка цели плана при расхождении с активной целью (AYLA-DEC-0090). Состав полей — при реализации, в пределах этой схемы.
- Предложение `{goal_key, why, template_version, actions}`.
- Для Decision Engine (AYLA-DEC-0097, ступень «следующее действие активного плана»):
  - актуальные версии действий с `done_count < target_count` в текущем ведре;
  - `action_id` версии — как ссылка на факт и провенанс;
  - время действия (слот дня + дни недели, CD §72 п.18) — для ступени «подтверждённое действие на текущее время».
  - Порядок выбора между действиями задаёт [[Ayla Decision Policy Contract]].
- События — раздел «События».

## Инварианты

| № | Инвариант | Основание |
|---|---|---|
| I-1 | План содержит от 1 до 3 действий, по одному на `action_type`; типы — только `book_service`, `log_food`, `log_water`; `target_count` 1…14 | AYLA-DEC-0088; `cat:wellness/plan_lite.py:56-58`, `:110-130` |
| I-2 | На пути плана нет ни одного наблюдения тела (вес, `ProgressObservation`); прогресс — только «N из M», без процентов результата | AYLA-DEC-0088; ТЗ инв. 3 |
| I-3 | LLM не создаёт, не меняет, не закрывает и не заменяет план и его действия. Писатели — только кнопка чата и экран Mini App | ТЗ инв. 7, 8; AYLA-DEC-0090 |
| I-4 | Предложение ничего не создаёт. План возникает только из явного подтверждения | ТЗ инв. 9; AYLA-DEC-0089, AYLA-DEC-0090 |
| I-5 | Подтверждение — только кнопкой; текстовое «да» план не создаёт и не меняет | ТЗ инв. 10 |
| I-6 | Не более одного `active` плана на человека | `cat:wellness/models.py:148-154` |
| I-7 | Смена цели не закрывает, не заменяет и не меняет активный план молча. Старый план остаётся `active`, пока новый не подтверждён кнопкой; при замене — `superseded` + `superseded_by` | AYLA-DEC-0090; ТЗ инв. 7–9 |
| I-8 | План без цели — только ручной (`source = manual`), все действия `source = user_selected`. Ayla без цели план не предлагает и не создаёт по своей инициативе. `book_service` такого плана считается только по категории, выбранной человеком из списка категорий каталога (ссылка на категорию каталога) | AYLA-DEC-0091; решение владельца 21.09 (CD §71 п.3); решение владельца 21.09, журнал главного окна CD §72 п.19 (вне git) |
| I-9 | «Выполнено» для `book_service` — только визит с серверным статусом `completed`, отнесённый к ведру **по дате визита**. Будущая запись, `confirmed`, `pending`, `awaiting_payment`, `cancelled`, `no_show` выполнением не являются. Путь исполнения — DRF-2216 | ТЗ инв. 11, 12, 13 |
| I-10 | Каждая версия действия несёт `source`, `source_ref`, `source_version`, `changed_by`, `changed_at`, `reason_code` (закрытый список), `supersedes_action_id` | AYLA-DEC-0092; ТЗ инв. 25 |
| I-11 | Версии неизменяемы. Правка — новая версия; удаление — версия `removed`, не стирание (кроме «Забудь всё», см. «Приватность») | AYLA-DEC-0092 |
| I-12 | На логическое действие приходится ровно одна версия `active`, сторож — на уровне БД. В «N из M», в показе плана и в Decision Engine участвует только она. Версии `superseded` и `removed` — история, в текущий расчёт не входят и прошлое не пересчитывают | AYLA-DEC-0092, AYLA-DEC-0097 |
| I-13 | Правка человека отличима от предложения Ayla: изменённая до подтверждения строка — `user_edited`, не `template` | AYLA-DEC-0092; ТЗ инв. 25 |
| I-14 | Частота действия — `PLAN_CADENCE`: только подтверждённая человеком организационная регулярность. Она не доказывает медицинскую или косметологическую пользу, совместимость процедур, минимальный или максимальный интервал, число процедур; к услуге как курс не применяется. Ни один компонент не приводит её как такое основание | AYLA-DEC-0093; ТЗ инв. 4 |
| I-15 | Частоты и тексты «почему» берутся только из утверждённой таблицы (данные `PlanTemplate`). Компоненты их не выдумывают и не выводят курс из поведения (ADR-0012 N-04, утверждено AYLA-DEC-0093) | AYLA-DEC-0089, AYLA-DEC-0093; ТЗ инв. 4 |
| I-16 | «В ориентире N» считается только по завершённым дням дневника. Ведра `per_day` / `per_week` — по локальной дате человека (цепочка пояса AYLA-DEC-0095) | AYLA-DEC-0095; ТЗ инв. 14, 15 |
| I-17 | Нет шаблона — нет предложения: 404 `no_template`, не пустой план. Нет ориентира — `within_target_count = null`, не 0 | `cat:wellness/plan_lite.py:90-92`, `:294-309`; ТЗ инв. 5, 6 |
| I-18 | Нового scope согласия план не вводит | AYLA-DEC-0088 |
| I-19 | «Забудь всё» стирает план и все версии действий; экспорт их отдаёт | AYLA-DEC-0101 (та же транзакция «всё или ничего»); ТЗ инв. 21 |
| I-20 | Специалист план клиента не меняет. Его изменение — предложение; версия `source = specialist` появляется только после подтверждения клиентом **кнопкой**. До подтверждения план и версии действий не меняются | решение владельца 21.09, журнал главного окна CD §72 п.20 (вне git); ТЗ инв. 7–10 |
| I-21 | Время действия — только слот дня (`утро` / `день` / `вечер`) и дни недели. Точного часа до пилота нет | решение владельца 21.09, журнал главного окна CD §72 п.18 (вне git) |
| I-22 | Паузы плана до пилота нет: состояния `paused` у `PersonalPlan` не существует | решение владельца 21.09, журнал главного окна CD §72 п.26 (вне git) |

## Согласие (Consent)

1. План нового scope не вводит (AYLA-DEC-0088).
   - План — производная от цели, данной под своим основанием, и от уже согласованных журналов (`cat:wellness/plan_lite.py:21-24`).
2. Запись фактов еды, которую считает `log_food`, идёт под согласием дневника (`food_diary_processing`, [[Consent Scope Registry]]) на стороне записи, не в плане.
   - Отзыв согласия дневника план не закрывает. Новые факты `log_food` при этом не появляются.
3. Mini App снимает строку «дневник» из предложения без согласия дневника (fail-closed) и не отправляет её в POST (`bot:apps/miniapp/src/screens/PlanLiteScreen.tsx:30-33`, `:288-294`).
   - Норма ли это для всех каналов — открытый вопрос 8.
4. Возврат к плану по opt-in (A4, DRF-2126) — proactive-уведомление по AYLA-DEC-0087. Регулируется Consent Scope Registry v1.5 и [[Ayla Decision Policy Contract]], не этим контрактом.

## Приватность (Privacy)

1. **Состав данных.** План и версии действий — персональные данные, внесённые человеком (`data_categories: pii`).
   - `goal_key` плана может раскрывать намерение человека (например, `body_shape`). Отсюда `data_sensitivity: high`.
   - Данных о здоровье план не хранит (I-2).
   - `within_target_count` — производная от профиля питания; в плане не хранится.
2. **«Забудь всё»** (AYLA-DEC-0101, ТЗ инв. 21) стирает `PersonalPlan` во всех состояниях и **все** версии `PlanAction`, включая `superseded` и `removed`, в одной транзакции с целями, профилем питания и дневником. Проверено на `cat@4dbff523`:
   - Функция `users/forget_all_catalog.py:77-158` стирает `PlanAction` (`:123`) до `PersonalPlan` (`:124`), потому что у `PlanAction.plan` стоит `PROTECT`. Введена PR #526 (`cf2e99a7`, DRF-2214), предок `refs/prm/dev`.
   - Её зовут все три пути:
     - приложение — `users/personal_context_views.py:200`;
     - `DELETE …/personal-context/` — `users/internal_personal_context_api.py:220`;
     - настоящий путь бота C5.2 — `users/personal_data_api.py:356-366`, по каждой личности субъекта в одной транзакции; подключён PR #530 (`33eddecc`, DRF-2214).
   - Сам `users/personal_context_erasure.py` план **не** стирает. Стирает соседний модуль `forget_all_catalog.py`, вызываемый рядом.
   - Удаление аккаунта (D3): `users/deletion_executor.py:572-573`.
   - **Следствие миграции:** появятся ссылки `superseded_by` (план → план) и `supersedes_action_id` (версия → версия). Стирание обязано снимать их внутри набора человека до удаления строк, как это уже делается для `ProgressObservation.superseded_by` (`users/forget_all_catalog.py:126`), либо ссылки должны быть `SET_NULL`. Иначе стирание упадёт на `PROTECT`.
3. **Экспорт** (ст. 14, AMD-001 C5.1) обязан отдавать план во всех состояниях и **все** версии действий с провенансом.
   - Сейчас экспорт каталога C5.1 плана не содержит: `users/personal_data_api.py:266-295` отдаёт профиль, `personal_context`, профиль специалиста и связанные личности.
   - Расхождение → DRF-2214 (экспортная часть).
4. `PlanTemplate` — не персональные данные, в стирание не входит (`cat:wellness/models.py:486-487`).
5. **Логи и события** — без тел, `goal_text`, фактов еды и идентификатора канала (DRF-2009; `bot:apps/orchestrator/plan_lite_card.py:48-49`).
6. Поправки [[Data Inventory Matrix]] (строка «план и версии действий») и [[AMD-001 C5 Pilot Personal Context Export-Forget Contract]] — отдельными PR волны AYLA-DEC-0087.

## Безопасность (Safety)

1. Safety имеет приоритет над планом (ТЗ инв. 22).
   - В Decision Engine ступень «следующее действие плана» идёт после safety и явного намерения (AYLA-DEC-0096, AYLA-DEC-0097).
   - При исходе `BLOCKED` или `HANDOFF` действие плана не предлагается.
2. `PLAN_CADENCE` не является медицинским основанием (I-14). Тексты «почему» показываются дословно из данных владельца, без обещаний результата (`cat:wellness/models.py:502-504`).
3. Никаких наблюдений тела, веса, процентов результата или «ты пропустил» (I-2; `bot:apps/miniapp/src/screens/PlanLiteScreen.tsx:21-27`, `:35-37`).
4. `book_service` ведёт к подбору услуг по курируемому ключу цели, а не к рекомендательному движку (`bot:apps/orchestrator/plan_lite_card.py:564-622`).
   - Наличие услуги не подменяет семантическую рекомендацию (ТЗ инв. 23).
5. Флаги здоровья в план не входят и во внешнюю LLM через план не передаются (AYLA-DEC-0098; у плана таких полей нет).

## Наблюдаемость (Observability)

1. События «Событий» после регистрации.
2. Каждая версия действия сама является журналом: `changed_by`, `changed_at`, `reason_code`, `supersedes_action_id` отвечают на вопрос «почему в моём плане это действие» (ТЗ инв. 25).
3. Логи бота — без тел, с классом отказа и версией шаблона. Существующие:
   - `orchestrator.plan_lite.{proposal, card, accepted, proposal_changed, book, book_no_services, declined, unavailable}` (`bot:apps/orchestrator/plan_lite_card.py:438-640`);
   - `customer_plan_lite.*` (`bot:apps/miniapp_api/views_plan_lite.py:127-135`, `:202-207`).
4. Метрики, которые нужно измерять (без порогов — их нет в решениях):
   - число планов по `source`;
   - доля строк `user_edited` среди подтверждений;
   - доля отказов `no_template` и `no_active_goal`;
   - число `superseded` по причине смены цели.
5. Наличие шаблонов §51 гарантирует миграция — так (слито #533, `a8c8f0c3`, DRF-2229): `cat@cca8a914:wellness/migrations/0007_seed_plan_templates_if_empty.py:30-45` кладёт активную версию 1 из `PLAN_TEMPLATES_SEED` только для целей, у которых в `PlanTemplate` нет ни одной строки; цели с активной (в том числе правленной в админке) или только снятыми версиями не трогает; обратная — ничего не делает (`:1-19`, `:54`). Ручная команда `seed_plan_templates` по-прежнему кладёт версию кода поверх отличающейся активной (`:16-19`). Применена ли миграция на стенде — **UNKNOWN** (стенд не проверялся).

## Поведение при сбоях (Failure behavior)

| Ситуация | Поведение |
|---|---|
| `PLAN_LITE_ENABLED` выключен | 404 `PLAN_LITE_DISABLED`, не 5xx: постоянный 5xx открыл бы общий circuit breaker бота (`cat:core/errors.py:239-241`; `cat:djangoProject/settings/base.py:558`; `bot:config/settings/base.py:1735`). Старая кнопка чата — «кнопка устарела», модель не зовётся (`bot:apps/orchestrator/plan_lite_card.py:632-634`) |
| Каталог недоступен | «сервис не отвечает»; план не создаётся, не закрывается и не заменяется; повтор — действие человека |
| Гонка двух подтверждений | частичная уникальность → 409 `PLAN_LITE_ALREADY_ACTIVE`, показывается существующий план (`cat:wellness/plan_lite.py:183-191`; `bot:apps/orchestrator/plan_lite_card.py:536-549`) |
| Шаблон обновился после показа предложения | план не создаётся, новая карточка (`bot:apps/orchestrator/plan_lite_card.py:517-527`) |
| Нет шаблона у цели | 404 `no_template`; конструктор без предложения (`bot:apps/miniapp/src/screens/PlanLiteScreen.tsx:14-16`) |
| Сбой посреди создания или замены плана | одна транзакция: либо весь план с версиями действий (и `superseded` старого), либо ничего |
| Подтверждение нового плана при смене цели не дошло | старый план остаётся `active` (AYLA-DEC-0090) |
| Нет ориентира калорий | `within_target_count = null` — строки нет, не 0 |
| Факт-поставщик получил неизвестный `action_type` | `ValueError`, не тихий ноль (`cat:wellness/fact_providers.py:97-111`) |
| Нарушение единственности `active`-версии | отказ записи на уровне БД; частично записанная версия не остаётся |

## Граница API / runtime

| # | Целевое поведение | Текущий runtime | Расхождение → лист |
|---|---|---|---|
| R-1 | Подтверждение только кнопкой; LLM плана не касается | Так: `bot:apps/orchestrator/plan_lite_card.py:500-561`, сторож `bot:apps/orchestrator/tests/test_plan_chat_2125.py:292-315`. Писатели `create_plan_lite` — только `bot:apps/orchestrator/plan_lite_card.py:533` и `bot:apps/miniapp_api/views_plan_lite.py:194`; у инструментов консьержа плана нет | нет |
| R-2 | Предложение эфемерно | Так: `cat:wellness/plan_lite.py:223-248` | нет |
| R-3 | План без цели (ручной) | 404 `no_active_goal`: `cat:wellness/plan_lite.py:172-175`, `cat:wellness/plan_lite_api.py:103-109`. Поле `goal` уже nullable | снять для `source = manual` → лист P-1 (UNKNOWN: номер не назначен) |
| R-4 | `book_service` без цели — по категории, выбранной человеком из списка категорий каталога (ссылка на категорию, CD §72 п.19) | без категорий цели засчитывается **любая** бронь (`cat:wellness/fact_providers.py:70-80`); носителя категории нет (`cat:wellness/models.py:489-490`) | поле-ссылка на категорию каталога (имя — предложение) → лист P-1 |
| R-5 | Провенанс каждой версии действия; одна актуальная версия; сторож уникальности | полей нет (`cat:wellness/models.py:390-452`); провенанс только у плана (`:138-142`) | лист P-2 (UNKNOWN) |
| R-6 | Правка до подтверждения — `user_edited` | Mini App шлёт изменённые или снятые строки с `template_version`, и план помечается `template:…:vN` (`bot:apps/miniapp/src/screens/PlanLiteScreen.tsx:288-294`, `:335-338`; `cat:wellness/plan_lite.py:165-169`, `:176-182`) — **правка теряет провенанс** | лист P-2 |
| R-7 | Правка или удаление действия — новая версия в том же плане | «Изменить план» **сначала закрывает** план, потом открывает конструктор (`bot:apps/miniapp/src/screens/PlanLiteScreen.tsx:353-369`). Уход из конструктора оставляет человека без плана | лист P-2 |
| R-8 | Смена цели: спросить; `superseded` после подтверждения | `supersede_active` плана не трогает (`cat:goals/lifecycle.py:126-135`, `cat:goals/api.py:249-259`). Предложение зовётся только при отсутствии плана (`bot:apps/orchestrator/plan_lite_card.py:484-487`). Карточка печатает «Твоя цель:» по снимку `goal_key` старой цели. `_book` подбирает по старому ключу (`:593-596`). Статуса `superseded` нет (`cat:wellness/models.py:100-102`) | лист G-1 (UNKNOWN); смежно DRF-2228 (lifecycle цели в UI) |
| R-9 | `book_service`: только `completed` по дате визита | `CONFIRMED` **или** `COMPLETED` по `created_at` (`cat:wellness/fact_providers.py:43-46`, `:64-69`) — будущая подтверждённая запись засчитывается. Нужные поля есть: `Appointment.start_datetime` (`cat:appointments/models.py:92`), статусы `:34-39`. `completed` может откатиться в `no_show` (`:389`), поэтому счёт читается на момент расчёта | **DRF-2216** |
| R-10 | «В ориентире N» — только по завершённым дням | считается по любому дню с записями, включая сегодняшний незакрытый (`cat:nutrition/services/plan_facts.py:14-17`, `:44-51`). Понятия «день завершён» в коде нет | лист по AYLA-DEC-0095 (UNKNOWN; смежно DRF-2215); см. [[Ayla Diary and Water Contract]] |
| R-11 | Шаблоны §51 на стенде | так (слито #533, `a8c8f0c3`): миграция-заполнитель `cat@cca8a914:wellness/migrations/0007_seed_plan_templates_if_empty.py:30-45` кладёт версию 1 из сида (`cat:wellness/plan_lite_templates.py:54-88`) для целей без строк, правленные в админке не трогает. Остаток: выравнивание «админка ↔ код» миграция не решает (`:16-19`); применение на стенде не проверено | DRF-2229 — код закрыт; стенд — UNKNOWN |
| R-12 | `PLAN_CADENCE` в реестре правил планирования | нет; в KB `planning-rules-registry.yaml` 0 KNOWN, `REPETITION` = INTENTIONALLY_UNSUPPORTED | поправка KB (волна DRF-2260…2263) |
| R-13 | «Забудь всё» стирает план и версии | так: см. «Приватность» п. 2 | нет (после миграции — ссылки `superseded_by` / `supersedes_action_id`) |
| R-14 | Экспорт отдаёт план и версии | нет: `cat:users/personal_data_api.py:266-295` | **DRF-2214** (экспорт) |
| R-15 | Decision Engine берёт следующее действие плана только из актуальных версий | плана не читает: `bot:apps/orchestrator/decision_policy.py` — 0 вхождений «plan» | путь [[Ayla Decision Policy Contract]] |
| R-16 | События `plan.*` | нет | KB-E (DRF-2260…2263), затем runtime |
| R-17 | Флаг | `PLAN_LITE_ENABLED` по умолчанию `false` в обоих репозиториях | нет (решение о включении — вне контракта) |
| R-18 | Ведро `per_day` / `per_week` — по локальной дате человека (цепочка AYLA-DEC-0095, [[Ayla Diary and Water Contract]] I-3) | по `timezone.localdate()` сервера (`cat:wellness/plan_lite.py:322`); `plan_facts` — `TruncDate` в зоне сервера (`cat:nutrition/services/plan_facts.py:31-51`) | лист **DRF-2269** (разные пояса суток — решается контрактом DY-1) |
| R-19 | Время действия — слот дня + дни недели (I-21, CD §72 п.18) | времени у действия нет (`cat:wellness/models.py:390-452`) | миграция `PlanAction` в серии G-1 / P-1 / P-2 (Миграции п. 11); лист — UNKNOWN |
| R-20 | Специалист предлагает, клиент подтверждает кнопкой (I-20, CD §72 п.20) | пути записи специалистом нет | после открытого вопроса 14; лист — UNKNOWN |

## Не входит (Non-goals)

- Вес, `ProgressObservation`, `DesiredOutcome`, `PlanOutcomeLink`, процент достижения цели (AYLA-DEC-0088, AYLA-DEC-0094).
- Plan Composer и любой вывод действий или частот из поведения; сложный NBA, скоринг, обучение (AYLA-DEC-0093, AYLA-DEC-0097).
- Курсы процедур, интервалы и совместимость услуг: `REPETITION`, `MIN_INTERVAL`, `MAX_INTERVAL` не меняются (AYLA-DEC-0093).
- Шаблон «без цели» (вариант (б) P-1 отвергнут).
- Состояние плана «пауза» — до пилота нет (CD §72 п.26).
- Напоминания; точный час действия — после пилота (CD §72 п.18).
- Proactive-возврат к плану (A4, DRF-2126) — предмет Consent Registry и Decision Policy.
- Семантика и жизненный цикл цели — [[Ayla Goal and Desired Outcome Contract]].
- Дневник, вода, день дневника — [[Ayla Diary and Water Contract]].

## Открытые вопросы

1. Закрыт решением владельца CD §72 п.18 → раздел «Сущности» (PlanAction, время действия), I-21, R-19, «Влияние на миграции» п. 11.
2. Закрыт решением владельца CD §72 п.19 → раздел «Сущности» (категория `book_service`), I-8, R-4, «Влияние на миграции» п. 12.
3. Закрыт решением владельца CD §72 п.26 → раздел «Сущности» (PersonalPlan), I-22.
4. Закрыт решением владельца CD §72 п.20 → раздел «Команды» (`ProposeSpecialistChange`, `ConfirmSpecialistChange`), I-20, R-20; остаток — открытый вопрос 14.
5. **`goal_changed` и `plan_rebuilt`.**
   - Действия нового плана при `ConfirmSupersession` лежат в другом `plan_id`. Что они «заменяют»?
   - Варианты:
     - (а) `supersedes_action_id` указывает на версию того же `action_type` старого плана, а действия без предшественника — `initial`;
     - (б) все действия нового плана — `initial`, связь только через `superseded_by` плана.
   - Когда применяется `plan_rebuilt` — решениями не определено.
6. **`closed_at` у `superseded` плана** — отдельное поле `superseded_at` или то же `closed_at`?
7. **`AddAction` и `changed_by = system`.**
   - Разрешено ли добавлять действие в активный план (P-2 допускает `user_selected`, прямого слова нет)?
   - Когда допустим `changed_by = system`? Контракт предлагает: только для технических версий без смены содержания (например, backfill миграции), поскольку система не меняет обязательства (инв. ТЗ 7–8). Нужно подтверждение.
8. **`log_food` без согласия дневника.** Норма ли для всех каналов снимать это действие из предложения (как Mini App), или действие допустимо, а факты просто не появятся?
9. **Backfill существующих строк.** Планы, подтверждённые с правкой, записаны как `template:…:vN`. Истинный провенанс их действий невосстановим.
   - Писать `template` — ложь для правленых строк; других значений закрытый список не даёт.
   - Нужно решение: допустимый маркер или принятие предела с явной записью. Число таких строк на стенде — UNKNOWN (флаг выключен; на стенде не измерялось).
10. **Пометка «план собран под прошлую цель»** (AYLA-DEC-0090, «Оставить»): вычисляется из `goal` ≠ активной цели или хранится отдельным признаком? Поле не вводится до решения.
11. *Закрыт по рецензии DRF-2261:* пояс ведра задан нормой («Производные»: локальная дата человека по цепочке AYLA-DEC-0095); текущий серверный пояс — расхождение «Граница API» R-18 (DRF-2269).
12. **Условие `status = removed ⇒ reason_code = action_removed`** выглядит следствием AYLA-DEC-0092, но прямо в решении не записано. В схему не введено. Свидетель текущего поведения — фикстура `valid_removed-initial-currently-allowed-oq12.json` (версия `removed` с `reason_code = initial` сейчас проходит схему). После решения — правило `if status = removed then reason_code = action_removed`, фикстура переходит в `invalid_*`.
13. **Кто пишет `source = ayla_proposal_accepted`.** Значение есть в закрытом списке `source` (AYLA-DEC-0092), но ни одна команда этого контракта его не пишет: `ConfirmProposal` пишет `template` / `user_edited`, `ReviseAction` — `user_edited`. Не определены: какая команда пишет `ayla_proposal_accepted` (принятие предложения Ayla из [[Ayla Dietitian Capability Contract]] / [[Ayla Decision Policy Contract]]), какой `reason_code` у такой версии (подходящего в закрытом списке нет) и формат `source_ref` предложения. Команда не вводится до решения.
14. **Права специалиста на предложение изменения плана** (остаток вопроса 4 после CD §72 п.20). Решено только «специалист предлагает, клиент подтверждает кнопкой». Не определены:
   - какой специалист вправе предлагать изменение плана клиента (связь «специалист — клиент») и через какую поверхность;
   - видит ли специалист план клиента и на каком основании согласия;
   - формат `source_ref` у версии `source = specialist`;
   - где лежит предложение специалиста до подтверждения клиентом и что с ним при отказе или без ответа.
   - Смежно — [[Ayla Dietitian Capability Contract]] (предложение Диетолога требует подтверждения, ТЗ E2E 18).

## Критерии приёмки

| # | Критерий (проверяемый) | E2E ТЗ §10 |
|---|---|---|
| A-1 | Без активной цели человек собирает план конструктором: 201, `source = manual`, `goal = null`, у всех действий `source = user_selected`. `GET proposal` без цели → 404 `no_active_goal` | №5, №1 |
| A-2 | `GET proposal` не создаёт строк: число `PersonalPlan` и `PlanAction` до и после одинаково | №6 |
| A-3 | Текст «да», «ок», «подтверждаю» не вызывает создания плана; тап `cb:plan:accept:<v>` создаёт план с версиями `reason_code = initial` | №7 |
| A-4 | Изменённая до подтверждения строка сохранена как `source = user_edited`, не `template` | №7 |
| A-5 | Смена цели при активном плане: план остаётся `active`, пока новый не подтверждён кнопкой. «Оставить» — `active` с пометкой. «Обновить» + подтверждение — старый `superseded` с `superseded_by`, новый `active`, одна транзакция | №8 |
| A-6 | Частоты и тексты «почему» предложения совпадают с активной версией `PlanTemplate`; при отсутствии шаблона — 404 `no_template`, не пустой и не выдуманный план | №9 |
| A-7 | Подтверждённая запись с визитом в будущем не увеличивает `done_count` `book_service` | №10 |
| A-8 | Визит, переведённый сервером в `completed`, увеличивает `done_count` в ведре своей **даты визита** | №11 |
| A-9 | `cancelled` и `no_show` (в том числе исправление `completed → no_show`) не входят в `done_count` | №12 |
| A-10 | `within_target_count` не учитывает незавершённый день | №13 |
| A-11 | Правка действия создаёт новую версию; прежняя — `superseded`, содержимое неизменно; в `plan_lite` одно действие этого типа | — (ТЗ §10 Unit: plan recalculation) |
| A-12 | Удаление действия — версия `removed`; с этого момента действие не входит в «M» и не выбирается Decision Engine | №22 |
| A-13 | Попытка записать вторую `active`-версию одного логического действия отклоняется БД | — (ТЗ §10 Contract: provenance) |
| A-14 | «Забудь всё» (все три пути) оставляет 0 строк `PersonalPlan` и `PlanAction` субъекта во всех состояниях, включая `superseded` и `removed` | №21 |
| A-15 | Экспорт содержит план во всех состояниях и все версии действий с провенансом | №21 |
| A-16 | Все валидные фикстуры `fixtures/plan-action/valid_*.json` проходят схему, каждая `invalid_*.json` отклоняется ровно по названному правилу; minor `contract_version` "1.1" проходит (`valid_minor-1-1.json`), неизвестная major "2.0" отклоняется (`invalid_major-2-0.json`) | — (ТЗ §10 Contract: schema/version compatibility, unknown major rejection, reason codes) |
| A-17 | Decision Engine при наличии активного плана возвращает `ACT` со ссылкой на `action_id` актуальной версии либо `NO_ACTION` с причиной, никогда не версию `superseded` или `removed` | №22, №23 |
| A-18 | Предложение специалиста не меняет план: число версий и актуальная версия до кнопки клиента те же. После кнопки — новая версия `source = specialist`, `changed_by = specialist`, `reason_code = specialist_change`, прежняя — `superseded` (CD §72 п.20) | №18 (по смыслу) |

## Влияние на миграции (Migration impact)

1. **Каталог, `PersonalPlan`** (аддитивно):
   - значение `superseded` в `Status` (`max_length = 16` достаточно);
   - поле `superseded_by` — nullable-ссылка на `PersonalPlan`.
   - Ограничение `personalplan_one_active_per_user` сохраняется. Порядок в транзакции замены: старый → `superseded`, затем новый `active`.
2. **Каталог, `PlanAction`** (аддитивно):
   - новые поля: `status`, `source`, `source_ref`, `source_version`, `changed_by`, `changed_at`, `reason_code`, `supersedes_action_id` — nullable-ссылка на `PlanAction`;
   - сторож БД: частичная уникальность (`plan`, `action_type`) при `status = active`. Опирается на правило писателя «один тип на план», `cat:wellness/plan_lite.py:128-129`;
   - **предложение (не из AYLA-DEC-0092):** сторож БД — уникальность `supersedes_action_id` при непустом значении, у версии не более одного преемника. Бриф P-2 даёт сторожа только для «не больше одной актуальной версии на действие»; этот сторож требует подтверждения;
   - `CHECK`: `reason_code = initial` ⇔ `supersedes_action_id IS NULL`.
3. **Backfill** существующих строк: `status = active` у действий активных планов, `reason_code = initial`, `changed_by = user`, `changed_at = created_at`. Значение `source` — открытый вопрос 9.
4. **Стирание:**
   - `users/forget_all_catalog.py` и `users/deletion_executor.py` — снять самоссылки до удаления строк (или `SET_NULL`);
   - сторожа стирания дополнить строками со ссылками.
5. **Писатель и API:**
   - `create_plan` принимает провенанс строк;
   - снимается 404 для `manual` без цели;
   - новые ручки правки и удаления действия;
   - `plan_lite_payload` отдаёт только актуальные версии.
6. **Бот и Mini App:**
   - передавать факт правки строк;
   - «Изменить план» — через версии, не закрытие;
   - вопрос при смене цели (чат и экран цели).
7. **`fact_providers`** — по DRF-2216.
8. **KB:**
   - `planning-rules-registry.yaml` (`PLAN_CADENCE`, перечень 13 → 14, `subject_kind: plan_template`) и `scripts/validate_planning_rules.py` — AYLA-DEC-0093;
   - [[Ayla Domain Event Registry]] (`plan.*`);
   - [[Data Inventory Matrix]];
   - [[AMD-001 C5 Pilot Personal Context Export-Forget Contract]];
   - [[Ayla Glossary]] (Plan Lite, Plan Action — актуальная версия / история, Plan Cadence).
9. **Сид шаблонов** — миграция `wellness/0007_seed_plan_templates_if_empty` (слито #533, DRF-2229); на стенде — после выкладки.
10. **Порядок.** Все изменения `PersonalPlan` и `PlanAction` (G-1, P-1, P-2) — одним исполнителем, иначе три миграции одной модели разойдутся (бриф, Итог 6).
11. **Время действия** (CD §72 п.18). Форма «слот дня (`утро` / `день` / `вечер`) + дни недели» — миграция `PlanAction` и реализация в той же серии (п. 10), затем minor-версия `plan-action.schema.json`. Поля точного часа нет. Значение у существующих строк — не выдумывается (время не задано).
12. **Категория `book_service` плана без цели** (CD §72 п.19). Поле-ссылка на категорию каталога (имя `service_category_ref` — предложение) — миграция `PlanAction` в той же серии, затем minor-версия схемы; `fact_providers` считают бронь плана без цели только по этой категории (R-4).

## Трассировка

**DEC → раздел**

| DEC | Разделы |
|---|---|
| AYLA-DEC-0087 | Назначение; Согласие п. 4; Миграции п. 8 |
| AYLA-DEC-0088 | Назначение; Сущности; Входы и выходы; Инварианты I-1, I-2, I-18; Согласие; Безопасность; Non-goals |
| AYLA-DEC-0089 | Владение; Источник истины п. 3; Сущности (PlanTemplate); Команды; I-4, I-15 |
| AYLA-DEC-0090 | Сущности (PersonalPlan); Состояния; Команды (`ResolveGoalChange`, `ConfirmSupersession`); Входы (`goal.superseded`); События (`plan.superseded`); I-7; R-8; A-5 |
| AYLA-DEC-0091; решение владельца 21.09 (CD §71 п.3) | Сущности (категория `book_service`, PlanProposal); Команды (`ComposeManual`); I-8; R-3, R-4; Открытый вопрос 2; A-1 |
| AYLA-DEC-0092 | Сущности (PlanAction); Состояния версии; Команды; События (`plan.action.revised`); I-10…I-13; R-5…R-7; схема; A-4, A-11…A-13, A-16 |
| AYLA-DEC-0093 | Владение; Источник истины п. 3; I-14, I-15; Безопасность п. 2; R-12; Миграции п. 8 |
| AYLA-DEC-0094 | Источник истины п. 4; Non-goals |
| AYLA-DEC-0095 | Сущности (Производные: пояс ведра); I-16; R-10, R-18; A-10 |
| AYLA-DEC-0096 | Безопасность п. 1 |
| AYLA-DEC-0097 | Входы и выходы; I-12; R-15; A-12, A-17 |
| AYLA-DEC-0098 | Безопасность п. 5 |
| AYLA-DEC-0101 | Приватность п. 2–3; I-19; R-13, R-14; A-14, A-15 |
| Решение владельца 21.09, журнал главного окна CD §72 п.18 (вне git) — время «утро / день / вечер» + дни недели | Сущности (PlanAction, время действия); Входы и выходы (для Decision Engine); I-21; R-19; Не входит; Миграции п. 11; Открытый вопрос 1 (закрыт) |
| CD §72 п.19 — категория из списка каталога | Сущности (категория `book_service`); I-8; R-4; Миграции п. 12; Открытый вопрос 2 (закрыт) |
| CD §72 п.20 — специалист предлагает, клиент подтверждает | Команды (`ProposeSpecialistChange`, `ConfirmSpecialistChange`); I-20; R-20; A-18; Открытые вопросы 4 (закрыт), 14 |
| CD §72 п.26 — паузы плана до пилота нет | Сущности (PersonalPlan); I-22; Не входит; Открытый вопрос 3 (закрыт) |

**Инвариант ТЗ §7 → раздел**

| Инв. | Разделы |
|---|---|
| 3 | I-2 |
| 4 | I-14, I-15 |
| 5, 6 | I-17 |
| 7 | I-3, I-7; Команды |
| 8 | I-3, I-7; R-1 |
| 9 | I-4, I-7; R-2; A-2 |
| 10 | I-5, I-20; Команды; R-1; A-3, A-18 |
| 11 | I-9; R-9; A-7 |
| 12 | I-9; R-9; A-8 |
| 13 | I-9; R-9; A-9 |
| 14, 15 | I-16; R-10; A-10 |
| 21 | I-19; Приватность; A-14, A-15 |
| 22 | Безопасность п. 1 |
| 23 | Безопасность п. 4 |
| 24 | A-17 |
| 25 | I-10, I-13; Наблюдаемость п. 2 |

## Change Log

### v0.1 — 2026-09-21 — первичная редакция (DRF-2261)

- Первая редакция контракта Plan Lite по AYLA-DEC-0088…0093 и AYLA-DEC-0097.
- Сверено с кодом `cat@4dbff523` и `bot@0e2c0100`.
- Машиночитаемое приложение `plan-action.schema.json` (`contract_version` "1.0") с фикстурами `valid_*` / `invalid_*`.

### v0.1 — правки по рецензии (DRF-2261)

- Пояс ведра `per_day` / `per_week` — норма «локальная дата человека по цепочке AYLA-DEC-0095»; серверный пояс — расхождение R-18 (DRF-2269); открытый вопрос 11 закрыт.
- Входы: `goal.superseded` — триггер `ResolveGoalChange`; `goal.state_changed` не потребляется до GOAL OQ-9.
- `ConfirmSupersession`: `reason_code` — по открытому вопросу 5 (снято `goal_changed`).
- Новый открытый вопрос 13: какая команда пишет `ayla_proposal_accepted` и с каким `reason_code`.
- Сторож уникальности `supersedes_action_id` помечен как предложение (не из AYLA-DEC-0092).
- Правило `source_ref` / `source_version` у `user_edited`; фикстуры выровнены.
- PlanProposal и I-8: ссылка на решение владельца 21.09 (CD §71 п.3).
- `contract_version`: шаблон `^1\.[0-9]+$`; фикстуры `valid_minor-1-1`, `invalid_major-2-0`, свидетель OQ-12 `valid_removed-initial-currently-allowed-oq12`.
- Runtime пересверен на `cat@cca8a914` / `bot@808ca79d`: R-11 и «Наблюдаемость» п. 5 — шаблоны §51 кладёт миграция (слито #533, DRF-2229). Прочие строки «Граница API» не менялись: файлы плана (`wellness/plan_lite*.py`, `fact_providers.py`, `models.py`, `nutrition/services/plan_facts.py`; бот `plan_lite_card.py`, `PlanLiteScreen.tsx`, `views_plan_lite.py`) после прежних снимков не изменены. Шапка: обозначения SHA.

### v0.1 — решения владельца CD §72 п.18, 19, 20, 26 вписаны (DRF-2261)

- Решения владельца 21.09, журнал главного окна CD §72 (вне git), «все по рекомендациям».
- п.18: время действия — слот дня «утро / день / вечер» + дни недели, точный час — после пилота (Сущности, I-21, R-19, Миграции п. 11). В схему поле не введено. Открытый вопрос 1 закрыт.
- п.19: план без цели — категория услуг из списка каталога, выбранная человеком; ссылка на категорию каталога, имя `service_category_ref` — предложение (Сущности, I-8, R-4, Миграции п. 12). Открытый вопрос 2 закрыт.
- п.20: специалист предлагает, клиент подтверждает кнопкой — команды `ProposeSpecialistChange` / `ConfirmSpecialistChange`, I-20, R-20, A-18. Открытый вопрос 4 закрыт; права специалиста — новый открытый вопрос 14.
- п.26: паузы плана до пилота нет (Сущности, I-22, Не входит). Открытый вопрос 3 закрыт.
