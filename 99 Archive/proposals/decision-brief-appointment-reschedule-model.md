# Decision Brief — Appointment Reschedule Model (AYLA-DEC-0022)

> **Статус:** v0.2.1 — **draft owner rulings received**. Решения владельца
> (2026-07-28) применены к тексту брифа. **Canonical write запрещён до
> завершения reconciliation с Journey v0.3, подтверждающей отсутствие
> противоречий, явный deferral UX-веток reschedule / cancel / late-window /
> substitute / external reschedule и наличие traceability table. Полная
> реализация этих веток внутри MVP Journey v0.3 не требуется** (owner
> ruling 2026-07-28, вариант Б — deferral). Не является решением до записи
> AYLA-DEC-0022 в [[Ayla Decision Log]]. Размещён в `99 Archive/proposals/` —
> validator-exempt (`scripts/validate_knowledge.py`, `IGNORED_PARTS`).
> **Дата:** 2026-07-28 · **Автор:** Domain Architecture (подготовка) ·
> **Целевая запись:** AYLA-DEC-0022 · **Зависит от (принятые):**
> AYLA-DEC-0015 (monetary boundary), AYLA-DEC-0016 (Subject Identity),
> AYLA-DEC-0017 (Tenant/Membership/Roles), AYLA-DEC-0018 (Offering↔
> Specialist, Option C), AYLA-DEC-0020 (Appointment fields:
> `service_offering_id`, `specialist_assignment_id`,
> `specialist_membership_id`, `price_snapshot{amount,currency}`,
> `effective_duration_snapshot`, `offering_title_snapshot`; запрет SoR
> `specialist_id`), AYLA-DEC-0021 (Availability/Slot: Slot — вычисляемая
> проекция, ключ `(specialist_offering_assignment_id, starts_at)`; Hold
> `held → confirmed | expired | released`; 6-шаговая транзакция
> ConfirmAppointment с DB-enforced interval protection; availability
> changed → release holds + remediation `needs_resolution`), AYLA-DEC-0025
> (Event Registry: lowercase dot-separated past-tense; `appointment.*` —
> канон, `booking.*` — legacy; один authoritative producer).
> **Смежные:** AYLA-DEC-0023/0024 (memory).
> **Режим брифа:** decision brief, НЕ решение; канон не изменяется этим
> документом.

## 1. Проблема и блокируемые разделы CDM

CDM v1.2.3 ([[Ayla Core Domain Model Specification]]) изображает перенос
записи одной строкой lifecycle и одним инвариантом. Дефекты §7.12
(зафиксированы каноном как открытые вопросы §24, Architecture п. 9 и
п. 12):

1. **`rescheduled` изображён как статус**, но инвариант 6 того же раздела
   («Reschedule сохраняет историю») трактует его как переход с историей.
   Внутреннее противоречие (`handoffs/review-core-dom-spec.md`, строки
   604–642 — вне vault, handoff ≠ канон): «является ли rescheduled статусом
   или действием; создаёт ли reschedule новый Appointment… это не
   устойчивое состояние записи, а переход с сохранением истории».
2. **`recommendation_id` — обычный атрибут** без условности; §20 (правило
   3) уже смягчил зависимость до recommendation-originated; обязательность
   — открытый вопрос §24, Architecture п. 9.
3. **Отсутствует `origin`**: неотличимы запись из AI-рекомендации, прямая
   запись, admin-запись и импортированная. Инвариант CAP-011 «Reschedule
   сохраняет origin» ([[Ayla Domain Capability Registry]]) ссылается на
   несуществующее поле.
4. **`price_snapshot` отсутствует в схеме §7.12**, хотя §8.7 и §13 на него
   ссылаются (частично закрыто AYLA-DEC-0020 — снапшоты приняты; полевая
   форма в CDM v1.3 ещё не внесена).
5. **Импортированные записи не представлены**: нет external ID, provenance
   синхронизации, правила разрешения конфликта.

Блокируемые разделы: CDM §7.12, §8.5/§8.7, §9, §10/§11 (payload-контракты),
§12 (строка Revision SoR), §24 (п. 9, п. 12). Смежно: [[Ayla Intent Model
Specification]] (`RESCHEDULE_APPOINTMENT`: слоты `appointment_ref`,
`new_time_slot` — execution-семантика), CAP-011.

## 2. Реальные сценарии

Источники: handoffs и docs клонов вне vault (handoff ≠ канон); канонические
ссылки даны отдельно. Имена handoff-файлов — по реестру scenario sources.

- **S1. Клиент переносит запись на другое время** (бот DM / Mini App):
  `customer-cancellation-reschedule-spec.md` §5.1–5.2 (клон
  `ai-bot-platform-booking`); `2026-05-18-customer-first-time-handoff.md`
  (ветка reschedule). Канон: intent `RESCHEDULE_APPOINTMENT`.
- **S2. При переносе предлагается другой мастер** (предпочтительный занят;
  альтернатива в том же Offering): `customer-cancellation-reschedule-spec.md`
  §5.2 шаг 3; `2026-05-18-master-mobile-handoff.md`.
- **S3. Мастер заболела / отпуск — массовый каскад re-offer**:
  `customer-cancellation-reschedule-spec.md` §6.1–6.5;
  `2026-05-19-master-time-off-handoff.md`. Смыкается с remediation
  `needs_resolution` (AYLA-DEC-0017 п. 7, AYLA-DEC-0021).
- **S4. Админ вносит и правит offline-записи**: `orch.txt:339`;
  AYLA-DEC-0017 п. 6.
- **S5. YClients-originated записи и sync-конфликты**:
  `2026-05-17-salon-onboarding-handoff.md`; `decisions-log.md` Q-MB11
  (отмена в YC → `cancelled_by=external_system`), Q-MM7 (запрет «тихого»
  дрейфа). Канон: YClients intake/calendar integration —
  [[Ayla Repository Responsibility Matrix]], строки 272–273.
- **S6. Анти-абуз лимитом переносов**: `customer-cancellation-reschedule-
  spec.md` §5.4 (default 3); `decisions-log.md` Q-CR7 (override), Q-CR14
  (cancel-then-rebook).
- **S7. Биллинг при переносе**: `customer-cancellation-reschedule-spec.md`
  §5.5 (строки 484–492) по `attribution-policy.md` Q12-α — перенос не
  создаёт billable. Канон: booking fee 90 ₽ — [[Ayla MVP Scope and Release
  Contract]] §6; AYLA-DEC-0015.
- **S8. Runtime ждёт модель**: rewrite `execute_reschedule` (roadmap D2/D3;
  `ref.txt:104, 234–241`; `block-a/w2.md:42–47`).
- **S9. Событийный контракт допускал обе модели** (`event-contract.md`
  §3.3: «both pathways are valid») — недетерминированность закрывается
  настоящим решением; известный P0-дрейф identity у consumers
  (`unified-system-architecture-audit.md:91`).
- **S10. Напоминания и projection**: re-peg на новое время
  (`event-contract.md` §3.3 consumer contract;
  `handoffs/review-journey-spec.md:587–595`).
- **S11. Оплаченная запись**: клиентская онлайн-оплата вне MVP
  (AYLA-DEC-0015 п. 4); «оплаченная» в MVP = booking fee списан с
  provider. Перенос клиентски-оплаченной записи — handoff-сценарий,
  подтверждён владельцем; документ вне vault.
- **S12. Substitute / отказ от замещения**:
  `2026-05-19-master-substitution-handoff.md` — модель обязана допускать
  отказ клиента от substitute-исполнителя без потери записи.
- **S13. Offboarding мастера**: `2026-05-19-master-offboarding-handoff.md`
  — переназначение будущих записей через remediation (AYLA-DEC-0017 п. 7),
  не через reschedule-модель.

## 3. Варианты модели (краткая история)

- **A — same-ID + version** для всех изменений: стабильная identity, но не
  выражает смену Offering/цены/tenant.
- **B — new-ID + link** для всех изменений (модель старой runtime-спеки):
  чистый аудит, но identity churn и дрейф consumers (S9).
- **C — чистый cancel+create** без причинности: отклонён (нет анти-абуза,
  двойной биллинг, потеря retention-аналитики).
- **Принято владельцем — гибрид**: same-ID только внутри одного и того же
  коммерческого обязательства; всё, что меняет существо обязательства, —
  replacement с причинной связью. Матрица — §4.

## 4. Матрица «тип изменения → операция» (ФИНАЛЬНАЯ, owner ruling)

Условия same-ID (все одновременно): тот же tenant; тот же
`service_offering_id`; неизменные цена и длительность; тот же
payment/consent scope; запись не в terminal state.

| Тип изменения | Операция | Обоснование (ruling) |
|---|---|---|
| Дата/время (`starts_at`), прочие условия same-ID соблюдены | **same-ID**: version + Revision | Базовое направление владельца; стабильные consumers |
| Специалист (новый `specialist_assignment_id` в том же Offering) | **same-ID**: version + Revision — **только при явном согласии клиента** + условия §10 (assignment активен/eligible, цена и длительность неизменны, новая доступность под hold, уведомление обоих исполнителей, earnings/review — фактическому исполнителю) | Принятие клиентом замены мастера — reschedule acceptance, НЕ новый объект Consent |
| Небизнесовые/технические метаданные (комментарий, внутренние заметки) | **same-ID** — только если не меняется итоговая сумма, способ/статус оплаты и доход мастера | Операционная правка, не обязательство |
| Другая услуга / Offering (`service_offering_id`) | **Replacement** — в любом статусе, включая `requested` | §21 инвариант 2; смена существа обязательства |
| **Изменение клиентской цены** | **ВСЕГДА replacement** (включая снижение; компромисс «same-ID с новым snapshot» отклонён) | Цена затрагивает клиентское обязательство, оплату/возврат, доход исполнителя, аудит, snapshot, комиссии |
| Изменение длительности | **Replacement** | `effective_duration_snapshot` — часть обязательства |
| Изменение payment boundary | **Replacement** | AYLA-DEC-0015: денежный контур — отдельное обязательство |
| Требуется новый юридический/медицинский/информационный Consent | **Replacement** | Consent scope — часть обязательства; новый Consent создаётся только при изменении юридического/медицинского/информационного scope |
| Другой tenant / организация | **Запрещено как reschedule**: cancel + новый booking flow, **без cross-tenant lineage** | Tenant boundary (AYLA-DEC-0017) |
| Terminal state (`completed`, `cancelled`, `no_show`, `expired`, `rejected`) | **Запрещено** любое изменение | §3.11 Historical Consistency |

## 5. Сущности и кардинальности

**Appointment** (расширение §7.12 CDM; поля assignment/offering/snapshot —
по AYLA-DEC-0020):

```yaml
appointment_id:
subject_id:
tenant_id:            # иммутабелен
provider_id:
service_offering_id:          # DEC-0020
specialist_assignment_id:     # DEC-0020
specialist_membership_id:     # DEC-0020
origin:               # NEW, enum, NOT NULL
recommendation_id:    # CONDITIONAL: обязателен iff origin = ai_recommendation
price_snapshot:       # {amount, currency} — DEC-0020; изменение => replacement
effective_duration_snapshot:  # DEC-0020
offering_title_snapshot:      # DEC-0020
reschedule_of:        # NEW, nullable → appointment_id (непосредственный предок; только replacement)
root_appointment_id:  # NEW: вычисляемое или сохранённое — корень lineage,
                      # для эффективного поиска цепочки и policy threshold
reschedule_count:     # NEW, наследуется +1 по lineage (успешные переносы)
external_ref:         # NEW, nullable: {system, external_id, source_timestamps, sync_metadata}
status:
scheduled_at:         # starts_at — ключ проекции Slot по DEC-0021
created_at:
confirmed_at:
cancelled_at:
completed_at:
version:              # монотонно, +1 на same-ID reschedule
```

`origin` enum: `ai_recommendation / direct_catalog / provider_created /
admin_created / external_import / campaign / rebooking`. Закрывает §24
Architecture п. 9 и инвариант CAP-011.

**Appointment Revision** (новая сущность; владеет Appointment Aggregate):

```yaml
revision_id:
appointment_id:
version:              # версия записи после изменения
changed_fields:       # [{field, old, new}] — starts_at, specialist_assignment_id,
                      # specialist_membership_id, метаданные
actor:                # user | specialist | admin | owner | system | external_system
reason:
command_id:           # + idempotency_key
created_at:
```

**Reschedule Proposal** (новая сущность — owner ruling; для master re-offer,
substitute-предложений и клиентских/manual запросов на перенос):

```yaml
proposal_id:
appointment_id:            # → Appointment, NOT NULL
proposed_assignment_id:    # nullable (если меняется только время)
proposed_starts_at:
proposed_price_snapshot:   # {amount, currency} — фиксирует неизменность цены;
                           # изменение цены proposal не выражает (=> replacement)
actor:                     # инициатор: user | specialist | admin | owner | system
reason:
expires_at:                # ограниченный TTL
status:                    # pending | accepted | declined | expired | withdrawn
```

Кардинальности: `Appointment 1 — 0..N Reschedule Proposal`; не более одного
`pending` proposal на Appointment в момент времени. `Appointment 1 — 0..N
Appointment Revision`. `Appointment 0..1 — reschedule_of → Appointment`
(непосредственный предок; ациклично; тот же tenant). `rescheduled_to` —
проекция, не хранимое поле. Правила proposal: до принятия исходная
Appointment остаётся `confirmed`, старое время занято, новая Reservation —
ограниченный TTL (hold по AYLA-DEC-0021), `appointment.rescheduled` НЕ
публикуется; pending proposal не меняет Appointment status; принятие —
атомарная reschedule-транзакция (§11); отказ/expiry/withdrawn — исходная
запись неизменна.

## 6. Lifecycle и переходы

Статус `rescheduled` **не вводится** (ни как терминальный, ни как
промежуточный). Reschedule same-ID — не переход статуса, а новая версия.

```text
requested → pending_confirmation → confirmed → completed
    ↘ rejected          ↘ expired       ↘ cancelled / no_show

reschedule (same-ID):   requested → requested · confirmed → confirmed
    (версия + Revision + событие appointment.rescheduled; статус не меняется)
replacement:            старая запись → cancelled (cancellation_reason =
    replaced_by_reschedule); новая запись проходит обычный lifecycle
    с reschedule_of на предка
```

Правила: same-ID reschedule допустим из `requested` и `confirmed` при
соблюдении условий §4; replacement — из `requested`, `pending_confirmation`,
`confirmed` (замена услуги — replacement даже в `requested`); из
терминальных статусов любое изменение запрещено; `no_show` — только из
действующей `confirmed`; `expired` — из `pending_confirmation`. Каждый
переход: actor + reason + событие + idempotency (CDM §9).

## 7. Команды и события (по AYLA-DEC-0025)

Команды (реестр CDM §10 не расширяется новыми типами):

- `RescheduleAppointment` — payload: `appointment_id`,
  `proposed_starts_at` (и/или `proposed_assignment_id`), `reason`,
  `idempotency_key`, `expected_version`. Создаёт Reschedule Proposal там,
  где требуется acceptance (смена мастера, master re-offer, late-window,
  сверх threshold лимита), либо исполняет немедленный same-ID перенос
  (клиент, в пределах прав, время-only).
- Acceptance/отклонение proposal — переходы `Reschedule Proposal.status`
  (`accepted | declined | withdrawn`), исполнение acceptance — атомарной
  транзакцией §11.
- Replacement оркестрируется существующими `CancelAppointment`
  (reason=`replaced_by_reschedule`) + `RequestAppointment`
  (`reschedule_of`, `root_appointment_id`) как одна сага с общим
  `correlation_id`/`causation_id`.

События (имена — lowercase dot-separated past-tense, `appointment.*`;
`booking.*` — legacy-алиасы consumers; единственный authoritative producer —
**CAP-011 Appointment Management**):

- `appointment.rescheduled` — только same-ID reschedule; payload:
  `appointment_id` (unchanged), `old/new starts_at`,
  `old/new specialist_assignment_id`, `actor`, `reason`, `version`.
  Публикуется **после** атомарного подтверждения (никогда на pending
  proposal).
- Replacement — канонические lifecycle-события старой и новой записи:
  `appointment.cancelled` (reason=`replaced_by_reschedule`) +
  `appointment.requested` / `appointment.confirmed` с `reschedule_of`,
  `root_appointment_id` в payload, связка correlation/causation.
- Каскад доступности (DEC-0021) — `availability.changed` → remediation
  `needs_resolution`, не событие записи.
- Отдельный integration event для sync-конфликтов — deferred (§15).

## 8. System of Record

- Appointment, Appointment Revision, Reschedule Proposal — Appointment
  Management (CAP-011); CDM §12 дополняется строками Revision и Proposal
  (Snapshot: NO для обеих — Revision и есть история; Replicated: proposal).
- Calendar mode tenant (§12): в `ayla_primary` SoR — Ayla; в
  `external_primary` SoR внешних записей — внешняя система, Ayla —
  projection с `external_ref` и sync metadata.
- LLM/AI Runtime никогда не SoR и не объявляет перенос без backend result
  (CDM §7.12 инвариант 5, §3.5).

## 9. Tenant boundary

`tenant_id` записи иммутабелен; reschedule никогда не пересекает tenant;
перенос между организациями — только cancel + новый booking flow **без
cross-tenant lineage** (`reschedule_of`/`root_appointment_id` не связывают
записи разных tenant'ов — constraint агрегата). Membership и
`active_tenant` проверяются на каждый запрос (AYLA-DEC-0017 п. 8).
Runtime-разрыв на remediation: emit-сайты cancel/reschedule без
`tenant_id`, нет cross-tenant authz на mutation endpoints
(`handoffs/Alpha.txt:15–25` — вне vault).

## 10. Authorization rules и late-window

| Актор | Scope | Условия |
|---|---|---|
| Клиент (Subject, DEC-0016) | свои записи | same-ID — немедленно (время-only, в пределах правил); смена мастера — через свой acceptance proposal; сверх threshold лимита (§16-резолюция Q7) — owner/admin review; late-window — manual request (ниже) |
| Specialist | только записи своего исполнения | перенос — только как Reschedule Proposal (re-offer); без acceptance клиента Appointment не изменяется |
| Admin | записи своего tenant | аудит обязателен (DEC-0017 п. 6); review late-запросов и сверх-лимитных переносов с actor/reason |
| Owner | записи своего tenant | всё + review/override |
| AI | не актор авторизации | исполняет команду только после backend result (§3.5); правила клиента применяются к AI-инициированным переносам |
| System | expiry, каскады | без автопереноса: remediation `needs_resolution` + proposal/re-offer |

**Смена специалиста (условия same-ID, owner ruling):** тот же tenant и
Offering; новый assignment активен и eligible; цена и длительность
неизменны; новая доступность под hold/reservation; явное согласие клиента
(reschedule acceptance, не новый Consent); Revision со старым и новым
assignment/membership; уведомление обоих исполнителей; earnings/review
относятся к фактическому исполнителю.

**Late-window (owner ruling):** запрос на перенос позднее чем за 1 час до
`starts_at` — **manual reschedule request**: клиент отправляет запрос
(Reschedule Proposal, actor=user), Appointment **не изменяется
автоматически**; решение принимает owner/admin вручную; до решения исходная
запись действующая. Неодобрение + неприход клиента — предмет отдельной
cancel/no-show policy, не reschedule-модели. Порог **1 час — платформенный
product default MVP**; число НЕ зашивается в lifecycle доменной модели;
tenant-настройка — позднее (§15).

## 11. Invariants и concurrency (7-шаговая транзакция)

Инварианты (дополнения к §7.12 CDM):

1. Same-ID reschedule выполняется только при условиях §4 (тот же tenant,
   Offering, цена, длительность, payment/consent scope, не terminal).
2. Идемпотентность по `idempotency_key`: повтор команды возвращает
   исходный результат без новой версии (`ayla-booking-rest-contract.md:153`
   — вне vault; `handoffs/delivery.txt:103`).
3. `version` монотонна; Revision иммутабельна; каждая версия имеет ровно
   одну Revision.
4. `tenant_id`, `subject_id`, `origin` иммутабельны; `reschedule_of`,
   `root_appointment_id` иммутабельны после создания записи.
5. Lineage ацикличен и не пересекает tenant.
6. `price_snapshot`, `effective_duration_snapshot` иммутабельны внутри
   версии; их изменение — только replacement (§4).
7. **Биллинг-инвариант: один фактически completed outcome в reschedule
   lineage → не более одного booking fee.** Billing обязан проверять всю
   lineage (по `root_appointment_id`), игнорировать отменённого предка, не
   начислять за факт replacement, начислять только за эффективную
   completed Appointment, не дублировать при retry.
8. Pending proposal не меняет Appointment и не публикует
   `appointment.rescheduled`.

**Concurrency — 7-шаговая атомарная транзакция reschedule (owner ruling,
изоморфна ConfirmAppointment по DEC-0021):**

1. Создать/заблокировать hold нового интервала (ключ
   `(specialist_offering_assignment_id, new_starts_at)`).
2. Заблокировать текущую Appointment и проверить `expected_version`.
3. Проверить права, deadline, eligibility, customer acceptance (при
   необходимости — accepted proposal).
4. Повторно проверить Rule/Block/external freshness (stale → отказ;
   degraded mode по DEC-0021).
5. Выполнить Revision (same-ID) либо создать replacement-связку.
6. Атомарно подтвердить новую Reservation и освободить старую.
7. Outbox-событие + idempotency result.

При любом отказе — старая запись и старая reservation без изменений.
Лимит переносов — **не доменный инвариант** (см. §16, Q7).

## 12. Импорт YClients — calendar mode (owner ruling)

Отклонено «YClients — универсальный SoR». Вводится **calendar mode tenant**:

- `ayla_primary` — SoR Ayla; внешняя система (если подключена) — зеркало.
- `external_primary` — SoR внешних записей — внешняя система (YClients).
- **Несинхронизированный dual-source запрещён.**

Правила `external_primary` в MVP: перенос выполняется во внешней системе;
Ayla импортирует результат; запись несёт `external_ref` (external_id,
source timestamps, sync metadata); конфликт разрешается в пользу
подтверждённой внешней версии; stale sync → degraded mode (DEC-0021).
**Внешние изменения нормализуются по матрице Ayla (§4):** внешнее
изменение только времени → same-ID Revision с `actor=external_system`;
внешняя смена Offering/цены/длительности/consent/payment boundary →
replacement по тем же правилам. **Запрещено любое внешнее изменение без
разбора записывать как Revision.** Клиент уведомляется по consent (аналог
Q-MB11); «тихий» дрейф запрещён (Q-MM7) — расхождение отображается в Sync
Health.

## 13. Migration impact

- **Канон (CDM v1.3, после reconciliation):** схема §7.12 (+`origin`,
  условный `recommendation_id`, `tenant_id`, `reschedule_of`,
  `root_appointment_id`, `reschedule_count`, `external_ref`; поля DEC-0020);
  сущности Appointment Revision и Reschedule Proposal; lifecycle §7.12 (§6
  настоящего брифа); §8.5/§8.7; §10/§11 payload-контракты; §12 (строки SoR);
  §24 — закрыть Architecture п. 9 и п. 12. Event Registry (DEC-0025) —
  регистрация `appointment.rescheduled` и payload-схем replacement-связки.
  Intent Model — execution-маппинг `appointment_ref → appointment_id`,
  `new_time_slot → proposed_starts_at`.
- **Runtime:** rewrite `execute_reschedule` (S8); consumers
  `appointment.rescheduled` — re-peg reminders/projection (S10); пронос
  `tenant_id` через emit-сайты (Alpha B2/B3); устранение дрейфа
  `booking_id` vs `appointment_id` (S9); миграция старой
  cancellation-reschedule спеки (new-ID-модель) на гибрид §4.
- **Данные:** pre-pilot — backfill не требуется; для pilot-данных `origin`
  по умолчанию `provider_created` с пометкой `backfilled`.
- **Блокер:** canonical write запрещён до завершения reconciliation с
  Journey v0.3, подтверждающей отсутствие противоречий, явный deferral
  UX-веток reschedule / cancel / late-window / substitute / external
  reschedule и наличие traceability table. Полная реализация этих веток
  внутри MVP Journey v0.3 не требуется (owner ruling 2026-07-28).

## 14. Recommendation/Attribution и billing (owner rulings)

**Attribution (ruling — слепое наследование `recommendation_id` убрано):**

- `origin` и provenance записи сохраняются всегда.
- Attribution Link не переписывается задним числом (§3.11; §7.13
  инвариант 4).
- Перенос **той же услуги** (same-ID, включая смену мастера): attribution
  продолжается по lineage без новых Attribution Link.
- Replacement на **другую услугу**: `recommendation_id` наследуется
  **только после проверки**, что новая услуга исполняет ту же
  Recommendation; самостоятельный выбор клиентом другого результата может
  завершать причинную связь (тогда `origin` новой записи — не
  `ai_recommendation`-lineage, attribution не продолжается). Attribution
  eligibility — **явное решение, не слепое копирование UUID**.
- Outcome ссылается на конкретную запись цепочки (§7.15); склейка — через
  `reschedule_of`/`root_appointment_id`.

**Billing (ruling):** reschedule не создаёт charge; replacement Appointment
**может породить charge после собственного завершения**. Инвариант §11.7:
один фактически completed outcome в lineage → не более одного booking fee.
Billing: проверять всю lineage по `root_appointment_id`; игнорировать
отменённого предка; не начислять за факт replacement; начислять только за
эффективную completed Appointment; не дублировать при retry. Клиентская
онлайн-оплата вне MVP (DEC-0015 п. 4) — перенос клиентских денег deferred.

## 15. Отложенные возможности (deferred)

- Перенос/возврат клиентской онлайн-оплаты (CAP-023, отдельное решение).
- Tenant-конфигурируемые политики переносов: late-порог, threshold лимита,
  редактор политик салона.
- Отдельный integration event для sync-конфликтов внешних записей.
- Substitute workflow (DEC-0017 п. 9; S12 — только требование допускать
  отказ без потери записи).
- Автоматический перенос без участия клиента; cross-sell/upsell при
  переносе — **запрещён**, не deferred (`customer-cancellation-reschedule-
  spec.md` §5.2 Forbidden — вне vault).
- Reschedule-аналитика (late-rate, abuse insights).

## 16. Открытые вопросы — закрыты owner rulings (2026-07-28)

- **Q1 (гибрид same-ID/replacement)** — **ПРИНЯТ** с уточнениями: условия
  same-ID формализованы (§4); изменение клиентской цены — всегда
  replacement; замена услуги — replacement даже в `requested`.
- **Q2 (дедлайн self-service)** — **РАЗРЕШЁН иначе**: late-window < 1 часа —
  не автоматический late cancel, а manual reschedule request с решением
  owner/admin (§10); 1 час — product default MVP, не зашивается в доменный
  lifecycle; tenant-настройка deferred.
- **Q3 (смена специалиста)** — **same-ID** при явном согласии клиента и
  условиях §10 (assignment eligible, цена/длительность неизменны, hold,
  Revision, уведомления, earnings/review фактическому исполнителю);
  введена сущность Reschedule Proposal.
- **Q4 (правка Offering в `requested`)** — **ЗАПРЕЩЕНА**: замена услуги —
  replacement в любом статусе.
- **Q5 (YClients SoR)** — **ПЕРЕФОРМУЛИРОВАН И РАЗРЕШЁН**: универсальный
  YClients-SoR отклонён; модель calendar mode tenant (`ayla_primary` /
  `external_primary`; dual-source запрещён); внешние изменения
  нормализуются по матрице §4 (§12).
- **Q6 (статус старой записи при replacement)** — **`cancelled` +
  `cancellation_reason = replaced_by_reschedule`**; статус `rescheduled`
  не вводится нигде; добавлен `root_appointment_id`.
- **Q7 (лимит переносов)** — **НЕ доменный инвариант**: `reschedule_count`
  хранится по lineage; платформа поддерживает policy threshold; MVP
  default — 3 успешных self-service reschedule на lineage; далее —
  owner/admin review (без блокировки/отмены записи) с actor/reason;
  tenant override — позднее.

Новых открытых вопросов rulings не породили; остаётся блокер верхнего
уровня — **reconciliation с Journey v0.3** (ветки reschedule/cancel,
master re-offer, late-window, substitute-отказ, YClients-сценарии) до
canonical write.

## 17. Предлагаемая формулировка owner ruling (AYLA-DEC-0022, DRAFT до Journey-reconciliation)

> **AYLA-DEC-0022 — Appointment Reschedule and Replacement Model**
>
> 1. Reschedule — не статус, а версионируемая операция. Same-ID
>    (сохранение `appointment_id`, монотонная `version`, иммутабельная
>    Appointment Revision на каждое изменение) допустим только при: тот же
>    tenant; тот же `service_offering_id`; неизменные цена и длительность;
>    тот же payment/consent scope; не terminal state. Статус `rescheduled`
>    не вводится.
> 2. Матрица операций — по §4 брифа (финальная): дата/время → same-ID;
>    специалист в том же Offering при неизменной цене/длительности и явном
>    согласии клиента → same-ID (принятие замены мастера — reschedule
>    acceptance, не новый Consent); небизнесовые метаданные → same-ID при
>    неизменных сумме, способе/статусе оплаты и доходе мастера; другая
>    услуга/Offering, изменение клиентской цены (всегда, включая снижение),
>    изменение длительности, изменение payment boundary, новый
>    юридический/медицинский/информационный Consent → replacement (в любом
>    статусе, включая `requested`); другой tenant → cancel + новый booking
>    flow без cross-tenant lineage; terminal state → запрещено.
> 3. Replacement: старая запись → `cancelled` с
>    `cancellation_reason=replaced_by_reschedule`; новая запись несёт
>    `reschedule_of` (непосредственный предок, ациклично, тот же tenant),
>    `root_appointment_id`, `reschedule_count` (наследуется +1).
> 4. Новая сущность Reschedule Proposal (appointment_id,
>    proposed_assignment_id, proposed_starts_at, proposed_price_snapshot,
>    actor, reason, expires_at; status: pending | accepted | declined |
>    expired | withdrawn): обязательна для смены мастера, master re-offer,
>    substitute-предложений, late-window и сверх-лимитных запросов. До
>    принятия исходная запись действующая, старое время занято, новая
>    Reservation с ограниченным TTL, `appointment.rescheduled` не
>    публикуется; принятие — атомарная 7-шаговая транзакция (§11); отказ/
>    expiry — исходная неизменна.
> 5. Late-window: запрос позднее чем за 1 час до starts_at — manual
>    reschedule request (proposal, решение owner/admin вручную, исходная
>    запись действующая до решения); порог — product default MVP, не
>    доменный инвариант.
> 6. Лимит переносов — policy, не инвариант: MVP default 3 успешных
>    self-service reschedule на lineage; далее — owner/admin review с
>    actor/reason; запись не блокируется и не отменяется; tenant override —
>    deferred.
> 7. Attribution: origin/provenance сохраняются; Attribution Link не
>    переписывается; при переносе той же услуги attribution продолжается
>    по lineage; при другой услуге `recommendation_id` наследуется только
>    после проверки исполнения той же Recommendation; attribution
>    eligibility — явное решение. Billing: reschedule не создаёт charge;
>    replacement может породить charge после собственного завершения; один
>    completed outcome в lineage → не более одного booking fee; billing
>    проверяет lineage по `root_appointment_id`.
> 8. Calendar mode tenant: `ayla_primary` | `external_primary`;
>    несинхронизированный dual-source запрещён. В `external_primary` (MVP):
>    перенос — во внешней системе; Ayla импортирует результат с
>    `external_ref` (external_id, source timestamps, sync metadata);
>    конфликт — в пользу подтверждённой внешней версии; stale → degraded
>    mode (DEC-0021); внешние изменения нормализуются по матрице §4
>    (время-only → same-ID Revision с actor=external_system; Offering/цена/
>    длительность/consent/payment → replacement); запись внешних изменений
>    как Revision без разбора запрещена.
> 9. События по DEC-0025: same-ID → `appointment.rescheduled`;
>    replacement → канонические lifecycle-события старой и новой записи;
>    `booking.*` — legacy; единственный producer — CAP-011. `no_show` —
>    только из действующей `confirmed`.
> 10. Concurrency: 7-шаговая транзакция (§11) с hold по DEC-0021,
>     `expected_version`, повторной проверкой Rule/Block/external freshness;
>     при любом отказе старая запись и reservation без изменений.
> 11. CDM v1.3: правки §7.12 (поля п. 3 + `origin` enum 7 значений +
>     условный `recommendation_id`), сущности Appointment Revision и
>     Reschedule Proposal, lifecycle §6 брифа, §12 SoR-строки; §24
>     Architecture п. 9 и п. 12 закрываются. Canonical write — после
>     reconciliation с Journey v0.3.
>
> **Зависит от:** AYLA-DEC-0015, -0016, -0017, -0018, -0020, -0021, -0025.
> **Затрагивает:** CDM (v1.3), Event Registry, Ayla Intent Model
> Specification (execution-маппинг), Ayla Domain Capability Registry
> (CAP-011), контур биллинга DEC-0015 (lineage check), runtime booking
> rewrite. Decision brief:
> `99 Archive/proposals/decision-brief-appointment-reschedule-model.md`.

## Change Log

| Версия | Дата | Изменение |
|---|---|---|
| 0.1 | 2026-07-28 | Первоначальный бриф (целевая запись AYLA-DEC-0020) |
| 0.2.1 | 2026-07-28 | Owner ruling (вариант Б — deferral): блокер canonical write переформулирован — reconciliation = проверка отсутствия противоречий + явный deferral UX-веток reschedule/cancel/late-window/substitute/external reschedule в Journey v0.3 + traceability table; полная реализация веток в Journey не требуется |
| 0.2 | 2026-07-28 | Применены draft owner rulings: финальная матрица §4 (цена — всегда replacement; замена услуги — replacement в любом статусе; условия same-ID формализованы); Reschedule Proposal (новая сущность); late-window как manual request (1 ч — product default, не инвариант); лимит переносов — policy threshold, не инвариант; YClients — calendar mode вместо универсального SoR; старая запись — `cancelled`+reason, статус `rescheduled` упразднён; `root_appointment_id`; attribution — без слепого наследования `recommendation_id`; billing-инвариант «один completed outcome → не более одного fee»; 7-шаговая транзакция; события по DEC-0025; полевая модель приведена к DEC-0020/0021; Q1–Q7 закрыты резолюциями; §17 переписан; целевая запись перенумерована в AYLA-DEC-0022. Статус: canonical write и accepted запрещены до reconciliation с Journey v0.3 |
