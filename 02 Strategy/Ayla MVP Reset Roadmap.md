---
node_id: ayla.strategy.mvp-reset-roadmap
title: Ayla MVP Reset Roadmap
type: specification
status: approved
version: "1.1"
owner: Product Owner
priority: P0
depends_on:
  - "[[Ayla Product Essence]]"
knowledge_area:
  - strategy
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
created: 2026-07-29
updated: 2026-09-21
review_cycle: monthly
---

# Ayla MVP Reset Roadmap

**Статус:** CANONICAL  
**Дата owner approval:** 2026-07-29  
**Владелец:** Product Owner  
**Слой:** Operational  
**Роль:** канонический операционный источник последовательности перестройки продукта и выпуска MVP

> Roadmap не переопределяет Product Essence и не занимает места в продуктовой иерархии между Essence и Product Vision. Каноническая рабочая версия хранится в `ayla-knowledge`. Внешняя копия `D:\Проекты\Ayla\Ayla_MVP_Reset_Roadmap.md` не является authoritative.

**Цель:** максимально быстро перестроить текущий продукт под новую Product Essence и выпустить MVP без блокировки на полноценном 3D Digital Twin.

## Заменённые разделы (v1.1, 2026-09-21)

**Версия 1.1 — частичная замена.** Разделы ниже заменены решениями владельца и **не действуют**. Их текст сохранён на месте для истории, каждый помечен строкой «Заменено». Все остальные разделы действуют без изменений. Основание: `AYLA-DEC-0087` (K-1) — «Reset Roadmap выпускается версией 1.1 с разделом “Заменённые разделы” — §2 “Основной путь”, §5 Sprint 1–4 и §7 “Минимальные новые сущности” заменены новыми DEC и не действуют, остальные разделы действуют».

| Раздел | Что больше не действует | Чем заменено |
|---|---|---|
| §2, блок «Основной путь» | обязательный линейный путь «регистрация → цель → фото/видео → … → прогресс» | `AYLA-DEC-0087`: цель необязательна; ни дневник, ни вода, ни вопрос, ни запись, ни явно выбранное действие не требуют цели. Перечень P0-документов §2 остаётся |
| §5 Sprint 1 «Goal + Baseline» | цель как первый обязательный шаг; baseline, фото/видео | `AYLA-DEC-0087`; `AYLA-DEC-0088` (без наблюдений тела); `AYLA-DEC-0094` (Desired Outcome не активируется) |
| §5 Sprint 2 «Desired Outcome + Plan» | желаемый образ, вероятностная визуализация, уверенность, «комплексный план» | `AYLA-DEC-0088` (Plan Lite: 1–3 действия, «N из M»); `AYLA-DEC-0089` (таблица «цель → план»); `AYLA-DEC-0094` |
| §5 Sprint 3 «Daily Execution» | состав ежедневного исполнения (сон, активность, расписание плана) | `AYLA-DEC-0087` (состав продукта: Plan Lite, дневник, ориентиры, вода, сканер, Диетолог-отчёты, proactive по opt-in); `AYLA-DEC-0095` (день дневника); `AYLA-DEC-0099` (вода) |
| §5 Sprint 4 «Progress Loop» | повторная фотофиксация, «старт / сегодня / цель», обновление уверенности | `AYLA-DEC-0088` (прогресс — только «N из M» действий); `AYLA-DEC-0094` |
| §7 «Минимальные новые сущности» | перечень TransformationGoal … ProcedureRecommendation как обязательный | `AYLA-DEC-0088`, `AYLA-DEC-0094`; сущности определяют контракты этапа C (Goal and Desired Outcome, Personal Plan, Diary and Water) |

§5 Sprint 5 «Procedure → Specialist → Booking» и Sprint 6 «Release Hardening» действуют.

## 1. Немедленно

На 2–4 дня вводится freeze на новые продуктовые функции.

Разрешены:

- исправления блокирующих ошибок;
- канонизация документов;
- инвентаризация кода;
- новый MVP vertical slice;
- release-critical инфраструктура.

## 2. Канонизация продукта — 2–4 дня

P0-документы:

1. Product Essence — утвердить.
2. Product Principles — создать.
3. MVP Scope — переписать.
4. MVP User Journey — переписать.
5. Screen Registry — обновить.
6. Transformation Goal Model — создать.
7. Prediction and Confidence Policy — создать.

Основной путь:

> **Заменено: `AYLA-DEC-0087`, не действует** (v1.1). Цель необязательна; обязательного линейного пути нет. Текст ниже сохранён для истории.

```text
регистрация
→ цель
→ фото/видео
→ исходная модель
→ желаемый результат
→ план
→ расписание
→ вода/еда/активность
→ процедура
→ запись
→ повторная фиксация
→ прогресс
```

## 3. Ревизия документов агентами — 3–5 дней

### Волна A — Foundation

- Product Vision
- Product Thesis
- Product Principles
- MVP Scope
- MVP User Journey

### Волна B — Domain

- Core Domain Model
- Transformation Goal Model
- Longitudinal Care Model
- Intent Model
- Memory Model
- Recommendation Model
- Prediction and Confidence Policy
- Consent Scope Registry
- Safety Policy

### Волна C — UX

- Screen Registry
- Navigation Model
- Onboarding Flow
- Daily Home Flow
- Visual Progress Flow
- Plan and Schedule Flow
- Food / Water / Fitness Flow
- Procedure and Booking Flow

### Волна D — Engineering

- backend architecture;
- AI orchestration;
- longitudinal care loop;
- memory pipeline;
- media pipeline;
- API contracts;
- analytics events;
- retention and deletion.

## 4. Инвентаризация кода — 2–3 дня параллельно

Для каждого модуля выставить:

- KEEP;
- ADAPT;
- REBUILD;
- DEFER;
- REMOVE;
- MISSING.

Обязательные модули аудита:

Auth, Profile, Chat, Memory, Goals, Media, Visual Model, Plan, Schedule, Food, Water, Fitness, Procedures, Specialists, Booking, Notifications, Consent, Analytics.

## 5. MVP vertical slice — 3–6 недель

### Sprint 1 — Goal + Baseline

> **Заменено: `AYLA-DEC-0087`, `AYLA-DEC-0088`, `AYLA-DEC-0094`, не действует** (v1.1).

- Transformation Goal;
- срок и приоритеты;
- consent;
- фото/видео;
- baseline;
- качество данных.

### Sprint 2 — Desired Outcome + Plan

> **Заменено: `AYLA-DEC-0088`, `AYLA-DEC-0089`, `AYLA-DEC-0094`, не действует** (v1.1).

- желаемый образ;
- вероятностная визуализация;
- уровень уверенности;
- комплексный план;
- объяснение факторов.

### Sprint 3 — Daily Execution

> **Заменено: `AYLA-DEC-0087`, `AYLA-DEC-0095`, `AYLA-DEC-0099`, не действует** (v1.1).

- главный экран;
- план дня;
- расписание;
- вода;
- еда;
- активность;
- сон;
- отметка выполнения;
- сообщения Ayla.

### Sprint 4 — Progress Loop

> **Заменено: `AYLA-DEC-0088`, `AYLA-DEC-0094`, не действует** (v1.1).

- повторная фотофиксация;
- старт / сегодня / цель;
- объяснение прогресса;
- обновление уверенности;
- корректировка плана.

### Sprint 5 — Procedure → Specialist → Booking

- рекомендация процедуры;
- связь с целью;
- специалист;
- время;
- запись;
- добавление в расписание.

### Sprint 6 — Release Hardening

- удаление данных;
- fallback AI;
- observability;
- analytics;
- notifications;
- privacy review;
- performance;
- app-store readiness.

## 6. Что не блокирует MVP

Отложить:

- полноценную фотореалистичную 3D-реконструкцию;
- сложную биомеханику;
- анализ походки;
- медицинский анализ кожи;
- точный состав тела;
- универсальный сценарный симулятор;
- полную wearable-интеграцию;
- социальные функции;
- сложную геймификацию.

## 7. Минимальные новые сущности

> **Заменено: `AYLA-DEC-0088`, `AYLA-DEC-0094`, не действует** (v1.1). Сущности определяют контракты этапа C.

- TransformationGoal
- BaselineAssessment
- DesiredOutcome
- PersonalPlan
- PlanItem
- DailyAction
- MediaCapture
- VisualModelVersion
- ProgressObservation
- Prediction
- ConfidenceAssessment
- FoodRecord
- WaterRecord
- ActivityRecord
- ProcedureRecommendation

## 8. Минимальный набор экранов

1. Welcome
2. Goal Creation
3. Photo and Video Capture
4. Current Model
5. Desired Outcome
6. Forecast and Confidence
7. Personal Plan
8. Today / Home
9. Schedule
10. Food Scanner
11. Water Quick Add
12. Fitness Action
13. Weekly Check-in
14. Progress Comparison
15. Procedure Recommendation
16. Specialist Selection
17. Booking Confirmation
18. Data and Consent

## 9. Release gates

### Product

- цель создаётся;
- baseline фиксируется;
- план формируется;
- ежедневные действия доступны;
- повторная фиксация работает;
- прогресс отображается.

### UX

- каталог не является центром;
- Digital Twin / Visual Progress — ключевой опыт;
- рекомендации объяснимы;
- прогноз не выглядит гарантией.

### Engineering

- фото и видео защищены;
- исходные и производные данные удаляются;
- AI имеет безопасный fallback;
- события отслеживаются;
- критические сценарии протестированы.

### Safety

- нет медицинской диагностики;
- нет body shaming;
- нет гарантированных обещаний;
- опасные цели ограничены;
- consent scopes прозрачны.

## 10. Метрики пилота

Главная метрика:

> Доля пользователей, которые создали цель, получили план и вернулись для повторной фиксации прогресса.

Дополнительно:

- onboarding completion;
- baseline completion;
- plan activation;
- D1 / D7 / D30 retention;
- weekly check-in;
- повторная фотофиксация;
- выполнение daily actions;
- Food Scanner usage;
- Water Tracker usage;
- procedure recommendation conversion;
- booking conversion.

## 11. Порядок запуска агентов

1. **Canon Architect** — Foundation.
2. **Domain Architect** — сущности и контракты.
3. **UX Architect** — screen registry и flows.
4. **AI Architect** — orchestration, memory, longitudinal loop.
5. **Backend Auditor** — code inventory и migration map.
6. **Mobile Auditor** — текущие экраны против нового MVP.
7. **Privacy/Safety** — consent, retention, deletion, prediction policy.
8. **Delivery Lead** — единый backlog и release plan.

## 12. Рекомендуемый календарь

### Неделя 1

- канон;
- MVP Scope;
- User Journey;
- code inventory;
- Screen Registry.

### Неделя 2

- domain contracts;
- API;
- UX prototype;
- migration plan.

### Недели 3–4

- Goal;
- Media Capture;
- Baseline;
- Desired Outcome;
- Plan;
- Home;
- Schedule.

### Недели 5–6

- Food;
- Water;
- Fitness;
- Progress;
- Procedure;
- Booking.

### Неделя 7

- safety;
- analytics;
- notifications;
- pilot.

### Неделя 8

- исправления;
- release candidate;
- ограниченный публичный запуск.

## 13. Главное правило скорости

Не строить весь Digital Twin до запуска.

Сначала доказать:

```text
человек видит цель
→ получает план
→ выполняет действия
→ возвращается
→ видит прогресс
```

После подтверждения этого цикла углублять 3D, симуляцию и прогнозирование.

## История версий

### v1.1 — 2026-09-21 — частичная замена (DRF-2260)

- Добавлен раздел «Заменённые разделы». §2 «Основной путь», §5 Sprint 1–4 и §7 «Минимальные новые сущности» помечены «Заменено … не действует» со ссылками на `AYLA-DEC-0087`, `0088`, `0089`, `0094`, `0095`, `0099`. Текст разделов сохранён.
- Статус документа (`approved`, CANONICAL) не менялся; новых значений статуса не вводилось. В CANON_INDEX — строка v1.1 CANONICAL и строка v1.0 SUPERSEDED (прецедент Product Essence v1.1 → v1.2).
- Закрыт OD-AUDIT-004 (противоречие с MVP User Journey в части обязательного линейного пути) — `AYLA-DEC-0087`.

### v1.0 — 2026-07-29

- Owner approval; канонический операционный источник.
