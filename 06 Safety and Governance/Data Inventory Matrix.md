---
node_id: ayla.governance.data-inventory-matrix
title: Data Inventory Matrix
type: data-inventory-matrix
status: draft
version: "1.1"
owner: Safety and Governance Domain
knowledge_area:
  - safety-governance
system_owner:
  - ayla-knowledge
source_repository: ayla-knowledge
created: 2026-07-24
updated: 2026-09-21
source_kind: canonical
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: medium
ai_indexing: metadata-only
export_policy: sanitized
review_cycle: quarterly
reviewers: []
tags: [data-governance, memory-ownership, data-inventory, privacy]
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Glossary]]"
  - "[[OWNER_DECISION_REGISTER]]"
related:
  - "[[AMD-001 C5 Pilot Personal Context Export-Forget Contract]]"
  - "[[Ayla Memory Domain Contract]]"
  - "[[Consent Scope Registry]]"
  - "[[Ayla Domain Event Registry]]"
---

# Data Inventory Matrix

## Purpose

Этот документ фиксирует классы данных в системе Ayla, их владельцев, источники истины и правила обработки. Цель — устранить противоречия во владении памятью и обеспечить соответствие privacy requirements.

## Matrix

| Class of Data | Data Subject | Normative Domain / System Owner | Physical Custodian | Source of Truth | Permitted Consumers | Write Authority | Consent / Purpose | Retention & Deletion Orchestrator | Temporary Projections Rules |
|---------------|--------------|--------------------------------|--------------------|-----------------|---------------------|-----------------|-------------------|-----------------------------------|----------------------------|
| Account / Profile | User | User Context Domain (`ayla-user-context`) | W2 Profile Service | W2 Profile Service | W3 Memory, Wellness, Consent, Notification | W2 only | Account creation purpose | W2 on user request or account closure | Allowed for UI rendering; no persistent storage outside W2 |
| Operational Preferences | User | User Context Domain | W2 Preferences Service | W2 Preferences Service | W3 Memory, Wellness, Notification (read-only) | W2 only | Service operation purpose | W2 on preference change or account closure | Allowed for session caching with TTL; must refresh from source on invalidation |
| Consent Records | User | Consent Domain | Consent Service | Consent Service | All domains (read-only for gating via authoritative cache with TTL) | Consent Service only | Explicit consent capture | Consent Domain per legal requirements; orchestrates deletion requests | Not allowed as independent source; authoritative cache with TTL and invalidation required |
| Semantic Memory (MemoryEntry) | User | W3 Memory & Identity Domain | W3 Memory Service | W3 Memory Service (after gate) | Approved consumers via purpose-limited API | W3 only (via proposal/consent/purpose gate) | Requires explicit consent + purpose approval | W3 privacy flow on user request | Not allowed; memory is persistent, not projected |
| Raw Wellness History | User | Wellness Domain | Wellness Service | Wellness Service | W3 Memory (for derivation), Dashboards (read-only) | Wellness Service only | Wellness tracking purpose | Wellness Domain per retention policy | Allowed for dashboards, summaries, API views; marked as derived |
| Wellness-Derived Memory | User | W3 Memory & Identity Domain | W3 Memory Service | W3 Memory Service (after memory gate) | Approved consumers via purpose-limited API | W3 only (via memory gate) | Requires consent + memory proposal approval | W3 privacy flow on user request | Not allowed; becomes semantic memory after gate |
| Purpose-Limited Projections | User | N/A — inherits normative ownership from source data class | Consumer-specific cache | Source domain (live) | Specific consumer only | No write authority; read-through only | Inherited from source + consumer purpose | Session lifetime or consumer-defined (must not exceed source retention) | Must be marked as temporary; cannot be persisted as memory |
| Notification Preferences | User | Notification Preferences Domain | Notification Service | Notification Service | Communication systems (read-only) | Notification Service only | Communication consent | Notification Domain on preference change | Allowed for delivery queue caching |
| Marketing Opt-Out | User | Consent Domain | Consent Service | Consent Service | Marketing systems (read-only for gating) | Consent Service only | Marketing consent (or lack thereof) | Consent Domain per legal requirements | Not allowed; must check live or via authoritative cache |
| Customer Service Preferences | User | User Context Domain | W2 Preferences Service | W2 Preferences Service | Substitute (booking-specific projection only) | W2 only | Booking purpose | W2 per booking lifecycle | Allowed only as booking-specific purpose-limited projection; never as MemoryEntry copy |
| Goal (`goals.ClientGoal`: дословный `goal_text`, `target_date`) | User | Goal Domain (W2, каталог `goals`) | W2 Postgres | W2 `goals.ClientGoal` — единственный живой носитель цели и её срока (AYLA-DEC-0094) | Plan Domain; Recommendation (W2, W3 по API — чтение); показ в Mini App и боте | W2 only; lifecycle цели меняет только человек (AYLA-DEC-0090; UI — DRF-2228) | Цель необязательна (AYLA-DEC-0087); назначение — персонализация плана и рекомендаций; scope согласия за классом не закреплён — [Q1] | «Забудь всё»: DELETE. Текущее — соответствует, W2 `erase_remembered_catalog` в транзакции C5.2 [N1]. Экспорт: целевое — несёт (T-6); текущее — не несёт [N2]; лист DRF-2214 (PR-2). Удаление аккаунта (D3) — DELETE | Снимок `PersonalPlan.goal_key` — ключ, не текст; W3 `Recommendation.facts` может цитировать подписи цели (см. строку Recommendation record) |
| Goal questionnaire (`goals.GoalAnketaRun` / `goals.GoalAnketaAnswer`: дословный `answer_text`) | User | Goal Domain (W2) | W2 Postgres | W2 `goals.GoalAnketaAnswer` — ответы хранятся дословно, не нормализуются | Goal Domain (выбор следующего вопроса анкеты) | W2 only | Как у Goal | «Забудь всё»: DELETE прогонов, ответы уходят каскадом. Текущее — соответствует [N1]. Экспорт: целевое — несёт; текущее — не несёт [N2]; лист DRF-2214 (PR-2) | Следующий вопрос анкеты — проекция на запрос, в БД не лежит |
| Personal Plan (`wellness.PersonalPlan`; обездвиженные `DesiredOutcome`, `PlanOutcomeLink`, `ProgressObservation` — AYLA-DEC-0094) | User | Plan Domain (W2, каталог `wellness`) | W2 Postgres | W2 `wellness.PersonalPlan` (0..1 ACTIVE на человека) | Adherence «N из M»; Decision Engine (AYLA-DEC-0097); показ | W2 only; план меняет только человек; статус `superseded` при смене цели — AYLA-DEC-0090 (целевое) | Plan Lite без наблюдений тела, нового scope согласия нет (AYLA-DEC-0088) | «Забудь всё»: DELETE плана вместе со связями, исходами и наблюдениями. Текущее — соответствует [N1]. Экспорт: целевое — несёт; текущее — не несёт [N2]; лист DRF-2214 (PR-2) | Adherence «N из M» — производная на запрос, не хранимый факт |
| Plan Action versions (`wellness.PlanAction`; неизменяемые версии с провенансом — AYLA-DEC-0092) | User | Plan Domain (W2) | W2 Postgres | Целевое: цепочка неизменяемых версий (источник; ссылка и версия источника; кто изменил; когда; причина из закрытого списка; ссылка на заменённое действие), в расчётах — одна актуальная версия. Текущее: одна строка без полей провенанса и версии [N3] | Adherence, Decision Engine, показ — только актуальная версия (AYLA-DEC-0092) | W2 only; правка — новая версия; удаление действия — версия со статусом «удалено» | Как у Personal Plan | «Забудь всё»: DELETE всех версий, включая версии «удалено»: действия входят в план, который стирается целиком (AYLA-DEC-0101); статус «удалено» — механика правки, а не исход «забудь всё». Текущее — все строки стираются [N1]. Экспорт: целевое — несёт (форма — [Q4]); текущее — не несёт [N2]; листы — серия G-1 / P-1 / P-2 (Ayla Personal Plan Contract), DRF-2214 (PR-2) | Старые и удалённые версии — история; в текущий расчёт не попадают |
| Diary Day (день дневника: `closed` / `corrected`, пояс и источник пояса — AYLA-DEC-0095) | User | Diary Domain (W2, каталог `nutrition`) | Целевое: W2 Postgres, новая сущность. Текущее: не хранится — вычисляется на запрос [N4] | Целевое: W2 | Оценка дня, «в ориентире» у плана, серии дней — только по завершённым дням (AYLA-DEC-0095) | W2 only; завершение — кнопкой «Завершить день» или автозакрытием предыдущего дня в 04:00 по поясу человека | Как у Food Diary | «Забудь всё»: целевое — DELETE в той же транзакции, что дневник (выведено из AYLA-DEC-0101 — [Q5]); текущее — хранить нечего. Экспорт: целевое — несёт; текущее — нет | До завершения дня — только текущие числа, без оценки «уложился / не уложился» |
| Food Diary (`nutrition.FoodLog`; `nutrition.DeletedFoodLog` — снимок на окно восстановления; `nutrition.SavedMeal` — включая мягко удалённые) | User | Diary Domain (W2, каталог `nutrition`) | W2 Postgres | W2 `nutrition.FoodLog`; избранное — W2 `nutrition.SavedMeal` | Сводка дня, отчёты Диетолога, Decision Engine, показ; во внешнюю LLM — без флагов здоровья и без признака их наличия; для человека с любым флагом здоровья внешний LLM-комментарий не вызывается — локальный нейтральный текст (AYLA-DEC-0098) | W2 only; исправлять и удалять свои записи человек может всегда (AYLA-DEC-0095) | Runtime-тип согласия `food_diary_processing`; в Consent Scope Registry v1.5 §5.10 — фактом, scope нет (`CSR-OD-13`) | «Забудь всё»: DELETE всех трёх, в одной транзакции с целями, планом и профилем питания (AYLA-DEC-0101). Текущее — соответствует [N1]. Экспорт: целевое — несёт дневник (AYLA-DEC-0101); текущее — не несёт [N2]; лист DRF-2214 (PR-2). Удаление аккаунта (D3) — DELETE | Сводки и отчёты — производные; кэш LLM-комментария сбрасывается при правке и удалении еды (DRF-2227) |
| Food scanner photo (`nutrition.FoodScan` + файл `image` в объектном хранилище) | User | Diary Domain (W2, каталог `nutrition`) | W2 Postgres (строка) + объектное хранилище (файл) | W2 `nutrition.FoodScan` | Сканер (распознавание, повтор без повторной загрузки фото); учёт стоимости провайдера | W2 only | Как у Food Diary; внешний провайдер распознавания — вне этой матрицы | «Забудь всё»: DELETE строки и файла; файл снимается раньше строки внутри транзакции, неснятый файл — `IncompleteErasure` и откат. Текущее — соответствует [N1]. Срок фото без «забудь всё» — 30 суток, задача очистки [N5]. Экспорт: целевое — несёт (включать ли сам файл — [Q6]); текущее — не несёт [N2]. Стоимость провайдера уходит вместе со строкой — [Q7] | Результат распознавания лежит в строке скана; копии фото вне объектного хранилища — не измерены |
| Water (`nutrition.WaterEntry`; `nutrition.WaterLog` — legacy) | User | Diary Domain (W2, каталог `nutrition`) | W2 Postgres | Целевое: `WaterEntry` — единственный источник (DRF-2217). Текущее: сводка дня читает `WaterLog`, люди пишут в `WaterEntry` (бриф, Приложение A T-1) | Сводка дня, действие плана `log_water`, показ | W2 only; вода хранится в миллилитрах (AYLA-DEC-0099) | Как у Food Diary | «Забудь всё»: DELETE обеих таблиц. Текущее — соответствует [N1]. Мягко удалённые `WaterEntry` без «забудь всё» дочищаются через 90 суток [N5]. Экспорт: целевое — несёт (AYLA-DEC-0101); текущее — не несёт [N2]. Старые адреса `WaterLog` — Sunset 31.10.2026 (CD §72 п.14); runtime — не измерено | «N стаканов» — пересчёт миллилитров при показе, не хранится |
| Nutrition Profile (`nutrition.NutritionProfile`: `weight_kg`, `height_cm`, `age`, `health_flags`, ориентиры и их входы) | User | Nutrition Domain (W2, каталог `nutrition`) | W2 Postgres | W2 `nutrition.NutritionProfile`; возраст — целевое: производный от даты рождения, `age` снимается (AYLA-DEC-0100) | Расчёт ориентира, сводки, Диетолог; `health_flags` во внешнюю LLM не передаются, при любом флаге внешний LLM-комментарий не вызывается (AYLA-DEC-0098) | W2 only, через канонического писателя профиля; подстановки не заданных человеком параметров запрещены (DRF-2219) | Runtime-тип согласия `personal_calculation`; в Consent Scope Registry v1.5 §5.10 — фактом, scope нет (`CSR-OD-16`); отзыв стирает входы расчёта | «Забудь всё»: DELETE — `erase_personal_calculation_inputs`, затем строка. Текущее — соответствует [N1]. Экспорт: целевое — несёт; текущее — не несёт [N2]. `health_flags.allergies` / `allergies_vague` принимаются без отдельного согласия и без возрастного статуса [N6] — закрыть или перевести на периметр строки Allergy (DRF-2132) | Ориентир — производная с происхождением; суточный кэш ответа профиля `ProfileIdempotencyKey` стирается тем же шагом [N1] |
| Recommendation record (W3 `recommendation.Recommendation`: `what`, `subline`, `why`, `facts`, `alternatives` — дословно показанное, включая подписи цели и ответов) | User | Recommendation Domain (бот W3) | W3 Postgres | W3 `recommendation.Recommendation` — неизменяемая запись показа (решение B13) | Attribution / аудит (связь с бронью), карточка C04 | W3 only; запись неизменяема, кроме реакции и брони | Рекомендации услуг — только по инициативе человека (требование сохраняется, AYLA-DEC-0087) | Удаление персональных данных (C5, `delete_personal_data`): ANONYMISE — строка остаётся надгробием, слова обнуляются [N7]. «Забудь всё» (чат и Mini App): целевое — ANONYMISE тем же глаголом (бриф T-6); текущее — не трогает [N7]; лист DRF-2214. Экспорт: текущее — состав не объявлен в `export_coverage` [N7]; целевое — объявить (DRF-2214); выдача значений — [Q8] | В память не проецируется |
| Decision Engine journal (исход ACT / CLARIFY / NO_ACTION / BLOCKED / HANDOFF с причиной, ссылками на факты, происхождением, заблокированными функциями, временем расчёта и версией политики — AYLA-DEC-0097) | User | Decision Policy (Ayla Decision Policy Contract) | Владение: открытый вопрос [Q9] | Открытый вопрос [Q9] | Наблюдаемость и разбор исходов | Только Decision Engine | Не определено | «Забудь всё» и экспорт — открытый вопрос [Q9]. Текущее — хранилища нет ни в одном репозитории [N8] | По решению исход несёт ссылки на факты; хранит ли журнал сами значения — не определено [Q9] |
| Allergy (`MemoryEntry` `kind=allergy`, red — AYLA-DEC-0100) | User | W3 Memory & Identity Domain | W3 Memory Service, Postgres `identity_memoryentry` (red) | W3 Memory Service — после отдельного явного согласия на запись и статуса `adult_eligibility_asserted` | Для обработки — только рекомендации (фильтр состава) и сканер (предупреждение); кроме них — доступ субъекта к своей записи (показ, экспорт, удаление) с журналом `memory.allergy.accessed`; в текст для модели — никогда; форма результата — `allergy-filter-result.schema.json` | W3 only: кандидат → показ распознанной формулировки → отдельное явное согласие → дата рождения → запись; без даты рождения или младше 18 запись не создаётся | Отдельное явное согласие на запись; scope `allergy_safety_filter` (Consent Scope Registry v1.5); без TTL | «Забудь аллергии» и «Забудь всё»: DELETE (надгробие + строка `RedZoneAccessLog`). Текущее: свип всех зон при «забудь всё» есть [N9]; записи не создаются — фраза отбрасывается [N9]; лист DRF-2132. Экспорт: целевое — отдаёт (AYLA-DEC-0100); текущее — red объявлен невыгружаемым [N9] → расхождение. Каждое чтение и каждый отказ — `memory.allergy.accessed` / `memory.allergy.access_denied`, без содержания | В промпт не проецируется; результат фильтра не содержит формулировки аллергии — только opaque-ссылки |
| Date of birth (единственный источник возраста — AYLA-DEC-0100) | User | Не назван — `CSR-OD-11`; физическое место — профиль W2 (AYLA-DEC-0100) | Целевое: одно поле профиля каталога W2. Текущее: в каталоге поля нет; в W3 есть отдельный носитель полной даты `identity.UserPreferences.birthday_date` [N10] | Целевое: W2 профиль | Наружу — только возрастной статус и возраст в полных годах (`age-status.schema.json`); полная дата не появляется в ответах API, логах, событиях и промптах | W2 only; человек называет дату один раз | Самодекларация, не юридическая проверка возраста | «Забудь всё»: целевое — DELETE, после чего статус `age_unknown` и аллергии недоступны до нового ответа (бриф M-1). Экспорт: целевое — несёт. Текущее (W3 `birthday_date`): «забудь всё» — RETAIN, текст команды обещает, что дата рождения останется; удаление C5 — DELETE; экспорт — несёт [N10] → конфликт двух носителей и текста команды с решением, [Q2] | Статус и возраст в годах — производные на запрос; `NutritionProfile.age` — второй источник возраста, снимается (AYLA-DEC-0100) |
| Glass size (размер стакана — AYLA-DEC-0099) | User | Diary Domain (вода) | Целевое: не определено [Q3]. Текущее: пользовательского значения нет — константа 250 мл в W3 [N11] | Не определено [Q3] | Интерфейс записи воды во всех каналах | Человек | Удобство интерфейса, не норма; нормой нигде не называется | «Забудь всё» и экспорт — открытый вопрос [Q3] | Новый размер применяется только к будущим записям; прошлые записи воды не пересчитываются |
| Operator task transcript snapshot (`handoff.AdminTask.transcript_snapshot` — снимок переписки в задаче оператора) | User | Handoff (бот W3) | W3 Postgres | W3 `handoff.AdminTask` | Оператор задачи | W3 only; снимок пишется при передаче оператору | Обработка обращения | «Забудь всё»: снимок переписки стирается, в том числе при открытой задаче (CD §72 п.2). Исход по решению; runtime — не измерено [N12] | Снимок — копия переписки на момент передачи |
| In-app notification history (`notifications.Notification`) | User | Notification (W2, каталог `notifications`) | W2 Postgres | W2 `notifications.Notification` | Показ истории в приложении | W2 only | Как у Notification Preferences | «Забудь всё»: история — DELETE; настройки уведомлений — RETAIN (CD §72 п.3). Исход по решению; runtime — не измерено [N12] | — |
| Favourite specialists (`users.FavoriteSpecialist`) | User | User Context Domain (W2, каталог `users`) | W2 Postgres | W2 `users.FavoriteSpecialist` | Главный экран и список избранного | W2 only; добавляет и снимает человек | Service operation purpose | «Забудь всё»: RETAIN; в текст команды дописывается, что избранное сохраняется (CD §72 п.3). Исход по решению; runtime — не измерено [N12] | — |
| In-app AI chat (`ai.Conversation` / `ai.Message`) | User | AI chat (W2, каталог `ai`) | W2 Postgres | W2 `ai.Conversation` / `ai.Message` | Чат в приложении | W2 only | Не определено | «Забудь всё»: DELETE (CD §72 п.3, «ИИ-чат приложения»). Исход по решению; runtime — не измерено; сопоставление «ИИ-чат приложения» → модели `ai` — по коду модуля [N12] | — |
| Nutrition outbox (`nutrition.NutritionOutboxEvent` — копии изменений профиля питания и воды для бота) | User | Nutrition Domain (W2, каталог `nutrition`) | W2 Postgres | W2 `nutrition.NutritionOutboxEvent` (очередь доставки в бот) | Бот (приёмник вебхуков) | W2 only; строка пишется в той же транзакции, что изменение | Как у Nutrition Profile / Water | «Забудь всё» и удаление аккаунта: DELETE (CD §72 п.3). Исход по решению; runtime — не измерено [N12] | Очередь доставки, не источник истины |

## Definitions

### Data Subject
Пользователь (end user), чьи данные обрабатываются в системе.

### Normative Domain / System Owner
Домен или система, несущая ответственность за семантику, политику и жизненный цикл данных.

### Physical Custodian
Сервис или хранилище, физически хранящее данные в данный момент.

### Source of Truth
Единственный авторитетный источник для данного класса данных. Все другие копии являются производными (projections) и должны синхронизироваться с источником.

### Permitted Consumers
Список доменов или сервисов, которым разрешено читать данные.

### Write Authority
Кто имеет право создавать, обновлять или удалять данные этого класса.

### Consent / Purpose
Требуемое согласие и цель обработки для данного класса данных.

### Retention & Deletion Orchestrator
Компонент, ответственный за соблюдение сроков хранения и выполнение запросов на удаление.

### Temporary Projections Rules
Правила создания временных проекций (кэшей, представлений, summary) для данного класса данных.

## Critical Boundaries

1. **W2 не владеет semantic memory.** W2 является владельцем account/profile и operational preferences, но не параллельной semantic memory.

2. **Raw wellness history ≠ memory.** Сырые измерения и история остаются в Wellness Domain. Персонализированные выводы становятся памятью только после прохождения memory gate в W3.

3. **Consent — отдельный источник истины.** Согласия не дублируются в других доменах; все решения используют authoritative consent state непосредственно из Consent Service либо из purpose-bound authoritative projection/cache с установленными freshness, TTL и invalidation guarantees. Независимый source of truth запрещён.

4. **Projections не являются памятью.** Временные проекции (dashboards, summaries, API views, booking-specific views) не становятся MemoryEntry без прохождения proposal/consent/purpose gate.

5. **Offboarding не переносит и не удаляет память.** Завершение сотрудничества (например, master offboarding) меняет access grants, но не владельца памяти. Удаление памяти возможно только через отдельный пользовательский privacy request через W3 privacy flow.

6. **Conversations и internal chat не создают память автоматически.** Создание MemoryEntry из разговоров возможно только через отдельный W3 proposal/consent/purpose gate.

7. **Master не имеет прямого доступа к semantic memory.** Master видит только разрешённую purpose-limited projection. Прямое чтение, редактирование, удаление или экспорт semantic memory запрещены.

8. **«Забудь всё» стирает дневник, цели, план и профиль питания одной транзакцией.** `FoodLog`, `WaterEntry`, `SavedMeal`, `FoodScan` с фото стираются в той же транзакции «всё или ничего», что цели, план и профиль питания; экспорт персональных данных несёт дневник (AYLA-DEC-0101). «Забудь всё» — не удаление аккаунта: бронирования и оплаты не затрагиваются. По CD §72 п.2–3 «забудь всё» также стирает снимок переписки в задаче оператора (и при открытой задаче), историю уведомлений в приложении, ИИ-чат приложения и `NutritionOutboxEvent`; настройки уведомлений и избранные мастера остаются, и текст команды говорит, что избранное сохраняется.

9. **Аллергия — красная зона с двумя читателями.** Для обработки читают только фильтр рекомендаций и сканер; кроме них — доступ субъекта к своей записи (показ, экспорт, удаление) с журналом. Аллергия не попадает ни в текст для любой модели, ни во внешнюю LLM. Неизвестный или неполный состав даёт `UNKNOWN`, а не «безопасно»; гарантий безопасности по одному отсутствию найденного аллергена нет (AYLA-DEC-0100).

10. **Дата рождения — одно место.** Полная дата рождения хранится только в профиле каталога; наружу — только возрастной статус и возраст в полных годах. Второй носитель возраста или даты рождения — нарушение этой границы (AYLA-DEC-0100), кроме переходного `NutritionProfile.age` до ближайшего прохода анкеты (бриф M-1). Сегодняшний второй носитель в боте — [Q2].

11. **Флаги здоровья не уходят во внешнюю модель.** Ни сами флаги, ни производный признак их наличия (AYLA-DEC-0098).

## Migration Notes

Этот документ не меняет существующие API shapes или runtime-поведение. Он фиксирует существующие границы и требует постепенного приведения реализации в соответствие с зафиксированной моделью.

Изменения кода, моделей, API и миграций выполняются в отдельных циклах после утверждения этой модели.

Строки v1.1 разделяют «целевое» (решение владельца) и «текущее» (факт кода на SHA ниже). Расхождение — долг с листом, а не новая норма.

## Runtime Evidence (pilot, 2026-09-21)

Каталог `djangoproject` @ `4dbff523`, бот `ai-bot-platform` @ `0e2c0100`; процитированные файлы не менялись до `a8c8f0c3` / `eec1ded5` (21.09 16:17 MSK); на более поздних головах номера строк не сверялись. Префиксы: `cat:` — каталог, `bot:` — бот.

- **[N1] «Забудь всё» в каталоге.** `cat:users/forget_all_catalog.py:77-158` (`erase_remembered_catalog`): цели и планы — :121-129; профиль питания — :134-135; дневник — :139-150 (файлы сканов снимаются раньше строк — :140-141). Все три вызывающих зовут его в одной `transaction.atomic()` с `erase_personal_context`: C5.2 — `cat:users/personal_data_api.py:356-366` (по каждой личности субъекта); приложение — `cat:users/personal_context_views.py:199-201`; внутренний `DELETE …/personal-context/` — `cat:users/internal_personal_context_api.py:219-221`. Пределы: поле `deleted` ответа C5.2 по-прежнему называет только `personal_context` (`cat:users/personal_data_api.py:30-31`, :371-374); readback C5.3 проверяет только строку `UserPersonalContext` (`cat:users/personal_data_api.py:420-429`, `cat:users/personal_context_erasure.py:164-184`) — стирание новых классов readback-ом не подтверждается; `recommendation.Recommendation.target_outcomes` каталога остаётся (`cat:users/forget_all_catalog.py:42-47`). Тесты `cat:users/tests/test_forget_all_catalog_2214.py`, `cat:users/tests/test_forget_all_diary_2214.py` — в этой работе не запускались.
- **[N2] Экспорт C5.1.** `cat:users/personal_data_api.py:266-296`: `profile`, `personal_context`, `specialist_profile`, `linked_identities`. Целей, анкеты, плана, профиля питания, дневника, воды, сканов нет. Бот отдаёт раздел `ayla` дословно (`bot:apps/identity/services/privacy.py:438-459`; `bot:apps/identity/export_coverage.py:280-284`).
- **[N3] PlanAction.** `cat:wellness/models.py:390-446`: `plan`, `action_type`, `cadence`, `target_count`, `created_at`; полей провенанса и версии нет.
- **[N4] DiaryDay.** `cat:nutrition/services/diary_days_service.py:67-80` — неизменяемый dataclass, вычисляемый на запрос; модели нет.
- **[N5] Сроки без «забудь всё».** Фото сканов: `TTL_DAYS = 30` — `cat:nutrition/management/commands/purge_expired_food_photos.py:121`. Мягко удалённая вода: `purge_deleted_water_entries(older_than_days=90)` — `cat:nutrition/services/water_entry_service.py:671`.
- **[N6] Латентный вход аллергий в каталоге.** `cat:nutrition/serializers.py:503-509` — `allergies`, `allergies_vague` среди ключей `health_flags`.
- **[N7] Recommendation (бот).** Модель — `bot:apps/recommendation/models.py:32-75`; обезличивание — `bot:apps/recommendation/erasure.py` (`anonymize_recommendations`), вызывается только из каскада удаления C5 (`bot:apps/identity/services/privacy.py:807-820`). Свип «забудь всё» его не вызывает (`bot:apps/identity/services/forget_all_sweep.py:160-289`); в матрице DRF-2134 строки нет (`bot:apps/identity/tests/test_forget_all_matrix.py:135-247`); в `export_coverage` строки нет (`bot:apps/identity/export_coverage.py:53-262`).
- **[N8] Журнал Decision Engine.** Поиск `class .*Decision.*(models.Model)` по обоим репозиториям на указанных SHA — ноль совпадений (охват — `*.py` без тестов; хранилища вне Django-моделей не искались).
- **[N9] Аллергия.** Запись: фраза отбрасывается — `bot:apps/persona/memory_extract.py:425-436` (`allergy_clause_dropped`). «Забудь всё»: свип всех трёх зон с `RedZoneAccessLog` на красную строку — `bot:apps/identity/services/forget_all_sweep.py:48-72`, :201-203; матрица DRF-2134 — DELETE для red, `bot:apps/identity/tests/test_forget_all_matrix.py:146-151`. DELETE в этой матрице — надгробие, физическая очистка — отдельно (`bot:apps/identity/tests/test_forget_all_matrix.py:28-30`; AMD-001 §3.4). Экспорт: red объявлен невыгружаемым — `bot:apps/identity/export_coverage.py:196-201` («отдельное решение владельца» — теперь принято: AYLA-DEC-0100).
- **[N10] Дата рождения.** Каталог: полей даты рождения в моделях нет (поиск `birth` по `*.py` без миграций и тестов — только комментарии). Бот: `bot:apps/identity/models.py:491-496` (`birthday_date`; год хранится «for age-conditional offers»); экспорт — `bot:apps/identity/export_coverage.py:81`, `bot:apps/identity/services/privacy.py:533-546`; «забудь всё» — RETAIN: `bot:apps/identity/services/forget_all_sweep.py:80-88`, `bot:apps/identity/tests/test_forget_all_matrix.py:197-202`, текст команды — `bot:apps/persona/memory_commands.py:66-78`; удаление C5 — DELETE: `bot:apps/identity/services/privacy.py:346-364`. Возраст сегодня — `cat:nutrition/models.py:481` (`NutritionProfile.age`).
- **[N11] Стакан.** `bot:apps/miniapp_api/views.py:3457` (`_WATER_GLASS_ML = 250`); старый путь воды каталога — фиксированные объёмы, `cat:nutrition/models.py:285-309`.
- **[N12] Хранилища из решения CD §72 (21.09, вечер; журнал главного окна вне git).** Носители найдены по коду; исход «забудь всё» по ним не измерялся. Бот @`0e2c0100`: `bot:apps/handoff/models.py:71` (`AdminTask`), `:132` (`transcript_snapshot`). Каталог @`4dbff523`: `cat:notifications/models.py:24` (`Notification`); `cat:users/models.py:537` (`FavoriteSpecialist`); `cat:ai/models.py:34` (`Conversation`), `:103` (`Message`); `cat:nutrition/models.py:326` (`NutritionOutboxEvent`). `cat:users/forget_all_catalog.py` на этом SHA ни одну из четырёх каталожных моделей не называет — вывод по тексту модуля, тесты не запускались. Модель настроек уведомлений не выбиралась.

## Связь с матрицей «забудь всё» DRF-2134

Эта матрица — нормативный перечень классов и исходов. Runtime-сторож бота — `bot:apps/identity/tests/test_forget_all_matrix.py` (DRF-2134): состав хранилищ бота выводится из `bot:apps/identity/export_coverage.py`, исход по каждому проверяется после свипа, дыры держатся `xfail(strict=True)`. Хранилища каталога в него не входят (`bot:apps/identity/tests/test_forget_all_matrix.py:47-53`); их держат тесты каталога DRF-2214 [N1]. Правило согласования: каждая строка v1.1 с физическим носителем в боте обязана иметь строку в `OUTCOMES` сторожа и строку в `export_coverage`; каждая строка с носителем в каталоге — тест исхода «забудь всё» в каталоге. Сегодня этому правилу не отвечают строки Recommendation record (нет ни в `OUTCOMES`, ни в `export_coverage` — [N7]) и Allergy (экспорт — [N9]). Строки по CD §72 (снимок переписки оператора, история уведомлений, избранное, ИИ-чат приложения, `NutritionOutboxEvent`) по этому правилу не сверялись [N12].

## Open Questions

- **[Q1]** Scope согласия для целей, анкеты цели и плана: в Consent Scope Registry за этими классами не закреплён. Нужна строка CSR или явное «не требуется».
- **[Q2]** Два носителя даты рождения. AYLA-DEC-0100: полная дата — одно место, профиль каталога; «забудь всё» её удаляет (бриф M-1). Бот хранит `UserPreferences.birthday_date` — полную дату для поздравлений; «забудь всё» её сохраняет, и текст команды это обещает («настройки уведомлений с датой рождения»). AYLA-DEC-0101 требует не менять текст команды. Нужно решение владельца: какой носитель остаётся, что говорит команда, стирает ли «забудь всё» дату для поздравлений.
- **[Q3]** Размер стакана: где хранится (W2 профиль, W3 `UserPreferences`, клиент) и его исход под «забудь всё» — RETAIN как настройка, которую ведёт человек, или DELETE как часть дневника.
- **[Q4]** Форма экспорта версий действия плана: только актуальная версия или вся история, включая версии «удалено».
- **[Q5]** День дневника под «забудь всё»: DELETE выведен из AYLA-DEC-0101 («стирать дневник вместе со всем»), в решении сущность не названа — подтвердить в Ayla Diary and Water Contract.
- **[Q6]** Экспорт сканов: только метаданные и результат распознавания или также файл фото.
- **[Q7]** Стоимость провайдера в `FoodScan` стирается вместе со строкой при «забудь всё»; при возврате попытки (DRF-2218) её решено не стирать. Нужно ли сохранять денежный учёт обезличенно — решение владельца.
- **[Q8]** Recommendation record в экспорте: выдавать значения (`what`, `why`, `facts`) или объявить невыгружаемыми с причиной.
- **[Q9]** Журнал Decision Engine: владелец, физический носитель, хранит ли значения фактов или только ссылки, исход «забудь всё», экспорт.

## Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-07-24 | Safety and Governance Domain | Initial draft created per memory ownership reconciliation plan |
| 1.1 | 2026-09-21 | Safety and Governance Domain | Добавлены 14 строк по решениям AYLA-DEC-0092, 0094, 0095, 0097, 0098, 0099, 0100, 0101: Goal, Goal questionnaire, Personal Plan, Plan Action versions, Diary Day, Food Diary, Food scanner photo, Water, Nutrition Profile, Recommendation record, Decision Engine journal, Allergy (red), Date of birth, Glass size. Исход «забудь всё» и экспорт — по коду каталога `4dbff523` и бота `0e2c0100`, в форме «целевое / текущее / лист». Добавлены критические границы 8–11, разделы Runtime Evidence, связь с DRF-2134 и Open Questions. Статус не меняется |
| 1.1 (рецензия KB-D) | 2026-09-21 | Safety and Governance Domain | По рецензии: основание согласия дневника и профиля — фактом CSR §5.10, scope нет (`CSR-OD-13`, `CSR-OD-16`); владелец даты рождения — `CSR-OD-11`; DT-1 в строке Food Diary — полностью; граница 9 — «ни в текст для любой модели»; граница 10 — переходный `NutritionProfile.age`; время снятия SHA в Runtime Evidence. По CD §72: строки снимка переписки оператора, истории уведомлений, избранного, ИИ-чата приложения, `NutritionOutboxEvent` (п.2–3) и Sunset старых адресов `WaterLog` 31.10.2026 (п.14) — исход по решению, runtime не измерен [N12]. Статус не меняется |
