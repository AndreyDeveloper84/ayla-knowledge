---
node_id: ayla.ux.owner-review-001
title: Owner Review Package 001 — Customer Screen Inventory
task_id: UX-CUST-001
owner: UX Architecture
type: specification
status: review
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
updated: 2026-08-03
review_cycle: monthly
---

# Owner Review Package 001 — Customer Screen Inventory

> **Superseded in part — 2026-08-02.** Decision 1 (механика переноса
> записи) заменено: **AYLA-DEC-0036** (OD-RESCHED-1) в
> `OWNER_DECISION_REGISTER.md` и **AYLA-DEC-0022** в [[Ayla Decision Log]].
> Для Wave 1 Simple Reschedule действует только модель **same-ID,
> time-only**: существующая запись сохраняет `appointment_id`, а
> `cancel + new booking` для этого сценария запрещён.
>
> Текст раздела «Decision 1» ниже и строка «перенос = cancel + new
> booking» в таблице «Резолюции 2026-07-29» сохранены как snapshot
> первоначального owner review от 2026-07-29 и не являются актуальным
> нормативным решением в части механики переноса. Действующая
> синхронизация — `decisions/ux-owner-decisions.md` (UX-OD-001) и
> `gaps/UX-GAP-0105.md`.

Дата: 2026-07-29. Основание: UX-CUST-001 + UX-INT-001 (integration review:
PASS_WITH_FIXES, правки внесены). Артефакт: `docs/ux/02-screen-inventory-customer.md`.

## Что сделано

- 19 customer-экранов (SCR-CUST-001…019) на двух поверхностях: MAX bot DM, Mini App.
- Волны: 16 W1 (блокеры пилота 2026-08-15), 3 W2. Readiness: 0 READY,
  7 READY_WITH_ASSUMPTIONS, 7 PARTIAL, 5 BLOCKED.
- Journey SRC-02 покрыт полностью: этапы 1–14 + N1–N9 отображены на экраны.
- Устаревшие спеки SRC-12 ревизованы: food scanner, wellness dashboard, анкета,
  proactive toggle, клиентская оплата, Telegram — в DEFERRED (соответствует SRC-01 §5).
- 6 P0 Gap Records + 7 P1 в `docs/ux/gaps/`.

## Decision 1 — Cancel/Reschedule в MVP (UX-GAP-0105, блокирует SCR-CUST-012/013)

**Why it matters:** CAP-011 включён в MVP с отменой/переносом (SRC-01 §4.1 п. 3),
но stage specifications веток — вне MVP-среза journey (SRC-02 OQ5 открыт).
Два экрана BLOCKED; без отмены записи пилотный контур неполон.

**Recommended option:** A — минимальный срез: отмена через диалог (подтверждение →
результат), перенос = отмена + новый выбор слота, без смены мастера.

**Alternatives:** B — полные flow по спеке SRC-12 (C1–C3, R1–R4) — дороже, спека
stale; C — вынести в W2 — риск: клиент не может отменить запись в пилоте.

**Risks:** вариант C создаёт operational-нагрузку (отмены вручную) и бьёт по
Trust-метрике; вариант B тратит дизайн-ресурс на непроверенную спеку.

**Exact owner question:** Подтверждаете ли вариант A (минимальный cancel/reschedule
через диалог в MVP, полный flow — W2)?

## Decision 2 — Human handoff (UX-GAP-0106, блокирует SCR-CUST-019, N1/N7)

**Why it matters:** «Нет критических тупиков» — release minimum (SRC-01 §8).
Сейчас повторная неудача понимания (N1) или недоступность tool/LLM (N7) — тупик.

**Recommended option:** C — честное завершение без оператора: сообщение + предложение
попробовать позже / переформулировать + контакты для связи с салоном вне Ayla.

**Alternatives:** A — чат оператора (Concierge Mode уже существует для первых
100–500 пользователей — расширить его); B — выдать контакты мастера/салона напрямую.

**Risks:** вариант A требует дежурства оператора и процедуры эскалации; вариант B
обходит Ayla-медиацию и может конфликтовать с Provider Trust Model.

**Exact owner question:** Какой вариант тупикового состояния принимаем для пилота:
A (оператор), B (контакты), C (честное завершение)?

## Decision 3 — Consent scopes Phase 1 (UX-GAP-0101, блокирует SCR-CUST-002, 017; частично 001, 009)

**Why it matters:** release blocker SRC-01 §10 п. 1: scopes `intent_understanding`,
`provider_selection` в статусе proposed. Спеки SRC-12 построены на другой модели
consent (152-ФЗ enum), не отображённой на 7 scopes CSR.

**Recommended option:** принять temporary assumption: Phase 1 — session-only,
обработка по `service_necessity`, без явного consent-экрана; consent-экраны в W2.
Параллельно — задание Privacy Owner на mapping 152-ФЗ ↔ CSR (Decision Record).

**Risks:** если юрист решит, что baseline 152-ФЗ consent обязателен при первом
контакте, welcome-flow потребует вставки одного экрана — стоимость переделки
ограничена SCR-CUST-001 (copy-уровень).

**Exact owner question:** 1) Подтверждаете temporary assumption (Phase 1 без
consent-экрана)? 2) Поручить ли Privacy Owner подготовить mapping 152-ФЗ ↔ CSR
как Decision Record?

## Decision 4 — Поверхность этапов 10–12 (слоты, создание, подтверждение записи)

**Why it matters:** SCR-CUST-006 не может получить контракт: канон не назначил,
где показываются слоты — bot DM inline или Mini App. Спека SRC-12 (stale)
предполагала Mini App.

**Recommended option:** гибрид — выбор слота в bot DM (inline, быстрый путь из
рекомендации), детали записи в Mini App. Соответствует ролям каналов
(SRC-02 §Cross-channel Experience).

**Alternatives:** всё в Mini App (как SRC-12); всё в bot DM (дёшево, но тесно
для календаря).

**Exact owner question:** Принять гибрид (слоты — bot DM, детали — Mini App)?

## Decision 5 — Mini App landing (UX-GAP-P1-01)

**Why it matters:** точка входа в Mini App (deep link, этап 1) не определена
каноном; wellness-dashboard из SRC-12 ушёл в DEFERRED.

**Recommended option:** records list (SCR-CUST-010) как home Mini App для MVP —
единственный канонически обоснованный контент Mini App в Phase 1.

**Alternatives:** заглушка «откройте диалог с Ayla» (dialog-first).

**Exact owner question:** Принять records list как home Mini App в Phase 1?

## Вопросы, НЕ требующие решения сейчас (информационно)

- Anonymous-режим (P1-03): граница регистрации зафиксирована на booking create
  (SCR-CUST-009); уточнение при Screen Contract.
- Конфликт DEC-0006 vs DEC-0015 (клиентская оплата): в MVP экранов оплаты нет;
  расхождение зафиксировано в P1-07, разрешение отложено до Phase 2.
- UX State Contract (P1-04), analytics events (P1-06): закрываются в UX-CUST-002.

## Affected artifacts при принятии решений

- Decision 1 → разблокирует SCR-CUST-012/013 → Screen Contracts.
- Decision 2 → разблокирует SCR-CUST-019 + закрывает release minimum «нет тупиков».
- Decision 3 → снимает copy-блок с SCR-CUST-001/009; запускает Privacy task.
- Decision 4/5 → разблокирует Screen Contracts SCR-CUST-006/010.

## Next после решений

UX-CUST-002: Screen Contracts для READY_WITH_ASSUMPTIONS (SCR-CUST-001, 005, 008,
010, 011, 014, 016) + разблокированных по решениям PO — параллельно 2–3 агентами.

## Резолюции 2026-07-29

Решения Product Owner приняты и зафиксированы в
`decisions/ux-owner-decisions.md`; применены к рабочим документам в UX-SYNC-001.

| Вопрос | Резолюция | Статус |
|---|---|---|
| D1 — Cancel/Reschedule в MVP | UX-OD-001 minimal_conversational_cancel_and_reschedule (вариант A: отмена через диалог, перенос = cancel + new booking) | accepted; UX-GAP-0105 закрыт (owner part); stage specs — UX-SPEC-001 |
| D2 — Human handoff (N1/N7) | UX-OD-002 honest_self_service_terminal_fallback (вариант C в ужесточённой форме: без оператора, без авто-выдачи контактов; обязательные действия retry/reformulate/return/try_later/exit) | accepted; UX-GAP-0106 закрыт для MVP; human handoff — P1-08 (Later, Operations Runbook) |
| D3 — Consent scopes Phase 1 | UX-OD-003 phase_1_session_only_service_necessity | accepted_as_temporary_assumption; UX-GAP-0101 остаётся open (release blocker); Privacy task UX-PRIV-001 запущена; revalidation before release |
| D4 — Поверхность этапов 10–12 | UX-OD-004 hybrid_booking_surface (bot DM — compact slots/подтверждение намерения/результат; Mini App — календарь/детали/управление; contextual deep link) | accepted; UX-GAP-P1-02 закрыт |
| D5 — Mini App landing | UX-OD-005 records_list_as_phase_1_mini_app_home (home = SCR-CUST-010) | accepted; UX-GAP-P1-01 закрыт |

Дополнительно при синхронизации: UX-GAP-0103 закрыт как ошибка синхронизации —
Ayla Intent Model Specification v0.9.2 существует и approved
(ayla-knowledge, owner AI Architecture, 2026-07-28).

## Changelog

- 2026-08-03 — Targeted fix (PR #9 review): добавлен supersession-banner к
  Decision 1 — механика переноса заменена **AYLA-DEC-0036** (OD-RESCHED-1,
  `OWNER_DECISION_REGISTER.md`) и **AYLA-DEC-0022** ([[Ayla Decision Log]]);
  для Wave 1 Simple Reschedule действует только same-ID, time-only,
  `cancel + new booking` запрещён. Текст Decision 1 и таблица «Резолюции
  2026-07-29» не переписаны — сохранены как исторический snapshot.
  Decisions 2–5 не затронуты.
