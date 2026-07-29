---
node_id: ayla.foundation.canon-governance.owner-decision-register
title: OWNER_DECISION_REGISTER
type: dashboard
status: draft
version: "0.1"
owner: Product Owner
knowledge_area:
  - foundation
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

# OWNER_DECISION_REGISTER

Реестр решений владельца продукта. Пуст при инициализации. Старые решения (включая `02 Strategy\Ayla Decision Log.md` и `AYLA-DEC-0011`) не импортируются автоматически.

## Правила

- Approved Owner Decisions обязательны к применению строго в пределах указанного в них scope.
- Owner Decision не может неявно переопределять Product Essence.
- Owner Decision создаётся только если после проверки по лестнице разрешения (см. `CANON_CONFLICT_REGISTER.md`) остаются минимум два разумных варианта, materially меняющих: продукт, MVP, главный journey, обязательства, safety/privacy, критический контракт или срок выпуска.

## Формат записи

```text
ID:             AYLA-DEC-XXXX
Date:           YYYY-MM-DD
Question:       —
Options:        —
Decision:       —
Rationale:      —
Scope:          — (точные границы применения)
Affected docs:  —
Status:         OPEN | DECIDED | SUPERSEDED
```

## Записи

### AYLA-DEC-0026 — Living Digital Twin as Ayla's Primary Visual Interface

```text
ID:             AYLA-DEC-0026
Date:           2026-07-29
Question:       Каково место Living Digital Twin в продукте Ayla?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Living Digital Twin является главным визуальным интерфейсом Ayla
                и долгоживущим цифровым отражением самого пользователя.
Rationale:      см. полный текст ruling (Recognition, Identity Preservation, Authentic Future)
Scope:          Product Essence v1.1; Living Digital Twin Manifesto; Product Vision;
                Product Thesis; Product Principles; MVP Scope; MVP User Journey;
                последующие Domain, UX, AI, Privacy/Safety и Engineering документы.
Affected docs:  Essence v1.1 (CREATE), LDT Manifesto (CREATE after v1.1 approval),
                пять Foundation-документов, реестры Canon Governance.
Status:         DECIDED
```

Каноническая запись решения:

> Living Digital Twin является главным визуальным интерфейсом Ayla и долгоживущим цифровым отражением самого пользователя. Его обязательное свойство — сохранение узнаваемой идентичности. Человек остаётся главным героем продукта, Transformation Goal — центральной доменной сущностью, Ayla — интеллектуальным помощником и оркестратором пути. Ayla показывает не усреднённый идеальный образ, а правдоподобные изменения именно этого человека и ясно разделяет фактическое состояние, реконструкцию, прогноз и цель.

Разделение центров:

```text
Продуктовая ценность: человек
Главный визуальный интерфейс: Living Digital Twin
Центральная доменная сущность: Transformation Goal
Интеллектуальная координация: Ayla
```

Примечание по ID: предпочтительный `AYLA-DEC-0012` занят в `02 Strategy\Ayla Decision Log.md` (owner directions по Domain Capability Registry); по правилу ruling использован следующий свободный — `AYLA-DEC-0026` (Decision Log занимает диапазон до `AYLA-DEC-0025`).

Источник: `D:\Проекты\Ayla\OWNER_RULING_LIVING_DIGITAL_TWIN_PRIMARY_VISUAL_INTERFACE.md` (owner ruling, 2026-07-29). Owner Decision не переопределяет Product Essence; изменение Essence выполняется через подготовку v1.1 с отдельным owner approval.
