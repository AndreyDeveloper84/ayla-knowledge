---
node_id: ayla.strategy.mvp-product-thesis
title: Ayla MVP Product Thesis
type: product-thesis
status: draft
canonical_status: candidate
version: "0.6"
owner: Product Owner
priority: P0
knowledge_area:
  - strategy
domain:
  - cross-domain
concerns:
  - governance
system_owner:
  - shared
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
updated: 2026-08-07
review_cycle: before-major-change
implements:
  - "[[Ayla Constitution]]"
depends_on:
  - "[[Ayla Product Essence]]"
  - "[[Ayla — Product Vision]]"
  - "[[Ayla Living Digital Twin Manifesto]]"
  - "[[Ayla Constitution]]"
  - "[[Ayla Decision Log]]"
related:
  - "[[Killer PRD]]"
  - "[[Ayla MVP User Journey Specification]]"
  - "[[Ayla Glossary]]"
supersedes: []
---

# Ayla MVP Product Thesis v0.6

**Статус:** DRAFT / canonical candidate — targeted amendment, ожидает
Product Owner Final Review
**Версия:** 0.6
**Положение:** Foundation document №2 (Vision → **Thesis** → Principles →
MVP Scope → User Journey)
**Основание:** Owner Decisions OD-MVP-1…4; `Ayla MVP Product Thesis —
Amendment Plan v0.5 → v0.6`; Ayla Product Essence v1.2 (candidate);
Ayla — Product Vision v2.1 (candidate)

> Документ находится ниже Ayla Product Essence v1.2 и Product Vision v2.1 и
> не может их переопределять. Это targeted amendment v0.5 → v0.6: заменена
> обязательная LDT-dependent MVP hypothesis на representation-neutral value
> loop; testable thesis structure, Phase 1/2 validation, unit economics и
> Product Owner closure сохранены. См. Change Log.

## 1. Purpose

Этот документ фиксирует **узкий, стратегический слой** над Killer PRD и
Ayla MVP User Journey Specification: что входит и не входит в MVP пилота, кто
целевая аудитория, и по какому принципу принимается решение включать новую
функцию в MVP. Он не переопределяет и не дублирует killer-сценарий, метрики
атрибуции или Journey-механику — они остаются нормативны в Killer PRD и
Journey Specification соответственно.

**Положение в каноне.** Этот документ — **Foundation document №2** в
канонической последовательности (Vision → Thesis → Principles → MVP Scope →
User Journey). Родительский продуктовый источник — [[Ayla Product Essence]]
v1.1 (CANONICAL); канонический долгосрочный контекст —
[[Ayla — Product Vision]] v2.0 (CANONICAL); обязательный согласующий input
для положений о Living Digital Twin — [[Ayla Living Digital Twin Manifesto]]
v1.0 (sibling-документ под Product Essence, **не родитель** этого Thesis).
Документ находится ниже Essence и Vision и не может их переопределять.

В отличие от Vision, Thesis фиксирует не долгосрочный горизонт, а
**проверяемую гипотезу MVP**: что именно пилот должен подтвердить или
опровергнуть, чтобы продуктовая стратегия считалась жизнеспособной.

## 2. Scope

Документ определяет:
- проверяемую MVP-гипотезу (§4) и качественные сигналы её подтверждения и
  опровержения (§8.1, §8.2);
- Product Thesis Validation Gate (§8.4);
- целевые сегменты пилота;
- явную границу MVP scope (что внутри / что снаружи);
- принцип admission criteria для новых функций.

## 3. Non-goals

Этот документ **не** определяет:
- долгосрочное видение продукта — см. [[Ayla — Product Vision]];
- точный релизный состав MVP — принадлежит MVP Scope (Foundation document
  №4);
- killer moment, attribution, qualified action — см. [[Killer PRD]] §3;
- состояния Journey, gates, memory classes — см.
  [[Ayla MVP User Journey Specification]];
- конкретные тарифы и расчётные схемы — см. [[Ayla Decision Log]]
  (AYLA-DEC-0001, 0007, 0008, 0010);
- домены и запреты продукта — см. [[Ayla Constitution]] Ст. I;
- UX flows и интерфейсные решения — UX-документы;
- техническую архитектуру и доменные схемы — Architecture/Domain-документы;
- AI/ML-реализацию, similarity score и числовые пороги — Measurement
  Framework (planned).

**Явная граница (v0.6):** точный обязательный feature composition MVP,
включая точную роль Living Digital Twin в первом релизе, принадлежит
`Ayla MVP Scope and Release Contract`, а не Product Thesis.

## 4. Central Thesis

### 4.1 Каноническая рамка

> **Изменено (v0.6, OD-MVP-1).** LDT снят из статуса обязательного элемента
> канонической рамки первого MVP и стал условным representation layer.

Документ применяет representation-neutral разделение центров канона
(Ayla Product Essence v1.2, Owner Decisions OD-MVP-1…4):

- **человек — главный герой** продукта;
- **Transformation Goal — центральная доменная сущность**;
- **Ayla — интеллектуальный помощник и оркестратор пути**;
- **relevant context/signal** — понимается в контексте цели;
- **память — механизм continuity и персонализации**, не центр продукта;
- **рекомендация — объяснимый следующий шаг**; **booking —
  downstream-действие** плана;
- **Living Digital Twin — опциональная стратегическая capability**,
  которая может усиливать видимость состояния и прогресса, но не является
  обязательным элементом первого MVP (Essence v1.2 §1, §9, §12).

Transformation Goal не является KPI, прогнозом или обещанием результата
(Vision §6).

### 4.2 Решение AYLA-DEC-0002

**Краткая формулировка (AYLA-DEC-0002, дословно):** Moat Ayla — не запись, а
накопленное и объяснимое понимание пользователя. Цепочка «еда → рекомендация
в beauty/wellness» — один из равноправных триггеров, не ядро продукта.
Конкурентное окно для формирования этого рва — 12–18 месяцев.

> **Примечание о характере цифры 12–18 месяцев:** эта оценка зафиксирована
> дословно в AYLA-DEC-0002 и не изменяется здесь как искажение цитаты
> решения. По существу это прогноз команды на основе Research Synthesis
> (`00-SYNTHESIS.md`, `05-competitive.md`), а не проверяемый факт — при
> использовании этой цифры вне цитаты решения (например, в презентациях)
> следует явно указывать её как оценочную, а не как доказанный срок.

> **Нормативное пояснение (v0.5):** AYLA-DEC-0002 действует, но память не
> является единственным центром продукта: по Product Essence v1.1 и Product
> Vision v2.0 она работает как continuity внутри составной продуктовой
> гипотезы. Защищаемое преимущество — составное: персональная память,
> долгоживущая Twin-модель и история прогресса, ежедневная привычка,
> поведенческие данные, сеть мастеров (Vision §17). Это пояснение фиксирует
> каноническую позицию и не вводит нового нормативного moat-contract.

> **Уточнение (v0.6, OD-MVP-1):** Living Digital Twin может усиливать moat
> (Vision §17), но не является обязательным условием первого доказательства
> Product Thesis. Food/beauty-триггер остаётся одним из равноправных
> trigger-сценариев и не становится вечной thesis-зависимостью; Food
> Intelligence — первая конкретная реализация класса `Signal` в MVP Scope,
> не идентичность Thesis.

### 4.3 Проверяемая гипотеза MVP

> **Заменено (v0.6, OD-MVP-1, OD-MVP-4).** Обязательная composite hypothesis
> с Living Digital Twin viability как элементом заменена на representation-
> neutral value loop `Goal → Signal → Context → Recommendation → Action →
> Memory Continuity → Progress`. LDT recognition/identity больше не является
> обязательным элементом проверки основной гипотезы Thesis.

**Развёрнутая гипотеза MVP:** если Ayla помогает пользователю сформулировать
личную Transformation Goal, понимать релевантные повседневные сигналы в
контексте этой цели, использовать разрешённую память для continuity (в
рамках согласия — Ст. VI, IX Конституции), предлагать объяснимый и уместный
следующий шаг от Ayla-оркестратора, превращать его в реалистичное действие
(включая booking как одно из downstream-действий), — и затем видеть понятный
прогресс относительно собственной цели, то пользователь продолжает работу
над собой и возвращается за продолжением собственного пути, а не ради
отдельной функции. Именно это сочетание — цель, релевантный контекст,
оркестрация, память, объяснимая рекомендация, реалистичное действие, видимый
прогресс — создаёт защищаемое конкурентное преимущество, а не любой один
элемент в отдельности.

Целевой validation loop:

```text
Transformation Goal
        ↓
Everyday Signal
        ↓
Context Understanding
        ↓
Explainable Recommendation
        ↓
Realistic Action
        ↓
Memory Continuity
        ↓
Goal-relative Progress
        ↓
Natural Return
        ↺
```

Thesis проверяет этот цикл целиком, а не отдельную функцию. Food
Intelligence — первая конкретная реализация `Signal` в MVP Scope; Thesis
остаётся signal-agnostic на своём уровне.

Это разворачивание не заменяет и не переопределяет AYLA-DEC-0002 — оно
делает исходную формулировку решения проверяемой в текущем каноне (см. §8.1
Success Criteria и §8.2 Failure Conditions). Подтверждение или опровержение
гипотезы проходит через Product Thesis Validation Gate (§8.4, по
AYLA-DEC-0018).

## 5. Target Segments — Pilot Scope (Пенза; дата — AYLA-DEC-0003)

### Provider side

Оба типа провайдера, симметрично тарифной модели AYLA-DEC-0001:

- **Соло-мастер** — независимый специалист без наёмного персонала.
- **Малый салон** — до 3 мастеров в штате.

Провайдеры вне этих двух профилей (крупные сети, франшизы) — вне MVP scope
пилота.

### Client side

Пользователи в предметной области Конституции Ст. I (питание, физическая
активность, спорт, восстановление, сон, self-care, внешний уход и связанные
услуги), физически находящиеся в зоне охвата пилотных провайдеров (Пенза).

**Обновлено (v0.2):** демографическая/психографическая сегментация
определена на уровне продукта в целом — [[Ayla — Product Vision]] §13:
«женщина 20–45, Россия и СНГ», «занятая профессионал 25–40»,
«self-improvement аудитория 20–35». Открытый вопрос сужается: действуют ли
все три персоны одинаково для пилота в Пензе, или пилот — валидация
подмножества (см. §10 Open Questions).

## 6. MVP Scope — What's In

- Каналы (факт, AYLA-DEC-0027; [[Ayla MVP Scope and Release Contract]] §8):
  **Mobile App** — primary product experience; **MAX Mini App** — required
  embedded companion; **MAX Bot** — required conversational / notification /
  routing companion; feature parity across channels — NOT_REQUIRED; shared
  backend/state/consent/safety/analytics — REQUIRED. AYLA-DEC-0027 уточняет
  AYLA-DEC-0004, не отменяет его: Telegram остаётся вне пилотного scope.
- Монетизация: подписка 690₽/990₽ + 90₽ за завершённую запись, платит
  провайдер (AYLA-DEC-0001).
- Онлайн-оплата клиентом — опционально, не обязательна для записи
  (AYLA-DEC-0006).
- Автосписание подписки и fee с провайдера через сохранённую карту
  (AYLA-DEC-0007), split per-master через YooKassa (AYLA-DEC-0008).
- **Transformation Goal:** пользователь формулирует личную цель, вокруг
  которой строится путь (thesis-уровень; структура цели и релизный состав —
  MVP Scope/Domain).
- **Everyday Contextual Signal viability (v0.6, OD-MVP-2, заменяет
  «Living Digital Twin viability»):** пилот проверяет способность Ayla
  получить реальный пользовательский signal, интерпретировать его в
  контексте Goal, отделить observation от confirmed fact, использовать
  signal для relevant recommendation и сохранить допустимую continuity —
  не переходя safety/privacy boundary. Конкретный первый signal (Food
  Intelligence) и точный состав реализации — MVP Scope.
- **Memory as continuity:** накопление разрешённого контекста, чтобы путь
  не начинался каждый раз с нуля (AYLA-DEC-0002, Killer PRD §2.2).
- **Ayla orchestration:** объяснимый следующий шаг и перевод рекомендации
  в реальное действие; booking — downstream-действие плана, не центр
  продукта.
- **Living Digital Twin (опционально, OD-MVP-1):** если LDT включён в
  конкретный релиз, он проверяется как усиливающая, не обязательная,
  capability — по принципам Essence §18 и LDT Manifesto. LDT viability не
  является обязательным условием подтверждения этой Thesis.

## 7. MVP Scope — What's Explicitly Out

- **Telegram** как канал — вне пилотного scope (AYLA-DEC-0004).
- **Внутренний баланс/кошелёк провайдера** (вывод T+24ч) — эпик этапа 2, не
  MVP (AYLA-DEC-0008).
- Провайдеры вне профиля «соло-мастер / малый салон до 3 мастеров» (см. §5).
- Любая функция, не усиливающая проверяемую составную гипотезу (§4)
  напрямую, или относящаяся к уровню MVP Scope / UX / architecture (см. §8
  admission criteria).

**Не хватает материала для полного списка:** этот раздел собран из решений,
уже зафиксированных в Decision Log. Полного исчерпывающего реестра
«явно исключённых функций» в проекте нет — он принадлежит MVP Scope; здесь
список обзорный и пополняется по мере появления кандидатов, а не считается
закрытым.

## 8. MVP Feature Admission Criteria

> **Переименовано (v0.3).** Было «Go/No-Go Criteria» — термин обычно
> относится к решению о запуске продукта целиком, а не к добавлению
> отдельной функции. Раздел определяет именно последнее.

**Принцип (решение владельца 2026-07-27, переформулирован в v0.6 под
текущий канон и OD-MVP-1…4):** функция входит в MVP пилота, только если она
вносит проверяемый вклад хотя бы в один элемент составной гипотезы (§4) —
Transformation Goal, Context/Signal Understanding, memory continuity,
оркестрацию Ayla, объяснимую рекомендацию, реалистичное действие, видимый
прогресс, safety/user agency — и не конфликтует с остальными элементами.
Вклад в жизнеспособность Living Digital Twin допустим как усиливающий, но
не обязательный критерий admission.

> Capability не входит в MVP только потому, что она полезна, интересна или
> технически готова (v0.6). Admission должен отвечать: (1) какую часть
> testable hypothesis она помогает доказать; (2) почему нужна именно в
> текущем validation stage; (3) какой evidence она должна дать.

Функция, которая не проходит этот тест — даже если она полезна сама по
себе, коммерчески привлекательна или технически готова — остаётся вне MVP
до отдельного пересмотра scope владельцем.

Принцип сознательно качественный: формальный чек-лист (конкретные вопросы
да/нет для конкретной функции) здесь не вводится — его формализация
принадлежит уровню MVP Scope (см. §10).

## 8.1 Success Criteria — как подтвердить тезис

> **Изменено (v0.6, OD-MVP-1).** Twin recognition, repeat photo fixation,
> Twin correction success и identity continuity metrics убраны как
> universal success conditions всей MVP Thesis. Эти критерии остаются
> LDT-specific validation criteria и применяются только если LDT включён в
> конкретный релиз/эксперимент (Essence v1.2 §18; LDT Manifesto).

Тезис (§4) считается **предварительно подтверждённым** по итогам пилота,
если наблюдается совокупность признаков из всех групп ниже:

> Ни один показатель сам по себе не подтверждает центральную гипотезу —
> рост retention без роста качества рекомендаций так же не доказывает
> тезис, как и explainable-рекомендация без возврата пользователя. Тезис
> подтверждается только совокупностью признаков.

**Цель и контекст (S1):**

- пользователь формулирует и удерживает Transformation Goal и связывает с
  ней ежедневные действия;
- последующие everyday signals интерпретируются в контексте Goal;
- пользователь понимает связь между контекстом и рекомендацией;
- рост релевантности/качества рекомендаций от начала к концу пилота
  (метрика и порог — design candidate, требует Measurement Framework, см.
  паттерн ADR-0012 OD-5/OD-6: `DEFER numbers / APPROVE behavior`).

**Рекомендация и действие (S2):**

- рекомендации воспринимаются как relevant и explainable;
- рекомендация ведёт к реалистичному следующему действию; действие не
  обязательно является booking;
- часть пользователей действительно выполняет предложенное следующее
  действие.

**Память как continuity:**

- измеримое использование сохранённой памяти в принятых
  (`qualified_action`, Killer PRD §3) рекомендациях, не только в показанных;
- повторное обращение пользователей без повторного объяснения контекста
  Ayla (согласуется с Vision §8.1 «пользователь никогда не объясняет
  дважды»).

**Прогресс и возврат (S4):**

- пользователь понимает движение относительно своей цели;
- прогресс не воспринимается как decorative analytics или искусственная
  engagement-метрика;
- возникает естественная причина вернуться к Ayla; ценность повторяется не
  только в первом session.

**Доверие и безопасность (S5):**

- рекомендации не требуют скрытой коммерческой манипуляции;
- health/wellness boundary соблюдается (Constitution Ст. X);
- пользователь сохраняет agency.

> **Фаза доказательства (AYLA-DEC-0018):** утверждения, зависящие от
> персистентной памяти (группа «Память как continuity»), подтверждаются
> только на Phase 2 evidence. Успешный Phase 1 (session-only vertical
> slice) подтверждает технический release gate, но не memory-dependent
> часть тезиса (см. §8.4).

**Конкретные числовые пороги не устанавливаются в этом документе.** Как и
числовые TTL/пороги ADR-0012, они остаются design candidates до появления
данных пилота или отдельного Measurement Framework — фиксировать их здесь
означало бы выдавать гипотезу за решение.

## 8.2 Failure Conditions — как опровергнуть тезис

> **Изменено (v0.6, OD-MVP-1).** Twin recognition failure, identity drift и
> отказ от повторной фотофиксации убраны как автоматическое опровержение
> всей MVP Thesis: они становятся LDT-specific failure только если LDT
> включён в конкретный релиз/эксперимент (Essence v1.2 §18; LDT Manifesto).

Тезис считается **неподтверждённым** для данной итерации, если по итогам
пилота наблюдается один или несколько из следующих сигналов:

1. Transformation Goal не влияет на дальнейшие рекомендации/действия.
2. Everyday context не улучшает релевантность рекомендаций.
3. Рекомендация остаётся generic, не персонализированной под контекст.
4. Explainability не создаёт доверия/понимания у пользователя.
5. Action layer не приводит к реалистичному действию пользователя.
6. Персонализация на основе памяти не увеличивает долю
   `qualified_action` по сравнению с рекомендациями без использования
   памяти (сопоставимого контекста); память не создаёт continuity.
7. Персистентный контекст вызывает confusion или недоверие к privacy
   (риск для Ст. VII, IX Конституции).
8. Пользователь не видит понятного прогресса относительно своей цели.
9. Нет естественной причины вернуться к Ayla.
10. Пользовательская ценность сводится только к одной функции (например,
    booking или food recognition) вместо составного пути.
11. Коммерческие стимулы искажают персональную рекомендацию.
12. Safety boundary систематически нарушается.

Как и в §8.1, конкретные пороги — design candidates, не решения.

**LDT-specific failure (условно, только если LDT включён):** систематическое
не-узнавание Twin, повторяющийся неразрешённый сигнал «это не похоже на
меня», систематический агрегатный отказ от повторной фотофиксации или
identity drift между версиями Twin. Это условие относится к LDT-specific
validation (Essence v1.2 §18) и не является автоматическим опровержением
основной MVP Thesis, если LDT не входит в проверяемый релиз.

## 8.3 MVP Principles — операционализация Конституции для MVP-этапа

> **Изменено (v0.6, OD-MVP-1…4).** LDT-specific строки (узнаваемость/
> идентичность Twin, контроль над Twin) сделаны условными — применяются
> только если LDT включён в релиз. Добавлены строки для User Outcome First,
> Contextual Proactivity, Progressive Memory и Safety & Wellness Boundary
> по мотивам Product Principles Amendment Plan v0.1 → v0.2 (формально
> закрепляются в Product Principles v0.2; здесь — операционализация для
> MVP-контекста).

Это **не новый список принципов**, а явная привязка существующих статей
Конституции и принципов канона к конкретному MVP-контексту, чтобы решения
по функциям можно было принимать без каждого обращения к Product Owner:

| MVP-принцип | Источник |
|---|---|
| Усиливает объяснимую память, не просто объём данных | Ст. VII (право на объяснение), §8.2 выше |
| Не увеличивает когнитивную нагрузку пользователя | Vision §3.1 (проблема когнитивной нагрузки); Ст. X (уместность прежде действия) |
| Сохраняет контроль пользователя над контекстом (просмотр/исправление/удаление) | Ст. VII, IX |
| Observation ≠ confirmed fact; AI inference ≠ user fact | Essence §8; Product Principles v0.2 (Progressive Memory) |
| Разделяет факт, реконструкцию, оценку, прогноз и цель — условно, где применимо persistent representation | LDT Manifesto §9; Essence §8 |
| Не создаёт скрытого коммерческого приоритета | Ст. IV (экономическая нейтральность) |
| Не расширяет предметную область без отдельного решения | Ст. I |
| Соблюдает Safety & Wellness Boundary: wellness-сигналы (включая food) не становятся медицинским выводом | Ст. X, Ст. XII; Product Principles v0.2 |
| User Outcome First: не оптимизирует engagement/booking-count вместо пользы для цели | Product Principles v0.2 |
| Proactivity — только по meaningful, explainable и goal-relevant сигналу | Product Principles v0.2 |

**Условно (только если LDT включён в релиз):**

| LDT-специфичный принцип | Источник |
|---|---|
| Сохраняет узнаваемость и идентичность Twin между версиями | LDT Manifesto §5, §6; Essence §7, §18 |
| Соблюдает body dignity и anti-shaming | LDT Manifesto §13; Vision §18 |
| Оставляет пользователю контроль над Twin («не похоже на меня», исправление, удаление данных) | LDT Manifesto §11; Vision §18 |

Функция, нарушающая любую строку основной таблицы, не проходит admission
criteria независимо от §8. Условные LDT-строки применяются только если LDT
входит в проверяемый релиз.

## 8.4 Product Thesis Validation Gate — когда тезис считается проверенным

> **Переименовано (v0.5).** Было «MVP Phase Exit Criteria». Раздел
> интегрирован с AYLA-DEC-0018 (Phase 2 and Product Thesis Validation
> Gate, accepted 2026-07-28).

> **v0.6:** evidence этого gate теперь оценивается по representation-neutral
> loop §4.3 (Goal → Signal → Context → Recommendation → Action → Memory →
> Progress), а не по LDT-dependent evidence.

Нормативные рамки AYLA-DEC-0018:

- **Phase 1 release readiness ≠ Product Thesis Validation.** Phase 1
  (session-only vertical slice) — самостоятельный технический release
  gate; его успех подтверждает работоспособность и безопасность сквозного
  сценария, но не продуктовую гипотезу §4.
- **Phase 2 activation ≠ автоматическая Product Thesis Validation.** Само
  наличие персистентной памяти не доказывает её ценность.
- Evidence-классы (functional, user-value, safety/privacy, anti-lock-in) и
  числовые thresholds здесь не дублируются: они зафиксированы в
  AYLA-DEC-0018 и будущем Measurement Framework.

### Thesis Validation — результат пилота

- центральный тезис (§4) прошёл проверку по §8.1/§8.2 на данных пилота,
  причём memory-dependent утверждения — только на Phase 2 evidence
  (AYLA-DEC-0018);
- unit-экономика пилота подтверждена (монетизация §6, Decision Log
  AYLA-DEC-0001/0007/0008/0010) на реальных данных, а не только как модель;
- killer moment (Killer PRD §3) зафиксирован как воспроизводимое, а не
  единичное событие.

### Governance Exit — готовность документации

- открытые блокеры §9 (ADR-0012 OD-1/OD-2 и связанные downstream
  approvals) закрыты или явно вынесены в план следующей фазы.

Thesis Validation описывает, подтверждён ли **продуктовый тезис**;
Governance Exit — готова ли **документация/canon**. Это разные оси, не одна
шкала: тезис может быть подтверждён при незакрытых governance-блокерах (и
наоборот).

**Product Thesis Validation закрывает Product Owner.** Даже при выполнении
критериев по обеим осям переход к следующей стадии (Vision §16 «Стратегия
запуска») — решение Product Owner на основании validation evidence, а не
автоматический триггер.

**Открытый вопрос:** нет утверждённых числовых порогов ни для одного из
пунктов — фиксация чисел принадлежит Measurement Framework (см. §10).

## 9. Dependencies and Blockers

Этот тезис не блокирован сам по себе. Фактическое состояние связанных
документов и решений (на 2026-08-07):

- **Ayla Product Essence v1.2 (candidate)** и **Ayla — Product Vision v2.1
  (candidate)** — parent-документы этого amendment; ожидают Product Owner
  Final Review параллельно с этим документом.
- **Ayla Product Principles v0.2 (candidate)** — sibling-документ,
  амендируется по тому же набору Owner Decisions OD-MVP-1…4; §8.3 этого
  документа ссылается на него.
- **Ayla MVP Scope and Release Contract** — следующий документ в
  canonization sequence; требует обновления релизного состава (Twin out of
  mandatory MVP; Food Intelligence in; Memory Foundation in) после
  канонизации Thesis v0.6.
- **ADR-0012 OD-1/OD-2** — STILL_BLOCKING для соответствующих downstream
  approvals (canonical approval Killer PRD, memory-контракты); сам Product
  Thesis они не блокируют.
- **[[Killer PRD]]** — LEGACY REFERENCE ONLY (CANON_INDEX): используется
  здесь как источник определений (`qualified_action`, killer moment), но
  не является canonical-документом; его approval заблокирован ADR-0012
  OD-1/OD-2.
- **Consent Scope Registry** — существует, approved v1.0 (уточнение §10 по
  AYLA-DEC-0018 — pending Change Control; на этот Thesis не влияет).
- **Data Inventory Matrix** — существует, draft v1.0; зависимость AMD-020
  Pilot Scope Registry от неё разрешена. OD-K11 (`canonical_status` в
  schema) — RESOLVED.
- **[[Ayla MVP User Journey Specification]] v1.2** — Foundation document
  №5; содержит собственный, отдельно принятый набор owner decisions
  (AYLA-DEC-0037…0054, 2026-08-04) и MUST_HAVE-ссылки на MVP Scope §6.4
  Twin-требования, которые устареют после обновления MVP Scope. Alignment
  pass Journey с OD-MVP-1…4 — зарегистрирован как отдельный follow-up gate,
  не выполняется этим документом; не блокирует канонизацию Thesis v0.6.
- **AYLA-DEC-0018** — integrated: Product Thesis Validation Gate
  зафиксирован в §8.4 этого документа.

## 10. Open Questions

### Resolved

- ~~Нужна ли более детальная сегментация клиентской аудитории?~~ —
  **закрыто в v0.2**, см. §5 Client side / Product Vision §13.
- ~~Нужен ли формальный чек-лист для admission criteria (§8)?~~ —
  **закрыто в v0.5: MOVE_TO_MVP_SCOPE** — формализация чек-листа
  принадлежит уровню MVP Scope, а не Thesis.
- ~~Вести ли полный реестр «вне MVP» функций отдельно?~~ — **закрыто в
  v0.5: MOVE_TO_MVP_SCOPE** — исчерпывающие exclusions принадлежат MVP
  Scope; §7 остаётся обзорным.

### Still open

- **Персоны пилота (STILL_OPEN_NON_BLOCKING).** Действуют ли все три
  персоны Vision §13 одинаково для пилота в Пензе, или пилот — валидация
  подмножества? Vision v2.0 закрыл сегменты для продукта в целом; выбор
  пилотного подмножества — рабочее допущение пилота и не блокирует
  канонизацию Thesis.
- **Числовые пороги Success/Failure/Gate (§8.1–8.4)
  (KEEP_NON_BLOCKING).** Design candidates; перенесены в Measurement
  Framework. Согласовано с AYLA-DEC-0018: thresholds решением не
  утверждаются.
- **Термин `Recommendation Trigger Scenario` (KEEP_NON_BLOCKING).**
  Остаётся Open Question: термин не канонизирован ни в Product Vision
  v2.0 (проверено повторно — используется неформальное
  «trigger-сценарий»), ни в Glossary; owner decision по термину не было.

## 11. Risks

При механическом применении составной гипотезы (§4) как автоматического
чек-листа разные участники команды могут по-разному интерпретировать вклад
конкретной функции в элементы гипотезы, что приведёт к расхождению решений
между Product, Engineering и Design. Защита — не преждевременная
формализация чек-листа в этом документе (она делегирована MVP Scope), а
обязательный пересмотр спорных случаев Product Owner до принятия решения
по функции.

**R-T1 — Feature-center regression (добавлено v0.6).** Риск заменить
Twin-first на Food-first как новый самостоятельный центр продукта.
Mitigation: Goal + context + recommendation + action + continuity +
progress остаются продуктовым циклом; Food — только первая реализация
Signal.

**R-T2 — Scope creep (добавлено v0.6).** Риск объявлять каждую полезную
capability обязательной для доказательства Thesis. Mitigation: admission
требует прямого вклада в testable hypothesis (§8).

**R-T3 — Memory overreach (добавлено v0.6).** Риск путать полезный
context с оправданием неограниченной persistence. Mitigation: progressive
memory + policy/consent gate (§8.3; Product Principles v0.2).

**R-T4 — Engagement substitution (добавлено v0.6).** Риск считать DAU,
messages или bookings доказательством user outcome. Mitigation:
progress/return evidence остаётся goal-relative (§8.1 S4).

## Change Log

> Этот журнал отражает историю изменений документа и не является
> нормативной частью спецификации. Нормативным считается текущее состояние
> разделов 1–11, а не записи ниже.

### v0.6 (2026-08-07) — Targeted amendment: representation-neutral MVP hypothesis

Выполнено по `Ayla MVP Product Thesis — Amendment Plan v0.5 → v0.6` на
основании Owner Decisions OD-MVP-1…4 и Product Essence v1.2 (candidate).

- **OD-MVP-1:** Living Digital Twin убран из статуса обязательного элемента
  MVP hypothesis; LDT recognition/identity criteria перенесены в
  LDT-specific validation (условно, только если LDT включён в релиз).
- **OD-MVP-2:** Food Intelligence зафиксирован как первая конкретная
  реализация generic класса `Everyday Signal`, не как вечная thesis-
  зависимость.
- **OD-MVP-3, OD-MVP-4:** составная гипотеза (§4.3) заменена на
  representation-neutral loop `Goal → Signal → Context → Recommendation →
  Action → Memory Continuity → Progress`.
- **§3** — добавлена явная граница: точный feature composition MVP
  принадлежит MVP Scope, не Thesis.
- **§4.1** — каноническая рамка сделана representation-neutral; LDT —
  опциональная capability.
- **§4.2** — добавлено уточнение: LDT усиливает moat, но не обязателен для
  первого доказательства Thesis.
- **§4.3** — MVP hypothesis переформулирована без обязательного LDT;
  добавлен целевой validation loop.
- **§6** — «Living Digital Twin viability» заменена на «Everyday
  Contextual Signal viability»; LDT остаётся опциональным пунктом.
- **§8** — admission principle обновлён под новую составную гипотезу; LDT
  вклад — усиливающий, не обязательный.
- **§8.1** — Success Criteria перегруппированы в S1–S5 (Цель и контекст;
  Рекомендация и действие; Память; Прогресс и возврат; Доверие и
  безопасность); Twin recognition/repeat capture убраны как universal
  success condition.
- **§8.2** — Failure Conditions переписаны без Twin-specific пунктов как
  автоматического опровержения; добавлен условный LDT-specific failure
  блок.
- **§8.3** — MVP Principles: LDT-specific строки сделаны условными;
  добавлены User Outcome First, Contextual Proactivity, Observation ≠ Fact,
  Safety & Wellness Boundary.
- **§8.4** — evidence переориентировано на representation-neutral loop.
- **§9** — актуализированы зависимости: Essence v1.2, Vision v2.1,
  Principles v0.2 (candidates); зафиксирован follow-up gate для User
  Journey v1.2 alignment (не выполняется этим документом).
- **§11** — добавлены риски R-T1…R-T4 (feature-center regression, scope
  creep, memory overreach, engagement substitution).
- **Не изменено:** §1, §2, §5, §7, §10 сохранены без стилистической
  правки; testable thesis structure, Phase 1/2 validation model, killer
  moment, unit economics и Product Owner closure сохранены без изменений.
- **Metadata:** version 0.5 → 0.6; status approved → draft; canonical_status
  approved → candidate (ожидает Product Owner Final Review); updated
  2026-07-30 → 2026-08-07.
- **Next gate:** Product Owner Final Review для Thesis v0.6, затем Product
  Principles v0.2, затем MVP Scope release composition update.

### v0.5 (2026-07-31) — Editorial propagation of AYLA-DEC-0027 channel model

Выполнено в Two-Phase Pilot Scope Reconciliation Window по промпту
`TWO_PHASE_PILOT_COMBINED_EDITORIAL_CLEANUP_PROMPT.md` после cross-document
consistency review (verdict: EDITORIAL_CLEANUP_REQUIRED), finding CD-P3-01.

- **§6** — обзорная строка канала приведена к owner-approved модели
  AYLA-DEC-0027: Mobile App — primary product experience; MAX Mini App и
  MAX Bot — required companion; feature parity — NOT_REQUIRED; shared
  backend/state/consent/safety/analytics — REQUIRED; добавлена ссылка на
  [[Ayla MVP Scope and Release Contract]] §8. AYLA-DEC-0027 уточняет
  AYLA-DEC-0004, не отменяет его.
- **Editorial only:** no scope change, no owner decision, no version bump,
  no canonical status change; thesis claims не изменены.

### v0.5 (2026-07-30) — Structured revision for current product canon

Выполнено в Product Thesis Canon Window по результатам Alignment and Gap
Analysis (P0=2, P1=7, P2=7, P3=4) и Structured Revision Plan. Основание:
Ayla Product Essence v1.1 (CANONICAL), Ayla Living Digital Twin Manifesto
v1.0 (CANONICAL), Ayla Product Vision v2.0 (CANONICAL), AYLA-DEC-0018,
AYLA-DEC-0026.

- **§1–§3** — зафиксирована каноническая иерархия: Foundation document №2;
  родительский источник — Essence v1.1; Manifesto v1.0 — согласующий
  input, не родитель. Scope дополнен проверяемой гипотезой и Validation
  Gate; non-goals — Vision, релизный состав, UX, архитектура, AI/ML,
  Measurement Framework.
- **§4 реформулирован** в составную проверяемую гипотезу: Transformation
  Goal + Living Digital Twin viability + Ayla orchestration + memory as
  continuity + visible progress + real next actions. Цитата AYLA-DEC-0002
  сохранена дословно; добавлено нормативное пояснение: память — не
  единственный центр продукта, moat — составной (Vision §17).
  Memory-first снят с позиции центра, память сохранена как continuity.
- **§5** — исправлены ссылки на Product Vision: раздел персон (§13) и
  wikilink (фактический title документа).
- **§6** — добавлены обзорные thesis-level пункты: Transformation Goal,
  Twin viability (качественно, Essence §18), memory as continuity,
  оркестрация Ayla, booking как downstream-действие. Действующие решения
  (канал, монетизация, оплата) сохранены.
- **§7, §8** — memory-only фильтр заменён составным admission-тестом по
  элементам гипотезы; формальный чек-лист делегирован MVP Scope.
- **§8.1/§8.2** — добавлены качественные сигналы: формулирование и
  удержание цели, recognition Twin, возврат к фиксации прогресса, сигнал
  «это не похоже на меня», identity drift. Memory-dependent claims
  привязаны к Phase 2 evidence (AYLA-DEC-0018). Числа не вводятся.
- **§8.3** — добавлены строки: разделение факт/реконструкция/оценка/
  прогноз/цель, recognition и identity preservation, body dignity,
  anti-shaming, контроль пользователя над Twin; исправлена ссылка на
  Vision (§3.1).
- **§8.4 переименован** в «Product Thesis Validation Gate» и интегрирован
  с AYLA-DEC-0018: Phase 1 release readiness ≠ validation; Phase 2
  activation ≠ автоматическая validation; validation закрывает Product
  Owner. Ось Governance Exit сохранена. Ссылка на стратегию запуска Vision
  исправлена (§16).
- **§9** — актуализированы статусы: Consent Scope Registry (exists,
  approved v1.0), Data Inventory Matrix (exists, draft v1.0), OD-K11
  (resolved), Killer PRD (legacy reference only), MVP User Journey
  (Foundation document №5, pending alignment), AYLA-DEC-0018 (integrated).
- **§10** — вопросы о чек-листе и реестре «вне MVP» переведены в MVP
  Scope; остальным присвоены явные вердикты.
- **§11** — риск переформулирован: не интерпретация memory-only тезиса, а
  механическое применение составной гипотезы как автоматического
  чек-листа.
- **Metadata** — version 0.4 → 0.5; добавлен `canonical_status:
  candidate`; owner → Product Owner; `depends_on` приведён к Essence /
  Vision / Manifesto / Constitution / Decision Log; `related`
  актуализирован (MVP User Journey Specification); устранён unresolved
  wikilink на Product Vision.

### v0.4 (2026-07-27) — Финальная терминологическая полировка

- **§5** заголовок смягчён: «Pilot (Пенза, 2026-08-15)» →
  «Pilot Scope (Пенза; дата — AYLA-DEC-0003)» — дата вынесена в ссылку на
  решение, чтобы перенос пилота не делал заголовок документа формально
  устаревшим.
- **§8.4** переименован в «MVP Phase Exit Criteria» (было «MVP Exit
  Criteria») — точнее отражает, что это критерии завершения фазы, не выхода
  из продукта.
- **§9** переупорядочен по уровню: сначала Journey (стратегический
  документ), затем Killer PRD, затем AMD-020 (governance/implementation).
- **§10** — пункт про `Recommendation Trigger Scenario` **не понижен** до
  «Documentation follow-up», как предлагалось: проверил Ayla Product Vision
  побайтово — термин там не канонизирован, только зафиксирован как та же
  открытая рекомендация. Пункт остался Open Question с уточнением.
- Добавлен дисклеймер перед Change Log: журнал не нормативен, нормативно
  текущее состояние §1–11.

### v0.3 (2026-07-27) — Редакционные улучшения перед канонизацией

- **§4** — добавлено пояснение о прогнозном характере «12–18 месяцев» без
  изменения дословной цитаты AYLA-DEC-0002.
- **§8** переименован из «Go/No-Go Criteria» в «MVP Feature Admission
  Criteria» — Go/No-Go обычно про запуск продукта целиком, не про admission
  отдельной функции.
- **§8.1** — добавлено пояснение, почему тезис подтверждается только
  совокупностью признаков, а не любым одним показателем.
- **§8.4** разделён на **Product Exit** (результат пилота: тезис,
  unit-экономика, killer moment) и **Governance Exit** (готовность
  документации: блокеры §9) — это разные оси, не одна шкала. Добавлена явная
  строка: даже при выполнении критериев решение о переходе остаётся за
  Product Owner, переход не автоматический.
- **§10** разделён на Resolved / Still open.
- **§11** — формулировка риска расширена: описан сам риск (расхождение
  решений между Product/Engineering/Design), а не только факт возможных
  разночтений.

### v0.2 (2026-07-27) — Success/Failure/Principles/Exit Criteria

- **§4** усилен: краткая формулировка AYLA-DEC-0002 сохранена дословно,
  добавлена развёрнутая проверяемая гипотеза (if-then форма) без замены
  исходного решения.
- **§5** обновлён: клиентские сегменты закрыты ссылкой на Product Vision
  (персоны); открытый вопрос сужен до применимости персон к пилоту в Пензе.
- **Добавлены §8.1–8.4:** Success Criteria, Failure Conditions, MVP
  Principles (явная привязка к статьям Конституции VII/X/IV/I, не новый
  список), MVP Exit Criteria. Все количественные пороги оставлены design
  candidates по паттерну ADR-0012 OD-5/OD-6 — не выданы за решения.
- Обновлён §10 Open Questions: один вопрос закрыт, добавлены новые из §8.1–8.4
  и из ревью Product Vision (термин `Recommendation Trigger Scenario`).
- `depends_on` дополнен ссылкой на Product Vision.

### v0.1 (2026-07-27) — Initial materialization

- Документ впервые материализован; ранее существовал только как
  `planned`/`blocked` ссылка в Ayla Glossary и Ayla User Journey
  Specification.
- Разграничение с Killer PRD и Journey Specification согласовано с
  владельцем: Product Thesis — MVP scope, сегменты, go/no-go; Killer PRD —
  killer-сценарий и атрибуция; Journey — пользовательский путь.
- Target Segments (§5), MVP Scope in/out (§6–7) и go/no-go принцип (§8)
  зафиксированы по прямому решению владельца (2026-07-27).
