---
node_id: ayla.knowledge.kb-001-dec-0026-collision-repair-2026-08-19
title: KB Repair Phase 1 — DEC-0026 Collision Repair — 2026-08-19
type: specification
status: draft
canonical_status: draft
version: "1.0"
owner: Canon Architect / Knowledge Base Auditor (agent)
knowledge_area:
  - foundation
domain:
  - cross-domain
concerns:
  - governance
  - audit
system_owner:
  - ayla-knowledge
source_repository: ayla-knowledge
created: 2026-08-19
updated: 2026-08-19
source_kind: canonical
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: sanitized
review_cycle: event-driven
---

# KB Repair Phase 1 — Impact Report: разрешение коллизии AYLA-DEC-0026 (KB-001)

**Дата:** 2026-08-19 · **Scope:** только KB-001 / DEC-0026 · **Основание:** `docs/audits/2026-08-19-full-kb-canon-audit-v2.md` (KB-001, P0), уточнение владельца продукта: LDT вынесен из MVP.

## 1. Природа коллизии

Один идентификатор `AYLA-DEC-0026` используется для двух разных решений:

| Решение | Ledger | Дата | Место записи |
|---|---|---|---|
| Living Digital Twin as Ayla's Primary Visual Interface | OWNER_DECISION_REGISTER | 2026-07-29 | `00 Foundation/Canon Governance/OWNER_DECISION_REGISTER.md:52` |
| Master MVP Canon Freeze (Auth/Authority + Customer Resolution, `appointment.completed`) | Ayla Decision Log | 2026-08-18 | `02 Strategy/Ayla Decision Log.md:1479` |

Корневая причина: два ledger'а делят одно ID-пространство `AYLA-DEC-NNNN`. Register занял 0026 как свободный (Log тогда занимал диапазон до 0025); позже Log присвоил тот же номер записи о freeze.

## 2. Каноническое разрешение (по промпту владельца)

- `AYLA-DEC-0026` сохраняется за **Living Digital Twin** (стратегическое решение; LDT не является частью MVP — подтверждено также AYLA-DEC-0063 / OD-MVP-1).
- Master MVP Freeze получает новый свободный ID: **`AYLA-DEC-0080`** (max занятый ID — 0079 в OWNER_DECISION_REGISTER; 0080+ не встречается нигде в KB).
- История не удаляется: перенумерация фиксируется примечанием по прецеденту AYLA-DEC-0035 (который сам был переномерован из 0011).

## 3. Инвентаризация ссылок (все вхождения DEC-0026, кроме сгенерированного `repomix-output.xml`)

### 3.1 Ссылки со смыслом «LDT / стратегия» — ОСТАЮТСЯ DEC-0026 (без изменений)

| Файл | Строки | Контекст |
|---|---|---|
| `00 Foundation/Canon Governance/OWNER_DECISION_REGISTER.md` | 52–101, 381, 779–785 | сама запись LDT; исполнительные отметки; соотношение с DEC-0063 |
| `00 Foundation/Ayla Living Digital Twin Manifesto.md` | 40, 372 | основание Manifesto |
| `00 Foundation/Canon Governance/windows/living-digital-twin/*` (4 файла) | множество | LDT Window: charter, outline, input manifest, alignment report |
| `00 Foundation/Canon Governance/windows/foundation/FOUNDATION_WINDOW_CHARTER.md` | 50 | «Approved Owner Decisions (AYLA-DEC-0026 и последующие)» |
| `00 Foundation/Canon Governance/windows/foundation/FOUNDATION_DOCUMENT_STATUS.md` | 32, 33, 38 | выравнивание Vision/Thesis по DEC-0026 |
| `00 Foundation/Canon Governance/CANON_INDEX.md` | 52 | Essence v1.1 basis: DEC-0026 |
| `00 Foundation/Canon Governance/CANON_CONFLICT_REGISTER.md` | 76 | диапазон «AYLA-DEC-0026…0036» (Register-решения) |
| `01 Product/Ayla Product Principles.md` | 186, 259, 876 | canonical sources рядом с Essence/Manifesto/Vision |
| `01 Product/Ayla Product Vision.md` | 87, 728 | основание: LDT |
| `01 Product/User Journeys/Ayla MVP User Journey Specification.md` | 149, 179, 180, 331, 354, 1837, 2141 | Transformation Goal / LDT как факт; диапазон 0026…0036 |
| `03 AI System/Ayla Intent Model Specification.md` | 218, 221, 1750 | LDT — главный визуальный интерфейс |
| `02 Strategy/Ayla MVP Product Thesis.md` | 686 | основание v0.5 (Essence/Manifesto/Vision/DEC-0026) |
| `02 Strategy/Ayla MVP Scope and Release Contract.md` | 909 | основание v0.3 (Essence/Manifesto/Vision/DEC-0026) |

### 3.2 Ссылки со смыслом «Master MVP Freeze / frozen contracts» — ЗАМЕНЯЮТСЯ на DEC-0080

| Файл | Строки | Контекст |
|---|---|---|
| `02 Strategy/Ayla Decision Log.md` | 1479 (заголовок записи), 1548 (changelog v1.10) | сама freeze-запись → перенумерация в 0080 с примечанием |
| `00 Foundation/CHANGELOG.md` | 29, 34 | запись «Master MVP Canon Freeze (AYLA-DEC-0026)» |
| `05 Architecture/Ayla Master MVP Auth and Authority Contract.md` | 58 | «governance ruling AYLA-DEC-0026» (canonicalization) |
| `05 Architecture/Ayla MVP Customer Resolution Contract.md` | 54 | «governance ruling AYLA-DEC-0026» (canonicalization) |
| `05 Architecture/Ayla Domain Event Registry.md` | 586, 1288, 1299, 1387, 1424, 1479 | регистрация `appointment.completed` v0.5 по freeze-решению |
| `docs/REPLY_MASTER_MVP_CANON_GOVERNANCE_FINAL_FREEZE.md` | 61, 201, 253, 276, 303 | review report freeze-прохода |
| `docs/REPLY_MASTER_SALON_UX_IMPLEMENTATION_READINESS.md` | 43, 81, 328 (×2) | «Frozen canon (AYLA-DEC-0026…)» |

### 3.3 Не изменяются (исторические/сгенерированные артефакты)

- `docs/audits/2026-08-19-full-kb-canon-audit-v2.md` / `.json` — датированный снимок аудита, документирующий сам дефект KB-001; служит доказательной записью. Разрешение фиксируется настоящим отчётом, а не переписыванием аудита.
- `repomix-output.xml` — сгенерированный артефакт; обновится при следующей генерации.

### 3.4 Ссылки со «смешанным» смыслом

Не обнаружено ни одного документа, где DEC-0026 означал бы оба решения одновременно, кроме самих записей-источников коллизии и аудита, её документирующего. Диапазоны «0026…0036» (User Journey §1837, CANON_CONFLICT_REGISTER §76) относятся к Register-линейке и остаются валидными.

## 4. Результаты исправления

### 5. Список изменённых документов

| Файл | Изменение |
|---|---|
| `02 Strategy/Ayla Decision Log.md` | Запись freeze перенумерована 0026 → **0080** + примечание о нумерации (прецедент DEC-0035); добавлен п. 5 (граница freeze, разграничение с LDT); новое правило «один AYLA-DEC-ID = одно решение»; Change Log v1.11 + уточнение v1.10; version 1.10 → 1.11, updated 2026-08-19 |
| `00 Foundation/Canon Governance/OWNER_DECISION_REGISTER.md` | Примечание по ID записи DEC-0026 дополнено фактом коллизии и разрешением; добавлено правило «один AYLA-DEC-ID = одно решение» в «Правила»; updated 2026-08-19. Запись LDT сохранена без изменения смысла |
| `00 Foundation/CHANGELOG.md` | Заголовок freeze-записи → AYLA-DEC-0080; governance record — сноска о перенумерации; новая запись 2026-08-19 о разрешении KB-001 |
| `05 Architecture/Ayla Master MVP Auth and Authority Contract.md` | Статусный блок: ruling AYLA-DEC-0026 → 0080 |
| `05 Architecture/Ayla MVP Customer Resolution Contract.md` | Статусный блок: ruling AYLA-DEC-0026 → 0080 |
| `05 Architecture/Ayla Domain Event Registry.md` | 6 ссылок на freeze-решение (регистрация `appointment.completed` v0.5) → 0080 |
| `docs/REPLY_MASTER_MVP_CANON_GOVERNANCE_FINAL_FREEZE.md` | 5 ссылок → 0080 + сноска о перенумерации в §governance ruling |
| `docs/REPLY_MASTER_SALON_UX_IMPLEMENTATION_READINESS.md` | 4 упоминания (frozen canon) → 0080 |

Не изменялись: LDT-контексты (§3.1), датированный аудит `2026-08-19-full-kb-canon-audit-v2.*` (доказательная запись дефекта), сгенерированный `repomix-output.xml`.

### 6. Decision graph до / после

**До (сломано):**

```text
AYLA-DEC-0026 ──┬── (Register, 2026-07-29) LDT ruling
                │      → Essence v1.1 → Manifesto, Vision, Thesis,
                │        Principles, MVP Scope, User Journey, Intent Model
                └── (Log, 2026-08-18) Master MVP Freeze
                       → Auth&Authority, Customer Resolution,
                         DER v0.5 (appointment.completed), CHANGELOG,
                         UX readiness/freeze reports
        ⇒ одна ссылка = два решения; трассировка неопределённа
```

**После (восстановлено):**

```text
AYLA-DEC-0026 (Register) — Living Digital Twin as Ayla's Primary
  Visual Interface (стратегия; LDT вне MVP)
    → Essence v1.1 → Manifesto, Vision, Thesis, Principles,
      MVP Scope, User Journey, Intent Model, LDT Window docs
    → уточнено AYLA-DEC-0063 (OD-MVP-1): LDT не обязателен в MVP

AYLA-DEC-0080 (Log) — Master MVP Canon Freeze (MVP boundary)
    → Master MVP Auth&Authority Contract (canonical v1.0)
    → MVP Customer Resolution Contract (canonical v1.0)
    → Domain Event Registry v0.5 (appointment.completed registered)
    → 00 Foundation/CHANGELOG.md; REPLY_MASTER_MVP_* reports
    → frozen set + Change Control; граница с LDT зафиксирована п. 5
```

Цепочка `Question → Decision → Requirement → Contract → Implementation` восстановлена: каждая ссылка AYLA-DEC-* указывает ровно на одно решение.

### 7. Проверка Acceptance Criteria

- DEC-0026 имеет одно значение (LDT) — **да**; freeze-смысл вынесен в DEC-0080.
- LDT остаётся стратегическим решением — **да**, запись в Register не изменена по смыслу.
- Master MVP Freeze имеет отдельный ID — **да**, AYLA-DEC-0080 (свободный; max занятый — 0079).
- Нет документов, где один DEC означает разные решения — **да**; единственные «двойные» упоминания остались в датированном аудите KB-001 (описание дефекта) и в примечаниях о перенумерации (описание истории).
- Decision graph восстановлен — **да** (§6).
- MVP scope не изменён — **да**; ни один контракт не изменён по содержанию, только ID-ссылки.
- Валидатор: baseline 131 errors / 20 warnings — **без дельты** (проверено stash-прогоном до/после).

### 8. Рекомендация по роли Decision Log и OWNER_DECISION_REGISTER

Факты: оба ledger'а пишут в одно ID-пространство `AYLA-DEC-NNNN`; Log содержит 0001…0026 + 0035 + 0080, Register — 0026…0079 (без 0035). Register (type: dashboard) де-факто выполняет роль второго ledger'а, что и породило KB-001.

**Рекомендация (требует owner ruling — автоматически не применять):** вариант (a) из OD-AUDIT-001 —
`Ayla Decision Log` объявляется **единственным нормативным источником истины** для AYLA-DEC-ID; `OWNER_DECISION_REGISTER` становится **представлением/owner dashboard**: отражает решения Log с удобной для владельца группировкой, не присваивает ID самостоятельно. Альтернативы: (b) разные префиксы ID-пространств; (c) Register как единственный ledger, Log в архив. Вариант (a) минимизирует переписывание ссылок: большинство downstream-документов уже цитируют оба источника единообразно.

До owner ruling действует добавленное обоим реестрам правило: один AYLA-DEC-ID = одно решение; номер проверяется по обоим реестрам перед присвоением.

### 9. Рекомендация по следующему этапу KB Repair

По приоритетам аудита v2:

1. **OD-AUDIT-001 (owner ruling)** — утвердить модель единого ledger'а (§8); после ruling — миграция записей Register 0027…0079 в Log (или нормативная фиксация границы) и backfill 0027…0034/0036+ в канонический реестр.
2. **KB-002 (P0)** — конфликт действующих решений по клиентской онлайн-оплате (DEC-0006 vs DEC-0015/DEC-0035) без записи о разрешении.
3. **KB-004** — амендировать approved Reset Roadmap / Documentation Roadmap под принятые owner decisions.
4. **KB-007, KB-013, KB-017** — displayable rule без upstream authority; UX-OD-001…005 вне Decision Log; нормативная регистрация availability event names.
5. Инвертированная канонизация (downstream CANONICAL при upstream candidates) — отдельный governance-проход после закрытия P0.

