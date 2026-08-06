# Decision Brief — Tenant, Membership and Role Model (AYLA-DEC-0017)

> **Статус:** готов к оформлению DEC после повторной проверки владельцем
> (owner review 2026-07-28 применён, v0.2). Не является решением до записи
> AYLA-DEC-0017 в [[Ayla Decision Log]]. Размещён в `99 Archive/proposals/`
> — validator-exempt.
> **Дата:** 2026-07-28 · **Автор:** Domain Architecture (подготовка) ·
> **Целевая запись:** AYLA-DEC-0017 · **Зависит от:** AYLA-DEC-0016
> (Subject Identity Model)

## 1. Проблема и почему решение требуется сейчас

CDM v1.2.2 моделирует исполнителя как `Specialist` (§7.8) с полями
`provider_id` + `user_id`: мастер жёстко привязан к одному провайдеру и к
учётной записи человека одновременно. Трёх разных вещей — профессиональный
профиль мастера, его доступ к салону и его связь с tenant — в модели нет:
нет Tenant как объекта (у Provider есть `tenant_id`-поле без referent,
§7.7), нет Membership, нет Role Assignment. Инвариант 2 §7.7 («самозанятый
может играть роли Provider и Specialist, но идентичности не смешиваются»)
уже признаёт проблему, но не даёт ей структуры.

Эксплуатация опять впереди канона. Аудит архитектуры
(`architecture-maps/05-architecture-problems-audit.md`, P1-1): «Tenancy in
Ayla is a single nullable `User.tenant` FK; N-tenant-per-user /
active-tenant verification is unmodeled. bot assumes JWT `tenant_id` =
`active_tenant` verified via `TenantUserRelationship`. The denormalization
invariant is **not DB-enforced**». То есть runtime предполагает
множественную связь человек↔tenant, которой нет ни в БД Ayla, ни в CDM.
Блокирующая область identity foundation (Subject/Tenant/Membership)
зафиксирована в CDM §1.

MVP-персоны (MVP Scope §2) — соло-мастер и малый салон до трёх мастеров —
уже требуют: отключения мастера без потери истории записей, доступа
администратора к записям салона, корректного offboarding. Без модели
membership каждый из этих процессов — ad-hoc правки FK с потерей аудита.

## 2. Реальные сценарии

Из handoff-материалов (подтверждённые):

- **S1. Один человек — несколько tenant'ов.** JWT `tenant_id` должен
  проверяться против связи человек↔tenant; связь не смоделирована
  (`architecture-maps/05-architecture-problems-audit.md`, P1-1;
  `architecture-maps/README.md`, строка 48).
- **S2. Администратор салона вносит offline-записи.** «все
  phone/walk-in/offline записи администратор заносит в Ayla»
  (`orch.txt`, строка 339, Вариант A primary calendar) — роль Admin
  действует от имени салона в чужих (клиентских) данных, это должен быть
  явный Role Assignment с audit, а не shared login.
- **S3. Профиль мастера сегодня per-tenant.** «"Любимый мастер" считается в
  ClientProfile, а он привязан к салону (per-tenant)»
  (`PersonalContext.txt`, строка 20) — текущая модель привязывает
  профессиональную идентичность мастера к tenant'у; кросс-тенантная
  агрегация «любимых» требует tenant-независимого профиля (строка 75).

Подтверждены владельцем как platform requirements (owner review
2026-07-28; источники указаны владельцем в ruling):

- **S4. Мастер работает в нескольких салонах** *(подтверждено:
  master-substitution-handoff, tenant selector)*. Один Specialist Profile,
  несколько активных Membership; расписание и записи разделены по tenant'ам.
- **S5. Отключение мастера в одном салоне** *(подтверждено:
  master-offboarding-handoff)*. Membership в салоне A — revoked, в салоне
  B — active; история записей салона A сохраняется полностью.
- **S6. Временный доступ замещающего** *(подтверждено:
  master-substitution-handoff, Q-MS6)*. Замещение per-tenant и scoped:
  time-boxed Role Assignment, один tenant, только назначенные Appointment,
  автоматическое истечение.
- **S7. Offboarding владельца/админа** *(подтверждено:
  master-offboarding-handoff)*. Отзыв всех Role Assignment, передача
  ownership, сохранение коммерческой истории салона.
- **S8. Мастер и администратор — разные роли** *(подтверждено:
  master-mobile-handoff)*. Разделение полномочий admin и specialist —
  нормативное требование, а не вариант реализации. Независимо: «Работодатель,
  партнёр или иной внешний участник не получает доступ к индивидуальному
  питанию, весу, здоровью, личной модели или истории пользователя»
  (Конституция, строка 440) — любая tenant-роль не даёт доступа к
  memory/consent клиентов.

## 3. Рассматриваемые варианты

### Вариант A — Статус-кво: Specialist = provider_id + user_id, роль как enum

Оставить §7.8; роль (owner/admin/master) — enum-поле на User или Specialist.

- **Плюсы:** нулевая миграция; минимальная модель для соло-мастера.
- **Минусы:** S4 требует либо двух `user_id` (сломанная идентичность,
  конфликт с AYLA-DEC-0016), либо дубли Specialist-строк (двойники профиля);
  S5 невозможен без удаления/перепривязки Specialist — история Appointment
  теряет referent; S6/S7 невыразимы; роль сшита с идентичностью — тот же
  класс ошибки, что унификация на `user_id` в identity-модели.

### Вариант B — Разделённые сущности (рекомендуемый)

Шесть объектов:

- **User** — человек (по AYLA-DEC-0016).
- **Tenant** — самостоятельная сущность границы изоляции и биллинга. В MVP
  один Provider связан ровно с одним Tenant, но понятия не синонимы.
- **Provider** — организация-исполнитель (салон или самозанятый).
- **Provider Membership** — связь User × Provider со статусом и периодом;
  носитель доступа человека к tenant'у.
- **Role Assignment** — роль (`owner` / `admin` / `specialist`) внутри
  Membership, time-boxed (`valid_from`, `valid_to`), отзываемая.
- **Specialist Profile** — профессиональный профиль мастера
  (квалификации, отображаемое имя, eligibility), привязан к User, **не** к
  Provider; видимость в tenant'е определяется активным Membership с ролью
  `specialist`.

Ключевое правило: **профиль ≠ доступ ≠ связь с tenant**. Appointment,
Service Offering и Availability Slot ссылаются на `specialist_id` +
`provider_id` (snapshot-семантика CDM §13 не меняется); валидность ссылки
проверяется через Membership на момент операции, а не через жёсткий FK
профиля к провайдеру.

- **Плюсы:** S1–S8 покрываются штатно; revoke Membership не трогает ни
  профиль, ни историю; модель совпадает с предположением runtime
  (`TenantUserRelationship`, P1-1) — канон и код сходятся, а не расходятся;
  самозанятый (инвариант 2 §7.7) — вырожденный случай: один User, один
  Tenant, один Provider, один Membership с двумя Role Assignment (`owner` +
  `specialist`), идентичности не смешиваются.
- **Минусы:** пять новых сущностей и переписывание §7.8; каждая
  авторизация — трёхзвенная проверка (membership active + role allows +
  tenant match); миграция существующих Specialist-строк.

### Вариант C — Membership без отдельного Specialist Profile

Связь и роль выделяются, но профиль мастера остаётся атрибутами Membership
(per-tenant).

- **Плюсы:** на одну сущность меньше; решает S1, S2, S5–S7.
- **Минусы:** нарушает правило «профиль ≠ связь с tenant»: квалификации и
  репутация дублируются per-tenant, S3/S4 (кросс-тенантный профиль,
  агрегация «любимых») не решаются; повторяет сегодняшний дефект
  per-tenant ClientProfile (`PersonalContext.txt`, строка 20) на стороне
  мастера.

## 4. Рекомендуемый вариант и обоснование

**Вариант B**, с разделением MVP-среза и platform-scope по образцу
AYLA-DEC-0015:

- **MVP-active:** Tenant (1 Provider = 1 Tenant), Provider, Provider
  Membership (create / suspend / revoke), роли `owner`, **`admin`
  (минимальная)**, `specialist`; отдельный Specialist Profile; правило
  «revoke ≠ delete» с remediation items для будущих записей (§5, R1).
  Полномочия `admin` в MVP: создание/изменение offline-записей; работа с
  расписанием; операционные данные своего tenant; клиентские обращения в
  пределах политики. Запреты `admin`: управление ownership, billing/legal
  settings, доступ к memory/wellness/consent клиента, назначение owner;
  все действия `admin` с чужими Appointment аудируются.
- **Platform-scope / deferred:** substitute-доступ (S6) как workflow —
  deferred, но модель обязана допускать time-boxed Role Assignment, scoped
  access, один tenant, только назначенные Appointment, автоматическое
  expiry; ownership transfer (S7); эксплуатационные процессы multi-salon
  мастера (S4 — модель допускает, UI/onboarding post-MVP); сложная
  multi-tenant тарификация (CAP-020 — `out` по MVP Scope §5); изменение
  кардинальности Provider↔Tenant.

Обоснование: вариант A воспроизводит на стороне персонала ту же ошибку,
которую AYLA-DEC-0016 устраняет на стороне клиентов (сшивание идентичности,
доступа и роли); вариант C сохраняет per-tenant дефект профиля, уже
признанный препятствием для персонализации. Runtime предполагает модель B
(P1-1) — канон догоняет эксплуатацию. Включение минимальной роли `admin` в
MVP подтверждено владельцем (основание: `orch.txt`, master-mobile,
substitution handoffs — сценарии S2, S8).

## 5. Достоинства и риски рекомендуемого варианта

Достоинства: мастер в нескольких салонах без дублей; точечный отзыв
доступа; неразрушающий offboarding; проверяемая tenant isolation;
вырожденный случай соло-мастера без спецкода.

Риски и митигации:

- **R1. «Висячие» будущие записи при revoke (owner ruling).** Revoke
  немедленно прекращает доступ; Appointment автоматически **не**
  изменяются. Для каждой будущей активной записи создаётся обязательный
  **remediation item** со статусом `needs_resolution` — это состояние
  операционной задачи, а **не** новый статус Appointment. Owner/admin
  уведомляется; решение (сохранить / переназначить / перенести / отменить)
  принимается явно, с actor, reason и уведомлением клиента. До
  автоматизации допускается ручная процедура только при наличии: списка
  затронутых записей, назначенного ответственного, audit trail и
  подтверждения обработки каждой записи.
- **R2. Усложнение авторизации.** Трёхзвенная проверка на каждый запрос.
  Митигация: единая authZ-функция `resolve_membership(user_id, tenant_id)
  → roles`, денормализованный `active_tenant` в JWT проверяется против неё
  (закрывает P1-1).
- **R3. Вырожденный соло-мастер: 5 строк вместо 1.** Митигация:
  onboarding-флоу создаёт связку атомарно; доменная модель не обязана
  повторять физическую компактность.
- **R4. Рассинхрон с текущей БД (`User.tenant` FK).** Митигация: миграция
  FK → Membership-таблица с backfill; interim-маппинг фиксируется в Scope
  Contract (механика AYLA-DEC-0016, п. 9).

## 6. Влияние на privacy, consent, memory и tenant isolation

- **Tenant isolation:** Tenant — самостоятельная сущность границы изоляции;
  Membership — единственный носитель доступа персонала к данным tenant'а;
  нет active Membership — нет доступа, включая JWT с устаревшим
  `tenant_id` (закрытие P1-1). Revoke действует немедленно для чтения и
  записи.
- **Memory/consent клиентов:** tenant-роли (любые, включая `owner` и
  `admin`) не дают доступа к memory, context и consent-записям клиентов
  (Конституция, строка 440; cross-tenant boundary `c5_contract_draft`,
  строка 333). Consent клиента — комбинация `subject_id + tenant_id +
  scope_id` (CSR §7); revoke Membership мастера не затрагивает consent
  клиентов салона.
- **История после отзыва:** Appointment — SoR статуса записи с
  historical-integrity snapshot (CDM §12–13); записи, созданные в период
  active Membership, остаются у Provider и в клиентской истории после
  revoke. Specialist Profile не удаляется, если на него ссылаются
  Appointments (архивируется).
- **Memory мастера как человека:** если мастер — также клиент Ayla, его
  личные memory/consent живут на его Subject (AYLA-DEC-0016) и не видны
  салонам, где он работает.

## 7. Влияние на существующие сущности и идентификаторы

- `Specialist` (§7.8): разделяется на Specialist Profile (`specialist_id`,
  `user_id` → User, квалификации, eligibility) и Provider Membership
  (`membership_id`, `user_id`, `provider_id`, status, период). Поле
  `provider_id` из профиля уходит; `specialist_id` сохраняется — ссылки из
  Offering/Slot/Appointment не переписываются.
- `Provider` (§7.7): получает явный referent для `tenant_id` — новую
  сущность Tenant (в MVP ровно 1:1, понятия не синонимы). Инвариант 2
  (самозанятый) реализуется через два Role Assignment.
- **Tenant (новый объект):** `tenant_id`, status, created_at; вводится
  сразу, чтобы изменение кардинальности Provider↔Tenant после MVP не
  требовало переопределения identity и authorization contracts.
- `Service Offering` (§7.9), `Availability Slot` (§7.10): идентификаторы не
  меняются; добавляется инвариант — создание/активация требует active
  Membership с ролью `specialist` для связки (specialist, provider).
- `Appointment` (§7.12): без изменений идентификаторов и статусной модели;
  revoke Membership не является событием жизненного цикла Appointment —
  последствия оформляются remediation items (§5, R1).
- `User` (§7.1, версия AYLA-DEC-0016): становится единственной ссылкой
  персонала; прямых `user_id` на Provider больше нет, на Specialist
  Profile — только владение профилем.

## 8. Lifecycle предлагаемых сущностей

```text
Provider Membership: requested/invited → active ⇄ suspended → revoked [terminal, retained for audit]
Role Assignment:     granted → expired (valid_to) | revoked [terminal, retained for audit]
Specialist Profile:  draft → active ⇄ suspended → archived [terminal; delete запрещён при наличии Appointments]
Provider:            active ⇄ suspended → closed [terminal]
Tenant:              active ⇄ suspended → closed [terminal]
Remediation Item:    needs_resolution → resolved (save | reassign | move | cancel) [с actor, reason, уведомлением клиента]
```

Инварианты: (1) `revoked`/`expired` записи не удаляются — audit;
(2) Role Assignment действует только внутри active Membership: revoke
Membership гасит все его Role Assignment; (3) повторный найм создаёт новый
Membership, а не реанимирует revoked; (4) у Provider всегда ≥1 active
Membership с ролью `owner` (кроме состояния `closed`); (5) time-boxed
Assignment с `valid_to` переходит в `expired` без ручного действия;
(6) самостоятельная заявка мастера создаёт Membership только в состоянии
`requested` (pending) без доступа до подтверждения owner; UI для
`requested` в MVP необязателен, модель допускает; (7) revoke Membership
порождает remediation item в `needs_resolution` для каждой будущей
активной записи.

## 9. System of Record

| Объект | System of Record | Примечание |
|---|---|---|
| Tenant | Identity and Access (CAP-019) | граница изоляции и биллинга |
| Provider | Provider Management (CAP-009) | как в CDM §12 |
| Specialist Profile | Provider Management (CAP-009) | наследует строку Specialist CDM §12 |
| Provider Membership | Provider Management (CAP-009) | business truth membership |
| Role Assignment | Provider Management (CAP-009) | business truth назначений |
| Membership/roles (авторизационная проекция) | Identity and Access (CAP-019) | CAP-019 владеет enforcement и хранит **только** проекцию, не business truth |

## 10. Migration impact

- **CDM (v1.3):** переписанный §7.8 (Specialist → Specialist Profile +
  Provider Membership + Role Assignment); §7.7 (referent `tenant_id`,
  вырожденный самозанятый); новый объект Tenant; новые инварианты
  §7.9–7.10; §12 — новые строки SoR (включая разделение business truth /
  enforcement projection); §24 — закрытие Tenant/Membership-части identity
  foundation.
- **Scope Contract:** MVP-срез ролей (`owner`, `admin` минимальная,
  `specialist`) фиксируется в Included Scope; substitute-workflow,
  ownership transfer, изменение кардинальности Provider↔Tenant — Excluded /
  deferred с активацией через §11; ссылка на AYLA-DEC-0015-механику
  ограниченного контура.
- **Domain Capability Registry:** `owned_concepts` CAP-009 расширяется
  (Provider Membership, Role Assignment, Specialist Profile); CAP-019
  дополняется Tenant и авторизационной проекцией membership/roles; CAP-020
  остаётся `mvp_scope: out`.
- **AMD-020:** без изменений — memory ownership не затрагивается.
- **Decision Log:** новая запись AYLA-DEC-0017 (формулировка §12).
- **Runtime (вне канона):** миграция `User.tenant` FK → Membership;
  authZ-функция `resolve_membership`; JWT `active_tenant` enforcement
  (закрытие P1-1); remediation-item очередь для revoke.

## 11. Открытые вопросы владельцу

Все вопросы закрыты owner review 2026-07-28:

- ~~Q1. Provider ≡ Tenant или отдельный Tenant~~ → **закрыт:** Tenant —
  самостоятельная сущность сразу; в MVP один Provider связан ровно с одним
  Tenant, но понятия не синонимы; изменение кардинальности после MVP не
  должно требовать переопределения identity и authorization contracts
  (§12, п. 2).
- ~~Q2. Роль admin в MVP~~ → **закрыт:** минимальная роль `admin` включена
  в MVP с перечнем полномочий и запретов (основание: `orch.txt`,
  master-mobile, substitution handoffs; §4, §12, п. 6).
- ~~Q3. Кто создаёт Membership~~ → **закрыт:** owner tenant'а или
  уполномоченный platform operator; самостоятельная заявка мастера создаёт
  только invitation/request в `requested` (pending) без доступа до
  подтверждения owner (§8, §12, п. 5).
- ~~Q4. Будущие записи при revoke~~ → **закрыт:** обязательные remediation
  items `needs_resolution` (не статус Appointment), уведомление owner/admin,
  явное решение с actor/reason/уведомлением клиента; ручная процедура до
  автоматизации — только при списке записей, ответственном, audit trail и
  подтверждении обработки каждой записи (§5, §12, п. 7).
- ~~Q5. Substitute-доступ~~ → **закрыт:** workflow deferred; модель обязана
  допускать time-boxed Role Assignment, scoped access, один tenant, только
  назначенные Appointment, автоматическое expiry (§4, §12, п. 9).
- ~~Q6. SoR Membership/Role Assignment~~ → **закрыт:** Provider Management
  (CAP-009) владеет business truth; Identity and Access (CAP-019) владеет
  enforcement и хранит только авторизационную проекцию (§9, §12, п. 10).
- ~~Q7. Статус S4–S8~~ → **закрыт:** подтверждены как platform requirements
  (источники: master-mobile-handoff, master-substitution-handoff Q-MS6,
  master-offboarding-handoff, substitution handoff tenant selector; §2).

## 12. Предлагаемая формулировка owner ruling (AYLA-DEC-0017)

> **AYLA-DEC-0017 — Tenant, Membership and Role Model**
>
> **Решение:**
>
> 1. Каноническая модель доступа персонала состоит из шести разделённых
>    объектов: User (по AYLA-DEC-0016), Tenant, Provider, Provider
>    Membership, Role Assignment, Specialist Profile.
> 2. Tenant вводится как самостоятельная сущность сразу. В MVP один
>    Provider связан ровно с одним Tenant, но понятия не синонимы.
>    Изменение кардинальности Provider↔Tenant после MVP не должно требовать
>    переопределения identity и authorization contracts.
> 3. Профессиональный профиль мастера, его доступ к салону и его связь с
>    tenant — три независимых факта: Specialist Profile привязан к User и не
>    содержит `provider_id`; связь с tenant выражается только Provider
>    Membership; доступ и полномочия — только Role Assignment внутри active
>    Membership.
> 4. Прямая привязка `Specialist.provider_id` (CDM §7.8 v1.2.2) отменяется.
>    Один Specialist Profile допускает любое число активных Membership в
>    разных Provider.
> 5. Membership создаёт owner tenant'а или уполномоченный platform
>    operator. Самостоятельная заявка мастера создаёт только
>    invitation/request в состоянии `requested` (pending) без доступа до
>    подтверждения owner. Lifecycle Membership: `requested/invited →
>    active ⇄ suspended → revoked`; UI для `requested` в MVP необязателен,
>    модель допускает.
> 6. Роли MVP: `owner`, `admin`, `specialist`. Минимальная роль `admin`:
>    создание/изменение offline-записей; работа с расписанием; операционные
>    данные своего tenant; клиентские обращения в пределах политики.
>    `admin` запрещено: управление ownership, billing/legal settings,
>    доступ к memory/wellness/consent клиента, назначение owner. Все
>    действия `admin` с чужими Appointment аудируются.
> 7. Revoke или expiry Membership/Role Assignment — терминальные события,
>    не удаляющие записи: Membership, история Appointment, Offering и
>    Specialist Profile сохраняются. Revoke немедленно прекращает доступ и
>    автоматически не изменяет Appointment; для каждой будущей активной
>    записи создаётся обязательный remediation item со статусом
>    `needs_resolution` (состояние операционной задачи, не новый статус
>    Appointment), с уведомлением owner/admin и явным решением (сохранить /
>    переназначить / перенести / отменить) с actor, reason и уведомлением
>    клиента. До автоматизации допускается ручная процедура только при
>    наличии: списка затронутых записей, назначенного ответственного, audit
>    trail и подтверждения обработки каждой записи.
> 8. Доступ персонала к данным tenant'а требует active Membership с
>    подходящей Role Assignment; JWT `active_tenant` обязан проверяться
>    против Membership на каждый запрос. Ни одна tenant-роль не даёт
>    доступа к memory, context и consent клиентов.
> 9. Substitute-доступ: workflow deferred (platform-scope); модель обязана
>    допускать time-boxed Role Assignment, scoped access, один tenant,
>    только назначенные Appointment и автоматическое expiry.
> 10. У Provider всегда существует не менее одного active Membership с
>     ролью `owner`, пока Provider не в состоянии `closed`. Повторный найм
>     создаёт новый Membership; реанимация revoked запрещена. Самозанятый —
>     вырожденный случай: один User, один Tenant, один Provider, один
>     Membership с Role Assignment `owner` + `specialist`.
> 11. System of Record: Provider, Specialist Profile, Provider Membership,
>     Role Assignment → Provider Management (CAP-009) владеет business
>     truth; Identity and Access (CAP-019) владеет enforcement и хранит
>     только авторизационную проекцию Membership/roles; Tenant → Identity
>     and Access (CAP-019).
> 12. CDM v1.3 вносит изменения пп. 1–11 (§7.7–7.10, новые §7.x, §12);
>     область Tenant/Membership снимается из блокирующих (CDM §1) после
>     публикации v1.3.
>
> **Основание:** CDM v1.2.2 сшивает профиль мастера, доступ и связь с
> tenant в одной строке Specialist (`provider_id` + `user_id`, §7.8), что
> делает невыразимыми мастера в нескольких салонах, точечное отключение,
> временный доступ и неразрушающий offboarding — сценарии, подтверждённые
> как platform requirements (master-mobile-handoff,
> master-substitution-handoff Q-MS6, master-offboarding-handoff,
> substitution handoff tenant selector; `orch.txt` — admin вносит
> offline-записи). Runtime уже предполагает связь человек↔tenant
> (`TenantUserRelationship`, аудит P1-1), которой нет в модели; tenancy
> реализована nullable FK без enforcement. Разделение сущностей повторяет
> подтверждённый AYLA-DEC-0016 принцип: идентичность, доступ и роль —
> разные факты с разными System of Record.
>
> **Затрагивает:** Ayla Core Domain Model Specification (§7.7–7.10, новые
> §7.x включая Tenant, §12, §24); Ayla MVP Scope and Release Contract
> (MVP-срез ролей owner/admin/specialist, deferred-перечень); Ayla Domain
> Capability Registry (`owned_concepts` CAP-009 и CAP-019; CAP-020 без
> изменений); зависит от AYLA-DEC-0016. AMD-020 Pilot Scope Registry,
> AMD-001 C5 Export/Forget Contract и Consent Scope Registry не изменяются.

## Change Log

- **v0.1 — 2026-07-28** — первичная версия брифа (12 разделов, рекомендация:
  вариант B).
- **v0.2 — 2026-07-28** — owner review applied: (1) Tenant — отдельная
  сущность сразу, Provider ≡ Tenant отклонён даже для MVP (MVP 1:1, не
  синонимы); (2) минимальная роль `admin` включена в MVP с перечнем
  полномочий и запретов; (3) создание Membership — owner или platform
  operator, самозаявка мастера → `requested` (pending) без доступа;
  (4) revoke → обязательные remediation items `needs_resolution` вместо
  «ручного процесса» как ответа; (5) SoR разделён: business truth —
  CAP-009, enforcement + авторизационная проекция — CAP-019; (6) substitute
  workflow deferred, модель допускает time-boxed/scoped/single-tenant/
  assigned-only/auto-expiry; (7) S4–S8 подтверждены владельцем как
  platform requirements. Q1–Q7 закрыты. Статус: готов к оформлению DEC
  после повторной проверки владельцем.
