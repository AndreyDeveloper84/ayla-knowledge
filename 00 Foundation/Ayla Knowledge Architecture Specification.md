---
node_id: ayla.knowledge.architecture
title: Ayla Knowledge Architecture Specification
type: knowledge-architecture-specification
status: review
activation_status: pending-infrastructure
version: "1.4"
owner: Product Architecture
priority: P0
knowledge_area:
  - foundation
domain: []
concerns:
  - knowledge-management
  - governance
system_owner:
  - ayla-knowledge
source_repository: ayla-knowledge
created: 2026-07-17
updated: 2026-07-22
source_kind: canonical
canonical_status: candidate
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
tags:
  - ayla
  - ayla/foundation
  - ayla/knowledge
  - ayla/governance
  - type/knowledge-architecture-specification
  - priority/p0
implements:
  - "[[Ayla Constitution]]"
depends_on: []
supersedes: []
review_cycle: quarterly
---

# Ayla Knowledge Architecture Specification

## 1. Назначение и нормативность

Эта спецификация определяет, как Ayla создаёт, хранит, версионирует, проверяет,
связывает и публикует знания компании и продукта.

Документ является нормативным для:

- Foundation- и продуктовых спецификаций;
- архитектурных решений и доменных контрактов;
- AI-, safety-, privacy- и business-документов;
- межрепозиторных mirrors;
- организации Obsidian vault;
- валидации знаний и AI export.

Спецификация управляет knowledge artifacts, но не подменяет исходный код,
схемы баз данных, CI/CD и issue tracker. Эти системы должны ссылаться на
канонические документы, если их поведение зависит от утверждённого решения.

**Канонический репозиторий:** `AndreyDeveloper84/ayla-knowledge`

**Канонический путь:** `00 Foundation/Ayla Knowledge Architecture Specification.md`

**Интерфейс для человека:** Obsidian

**История версий и аудит:** Git и GitHub

## 2. Модель источников истины

### 2.1. Роли репозиториев

`ayla-knowledge` является каноническим источником для:

- Root MOC;
- этой спецификации;
- Ayla Constitution;
- общего Glossary и metadata registry;
- межрепозиторных карт;
- правил knowledge governance.

Документ, который должен меняться вместе с кодом конкретной системы, остаётся
каноническим в owning repository. В `ayla-knowledge` он попадает только как
генерируемый read-only mirror.

Начальное распределение ответственности:

| Репозиторий | Каноническая ответственность |
|---|---|
| `beautygo_backend` | booking, payments, catalog, identity и backend contracts |
| `ai-bot-platform` | bot, conversations, channel integrations и AI backbone |
| `ayla-ai-core` | intent, recommendation, orchestration и evaluation |
| `ayla-knowledge` | cross-product foundations, governance, MOC и общая терминология |

### 2.2. Один канонический источник

У knowledge artifact может быть только один канонический источник.

- Канонический документ редактируется только в owning repository.
- Mirror генерируется из неизменяемой редакции источника.
- Obsidian является редактором и интерфейсом навигации, а не отдельным
  источником истины.
- Локальные копии вне Git не являются каноническими.
- Миграция документа фиксирует старый источник, новый источник и migration
  commit.

### 2.3. Машинные и человекочитаемые источники

Ответственность разделена так:

1. `.knowledge/schema.yaml` — машинный источник истины для metadata fields,
   enums, lifecycle transitions и relationship constraints.
2. `Ayla Domain and Metadata Registry` — человекочитаемое представление enums
   и ownership mappings.
3. `Ayla Glossary` — семантика продуктовых, доменных и архитектурных терминов.
4. ADR и профильные спецификации — конкретные решения и policies.

Документы не поддерживают конкурирующие копии машинных enum-реестров.

## 3. Модель версионности

### 3.1. Стабильная идентичность

Между редакциями не меняются:

- `node_id`;
- имя канонического файла;
- путь в каноническом репозитории, кроме отдельно утверждённой миграции или
  rename.

Для этой спецификации:

```yaml
node_id: ayla.knowledge.architecture
version: "1.3"
```

Каноническое имя файла:

```text
Ayla Knowledge Architecture Specification.md
```

Semantic version не включается в имя активного канонического файла. Файлы
вида `Ayla Knowledge Architecture Specification v1.3.md` и автоматически
созданные копии вида `v1.3 1.md` запрещены.

### 3.2. История редакций и releases

- `version` хранит semantic version документа.
- Change Log объясняет смысловые изменения.
- Git commit SHA идентифицирует точное содержимое.
- Git tag или Knowledge Release Bundle фиксирует согласованный набор версий.
- Предыдущие редакции сравниваются через Git history.

Предыдущая редакция того же логического документа не является отдельным
Knowledge Node и не записывается в `supersedes`.

`supersedes` используется только тогда, когда один логический документ заменяет
другой документ с иной стабильной идентичностью. Заменённый node сохраняется в
Git со статусом `superseded`.

### 3.3. Правила semantic version

- PATCH — редакторское исправление без изменения policy или contract.
- MINOR — обратно совместимое смысловое дополнение или уточнение.
- MAJOR — несовместимое изменение policy, ownership, lifecycle или contract.

Смысловое изменение без обновления `version`, даты `updated` и Change Log
недопустимо.

## 4. Структура репозитория

Корень репозитория одновременно является корнем Obsidian vault:

```text
ayla-knowledge/
├── Ayla.md
├── 00 Foundation/
│   ├── Ayla Constitution.md
│   ├── Ayla Knowledge Architecture Specification.md
│   ├── Glossary.md
│   └── Foundation MOC.md
├── 01 Product/
├── 02 Strategy/
├── 03 AI System/
├── 04 Domain Models/
├── 05 Architecture/
├── 06 Safety and Governance/
├── 07 Design/
├── 08 Business/
├── 09 Research/
├── 10 Operations/
├── 90 Sources/
├── 99 Archive/
├── .knowledge/
│   ├── schema.yaml
│   └── sources-manifest.yaml
├── scripts/
└── .github/workflows/
```

Номер папки задаёт порядок навигации, но не ownership. Ответственность
фиксируется в metadata.

`Ayla.md` является Root MOC. У каждой заполненной области должен быть MOC либо
явная ссылка из MOC верхнего уровня.

## 5. Контракт Knowledge Node

### 5.1. Обязательный frontmatter

Каждый активный Knowledge Node должен соответствовать
`.knowledge/schema.yaml`.

Минимальный контракт:

```yaml
node_id: stable.machine.identifier
title: Human-readable title
type: specification
status: draft
version: "0.1"
owner: Responsible role or team
knowledge_area:
  - architecture
domain:
  - booking
system_owner:
  - ayla-booking
source_kind: canonical
canonical_status: candidate
classification: internal
data_sensitivity: none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
updated: 2026-07-18
review_cycle: quarterly
```

### 5.2. Границы полей

| Поле | Смысл |
|---|---|
| `node_id` | неизменяемая логическая идентичность |
| `owner` | ответственная роль или команда |
| `knowledge_area` | место в архитектуре знаний |
| `domain` | бизнес- или системный bounded context |
| `system_owner` | архитектурная система, владеющая описываемой ответственностью |
| `source_repository` | Git-репозиторий канонического источника |
| `concerns` | сквозные аспекты |
| `source_kind` | canonical, mirror или external |

`domain` может быть пустым только для разрешённого schema cross-domain или
foundation-документа.

### 5.3. Tags

Tags используются для навигации, но не заменяют typed metadata и relationships.
Обязательные семейства tags определяются schema и validator, а не локальными
копиями правил в документах.

### 5.4. `source_kind` и `canonical_status`

`source_kind` и `canonical_status` — независимые характеристики документа:

| Поле | Что описывает | Примеры |
|---|---|---|
| `source_kind` | Природу источника: канонический документ, зеркало, внешняя ссылка или тип документа. | `canonical`, `mirror`, `external`, `product-requirements` |
| `canonical_status` | Степень канонической зрелости: черновик, кандидат, утверждённый источник истины, устаревший. | `draft`, `candidate`, `approved`, `deprecated` |

`source_kind: canonical` означает, что документ создан внутри канонического
репозитория `ayla-knowledge`, а не что он уже утверждён как действующая норма.
Документ может быть `source_kind: canonical` и одновременно
`canonical_status: candidate` — это типичное состояние Draft-нормативного
документа, прошедшего содержательное ревью, но не закрывшего все approval gates
(например, Killer PRD v1.4).

`canonical_status: approved` совместим только со статусами, отличными от
`draft`, и с `decision_status`, отличным от `proposed`. Validator проверяет эти
конфликты. При отсутствии `canonical_status` документ считается `draft` до
явного backfill.

## 6. Статусы и lifecycle

Канонические статусы определены в `.knowledge/schema.yaml`.

Основной lifecycle нормативного документа:

```text
idea → draft → review → approved-with-amendments → approved → implemented
```

Дополнительные состояния:

```text
cancelled, blocked, deprecated, superseded, archived
```

Status описывает зрелость документа. Он не доказывает реализацию, если документ
не имеет статус `implemented` и ссылку на implementation evidence.

`activation_status` имеет отдельный смысл:

- `pending-infrastructure` — policy проходит review или обязательная
  автоматизация ещё не завершена;
- `active` — repository controls и validation работают;
- `suspended` — активация временно отозвана с зафиксированной причиной.

## 7. Семантика relationships

Relationships задаются явными полями frontmatter:

| Relationship | Смысл |
|---|---|
| `implements` | реализует principle, ADR или approved specification |
| `depends_on` | не может корректно использоваться без target |
| `adr` | управляется архитектурным решением |
| `related` | полезная связь, не являющаяся зависимостью |
| `conflicts_with` | известное смысловое противоречие |
| `supersedes` | заменяет другой логический документ |

Правила:

- `depends_on` и `supersedes` должны быть acyclic;
- все relationship targets должны разрешаться до статуса `approved`;
- отсутствующий target у review-документа с
  `activation_status: pending-infrastructure` является migration warning;
- `conflicts_with` требует resolution note или decision reference;
- backlinks помогают навигации, но не заменяют relationship semantics.

## 8. Канонические документы и mirrors

Mirror обязан содержать:

```yaml
source_kind: mirror
source_repository: beautygo_backend
source_path: docs/architecture/example.md
source_ref: <immutable-commit-sha>
source_content_hash: <sha256>
synced: 2026-07-18
```

Правила mirrors:

- ручные смысловые изменения запрещены;
- `source_ref` разрешается в immutable commit;
- содержимое нормализуется в UTF-8 и LF до расчёта hash;
- collisions вызывают fail-fast;
- удаление источника создаёт deprecation PR, но не стирает историю;
- rename сохраняет `node_id` и backlinks;
- результат sync проходит review через pull request.

Синхронизация описывается в `.knowledge/sources-manifest.yaml`.

## 9. Ревью и управление изменениями

### 9.1. Review gate

Перед каждым push документа проверяются:

1. **Противоречия** — внутренние конфликты и расхождения с каноническими
   источниками.
2. **Полнота** — purpose, scope, owner, dependencies, decisions, open
   questions, migration и Definition of Done.
3. **Полезность** — может ли читатель принять или проверить решение без
   восстановления отсутствующего контекста.
4. **Metadata** — schema compliance и стабильная идентичность.
5. **Links** — разрешаемые relationships либо явные migration warnings.
6. **Security и export** — classification, sensitive content и AI-indexing
   policy.

Результат review:

- `pass`;
- `pass-with-warnings`;
- `fail`.

Документ с результатом `fail` не отправляется как каноническое изменение.

### 9.2. Обязательные reviewers

| Класс документа | Обязательное review |
|---|---|
| Foundation / P0 | Founder и Product Architecture |
| ADR | Architecture owner и затронутые domain owners |
| Safety / privacy | Safety, Security или Data Protection owner |
| Product specification | Product owner и затронутые Engineering/UX owners |
| Mirror | Source owner или knowledge maintainer |

Protected branches, CODEOWNERS и pull requests применяются по мере развития
команды и repository access. Direct commit обязан сохранять эквивалентное
review evidence.

### 9.3. Противоречия

Если approved-документы противоречат друг другу:

1. фиксируется `conflicts_with`;
2. создаётся issue, ADR или amendment;
3. определяется управляющий принцип верхнего уровня;
4. конфликт разрешается явно;
5. зависимые документы обновляются или supersede;
6. фиксируется migration impact.

Более свежая дата сама по себе не делает документ приоритетным.

## 10. Валидация

### 10.1. Локальная проверка

Перед commit:

```powershell
python scripts/validate_knowledge.py
```

Validator проверяет как минимум:

- parseable frontmatter и duplicate YAML keys;
- обязательные поля и enum values;
- стабильный и уникальный `node_id`;
- стабильные имена канонических файлов;
- duplicate canonical titles;
- relationship targets и dependency cycles;
- обязательные разделы по типу документа;
- data classification и AI export constraints.

### 10.2. CI validation

GitHub Actions запускает тот же validator для pull requests и push в `main`.
CI не должен использовать более слабые правила, чем локальная проверка.

Во время поэтапной миграции missing links у review-документа с
`activation_status: pending-infrastructure` являются warnings. Для approved
документов или после активации они становятся errors.

### 10.3. Knowledge Health

Scheduled health report должен показывать:

- broken links;
- orphan canonical nodes;
- duplicate identities или canon;
- stale mirrors;
- overdue reviews;
- unresolved conflicts;
- P0/P1 coverage;
- документы без owner;
- документы, исключённые из AI index.

## 11. Security, privacy и AI export

Экспорт работает по deny-by-default, если metadata явно не разрешает его.

Документы с реальными PII, health data, raw messages, production dumps,
credentials или encryption material не попадают в AI index без утверждённой
sanitization policy.

Обязательные metadata:

```yaml
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
```

Доступ к Git-репозиторию не отменяет classification документа.

## 12. Рабочая модель Obsidian

В Obsidian открывается корень репозитория.

Правила:

- канонические файлы редактируются только в рабочей Git branch;
- перед редактированием выполняется pull, перед commit просматривается diff;
- ручные копии для сравнения версий не создаются;
- для сравнения используется Git history или diff plugin;
- при rename включается автоматическое обновление wikilinks;
- пользовательское состояние workspace не коммитится без отдельного решения;
- Graph View является исследовательским инструментом, а MOC и search —
  основными способами навигации.

Рекомендуемый сценарий сравнения:

```text
выбрать файл
→ открыть Git history
→ выбрать два commit или tag
→ сравнить редакции
```

## 13. Миграция из backend

Начальный staging source:

```text
repository: AndreyDeveloper84/beautygo_backend
commit: 88a66515
path: docs/00 Foundation/Ayla Knowledge Architecture Specification v1.2.md
```

Правила миграции:

1. Документы проверяются и нормализуются по одному.
2. Назначаются стабильные filename и `node_id`.
3. Фиксируются source repository, source path и source commit.
4. Выполняется локальная validation.
5. До push показываются review findings и diff.
6. Push выполняется только после явного подтверждения.
7. Старый источник сохраняется до проверки нового canonical commit.
8. Старый источник превращается в mirror или canonical-location notice
   отдельным reviewed-изменением.

Исходный файл и его копия v1.0 впервые попали в Git backend одним commit,
поэтому отдельная содержательная Git-история при миграции не теряется.
Provenance сохраняется через указанный source commit и этот Change Log.

## 14. План активации

Спецификация остаётся `pending-infrastructure`, пока:

- schema и validator не закоммичены;
- CI validation не работает в `main`;
- не созданы Root MOC и минимальный набор Foundation nodes;
- не настроена branch protection или эквивалентный review rule;
- не утверждены credentials и запуск mirror manifest;
- в migration queue остаются неклассифицированные P0 documents.

Активация требует reviewed metadata-only изменения:

```yaml
activation_status: active
```

## 15. Definition of Done

Версия 1.3 готова к approval, когда:

- приняты stable identity и Git-based versioning;
- отдельный repository признан каноном cross-product knowledge;
- корень repository используется как Obsidian vault;
- schema, validator и CI согласованы;
- migration provenance зафиксирован;
- приняты review roles и push gate;
- unresolved relationship targets видны как migration warnings;
- нормативные разделы не переопределяют друг друга.

## 16. Открытые вопросы

1. Какой Git history/diff plugin стандартизируется для Obsidian?
2. Какой retention period применяется после supersession?
3. Какие thresholds запускают Knowledge Health alerts?
4. Когда будут выданы credentials для automated mirrors?

## Change Log

### v1.4 — 2026-07-22

- введено поле `canonical_status`, независимое от `source_kind`;
- расширен `source_kind` значением `product-requirements`;
- добавлена §5.4 о различии `source_kind` и `canonical_status`;
- validator проверяет enum `canonical_status` и конфликты `approved × draft/proposed`.

### v1.3 — 2026-07-18

- каноническая спецификация перенесена в отдельный `ayla-knowledge`;
- versioned filenames и `node_id` заменены стабильной идентичностью;
- Git history, tags и release bundles закреплены как механизмы версионности;
- `supersedes` ограничен заменой другого логического документа;
- поправки v1.1 и metadata-изменения v1.2 объединены в единую нормативную
  структуру;
- repository-relative paths переведены с `docs/...` на vault-root paths;
- добавлены review gate и staged-migration policy;
- зафиксирован provenance из `beautygo_backend@88a66515`.

### v1.2 — 2026-07-18

- семантически разделены `owner`, `system_owner` и `source_repository`;
- metadata contract приведён к schema v1.3;
- добавлены registries и migration constraints.

### v1.1 — 2026-07-18

- выбрана модель отдельного knowledge repository и read-only mirrors;
- определены manifest-driven sync, governance и export boundaries;
- введены schema-driven validation и release bundles.

### v1.0 — 2026-07-17

- создана первая полная Knowledge Architecture specification.

## Approval

**Status:** Review — Pending Infrastructure Activation

**Founder:** Андрей Тихонов

**Owner:** Product Architecture

**Approval date:** __________________

**Decision reference:** __________________
