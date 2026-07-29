---
artifact: handoff
task_id: UX-CUST-001
status: delivered
date: 2026-07-29
node_id: ayla.ux.customer-inventory-handoff
title: Handoff — UX-CUST-001 (MVP Screen Inventory, customer)
type: specification
owner: UX Architecture
version: "0.1"
domain:
  - cross-domain
system_owner:
  - ayla-knowledge
knowledge_area:
  - product
source_repository: ayla-knowledge
source_kind: product-requirements
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
updated: 2026-07-29
review_cycle: monthly
---

# Handoff — UX-CUST-001 (MVP Screen Inventory, customer)

## summary

Сформирован инвентарь customer-поверхности MVP: 19 экранов (SCR-CUST-001…019)
на двух поверхностях (MAX bot DM, Mini App), дедуплицированных против 12 спек
SRC-12. Волны: 16 W1 (Phase 1, session-only), 3 W2 (Phase 2). Readiness:
0 READY, 7 READY_WITH_ASSUMPTIONS, 7 PARTIAL, 5 BLOCKED. Journey покрыт
полностью: этапы 1–14 и N1–N9 отображены на screen_id; непокрыты системный
этап 6 (экран не требуется) и Mini App landing (gap P1-01). В DEFERRED из
SRC-12 ушли: food scanner (оба файла), wellness dashboard, onboarding S3–S5,
profile R2/R4, reminders B7/B9, клиентская оплата, Telegram-варианты.

## changes_proposed

- Инвентарь `docs/ux/02-screen-inventory-customer.md` (таблица, DEFERRED,
  маппинг journey).
- 6 P0 Gap Records + реестр 7 P1 в `docs/ux/gaps/`.
- Изменений вне `docs/ux/` нет; спеки SRC-12 не переписывались.

## decisions_required (к Product Owner)

1. OQ5: включать ли stage specs отмены/переноса в MVP-срез — блокирует
   SCR-CUST-012/013. Варианты: включить полные flow / минимальный путь через
   диалог / перенести в W2.
2. Human handoff (OQ2): порог и процедура. Варианты: чат оператора / контакты
   мастера / честное завершение без оператора.
3. Mini App landing: records list как home / диалог-first заглушка / иное.
4. Поверхность этапов 10–12: Mini App (как в SRC-12) / bot DM inline / гибрид.
5. Anonymous-режим: существует ли в MVP и где граница регистрации.

## gaps_found

- P0: UX-GAP-0101 (consent-модель/scopes), UX-GAP-0102 (Phase 2 gates),
  UX-GAP-0103 (Intent Model Spec), UX-GAP-0104 (Recommendation Contract),
  UX-GAP-0105 (cancel/reschedule specs), UX-GAP-0106 (human handoff).
- P1: P1-01…P1-07 (landing, surface assignment, anonymous mode, UX State
  Contract, CAP-006/триггер этапа 14, analytics events, DEC-0006 vs DEC-0015).

## documents_affected

Созданы: инвентарь, 6 P0-файлов и P1-реестр в `docs/ux/gaps/`, этот handoff.
Изменены: нет.

## conflicts_found (SRC-12 vs канон)

- Дата «15 July» во всех SRC-12 vs канон 2026-08-15 (AYLA-DEC-0003);
  Telegram-упоминания vs MAX (AYLA-DEC-0004).
- Consent-модель SRC-12 (152-ФЗ enum PERSONAL_DATA…) vs 7 scopes CSR
  (UX-GAP-0101).
- SRC-12 wellness-scope (food scanner, dashboard, anketa) vs SRC-01 §4.1
  (booking vertical slice) — ушло в DEFERRED.
- DEC-0006 (опциональная клиентская оплата) vs DEC-0015/SRC-01 §5.1
  (исключена) — UX-GAP-P1-07.

## assumptions

- Phase 1 = W1, Phase 2 = W2 (SRC-01 §3, AYLA-DEC-0018).
- Cancel/reschedule — W1, т.к. CAP-011 включён полностью (SRC-01 §4.1 п. 3),
  readiness BLOCKED по OQ5.
- Словарь состояний/ошибок SRC-02 использован как рабочий (P1-04).

## acceptance_criteria

- Этапы 1–14 и N1–N9 отображены на screen_id — выполнено.
- Один экран = один screen_id — выполнено (19 id).
- P0-пробелы имеют Gap Records полного формата — выполнено (6 файлов).

## recommended_next_task

UX-CUST-002: Screen Contracts для экранов READY_WITH_ASSUMPTIONS
(SCR-CUST-001, 005, 008, 010, 011, 014, 016) — до решений PO по gap-блокерам.

## artifact_path

`docs/ux/02-screen-inventory-customer.md`
