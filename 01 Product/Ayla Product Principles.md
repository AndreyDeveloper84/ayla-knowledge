---
node_id: ayla.product.product-principles
title: Ayla Product Principles
type: foundation
status: draft
canonical_status: candidate
version: "0.2"
owner: Product Owner
priority: P0
knowledge_area:
  - product
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
created: 2026-07-31
updated: 2026-08-07
review_cycle: before-major-change
depends_on:
  - "[[Ayla Product Essence]]"
  - "[[Ayla Living Digital Twin Manifesto]]"
  - "[[Ayla — Product Vision]]"
  - "[[Ayla MVP Product Thesis]]"
  - "[[Ayla Constitution]]"
  - "[[Ayla Decision Log]]"
implements:
  - "[[Ayla Constitution]]"
related:
  - "[[Ayla Glossary]]"
  - "[[Ayla MVP User Journey Specification]]"
supersedes: []
open_schema_question: >
  Тип `product-principles` не зарегистрирован в `.knowledge/schema.yaml`;
  использован `foundation` по действующему precedent. Рассмотреть явное
  добавление типа при следующем amendment схемы.
---

# Ayla Product Principles v0.2

**Статус:** DRAFT / canonical candidate — targeted amendment, ожидает
Product Owner Final Review
**Версия:** 0.2
**Положение:** Foundation document №3 (Vision → Thesis → **Principles** →
MVP Scope → User Journey)
**Владелец:** Product Owner
**Основание:** Owner Decisions OD-MVP-1…4; `Ayla Product Principles —
Amendment Plan v0.1 → v0.2`; Ayla Product Essence v1.2 (candidate), Ayla
Living Digital Twin Manifesto v1.0, Ayla — Product Vision v2.1 (candidate),
Ayla MVP Product Thesis v0.6 (candidate)

> Документ находится ниже Ayla Product Essence v1.2 и не может её
> переопределять. Он не переопределяет Product Vision v2.1 и Product Thesis
> v0.6. Living Digital Twin Manifesto v1.0 — sibling-документ и обязательный
> согласующий input для положений о Living Digital Twin, не родитель этого
> документа. Ayla Constitution — hard constraint и conditional reference,
> не шаблон этого документа. Это targeted amendment v0.1 → v0.2: сохранён
> governance-skeleton v0.1 (Purpose, Position in Canon, Non-goals,
> Relationship to Canonical Sources); изменены нормы, затронутые
> OD-MVP-1…4. См. Change Log.

## 1. Purpose

Этот документ фиксирует **стабильные продуктовые правила принятия решений**
Ayla: нормы, которые неизменны на горизонте MVP и последующих стадий.

В канонической последовательности Foundation-документов Principles отвечают
на вопрос **«какие нормы неизменны»**: Vision отвечает, куда идёт продукт;
Thesis — почему этот продукт должен существовать и победить; MVP Scope —
что входит в первый релиз; User Journey — как человек проходит ключевые
сценарии.

Principles применяются между Vision/Thesis и MVP Scope: они нормируют то,
что Vision объявил направлением, а Thesis — проверяемой гипотезой, и задают
границы, внутри которых MVP Scope выбирает релизный состав.

> **Граница (v0.2):** Product Principles определяют устойчивые правила
> принятия продуктовых решений, но не конкретный feature composition
> отдельного релиза. Какая функция входит в конкретный MVP — решение MVP
> Scope and Release Contract, не этого документа.

Документ не повторяет Constitution, Manifesto, Vision или Thesis. Он
переводит их положения в продуктовые эвристики и ссылается на источники
вместо пересказа.

## 2. Position in Canon

```text
Ayla Constitution — hard constraints / side anchor
Ayla Product Essence — highest product source
├── LDT Manifesto — sibling / aligning input
├── Product Vision — sibling
├── Product Thesis — sibling
└── Product Principles — sibling
      ↓
MVP Scope → User Journey → Domain → UX → Engineering
```

- **Ayla Product Essence v1.2** — высший продуктовый источник; при любом
  конфликте побеждает Essence.
- **LDT Manifesto v1.0** — sibling-документ под Essence и обязательный
  согласующий input для LDT-положений этого документа; Manifesto не является
  родителем Product Principles. LDT-specific нормы Manifesto не становятся
  автоматически mandatory requirements первого MVP (OD-MVP-1).
- **Product Vision v2.1** и **Product Thesis v0.6** — sibling-документы;
  Product Principles находится ниже Essence и не переопределяет Vision
  или Thesis.
- **Ayla Constitution v2.2** — hard constraint и боковой якорь: её статьи
  не переписываются здесь, а учитываются как conditional reference.
- Этот документ не создаёт новую иерархию: он фиксирует существующую
  sibling-структуру, заданную Essence §21.

## 3. How to Use These Principles

Принципы применяются:

- при продуктовой и дизайн-приоритизации;
- при продуктовых спорах между участниками команды;
- при оценке любого нового решения, функции или изменения сценария.

Принципы — **эвристики, а не автоматический feature checklist**. Они не
заменяют суждение Product Owner: механическое применение принципов как
бинарного фильтра без контекста — известный риск (Thesis §11), и спорные
случаи разбираются с участием Product Owner.

**Hard Precedence Layer (v0.2).** Для конфликтов, затрагивающих safety,
autonomy, user outcome или commercial interest, действует ограниченный
обязательный порядок:

```text
1. Safety / legal hard constraints
2. User autonomy and consent
3. Expected user outcome
4. Engagement optimization
5. Commercial optimization
```

После применения этого порядка остальные продуктовые эвристики остаются
contextual и могут требовать owner judgment.

Если конфликт между принципами не разрешается Hard Precedence Layer или
направлениями раздела 6, он делается явным и эскалируется по лестнице
разрешения (CANON_CONFLICT_REGISTER); Owner Decision создаётся только при
materially unresolved выборе.

Гипотеза не выдаётся за решение: положения, не подтверждённые canonical
источниками, не включаются в принципы и не применяются как нормы.

## 4. Core Product Principles

> **Изменено (v0.2, OD-MVP-1…4).** Набор принципов расширен с 11 до 14 и
> реорганизован. Identity Continuity (было 4.4) перестала быть отдельным
> universal core principle и стала условной нормой внутри 4.3 (применяется
> только если используется persistent personal representation, включая
> LDT). Добавлены Contextual Proactivity, Safety & Wellness Boundary, User
> Outcome First и Product Restraint / Release Discipline. См. таблицу
> mapping v0.1 → v0.2 в Change Log.

### 4.1 Human First

**Норматив:** Главный герой продукта — человек: его состояние, его цель,
его изменения. Каждое продуктовое решение усиливает ощущение «это мой путь,
моя цель и мои изменения». Living Digital Twin, Ayla, память и запись —
не герои продукта: Twin — отражение человека, Ayla — его помощник, план —
его путь, прогресс — его результат.

**Почему:** Смещение фокуса с человека на технологию или транзакцию разрушает
саму ценность продукта; этот принцип первичен по отношению ко всем остальным.

**Decision test:**
- Усиливает ли решение ощущение «мой путь, моя цель, мои изменения»?
- Не смещает ли оно фокус с человека на Twin, Ayla или отдельную функцию?

**Anti-pattern:**
- Twin как самоценный объект вместо отражения человека;
- AI как герой продукта вместо помощника;
- метрика отдельной функции важнее пути человека;
- каталог функций, объединённых AI-обёрткой.

**Canonical sources:** Essence §4; Manifesto §2; Vision §9; AYLA-DEC-0026
(разделение центров).

### 4.2 Goal at the Center

**Норматив:** Transformation Goal — центральная доменная сущность, вокруг
которой строится весь продуктовый путь. Цель принадлежит человеку: Ayla
помогает её сформулировать, но никогда не навязывает. Цель — не KPI,
не внешний идеал и не прогноз. Питание, вода, сон, фитнес, процедуры,
специалисты и запись — инструменты пути к цели, а не самостоятельные центры
продукта.

> **Пользователь определяет цель (v0.2).** Ayla может помочь прояснить
> цель, но не должна незаметно подменять её собственным определением
> успеха: `User-defined Goal → Allowed Signals → Context → Progress
> interpretation`.

**Почему:** Единый центр домена защищает продукт от распада на набор
несвязанных трекеров и от навязывания человеку чужих целей.

**Decision test:**
- Связывает ли решение действие пользователя с его Transformation Goal?
- Не превращает ли оно отдельный инструмент в самостоятельный центр продукта?

**Anti-pattern:**
- набор несвязанных трекеров без общей цели;
- цель, навязанная Ayla вместо цели человека;
- цель как числовое обещание или KPI;
- функция, живущая ради самой себя, а не ради цели.

**Canonical sources:** Essence §1, §20; Vision §6; Thesis §4.1.

### 4.3 Visible & Understandable Path

> **Изменено существенно (v0.2, OD-MVP-1).** Было «The Path Is Visible» с
> обязательной привязкой к Living Digital Twin. Identity Continuity (было
> отдельным принципом 4.4) свёрнута в условную норму внутри этого принципа.

**Норматив:** В ключевых пользовательских сценариях человек должен понимать
своё текущее состояние, цель, значимые изменения и движение к цели. Living
Digital Twin может быть одним из способов представления пути, но не
является обязательным механизмом первого MVP или каждого этапа продукта.
Карточки, списки, чат, timelines и графики — равноправные representation
layers там, где Twin не используется.

**Условная норма — Identity Continuity.** Если используется persistent
personal representation, включая Living Digital Twin, она должна сохранять
узнаваемую идентичность пользователя между версиями и состояниями. Identity
drift — недопустимый класс дефекта независимо от визуального качества
результата. Эта норма действует полностью, когда такая representation
используется; она не создаёт universal MVP-требование там, где она не
используется.

**Почему:** Видимый и понятный путь — ключевое отличие Ayla; человеку
недостаточно строк в трекере, он должен понимать движение к цели. Там, где
используется узнаваемая persistent representation, потеря идентичности
незаметно разрушает доверие ко всей линии пути.

**Decision test:**
- Понимает ли пользователь своё положение относительно цели и значимые
  изменения?
- Честно ли representation разделяет факт, оценку и прогноз?
- Если используется LDT или другая persistent representation — узнаёт ли
  пользователь себя в ней и сохраняется ли идентичность между версиями?
- Не зависит ли ценность искусственно от одной representation technology?

**Anti-pattern:**
- LDT как обязательный gateway к пользовательской ценности;
- красивое, но чужое изображение вместо узнаваемого — там, где
  representation используется;
- «улучшение» образа ценой узнаваемости;
- обязательный Twin на каждом экране, включая служебные.

**Canonical sources:** AYLA-DEC-0026; OD-MVP-1; Essence §7, §9, §12, §18;
Manifesto §3, §5, §6; Vision §5, §8.4.

### 4.4 Honest Representation

> **Расширено (v0.2).** Добавлены явные инварианты Observation ≠ Confirmed
> Fact и AI Inference ≠ User Fact, включая food-specific правило.

**Норматив:** Ayla никогда не выдаёт один класс достоверности за другой:
реконструкцию — за факт, оценку — за измерение, прогноз — за наблюдение,
желаемую цель — за вероятный результат. Прогноз не является обещанием;
цель не равна прогнозу. Неопределённость обозначается честно; ложная
точность — видимость точности, которой у продукта нет, — недопустима.

**Hard invariants (v0.2):**

> Observation ≠ Confirmed Fact.
> AI Inference ≠ User Fact.

Для everyday-сигналов, включая Food Intelligence: распознавание еды или
поведения — observation/model output и не становится автоматически
подтверждённым или медицинским фактом.

**Почему:** Доверие к пути строится на честности представления: одна
подмена класса достоверности обесценивает всё, что продукт показывает
человеку.

**Decision test:**
- Понятно ли пользователю, что зафиксировано, что реконструировано, что
  оценено, что спрогнозировано и что является целью?
- Не создаётся ли видимость точности, которой у продукта нет?
- Не выдаётся ли observation за подтверждённый факт?

**Anti-pattern:**
- прогноз, поданный как обещание («вот что с вами будет»);
- корреляция, выданная за причинность;
- числовая уверенность без поддержки модели (deceptive precision);
- реконструкция или оценка, поданная как измеренный факт;
- распознанный food-сигнал, поданный как подтверждённый или медицинский
  факт.

**Canonical sources:** Essence §7, §8, §14; Manifesto §7, §9, §10;
Constitution Ст. II, Ст. XI; OD-MVP-2, OD-MVP-3.

### 4.5 Progressive Memory + User Control

> **Переименовано и расширено (v0.2, OD-MVP-3).** Было «Memory as
> Continuity». Добавлен явный progressive lifecycle и права пользователя.

**Норматив:** Ayla сохраняет разрешённый пользователем контекст, чтобы путь
не начинался каждый раз с нуля. Память — механизм continuity и
персонализации, а не центр продукта и не самоцель: больше сохранённых
фактов не означает лучшее понимание человека.

Memory Foundation входит в MVP с начала и следует progressive lifecycle:

```text
Current Interaction
        ↓
Working Context
        ↓
Useful Memory Candidate
        ↓
Policy / Consent Gate
        ↓
Persistent Memory
```

**Invariants:**

- session context не автоматически становится persistent memory;
- observation не автоматически становится confirmed fact (см. 4.4);
- AI inference не автоматически становится user fact (см. 4.4);
- persistent memory проходит policy/consent gate;
- sensitive information имеет более строгий режим.

**Права пользователя:** **See** — понимать, что помнит Ayla; **Correct** —
исправить неточную память; **Forget** — удалить конкретную память;
**Disable** — ограничить или отключить persistent memory.

Если память материально влияет на рекомендацию, Ayla должна уметь объяснить
релевантный remembered context в понятных пользователю терминах.

**Почему:** Накопленное понимание пользователя — защищаемое преимущество
Ayla, но оно работает только как continuity внутри составного пути,
а не как самостоятельный центр.

**Decision test:**
- Избавляет ли решение пользователя от необходимости объяснять дважды?
- Усиливает ли память качество пути, а не только объём данных?
- Проходит ли persistent-запись policy/consent gate?

**Anti-pattern:**
- сбор данных «на будущее» без понятной цели;
- количество сохранённых фактов как цель оптимизации;
- память как единственный центр продукта (memory-first);
- новый разговор, ничего не знающий о прошлом пути;
- persistent запись без прохождения consent gate.

**Canonical sources:** Vision §1, §4.2, §8.1; Thesis §4.3, §6, §8.2;
Essence §13; Constitution Ст. VI, Ст. IX (reference); OD-MVP-3.

### 4.6 Explainability & User Agency

> **Переименовано и усилено (v0.2).** Было «Explainable Next Step».

**Норматив:** Каждая значимая рекомендация объяснима — пользователь понимает,
что предлагается, почему, на каких данных и с какой неопределённостью, — и
ведёт к реалистичному следующему шагу. Уместность прежде действия: «ничего
не делать» тоже может быть корректной рекомендацией. Ayla оркестрирует путь
целиком, а не выдаёт разрозненные советы.

Ayla может иметь точку зрения и рекомендовать primary next step, но
финальное решение всегда остаётся за пользователем. Альтернативы доступны
по запросу, после отказа, при недоступности primary варианта или при
близкой релевантности нескольких вариантов. Отказ пользователя — сигнал, не
провал: Ayla не оказывает давление и не навязывает одно и то же действие
повторно.

**Почему:** Объяснимость превращает рекомендацию из чёрного ящика в шаг,
которому можно доверять, а уместность защищает пользователя от действий
ради действий.

**Decision test:**
- Понятно ли пользователю, почему это предложено и что делать дальше?
- Уместно ли предложение сейчас — или лучше ничего не предлагать?
- Остаётся ли финальное решение за пользователем?

**Anti-pattern:**
- рекомендация без объяснимой причины;
- действие ради действия или ради активности;
- скрытая коммерческая мотивация шага;
- поток дисклеймеров на каждую несущественную мелочь;
- давление или повторное навязывание отклонённой рекомендации.

**Short form:** Recommend, explain, never coerce.

**Canonical sources:** Essence §14 (Explainable Transformation);
Constitution Ст. VII, Ст. X; Vision §11, §19; Manifesto §10; Thesis §4.1.

### 4.7 Booking Is Downstream

**Норматив:** Запись к специалисту — одно из downstream-действий
персонального плана, а не центр продукта и не цель оптимизации. Рекомендация
важнее транзакции: успех сценария измеряется пользой для пути человека,
а не фактом записи.

**Почему:** Возврат к booking-first превратил бы Ayla обратно в маркетплейс
услуг и разрушил бы составное преимущество продукта.

**Decision test:**
- Оценивается ли успех сценария пользой для пути, а не фактом записи?
- Не подталкивает ли решение к записи в ущерб уместности?

**Anti-pattern:**
- каталог услуг с AI-обёрткой;
- конверсия в запись как главная метрика продукта;
- запись как дефолтный исход любой рекомендации.

**Canonical sources:** Essence §13, §20; Vision §1, §8.3; Thesis §4.1, §6;
Constitution Ст. I, Термины (Expected User Success).

### 4.8 User in Control

> **Обобщено (v0.2).** Контроль расширен с данных/Twin на memory,
> personalization и proactive behavior.

**Норматив:** Контроль над данными, memory, personalization, proactive
behavior и personal representations (включая Twin, где он используется)
остаётся у пользователя: он может сообщить «это не похоже на меня» (если
используется persistent representation), исправить или перестроить её,
удалить исходные и производные данные, отозвать согласие и отказаться от
конкретных входных данных без скрытых санкций. Последствия отказа
объясняются заранее и честно. Согласие и ограничение целей использования
данных действуют по правилам Constitution и Manifesto — здесь они не
переписываются.

**Почему:** Доверие — условие всего цикла продукта: человек открывает
контекст только тому, кем может управлять.

**Decision test:**
- Может ли пользователь отказаться, исправить и удалить — и понимает ли
  последствия заранее?
- Контролирует ли пользователь memory, personalization и proactive
  behavior, а не только исходные данные?

**Anti-pattern:**
- отказ от данных блокирует несвязанную функциональность;
- тихое расширение scope использования данных без нового разрешения;
- удаление, которое выглядит удалением, но продолжает влиять на
  рекомендации;
- proactive поведение или персонализация без возможности отключить.

**Canonical sources:** Manifesto §11; Essence §15; Vision §18;
Constitution Ст. VII, Ст. IX, Ст. XIV (reference); Manifesto §12 (reference).

### 4.9 Goal-Relative Progress Without Pressure

> **Расширено (v0.2).** Добавлено явное определение progress относительно
> user-defined goal и запрет универсальных допущений.

**Норматив:** Ayla поддерживает человека без стыда, вины, страха и FOMO.
Продукт не навязывает универсальный идеал: внешность, вес и состояние не
определяют ценность человека, пауза — не моральный провал, и не существует
единого стандарта, к которому Ayla подталкивает всех.

Progress оценивается относительно собственной цели пользователя, а не
универсального счёта, придуманного Ayla:

> User-defined goal → allowed signals → understandable progress.

Ayla не должна автоматически считать progress: снижение веса; рост
количества booking; рост активности; рост использования продукта — сами по
себе. Ayla может помочь уточнить размытую цель, но не должна незаметно
подменить её собственным критерием успеха.

**Почему:** Продукт работает с телом и внешностью — зоной максимального
риска вреда от мотивационных механик; давление разрушает и доверие, и путь.
Универсальные метрики прогресса подменяют цель пользователя целью продукта.

**Decision test:**
- Использует ли механика стыд, вину, страх или навязанный идеал?
- Наказывает ли продукт за паузу или нелинейный прогресс?
- Определён ли progress относительно собственной цели пользователя, а не
  универсальной метрики?

**Anti-pattern:**
- шейминг-нотификации и «догоняй»;
- прогноз, использованный для запугивания;
- рейтинг или оценка привлекательности;
- идеализированная целевая внешность «как у всех»;
- количество bookings/activity/usage, выданное за progress по умолчанию.

**Canonical sources:** Manifesto §13; Essence §5, §14, §16; Vision §18;
Constitution Ст. VIII, Ст. XI (reference); OD-MVP-4.

### 4.10 Economic Neutrality & Trust

> **Переименовано и усилено (v0.2).** Было «Value on Both Sides, Neutral by
> Default». Добавлен явный ranking invariant.

**Норматив:** Ayla создаёт ценность и клиенту, и провайдеру, но главный
пользователь — клиент: при конфликте интересов приоритет у человека и его
пути. Коммерческий статус, тариф или платёж провайдера никогда не влияют на
персональные рекомендации — экономическая нейтральность не торгуется
(Constitution Ст. IV — здесь не переписывается).

**Ranking invariant:**

> Organic relevance ≠ commercial value.

Комиссия, тариф провайдера, промо-бюджет, расходы на рекламу, платформенная
маржа и ценность коммерческого партнёрства не могут скрыто повышать organic
ranking. Paid placement допустим только как отдельная, явно маркированная
поверхность и не может маскироваться под личную рекомендацию Ayla. При
равнозначных вариантах допустимы нейтральные tie-breakers: доступность,
расстояние, цена для пользователя, предпочтения, качество/надёжность,
вероятность выполнения действия.

**Почему:** Двусторонняя модель работает только пока клиент доверяет
рекомендациям; один скрытый коммерческий приоритет обесценивает доверие
обеих сторон.

**Decision test:**
- Свободно ли решение от скрытого коммерческого приоритета?
- Не выигрывает ли supply-сторона в ущерб клиенту?
- Отделено ли paid placement от organic-рекомендации явной маркировкой?

**Anti-pattern:**
- платное ранжирование или реклама под видом независимого совета;
- рекомендация, оптимизированная на тарифицируемое действие;
- продуктовые решения в интересах провайдера в ущерб клиенту;
- скрытый commercial tie-breaking там, где заявлены нейтральные критерии.

**Canonical sources:** Constitution Преамбула, Ст. III, Ст. IV (reference);
Vision §13, §14; Thesis §8.3.

### 4.11 Contextual Proactivity

> **Добавлено (v0.2, ADD CORE PRINCIPLE).** Поднято из trade-off (было в
> §6 Tensions v0.1) в самостоятельный core principle.

**Норматив:** Ayla может действовать проактивно только тогда, когда есть
meaningful, explainable и goal-relevant сигнал. Ayla не конкурирует за
внимание пользователя и не считает частоту сообщений, push-уведомлений или
DAU самоцелью.

```text
Signal
  ↓
Observation
  ↓
Recommendation Candidate
  ↓
Relevance / Timing / Safety Gate
  ↓
Optional Proactive Interaction
```

Не каждое observation становится recommendation. Не каждая recommendation
становится notification. Пользователь сохраняет контроль над proactive
поведением; при сомнении предпочтительна тишина.

**Short form:** Useful when needed, quiet when not.

**Почему:** Полезность сигнала сама по себе не даёт Ayla безусловного права
прерывать пользователя; надоедливая проактивность разрушает доверие быстрее,
чем отсутствие функции.

**Decision test:**
- Есть ли meaningful, explainable и goal-relevant сигнал для этого
  прерывания?
- Не оптимизируется ли решение на частоту взаимодействия?

**Anti-pattern:**
- уведомление без meaningful сигнала;
- рост DAU/частоты сообщений как самостоятельная цель;
- проактивность, которую нельзя отключить;
- прерывание пользователя «на всякий случай».

**Canonical sources:** OD-MVP-3; Thesis §8.3; Essence §14.

### 4.12 Safety & Wellness Boundary

> **Добавлено (v0.2, ADD CORE PRINCIPLE, OD-MVP-2).**

**Норматив:** Ayla — wellness-продукт, а не медицинская диагностическая
система. Ayla может помогать понимать повседневные паттерны: питание,
гидратация, сон, активность, восстановление, beauty/wellness-рутины,
привычки, немедицинский self-care.

Ayla не должна: диагностировать заболевания; выводить болезни из обычных
поведенческих сигналов; выдавать wellness-наблюдение за медицинский факт;
заменять профессиональную медицинскую помощь; превращать неопределённый
вывод модели в устойчивую медицинскую истину.

**Hard invariants:**

> Food observation ≠ medical fact.
> Inference ≠ diagnosis.

**Почему:** Продукт работает в зоне повышенного риска вреда (тело, питание,
здоровье); нарушение этой границы недопустимо независимо от полезности
функции.

**Decision test:**
- Остаётся ли рекомендация в границах wellness, а не медицинского вывода?
- Не выдаётся ли inference за диагноз?

**Anti-pattern:**
- медицинский диагноз или вывод о заболевании из food/behavioral сигналов;
- замена профессиональной медицинской помощи;
- презентация uncertain inference как устойчивого медицинского факта.

**Canonical sources:** Constitution Ст. X, Ст. XII; OD-MVP-2; Essence §16.

### 4.13 User Outcome First

> **Добавлено (v0.2, ADD CORE PRINCIPLE).**

**Норматив:** Ayla оптимизирует прогресс к цели пользователя, а не
engagement, число booking, время в продукте или revenue от конкретной
рекомендации. Корректной рекомендацией может быть отдых, изменение
привычки, бесплатное действие или отсутствие действия.

**Hard rule:**

> Commercial or engagement optimization must never override safety,
> autonomy or expected user benefit.

**Почему:** Метрики engagement и revenue — бизнес-метрики; они не являются
заменой пользовательской ценности.

**Decision test:**
- Оптимизировано ли решение на пользу пользователю, а не на engagement или
  revenue?
- Допускает ли решение честно рекомендовать «ничего не делать» или
  бесплатное действие?

**Anti-pattern:**
- рекомендация, выбранная из-за revenue, а не из-за пользы;
- метрика engagement, используемая как proxy пользовательской ценности.

**Canonical sources:** OD-MVP-4; Thesis §4.3; Essence §14.

### 4.14 Product Restraint / Release Discipline

> **Добавлено (v0.2, ADD GOVERNANCE PRINCIPLE).**

**Норматив:** Функция должна создавать явную пользовательскую ценность
сейчас или материально улучшать способность Ayla помогать позже — иначе она
не принадлежит текущему product scope. После фиксации release scope новая
функциональность входит только если закрывает подтверждённый critical-path,
safety или release blocker.

**Decision questions:**
1. Какую user problem решает capability?
2. Как она улучшает движение к цели?
3. Почему она нужна именно сейчас?

Конкретные решения вида «Food Scanner — in» или «Twin — out MVP» не
фиксируются здесь: это решения MVP Scope and Release Contract, принятые на
основании Owner Decisions (см. §7 Non-goals).

**Почему:** Без явной дисциплины release scope продукт накапливает функции
без проверенной пользовательской ценности, что разрушает фокус MVP.

**Decision test:**
- Отвечает ли предложение на три decision questions?
- Закрывает ли изменение подтверждённый critical-path/safety/release
  blocker, если release scope уже зафиксирован?

**Anti-pattern:**
- функция, добавленная «на будущее» без текущей пользовательской пользы;
- расширение зафиксированного release scope без owner decision.

**Canonical sources:** OD-MVP-1…4; Thesis §8, §11.

## 5. Decision Test

> **Пересобрано (v0.2, REBUILD).** Вопрос про Twin/identity стал условным
> (п. 3); добавлены вопросы про safety/wellness boundary, memory,
> proactivity и release scope; снят universal-вопрос про Twin как
> обязательный центр.

При оценке любого продуктового решения команда спрашивает (вопросы
применяются с контекстом, а не как бинарная автоматика):

1. Помогает ли решение двигаться к self-defined goal? — Essence §22;
   Principle 4.2
2. Сохраняет ли оно user agency? — Principle 4.6, 4.8
3. Находится ли решение внутри Safety & Wellness Boundary? — Principle 4.12
4. Используется ли memory корректно и прозрачно (progressive lifecycle,
   consent)? — Principle 4.5
5. Объяснима ли значимая рекомендация? — Principle 4.6; Constitution Ст. VII
6. Свободен ли organic ranking от скрытого коммерческого влияния? —
   Principle 4.10; Constitution Ст. IV
7. Основана ли проактивность на meaningful сигнале и уместном timing? —
   Principle 4.11
8. Показывается ли progress относительно цели пользователя? — Principle 4.9
9. Создаёт ли решение ценность сейчас или материально улучшает будущую
   помощь? — Principle 4.13, 4.14
10. Принадлежит ли изменение текущему release scope? — Principle 4.14

Если используется Living Digital Twin или другая persistent personal
representation, дополнительно: узнаёт ли пользователь себя и сохраняется ли
идентичность между версиями (Principle 4.3)?

№10 — governance/admission-вопрос, а не вечная характеристика продукта.

## 6. Tensions and Trade-offs

> **Изменено (v0.2).** Proactive help vs relevance больше не trade-off:
> Contextual Proactivity (4.11) стала core principle. Twin fidelity vs user
> effort сделан условным. Conflict model дополнена Hard Precedence Layer
> (§3).

Для конфликтов, не покрытых Hard Precedence Layer (§3), типовые trade-offs
разрешаются направлением по умолчанию; если направление не разрешает
конкретный случай, конфликт делается явным и эскалируется.

- **Personalization vs minimization.** Глубокая персонализация требует
  данных, но сбор «на будущее» запрещён. По умолчанию — минимизация:
  запрашивается только то, что нужно для понятной пользователю цели.
  — Constitution Ст. VI; Principle 4.5
- **Representation fidelity vs user effort.** Там, где используется
  persistent representation (включая LDT), её качество растёт от данных, но
  фиксация не должна становиться обязанностью. По умолчанию — управляемая
  фиксация без принуждения. — Essence §18; Principles 4.3, 4.8
- **Business value vs neutrality.** Коммерческие интересы платформы не
  должны искажать рекомендации. По умолчанию — нейтральность не торгуется.
  — Constitution Ст. IV; Principle 4.10
- **Progress visibility vs dignity.** Показ прогресса не должен превращаться
  в оценку человека. По умолчанию — при конфликте побеждает dignity.
  — Manifesto §13; Principle 4.9

Лёгкая conflict model:

```text
Constitution / safety / legal — non-negotiable
Product Essence — highest product source
Canonical siblings — alignment required
Hard Precedence Layer (§3) — safety > autonomy > outcome > engagement > commercial
Product Principles — heuristics
Unresolved trade-offs — explicit + escalated
```

Эскалация Product Owner обязательна, если trade-off меняет центр продукта,
MVP, критический пользовательский journey, обязательства privacy/safety,
канонический контракт или не разрешается существующей лестницей разрешения.

## 7. Non-goals

- Не Constitution — не дублирует и не заменяет hard governance и safety
  constraints.
- Не Manifesto — не дублирует философию и границы Living Digital Twin.
- Не Product Vision — не задаёт долгосрочное направление.
- Не Product Thesis — не фиксирует проверяемую гипотезу и критерии пилота.
- Не MVP Scope — не определяет релизный состав.
- Не UX standards — не содержит интерфейсных паттернов и правил экранов.
- Не architecture principles — не содержит технических и доменных решений.
- Не safety policy — не задаёт матрицы компетенций, рисков и эскалации.
- Не measurement framework — не содержит метрик, порогов и числовых целей.
- Не feature checklist — не перечень функций и не фильтр admission.
- Не tone-of-voice guide — не определяет голос и стиль коммуникации.
- Не business model specification — не содержит тарифов, сегментов и
  unit-экономики.
- Beauty/wellness — первая вертикаль, а не идентичность продукта (Vision
  §15, §19): этот документ не превращает Ayla в beauty-продукт.
- **Не определяет точный feature composition или Wave sequencing
  конкретного MVP release (v0.2).** LDT — не обязателен для первого MVP;
  Food Scanner входит в MVP; конкретная Wave-последовательность и набор
  capabilities — решения `Ayla MVP Scope and Release Contract`, принятые
  на основании Owner Decisions, не этого документа.

## 8. Relationship to Canonical Sources

| Source | Role | What Principles translates | What Principles does not duplicate |
|---|---|---|---|
| Ayla Product Essence | Highest product source / parent product source | Продуктовый центр, иерархия документов (Essence §21; раскрыта также в §2), неизменная продуктовая истина: human-first, Transformation Goal, разделение ролей, representation-neutral identity | Полный narrative Essence, каноническая формула продукта, полная модель ролей, развёрнутые критерии решений (§22) |
| Ayla Constitution | Hard constraints / side anchor | Продуктовые эвристики объяснимости, уместности, нейтральности, контроля | Тексты статей; consent-нормы (Ст. VI, XIV); safety-компетенции (Ст. VIII, XII, XIII); governance-процесс |
| LDT Manifesto | Sibling / aligning input для LDT-положений | Recognition, identity preservation, разделение классов достоверности, body dignity — как продуктовые decision rules, применяемые условно (только когда LDT используется) | Living Timeline; семь классов достоверности дословно (§9); Consent and Data Dignity (§12); MVP Principles (§14); Long-Term Boundaries (§15). LDT-specific нормы Manifesto не становятся автоматически mandatory requirements первого MVP (OD-MVP-1) |
| Product Vision | Sibling / long-term direction | Human-first, memory as continuity, видимый и понятный путь, «ничего не делать» — как стабильные нормы; LDT как долгосрочная стратегическая capability | Конкурентный ландшафт; персоны; стратегия запуска; позиционирование |
| Product Thesis | Sibling / testable MVP hypothesis | Representation-neutral value loop (Goal → Signal → Context → Recommendation → Action → Memory → Progress); booking downstream; «больше фактов ≠ лучше понимание» | Пилотные сегменты; тарифы и канал; success/failure signals; Product Thesis Validation Gate |
| MVP Scope | Downstream / release content | — | Релизный состав целиком, включая точную роль LDT в конкретном релизе: выбирается в пределах этих Principles, здесь не определяется |

## 9. Open Questions

- **Tone of voice «подруга-эксперт» (KEEP_NON_BLOCKING).** Зафиксирован
  впервые в Product Vision §9 и не имеет пока нормативного источника в
  Glossary/Constitution. Этот документ вопрос не закрывает: тон — не
  предмет Product Principles (см. §7, non-goal «tone-of-voice guide»).
- **Schema type `product-principles` (KEEP_NON_BLOCKING).** Тип не
  зарегистрирован в `.knowledge/schema.yaml`; использован `foundation` по
  действующему precedent (см. `open_schema_question` в frontmatter).
  Явное добавление типа — при следующем amendment схемы, отдельным решением.
- **OQ-P1 — Product Thesis alignment (RESOLVED в v0.2).** Требовался ли
  amendment Thesis v0.5 из-за LDT-dependent MVP hypothesis? Да — выполнен
  как Thesis v0.6 параллельно с этим документом.
- **OQ-P2 — LDT Manifesto relationship (KEEP_NON_BLOCKING).** Manifesto §14
  («MVP обязан проверить жизнеспособность Living Digital Twin») содержит
  formulation, конфликтующую с OD-MVP-1 в части обязательности; требуется
  minimal amendment Manifesto (не полная переработка) — зарегистрировано
  отдельно в рамках этой канонизации, вне scope amendment Principles.
- **OQ-P3 — Principle numbering (RESOLVED в v0.2).** Применена чистая
  нумерация v0.2 (4.1–4.14) с explicit mapping в Change Log; Identity
  Continuity свёрнута в условную норму внутри 4.3.

## Change Log

> Этот журнал отражает историю изменений документа и не является
> нормативной частью спецификации. Нормативным считается текущее состояние
> разделов 1–9, а не записи ниже.

### v0.2 (2026-08-07) — Targeted amendment: LDT/MVP boundary, memory, proactivity, safety

Выполнено по `Ayla Product Principles — Amendment Plan v0.1 → v0.2` на
основании Owner Decisions OD-MVP-1…4, Product Essence v1.2, Product Vision
v2.1 и Product Thesis v0.6 (все candidates).

**Mapping v0.1 → v0.2:**

| v0.1 | Действие | v0.2 |
|---|---|---|
| 4.1 Human First | KEEP | 4.1 Human First |
| 4.2 Goal at the Center | KEEP + strengthen | 4.2 Goal at the Center |
| 4.3 The Path Is Visible | MODIFY | 4.3 Visible & Understandable Path |
| 4.4 Identity Continuity | RELOCATE | условная норма внутри 4.3 |
| 4.5 Honest Representation | KEEP + extend | 4.4 Honest Representation |
| 4.6 Memory as Continuity | EXPAND | 4.5 Progressive Memory + User Control |
| 4.7 Explainable Next Step | KEEP + strengthen | 4.6 Explainability & User Agency |
| 4.8 Booking Is Downstream | KEEP | 4.7 Booking Is Downstream |
| 4.9 User in Control | KEEP + generalize | 4.8 User in Control |
| 4.10 Progress Without Pressure | KEEP + expand | 4.9 Goal-Relative Progress Without Pressure |
| 4.11 Value on Both Sides | KEEP + strengthen | 4.10 Economic Neutrality & Trust |
| — | ADD | 4.11 Contextual Proactivity |
| — | ADD | 4.12 Safety & Wellness Boundary |
| — | ADD | 4.13 User Outcome First |
| — | ADD | 4.14 Product Restraint / Release Discipline |
| «нет формального порядка» | MODIFY | Hard Precedence Layer (§3) + contextual heuristics |

- **§1** — добавлена явная граница: Principles не определяют feature
  composition отдельного релиза.
- **§2** — обновлены версии parent-документов (Essence v1.2, Vision v2.1,
  Thesis v0.6).
- **§3** — добавлен ограниченный Hard Precedence Layer (safety → autonomy
  → user outcome → engagement → commercial).
- **§4** — см. таблицу mapping выше.
- **§5** — Decision Test пересобран: LDT-вопрос стал условным; добавлены
  вопросы про safety/wellness, memory, proactivity, release scope.
- **§6** — Contextual Proactivity убрана из trade-offs (стала core
  principle); `Twin fidelity vs user effort` переименован в
  `Representation fidelity vs user effort`; conflict model дополнена Hard
  Precedence Layer.
- **§7** — добавлен non-goal: Principles не определяют exact feature
  composition или Wave sequencing.
- **§8** — таблица уточнена: LDT Manifesto нормы применяются условно;
  Product Thesis описан через representation-neutral value loop.
- **§9** — OQ-P1 resolved (Thesis amended в v0.6); добавлен OQ-P2 (LDT
  Manifesto §14 требует minimal amendment — зафиксировано отдельно, вне
  scope этого документа); OQ-P3 resolved (чистая нумерация v0.2).
- **Metadata:** version 0.1 → 0.2; status approved → draft; canonical_status
  approved → candidate (ожидает Product Owner Final Review); updated
  2026-07-31 → 2026-08-07.
- **Next gate:** Product Owner Final Review для Principles v0.2, затем
  обновление `Ayla MVP Scope and Release Contract` с фактическим релизным
  составом (Twin out of mandatory MVP; Food Intelligence in; Memory
  Foundation in; новый validation loop).

### v0.1 (2026-07-31) — Initial canonical candidate authoring

- Создан новый Foundation document №3 (Vision → Thesis → **Principles** →
  MVP Scope → User Journey) в режиме NEW_CANONICAL_AUTHORING; ранее
  существовал только как `MISSING / CREATE` в CANON_INDEX.
- Основание: Ayla Product Essence v1.1 (CANONICAL), Living Digital Twin
  Manifesto v1.0 (CANONICAL), Product Vision v2.0 (CANONICAL), Product
  Thesis v0.5 (CANONICAL), Ayla Constitution v2.2 (conditional reference),
  AYLA-DEC-0026.
- Сформирован ровно 11 core principles по результатам Canonical
  Requirements and Source Analysis; sibling-иерархия сохранена: Manifesto —
  согласующий input, не родитель; новая иерархия не создаётся.
- Добавлен синтезированный 10-question Decision Test (Essence §22,
  Manifesto §17, Thesis §8/§11) без копирования трёх исходных списков.
- Добавлена лёгкая Tensions and Trade-offs модель (5 пар) без формального
  precedence order между принципами.
- Добавлены 13 non-goals, включая границу «beauty/wellness — первая
  вертикаль, не идентичность продукта».
- Зафиксирована `open_schema_question`: тип `product-principles` не
  зарегистрирован в schema; использован `foundation` по precedent.
- Документ имеет статус DRAFT / canonical candidate и не объявляется
  CANONICAL: статус CANONICAL присваивается только после consistency review
  и owner approval.
