---
node_id: ayla.product.mvp-user-journey
title: Ayla MVP User Journey Specification
type: user-journey-specification
status: draft
decision_status: proposed
version: "0.3"
owner: Product Owner
priority: P0
knowledge_area:
  - product
domain:
  - cross-domain
concerns:
  - privacy
  - safety
system_owner:
  - ayla-knowledge
source_repository: ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
created: 2026-07-27
updated: 2026-07-28
review_cycle: monthly
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla User Journey Specification]]"
  - "[[Ayla MVP Scope and Release Contract]]"
  - "[[Ayla MVP Documentation Roadmap]]"
related:
  - "[[Consent Scope Registry]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Killer PRD]]"
---

# Ayla MVP User Journey Specification

> **Статус:** Draft v0.3-final — proposed. Это **не канонизация**: документ
> является производным MVP-срезом [[Ayla User Journey Specification]] по
> решению AYLA-DEC-0014 ([[Ayla MVP Documentation Roadmap]] §2.1) и не
> заменяет полную спецификацию. Нормативную силу документ получает только
> после approval Product Owner; до этого все положения имеют статус
> `proposed`.
>
> **Соглашение о метках.** Утверждения, дословно или близко следующие из
> канонических источников, помечены как *(факт — источник §)*. Предложения,
> не зафиксированные в источниках, помечены **(proposal)** и подлежат
> review. Незакрытые решения собраны в Open Questions; вопросы, выходящие
> за полномочия этого документа (изменение approved-источников), помечены
> как **upstream**.

## Purpose

Назначение документа (основание — [[Ayla MVP Documentation Roadmap]] §2.1):

- зафиксировать единственный обязательный сквозной сценарий MVP
  ([[Ayla MVP Scope and Release Contract]] §3) в виде 14 этапов с полями
  actor, trigger, пользовательская цель, системное действие, отображаемое
  состояние, ошибка, fallback, события, owning capability;
- описать обязательные негативные сценарии и их поведение;
- связать каждый этап с owning capability (CAP-ID по
  [[Ayla Domain Capability Registry]] §6) и consent-правилами
  ([[Consent Scope Registry]]);
- дать frontend, backend и AI-команде одну трактовку пользовательского
  потока, чтобы они не реализовывали один бизнес-процесс по-разному
  (Roadmap, вводная часть);
- **(proposal, v0.2)** зафиксировать, как Ayla извлекает, проверяет и
  применяет разрешённый персональный контекст на протяжении всего journey,
  а не только на этапе 6;
- **(proposal, v0.2)** определить замкнутый цикл памяти: context retrieval →
  recommendation use → explanation → outcome → memory proposal → user
  confirmation → context update;
- **(proposal, v0.2)** обеспечить, чтобы повторное взаимодействие становилось
  полезнее первого, не создавая скрытого profiling, устаревшей
  персонализации, cross-tenant contamination или lock-in на прошлые решения;
- **(proposal, v0.2)** определить Product Thesis Validation Scenario
  (см. Memory Interaction), без которого основная продуктовая гипотеза Ayla
  не считается проверенной. Статус этого критерия определён решением
  AYLA-DEC-0018 (accepted, Option C): он не является release gate Phase 1 —
  Product Thesis Validation остаётся открытой до Phase 2.

Документ **не** описывает все будущие journeys: долгосрочные состояния
(S7 Long-term), доменные journeys (Nutrition Guidance), проактивные сценарии
и полная state machine остаются в [[Ayla User Journey Specification]] и здесь
не дублируются (см. Non-goals).

Целевая аудитория: продуктовая команда, AI-команда, backend/frontend
разработчики, QA.

## Journey Operating Model

Факты из источников:

- **Один сквозной сценарий** (дословно, Roadmap §1.2 = Scope Contract §3):
  пользователь выражает потребность → Ayla уточняет intent → подбирает услугу
  или действие → объясняет рекомендацию → пользователь подтверждает → Ayla
  создаёт запись → пользователь получает подтверждение.
- **Одна канальная платформа:** MAX (бот + Mini App) — единственные
  обязательные каналы MVP (Scope Contract §7, AYLA-DEC-0004). Telegram — вне
  пилотного scope.
- **Два activation gate** ([[Consent Scope Registry]] §10): MVP Phase 1 —
  session-only vertical slice без персистентной памяти; MVP Phase 2 — opt-in
  persistent preferences. Phase 2 не является условием релиза Phase 1.
  Соответствие этой модели memory-first продуктовому тезису определено
  решением AYLA-DEC-0018 (accepted, Option C): Phase 1 — самостоятельный
  технический release gate; Product Thesis Validation открыта до Phase 2.
- **Автономные действия без подтверждения пользователя запрещены** (Roadmap
  §1.2 out of scope; Конституция).
- **Fail-closed по умолчанию** ([[Consent Scope Registry]] §2): неизвестный,
  отсутствующий, просроченный или неутверждённый scope обрабатывается как
  запрет; отсутствие consent record не интерпретируется как согласие.
- **Один primary recommendation**, до двух alternatives — только по запросу
  или после отклонения primary, каждая с собственным `recommendation_id`
  (факт — [[Killer PRD]] §5.1).
- Journey не строго линейна: пользователь может уточнять intent и менять
  решение; обратные переходы (уточнение, «давай другую опцию») допустимы
  (факт — полная UJS, State Transitions).

Принципы operating model, добавленные в v0.2 (**proposal**):

- **Personal Context Management (CAP-001) — сквозная capability** всего
  journey наряду с CAP-014 (Safety), CAP-018 (Orchestration) и CAP-026
  (Audit), а не только owning capability этапа 6. Этап 6 фиксирует
  обязательную recommendation-time проверку контекста, но не является
  единственной точкой извлечения.
- **Контекст может извлекаться на нескольких точках:** session context
  bootstrap (этап 2), intent disambiguation (этап 4), clarification
  suppression — не спрашивать известное повторно (этап 5),
  recommendation-time retrieval (этап 6), execution context (этапы 10–11),
  outcome interpretation (этап 14). Нумерация этапов 4–6 отражает
  пользовательскую ответственность, а не обязательный однопроходный порядок
  исполнения: intent detection, context retrieval и clarification могут
  итерироваться.
- **Каждое использование контекста — в пределах активного scope** (факт —
  CSR §2); сквозная роль памяти не расширяет разрешённый доступ: принцип —
  максимально полезное использование минимально необходимого разрешённого
  контекста.

Роли (actors) в сценарии:

| Actor | Описание |
|---|---|
| User | Клиент, ищущий услугу или специалиста (персона пилота, Scope Contract §2) |
| Ayla (AI) | Диалоговая логика: ai-bot-platform (runtime/channel consumer) + ayla-ai-core (reusable AI logic) — факт, Roadmap §5.1 |
| Backend | beautygo_backend — SoR для каталога, провайдеров, availability, записей, consent, context facts (факт — Scope Contract §6) |
| Provider | Соло-мастер или малый салон (≤3 мастеров), подтверждающий запись (персона пилота, Scope Contract §2) |

## Journey Overview

14 обязательных этапов (порядок и состав — дословно Roadmap §2.1). Маппинг
на состояния полной UJS приведён для трассируемости и не расширяет scope.

| # | Этап | Соответствие полной UJS | Owning capability (proposal) |
|---|---|---|---|
| 1 | Entry | S0 Acquisition → S1 First Contact | CAP-016 |
| 2 | First interaction | S1 First Contact | CAP-016 |
| 3 | Consent request | Consent-шаги S1–S6 | CAP-002 |
| 4 | Intent detection | S3 Intent Understanding | CAP-003 |
| 5 | Clarification | S2 Discovery / S3 | CAP-003 |
| 6 | Context retrieval | S2/S3 Memory Lookup | CAP-001 |
| 7 | Recommendation | S4 Recommendation Layer | CAP-004 |
| 8 | Explanation | S4 (Explanation) | CAP-005 |
| 9 | User confirmation | S4 → S5 переход | CAP-004 |
| 10 | Availability selection | S5 Execution (slots) | CAP-010 |
| 11 | Booking creation | S5 Execution (Booking) | CAP-011 |
| 12 | Booking confirmation | S5 Confirmation | CAP-011 |
| 13 | Notification | S5/S6 уведомления | CAP-021 |
| 14 | Outcome or feedback prompt | S6 Feedback Loop | CAP-006 |

> Маппинг CAP-ID — **proposal**: по [[Ayla MVP Scope and Release Contract]] §4
> он остаётся предложением до перевода записей Registry в MVP-active
> (волна 2, AYLA-DEC-0014). Enabling capabilities CAP-014 (Safety Policy
> Enforcement), CAP-018 (AI Orchestration and Tool Execution) и CAP-026
> (Audit and Observability) действуют сквозным образом на всех этапах
> (факт — Scope Contract §4.2) и не дублируются в каждой строке. В v0.2 к
> сквозным capability **(proposal)** добавлена CAP-001 (Personal Context
> Management) — см. Journey Operating Model.

Сквозная цепочка (пользовательский слой):

```text
Entry → First interaction → Consent request → Intent detection
→ Clarification → Context retrieval → Recommendation → Explanation
→ User confirmation → Availability selection → Booking creation
→ Booking confirmation → Notification → Outcome or feedback prompt
```

Этап 3 (Consent request) — не обязательно отдельный экран: в Phase 1
обработка текущего сообщения выполняется по `service_necessity` без
consent record (факт — [[Consent Scope Registry]] §3 «Разграничение session
use и persistent consent»); явный запрос согласия требуется только для
persistence, проактивности и передачи данных для другой цели.

Сквозной memory loop (**proposal**, v0.2 — детали в Memory Interaction):

```text
Session context bootstrap
→ Targeted retrieval
→ Context sufficiency check
→ Recommendation-time application
→ Explanation of context use
→ Outcome capture
→ Memory Proposal
→ User confirmation
→ Context Fact create / correct / supersede
→ Next journey
```

## Stage Specifications

Формат полей каждого этапа — по Roadmap §2.1: actor, trigger,
пользовательская цель, системное действие, отображаемое состояние, ошибка,
fallback, owning capability и события. «Отображаемое состояние» использует
терминологию продуктовых состояний MVP UX State Contract (Roadmap §2.2, P1,
planned): loading, clarification required, recommendation ready, no
recommendation, consent required, slot unavailable, booking pending, booking
confirmed, booking failed, retry, human handoff. Коды ошибок — по перечню
Error and Reason Code Registry (Roadmap §6.5, planned).

Поле событий разделено на **три класса с разными владельцами контрактов**
(v0.1.1; не в каждом этапе присутствуют все три):

- **domain event** — изменение authoritative business state; перечень —
  Roadmap §6.4 (planned Domain Event Registry, P1);
- **analytics event** — измерение поведения и funnel; рабочие имена,
  proposal — до Analytics Event Contract (informative — CSR §9.2);
- **audit event** — consent, authorization и policy checks; канонический
  перечень — [[Consent Scope Registry]] §9.1.

Именование событий (v0.3-final): конвенция и правила установлены решением
AYLA-DEC-0025 (lowercase dot-separated past-tense; две оси классификации
`semantic_class` × `publication_scope`; один authoritative producer);
канонический реестр создан (`05 Architecture/Ayla Domain Event
Registry.md`, v0.2). **Миграция выполнена только для active canonical
event names** (owner ruling 2026-07-28): `consent.*`,
`intent.resolution_produced`, `appointment.*` (этапы 3, 4, 11, 12, 14);
legacy-формы указаны справочно. Имена pending-семейств
(`recommendation.*`, `qualified_action.*`, `memory.*`) **не мигрированы**
и сохранены по источникам (Roadmap §6.4, CSR §9.1) до утверждения
соответствующих записей реестра; отсутствующие события не выдумываются
(registry gaps — Open Question №8).

### Этап 1. Entry

| Поле | Значение |
|---|---|
| actor | User |
| trigger | Пользователь открывает MAX-бот (DM) или переходит по deep link в Mini App (факт — полная UJS, Stage 1 Entry Points) |
| пользовательская цель | Получить помощь с beauty/wellness-потребностью без поиска по каталогу |
| системное действие | Показать приветствие с выбором категории состояния и возможностью свободного ввода (факт — полная UJS, Stage 1 First Message) |
| отображаемое состояние | Приветственное сообщение + кнопки категорий + поле ввода |
| ошибка | Канал недоставляет сообщение / сбой платформы MAX |
| fallback | Повторная доставка при следующем открытии; без альтернативного канала в MVP (Telegram — out of scope) **(proposal)** |
| analytics event | `session_started` **(proposal)** |
| owning capability | CAP-016 — Conversation Experience |

Ограничения (факт — полная UJS, Stage 1 Forbidden Behavior): не запрашивать
имя, возраст, вес при первом контакте; не начинать с анкеты; не продавать.

### Этап 2. First interaction

| Поле | Значение |
|---|---|
| actor | User → Ayla |
| trigger | Пользователь выбрал категорию или написал свободный запрос |
| пользовательская цель | Выразить потребность своими словами и быть понятым |
| системное действие | Принять сообщение; подтвердить получение; начать обработку в session-only режиме. **(proposal, v0.2)** Session context bootstrap: поднять контекст текущей сессии и — при активном `preference_memory` (Phase 2) — проверить наличие релевантных актуальных фактов до ответа, не показывая их без необходимости |
| отображаемое состояние | loading → первый содержательный ответ Ayla |
| ошибка | `MODEL_UNAVAILABLE` — LLM-провайдер недоступен |
| fallback | model/provider fallback, определённый в Release Readiness (факт — Roadmap §9.1); при полной недоступности — честное сообщение о сбое и предложение вернуться позже (факт — полная UJS, Error Recovery 3) |
| analytics event | `first_message_received` **(proposal)** |
| owning capability | CAP-016 — Conversation Experience |

### Этап 3. Consent request

| Поле | Значение |
|---|---|
| actor | Ayla → User |
| trigger | Наступление операции, требующей согласия: сохранение предпочтения между сессиями (Phase 2, scope `preference_memory`), иное использование за пределами текущей сессии (факт — [[Consent Scope Registry]] §3, §5.7) |
| пользовательская цель | Понять, зачем запрашиваются данные, и сохранить контроль |
| системное действие | Запросить согласие с указанием цели (scope), а не факта «сохранить данные»; дать возможность отклонить без прерывания диалога (факт — CSR §8 UX Requirements) |
| отображаемое состояние | consent required |
| ошибка | Отсутствие, отказ или отзыв consent → **fail-closed**: операция не выполняется (факт — CSR §2) |
| fallback | Session-only обработка без сохранения (факт — CSR §5.7: «без него — данные не сохраняются, только session-only обработка»); сценарий продолжается |
| audit event | `consent_granted` / `consent_denied` / `consent_revoked` (факт — CSR §9.1; audit — проекция/consumer доменных событий consent, не конкурирующая форма канона — AYLA-DEC-0025) |
| domain event | `consent.granted` / `consent.revoked` (канон — AYLA-DEC-0025 / Domain Event Registry v0.2 §6.2; legacy: `ConsentGranted`, `ConsentRevoked`) |
| owning capability | CAP-002 — Consent Management |

В Phase 1 этот этап не показывает диалог согласия для понимания текущего
запроса: `intent_understanding` и `provider_selection` работают по
`service_necessity` в пределах сессии (факт — CSR §5.1/§5.2). Persistent
memory в Phase 1 технически отключена (факт — CSR §10.1).

### Этап 4. Intent detection

| Поле | Значение |
|---|---|
| actor | Ayla |
| trigger | Получено пользовательское сообщение с потребностью |
| пользовательская цель | Чтобы Ayla поняла, чего пользователь хочет достичь, а не только что написал (Query vs Intent — факт, полная UJS Stage 3) |
| системное действие | Извлечь intent и slots из сообщения; определить confidence; проверить safety constraints до перехода к рекомендации (факт — полная UJS, Stage 3 Intent Extraction / Safety Check). Поддерживаемые intent types, required/optional slots и confidence levels определяет Ayla Intent Model Specification (planned, Roadmap §3.1 — документ в разработке, не материализован). **(proposal, v0.2)** Для разрешения ссылок на прошлый опыт («как в прошлый раз», «к ней», «снова») допускается targeted memory retrieval до окончательного разрешения intent — в пределах активного scope |
| отображаемое состояние | Формулировка понимания с уровнем уверенности через язык (факт — полная UJS, Stage 3 Confidence) |
| ошибка | `INTENT_UNRESOLVED` — intent не распознан или confidence ниже порога |
| fallback | Переход к этапу 5 (Clarification); при повторной неудаче — см. Negative Scenarios №1 |
| domain event | `intent.resolution_produced` (канон — AYLA-DEC-0025 / Domain Event Registry v0.2 §6.1; результат — в payload `resolution_status`; legacy: `IntentResolved`) |
| owning capability | CAP-003 — Intent Understanding |

Минимальный набор intent types (факт — Roadmap §3.1): DISCOVER_SERVICE,
FIND_SPECIALIST, BOOK_APPOINTMENT, RESCHEDULE_APPOINTMENT,
CANCEL_APPOINTMENT, ASK_ABOUT_SERVICE, ASK_ABOUT_PRICE,
ASK_ABOUT_AVAILABILITY, PROVIDE_CONTEXT, CORRECT_CONTEXT, REVOKE_CONSENT,
UNKNOWN.

### Этап 5. Clarification

| Поле | Значение |
|---|---|
| actor | Ayla ↔ User |
| trigger | `requires_clarification`: недостаточно обязательных слотов или низкий confidence (факт — Roadmap §3.1 output contract; полная UJS, Context Sufficiency Gate) |
| пользовательская цель | Ответить на минимум вопросов и получить решение, а не анкету |
| системное действие | Задать минимально необходимый вопрос; не более 5 вопросов за сессию Discovery (факт — полная UJS, Stage 2 Maximum Questions); при отказе отвечать — продолжить с имеющимся контекстом, обозначив неопределённость (факт — полная UJS, Handling Incomplete Answers). **(proposal, v0.2)** Clarification suppression: не задавать вопрос, ответ на который уже содержится в актуальном разрешённом факте; устаревший или конфликтующий факт не заменяет уточнение (см. Memory Interaction, Context Sufficiency Model) |
| отображаемое состояние | clarification required |
| ошибка | Пользователь не отвечает / отвечает односложно / противоречиво |
| fallback | Переформулировать вопрос с примерами; fast path «просто запиши меня» не обходит safety evaluation и явное подтверждение действия (факт — полная UJS, Context Sufficiency Gate) |
| analytics event | `clarification_requested` **(proposal)**; вклад в clarification rate (факт — Roadmap §9.2) |
| owning capability | CAP-003 — Intent Understanding |

### Этап 6. Context retrieval

| Поле | Значение |
|---|---|
| actor | Ayla (ai-bot-platform → Backend) |
| trigger | Intent resolved; требуется контекст для подбора. **(proposal, v0.2)** Это обязательная recommendation-time проверка контекста, но не единственная точка извлечения — см. Journey Operating Model |
| пользовательская цель | Чтобы Ayla учитывала только то, что пользователь разрешил |
| системное действие | Получить разрешённый контекст: в Phase 1 — только session context текущего диалога; в Phase 2 — дополнительно persistent preferences при активном `preference_memory` consent (факт — CSR §5.1/§5.2/§5.7, §10). В prompt передаются только данные, разрешённые активным scope и необходимые для конкретного запроса (факт — CSR §2 п. 8). **(proposal, v0.2)** Результат оформляется как Context Sufficiency Summary (см. Memory Interaction) |
| отображаемое состояние | Не отображается напрямую; результат виден в объяснении рекомендации (этап 8) |
| ошибка | `CONTEXT_NOT_ALLOWED` — запрошенный контекст не разрешён scope (fail-closed deny, факт — CSR §2) |
| fallback | Session-only режим без persistent контекста; рекомендация формируется только по текущему диалогу (факт — CSR §5.7 fallback) |
| audit event | `authorization_scope_checked`, `context_read_allowed` / `context_read_denied`, `memory_fact_used` (факт — CSR §9.1) |
| owning capability | CAP-001 — Personal Context Management |

Whitelist допустимых персональных фактов: каноническая форма — категориальный
whitelist AYLA-DEC-0023 (категории со статусом allowed / requires dedicated
consent / forbidden, наследование политики полями, расширение — только owner
decision). Плоский список Roadmap §3.4 = Scope Contract §4.1 п. 8 —
**superseded, non-normative historical reference** (Change Control
2026-07-28); позиция «согласие на персонализацию» из него исключена
(Consent state ≠ Context Fact — см. Memory Interaction). Inferred signals не
сохраняются и не используются как самостоятельное основание рекомендации
(факт — CSR §5.7 Prohibited; полная UJS, MVP Memory Heuristic; единственный
pipeline inference → confirmation → persist — факт, AYLA-DEC-0023 п. 2).

### Этап 7. Recommendation

| Поле | Значение |
|---|---|
| actor | Ayla (ayla-ai-core Recommendation Composer) |
| trigger | Intent resolved + разрешённый контекст получен |
| пользовательская цель | Получить один понятный следующий шаг, а не каталог |
| системное действие | Выполнить decision pipeline: consent/privacy gate → safety gate → eligibility/availability → relevance → preference boost → economic-neutrality check → primary output (факт — [[Killer PRD]] §5.1). Сформировать одну primary recommendation с `recommendation_id`; кандидат, исключённый на любом этапе, не возвращается (факт — там же). **(proposal, v0.2)** Роль памяти не сводится к preference boost — см. Recommendation and Proactivity Gates, «Memory influence model» |
| отображаемое состояние | recommendation ready (одна карточка primary); no recommendation — если кандидатов не осталось |
| ошибка | `NO_CANDIDATES`; `SAFETY_BLOCKED`; `ranking_economic_neutrality_alert` (внутренний policy/observability alert, не user-facing ошибка: блокирует выдачу до разбора — факт, Killer PRD §5.2/§5.3) |
| fallback | При `NO_CANDIDATES` — честное состояние no recommendation + обычный поиск/запись без персонализированной primary (факт — Killer PRD §5.3 Fallback); при safety-блокировке — S8 Boundary Handling (см. Negative Scenarios №8) |
| domain event | `RecommendationShown` (факт — Roadmap §6.4; семейство `recommendation.*` намеренно не зарегистрировано — семантика pending, AYLA-DEC-0025 п. 8) |
| analytics event | `recommendation_created` (informative — CSR §9.2, владелец схемы — Killer PRD; candidate до Domain Event Registry) |
| owning capability | CAP-004 — Recommendation Formation |

Персистентность рекомендации и expiry/invalidation определяются MVP
Recommendation Contract (planned, Roadmap §3.2).

### Этап 8. Explanation

| Поле | Значение |
|---|---|
| actor | Ayla → User |
| trigger | Primary recommendation сформирована |
| пользовательская цель | Понять, почему предложено именно это |
| системное действие | Показать объяснение «почему эта рекомендация» и какой разрешённый контекст применён (факт — Scope Contract §4.1 п. 9; Конституция Ст. VII). Объяснение соответствует фактически использованному контексту, не заявляет неиспользованные факты и не раскрывает sensitive context (факт — Capability Registry §6.5, key invariants CAP-005). **(proposal, v0.2)** Персонализация, которую Ayla не может объяснить пользователю, недопустима (см. Non-goals) |
| отображаемое состояние | Карточка рекомендации с объяснением (inline attribution применённого контекста — факт, Killer PRD §6.1 п. 3) |
| ошибка | Объяснение не может быть сформировано без раскрытия запрещённого контекста |
| fallback | Редактированное (redacted) объяснение только по разрешённым фактам; без объяснения рекомендация не показывается **(proposal)** |
| analytics event | `recommendation_explanation_rendered` (informative — CSR §9.2) |
| owning capability | CAP-005 — Explanation and Context Attribution |

### Этап 9. User confirmation

| Поле | Значение |
|---|---|
| actor | User → Ayla |
| trigger | Пользователю показана рекомендация с объяснением |
| пользовательская цель | Контролировать действие: ничего не происходит без явного согласия |
| системное действие | Ожидать явное подтверждение; без него не создавать запись (факт — Roadmap §1.2: автономные действия без подтверждения — out of scope). После первого отклонения primary — зафиксировать `rerank_reason` и предложить alternative в пределах установленного лимита (одновременно не более одной primary и до двух alternative — факт, Killer PRD §5.1). После повторного или явно жёсткого отказа дальнейшие предложения подавляются: принять отказ без давления (факт — полная UJS, Proactive Suppression Rules / User Communication) |
| отображаемое состояние | recommendation ready + CTA подтверждения; после отказа — нейтральное acknowledgement |
| ошибка | Пользователь отклоняет или игнорирует предложение |
| fallback | Отказ — валидный исход: после окончательного (повторного или жёсткого) отказа Ayla не предлагает новых вариантов и не инициирует повторное (факт — полная UJS, User Communication); см. Negative Scenarios №9 |
| domain event | `RecommendationAccepted` (факт — Roadmap §6.4; семейство `recommendation.*` намеренно не зарегистрировано — семантика pending, AYLA-DEC-0025 п. 8) |
| analytics event | `recommendation_dismissed` (informative — CSR §9.2) |
| owning capability | CAP-004 — Recommendation Formation (acceptance как часть lifecycle рекомендации; доставка UX — CAP-016) |

### Этап 10. Availability selection

| Поле | Значение |
|---|---|
| actor | User ↔ Ayla ↔ Backend |
| trigger | Пользователь подтвердил рекомендацию |
| пользовательская цель | Выбрать удобное время |
| системное действие | Запросить актуальные слоты у Backend (SoR availability, факт — Scope Contract §6); показать доступные варианты. Displayed slot не является reservation; slot проверяется при commit booking (факт — Capability Registry §6.10, key invariants CAP-010). **(proposal, v0.2)** Execution context: при показе слотов учитывать актуальные разрешённые факты (предпочтение времени, прошлый мастер), не скрывая альтернатив (anti-lock-in, см. Memory Interaction). **Slot hold (факт — AYLA-DEC-0021 п. 3, v0.3-final):** при выборе слота пользователем выполняется цепочка «slot selected → hold acquired → confirmation in progress»; hold создаётся с серверным `expires_at` (TTL 15 минут — платформенный параметр); hold не показывается пользователю до его фактического создания; внутренние термины (ledger, locking, reservation boundary) пользователю не отображаются |
| отображаемое состояние | Список слотов; slot unavailable — если слотов нет; после выбора — «Слот временно закреплён за вами до HH:MM. Завершите запись в течение 15 минут» (время — серверный `expires_at`, факт — AYLA-DEC-0021) |
| ошибка | `NO_AVAILABLE_SLOTS` |
| fallback | Предложить альтернативу: другой мастер или другое время (факт — полная UJS, Error Recovery 1); см. Negative Scenarios №4 |
| analytics event | `availability_requested` / `slots_shown` **(proposal)** |
| owning capability | CAP-010 — Availability Management |

### Этап 11. Booking creation

| Поле | Значение |
|---|---|
| actor | Ayla → Backend |
| trigger | Пользователь выбрал слот |
| пользовательская цель | Чтобы запись была создана ровно одна и на выбранных условиях |
| системное действие | Вызвать tool `create_appointment` (минимальный набор tools — факт, Roadmap §6.3); Backend создаёт Appointment и возвращает фактическое состояние; Booking Request, Booking Created и Confirmed Booking не взаимозаменяемы (legacy-цитата — полная UJS, Stage 5 Booking). **Подтверждение hold (факт — AYLA-DEC-0021 п. 3, v0.3-final):** цепочка «slot selected → hold acquired → confirmation in progress» завершается одной транзакцией — заблокировать hold, проверить статус и серверный TTL, повторно проверить актуальные Rule/Block/external busy, создать Appointment, перевести hold в `confirmed` |
| отображаемое состояние | booking pending (confirmation in progress; hold-индикатор из этапа 10 остаётся до результата) |
| ошибка | `APPOINTMENT_CONFLICT`, `TOOL_TIMEOUT`, `APPOINTMENT_NOT_CONFIRMED`, `SLOT_TAKEN` (факт — AYLA-DEC-0021 п. 3: нарушение занятости при confirm), hold expired (истёкший hold не подтверждается — факт, там же) |
| fallback | После expiry hold — отключить подтверждение и предложить повторную проверку доступности (факт — AYLA-DEC-0021); при нарушении занятости — понятный пользователю `SLOT_TAKEN` без внутренних терминов; показать booking failed с честным описанием и recovery path: повторить, выбрать другой слот, записаться позже (факт — полная UJS, Error Recovery 3; Success Criteria — «пользователь получил честное описание ошибки и Recovery path»); см. Negative Scenarios №6–7 |
| domain event | `appointment.created` (канон — AYLA-DEC-0025 / Domain Event Registry v0.2 §6.3; legacy: `AppointmentCreated`, `booking.*`) |
| owning capability | CAP-011 — Appointment Management |

### Этап 12. Booking confirmation

| Поле | Значение |
|---|---|
| actor | Backend / Provider → Ayla → User |
| trigger | Backend подтвердил переход Appointment в authoritative `confirmed` state (hold → `confirmed`, факт — AYLA-DEC-0021 п. 3) |
| пользовательская цель | Получить достоверное подтверждение (кто, когда, где) |
| системное действие | Показать user-facing confirmation только после получения authoritative confirmed state (факт — полная UJS, Stage 5 Booking); подтвердить детали и предложить напоминание (факт — полная UJS, Confirmation) |
| отображаемое состояние | booking confirmed |
| ошибка | Провайдер не подтверждает / отклоняет запись → `APPOINTMENT_NOT_CONFIRMED` |
| fallback | Не показывать подтверждение неподтверждённой записи (факт — полная UJS, Success Criteria: «Ayla подтвердила только фактически достигнутое состояние»); предложить альтернативный слот/мастера **(proposal)**; см. Negative Scenarios №6 |
| domain event | `appointment.confirmed` (канон — AYLA-DEC-0025 / Domain Event Registry v0.2 §6.3; legacy: `AppointmentConfirmed`); при соблюдении условий — `QualifiedActionAttributed` с `recommendation_id` (факт — Roadmap §6.4; семантика `qualified_action.attributed` pending, AYLA-DEC-0025 п. 8; правила атрибуции — Killer PRD §6.2) |
| analytics event | `booking_confirmation_shown` **(proposal — legacy-маркер; канонического analytics event в Domain Event Registry v0.2 нет, registry gap зарегистрирован в Open Question №8)** |
| owning capability | CAP-011 — Appointment Management |

Подтверждённая запись в пределах attribution window может составить
`killer_moment` при выполнении всех пяти условий (факт — Killer PRD §6.1);
последующая отмена не удаляет историческое событие (факт — Killer PRD §6.3
«Отмена записи»).

### Этап 13. Notification

| Поле | Значение |
|---|---|
| actor | Ayla → User |
| trigger | Подтверждение записи; приближение времени записи (напоминание, если пользователь его запросил на этапе 12) |
| пользовательская цель | Не забыть о записи; иметь детали под рукой |
| системное действие | Отправить транзакционное уведомление по записи (факт — Scope Contract §4.1 п. 10: Notification — транзакционные уведомления по записи) |
| отображаемое состояние | Уведомление в MAX-боте |
| ошибка | Недоставка уведомления |
| fallback | Детали записи доступны по запросу в диалоге и в Mini App **(proposal)**; повторная отправка по retry policy notification-контура **(proposal)** |
| analytics event | `notification_sent` / `notification_failed` **(proposal)** |
| owning capability | CAP-021 — Notification Coordination |

Проактивные уведомления вне транзакционного контура записи в MVP не
выполняются: Phase 1 работает в режиме no proactive recommendations
(факт — CSR §10).

### Этап 14. Outcome or feedback prompt

| Поле | Значение |
|---|---|
| actor | Ayla → User |
| trigger | Время записи прошло (запись состоялась или завершилась); надёжный доменный триггер — см. Open Question №8 |
| пользовательская цель | Быстро оценить результат одним действием |
| системное действие | Спросить, как прошло, с прогрессивным раскрытием (базовая оценка → при негативе уточнение причины) (факт — полная UJS, Stage 6 Feedback Collection). Feedback создаёт только Memory Proposal; persistent memory обновляется после sensitivity/purpose check и проверки применимого consent (факт — полная UJS, Memory Proposal). **(proposal, v0.2)** Этап 14 — не конец journey, а вход в Memory Evaluation and Update (см. Memory Interaction): outcome интерпретируется, классифицируется и — после подтверждения пользователя — становится входом следующего journey |
| отображаемое состояние | Сообщение с вариантами оценки |
| ошибка | Пользователь не отвечает — молчание не интерпретируется как согласие или отрицание (факт — полная UJS, Learning Signals) |
| fallback | Не повторять prompt навязчиво; feedback остаётся опциональным **(proposal)** |
| domain event | `appointment.completed` (канон — AYLA-DEC-0025 / Domain Event Registry v0.2 §6.3, `semantic_status: incomplete` до Appointment Contract) — входной доменный триггер этапа, не событие самого feedback prompt; `ContextFactCorrected` при коррекции контекста (факт — Roadmap §6.4; candidate mapping `memory.entry_superseded` по AYLA-DEC-0024 п. 4 — не мигрировано до подтверждения записи реестра) |
| analytics event | `feedback_received` **(proposal)** |
| owning capability | CAP-006 — Outcome Capture (в MVP — только простой feedback prompt; advanced outcome learning deferred — факт, Scope Contract §5) |

## Negative Scenarios

Состав обязателен (факт — Roadmap §2.1). Для каждого сценария: триггер,
поведение системы, пользовательское состояние, owning capability.
Коды ошибок — по Roadmap §6.5 (planned Error and Reason Code Registry).

### N1. Ayla не поняла запрос

- **Триггер:** `INTENT_UNRESOLVED` — intent не распознан или confidence ниже
  порога после этапов 4–5.
- **Поведение системы:** честно признать неопределённость, не имитировать
  понимание; уточнить несколько деталей или помочь найти специалиста
  (факт — полная UJS, Edge Case 3); low-confidence не маскируется как
  определённый intent (факт — Capability Registry §6.3, key invariants
  CAP-003).
- **Пользовательское состояние:** clarification required; после повторной
  неудачи — human handoff **(proposal)**.
- **Owning capability:** CAP-003.

### N2. Отсутствует consent

- **Триггер:** операция требует scope, по которому нет effective consent
  record (отсутствует, `denied`, `revoked`, `expired`) — `CONSENT_REQUIRED`.
- **Поведение системы:** fail-closed deny (факт — CSR §2 п. 2; §7 «отсутствие
  consent record не интерпретируется как согласие»); предложить session-only
  продолжение либо явный запрос согласия с названием цели; negative test
  «отсутствие consent → deny» обязателен к Phase 2 (факт — CSR §10.2).
- **Пользовательское состояние:** consent required; диалог не прерывается
  при отказе (факт — CSR §8 UX Requirements).
- **Owning capability:** CAP-002.

### N3. Нет подходящей услуги

- **Триггер:** `NO_CANDIDATES` — все кандидаты исключены на этапах
  eligibility/relevance (seed catalog пилота ограничен — факт, Scope
  Contract §4.1 п. 4).
- **Поведение системы:** показать честное состояние no recommendation, не
  выдумывать рекомендацию; сохранить обычный поиск и запись без
  персонализированной primary (факт — Killer PRD §5.3 Fallback).
- **Пользовательское состояние:** no recommendation + вариант обычного
  поиска.
- **Owning capability:** CAP-004 (подбор), CAP-008 (полнота каталога).

### N4. Нет свободных слотов

- **Триггер:** `NO_AVAILABLE_SLOTS` на этапе 10.
- **Поведение системы:** предложить альтернативу — другой мастер или другое
  время (факт — полная UJS, Error Recovery 1: «Могу предложить Елену…»);
  повторный прогон Recommendation Composer с уточнённым constraint,
  alternative получает собственный `recommendation_id` (факт — Killer PRD
  §5.1).
- **Пользовательское состояние:** slot unavailable + альтернативные варианты.
- **Owning capability:** CAP-010.

### N5. Специалист недоступен

- **Триггер:** `PROVIDER_INELIGIBLE` — провайдер/специалист не принимает
  запись (inactive provider не принимает запись — факт, Capability Registry
  §6.9, key invariants CAP-009).
- **Поведение системы:** исключить кандидата до показа primary; если
  недоступность выявлена после показа — честно сообщить и предложить
  alternative (факт — Killer PRD §5.1 порядок gates: eligibility до ranking).
- **Пользовательское состояние:** альтернативная рекомендация с объяснением
  замены **(proposal)**.
- **Owning capability:** CAP-009.

### N6. Запись не подтверждена

- **Триггер:** `APPOINTMENT_NOT_CONFIRMED` или `APPOINTMENT_CONFLICT` —
  backend/provider не перевёл Booking в `confirmed`.
- **Поведение системы:** не показывать подтверждение неподтверждённой
  записи (факт — полная UJS, Stage 5 Success Criteria); сообщить фактическое
  состояние и предложить recovery: другой слот, другой мастер, повторить
  позже (факт — полная UJS, Error Recovery).
- **Пользовательское состояние:** booking failed + recovery path.
- **Owning capability:** CAP-011.

### N7. Tool или LLM недоступен

- **Триггер:** `TOOL_TIMEOUT` / `MODEL_UNAVAILABLE` на любом этапе,
  использующем tool call или LLM.
- **Поведение системы:** применить model/provider fallback (факт — Roadmap
  §9.1); при недоступности — извиниться и предложить альтернативу:
  записаться позже или дать контакты мастера для прямой записи (факт —
  полная UJS, Error Recovery 3); дублирование side effects при retry
  недопустимо (идемпотентность tool calls — факт, Roadmap §6.3
  `idempotency`).
- **Пользовательское состояние:** retry; при повторном сбое — human
  handoff **(proposal)**.
- **Owning capability:** CAP-018.

### N8. Рекомендация заблокирована safety gate

- **Триггер:** `SAFETY_BLOCKED` — safety gate Recommendation Composer
  обнаружил конфликт с safety-critical контекстом или competence boundary
  (факт — Killer PRD §5.1 этап 2; полная UJS, Stage 3 Safety Check).
- **Поведение системы:** остановить обработку и перейти в S8 Boundary
  Handling: не подтверждать и не продолжать небезопасный путь; задать только
  минимальные вопросы о срочности и red flags; предложить безопасный
  следующий шаг или направление к квалифицированному специалисту (факт —
  полная UJS, Edge Case 2; при явно сообщённом срочном симптоме —
  safety-routing flow, факт — Killer PRD §4.1 OD-K6).
- **Пользовательское состояние:** boundary message без CTA на заблокированную
  услугу; безопасная альтернатива — только после Boundary Handling (факт —
  полная UJS, State Transitions S8).
- **Owning capability:** CAP-014.

### N9. Пользователь отказывается от предложения

- **Триггер:** пользователь отклоняет primary recommendation на этапе 9.
- **Поведение системы:** после первого отклонения — зафиксировать
  `rerank_reason`, повторно пройти Composer с уточнённым constraint и
  предложить alternative в пределах лимита (не более двух) (факт — Killer
  PRD §5.1). После повторного или явно жёсткого отказа дальнейшие
  предложения подавляются: жёсткий отказ («не напоминай») — блокировка без
  `reconsider_after`, мягкий — нейтральное acknowledgement без CTA (факт —
  полная UJS, Proactive Suppression Rules / User Communication). Отклонённая
  рекомендация не получает атрибуцию (факт — Killer PRD §6.2).
- **Пользовательское состояние:** альтернатива с объяснением либо спокойное
  завершение без давления (факт — полная UJS, Anti-pattern 3 «Ayla давит»).
- **Owning capability:** CAP-004 (rerank), CAP-016 (поведение диалога).

## Memory Interaction

MVP-срез правил памяти полной UJS (What Ayla Remembers / When Memory is
Created / When Memory is Used); полная модель — в UJS и ADR-0012. Раздел
расширен в v0.2: подразделы, помеченные **(proposal)**, выражают
memory-first модель продукта и подлежат отдельному review; там, где они
пересекаются с approved-источниками, конфликт вынесен в Open Questions
№9–12, а не решён этим документом.

### Факты из источников

- **Whitelist фактов MVP:** каноническая форма — категориальный whitelist
  AYLA-DEC-0023 (статусы категорий allowed / requires dedicated consent /
  forbidden; красная зона — default deny; расширение — только owner
  decision с проверками product_value / privacy_review / retention_policy /
  deletion_behavior). Плоский список Roadmap §3.4 = Scope Contract §4.1
  п. 8 — superseded, non-normative historical reference (Change Control
  2026-07-28); позиция «согласие на персонализацию» из него исключена
  (см. правило Consent state ≠ Context Fact ниже). Ничего сверх whitelist
  в MVP не сохраняется.
- **Phase 1 — session-only** (CSR §10.1): persistent memory технически
  отключена; контекст живёт только в пределах текущей сессии; обработка
  текущего сообщения — по `service_necessity` без consent record.
- **Phase 2 — opt-in persistent** (CSR §10.2): единственный persistent-write
  scope — `preference_memory`; требуется `explicit_consent`; запись только
  явно подтверждённых фактов (`inferred_signal` prohibited — CSR §5.7).
- **Memory Proposal flow** (полная UJS, When Memory is Created): сообщение
  или событие создаёт только proposal; persistent memory — после
  sensitivity/purpose check и consent check. Молчание и продолжение диалога
  не являются согласием.
- **Revocation** (CSR §2 п. 6, §5.7, §7): отзыв прекращает новое
  использование, становится видимым runtime без новой сессии; сохранённые
  предпочтения помечаются `revoked` и перестают использоваться в
  `provider_selection`/`intent_understanding`.
- **Команды пользователя MVP** (факт — CSR §8): просмотр активных согласий;
  отзыв отдельного scope; отключение всей persistent personalization;
  «Что Ayla знает обо мне»; удаление выбранного memory fact; «Забыть это».
- **Перепроверка памяти** (полная UJS, When Memory Must be Questioned /
  MVP Memory Heuristic): Ayla переспрашивает при низкой актуальности факта,
  истечении TTL, противоречии, а также когда временный, изменяемый или
  safety-critical факт используется для существенного решения; подтверждённая
  пользователем гипотеза преобразуется в confirmed context с сохранением
  provenance.

### Memory Learning Loop **(proposal)**

Замкнутый цикл, делающий повторный journey полезнее первого:

```text
Observe (сообщение, событие, outcome)
→ Propose (Memory Proposal: candidate fact + source + purpose + confidence)
→ Verify (sensitivity/purpose check + подтверждение пользователя)
→ Store (Context Fact с provenance, только при активном scope)
→ Retrieve (targeted, в пределах scope и релевантности)
→ Apply (recommendation, clarification suppression, execution context)
→ Measure outcome (feedback, acceptance, correction)
→ Correct (confirm / supersede / expire / delete)
```

Поля Memory Proposal **(proposal)**: `candidate_fact`, `fact_type`,
`source`, `proposal_confidence`, `sensitivity`, `purpose`,
`confirmation_requirement`, `conflict_with_existing`, `persistence_result`,
`review_after` / `expires_at`, `audit_events`.

> Поле `proposal_confidence` (v0.3, по AYLA-DEC-0024 п. 1): допустимо у
> MemoryProposal и в audit metadata, но **не переходит в canonical
> MemoryEntry** — там `confidence` запрещён и не влияет на использование
> факта. После подтверждения создаётся MemoryEntry без confidence. Состав
> MemoryEntry (типизированное `value`, `provenance`, `consent_scope`,
> `purpose_tags`, `effective_from`, `superseded_by`, `expires_at` и др.) и
> статусы MemoryProposal (`pending_confirmation | accepted | rejected |
> expired`) определяются AYLA-DEC-0024.

Кандидатные lifecycle-события цикла **(proposal — все имена candidate до
Domain Event Registry; конвенция и producer правила — AYLA-DEC-0025,
семейство `memory.*`, producer — Memory Service по AYLA-DEC-0024)**:
`MemoryProposalCreated`, `MemoryProposalPresented`,
`MemoryProposalAccepted`, `MemoryProposalRejected`, `ContextFactCreated`,
`ContextFactCorrected` (пересекается с Roadmap §6.4 — факт),
`ContextFactSuperseded`, `ContextFactExpired`, `ContextFactDeleted`.

`ContextFactUsed` — **candidate, classification unresolved** (v0.2.1):
использование факта не меняет состояние Context Fact, происходит часто и
важно для audit/observability; вероятнее audit-событие `memory_fact_used`
(факт — CSR §9.1) или recommendation evidence record
(`recommendation_id` + `context_fact_id` + `usage_role` + `used_at`), а не
lifecycle domain event. В обязательный lifecycle Memory Proposal не
включён.

Предлагаемое владение областями цикла **(proposal, v0.2.1)**: Journey
Specification определяет взаимодействие capabilities, но не назначает
новый System of Record и не заменяет Core Domain Model.

| Область | Предлагаемый владелец | Статус |
|---|---|---|
| Memory Proposal lifecycle | CAP-001 Personal Context Management | proposal |
| Consent authorization | CAP-002 Consent Management | inherited |
| Runtime orchestration | CAP-018 AI Orchestration and Tool Execution | inherited |
| Persistent Context Fact storage | User Context Domain / backend (SoR — Core Domain Model) | requires contract confirmation |
| Memory audit | CAP-026 Audit and Observability | inherited |
| Recommendation-time use | CAP-004 + CAP-001 | requires Recommendation Contract |
| Outcome interpretation | CAP-006 + CAP-001 | requires CAP-006 depth decision (Open Question №6) |

Не каждый feedback становится памятью **(proposal)**: оценка специалиста,
оценка услуги, достижение цели, временная реакция и safety signal —
разные interpretation candidates; Ayla не выбирает значение автоматически,
а предлагает сохранить конкретный факт («Запомнить, что предпочитаете более
мягкую интенсивность?»).

### Memory taxonomy **(proposal)**

Вместо плоского списка — типизированные классы фактов, каждый со своими
purpose, sensitivity, source, confidence, сроком актуальности, способом
подтверждения и допустимым влиянием на решение:

| Тип факта | Пример | Влияние на решение |
|---|---|---|
| Preference Fact | предпочтение времени, стиля общения | preference weighting |
| Constraint Fact | явно подтверждённый отказ от интенсивных процедур | constraint / exclusion, не boost |
| Historical Action Fact | предыдущая подтверждённая услуга, мастер | candidate generation, disambiguation |
| Outcome Fact | прошлая услуга не дала ожидаемого результата | смена стратегии рекомендации |
| Communication Preference | краткие или подробные объяснения | explanation style |
| Temporary Context | событие через две недели, период восстановления | time-bounded relevance + expiry |
| User-confirmed Correction | исправление ранее сохранённого факта | supersede с приоритетом над старым фактом |

**Temporary Context — session-only класс (owner ruling 2026-07-28):**
существует только в активной сессии; не сохраняется в долговременную
память по умолчанию; не извлекается в будущих сессиях; не становится
User Fact автоматически; перевод в persistent memory — только через
Memory Proposal по AYLA-DEC-0024 (pipeline: proposal → confirmation →
whitelist check → persist); внутри сессии используется в пределах
`purpose_tags` (AYLA-DEC-0024 п. 1).

> **Normative guard (v0.2.1).** Данная taxonomy **не расширяет** approved
> persistent-memory whitelist (факт — Roadmap §3.4 = Scope Contract §4.1).
> Класс факта может использоваться для session context, runtime
> classification или proposal generation, но persistent сохранение
> разрешено только для типов, явно включённых в действующий whitelist,
> допустимый purpose и активный consent scope. Расширение whitelist —
> только owner decision с четырьмя проверками (факт — AYLA-DEC-0023 п. 5).

Outcome Fact несёт источник и статус подтверждения **(proposal, v0.2.1)**:
`reported` (сообщён пользователем), `confirmed` (подтверждён допустимым
authoritative source), `inferred` (вычислен системой — не может
автоматически становиться persistent Context Fact), `disputed` (оспорен
пользователем), `superseded` (заменён более актуальным фактом).
Поведенческий сигнал, отсутствие повторной записи или модельный вывод не
являются подтверждённым Outcome Fact без отдельной verification.

Правило: **Consent state ≠ Context Fact** — статус согласия хранится и
проверяется только через Consent Management / [[Consent Scope Registry]],
а не как факт памяти; иначе возможен конфликт «consent revoked, но факт
ещё говорит consented». Допустимо derived runtime-представление
(`authorization_context: preference_memory: allowed | denied | revoked |
expired`), но оно не становится независимым persistent fact. Решено
(v0.3): AYLA-DEC-0023 заменяет плоский whitelist Roadmap §3.4
категориальной формой — позиция «согласие на персонализацию» как факт
вытесняется; MemoryEntry хранит только ссылку `consent_scope`, а не
consent state как значение (факт — AYLA-DEC-0024 п. 1). Плоский список
Roadmap §3.4 / Scope Contract §4.1 помечен superseded (Change Control
2026-07-28).

Кто может создавать факты **(proposal)**: пользователь (explicit) и Ayla
(proposal на подтверждение). Provider-authored данные могут быть
authoritative operational facts в пределах owning domain, но не становятся
фактами о предпочтениях, намерениях или субъективном результате
пользователя без подтверждения самого пользователя (v0.2.1).

### Context Sufficiency Model

Общий принцип достаточности контекста — **факт**, унаследован из полной
UJS (Context Sufficiency Gate): sufficiency определяется обязательным
набором данных для конкретных Intent Type, Action Class и Risk Level, а не
количеством заполненных слотов.

Формальная структура сводки — **proposal (v0.2)**, не утверждённая часть
полной UJS (v0.2.1):

```yaml
context_summary:
  applicable_facts: []
  uncertain_facts: []
  conflicting_facts: []
  stale_facts: []
  missing_required_context: []
  authorization_scope:
  sufficiency: sufficient | partial | insufficient
```

Правила **(proposal)**: память не заменяет уточнение, если релевантный факт
устарел, конфликтует, недостаточно подтверждён или неоднозначно применим к
текущей ситуации; конфликтующие факты не применяются одновременно —
запрашивается пользовательское разрешение конфликта (согласуется с фактом —
полная UJS, When Memory Must be Questioned).

### Freshness, expiry и supersession **(proposal)**

Каждый факт несёт временную модель: `observed_at`, `confirmed_at`,
`effective_from`, `expires_at`, `review_after`, `supersedes_fact_id`.
Временные и изменяемые факты перед существенным использованием требуют
повторного подтверждения (факт — полная UJS, MVP Memory Heuristic п. 2;
числовые TTL — design candidates до ADR-0012, факт — полная UJS, What Ayla
Remembers). Пользовательские сценарии актуализации: «Это всё ещё
актуально?», «Оставить это предпочтение?», «Использовать только сегодня»,
«Забыть это» (последнее — факт, CSR §8).

### Anti-lock-in и novelty guard **(proposal)**

- История пользователя — не безусловный приказ повторить прошлый выбор:
  высокая повторяемость прошлого решения может означать filter bubble, а не
  качество.
- Preference boost не обходит safety, eligibility и economic-neutrality
  (факт в части gates — Killer PRD §5.1/§5.3).
- Негативный outcome снижает повторение прошлого решения, но не создаёт
  автоматически sensitive inference (согласуется с фактом — CSR §5.7
  Prohibited; полная UJS, Learning Signals).
- Система сохраняет разумную возможность исследования alternatives; Ayla
  может спросить: «Повторить знакомый вариант или посмотреть что-то
  новое?» — вместо скрытого решения за пользователя.

### User memory controls

Факты (CSR §8): просмотр активных согласий по scope; отзыв scope одной
командой; отключение всей persistent personalization; «Что Ayla знает обо
мне»; удаление выбранного memory fact; «Забыть это»; подтверждение
пользователю, что именно изменилось после отзыва.

Дополнения **(proposal)**: «Почему это сохранено» и «Где это использовалось»
(provenance disclosure); ограничение использования факта — через модель
`purpose_tags` (AYLA-DEC-0024: retrieval допустим только в пределах
declared purpose; отдельный fact-level opt-out «не использовать для
рекомендаций» не канонизируется); «Не спрашивать снова»; «Сохранить только
на эту сессию»; explanation CTA из карточки рекомендации к управлению
памятью (чат-команда или экран Mini App — факт роли каналов, полная UJS §7).

> Ограничение контроля «Не спрашивать снова» (v0.2.1): применяется только к
> необязательным повторным вопросам и Memory Proposal prompts. Не отключает
> обязательные safety checks, authorization checks, consent revalidation,
> freshness verification и legal/policy-required confirmations.

### Product Thesis Validation Scenario **(proposal)**

Сценарий проверки memory-first тезиса на пилоте (переименован в v0.2.1;
ранее «Memory proof scenario»). Сценарий обязателен для проверки
memory-first продуктовой гипотезы; его статус определён решением
AYLA-DEC-0018 (accepted, Option C): он не является release gate Phase 1 —
Phase 1 session-only остаётся самостоятельным техническим release gate
(факт — CSR §10), а Product Thesis Validation закрывается только после
Phase 2 и успешного прохождения этого сценария.

**Первый визит.** Пользователь сообщает цель, удобное время и важное
ограничение. Ayla использует их в текущей сессии, предлагает сохранить
допустимые предпочтения, получает согласие, сохраняет подтверждённые факты.

**Повторный визит.** Пользователь: «Хочу снова записаться на этой неделе».
Ayla извлекает релевантные актуальные факты, не повторяет известные
вопросы, уточняет только изменяемое, учитывает прошлый outcome, предлагает
решение, объясняет использование памяти и даёт возможность его исправить.

**Acceptance criterion:** повторный journey короче, точнее и персональнее
первого; при этом Ayla использует минимум один релевантный подтверждённый
факт, показывает его влияние на решение, позволяет исправить или отключить
его и не использует нерелевантные или отозванные данные.

## Recommendation and Proactivity Gates

MVP-срез; полные правила — полная UJS §6 и [[Killer PRD]] §5.

Факты:

- **User-Initiated Recommendation Gate** (полная UJS §6): ответ на явный
  запрос проверяет safety, eligibility, Context Sufficiency, competence
  boundary и explicit current refusal. В MVP существуют только
  user-initiated рекомендации.
- **Proactive Readiness Gate — неактивен в MVP:** Phase 1 работает в режиме
  no proactive recommendations (CSR §10); scope `proactive_recommendation`
  не входит в обязательные Phase 1/2 и может оставаться `blocked` (факт —
  CSR §5.7 примечание). Этап 13 допускает только транзакционные
  уведомления по записи.
- **Обязательный порядок gates** для любой рекомендации (Killer PRD §5.1):
  consent/privacy → safety → eligibility/availability → relevance →
  preference boost → economic-neutrality → primary output.
- **Economic neutrality** (Killer PRD §5.3; Конституция): комиссия, booking
  fee и коммерческий статус провайдера не влияют на organic ranking;
  нарушение блокирует выдачу и переводит ranking release в `quarantined`.

**Memory influence model (proposal, v0.2):** влияние памяти не сводится к
одному preference boost на этапе ranking. Разные типы фактов (таксономия —
Memory Interaction) работают на разных этапах решения: интерпретация intent,
hard constraints и exclusions, формирование candidate set, outcome-informed
relevance, preference weighting, novelty/diversity guard, выбор explanation
и уровня уверенности, решение «предложить действие или продолжить
уточнение». Канонический pipeline Killer PRD §5.1 этим не отменяется —
порядок gates сохраняется; уточнение контракта «как тип факта влияет на
решение» — предмет MVP Recommendation Contract (planned, Roadmap §3.2) и
upstream Open Question №11.

## Cross-channel Experience

Факты:

- **Единственная канальная платформа MVP — MAX** (Scope Contract §7,
  AYLA-DEC-0004): MAX-бот — primary channel (диалог, рекомендация, быстрые
  действия, feedback); MAX Mini App — для сложных действий (профиль,
  детали записи) (факт — полная UJS §7, роли каналов).
- **Telegram — вне пилотного scope** (Scope Contract §7).
- **Context continuity** между ботом и Mini App — в пределах consent и
  purpose limitation (факт — полная UJS §7 Context Continuity).
- Универсальная multi-channel спецификация для MVP не требуется (факт —
  Scope Contract §7; Roadmap «Что не должно блокировать MVP»).

## Business Alignment

- Этапы 7–12 реализуют главную метрику MVP: переход «осмысленный запрос →
  полезная рекомендация → подтверждённое действие» (факт — Roadmap §9.2 =
  Scope Contract §9).
- Этап 12 связывает запись с `recommendation_id`, обеспечивая минимальный
  direct linkage атрибуции (факт — Scope Contract §4.1 п. 11; Killer PRD §6).
- Экономическая нейтральность рекомендации (этап 7) защищает доверие как
  актив пилота (факт — Killer PRD §5.3; полная UJS, Monetization Neutrality).
- Проверяемый тезис MVP: накопленное и объяснимое понимание пользователя, а
  не сама функция записи, создаёт преимущество (факт — Scope Contract §1,
  AYLA-DEC-0002). Этапы 6–8 — носители этого тезиса в journey.
- **(proposal, v0.2)** Product Thesis Validation Scenario (Memory
  Interaction) — продуктовый критерий проверки тезиса AYLA-DEC-0002 на
  уровне journey: повторная рекомендация доказуемо полезнее благодаря
  разрешённой памяти. Его статус определён решением AYLA-DEC-0018
  (accepted, Option C): технический пилот Phase 1 не подменяется
  продуктовой валидацией; memory-enabled repeat journey не является
  условием релиза Phase 1, но гипотеза не считается проверенной до
  успешного Product Thesis Validation.

## Metrics

Метрики этапов привязаны к минимальному набору метрик пилота (факт —
Roadmap §9.2 = Scope Contract §9). Числовые пороги здесь не фиксируются:
по Scope Contract §9 они остаются design candidates до данных пилота или
отдельного Measurement Framework.

| Метрика пилота (факт — Roadmap §9.2) | Этапы данного документа |
|---|---|
| доля resolved intents | 4–5 |
| clarification rate | 5 |
| recommendation shown rate | 7–8 |
| recommendation acceptance rate | 9 |
| booking conversion | 9–12 |
| booking completion | 11–13 |
| attributed qualified actions | 12 |
| recommendation rejection reasons | 9, N9 |
| unsafe block rate | N8 |
| tool failure rate | N7 |
| median response time | все |
| пользовательская оценка полезности | 14 |

Целевые ориентиры полной UJS (Journey Quality Metrics — First Contact
Completion Rate, Discovery Completion Rate, Intent Recognition Accuracy,
Booking Success Rate, Feedback Response Rate и др.) остаются справочными для
пилота и не переопределяются этим документом.

**Memory-quality метрики (proposal, v0.2):** без них команда может
оптимизировать booking conversion и считать продукт успешным, даже если
память не влияет на решения. Кандидаты (числовые пороги — design
candidates, паттерн Scope Contract §9). Measurement method и baseline для
всех метрик этой таблицы — pending Measurement Framework (v0.2.1):
precision/recall требуют ground truth (размеченные pilot conversations,
synthetic test cases, QA fixtures, экспертная разметка); repeat-journey
value uplift требует определённого baseline (первый journey того же
пользователя, session-only режим, контрольная группа или journey без
использования памяти).

| Группа | Метрика-кандидат | Что измеряет |
|---|---|---|
| Retrieval quality | context retrieval precision / recall | доля извлечённых фактов, релевантных запросу; доля найденных релевантных фактов |
| Retrieval quality | stale fact rate | доля использованных фактов, потерявших актуальность |
| Retrieval quality | contradictory fact rate | доля решений с конфликтующими фактами |
| Пользовательская полезность | repeated-question rate | как часто Ayla спрашивает уже известное |
| Пользовательская полезность | context correction rate | как часто пользователь исправляет применённую память |
| Пользовательская полезность | recommendation acceptance uplift | прирост принятия при корректном использовании контекста |
| Пользовательская полезность | repeat-journey value uplift | насколько второй journey полезнее первого |
| Безопасность | unauthorized context use rate = 0 | использование контекста вне scope |
| Безопасность | unexplained memory use rate | использование памяти без объяснения |
| Безопасность | sensitive inference persistence rate = 0 | сохранение inferred sensitive signals |
| Безопасность | cross-tenant memory contamination rate = 0 | утечка контекста между tenant |
| Безопасность | revoked fact use rate = 0 | использование отозванных данных |
| Анти-lock-in | incumbent repetition rate / novelty exposure rate | подавление новых вариантов историей |

Фиксированные нулевые значения safety-метрик — не настраиваемые
бизнес-пороги, а мониторинг действующих hard invariants (fail-closed,
revocation, запрет sensitive inference — факты CSR §2/§5.7).

## Constitutional Traceability

Матрица MVP-среза; полная матрица — [[Ayla User Journey Specification]] §14.

| Принцип Конституции | Этапы | Реализация в MVP-срезе |
|---|---|---|
| Ст. I (предметная область) | 1–2 | Journey начинается с потребности в beauty/wellness, не с каталога |
| Ст. VI (доверие расходуется вопросами) | 5 | Не более 5 вопросов Discovery (полная UJS, Maximum Questions); clarification suppression (proposal) |
| Ст. VII (объяснимость) | 8 | Объяснение рекомендации обязательно (Scope Contract §4.1 п. 9); unexplained memory use недопустимо (proposal) |
| Ст. X (уместность прежде действия) | 3, 9, 13 | Явное подтверждение перед записью; отказ без прерывания диалога; никакой проактивности в Phase 1 |
| Пользователь контролирует персональный контекст | 3, 6, 14 | Fail-closed consent; whitelist фактов; revocation; команды CSR §8; user memory controls (proposal) |
| AI не является источником истины | 4, 11–12 | Backend — SoR; подтверждение только фактически достигнутого состояния; inference не становится фактом без подтверждения (полная UJS, Memory Proposal) |
| Recommendation отделяется от action | 7, 9, 11 | Рекомендация не создаёт запись без явного подтверждения (CAP-004 invariant) |
| Экономическая нейтральность | 7 | Economic-neutrality check до показа primary (Killer PRD §5.3) |
| Критические решения прослеживаемы | все | Audit events CSR §9.1; `recommendation_id` сквозная связь; provenance фактов памяти (proposal) |

## Non-goals

Не входит в данный MVP-срез (основания указаны; детали — в полной UJS и
связанных документах):

- все состояния и journeys полной [[Ayla User Journey Specification]] за
  пределами сквозного сценария: S7 Long-term Relationship, доменный journey
  Nutrition Guidance, полная state machine, re-engagement;
- проактивные рекомендации и Proactive Readiness Gate в действии
  (deferred — CSR §10; scope `proactive_recommendation`);
- cross-domain personalization и food→beauty trigger-сценарии Killer PRD §4
  как реализованные MVP-функции (scope `cross_domain_personalization` —
  blocked; факт — CSR §11.2);
- платежи пользователя, оплата в journey (Scope Contract §5: клиентская
  онлайн-оплата вне MVP; Error Recovery «оплата не прошла» из полной UJS в
  MVP-срез не входит);
- перенос и отмена записи, late-window, substitute и YClients reschedule
  как полноценные ветки journey — **deferred (вариант Б, owner ruling
  2026-07-28)**: intent types RESCHEDULE/CANCEL поддерживаются моделью
  intent (реестр Roadmap §3.1), но stage specifications и операционная
  семантика этих веток выходят за MVP primary-booking journey и
  определяются planned AYLA-DEC-0022 (см. reconciliation table ниже);

**Deferred branches — reconciliation / traceability (owner ruling
2026-07-28, вариант Б).** Для каждой ветки: Deferred beyond MVP
primary-booking journey; доменная семантика определяется planned
AYLA-DEC-0022 — `99 Archive/proposals/decision-brief-appointment-reschedule-model.md`
(draft до Journey-reconciliation; матрица операций — §4, сценарии — §2):

| Ветка | Сценарии decision brief | Статус в этом документе |
|---|---|---|
| Reschedule записи | S1 (клиент переносит), S2 (другой мастер при переносе), S6 (анти-абуз лимиты), S7 (биллинг при переносе), S8 (runtime) | deferred beyond MVP primary-booking journey; семантика — planned AYLA-DEC-0022 |
| Cancel записи | S1–S3 (включая массовый каскад re-offer при болезни/отпуске мастера), S13 (offboarding — через remediation, не reschedule-модель) | deferred beyond MVP primary-booking journey; семантика — planned AYLA-DEC-0022 |
| Late-window изменения | §10 Authorization rules и late-window; S6 (лимиты) | deferred beyond MVP primary-booking journey; семантика — planned AYLA-DEC-0022 |
| Substitute / отказ от замещения | S12 (модель обязана допускать отказ клиента от substitute без потери записи) | deferred beyond MVP primary-booking journey; семантика — planned AYLA-DEC-0022 |
| YClients reschedule / sync-конфликты | S5 (YClients-originated записи, sync-конфликты), §12 (импорт YClients, calendar mode) | deferred beyond MVP primary-booking journey; семантика — planned AYLA-DEC-0022 |

Проверка отсутствия конфликтов (owner ruling 2026-07-28): в этапах 1–14
и негативных сценариях N1–N9 нет статусов, событий или операций,
относящихся к reschedule/cancel/late-window/substitute/YClients
reschedule; intent types RESCHEDULE_APPOINTMENT / CANCEL_APPOINTMENT
упоминаются только как элементы реестра Roadmap §3.1 (этап 4) без
операциональной семантики. Конфликтующих определений не выявлено.
- Telegram и любые каналы кроме MAX (Scope Contract §7);
- программа лояльности, marketplace-сценарии, несколько стран (Scope
  Contract §5).

Ложные трактовки памяти, запрещённые в MVP (факты — CSR §5.7 Prohibited,
CSR §2, полная UJS Memory Proposal; остальное — **proposal**, v0.2):

- скрытое сохранение inferred traits без подтверждения пользователя (факт);
- использование отозванного или неразрешённого контекста (факт);
- построение sensitive attributes из поведения (факт — CSR §5.7,
  `inferred_signal` prohibited);
- бессрочное использование предпочтений без проверки актуальности
  **(proposal)**;
- использование provider-authored данных как пользовательских предпочтений
  без маркировки источника и подтверждения **(proposal)**;
- автоматическое повторение прошлого выбора только на основании истории
  **(proposal)**;
- персонализация, которую Ayla не может объяснить пользователю
  **(proposal)**;
- оптимизация рекомендаций только по booking conversion (факт — полная UJS,
  Business Metrics «Правило приоритета» / «Запрещено»).

## Open Questions

1. **Финальные имена analytics events.** События, помеченные (proposal),
   подлежат фиксации в Analytics Event Contract; до его материализации
   имена в Stage Specifications — рабочие.
2. **Human handoff.** Порог перехода к оператору/человеку (N1, N7) и сама
   процедура не определены в источниках; требуется решение в Pilot
   Operations Runbook (Roadmap §9.3, P1).
3. **Поведение этапа 12 при отклонении записи провайдером.** Предложение
   «альтернативный слот/мастер» помечено (proposal); требуется подтверждение
   продуктового решения.
4. **Fallback этапа 8.** Правило «без объяснения рекомендация не
   показывается» — (proposal), требует сверки с MVP Recommendation Contract
   (planned, Roadmap §3.2).
5. **Ветки переноса/отмены записи.** Включать ли их stage specifications в
   следующую версию MVP-среза — открыто (Non-goals п. 5).
6. **Статус CAP-006 в MVP.** Stage 14 отнесён к Outcome Capture, но в
   Included Capabilities Scope Contract §4.1 прямой записи нет (advanced
   outcome learning deferred); маппинг подлежит сверке в волне 2 перевода
   Registry в MVP-active (AYLA-DEC-0014). Кандидат-решение из review:
   разделить Basic Feedback Capture (MVP-active) и Advanced Outcome
   Learning (deferred).
7. **Зависимость от Ayla Intent Model Specification (planned).** Этапы 4–5
   ссылаются на output contract intent resolution, который фиксируется в
   документе, находящемся в разработке параллельно; после его
   материализации формулировки этапов 4–5 требуют сверки. Wikilink
   намеренно не установлен до создания документа.
8. **(ЧАСТИЧНО РЕШЁН — v0.3-final).** Domain Event Registry v0.1 создан
   (`05 Architecture/Ayla Domain Event Registry.md`, актуальная редакция —
   v0.2). Миграция выполняется для active canonical event names
   (`consent.*`, `intent.resolution_produced`, `appointment.*` — применена
   в этапах 3, 4, 11, 12, 14); pending и отсутствующие события остаются
   открытыми до утверждения соответствующих записей реестра:
   регистрация `recommendation.*` (семантика — MVP Recommendation
   Contract v0.1, OQ-R), `qualified_action.attributed`, имена `memory.*`
   (candidate mappings, включая `ContextFactCorrected →
   memory.entry_superseded`), финальные payload и owner для этапа 14.
   **Registry gap:** канонический analytics event для
   `booking_confirmation_shown` (этап 12) в реестре отсутствует —
   событие остаётся legacy-маркером до регистрации.
9. **(ЗАКРЫТ — AYLA-DEC-0018, accepted 2026-07-28, Option C). Статус Phase 2
   как product-validation gate.** Решение ([[Ayla Decision Log]],
   AYLA-DEC-0018): Phase 1 (session-only) остаётся самостоятельным
   техническим release gate; его успех подтверждает работоспособность и
   безопасность session-only vertical slice, но НЕ memory-first продуктовую
   гипотезу (AYLA-DEC-0002). Product Thesis Validation остаётся открытой до
   активации Phase 2 и успешного прохождения Product Thesis Validation
   Scenario с измеримым улучшением повторного journey; активация Phase 2
   сама по себе validation не закрывает (`Phase 1 release readiness ≠
   Product Thesis Validation`; `Phase 2 activation ≠ автоматическая
   validation`). Уточнение [[Consent Scope Registry]] §10 и
   [[Ayla MVP Scope and Release Contract]] §3 — follow-up Change Control
   по AYLA-DEC-0018; критерии валидации и рассмотренные варианты A/B — в
   тексте решения.
10. **(ЗАКРЫТ — AYLA-DEC-0023, accepted 2026-07-28). Достаточность memory
    whitelist.** Whitelist определён в категориальной форме: категории со
    статусом allowed / requires dedicated consent / forbidden, scope из
    Consent Scope Registry и основание; поле не существует вне категории и
    наследует её политику; красная зона — default deny; persistent memory —
    только устойчивые факты (состояние сессии — Conversation State, не
    Persistent Memory); единственный pipeline user message → inference →
    confirmation → whitelist check → persist; user-stated safety
    constraints — отдельная категория (память хранит утверждение
    пользователя, не медицинский вывод); расширение — только owner decision
    с проверками product_value / privacy_review / retention_policy /
    deletion_behavior. Машиночитаемая политика категорий
    (`MemoryCategoryPolicy`: allowed_scopes, purposes, cardinality, TTL,
    confirmation, revocation) — по AYLA-DEC-0024 п. 7. Приведение плоского
    списка Roadmap §3.4 / Scope Contract §4.1 к категориальной форме —
    через Change Control approved-источников.
11. **(upstream, v0.2 — OPEN). Роль памяти в recommendation pipeline.**
    Канонический pipeline (Killer PRD §5.1) содержит preference boost как
    один из этапов; Memory influence model (proposal) предполагает более
    широкую роль типов фактов: constraint, exclusion, candidate-generation
    input, ranking weight, outcome modifier, explanation evidence,
    clarification trigger, novelty guard. Memory lifecycle и storage
    semantics определены AYLA-DEC-0024 (v0.3); открытым остаётся именно
    то, как retrieved memory влияет на candidate generation, ranking,
    explanation, alternatives и final recommendation, — предмет MVP
    Recommendation Contract (planned, Roadmap §3.2); изменять
    канонический порядок Killer PRD не обязательно (v0.2.1).
12. **(ЗАКРЫТ — resolved by AYLA-DEC-0023/0024, accepted 2026-07-28).
    «Согласие на персонализацию» в whitelist.** Нормативный вывод: consent
    state — это authorization metadata, а не Context Fact и не значение
    MemoryEntry. MemoryEntry может ссылаться на применимый consent scope
    (поле `consent_scope`, AYLA-DEC-0024 п. 1), но само согласие не
    персистируется как пользовательская память; authoritative consent state
    принадлежит Consent Management / Consent Scope Registry. Категориальная
    форма whitelist (AYLA-DEC-0023) вытесняет позицию «согласие на
    персонализацию» из плоского списка Roadmap §3.4; приведение источников
    — через Change Control approved-документов.
13. **(cross-document, deferred — backlog). Naming-дрейф полной UJS и
    термин «substitute» (2026-07-28).**
    - Полная [[Ayla User Journey Specification]] v1.2 использует
      `booking.created` / `booking.confirmed` — расхождение с каноном
      AYLA-DEC-0025 (`appointment.*`). Не блокер для этого документа и
      для planned AYLA-DEC-0022; отдельный backlog-пункт: аменда полной
      UJS к канону имён или сознательный deferral до её следующей
      редакции. Сознательно не правится сейчас, чтобы не расползаться по
      двум документам сразу.
    - Терминологическое пересечение: «substitute offer» в полной UJS
      (Proactive Readiness Gate, строка ~930 — подменное предложение при
      блокировке проактивности) ≠ substitute-исполнитель (S12
      decision-brief-appointment-reschedule-model, замещающий мастер).
      Разные семантики одного термина; сверить при итоговой приёмке
      v0.3-final и reconciliation DEC-0022 — в этом документе «substitute»
      используется только во втором значении (deferral-ветка).

## Change Log

### v0.3-final (2026-07-28) — Owner rulings 2026-07-28 (финализация MVP primary-booking journey)

- **Deferral (вариант Б):** ветки reschedule / cancel / late-window /
  substitute / YClients reschedule закреплены в Non-goals; добавлена
  Deferred branches reconciliation/traceability table со ссылкой на
  `99 Archive/proposals/decision-brief-appointment-reschedule-model.md`
  (planned AYLA-DEC-0022, draft до Journey-reconciliation). Проверено:
  конфликтующих статусов, событий и операций в этапах 1–14 и N1–N9 нет.
- **Slot hold (AYLA-DEC-0021):** этапы 10–11 дополнены цепочкой
  «slot selected → hold acquired → confirmation in progress»;
  UX-формулировка «Слот временно закреплён за вами до HH:MM…» с
  серверным `expires_at` (TTL 15 минут); hold не показывается до
  фактического создания; после expiry — повторная проверка доступности;
  `SLOT_TAKEN` добавлен в ошибки этапа 11; внутренние термины (ledger,
  locking, reservation boundary) пользователю не отображаются.
- **Миграция имён событий — только active canonical:** `consent.granted /
  consent.revoked` (этап 3), `intent.resolution_produced` (этап 4),
  `appointment.created / appointment.confirmed / appointment.completed`
  (этапы 11, 12, 14). Pending-семейства (`recommendation.*`,
  `qualified_action.*`, `memory.*`) не мигрированы; отсутствующие события
  не выдуманы. `booking_confirmation_shown` (этап 12) оставлен
  legacy-маркером — канонического analytics event в реестре нет
  (registry gap в Open Question №8).
- **Open Question №8** переформулирован: реестр создан (v0.2); миграция —
  для active canonical names; pending и отсутствующие события — до
  утверждения записей реестра.
- **Temporary Context** зафиксирован как session-only класс (без
  persistence по умолчанию, без извлечения в будущих сессиях, перевод в
  persistent — только через Memory Proposal по AYLA-DEC-0024, использование
  в сессии — в пределах `purpose_tags`). Fact-level opt-out «не
  использовать для рекомендаций» не канонизирован — заменён ссылкой на
  модель `purpose_tags`.
- **Терминология этапов 11–12:** существительное Booking заменено на
  Appointment (создание и подтверждение записи, переход в `confirmed`);
  имена этапов сохранены дословно по Roadmap §2.1 («Booking creation»,
  «Booking confirmation») как канонические идентификаторы; цитаты полной
  UJS («Booking Request / Booking Created / Confirmed Booking», «Stage 5
  Booking») и UX-state tokens Roadmap §2.2 (booking pending/confirmed/
  failed) оставлены как legacy-цитаты.
- Баннер статуса синхронизирован: Draft v0.3-final. Статус документа не
  изменён: draft / proposed.
- **Дополнено при приёмке (2026-07-28):** добавлен Open Question №13
  (cross-document backlog): naming-дрейф полной UJS v1.2
  (`booking.created/confirmed` → канон `appointment.*` — отдельная аменда
  или deferral) и терминологическое пересечение «substitute offer»
  (полная UJS, proactive gate) vs substitute-исполнитель (S12
  decision-brief-appointment-reschedule-model) — на сверку при
  reconciliation DEC-0022.

### v0.3 (2026-07-28) — Приведение к AYLA-DEC-0023/0024/0025 (cross-decision сверка)

- **OQ №10 закрыт** (AYLA-DEC-0023/0024): whitelist — категориальная форма,
  наследование политики от категории, красная зона default deny, session
  state ≠ Persistent Memory, единственный pipeline
  inference → confirmation → persist, model-derived medical facts
  запрещены, расширение — только owner decision.
- **OQ №12 закрыт** (AYLA-DEC-0023/0024): consent state — authorization
  metadata, не Context Fact и не значение MemoryEntry; MemoryEntry
  ссылается на `consent_scope`, но согласие не персистируется как память.
- **OQ №8 — partially resolved** (AYLA-DEC-0025): решены конвенция
  имён, классификация, ownership, семантика intent- и consent-событий;
  открыты — регистрация `recommendation.*`, `qualified_action.attributed`,
  создание канонического Domain Event Registry, финальные payload/owner
  для этапа 14.
- **Миграция имён событий в Stage Specifications НЕ выполнена** (owner
  direction 2026-07-28): Decision Log не подменяет реестр; имена сохранены
  по источникам (Roadmap §6.4, CSR §9.1) и помечены как legacy/conflicting;
  приведение к канону AYLA-DEC-0025 — follow-up после создания
  Domain Event Registry. `recommendation.*` не объявлены
  зарегистрированными событиями.
- **Memory Interaction приведён к решениям:** поле переименовано в
  `proposal_confidence` — допустимо у MemoryProposal и в audit, но не
  переходит в canonical MemoryEntry (AYLA-DEC-0024 п. 1); упоминания
  whitelist (этап 6, факты, normative guard) переведены на категориальную
  форму; приведение Roadmap §3.4 и Scope Contract §4.1 выполнено единым
  Change Control approved-документов.
- Статус не повышён: draft/proposed. Открыты: OQ №1–7, №11; OQ №8 —
  partially resolved.

### v0.2.2 (2026-07-28) — OQ №9 закрыт по AYLA-DEC-0018 (accepted, Option C)

- **Open Question №9 закрыт** ссылкой на [[Ayla Decision Log]] (AYLA-DEC-0018,
  accepted 2026-07-28): Phase 1 (session-only) — самостоятельный технический
  release gate; Product Thesis Validation открыта до Phase 2 и успешного
  Product Thesis Validation Scenario; активация Phase 2 сама по себе
  validation не закрывает.
- Повторяющиеся оговорки «upstream Open Question №9» в Purpose, Journey
  Operating Model, Product Thesis Validation Scenario и Business Alignment
  заменены ссылками на принятое решение (по follow-up AYLA-DEC-0018).
  14 этапов journey не менялись.
- Уточнение [[Consent Scope Registry]] §10 и Scope Contract §3
  ([[Ayla MVP Scope and Release Contract]]) — отдельный follow-up Change
  Control по AYLA-DEC-0018, этим документом не выполняется.
- Статус не повышён: draft/proposed; approval блокируется Open Questions
  №6–8, №10–12 и сверкой с Intent Model (№7).

### v0.2.1 (2026-07-27) — Memory layer review fixes (по итогам review v0.2)

- **Open Question №8 расширен** до единой точки reconciliation всех
  candidate event names: Recommendation, Appointment, Memory Proposal и
  Context Fact events (включая `Created`/`Recorded`/`Confirmed` в Core
  Domain Model); все memory event names явно помечены candidate/non-stable.
- `ContextFactUsed` переклассифицирован: candidate, classification
  unresolved — не lifecycle domain event (использование факта не меняет
  его состояние; вероятнее audit `memory_fact_used` или recommendation
  evidence record).
- Memory taxonomy: добавлен normative guard — taxonomy не расширяет
  approved whitelist (persistent сохранение только для типов из whitelist +
  допустимый purpose + активный scope); добавлены статусы Outcome Fact
  (`reported`/`confirmed`/`inferred`/`disputed`/`superseded`).
- Provider-authored данные: уточнено — могут быть authoritative
  operational facts в owning domain, но не фактами о предпочтениях,
  намерениях или субъективном результате пользователя без его
  подтверждения.
- Context Sufficiency Model: разведены унаследованный принцип (факт —
  полная UJS, Context Sufficiency Gate) и proposal-контракт
  `context_summary`.
- User memory controls: «Не спрашивать снова» ограничен — не отключает
  mandatory safety/authorization/consent/freshness/legal checks.
- «Memory proof scenario» переименован в **Product Thesis Validation
  Scenario**; явно зафиксировано, что его статус release gate не установлен
  (зависит от Open Question №9).
- Memory Learning Loop: добавлена таблица предлагаемого владения
  областями цикла; поле `confidence` Memory Proposal объявлено proposal
  placeholder до Memory Contract.
- Этап 7: `recommendation_created` перенесён из domain event в analytics
  event (namespace fix).
- Metrics: добавлена оговорка — measurement method и baseline для
  memory-quality метрик pending Measurement Framework (ground truth для
  precision/recall; baseline для repeat-journey uplift).
- Open Question №9: добавлены варианты owner decision (A/B/C) с
  рекомендацией review — Option C. Open Questions №10–12 дополнены
  критериями решения.
- Статус не повышён: draft/proposed; approval блокируется Open Questions
  №6–12 и сверкой с Intent Model.

### v0.2 (2026-07-27) — Memory-first proposal layer (по итогам review)

- Purpose дополнен целями memory loop и memory proof **(proposal)**.
- Journey Operating Model: CAP-001 обозначена сквозной capability всего
  journey **(proposal)**; зафиксированы точки извлечения контекста за
  пределами этапа 6 (bootstrap, intent disambiguation, clarification
  suppression, recommendation-time, execution, outcome) **(proposal)**;
  уточнено, что нумерация этапов 4–6 — пользовательская ответственность, а
  не однопроходный порядок исполнения.
- Journey Overview: добавлена двухслойная модель — пользовательский слой
  (14 этапов, без изменений) + сквозной memory loop **(proposal)**.
- Memory Interaction расширен: Memory Learning Loop, memory taxonomy,
  Context Sufficiency Model, freshness/expiry/supersession, anti-lock-in и
  novelty guard, user memory controls, memory proof scenario — всё
  **(proposal)**, с сохранением фактов CSR/UJS без изменений.
- Recommendation and Proactivity Gates: добавлена Memory influence model
  **(proposal)** — память не сводится к preference boost; канонический
  порядок gates Killer PRD §5.1 сохранён.
- Metrics: добавлены memory-quality метрики **(proposal)**.
- Non-goals: добавлены запрещённые ложные трактовки памяти (часть — факты
  CSR/UJS, часть — proposal).
- Open Questions №9–12 (upstream): статус Phase 2 как product gate vs
  approved CSR §10; достаточность whitelist vs Roadmap §3.4 (Change
  Control); роль памяти в pipeline vs Killer PRD §5.1; «согласие на
  персонализацию» как Context Fact vs Consent state.
- Статус не повышён: draft/proposed; approval блокируется Open Questions
  №6–12 и сверкой с Intent Model.

### v0.1.1 (2026-07-27) — Event namespace clarification (по итогам review)

- Поле событий этапов разделено на три класса с разными владельцами
  контрактов: **domain event** (Roadmap §6.4), **analytics event** (рабочие
  имена, proposal), **audit event** (CSR §9.1); добавлено пояснение классов
  в начале Stage Specifications.
- Domain events, по которым Roadmap §6.4 расходится с Core Domain Model §11
  (`RecommendationShown`/`RecommendationPresented`,
  `AppointmentCreated`/`AppointmentRequested`), помечены *pending Domain
  Event Registry reconciliation*; добавлен Open Question №8 (включая
  семантику `IntentResolved` и доменный триггер этапа 14).
- `AppointmentCompleted` на этапе 14 переклассифицирован из analytics в
  domain event — входной триггер этапа, а не событие самого prompt.
- Редакторски уточнено поведение при отказе от рекомендации (этап 9, N9):
  первый отказ → alternative в пределах лимита; повторный или жёсткий отказ
  → suppression без новых предложений.
- Уточнено, что `ranking_economic_neutrality_alert` (этап 7) — внутренний
  policy/observability alert, а не user-facing ошибка.
- Статус не повышён: draft/proposed сохраняются до решения CAP-006 (Open
  Question №6), сверки с Intent Model (№7) и reconciliation событий (№8).

### v0.1 (2026-07-27) — Initial draft

- Документ создан по AYLA-DEC-0014 как производный MVP-срез
  [[Ayla User Journey Specification]] (Roadmap §2.1): 14 обязательных
  этапов с полями actor/trigger/цель/действие/состояние/ошибка/fallback/
  analytics event/owning capability и 9 обязательных негативных сценариев.
- Границы MVP зафиксированы по [[Ayla MVP Scope and Release Contract]]
  (§3 сценарий, §4 capabilities, §7 каналы); consent-шаги и fail-closed
  поведение — по [[Consent Scope Registry]] (§2, §5, §7, §8, §10).
- Маппинг CAP-ID выполнен по [[Ayla Domain Capability Registry]] §6 и
  помечен proposal до волны 2 (перевод записей в MVP-active).
- Ссылки на Ayla Intent Model Specification даны текстом как planned —
  документ в разработке, wikilink не установлен.
