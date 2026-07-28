---
node_id: ayla.strategy.decision-log
title: Ayla Decision Log
type: decision-log
status: review
activation_status: pending-infrastructure
version: "1.4"
owner: Founder / Product Architecture
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
created: 2026-07-18
updated: 2026-07-28
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
  - ayla/strategy
  - type/decision-log
  - priority/p0
depends_on:
  - "[[Ayla Constitution]]"
related:
  - "[[Ayla Knowledge Architecture Specification]]"
supersedes: []
review_cycle: event-driven
---

# Ayla Decision Log

## Назначение

Реестр межрепозиторных решений владельца (Founder). Каждая запись — решение,
принятое вне отдельного репозитория и влияющее на несколько систем или на
продукт целиком.

Правила ведения:

- Одна запись = одно решение; изменения — батчем `agent/decision-log-*`,
  один логический batch = один commit.
- Реализационные ADR, меняющиеся вместе с кодом, остаются каноническими в
  owning repository (см. [[Ayla Knowledge Architecture Specification]] §2.1)
  и подключаются сюда ссылкой; mirror — по `sources-manifest.yaml`.
- Расхождение кода с решением не исправляется молча: новая запись, amendment
  или ADR.
- Записи не удаляются; пересмотренное решение сохраняет superseded-редакцию
  и причину пересмотра.
- Каждая запись содержит: Решение, Основание, Затрагивает.

Идентификаторы: глобальные `AYLA-DEC-NNNN` (стабильные, не переиспользуются).
Краткие алиасы `D1`…`D9` сохранены как `legacy_id` для обратной совместимости
со ссылками из кодовых репозиториев.

Статусы записей: `действует`, `в работе`, `ожидает`, `отменено`.

**Provenance:** перенесено из `beautygo_backend` `docs/PROJECT_INDEX.md` §5.4
(рабочая копия 2026-07-18; файл **не находится под Git** — sha256 содержимого
на момент миграции:
`5a78c4449c1d73ad44d9c1cf9bcd9d02f54b9e67cc2adf44bf835dba5d4762f5`).
Старый источник превращается в ссылку на этот канон отдельным
reviewed-изменением после проверки commit миграции.

## Реестр решений

### AYLA-DEC-0001 — Модель монетизации пилота

`legacy_id: D1` · **Дата:** 2026-07-18 · **Статус:** действует

- **Решение:** подписка 690₽/мес (соло-мастер), 990₽/мес (салон, 3 мастера)
  + 90₽ за успешную запись — платит специалист. Пользователь не платит
  ничего ([[Ayla Constitution]], Ст. IV).
- **Основание:** заменяет две конфликтовавшие модели — 8% split в коде и
  tiered-рекомендацию Product Audit (3/5/6–7%); закрывает спор о двойной
  монетизации пользователя (690₽/мес + 100₽/запись) в пользу Конституции.
- **Затрагивает:** новый эпик Billing в `beautygo_backend`; пересмотр
  YooKassa split в `payments/`; Unit Economics; Business Model doc.

### AYLA-DEC-0002 — Moat: память / «расширенное понимание»

`legacy_id: D2` · **Дата:** 2026-07-18 · **Статус:** действует

- **Решение:** память — центр killer-сценария («Ayla помнит и понимает меня»);
  цепочка еда→beauty остаётся одним из триггеров, но не ядром.
- **Основание:** booking — commodity (YCLIENTS ~90% сетевых, DIKIDI);
  единственный защищаемый ров — накопленный контекст и понимание
  пользователя; окно конкурентной гонки 12–18 месяцев (Research Synthesis).
- **Затрагивает:** Killer PRD → переработка v1.1; North Star метрики;
  S3 Memory — главный критический путь пилота.

### AYLA-DEC-0003 — Дата пилота

`legacy_id: D3` · **Дата:** 2026-07-18 · **Статус:** действует

- **Решение:** пилот — **2026-08-15**, Пенза. Предыдущие даты
  (2026-06-30, 2026-07-15) отменены.
- **Основание:** прежние даты прошли без подтверждения; 4 недели — реальный
  минимум по критическому пути (каталог→бронь + память); более ранняя дата
  нереалистична, более поздняя съедает конкурентное окно.
- **Затрагивает:** MVP Roadmap (ребейз дат); 4-недельный план потоков
  W1–W6 (`beautygo_backend` `docs/PILOT_STREAMS_2026-08-15.md`).

### AYLA-DEC-0004 — Канал пилота

`legacy_id: D4` · **Дата:** 2026-07-18 · **Статус:** действует

- **Решение:** основной канал — **MAX-бот + MAX Mini App**. Telegram —
  вне пилотного scope.
- **Основание:** Journey Specification v1.1 и Product Audit: MAX — главный
  канал и moat (0 friction install, CAC −5–10x, конкурентов в MAX нет);
  снимает противоречие с MVP Roadmap (там устаревший Telegram).
- **Затрагивает:** scope `channels/` в `ai-bot-platform`; известный риск —
  фрикция оплаты YooKassa вне MAX (Mini App SDK).

### AYLA-DEC-0005 — Статусы документов

`legacy_id: D5` · **Дата:** — · **Статус:** ожидает (pending decision)

- **Решение:** _не принято_. Предмет: Killer PRD draft→approve (после
  переработки по AYLA-DEC-0002); Knowledge Architecture Specification
  review→approved.
- **Основание:** документы, используемые как нормативные (нормативный путь
  продукта), обязаны иметь честные статусы; Killer PRD цитируется как основа
  Phase 1.5, оставаясь draft.
- **Затрагивает:** governance `ayla-knowledge`.

### AYLA-DEC-0006 — Онлайн-оплата клиентом в пилоте

`legacy_id: D6` · **Дата:** 2026-07-18 · **Статус:** действует
(пересмотрено в тот же день)

- **Решение:** клиент может оплатить онлайн/безналом — **опционально**, не
  обязательное условие записи. Привязка карты мастера — для абонемента
  (AYLA-DEC-0007).
- **Основание:** онлайн-оплата повышает доверие к записи и защищает мастера
  от no-show; интеграция YooKassa частично существует.
- **Superseded-редакция (2026-07-18, та же дата, ранее):** «Пилот без
  онлайн-оплаты клиентом; клиентский платёжный контур (hold/capture/refund)
  уходит за feature flag до этапа 2».
- **Причина пересмотра:** решение владельца — ценность онлайн-оплаты
  (доверие, защита от no-show) важнее упрощения scope; capture-баг всё равно
  требовал исправления для split-модели (AYLA-DEC-0008).
- **Затрагивает:** `beautygo_backend` W1: fix capture (hold→capture на
  completed) в критическом пути; flat 90₽ вместо 8%; путь записи без
  предоплаты сохраняется.

### AYLA-DEC-0007 — Сбор денег с мастера

`legacy_id: D7` · **Дата:** 2026-07-18 · **Статус:** действует

- **Решение:** автосписание (рекуррент): сохранённая карта мастера,
  автоплатёж за подписку + начисленные 90₽. Порядок взыскания fee — по
  инварианту AYLA-DEC-0010.
- **Основание:** автосписание убирает операционную стоимость ручных инвойсов
  и churn от «забыли оплатить»; карта привязывается один раз; рекуррент
  YooKassa закрывает пилот без полноценного биллинг-цикла.
- **Затрагивает:** Billing: `save_payment_method`, согласие на автоплатёж
  (юр.), dunning + блокировка записей при долге, чеки 54-ФЗ
  платформа→мастер.

### AYLA-DEC-0008 — Расчётная схема с мастером

`legacy_id: D8` · **Дата:** 2026-07-18 · **Статус:** действует

- **Решение:** **YooKassa split per-master** — при capture 90₽ платформе,
  остальное мастеру на суб-счёт (вывод по расписанию ЮKassa). Эквайринг —
  YooKassa. Внутренний баланс/кошелёк (вывод T+24ч) — **эпик этапа 2** с
  юристом и банком. Порядок взыскания fee — по инварианту AYLA-DEC-0010.
- **Основание:** деньги клиента не проходят через наш расчётный счёт — нет
  деятельности платёжного агента (161-ФЗ) и нет стройки ledger в 4 недели;
  выплата мастеру на лицензированной инфраструктуре ЮKassa.
- **Затрагивает:** flat 90₽ + transfers per-master в `payments/`;
  KYC-онбординг мастеров в ЮKassa (операционно, неделя 1 пилот-плана).

### AYLA-DEC-0009 — Capture-стратегия

`legacy_id: D9` · **Дата:** 2026-07-18 · **Статус:** действует

- **Решение:** немедленный capture после подтверждения оказания услуги
  (`CAPTURE_DELAY_HOURS=0`); механизм — параметризуемая отложенная задача
  (готова к 24ч); планирование относительно `expires_at` (safety buffer
  60 мин); идемпотентность + reconciliation + алерты обязательны.
  Переключение на 24ч — по измеримым триггерам.
- **Основание:** мастера получают деньги быстрее (supply пилота ограничен);
  Concierge Mode снижает ценность окна разбирательства; споров ожидается
  мало; клиентский UX без второго банковского события; переход — конфигом,
  без переделки контура.
- **Канонический ADR:** `beautygo_backend`
  `docs/architecture/payments-capture-strategy.md` (реализационный ADR,
  остаётся в owning repo; сюда — mirror по manifest).
- **Затрагивает:** W1 capture-задача, reconciliation, алерты; UX-статусы
  платежа; копирайтинг без обещания «24ч на жалобу».

### AYLA-DEC-0010 — Инвариант одиночного взыскания booking fee

**Дата:** 2026-07-18 · **Статус:** действует

- **Решение (инвариант):** одна completed booking → fee 90₽ взыскивается
  **ровно один раз**:
  - online-paid booking → 90₽ удерживается через split при capture
    (AYLA-DEC-0008);
  - offline-paid booking → 90₽ начисляется в provider billing
    (AYLA-DEC-0007);
  - двойное взыскание (split + начисление) запрещено; отсутствие взыскания
    по completed booking — инцидент reconciliation.
- **Основание:** AYLA-DEC-0007 и AYLA-DEC-0008 без явного инварианта
  допускают прочтение с двойным взысканием одной и той же fee; денежный
  контур — зона нулевой терпимости к двусмысленности.
- **Затрагивает:** `payments/` (split), `billing/` (BookingFee создаётся
  только при отсутствии online-paid Payment по записи); обязательный
  инвариант-тест; правило reconciliation job.

### AYLA-DEC-0011 — Последовательность документов продуктового роадмапа
 
**Дата:** 2026-07-27 · **Статус:** действует
 
- **Решение:** зафиксирована обязательная последовательность материализации
  и канонизации следующего уровня документации Ayla:
```
  Killer PRD
      ↓
  Ayla User Journey Specification
      ↓
  Ayla Intent Model Specification
      ↓
  Ayla Domain Context Map
      ↓
  Ayla Core Domain Model
```
 
  Следующий документ может существовать как `draft` (структура, сбор
  источников, терминология) параллельно с работой над предыдущим — это не
  запрещено. Запрещён переход следующего документа к содержательной
  канонизации (`review` без открытых P0-противоречий → `approved`) раньше,
  чем предыдущий документ в цепочке достигнет состояния `review` без
  открытых P0-противоречий. В частности:
  - Intent Model не формализуется до готовности Journey (границы намерений
    производны от пользовательского пути, не наоборот);
  - Domain Context Map не строится до готовности Intent Model (границы
    bounded contexts производны от уже определённых сценариев и намерений);
  - Core Domain Model (агрегаты, инварианты) не проектируется до утверждения
    Domain Context Map — проектирование агрегатов до фиксации границ
    контекстов создаёт риск их полной переделки при последующем изменении
    границ.
  Вышестоящая последовательность уже определена и не пересматривается этой
  записью:
 
```
  Ayla Constitution
      ↓
  Ayla Product Vision
      ↓
  Ayla MVP Product Thesis
```
 
  Настоящее решение фиксирует порядок следующего уровня документации,
  начиная с Killer PRD, как естественное продолжение уже сформированной
  архитектуры документации.
 
- **Основание:** обратный или произвольный порядок создаёт риск
  искусственных сущностей и дублирования понятий — например, доменные
  агрегаты, спроектированные до утверждения Context Map, потребуют
  переделки при изменении границ bounded context. Ayla Constitution и
  Ayla MVP Product Thesis уже определяют вышестоящие уровни (миссия,
  MVP-гипотеза); эта запись закрывает недостающее звено — порядок
  документов, которые их детализируют.
- **Затрагивает:** Ayla Domain and Metadata Registry (потребуется
  добавление planned-узлов `Ayla Intent Model Specification`,
  `Ayla Domain Context Map`, `Ayla Core Domain Model`, которых сейчас нет в
  реестре ни в каком статусе); Domain_Model_MOC (навигация должна отражать
  этот порядок); последовательность работы Knowledge/Canon Architect по
  дальнейшей канонизации.
- **Важное ограничение (зафиксировано при вводе записи):** эта запись
  фиксирует **порядок и обязательность последовательности**, а не
  содержание самих документов «Intent Model», «Domain Context Map» и
  «Core Domain Model» — они не материализованы и не существуют как файлы
  в `ayla-knowledge` на момент этой записи. Материализация каждого из них
  проходит обычный процесс (проверка на дублирование, предложение
  структуры, согласование границ — см. правила Chief Knowledge Architect),
  а не создаётся автоматически из факта этой записи.

### AYLA-DEC-0012 — Owner directions по Ayla Domain Capability Registry (OD-CAP-1..4)

**Дата:** 2026-07-27 · **Статус:** действует

- **Решение:** по результатам ревью draft «Ayla Domain Capability
  Specification» v1.0 владелец зафиксировал четыре owner directions:
  - **OD-CAP-1 (владение capability-слоем):** capability-слой принадлежит
    Product Architecture; канонический реестр хранится в `ayla-knowledge`.
    Capability не владеет runtime state и не заменяет domain
    specifications. Документ отвечает только на три вопроса: какая
    способность нужна продукту, какой бизнес-результат она создаёт, в
    каком candidate context она предположительно реализуется. Полная
    DDD-методология остаётся в [[Ayla Domain Context Map]].
  - **OD-CAP-2 (единая классификация):** сохраняется таксономия Domain
    Context Map — Core / Supporting / Generic / Technical Capability;
    одна категория на запись, multi-classification запрещена. Governance
    и Platform — не DDD-категории, а `characteristics` записи
    (например, Consent Management: `classification: supporting`,
    `characteristics: [governance]`).
  - **OD-CAP-3 (место в цепочке AYLA-DEC-0011):** документ не ставит
    себя выше Context Map. Цепочка уточняется вставкой реестра:
    Product Vision → Killer PRD → Intent Model Specification →
    **Domain Capability Registry** → Domain Context Map. Параллельный
    draft допустим; approval и использование для подтверждения bounded
    contexts — только после predecessor documents по AYLA-DEC-0011.
  - **OD-CAP-4 (Payment Processing):** остаётся в реестре экосистемы с
    `mvp_scope: out`, `platform_scope: in`, `activation_status: deferred`.
    Не влияет на MVP Context Boundary Review; не трассируется к Killer
    PRD как MVP-функция — evidence из Product Vision, business model
    или backend contracts.
- **Основание:** ревью 2026-07-27 показало, что draft v1.0 конкурировал
  с Domain Context Map (дублирование методологии классификации и
  split/merge, две таксономии, multi-classification), не имел evidence
  ни у одной из 27 записей и позиционировался выше Context Map вопреки
  AYLA-DEC-0011.
- **Затрагивает:** `00 Foundation/Ayla Domain Capability Registry.md`
  (переименование и переработка: удаление методологических разделов,
  сокращённый record schema, обязательный evidence, Capability–Context
  Reconciliation, MVP Scope Matrix); Ayla Domain Context Map (остаётся
  владельцем DDD-методологии); формулировки роли
  `validate_knowledge.py` во всех документах (структурная и ссылочная
  корректность, не canonical approval).

### AYLA-DEC-0013 — C-02: эволюция schema v1.6 → v1.7 (proposed) и границы доменных документов

**Дата:** 2026-07-27 · **Статус:** действует (owner approval 2026-07-27; внедрение — schema v1.12, фактическая нумерация вместо «v1.7»)

- **Контекст:** Ayla Domain Context Map, Ayla Core Domain Model
  Specification и Data Inventory Matrix написаны в повторяющемся
  метаданном диалекте, отличном от schema v1.6. Повторяемость диалекта
  показывает потребность в осознанной эволюции схемы, а не в механической
  подгонке документов.
- **Действует сейчас:** schema v1.6 остаётся авторитетной; validator не
  изменён. Frontmatter трёх документов временно (interim) нормализован
  под v1.6 для сохранения зелёного состояния валидатора — это не
  прецедент решения C-02 и не owner approval.
- **Owner direction (действует) — границы функций документов:**
  - Domain Context Map — на какие bounded contexts разделена Ayla и как
    они взаимодействуют (карта границ и отношений);
  - Core Domain Model Specification — сущности, агрегаты, value objects,
    инварианты и события внутри этих контекстов (содержимое доменов);
  - Data Inventory Matrix — данные, места хранения, владельцы,
    чувствительность, retention/export/deletion.
  Взаимное поглощение запрещено. Core Domain Model остаётся честным
  draft/proposed; содержательное наполнение — только после решения C-02.
- **Proposed (ожидает owner approval):** эволюция schema v1.6 → v1.7 по
  сравнительной таблице ниже. После approval schema, validator и
  frontmatter трёх документов обновляются одним согласованным изменением.

Сравнительная таблица диалекта:

| Элемент диалекта | schema v1.6 | Предполагаемая семантика | Вариант нормализации | Обратная совместимость | Влияние | Рекомендация |
|---|---|---|---|---|---|---|
| `owners` (массив) | `owner` обязателен (строка); `owners` игнорируется как extra | несколько ответственных ролей | `owner` = ведущая роль | совместимо (extra-поле допустимо) | валидатор и nodes без изменений | Заменить существующим `owner`; `owners` допустить как optional-информативное |
| `system_owner` vs `owner` | оба поля есть, определения не закреплены | `owner` — орг-роль владельца документа; `system_owner` — система/репозиторий из enum | зафиксировать определения | совместимо | документация schema | Сохранить различие; в v1.7 добавить явные определения |
| `canonical-candidate` | source_kind: canonical/mirror/external/product-requirements | «претендует на канон» — смешение source_kind и status | `canonical` + претензия через `status`/`decision_status` | совместимо | без изменений | Отклонить: source_kind описывает происхождение, не зрелость |
| `domain` в `knowledge_area` | есть `domain-model` | доменная область знаний | → `domain-model` | совместимо | без изменений | Заменить существующим `domain-model` |
| `security_sensitivity: internal` | none/low/medium/high/critical | «внутреннее» — смешение classification и sensitivity | → `low`; признак internal несёт `classification` | совместимо | без изменений | Отклонить: нормализовать в enum sensitivity |
| `export_policy: internal-only` | full/sanitized/metadata-only/prohibited | «не экспортировать наружу» | временно `full` по конвенции internal-документов; семантически ближе `prohibited`/`metadata-only` | требует решения владельца | экспорт-пайплайн не активирован | В v1.7: определить матрицу classification × export_policy; значение отклонить |
| тип `domain-context-map` | нет в document_type_rules | профильный нормативный тип | сейчас → `architecture-specification` | добавление типа обратно совместимо | schema + validator + registry + 1 node | Добавить в v1.7 как самостоятельный тип |
| тип `domain-specification` | нет | спецификация доменной модели | сейчас → `specification` | добавление совместимо | schema + validator + 1 node | Добавить в v1.7 (семейство domain-*) |
| тип `data-inventory-matrix` | нет | реестр классов данных | сейчас → `safety-specification` | добавление совместимо | schema + validator + 1 node | Добавить в v1.7 |

- **Порядок работ (зафиксирован):** (1) аудит на стабильном состоянии +
  commit SHA; (2) Root MOC v1.2 — выполнено; (3) регистрация C-02 —
  настоящая запись; (4) предложение schema v1.7 + migration impact;
  (5) после owner approval — schema, validator и frontmatter одним
  изменением; (6) исправить битые `depends_on`, включая
  `ayla.strategy.killer-prd`; (7) судьба `acceptance_ids.txt`;
  (8) содержательное ревью Context Map и наполнение Core Domain Model.
- **C-03:** массовое создание stub-документов запрещено. Каждая
  отсутствующая ссылка сначала классифицируется как: реальный
  отсутствующий knowledge node / внешний документ из owning repository /
  устаревшее название / ошибочный ID / ещё не утверждённый planned
  artifact.

### AYLA-DEC-0014 — Роадмап документации к MVP: MVP-объём вместо канонизации экосистемы

**Дата:** 2026-07-27 · **Статус:** действует

- **Решение:** принят роадмап документов к максимально быстрому MVP.
  Главный принцип: документация уменьшает неопределённость разработки и
  не становится отдельным проектом; канонизируются только решения, без
  которых разработчики реализуют процесс по-разному, создадут
  несовместимые модели данных, нарушат privacy/safety или не смогут
  проверить, что MVP работает.
- **Состав роадмапа (зафиксирован владельцем):**
  - минимальный комплект для старта разработки — 12 артефактов:
    Constitution, Product Vision, MVP Product Thesis, Killer PRD,
    **MVP Scope and Release Contract**, MVP User Journey, Intent Model
    Specification, MVP Context Map, MVP Core Domain Model, MVP
    Architecture, API + Tool Contracts, Consent and Safety Contracts;
  - волны исполнения: (1) продуктовые блокеры — Thesis, Scope Contract,
    проверка Killer PRD, MVP Journey, Intent Model; (2) доменные —
    MVP-active записи Capability Registry, Context Boundary Review,
    MVP Context Map, Core Domain Model slice, Consent Scope Registry,
    Safety Policy; (3) технические контракты — MVP Architecture,
    Repository Responsibility Matrix, Prompt Canon boundary, Memory
    Pipeline, Public API Registry, OpenAPI, Tool Schema Registry,
    Error Code Registry, Cross-Repo Change Policy, Consumer Matrix;
    (4) доставка — Delivery Roadmap, Backlog rules, DoD, Threat Model
    Lite, Release Readiness, Measurement Plan, Runbook;
  - **change control:** после approval MVP Scope and Release Contract
    любое расширение Included Scope требует owner decision с указанием:
    зачем нужно до MVP, какой срок добавляет, какую задачу вытесняет;
  - не блокируют MVP (остаются draft/отложены): полная Context Map
    экосистемы, Payment/Billing спецификации, Outcome Learning,
    Experimentation, полный Event Catalog, multi-country legal,
    микросервисная декомпозиция, DWH и ML training архитектуры.
- **Соотношение с действующими решениями:**
  - не отменяет AYLA-DEC-0011: порядок канонизации сохраняется, Intent
    Model остаётся predecessor для Context Map и Core Domain Model;
    роадмап уточняет объём (MVP slice), а не порядок;
  - MVP Scope and Release Contract — продуктовый уровень (после Killer
    PRD), в цепочку DEC-0011 доменных документов не встраивается;
    граница с AMD-020 Pilot Scope Registry: тот владеет pilot/memory
    ownership, новый документ — release scope capabilities;
  - MVP User Journey — производный срез полной User Journey
    Specification (14 этапов + негативные сценарии), не замена ей;
  - MVP-active/deferred разбиение Capability Registry соответствует
    OD-CAP-4 (AYLA-DEC-0012) и использует §9 MVP Scope Matrix реестра.
- **Затрагивает:** Root MOC Migration Queue (новые P0: MVP Scope and
  Release Contract, Intent Model Specification, MVP-срез Journey);
  Ayla Domain Capability Registry (перевод записей MVP-active);
  Ayla Domain Context Map и Core Domain Model (MVP slice вместо полной
  канонизации); новые документы волн 1–4.

### AYLA-DEC-0015 — MVP Monetary Boundary (OD-MVP-PAY-1)

**Дата:** 2026-07-27 · **Статус:** действует

- **Решение:**
  1. CAP-023 Payment Processing остаётся `mvp_scope: out`,
     `platform_scope: in`, `activation_status: deferred`.
  2. MVP включает ограниченный provider-side monetary flow,
     необходимый для: списания подписки; списания booking fee 90 ₽;
     обработки результата списания; обновления billing status;
     применения provider eligibility; минимальной reconciliation
     с YooKassa.
  3. Ограниченный monetary flow не считается активацией полной
     Payment Processing capability и не создаёт универсальный
     payment domain.
  4. Вне MVP остаются: клиентская онлайн-оплата; wallet; payouts;
     refunds; chargebacks; универсальный split-payment; полноценный
     payment lifecycle; financial ledger.
  5. YooKassa входит в Required Integrations только в пределах
     provider-side monetary flow.
  6. CAP-022 Billing Eligibility является MVP-active.
  7. CAP-014 Safety Policy Enforcement имеет статус mandatory
     cross-cutting requirement (`user_visible_capability: false`).
  8. CAP-018 AI Orchestration and Tool Execution имеет статус
     mandatory enabling technical capability
     (`user_visible_capability: false`).
- **Основание:** Thesis §6 (автосписание подписки/fee через YooKassa)
  противоречило OD-CAP-4 (CAP-023 deferred), создавая скрытый
  архитектурный конфликт. Разделение «полноценная payment capability»
  (lifecycle, refunds, ledger, disputes) и «ограниченный провайдерский
  денежный срез» (charge attempt → result → billing status →
  eligibility) снимает конфликт без построения payment domain.
  Минимальный контур оформляется как `mvp_commercial_integration`
  внутри Scope Contract, а не как отдельная capability.
- **Затрагивает:** Ayla MVP Scope and Release Contract (§4 разделён на
  product/enabling capabilities, §5.1, §6 YooKassa); Ayla Domain
  Capability Registry (CAP-022 → MVP-active, release_role CAP-014/018 —
  при переводе записей в MVP-active, волна 2 AYLA-DEC-0014); MVP
  Architecture (minimal YooKassa adapter); открытые вопросы Scope
  Contract по платежам, CAP-014/018, персонам пилота и YooKassa —
  закрыты.

### AYLA-DEC-0016 — Subject Identity Model

**Дата:** 2026-07-28 · **Статус:** действует

- **Решение:**
  1. Каноническая identity-модель — пять разделённых сущностей: Subject
     (субъект персональных данных, consent и memory), User (человек в
     бизнес-модели), Account (учётная запись входа), Identity Reference
     (внешний идентификатор: MAX / Telegram / phone / email), Provider
     Membership (связь человека с tenant — детали в AYLA-DEC-0017).
  2. Кардинальность: в нормальном активном состоянии один Subject имеет
     не более одного active User, один User принадлежит ровно одному
     Subject; User 1—0..N Account; Account 1—0..N Identity Reference.
     Исторические, merged и anonymized записи сохраняются и не обязаны
     поддерживать физическую симметрию 1:1; удаление или деактивация User
     не каскадирует в удаление Subject. `subject_id` во всех доменных
     объектах ссылается на Subject и никогда не переписывается в
     исторических записях.
  3. Унификация идентификаторов на `user_id` запрещена: `user_id`,
     `subject_id`, `account_id`, `identity_ref_id` — раздельные
     идентификаторы с раздельными System of Record.
  4. Merge, relink и person-wide deletion — отдельные управляемые
     операции с audit events (`subject_merged`, `identity_ref_relinked`,
     `subject_anonymized`), actor и reason. Автоматический merge запрещён.
     Merge инициирует только уполномоченная support/privacy-функция по
     подтверждённому запросу пользователя; владелец tenant не может
     инициировать или подтверждать merge. До реализации consent resolver
     (п. 5) merge запрещён.
  5. Consent при merge: consent records не сливаются и не
     переписываются, сохраняют исходный `subject_id` для аудита. Для
     каждой комбинации `tenant_id + scope_id + policy version`
     вычисляется новое effective-состояние: `granted + granted` →
     `granted` при совместимой policy version; `granted + revoked`,
     `granted + denied`, `granted + expired` → `needs_reconfirmation`.
  6. Relink Identity Reference допустим только для reference в состоянии
     `verified`.
  7. Person-wide deletion управляется retention manifest: юридически
     или договорно обязательные записи не удаляются автоматически, а
     минимизируются, обезличиваются или сохраняются на установленный
     срок с documented legal basis. Retention manifest — отдельный
     privacy/legal артефакт, не часть настоящего решения.
  8. MVP-срез: Subject, User, один Account-канал (MAX), Identity
     Reference (`max_user_id`, `phone`), операции relink и person-wide
     deletion. Merge, дополнительные каналы, multi-account UI и чтение
     cross-tenant personalization — deferred (активация через Scope
     Contract §11).
  9. `ayla_user_id → subject_id` — interim mapping, не финальная
     физическая модель. BotUser — interim runtime representation,
     содержащий часть данных Account, Identity Reference и tenant-local
     projection; не канонический эквивалент какой-либо одной сущности до
     отдельного mapping audit. Немедленного рефакторинга runtime
     решение не требует.
  10. System of Record: Subject → Memory & Identity Domain; User,
      Account, Identity Reference → Identity and Access (CAP-019).
      Consent и Memory SoR не изменяются.
  11. CDM v1.3 вносит сущности п. 1, кардинальность п. 2 и строки SoR
      п. 10; область identity foundation снимается из блокирующих после
      публикации v1.3.
- **Основание:** CDM оперирует `subject_id` без определённого субъекта;
  runtime уже реализует person-уровень (person-wide delete по всем
  tenant'ам), канон отстаёт от эксплуатации. Унификация на `user_id`
  делает смену телефона, merge и удаление учётной записи разрушающими
  операциями над audit trail. Безусловная симметрия Subject↔User 1:1
  отклонена: она делает удаление User каскадным для Subject и
  несовместимой с сохранением merged/anonymized записей.
- **Затрагивает:** Ayla Core Domain Model Specification; Ayla MVP Scope
  and Release Contract (CAP-019 → MVP-active, ограниченный срез); Ayla
  Domain Capability Registry (CAP-019); AMD-020 Pilot Scope Registry.
  Consent Scope Registry не изменяется. Decision brief:
  `99 Archive/proposals/decision-brief-subject-identity-model.md`.

### AYLA-DEC-0017 — Tenant, Membership and Role Model

**Дата:** 2026-07-28 · **Статус:** действует

- **Решение:**
  1. Каноническая модель доступа персонала — шесть разделённых
     объектов: User (по AYLA-DEC-0016), Tenant, Provider, Provider
     Membership, Role Assignment, Specialist Profile.
  2. Tenant — самостоятельная сущность. В MVP один Provider связан
     ровно с одним Tenant, но понятия не синонимы. Изменение
     кардинальности Provider↔Tenant после MVP не должно требовать
     переопределения identity и authorization contracts.
  3. Профессиональный профиль мастера, его доступ к салону и связь с
     tenant — три независимых факта: Specialist Profile привязан к User
     и не содержит `provider_id`; связь с tenant — только Provider
     Membership; доступ и полномочия — только Role Assignment внутри
     active Membership.
  4. Прямая привязка `Specialist.provider_id` отменяется. Один
     Specialist Profile допускает любое число активных Membership в
     разных Provider.
  5. Membership создаёт owner tenant'а или уполномоченный platform
     operator. Самостоятельная заявка мастера создаёт только
     invitation/request в состоянии `requested` без доступа до
     подтверждения owner. Lifecycle: `requested/invited → active ⇄
     suspended → revoked`.
  6. Роли MVP: `owner`, `admin`, `specialist`. Минимальный `admin`:
     создание/изменение offline-записей; работа с расписанием;
     операционные данные своего tenant; клиентские обращения в пределах
     политики. Запрещено: управление ownership, billing/legal settings,
     доступ к memory/wellness/consent клиента, назначение owner. Все
     действия `admin` с чужими Appointment аудируются.
  7. Revoke/expiry — терминальные, не удаляющие: Membership, история
     Appointment, Offering и Specialist Profile сохраняются. Revoke
     немедленно прекращает доступ и автоматически не изменяет
     Appointment; для каждой будущей активной записи создаётся
     обязательный remediation item со статусом `needs_resolution`
     (состояние операционной задачи, не новый статус Appointment),
     уведомление owner/admin и явное решение (сохранить / переназначить
     / перенести / отменить) с actor, reason и уведомлением клиента. До
     автоматизации — ручная процедура только при наличии списка
     затронутых записей, ответственного, audit trail и подтверждения
     обработки каждой записи.
  8. Доступ персонала требует active Membership с подходящей Role
     Assignment; JWT `active_tenant` проверяется против Membership на
     каждый запрос. Ни одна tenant-роль не даёт доступа к memory,
     context и consent клиентов.
  9. Substitute workflow — deferred; модель обязана допускать
     time-boxed Role Assignment, scoped access, один tenant, только
     назначенные Appointment и автоматическое expiry.
  10. У Provider всегда не менее одного active Membership с ролью
      `owner`, пока Provider не `closed`. Повторный найм создаёт новый
      Membership; реанимация revoked запрещена. Самозанятый —
      вырожденный случай: один User, один Tenant, один Provider, один
      Membership с ролями `owner` + `specialist`.
  11. System of Record: Provider, Specialist Profile, Provider
      Membership, Role Assignment → Provider Management (CAP-009)
      владеет business truth; Identity and Access (CAP-019) владеет
      enforcement и хранит только авторизационную проекцию
      Membership/roles; Tenant → Identity and Access (CAP-019).
  12. CDM v1.3 вносит изменения пп. 1–11; область Tenant/Membership
      снимается из блокирующих после публикации v1.3.
- **Основание:** прежняя модель сшивала профиль мастера, доступ и связь
  с tenant в одной строке Specialist (`provider_id` + `user_id`), что
  делало невыразимыми мастера в нескольких салонах, точечное отключение,
  временный доступ и неразрушающий offboarding. Сценарии подтверждены
  владельцем как platform requirements (master-mobile, substitution —
  включая Q-MS6 и tenant selector, offboarding handoff-сценарии;
  внешние документы недоступны в vault — owner direction; `orch.txt` —
  admin вносит offline-записи). Runtime уже предполагает связь
  человек↔tenant (`TenantUserRelationship`, аудит P1-1), которой нет в
  модели. Зависит от AYLA-DEC-0016.
- **Затрагивает:** Ayla Core Domain Model Specification; Ayla MVP Scope
  and Release Contract (MVP-срез ролей); Ayla Domain Capability
  Registry (CAP-009, CAP-019). AMD-020 и Consent Scope Registry не
  изменяются. Decision brief:
  `99 Archive/proposals/decision-brief-tenant-membership-roles.md`.

### AYLA-DEC-0018 — Phase 2 and Product Thesis Validation Gate (proposed)

**Дата:** 2026-07-28 · **Статус:** proposed — pending Product Owner approval

- **Тип:** product-architecture-decision. **Owner:** Product Owner.
  **Scope:** MVP release model, memory-first product thesis, product
  validation, persistent personalization. **Связанные решения:**
  AYLA-DEC-0002, AYLA-DEC-0014.
- **Предупреждение:** запись фиксирует варианты и рекомендацию, но не
  изменяет approved release gates до owner approval и синхронного
  обновления затрагиваемых документов (Consent Scope Registry §10,
  Ayla MVP Scope and Release Contract §3, Ayla MVP User Journey
  Specification) через отдельный Change Control.
- **Контекст:** утверждённая MVP-модель (Consent Scope Registry §10,
  Scope Contract §3) определяет два activation gate. Phase 1 — session-only
  vertical slice без persistent memory, самостоятельный релизный gate.
  Phase 2 — opt-in persistent preferences, не является условием релиза
  Phase 1. Memory-first тезис (AYLA-DEC-0002) утверждает, что ценность
  Ayla — в накопленном понимании пользователя: извлечь разрешённый
  контекст → применить → получить outcome → скорректировать память →
  улучшить повторное взаимодействие. Phase 1 проверяет техническую
  работоспособность сквозного сценария (intent, recommendation,
  explanation, booking, safety, session-only context), но не может
  доказать: что Ayla помнит пользователя между journey; что повторный
  journey точнее/короче; что память корректно обновляется после outcome;
  что контекст не устаревает и не создаёт lock-in. Вопрос: считается ли
  продуктовая гипотеза подтверждённой после успешного Phase 1 или для
  этого обязателен Phase 2?
- **Decision drivers:** (1) не блокировать технический запуск Phase 1;
  (2) не объявлять memory-first гипотезу проверенной без памяти;
  (3) не переписывать approved gates задним числом — разделять release
  readiness, technical pilot success и product thesis validation;
  (4) сохранить измеримость — отдельные проверяемые критерии валидации;
  (5) не ослаблять consent/privacy — Phase 2 только при opt-in consent,
  утверждённом whitelist, purpose limitation, retention, user memory
  controls, audit и revocation.
- **Option A — Phase 1 считается полным MVP Ayla.** Плюсы: простая
  трактовка, быстрый пилот, нет зависимости от persistent memory
  infrastructure. Минусы: booking flow ошибочно приравнивается к
  memory-first продукту; накопительная ценность не проверяется; риск
  заявить product evidence раньше проверки; Phase 2 может быть постоянно
  отложена. Оценка: не рекомендуется.
- **Option B — Phase 1 является только technical pilot; MVP — только
  после Phase 2.** Плюсы: жёстко защищает memory-first тезис. Минусы:
  меняет смысл утверждённых Phase 1 gates; блокирует технический запуск;
  объединяет release readiness и product validation; требует немедленной
  правки нескольких approved документов. Оценка: не рекомендуется для
  текущей стадии.
- **Option C — Phase 1 можно выпустить, но Product Thesis Validation
  остаётся открытой до Phase 2 (рекомендуемый).** Phase 1 остаётся
  самостоятельным техническим release gate; его успех подтверждает
  работоспособность и безопасность session-only vertical slice, но не
  memory-first гипотезу. Product Thesis Validation закрывается только
  после Phase 2 и успешного Product Thesis Validation Scenario. Плюсы: не
  блокирует запуск; не переписывает approved status Phase 1; честно
  разделяет техническую и продуктовую валидацию; позволяет измерять
  repeat-journey value. Минусы: два статуса (release validation и product
  thesis validation) требуют отдельной отчётности; риск отложить Phase 2
  — снижается отдельным milestone, owner-visible статусом, явными
  acceptance criteria и запретом считать гипотезу подтверждённой до
  Phase 2.
- **Предлагаемое решение (Option C), нормативная формулировка:** Phase 1
  остаётся самостоятельным техническим release gate. Его успешное
  завершение подтверждает: работоспособность session-only vertical slice;
  техническую интеграцию обязательных capabilities; корректность основного
  user journey; safety и consent enforcement в пределах Phase 1. Оно НЕ
  подтверждает memory-first продуктовую гипотезу. Product Thesis
  Validation остаётся открытой, пока: активирован Phase 2; persistent
  memory используется только при допустимом opt-in consent; реализован
  утверждённый Memory Contract; применён утверждённый persistent-memory
  whitelist; выполнен Product Thesis Validation Scenario; повторный
  journey показывает измеримое улучшение; отсутствуют блокирующие
  privacy/safety/memory-quality нарушения. `Phase 1 release readiness ≠
  Product Thesis Validation`; `Phase 2 activation ≠ автоматическая
  Product Thesis Validation` — само наличие памяти не доказывает ценность.
- **Product Thesis Validation criteria** (числовые thresholds — за
  Measurement Framework, этим решением не утверждаются):
  - *Functional evidence:* подтверждённый Context Fact сохранён в Phase 2;
    факт извлечён в следующем journey и применён в допустимом purpose;
    влияние памяти прослеживается в recommendation evidence; пользователь
    может увидеть/исправить применённый контекст; outcome порождает новый
    Memory Proposal; correction, supersession и revocation работают
    корректно.
  - *User-value evidence:* повторный journey демонстрирует минимум одно
    подтверждённое улучшение — меньше повторных вопросов; точнее
    рекомендация; лучше соблюдение ограничений; лучше объяснение;
    релевантнее выбор; меньше ручной коррекции.
  - *Safety and privacy evidence (инварианты):* unauthorized context use
    rate = 0; revoked fact use rate = 0; sensitive inference persistence
    rate = 0; cross-tenant memory contamination rate = 0.
  - *Anti-lock-in evidence:* память не повторяет безусловно прошлый выбор;
    не подавляет релевантные альтернативы; не превращает preference в hard
    constraint; не игнорирует новый intent или outcome; не препятствует
    исправлению профиля.
- **Consequences.** Позитивные: Phase 1 выпускается без искусственной
  блокировки; честная картина зрелости продукта; memory-first тезис
  получает самостоятельную проверку; MVP User Journey не меняет approved
  gates самостоятельно. Негативные: дополнительный управленческий статус;
  запрет фразы «гипотеза Ayla подтверждена» после session-only пилота;
  требуются решения по OQ №10–12, Measurement Framework и отдельный
  validation report.
- **Required follow-up (после принятия):** (1) перевести запись в
  accepted; (2) Consent Scope Registry §10 — уточнить: Phase 1 —
  самостоятельный release gate; Phase 2 — обязательное условие Product
  Thesis Validation; активация Phase 2 ≠ прохождение validation;
  (3) Scope Contract — разделить Phase 1 release acceptance и Product
  Thesis Validation acceptance, не делая Phase 2 условием релиза Phase 1;
  (4) MVP User Journey — закрыть OQ №9, заменить оговорки ссылкой на
  решение, сохранить Product Thesis Validation Scenario, 14 этапов не
  менять; (5) Measurement Framework — baseline, pilot cohort, ground
  truth, repeat-journey comparison, thresholds, validation report format;
  (6) до проведения validation закрыть OQ №10–12, Memory Contract, MVP
  Recommendation Contract и относящуюся часть Domain Event Registry.
- **Non-decisions:** решение не активирует Phase 2; не расширяет memory
  whitelist; не разрешает persistent storage без consent; не меняет
  recommendation pipeline; не утверждает числовые метрики; не объявляет
  Memory Contract принятым; не меняет Phase 1 implementation scope; не
  повышает статус MVP User Journey; не подтверждает гипотезу без
  validation evidence.
- **Rejected interpretations:** «Phase 1 выпущен → гипотеза
  подтверждена»; «Phase 2 включён → validation автоматически пройдена»;
  «для выпуска Phase 1 обязательна persistent memory»; «persistent memory
  можно включить до утверждения consent и whitelist»; «Product Thesis
  Validation заменяет release acceptance».
- **Acceptance criteria решения:** Product Owner явно выбрал опцию; до
  approval approved-документы не изменены; release readiness отделена от
  Product Thesis Validation; при Option C Phase 2 не условие релиза
  Phase 1; validation не закрывается фактом активации Phase 2; consent,
  whitelist, safety, privacy — обязательные предусловия; правки
  approved-документов — только отдельным Change Control; MVP User Journey
  обновляется только после принятия решения.
- **Затрагивает (после approval, через Change Control):** Consent Scope
  Registry §10; Ayla MVP Scope and Release Contract §3; Ayla MVP User
  Journey Specification (OQ №9); Measurement Framework (planned).
  Источник: OQ №9 [[Ayla MVP User Journey Specification]] v0.2.1.

### AYLA-DEC-0019 — Intent Detected Lifecycle Boundary

**Дата:** 2026-07-28 · **Статус:** действует (accepted; owner ruling
KM-IM-1 от 2026-07-27, зарегистрирован 2026-07-28)

- **Тип:** architecture-decision. **Owner:** Product Owner. **Scope:**
  intent resolution, intent lifecycle, runtime contracts, orchestration
  boundary. **Связанные элементы:** KM-IM-1, OQ-11
  [[Ayla Intent Model Specification]].
- **Контекст:** Core Domain Model ранее использовал состояние `detected`
  как часть жизненного цикла Intent и мог отображать его в промежуточное
  значение `unresolved`. Ayla Intent Model Specification определяет
  публичный Intent Resolution Output Contract, создаваемый только после
  первого resolution pass. Требовалась граница между внутренним
  состоянием процесса Intent Resolution, опубликованным состоянием
  Intent, orchestration state и execution readiness. Регистрация устраняет
  collision: ссылка на это решение ошибочно указывала на AYLA-DEC-0016
  (Subject Identity Model); AYLA-DEC-0016 не изменяется.
- **Решение:** `detected` является внутренним lifecycle-состоянием
  процесса Intent Resolution. `detected`: не входит в публичный Intent
  Resolution Output Contract; не является значением `Intent.status`; не
  сериализуется как опубликованный Intent Result; не является
  orchestration state; не означает intent-level readiness; не означает
  execution readiness; не подтверждает intent type; не запускает
  downstream capabilities; не может быть основанием для side effects; не
  отображается в `unresolved`. Первый публикуемый Intent Resolution
  Output создаётся только после завершения первого resolution pass и
  содержит consumer-meaningful intent-level результат. Допустимые
  публикуемые состояния определяются Intent Model: `resolved`,
  `needs_clarification`, `unresolved`, `blocked_safety`. Состояния
  дальнейшего lifecycle (`superseded`, `expired`) применяются только к
  уже опубликованному Intent в соответствии с утверждёнными контрактами.
- **Normative boundary:**
  `internal resolver lifecycle ≠ Intent Resolution Output ≠ orchestration
  state ≠ execution state`; `detected ≠ unresolved`;
  `Intent resolved ≠ action authorized ≠ action confirmed ≠ action
  executed ≠ action succeeded`.
- **Implementation impact:**
  - *Intent Model:* семантика Output Contract не меняется; OQ-11 закрыт
    этим решением; исправлена ошибочная ссылка AYLA-DEC-0016 →
    AYLA-DEC-0019.
  - *Core Domain Model (отдельная задача синхронизации, не выполняется
    этой записью):* удалить mapping `detected → unresolved` (interim);
    исключить `detected` из публичного `Intent.status`; разделить
    internal resolver lifecycle и published Intent lifecycle; определить
    класс `IntentDetected` через Domain Event Registry.
  - *Runtime and orchestration:* consumers не получают `detected` как
    contract output, не принимают orchestration decisions и не запускают
    capability/side effect на его основании.
  - *Observability:* `detected` допустим для traces, logs, latency
    metrics, recovery, deterministic replay и внутренней диагностики; это
    не превращает его в публичный domain или integration contract.
- **Consequences.** Позитивные: устраняется двойная семантика
  `unresolved`; публичный Intent Contract остаётся consumer-meaningful;
  internal processing не протекает в orchestration; снижается риск
  преждевременного capability dispatch; сохраняется внутренний tracing.
  Негативные: Core Domain Model требует отдельного amendment;
  implementation не может использовать `unresolved` как технический
  default до первого resolution pass; требуется сверка event semantics.
- **Non-decisions:** решение не удаляет `detected` из внутренней
  реализации; не добавляет новый публичный status; не определяет
  окончательное имя `IntentDetected`; не утверждает Domain Event
  Registry; не определяет execution readiness; не меняет slot
  requirements, правила safety, authorization или user confirmation
  contracts.
- **Rejected alternatives:** сделать `detected` публичным status
  (consumers не могут принять содержательное решение на его основании);
  отображать `detected` в `unresolved` (смешивает незавершённую обработку
  с завершённым resolution pass); полностью удалить `detected`
  (допустим для внутренней observability и processing lifecycle).
- **Затрагивает:** [[Ayla Intent Model Specification]] (OQ-11 закрыт);
  [[Ayla Core Domain Model Specification]] (отдельная задача
  синхронизации — lifecycle, persistence, `IntentDetected`,
  `IntentResolved`, `IntentAbandoned`, `IntentFulfilled`, ERD, global
  invariants, Domain Event Registry dependencies).

### AYLA-DEC-0020 — Service Offering ownership and Specialist assignment

**Дата:** 2026-07-28 · **Статус:** действует

- **Решение:**
  1. **target_model.** Трёхуровневая коммерческая модель с разрешением
     исполнителя через Membership → Profile: Catalog Service (смысловая
     услуга) → Service Offering (коммерческое предложение) → Specialist
     Offering Assignment → Specialist Membership → Specialist Profile.
  2. **offering_owner.** Service Offering принадлежит Provider как
     организации-владельцу коммерческого предложения. Offering несёт
     `tenant_id` как границу изоляции и доступа, но Tenant не является
     владельцем прайса; понятия не взаимозаменяемы (AYLA-DEC-0017).
     Соло-мастер — Provider с одним active Specialist Membership;
     отдельного доменного контура соло не существует.
  3. **assignment_target.** Specialist Offering Assignment ссылается на
     `specialist_membership_id`; модель `assignment.specialist_id`
     запрещена. Assignment несёт price_override, duration_override,
     booking_enabled, status и qualification_status со ссылкой
     `qualification_evidence_ref`; assignment не является доказательством
     квалификации. Effective values:
     `effective_price = price_override ?? base_price`;
     `effective_duration = duration_override ?? base_duration`.
     `booking_allowed` — результат domain policy evaluation, а не поле
     Assignment: offering active AND offering booking enabled AND
     assignment active AND assignment booking enabled AND membership
     active AND availability decision = available (определяется planned
     AYLA-DEC-0021) AND qualification/safety requirements satisfied
     (если применимая policy требует verified qualification).
  4. **solo_auto_assignment.** Активация Offering соло-организации
     невозможна без active Assignment на единственный eligible
     Specialist Membership; draft Offering без assignment допустим.
     Команда создания с немедленной активацией создаёт обе сущности
     атомарно; асинхронное создание assignment запрещено. Для
     организации с несколькими мастерами авто-assignment не
     выполняется — назначение делает owner.
  5. **specialist_permissions.** Specialist управляет собственной
     доступностью (`active → self_disabled`); возврат — owner/admin,
     для safety-sensitive услуг — только с подтверждением специалиста.
     `base_price` специалисту запрещён; own `price_override` — только по
     делегированному permission. Минимальный набор:
     `offering.manage_base_price`,
     `offering_assignment.manage_own_availability`,
     `offering_assignment.manage_own_price_override`,
     `offering_assignment.manage_any`.
  6. **pricing_domain.** Offering price — Commerce / Catalog
     Management, не Platform Billing (тариф подписки, комиссия Ayla,
     реквизиты). Матрица: Owner — billing да, pricing да; Admin —
     billing нет, pricing по permission policy; Specialist — billing
     нет, own override по делегированию. Смысл AYLA-DEC-0017 п. 6 не
     изменяется.
  7. **yclients_mvp.** В MVP — guided/manual import с валидацией,
     dry-run, отчётом о дублях и подтверждением owner; полная
     авто-синхронизация deferred. Модель import-ready: ExternalMapping
     (provider, external_entity_type, external_id, internal_entity_type,
     internal_id), правила дедупликации, idempotency key. Импорт
     создаёт 1 Offering + N Assignments, не N Offerings.
  8. **appointment_contract.** Appointment хранит
     `service_offering_id`, `specialist_assignment_id`,
     `specialist_membership_id` и snapshots: `price_snapshot {amount,
     currency}`, `effective_duration_snapshot`, `offering_title_snapshot`.
     Канонический `specialist_id` как SoR-атрибут Appointment
     запрещён: исполнитель определяется через
     `specialist_membership_id`, глобальный профиль — через Membership →
     Specialist Profile. Денормализованный `specialist_id` допустим
     только в read models, search indexes и analytics как derived-поле:
     не принимается в write commands и не участвует в доменных
     инвариантах. Инвариант цепочки: `service_offering_id` и
     `specialist_membership_id` в Appointment обязаны совпадать с
     Offering и Membership, на которые ссылается
     `specialist_assignment_id`; все три сущности принадлежат одному
     tenant. Историческая запись не изменяется при изменении прайса.
  9. **slot_calculation.** Слот рассчитывается от `effective_duration`
     конкретного assignment; детальный алгоритм доступности и расчёта
     слотов — отдельное решение (planned AYLA-DEC-0021).
  10. **migration.** Переход per-master → целевая модель: candidate
      grouping → confidence → preview → owner confirmation → commit.
      Объединение только по названию запрещено; минимальные ключи:
      organization, canonical service, branch/location, service
      variant, currency.
  11. **lifecycle.** Offering: `draft / active / paused / archived`;
      Assignment transitions: `pending → {active, archived}`;
      `active → {self_disabled, organization_disabled, suspended,
      archived}`; `self_disabled → {active, organization_disabled,
      suspended, archived}`; `organization_disabled → {active,
      suspended, archived}`; `suspended → {active, archived}`;
      `archived → {}`. `organization_disabled` — коммерческое решение
      организации; `suspended` — принудительное ограничение
      (compliance, qualification, safety, platform enforcement).
      Offering paused → новые записи запрещены, assignments
      сохраняются; membership terminated → assignments not bookable,
      сохраняются для истории; archived не удаляется при наличии
      записей.
  12. **catalog_projection.** Клиент видит offering один раз
      («от 1500 ₽», «60–90 минут», N специалистов); «от X» = min
      effective_price активных assignments — derived projection, не
      SoR.
  13. **Non-goals.** Не входят: алгоритм слотов, наложение расписаний,
      room/equipment, пакеты, акции/скидки, JSON Schema импорта,
      полный permission-каталог.
  14. **SoR и влияние на канон.** System of Record: Service Offering и
      Specialist Offering Assignment → Provider Management (CAP-009,
      business truth); CAP-019 — enforcement; CAP-008 — только
      канонический Catalog Service; формулировка `Provider/Catalog
      boundary` упраздняется. CDM v1.3 вносит пп. 1–13; области
      «Offering owner» и «Offering lifecycle» снимаются из блокирующих
      после публикации v1.3. Пустые записи AYLA-DEC-0021/0022 в
      журнале не создаются; ссылки — «planned».
- **Основание:** per-master модель услуг (текущая runtime-модель и
  ранний CDM) дублирует прайс по числу мастеров, ломает единое
  изменение цены салоном, плодит дубли при импорте YClients и сшивает
  коммерческое предложение с конкретным человеком вопреки AYLA-DEC-0017
  (профиль ≠ доступ ≠ связь с tenant). Разделение Offering/Assignment
  устраняет дублирование, сохраняет per-master overrides и не требует
  отдельной архитектуры для соло-мастера. Decision brief:
  `99 Archive/proposals/decision-brief-offering-specialist-model.md`.
- **Затрагивает:** Ayla Core Domain Model Specification (§7.7–7.9,
  §7.12, §12 — v1.3); Ayla MVP Scope and Release Contract; Ayla Domain
  Capability Registry (CAP-008, CAP-009); planned AYLA-DEC-0021
  (Availability/Slot — зависит от effective_duration assignment);
  миграция runtime per-master services (отдельный migration plan).

### AYLA-DEC-0023 — Memory Whitelist (OQ-10): что Ayla имеет право помнить

**Дата:** 2026-07-28 · **Статус:** действует

- **Решение:**
  1. **Форма whitelist — по категориям + нормативные примеры, не по
     полям.** Новые поля автоматически наследуют политику своей
     категории. Инвариант: поле не может существовать вне категории —
     каждое persistable-поле обязано принадлежать ровно одной
     whitelist-категории. Каждая категория имеет статус (allowed /
     requires dedicated consent / forbidden), scope из Consent Scope
     Registry и основание.
  2. **Inference никогда не становится persistent memory
     самостоятельно.** Допустим единственный pipeline:
     user message → model inference → assistant asks for confirmation →
     explicit user confirmation → memory candidate → whitelist check →
     persist. Альтернативных путей не существует; автоматическое
     сохранение inference запрещено. Неподтверждённый inference живёт
     только в сессии.
  3. **User-stated safety constraints — отдельная whitelist-категория.**
     Разрешено хранить то, что пользователь сам сообщил как ограничение
     («у меня аллергия на масло ши», «нельзя сильный прогрев»). Память
     хранит утверждение пользователя, а не медицинский вывод:
     `user_stated_safety_constraint: "Пользователь сообщил, что…"`, а не
     `diagnosis: "…"`. Инвариант: Memory хранит user-stated constraints,
     а не model-derived medical facts. Любые выводы модели о здоровье
     («похоже, диабет», «вероятно, беременность») запрещены к
     сохранению всегда.
  4. **Красная зона — default deny.** По умолчанию запрещено всё
     чувствительное; разрешается только то, что отдельным owner
     decision внесено в whitelist. В MVP запрещены: диагнозы;
     психическое здоровье; сексуальная жизнь; политические взгляды;
     религия; этническое происхождение; биометрические данные; финансы;
     содержимое личной переписки как память; live-location;
     предположения модели; любые иные чувствительные категории без
     отдельного owner decision.
  5. **Расширение whitelist — только owner decision** с четырьмя
     обязательными проверками новой категории: product_value (зачем
     продукту), privacy_review (почему можно хранить), retention_policy
     (сколько хранить), deletion_behavior (как удалять и что при отзыве
     consent).
  6. **Persistent Memory хранит только устойчивые пользовательские
     факты.** Долгоживущие предпочтения и ограничения — да («любит
     спортивный массаж», «не хочет процедур с маслом ши»); состояние
     текущего разговора — нет («сегодня устал», «сегодня болит
     голова»). Состояние сессии, временные намерения и контекст
     разговора относятся к Conversation State и не являются Persistent
     Memory.
- **Граница трёх контуров (нормативная):** Conversation Context (живёт
  в рамках текущего диалога) / Persistent Memory (то, что пользователь
  осознанно разрешил помнить, в рамках whitelist) / Sensitive Knowledge
  (принципиально не сохраняется).
- **Основание:** OQ-10 — P0-узел: whitelist определяет границу продукта;
  ошибка здесь требует переработки Memory Contract, Consent, Privacy,
  Recommendation, Retrieval и UX. Решение превращает скелет из Consent
  Scope Registry v1.0 (категории данных), Constitution (inference ≠
  fact) и AMD-020 (memory gate) в явный нормативный контракт.
- **Затрагивает:** Consent Scope Registry (согласование категорий и
  scope); будущий Memory Contract (данный DEC — его §1-основание);
  Ayla Domain Capability Registry (CAP-001); AMD-020 Pilot Scope
  Registry; Killer PRD (memory thesis); Ayla Intent Model Specification
  (PROVIDE_CONTEXT / CORRECT_CONTEXT — pipeline п. 2); Ayla Core Domain
  Model (Context Fact vs Inference, §6).

### AYLA-DEC-0024 — Memory Contract: жизненный цикл персистентной памяти

**Дата:** 2026-07-28 · **Статус:** действует

- **Решение:**
  1. **MemoryEntry.** Состав: `memory_id`, `subject_id`, `tenant_id`,
     `category` (из whitelist, AYLA-DEC-0023), `value` типизированное
     (`type`, `payload`, `display_text` — свободный текст как единственная
     форма запрещён), `provenance` (`user_stated` |
     `user_confirmed_inference`), `consent_scope`, `purpose_tags`,
     `status`, `created_at`, `updated_at`, `effective_from`,
     `superseded_by`, `expires_at`, `source_event_id`, `deletion_due_at`.
     Видимость записи определяется `memory_scope` (`person | tenant |
     provider`), выводимым из category policy. Запись иммутабельна.
     `confidence` в canonical Memory Entry запрещён (допустим у
     MemoryProposal и в audit metadata, не влияет на использование
     факта).
  2. **MemoryProposal — отдельная сущность.** Статусы:
     `pending_confirmation | accepted | rejected | expired`; имеет TTL
     и истекает при завершении сессии. До подтверждения это не память.
     MemoryEntry начинается с `active`; статусы: `active | superseded |
     expired | deletion_pending | deleted`. Цепочка:
     `proposal.pending_confirmation → accepted → entry.active →
     superseded | expired | deletion_pending → deleted`; superseded и
     expired переходят в deletion_pending, если retention policy
     требует физического удаления.
  3. **Retrieval — только purpose-limited.** Контракт:
     `MemoryRetrievalRequest {subject_id, tenant_id, consumer_id,
     purpose, allowed_categories, session_id, correlation_id}`.
     Возвращается пересечение: requested categories ∩ allowed for
     purpose ∩ allowed by consent ∩ readable active entries
     (`active AND consent_valid AND scope_match AND purpose_allowed AND
     category_allowed AND not_expired AND not_revoked`). Инвариант:
     retrieval без declared purpose запрещён; API вида
     `get_all_memory(subject_id)` запрещён даже внутренним consumers;
     retrieval аудируется (кто, цель, категории — без обязательного
     логирования значений).
  4. **Correction — immutable history.** Update-in-place запрещён;
     смена active entry атомарна: old → `superseded`
     (`superseded_by = new_id`), new → `active`. Обязателен
     `supersession_reason` (`corrected | changed | consolidated |
     policy_migration`). Category policy определяет cardinality
     (`single | multi`); для single новая запись атомарно замещает
     старую. Удаление без замены — НЕ supersession: запись переходит в
     `deletion_pending`.
  5. **Revocation — четыре слоя.** (а) Немедленный runtime effect:
     read gate проверяет актуальное consent state — все затронутые
     записи становятся unreadable немедленно, независимо от асинхронных
     обновлений, кэшей и реплик. (б) Записи переводятся в
     `deletion_pending` с `revoked_at`, `revocation_event_id`,
     `deletion_due_at`. (в) Distributed deletion по всем копиям и
     derived artifacts: retrieval cache, vector/search indexes,
     recommendation profile, precomputed summaries, embeddings,
     идентифицируемые analytics projections, локальные копии consumers.
     Инвариант: отзыв применяется ко всем readable и derived
     representations. (г) После удаления — только content-free
     tombstone (`memory_id`, `subject_id`, `category`, `status:
     deleted`, `deleted_at`, `deletion_reason`, `revocation_event_id`);
     значение и производные исчезают. Физическое удаление — асинхронно
     с дедлайном по retention manifest. Повторное согласие НЕ
     восстанавливает старые записи — новая память создаётся только
     через pipeline. Compliance audit records живут отдельно от Memory
     domain, не содержат значения и недоступны personalization.
  6. **Conversation State ≠ Persistent Memory** — разделение по
     хранилищам и API: ConversationState (`session_id`, `subject_id`,
     `temporary_slots`, `recent_context`, `unresolved_questions`,
     `current_intents`, `expires_at`) — session-scoped, короткий TTL,
     недоступен через Memory Retrieval API. Запрещены batch promotion,
     automatic summarization и background copying из Conversation State
     в Persistent Memory. Завершение сессии не создаёт память, не
     является implicit consent и не подтверждает pending proposals.
  7. **MemoryCategoryPolicy — machine-readable registry** для каждой
     whitelist-категории: `category`, `allowed_provenance`,
     `allowed_scopes`, `allowed_purposes`, `cardinality`, `default_ttl`,
     `max_ttl`, `requires_explicit_confirmation`, `revocation_behavior`.
  8. **TTL.** `expires_at` обязателен для категорий с TTL; бессрочность
     разрешена только policy категории. Expired запись не читается;
     expiration ≠ deletion — после expiration действует retention
     policy. User-stated safety constraints подлежат периодическому
     reconfirmation и не считаются вечной истиной.
  9. **Идемпотентность.** `source_event_id` уникален в Memory Service
     (или отдельный idempotency key) — один confirmation event не
     создаёт двух записей.
  10. **Ownership.** Memory Service (W3) — единственный владелец всех
      state transitions. Consumers не могут INSERT/UPDATE MemoryEntry;
      допустимы только: submit proposal, confirm proposal, request
      correction, request deletion, retrieve by purpose.
- **Основание:** без единого контракта жизненного цикла каждый документ
  описывает память по-своему, а реализация расходится в разночтениях
  «логическое vs физическое удаление», «чтение из кэша после отзыва»,
  «ночное копирование диалогов в память». Контракт реализует
  AYLA-DEC-0023 (whitelist), AYLA-DEC-0016 (subject_id, person-wide
  deletion), AMD-020 (W3 exclusive write, gate) и Constitution
  (inference ≠ fact, consent control).
- **Затрагивает:** AMD-020 Pilot Scope Registry (уточнение gate и
  deletion); Consent Scope Registry (revocation effects, category
  policy); будущий MVP Memory Pipeline Contract (роадмап §3.4 — данный
  DEC является его нормативным ядром); Ayla Domain Capability Registry
  (CAP-001); Ayla Core Domain Model (Context Fact, §6, §12); retention
  manifest (отдельный privacy/legal артефакт по AYLA-DEC-0016 п. 7).

## Change Log

### v1.4 — 2026-07-28

- новая запись AYLA-DEC-0024 (Memory Contract): MemoryEntry с
  типизированным value и запретом confidence; MemoryProposal отдельно;
  purpose-limited retrieval с запретом get_all; immutable correction с
  cardinality policy; revocation в четыре слоя с distributed deletion и
  content-free tombstone; Conversation State отделён с запретом
  background promotion; MemoryCategoryPolicy registry; TTL;
  идемпотентность; W3 — exclusive writer.

### v1.3 — 2026-07-28

- новая запись AYLA-DEC-0023 (Memory Whitelist, OQ-10): whitelist по
  категориям с наследованием политики полями; единственный pipeline
  inference → confirmation → persist; user-stated safety constraints vs
  запрет model-derived medical facts; красная зона default deny;
  расширение только через owner decision с 4 проверками; persistent
  memory — только устойчивые факты, не состояние сессии. Номер 0023
  присвоен вне очереди: 0021/0022 зарезервированы planned-ссылками
  DEC-0020 под Availability/Reschedule.

### v1.2 — 2026-07-28

- новая запись AYLA-DEC-0020 (Service Offering ownership and Specialist
  assignment): трёхуровневая коммерческая модель, assignment →
  membership, effective values, appointment contract без SoR
  specialist_id, pricing ≠ Platform Billing, guided YClients import,
  lifecycle transitions; записана немедленно по решению владельца —
  planned DEC-0021 зависит от действующего решения, а не от proposal.

### v1.1 — 2026-07-28

- новая запись AYLA-DEC-0019 (Intent Detected Lifecycle Boundary,
  accepted): регистрация ранее принятого owner ruling KM-IM-1 — `detected`
  является внутренним lifecycle-состоянием Intent Resolution, не входит в
  публичный Intent Resolution Output Contract, не отображается в
  `unresolved`; устранена collision ошибочной ссылки на AYLA-DEC-0016;
  AYLA-DEC-0016 (Subject Identity Model) не изменялся. Core Domain Model
  синхронизируется отдельной задачей.

### v1.0 — 2026-07-28

- новая запись AYLA-DEC-0018 (Phase 2 and Product Thesis Validation Gate,
  proposed — pending Product Owner approval): варианты A/B/C статуса
  Phase 1/Phase 2 относительно проверки memory-first тезиса, рекомендация
  Option C (Phase 1 — самостоятельный technical release gate; Product
  Thesis Validation открыта до Phase 2 и успешного Product Thesis
  Validation Scenario), validation criteria, non-decisions и follow-up.
  Approved-документы до owner approval не изменяются.

### v0.9 — 2026-07-28

- новые записи AYLA-DEC-0016 (Subject Identity Model: пять разделённых
  сущностей, стабильный subject_id, управляемые merge/relink/deletion,
  consent resolver с needs_reconfirmation, retention manifest отдельно,
  interim-маппинги runtime) и AYLA-DEC-0017 (Tenant, Membership and
  Role Model: Tenant отдельно, Provider 1:1 Tenant в MVP, роли
  owner/admin/specialist, lifecycle Membership, remediation при revoke,
  разделение SoR CAP-009/CAP-019); оформлены раздельно по решению
  владельца, не монолитом; подготовлены по двум decision briefs после
  owner review.

### v0.8 — 2026-07-27

- новая запись AYLA-DEC-0015 (MVP Monetary Boundary, OD-MVP-PAY-1):
  CAP-023 deferred, ограниченный provider-side monetary flow в MVP,
  YooKassa только для этого контура, CAP-022 MVP-active, release_role
  CAP-014/018; применено в Scope Contract v0.2.

### v0.7 — 2026-07-27

- новая запись AYLA-DEC-0014: роадмап документации к MVP (12-артефактный
  минимум, 4 волны, change control для Included Scope, перечень
  неблокирующих документов); зафиксировано соотношение с DEC-0011/0012
  и граница MVP Scope Contract ↔ AMD-020 Pilot Scope Registry.

### v0.6 — 2026-07-27

- AYLA-DEC-0013 переведена из proposed в действующую: owner approval
  2026-07-27. Уточнение нумерации: фактическая schema_version — 1.11,
  внедряемая версия — 1.12 (в тексте записи «v1.6/v1.7» читать как
  «1.11/1.12»). Решения по открытым вопросам: проверка «owner ∈
  owners» — warning; require_sections для domain-specification —
  отложены до наполнения Core Domain Model.

### v0.5 — 2026-07-27

- новая запись AYLA-DEC-0013: C-02 оформлен как proposed-решение об
  эволюции schema v1.6 → v1.7 (сравнительная таблица диалекта,
  рекомендации по `owners`, `canonical-candidate`, `internal`,
  `internal-only`, `domain`, новым типам документов); owner direction о
  границах Domain Context Map / Core Domain Model / Data Inventory
  Matrix; interim-нормализация frontmatter трёх документов зафиксирована
  как временная мера; порядок работ и классификация C-03.

### v0.4 — 2026-07-27

- новая запись AYLA-DEC-0012 (owner directions OD-CAP-1..4 по Domain
  Capability Registry: владение capability-слоем, единая классификация
  из Domain Context Map с characteristics вместо категорий Governance/
  Platform, уточнение цепочки AYLA-DEC-0011 вставкой реестра между
  Intent Model Specification и Domain Context Map, deferred-статус
  Payment Processing).

### v0.3 — 2026-07-27
 
- новая запись AYLA-DEC-0011 (последовательность документов роадмапа:
  Killer PRD → Journey → Intent Model → Domain Context Map → Core Domain
  Model), решение владельца от 2026-07-27; связана с уже принятой
  вышестоящей последовательностью Constitution → Product Vision → MVP
  Product Thesis;
- правило смягчено: draft следующего документа разрешён параллельно,
  запрещён только опережающий переход к канонизации;
- запись содержит явное ограничение: фиксирует порядок, не содержание ещё
  не материализованных документов (Intent Model, Domain Context Map, Core
  Domain Model — не существуют как файлы в `ayla-knowledge` на дату записи);
- затронутые документы отмечены: Ayla Domain and Metadata Registry
  (потребуются новые planned-узлы), Domain_Model_MOC (навигация).


### v0.2 — 2026-07-18

- правки по review первого коммита: глобальные ID `AYLA-DEC-*` (+ legacy
  aliases); новая запись AYLA-DEC-0010 (инвариант одиночного взыскания fee);
  superseded-редакция и причина пересмотра AYLA-DEC-0006; provenance
  дополнен sha256 и отметкой об отсутствии источника в Git; структура
  «Решение / Основание / Затрагивает» во всех записях; AYLA-DEC-0005
  промаркирована как pending decision; убрано `implements` для Constitution;
  `status` понижен до `review` до завершения review.

### v0.1 — 2026-07-18

- первый перенос Decision Log из `beautygo_backend` `docs/PROJECT_INDEX.md`
  §5.4: записи D1–D4, D6–D9 действуют, D5 ожидает.
