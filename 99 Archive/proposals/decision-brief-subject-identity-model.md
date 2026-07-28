# Decision Brief — Subject Identity Model (AYLA-DEC-0016)

> **Статус:** готов к оформлению DEC после повторной проверки владельцем
> (owner review 2026-07-28 применён, v0.2). Не является решением до записи
> AYLA-DEC-0016 в [[Ayla Decision Log]]. Размещён в `99 Archive/proposals/`
> — validator-exempt, вне канонического дерева до approval.
> **Дата:** 2026-07-28 · **Автор:** Domain Architecture (подготовка) ·
> **Целевая запись:** AYLA-DEC-0016

## 1. Проблема и почему решение требуется сейчас

CDM v1.2.2 определяет `User` (§7.1) как «человека, взаимодействующего с
Ayla», но весь слой персональных данных оперирует `subject_id`: Consent (§7.2),
Context Fact, Inference, Recommendation (§7.11), Appointment (§7.12), Action
(§6.3). Сущность Subject в модели **не определена** — `subject_id` используется
без владельца, lifecycle и System of Record (§12 знает только строку
«User identity → Identity / Backend, proposal»). Account (учётная запись
входа) и Identity Reference (MAX / Telegram / phone / email) как объекты
отсутствуют: §7.1 держит `identity_refs` массивом-атрибутом внутри User.

Readiness-блок CDM §1 прямо называет identity foundation
(Subject/Tenant/Membership) **блокирующей областью** (§18, §22, §24). Параллельно
runtime уже принял решение за нас: handoff `c5_revision_2026-07-21.md`
(finding C, «заморожено») фиксирует «Subject удаления — person
(`ayla_user_id`), не per-tenant BotUser», а `c5_contract_draft_2026-07-23.md`
(строки 149, 307, 351) требует, чтобы export/delete охватывали все
per-tenant BotUser-строки человека во всех tenant'ах. Каноническая модель
отстаёт от эксплуатационного факта: сейчас person-уровень существует в коде,
но не имеет ни имени, ни инвариантов, ни SoR.

Цена отсрочки: любая смена телефона, повторная регистрация через другой
канал или удаление учётной записи сегодня имеет недетерминированный результат
для памяти и согласий — либо потерю истории человека, либо ошибочное
продолжение обработки после отзыва, либо (худший случай) склейку данных двух
разных людей под одним идентификатором. Все три исхода — прямые нарушения
Конституции (ст. XIV: разделение согласий; право исправлять и удалять —
строки 315–331).

## 2. Реальные сценарии

Из handoff-материалов (подтверждённые):

- **S1. Person-wide deletion (152-ФЗ).** Delete-запрос человека охватывает
  все его per-tenant строки во всех салонах: «человек = один ayla_user_id,
  BotUser per-tenant (all_tenants по ayla_user_id) — delete покрывает все
  tenant-строки» (`c5_revision_2026-07-21.md`, строки 47–48; заморожено как
  finding C). Tombstone-семантика и порядок каскада формализованы в
  `c5_contract_draft_2026-07-23.md` (строка 368).
- **S2. Cross-tenant personalization.** «Кросс-тенантная история —
  агрегировать "любимых" по всем салонам (сейчас preferred_master_id живёт в
  per-tenant ClientProfile; нужен кросс-тенантный источник — часть работы
  G2)» (`PersonalContext.txt`, строка 75). Персонализация «Твои мастера» на
  глобальном пути «конфликтует с гейтом согласия» (строки 18–23).
- **S3. Multi-tenant identity в runtime.** «Cross-tenant boundary: green
  reusable в рамках person, но не передаётся провайдерам»
  (`c5_contract_draft_2026-07-23.md`, строка 333) — память переиспользуется
  на уровне person, изолирована от tenant'ов.

Expected platform scenarios (по owner review 2026-07-28: подтверждённых
handoff-источников для смены телефона, cross-channel merge и удаления
channel account **нет**; сценарии поддерживаются архитектурно, без
приписывания provenance):

- **S4. Смена номера телефона** *(expected platform scenario)*. Человек
  меняет SIM; phone-reference должен быть перепривязан к тому же Subject без
  потери памяти и согласий и без захвата истории прежнего владельца номера.
- **S5. Два канала — один человек** *(expected platform scenario)*.
  Регистрация через MAX, затем через Telegram: возникают два Account/User,
  которые нужно слить в один Subject управляемой операцией merge.
- **S6. Удаление учётной записи канала** *(expected platform scenario)*.
  Пользователь отвязывает MAX-аккаунт, но юридически обязательные записи
  (история записей, платёжные события) сохраняются — инвариант 4 §7.1 CDM
  уже это требует, но без Account-объекта операцию не на что повесить.

## 3. Рассматриваемые варианты

### Вариант A — Унификация на `user_id` (статус-кво+)

`user_id` остаётся единственным идентификатором человека; каналы, телефоны и
логины — атрибуты User; `subject_id` объявляется синонимом `user_id`.

- **Плюсы:** нулевая миграция runtime (`ayla_user_id` уже играет эту роль);
  одна таблица, один FK-стиль; минимальные правки CDM.
- **Минусы:** смена телефона и merge двух учётных записей требуют
  перезаписи `user_id` во всех consent/memory/appointment-строках —
  разрушение audit trail и provenance (нарушение §3.11 Historical
  Consistency); удаление учётной записи канала неотличимо от удаления
  человека; S4–S6 не решаются; проблема отложена до первого инцидента, а
  CDM §1 уже признал область блокирующей.

### Вариант B — Разделённая identity-модель (рекомендуемый)

Пять сущностей с явными ролями:

- **Subject** — стабильный субъект персональных данных: владелец consent,
  memory, context. Никогда не переиспользуется, не перепривязывается.
- **User** — человек как участник бизнес-модели (клиент, мастер, владелец
  салона). В нормальном активном состоянии — не более одного active User на
  Subject.
- **Account** — учётная запись входа (сессии, аутентификация). 0..N на User.
- **Identity Reference** — верифицируемый внешний идентификатор:
  `max_user_id`, `telegram_user_id`, `phone`, `email`. 0..N на Account.
- **Provider Membership** — связь человека с tenant (детали — бриф
  AYLA-DEC-0017).

Связь: `Subject 1—0..1 User (active) 1—0..N Account 1—0..N Identity
Reference`. В нормальном активном состоянии один Subject имеет не более
одного active User, а один User принадлежит ровно одному Subject.
Исторические, merged и anonymized записи сохраняются и не обязаны
поддерживать физическую симметрию 1:1. Все ссылки на персональные данные
(`subject_id` в Consent, Context Fact, Inference, Recommendation,
Appointment, Action) указывают на Subject. `merge`, `relink`, `deletion` —
отдельные управляемые операции с audit events, а не побочные эффекты UPDATE.

- **Плюсы:** S1–S6 покрываются без перезаписи истории: relink меняет
  Identity Reference, merge создаёт redirect на surviving subject, deletion
  каскадируется по стабильному ключу (finding C ложится нативно).
  Совместимость с CSR (§7: consent = subject_id + tenant_id + scope_id) и
  AMD-020 (Semantic Memory → Memory & Identity Domain, deletion orchestrator
  W3) — оба документа уже оперируют именно субъектом, а не логином.
  Инвариант 3 §7.1 («User не равен Account, Specialist или Provider»)
  получает модель, в которой он выполним.
- **Минусы:** пять сущностей вместо одной; миграция существующих
  consent/memory-строк на формальный `subject_id`; расхождение с runtime
  (per-tenant BotUser + `ayla_user_id`) требует отдельного mapping audit;
  merge — операция с privacy-риском, запрещена до реализации consent
  resolver (§6).

### Вариант C — Промежуточный: Subject + Identity Reference, User ≡ Account

Выделяются только Subject и Identity Reference; учётная запись не отделяется
от бизнес-участника.

- **Плюсы:** дешевле B; решает S1, S2, S4.
- **Минусы:** S5 (merge двух каналов) и S6 (удаление учётки без удаления
  человека) не решаются — логин снова сшит с участником; через одну
  итерацию потребуется вариант B с повторной миграцией.

## 4. Рекомендуемый вариант и обоснование

**Вариант B**, с разделением MVP-среза и platform-scope по образцу
AYLA-DEC-0015:

- **MVP-active:** Subject, User, один Account-канал (MAX), Identity Reference
  (`max_user_id`, `phone`), управляемые операции `relink` (смена телефона) и
  person-wide `deletion` (S1 — уже эксплуатационный факт, требует канонической
  опоры).
- **Platform-scope / deferred:** merge двух Subjects — **запрещён до
  реализации consent resolver** (§6), то есть заведомо за пределами MVP;
  дополнительные каналы (email/telegram), multi-account UI, чтение
  cross-tenant personalization (S2 — post-pilot, зависит от G2 и consent
  gate, `PersonalContext.txt` строки 18–23).

Обоснование: вариант A откладывает признанную блокирующую область (CDM §1)
и делает ошибочный merge вопросом времени; вариант C покупает две миграции
вместо одной. Runtime уже живёт по модели B (finding C, all_tenants delete) —
канон догоняет эксплуатацию, а не изобретает новую.

## 5. Достоинства и риски рекомендуемого варианта

Достоинства: стабильный ключ для всех privacy-операций; audit trail не
перезаписывается; S4–S6 становятся штатными операциями; снятие блокера
identity foundation из CDM §1.

Риски и митигации:

- **R1. Ошибочный merge (склейка двух людей) — privacy-инцидент высшей
  категории.** Митигация (по owner ruling): merge инициирует только
  уполномоченная support/privacy-функция по подтверждённому запросу
  пользователя; владелец tenant **не может** инициировать или подтверждать
  merge; автоматический merge запрещён; до реализации consent resolver merge
  запрещён полностью; обязательный audit event `subject_merged` с actor и
  reason.
- **R2. Переиспользование номера телефона оператором.** relink по phone без
  верификации владения может отдать чужую историю. Митигация: Identity
  Reference имеет `pending_verification → verified` lifecycle; relink
  только для verified.
- **R3. Расхождение канона и runtime (BotUser per-tenant).** Митигация (по
  owner ruling): `ayla_user_id → subject_id` фиксируется как interim
  mapping, не финальная физическая модель; BotUser — interim runtime
  representation, содержащий часть данных Account, Identity Reference и
  tenant-local projection, и **не объявляется каноническим эквивалентом
  какой-либо одной сущности** до отдельного mapping audit.
- **R4. Миграция существующих строк.** Митигация: одноразовый backfill
  `subject_id := ayla_user_id` с проверкой целостности; окно миграции —
  до активации новых каналов.

## 6. Влияние на privacy, consent, memory и tenant isolation

- **Consent:** CSR §7 уже определяет effective-состояние как комбинацию
  `subject_id + tenant_id + scope_id` — модель B даёт `subject_id`
  формального владельца, CSR не меняется.
- **Consent при merge (owner ruling):** consent records **не сливаются и не
  переписываются**, сохраняют исходный `subject_id` для аудита. Для каждой
  комбинации `tenant_id + scope_id + policy version` вычисляется новое
  effective-состояние по правилам resolver: `granted + granted` → `granted`
  при совместимой policy version; `granted + revoked`, `granted + denied`,
  `granted + expired` → `needs_reconfirmation`. До реализации resolver merge
  запрещён.
- **Memory:** AMD-020 закрепляет Semantic Memory за Memory & Identity
  Domain, write authority — memory proposal flow, deletion orchestrator —
  W3 Privacy Flow. Subject становится ключом удаления: person-wide deletion
  (S1) — штатный каскад по `subject_id`, включая tombstone-семантику
  `c5_contract_draft`.
- **Deletion и retention (owner ruling):** person-wide deletion управляется
  retention manifest: юридически/договорно обязательные записи не удаляются
  автоматически, а минимизируются, обезличиваются или сохраняются на
  установленный срок с documented legal basis. Сам retention manifest —
  отдельный privacy/legal артефакт, не часть AYLA-DEC-0016.
- **Tenant isolation:** память переиспользуется в рамках Subject, но не
  передаётся провайдерам (`c5_contract_draft`, строка 333); tenant-роли
  доступа к индивидуальной памяти клиентов не получают (Конституция,
  строка 440). Модель B закрепляет это: Subject не принадлежит tenant'у,
  tenant-скоуп задаётся только связью Membership (бриф AYLA-DEC-0017) и
  consent-комбинацией `subject_id + tenant_id`.
- **Автономия:** разделение согласий (Конституция, ст. XIV) и право
  видеть/исправлять/удалять (строки 315–331) опираются на стабильного
  субъекта; при варианте A операции над «аккаунтом» неотличимы от операций
  над «человеком», что делает гранулярный отзыв невыразимым.

## 7. Влияние на существующие сущности и идентификаторы

- `User` (CDM §7.1): теряет массив `identity_refs` (выносится в Identity
  Reference); получает обязательную ссылку `subject_id`. Инварианты 1–4
  сохраняются, инвариант 3 становится проверяемым. Удаление или деактивация
  User **не каскадирует** в удаление Subject (симметрия 1:1 не требуется —
  §8).
- `subject_id` во всех потребителях (Consent, Context Fact, Inference,
  Recommendation, Appointment, Action): семантика не меняется, появляется
  формальный referent.
- `Specialist.user_id` (§7.8): перепривязывается к User (не к Subject) —
  разделение профиля и доступа детально в брифе AYLA-DEC-0017.
- Runtime `ayla_user_id`: interim mapping на `subject_id` (не финальная
  физическая модель, R3).
- Новые идентификаторы: `account_id`, `identity_ref_id`; `user_id`
  сохраняется как идентификатор User (не отменяется — исторические ссылки
  не переписываются).

## 8. Lifecycle предлагаемых сущностей

```text
Subject:            created → active → merged_into(subject_id) [terminal]
                                  ↘ anonymized [terminal, person-wide deletion]
User:               active → suspended → active | deactivated [terminal]
Account:            linked → unlinked → linked (re-auth) | closed [terminal]
Identity Reference: pending_verification → verified → unlinked [terminal]
```

Инварианты: (1) `merged_into` и `anonymized` — терминальные, повторный
`granted`-consent после них создаёт новый Subject; (2) unlinked Identity
Reference не переиспользуется для автоматической привязки без повторной
верификации; (3) deletion каскадируется от Subject, а не от Account;
(4) merge сохраняет redirect-запись для audit (stale `subject_id` резолвится
в surviving, но не перезаписывается в исторических записях); (5) в
нормальном активном состоянии Subject имеет не более одного active User;
исторические, merged и anonymized записи сохраняются и не обязаны
поддерживать физическую симметрию 1:1 — удаление User не каскадирует в
удаление Subject.

## 9. System of Record

| Объект | System of Record | Примечание |
|---|---|---|
| Subject | Memory & Identity Domain | владелец person-ключа; deletion orchestrator W3 (AMD-020) |
| User | Identity and Access (CAP-019) | заменяет строку «User identity → Identity / Backend» CDM §12 |
| Account | Identity and Access (CAP-019) | сессии и аутентификация |
| Identity Reference | Identity and Access (CAP-019) | верификация владения |
| Consent / Memory | без изменений | CSR / AMD-020 (Consent Management, Memory & Identity Domain) |

## 10. Migration impact

- **CDM (v1.3):** новые §7.x (Subject, Account, Identity Reference);
  переписанный §7.1 User; §12 — четыре строки SoR вместо одной; §13 —
  правило «stale subject_id резолвится, не перезаписывается»; закрытие
  identity-части §24.
- **Scope Contract:** CAP-019 Identity and Access переводится в MVP-active
  с ограниченным срезом (§4: один канал, relink, deletion; merge — deferred),
  по механике AYLA-DEC-0015 (ограниченный контур ≠ активация полной
  capability).
- **Domain Capability Registry:** маппинг User → CAP-019 из `proposal` в
  `confirmed`; добавить Subject, Account, Identity Reference в
  `owned_concepts` CAP-019.
- **AMD-020:** Ownership Summary дополняется строкой «Subject identity →
  Memory & Identity Domain (нормативный владелец), W3 (custodian)».
- **CSR:** без изменений.
- **Decision Log:** новая запись AYLA-DEC-0016 (формулировка §12).
- **Runtime (вне канона, для планирования):** backfill
  `subject_id := ayla_user_id` (interim mapping); отдельный mapping audit
  для BotUser (R3) — до него BotUser не приравнивается ни к одной
  канонической сущности.

## 11. Открытые вопросы владельцу

Закрыты owner review 2026-07-28:

- ~~Q2. Инициатор merge~~ → **закрыт:** только уполномоченная
  support/privacy-функция по подтверждённому запросу пользователя; владелец
  tenant не может инициировать или подтверждать merge (§12, п. 4).
- ~~Q3. Конфликт consent при merge~~ → **закрыт:** records не сливаются,
  сохраняют исходный `subject_id`; effective-состояние вычисляется resolver
  по `tenant_id + scope_id + policy version`; конфликты →
  `needs_reconfirmation`; до реализации resolver merge запрещён (§6, §12,
  п. 5).
- ~~Q4. Retention manifest~~ → **закрыт:** в DEC фиксируется только принцип
  (обязательные записи минимизируются/обезличиваются/хранятся на срок с
  documented legal basis); сам manifest — отдельный privacy/legal артефакт
  (§6, §12, п. 7).
- ~~Q6. Статус S4–S6~~ → **закрыт:** подтверждённых handoff-источников нет;
  сценарии остаются expected platform scenarios, поддерживаются
  архитектурно, без выдуманного provenance (§2).

Остаются открытыми:

- **Q1.** После реализации consent resolver: автоматический merge при
  совпадении verified phone запрещён полностью или допустим с последующим
  уведомлением и окном отмены? (В MVP merge запрещён в любом виде — §12,
  п. 4.)
- **Q5.** В какую волну AYLA-DEC-0014 входит канонизация identity foundation
  (блокер CDM §1)?

## 12. Предлагаемая формулировка owner ruling (AYLA-DEC-0016)

> **AYLA-DEC-0016 — Subject Identity Model**
>
> **Решение:**
>
> 1. Каноническая identity-модель состоит из пяти разделённых сущностей:
>    Subject (субъект персональных данных, consent и memory), User (человек
>    в бизнес-модели), Account (учётная запись входа), Identity Reference
>    (внешний идентификатор: MAX / Telegram / phone / email), Provider
>    Membership (связь человека с tenant, детали — AYLA-DEC-0017).
> 2. Кардинальность связей: в нормальном активном состоянии один Subject
>    имеет не более одного active User, а один User принадлежит ровно одному
>    Subject; User 1—0..N Account; Account 1—0..N Identity Reference.
>    Исторические, merged и anonymized записи сохраняются и не обязаны
>    поддерживать физическую симметрию 1:1; удаление или деактивация User не
>    каскадирует в удаление Subject. `subject_id` во всех доменных объектах
>    (Consent, Context Fact, Inference, Recommendation, Appointment, Action)
>    ссылается на Subject и никогда не перезаписывается в исторических
>    записях.
> 3. Унификация идентификаторов на `user_id` запрещена: `user_id`,
>    `subject_id`, `account_id`, `identity_ref_id` — раздельные
>    идентификаторы с раздельными System of Record.
> 4. Merge двух Subjects, relink Identity Reference и person-wide deletion —
>    отдельные управляемые операции с обязательными audit events
>    (`subject_merged`, `identity_ref_relinked`, `subject_anonymized`),
>    actor и reason. Автоматический merge запрещён. Merge инициирует только
>    уполномоченная support/privacy-функция по подтверждённому запросу
>    пользователя; владелец tenant не может инициировать или подтверждать
>    merge. До реализации consent resolver (п. 5) merge запрещён.
> 5. Consent при merge: consent records не сливаются и не переписываются,
>    сохраняют исходный `subject_id` для аудита. Для каждой комбинации
>    `tenant_id + scope_id + policy version` вычисляется новое
>    effective-состояние: `granted + granted` → `granted` при совместимой
>    policy version; `granted + revoked`, `granted + denied`,
>    `granted + expired` → `needs_reconfirmation`.
> 6. Relink Identity Reference допустим только для reference в состоянии
>    `verified`.
> 7. Person-wide deletion управляется retention manifest: юридически или
>    договорно обязательные записи не удаляются автоматически, а
>    минимизируются, обезличиваются или сохраняются на установленный срок с
>    documented legal basis. Retention manifest — отдельный privacy/legal
>    артефакт и не является частью настоящего решения.
> 8. MVP-срез: Subject, User, один Account-канал (MAX), Identity Reference
>    (`max_user_id`, `phone`), операции relink и person-wide deletion.
>    Merge (п. 4), дополнительные каналы, multi-account UI и чтение
>    cross-tenant personalization — deferred (platform-scope), активация
>    только через Scope Contract §11.
> 9. Маппинг `ayla_user_id → subject_id` признаётся interim mapping, а не
>    финальной физической моделью. BotUser является interim runtime
>    representation, содержащим часть данных Account, Identity Reference и
>    tenant-local projection; BotUser не объявляется каноническим
>    эквивалентом какой-либо одной сущности до отдельного mapping audit.
>    Немедленного рефакторинга runtime настоящее решение не требует.
> 10. System of Record: Subject → Memory & Identity Domain; User, Account,
>     Identity Reference → Identity and Access (CAP-019). Consent и Memory
>     SoR не изменяются.
> 11. CDM v1.3 вносит сущности п. 1, кардинальность п. 2, lifecycle §8
>     брифа и строки SoR п. 10; область identity foundation снимается из
>     блокирующих (CDM §1) после публикации v1.3.
>
> **Основание:** CDM v1.2.2 оперирует `subject_id` без определённого
> субъекта (§7.2, §7.11, §7.12) при признанной блокирующей области identity
> foundation (§1). Runtime уже реализует person-уровень (`c5_revision`
> finding C: subject = person, не per-tenant BotUser; person-wide delete по
> всем tenant'ам), канон отстаёт от эксплуатации. Унификация на `user_id`
> делает смену телефона, merge и удаление учётной записи разрушающими
> операциями над audit trail и откладывает признанный блокер. Безусловная
> симметрия Subject↔User 1:1 отклонена: она делает удаление User каскадным
> для Subject и несовместимой с сохранением merged/anonymized записей.
>
> **Затрагивает:** Ayla Core Domain Model Specification (§7.1, новые §7.x,
> §12, §13, §24); Ayla MVP Scope and Release Contract (CAP-019 → MVP-active,
> ограниченный срез); Ayla Domain Capability Registry (маппинг и
> `owned_concepts` CAP-019); AMD-020 Pilot Scope Registry (строка Subject
> identity в Ownership Summary). Consent Scope Registry не изменяется.
> Retention manifest оформляется отдельным privacy/legal артефактом.

## Change Log

- **v0.1 — 2026-07-28** — первичная версия брифа (12 разделов, рекомендация:
  вариант B).
- **v0.2 — 2026-07-28** — owner review applied: (1) кардинальность
  Subject–User — «не более одного active User», исторические/merged/
  anonymized записи без физической симметрии 1:1, удаление User не
  каскадирует в Subject; (2) BotUser — interim runtime representation
  (Account + Identity Reference + tenant-local projection), не канонический
  эквивалент до mapping audit; `ayla_user_id → subject_id` — interim
  mapping; (3) consent при merge — records не сливаются, resolver с
  `needs_reconfirmation`, merge запрещён до реализации resolver; (4)
  инициатор merge — только support/privacy-функция, tenant owner исключён;
  (5) retention manifest — только принцип, отдельный privacy/legal артефакт;
  (6) S4–S6 — expected platform scenarios без подтверждённого provenance.
  Q2, Q3, Q4, Q6 закрыты. Статус: готов к оформлению DEC после повторной
  проверки владельцем.
