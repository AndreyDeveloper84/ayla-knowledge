---
screen_id: SCR-CUST-003
name: Intent & clarification dialog (уточнение, confidence, N1)
version: "0.1"
status: draft
task_id: UX-CUST-002a
readiness: READY_WITH_ASSUMPTIONS
sources: [Ayla Intent Model Specification v0.9.2 (approved), SRC-02 (UJS этапы 4–5, N1), UX-OD-002, UX-OD-003, design-wave-1a §3–4]
node_id: ayla.ux.scr-cust-003
title: SCR-CUST-003 — Intent & clarification dialog
type: specification
owner: UX Architecture
domain:
  - intent
system_owner:
  - ayla-conversation
  - ayla-mini-app
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

# SCR-CUST-003 — Intent & clarification dialog

- **actor:** Ayla ↔ User
- **surface:** bot DM (MAX)
- **mvp_flow:** Happy Path Booking (Wave 1A.1), этапы 4–5 (Intent detection,
  Clarification), N1

## purpose
Понять, чего пользователь хочет достичь, и собрать минимум обязательных
слотов — диалогом, не анкетой. Источник правил слотов/confidence —
Intent Model Spec v0.9.2 (approved).

## user_goal
Выразить потребность своими словами, ответить на минимум вопросов и получить
решение (SRC-02 этапы 2, 5).

## primary_action
Ответить на один уточняющий вопрос Ayla (или подтвердить формулировку
понимания при medium confidence) → далее SCR-CUST-004.

## secondary_actions
- Свободно доуточнить/исправить сказанное (PROVIDE_CONTEXT, CORRECT_CONTEXT).
- Отказаться отвечать — Ayla продолжает с имеющимся контекстом, обозначив
  неопределённость (SRC-02 этап 5).
- Выйти из сценария (exit).

## required_data (из Intent Output Contract, § Output Contract)
`intent_type`, `status` (resolved / needs_clarification / unresolved /
blocked_safety), `confidence`, `missing_required_slots`,
`unmet_slot_requirements`, `clarification_question` (ровно один конкретный
вопрос, ссылающийся на сказанное), `clarification_reason`, `safety_flags`.
UX не вычисляет intent — только отражает результат resolver'а.

## key_components
- Формулировка понимания уровнем уверенности через язык (SRC-02 этап 4):
  high — утвердительно; medium (0.5–0.8) — подтверждающая формулировка
  «Возможно, ты хочешь…», подтверждение обязательно перед side-effect;
  low (<0.5) — уточнение или `UNKNOWN`, угадывание запрещено.
- Один уточняющий вопрос за ход (clarification rules п. 2).
- Quick-reply кнопки для типовых ответов (вариант дизайна; свободный ввод
  всегда доступен).

## states
1. **default (понимание сформулировано)** — Ayla озвучивает понимание
   (при medium — как вопрос-подтверждение). Действия: подтвердить, поправить.
2. **clarification (slot-level)** — intent распознан, не хватает слотов
   (`missing_required_slot` / `unmet_any_of_requirement`): один конкретный
   вопрос. Действия: ответить, отказаться («просто запиши меня» не обходит
   safety и явное подтверждение — SRC-02 этап 5).
3. **unclear_input / N1 (intent-level)** — low confidence или конфликт
   значений (`intent_low_confidence`, `conflicting_slot`,
   `status = needs_clarification`): честное признание неопределённости, без
   имитации понимания. Действия: переформулировать, ответить на уточнение.
4. **exit (повторная неудача)** — `max_clarification_exceeded` (после 2
   подходов по одному intent) → переход в SCR-CUST-019 (terminal fallback,
   UX-OD-002): без оператора, без контактов мастера, с сохранением безопасного
   контекста сессии.

## dependencies
- Intent Model Spec v0.9.2 — slot requirements, confidence bands, лимиты.
- SRC-02 этап 5: **не более 5 вопросов за сессию Discovery** (факт).
- Intent Model §Confidence п. 3: **не более 2 clarification-подходов подряд
  по одному intent**, далее `unresolved` → N1 fallback.
- UX-OD-002: exit N1 → SCR-CUST-019. UX-OD-003: session-only, без
  memory-формулировок. При `safety_flags` — маршрут в SCR-CUST-016 (вне
  этого экрана).

## assumptions
- **A1.** Числовые пороги confidence (0.5/0.8) — versioned runtime config
  ayla-ai-core; семантика уровней канонична (Intent Model §Confidence).
- **A2.** Naming UX-состояний — P1-04 (UX State Contract), рабочие названия
  из этого контракта.

## blockers
Нет screen-level блокеров (UX-GAP-0103 закрыт: спека approved 2026-07-28).

## design_notes
- Не показывать confidence числом — только языком (SRC-02 этап 4).
- Запрещено: анкета, серия вопросов подряд, memory-ветки W2 («запомню»),
  маскировка low-confidence под определённый intent.
- Ответ пользователя на уточнение — продолжение того же `intent_id`, не новый
  intent (Intent Model п. 4): диалог не «перезапускается» визуально.
