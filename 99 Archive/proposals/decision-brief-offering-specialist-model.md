# Decision Brief — Service Offering ownership and Specialist assignment (AYLA-DEC-0020)

> **Статус:** решение зарегистрировано как AYLA-DEC-0020 (финальная сверка
> владельца 2026-07-28 применена, v0.4). Документ — архивный артефакт
> подготовки решения; нормативным источником является запись AYLA-DEC-0020
> в [[Ayla Decision Log]]. Размещён в `99 Archive/proposals/` —
> validator-exempt.
> **Дата:** 2026-07-28 · **Версия:** v0.4 · **Автор:** Domain Architecture
> (подготовка) · **Запись:** AYLA-DEC-0020 ·
> **Зависит от:** AYLA-DEC-0016 (Subject Identity Model), AYLA-DEC-0017
> (Tenant, Membership and Role Model) · **Связано:** AYLA-DEC-0015 (MVP
> Monetary Boundary), planned AYLA-DEC-0021 (slot calculation —
> forward-ссылка; пустые записи-заглушки не создаются)

## 1. Проблема и блокируемые разделы CDM

CDM v1.2.3 моделирует Service Offering (§7.9) как единую сущность с полями
`provider_id` **и** `specialist_id` одновременно: прайс организации и
связь с конкретным мастером сшиты в одну строку. Это создаёт четыре
нерешённые проблемы:

1. **System of Record не определён.** §12 фиксирует Offering как
   `Provider/Catalog boundary` — это описание спорной границы, а не bounded
   context; у состояния не может быть два владельца
   (`handoffs/review-core-dom-spec.md`, CDM-8). §22 и §23 помечают строку
   `unresolved`; §24 (Architecture, п. 1 и п. 11) требует owner decision к
   CDM v1.3.
2. **Модель устарела относительно AYLA-DEC-0017.** DEC-0017 п. 4 отменил
   прямую привязку `Specialist.provider_id`: Specialist Profile
   существует независимо от Provider, связь с tenant — только через
   Provider Membership. Offering, написанный до этого решения, жёстко
   сшивает мастера и салон и не выражает мастера в нескольких салонах.
3. **Невыразимы реальные коммерческие факты.** Один и тот же Service в
   одной организации оказывается разными мастерами с разной ценой и
   длительностью; услугу нужно отключать точечно (у мастера) и глобально
   (у организации). Модель «одна строка Offering = provider + specialist»
   выражает это только дублированием записей.
4. **Lifecycle, commands и events для Offering не определены** (CDM §24,
   Architecture п. 6; CDM-AC-04) — Roadmap §4.3 требует state/lifecycle/
   commands/events для каждой MVP-модели, включая Service Offering.

Блокируемые разделы CDM: §7.9 (определение), §7.10 (Availability Slot
ссылается на `offering_id` + `specialist_id`), §12 (строка Service
Offering), §19 (ERD), §22/§23 (ownership/mapping), §24 (Architecture
п. 1, 6, 11), §18 (CDM-AC-01, CDM-AC-04, CDM-AC-05).

## 2. Реальные сценарии

Подтверждённые документами (точные ссылки):

- **S1. У мастера своя цена и длительность на услугу.** Runtime Ayla уже
  хранит услугу per-specialist: `Service.specialist FK`, собственные
  `price`, `duration_minutes`, `is_active`, `buffer_after_minutes`
  (`Ayla/djangoproject/services/models.py:215–303`). Канон отстаёт от
  эксплуатации.
- **S2. Канонический каталог с рамками длительности.** `ServiceTemplate`
  (category, name, `duration_default/min/max`, `is_popular`) и
  `RegionalPricing` (`price_min/price_max`) существуют отдельно от услуги
  мастера и **не связаны** с ней FK
  (`Ayla/djangoproject/services/models.py:77–213`;
  `Ayla/djangoproject/docs/CANONICAL_CATALOG_SEED_PLAN_2026-07.md`, §2).
- **S3. Goal-based и price-aware подбор через связь мастер↔услуга.**
  «MasterServiceOffering (master↔service связь) — значит можно джойнить
  мастер → услуги → цели/цена и делать goal-based и price-aware поиск
  cross-tenant» (`handoffs/PersonalContext.txt`, строки 9, 54–56).
- **S4. Точечное отключение услуги.** `is_active` живёт на услуге мастера
  (models.py:251); API отдаёт «услуги специалиста» и фильтр специалистов
  по `service_id` (`ai-bot-platform-booking/docs/architecture/
  ayla-booking-rest-contract.md`, §3.1).
- **S5. Импорт из YClients.** Мастера синхронизируются из YClients:
  `SpecialistProfile.booking_source = ayla_local | yclients`,
  `yclients_staff_id` (`Ayla/djangoproject/users/models.py:183–199`;
  `Ayla/djangoproject/docs/BOT_CODE_AUDIT_2026-04.md`, §1.7 — «Master
  (sync from YClients) → Ayla SpecialistProfile»). Полные сущности
  `SalonService` / `YClientsMapping` осознанно отложены
  (`CANONICAL_CATALOG_SEED_PLAN_2026-07.md`, §8).
- **S6. Offboarding не удаляет Offering.** Revoke Membership терминален и
  не удаляющий: «Membership, история Appointment, Offering и Specialist
  Profile сохраняются» (AYLA-DEC-0017, п. 7).

Подтверждены владельцем как owner direction (документ вне vault):

- **S7. Прайс принадлежит организации, мастер — переопределение.** *(owner
  direction 2026-07-28; handoff-сценарий, подтверждён владельцем; документ
  вне vault)*. Service Offering принадлежит организации; цена,
  длительность, доступность и локальное отключение переопределяются на
  уровне связи мастер↔offering.
- **S8. Импорт прайса организации из YClients как onboarding-поток.**
  *(handoff-сценарий, подтверждён владельцем; документ вне vault;
  косвенно подтверждён S5 и эпиком #200 в seed-плане §1)*.

## 3. Варианты модели

- **V1 — Organization-level Offering + Specialist Offering Assignment
  (owner direction, подтверждён ruling).** Трёхуровневая коммерческая
  модель с разрешением исполнителя через Membership → Profile:
  Catalog Service (смысловая услуга «что это вообще») → Service Offering
  (коммерческое предложение организации) → Specialist Offering Assignment
  → Specialist Membership (НЕ глобальный профиль) → Specialist Profile.
  Assignment несёт override-поля (цена, длительность, доступность,
  локальное отключение). Плюсы: нет дублирования; салонное изменение цены —
  одна запись; естественный маппинг импорта YClients (прайс организации +
  staff-ссылки); согласовано с DEC-0017. Минусы: +1 сущность, +1 join в
  подборе и слотах — приняты владельцем.
- **V2 — Per-specialist Offering (runtime status quo).** Каждый мастер
  владеет собственными Offering (как `Service` в runtime, S1). Плюсы:
  технически проще, соответствует существующему коду и API (S4). Минусы:
  дублирование одной услуги организации по каждому мастеру; изменение
  прайса — fan-out по дублям с риском рассинхрона; нет понятия «прайс
  организации» (ломает S7); импорт YClients (organization-level) требует
  размножения записей. **Отклонён владельцем.**
- **V3 — Текущий CDM (offering с `provider_id` + `specialist_id`, без
  assignment).** Наследует дублирование V2 и жёсткую связку мастер↔
  организация, отменённую DEC-0017; не выражает мастера в двух
  организациях с одним профилем. **Отклонён.**

Ключевое уточнение ruling к V1: модель `assignment.specialist_id`
**запрещена** — Assignment ссылается на `specialist_membership_id`
(Specialist Membership по DEC-0017), а не на глобальный Specialist
Profile напрямую. Это делает невозможным assignment мастера, не имеющего
active membership в организации, на структурном уровне, а не на уровне
проверки.

## 4. Рекомендуемый вариант

**V1 — подтверждён owner ruling 2026-07-28, уточнён финальной сверкой**
со следующими нормативными положениями:

- Соло-мастер — не отдельный контур, а организация с одним active
  membership (наследует DEC-0017 п. 10); единая архитектура для соло и
  салона.
- Соло-инвариант (сужен финальной сверкой): **активация** Offering
  соло-организации невозможна без active Assignment на единственный
  eligible Specialist Membership; draft Offering без assignment
  допустим; create+activate — одна атомарная транзакция. Асинхронное
  создание assignment при активации запрещено — промежуточное состояние
  «услуга есть, записаться нельзя» недопустимо. Для организации с
  несколькими мастерами авто-assignment всем membership НЕ выполняется —
  назначение выбирает owner.
- Assignment ≠ доказательство квалификации: отдельные поля
  `qualification_status` и `qualification_evidence_ref` (см. §5), для
  обычных услуг в MVP необязательны.

## 5. Сущности и кардинальности

Цепочка: Catalog Service 1—0..N Service Offering 1—0..N Specialist
Offering Assignment N—1 Specialist Membership N—1 Specialist Profile.

```yaml
service_offering:            # переработанный CDM §7.9
  offering_id:
  service_id:                # → канонический Catalog Service (CAP-008)
  provider_id:               # Provider — владелец прайса; specialist_id УДАЛЯЕТСЯ
  tenant_id:                 # граница изоляции/доступа (НЕ владелец), DEC-0017 п. 2
  offering_title:            # отображаемое название (snapshot-источник)
  base_price:
  currency:
  base_duration_minutes:
  is_active:
  booking_enabled:           # организационное отключение записи без архивации
  status:                    # draft / active / paused / archived
  eligibility_rules:         # не ослабляют глобальные safety rules (§7.9 инв. 5)
  created_at: / updated_at:

specialist_offering_assignment:   # новая сущность
  assignment_id:
  offering_id:                     # → Service Offering
  specialist_membership_id:        # → Specialist Membership (НЕ specialist_id)
  price_override:                  # nullable; null = base_price
  duration_override_minutes:       # nullable; null = base_duration
  booking_enabled:                 # локальное отключение (S4, S7)
  status:      # pending / active / self_disabled / organization_disabled /
               # suspended / archived
  qualification_status:            # not_required / unverified / verified / expired
  qualification_evidence_ref:      # nullable; ≠ доказательство через assignment
  created_at: / updated_at:
```

Effective values (нормативные формулы ruling, редакция финальной сверки):

```text
effective_price    = price_override ?? base_price
effective_duration = duration_override_minutes ?? base_duration_minutes
booking_allowed    = offering.is_active
                 AND offering.booking_enabled
                 AND assignment.status = active
                 AND assignment.booking_enabled
                 AND membership active
                 AND availability decision = available
                     -- определяется отдельным контрактом (planned AYLA-DEC-0021)
                 AND qualification/safety requirements satisfied
```

`booking_allowed` — результат domain policy evaluation, а не поле
Assignment. Политика квалификации: `booking_allowed` требует
`qualification_status = verified`, если применимая policy требует
подтверждения квалификации. Effective values вычисляются, не хранятся как
SoR. Слот рассчитывается от `effective_duration` конкретного assignment
(детальный алгоритм слотов — planned AYLA-DEC-0021, вне scope этого
решения). Уникальность пары `(offering_id, specialist_membership_id)`
среди не-archived Assignment.

Каталожная проекция (ruling п. 12): клиент видит offering один раз —
«от 1500 ₽», «60–90 минут», N специалистов; «от X» = min effective_price
по active assignments. Это **derived projection, не SoR**.

## 6. Lifecycle и переходы

Offering: `draft → active ⇄ paused → archived`.

Assignment — явный перечень допустимых переходов (финальная сверка):

```text
pending               → {active, archived}
active                → {self_disabled, organization_disabled, suspended, archived}
self_disabled         → {active, organization_disabled, suspended, archived}
organization_disabled → {active, suspended, archived}
suspended             → {active, archived}
archived              → {}  (терминален)
```

Нормативное различие состояний: `organization_disabled` — коммерческое
решение организации; `suspended` — принудительное ограничение
(compliance / qualification / safety / platform enforcement).

Нормативные правила (ruling п. 10):

- `offering paused` → новые записи запрещены, assignments сохраняются в
  текущем состоянии.
- `membership terminated` (revoke по DEC-0017 п. 7) → assignments
  становятся not bookable, но **сохраняются для истории**, не удаляются
  и не архивируются принудительно.
- `archived` терминален и не удаляющий; Assignment с существующими
  записями (Appointment) не удаляется никогда.
- `self_disabled` устанавливает сам specialist (см. §10); возврат в
  `active` — owner/admin, для safety-sensitive услуг — только с
  подтверждением специалиста.
- Общие правила CDM §9: actor, reason, event, idempotency, audit trail.

## 7. Команды и события

Administrative commands (новые, группа Administrative по CDM §10):
`CreateOffering` (для соло create+activate — атомарно с
`AssignOfferingToMembership`), `UpdateOfferingTerms`, `PauseOffering`,
`ResumeOffering`, `ArchiveOffering`, `AssignOfferingToMembership`,
`UpdateAssignmentOverrides`, `SelfDisableAssignment`,
`EnableAssignment` (owner/admin; для safety-sensitive — с подтверждением
специалиста), `OrganizationDisableAssignment`, `SuspendAssignment`,
`ArchiveAssignment`, `DelegateAssignmentPermission`.

Business events (CDM §11): `OfferingCreated`, `OfferingTermsUpdated`,
`OfferingPaused`, `OfferingResumed`, `OfferingArchived`,
`SpecialistOfferingAssigned`, `AssignmentOverridesUpdated`,
`AssignmentSelfDisabled`, `AssignmentEnabled`,
`AssignmentOrganizationDisabled`, `AssignmentSuspended`,
`AssignmentArchived`, `AssignmentPermissionDelegated`. Все — с
actor/reason, tenant-scoped, PII-free payload (коммерческие данные, не
персональные).

## 8. System of Record

Service Offering и Specialist Offering Assignment → **Provider Management
(CAP-009)** владеет business truth; Identity and Access (CAP-019) владеет
только enforcement доступа (наследует DEC-0017 п. 11). Service Catalog
(CAP-008) владеет каноническим Catalog Service и может индексировать
Offering, но не владеть им (review-core-dom-spec, CDM-8; инвариант
CAP-008 «Provider offering не равна canonical service» уже нормативен).
Каталожная проекция «от X ₽» (§5) — derived, не SoR. `specialist_id` в
Appointment — не SoR-атрибут (см. §14). Закрывает CDM §24, Architecture
п. 1 и п. 11; строка §12 `Provider/Catalog boundary` заменяется на
конкретного владельца.

## 9. Tenant boundary

Service Offering принадлежит **Provider**; Offering несёт `tenant_id` как
границу изоляции/доступа, но Tenant не владелец прайса — понятия не
взаимозаменяемы (AYLA-DEC-0017 п. 2; MVP: Provider 1:1 Tenant). Все
reads/writes scoped по tenant. Assignment структурно привязан к tenant
через `specialist_membership_id`: Membership по DEC-0017 всегда
принадлежит одному tenant, поэтому cross-tenant assignment невыразим.
Offering, Assignment и Membership, участвующие в одном Appointment,
обязаны принадлежать одному tenant (инвариант цепочки, §14). Cross-tenant
чтение прайсов запрещено; marketplace-выдача фильтрует tenant-first
(соответствует runtime-индексу `svc_tenant_active_idx`,
models.py:296–299). Кросс-тенантный goal-based поиск (S3) работает по
агрегированной read-проекции, не по чужим строкам SoR.

## 10. Authorization rules

**Offering price — это Commerce/Catalog Management, не Platform Billing**
(ruling п. 6). Platform Billing — тариф подписки, комиссия Ayla,
реквизиты (контур AYLA-DEC-0015). Этим разделением разрешается коллизия
с DEC-0017 п. 6 (запрет admin на billing/legal settings): смысл DEC-0017
не меняется, запрет на Platform Billing сохраняется в полном объёме.

Permission-набор (минимальный, полный permission-каталог — Non-goal):

```text
offering.manage_base_price
offering_assignment.manage_own_availability
offering_assignment.manage_own_price_override
offering_assignment.manage_any
```

Матрица (ruling п. 6):

| Роль | Platform Billing | Pricing (offering) |
|---|---|---|
| Owner | да | да |
| Admin | нет (DEC-0017 п. 6) | по permission policy организации |
| Specialist | нет | own price_override — только по делегированному permission |

Права specialist (ruling п. 5): может управлять **собственной**
доступностью (`active → self_disabled`; возврат — owner/admin, для
safety-sensitive услуг — только с подтверждением специалиста).
`base_price` — запрещено. Own `price_override` — только при наличии
делегированного `offering_assignment.manage_own_price_override`.
Делегирование фиксируется с actor/reason и аудируется (CAP-026).
Platform operator — только по процедуре DEC-0017 п. 5.

## 11. Invariants

1. Offering всегда ссылается на существующий канонический Catalog Service
   (CDM §21, инв. 3 сохраняется).
2. Assignment ссылается на `specialist_membership_id`; модель
   `assignment.specialist_id` запрещена.
3. `booking_allowed` — результат domain policy evaluation по формуле §5;
   ни один путь записи не обходит её; `booking_allowed` требует
   `qualification_status = verified`, если применимая policy требует
   подтверждения квалификации.
4. Offering в статусе `paused`/`archived` не принимает новые записи;
   assignments при этом сохраняются.
5. Terminated Membership делает assignments not bookable, не удаляя их
   (S6, DEC-0017 п. 7).
6. Пара `(offering_id, specialist_membership_id)` уникальна среди
   не-archived Assignment.
7. Override не ослабляет глобальные safety rules и eligibility_rules
   Offering (CDM §7.9, инв. 5); возврат из `self_disabled` для
   safety-sensitive услуг требует подтверждения специалиста.
8. Соло-инвариант: активация Offering соло-организации невозможна без
   active Assignment на единственный eligible Specialist Membership;
   draft Offering без assignment допустим; create+activate — атомарная
   транзакция.
9. Импорт создаёт 1 Offering + N Assignments, не N Offerings.
10. Исторический Appointment не изменяется при изменении цены/
    длительности/title — действуют snapshots (§14).
11. Цена (base и override) > 0; валюта едина внутри Offering.
12. Assignment не является доказательством квалификации.
13. Цепочка ссылок Appointment согласована: `service_offering_id` и
    `specialist_membership_id` обязаны совпадать с Offering и Membership,
    на которые ссылается `specialist_assignment_id`; все три сущности —
    один tenant. `specialist_id` не является SoR-атрибутом Appointment и
    не участвует в инвариантах и write commands.
14. LLM не создаёт и не изменяет Offering/Assignment (CDM §21, инв. 7).

## 12. Последствия для импорта из YClients

**MVP (ruling п. 8): guided/manual import** — с валидацией, dry-run,
отчётом о дублях и обязательным подтверждением owner. Полная
авто-синхронизация — deferred.

Модель import-ready (нормативно):

```yaml
external_mapping:
  provider:
  external_entity_type:    # service / staff / ...
  external_id:
  internal_entity_type:    # offering / membership / ...
  internal_id:
```

Плюс правила дедупликации и idempotency key на операцию импорта. Маппинг:
прайс YClients → 1 Offering (дедупликация по минимальным ключам §13),
привязка staff (`yclients_staff_id`, users/models.py:195) → Assignments.
Импорт создаёт **1 Offering + N Assignments, не N Offerings** (инв. 9).
JSON Schema формата импорта — Non-goal этого решения.

## 13. Migration impact

- **CDM v1.3:** переработка §7.9 (удаление `specialist_id`, добавление
  `tenant_id`, `base_*`, `booking_enabled`, lifecycle); новый раздел для
  Specialist Offering Assignment (ссылка на `specialist_membership_id`);
  §7.12 — контракт Appointment по §14 (удаление `specialist_id` как
  SoR-атрибута, snapshots с суффиксом `_snapshot`); точечные правки §7.10
  (слот от effective_duration — детали к planned AYLA-DEC-0021), §12,
  §19, §20, §22, §23; закрытие §24 Architecture п. 1, 11 и частично п. 6.
- **Scope Contract:** §4.1 CAP-009 — ограничение MVP уточняется:
  «минимальный профиль провайдера + offering/assignment management +
  guided YClients import»; полная авто-синхронизация YClients — в §5
  Deferred.
- **Capability Registry:** CAP-009 `owned_concepts` дополняется
  `Specialist Offering Assignment` и `External Mapping`; CAP-008 без
  изменений.
- **Runtime-миграция per-master → целевая модель (ruling п. 9):**
  процедура `candidate grouping → confidence → preview → owner
  confirmation → commit`. **Запрещено объединение только по названию.**
  Минимальные ключи группировки: organization, canonical service,
  branch/location, service variant, currency. Немедленного рефакторинга
  runtime решение не требует (по образцу DEC-0016 п. 9).

## 14. Влияние на Appointment, Recommendation и billing

- **Appointment contract (ruling п. 4, редакция финальной сверки):**
  ссылки `service_offering_id` + `specialist_assignment_id` +
  `specialist_membership_id`; snapshots с обязательным суффиксом
  `_snapshot`: `effective_price_snapshot`, `effective_duration_snapshot`,
  `offering_title_snapshot`; цена — value object
  `price_snapshot {amount, currency}`. Историческая запись не изменяется
  при изменении цены (CDM §3.11, §13 — historical integrity snapshot).
- **`specialist_id` в Appointment запрещён как SoR-атрибут:** исполнитель
  определяется через `specialist_membership_id`; профиль — через
  Membership → Profile. Denormalized `specialist_id` допустим только в
  read models / search / analytics как derived-проекция — не в write
  commands и не в инвариантах.
- **Инвариант цепочки:** `service_offering_id` и
  `specialist_membership_id` в Appointment обязаны совпадать с Offering и
  Membership, на которые ссылается `specialist_assignment_id`; все три
  сущности — один tenant.
- **Recommendation:** кандидат — пара (Offering, Assignment) с
  `booking_allowed = true` (domain policy evaluation, §5); price-aware
  ranking (S3) использует effective_price; каталожная выдача
  дедуплицирует offering («от X ₽», N специалистов — derived
  projection, §5).
- **Billing (AYLA-DEC-0015):** offering price относится к Commerce/
  Catalog, не к Platform Billing; booking fee 90 ₽ и подписка не зависят
  от цены услуги; клиентская онлайн-оплата вне MVP (Scope Contract §5.1).
  Provider eligibility (CAP-022) проверяется на `offering.provider_id` до
  подтверждения (CDM §7.12, инв. 9) — gate не меняется.

## 15. Отложенные возможности и Non-goals

**Non-goals AYLA-DEC-0020 (явно, по ruling п. 14):** алгоритм слотов и
расчёт доступности (→ planned AYLA-DEC-0021); наложение расписаний;
room/equipment; пакеты услуг; акции/скидки; JSON Schema формата импорта;
полный permission-каталог.

**Deferred (активация через change control Scope Contract §11):** полная
авто-синхронизация YClients; `SalonService`/`YClientsMapping` как
полноценные сущности (полный #200); `RegionalPricing`; aftercare-контент
per service; substitute-scoped Assignment (наследует substitute workflow
DEC-0017 п. 9); комиссии/fee per offering; cross-tenant агрегация
«любимых мастеров» (post-pilot, `PersonalContext.txt`, развилка).

## 16. Открытые вопросы — статус после ruling и финальной сверки

- **Q1. Нумерация DEC — ЗАКРЫТ:** решение зарегистрировано как
  AYLA-DEC-0020.
- **Q2. Вариант модели — ЗАКРЫТ:** V1 с assignment на
  `specialist_membership_id` (ruling п. 1).
- **Q3. Авто-assignment соло — ЗАКРЫТ:** активация Offering невозможна
  без active Assignment на единственный eligible Specialist Membership;
  draft без assignment допустим; create+activate атомарны; для салона
  авто-assignment не выполняется (ruling п. 7, финальная сверка).
- **Q4. Ссылка слота — ЗАКРЫТ:** слот считается от effective_duration
  конкретного assignment; availability decision — отдельный контракт
  (planned AYLA-DEC-0021).
- **Q5. Права specialist — ЗАКРЫТ:** own availability да; base_price нет;
  own override по делегированию (ruling п. 5).
- **Q6. Цена vs billing — ЗАКРЫТ:** pricing = Commerce/Catalog, не
  Platform Billing; матрица Owner/Admin/Specialist (ruling п. 6).
- **Q7. YClients в MVP — ЗАКРЫТ:** guided/manual import; авто-синк
  deferred (ruling п. 8).
- **Q8. Effective price — ЗАКРЫТ:** вычислимый по формуле; SoR —
  base + override; «от X» — derived projection (ruling п. 3, 12).
- **Q9. `specialist_id` в Appointment — ЗАКРЫТ (финальная сверка):**
  запрещён как SoR-атрибут; допустим только как derived в read
  models/search/analytics; действует инвариант цепочки (§14).

Открытых вопросов, блокирующих оформление DEC, не осталось. Forward-
ссылка на planned AYLA-DEC-0021 не требует создания пустой записи-
заглушки (owner direction: без резервирования номеров).

## 17. Owner ruling (финальный текст, зарегистрирован как AYLA-DEC-0020)

1. **target_model.** Каноническая модель — трёхуровневая коммерческая
   модель с разрешением исполнителя через Membership → Profile:
   Catalog Service (смысловая услуга) → Service Offering (коммерческое
   предложение организации) → Specialist Offering Assignment →
   Specialist Membership → Specialist Profile.
2. **offering_owner.** Service Offering принадлежит Provider; Offering
   несёт `tenant_id` как границу изоляции/доступа, но Tenant не владелец
   прайса — понятия не взаимозаменяемы (AYLA-DEC-0017). Соло-мастер —
   организация с одним active membership; отдельного контура соло не
   существует.
3. **assignment_target.** Specialist Offering Assignment ссылается на
   `specialist_membership_id`; модель `assignment.specialist_id`
   запрещена. Assignment несёт price_override, duration_override,
   booking_enabled, status, qualification_status с
   qualification_evidence_ref; assignment не является доказательством
   квалификации. Effective values: `effective_price = override ??
   base_price`; `effective_duration = override ?? base_duration`.
   `booking_allowed` — результат domain policy evaluation, не поле
   Assignment: `offering.is_active AND offering.booking_enabled AND
   assignment.status = active AND assignment.booking_enabled AND
   membership active AND availability decision = available
   (определяется отдельным контрактом — planned AYLA-DEC-0021) AND
   qualification/safety requirements satisfied`; `booking_allowed`
   требует `qualification_status = verified`, если применимая policy
   требует подтверждения квалификации.
4. **solo_auto_assignment.** Активация Offering соло-организации
   невозможна без active Assignment на единственный eligible Specialist
   Membership; draft Offering без assignment допустим; create+activate —
   синхронная атомарная транзакция; асинхронное создание assignment при
   активации запрещено. Для организации с несколькими мастерами
   авто-assignment всем membership не выполняется — назначение делает
   owner.
5. **specialist_permissions.** Specialist управляет собственной
   доступностью (`active → self_disabled`); возврат — owner/admin, для
   safety-sensitive услуг — только с подтверждением специалиста.
   `base_price` специалисту запрещён; own `price_override` — только по
   делегированному permission. Минимальный permission-набор:
   `offering.manage_base_price`,
   `offering_assignment.manage_own_availability`,
   `offering_assignment.manage_own_price_override`,
   `offering_assignment.manage_any`.
6. **pricing_domain.** Offering price — Commerce/Catalog Management, не
   Platform Billing (тариф подписки, комиссия Ayla, реквизиты). Матрица:
   Owner — billing да, pricing да; Admin — billing нет, pricing по
   permission policy; Specialist — billing нет, own override по
   делегированию. Смысл AYLA-DEC-0017 п. 6 не изменяется.
7. **yclients_mvp.** В MVP — guided/manual import с валидацией, dry-run,
   отчётом о дублях и подтверждением owner; полная авто-синхронизация
   deferred. Модель import-ready: ExternalMapping (provider,
   external_entity_type, external_id, internal_entity_type, internal_id),
   правила дедупликации, idempotency key. Импорт создаёт 1 Offering +
   N Assignments, не N Offerings.
8. **appointment_contract.** Appointment хранит ссылки
   `service_offering_id` + `specialist_assignment_id` +
   `specialist_membership_id` и snapshots `effective_price_snapshot`,
   `effective_duration_snapshot`, `offering_title_snapshot` (суффикс
   `_snapshot` обязателен); цена — value object
   `price_snapshot {amount, currency}`. Историческая запись не изменяется
   при изменении цены. `specialist_id` запрещён как SoR-атрибут
   Appointment: исполнитель — через `specialist_membership_id`, профиль —
   через Membership → Profile; denormalized `specialist_id` допустим
   только в read models/search/analytics (derived, не в write commands,
   не в инвариантах). Инвариант цепочки: `service_offering_id` и
   `specialist_membership_id` в Appointment обязаны совпадать с Offering
   и Membership, на которые ссылается `specialist_assignment_id`; все
   три сущности — один tenant.
9. **slot_calculation.** Слот рассчитывается от effective_duration
   конкретного assignment; availability decision определяется отдельным
   контрактом; алгоритм слотов, наложение расписаний, room/equipment —
   вне scope, отдельное решение (planned AYLA-DEC-0021; пустые
   записи-заглушки не создаются).
10. **migration.** Переход per-master → целевая модель: candidate
    grouping → confidence → preview → owner confirmation → commit.
    Объединение только по названию запрещено; минимальные ключи:
    organization, canonical service, branch/location, service variant,
    currency.
11. **lifecycle.** Offering: `draft / active / paused / archived`.
    Assignment — допустимые переходы: `pending → {active, archived}`;
    `active → {self_disabled, organization_disabled, suspended,
    archived}`; `self_disabled → {active, organization_disabled,
    suspended, archived}`; `organization_disabled → {active, suspended,
    archived}`; `suspended → {active, archived}`; `archived → {}`.
    Различие: `organization_disabled` — коммерческое решение организации;
    `suspended` — принудительное ограничение (compliance/qualification/
    safety/platform enforcement). Offering paused → новые записи
    запрещены, assignments сохраняются; membership terminated →
    assignments not bookable, сохраняются для истории; archived не
    удаляется при наличии записей.
12. **catalog_projection.** Клиент видит offering один раз («от 1500 ₽»,
    «60–90 минут», N специалистов); «от X» = min effective_price активных
    assignments — derived projection, не SoR.
13. **Non-goals.** В AYLA-DEC-0020 не входят: алгоритм слотов, наложение
    расписаний, room/equipment, пакеты, акции/скидки, JSON Schema
    импорта, полный permission-каталог.
14. **SoR и migration канона.** System of Record: Service Offering и
    Specialist Offering Assignment → Provider Management (CAP-009,
    business truth); CAP-019 — enforcement; CAP-008 — только канонический
    Catalog Service; формулировка `Provider/Catalog boundary`
    упраздняется. CDM v1.3 вносит пп. 1–13; области «Offering owner» и
    «Offering lifecycle» снимаются из блокирующих после публикации v1.3.

## Change Log

| Версия | Дата | Изменение |
|---|---|---|
| v0.1 | 2026-07-28 | Первоначальный бриф: варианты V1/V2/V3, рекомендация V1 (provider-level Offering + Assignment на `specialist_id`), 8 открытых вопросов |
| v0.3 | 2026-07-28 | Применён owner ruling: трёхуровневая модель с Assignment на `specialist_membership_id` (модель `assignment.specialist_id` запрещена); формализованы effective values и `booking_allowed`; контракт Appointment (3 ссылки + 3 snapshot); permission-набор и разделение pricing/billing; статусы offering/assignment по ruling; соло авто-assignment атомарный; guided YClients import с ExternalMapping; процедура миграции с минимальными ключами; Q1–Q8 закрыты; целевая запись AYLA-DEC-0020; §17 переписан по структуре ruling (14 нормативных пунктов) |
| v0.4 | 2026-07-28 | Решение зарегистрировано как AYLA-DEC-0020; применены правки финальной сверки: (1) `specialist_id` в Appointment запрещён как SoR-атрибут (только derived read models), добавлен инвариант цепочки offering/assignment/membership + один tenant; (2) offering_owner — Provider, `tenant_id` граница изоляции, не владелец; (3) без резервирования номеров — все ссылки «planned AYLA-DEC-0021»; (4) `booking_allowed` — domain policy evaluation: убрано «specialist available», добавлены «availability decision = available (planned AYLA-DEC-0021)» и «qualification/safety requirements satisfied»; (5) snapshots с обязательным суффиксом `_snapshot`, цена — value object `price_snapshot {amount, currency}`; (6) соло-инвариант сужен до активации Offering, draft без assignment допустим; (7) lifecycle Assignment — явный перечень переходов, различие `organization_disabled` vs `suspended`; (8) `qualification_evidence` → `qualification_evidence_ref`, qualification-gate в `booking_allowed`; (9) термин «трёхуровневая коммерческая модель с разрешением исполнителя через Membership → Profile»; добавлен Q9 в §16 |
