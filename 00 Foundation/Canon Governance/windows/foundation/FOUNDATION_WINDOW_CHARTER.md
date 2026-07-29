---
node_id: ayla.foundation.canon-governance.foundation-window-charter
title: FOUNDATION_WINDOW_CHARTER
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

# FOUNDATION_WINDOW_CHARTER

**Window:** Foundation Canon Window
**Статус окна:** NOT_OPENED
**Gate:** FOUNDATION_NOT_STARTED

## Mission

Привести пять Foundation-документов — Product Vision, Product Thesis, Product Principles, MVP Scope, MVP User Journey — в состояние `READY_FOR_OWNER_REVIEW`, согласованное с Product Essence и MVP Reset Roadmap.

## Authoritative sources

- **Product Essence** (`00 Foundation\Ayla Product Essence.md`) — высший продуктовый источник. Статус: `CANONICAL` (owner approved 2026-07-29). Внешняя копия на `D:` не authoritative.
- **MVP Reset Roadmap** (`02 Strategy\Ayla MVP Reset Roadmap.md`) — операционный источник порядка перестройки и выпуска. Статус: `CANONICAL` (owner approved 2026-07-29). Не переопределяет Product Essence и не занимает места в иерархии между Essence и Product Vision. Внешняя копия на `D:` не authoritative.
- **Approved Owner Decisions** — обязательные точечные решения строго в пределах своего scope. Owner Decision не может неявно переопределять Product Essence.

Модель не линейная: каждый источник авторитетен в своей роли.

## Files in scope

Пять Foundation-документов (см. `FOUNDATION_INPUT_MANIFEST.md`). Product Principles и MVP Scope отсутствуют — их создание входит в scope:

- **Product Principles — MISSING / CREATE.** Ayla Constitution используется только как conditional reference для проверки применимых ограничений; не шаблон и не основа для автоматического переноса.
- **MVP Scope — MISSING / CREATE FROM NEW CANON.** Создаётся сверху вниз от: 1) Product Essence; 2) MVP Reset Roadmap; 3) обновлённого Product Vision; 4) Product Thesis; 5) Product Principles; 6) утверждённых Owner Decisions. `Killer PRD` — LEGACY REFERENCE ONLY: читать для поиска применимых требований, ранее принятых решений, рисков и сценариев; запрещено использовать как родительский документ, основной черновик или основу структуры.

## Files out of scope

Domain-, UX-, AI-, Engineering-, API-, Safety/Governance-документы; реестры `00 Foundation` (кроме conditional references из манифеста); код, scripts, tests; каталог `99 Archive`.

## Work phases

1. **Foundation Intake and Alignment Pass** — классификация, конфликты, зависимости, разделение AUTO / Owner Decision. Без переписывания документов.
2. **Owner Decision batch** — только по конфликтам, прошедшим лестницу разрешения P0.
3. **Canonical rewrite** — по одному документу сверху вниз.
4. **Consistency review** — сквозная проверка пяти документов.
5. **Handoff** — `FOUNDATION_HANDOFF.md` и статус `FOUNDATION_READY_FOR_OWNER_REVIEW`.

## Subagent policy

Фаза 1 — субагенты запрещены. Фазы 3–4 — допустимы только read/analyze-субагенты с явным списком файлов, без права записи вне scope.

## Owner Decision boundary

P0 не равен Owner Decision автоматически. Перед эскалацией каждый P0 проверяется на разрешимость через: 1) Product Essence; 2) утверждённые Owner Decisions; 3) удаление/замену legacy-положения; 4) явную границу MVP/post-MVP; 5) более простое обратимое решение; 6) редакционное/структурное исправление. Owner Decision создаётся только когда после этих проверок остаются минимум два разумных варианта, materially меняющих продукт, MVP, главный journey, обязательства, safety/privacy, критический контракт или срок выпуска.

## Duplicate resolution rule

Primary candidate среди версий Vision / Thesis / Journey не выбирается по имени файла. Intake определяет его по: frontmatter; version; status; modified date (вспомогательный сигнал); ссылкам на решения; полноте; соответствию Product Essence; отсутствию устаревших положений. Intake возвращает: рекомендуемую primary candidate, таблицу различий, доказательство выбора, значимые расхождения. Это не Owner Decision, если версии не содержат альтернативных стратегических направлений. Сверка охватывает обе локации: KB (`ayla-knowledge`) и `D:\Проекты\Ayla`.

## Acceptance criteria

- Все пять документов имеют статус `READY_FOR_OWNER_REVIEW` в `CANON_INDEX.md`.
- Ноль открытых P0-конфликтов (разрешены или оформлены как Owner Decisions).
- Каждый документ ссылается на версию Product Essence.
- Дубликаты и устаревшие версии помечены `LEGACY` / `DUPLICATE` / `SUPERSEDED`.
- Окно не присваивает статус `CANONICAL` самостоятельно.

## Gate model

```text
FOUNDATION_NOT_STARTED
FOUNDATION_ALIGNMENT_IN_PROGRESS
FOUNDATION_ALIGNMENT_COMPLETE
OWNER_DECISIONS_REQUIRED
FOUNDATION_CANONICALIZATION_IN_PROGRESS
FOUNDATION_READY_FOR_OWNER_REVIEW
FOUNDATION_COMPLETE
```

P0 не считается разрешённым только потому, что он оформлен как открытый Owner Decision.

**FOUNDATION_ALIGNMENT_COMPLETE** — допустимы: P0-конфликты со статусом `ESCALATED`; связанные Owner Decisions со статусом `OPEN`; отсутствие canonical rewrite до получения решений.

**OWNER_DECISIONS_REQUIRED** — обязательно: каждый эскалированный P0 связан с конкретным Owner Decision; каждый Owner Decision содержит точный scope; окно не продолжает canonical rewrite в затронутой области до решения владельца.

**FOUNDATION_READY_FOR_OWNER_REVIEW** — обязательно: ноль P0 со статусом `OPEN`; ноль P0 со статусом `ESCALATED`; все применимые Owner Decisions имеют статус `DECIDED`; решения применены к пяти Foundation-документам; consistency review завершён; пять документов имеют статус `READY_FOR_OWNER_REVIEW`.

**FOUNDATION_COMPLETE** — дополнительно обязательно: итоговый Foundation-пакет одобрен Product Owner; пять Foundation-документов получили статус `CANONICAL`; создан `FOUNDATION_HANDOFF.md`; в `CANON_WORKSTREAM_STATUS.md` зафиксировано открытие следующего разрешённого gate.

Результат работы окна: `FOUNDATION_READY_FOR_OWNER_REVIEW`. Переход в `FOUNDATION_COMPLETE` выполняется только через owner approval.

## Required handoff

Обновлённый `CANON_INDEX.md`; закрытые записи `CANON_CONFLICT_REGISTER.md`; список созданных Owner Decisions; `FOUNDATION_HANDOFF.md` с сигналом `FOUNDATION_READY_FOR_OWNER_REVIEW`.
