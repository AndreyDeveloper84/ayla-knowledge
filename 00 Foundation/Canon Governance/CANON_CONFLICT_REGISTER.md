---
node_id: ayla.foundation.canon-governance.canon-conflict-register
title: CANON_CONFLICT_REGISTER
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

# CANON_CONFLICT_REGISTER

Реестр конфликтов между документами канона. Пуст при инициализации.

## Лестница разрешения P0

P0 не равен Owner Decision автоматически. Каждый P0 сначала проверяется на разрешимость через (по порядку):

1. Product Essence;
2. утверждённые Owner Decisions;
3. удаление или замену legacy-положения;
4. явную границу MVP / post-MVP;
5. более простое обратимое решение;
6. редакционное или структурное исправление.

Owner Decision создаётся только если после всех шагов остаются минимум два разумных варианта, materially меняющих продукт, MVP, главный journey, обязательства, safety/privacy, критический контракт или срок выпуска.

## Формат записи

```text
ID:              CFT-XXX
Severity:        P0 | P1
Documents:       —
Contradiction:   —
Ladder result:   RESOLVED_BY_<step> | ESCALATE_TO_OWNER
Resolution path: AUTO | OWNER_DECISION (ссылка на AYLA-DEC-XXXX)
Status:          OPEN | RESOLVED | ESCALATED
```

## Записи

(нет записей)
