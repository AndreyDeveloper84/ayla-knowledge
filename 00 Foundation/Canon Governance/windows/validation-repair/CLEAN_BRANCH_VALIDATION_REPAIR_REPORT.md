---
node_id: ayla.foundation.canon-governance.clean-branch-validation-repair-report
title: CLEAN_BRANCH_VALIDATION_REPAIR_REPORT
type: dashboard
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
created: 2026-07-30
updated: 2026-07-30
review_cycle: monthly
---

# Clean Branch Validation Repair Report

Операционный отчёт repair-задания. Не открывает новый канонизационный workstream.

## Baseline

```text
Branch: agent/ux-mvp
Worktree: ayla-knowledge-canon-final
HEAD: 91a344e
Working tree: clean
Validation: 8 errors, 22 warnings
```

## Error Inventory

| # | Source file | Broken reference | Expected target | Error type |
|---|---|---|---|---|
| 1 | `01 Product/UX MVP/contracts/recommendation-ux-addendum.md` | `[[Ayla MVP Recommendation Contract]]` | `05 Architecture/Ayla MVP Recommendation Contract.md` | unresolved depends_on |
| 2 | `02 Strategy/Ayla MVP Scope and Release Contract.md` | `[[AMD-020 Pilot Scope Registry]]` | `05 Architecture/AMD-020 Pilot Scope Registry.md` | unresolved related |
| 3 | `05 Architecture/ADR-0013 Recommendation Snapshot.md` | `[[Ayla MVP Recommendation Contract]]` | то же | unresolved related |
| 4 | `05 Architecture/ADR-0014 Conversation Context ID.md` | `[[Ayla MVP Recommendation Contract]]` | то же | unresolved related |
| 5 | `05 Architecture/Ayla Core Domain Model Specification.md` | `[[AMD-020 Pilot Scope Registry]]` | то же | unresolved depends_on |
| 6 | `05 Architecture/Ayla Transaction State Model.md` | `[[Ayla MVP Recommendation Contract]]` | то же | unresolved related |
| 7 | `06 Safety and Governance/Consent Scope Registry.md` | `[[AMD-020 Pilot Scope Registry]]` | то же | unresolved related |
| 8 | `06 Safety and Governance/Consent Scope Registry.md` | `[[AMD-020 Pilot Scope Registry]]` | то же | unresolved depends_on |

Все 8 ошибок — дубликаты двух отсутствующих целей. Ссылки — wikilinks в frontmatter (`depends_on`, `related`). Path/case/slash mismatch не обнаружен; в Git целей под другими именами/node_id нет (проверено `git grep`).

## Missing Targets

1. `05 Architecture/AMD-020 Pilot Scope Registry.md` — существовал только как untracked в основном worktree.
2. `05 Architecture/Ayla MVP Recommendation Contract.md` — существовал только как untracked в основном worktree.

## Source References

- **AMD-020 Pilot Scope Registry**: MVP Scope and Release Contract (граница по AYLA-DEC-0014), Core Domain Model (нормативный источник ownership: Consent cache, Inference SoR, Bounded Context confirmations), Consent Scope Registry (depends_on + related), Decision Log, Product Thesis, `Ayla.md`. Роль: authoritative pilot scope / memory-ownership registry — REQUIRED, canonical input.
- **Ayla MVP Recommendation Contract**: recommendation-ux-addendum (depends_on; «CANON v0.3»), ADR-0013, ADR-0014, Transaction State Model, UX source index (SRC-16), экраны SCR-CUST-004/006. Роль: единый recommendation-контракт — REQUIRED как draft/proposed canonical artifact.

Удаление ссылок как «преждевременных» невозможно: это существенные архитектурные зависимости (ladder п. 10).

## Candidate File Review

- **AMD-020 Pilot Scope Registry** (189 строк): frontmatter валиден (`type: adr`, `status: approved`, `decision_status: approved`, `adr_id: AMD-020`, `revision: 3`, v0.3); depends_on — Constitution, Data Inventory Matrix (оба tracked). Полный change log v0.1→v0.3; TODO/TBD/placeholder — 0; конфликтов с Essence v1.1 нет (scope-registry уровень, не визуальный опыт). Provenance: Architecture workstream, упоминается решениями AYLA-DEC-0014 и Decision Log как действующий реестр.
- **Ayla MVP Recommendation Contract** (1025 строк): frontmatter валиден (`type: specification`, `status: draft`, `decision_status: proposed`, v0.3, P0, depends_on присутствует); незавершённость явно описана (Open Questions OQ-R1..R10, «Статус: draft / proposed»); tracked-ссылки представляют его именно как «v0.3, draft/proposed, canonical» — ложного впечатления готовности нет (соответствует AYLA-DEC-0013: `source_kind: canonical` ≠ нормативная зрелость). TODO/TBD — 0; конфликтов с committed-документами не выявлено. Provenance: Product Architecture, reconciliation зафиксирован в `reviews/recon-recommendation-contract-001.md`.

## Classification Decisions

| Target | Class | Обоснование |
|---|---|---|
| AMD-020 Pilot Scope Registry | **A. READY_TO_COMMIT** | Завершён, approved ADR, schema-valid, нужен tracked-документам, validator проходит |
| Ayla MVP Recommendation Contract | **B. DRAFT_BUT_REQUIRED** | Статус явно draft/proposed; tracked-зависимости законно ссылаются на него как на draft artifact; schema-valid; незавершённость описана |

Классы C/D/E не применимы: ссылки существенные, целей под другими именами нет, материальных конфликтов не выявлено.

## Repairs Applied

Оба файла скопированы байт-в-байт из основного worktree в чистый worktree (оригиналы не изменялись) и добавлены в Git точечным staging. Содержимое файлов не редактировалось — content и metadata зрелые, правок не потребовалось.

## Files Added

```text
05 Architecture/AMD-020 Pilot Scope Registry.md
05 Architecture/Ayla MVP Recommendation Contract.md
```

## References Corrected

Нет — все ссылки корректны; исправление не требовалось.

## Validation Before

```text
8 errors, 22 warnings
```

## Validation After

```text
0 errors, 21 warnings
git diff --check: clean
```

## Existing Warnings

21 предупреждение — все существовали до repair (unresolved wikilinks на будущие документы: Recommendation Engine Specification, Safety and Boundary Specification, Analytics Event Taxonomy, ADR-0009 и т.п.). Дельта к baseline: −1 (warning `Ayla.md: unresolved wikilink [[AMD-020 Pilot Scope Registry]]` разрешился добавлением файла) — проверено детерминированным diff списков предупреждений. Новых предупреждений нет.

## Unrelated Files Excluded

Не добавлялись: `.claude/`, `05 Architecture/Ayla MVP Appointment Contract.md` (untracked, но валидацию не ломает — на него нет unresolved-ссылок из tracked-файлов), `tests/fixtures/`, а также 8 modified-файлов основного worktree.

## Remaining Risks

- `Ayla MVP Appointment Contract.md` остаётся untracked в основном worktree; при появлении tracked-ссылок на него ошибка воспроизведётся — рекомендуется отдельное решение владельца о его коммите.
- Recommendation Contract остаётся draft/proposed с открытыми OQ-R1..R10 — нормативную силу получит только после `status: approved`.

## Owner Decisions Required

Нет. Материально нерешённых продуктовых вопросов repair не выявил.

## Commit

Один атомарный repair commit на `agent/ux-mvp`:

```text
canon: repair clean-branch knowledge validation
```

Состав: два добавленных target-файла + настоящий отчёт. Push не выполнялся.
