---
node_id: ayla.governance.data-inventory-matrix
title: Data Inventory Matrix
type: data-inventory-matrix
status: draft
version: "1.0"
owner: Safety and Governance Domain
knowledge_area:
  - safety-governance
system_owner:
  - ayla-knowledge
source_repository: ayla-knowledge
created: 2026-07-24
updated: 2026-07-24
source_kind: canonical
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: medium
ai_indexing: metadata-only
export_policy: sanitized
review_cycle: quarterly
reviewers: []
tags: [data-governance, memory-ownership, data-inventory, privacy]
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Glossary]]"
---

# Data Inventory Matrix

## Purpose

Этот документ фиксирует классы данных в системе Ayla, их владельцев, источники истины и правила обработки. Цель — устранить противоречия во владении памятью и обеспечить соответствие privacy requirements.

## Matrix

| Class of Data | Data Subject | Normative Domain / System Owner | Physical Custodian | Source of Truth | Permitted Consumers | Write Authority | Consent / Purpose | Retention & Deletion Orchestrator | Temporary Projections Rules |
|---------------|--------------|--------------------------------|--------------------|-----------------|---------------------|-----------------|-------------------|-----------------------------------|----------------------------|
| Account / Profile | User | User Context Domain (`ayla-user-context`) | W2 Profile Service | W2 Profile Service | W3 Memory, Wellness, Consent, Notification | W2 only | Account creation purpose | W2 on user request or account closure | Allowed for UI rendering; no persistent storage outside W2 |
| Operational Preferences | User | User Context Domain | W2 Preferences Service | W2 Preferences Service | W3 Memory, Wellness, Notification (read-only) | W2 only | Service operation purpose | W2 on preference change or account closure | Allowed for session caching with TTL; must refresh from source on invalidation |
| Consent Records | User | Consent Domain | Consent Service | Consent Service | All domains (read-only for gating via authoritative cache with TTL) | Consent Service only | Explicit consent capture | Consent Domain per legal requirements; orchestrates deletion requests | Not allowed as independent source; authoritative cache with TTL and invalidation required |
| Semantic Memory (MemoryEntry) | User | W3 Memory & Identity Domain | W3 Memory Service | W3 Memory Service (after gate) | Approved consumers via purpose-limited API | W3 only (via proposal/consent/purpose gate) | Requires explicit consent + purpose approval | W3 privacy flow on user request | Not allowed; memory is persistent, not projected |
| Raw Wellness History | User | Wellness Domain | Wellness Service | Wellness Service | W3 Memory (for derivation), Dashboards (read-only) | Wellness Service only | Wellness tracking purpose | Wellness Domain per retention policy | Allowed for dashboards, summaries, API views; marked as derived |
| Wellness-Derived Memory | User | W3 Memory & Identity Domain | W3 Memory Service | W3 Memory Service (after memory gate) | Approved consumers via purpose-limited API | W3 only (via memory gate) | Requires consent + memory proposal approval | W3 privacy flow on user request | Not allowed; becomes semantic memory after gate |
| Purpose-Limited Projections | User | Varies by source domain | Consumer-specific cache | Source domain (live) | Specific consumer only | No write authority; read-through only | Inherited from source + consumer purpose | Session lifetime or consumer-defined (must not exceed source retention) | Must be marked as temporary; cannot be persisted as memory |
| Notification Preferences | User | Notification Preferences Domain | Notification Service | Notification Service | Communication systems (read-only) | Notification Service only | Communication consent | Notification Domain on preference change | Allowed for delivery queue caching |
| Marketing Opt-Out | User | Consent Domain | Consent Service | Consent Service | Marketing systems (read-only for gating) | Consent Service only | Marketing consent (or lack thereof) | Consent Domain per legal requirements | Not allowed; must check live or via authoritative cache |
| Customer Service Preferences | User | User Context Domain | W2 Preferences Service | W2 Preferences Service | Substitute (booking-specific projection only) | W2 only | Booking purpose | W2 per booking lifecycle | Allowed only as booking-specific purpose-limited projection; never as MemoryEntry copy |

## Definitions

### Data Subject
Пользователь (end user), чьи данные обрабатываются в системе.

### Normative Domain / System Owner
Домен или система, несущая ответственность за семантику, политику и жизненный цикл данных.

### Physical Custodian
Сервис или хранилище, физически хранящее данные в данный момент.

### Source of Truth
Единственный авторитетный источник для данного класса данных. Все другие копии являются производными (projections) и должны синхронизироваться с источником.

### Permitted Consumers
Список доменов или сервисов, которым разрешено читать данные.

### Write Authority
Кто имеет право создавать, обновлять или удалять данные этого класса.

### Consent / Purpose
Требуемое согласие и цель обработки для данного класса данных.

### Retention & Deletion Orchestrator
Компонент, ответственный за соблюдение сроков хранения и выполнение запросов на удаление.

### Temporary Projections Rules
Правила создания временных проекций (кэшей, представлений, summary) для данного класса данных.

## Critical Boundaries

1. **W2 не владеет semantic memory.** W2 является владельцем account/profile и operational preferences, но не параллельной semantic memory.

2. **Raw wellness history ≠ memory.** Сырые измерения и история остаются в Wellness Domain. Персонализированные выводы становятся памятью только после прохождения memory gate в W3.

3. **Consent — отдельный источник истины.** Согласия не дублируются в других доменах; все системы проверяют consent live через Consent Service.

4. **Projections не являются памятью.** Временные проекции (dashboards, summaries, API views, booking-specific views) не становятся MemoryEntry без прохождения proposal/consent/purpose gate.

5. **Offboarding не переносит и не удаляет память.** Завершение сотрудничества (например, master offboarding) меняет access grants, но не владельца памяти. Удаление памяти возможно только через отдельный пользовательский privacy request через W3 privacy flow.

6. **Conversations и internal chat не создают память автоматически.** Создание MemoryEntry из разговоров возможно только через отдельный W3 proposal/consent/purpose gate.

7. **Master не имеет прямого доступа к semantic memory.** Master видит только разрешённую purpose-limited projection. Прямое чтение, редактирование, удаление или экспорт semantic memory запрещены.

## Migration Notes

Этот документ не меняет существующие API shapes или runtime-поведение. Он фиксирует существующие границы и требует постепенного приведения реализации в соответствие с зафиксированной моделью.

Изменения кода, моделей, API и миграций выполняются в отдельных циклах после утверждения этой модели.

## Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-07-24 | Safety and Governance Domain | Initial draft created per memory ownership reconciliation plan |
