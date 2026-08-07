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
updated: 2026-08-07
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

### CFT-001 — Duplicate `node_id` for MVP User Journey v1.2 candidate and approved v1.1

```text
ID:              CFT-001
Severity:        P0
Documents:       Ayla MVP User Journey Specification v1.2 (draft/proposed/candidate);
                 approved_v1_1.md / Ayla MVP User Journey Specification v1.1 (approved)
Contradiction:   Оба документа объявляют `node_id: ayla.product.mvp-user-journey`.
                 `Ayla Domain and Metadata Registry` v1.0 §9 и `.knowledge/schema.yaml`
                 field_constraints.node_id требовали `unique: true`. Validator
                 `scripts/validate_knowledge.py` фиксировал duplicate node_id.
Ladder result:   RESOLVED_BY_RULE_CHANGE
Resolution path: OWNER_DECISION — Variant C adopted (Active Canon scoped uniqueness)
Status:          RESOLVED
```

Прохождение по лестнице разрешения P0:

1. **Product Essence** — не разрешает коллизию `node_id`;
2. **Утверждённые Owner Decisions** — не разрешают: AYLA-DEC-0026…0036 и
   AYLA-DEC-0037…0054 не касаются metadata-регистрации редакций;
3. **Удаление legacy-положения** — неприменимо: approved v1.1 остаётся
   действующим canonical документом;
4. **Граница MVP / post-MVP** — неприменима: обе редакции относятся к одному
   Knowledge Node внутри MVP;
5. **Более простое обратимое решение** — отсутствует: любое разрешение
   (смена `node_id` у v1.2, `supersedes` v1.1, архивация v1.1, изменение
   `schema.yaml`) требует owner approval и влияет на canonical lineage;
6. **Редакционное или структурное исправление** — недостаточно: правило
   `node_id: unique: true` зафиксировано в DMR v1.0 и schema.yaml.

Необходимое owner decision: выбрать один из вариантов и канонизировать его:

- (A) Присвоить v1.2 новый `node_id` (например, `ayla.product.mvp-user-journey.v1-2`)
  — потребует изменения `.knowledge/schema.yaml` или принятия исключения;
- (B) Перевести approved v1.1 в `superseded`/`archived` при одобрении v1.2;
- (C) Изменить правило `node_id: unique: true` в DMR/schema.yaml, разрешив
  co-existing редакциям одного Knowledge Node иметь общий `node_id`;
- (D) Другое явное canonical rule, регламентирующее редакции.

До принятия решения оба документа сохраняют текущие frontmatter без изменений
(см. targeted follow-up instruction #4).

**Resolution (2026-08-05):**

- Принят Variant C: `node_id` идентифицирует Knowledge Node, а не конкретную редакцию.
- Уникальность `node_id` и `title` перенесена с глобальной на множество Active Canon revisions.
- Active Canon — revision со `source_kind: canonical` и `status` из множества `approved`, `approved-with-amendments`, `implemented`, `delivered`.
- Исторические редакции (draft, candidate, superseded, archived и др.) могут сосуществовать с Active Canon.
- Изменены: `.knowledge/schema.yaml` v1.13, `Ayla Domain and Metadata Registry.md`, `scripts/validate_knowledge.py`.
- `scripts/validate_knowledge.py` после изменений проходит без ошибок; Journey v1.1 (approved) и Journey v1.2 (candidate) больше не конфликтуют.

### CFT-002 — LDT Manifesto §14 claimed authority over exact MVP scope, conflicting with OD-MVP-1

```text
ID:              CFT-002
Severity:        P0
Documents:       Ayla Living Digital Twin Manifesto v1.0 §14 ("MVP обязан
                 проверить жизнеспособность Living Digital Twin");
                 Owner Decisions AYLA-DEC-0063 (OD-MVP-1) — LDT excluded
                 from mandatory first-MVP critical path
Contradiction:   Manifesto §14 нормативно утверждал обязательность LDT для
                 любого MVP — прямое противоречие AYLA-DEC-0063, принятому
                 позже (2026-08-07). §14 claimed authority over exact MVP
                 scope, что запрещено LDT ownership rule этой канонизации
                 (документы, посвящённые непосредственно LDT, не
                 переписываются автоматически под representation-neutral
                 model, но если документ claims authority over exact MVP
                 scope — конфликт фиксируется и предлагается minimal
                 amendment).
Ladder result:   RESOLVED_BY_OWNER_DECISION
Resolution path: OWNER_DECISION (AYLA-DEC-0063 / OD-MVP-1) — minimal
                 targeted amendment: §14 первое предложение сделано
                 условным («если LDT включён в релиз»); остальные 17
                 разделов Manifesto не переоткрывались.
Status:          RESOLVED
```

Прохождение по лестнице разрешения P0:

1. **Product Essence** — разрешает: Essence v1.2 §18 уже устанавливает, что LDT не обязателен для MVP;
2. **Утверждённые Owner Decisions** — разрешают: AYLA-DEC-0063 (OD-MVP-1) прямо адресует этот вопрос;
3. **Удаление legacy-положения** — не потребовалось: минимальная правка одного предложения достаточна;
4. Остальные шаги лестницы не понадобились — конфликт разрешён на шаге 2.

Manifesto v1.0 → v1.1 (minimal amendment, 2026-08-07); см. Change Log документа.
