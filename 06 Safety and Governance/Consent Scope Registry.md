---
node_id: ayla.governance.consent-scope-registry
title: Consent Scope Registry
type: specification
status: draft
version: "0.5"
owner: User Context Domain Owner / Privacy Owner
priority: P0
knowledge_area:
  - safety-governance
domain:
  - consent
  - user-context
system_owner:
  - ayla-knowledge
concerns:
  - privacy
  - governance
  - audit
created: 2026-07-27
updated: 2026-07-27
source_kind: canonical
source_repository: ayla-knowledge
classification: internal
data_sensitivity: high
data_categories:
  - pii
security_sensitivity: high
ai_indexing: metadata-only
export_policy: metadata-only
review_cycle: before-major-change
depends_on:
  - "[[Ayla Constitution]]"
  - "[[ADR-0012 Dynamic User Model]]"
related:
  - "[[Killer PRD]]"
  - "[[AMD-020 Pilot Scope Registry]]"
  - "[[Data Inventory Matrix]]"
target_milestone: MVP vertical slice and Killer PRD canonization
blocking_reason: >
  Persistent user context and cross-session personalization must remain
  fail-closed until the applicable scope is approved and enforced at runtime.
---

# Consent Scope Registry

## 1. Назначение

Consent Scope Registry — нормативный реестр целей использования
пользовательского контекста в Ayla.

Для каждого scope он определяет:

- для какой цели разрешено использовать данные;
- какие категории данных допустимы;
- какие компоненты могут быть consumers;
- какие операции разрешены и запрещены;
- какое согласие или иное утверждённое основание требуется;
- как действует отзыв;
- какие audit events обязательны.

Registry отвечает на вопрос **«разрешено ли использовать эти данные этим
компонентом для этой цели?»**.

Он не определяет физическое владение данными, место хранения или source of
truth. Эти вопросы регулируются [[AMD-020 Pilot Scope Registry]],
[[Data Inventory Matrix]] и профильными domain contracts.

## 2. Нормативные правила

1. Любое использование persistent user context должно быть связано с
   зарегистрированным `scope_id`.
2. Неизвестный, отсутствующий, просроченный или неутверждённый scope
   обрабатывается по правилу **fail-closed**.
3. Разрешение для одной цели не распространяется автоматически на другую.
4. Разрешение на чтение не означает разрешение на запись, вывод нового факта,
   передачу модели или аналитическое использование.
5. Sensitive inference запрещён, если он явно не разрешён отдельным
   утверждённым scope.
6. Отзыв согласия прекращает новое использование scope и запускает указанное
   `revocation_effect`.
7. Runtime-компоненты не могут расширять категории данных, consumers или
   операции локальной конфигурацией.
8. В prompt или model context передаются только данные, разрешённые активным
   scope и необходимые для конкретного запроса.
9. Документ задаёт продуктовые и архитектурные ограничения, но не заменяет
   обязательное Privacy/Legal заключение.

## 3. Термины

| Термин | Значение |
|---|---|
| `scope_id` | Стабильный машинный идентификатор цели использования |
| `scope_version` | Версия конкретного scope — независима от `registry_version` документа в целом; scope может не меняться при редакторских правках Registry |
| `data_category` | Нормативный класс пользовательских данных |
| `consumer` | Система-потребитель данных (`ai-bot-platform`, `ayla-ai-core`, `beautygo_backend`) — не runtime-модуль внутри неё |
| `consumer_component` | Опциональный уточняющий модуль внутри consumer-системы (например, `recommendation-composer`) — информативное поле, не влияет на authorization decision в MVP |
| `operation` | Действие над данными: `read`, `write`, `delete`, `derive`, `model_transfer`, `user_disclosure`, `measure` |
| `authorization_basis` | Правовое/продуктовое основание использования: `explicit_consent` \| `service_necessity` \| `legal_obligation` \| `approved_legitimate_interest` \| `system_operation` — отдельно от факта наличия consent record. `system_operation` — для внутренних технических операций (например, memory cleanup по истечении retention), которые не требуют consent, так как не используют данные в целях персонализации |
| `session_context` | Контекст, живущий только в пределах текущей сессии |
| `persistent_context` | Контекст, доступный между сессиями |
| `revocation_effect` | Обязательное поведение системы после отзыва |
| `fail-closed` | Запрет использования при отсутствии подтверждённого разрешения |
| `mvp_status` | Машиночитаемый статус scope: `draft` \| `proposed` \| `approved` \| `blocked` \| `deprecated`; причина блокировки — в отдельном поле `blocking_reason`, не внутри значения статуса |

**Запрещены wildcard scopes.** Значения вида `all_personalization`,
`all_context`, `*` не допускаются ни для одного `scope_id` — каждый scope
должен иметь конкретный, ограниченный purpose (purpose limitation).

**Разграничение session use и persistent consent.** Обработка текущего
сообщения пользователя в рамках текущей сессии не требует отдельного
consent — пользователь, отправивший сообщение, уже разрешил его
обработать для ответа. Отдельное согласие требуется не на понимание
сообщения, а на: долговременное сохранение; повторное использование в
будущих сессиях; проактивное использование; передачу для другой цели.
Это правило — центральное для того, чтобы consent UX не стал избыточным
(см. §5.1/5.2 `Consent requirement`, где текущий запрос не требует
согласия, а persistence — требует).

## 4. Зарегистрированные категории данных MVP

| `data_category` | Описание | Чувствительность | Persistent storage | Owner |
|---|---|---:|---|---|
| `explicit_goal` | Явно сформулированная цель пользователя | medium | Разрешается только по scope | Не определён в AMD-020 Ownership Summary — открытый вопрос |
| `service_preference` | Предпочтения по услугам и процедурам | medium | Разрешается только по scope | User Context Domain (по аналогии с Account/Profile, AMD-020) |
| `provider_preference` | Предпочтения по специалисту, полу, формату и другим параметрам выбора | medium | Разрешается только по scope | User Context Domain (по аналогии с Account/Profile, AMD-020) |
| `booking_history` | Факты записей и их статусы из backend source of truth | medium | Backend является source of truth | Booking Domain — не в Ownership Summary AMD-020 явно, открытый вопрос |
| `interaction_history` | Факты взаимодействия с рекомендациями и диалогом | medium | Ограниченно, по scope | Не определён в AMD-020 — открытый вопрос |
| `recommendation_feedback` | Принятие, отказ и указанная причина отказа | medium | Разрешается по scope | Recommendation Owner (по аналогии с scope owner §5.6) |
| `session_signal` | Сигнал, применимый только к текущей сессии | low–medium | По умолчанию не сохраняется | Не применимо — не persistent, владелец не требуется |
| `inferred_signal` | Выведенное системой предположение, не сообщённое пользователем явно | high | Запрещено по умолчанию | Memory & Identity Domain (AMD-020: Semantic Memory) |
| `health_related_signal` | Сведения или выводы о здоровье, диагнозах, симптомах и противопоказаниях | special/high | Вне MVP; запрещено | Wellness Domain (AMD-020: Raw Wellness History) |
| `religious_or_diet_signal` | Религиозные убеждения или чувствительные диетические признаки | special/high | Заблокировано до Legal ruling | User Context Domain, под OD-1 — не окончательно |

**Честно про пробелы:** для `explicit_goal`, `booking_history`,
`interaction_history` нет прямого соответствия в Ownership Summary
AMD-020 — не придумываю владельца, оставляю как открытый вопрос до
уточнения у Product Architecture / User Context Domain Owner.

## 4.1 Data Category Mapping

> **Провизорно, до Data Inventory Matrix.** Правильная цепочка владения —
> `physical field → data_category` должна принадлежать Data Inventory
> Matrix (сейчас не существует в проекте), а этот Registry должен зависеть
> только от стабильного `data_category`, не от конкретных имён полей.
> Пока Data Inventory Matrix не материализована, таблица ниже временно
> берёт на себя эту функцию — при появлении Matrix маппинг переносится
> туда, а здесь остаётся только список `data_category`.

Сопоставление `data_category` с реальными полями. **Только поля,
подтверждённые в ADR-0012 §N (полевой каталог) — остальное оставлено как
открытый вопрос, а не придумано по аналогии.**

| `data_category` | Поля (источник: ADR-0012) | Zone (ADR-0011, через цитату ADR-0012) |
|---|---|---|
| `service_preference` | `preferred_districts`, `workplace_district`, `home_district`, `preferred_time_slots`, `busy_days`, `price_range_min/max` | `green` по контракту |
| `provider_preference` | `prefers_flexible_cancellation`, `favorite_masters`, `min_rating_preference` | `green` по контракту |
| `religious_or_diet_signal` | `diet_type` | Спорно — контракт: `green`; ADR-0011 §4.2 (по цитате ADR-0012): `yellow` для vegan/keto/allergies; halal/kosher — под OD-1, требует Legal ruling |
| `health_related_signal` | `skin_sensitivities` | Спорно — контракт: `green`; ADR-0011 §4.2: `yellow`; под OD-1 |

**Открытый вопрос (не выдумано, честно не хватает источника):** `explicit_goal`,
`booking_history`, `interaction_history`, `recommendation_feedback`,
`session_signal`, `inferred_signal` — для этих категорий нет точного
маппинга на существующие поля ADR-0012. Требуется либо расширение
полевого каталога ADR-0012, либо отдельный источник (например, event
schema `ai-bot-platform`), прежде чем runtime authorization layer сможет
проверять их по имени поля, а не только по названию категории.

## 5. Реестр scopes MVP

### 5.1. `intent_understanding`

| Поле | Значение |
|---|---|
| Scope version | `1.0` (независима от `registry_version` документа) |
| Purpose | Понять текущий запрос и определить необходимое продолжение диалога |
| Allowed data | `explicit_goal`, `service_preference`, `provider_preference`, `session_signal` |
| Consumers | `ai-bot-platform`, `ayla-ai-core` |
| Allowed operations | `read`, `model_transfer` (только для текущего запроса; persistence — вне этого scope, см. §5.7 `preference_memory`) |
| Persistent context | **Не разрешена этим scope.** Чтение persistent context для intent understanding требует отдельного активного consent на `preference_memory` (§5.7) |
| Prohibited | `write`/`delete` (сохранение — не purpose этого scope); `inferred_signal` persistence; health/religious inference; использование для рекламы |
| Authorization basis | `service_necessity` — обработка текущего сообщения не требует отдельного consent record (см. §3 «Разграничение session use и persistent consent») |
| Consent requirement | Не требуется для текущего запроса (session use) |
| Validity | Текущая сессия |
| Revocation effect | Не применимо — scope не создаёт persistent state |
| Audit events | `consent_scope_checked`, `context_read_allowed`, `context_read_denied` |
| Scope owner | User Context Domain Owner + Privacy Owner |
| MVP status | `proposed` |
| Blocking reason | — |

### 5.2. `provider_selection`

| Поле | Значение |
|---|---|
| Scope version | `1.0` |
| Purpose | Подобрать подходящего специалиста или вариант услуги, используя уже доступный контекст |
| Allowed data | `explicit_goal`, `service_preference`, `provider_preference`, `booking_history`, `recommendation_feedback` |
| Consumers | `ai-bot-platform`, `ayla-ai-core` |
| Data source (не consumer) | `beautygo_backend` — источник `booking_history`/availability, не consumer этого scope. Backend не читает persistent preference data через этот контракт; он предоставляет booking-факты как исходные данные (см. §11.4 для разграничения data provider / data consumer) |
| Allowed operations | `read`, `model_transfer` |
| Persistent context | Чтение уже сохранённых предпочтений разрешено при активном `preference_memory` consent (§5.7); этот scope **не создаёт** persistent state сам по себе |
| Prohibited | `write`/`delete` (см. §5.7); экономически мотивированное ранжирование; sensitive inference; передача лишних идентификаторов модели |
| Authorization basis | `service_necessity` для обработки текущего запроса; чтение persistent preferences зависит от `preference_memory` |
| Consent requirement | Не требуется для подбора по текущему запросу; persistent preferences — через `preference_memory` |
| Validity | Текущая сессия для базового сценария |
| Revocation effect | Не применимо на уровне этого scope — отзыв persistent preferences регулируется `preference_memory` |
| Audit events | `consent_scope_checked`, `memory_fact_used`, `candidate_selection_completed` |
| Scope owner | User Context Domain Owner + Privacy Owner |
| MVP status | `proposed` |
| Blocking reason | — |

### 5.3. `proactive_recommendation`

| Поле | Значение |
|---|---|
| Scope version | `1.0` |
| Purpose | Инициировать полезную рекомендацию без прямого запроса в текущем сообщении |
| Allowed data | `explicit_goal`, `service_preference`, `provider_preference`, `booking_history`, `interaction_history`, `recommendation_feedback` |
| Consumers | `ai-bot-platform`, `ayla-ai-core` |
| Allowed operations | `read`, `model_transfer` |
| Persistent context | Обязательна; зависит от активного `preference_memory` consent |
| Prohibited | Proactive use без отдельного согласия; health/religious inference; скрытое коммерческое продвижение |
| Authorization basis | `explicit_consent` — обязателен, session use здесь неприменим по определению scope |
| Consent requirement | Отдельное явное согласие на proactive personalization |
| Validity | До отзыва; повторное согласие при MAJOR-изменении scope (§7) |
| Revocation effect | Немедленно прекратить proactive recommendations; сохранить возможность обычного ответа на прямой запрос |
| Audit events | `consent_scope_checked`, `proactive_trigger_evaluated`, `proactive_recommendation_shown` |
| Scope owner | Product Owner + User Context Domain Owner + Privacy Owner |
| MVP status | `blocked` |
| Blocking reason | Privacy/Legal approval required |

### 5.4. `cross_domain_personalization`

| Поле | Значение |
|---|---|
| Scope version | не применяется до утверждения |
| Purpose | Использовать контекст одного домена для персонализации в другом домене |
| Allowed data | Только явно перечисленные категории после отдельного amendment |
| Consumers | Не утверждены |
| Allowed operations | Нет для MVP |
| Persistent context | Требуется |
| Prohibited | Любой cross-domain перенос по неявному сходству или inferred signal |
| Authorization basis | `explicit_consent`, отдельно по паре доменов |
| Consent requirement | Отдельное гранулярное согласие по паре source-domain → target-domain |
| Validity | Не применяется до утверждения |
| Revocation effect | Запрет всех новых cross-domain reads; последующая обработка определяется retention policy |
| Audit events | `cross_domain_access_denied` |
| Scope owner | Privacy Owner + владельцы обоих доменов |
| MVP status | `blocked` |
| Blocking reason | Cross-domain consent model не утверждена (CSR-OD-3) |

### 5.5. `recommendation_explanation`

| Поле | Значение |
|---|---|
| Scope version | `1.0` |
| Purpose | Объяснить пользователю, почему была предложена конкретная рекомендация |
| Allowed data | Только факты, фактически использованные при формировании рекомендации и разрешённые исходным scope |
| Consumers | `ai-bot-platform`, `ayla-ai-core` |
| Allowed operations | `read`, `model_transfer`, `user_disclosure` |
| Persistent context | Наследует ограничения исходного recommendation scope |
| Prohibited | Раскрытие внутренних score, скрытых коммерческих факторов, данных третьих лиц или запрещённых inference |
| Authorization basis | То же основание, что у исходной рекомендации (наследуется, не проверяется заново как отдельный consent) |
| Consent requirement | То же основание, что у исходной рекомендации |
| Validity | Пока доступна recommendation evidence |
| Revocation effect | Не использовать отозванные persistent facts в новых объяснениях |
| Audit events | `recommendation_explanation_requested`, `recommendation_explanation_rendered` |
| Scope owner | Recommendation Owner + Privacy Owner |
| MVP status | `proposed` |
| Blocking reason | — |

### 5.6. `recommendation_measurement`

| Поле | Значение |
|---|---|
| Scope version | `1.0` |
| Purpose | Измерять показ, принятие, отказ, запись и attribution результата рекомендации |
| Allowed data | `interaction_history`, `recommendation_feedback`, идентификаторы recommendation/booking linkage |
| Consumers | `ai-bot-platform`, `beautygo_backend`, analytics pipeline |
| Allowed operations | `write`, `read`, `measure` |
| Persistent context | Не требует semantic memory; события хранятся по отдельной retention policy |
| Prohibited | Использование event data для новых персональных inference без отдельного scope |
| Authorization basis | `approved_legitimate_interest`, reference: `CSR-OD-1` — **не пользовательский consent**; продуктовая аналитика имеет собственное правовое основание, отдельное от personalization consent. Персонализация из этих данных (если появится) потребует `explicit_consent` отдельным scope |
| Consent requirement | Не требует consent record для базового измерения; персонализация из этих данных — отдельный consent |
| Validity | Согласно Analytics Retention Policy |
| Revocation effect | Прекратить персонализированное использование; удаление/обезличивание — согласно утверждённой policy |
| Audit events | `recommendation_created`, `recommendation_shown`, `recommendation_accepted`, `recommendation_dismissed`, `booking_linked` |
| Scope owner | Analytics Owner + Privacy Owner |
| MVP status | `blocked` |
| Blocking reason | CSR-OD-1 не решён — Legal basis для measurement retention не утверждён |

### 5.7. `preference_memory`

**Новый scope (v0.4).** Разделяет использование предпочтений при подборе
(§5.1, §5.2 — только `read`) от их сохранения для будущей персонализации
(`write`). Один и тот же `scope_id` не может одновременно разрешать
«использовать для текущего подбора» и «сохранить для будущего» — это два
разных purpose с разным уровнем риска.

| Поле | Значение |
|---|---|
| Scope version | `1.0` |
| Purpose | Сохранять явно подтверждённые предпочтения пользователя для будущей персонализации |
| Allowed data | `service_preference`, `provider_preference` |
| Consumers | `ai-bot-platform`, `ayla-ai-core` |
| Allowed operations | `write`, `read`, `delete` |
| Persistent context | Это единственный scope, создающий persistent context для предпочтений |
| Prohibited | `inferred_signal`; `health_related_signal`; `religious_or_diet_signal` — запись только явно подтверждённых, не выведенных фактов |
| Authorization basis | `explicit_consent` — обязателен для любой `write`-операции |
| Consent requirement | Отдельное явное согласие; без него — данные не сохраняются, только session-only обработка через §5.1/§5.2 |
| Validity | До отзыва или MAJOR-изменения scope (§7) |
| Revocation effect | Прекратить использование сохранённых предпочтений в `provider_selection`/`intent_understanding`; данные помечаются `revoked`, не обязательно удаляются немедленно (retention policy) |
| Audit events | `consent_scope_checked`, `memory_fact_written`, `memory_fact_used`, `memory_fact_deleted` |
| Scope owner | User Context Domain Owner + Privacy Owner |
| MVP status | `proposed` |
| Blocking reason | — |

**Это один из трёх scopes, реально необходимых для MVP** (наряду с
`intent_understanding` и `provider_selection` в их read-only форме выше) —
остальные четыре (`proactive_recommendation`, `cross_domain_personalization`,
`recommendation_explanation`, `recommendation_measurement`) могут
оставаться `blocked`/`proposed` без остановки запуска session-only +
opt-in-persistence MVP.

## 6. Runtime authorization contract

`registry_version` (версия документа) и `scope_version` (версия конкретного
scope, §5) — разные оси; запрос ссылается на `scope_version` того scope,
который запрашивается, а не на версию всего документа.

Каждый запрос к persistent user context должен содержать:

```yaml
scope_id: provider_selection
scope_version: "1.0"              # версия scope (§5.2), не registry_version документа
registry_version: "0.4"           # версия этого документа на момент запроса, информативно
subject_id: "<user-id>"
tenant_id: "<tenant-id>"
consumer: ai-bot-platform          # системный идентификатор — только из списка Consumers scope (§5)
consumer_component: "recommendation-composer"   # опционально, информативно; не влияет на decision в MVP
operation: read
requested_data_categories:
  - provider_preference
  - booking_history
purpose_context:
  conversation_id: "<conversation-id>"
  recommendation_id: "<optional-recommendation-id>"
```

Минимальный ответ authorization layer. **Правило для MVP — atomic deny**:
если хотя бы одна запрошенная категория не разрешена, весь запрос
отклоняется целиком; partial read не поддерживается (нет
`partial_allow` в MVP — это сознательное упрощение ради безопасности и
простоты, не пропуск):

```yaml
decision: allow | deny
reason:
  - active_consent
  - session_only
  - consent_missing
  - consent_revoked
  - scope_unknown
  - scope_blocked
  - consumer_not_allowed
  - operation_not_allowed
  - data_category_not_allowed
  - tenant_mismatch
  - scope_version_mismatch
scope_version: "1.0"               # версия scope, на который получен ответ
registry_version: "0.4"            # версия документа на момент decision, для аудита эволюции контракта
allowed_data_categories: []        # при decision=allow — полный список запрошенных категорий; при deny — всегда []
decision_id: "<audit-id>"
```

Если consumer нуждается только в части категорий — он должен явно
сформировать новый запрос с уменьшённым `requested_data_categories`, а не
полагаться на partial allow.

### Enforcement ownership

| Ответственность | Owner |
|---|---|
| Source of consent facts | User Context / consent service |
| Runtime consent check | `ai-bot-platform` на retrieval boundary |
| Повторная защита при rendering | `ayla-ai-core` |
| Source data access control | Owning backend/domain service |
| Audit decision event | Компонент, выполнивший gate |
| Canonical policy | Этот Registry в `ayla-knowledge` |

Ни один отдельный runtime-компонент не считается единственной защитой. Backend,
platform и core применяют defence in depth в пределах своей ответственности.

### Edge Cases and Error Handling

**Запрос запрещённой категории данных.** Если `requested_data_categories`
содержит хотя бы одну категорию, не разрешённую scope: **весь запрос
отклоняется целиком** — `decision: deny`, `reason: data_category_not_allowed`;
audit event `context_read_denied` с указанием запрещённой категории.
Partial read (частичная выдача только разрешённых категорий в одном
ответе) не поддерживается в MVP — consumer, которому нужна только часть
категорий, должен явно повторить запрос с уменьшённым набором.

**Cross-tenant запрос.** Если `tenant_id` в запросе не совпадает с
`tenant_id` записи: `decision: deny`, `reason: tenant_mismatch`; audit event
`cross_tenant_access_denied`. **Global user scope (`tenant_id=null`) для
MVP — `blocked`**, не разрешён ни для одной категории: не определены
владелец cross-tenant authorization, правила отделения глобальной памяти
от tenant-owned фактов, и кто устанавливает `tenant_id=null`. Требует
отдельного identity/tenancy контракта до активации.

**Устаревший `scope_version`.** Пока `CSR-OD-6` (совместимость между
MINOR-версиями) не решён — **автоматическая совместимость не
предполагается**: любое изменение scope, затрагивающее purpose, data
categories, consumers, operations или authorization basis, требует
Privacy review, независимо от того, MINOR оно или MAJOR по формальной
нумерации. Текст ниже в §7 «Scope Version Migration» — design candidate,
не действующая норма, пока `CSR-OD-6` открыт.

**Истёкший consent, актуальная запись.** Если `consent.expires_at < now()`,
но запись существует: `decision: deny`, `reason: consent_expired`; запись
не удаляется автоматически (retention policy); consumer не получает
данные; запрос на продление consent — при следующем релевантном
взаимодействии.

**Отсутствие consent record.** `decision: deny`, `reason: consent_missing`
— fail-closed: отсутствие consent не интерпретируется как согласие.
Consumer получает только session-only данные, если это разрешено scope.

### Integration with Recommendation Composer (Killer PRD §5.1)

> **Informative, не нормативный раздел.** Описывает, как Killer PRD
> потребляет контракт §6 — нормативна только сама §6. Изменения в Killer
> PRD не требуют синхронной правки этого раздела построчно, только
> сверки при следующем ревью. (См. также open question о разнесении
> интеграционных описаний по owning-документам — конец файла.)

Composer вызывает этот контракт на этапе 1 (Consent / privacy gate),
дословно определённом в Killer PRD: «сохранена ли требуемая память в
рамках `consent_scope`, охватывающего данную цель? Совместима ли
sensitivity zone с этой рекомендацией?» — обе проверки выполняются на
одном этапе, не последовательно.

```yaml
# Уровень спецификации, не реализация (см. Killer PRD §5.1)

determine_scope(intent):
  booking    → scope_id: provider_selection      # read-only, §5.2
  proactive  → scope_id: proactive_recommendation   # MVP status: blocked (§5.3) — decision: deny до Privacy/Legal approval
  other      → scope_id: intent_understanding    # read-only, §5.1

gate_1_consent_privacy(candidate, intent):
  scope_id ← determine_scope(intent)
  required_categories ← категории для candidate (см. §4.1 Data Category Mapping)

  auth_response ← authorization_layer.check(          # контракт §6 выше
    scope_id, scope_version, subject_id,
    consumer="ai-bot-platform", consumer_component="recommendation-composer",
    operation="read", requested_data_categories=required_categories)

  zone_check ← sensitivity_zone(required_categories) совместим с candidate?  # ADR-0011/ADR-0012, см. §11 ниже

  if auth_response.decision == deny OR zone_check == incompatible:
    → session-only fallback ИЛИ явный запрос разрешения пользователю   # Killer PRD §5.1: оба пути, не один
  else:
    → продолжить к этапу 2 (Safety gate) с auth_response.allowed_data_categories
```

Рабочий пример из Killer PRD §5.2: рекомендация на основе inferred
пищевого предпочтения без consent для `proactive_recommendation` →
исключена, память не используется.

### Integration with Proactive Readiness Gate (Journey Specification)

> **Informative, не нормативный раздел** (см. пометку выше).

**Уточнение, не независимая двойная проверка.** Journey Specification уже
включает `proactivity_consent_missing` как один из шести suppression-факторов
внутри самой таблицы Proactive Readiness Gate — согласие не проверяется
отдельным параллельным гейтом, оно частично встроено в Readiness Gate.

Явное сопоставление:

| Readiness Gate фактор (Journey) | Соответствие в этом Registry |
|---|---|
| `proactivity_consent_missing` | Нет активного `granted` consent для scope `proactive_recommendation` (§5.3) |

Остальные suppression-факторы (`explicit_do_not_disturb`,
`topic_cooldown_active`, `high_workload_context`, `quiet_hours`,
`low_relevance`) — вне области этого Registry, регулируются Journey
Specification независимо.

**Правило:** оба источника блокировки должны быть чисты для проактивного
действия — `proactivity_consent_missing=false` (этот Registry) и остальные
пять факторов не активны (Journey) — но это не два отдельных «allow/deny»
ответа от двух систем, а одна логическая проверка, распределённая между
двумя документами. При материализации Readiness Gate (пока `proposed`)
нужно явно решить, какой компонент физически хранит и проверяет
`proactivity_consent_missing` — этот Registry или Journey-слой.

### Integration with Memory Proposal Flow (ADR-0012 N-02)

> **Informative, не нормативный раздел** (см. пометку выше).

ADR-0012 N-02 (Proposal-first) определяет поток: Signal/Explicit → Proposal
→ Sensitivity+Purpose Check → Consent Check → Persistent / Session only.
Purpose Check на этом потоке — это определение `scope_id` для proposal.

**Исправлено относительно предыдущей версии:** запись (`operation="write"`)
не может идти через `provider_selection`/`intent_understanding` — они
разрешают только `read` (§5.1, §5.2). Любой persistent write адресуется
scope `preference_memory` (§5.7).

```yaml
# Уровень спецификации (ADR-0012 N-02), не реализация

purpose_check(proposal):
  if proposal подразумевает persistence (write):
    scope_id ← preference_memory                 # §5.7 — единственный scope с write
  elif proposal.context == "proactive":
    scope_id ← proactive_recommendation           # §5.3 — read, blocked до Privacy/Legal
  else:
    scope_id ← intent_understanding               # §5.1 — read, session use
  if scope_id не зарегистрирован в §5 → отклонить proposal с ошибкой конфигурации
  proposal.consent_scope ← scope_id

consent_check(proposal):
  auth_response ← authorization_layer.check(         # контракт §6
    scope_id=proposal.consent_scope, scope_version,
    subject_id=proposal.user_id,
    consumer="ai-bot-platform", consumer_component="user-context-write",
    operation="write" if proposal.consent_scope == "preference_memory" else "read",
    requested_data_categories=[proposal.data_category])

  if auth_response.decision == deny:
    proposal.storage_scope ← session       # N-02: session/ephemeral
  else:
    proposal.storage_scope ← persistent    # только для scope_id=preference_memory
```

Audit trail proposal: `proposal_id`, `consent_scope`, `consent_status`
(`granted`/`missing`), `storage_scope` (`session`/`persistent`).

## 7. Consent lifecycle MVP

Минимальные состояния:

```text
not_requested
→ granted
→ revoked

not_requested
→ denied

granted
→ expired
```

Обязательные поля consent record:

```yaml
consent_id: uuid
subject_id: uuid
scope_id: string
scope_version: string
status: granted | denied | revoked | expired
granted_at: datetime | null
revoked_at: datetime | null
expires_at: datetime | null
source: chat | profile | onboarding | support
proof_reference: string
```

Правила:

- согласие относится к конкретной версии scope;
- совместимое MINOR-уточнение может продолжить действовать только после
  Privacy review;
- несовместимое изменение purpose, data categories, consumers или operations
  требует новой версии и повторного согласия;
- отсутствие consent record не интерпретируется как согласие;
- отзыв должен стать видимым runtime-компонентам без ожидания новой сессии.

### Scope Version Migration

> **Design candidate — non-normative до закрытия `CSR-OD-6`.** Пока
> совместимость между MINOR-версиями scope не решена как открытый вопрос,
> правило ниже описывает целевое поведение, а не действующую норму. До
> закрытия `CSR-OD-6` действует консервативный дефолт из Edge Cases выше:
> любое изменение scope требует Privacy review, автоматическая
> совместимость не предполагается.

**MINOR-версия** (добавление опционального поля, уточнение формулировки
без изменения purpose): существующий consent продолжает действовать;
пользователь получает уведомление об изменении, но повторное согласие не
требуется; audit event `scope_version_minor_updated`.

**MAJOR-версия** (новая категория данных, изменение purpose, новый
consumer): существующий consent автоматически переходит в `expired`;
запрос на повторное согласие при следующем взаимодействии; до повторного
согласия данные не используются (fail-closed); audit events
`scope_version_major_updated`, `consent_expired`.

**Переходный период для MAJOR:** повторное согласие запрашивается при
следующем релевантном взаимодействии с пользователем — без фиксированного
числа дней. Конкретный срок (было: «30 дней») намеренно убран: если
consent сразу становится `expired`, число дней ничего не меняет в
authorization decision, а зафиксированное число рискует восприниматься
разработчиками как контракт. Записи памяти не удаляются (retention
policy), но не используются для персонализации до повторного согласия.

## 8. Команды пользователя

MVP должен поддерживать:

- просмотр активных согласий;
- отзыв отдельного scope;
- отключение всей persistent personalization;
- команду «Что Ayla знает обо мне»;
- удаление выбранного memory fact;
- команду «Забыть это».

Точная судьба исходных backend-фактов определяется owning domain и retention
policy. Команда удаления memory fact не должна молча удалять подтверждённую
booking history из её source of truth.

### UX Requirements (функциональные, не сценарий диалога)

Конкретные реплики бота — предмет будущего Conversation Design (planned,
пока не материализован в проекте), не этого governance-документа. Здесь
фиксируются только обязательные функциональные требования:

- запрос согласия должен называть **цель** использования (какой scope),
  а не только факт «сохранить данные»;
- пользователь должен иметь возможность отклонить запрос без прерывания
  текущего диалога (Constitution Ст. X — уместность прежде действия);
- команда «Что Ayla знает обо мне» должна показывать активные согласия
  по scope, а не только список фактов памяти;
- отзыв — не более чем одной командой, без перехода в отдельный интерфейс;
- после отзыва система должна подтвердить пользователю, что именно
  изменилось (какой scope отозван, что это означает для будущих
  рекомендаций) — без придумывания точной формулировки здесь.

## 9. Audit events

Минимальный набор:

| Event | Когда создаётся |
|---|---|
| `consent_granted` | Пользователь предоставил согласие |
| `consent_denied` | Пользователь отказал |
| `consent_revoked` | Пользователь отозвал согласие |
| `consent_expired` | Согласие истекло |
| `consent_scope_checked` | Выполнена runtime-проверка |
| `context_read_allowed` | Чтение разрешено |
| `context_read_denied` | Чтение запрещено |
| `memory_fact_used` | Persistent fact вошёл в рекомендацию |
| `memory_fact_deleted` | Memory fact удалён |
| `scope_version_mismatch` | Consent относится к несовместимой версии scope |

Audit event не должен содержать полный текст чувствительного факта, если для
аудита достаточно идентификатора, категории и decision metadata.

### Audit Event Storage and Retention

**Формат записи** — JSON: `event_id`, `event_name`, `timestamp`,
`subject_id`, `scope_id`, `scope_version`, `consumer`, `decision`, `reason`,
`data_categories`, `tenant_id`, `conversation_id`.

**Хранение — не решено, зависит от KM-CSR-1.** AMD-020 Pilot Scope Registry
(approved) уже называет «Consent Domain» нормативным владельцем и source of
truth для Consent Records, отдельно от User Context Domain. Пока это
расхождение (KM-CSR-1 из прошлого ревью) не разрешено, конкретная система
и таблица хранения audit log здесь **не фиксируются** — это предвосхитило
бы решение, которое ещё не принято.

**Retention period — design candidates, не финальные решения:**
- Consent lifecycle events (`consent_granted`, `consent_revoked`) —
  предлагается длительный период для compliance с 152-ФЗ; точный срок
  требует подтверждения Legal, не фиксируется здесь как факт (тот же
  паттерн, что ADR-0012 OD-5/OD-6 — числа остаются design candidate).
- Runtime access events (`context_read_allowed/denied`) — операционный,
  короче consent lifecycle events; точное число — тоже design candidate.
- Aggregated analytics — обезличенные данные, retention вне scope этого
  документа.

**Доступ:** Privacy Owner — полный доступ для compliance audit; Safety
Owner — доступ к `context_read_denied` для расследования инцидентов;
Product Owner — доступ к обезличенной aggregate analytics; разработчики —
только через отдельно утверждённую break-glass процедуру. **Не цитирую
«ADR-0011 §7.2»** как источник этой процедуры — ADR-0011 в этом проекте
существует только как несинхронизированная mirror-заглушка без реального
содержания; ссылка на конкретный параграф непроверяема, пока mirror sync
не активирован.

## 10. MVP activation gate

Persistent personalization может быть включена только когда:

- scopes `intent_understanding` и `provider_selection` имеют статус `approved`;
- Privacy Owner подтвердил формулировки согласия;
- runtime authorization contract реализован;
- consent lifecycle хранится в утверждённом source of truth;
- revocation распространяется на runtime без новой сессии;
- существуют audit events;
- реализован negative test: отсутствие consent всегда приводит к deny;
- реализована команда отключения persistent personalization.

До выполнения gate система работает в режиме:

```text
session context only
+
no proactive recommendations
+
no cross-domain personalization
+
no persistent inferred signals
```

## 11. Отношение к Killer PRD

Killer PRD является consumer этого Registry.

Для канонизации Killer PRD достаточно:

1. материализовать данный Registry;
2. утвердить минимальные scopes, непосредственно используемые killer-сценарием;
3. сохранить заблокированными scopes, требующие отдельных Legal/Privacy решений;
4. связать `OD-K9` (Killer PRD) с этим node через traceability.

Наличие Registry не означает автоматического разрешения всех перечисленных
scopes.

**Дублирующий идентификатор:** ADR-0012 фиксирует тот же блокер под
собственным `OD-9` («Canonical consent-scope registry: утвердить versioned
список»). `OD-K9` (Killer PRD) и `OD-9` (ADR-0012) — один и тот же
открытый вопрос под двумя разными ID в разных документах; при канонизации
любого из двух стоит явно связать их друг с другом, а не оставлять как
два независимых номера.

## 11.1 Relationship to ADR-0011 Sensitivity Zones

> **Informative, не нормативный раздел** — нормативны сами `sensitivity_zone`
> (ADR-0011/ADR-0012) и `consent_scope` (§5 этого документа) по отдельности;
> этот раздел только их сопоставляет.

Разделение ответственности: **Sensitivity Zone** (ADR-0011, через ADR-0012)
определяет, насколько чувствительно содержимое и каковы правила хранения/
retention. **Consent Scope** (этот Registry) определяет, для какой цели
можно использовать данные. Обе проверки выполняются совместно на одном
этапе (Killer PRD §5.1, gate 1) — см. §6 «Integration with Recommendation
Composer» выше.

Примеры, **сверенные с ADR-0012 дословно** (не придуманные):

| Поле | Sensitivity Zone | Consent Scope |
|---|---|---|
| `preferred_time_slots` | `green` (по контракту) | `provider_selection` |
| `diet_type=vegan` | `yellow` (ADR-0011 §4.2, по цитате ADR-0012) | `provider_selection` |
| Подтверждённая беременность | `red` (единственный явный пример `red` в ADR-0012) | зависит от scope, использующего этот факт |

**Исправление относительно предложенного примера:** аллергии (`vegan/keto/
allergies`) в ADR-0012 дословно отнесены к `yellow`, **не** `red` — я не
могу подтвердить пример «`allergy=peanuts` → `red`» и не вношу его в этом
виде. Единственный подтверждённый пример `red` в корпусе — подтверждённая
беременность.

Runtime-проверка: authorization layer проверяет оба измерения — если хотя
бы одно возвращает отказ (`consent_scope` не разрешён ИЛИ zone
несовместима), итоговое решение — `deny`.

## 11.2 Cross-Domain Personalization Design (Post-MVP, `blocked`)

Требования при разблокировке `cross_domain_personalization` (§5.4):

1. Отдельное гранулярное согласие по паре source-domain → target-domain.
2. Явное объяснение пользователю, какой контекст используется и откуда.
3. Возможность отозвать согласие для конкретной пары доменов независимо
   от остальных.

```yaml
scope_id: cross_domain_personalization
source_domain: <domain>
target_domain: <domain>
allowed_data: только явно перечисленные категории после отдельного amendment
consent_requirement: отдельное явное согласие по паре доменов
```

**Activation criteria:** Legal review cross-domain data transfer; Privacy
impact assessment; user research на понимание cross-domain consent;
Measurement Framework для оценки полезности.

**Про иллюстративный пример: сознательно не привожу конкретный сценарий
здесь.** Предложенный в ревью пример («сканирует завтрак → дефицит
витамина D → рекомендует массаж») — это тот самый единственный food-first
сценарий, который был явно исключён из Ayla Product Vision (v1.0→v1.1) как
противоречащий AYLA-DEC-0002 и Killer PRD §2.2/§4 (четыре равноправных
триггера, еда — не центр). Использование этого примера здесь вернуло бы
устаревшую формулировку в канон через другой документ. Если нужен
иллюстративный пример cross-domain personalization — его стоит взять из
одного из четырёх официальных trigger-сценариев Killer PRD §4, не
изобретать заново.

## 11.3 Integration with Data Export (AMD-020 C5)

> **Informative, не нормативный раздел** — нормативная модель экспорта
> целиком в AMD-020 C5, здесь только точка соприкосновения с consent
> metadata.

**Не пересказываю C5 упрощённо — ссылаюсь на его реальную модель.**
`AMD-020 C5 Pilot Personal Context Export-Forget Contract` уже определяет
`operation_id`, `operation_type: export|delete`, исполнителя `W3`, и
барьерную/идемпотентную обработку запросов — это не переизобретается
здесь.

Что специфично для этого Registry: `consent_scope`, `sensitivity_zone` и
`provenance` (ADR-0012) должны попадать в export payload как метаданные
memory-записей — это дополняет, а не заменяет модель C5.

**Важное ограничение из самого C5, которое нельзя не упомянуть:**
Wellness/sleep history и Conversations/messages **явно исключены** из
пилотного scope C5 (`excluded_post_pilot_inventory`) — это активно
отслеживаемый пробел, помеченный в самом контракте как противоречащий
ожиданиям пользователя (wellness handoff подразумевает экспорт raw sleep
history, что «directly contradicts AMD-020 exclusion»). Any данные,
подпадающие под `health_related_signal` в этом Registry, наследуют то же
исключение — экспорт этой категории вне scope MVP, синхронно с тем, что
она и так `запрещено` для persistent storage (§4).

`RedZoneAccessLog` — подтверждено ADR-0012 — при экспорте включается
только как metadata, не raw содержимое.

**Не ввожу новую команду** («Экспортируй мои данные») — C5 уже определяет
операционную модель через `operation_type: export`; конкретная
пользовательская фраза, инициирующая её, — вопрос Conversation Design, не
этого документа.

## 11.4 Integration with Minor Protection

**Не могу подтвердить «ADR-0011 §10» как источник.** ADR-0011 в этом
проекте существует только как несинхронизированная mirror-заглушка
(`status: planned`, содержания нет) — то же ограничение, что я уже отмечал
для «§7.2» в этом ревью. Фиксирую идею как **открытый вопрос**, не как
подтверждённое правило:

**Открытый вопрос:** если ADR-0011 (после синхронизации) определяет защиту
несовершеннолетних через блокировку yellow/red записей независимо от
consent, то приоритет должен быть явно зафиксирован — protection
несовершеннолетних не может быть снята одним лишь наличием `granted`
consent в этом Registry. Требует подтверждения после активации mirror sync
ADR-0011, не фиксируется здесь как решение.

## 12. Open decisions

| ID | Решение | Блокирует |
|---|---|---|
| CSR-OD-1 | Privacy/Legal основание и retention для recommendation measurement | Analytics activation |
| CSR-OD-2 | Допустимость proactive personalization и формулировка отдельного consent | `proactive_recommendation` |
| CSR-OD-3 | Cross-domain consent model | `cross_domain_personalization` |
| CSR-OD-4 | Решение по diet/religion/skin-sensitivity signals | Соответствующие data categories |
| CSR-OD-5 | Канонический source of truth для consent records | Persistent personalization |
| CSR-OD-6 | Совместимость consent между MINOR-версиями scope | Scope version migration |
| CSR-OD-7 | Разделить Registry на нормативное ядро (правила, scopes, authorization basis, lifecycle) + отдельный Consent Runtime Authorization Contract (request/response, errors, tenant isolation, versioning) — интеграционные разделы (§6 integration, §11) остаются informative до решения | Структура документа, не блокирует MVP-контент |
| CSR-OD-8 | Identity/tenancy контракт для global user scope (`tenant_id=null`) | Любое использование глобальной (не tenant-scoped) памяти — сейчас `blocked` |

**Примечание о дублировании ID:** `CSR-OD-4` — тот же вопрос, что `OD-1` в
ADR-0012/Killer PRD (diet_type/skin_sensitivities/religious inference,
Legal ruling). Это один открытый вопрос под тремя разными
идентификаторами (`OD-1`, `OD-K1`-соседний контекст в Killer PRD §12,
`CSR-OD-4` здесь) — при получении Legal ruling нужно закрыть все три
одновременно, не по отдельности.

## 12.1 Future Considerations (post-MVP, не выполняется сейчас)

Зафиксировано намерение, не действие:

- **Разделение документа** (~1000 строк уже сейчас, риск роста до ~2000):
  Consent Scope Registry (правила, scopes, authorization basis) → Consent
  Runtime Contract (request/response, errors, versioning) → Consent Audit
  Contract → Consent UX. См. `CSR-OD-7`. До MVP — один документ, это
  нормально.
- **`recommendation_measurement`** (§5.6) смешивает attribution, analytics,
  privacy и recommendation metrics — после MVP может быть вынесен в
  отдельный `Recommendation Analytics Contract`. Пока `blocked` (CSR-OD-1),
  откладывать не критично.
- **Scope inheritance** (например, `provider_selection` наследует
  категории `intent_understanding`, чтобы не дублировать список) — полезно
  при росте количества scopes, не нужно для текущих семи. Не вводится
  сейчас, чтобы не усложнять MVP-контракт преждевременно.

## 13. Delivery ownership

| Work item | Owner |
|---|---|
| Утверждение scope purposes | Product Owner |
| Privacy review | Privacy Owner |
| Legal basis и тексты согласия | Legal |
| Consent storage и API | User Context Domain |
| Retrieval enforcement | `ai-bot-platform` |
| Rendering/grounding enforcement | `ayla-ai-core` |
| Source data enforcement | Owning backend domains |
| Audit and analytics integration | Analytics Owner |
| KB validation and navigation | Product Architecture |

## 14. Change Log

### v0.5 — 2026-07-27 — P1/P2 полировка

- `registry_version` добавлен в ответ authorization layer (был только в
  запросе).
- §4 — добавлена колонка `Owner` по data category; честно помечены три
  категории (`explicit_goal`, `booking_history`, `interaction_history`),
  для которых нет прямого соответствия в AMD-020 Ownership Summary —
  открытый вопрос, не выдуманный владелец.
- `authorization_basis` расширен значением `system_operation` — для
  внутренних технических операций (memory cleanup), не требующих consent.
- Добавлен §12.1 Future Considerations — разделение документа (`CSR-OD-7`),
  вынос `recommendation_measurement`, scope inheritance — зафиксированы
  как намерение, не выполнены, по прямой рекомендации ревью «не сейчас».

### v0.4 — 2026-07-27 — Повторное ревью: устранение внутренних противоречий

**Проверено и отклонено:**
- **P0-1 (повреждённый frontmatter)** — не подтвердилось. Побайтовая
  проверка (`od -c`): файл корректно начинается с `---\nnode_id: ...`.
  Второй случай такой же ложной претензии за эту сессию (первый — на
  Ayla Product Vision) — похоже на устойчивый артефакт рендеринга в
  инструменте ревью, не реальный дефект.

**Внесено (P0):**
- P0-2 — разделены `registry_version` (документ) и `scope_version`
  (конкретный scope, теперь отдельное поле в каждой таблице §5,
  независимая нумерация с `1.0`); все embedded-примеры исправлены.
- P0-3 — новый scope `preference_memory` (§5.7): `provider_selection` и
  `intent_understanding` теперь строго `read`/`model_transfer`, без
  `write`; Memory Proposal Flow исправлен — persistence адресуется
  `preference_memory`, не read-only scopes.
- P0-4 — унифицированы consumer-идентификаторы: только системные
  (`ai-bot-platform`, `ayla-ai-core`, `beautygo_backend`) из списков
  `Consumers` в §5; добавлено информативное поле `consumer_component` для
  конкретного модуля.
- P0-5 — добавлен `authorization_basis` (`explicit_consent` /
  `service_necessity` / `legal_obligation` / `approved_legitimate_interest`)
  отдельно от `consent_required`; `recommendation_measurement` переведён
  на `approved_legitimate_interest` + `CSR-OD-1`, статус `blocked` до
  решения.

**Внесено (P1):**
- P1-1 — устранено противоречие partial read: MVP-правило — atomic deny
  (одна запрещённая категория → отказ всего запроса).
- P1-2 — Scope Version Migration помечен design candidate / non-normative
  до закрытия `CSR-OD-6`; консервативный дефолт — Privacy review для
  любого изменения.
- P1-3 — `mvp_status` переведён на enum (`draft`/`proposed`/`approved`/
  `blocked`/`deprecated`) + отдельное поле `blocking_reason`.
- P1-4 — интеграционные разделы (§6 integration, §11.1/11.3) помечены
  Informative, не нормативные; разделение на отдельный Consent Runtime
  Authorization Contract зафиксировано как `CSR-OD-7`, не выполнено
  явочным порядком.
- P1-5 — global user scope (`tenant_id=null`) переведён в `blocked` до
  отдельного identity/tenancy контракта (`CSR-OD-8`).
- P1-6 — `beautygo_backend` в `provider_selection` явно помечен как data
  source (`booking_history`), не consumer scope.

**Внесено (P2):**
- P2-1 — §4.1 помечен провизорным, до материализации Data Inventory
  Matrix, которая должна владеть маппингом `field → data_category`.
- P2-2 — операция `render` заменена на точный набор (`read`, `write`,
  `delete`, `derive`, `model_transfer`, `user_disclosure`, `measure`).
- P2-3 — явный запрет wildcard scopes (`all_personalization`, `*`).
- P2-4 — правило разграничения session use / persistent consent вынесено
  в §3 как центральное.
- P2-5 — число «30 дней» убрано полностью, заменено качественным
  правилом «при следующем релевантном взаимодействии».

### v0.3 — 2026-07-27 — Ревью: 5 критических пробелов + 7 архитектурных вопросов

**Внесено:**
- §4.1 Data Category Mapping — только поля, подтверждённые в ADR-0012;
  остальные категории явно помечены как открытый вопрос, не выдуманы.
- Edge Cases and Error Handling (§6) — пять сценариев отказа с точным
  `reason`.
- Scope Version Migration (§7) — MINOR/MAJOR правила; численный переходный
  период (30 дней) помечен как design candidate.
- UX Requirements (§8) — функциональные требования вместо сценария
  диалога; конкретные реплики оставлены Conversation Design.
- Audit Event Storage and Retention (§9) — формат и доступ зафиксированы;
  хранение и retention period — design candidates, зависят от
  нерешённого KM-CSR-1.
- Integration with Recommendation Composer, Proactive Readiness Gate,
  Memory Proposal Flow (§6) — все три в псевдокоде/YAML, не в Python
  (уровень спецификации, не реализации).
- §11.1 Relationship to ADR-0011 Sensitivity Zones — с исправленным
  примером (аллергии — `yellow`, не `red`, по дословной цитате ADR-0012).
- §11.2 Cross-Domain Personalization Design — без food-first примера (см.
  ниже, почему отклонён).
- §11.3 Integration with Data Export (AMD-020 C5) — ссылка на реальную
  модель C5 (`operation_id`/`operation_type`/`W3`), включая упоминание
  исключения wellness/conversations из пилотного scope.
- §11.4 Integration with Minor Protection — как открытый вопрос, не как
  подтверждённая цитата.
- Связаны дублирующиеся идентификаторы: `OD-K9` (Killer PRD) ↔ `OD-9`
  (ADR-0012); `CSR-OD-4` ↔ `OD-1`.

**Отклонено или изменено относительно предложенного ревью:**
- Пример «`allergy=peanuts` → `red` zone» — не подтверждён; ADR-0012
  дословно относит аллергии к `yellow`.
- Пример cross-domain personalization «завтрак → дефицит витамина D →
  массаж» — это deprecated food-first сценарий, уже исключённый из Ayla
  Product Vision за противоречие AYLA-DEC-0002; не внесён.
- Упрощённое описание Data Export — заменено ссылкой на реальную модель
  AMD-020 C5 вместо параллельного упрощённого пересказа; добавлено
  критичное упущение — исключение wellness/conversations из пилота.
- Цитаты «ADR-0011 §7.2» (break-glass) и «ADR-0011 §10» (Minor Protection)
  — не приняты как подтверждённые: ADR-0011 в проекте существует только
  как несинхронизированная mirror-заглушка без реального содержания.
- Retention «7 лет compliance 152-ФЗ» и хранение в конкретной таблице
  `ai-bot-platform` — понижены до design candidates / открытых вопросов,
  не зафиксированы как решения (второе дополнительно зависит от
  нерешённого KM-CSR-1 — Consent Domain vs User Context Domain).
- Python-код в предложенных интеграционных разделах — переведён в
  псевдокод/YAML по конвенции остального документа (§6).
- Таблица согласованности ревью ссылалась на «Killer PRD v1.1» —
  актуальная версия v1.4.1.

### v0.2 — 2026-07-27

- planned placeholder преобразован в минимальный исполнимый MVP Registry;
- добавлены категории данных и шесть scopes из Killer PRD;
- scopes, требующие отдельных решений, оставлены `blocked`;
- определены runtime authorization request/decision contracts;
- введён consent lifecycle и правила version compatibility;
- определены user controls, audit events и activation gate;
- canonical system owner изменён на `ayla-knowledge`;
- metadata sensitivity повышена до personal/high;
- AI indexing ограничен, export policy изменена на metadata-only;
- добавлены open decisions и delivery ownership.

### v0.1 — 2026-07-27

- документ материализован как planned knowledge node;
- зафиксированы назначение, владельцы и связь с Killer PRD и AMD-020.
