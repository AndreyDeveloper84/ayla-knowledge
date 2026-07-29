---
artifact: customer-cancel-reschedule-stages
version: "0.1"
status: draft
date: 2026-07-29
task_id: UX-SPEC-001
basis:
  - UX-OD-001
  - UX-OD-002
  - UX-OD-004
screens:
  - SCR-CUST-010
  - SCR-CUST-011
  - SCR-CUST-012
  - SCR-CUST-013
node_id: ayla.ux.cust-cancel-reschedule-stages
title: Customer Cancel / Reschedule — Stage Specifications (MVP Phase 1)
type: specification
owner: UX Architecture
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

# Customer Cancel / Reschedule — Stage Specifications (MVP Phase 1)

Минимальные stage specifications веток отмены и переноса записи по owner
decision **UX-OD-001** (accepted, 2026-07-29), действиям при ошибках
**UX-OD-002** и ролям каналов **UX-OD-004**. Продуктовые решения за
пределами owner decisions не принимаются: неизвестное — Open Questions.
Метки (как в MVP UJS): *(факт — источник)*; **(proposal)** подлежит review.

## Соглашения

- **surface:** `bot DM` — нить MAX-бота (сообщения + inline-кнопки); `Mini
  App` — webview. Роли: bot DM — компактные слоты кнопками + pending/result;
  Mini App — расширенный календарь; deep link сохраняет контекст записи и
  `recommendation_id` *(факт — UX-OD-004)*.
- **Доменные статусы:** только **Request ≠ Created ≠ Confirmed** *(факт —
  SRC-02 этап 11)* и `cancelled` / `cancel_failed` из UX-OD-001; всё прочее
  — к Booking owner (OQ-2).
- Отмена — только bot DM; Mini App — для reschedule при необходимости
  расширенного выбора слота (contextual deep link) *(факт — UX-OD-001)*.
- Успех — только после подтверждения booking SoR *(факт — UX-OD-001; SRC-02
  этап 12)*.
- **Deferred to W2:** смена мастера при переносе, расширенные альтернативы,
  standalone full-screen flows *(факт — UX-OD-001)*.

## Entry points

| Entry | Surface | Переход |
|---|---|---|
| «Отменить» / «Перенести» в списке записей (SCR-CUST-010) и на детали записи (SCR-CUST-011) | Mini App | Contextual deep link в bot DM с `booking_id` → C1 / R1 **(proposal)** |
| Запрос в диалоге: «отмени запись» / «перенеси» / «не приду» | bot DM | Intent `CANCEL_APPOINTMENT` / `RESCHEDULE_APPOINTMENT` *(факт — SRC-02 этап 4)* → C1 / R1 |

## Stage spec: Cancel (SCR-CUST-012)

### C1. Identify booking

| Поле | Значение |
|---|---|
| actor | Ayla ↔ User |
| trigger | Intent отмены разрешён |
| пользовательская цель | Указать, какую запись отменить |
| системное действие | Запросить активные записи у Backend. Ноль — empty state «У тебя сейчас нет активных записей»; одна — сразу к C2; несколько — выбор записи кнопками (дата · время · услуга) *(факт — UX-OD-001)* |
| отображаемое состояние | Кнопки записей либо empty state |
| ошибка | Нет активных записей; список недоступен |
| fallback | Empty state — не ошибка, диалог открыт; недоступность списка — `try_later` (UX-OD-002) |
| owning capability | CAP-011 |

### C2. Show booking summary

| Поле | Значение |
|---|---|
| actor | Ayla → User |
| trigger | Запись идентифицирована |
| пользовательская цель | Убедиться, что речь о нужной записи |
| системное действие | Показать дату, время, услугу, специалиста *(факт — UX-OD-001)* |
| отображаемое состояние | Сводка записи в диалоге |
| ошибка | Запись стала неактивной между C1 и C2 (см. N-CR3) |
| fallback | Вернуться к C1 с актуальным списком **(proposal)** |
| owning capability | CAP-011 |

### C3. Explicit confirmation

| Поле | Значение |
|---|---|
| actor | User → Ayla |
| trigger | Показана сводка C2 |
| пользовательская цель | Контролировать необратимое действие |
| системное действие | Запросить явное подтверждение с указанием последствий («запись будет отменена»; штрафы/дедлайны — только при подтверждённой каноном политике, см. OQ-1); без подтверждения ничего не отменять *(факт — UX-OD-001)* |
| отображаемое состояние | Кнопки «Да, отменить» / «Оставить» |
| ошибка | Отказ — валидный исход |
| fallback | Нейтральное acknowledgement без давления *(факт — SRC-02 этап 9)* |
| owning capability | CAP-011 |

### C4. Cancel pending

| Поле | Значение |
|---|---|
| actor | Ayla → Backend |
| trigger | Явное подтверждение на C3 |
| пользовательская цель | Отмена выполнена ровно один раз |
| системное действие | Вызвать отмену в booking SoR, ожидать фактический результат; вызовы идемпотентны *(факт — SRC-02 N7)* |
| отображаемое состояние | cancel pending («Отменяю…») *(факт — UX-OD-004)* |
| ошибка | `TOOL_TIMEOUT`, backend error, запись уже не активна |
| fallback | Переход в C5 cancel_failed; без авто-retry **(proposal)** |
| owning capability | CAP-011 |

### C5. Result: cancelled / cancel_failed

| Поле | Значение |
|---|---|
| actor | Backend → Ayla → User |
| trigger | Получен результат из SoR |
| пользовательская цель | Достоверный итог |
| системное действие | **cancelled:** успех только после подтверждения SoR, рекап (дата, время, услуга, специалист) *(факт — UX-OD-001)*. **cancel_failed:** честная ошибка + действия UX-OD-002: `retry` / `return_to_previous_safe_step` (к C2) / `try_later` / `exit`; без оператора и автовыдачи контактов *(факт — UX-OD-002)* |
| отображаемое состояние | cancelled / cancel_failed |
| owning capability | CAP-011 |

## Stage spec: Reschedule (SCR-CUST-013)

Механика MVP: **cancel_then_create_new_booking** — две независимые операции.
Пользователю заранее сообщается неатомарность; впечатление атомарной замены
запрещено *(факт — UX-OD-001)*.

### R1. Identify booking

Правила C1 (ноль — empty state; одна — контекст; несколько — выбор).
Trigger — intent переноса. Owning capability — CAP-011.

### R2. Confirm intent + раскрытие неатомарности

| Поле | Значение |
|---|---|
| actor | User → Ayla |
| trigger | Запись идентифицирована |
| пользовательская цель | Понять, что будет со старой записью |
| системное действие | Подтвердить намерение и заранее сообщить: текущая запись будет отменена, новая создана отдельно; если новое время не подтвердится, старой записи уже не будет *(факт — UX-OD-001)* |
| отображаемое состояние | Сводка + кнопки «Перенести» / «Оставить как есть» |
| ошибка | Отказ — валидный исход |
| fallback | Нейтральное acknowledgement |
| owning capability | CAP-011 |

### R3. Cancel existing

| Поле | Значение |
|---|---|
| actor | Ayla → Backend |
| trigger | Подтверждение на R2 |
| системное действие | Отменить запись через SoR (механика C4) |
| отображаемое состояние | cancel pending |
| ошибка | `cancel_failed` |
| fallback | **Стоп:** поток не идёт к выбору слота; явно сообщается, что запись **остаётся активной**; действия UX-OD-002 (retry / return_to_previous_safe_step → R2 / try_later / exit) *(факт — UX-OD-001/002)* |
| owning capability | CAP-011 |

### R4. Slot selection

| Поле | Значение |
|---|---|
| actor | User ↔ Ayla ↔ Backend |
| trigger | Старая запись `cancelled` |
| пользовательская цель | Выбрать новое время |
| системное действие | Запросить актуальные слоты у Backend; displayed slot — не reservation *(факт — SRC-02 этап 10)*. Bot DM — компактные слоты кнопками; при необходимости расширенного выбора — deep link в Mini App (календарь), контекст записи и `recommendation_id` сохраняются *(факт — UX-OD-004)*. Смена мастера — W2 *(факт — UX-OD-001)* |
| отображаемое состояние | Кнопки слотов / календарь; slot unavailable при пустой выдаче |
| ошибка | `NO_AVAILABLE_SLOTS`; stale slot при commit |
| fallback | См. N-CR1, N-CR4 |
| owning capability | CAP-010 |

### R5. Create new booking

| Поле | Значение |
|---|---|
| actor | Ayla → Backend |
| trigger | Пользователь выбрал слот |
| системное действие | Создать новую запись (Request ≠ Created ≠ Confirmed); slot проверяется при commit *(факт — SRC-02 этапы 10–11)* |
| отображаемое состояние | booking pending |
| ошибка | `APPOINTMENT_CONFLICT`, `TOOL_TIMEOUT`, `APPOINTMENT_NOT_CONFIRMED` |
| fallback | При ошибке booking — возврат к выбору слота (R4), если данные актуальны *(факт — UX-OD-002)*; иначе R6 failed |
| owning capability | CAP-011 |

### R6. Result: confirmed / failed

| Поле | Значение |
|---|---|
| actor | Backend → Ayla → User |
| trigger | Получен результат создания записи |
| пользовательская цель | Достоверный итог по обеим записям |
| системное действие | **confirmed:** два явных статуса — «старая запись отменена» + «новая запись подтверждена» (дата, время, услуга, специалист), только после authoritative confirmed *(факт — UX-OD-001; SRC-02 этап 12)*. **failed:** честная ошибка + действия UX-OD-002. **Критический кейс — старая отменена, новая НЕ создана:** явный текст, что старой записи больше нет и новая не создана; действия: `retry` (создание по выбранному слоту), `return_to_previous_safe_step` (к R4, если данные актуальны), `try_later`, `exit`; без оператора и контактов *(факт — UX-OD-002)* |
| отображаемое состояние | confirmed / failed / failed-critical |
| owning capability | CAP-011 |

## Таблица состояний

| Состояние | Surface | Что видит пользователь | Действия | Запрещено показывать |
|---|---|---|---|---|
| C1 empty | bot DM | «Нет активных записей» | Продолжить диалог | Фиктивные записи |
| C1 select | bot DM | Кнопки активных записей | Выбрать, выйти | Прошлые/отменённые записи |
| C2/C3 summary | bot DM | Дата, время, услуга, специалист + последствия | Подтвердить, отказаться | Неподтверждённую каноном политику штрафов (OQ-1) |
| C4 / R3 pending | bot DM | «Отменяю…» | — | Успех до ответа SoR |
| C5 cancelled | bot DM | Итог + рекап | Записаться снова, выйти | Подтверждение без authoritative статуса |
| C5 cancel_failed | bot DM | Честная ошибка | Действия UX-OD-002 | Оператор, контакты мастера |
| R2 intent | bot DM | Сводка + неатомарность | «Перенести», «Оставить» | Впечатление атомарной замены |
| R3 failed | bot DM | «Перенос не выполнен, запись активна» | Действия UX-OD-002 | Переход к выбору слота |
| R4 slots | bot DM / Mini App | Слоты кнопками / календарь | Выбрать слот, выйти | Смену мастера и расширенные альтернативы (W2) |
| R5 pending | bot DM | «Создаю запись…» | — | Успех до authoritative confirmed |
| R6 confirmed | bot DM | Два статуса: старая cancelled + новая confirmed | Открыть запись, выйти | Единый статус «перенесено» без двух явных состояний |
| R6 failed | bot DM | Ошибка создания | Действия UX-OD-002; возврат к R4 | — |
| R6 failed-critical | bot DM | «Старая отменена, новая не создана» — явно | retry / return_to_previous_safe_step / try_later / exit | Маскировку потери записи; оператора; контакты |

## Негативные ветки

Каждая ветка разрешается в существующее состояние, новых экранов нет.

- **N-CR1. Stale slot.** Триггер: `APPOINTMENT_CONFLICT` при commit (R5).
  Поведение: «это время только что заняли»; возврат к **R4** с актуальными
  слотами, если данные актуальны *(факт — UX-OD-002)*. Состояние: R4 slot
  unavailable. Owning capability: CAP-010.
- **N-CR2. Backend timeout.** Триггер: `TOOL_TIMEOUT` на C4 / R3 / R5.
  Поведение: без авто-retry; pending завершается в соответствующий failed
  (C5 / R3 failed / R6 failed) с действиями UX-OD-002; retry идемпотентен
  *(факт — SRC-02 N7)*. Owning capability: CAP-018.
- **N-CR3. Повторная отмена уже отменённой записи.** Триггер: SoR
  возвращает «запись уже не активна» на C4/R3 (гонка). Поведение: не ошибка
  пользователя; сообщить фактическое состояние «эта запись уже отменена»;
  для cancel — завершить в **C5 cancelled**, для reschedule — стоп, новую
  не создавать без подтверждения, возврат к R2 **(proposal)**. Owning
  capability: CAP-011.
- **N-CR4. Reschedule недоступен — нет слотов.** Триггер:
  `NO_AVAILABLE_SLOTS` на R4. Поведение: честное «свободного времени нет»;
  явное напоминание, что старая запись уже отменена; действия UX-OD-002
  (`try_later`, `exit`, повтор слотов позже). Другой мастер — W2 *(факт —
  UX-OD-001)*. Состояние: R4 slot unavailable. Owning capability: CAP-010.

## Open Questions

| # | Вопрос | Кому |
|---|---|---|
| OQ-1 | Политика отмены (дедлайны, штрафы, возвраты) подтверждена ли каноном? Формулировки «последствий» на C3 и no-fault возвраты из SRC-12 §4/§6 — proposal до owner decision | Product Owner |
| OQ-2 | Кто владеет доменным статусом `cancelled` и переходами cancel/reschedule, включая компенсацию и аудит кейса «старая cancelled, новая не created»? | Booking owner |
| OQ-3 | Подтверждён ли механизм deep link Mini App → bot DM (канал MAX) и состав контекста (`booking_id`, `recommendation_id`)? | Platform owner |
| OQ-4 | Допустим ли retry создания записи по ранее выбранному слоту без повторного показа слотов (R6 failed-critical) и в каком окне времени? | Booking owner |
| OQ-5 | Уведомление провайдера об отмене/переносе: контур и формулировки вне scope этого документа | Product Owner |

## Источники и связь

- UX-OD-001 (механика, неатомарность, deferred W2), UX-OD-002 (действия при
  ошибках), UX-OD-004 (роли каналов); SRC-02 этапы 10–12, N4, N6–N7 —
  инварианты (SoR, Request ≠ Created ≠ Confirmed, идемпотентность).
- `docs/screens/customer-cancellation-reschedule-flow.md` (SRC-12, stale) —
  переиспользованы: intent resolution по числу записей, кейс «старая
  отменена, новая не создана». Отброшено как вне UX-OD-001: смена мастера,
  full-screen flows, no-fault каскад, billing chain copy.
