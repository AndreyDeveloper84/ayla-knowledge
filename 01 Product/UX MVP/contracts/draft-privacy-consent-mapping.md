---
title: MVP Personal Data and Consent Mapping (Phase 1)
type: specification
status: draft
review_status: ready-for-privacy-owner
owner: Privacy Owner
prepared_by: Cross-domain Contract Agent (Privacy/Consent) — UX side
created: 2026-07-29
basis:
  - UX-OD-003 (accepted_as_temporary_assumption, 2026-07-29)
  - Consent Scope Registry v1.1 (approved)
  - Data Inventory Matrix v1.0 (draft)
  - Ayla MVP Scope and Release Contract v0.3 (§8, §10)
  - AMD-020 C5 Pilot Personal Context Export-Forget Contract
  - SRC-12: global-bot-welcome-consent-spec, customer-booking-confirm-registration-spec
disclaimer: >
  UX не владеет privacy-правилами. Этот документ — ПРОЕКТ для Privacy Owner:
  только предложения и вопросы. Ничто здесь не является принятым
  privacy-решением и не меняет нормативных документов (CSR, DIM, SRC-01).
node_id: ayla.ux.privacy-consent-mapping
version: "0.1"
domain:
  - consent
system_owner:
  - ayla-user-context
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

# MVP Personal Data and Consent Mapping — Phase 1 (проект)

## 0. Контекст и рамка

Owner decision UX-OD-003 (временное допущение, revalidation before release =
true) зафиксировал Phase 1 как **session-only + service_necessity**: persistent
memory отключена, экран consent на `preference_memory` в W1 не создаётся.
Разрешены четыре процесса: `intent_understanding`, `provider_selection`,
`booking_execution`, `transactional_booking_support`. Запрещены до решения
Privacy Owner: persistent prefs, Memory Facts, трактовка продолжения диалога
как согласия на память, скрытое профилирование, маркетинг, проактивные
рекомендации, secondary use, health inference, перенос session data в
persistent storage.

Этот проект отображает старую consent-модель SRC-12 на Consent Scope Registry
(CSR) и предлагает минимальный контракт, разблокирующий customer UX Phase 1.

## 1. Mapping: старая модель SRC-12 ↔ CSR

Старая модель (SRC-12, спеки welcome/registration): enum
`ConsentRecord.ConsentType` = `PERSONAL_DATA` (152-ФЗ baseline),
`PHOTO_BIOMETRIC` (food scanner), `MARKETING`, `HEALTH`; document-versioned
(`privacy-v2.0`); soft-gate Variant A — discovery/chat/одноразовая booking без
согласия, persistent memory и проактив — только с `PERSONAL_DATA`. Legal ACK
#947 (флип A→B, жёсткий гейт) — pending.

| SRC-12 enum | Отображение на CSR | Предложение |
|---|---|---|
| `PERSONAL_DATA` | **Не мапится на один scope.** Это юридический слой 152-ФЗ baseline: уведомление об обработке ПДн и правовое основание для любой обработки. В CSR этому соответствуют: (а) `service_necessity` для session-only обработки по §5.1/§5.2 — отдельный consent record не требуется (CSR §5.1, поле Authorization basis); (б) `preference_memory` (§5.7) — explicit consent для persistent хранения, Phase 2 | Сохранить `PERSONAL_DATA` как отдельный юридический baseline-слой поверх scopes, либо формально заменить его связкой «service_necessity + preference_memory». Решение — Privacy Owner/юрист (Q1) |
| `PHOTO_BIOMETRIC` | Нет соответствия в 7 scopes; функция (food scanner) вне customer booking Phase 1 | Остаётся отдельным consent в своей точке, вне Phase 1. Без вопроса, кроме подтверждения «не в пилоте» |
| `MARKETING` | Нет scope; DIM фиксирует `Marketing Opt-Out` как класс Consent Domain | В Phase 1 маркетинг запрещён (UX-OD-003). Отдельный юридический слой, не затрагивается. Подтвердить (Q6) |
| `HEALTH` | `health_related_signal` (CSR §4) — «Вне MVP; запрещено»; CSR-OD-4 открыт | Не мапится. Health inference запрещён (UX-OD-003). Без вопроса |

**Предложение P1.** Для Phase 1 контракт строится на CSR, а enum SRC-12
трактуется как параллельный юридический слой 152-ФЗ: `PERSONAL_DATA` —
baseline notice/основание; остальные три enum — вне Phase 1. Runtime-гейтинг
идёт по scopes, не по enum.

## 2. Phase 1 data boundary (предложение)

Источники: CSR §4 (data categories), §5.1/§5.2 (allowed data), DIM (владельцы
и правила проекций). Все данные — только в рамках текущей сессии; persistent
storage запрещён (UX-OD-003, SRC-01 §8: «no persistent preference storage»).

| Процесс (UX-OD-003) | Scope / основание | Допустимые данные в session-only | Хранение |
|---|---|---|---|
| `intent_understanding` | CSR §5.1, `service_necessity`, consent не требуется | `explicit_goal`, `service_preference`, `provider_preference`, `session_signal` — только то, что пользователь сказал в текущей сессии | Не сохраняется. `session_signal` по умолчанию не сохраняется (CSR §4) |
| `provider_selection` | CSR §5.2, `service_necessity` | Те же категории + `booking_history` (чтение фактов из backend SoR) и `recommendation_feedback` текущего взаимодействия | Не создаёт persistent state (CSR §5.2). Backend остаётся SoR для booking-фактов (DIM) |
| `booking_execution` | **Вне scopes CSR** — не personalization-purpose. Предложение: `service_necessity` для исполнения явного действия пользователя | Identity-данные для создания записи (имя, контакт), параметры записи (услуга, мастер, слот, note) | Запись в backend (Booking/Account — DIM: W2 Profile, Booking Domain). Это operational storage, не memory. Граница требует подтверждения (Q4) |
| `transactional_booking_support` | **Вне scopes CSR.** Предложение: `service_necessity` для транзакционных уведомлений по записи | Данные самой записи; канал доставки | Notification Preferences — отдельный класс DIM («Communication consent»). Только транзакционные, не маркетинг (Q4, Q6) |

Явно запрещено в Phase 1 (по UX-OD-003 и CSR): `inferred_signal` persistence,
`health_related_signal`, `religious_or_diet_signal` (CSR-OD-4 не решён),
`proactive_recommendation` / `cross_domain_personalization` /
`recommendation_measurement` / `recommendation_explanation` (blocked, CSR
§5.3–5.6), `preference_memory` write, перенос session data в persistent
storage, `tenant_id=null` global scope (CSR §6 Edge Cases, CSR-OD-8).

**Примечание о DIM.** DIM (draft) подтверждает границы: «Projections не
являются памятью» (Critical Boundaries §4) и «Conversations не создают память
автоматически» (§6) — session-only обработка по модели «purpose-limited
projection, session lifetime» соответствует DIM. DIM сам в статусе draft —
подтвердить применимость (Q7).

## 3. Статусы scopes (предложение)

**P2. Перевести `intent_understanding` и `provider_selection` из `proposed` в
`approved` для Phase 1.** Обоснование:

- Это условие activation gate Phase 1 (CSR §10.1) и release blocker SRC-01
  §10 п. 1 — без `approved` релиз заблокирован.
- Оба scope имеют authorization basis `service_necessity` и не требуют
  consent record для session use (CSR §5.1/§5.2, Consent requirement).
- Persistent memory технически отключена (CSR §10.1, UX-OD-003), поэтому
  dependent authorization на `preference_memory` для
  `context_mode: persistent` не активируется никогда — риск-контур минимален.
- Runtime authorization contract (CSR §6) fail-closed: отсутствие consent →
  deny; atomic deny на запрещённые категории.

**P3. `preference_memory` — Phase 2** (CSR §10.2): отдельный экран/момент
explicit consent, формулировки подтверждает Privacy Owner, плюс закрытие
CSR-OD-5. В Phase 1 никаких формулировок и обещаний памяти в UX.

**P4. Остальные четыре scope остаются `blocked`** — без изменений, они не
нужны Phase 1 (CSR §5.7, «Однозначно про первый релиз»).

## 4. Модель Transparency → Notice → Consent и notice-точки (предложение, без consent-экрана)

### 4.1. Трёхуровневая модель информирования (owner ruling 2026-07-29)

Owner ruling (2026-07-29): вместо двух уровней («информирование / согласие»)
вводятся **три уровня**: **Transparency → Notice → Consent**. Не каждое
информирование является Notice, и не каждый Notice требует Consent.

| Уровень | Определение | Примеры для Ayla Phase 1 (предложение) |
|---|---|---|
| **Transparency** | Пассивная доступность информации: пользователь может ознакомиться, система не обязана активно показывать в каждой точке | Политика конфиденциальности / полный текст обработки ПДн (ссылка «Подробнее»); описание «что Ayla умеет» и какие данные использует |
| **Notice** | Активное уведомление в точке обработки данных: пользователь явно информируется в момент обработки, клик-согласие не требуется | Welcome-строка уведомления об обработке ПДн (SCR-CUST-001, §4.3 п. 1); уведомление при сборе identity-данных в booking create (SCR-CUST-009, §4.3 п. 2) |
| **Consent** | Активное согласие (явное действие пользователя) | Только scope-требующие операции; в Phase 1 таких нет — первый Consent-момент: `preference_memory` в Phase 2 (P3) |

### 4.2. Реклассификация существующих notice-точек (предложение, не решение)

Оценка существующих точек по трёх уровням — **предложение, подтверждает
Privacy Owner (Q10)**:

- **Welcome-строка SCR-CUST-001** — остаётся **Notice**: активное уведомление
  в первой точке обработки диалога. Понижение до Transparency ослабит
  информирование в единственной гарантированной точке контакта.
- **Booking create SCR-CUST-009** — остаётся **Notice**: точка сбора
  identity-данных (имя, контакт) требует активного уведомления.
- **Полный текст политики / «что Ayla умеет»** — достаточно уровня
  **Transparency** (пассивная доступность по ссылке «Подробнее»); отдельной
  активной точки не требуется.
- **Consent-уровень в Phase 1 отсутствует** — все разрешённые процессы
  работают на `service_necessity`; первый Consent — Phase 2 (`preference_memory`).

### 4.3. Mandatory notice points

По UX-OD-003 экран согласия не создаётся; по 152-ФЗ-модели SRC-12 действует
soft-gate Variant A (диалог и booking без согласия допустимы). Предложение —
две обязательные точки уровня **Notice** (уведомление, не запрос согласия; в
терминах модели §4.1):

1. **Welcome (SCR-CUST-001).** Одна строка уведомления об обработке
   персональных данных в рамках диалога + ссылка на полный текст
   (progressive-disclosure, наследуем паттерн SRC-12 «Подробнее»). Не
   блокирует диалог. Важно: текст **не обещает память** — в Phase 1 она
   отключена, а старый копирайт SRC-12 («запомню твои предпочтения»)
   неприменим.
2. **Booking create (SCR-CUST-009).** Точка сбора identity-данных (имя,
   контакт) — короткое уведомление, что эти данные используются только для
   оформления записи.

Опционально (предложение, Q5): в registration-моменте старого флоу
(customer-booking-confirm) сохранить существующий `PERSONAL_DATA` consent,
если Privacy Owner решит Q1 в пользу сохранения baseline-слоя.

## 5. Пользовательские формулировки (проекты, по одной на точку)

> Draft для Privacy Owner; финальные тексты утверждает Privacy Owner.

**N1 — Welcome (SCR-CUST-001):**
«Я обрабатываю то, что ты пишешь, чтобы помочь с записью. Всё, что ты
сказываешь, живёт только в этом диалоге. Подробнее — [ссылка].»

**N2 — Booking create (SCR-CUST-009):**
«Имя и телефон нужны только для этой записи — мастер будет знать, кто
придёт. Никуда больше они не уходят.»

Обе формулировки: без юридического канцелярита, без обещания памяти, без
запроса согласия (notice, не consent). Кнопки «Даю согласие» в Phase 1 нет.

## 6. Граница Phase 1 / Phase 2 (export/forget)

AMD-020 C5 определяет export/forget для трёх included-классов
(UserPersonalContext, green MemoryEntry, ConsentRecord) — всё это persistent
контур. В Phase 1 persistent memory и consent records на память отсутствуют,
поэтому команды CSR §8 («Что Ayla знает обо мне», «Забыть это», отзыв scope)
не активируются. Достаточный минимум Phase 1 (предложение): booking-факты
живут в backend и подчиняются его retention; session data не переживает
сессию. Export/forget контракт становится обязательным с Phase 2 (Q8 —
подтвердить, что отсутствие команд §8 в Phase 1 допустимо).

## 7. Open questions (Privacy Owner / юрист)

1. **Baseline-слой 152-ФЗ.** Сохраняется ли `PERSONAL_DATA` как единый
   baseline-consent параллельно со scopes CSR, или Phase 1 строится только
   на service_necessity без consent record? (Определяет судьбу спек SRC-12.)
2. **Notice vs жёсткий гейт (с учётом трёх уровней).** Достаточно ли для
   Phase 1 уровней **Transparency + Notice** (§4.1–§4.3) без Consent-момента
   (без клика-согласия) для session-only + booking? Юрист по треку #947 может
   флипнуть Variant A→B (жёсткий гейт = Consent до первого ответа) —
   подтвердить, что для Phase 1 остаётся Variant A и Consent-уровень не
   вводится.
3. **Approval scopes.** Подтвердить перевод `intent_understanding` и
   `provider_selection` в `approved` (P2) — блокер SRC-01 §10 п. 1.
4. **Покрытие booking/notification.** Требуют ли `booking_execution` и
   `transactional_booking_support` регистрации отдельных scopes в CSR, или
   они покрываются service_necessity вне personalization-scopes (P: вне
   scopes, но зафиксировать явно)?
5. **Registration-момент.** Сохранять ли `PERSONAL_DATA` consent на
   экране customer-booking-confirm в Phase 1, если persistent memory там
   отключена? (Зависит от Q1; сейчас этот экран предлагает согласие на
   память, которой нет.)
6. **Маркетинг.** Подтвердить, что `MARKETING`/Marketing Opt-Out (DIM) не
   активируется в Phase 1 и не требует UX-точек.
7. **DIM status.** Data Inventory Matrix — draft; подтвердить, что её
   границы (§2) применимы к Phase 1 контракту до её approval.
8. **Команды CSR §8.** Допустимо ли, что команды просмотра/отзыва согласий
   отсутствуют в Phase 1 (нет granted scopes) и появляются только в Phase 2?
9. **Consent records SoR.** Если по Q1/Q5 consent record в Phase 1 всё же
   появится — где он хранится, пока CSR-OD-5 (canonical SoR) не закрыт?
10. **Классификация точек по уровням.** Подтвердить предложенную
    классификацию точек информирования по модели Transparency → Notice →
    Consent (§4.2): welcome (SCR-CUST-001) — Notice, booking create
    (SCR-CUST-009) — Notice, политика/«что Ayla умеет» — Transparency,
    Consent — только Phase 2. (Предложение UX, не решение.)

## 8. Acceptance criteria

Контракт считается принятым, когда Privacy Owner:

1. Ответил на Q1–Q10 (или явно делегировал/отложил с фиксацией).
2. Подтвердил или скорректировал P1–P4 (mapping, статусы scopes, notice
   points, Phase 2 boundary).
3. Утвердил или переписал формулировки N1/N2.
4. Подтвердил соответствие CSR §10.1 (Phase 1 gate): оба scope `approved`,
   persistent memory технически off.
5. После этого — перевод UX-OD-003 из `accepted_as_temporary_assumption`
   в окончательное решение (revalidation before release выполнена).

## 9. Что этот документ не делает

- Не меняет CSR, DIM, SRC-01 и спецификации экранов.
- Не вводит consent-экран, не трактует диалог как согласие.
- Не покрывает Phase 2 (`preference_memory` формулировки, export/forget
  enforcement) — только фиксирует границу.

## Changelog

- 2026-07-29 — UX-REFINE-001: добавлена трёхуровневая модель Transparency →
  Notice → Consent (§4.1, owner ruling 2026-07-29); реклассификация
  notice-точек как предложение (§4.2); notice-точки перенесены в §4.3 с
  привязкой к уровням; Q2 переформулирован с учётом трёх уровней; добавлен
  Q10 (подтверждение классификации точек); acceptance §8 обновлён (Q1–Q10).
  Основание: owner ruling 2026-07-29 (Privacy).
