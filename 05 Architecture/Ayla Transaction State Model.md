---
node_id: ayla.arch.transaction-state-model
title: Ayla Transaction State Model
type: specification
status: draft
decision_status: proposed
version: "0.1"
owner: Architecture
co_owner: Booking
task_id: UX-TSM-001
priority: P1
knowledge_area:
  - architecture
domain:
  - cross-domain
system_owner:
  - shared
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
depends_on:
  - "[[Ayla MVP User Journey Specification]]"
  - "[[Ayla Domain Event Registry]]"
related:
  - "[[Ayla MVP Recommendation Contract]]"
  - "[[Ayla Domain Capability Registry]]"
---

# Ayla Transaction State Model

> **Статус:** draft. Документ фиксирует **общий каркас жизненного цикла
> транзакционных операций**, но **не принимает решений**: набор состояний,
> переходы и reason codes подлежат подтверждению владельцами (§7). Пометки:
> *(факт — источник)*, **(proposal)** — предложение этого драфта.

## 1. Мотивация и scope

В UX-документах размножились состояния: `pending`, `confirmed`, `failed`,
`stale`, `cancelled`, `cancel_pending`, `cancel_failed`, `booking_pending`,
`stale_slot`, `hold_expired`, `APPOINTMENT_NOT_CONFIRMED` и пр. Контракты
описывают одни фазы разными именами — риск расхождения моделей.

Scope: операции, инициированные намерением пользователя или провайдера и
завершающиеся изменением состояния в authoritative SoR: **booking create,
booking cancel, reschedule, recommendation commit (accept), provider
confirmation; payment — placeholder (Phase 2)**.

**Граница владения (§6):** документ НЕ владеет доменными статусами
бронирования (owner — Booking) и lifecycle рекомендации (owner —
Recommendation); он фиксирует каркас для доменных lifecycle.

## 2. Ядро модели

Транзакция — единица работы с одним authoritative owner (SoR-сервисом),
начинающаяся от подтверждённого намерения и завершающаяся терминальным
состоянием с reason code **(proposal)**.

### 2.1. Core states **(proposal)**

| state | Определение | Кто переводит |
|---|---|---|
| `initiated` | Намерение зафиксировано (пользовательское действие / подтверждённый intent), вызов к SoR ещё не завершён. Request ≠ результат *(факт — UJS этап 11: Request ≠ Created ≠ Confirmed)* | Инициатор (Ayla/backend) |
| `pending` | Операция отправлена в SoR, authoritative ответ не получен. Успех в этом состоянии запрещён *(факт — UX-OD-004, SCR-CUST-007)* | Authoritative owner |
| `confirmed` | SoR подтвердил достижение целевого состояния. Терминальное (для самой транзакции). Только authoritative confirmation *(факт — UX-OD-001, UJS этап 12)* | Только authoritative owner |
| `failed` | SoR вернул отказ или операция не завершилась (`TOOL_TIMEOUT`, conflict, not confirmed). Терминальное; обязателен reason code и recovery path *(факт — UX-OD-002, UJS N6/N7)* | Только authoritative owner |
| `expired` | Терминальное: транзакция/её контекст утратили валидность по TTL (hold expired, source entity expired) *(факт — AYLA-DEC-0021, цит. по SCR-CUST-007)* | Authoritative owner |
| `cancelled` | Терминальное: результат успешной cancel-операции либо отказ инициатора до отправки (abort). Доменная семантика — у Booking | Только authoritative owner |

### 2.2. `stale` — квалификатор, НЕ состояние

`stale` не входит в lifecycle — это **квалификатор входных данных**
(`stale_slot`, устаревший список записей): данные, на которых основана
транзакция, перестали соответствовать SoR. Обнаруживается при commit и
выражается как `failed` с reason code (напр. `SLOT_TAKEN`) + recovery на
повторное получение данных *(факт — UX-OD-004: stale_slot обязателен как
UX-состояние; SS N-CR1)*. Отдельного состояния `stale` нет **(proposal)**.

### 2.3. Таблица переходов **(proposal)**

| from → to | initiated | pending | confirmed | failed | expired | cancelled |
|---|---|---|---|---|---|---|
| initiated | — | да (вызов SoR) | нет | да (отказ инициатора до вызова) | да (TTL истёк до вызова) | да (abort пользователем) |
| pending | нет | — | да (authoritative) | да (authoritative) | да (TTL/hold) | да (только для cancel-операции как целевой результат) |
| confirmed | нет | нет | — | нет | нет | нет (отмена — новая транзакция) |
| failed / expired / cancelled | нет | нет | нет | — | нет | нет |

Терминальные состояния не имеют исходящих переходов: продолжение — **новая
транзакция** (retry, return_to_previous_safe_step).

## 3. Инварианты

1. **No success до authoritative confirmation.** Ни один контур не
   показывает success до подтверждения SoR *(факт — UX-OD-001, UX-OD-004,
   UJS этап 12 Success Criteria)*.
2. **Намерение ≠ результат.** Подтверждение намерения пользователем
   (`initiated`) не является подтверждением записи (`confirmed`) *(факт —
   UX-OD-004: подтверждение намерения ≠ подтверждение записи)*.
3. **Каждое терминальное состояние — с reason code.** `failed`/`expired`/
   `cancelled` без machine-readable reason code недопустимы **(proposal)**;
   registry — OQ-TSM-2.
4. **`failed` всегда имеет recovery path.** Действия: `retry` /
   `reformulate` / `return_to_previous_safe_step` / `try_later` / `exit`
   *(факт — UX-OD-002)*; retry идемпотентен *(факт — UJS N7, Roadmap §6.3)*.
5. **UX отображает, не изобретает.** UX-состояния строго производны от
   доменного состояния; UI не вводит статусов вне маппинга §4 **(proposal)**.
6. **Единственный authoritative owner на переход.** Только сервис-владелец
   SoR переводит транзакцию в терминальные состояния; UX и оркестратор
   переходы не выполняют *(факт — UX-OD-001)*.

## 4. Mapping операций на ядро

| Операция | initiated | pending | confirmed | failed (примеры reason) | expired | Особенности |
|---|---|---|---|---|---|---|
| booking create | slot selected + intent confirm (SCR-CUST-006) | `booking_pending` (SCR-CUST-007) | authoritative `confirmed` → SCR-CUST-008 | `APPOINTMENT_CONFLICT`, `SLOT_TAKEN` (stale slot), `APPOINTMENT_NOT_CONFIRMED`, `TOOL_TIMEOUT` (N6/N7) | hold expired (TTL 15 мин, AYLA-DEC-0021) | Success живёт только на SCR-CUST-008 |
| booking cancel | explicit confirmation C3 | `cancel_pending` C4 (обязателен — UX-OD-001) | целевой результат — `cancelled` (C5) | `cancel_failed` C5 (обязателен — UX-OD-001); повторная отмена → не ошибка, завершается `cancelled` (N-CR3) | — | Успех только после SoR |
| reschedule | confirm + раскрытие неатомарности R2 | два pending: cancel (R3) + create (R5) | `cancelled` + `confirmed` — два явных статуса (R6) | failed на любом из двух; критический кейс: старая `cancelled`, новая `failed` (R6 failed-critical) | — | = cancel + create, две независимые транзакции (UX-OD-001); атомарность не имитируется |
| recommendation commit (accept) | accept на карточке (SCR-CUST-004) | переход к slot selection/booking create | qualified action при booking `confirmed` в attribution window | `NO_AVAILABLE_SLOTS` после accept (N4) | `expired`/`invalidated` рекомендации (OQ-REC-2) | Сам accept не создаёт booking; commit завершается booking create |
| provider confirmation | request провайдеру (после create) | ожидание ответа провайдера | `appointment.confirmed` (UJS этап 12) | отказ провайдера → `APPOINTMENT_NOT_CONFIRMED` | provider response window — OQ-TSM-3 | Триггеры переходов со стороны провайдера — OQ-TSM-3 |
| payment (placeholder) | — | — | — | — | — | Phase 2; вне scope MVP, каркас резервируется |

## 5. Naming — канонические идентификаторы **(proposal)**

Все состояния и reason codes — `snake_case`. Нормализация рабочих имён:

| Рабочее имя (источник) | Каноническое |
|---|---|
| `APPOINTMENT_NOT_CONFIRMED` (UJS N6, SCR-CUST-007) | `appointment_not_confirmed` (reason code) |
| `cancel_pending`, `cancel_failed` (UX-OD-001, SS C4/C5) | `pending` / `failed` транзакции cancel |
| `booking_pending` (SCR-CUST-007) | `pending` транзакции booking create |
| `stale_slot`, `SLOT_TAKEN` | reason code `slot_taken` + stale-квалификатор данных |
| `hold_expired` (SCR-CUST-007) | `expired` + reason `hold_expired` |
| `confirmed`/`failed`/`cancelled` | без изменений |

Это закрывает рабочую часть **UX-GAP-P1-04** для транзакционного контура;
полный reason code registry — OQ-TSM-2.

## 6. Граница владения

Документ владеет только каркасом: core states, переходы, инварианты,
naming. Доменные lifecycle Appointment (Request / Created / Confirmed,
компенсации, аудит кейса «старая cancelled, новая не created») — owner
**Booking** (SS OQ-2). Lifecycle рекомендации (`created → shown →
accepted | declined | expired | invalidated`) — owner **Recommendation**
(RC §3). Требование: доменные lifecycle обязаны выражаться через core
states §2 либо явно заявить расширение через изменение этого документа
**(proposal)**.

## 7. Open Questions

| # | Вопрос | Владелец |
|---|---|---|
| OQ-TSM-1 | Подтверждение core states (§2.1) и таблицы переходов (§2.3), включая терминальность `expired` | Architecture + Booking |
| OQ-TSM-2 | Reason code registry: владелец, формат, полный список (закрытие UX-GAP-P1-04 целиком) | Architecture + Booking |
| OQ-TSM-3 | Provider-initiated transitions: допустимые переходы провайдера, окно provider confirmation, timeout | Booking + Product Owner |
| OQ-TSM-4 | Retry semantics: окна retry (в т.ч. по ранее выбранному слоту — SS OQ-4), лимиты, idempotency keys | Booking |
| OQ-TSM-5 | Payment: применимость каркаса к payment lifecycle (Phase 2) | Architecture + Payments owner |

## Источники

- UX-OD-001/002/004 (`decisions/ux-owner-decisions.md`); SS C1–C5, R1–R6,
  N-CR1–4 (`flows/customer-cancel-reschedule-stages.md`); SCR-CUST-007/008;
  UJS этапы 10–13, N6/N7; RC §3 (`contracts/draft-mvp-recommendation-contract.md`).
