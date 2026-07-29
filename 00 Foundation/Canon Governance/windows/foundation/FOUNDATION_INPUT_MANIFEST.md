---
node_id: ayla.foundation.canon-governance.foundation-input-manifest
title: FOUNDATION_INPUT_MANIFEST
type: specification
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

# FOUNDATION_INPUT_MANIFEST

Входной манифест Foundation Canon Window. KB = `C:\Users\user\PycharmProjects\Ayla\ayla-knowledge`. Канонические рабочие версии двух высших источников хранятся в KB; копии на `D:\Проекты\Ayla` — внешние исходные, non-authoritative.

## REQUIRED

```text
KB\00 Foundation\Ayla Product Essence.md              — высший продуктовый источник (CANONICAL)
KB\02 Strategy\Ayla MVP Reset Roadmap.md              — операционный источник (CANONICAL)
KB\01 Product\Ayla Product Vision.md                  — кандидат Product Vision
KB\02 Strategy\Ayla MVP Product Thesis.md             — кандидат Product Thesis
KB\01 Product\User Journeys\Ayla MVP User Journey Specification.md — кандидат MVP User Journey
```

## OPTIONAL IF CONFLICT

```text
KB\02 Strategy\Ayla MVP Scope and Release Contract.md — legacy-вход; новый MVP Scope создаётся from new canon
KB\02 Strategy\Killer PRD.md                          — LEGACY REFERENCE ONLY
D:\Проекты\Ayla\Killer_PRD_v1.1_RU.md                 — LEGACY REFERENCE ONLY
KB\00 Foundation\Ayla Constitution.md                 — conditional reference (ограничения), не шаблон Principles
KB\00 Foundation\Ayla Glossary.md                     — при терминологических конфликтах
KB\00 Foundation\Document Quality Bar (W7).md         — критерий качества при финализации
KB\02 Strategy\Ayla Decision Log.md                   — поиск ранее принятых решений; без автоимпорта
KB\01 Product\User Journeys\Ayla User Journey Specification.md — предшествующая версия Journey
D:\Проекты\Ayla\Ayla_Product_Vision.md (+ дубликат "(1)")      — cross-location сверка версий Vision
D:\Проекты\Ayla\Ayla_MVP_Product_Thesis.md (+ "(1)", "(2)")    — cross-location сверка версий Thesis
D:\Проекты\Ayla\Ayla_User_Journey_v1.0_FINAL_FULL.md           — cross-location сверка версий Journey
```

## DO NOT LOAD

```text
KB\00 Foundation\Ayla Domain Capability Registry.md
KB\00 Foundation\Ayla Domain and Metadata Registry.md
KB\00 Foundation\Ayla Knowledge Architecture Specification.md
KB\00 Foundation\Ayla Repository Responsibility Matrix.md
KB\01 Product\UX MVP\** (весь каталог)
KB\03 AI System\**, KB\05 Architecture\**, KB\06 Safety and Governance\**
KB\99 Archive\**, KB\scripts\**, KB\tests\**
D:\Проекты\Ayla\Ayla_Product_Essence_v1.0.md — внешняя исходная копия, non-authoritative
D:\Проекты\Ayla\Ayla_MVP_Reset_Roadmap.md    — внешняя исходная копия, non-authoritative
D:\Проекты\Ayla — всё остальное: Constitution v2.0/v2.1, все .docx и .ini,
Consent_Scope_Registry* (все версии), Domain-документы, schema-v1.2*,
repomix-output.xml, каталог aibot, изображения, Killer_PRD.md (устаревшая),
Glossary v1.1_REVIEW, «Объяснение сложных терминов»
```
