---
node_id: ayla.foundation.canon-governance.ldt-window-charter
title: LIVING_DIGITAL_TWIN_WINDOW_CHARTER
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

# LIVING_DIGITAL_TWIN_WINDOW_CHARTER

**Window:** Living Digital Twin Foundation Window
**Основание:** AYLA-DEC-0026 — Living Digital Twin as Ayla's Primary Visual Interface

```text
Phase A: COMPLETE
Essence v1.1: CANONICAL (owner approved 2026-07-30; merge f148e55)
Phase B: COMPLETE (2026-07-30)
Manifesto: CANONICAL / v1.0
```

Phase B завершена 2026-07-30: Manifesto подготовлен, прошёл consistency review, утверждён Product Owner и канонизирован.

## Phase B — Living Digital Twin Manifesto

### Status

COMPLETE

Completion basis:

- Manifesto drafted (`23dea7c`);
- consistency review passed (`70e5e11`; P0=0, P1=0, P2=0);
- Product Owner approval recorded (APPROVE_WITH_NON_BLOCKING_EDITORIAL_NOTES, 2026-07-30);
- approved P3 cleanup completed (P3-1, P3-2 в `b072a05`);
- Manifesto canonized (v1.0, canonical_status: approved).

### Mission

Подготовить `00 Foundation\Ayla Living Digital Twin Manifesto.md` (первоначальный статус DRAFT), раскрывающий: зачем Ayla нужен Living Digital Twin; почему пользователь должен узнавать себя; как сохраняется идентичность; что такое Authentic Future; как Twin живёт во времени; как разделяются факт, реконструкция, оценка, прогноз и цель; как объясняется трансформация; какой контроль остаётся у пользователя; какие trust/safety-принципы обязательны; где проходит граница MVP и long-term vision; как Manifesto направляет downstream Domain/UX/AI/Safety/Engineering; чего Manifesto не должен определять.

Manifesto находится ниже Product Essence v1.1, не может её переопределять и не заменяет Product Vision, Product Thesis, Product Principles, MVP Scope, User Journey, Domain Model, UX-, AI/ML- и Engineering-спецификации.

### Authoritative Inputs

Ayla Product Essence v1.1 (authoritative source); AYLA-DEC-0026 (только в пределах своего scope, не переопределяет Essence); LDT Alignment Report (трассировка, не источник истины выше Essence); LDT Window Charter; LDT Input Manifest; LDT Outline. Полный перечень и режимы доступа — `LIVING_DIGITAL_TWIN_INPUT_MANIFEST.md` (раздел Phase B).

### Allowed Outputs

Manifesto может устанавливать: обязательные продуктовые принципы; язык и терминологию; trust boundaries; philosophical and product constraints; downstream obligations; запреты на identity drift, deceptive precision, body shaming; обязательность user control; distinction of data/state classes; границу MVP vs long-term на уровне принципов.

### Forbidden Scope

Manifesto не должен содержать: API/database schemas; model architecture и выбор провайдера; ML thresholds и exact similarity scores; SLA; exact UI layouts и animation timing; endpoint contracts; storage design; retention implementation; detailed consent workflow; backlog; release plan; точные acceptance-метрики без утверждённой measurement model.

### Subagent Policy

Subagents: FORBIDDEN. Могут быть разрешены только отдельной командой владельца или Charter amendment.

### Completion Criteria

1. Manifesto создан как `DRAFT`.
2. Manifesto не противоречит Product Essence v1.1.
3. Все обязательные принципы (Mission, 12 пунктов) покрыты.
4. Нет P0 conflicts.
5. Нет скрытых MVP guarantees.
6. Validation проходит с 0 errors.
7. Manifesto передан на Product Owner review.
8. Phase B не закрывается до owner approval или отдельного owner ruling о статусе DRAFT.

### Owner Review Gate

Итог Phase B — Manifesto DRAFT на Product Owner review. Переходы статуса документа (DRAFT → выше) выполняет только оркестратор по owner ruling; окно самостоятельно статус не повышает.

## Mission

1. Подготовить Product Essence v1.1 (semantic patch, не переписывание с нуля).
2. Сохранить человека главным героем продукта.
3. Сохранить Transformation Goal как центральную доменную сущность.
4. Определить обязательные принципы Living Digital Twin.
5. Отделить MVP-обязательства от long-term vision.
6. После owner approval v1.1 подготовить Living Digital Twin Manifesto.
7. Вернуть компактный handoff.

## Authoritative sources

- Ayla Product Essence v1.0 (`00 Foundation\Ayla Product Essence.md`) — CANONICAL, база для patch; не изменяется, v1.1 готовится как отдельный кандидат.
- AYLA-DEC-0026 (`..\..\OWNER_DECISION_REGISTER.md`) — содержание изменения.
- Полный текст ruling: `D:\Проекты\Ayla\OWNER_RULING_LIVING_DIGITAL_TWIN_PRIMARY_VISUAL_INTERFACE.md`.
- Ayla MVP Reset Roadmap (`02 Strategy\Ayla MVP Reset Roadmap.md`) — операционный контекст; не изменяется.

## Правило версий

- До утверждения v1.1: v1.0 остаётся CANONICAL; v1.1 — кандидат со статусом READY_FOR_OWNER_REVIEW по завершении; Foundation Window закрыт; Domain, UX, AI, Engineering и API — BLOCKED.
- После owner approval: v1.1 → CANONICAL; v1.0 → SUPERSEDED; обновляются CANON_INDEX, Foundation Charter и Foundation Manifest.
- Окно не утверждает v1.1 самостоятельно и не переводит v1.0 в SUPERSEDED.

## Scope изменений Essence v1.1 (semantic patch)

1. Уточнить определение Ayla.
2. Добавить Product Promise: «Каждый раз открывая Ayla, человек должен видеть прежде всего самого себя: где он находится сегодня, к какому состоянию движется, что уже изменилось и какой следующий реалистичный шаг приблизит его к цели».
3. Добавить Living Digital Twin Philosophy.
4. Усилить Killer Feature: Recognition; Identity Preservation; Authentic Future; запрет identity drift.
5. Обновить главный продуктовый цикл (12-шаговый цикл из ruling §9).
6. Обновить роль Food, Water, Sleep, Fitness, Procedures, Specialists, Booking, Memory и Schedule.
7. Обновить UX-принцип: Twin — главная визуальная поверхность; остальные элементы вспомогательные (без абсолютного запрета карточек/списков/меню и без требования Twin на каждом служебном экране).
8. Сохранить Transformation Goal как центральную доменную сущность.
9. Добавить Living Digital Twin как центральную долгоживущую визуальную модель.
10. Добавить границу: source media / observed state / reconstruction / measured facts / inferred state / prediction / desired outcome.
11. Обновить критерий принятия решений: узнаёт ли пользователь себя; сохраняется ли идентичность; разделены ли факт, реконструкция, прогноз и цель; помогает ли решение понять состояние, прогресс или следующий шаг.

## Границы содержания

- **Не канонизировать как обязательство MVP** без отдельного решения: пункты ruling §13 (медицински точная 3D-реконструкция, гарантированное фотографическое совпадение, точная биомеханика, диагностика кожи, точный состав тела по камере, гарантированный прогноз внешности 30/60/90, точная причинность вида «массаж изменил плечи», точное отображение энергии, автостарение, универсальный морфинг, обязательный fullscreen Twin, обязательный confidence в процентах, изменение Twin после каждого действия).
- **Минимальные обязательства MVP** (уровень принципа, без технических thresholds): 14 пунктов ruling §14, включая управляемую фотофиксацию, устойчивую узнаваемость, сохранение идентичности между версиями, разделение факта/реконструкции/прогноза/цели, «это не похоже на меня», исправление/перестройку модели, удаление данных, защиту от body shaming, запрет универсального идеала.

## Deliverables

1. `Ayla Product Essence v1.1` — кандидат, статус `READY_FOR_OWNER_REVIEW`, с пометкой `Supersedes after approval: v1.0`.
2. После approval v1.1 — `00 Foundation\Ayla Living Digital Twin Manifesto.md` (DRAFT, ниже Essence, не переопределяет её; структура — см. `LIVING_DIGITAL_TWIN_OUTLINE.md`).
3. Компактный handoff (`LIVING_DIGITAL_TWIN_HANDOFF.md` — создаётся только на фазе handoff).

## Subagent policy

Субагенты запрещены до отдельного разрешения владельца.

## Запреты окна

Не изменять: Essence v1.0, MVP Reset Roadmap, Product Vision, Product Thesis, MVP User Journey, существующий MVP Scope, Killer PRD, Domain/UX/AI/Architecture/Safety/API-документы, код. Не создавать Alignment Report и Handoff до соответствующих фаз.

## Acceptance criteria

- v1.1 — минимальный semantic patch, не полная переработка; каждое изменение трассируется к пункту AYLA-DEC-0026 / ruling §12.
- Человек — главный герой; Transformation Goal — центральная доменная сущность; разделение центров из ruling §2 сохранено.
- MVP-граница (§13/§14) воспроизведена без ужесточения и без ослабления.
- v1.0 не изменена; статусы соответствуют правилу версий.
