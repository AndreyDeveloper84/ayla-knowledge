---
node_id: ayla.strategy.decision-log
title: Ayla Decision Log
type: decision-log
status: review
activation_status: pending-infrastructure
version: "0.9"
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
updated: 2026-07-27
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

## Change Log

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
