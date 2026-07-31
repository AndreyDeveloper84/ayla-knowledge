---
node_id: ayla.foundation.canon-governance.foundation-window-charter
title: FOUNDATION_WINDOW_CHARTER
type: specification
status: approved
version: "1.0"
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
updated: 2026-07-30
review_cycle: monthly
---

# FOUNDATION_WINDOW_CHARTER

**Window:** Foundation Canon Window

## Status

```text
Foundation Window: OPEN (открыто 2026-07-30)
Current gate: FOUNDATION_IN_PROGRESS
Active blocker: NONE
Product Vision stage: COMPLETE / CANONICAL v2.0 (owner approval recorded 2026-07-30)
Product Thesis stage: COMPLETE / CANONICAL v0.5 (owner approval recorded 2026-07-30)
Product Principles stage: COMPLETE / CANONICAL v0.1 (owner approval recorded 2026-07-31)
Current Foundation document: MVP Scope
```

## Mission

Привести пять Foundation-документов — Product Vision, Product Thesis, Product Principles, MVP Scope, User Journey — в каноническое состояние, согласованное с Ayla Product Essence v1.1 и Living Digital Twin Manifesto v1.0. Содержательная работа над каждым документом выполняется последовательно, по одному документу за раз, в отдельных документных окнах.

## Authoritative Inputs

- **Ayla Product Essence v1.1** (`00 Foundation\Ayla Product Essence.md`) — высший продуктовый источник; побеждает при любом конфликте.
- **Living Digital Twin Manifesto v1.0** (`00 Foundation\Ayla Living Digital Twin Manifesto.md`) — обязательный согласующий input для LDT-положений Foundation-документов; sibling под Essence, не родитель Vision/Thesis/Principles.
- **Approved Owner Decisions** (AYLA-DEC-0026 и последующие) — обязательны строго в пределах своего scope; не переопределяют Essence.
- Реестры Canon Governance: CANON_INDEX, CANON_WORKSTREAM_STATUS, OWNER_DECISION_REGISTER (read-only для окна), CANON_CONFLICT_REGISTER.

Полный перечень входов и режимы доступа — `FOUNDATION_INPUT_MANIFEST.md`.

## Documents in Scope

```text
Product Vision      — 01 Product\Ayla Product Vision.md (v2.0, CANONICAL — COMPLETE)
Product Thesis      — 02 Strategy\Ayla MVP Product Thesis.md (v0.5, CANONICAL — COMPLETE)
Product Principles  — 01 Product\Ayla Product Principles.md (v0.1, CANONICAL — COMPLETE)
MVP Scope           — 02 Strategy\Ayla MVP Scope and Release Contract.md (v0.2, draft — CURRENT)
User Journey        — 01 Product\User Journeys\Ayla MVP User Journey Specification.md (v1.0, approved до LDT-канона)
```

Фактические статусы и next actions — `FOUNDATION_DOCUMENT_STATUS.md`.

## Canonization Sequence

```text
1. Product Vision
2. Product Thesis
3. Product Principles
4. MVP Scope
5. User Journey
```

Порядок не меняется без отдельного owner ruling. Обоснование — `FOUNDATION_CANONIZATION_SEQUENCE.md`.

## Allowed Outputs

- обновлённые/созданные версии пяти Foundation-документов (через отдельные документные окна, по одному);
- статусные обновления `FOUNDATION_DOCUMENT_STATUS.md` и реестров;
- записи конфликтов в CANON_CONFLICT_REGISTER (через оркестратора);
- эскалации Owner Decisions по лестнице разрешения (см. CANON_CONFLICT_REGISTER);
- handoff-документы окна.

## Forbidden Scope

- переопределение Product Essence v1.1 или Manifesto v1.0;
- изменение Domain-, UX-, AI-, Safety-, Architecture-, API-документов и кода;
- открытие Domain/UX/AI/Engineering workstreams;
- присвоение статуса CANONICAL без отдельного review и owner approval;
- параллельная работа над несколькими Foundation-документами без отдельного разрешения владельца;
- изменение schema/validator;
- push без отдельного указания.

## Subagent Policy

```text
FORBIDDEN
```

Субагенты могут быть разрешены позже только отдельной owner-командой и по одному документу.

## Owner Review Gates

- Каждый документ проходит: authoring/alignment → consistency review → `READY_FOR_OWNER_REVIEW` → owner approval → CANONICAL (статус присваивает оркестратор, не окно).
- P0-конфликты обрабатываются по лестнице разрешения (6 шагов, см. CANON_CONFLICT_REGISTER); Owner Decision создаётся только при materially unresolved выборе.
- Gate-модель Foundation: `FOUNDATION_IN_PROGRESS → FOUNDATION_READY_FOR_OWNER_REVIEW → FOUNDATION_COMPLETE` (детальные критерии состояний — CANON_WORKSTREAM_STATUS).

## Completion Criteria

1. Все пять документов имеют статус CANONICAL (каждый — после отдельного owner approval).
2. Каждый документ согласован с Essence v1.1 и (в LDT-темах) с Manifesto v1.0 и ссылается на них.
3. Ноль открытых P0-конфликтов; применимые Owner Decisions — DECIDED и применены.
4. Sibling-иерархия сохранена: Manifesto не стал родителем Vision/Thesis/Principles.
5. MVP Scope определяет релизный состав; User Journey — путь пользователя без технической реализации.
6. Validation 0 errors; предупреждения не выросли без обоснования.
7. `FOUNDATION_DOCUMENT_STATUS.md` и реестры отражают итоговое состояние.
8. Создан handoff и зафиксировано открытие следующего разрешённого gate.

## Stop Conditions

Окно останавливается и возвращает blocker report, если: требуется изменить Essence или Manifesto; выявлен materially unresolved продуктовый выбор (эскалация владельцу); требуется schema/validator change; конфликт реестров требует отдельного ruling; изменение выходит за allowed scope.
