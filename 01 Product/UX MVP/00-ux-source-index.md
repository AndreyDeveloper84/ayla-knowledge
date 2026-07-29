---
node_id: ayla.ux.source-index
title: UX Source Index
type: moc
status: draft
version: "0.2"
owner: UX Architecture
knowledge_area:
  - product
domain:
  - cross-domain
system_owner:
  - ayla-knowledge
source_repository: ayla-knowledge
source_kind: product-requirements
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

# UX Source Index

Единый индекс источников для UX-работы. Агенты сначала читают этот индекс,
затем открывают только нужные разделы перечисленных документов.
Запрещено читать документы «на всякий случай».

| ID | Документ | Путь | Владеет | Статус | Когда читать |
|---|---|---|---|---|---|
| SRC-01 | Ayla MVP Scope and Release Contract v0.3 | `Ayla/ayla-knowledge/02 Strategy/` | Границы MVP | draft, change control через AYLA-DEC | Классификация экранов MVP/NEXT/LATER (§3–5, §7, §10) |
| SRC-02 | Ayla MVP User Journey Specification | `Ayla/ayla-knowledge/01 Product/User Journeys/` | Этапы journey пилота | approved-track | Построение flows (Stage 1–14, Negative N1–N9, Memory Interaction) |
| SRC-03 | Ayla User Journey Specification (полная) | `Ayla/ayla-knowledge/01 Product/User Journeys/` | Journey за пределами MVP | approved-with-amendments | Только если MVP-спека ссылается; не для MVP inventory |
| SRC-04 | Ayla Intent Model Specification v0.9.2 | `Ayla/ayla-knowledge/03 AI System/` | Intent, slots, clarification | v0.9.2 owner-approved | Conversation UX, экраны уточнения, safety-sensitive intents |
| SRC-05 | Consent Scope Registry | `Ayla/ayla-knowledge/06 Safety and Governance/` | Consent scopes (7 шт.) | normative | Любой экран с персональными данными, памятью, рекомендациями (§5, §7, §8 UX Requirements) |
| SRC-06 | Ayla Decision Log | `Ayla/ayla-knowledge/02 Strategy/` | Owner decisions AYLA-DEC-0001+ | canonical | Перед любым предположением — проверить, нет ли решения |
| SRC-07 | Ayla Constitution v2.2 | `Ayla/ayla-knowledge/00 Foundation/` | Права пользователя, границы | approved 2026-07-16 | Спорные UX-решения: память, вето, объяснение, монетизация |
| SRC-08 | ADR-0012 Dynamic User Model | `Ayla/ayla-knowledge/05 Architecture/` | Memory lifecycle | accepted | Memory-зависимости экранов |
| SRC-09 | Consent export/forget: AMD-020 C5 | `Ayla/ayla-knowledge/05 Architecture/` | Export/forget contract | accepted-track | Экраны приватности, удаление данных |
| SRC-10 | Data Inventory Matrix | `Ayla/ayla-knowledge/06 Safety and Governance/` | Категории данных | normative | required_data экрана, допустимость показа actor-у |
| SRC-11 | Domain Capability Registry | `Ayla/ayla-knowledge/00 Foundation/` | owning_capabilities | normative | Поле owning_capabilities в Screen Contract |
| SRC-12 | Customer screen specs (10 файлов, 2026-05) | `ai-bot-platform/docs/screens/customer-*.md` | Существующие драфты UX | **draft, stale** (pilot 15.07 → канон 15.08) | Материал ревизии для inventory, НЕ канон |
| SRC-13 | Design policies | `ai-bot-platform/docs/design/policies/` | Voice, consent UX, memory UX | draft | Voice patterns, privacy UX, gated flows |
| SRC-14 | PROJECT_INDEX 2026-07-18 | `Ayla/djangoproject/docs/` | Снимок экосистемы, Decision Log зеркало до DEC-0010 | snapshot | Только контекст интеграций; решения сверять с SRC-06 |
| SRC-15 | MVP Roadmap 2026-07 | `Ayla/djangoproject/docs/` | Этапность, потоки S1–S7 | **partially stale** (Telegram → устарел, D4 = MAX) | Критический путь пилота; канал сверять с D4 |
| SRC-16 | Ayla MVP Recommendation Contract v0.3 (CANON) | `Ayla/ayla-knowledge/05 Architecture/` | Product Architecture | v0.3, draft/proposed, canonical | Рекомендационные правила — читать всегда при работе с SCR-CUST-004/005/006 (§3–4, §9–10, §13–15, §18–20, §22–23); UX-слой — `contracts/recommendation-ux-addendum.md` |

## Правила использования

- Конфликт источников: SRC-06 (Decision Log) > SRC-07 (Constitution) > SRC-01 > SRC-02 > остальное. SRC-12–SRC-15 никогда не побеждают канон.
- По recommendation-домену: SRC-16 (CANON) — source of truth доменной семантики; UX-документы (addendum, Screen Contracts) не дублируют его, а ссылаются (результат UX-RECON-001, вариант B).
- Каждая ссылка в UX-документах — как `SRC-XX §раздел`, не пересказ содержимого.
- Новый источник добавляется в индекс только с полем «Когда читать».
