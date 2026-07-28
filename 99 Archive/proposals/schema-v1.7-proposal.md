# Schema v1.7 Proposal — эволюция метаданной схемы knowledge base

> **Расположение файла.** Запрошенный путь — `.knowledge/schema-v1.7-proposal.md`,
> но `scripts/validate_knowledge.py` сканирует все `**/*.md`, кроме частей пути из
> `IGNORED_PARTS = {".git", ".obsidian", ".venv", "__pycache__", "99 Archive"}`.
> Каталог `.knowledge/` в исключения не входит: любой `.md` там трактуется как
> knowledge node и без frontmatter даёт ошибку `missing YAML frontmatter`
> (проверено эмпирически 2026-07-27: probe-файл в `.knowledge/` дал 1 error).
> Поэтому proposal размещён в `99 Archive/proposals/` — единственном
> validator-exempt месте внутри репозитория. После owner approval
> рекомендуется добавить `.knowledge` в `IGNORED_PARTS` (см. п. 5 и 7) и
> перенести файл на канонический путь.

## 1. Purpose и статус

- **Статус:** `proposed` — ожидает owner approval по AYLA-DEC-0013
  (`02 Strategy/Ayla Decision Log.md`, запись «C-02: эволюция schema v1.6 →
  v1.7 (proposed) и границы доменных документов»).
- **Авторитетность:** schema v1.6 (текущая `.knowledge/schema.yaml`) остаётся
  авторитетной до approval. Validator и frontmatter трёх документов НЕ
  изменяются этим proposal. Interim-нормализация frontmatter Domain Context
  Map, Core Domain Model Specification и Data Inventory Matrix под v1.6 —
  временная мера, не прецедент.
- **Основание:** сравнительная таблица диалекта в AYLA-DEC-0013. Три
  документа написаны в повторяющемся метаданном диалекте; повторяемость
  трактуется как потребность в осознанной эволюции схемы.
- **После approval:** schema, validator, сгенерированный реестр и frontmatter
  трёх документов обновляются одним согласованным изменением (п. 6).

## 2. Proposed changes

### 2.1. Новые document types в `document_type_rules`

| Тип | normative | require_sections | Обоснование |
|---|---|---|---|
| `domain-context-map` | `true` | `Document Status and Purpose`, `Scope and Source Documents`, `Context Mapping Method`, `Domain Classification — Commentary` | Тип нормативной карты bounded contexts; секции соответствуют фактическим заголовкам `05 Architecture/Ayla Domain Context Map.md` (validator срезает числовые префиксы и сравнивает case-insensitively). `Change Log` в документе сейчас отсутствует — не включается (см. open question Q6). |
| `domain-specification` | `true` | — (отложено) | Core Domain Model Specification — намеренно пустой draft/proposed по DEC-0013; наполнение только после решения C-02. Требование секций сейчас сломало бы валидацию. require_sections добавляются follow-up изменением вместе с шаблоном документа (см. Q2). |
| `data-inventory-matrix` | `true` | `Purpose`, `Matrix`, `Definitions`, `Critical Boundaries`, `Change Log` | Секции соответствуют фактическим заголовкам `06 Safety and Governance/Data Inventory Matrix.md`. `Migration Notes` не требуется — раздел миграционный, может быть удалён после завершения миграции. |

Добавление типов обратно совместимо: старые типы
(`architecture-specification`, `specification`, `safety-specification`)
остаются в правилах; validator отклоняет только типы, отсутствующие в
`document_type_rules`.

### 2.2. Явные определения `owner` vs `system_owner`

Сейчас оба поля обязательны, но семантика не закреплена. Предлагается
добавить в schema секцию `field_definitions` (документационную, читается
людьми и генератором реестра):

- **`owner`** (string, required) — организационная роль, *accountable* за
  содержание, актуальность и ревью документа. Не система и не репозиторий.
- **`owners`** (list of strings, optional, informative) — все роли,
  разделяющие ответственность; `owner` — ведущая роль из этого списка.
  Информативное поле: не участвует в проверках полноты метаданных.
- **`system_owner`** (list from enum `system_owner`, required) —
  системы/репозитории, владеющие предметом документа. Не люди и не роли.

### 2.3. Правило для `owners`

- `owner` остаётся обязательным (`required_fields` не меняется).
- `owners` допустим как optional информативный массив (сейчас игнорируется
  как extra-поле; v1.7 легализует его).
- Предлагаемая consistency-проверка валидатора: если `owners` присутствует,
  `owner` должен входить в `owners` (иначе дрейф ведущей роли). Уровень
  severity — error или warning — open question Q3.

### 2.4. Отклонённые элементы диалекта

| Элемент диалекта | Решение | Обоснование |
|---|---|---|
| `source_kind: canonical-candidate` | **Отклонить** | `source_kind` описывает происхождение источника, а не зрелость. Претензия на канон уже выражается существующими средствами: `source_kind: canonical` + `canonical_status: candidate` (enum введён в schema 1.11) и/или `status`/`decision_status`. |
| `knowledge_area: domain` | **Отклонить** | Значение `domain-model` уже есть в enum `knowledge_area`; дублирование не нужно. Interim-нормализация (`domain` → `domain-model`) остаётся в силе. |
| `security_sensitivity: internal` | **Отклонить** | Смешение classification и sensitivity. Признак «внутреннее» несёт `classification: internal`; sensitivity нормализуется в enum none/low/medium/high/critical (interim: `low`). |
| `export_policy: internal-only` | **Отклонить** | Семантика «не экспортировать наружу» покрывается парой `classification: internal` + матрицей п. 2.5. Отдельное значение создало бы параллельную ось классификации. Interim-нормализация (`internal-only` → `full` по конвенции internal-документов) остаётся до активации экспорт-пайплайна (см. Q4). |

### 2.5. Матрица classification × export_policy (предложение)

| classification | Допустимые export_policy | Комментарий |
|---|---|---|
| `public` | `full`, `sanitized`, `metadata-only`, `prohibited` | Без ограничений (правило не добавляется). |
| `internal` | `full`, `sanitized`, `metadata-only`, `prohibited` | **Новое явное правило v1.7.** Все четыре значения допустимы; `full` — действующая конвенция для internal knowledge-документов. Правило делает матрицу тотальной и заменяет диалектное `internal-only`. |
| `confidential` | `sanitized`, `metadata-only`, `prohibited` | Существующее правило, без изменений. |
| `restricted` | `metadata-only`, `prohibited` | Существующее правило, без изменений. |

Перекрёстное правило (без изменений): `ai_indexing: denied` ⇒
`export_policy ∈ {metadata-only, prohibited}`; для `restricted` дополнительно
`ai_indexing ∈ {denied, metadata-only}`.

## 3. Предлагаемый diff схемы (фрагменты YAML v1.7)

Только изменяемые секции. Ключ `schema_changes` — см. open question Q1
(нумерация: DEC-0013 называет эволюцию «v1.7», счётчик `schema_version` в
schema.yaml уже на `1.11`).

```yaml
# schema_changes — добавить запись
  "1.12":  # "schema v1.7" по AYLA-DEC-0013; ключ уточняется в Q1
    - register domain-context-map, domain-specification and data-inventory-matrix document types
    - define owner vs system_owner semantics; allow optional informative owners array
    - make classification x export_policy matrix explicit for internal documents
```

```yaml
# новая секция (документационная)
field_definitions:
  owner: >-
    Accountable organizational role for the document content, its accuracy
    and review. Not a system and not a repository.
  owners: >-
    Optional informative list of all roles sharing responsibility. The
    required owner field names the leading (accountable) role and must be
    one of this list when the list is present.
  system_owner: >-
    Systems or repositories (from the system_owner enum) that own the
    subject matter of the document. Not people and not roles.
```

```yaml
# field_constraints — добавить
  owners:
    optional: true
    type: list
    unique_items: true
    must_contain_field: owner   # consistency rule; severity per Q3
```

```yaml
# conditional_rules — добавить
  internal:
    when:
      classification: internal
    allowed_export_policy:
      - full
      - sanitized
      - metadata-only
      - prohibited
```

```yaml
# document_type_rules — добавить
  domain-context-map:
    normative: true
    require_sections:
      - Document Status and Purpose
      - Scope and Source Documents
      - Context Mapping Method
      - Domain Classification — Commentary
  domain-specification:
    normative: true
    # require_sections намеренно отложены: документ — честный пустой draft
    # по AYLA-DEC-0013; секции добавляются вместе с шаблоном (Q2).
  data-inventory-matrix:
    normative: true
    require_sections:
      - Purpose
      - Matrix
      - Definitions
      - Critical Boundaries
      - Change Log
```

## 4. Migration impact

`node_id` всех документов **не меняются** (stable по `versioning.node_id`).
Откат interim-нормализации требуется **только для `type`**: остальные
interim-подстановки (`domain` → `domain-model`, `internal` → `low`,
`internal-only` → `full`) соответствуют отклонённым элементам диалекта
(п. 2.4) и остаются постоянными.

| Документ | node_id | Изменение frontmatter | Полей |
|---|---|---|---|
| `05 Architecture/Ayla Domain Context Map.md` | `ayla.domain.context-map` | `type: architecture-specification` → `domain-context-map`. `owners` сохраняется (становится легальным). | 1 |
| `05 Architecture/Ayla Core Domain Model Specification.md` | `ayla.domain.core-domain-model` | `type: specification` → `domain-specification`. Пустое тело остаётся валидным (require_sections отложены). | 1 |
| `06 Safety and Governance/Data Inventory Matrix.md` | `ayla.governance.data-inventory-matrix` | `type: safety-specification` → `data-inventory-matrix`. | 1 |
| `00 Foundation/Ayla Domain Capability Registry.md` | `ayla.foundation.domain-capability-registry` | Без изменений: документ не написан в новом диалекте (один `owner`, нет `owners`); `type: specification` корректен. Отдельный тип `capability-registry` — вне скоупа v1.7. | 0 |
| `00 Foundation/Ayla Repository Responsibility Matrix.md` | `ayla.foundation.repository-responsibility-matrix` | Обязательных изменений нет: `type: architecture-specification` корректен по существу; имеющийся `owners` становится легальным без правки. | 0 |

**Оценка объёма правок:** 3 строки frontmatter в 3 файлах; schema.yaml —
4 секции (см. п. 3); обязательная регенерация `00 Foundation/Ayla Domain
and Metadata Registry.md` через `scripts/render_domain_registry.py` (см.
п. 5); валидатор — 1–2 новые проверки; тесты — добавление кейсов.
Обновление `00 Foundation/Ayla Knowledge Architecture Specification.md`
(описание модели метаданных) — опциональный follow-up, вне скоупа
согласованного изменения.

## 5. Validator impact

Добавить/изменить в `scripts/validate_knowledge.py` (перечислением):

1. **Новые типы — без кода.** Проверка «unknown document type» читает
   `document_type_rules` из schema; после обновления schema новые типы
   принимаются автоматически. `require_sections` также обрабатывается
   generic-кодом `check_required_sections`.
2. **Новая проверка `owners`:** если поле присутствует — это список
   уникальных строк, содержащий значение `owner` (severity per Q3).
3. **Правило internal × export_policy:** либо hardcoded-проверка по образцу
   существующих `restricted`/`confidential`/`denied_ai_index` в
   `check_metadata`, либо (предпочтительно) небольшой рефакторинг:
   data-driven исполнение `allowed_export_policy`/`allowed_ai_indexing` из
   `conditional_rules` schema, чтобы матрица п. 2.5 жила только в schema.
4. **Реестр:** `scripts/render_domain_registry.py` регенерирует
   `00 Foundation/Ayla Domain and Metadata Registry.md` из schema
   (`generated_from`), обновляя встроенный `SOURCE_SHA256`. Проверить, что
   рендерер корректно обрабатывает новую секцию `field_definitions`
   (отрендерить или осознанно игнорировать).
5. **Опционально (рекомендуется):** добавить `.knowledge` в
   `IGNORED_PARTS`, чтобы governance-артефакты (включая этот proposal после
   переноса на запрошенный путь) не трактовались как nodes. См. Q5.

Влияние на `tests/` (`tests/test_validate_knowledge.py`, unittest,
импортирует функции валидатора напрямую):

- Добавить кейсы: новые типы принимаются; `data-inventory-matrix` требует
  секции (positive/negative); consistency `owners` ∋ `owner`; правило
  internal × export_policy (включая reject-кейс, если матрицу сделают
  строже по Q4).
- Существующие тесты не меняются (изменения аддитивны);
  `test_unknown_document_type_is_rejected` остаётся зелёным.
- `test_generated_domain_registry_matches_schema` станет красным, пока
  реестр не регенерирован, — поэтому регенерация входит в то же изменение.

## 6. Rollback plan и порядок внедрения

Внедрение — **одним согласованным изменением** (один commit/PR), как
зафиксировано в AYLA-DEC-0013 (шаг 5 порядка работ):

1. В Decision Log: статус schema-части AYLA-DEC-0013 `proposed` →
   `approved` + запись в Change Log документа.
2. `.knowledge/schema.yaml`: фрагменты п. 3.
3. `scripts/validate_knowledge.py`: проверки п. 5.
4. Регенерация реестра: `python scripts/render_domain_registry.py`.
5. Frontmatter трёх документов: смена `type` (п. 4).
6. Тесты: новые кейсы п. 5.
7. Приёмка: `python scripts/validate_knowledge.py` — 0 errors, warnings не
   выше текущих 24; `python -m unittest discover tests` — зелёный.

Если изменение всё же дробится: строгий порядок — schema+validator+реестр
сначала, frontmatter после (старые типы остаются в правилах, поэтому такой
порядок безопасен; обратный — frontmatter раньше schema — гарантированно
ломает валидацию трёх nodes).

**Rollback:** `git revert` одного согласованного коммита. Восстанавливает
schema v1.6, прежний validator, реестр и interim frontmatter — известное
зелёное состояние (0 errors). Миграции данных нет, `node_id` не меняются,
поэтому откат тривиален и не оставляет следов.

## 7. Open questions для владельца

- **Q1. Нумерация версии.** DEC-0013 называет эволюцию «v1.6 → v1.7», но
  `schema_version` в schema.yaml уже `1.11`. Следующий ключ `schema_changes`
  — `"1.12"` с отсылкой к DEC-0013, или выравнивание нумерации?
- **Q2. require_sections для `domain-specification`.** Определить сейчас
  (тогда пустой Core Domain Model упадёт до наполнения) или вместе с
  шаблоном документа после содержательного ревью (шаг 8 порядка работ
  DEC-0013)? Предложение: отложить.
- **Q3. Severity проверки `owners` ∋ `owner`.** Error (жёсткая
  консистентность) или warning (мягкий старт)?
- **Q4. Экспорт internal-документов.** Оставить конвенцию
  `export_policy: full` для internal knowledge-документов или при
  активации экспорт-пайплайна ужесточить матрицу для `internal`
  (например, исключить `full`)? Сейчас пайплайн не активирован.
- **Q5. `.knowledge/` в `IGNORED_PARTS`.** Добавить в рамках v1.7, чтобы
  proposal-файлы могли жить в `.knowledge/` (текущий validator подхватывает
  `.knowledge/*.md` как nodes — подтверждено probe-тестом)? Если да, этот
  файл переносится на `.knowledge/schema-v1.7-proposal.md` тем же
  изменением.
- **Q6. Change Log в Domain Context Map.** В документе нет раздела
  `Change Log` (отклонение от стиля большинства normative-типов). Добавить
  раздел в документ и в `require_sections` тем же изменением или отдельно?
- **Q7. canonical_status трёх документов.** Проставить
  `canonical_status: candidate` (или оставить default `draft`) при
  миграции на v1.7? В скоуп согласованного изменения или отдельно?
