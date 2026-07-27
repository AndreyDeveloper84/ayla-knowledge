---
node_id: ayla.root
title: Ayla
type: moc
status: review
activation_status: pending-infrastructure
version: "1.2"
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
created: 2026-07-18
updated: 2026-07-18
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
  - ayla/root
  - ayla/foundation
  - type/moc
  - priority/p0
implements: []
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Knowledge Architecture Specification]]"
related:
  - "[[Ayla Decision Log]]"
supersedes: []
review_cycle: monthly
migration_source:
  repository: beautygo_backend
  commit: 88a66515
  path: docs/Ayla.md
  sha256: f72354e53dd8a54ffebf83384838eeb34ebd1cac9045027cc7b05061f15e38ca
  imported: 2026-07-18
---

# Ayla

Единая точка входа в канонические продуктовые, архитектурные и операционные
знания Ayla.

Этот файл отвечает на четыре вопроса:

1. Что прочитать в первую очередь?
2. Какие документы уже являются каноническими?
3. Где находится источник решения?
4. Какие документы мигрируются следующими?

## Start Here

Обязательный порядок первого чтения:

1. [[Ayla Constitution]]
2. [[Ayla Knowledge Architecture Specification]]
3. [[Ayla Decision Log]]
4. Этот Root MOC

До перевода документа в `approved` его каноничность определяется
frontmatter и validator output, а не наличием файла в vault.

## Current Canonical Set

Reviewed nodes (прошли перенос и проверку):

| Document | Version | Status | Authority |
|---|---:|---|---|
| [[Ayla Constitution]] | 2.2 | approved | фундаментальные права, принципы и ограничения |
| [[Document Quality Bar (W7)]] | 1.0 | approved | планка качества документов |
| [[Ayla Knowledge Architecture Specification]] | 1.4 | review / pending infrastructure | управление knowledge repository |
| [[Ayla Decision Log]] | 0.4 | review / pending infrastructure | межрепозиторные решения Founder |
| [[Ayla Glossary]] | 2.1 | review / pending infrastructure | терминологический стандарт |
| [[Ayla Domain and Metadata Registry]] | 1.0 | review / pending infrastructure | карта schema и ownership |
| [[Ayla Product Vision]] | 1.4 | review / pending infrastructure | видение продукта и сегменты |
| [[Ayla User Journey Specification]] | 1.2 | review / pending infrastructure | experience contract |
| [[Ayla]] | 1.2 | review / pending infrastructure | навигация и migration state |

Draft / proposed nodes (в vault, НЕ канон; approval ограничен AYLA-DEC-0011):

| Document | Version | Status | Назначение |
|---|---:|---|---|
| [[Ayla MVP Product Thesis]] | 0.4 | draft | product scope и economic boundaries |
| [[Killer PRD]] | 1.4.1 | draft / proposed | killer flow и память |
| [[ADR-0012 Dynamic User Model]] | 0.2 | draft / proposed | динамическая модель пользователя |
| [[AMD-020 C5 Implementation Amendment]] | 0.8 | draft / proposed | поправка реализации C5 |
| [[AMD-020 C5 Pilot Personal Context Export-Forget Contract]] | 0.8 | draft / proposed | export/forget контракт |
| [[AMD-020 Pilot Scope Registry]] | 0.3 | review / proposed | memory ownership alignment |
| [[Ayla Domain Context Map]] | 1.0 | draft / proposed | DDD-методология и контексты |
| [[Ayla Core Domain Model Specification]] | 1.0 | draft / proposed | заглушка, требует наполнения |
| [[Ayla Domain Capability Registry]] | 1.2 | draft / proposed | реестр capabilities (AYLA-DEC-0012) |
| [[Ayla Repository Responsibility Matrix]] | 0.1 | draft / proposed | ответственность репозиториев |
| [[Consent Scope Registry]] | 0.5 | draft | scope согласий |
| [[Data Inventory Matrix]] | 1.0 | draft | классы данных и владение |

Таблицы отражают фактическое состояние vault и не считаются
release bundle.

## Decision Hierarchy

При чтении документов применяется следующий порядок:

1. Ayla Constitution.
2. Действующие записи [[Ayla Decision Log]] — в пределах scope конкретного
   решения.
3. Утверждённые cross-product policies и Foundation specifications.
4. Accepted ADR — только в пределах decision scope конкретного ADR.
5. Утверждённые domain и product specifications.
6. API-, event- и implementation contracts.
7. Plans, research, handoff и working notes.

Более свежая дата не создаёт автоматического приоритета.

Если код расходится с документом:

- код является источником фактического текущего поведения;
- канонический документ является источником утверждённого намерения и
  ограничений;
- расхождение фиксируется явно;
- изменение intent выполняется через Decision Log, amendment или ADR;
- документ не исправляется задним числом так, будто конфликта не было.

## Repository Map

Корень репозитория является корнем Obsidian vault.

| Path | Назначение |
|---|---|
| `00 Foundation/` | Constitution, Glossary, knowledge governance |
| `01 Product/` | product thesis, PRD, journeys и metrics |
| `02 Strategy/` | strategy, roadmap и portfolio decisions |
| `03 AI System/` | intent, recommendation, orchestration, memory и evaluation |
| `04 Domain Models/` | identity, provider, booking, payment и другие bounded contexts |
| `05 Architecture/` | cross-system architecture и ADR navigation |
| `06 Safety and Governance/` | safety, privacy, security и compliance |
| `07 Design/` | UX principles и design system |
| `08 Business/` | economic model и commercial constraints |
| `09 Research/` | evidence и research artifacts |
| `10 Operations/` | runbooks, incidents и release operations |
| `90 Sources/` | external sources и generated mirrors |
| `99 Archive/` | deprecated и superseded material после retention gate |
| `.knowledge/` | schema и sync manifest |

Папка не определяет ownership. Источник и ответственность задаются metadata.

## System Map

| Repository | Роль |
|---|---|
| `ayla-knowledge` | cross-product foundations, governance, MOC и общая терминология |
| `beautygo_backend` | booking, payments, catalog, identity и backend contracts |
| `ai-bot-platform` | conversation, channels, memory integration и AI backbone |
| `ayla-ai-core` | intent, recommendation, orchestration и evaluation library |

Implementation-local документ остаётся каноническим в owning repository и
подключается сюда как read-only mirror.

## Migration Queue

Мигрировано 2026-07-19 — 2026-07-27: Ayla Glossary, Ayla Domain and
Metadata Registry, Ayla Product Vision, Ayla MVP Product Thesis, Ayla
User Journey Specification, Consent Scope Registry, Ayla Repository
Responsibility Matrix, Ayla Domain Context Map (draft), Ayla Core Domain
Model Specification (draft-заглушка), Ayla Domain Capability Registry
(draft), Data Inventory Matrix (draft).

Текущая очередность:

| Order | Document | Reason | Intended outcome |
|---:|---|---|---|
| 1 | Ayla Intent Model Specification | единственный отсутствующий predecessor по AYLA-DEC-0011; блокирует approval Capability Registry и Context Map | reviewed canonical node |
| 2 | Area MOC | завершить навигацию по заполненным областям | validated navigation |

Название в очереди не создаёт Knowledge Node и не означает approval.

## Agent Workflow

### Перед изменением кода

Агент обязан:

1. получить список документов, обязательных для задачи;
2. прочитать их до анализа кода;
3. указать применимые статьи Constitution, ADR и contracts;
4. проверить, не конфликтует ли задача с каноническим решением;
5. остановить реализацию при неразрешённом нормативном конфликте.

### При конфликте

Запрещено молча выбирать код или документ.

Допустимые результаты:

- код исправляется в соответствии с действующим contract;
- создаётся запись [[Ayla Decision Log]];
- создаётся или изменяется ADR;
- выпускается amendment или новая semantic version;
- задача блокируется до решения владельца.

### После изменения кода

Приёмка проверяет:

- реализацию против Constitution и профильных contracts;
- обновление implementation evidence;
- отсутствие незадокументированных отклонений;
- необходимость обновить ADR, Decision Log, runbook или API contract.

## Document Change Workflow

Для изменения knowledge repository:

1. выполнить pull актуального `main`;
2. создать отдельную branch;
3. менять один логический документ или согласованный batch;
4. провести review на противоречия, полноту и полезность;
5. запустить:

```powershell
python scripts/validate_knowledge.py
python -m unittest discover -s tests -v
```

6. показать findings и diff до push;
7. выполнить merge или direct push только после явного подтверждения;
8. проверить remote commit SHA и CI.

P0 Foundation, Constitution, safety и privacy требуют профильного review.

## Governance Status

| Capability | State |
|---|---|
| Separate `ayla-knowledge` repository | active |
| Stable filenames and `node_id` | active |
| Schema | active, v1.11 |
| Local validator | active |
| Validator tests | active |
| GitHub Actions workflow | configured; remote status requires verification |
| Branch protection / CODEOWNERS | not configured |
| Manifest-driven mirrors | specified, disabled |
| Root and area MOC coverage | in progress |
| AI export pipeline | not activated |

Knowledge Architecture и Root MOC сохраняют
`activation_status: pending-infrastructure`, пока не выполнен их activation
plan.

## Search Order

Рекомендуемый порядок поиска:

```text
Root MOC
→ area MOC
→ full-text search
→ metadata filters
→ backlinks
→ Graph View
```

Graph View помогает исследовать связи, но не определяет authority.

## Review Checklist

Root MOC готов к approval, когда:

- Start Here содержит только существующие nodes;
- Current Canonical Set соответствует validator output;
- migration queue имеет owner или порядок review;
- repository и system maps не смешивают navigation с ownership;
- agent workflow принят для code/document reconciliation;
- governance status проверен по фактическому repository state;
- ссылки разрешаются без migration warnings.

## Change Log

### v1.2 — 2026-07-27

- Current Canonical Set синхронизирован с фактическим состоянием vault
  и разделён на reviewed nodes и draft/proposed nodes;
- Migration Queue очищена от выполненного (Glossary, Domain and Metadata
  Registry, Product Vision, MVP Product Thesis, User Journey
  Specification и другие мигрированы 2026-07-19 — 2026-07-27);
- актуальная очередь: Ayla Intent Model Specification (predecessor по
  AYLA-DEC-0011), Area MOC;
- версии Decision Log (0.4) и Knowledge Architecture Specification (1.4)
  актуализированы; Document Quality Bar и Product Vision добавлены в
  reviewed set.

### v1.1 — 2026-07-18

- Root MOC перенесён в отдельный `ayla-knowledge`;
- versioned links заменены стабильными canonical links;
- удалён устаревший milestone `Intent and Recommendation design`;
- фактический canonical set отделён от migration queue;
- добавлены repository map, system map и agent workflow;
- governance status приведён к текущему состоянию;
- зафиксирован migration provenance из `beautygo_backend@88a66515`;
- Decision Log добавлен в Start Here, canonical set и decision hierarchy;
- завершённый перенос Decision Log удалён из migration queue;
- schema status обновлён до v1.6.

### v1.0 — 2026-07-18

- создана первая Root MOC в staging knowledge tree.

## Approval

**Status:** Review — Pending Infrastructure Activation

**Owner:** Product Architecture

**Approval date:** __________________

**Decision reference:** __________________
