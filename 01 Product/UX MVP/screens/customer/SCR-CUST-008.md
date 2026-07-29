---
screen_id: SCR-CUST-008
name: Booking confirmation + предложение напоминания
task_id: UX-CUST-002b
wave: 1A.1 Happy Path Booking
status: draft
date: 2026-07-29
sources: [UJS этапы 12–13; UX-OD-003, UX-OD-004; SRC-01 §4.1 п. 10–11; recommendation-ux-addendum (UXA §4); SRC-12 customer-booking-flow F5 (компоненты)]
node_id: ayla.ux.scr-cust-008
title: SCR-CUST-008 — Booking confirmation + предложение напоминания
type: specification
owner: UX Architecture
version: "0.1"
domain:
  - booking
system_owner:
  - ayla-booking
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

# SCR-CUST-008 — Booking confirmation + предложение напоминания

| Поле | Значение |
|---|---|
| screen_id | SCR-CUST-008 |
| name | Booking confirmation + предложение напоминания |
| actor | Backend/Provider → Ayla → User |
| surface | bot DM (result notification) + Mini App (detail — SCR-CUST-011), UX-OD-004 |
| mvp_flow | W1, подволна 1A.1; UJS этап 12 (confirmation), вход — `appointment.confirmed` |
| purpose | Дать достоверное подтверждение записи (кто, когда, где) и предложить напоминание |
| user_goal | Получить достоверное подтверждение; не забыть о записи |
| primary_action | Принять подтверждение; открыть детали записи (deep link в Mini App SCR-CUST-011) |
| secondary_actions | Включить напоминание / отказаться от напоминания; вернуться к диалогу |

## required_data

- Authoritative `confirmed` state от booking SoR (без него экран не рендерится — UX-OD-004, UJS этап 12).
- Детали записи: услуга, специалист, салон/место, дата и время.
- `recommendation_id` для attribution: при подтверждении в attribution window фиксируется qualified action (факт — SRC-01 §4.1 п. 11; RC §4; семантика `QualifiedActionAttributed` pending — OQ-REC-5).

## key_components

- **Confirmation-сообщение (bot DM):** recap «кто, когда, где» — только после authoritative confirmed (паттерн recap из stale F5 — компонент, не копирайт-канон).
- **Кнопка «Открыть запись»:** contextual deep link в Mini App booking detail (SCR-CUST-011), НЕ на generic home (UX-OD-004); `recommendation_id` и контекст сохраняются.
- **Предложение напоминания:** транзакционное, по запросу пользователя на этапе 12 (UJS этап 13: напоминание «если пользователь его запросил»); без проактивности (UX-OD-003, CSR §10).
- Reuse из F5 (только компоненты): чек-индикатор, секция «что дальше». НЕ переносятся: loyalty, «записаться ещё», обещание расписания напоминаний, «запомню тебя» (persistent memory off).

## states

| state | Что видит пользователь | Доступные действия |
|---|---|---|
| success (confirmed) | Подтверждение с деталями записи; кнопки «Открыть запись», напоминание | Открыть detail (Mini App); включить/отклонить напоминание; продолжить диалог |
| reminder_offered | Вопрос «Напомнить перед визитом?» (транзакционный) | «Да, напомни» / «Не надо» |
| reminder_set | Подтверждение включения напоминания, без обещания конкретного расписания (assumption 2) | Открыть detail; продолжить диалог |
| detail_view (Mini App, SCR-CUST-011) | Карточка записи: услуга, специалист, место, время, статус confirmed | Навигация в Mini App; возврат в bot DM |

**Запрещено:** любое «записано/подтверждено» до authoritative confirmation
(design-wave-1a §3 п. 1); pending и failed живут в SCR-CUST-007, не здесь.

## dependencies

- CAP-011 (authoritative confirmed state), CAP-021 (Notification Coordination — доставка напоминания по транзакционному контуру).
- UX-OD-004 (no confirmed state до backend confirmation; result — bot DM, detail — Mini App); UX-OD-003 (session-only, no proactive).
- SCR-CUST-011 (booking detail, цель deep link); SCR-CUST-014 (контур транзакционных уведомлений/напоминаний).

## assumptions

1. Состав деталей (кто/когда/где — факт UJS этап 12; адрес/цена не нормированы) — показываем только подтверждённые SoR поля.
2. Параметры напоминания (за сколько часов, сколько раз) не нормированы — UX не обещает конкретное расписание; расписание — за владельцем CAP-021.
3. Analytics `booking_confirmation_shown` — proposal (UJS OQ8); экран не блокируется отсутствием канонического события.
4. Недоставка confirmation-уведомления — детали доступны по запросу в диалоге и в Mini App (UJS этап 13, proposal).

## blockers

Нет (readiness READY — единственный экран батча без P0-зависимостей).

## design_notes

- Подтверждение — фактически достигнутое состояние, не оптимистичный UI (UJS Success Criteria).
- Предложение напоминания — единственный «следующий шаг»; никаких upsell, cross-sell, «записаться ещё» как primary (anti-pushiness, Phase 1 no proactive).
- Booking без `recommendation_id` — `unattributed` (факт — RC §4); UX не скрывает и не чинит это на своей стороне.
- Session-only: никаких «я запомню» / персональных обещаний (UX-OD-003).
