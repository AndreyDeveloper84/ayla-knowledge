---
node_id: ayla.strategy.mvp-reset-roadmap
title: Ayla MVP Reset Roadmap
type: specification
status: approved
version: "1.0"
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
updated: 2026-07-29
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

- Transformation Goal;
- срок и приоритеты;
- consent;
- фото/видео;
- baseline;
- качество данных.

### Sprint 2 — Desired Outcome + Plan

- желаемый образ;
- вероятностная визуализация;
- уровень уверенности;
- комплексный план;
- объяснение факторов.

### Sprint 3 — Daily Execution

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
