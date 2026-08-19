---
node_id: ayla.architecture.master-mvp-auth-authority-contract
title: Ayla Master MVP Auth and Authority Contract
type: specification
status: approved
decision_status: accepted
canonical_status: approved
version: "1.0"
owner: Domain Architecture
owners:
  - Domain Architecture
  - Product Architecture
  - Product Owner
knowledge_area:
  - architecture
domain:
  - identity
  - booking
system_owner:
  - shared
source_repository: ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: medium
data_categories:
  - pii
  - credentials
security_sensitivity: high
ai_indexing: allowed
export_policy: sanitized
created: 2026-08-17
updated: 2026-08-18
review_cycle: monthly
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Glossary]]"
  - "[[Ayla Repository Responsibility Matrix]]"
  - "[[Ayla Knowledge Area Taxonomy]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Ayla Domain Context Map]]"
  - "[[Ayla Core Domain Model Specification]]"
  - "[[Ayla Decision Log]]"
  - "[[Ayla MVP Appointment Contract]]"
  - "[[Consent Scope Registry]]"
related:
  - "[[Ayla MVP Customer Resolution Contract]]"
  - "[[Ayla Master System and Recovery UX Contract]]"
  - "[[Ayla Master Schedule UX Contract]]"
  - "[[Ayla Salon Operations MVP Contract]]"
  - "[[Ayla Master Operations Screen Contract]]"
  - "[[Ayla Master Appointment Flow MVP]]"
  - "[[Ayla Master App Information Architecture]]"
---

# Ayla Master MVP Auth and Authority Contract

> Статус: **Canonical** — принят в canon 2026-08-18 (Canon Review: READY FOR
> CANON; governance ruling AYLA-DEC-0026). Master MVP canonical set:
> FROZEN FOR ENGINEERING / CONTROLLED PILOT.
>
> Этот документ закрывает P0-B1 (Master authentication / session / identity /
> tenant context) и P0-B2 (Master authority / permissions для обязательных P0
> writes) по результатам аудита `docs/REPLY_MASTER_MVP_FINAL_GAP_CHECK.md` и
> owner ruling `docs/MASTER_MVP_P0_AUTHORITY_RUNTIME_CLOSURE(1).md`.
> Он не создаёт новую identity model, не строит IAM-платформу и не меняет
> утверждённые решения AYLA-DEC-0016, AYLA-DEC-0017, AYLA-DEC-0020, AYLA-DEC-0021.
> Он фиксирует минимальный implementation-readable контракт, собранный из уже
> принятых canonical решений.

## 1. Purpose

Этот контракт определяет минимальные canonical правила, необходимые Engineering
для Master MVP Controlled Pilot:

1. путь `OPEN APP → AUTHENTICATE → RESOLVE PRINCIPAL → RESOLVE MASTER IDENTITY →
   RESOLVE SALON/TENANT CONTEXT → ENTER MASTER APP`;
2. поведение при `SESSION EXPIRES / INVALID / REVOKED → REFRESH OR RE-AUTH →
   RESTORE SAFE CONTEXT или RETURN TO AUTH`;
3. authority/permission boundary обязательных P0 reads и writes Master MVP,
   единую для Manual UI и Ayla.

Документ является canonical owner для session lifecycle и Master MVP authority
policy. Entity semantics (Subject, User, Account, Identity Reference, Tenant,
Provider Membership, Role Assignment, Specialist Profile) принадлежат
`Ayla Core Domain Model Specification` и здесь не переопределяются. Capability
ownership: Identity and Access (CAP-019) владеет identities, credentials и
access decisions; Provider Management (CAP-009) владеет business truth
Membership/roles; Appointment (CAP-011) и Availability (CAP-010) владеют
соответствующими commands.

## 2. Scope and Non-Goals

В scope — только Master MVP P0: authenticated principal, Master identity,
tenant/salon scope, session lifecycle minimum, permission policy обязательных
P0 operations, fail-closed и recovery semantics.

Не строится в этом контракте:

- Profile, Account Settings, device management UI;
- full IAM platform, enterprise RBAC/ABAC;
- advanced multi-tenant switcher, admin account management;
- customer-facing auth/account-linking UX flow (отдельный downstream артефакт
  I-16 `Ayla Mobile Auth and Account-Linking Flow`, owner — UX; настоящий
  контракт не дублирует его identity model);
- customer-side каналы и customer-side exception authority;
- Master Mark No Show authority/evidence (остаётся Open/Deferred, см. OQ-AC-7);
- новые domain entities, statuses, events, commands, permission engine.

## 3. Authenticated Principal

Authoritative authenticated principal — **Account** (AYLA-DEC-0016,
`Ayla Core Domain Model Specification` §7.1). Account — учётная запись входа;
аутентификация устанавливает факт «этот вызов выполняется от Account».

- Principal resolution: `Account → User` (User 1—0..N Account; унификация
  идентификаторов на `user_id` запрещена, AYLA-DEC-0016 п. 2–3).
- MVP identity slice: один Account-канал (MAX), Identity References
  `max_user_id` и `phone` (AYLA-DEC-0016 п. 8). Канальный credential/transport
  механизм (token format, OTP, MAX linking handshake) — implementation detail
  канала и Engineering, не domain decision.
- Session всегда привязана к `account_id`; анонимный или channel-only
  principal для Master App не существует.

## 4. Master Identity Resolution

`authenticated principal → Master identity` резолвится через canonical цепочку:

```text
Account → User → Specialist Profile
```

- Specialist Profile привязан к User и не содержит `provider_id`; профиль,
  доступ и tenant-связь — три независимых факта (AYLA-DEC-0017 п. 3).
- Master identity для presentation — Specialist Profile; исполнитель в
  Appointment определяется через `specialist_membership_id`
  (AYLA-DEC-0020 п. 8); денормализованный `specialist_id` в write commands
  запрещён.
- Наличие Specialist Profile не даёт доступа само по себе: доступ определяется
  только Membership + Role Assignment (§5).

## 5. Tenant / Salon Scope

Tenant context определяется канонической моделью AYLA-DEC-0017:

- Доступ персонала требует **active Provider Membership + подходящей Role
  Assignment**; JWT `active_tenant` проверяется против Membership **на каждый
  запрос** (AYLA-DEC-0017 п. 8).
- MVP: один Provider связан ровно с одним Tenant (п. 2); роли MVP: `owner`,
  `admin`, `specialist` (п. 6).
- Business truth Membership/roles — Provider Management (CAP-009); Identity and
  Access (CAP-019) владеет enforcement и хранит только авторизационную проекцию
  (п. 11).
- **Fail-closed:** отсутствие active Membership, несовпадение `active_tenant`,
  suspended/revoked Membership → доступ запрещён, операция не выполняется,
  отсутствие данных никогда не интерпретируется как разрешение.
- **No silent cross-tenant access:** любой read/write выполняется только в
  активном tenant scope; tenant switching без явной смены контекста невозможен.

### 5.1. P0 tenant scope statement (Controlled Pilot)

- Соло-мастер — вырожденный случай: один User, один Tenant, один Provider,
  один Membership с ролями `owner` + `specialist` (AYLA-DEC-0017 п. 10). Это
  базовая конфигурация Controlled Pilot.
- Canonical модель допускает несколько active Membership у одного Specialist
  Profile (п. 4), поэтому ограничение P0 не является model change.
- Для Master MVP P0 действует **один active tenant context на сессию**.
  Multi-salon tenant switcher UX — post-MVP и не создаётся. Мастер с несколькими
  active Membership вне подтверждённого pilot scope; поддержка такого входа —
  OWNER DECISION / расширение pilot scope, а не implementation detail.

## 6. Session Lifecycle Minimum

Session — owned concept Identity and Access (CAP-019). Этот раздел фиксирует
минимальный canonical lifecycle; физические параметры (token TTL, storage,
rotation) — Engineering detail, обязанный соблюдать семантику ниже.

| Событие | Canonical поведение |
|---|---|
| Initial authentication | Успешная аутентификация канала создаёт authenticated session, привязанную к `account_id` и `active_tenant`. До завершения principal/identity/tenant resolution ни один P0 read/write недоступен. |
| Session valid | Reads и writes выполняются в рамках authority §7. Session не расширяет authority: право вычисляется из Membership/Role на момент операции на authoritative backend layer. |
| Session expires | Истёкшая session не даёт права ни на read, ни на write. Клиент выполняет refresh; при невалидном refresh — re-auth. Consequential write с истёкшей session отклоняется fail-closed. |
| Refresh | Refresh продлевает ту же логическую session при валидных credentials; revocation проверяется и при refresh. |
| Re-auth | Повторная аутентификация создаёт новую session; прежняя считается revoked. Re-auth не изменяет tenant context автоматически: контекст восстанавливается через authoritative resolution §3–§5. |
| Session invalid / revoked | Немедленный fail-closed: все операции отклоняются, включая reads. UX возвращает пользователя в auth согласно `Ayla Master System and Recovery UX Contract`; локальные данные не используются как trusted context. |
| Logout | Явный revoke session; повторное использование session credentials запрещено. |
| Membership revoked/suspended внутри живой session | Доступ прекращается немедленно на следующем запросе (per-request проверка `active_tenant`, AYLA-DEC-0017 п. 8); session не является обходом revocation. |
| Safe recovery после refresh/re-auth | Восстановление контекста только через authoritative revalidation: stale projection требует revalidation перед consequential write; offline consequential writes в P0 запрещены; unknown write — reconciliation/readback, blind duplicate запрещён (`Ayla Master System and Recovery UX Contract` §4, §9). |

Отдельная recovery model не создаётся: presentation/recovery semantics полностью
переиспользуют `Ayla Master System and Recovery UX Contract` (FROZEN).

## 7. Master Authority / Permission Policy (P0)

### 7.1. Invariants

1. **Visibility ≠ Write Permission.** Object-level и action-level permission
   различаются; право записи никогда не выводится из видимости, назначения или
   отрисовки кнопки (`Ayla Master System and Recovery UX Contract` §8).
2. **UI ≠ Security Boundary.** Клиент (Mobile UI, Ayla surface) не является
   security boundary; скрытие действия в UI не является enforcement.
3. **Authoritative enforcement.** Consequential permission проверяется только
   authoritative backend layer: CAP-019 enforcement projection против business
   truth CAP-009, на каждый запрос, в tenant scope.
4. **Ayla has no elevated authority.** Ayla действует в модели
   READ/PROPOSE/COMMAND (`Ayla Repository Responsibility Matrix` §5); WRITE
   выполняет только domain owner. AI suggestion ≠ business action; AI tool
   invocation ≠ WRITE. AI-specific permissions и AI-specific booking commands
   не создаются.
5. **Одна authority boundary.** Manual UI и Ayla приходят к одной canonical
   authority boundary и одним commands; разные permission semantics для UI и AI
   запрещены.
6. **Failure semantics.** `DENIED`, `CONFLICT`, `UNKNOWN` переиспользуют
   System/Recovery contract: DENIED — fail-closed без данных; CONFLICT —
   остановка stale write, сохранение валидного контекста, без silent
   overwrite/shift; UNKNOWN ≠ SUCCESS ≠ CONFIRMED FAILURE — authoritative
   readback/reconciliation, blind duplicate запрещён.

### 7.2. P0 permission policy matrix

| Operation | Who may initiate | Tenant / provider scope | Permission / policy gate | Authoritative command owner | Denial / conflict |
|---|---|---|---|---|---|
| View Today / View Schedule / View Appointment Detail; Ayla operational reads | Любой actor с active Membership (`owner`, `admin`, `specialist`) | Только активный tenant; purpose-limited projection (RRM §13) | Active Membership + совпадение `active_tenant` | Read projections CAP-010 / CAP-011 | DENIED → fail-closed, нет данных; stale → revalidation перед consequential действием |
| CreateAppointment (Manual Booking) | `specialist` — в пределах своих assignment; `owner`/`admin` — в пределах tenant | Tenant + `specialist_membership_id` контекст исполнителя | Active Membership + role; offline/admin booking: обязательный audit, те же overlap-проверки в той же locking boundary; запись вне Availability Rule — явная override-команда с actor + reason (AYLA-DEC-0021 п. 8) | Appointment Management (CAP-011), команда `CreateAppointment` | DENIED (нет права); CONFLICT (`SLOT_TAKEN` / overlap — запрещён даже override); UNKNOWN → authoritative readback |
| CreateAppointment (Ayla) | Те же actors; Ayla только PROPOSE/COMMAND с подтверждением мастера | Как Manual Booking | Как Manual Booking; elevated AI authority отсутствует | Appointment Management (CAP-011), та же команда `CreateAppointment` | Как Manual Booking |
| Working Hours (изменение Availability Rule) | `specialist` — собственная доступность (self-service, AYLA-DEC-0021 п. 9; recurring change — через approval workflow); `owner`/`admin` — tenant | Tenant + собственный assignment для specialist | `offering_assignment.manage_own_availability` / `offering_assignment.manage_any` (AYLA-DEC-0020 п. 5) + active Membership | Availability Management (CAP-010) | DENIED; versioned rules (AYLA-DEC-0021 п. 10); конфликтующие hold → `released` + audit (п. 6); Appointment автоматически не изменяются — remediation `needs_resolution` |
| Specific Day Exception (Schedule Block `date_exception` / `override`) | Как Working Hours | Как Working Hours | Как Working Hours | Availability Management (CAP-010) | Как Working Hours |
| Time Off create (Schedule Block `time_off` / `sick_day`) | `specialist` — свой; `owner`/`admin` — tenant | Tenant + собственный assignment для specialist | Как Working Hours; `sick_day` — немедленный эффективный Block + audit + уведомление admin; vacation/planned leave — через approval workflow (AYLA-DEC-0021 п. 9) | Availability Management (CAP-010) | Как Working Hours |
| Time Off edit/delete | Те же actors, в объёме, утверждённом `Ayla Master Schedule UX Contract` для P0 | Как Time Off create | Как Time Off create | Availability Management (CAP-010) | Как Working Hours |

Матрица является компактной canonical policy для P0. Расширение ролей,
permission framework и новые permissions вне перечисленных — вне scope.

### 7.3. Known dependencies (не domain gaps)

- Точные имена availability commands/events (SCH-OQ-02) — canon/engineering
  dependency CAP-010; настоящая policy ссылается на владельца и gate, не
  выдумывая command names.
- Физический SoR `beautygo_backend` — `Proposed` (OD-RRM-1); это не меняет
  domain ownership выше.
- Completion/no-show write authority по ролям (OQ-AC-7) — отдельный вопрос,
  настоящий контракт его не закрывает и не блокируется им.

## 8. Recovery

Recovery semantics не создаются заново. Все состояния (Loading, Empty, Stale,
Offline, Unknown, Conflict, Permission) потребляются из
`Ayla Master System and Recovery UX Contract` (FROZEN FOR IMPLEMENTATION).
Auth/session события §6 отображаются на них так: expired/invalid/revoked →
return to auth; recovery → authoritative revalidation; unknown write →
reconciliation/readback.

## 9. Open Questions Classification

| Item | Classification | Основание |
|---|---|---|
| Authenticated principal, Master identity, tenant scope, session lifecycle | RESOLVED BY CANON (этот контракт) | AYLA-DEC-0016, AYLA-DEC-0017, CDM §7 |
| Master authority/permissions для P0 writes (SCH-OQ-06) | RESOLVED BY CANON (этот контракт, §7) | AYLA-DEC-0020 п. 5, AYLA-DEC-0021 п. 8–9 |
| Multi-salon tenant switcher | DEFERRED (post-MVP) | AYLA-DEC-0017 п. 4 допускает модель; UX не требуется pilot |
| Делегирование внешнему identity provider | DEFERRED (open question AYLA-CTX-018) | Domain Context Map §5.22 |
| Customer-facing auth/account-linking UX flow (I-16) | DEFERRED (UX-owned downstream artifact) | `Ayla MVP v0.3 Downstream Migration Plan` I-16 |
| Master Mark No Show authority/evidence (OQ-AC-7) | DEFERRED | Owner ruling: no-show не расширяет текущую задачу |
| Credential mechanism, token TTL, session storage | ENGINEERING DETAIL | Обязан соблюдать §6 |
| Availability command/event names (SCH-OQ-02) | ENGINEERING / canon dependency CAP-010 | Не блокирует authority policy |
| Физический SoR (OD-RRM-1) | ENGINEERING / owner decision вне этой задачи | RRM §14 |

## 10. Definition of Done Coverage

Этот контракт отвечает на вопросы Engineering 1–11 из closure brief: кто
authenticated principal (§3); связь principal → Master (§4); salon/tenant scope
(§5); session expiry (§6); revoked/invalid session (§6); кто может создать
Appointment, менять Working Hours, конкретный день, создавать Time Off (§7.2);
где authoritative permission enforcement (§7.1 п. 3); получает ли Ayla
дополнительные права (§7.1 п. 4 — нет).
