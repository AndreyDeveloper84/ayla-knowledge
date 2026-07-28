# Decision Brief — Availability and Slot Model (AYLA-DEC-0021)

> **Статус:** owner ruling received (v0.2) — готов к записи AYLA-DEC-0021
> в [[Ayla Decision Log]] после показа diff владельцу. Размещён в
> `99 Archive/proposals/` — validator-exempt (`scripts/validate_knowledge.py`,
> `IGNORED_PARTS`).
> **Дата:** 2026-07-28 (v0.1); 2026-07-28 (v0.2, owner ruling applied) ·
> **Автор:** Domain Architecture (подготовка) ·
> **Целевая запись:** AYLA-DEC-0021 · **Зависит от:** AYLA-DEC-0016
> (Subject Identity Model), AYLA-DEC-0017 (Tenant, Membership and Role
> Model), AYLA-DEC-0020 (Service Offering ownership and Specialist
> assignment — действует; п. 9 отсылает к настоящему решению) ·
> **Связано:** AYLA-DEC-0025 (Domain Event Registry — конвенция событий)

## 1. Проблема и блокируемые разделы CDM

CDM §7.10 моделирует доступность одним хранимым объектом **Availability
Slot** (`slot_id, specialist_id, offering_id, starts_at, ends_at, status,
source, version, expires_at`) с lifecycle `available → held → booked (↘
released / expired)`. Это единственная модель времени мастера во всей CDM:

- **нет рабочего расписания** — из чего слот возникает, модель не знает;
  поле `source` не имеет определённого доменного referent'а;
- **нет блокировок** — отпуск, больничный, ручная блокировка и внешняя
  занятость (YClients) невыразимы иначе как «отсутствие слота», что не
  отличимо от «слот ещё не сгенерирован» и не несёт actor/reason/audit
  (требование CDM §9);
- **слот прибит к Offering**: каждый рабочий интервал мастера материализуется
  строкой на каждую услугу мастера — N услуг × M интервалов × горизонт
  бронирования хранимых строк, пересчитываемых при любом изменении
  длительности, расписания или набора услуг;
- **владелец объекта не назначен**: CDM §22 — Availability Slot
  `unresolved` (§24, Architecture п. 2); CDM §18 CDM-AC-01 — `PARTIAL`;
  строка SoR (§12) — `proposal` по всем колонкам;
- per-object commands/events для Availability Slot отсутствуют в §10/§11 —
  несоответствие [[Ayla MVP Documentation Roadmap]] §4.3.

AYLA-DEC-0020 (действует) зафиксировал коммерческую цепочку Catalog
Service → Service Offering → Specialist Offering Assignment → Specialist
Membership → Specialist Profile, effective_duration assignment (п. 3) и
расчёт слота от effective_duration (п. 9, «детальный алгоритм доступности —
planned AYLA-DEC-0021»); ссылка `assignment.specialist_id` запрещена (п. 3),
`specialist_id` как SoR-атрибут запрещён (п. 8). Настоящее решение
определяет алгоритм доступности поверх этой цепочки.

Решение блокирует: CDM §7.10 (переопределение объекта), §8.6–8.7, §10–§11
(реестры команд и событий), §12 (SoR), §19 (ERD), §21–§24, а также
MVP-формулировку Availability в [[Ayla MVP Scope and Release Contract]]
§4.1 («Актуальные слоты пилотных провайдеров», CAP-010).

CAP-010 (Capability Registry §6.10) уже декларирует раздельные концепты —
`Schedule`, `Availability Window`, `Slot`, `Block`, `Working Rule`,
`Resource Constraint`, `Availability Version` — и инварианты «Displayed
slot не reservation», «Manual block приоритетен», «Slot проверяется при
commit booking», «Availability не владеет appointment lifecycle». CDM §7.10
этому составу не соответствует: в модели есть только Slot.

## 2. Реальные сценарии

Из handoff-материалов с точными ссылками (handoff — источник сценариев,
не канон; внутренние модели и события handoff'ов в DEC не переносятся):

- **S1. Услуги разной длительности и буферы.** Длительность обязана быть
  resolved на bookable-уровне (`orch.txt`, §10: «Для booking duration
  обязана быть resolved на bookable-уровне»); разрешение длительности —
  `specialist → salon → template` (`stream1.txt`, таблица решений D1);
  буфер — на назначении услуги мастеру: `buffer_after_minutes …
  unique(specialist, salon_service)` (`stream1.txt`, строка 25).
  Канонизировано AYLA-DEC-0020 п. 3 (`duration_override`,
  `effective_duration`).
- **S2. Защита от двойной брони при внешнем календаре.** «YClients inbound
  availability sync required if pilot salon continues using YClients as
  operational calendar» (`orch.txt`, строка 315); gate G-CalendarSync
  (`orch.txt`, строки 325–331); «Ayla должна уметь заблокировать окно
  мастера как external_busy» без service mapping (`orch.txt`, строки
  353–370). Подключение YClients — часть onboarding салона
  (salon-onboarding-handoff; предоставлен владельцем на owner review
  2026-07-28).
- **S3. Администратор вносит offline-записи.** «все phone/walk-in/offline
  записи администратор заносит в Ayla» (`orch.txt`, §9 Вариант A;
  подтверждено AYLA-DEC-0017, роль `admin`).
- **S4. Runtime отдаёт слоты как вычисляемый read model.** `GET
  /api/v1/internal/specialists/{id}/slots/?service_id&date=` возвращает
  список ISO-времён за день; range-endpoint нет (`ai-bot-platform/docs/
  architecture/ayla-booking-rest-contract.md`, строки 68, 106–111);
  конфликт при бронировании — `409 SLOT_TAKEN` (там же, строки 160, 167).
- **S5. Hold живёт в booking flow.** Booking flow хранит `slot_id` как
  часть контекста шага (`UX-T0.txt`, строки 139–157); UX первой записи и
  переноса (customer-first-time-handoff; предоставлен владельцем на owner
  review 2026-07-28): hold — короткоживущее состояние бронирования, а не
  состояние рабочего времени мастера.
- **S6. Time off.** Больничный (немедленный, день за днём), отпуск и
  planned leave (заранее, с согласованием), изменение recurring-графика,
  per-booking remediation затронутых записей (master-time-off-handoff;
  предоставлен владельцем на owner review 2026-07-28). **Подтверждён.**
- **S7. Recurring schedule.** Рабочая неделя мастера как версионируемый
  шаблон с датами начала/окончания действия; смена будущего графика не
  переписывает прошлое (master-time-off-handoff, требование versioned
  recurring weekly rules; предоставлен владельцем на owner review
  2026-07-28). **Подтверждён.**
- **S8. Замена мастера.** Замещение и проверка доступности замещающего
  (master-substitution-handoff; предоставлен владельцем на owner review
  2026-07-28; workflow substitute — deferred по AYLA-DEC-0017 п. 9).
  Доступность замещающего вычисляется из его собственных правил.
- **S9. Self-service мастера.** Мастер инициирует availability request из
  мобильного интерфейса; график показывает состояния booking/free/blocked
  (master-mobile-handoff; предоставлен владельцем на owner review
  2026-07-28). **Подтверждён** (объём self-service — §10, §16).
- **S10. Offboarding мастера.** Будущие записи после отзыва доступа —
  remediation (master-offboarding-handoff; AYLA-DEC-0017 п. 7).

## 3. Варианты модели

### Вариант A — Статус-кво: slot as stored entity per offering (CDM §7.10)

- **Плюсы:** явная строка под каждое окно; тривиальный unique-констрейнт;
  прямой FK из Appointment.
- **Минусы:** декартово произведение «интервалы × услуги × горизонт»;
  изменение длительности/буфера инвалидирует массив строк; S2 (external_busy
  без услуги) невыразим; S3 требует фиктивных слот-строк; S6 — массовое
  удаление строк вместо одной блокировки с audit; S7 требует фоновой
  генерации, которой в модели нет; противоречит эксплуатируемому контракту
  S4 и составу концептов CAP-010; `slot_id` как постоянный UUID сущности
  несовместим с цепочкой DEC-0020 (ключ через assignment).

### Вариант B — Правила + проекция (рекомендуемый; подтверждён owner ruling)

- **Availability Calendar** — календарь доступности локации; несёт IANA
  timezone; в MVP один на tenant (наследует `Tenant.default_timezone`).
- **Availability Rule** — версионируемый недельный шаблон рабочего времени
  (`effective_from`/`effective_until`); хранится.
- **Schedule Block** — интервал недоступности: `manual`, `sick_day`,
  `time_off`, `external_busy`; хранится, с actor/reason/audit.
- **Bookable Slot / Slot Projection** — **вычисляемый, не хранимый** read
  model; ключ `(specialist_offering_assignment_id, starts_at)`.
- **Slot Hold** — хранимое короткоживущее удержание ключа слота с TTL.

Плюсы/минусы — как в v0.1; направление подтверждено владельцем.

### Вариант C — Гибрид: материализованная сетка из правил

Отклонён (v0.1): сетка — кэш, выдаваемый за SoR (нарушение CDM §13);
двойной write-path; минусы A по объёму сохраняются.

## 4. Рекомендуемый вариант

**Вариант B**, MVP-срез и platform-scope:

- **MVP-active:**
  - Availability Calendar: один на tenant, timezone наследует
    `Tenant.default_timezone` (IANA, например `Europe/Moscow`);
  - Availability Rule: недельный шаблон (день недели × интервалы),
    версионируемый с `effective_from`/`effective_until`; изменение будущего
    pattern создаёт новую версию и не переписывает историческую (S7);
  - Schedule Block: типы `manual`, `sick_day`, `time_off`, `external_busy`;
    date exceptions выражаются блоками (не deferred);
  - Slot Projection: вычисление на чтении; горизонт — tenant-configurable
    параметр чтения, дефолт 30 дней;
  - Slot Hold: TTL 15 минут (платформенный параметр);
  - self-service split: SICK_DAY немедленно; vacation/planned
    leave/recurring change — через approval workflow; availability request
    мастера поддержан моделью и authorization contracts;
  - DB-enforced защита от пересечений интервалов (§11).
- **Platform-scope / deferred:** произвольный RRULE и сложная
  рекуррентность; свободный редактор расписания мастера; resource
  constraints (кабинеты, оборудование); multi-resource и multi-service
  Appointment; substitute-переназначение как workflow (AYLA-DEC-0017 п. 9);
  двусторонняя календарная синхронизация; импорт рабочих правил из внешних
  календарей; waitlist; overbooking-политики; parallel capacity.

## 5. Сущности и кардинальности

```yaml
Availability Calendar:            # хранится; SoR — CAP-010 (MVP: 1 per tenant)
  calendar_id:
  provider_id:                    # tenant-скоуп (1 Provider = 1 Tenant в MVP)
  timezone:                       # IANA (Europe/Moscow), НЕ смещение UTC+3
  # MVP: наследует Tenant.default_timezone; локации — post-MVP

Availability Rule:                # хранится; SoR — CAP-010; versioned
  rule_id:
  calendar_id:
  specialist_membership_id:       # канон по AYLA-DEC-0020 (НЕ specialist_id)
  weekday_template:               # [{weekday, intervals:[{start,end}]}] — local wall time календаря
  effective_from:
  effective_until:                # nullable
  status:                         # draft | active | suspended | archived
  version:
  created_by / updated_by:

Schedule Block:                   # хранится; SoR — CAP-010
  block_id:
  calendar_id:
  specialist_membership_id:
  starts_at:                      # UTC
  ends_at:                        # UTC
  block_type:                     # manual | sick_day | time_off | external_busy
  source:                         # manual | yclients | …
  external_ref:                   # nullable; ключ ExternalMapping (AYLA-DEC-0020 п. 7)
  source_updated_at:              # nullable; версия данных внешней системы
  observed_at:                    # когда Ayla зафиксировала факт
  sync_status:                    # synced | pending | quarantined | stale
  reason:                         # nullable для external_busy
  status:                         # active | cancelled
  created_by:

Slot Hold:                        # хранится; SoR — CAP-010
  hold_id:
  specialist_offering_assignment_id:   # ключ слота, ч. 1 (DEC-0020)
  starts_at:                      # ключ слота, ч. 2 (UTC)
  ends_at:                        # starts_at + effective_duration + buffers
  provider_id:                    # денормализация tenant-скоупа
  subject_id:                     # клиент (AYLA-DEC-0016)
  status:                         # held | confirmed | expired | released
  release_reason:                 # nullable; client_abort | AVAILABILITY_CHANGED | …
  expires_at:                     # created_at + TTL (15 мин)
  idempotency_key:
  created_at:

Bookable Slot (Slot Projection):  # НЕ хранится; без SoR
  key: (specialist_offering_assignment_id, starts_at)
  # assignment_id однозначно определяет tenant, membership, offering,
  # effective_duration и buffers (AYLA-DEC-0020 пп. 3, 9)
  # входы: active Rules, active Blocks (вкл. external_busy), будущие
  #        active Appointment, активные Holds, timezone календаря
  # API: допустим подписанный projection token с версией входных данных —
  #      transport-артефакт, НЕ сущность и НЕ SoR; slot_id UUID не вводится
```

Кардинальности: Tenant 1—1 Availability Calendar (MVP); Calendar 1—0..N
Rule и 1—0..N Block; Specialist Membership 1—0..N версий Rule
(пересечение `active`-версий по времени запрещено); ключ слота 1—0..1
активный Slot Hold; Slot Hold 0..1—1 Appointment; Appointment 1—1 ключ
слота (факт записи, §14). Rule и Block не ссылаются на Offering: рабочее
время и занятость — свойства мастера; услуга вступает через ключ проекции.

## 6. Lifecycle и переходы

```text
Availability Rule: draft → active ⇄ suspended → archived [terminal, retained]
                   (новая версия pattern = новая Rule-версия с effective_from;
                    предшествующая получает effective_until, не переписывается)
Schedule Block:    active → cancelled [terminal, retained]
Slot Hold:         held → confirmed      # Appointment подтверждён (транзакция §11)
                        ↘ expired        # TTL 15 мин истёк
                        ↘ released       # client_abort | AVAILABILITY_CHANGED | admin
```

Правила Slot Hold: (1) терминальные записи не удаляются (audit, CDM §9);
(2) истечение TTL — системный процесс или лениво при первом касании после
`expires_at`, оба пути публикуют один факт; (3) повторный hold того же
ключа тем же `subject_id` идемпотентен по `idempotency_key`; (4) **при
создании Schedule Block или изменении Availability Rule система находит
конфликтующие активные hold и переводит их в `released` с
`release_reason = AVAILABILITY_CHANGED` + audit + уведомление активной
booking session + предложение пересчитать варианты** — hold не остаётся
визуально активным до TTL; (5) `confirmed` hold не освобождает слот:
занятость далее несёт Appointment, hold сохраняется как provenance.

## 7. Команды и события

Имена событий — в канонической dot-separated форме AYLA-DEC-0025
(регистрация в [[Ayla Domain Event Registry]], owner — Availability
context, класс `domain_fact`; scope и PII-классификация фиксируются при
регистрации).

Команды (дополнение CDM §10):

```text
Administrative (owner/admin):  SetAvailabilityRule        # новая версия шаблона
                 SuspendAvailabilityRule / ArchiveAvailabilityRule
                 CreateScheduleBlock       # manual | time_off
                 CancelScheduleBlock
                 CreateOfflineAppointment  # без hold; overlap-проверка обязательна (§11)
                 CreateOverrideAppointment # запись вне Rule: actor + reason обязательны;
                                           # пересечение с Appointment запрещено (§11)
                 ApproveAvailabilityRequest / RejectAvailabilityRequest
Specialist (self-service): SubmitAvailabilityRequest  # vacation/planned leave/recurring change
                 RecordSickDay             # немедленный эффективный Block sick_day
User (booking):  HoldSlot / ReleaseSlotHold
System:          ExpireSlotHold            # TTL
                 ConfirmSlotHold           # в транзакции ConfirmAppointment (§11)
                 ReleaseConflictingHolds   # AVAILABILITY_CHANGED (§6)
                 ImportExternalBusyBlock   # идемпотентный upsert по external_ref (§12)
```

События (дополнение CDM §11 / Domain Event Registry):

```text
availability_rule.set / .suspended / .archived
schedule_block.created / .cancelled
slot_hold.created / .confirmed / .expired / .released   # release_reason в payload
external_busy.imported                                   # upsert-факт, sync_status
availability_request.submitted / .approved / .rejected
sick_day.recorded                                        # = schedule_block.created(type=sick_day), отдельным событием для уведомления admin
```

События «слот появился/исчез» не существуют: проекция — не доменный факт.
`PendingAppointmentExpired` (CDM §11) остаётся событием Appointment.

## 8. System of Record

| Объект | Хранится/вычисляется | System of Record | Примечание |
|---|---|---|---|
| Availability Calendar | хранится | Availability Management (CAP-010) | MVP: 1 per tenant, timezone от Tenant.default_timezone |
| Availability Rule | хранится | Availability Management (CAP-010) | versioned |
| Schedule Block | хранится | Availability Management (CAP-010) | вкл. `external_busy` |
| Slot Hold | хранится | Availability Management (CAP-010) | SoR удержания, не записи |
| Bookable Slot / Slot Projection | **вычисляется** | **без SoR** (derived) | кэш — только non-authoritative read optimization; projection token — transport, не SoR |
| Appointment (занятость ключа) | хранится | Appointment Management (CAP-011) | как в CDM §12 |
| Внешняя запись (YClients) | внешняя | **внешняя система** | Ayla ей не владеет |
| Локальная проекция external busy | хранится | Availability Management (CAP-010) | Schedule Block: `source`, `external_ref`, `source_updated_at`, `observed_at`, `sync_status`; идемпотентное обновление существующего блока, дубли от повторных webhook запрещены |

Граница с AYLA-DEC-0020: длительность и буферы — атрибуты Offering /
Assignment (`effective_duration`), Availability их **читает** через
`specialist_offering_assignment_id` и не дублирует. Строка «Availability
Slot» в CDM §12 заменяется строками Calendar/Rule/Block/Hold.

## 9. Tenant boundary

- Calendar, Rule, Block, Hold несут tenant-скоуп (`provider_id` /
  `calendar_id`); `specialist_membership_id` резолвится в tenant через
  active Membership (AYLA-DEC-0017, AYLA-DEC-0020 п. 3).
- Мастер с Membership в нескольких салонах имеет независимые правила и
  блоки per tenant; проекции cross-tenant не смешиваются.
- external_busy импортируется строго внутрь одного tenant'а
  (`company_id → tenant`, `staff_id → specialist membership`, orch.txt
  строки 363–364; ExternalMapping — AYLA-DEC-0020 п. 7).
- Revoke Membership исключает правила и блоки мастера из проекции
  tenant'а немедленно; будущие Appointment — remediation (AYLA-DEC-0017
  п. 7).

## 10. Authorization rules

- Управление Rule/Block своего tenant'а: `owner`, `admin` («работа с
  расписанием», AYLA-DEC-0017 п. 6); actor/reason, аудит.
- **Self-service мастера (split, owner ruling):**
  - `RecordSickDay` — мастер в пределах своего tenant assignment;
    немедленный эффективный Block `sick_day` + audit + уведомление admin;
  - `SubmitAvailabilityRequest` (vacation, planned leave, recurring
    change) — мастер инициирует; вступает в силу через approval workflow
    (owner/admin); модель и authorization contracts поддерживают requests
    уже сейчас;
  - свободный редактор расписания — deferred;
  - assignment-level доступность (`active → self_disabled`) — по
    AYLA-DEC-0020 п. 5, настоящим решением не ограничивается.
- `CreateOfflineAppointment` — owner/admin, audit обязателен, те же
  overlap-проверки (§11). `CreateOverrideAppointment` (вне Rule) — явная
  override-команда с actor и reason; пересечение с другой Appointment
  запрещено даже override до введения политики parallel capacity.
- HoldSlot/ReleaseSlotHold — клиент (`subject_id`) в booking flow.
- Чтение проекции: публично в рамках каталога tenant'а; наружу только
  занято/свободно без reason блоков.
- Ни одна операция availability не даёт доступа к memory/consent клиента
  (AYLA-DEC-0017 п. 8).

## 11. Invariants

1. **Ключ слота не занимается дважды — DB-enforced по интервалам.**
   Обычный UNIQUE INDEX недостаточен: он не защищает пересечение
   интервалов (14:00–15:00 vs 14:30–15:30). Обязательно: PostgreSQL
   exclusion constraint по `tstzrange` ЛИБО единый Time Reservation
   ledger (`reservation_kind = hold | appointment`, `resource_key`,
   `occupied_range`, `active`) с exclusion constraint для активных
   reservation одного ресурса. Если Hold и Appointment — разные таблицы,
   обязательна **общая locking boundary** (единый порядок блокировок
   ресурса для hold, confirm, offline и override путей). Выбор физической
   формы — implementation; инвариант фиксирован доменно. Нарушение →
   `SLOT_TAKEN`.
2. **ConfirmAppointment — одна транзакция:** блокировать hold/reservation
   → проверить статус hold и TTL → повторно проверить актуальные
   Rule/Block/external busy (ключ всё ещё выводится) → создать
   Appointment → перевести hold в `confirmed` → зафиксировать
   идемпотентный результат. Повторный confirm — идемпотентен.
3. **Hold имеет TTL 15 минут;** истёкший hold не удерживает ключ и не
   подтверждается. Изменение Rule/Block переводит конфликтующие активные
   hold в `released` (`AVAILABILITY_CHANGED`) немедленно, не дожидаясь
   TTL (§6).
4. **Offline/override:** Appointment админа создаётся без hold, но с теми
   же overlap-проверками и в той же locking boundary; пересечение с
   другой Appointment запрещено и для override (parallel capacity не
   введена).
5. Displayed slot — не reservation (CAP-010); гарантия возникает только
   на Hold.
6. Manual block приоритетен (CAP-010).
7. **Timezone:** хранение UTC; recurring rules — local wall time + IANA
   timezone календаря (`Europe/Moscow`, не `UTC+3`); границы дня — в
   timezone календаря; в MVP календарь наследует `Tenant.default_timezone`;
   клиенту — время места оказания услуги с явной зоной; timezone
   устройства — только дополнительная display-проекция; timezone создания
   записи фиксируется snapshot-полем; «завтра в 14:00» интерпретируется в
   зоне места услуги и отражается в подтверждении; исторические
   Appointment не переписываются.
8. Availability не владеет appointment lifecycle (CAP-010): ни один
   переход Calendar/Rule/Block/Hold не меняет статус Appointment;
   последствия — remediation items (AYLA-DEC-0017 п. 7).
9. Создание/активация Rule и Block требует active Membership для связки
   (specialist, provider) (AYLA-DEC-0017, AYLA-DEC-0020).
10. Проекция не является authoritative состоянием и не публикуется как
    доменный факт (CDM §3.5, §13).
11. External busy — идемпотентный upsert по `external_ref`: повторный
    webhook обновляет существующий блок, дубли запрещены.

## 12. Последствия для импорта из YClients

- **Внешняя занятость → Schedule Block `external_busy`** (подключается при
  onboarding салона, salon-onboarding-handoff). Поля: `source`,
  `external_ref`, `source_updated_at`, `observed_at`, `sync_status`
  (§5, §8). Идемпотентный upsert по `external_ref`; удаление/перенос
  внешней записи — отмена/пересоздание блока тем же идемпотентным путём;
  неизвестный `staff_id` — блок в `sync_status = quarantined` с
  уведомлением admin, не молчаливый пропуск.
- **G-CalendarSync (усилен, owner ruling):** несинхронизированный
  dual-source запрещён (orch.txt строки 331–347). Дополнительно:
  - максимально допустимый возраст синхронизации (freshness limit);
    поведение при недоступном webhook/import; reconciliation job;
    мониторинг расхождений (block-c/alpha.md строки 73, 84–85);
    идемпотентность событий; обработка удаления/переноса внешней записи;
    действие при неизвестном staff_id; degraded mode;
  - правило: freshness сверх лимита → Ayla **не подтверждает**
    автоматически, либо требует синхронной проверки внешней системы при
    confirm; если проверка невозможна — отдельный временный reason code
    (НЕ `SLOT_TAKEN`);
  - точный SLA, лимиты и коды — в integration contract, не в доменном DEC.
- **Внешнее расписание (рабочие часы)** в Availability Rule не
  импортируется (deferred, §15); правила вводит owner/admin или мастер
  через request/approval (§10).
- **Mapping** — ExternalMapping (AYLA-DEC-0020 п. 7) единый для каталога
  и занятости.
- Вариант «Ayla primary calendar» работает без YClients: занятость несут
  Appointment и ручные Block.

## 13. Migration impact

- **CDM (v1.3):** §7.10 переписывается (Calendar, Rule, Block, Hold,
  Projection); §7.12 — ключ слота через `specialist_offering_assignment_id`
  + `starts_at`, nullable `hold_id`, snapshot timezone (стыковка с
  DEC-0020 п. 8); §8.6–8.7, §10–§11 (команды/события §7), §12 (таблица
  §8), §19 (Slot — derived), §21 (инварианты §11), §22 (снятие
  `unresolved`), §23 (детализация CAP-010), §24 (закрытие Arch п. 2).
- **Domain Event Registry:** регистрация событий §7 по конвенции
  AYLA-DEC-0025 (dot-separated, owner — Availability context).
- **Scope Contract:** формулировка CAP-010 в §4.1 уточняется; deferred —
  через §11.
- **Capability Registry:** состав `owned_concepts` CAP-010 покрывает
  модель без изменений.
- **Decision Log:** запись AYLA-DEC-0021 (формулировка §17).
- **Runtime (вне канона):** REST-контракт слотов соответствует проекции
  (S4); добавляются hold-эндпоинт, подписанный projection token,
  exclusion constraint / Time Reservation ledger, webhook-контур
  external_busy с reconciliation job; генератор per-offering слотов, если
  существует, выводится из критического пути.
- **Данные:** персистентных строк §7.10-модели в пилотном объёме нет (S4);
  подтверждение отсутствия хранимых слот-таблиц — precondition.

## 14. Влияние на Appointment и Recommendation

- **Appointment (§7.12, в связке с DEC-0020 п. 8):** хранит ключ слота
  (`specialist_offering_assignment_id`, `starts_at`, `ends_at` — факт
  записи, historical-integrity), nullable `hold_id` (offline/override —
  без hold) и snapshot timezone создания записи. Инвариант «нельзя
  подтвердить запись на недоступный Slot» = атомарная проверка §11 п. 2.
  Reschedule требует нового hold на новый ключ; сам reschedule lifecycle —
  CDM §24 Arch п. 12, отдельный трек.
- **Recommendation (§7.11):** кандидаты включают доступность как
  вычисляемый вход; Recommendation хранит снапшот предложенных ключей с
  `presented_at`; hold создаётся только при переходе к бронированию;
  `NO_AVAILABLE_SLOTS` — reason code результата (Roadmap). Recommendation
  не равна Appointment (инв. 8 §7.11).

## 15. Отложенные возможности (deferred)

Активация — только через change control [[Ayla MVP Scope and Release
Contract]] §11:

- произвольный RRULE и сложная рекуррентность (скользящие/плавающие
  графики); **date exceptions НЕ deferred — выражаются Schedule Block**;
- свободный редактор расписания мастера (self-service requests и approval
  workflow — НЕ deferred, §10);
- resource constraints (кабинеты, оборудование), parallel capacity,
  multi-resource и multi-service Appointment;
- импорт рабочих правил из внешних календарей; двусторонняя
  синхронизация;
- substitute-переназначение как workflow (AYLA-DEC-0017 п. 9);
- waitlist, overbooking-политики, динамический шаг сетки;
- Availability Version как публикуемый контракт;
- несколько Availability Calendar / локаций на tenant.

## 16. Открытые вопросы владельцу

Закрыты owner ruling 2026-07-28 (v0.2):

- ~~Q1. TTL Slot Hold~~ → **закрыт:** 15 минут, платформенный параметр.
- ~~Q2. Self-service мастера~~ → **закрыт (split):** SICK_DAY немедленно;
  vacation/planned leave/recurring change — approval workflow; свободный
  редактор — deferred (§10).
- ~~Q3. Гранулярность шаблона~~ → **закрыт:** день недели × интервалы;
  date exceptions через Schedule Block; versioned rules
  (effective_from/effective_until) — в MVP.
- ~~Q4. Горизонт проекции~~ → **закрыт:** 30 дней, tenant-configurable
  параметр чтения.
- ~~Q5. Сценарии S6/S7~~ → **закрыт:** подтверждены
  (master-time-off-handoff, master-mobile-handoff; §2).
- ~~Q6. Offline-запись~~ → **закрыт:** без hold, с audit и теми же
  overlap-проверками; запись вне Rule — override-команда; пересечение с
  Appointment запрещено (§10, §11).
- ~~Q8. Нумерация~~ → **закрыт:** AYLA-DEC-0019 — Intent Detected
  Lifecycle Boundary, AYLA-DEC-0020 — Offering/Assignment (обе в
  журнале); настоящее решение — AYLA-DEC-0021.

Остаются открытыми:

- **Q7. Retention блоков и hold-записей** (audit vs retention manifest,
  механика AYLA-DEC-0016 п. 7) — не адресован owner ruling.
- **Q9. Точный SLA/freshness-лимиты синхронизации** — по ruling выносится
  в integration contract (не доменный DEC); подтвердить, что доменному
  DEC достаточно правила «stale → no auto-confirm / sync check /
  отдельный reason code».

## 17. Owner ruling (AYLA-DEC-0021) — финальная формулировка

> **AYLA-DEC-0021 — Availability and Slot Model**
>
> **Решение:**
>
> 1. **Bookable Slot — вычисляемая проекция без System of Record.**
>    Ключ слота — `(specialist_offering_assignment_id, starts_at)`;
>    assignment_id однозначно определяет tenant, membership, offering,
>    effective_duration и buffers (AYLA-DEC-0020). `slot_id` как
>    постоянный UUID доменной сущности не вводится; для API допустим
>    подписанный projection token с версией входных данных —
>    transport-артефакт, не SoR. Модель «slot as stored entity per
>    offering» (CDM §7.10) отменяется.
> 2. **System of Record:** Availability Calendar, Availability Rule,
>    Schedule Block, Slot Hold → Availability Management (CAP-010);
>    Bookable Slot — без SoR (derived); Appointment → Appointment
>    Management (CAP-011); внешняя запись YClients — внешняя система;
>    локальная проекция external busy → CAP-010 как Schedule Block с
>    полями `source`, `external_ref`, `source_updated_at`, `observed_at`,
>    `sync_status` и идемпотентным обновлением существующего блока
>    (дубли от повторных webhook запрещены). Открытый вопрос CDM §24
>    (Architecture п. 2) закрыт назначением owner CAP-010.
> 3. **Slot Hold:** lifecycle `held → confirmed | expired | released`;
>    TTL 15 минут — платформенный параметр. ConfirmAppointment — одна
>    транзакция: блокировать hold/reservation → проверить статус и TTL →
>    повторно проверить актуальные Rule/Block/external busy → создать
>    Appointment → перевести hold в `confirmed` → зафиксировать
>    идемпотентный результат. Истёкший hold не подтверждается; повторный
>    confirm идемпотентен; нарушение занятости → `SLOT_TAKEN`.
> 4. **Защита от двойной записи — DB-enforced по интервалам.** Обычный
>    UNIQUE INDEX недостаточен (не защищает пересечения 14:00–15:00 vs
>    14:30–15:30). Обязателен PostgreSQL exclusion constraint по
>    `tstzrange` ЛИБО единый Time Reservation ledger (`reservation_kind =
>    hold | appointment`, `resource_key`, `occupied_range`, `active`) с
>    exclusion constraint для активных reservation одного ресурса; если
>    Hold и Appointment — разные таблицы, обязательна общая locking
>    boundary для всех путей занятия интервала.
> 5. **Timezone:** хранение UTC; recurring rules — local wall time +
>    IANA timezone календаря доступности (например `Europe/Moscow`, не
>    `UTC+3`); границы дня — в timezone календаря; в MVP календарь один
>    на tenant и наследует `Tenant.default_timezone`; клиенту — время
>    места оказания услуги с явной зоной; timezone устройства — только
>    дополнительная display-проекция; timezone создания записи —
>    snapshot-поле; «завтра в 14:00» интерпретируется в зоне места
>    услуги и отражается в подтверждении; исторические Appointment не
>    переписываются.
> 6. **Изменение расписания:** создание Schedule Block или изменение
>    Availability Rule немедленно переводит конфликтующие активные hold
>    в `released` с reason `AVAILABILITY_CHANGED` + audit + уведомление
>    активной booking session + предложение пересчитать варианты; hold не
>    остаётся визуально активным до TTL. Appointment автоматически не
>    изменяются — обязательные remediation items `needs_resolution`
>    (AYLA-DEC-0017 п. 7). События «слот исчез» не существует.
> 7. **G-CalendarSync:** несинхронизированный dual-source запрещён.
>    Определяются: max допустимый возраст синхронизации, поведение при
>    недоступном webhook/import, reconciliation job, мониторинг
>    расхождений, идемпотентность событий, обработка удаления/переноса
>    внешней записи, действие при неизвестном staff_id (quarantined +
>    уведомление), degraded mode. Freshness сверх лимита → Ayla не
>    подтверждает автоматически либо требует синхронной проверки внешней
>    системы; если проверка невозможна — отдельный временный reason code
>    (НЕ `SLOT_TAKEN`). Точный SLA — в integration contract, не в
>    доменном DEC.
> 8. **Offline/admin-записи:** Appointment создаётся без hold, с
>    обязательным audit и теми же overlap-проверками в той же locking
>    boundary; запись вне Availability Rule — явная override-команда с
>    actor и reason; пересечение с другой Appointment запрещено даже
>    override (политика parallel capacity не введена).
> 9. **Self-service мастера (split):** мастер инициирует availability
>    request в пределах своего tenant assignment; SICK_DAY — немедленный
>    эффективный Block `sick_day` + audit + уведомление admin;
>    vacation/planned leave/recurring change — через approval workflow;
>    свободный редактор расписания — deferred; модель и authorization
>    contracts поддерживают self-service requests уже сейчас.
>    Assignment-level `self_disabled` (AYLA-DEC-0020 п. 5) не
>    ограничивается.
> 10. **Горизонт и шаблон:** горизонт проекции 30 дней
>     (tenant-configurable параметр чтения); MVP-шаблон — день недели ×
>     интервалы; date exceptions выражаются Schedule Block (не deferred);
>     recurring weekly rules версионируются
>     (`effective_from`/`effective_until`): изменение будущего pattern
>     создаёт новую версию и не переписывает историческую; произвольный
>     RRULE — deferred.
>
> **Основание:** CDM §7.10 описывает хранимый per-offering слот, которого
> нет в эксплуатируемом контракте (slots API возвращает вычисленные
> времена, `ai-bot-platform/docs/architecture/ayla-booking-rest-contract.md`,
> строки 68, 106–111) и который не выражает подтверждённые сценарии:
> external_busy без услуги и gate G-CalendarSync (`orch.txt`, строки
> 315–370), offline-записи admin (`orch.txt`, §9 Вариант A), буферы на
> назначении услуги (`stream1.txt`, строка 25; AYLA-DEC-0020 п. 3), hold
> в session flow (`UX-T0.txt`, строки 139–157), time-off и versioned
> weekly rules (master-time-off-handoff), self-service availability
> request (master-mobile-handoff), замещение (master-substitution-handoff),
> подключение YClients при onboarding (salon-onboarding-handoff), UX
> первой записи (customer-first-time-handoff), будущие записи при
> offboarding (master-offboarding-handoff; AYLA-DEC-0017 п. 7). Состав
> `owned_concepts` CAP-010 уже декларирует разделение; владелец
> Availability Slot был `unresolved` (CDM §22, §24). Handoff-источники —
> scenario sources, не канон; их внутренние модели и события в DEC не
> переносятся.
>
> **Затрагивает:** Ayla Core Domain Model Specification (§7.10, §7.12,
> §8.6–8.7, §10–§12, §19, §21–§24 — v1.3); Ayla Domain Event Registry
> (регистрация событий availability по AYLA-DEC-0025); Ayla MVP Scope
> and Release Contract (§4.1 формулировка CAP-010, deferred-перечень);
> зависит от AYLA-DEC-0016, AYLA-DEC-0017, AYLA-DEC-0020. Ayla Domain
> Capability Registry (состав CAP-010), AMD-020 и Consent Scope Registry
> не изменяются.

## Change Log

- **v0.1 — 2026-07-28** — первичная версия брифа (17 разделов,
  рекомендация: вариант B — правила + проекция). Открытые вопросы Q1–Q8.
- **v0.2 — 2026-07-28** — owner ruling applied: (1) ключ слота
  `(specialist_offering_assignment_id, starts_at)` по DEC-0020, без
  `slot_id` UUID, подписанный projection token — не SoR; (2) SoR-таблица
  расширена: Availability Calendar, внешняя запись YClients — внешняя
  система, локальная проекция external busy с полями `source`,
  `external_ref`, `source_updated_at`, `observed_at`, `sync_status` и
  идемпотентным upsert; (3) критическая поправка конкурентного
  бронирования: exclusion constraint по tstzrange ЛИБО единый Time
  Reservation ledger + общая locking boundary, обычный UNIQUE INDEX
  признан недостаточным; транзакция ConfirmAppointment из 6 шагов;
  (4) timezone — свойство календаря доступности (IANA, local wall time),
  в MVP от `Tenant.default_timezone`, snapshot timezone на Appointment;
  (5) изменение Rule/Block → немедленный `released` конфликтующих hold с
  `AVAILABILITY_CHANGED` + уведомление booking session; (6) вопрос 6
  разделён: G-CalendarSync усилен (freshness, degraded mode,
  reconciliation, quarantined staff_id, отдельный reason code); offline —
  те же overlap-проверки, override с actor/reason, parallel capacity не
  введена; self-service split (SICK_DAY немедленно, остальное — approval
  workflow); горизонт 30 дней; date exceptions через Block (не deferred);
  versioned weekly rules в MVP; RRULE deferred; (7) provenance обновлён:
  шесть handoff-источников (master-time-off, master-mobile,
  master-substitution, master-offboarding, customer-first-time,
  salon-onboarding) подтверждены владельцем на owner review; сценарии
  S6/S7/S9 переведены из «owner direction» в подтверждённые; события
  переведены на dot-separated конвенцию AYLA-DEC-0025. Q1–Q6, Q8 закрыты;
  Q7 (retention) и Q9 (SLA в integration contract) открыты. Статус:
  готов к записи AYLA-DEC-0021 после показа diff.
