---
node_id: ayla.foundation.glossary
title: Ayla Glossary
type: terminology-standard
status: review
activation_status: pending-infrastructure
version: "2.2"
owner: Product Architecture
priority: P0
knowledge_area:
  - foundation
domain: []
concerns:
  - knowledge-management
  - governance
system_owner:
  - ayla-knowledge
source_repository: ayla-knowledge
created: 2026-07-18
updated: 2026-08-25
source_kind: canonical
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
tags:
  - ayla
  - ayla/foundation
  - ayla/glossary
  - type/terminology-standard
  - priority/p0
implements: []
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Knowledge Architecture Specification]]"
  - "[[Ayla Decision Log]]"
adr:
  - "[[ADR-0007 Conversation State Enum]]"
related:
  - "[[Ayla Domain and Metadata Registry]]"
  - "[[Knowledge Schema Reference]]"
  - "[[Ayla User Journey Specification]]"
supersedes: []
review_cycle: quarterly
migration_source:
  repository: beautygo_backend
  path: docs/00 Foundation/Glossary.md
  tracked_in_source_git: false
  sha256: e4f986bcf4e8fb8f01e5fd56c777a36be6dd0aa5949d109312854283fb47562a
  imported: 2026-07-18
---

# Ayla Glossary v2.1

## 1. Purpose and authority

Этот документ задаёт канонические значения продуктовых, доменных, AI-, safety-, business- и knowledge-терминов Ayla.

Главная задача:

> одинаковые слова во всех документах, коде, аналитике и обсуждениях должны обозначать одинаковые сущности и процессы.

Ayla Glossary является нормативным терминологическим стандартом. Он обязателен для Foundation, Product, UX, AI, Architecture, Safety, Business, Analytics и Operations-документов.

Glossary определяет смысл термина, но не подменяет профильный источник решения. Если термин определён Accepted ADR или утверждённой спецификацией, Glossary пересказывает его смысл и ссылается на источник, но не изменяет решение самостоятельно.

## 1.1. Source-of-truth boundaries

Источники истины разделены так:

1. `schema.yaml` — машинный источник истины для metadata enums, document types, lifecycle transitions, validation constraints и разрешённых relationship fields.
2. `Ayla Domain and Metadata Registry` — человекочитаемое представление schema и ownership mappings.
3. `Ayla Glossary` — семантика продуктовых, доменных и архитектурных терминов.
4. ADR и профильные спецификации — источник конкретных архитектурных, lifecycle и policy-решений.

Glossary не поддерживает независимые копии enum-реестров schema.

## 1.2. Term maturity model

Каждый ключевой нормативный термин имеет:

- `Defined by`;
- `Status`: `planned`, `proposed`, `accepted`, `implemented`, `deprecated`;
- `Owner`.

Glossary не повышает зрелость термина. Термин из proposed-документа остаётся proposed.

## 1.3. Canonical term contract

Для ключевого нормативного термина обязательны:

- canonical heading или `Canonical name`;
- `Definition`;
- `Defined by`;
- `Status`;
- `Owner`.

Дополнительно указываются, когда применимо:

- `Russian name`;
- `Not`;
- `Allowed aliases`;
- `Forbidden aliases`;
- code name;
- current basis;
- planned source.

Расширенный шаблон обязателен, если термин:

- имеет распространённые неоднозначные синонимы;
- используется одновременно в product language и code/API;
- заменяет deprecated-термин;
- ограничивает Safety, Privacy или Economy и требует явного определения
  допустимого и недопустимого употребления.

Для вспомогательных explanatory terms допускается сокращённая карточка, если
она не создаёт самостоятельного нормативного контракта.

## 2. Правила использования

### 2.1. Один термин — одно каноническое значение

Если одно слово используется в разных смыслах, значения разделяются на отдельные термины.

Например, слово «профиль» нельзя одновременно использовать для:

- аккаунта;
- набора предпочтений;
- экрана приложения;
- модели памяти.

Нужно различать:

- `Account`;
- `User Profile`;
- `Preference Set`;
- `Profile Screen`;
- `User Model`.

### 2.2. Русское и английское имя

Для продуктовых и технических сущностей фиксируются:

- canonical English name;
- рекомендуемое русское название;
- допустимые сокращения;
- запрещённые синонимы.

В коде, API и analytics используется английское имя. В интерфейсе — понятная локализованная формулировка.

### 2.3. Термин не означает реализацию

Наличие термина не означает, что сущность уже:

- входит в MVP;
- реализована;
- хранится в базе;
- доступна пользователю.

Scope определяется профильной спецификацией.

### 2.4. Неопределённость должна быть явной

Спорный термин получает статус `planned`, `proposed` или `deprecated`.

---

## 3. Базовые продуктовые понятия и роли

### Ayla

**Canonical name:** `Ayla`  
**Русское название:** Ayla  
**Определение:** персональный AI для заботы о себе и платформа, координирующая знания, действия, специалистов и сервисы вокруг целей пользователя в области питания, физической активности, спорта, восстановления, сна, self-care, внешнего ухода и связанных профессиональных услуг.  
**Не является:** медицинским диагностом, рекламным агрегатором, обычным каталогом или чат-ботом общего назначения.  
**Defined by:** [[Ayla Constitution]]  
**Status:** accepted  
**Owner:** Product Architecture

### Ayla Pro

**Русское название:** профессиональный контур Ayla  
**Определение:** профессиональный контур для самостоятельных специалистов и организаций, предоставляющий инструменты платформы без права управлять персональным AI, вниманием, контекстом, памятью или выбором пользователя.  
**Не является:** владельцем User, его User Model или каналом покупки приоритета в Recommendation.  
**Defined by:** [[Ayla Constitution]]  
**Status:** accepted  
**Owner:** Product Architecture

### User

**Русское название:** пользователь  
**Определение:** человек в глобальном продуктовом контексте Ayla, в интересах которого действует Ayla и который управляет своими целями, согласиями, персональным контекстом и выбором.  
**Не является:** обязательно зарегистрированным аккаунтом, Customer конкретного tenant или собственностью Provider.  
**Defined by:** [[Ayla Constitution]]  
**Status:** accepted  
**Owner:** Product Architecture

### Guest User

**Русское название:** гость  
**Определение:** User без подтверждённой постоянной identity в Ayla.
**Status:** proposed  
**Owner:** Identity Domain

### Registered User

**Русское название:** зарегистрированный пользователь  
**Определение:** User, для которого создан account и подтверждена связь с поддерживаемым идентификатором.
**Status:** proposed  
**Owner:** Identity Domain

### BotUser

**Русское название:** технический пользователь бота  
**Определение:** техническая identity-сущность, связывающая User с каналом и account Ayla.  
**Planned source:** `ADR-0008 Role Detection and Staff Model`  
**Status:** planned  
**Owner:** Identity Domain

### Customer

**Русское название:** клиент конкретного Provider  
**Определение:** tenant-scoped роль User относительно конкретного Provider.  
**Не является:** глобальной identity-сущностью Ayla.  
**Planned source:** `ADR-0008 Role Detection and Staff Model`  
**Status:** planned  
**Owner:** Identity Domain

### Provider

**Русское название:** провайдер / поставщик услуги  
**Определение:** самостоятельный Specialist или организация, предоставляющие услугу, консультацию, программу, Slot, обследование или иной ресурс. Один человек может одновременно быть Provider как сторона профессионального контура и Specialist как исполнитель услуги.  
**Не является:** владельцем глобального User, его User Model, Cross-Provider Memory или приоритета в Recommendation.  
**Defined by:** [[Ayla Constitution]]  
**Status:** accepted  
**Owner:** Provider Domain

### Tenant

**Русское название:** тенант  
**Определение:** техническая граница данных и операций конкретного Provider в multi-tenant архитектуре.  
**Planned source:** `Tenant as Provider Model`  
**Status:** planned  
**Owner:** Platform Architecture

### Salon

**Русское название:** салон  
**Определение:** конкретный subtype Provider.  
**Не является:** универсальным синонимом Provider.
**Status:** proposed  
**Owner:** Provider Domain

### Specialist

**Русское название:** специалист  
**Определение:** человек, непосредственно оказывающий услугу и несущий профессиональную ответственность в пределах подтверждённой компетенции.  
**Defined by:** [[Ayla Constitution]]  
**Status:** accepted  
**Owner:** Provider Domain

### Master

**Русское название:** мастер  
**Определение:** принятое техническое имя роли Specialist в ai-bot-platform.  
**Planned source:** `ADR-0008 Role Detection and Staff Model`  
**Status:** planned  
**Owner:** Provider Domain

### CatalogMaster

**Русское название:** мастер каталога  
**Определение:** техническое представление Specialist, доступного в каталоге и подборе.
**Planned source:** `ADR-0008 Role Detection and Staff Model`  
**Status:** planned  
**Owner:** Provider Domain

### TenantStaff

**Русское название:** сотрудник Provider  
**Определение:** обобщающая техническая роль сотрудника tenant.  
**Подтипы:** `Receptionist`, `Admin`, `Owner`, `Master`.  
**Planned source:** `ADR-0008 Role Detection and Staff Model`  
**Status:** planned  
**Owner:** Identity Domain

### Receptionist

**Русское название:** администратор записи  
**Определение:** TenantStaff, управляющий расписанием, обращениями и booking operations в пределах прав.
**Status:** planned  
**Owner:** Identity Domain

### Admin

**Русское название:** администратор tenant  
**Определение:** TenantStaff с административными полномочиями.
**Status:** planned  
**Owner:** Identity Domain

### Owner

**Русское название:** владелец Provider  
**Определение:** tenant role, представляющая владельца организации.
**Status:** planned  
**Owner:** Identity Domain

### Canonical actor mapping

| Product language | Technical/domain language | Meaning |
|---|---|---|
| `User` | `BotUser` / registered account | человек в глобальном контексте Ayla |
| `Customer` | tenant-scoped role | User как клиент конкретного Provider |
| `Specialist` | `Master` / `CatalogMaster` | человек, оказывающий услугу |
| `Provider` | provider account / `Tenant` | самостоятельный специалист или организация как сторона профессионального контура |
| `Salon` | Provider subtype | конкретный тип Provider |
| `TenantStaff` | staff role family | сотрудники Provider |

## 4. Понимание человека

### User Message

**Русское название:** сообщение пользователя  
**Определение:** текстовое, голосовое, визуальное или структурированное выражение, полученное Ayla в конкретный момент.  
**Не является:** Intent, Goal или достоверным фактом само по себе.

### Query

**Русское название:** запрос  
**Определение:** нормализованное содержимое текущего обращения для обработки.

### Human State

**Русское название:** состояние человека  
**Определение:** описанная или наблюдаемая текущая ситуация, влияющая на выбор полезного действия.  
**Не является:** диагнозом.  
**Owner:** AI Architecture

### Journey State

**Русское название:** состояние пользовательского пути  
**Определение:** дискретная стадия journey state machine, например S0–S8.  
**Defined by:** [[Ayla User Journey Specification]]  
**Status:** proposed  
**Owner:** Product Architecture

### User Lifecycle State

**Русское название:** состояние жизненного цикла пользователя  
**Определение:** стадия отношений User с Ayla, не равная Journey State конкретного сценария.  
**Defined by:** [[Core User States]]  
**Status:** proposed  
**Owner:** Product Architecture

### Conversation State

**Русское название:** состояние диалога  
**Определение:** техническое состояние conversation state machine.  
**Defined by:** [[ADR-0007 Conversation State Enum]]  
**Status:** accepted  
**Owner:** Conversation Domain

### Booking State

**Русское название:** состояние бронирования  
**Определение:** текущее lifecycle-состояние Booking.  
**Current basis:** [[Event Taxonomy]] и существующая backend-модель  
**Planned canonical source:** [[Booking Lifecycle Specification]]  
**Status:** proposed  
**Owner:** Booking Domain

### Entity State

**Русское название:** состояние сущности  
**Определение:** lifecycle-состояние конкретной domain entity.  
**Status:** proposed  
**Owner:** Product Architecture

> Самостоятельное нормативное употребление слова `State` запрещено. Всегда используется квалифицированный термин.

### Intent

**Русское название:** намерение  
**Определение:** структурированное представление того, что человек пытается изменить, понять, выбрать или сделать в текущем контексте.  
**Не является:** ключевым словом, названием услуги или буквальным повторением сообщения.  
**Defined by:** [[Ayla Intent Model Specification]]  
**Status:** planned  
**Owner:** AI Architecture

### Intent Type

**Русское название:** тип намерения  
**Определение:** коммуникативный тип Intent.  
**Начальные категории:** `goal`, `action`, `information`, `management`, `feedback`, `correction`.

### Primary Intent

**Русское название:** основное намерение  
**Определение:** Intent, наиболее существенно определяющий текущий следующий шаг.

### Secondary Intent

**Русское название:** вторичное намерение  
**Определение:** дополнительный Intent, не являющийся главным для текущего решения.

### Goal Intent

**Определение:** Intent Type, выражающий желаемый результат.

### Action Intent

**Определение:** Intent Type, выражающий желание совершить действие.

### Information Intent

**Определение:** Intent Type, выражающий желание понять ситуацию, варианты или следующий шаг.

### Goal

**Русское название:** цель  
**Определение:** желаемый результат на уровне изменения состояния пользователя.  
**Не является:** услугой или действием.

### Goal Category

**Русское название:** категория цели  
**Определение:** предметная или lifecycle-категория Goal.  
**Примеры:** wellness, recovery, appearance, fitness, nutrition, booking. Acquisition, activation и retention являются product lifecycle goals и не должны называться Intent Type.

### Task

**Русское название:** задача  
**Определение:** промежуточная работа, необходимая для продвижения к Goal.

### Action

**Русское название:** действие  
**Определение:** конкретный исполнимый шаг User, Ayla или внешней системы.

### Next Best Action

**Русское название:** лучший следующий шаг  
**Определение:** наиболее полезное, безопасное и реалистичное действие в текущем контексте.  
**Не означает:** коммерчески наиболее выгодное действие.

### Intent Transition

**Русское название:** изменение намерения  
**Определение:** переход к новому Primary Intent после появления дополнительной информации.

### Multi-Intent

**Русское название:** множественное намерение  
**Определение:** ситуация, в которой одно сообщение содержит несколько значимых Intent.

## 5. Контекст

### Context

**Русское название:** контекст  
**Определение:** совокупность текущих данных, необходимых для понимания ситуации и выбора действия.  
**Не является:** автоматически достоверной истиной.

### Context Slot

**Русское название:** контекстный параметр / слот  
**Определение:** именованная единица Context, которая может быть заполнена, отсутствовать, конфликтовать или требовать подтверждения.

### Food Scanner

**Русское название:** сканер питания  
**Определение:** инструмент в составе Ayla, позволяющий User с минимальными усилиями, например через фото, предоставить данные о рационе для анализа паттернов.  
**Не является:** самостоятельным трекером калорий, медицинским диагностическим инструментом или отдельным продуктом.  
**Цель:** снижение трения при сборе Context и обогащение входных данных для Recommendation Engine.  
**Planned source:** [[Ayla MVP Product Thesis]]  
**Status:** planned  
**Owner:** Nutrition Domain

### Current Human State

**Русское название:** текущее состояние человека  
**Определение:** Human State, релевантный текущему решению.

### Constraint

**Русское название:** ограничение  
**Определение:** условие, сужающее или запрещающее часть решений. Safety Constraint имеет приоритет над Preference и коммерческими факторами.

### Preference

**Русское название:** предпочтение  
**Определение:** желательное, но обычно не обязательное условие.

### Relevant History

**Русское название:** релевантная история  
**Определение:** подтверждённая информация о прошлом опыте, влияющая на текущий выбор.

### Urgency

**Русское название:** срочность  
**Определение:** временная чувствительность цели или действия. Не равна Emergency Signal.

### Budget

**Русское название:** бюджет  
**Определение:** финансовый диапазон или ограничение для решения.

### Readiness Level

**Русское название:** уровень готовности пользователя  
**Определение:** оценка готовности User перейти от обсуждения к конкретному действию.  
**Начальные значения:** `exploring`, `considering`, `ready`, `not-ready`.  
**Не является:** разрешением системы на проактивное действие.

### User-Initiated Recommendation Gate

**Русское название:** шлюз рекомендации по запросу пользователя  
**Определение:** policy-механизм, который перед ответом рекомендацией на явный
текущий запрос User проверяет Safety, Eligibility, Context Sufficiency,
Competence Boundary и explicit current refusal.  
**Не является:** механизмом подавления проактивности; quiet hours и cooldown не
блокируют ответ на явный запрос User.  
**Defined by:** [[Ayla User Journey Specification]]  
**Status:** proposed  
**Owner:** Product Architecture

### Proactive Readiness Gate

**Русское название:** шлюз уместности проактивного действия  
**Определение:** policy-механизм, который перед проактивным предложением или
напоминанием дополнительно оценивает explicit refusal, cooldown, quiet hours,
proactivity Consent, relevance, recent duplicates и channel restrictions.  
**Правило:** если Gate блокирует проактивность, Ayla применяет `Helpful
Restraint`, не инициирует действие и не предлагает substitute offer.  
**Defined by:** [[Ayla User Journey Specification]]; planned source:
`ADR-0012 Dynamic User Model`  
**Status:** proposed  
**Owner:** Product Architecture

### Suppression Factor

**Русское название:** фактор подавления действия  
**Определение:** причина, по которой Proactive Readiness Gate запрещает или
откладывает проактивное действие.

### Helpful Restraint

**Русское название:** полезное воздержание  
**Определение:** осознанное решение Ayla не инициировать действие, когда вмешательство неуместно, нежелательно или небезопасно.

### Missing Information

**Русское название:** недостающая информация  
**Определение:** Context, без которого нельзя безопасно или полезно продолжить.

### Context Sufficiency

**Русское название:** достаточность контекста  
**Определение:** наличие минимально необходимой информации для конкретного класса действия.

### Context Sufficiency Gate

**Русское название:** проверка достаточности контекста  
**Определение:** policy-этап, решающий, можно ли рекомендовать, нужно ли уточнить, остановиться или перейти к Boundary Handling.

## 6. Уверенность и неопределённость

### Confidence

**Русское название:** уверенность модели  
**Определение:** оценка надёжности конкретного структурированного вывода.  
**Не является:** доказательством истинности.

### Intent Confidence

Оценка уверенности в определённом Intent.

### Slot Confidence

Оценка надёжности конкретного Context Slot.

### Unknown

**Русское название:** неизвестно  
**Определение:** валидное состояние, когда оснований для вывода недостаточно.  
**Правило:** Unknown предпочтительнее выдуманного ответа.

### Hypothesis

**Русское название:** гипотеза  
**Определение:** предположение, которое не подтверждено пользователем или надёжным источником.  
**Правило:** не используется как safety-critical факт.

---

## 7. Рекомендации и решения

### Recommendation

**Русское название:** рекомендация  
**Определение:** обоснованное предложение следующего действия на основе Intent, Context, Safety и доступных вариантов.  
**Не является:** приказом, гарантией результата или автоматическим выполнением.

### Substantial Recommendation

**Русское название:** существенная рекомендация  
**Определение:** Recommendation, способная заметно повлиять на здоровье, безопасность, деньги, персональные данные, доступ к Specialist, долгосрочную Goal или иное значимое решение User.  
**Правило:** требует объяснения, трассируемого к структурированным причинам и допустимым источникам.  
**Defined by:** [[Ayla Constitution]]  
**Status:** accepted  
**Owner:** Product Architecture

### Recommendation Candidate

**Русское название:** кандидат рекомендации  
**Определение:** потенциальный вариант до применения safety, eligibility, ranking и policy-фильтров.

### Candidate Generation

**Русское название:** генерация кандидатов  
**Определение:** формирование множества возможных действий, услуг или специалистов.

### Eligibility

**Русское название:** допустимость  
**Определение:** соответствие кандидата обязательным правилам участия в решении.

### Ranking

**Русское название:** ранжирование  
**Определение:** упорядочивание допустимых кандидатов по полезности для пользователя.

### Reason Code

**Русское название:** код причины  
**Определение:** машиночитаемое объяснение выбора, отклонения или ограничения варианта.

### Recommendation Explanation

**Русское название:** объяснение рекомендации  
**Определение:** понятное пользователю описание факторов, повлиявших на предложение.

### User Override

**Русское название:** изменение выбора пользователем  
**Определение:** явный выбор другого допустимого варианта.  
**Правило:** override не отменяет safety constraints.

### No Action

**Русское название:** отсутствие действия  
**Определение:** осознанный результат при недостатке контекста, отсутствии готовности, риске или отсутствии полезного варианта.

---

## 8. Safety и границы

### Safety

Правила и механизмы, предотвращающие неоправданный вред здоровью, безопасности, автономии, правам или данным User, Specialist и третьих лиц. Коммерческий или репутационный риск компании сам по себе не является основанием ограничить автономию User и управляется отдельными business, security и compliance policies.
**Defined by:** [[Ayla Constitution]]  
**Status:** accepted  
**Owner:** Safety Owner

### Safety Flag

Структурированный индикатор потенциального риска.

### Safety-Critical Information

**Русское название:** safety-critical сведения  
**Определение:** данные, ошибка, игнорирование или преждевременное забывание которых может создать риск для здоровья или безопасности User.  
**Правило:** давность сама по себе не удаляет сведения; они могут перейти в состояние «требует подтверждения», а прекращение использования должно быть объяснимым и контролируемым.  
**Defined by:** [[Ayla Constitution]]  
**Status:** accepted  
**Owner:** Safety Owner

### Safety Constraint

Обязательное правило, исключающее или изменяющее часть решений. Имеет приоритет над Goal, Preference, Budget и коммерческими факторами.

### Competence Boundary

Предел, за которым Ayla не выдаёт самостоятельную персонализированную рекомендацию или заключение.

### Boundary Handling

Сценарий, в котором Ayla объясняет ограничение и предлагает допустимый следующий шаг.

### Escalation

Передача ситуации человеку, специалисту, поддержке или экстренной службе согласно policy.

### Emergency Signal

Признак возможной немедленной угрозы здоровью или безопасности.

### Out of Domain

Запрос вне поддерживаемой области или требующий отсутствующей компетенции.

### Harmful Recommendation

Рекомендация, способная создать неоправданный риск.

---

## 9. Память и персонализация

### User Model

**Русское название:** модель пользователя  
**Определение:** федеративная, управляемая User система подтверждённых сведений, временного контекста, наблюдений и Hypothesis, разделённых по предметным областям и целям использования, с явной маркировкой Provenance, актуальности и допустимости использования.  
**Не является:** психологическим профилем, абсолютной истиной или собственностью Provider.  
**Дополнение:** Dynamic User Model является planned-развитием: знания могут иметь классы стабильности, срок актуальности или TTL и `current_relevance`. MVP может реализовывать только подмножество модели.  
**Defined by:** [[Ayla Constitution]]  
**Status:** accepted  
**Owner:** User Context Domain

### Dynamic User Model

**Русское название:** динамическая модель пользователя  
**Определение:** User Model, в которой знания изменяются во времени, имеют provenance, класс стабильности, актуальность и правила повторного подтверждения.
**Planned source:** `ADR-0012 Dynamic User Model`  
**Status:** planned  
**Owner:** User Context Domain

### User Personal Context

**Русское название:** персональный контекст пользователя  
**Canonical code name:** `UserPersonalContext`  
**Определение:** управляемый контейнер данных и знаний, используемых с учётом Consent, Provenance, Sensitivity Zone и Retention Policy.  
**Planned source:** `ADR-0011 User Context Privacy`  
**Status:** planned  
**Owner:** User Context Domain

### Declared Personal Context

**Русское название:** заявленный персональный контекст  
**Определение:** информация, явно сообщённая User или подтверждённая им.

### Memory

**Русское название:** память Ayla  
**Определение:** механизм хранения и извлечения UserPersonalContext между сессиями.  
**Принцип:** memory is context, not truth.

### Memory Entry

**Русское название:** запись памяти  
**Определение:** структурированная единица памяти с source, provenance, sensitivity, consent, lifecycle и retention.
**Planned source:** [[Memory Entry Schema]]  
**Status:** planned  
**Owner:** User Context Domain

### Memory Source

**Русское название:** источник записи памяти  
**Категории:** `explicit`, `inferred`, `signal`.  
**Planned source:** [[Memory Entry Schema]]  
**Status:** planned

### Explicit Fact

**Русское название:** явно сообщённый факт  
**Определение:** информация, выраженная User напрямую. Не означает бессрочной актуальности.

### Inferred Context

**Русское название:** выведенный контекст  
**Определение:** предположение системы, полученное из сообщений или поведения и маркированное как inferred.

### Signal

**Русское название:** сигнал  
**Определение:** низкоуровневое наблюдение, которое может поддерживать гипотезу, но само не считается подтверждённым фактом.

### Provenance

**Русское название:** происхождение данных  
**Определение:** сведения о том, откуда, когда, каким способом и на каком основании возникла Memory Entry.

### Consent

**Русское название:** согласие  
**Определение:** отзывное разрешение User на конкретную цель и вид сбора, хранения, использования или передачи данных. Согласия на разные существенные цели разделяются и отзываются независимо.  
**Не является:** бессрочным или универсальным разрешением; молчание, бездействие и согласие на хранение истории не означают согласия на профилирование, гипотезы или проактивность.  
**Defined by:** [[Ayla Constitution]]  
**Status:** accepted  
**Owner:** Privacy and Safety

### Sensitivity Zone

**Русское название:** зона чувствительности пользовательской памяти  
**Определение:** policy-классификация `green`, `yellow`, `red`.  
**Не является:** `data_sensitivity` knowledge-документа.  
**Planned source:** `ADR-0011 User Context Privacy`  
**Status:** planned  
**Owner:** Privacy and Safety

### Retention Policy

**Русское название:** политика хранения  
**Определение:** правила срока хранения, пересмотра, удаления или обезличивания.

### Session Context

**Русское название:** контекст текущей сессии  
**Определение:** временные данные текущего взаимодействия.

### Persistent Memory

**Русское название:** долговременная память  
**Определение:** данные, сохраняемые между сессиями согласно Consent и governance.

### Memory Proposal

**Русское название:** предложение сохранить информацию  
**Определение:** кандидат на сохранение, ещё не ставший Persistent Memory.

### Memory Correction

**Русское название:** исправление памяти  
**Определение:** изменение сохранённой информации по инициативе User или после подтверждённого конфликта.

### Memory Suppression

**Русское название:** запрет использования записи  
**Определение:** policy-запрет использовать конкретную запись в персонализации.

### Provider-Specific History

**Русское название:** история конкретного Provider  
**Определение:** данные о взаимодействиях User с конкретным Provider, которые не должны автоматически становиться доступными другим Provider.

### Cross-Provider Memory

**Русское название:** межпровайдерная память Ayla  
**Определение:** персональный контекст, принадлежащий пользовательскому контуру Ayla, а не конкретному Provider.
**Planned source:** `ADR-0011 User Context Privacy`  
**Status:** planned  
**Owner:** Privacy and Safety

## 10. Диалог и каналы

### Conversation

Последовательность связанных взаимодействий пользователя и Ayla.

### Conversation Layer

Слой, управляющий сообщениями, состоянием диалога и continuity между каналами.

### Channel

Интерфейс взаимодействия пользователя с Ayla. Примеры: MAX Bot, Mini App, mobile app, web.

### Channel Adapter

Компонент, преобразующий возможности конкретного канала в канонический интерфейс Conversation Layer.

### MAX Bot

Первый conversational channel adapter Ayla. Не является ядром продукта.

### Mini App

Встроенный интерфейс для сценариев, которым недостаточно возможностей чата.

### Cross-Channel Continuity

Сохранение Intent, Context и незавершённого действия при переходе между каналами.

### Pending Intent

Сохранённое состояние цели или действия, которое продолжается после регистрации, перехода или прерывания.

---

## 11. Выполнение и Booking lifecycle

### Execution

**Русское название:** выполнение  
**Определение:** фактическое совершение выбранного действия через внутреннюю или внешнюю систему.

### Execution Layer

**Русское название:** слой выполнения  
**Определение:** компоненты, преобразующие подтверждённое решение в операцию.

### Booking

**Русское название:** бронирование / запись  
**Определение:** канонический агрегат бронирования, существующий на протяжении всего lifecycle — от создания до подтверждения, отмены, завершения или иного финального состояния.  
**Не является:** только подтверждённой записью.  
**Current basis:** [[Event Taxonomy]] и существующая backend-модель  
**Planned canonical source:** [[Booking Lifecycle Specification]]  
**Status:** proposed  
**Owner:** Booking Domain

### Booking Intent

**Русское название:** намерение записаться  
**Определение:** Intent User создать Booking.

### Booking Request

**Русское название:** запрос на бронирование  
**Определение:** команда или структурированный запрос на создание Booking.

### Confirmed Booking

**Русское название:** подтверждённое бронирование  
**Определение:** Booking в состоянии `confirmed`.

### Booking Lifecycle

**Русское название:** жизненный цикл бронирования  
**Определение:** набор допустимых Booking State и переходов между ними.  
**Не является:** отдельным состоянием.  
**Примеры событий:** `booking.created`, `booking.confirmed`, `booking.cancelled`, `booking.completed`.  
**Правило:** полный enum определяется профильным источником.  
**Planned canonical source:** [[Booking Lifecycle Specification]]  
**Status:** planned  
**Owner:** Booking Domain

### Appointment

**Русское название:** техническая запись на приём  
**Определение:** backend-сущность Ayla, если это имя закреплено в модели данных. Не является универсальным продуктовым термином для всего Booking lifecycle.

### Slot

**Русское название:** временной слот  
**Определение:** доступный интервал времени для Booking.

### Slot Hold

**Русское название:** удержание слота  
**Определение:** временная блокировка доступности на период завершения booking flow.

### Idempotency

**Русское название:** идемпотентность  
**Определение:** повтор одного запроса не создаёт повторное действие.

## 12. Результаты и обратная связь

### Expected User Success

**Русское название:** ожидаемый успех пользователя  
**Определение:** вероятность полезного для User результата с учётом Safety, соответствия явному Intent, реализуемости, качества исполнения и последующей Feedback.  
**Не является:** фактом создания или подтверждения Booking самим по себе.  
**Defined by:** [[Ayla Constitution]]  
**Status:** accepted  
**Owner:** Product Architecture

### Outcome

Наблюдаемое изменение или завершение сценария после действия.

### Intent Resolution

Пользователь получил полезный итог по исходному Intent.

### Understanding Resolution

Пользователь лучше понял ситуацию и следующий шаг.

### Decision Resolution

Пользователь выбрал подходящий следующий шаг.

### Execution Resolution

Выбранное действие успешно выполнено.

### Feedback

Реакция пользователя на понимание, рекомендацию, выполнение или результат.

### Outcome Feedback

Оценка фактического эффекта после действия или услуги.

### User Correction

Указание, что Ayla неверно поняла Intent, Context, Preference или другое значение.

---

## 13. Поставщики и доверие

### Provider Eligibility

Соответствие минимальным обязательным условиям участия в подборе.

### Provider Trust

Совокупность проверяемых сигналов надёжности. Не является гарантией качества.

### Verification

Подтверждение конкретных данных или статуса исполнителя.

### Qualification

Подтверждённая подготовка, право или компетенция специалиста.

### Availability Freshness

Степень доверия к тому, что отображаемые слоты доступны сейчас.

### Supply Quality

Способность доступного пула исполнителей удовлетворять намерения безопасно и с приемлемым результатом.

---

## 14. Экономическая модель

### Economic Neutrality

Коммерческая выгода Ayla не должна скрыто ухудшать полезность рекомендации.

### Commercial Blindness

Исключение запрещённых коммерческих факторов из части recommendation/ranking pipeline.

### Booking Fee

**Русское название:** плата Provider за успешную запись  
**Определение:** фиксированная плата 90 ₽ за одну completed Booking, взыскиваемая ровно один раз: через split для online-paid Booking либо через provider billing для offline-paid Booking.  
**Не является:** платой User за доступ к Ayla, процентной комиссией или основанием влиять на Recommendation.  
**Defined by:** [[Ayla Decision Log]] — AYLA-DEC-0001 и AYLA-DEC-0010  
**Status:** proposed  
**Owner:** Business / Payment Domain

### Billable Booking

**Русское название:** тарифицируемая завершённая запись  
**Определение:** Booking в состоянии `completed`, соответствующая условиям однократного взыскания Booking Fee.  
**Не является:** созданной, подтверждённой, отменённой или no-show Booking.  
**Defined by:** [[Ayla Decision Log]] — AYLA-DEC-0010  
**Status:** proposed  
**Owner:** Booking / Payment Domain

### Billable Visit

**Status:** deprecated  
**Use instead:** `Billable Booking`  
**Причина:** слово Visit не совпадает с каноническим агрегатом Booking и скрывает точное lifecycle-условие тарификации.

### Attribution

Правило определения связи конкретного визита или результата с Ayla.

### Provider Subscription

Периодическая плата Provider за инструменты Ayla Pro. Не покупает приоритет в Recommendation и не заменяет Booking Fee. Конкретные тарифы определяются [[Ayla Decision Log]], а не Glossary.

---

## 15. Архитектура

### AI Orchestrator

Компонент, управляющий пониманием, контекстом, safety, выбором действия, инструментами и формированием ответа. Не является одной LLM.

### Intent Model

Система, преобразующая ввод и контекст в Intent, Goal, slots, confidence и missing information.

### Recommendation Engine

Система, формирующая и оценивающая допустимые следующие действия.

### Safety Layer

Policy-проверки и механизмы обработки риска между пониманием и действием.

### Policy Engine

Компонент, применяющий утверждённые правила к структурированному состоянию.

### Tool

Вызываемая операция или интеграция для чтения данных или выполнения действия.

### Agent

Автономный или полуавтономный компонент для многошаговой задачи. Не следует называть агентом любую функцию с LLM.

### State Machine

Явная модель допустимых состояний и переходов процесса.

### Domain Model

Описание сущностей, правил и отношений предметной области независимо от интерфейса и БД.

### Bounded Context

Область модели со своим языком, правилами и ответственностью.

### Contract

Формальные входы, выходы, ограничения и гарантии взаимодействия компонентов.

### Source of Truth

Единственное каноническое место, где данные или решение считаются авторитетными.

---

## 16. Knowledge Architecture

### Knowledge Repository

Git-репозиторий с каноническими cross-repository документами, mirrors, schema, MOC и validation tooling.

### Canonical Document

Авторитетная версия документа.

### Mirror

Синхронизированная read-only копия канонического документа.

### External Source

Материал вне системы канонических документов Ayla. Не является автоматически утверждённым правилом.

### Map of Content

Навигационный документ со структурой области, порядком чтения и пробелами. Сокращение: MOC.

### Root MOC

Главная точка входа в knowledge repository. Канонический файл: `Ayla.md`.

### Knowledge Node

Документ или управляемый stub с `node_id`, metadata и связями.

### Planned Node

Содержательный stub будущего документа с owner, milestone, status и dependencies.

### Orphan Node

Документ без значимых входящих и исходящих связей, если это не разрешено его типом.

### Broken Link

Ссылка на отсутствующий Knowledge Node.

### Knowledge Health

Состояние консистентности, актуальности, связности и управляемости repository.

---

## 17. Управление документами

### Document Status

**Определение:** управляемое состояние Knowledge Node в документном lifecycle.

Полный перечень допустимых значений и переходов определяется
`.knowledge/schema.yaml`.

Человекочитаемые пояснения публикуются в
[[Ayla Domain and Metadata Registry]].

**Defined by:** `.knowledge/schema.yaml`  
**Status:** implemented  
**Owner:** Knowledge Owner

### Architecture Decision Record

Документ с контекстом, решением, альтернативами и последствиями. Сокращение: ADR.

### Amendment

Формальное дополнение или изменение утверждённого документа.

### Revision

Новая редакционная версия, не обязательно меняющая основное решение.

### Handoff

Временный документ со статусом реализации, проблемами и следующими действиями. Не является заменой PRD, specification или ADR.

### Runbook

Пошаговая инструкция повторяемой процедуры.

---

## 18. Metadata and relationship registries

Glossary не является источником машинных enum-значений.

Канонические источники:

- `schema.yaml` — document types, statuses, lifecycle transitions, sensitivity scales, export policies и разрешённые relationship fields;
- [[Ayla Domain and Metadata Registry]] — человекочитаемое представление schema и ownership mappings;
- [[Ayla Knowledge Architecture Specification]] — governance отношений между документами.

Термины `knowledge_area`, `domain`, `concern`, `system_owner`, `classification`, `data_sensitivity`, `security_sensitivity`, `ai_indexing`, `export_policy`, `implements`, `depends_on`, `adr`, `related`, `conflicts_with` не дублируются здесь как независимо поддерживаемые реестры.

## 19. Аналитические понятия

### Metric

Количественно определённый показатель состояния, процесса или результата.

### KPI

Метрика, по которой принимается управленческое решение и закреплена ответственность. Не является любой отображаемой цифрой.

### Guardrail Metric

Показатель, предотвращающий улучшение одной метрики ценой вреда в другой области.

### Intent Resolution Rate

Доля взаимодействий, где Intent получил полезное разрешение.

### Time to First Value

Время от начала значимого взаимодействия до первого полезного результата.

### Wrong Understanding Rate

Доля сценариев с подтверждённо неправильным пониманием Intent или ключевого Context.

### Recommendation Acceptance Rate

Доля рекомендаций, выбранных или подтверждённых пользователем.

### Outcome Confirmation Rate

Доля выполненных действий, по которым получено подтверждение результата.

---

## 20. Pilot и operations

### Pilot

Ограниченный запуск с контролируемым scope, аудиторией, supply и метриками.

### Concierge Mode

**Русское название:** режим консьержа / ручной калибровки  
**Определение:** операционный режим раннего запуска, ориентировочно для первых
100–500 пользователей, при котором рекомендации, решения и транзакционные
сценарии могут проходить ручную проверку, подтверждение или корректировку
оператором Ayla в зависимости от класса риска.  
**Режимы проверки:**

- низкорисковые сценарии могут проверяться асинхронно после выдачи;
- существенные рекомендации и сценарии высокой неопределённости могут
  требовать проверки до выдачи или выполнения;
- safety-critical сценарии немедленно обрабатываются утверждёнными
  policy-правилами и не должны зависеть от доступности оператора.

**Цель:** сбор качественных размеченных данных для калибровки, оценки и
улучшения Intent Model и Recommendation Engine, а также снижение риска
ошибочных рекомендаций до перехода к полной автоматизации.  
**Правило прозрачности:** участие оператора не скрывается, если оно существенно
влияет на результат.  
**Правило полномочий:** оператор не заменяет Consent, явное подтверждение User,
Safety Constraint, authorization или idempotency; транзакция не выполняется
только на основании ручной корректировки.  
**Не является:** постоянной заменой автоматизации.  
**Defined by:** [[Ayla User Journey Specification]]  
**Status:** proposed  
**Owner:** Pilot Operations

### Incident

Событие, нарушившее или способное нарушить безопасность, приватность, доступность или целостность.

### Knowledge Release Bundle

Согласованный набор версий документов для конкретного milestone или release.

---

## 21. Запрещённые неоднозначности

### «Клиент»

Использовать:

- `User` — в глобальном продуктовом контексте Ayla;
- `Customer` — как tenant-scoped роль User у конкретного Provider;
- «клиент» — в UI, когда контекст однозначен.

### «Мастер»

Использовать:

- `Specialist` — продуктовый термин;
- `Master` / `CatalogMaster` — принятые технические термины;
- `Provider` — самостоятельный Specialist или организация как сторона профессионального контура; не использовать как технический синоним `Master`.

### «State»

Самостоятельное нормативное употребление запрещено. Нужно указывать Human State, Journey State, User Lifecycle State, Conversation State, Booking State или Entity State.

### «Профиль»

Всегда уточнять: User Profile, Provider Profile, Profile Screen, AI Persona или User Model.

### «Рекомендация»

Не использовать для рекламного показа, списка всех вариантов, медицинского заключения или автоматически выполненного действия.

### «Память»

Не использовать как синоним истории сообщений, User Model целиком, базы данных, кэша или Session Context.

### «AI»

Не использовать как название конкретного компонента. Уточнять LLM, Intent Model, Recommendation Engine, AI Orchestrator, classifier, Policy Engine или Agent.

### «Граф»

Уточнять: Obsidian Graph View, Knowledge Graph, dependency graph, state transition graph или analytics chart.

## 22. Key term authority matrix

До материализации и принятия профильного источника planned-термин не может
повышаться до `accepted` только на основании упоминания в Glossary. На дату
ревью подтверждён `ADR-0007`; идентификаторы `ADR-0008`, `ADR-0011` и
`ADR-0012` зарезервированы как planned sources и не считаются действующими ADR.

| Term group | Defined by | Maturity | Owner |
|---|---|---|---|
| Ayla, Ayla Pro, User, Provider, Specialist | [[Ayla Constitution]] | accepted | Product Architecture |
| Customer, Master, TenantStaff | planned `ADR-0008 Role Detection and Staff Model` | planned | Identity Domain |
| Tenant | planned `Tenant as Provider Model` | planned | Platform Architecture |
| Salon | Ayla Glossary | proposed | Provider Domain |
| Conversation State | [[ADR-0007 Conversation State Enum]] | accepted | Conversation Domain |
| Journey State, User-Initiated Recommendation Gate | [[Ayla User Journey Specification]] | proposed | Product Architecture |
| Proactive Readiness Gate | [[Ayla User Journey Specification]]; planned ADR-0012 | proposed | Product Architecture |
| User Lifecycle State | [[Core User States]] | proposed | Product Architecture |
| Intent Type, Goal Category | [[Ayla Intent Model Specification]] | planned | AI Architecture |
| Recommendation concepts | [[Ayla Recommendation Engine Specification]] | planned | AI Architecture |
| Memory Source, Memory Entry | [[Memory Entry Schema]] | planned | User Context Domain |
| User Model, Consent, Safety, Safety-Critical Information | [[Ayla Constitution]] | accepted | Privacy and Safety |
| Sensitivity Zone, Cross-Provider Memory | planned `ADR-0011 User Context Privacy` | planned | Privacy and Safety |
| Dynamic User Model | planned `ADR-0012 Dynamic User Model` | planned | User Context Domain |
| Booking State, booking event names | [[Event Taxonomy]] | proposed | Booking Domain |
| Booking aggregate | Ayla Glossary / backend model | proposed | Booking Domain |
| Booking Lifecycle | [[Booking Lifecycle Specification]] | planned | Booking Domain |
| Booking Fee, Billable Booking | [[Ayla Decision Log]] | proposed | Booking / Payment Domain |
| Food Scanner | [[Ayla MVP Product Thesis]] | planned | Nutrition Domain |
| Concierge Mode | [[Ayla User Journey Specification]] | proposed | Pilot Operations |

## 23. Change process

Новый термин добавляется, если:

- используется в двух и более канонических документах;
- устраняет неоднозначность;
- представляет устойчивую domain-сущность;
- нужен для schema, API или analytics.

Изменение термина требует:

1. описания причины;
2. проверки связанных документов;
3. оценки migration impact;
4. обновления синонимов;
5. повышения версии;
6. обновления Domain Registry при необходимости.

Удаление допускается только через:

- `deprecated`;
- ссылку на замену;
- период совместимости;
- миграцию зависимых документов.

---

## 24. Ownership

### Product Architecture

Отвечает за общую терминологию, product/AI concepts и междокументные конфликты.

### Domain Owners

Отвечают за точность терминов bounded context и совместимость с кодом/API.

### Safety Owner

Проверяет safety, boundary, escalation и risk terminology.

### Knowledge Owner

Проверяет metadata, node IDs, связи и соответствие schema.

---

## 25. Definition of Done

Glossary v2.1 считается утверждённым, когда:

- согласованы базовые product terms;
- согласованы Intent и Context terms;
- согласованы Recommendation и Safety terms;
- согласованы Memory terms;
- согласованы Provider и Booking terms;
- согласованы Knowledge Architecture terms;
- Glossary не дублирует enum-реестры schema.yaml;
- Domain and Metadata Registry генерируется из schema либо валидируется против неё;
- Root MOC ссылается на Glossary;
- validator проверяет controlled vocabularies;
- отсутствуют термины с maturity выше maturity профильного источника;
- каждый accepted-термин имеет разрешимый `Defined by`;
- каждый термин authority matrix имеет ровно одну нормативную карточку;
- запрещённые неоднозначности проходят lint;
- Glossary не содержит independently maintained enum lists;
- Change Log соответствует фактическим изменениям документа.

---

## 26. Открытые вопросы

1. Использовать ли `Body Wellness` как один domain или umbrella category.
2. Разделять ли `Provider` и `Merchant` в будущей marketplace-модели.
3. ~~Нужен ли отдельный термин `Care Plan`~~ — **решено 2026-08-24 (В-6, owner ruling): нет.** Каноническое и пользовательское имя — **Personal Plan**; `Care Plan` — только рабочий alias `SPEC_CARE_CONTRACT`; `CareEpisode` категорически не использовать — имя занято другой сущностью (эпизод послепроцедурного сопровождения из AUDIT_CARE_RUNTIME).
4. Входит ли `Coach` в Specialist.
5. Как назвать пользовательский экран памяти: «Что Ayla знает обо мне» или иначе.
6. Нужен ли отдельный `Clinical Boundary`.
7. Разделять ли `Recommendation` и `Guidance`.
8. Как обозначать оплаченную, но ещё не подтверждённую Booking.

---

## 27. Следующие документы

1. [[Ayla Domain and Metadata Registry]]
2. [[Ayla Intent Model Specification]]
3. [[Ayla Recommendation Engine Specification]]
4. [[Ayla Safety and Boundary Specification]]
5. [[Ayla Analytics Event Taxonomy]]

---

# Change Log

## v2.2 — 2026-08-25

- закрыт открытый вопрос §26.3 по решению владельца В-6 (2026-08-24,
  `docs/OD_CARE_CONTRACT_RULINGS.md`): отдельный термин `Care Plan` не
  вводится; каноническое имя — **Personal Plan**; `Care Plan` — рабочий
  alias рабочей спецификации; `CareEpisode` запрещено (имя занято другой
  сущностью).

## v2.1 — 2026-07-19

- удалён неполный список Document Status; источником enum оставлена schema;
- восстановлено полное определение Concierge Mode для первых 100–500
  пользователей с risk-based post-hoc, pre-flight и hard policy modes,
  прозрачностью и ограничением полномочий ручного участия;
- User-Initiated Recommendation Gate отделён от Proactive Readiness Gate;
- Journey State, оба gate-термина и Concierge Mode оставлены proposed до
  approval профильного Journey и принятия ADR-0012;
- Booking State отделён от Booking Lifecycle;
- уточнены current и planned источники Booking terminology;
- полный шаблон заменён выполнимым canonical term contract с минимальными и
  условно обязательными полями;
- User Lifecycle State понижен до proposed до материализации источника;
- `UserPersonalContext` оформлен как code name термина User Personal Context;
- Definition of Done дополнен проверяемыми условиями.

## v2.0 — 2026-07-18

- канонический документ перенесён в отдельный `ayla-knowledge` со стабильным filename и `node_id`;
- значение Provider согласовано с Constitution: самостоятельный Specialist или организация;
- добавлены конституционные термины Ayla Pro, Substantial Recommendation, Safety-Critical Information и Expected User Success;
- User Model и Consent приведены к управляемой пользователем, purpose-scoped модели Constitution;
- технические термины без найденных ADR-источников понижены из accepted в planned;
- Safety отделена от коммерческого и репутационного риска компании;
- Billable Visit deprecated в пользу Billable Booking, а Booking Fee согласована с AYLA-DEC-0010;
- versioned wikilinks заменены стабильными canonical links;
- зафиксирован provenance untracked source-файла из `beautygo_backend`.

## v1.2 — 2026-07-18

- Glossary интегрирован с schema v1.3 и Knowledge Architecture v1.2;
- maturity-статусы синхронизированы с фактическими статусами источников;
- `mixed` удалён из term maturity;
- материализованы planned/source-placeholder knowledge nodes;
- исправлены wikilinks, нумерация и имя Domain and Metadata Registry;
- история первоначального stub сохраняется через Git без фиктивного superseded node.

## v1.1 — 2026-07-18

- frontmatter приведён к schema v1.2;
- тип изменён на нормативный `terminology-standard`;
- schema, Registry и Glossary разделены по источникам истины;
- разведены квалифицированные State;
- согласованы User, Customer, Provider, Tenant, Specialist, Master и TenantStaff;
- исправлена Booking lifecycle terminology;
- расширена memory/privacy taxonomy;
- разделены Intent Type и Goal Category;
- разделены Readiness Level, Readiness Gate и Suppression Factor;
- добавлены Food Scanner и Helpful Restraint;
- усилено определение Concierge Mode;
- добавлена матрица источников, зрелости и владельцев.

## v1.0 — 2026-07-18

- создан первый канонический словарь Ayla;
- определены product, AI, safety, memory, provider, booking и knowledge-термины;
- добавлены controlled vocabularies;
- зафиксированы запрещённые неоднозначности;
- определён процесс изменения Glossary.

---

# Approval

**Status:** Review  
**Founder:** Андрей Тихонов  
**Product Architecture:** __________________  
**Safety Owner:** __________________  
**Approval date:** __________________  
**Decision reference:** __________________
