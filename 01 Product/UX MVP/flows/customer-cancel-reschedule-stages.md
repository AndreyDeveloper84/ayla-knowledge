---
artifact: customer-cancel-reschedule-stages
version: "0.4"
status: draft
date: 2026-07-29
task_id: UX-SPEC-001
basis:
  - UX-OD-001
  - UX-OD-002
  - UX-OD-004
  - AYLA-DEC-0022
  - AYLA-DEC-0036
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
updated: 2026-08-02
review_cycle: monthly
---

# Customer Cancel / Reschedule — Stage Specifications (MVP Phase 1)

Минимальные stage specifications веток отмены и переноса записи по owner
decision **UX-OD-001** (accepted, 2026-07-29; reschedule-механика
синхронизирована с каноном 2026-08-02), действиям при ошибках
**UX-OD-002** и ролям каналов **UX-OD-004**. Продуктовые решения за
пределами owner decisions не принимаются: неизвестное — Open Questions.
Механика reschedule (same-ID, версионирование, события) — не UX-решение;
источник — **AYLA-DEC-0022** (Appointment Reschedule and Replacement
Model, accepted). Метки (как в MVP UJS): *(факт — источник)*; **(proposal)**
подлежит review.

> **Границы scope (cancel):** ветка C1–C5 ниже — **minimal conversational
> cancel** (identify → summary → explicit confirmation → pending → result),
> единственная cancel-механика, авторизованная для Wave 1 owner-решением
> UX-OD-001 (`minimal_conversational_cancel_and_reschedule`). Она **не
> является** full Cancellation journey: policy/deadline/refund flow (см.
> OQ-1), standalone full-screen cancellation management, late-window/
> waitlist-ветки и провайдер-уведомления вне scope этого документа (OQ-5) —
> всё это отдельно остаётся **deferred** (owner ruling 2026-07-28, вариант
> Б; формально зафиксировано как **AYLA-DEC-0036**, OD-RESCHED-1,
> `OWNER_DECISION_REGISTER.md`, 2026-08-02 — этим решением deferral не
> расширяется и не сужается). Backend cancel capability (CAP-011) может
> существовать шире C1–C5, но это не делает полную UX cancellation journey
> частью Wave 1.

## Соглашения

- **surface:** `bot DM` — нить MAX-бота (сообщения + inline-кнопки); `Mini
  App` — webview. Роли: bot DM — компактные слоты кнопками + pending/result;
  Mini App — расширенный календарь; deep link сохраняет контекст записи и
  `recommendation_id` *(факт — UX-OD-004)*.
- **Доменные статусы:** **Request ≠ Created ≠ Confirmed** *(факт — SRC-02
  этап 11)*; `cancelled` / `cancel_failed` из UX-OD-001 (cancel flow);
  `rescheduled` / `reschedule_failed` из UX-OD-001 (reschedule flow, same-ID
  — AYLA-DEC-0022 п. 1, п. 9: статус `rescheduled` как отдельный domain
  status каноном не вводится, здесь это UX-facing исход операции, не
  доменный статус записи); всё прочее — к Booking owner (OQ-2).
- Отмена — только bot DM; Mini App — для reschedule при необходимости
  расширенного выбора слота (contextual deep link) *(факт — UX-OD-001)*.
- Успех — только после подтверждения booking SoR *(факт — UX-OD-001; SRC-02
  этап 12)*.
- **Reschedule (Wave 1, Simple Reschedule):** same-ID, time-only —
  сохраняется `appointment_id`, меняются только дата/время в пределах того
  же Offering, версия монотонно увеличивается, публикуется
  `appointment.rescheduled` *(факт — AYLA-DEC-0022 п. 1, п. 2, п. 9)*.
  Cancel + create для этого сценария не используется.
- **Deferred to W2:** смена мастера/услуги при переносе, replacement,
  re-offer, расширенные альтернативы, standalone full-screen flows *(факт —
  UX-OD-001)*.

## Entry points

| Entry | Surface | Переход |
|---|---|---|
| «Отменить» / «Перенести» в списке записей (SCR-CUST-010) и на детали записи (SCR-CUST-011) | Mini App | Contextual deep link в bot DM с `appointment_id` → C1 / R1 **(proposal)** |
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

Механика MVP (Simple Reschedule, Wave 1): **same-ID, time-only** — одна
версионируемая операция над существующей записью, не две независимые
операции *(факт — AYLA-DEC-0022 п. 1, п. 2, п. 9)*. `appointment_id` не
меняется; исходная запись при любом отказе остаётся активной и без
изменений *(факт — AYLA-DEC-0022 п. 10)*. Впечатление создания новой
отдельной записи запрещено. Смена мастера/услуги — W2 *(факт — UX-OD-001)*.

### R1. Identify booking

Правила C1 (ноль — empty state; одна — контекст; несколько — выбор).
Trigger — intent переноса. Owning capability — CAP-011.

### R2. New date/time selection

| Поле | Значение |
|---|---|
| actor | User ↔ Ayla ↔ Backend |
| trigger | Запись идентифицирована |
| пользовательская цель | Выбрать новое время для этой же записи |
| системное действие | Запросить актуальные слоты того же Offering/специалиста у Backend; displayed slot — не reservation *(факт — SRC-02 этап 10)*. Bot DM — компактные слоты кнопками; при необходимости расширенного выбора — deep link в Mini App (календарь), контекст записи и `recommendation_id` сохраняются *(факт — UX-OD-004)*. Смена мастера — W2 *(факт — UX-OD-001)* |
| отображаемое состояние | Кнопки слотов / календарь; slot unavailable при пустой выдаче |
| ошибка | `NO_AVAILABLE_SLOTS` |
| fallback | См. N-CR4 |
| owning capability | CAP-010 |

### R3. Explicit confirmation

| Поле | Значение |
|---|---|
| actor | User → Ayla |
| trigger | Выбрано новое время на R2 |
| пользовательская цель | Контролировать изменение записи |
| системное действие | Показать текущее и предлагаемое дата/время, услугу, специалиста; запросить явное подтверждение; без подтверждения ничего не переносить *(факт — UX-OD-001; AYLA-DEC-0022 п. 1)* |
| отображаемое состояние | Сводка «было → станет» + кнопки «Перенести» / «Оставить как есть» |
| ошибка | Отказ — валидный исход |
| fallback | Нейтральное acknowledgement; возврат к R2 при отказе от предложенного времени **(proposal)** |
| owning capability | CAP-011 |

### R4. Reschedule pending

| Поле | Значение |
|---|---|
| actor | Ayla → Backend |
| trigger | Явное подтверждение на R3 |
| пользовательская цель | Перенос выполнен ровно один раз, без потери записи |
| системное действие | Вызвать reschedule-операцию в booking SoR над тем же `appointment_id` (`expected_version` проверяется на стороне SoR); вызовы идемпотентны *(факт — AYLA-DEC-0022 п. 9, п. 10)* |
| отображаемое состояние | reschedule pending («Переношу…») |
| ошибка | `TOOL_TIMEOUT`, backend error, `APPOINTMENT_CONFLICT` (слот занят), запись более не активна/изменена |
| fallback | Переход в R5 reschedule_failed; исходная запись при любом отказе не меняется *(факт — AYLA-DEC-0022 п. 10)*; без авто-retry **(proposal)** |
| owning capability | CAP-011 |

### R5. Result: rescheduled / reschedule_failed

| Поле | Значение |
|---|---|
| actor | Backend → Ayla → User |
| trigger | Получен результат из SoR |
| пользовательская цель | Достоверный итог по одной записи |
| системное действие | **rescheduled:** успех только после authoritative подтверждения новой версии SoR; рекап той же записи (дата, время, услуга, специалист) — не «две записи» *(факт — UX-OD-001; AYLA-DEC-0022 п. 9; SRC-02 этап 12)*. **reschedule_failed:** честная ошибка + действия UX-OD-002: `retry` / `return_to_previous_safe_step` (к R2) / `try_later` / `exit`; явно сообщается, что запись **осталась на прежнем времени, не потеряна**; без оператора и автовыдачи контактов *(факт — UX-OD-002; AYLA-DEC-0022 п. 10)* |
| отображаемое состояние | rescheduled / reschedule_failed |
| owning capability | CAP-011 |

## Таблица состояний

| Состояние | Surface | Что видит пользователь | Действия | Запрещено показывать |
|---|---|---|---|---|
| C1 empty | bot DM | «Нет активных записей» | Продолжить диалог | Фиктивные записи |
| C1 select | bot DM | Кнопки активных записей | Выбрать, выйти | Прошлые/отменённые записи |
| C2/C3 summary | bot DM | Дата, время, услуга, специалист + последствия | Подтвердить, отказаться | Неподтверждённую каноном политику штрафов (OQ-1) |
| C4 pending | bot DM | «Отменяю…» | — | Успех до ответа SoR |
| C5 cancelled | bot DM | Итог + рекап | Записаться снова, выйти | Подтверждение без authoritative статуса |
| C5 cancel_failed | bot DM | Честная ошибка | Действия UX-OD-002 | Оператор, контакты мастера |
| R2 slots | bot DM / Mini App | Слоты кнопками / календарь | Выбрать слот, выйти | Смену мастера и расширенные альтернативы (W2) |
| R3 confirm | bot DM | Сводка «было → станет» | «Перенести», «Оставить» | Впечатление создания отдельной новой записи |
| R4 pending | bot DM | «Переношу…» | — | Успех до ответа SoR |
| R5 rescheduled | bot DM | Итог + рекап той же записи (новые дата/время) | Открыть запись, выйти | Два отдельных статуса вместо одного перенесённого состояния |
| R5 reschedule_failed | bot DM | «Перенос не выполнен, запись на прежнем времени» | Действия UX-OD-002; возврат к R2 | Маскировку факта неудачи; оператора; контакты |

## Негативные ветки

Каждая ветка разрешается в существующее состояние, новых экранов нет.

- **N-CR1. Stale slot.** Триггер: `APPOINTMENT_CONFLICT` при commit (R4).
  Поведение: «это время только что заняли»; возврат к **R2** с актуальными
  слотами, если данные актуальны *(факт — UX-OD-002)*. Состояние: R2 slot
  unavailable. Owning capability: CAP-010.
- **N-CR2. Backend timeout.** Триггер: `TOOL_TIMEOUT` на C4 / R4.
  Поведение: без авто-retry; pending завершается в соответствующий failed
  (C5 / R5 reschedule_failed) с действиями UX-OD-002; retry идемпотентен
  *(факт — SRC-02 N7; AYLA-DEC-0022 п. 9)*. Owning capability: CAP-018.
- **N-CR3. Гонка: запись уже изменена/неактивна.** Триггер: SoR возвращает
  «запись уже не активна» (C4) либо `expected_version` устарела/запись уже
  перенесена или отменена другим actor (R4). Поведение: не ошибка
  пользователя; сообщить фактическое состояние. Для cancel — завершить в
  **C5 cancelled**, если запись действительно уже отменена. Для reschedule
  — стоп без применения предложенного времени; показать актуальное
  состояние записи; возврат к **R1** для повторной идентификации *(факт —
  AYLA-DEC-0022 п. 9, п. 10 — expected_version + повторная проверка)*.
  Owning capability: CAP-011.
- **N-CR4. Reschedule недоступен — нет слотов.** Триггер:
  `NO_AVAILABLE_SLOTS` на R2. Поведение: честное «свободного времени нет»;
  явно сообщается, что текущая запись **не изменена, остаётся на прежнем
  времени** *(факт — AYLA-DEC-0022 п. 10)*; действия UX-OD-002
  (`try_later`, `exit`, повтор слотов позже). Другой мастер — W2 *(факт —
  UX-OD-001)*. Состояние: R2 slot unavailable. Owning capability: CAP-010.

## Open Questions

| # | Вопрос | Кому |
|---|---|---|
| OQ-1 | Политика отмены (дедлайны, штрафы, возвраты) подтверждена ли каноном? Формулировки «последствий» на C3 и no-fault возвраты из SRC-12 §4/§6 — proposal до owner decision | Product Owner |
| OQ-2 | Кто владеет доменным статусом `cancelled` и переходами cancel flow (аудит, отчётность)? *(2026-08-02: компенсация/аудит кейса «старая cancelled, новая не created» из формулировки снята — для Simple Reschedule (same-ID) этот кейс не существует, см. N-CR3/N-CR4 и AYLA-DEC-0022 п. 10)* | Booking owner |
| OQ-3 | Подтверждён ли механизм deep link Mini App → bot DM (канал MAX) и состав контекста (`appointment_id`, `recommendation_id`)? | Platform owner |
| OQ-4 | ~~Допустим ли retry создания записи по ранее выбранному слоту без повторного показа слотов (R6 failed-critical)?~~ **Закрыт 2026-08-02.** Для Simple Reschedule сценарий failed-critical не существует: same-ID транзакция атомарна, при любом отказе исходная запись не меняется (AYLA-DEC-0022 п. 10); retry на R4 — обычный idempotent retry той же pending-операции, не создание отдельной записи. | — |
| OQ-5 | Уведомление провайдера об отмене/переносе: контур и формулировки вне scope этого документа | Product Owner |

## Источники и связь

- UX-OD-001 (механика cancel/reschedule, deferred W2), UX-OD-002 (действия
  при ошибках), UX-OD-004 (роли каналов); SRC-02 этапы 10–12, N4, N6–N7 —
  инварианты (SoR, Request ≠ Created ≠ Confirmed, идемпотентность).
- **AYLA-DEC-0022** — Appointment Reschedule and Replacement Model
  (accepted, 2026-07-28), п. 1, п. 2, п. 9, п. 10: same-ID модель,
  reschedule-матрица, событие `appointment.rescheduled`, concurrency/
  expected_version. Источник reschedule-механики R1–R5 (2026-08-02,
  заменяет ранее описанную cancel_then_create_new_booking).
- **AYLA-DEC-0036** (OD-RESCHED-1) — Wave 1 Simple Reschedule owner ruling
  (registered 2026-08-02, `OWNER_DECISION_REGISTER.md`): формально
  запрещает cancel_then_create_new_booking для этого сценария и фиксирует
  deferred-scope Wave 1; применение AYLA-DEC-0022 к UX-слою, не
  переопределение канона.
- `docs/screens/customer-cancellation-reschedule-flow.md` (SRC-12, stale) —
  переиспользовано для cancel flow: intent resolution по числу записей.
  Отброшено как вне UX-OD-001/AYLA-DEC-0022: смена мастера, full-screen
  flows, no-fault каскад, billing chain copy, модель «старая отменена,
  новая не создана» (не применима к same-ID reschedule).

## Change Log

### v0.4 (2026-08-02) — Cancellation scope reconciliation + naming sync

- Добавлен явный блок «Границы scope (cancel)»: C1–C5 — **minimal
  conversational cancel**, единственная cancel-механика Wave 1
  (UX-OD-001); full Cancellation journey (policy/deadline/refund,
  standalone screens, late-window/waitlist, провайдер-уведомления)
  остаётся deferred (owner ruling 2026-07-28, вариант Б; формализовано в
  AYLA-DEC-0036). Устраняет противоречие: документ ранее специфицировал
  C1–C5 как активную Phase 1 ветку без указания, что это не есть полная
  cancellation journey.
- Naming: `booking_id` → `appointment_id` в Entry points и OQ-3 (canonical
  Appointment reference; `booking_id` — legacy compatibility adapter, см.
  Ayla Core Domain Model Specification §14 naming rules). Семантика C1–C5,
  R1–R5 не изменена.

### v0.3 (2026-08-02) — Owner ruling formally registered (AYLA-DEC-0036)

Owner ruling для Wave 1 Simple Reschedule формально зарегистрирован как
**AYLA-DEC-0036** (OD-RESCHED-1) в `OWNER_DECISION_REGISTER.md`. Добавлена
ссылка в `basis` frontmatter и в раздел «Источники и связь». Семантика
R1–R5, state-таблицы и Open Questions (v0.2) не изменена.

### v0.2 (2026-08-02) — Wave 1 Simple Reschedule canon alignment

Reschedule-ветка (ранее R1–R6, cancel_then_create_new_booking) переписана
на same-ID модель по AYLA-DEC-0022: R1 Identify → R2 New date/time
selection → R3 Explicit confirmation → R4 Reschedule pending → R5 Result
(rescheduled / reschedule_failed). Cancel-ветка (C1–C5) не изменена.
Обновлены: state-таблица (reschedule-строки), N-CR1/N-CR3/N-CR4 (возврат к
R2/R1 вместо R4, без промежуточного `cancelled`), OQ-2 (снята
компенсация/аудит двух записей), OQ-4 (закрыт — failed-critical сценарий
не существует для same-ID). Добавлена traceability на AYLA-DEC-0022 и
`appointment.rescheduled`.

### v0.1 (2026-07-29) — Initial draft

Stage specifications cancel/reschedule по UX-OD-001/002/004 (UX-SPEC-001).
