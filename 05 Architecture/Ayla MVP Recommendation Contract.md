---
node_id: ayla.architecture.mvp-recommendation-contract
title: Ayla MVP Recommendation Contract
type: specification
status: draft
decision_status: proposed
version: "0.3"
owner: Product Architecture
priority: P0
knowledge_area:
  - architecture
domain:
  - recommendation
concerns:
  - safety
  - privacy
  - explainability
  - governance
system_owner:
  - ayla-recommendation
source_repository: ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
created: 2026-07-28
updated: 2026-07-29
review_cycle: monthly
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Decision Log]]"
  - "[[Killer PRD]]"
  - "[[Ayla MVP Scope and Release Contract]]"
  - "[[Consent Scope Registry]]"
  - "[[Ayla MVP User Journey Specification]]"
related:
  - "[[Ayla Domain Event Registry]]"
  - "[[Ayla Intent Model Specification]]"
  - "[[Ayla Core Domain Model Specification]]"
  - "[[Ayla Domain Capability Registry]]"
---

# Ayla MVP Recommendation Contract

> **Статус:** Draft v0.3 — proposed. Это не канонизация: документ определяет
> доменный контракт Recommendation для MVP и подлежит финальному review
> перед регистрацией событий.
> Основания: AYLA-DEC-0002 (memory-first тезис), AYLA-DEC-0018 (Product
> Thesis Validation), AYLA-DEC-0023 (whitelist), AYLA-DEC-0024 (Memory
> Contract), AYLA-DEC-0025 (event rules),
> [[Ayla MVP User Journey Specification]] v0.3,
> [[Ayla Domain Event Registry]] v0.2,
> [[Ayla Intent Model Specification]],
> [[Ayla Core Domain Model Specification]], [[Consent Scope Registry]],
> [[Ayla MVP Scope and Release Contract]], [[Killer PRD]].
>
> Документ **не** изменяет Domain Event Registry, **не** мигрирует Journey
> Stage Specifications и **не** закрывает OQ №11 (Journey) и OQ-E1
> (Registry) — их закрытие выполняется отдельным шагом после финального
> review. В v0.3 зафиксированы **owner rulings по OQ-R** (§26): R1 —
> immutable decision record + RecommendationSet; R2/R10 — publication
> matrix (§15); R3 — transport-level acknowledgement MAX для
> `recommendation.presented` (§16); R4 — таксономия qualified actions
> (§18); R5 — concrete attribution windows принадлежат Measurement
> Framework (§19); R6 — ownership availability/price после начала booking
> flow переходит Booking context (§22). OQ-R9 остаётся открытым
> (Privacy/Legal). В v0.2 устранены противоречия ревью v0.1:
> порядок gates, граница safety, модель идентичности
> RecommendationSet + отдельные Recommendation records, владение
> attribution-событием, immutable snapshot references.

## 1. Назначение

Документ отвечает на вопросы:

- Что в Ayla считается рекомендацией?
- Когда рекомендация появляется как доменный объект и кто её authoritative
  owner?
- Как intent, context, memory и candidate data влияют на результат?
- Чем primary recommendation отличается от альтернатив?
- Как рекомендация объясняется пользователю?
- Как связать рекомендацию с действием и результатом (attribution)?
- Какие события lifecycle можно зарегистрировать (предложение, §15)?
- Какие safety и consent gates обязательны?
- Что считается успешной рекомендацией?

## 2. Граница Recommendation

Recommendation — это **версионированное доменное решение**, связывающее
Intent Resolution, допустимый Context, допустимую Memory, Candidate Set,
Ranking Decision, Evidence, Explanation и применённые Safety/Consent Gates
с конкретным предлагаемым действием пользователя.

Базовая формулировка: Recommendation — зафиксированное решение Ayla
предложить пользователю один основной вариант и, при необходимости,
допустимые альтернативы на основании разрешённого контекста, evidence и
применённых policy gates.

Recommendation **не является**:

- сырым ответом LLM;
- списком кандидатов;
- результатом поиска;
- текстовым сообщением;
- записью (appointment);
- рекламным размещением;
- аналитическим событием.

## 3. Recommendation Record и RecommendationSet

Модель идентичности (**owner ruling OQ-R1 — ACCEPT, v0.3**; модель v0.2
по ревью P0-3 подтверждена; согласована с фактом [[Killer PRD]] §5.1:
каждая alternative имеет собственный `recommendation_id`):

- **Recommendation — immutable decision record** (не mutable aggregate);
- **RecommendationSet — immutable группирующая запись одной выдачи**
  (одного решения «что предложить сейчас»);
- **Каждый предложенный вариант — отдельная immutable Recommendation
  record** со своим `recommendation_id` (primary и каждая alternative);
- изменение candidate, ranking, evidence, consent evaluation, safety
  evaluation или decision semantics создаёт **новый
  `recommendation_id`**;
- presentation-only изменение не создаёт новую Recommendation и
  отражается через `presentation_version`;
- lifecycle `active | superseded | expired | invalidated` — вычисляемая
  projection, а не изменяемое поле записи (§14).

```yaml
RecommendationSet:
  recommendation_set_id:
  tenant_id:
  subject_id:              # псевдонимизированный идентификатор (§16 privacy)
  journey_id:
  intent_id:
  resolution_ref:
  primary_recommendation_id:
  alternative_recommendation_ids: []
  created_at:

Recommendation:            # immutable decision record
  recommendation_id:
  recommendation_set_id:
  recommendation_role: primary | alternative
  parent_recommendation_id:   # для alternative — primary, из которой выполнен rerank
  rerank_reason:              # для alternative; null у primary
  candidate_id:
  rank:
  reason_codes: []
  evidence_refs: []
  candidate_set_ref:
  context_snapshot_ref:       # immutable snapshot (§7)
  memory_snapshot_ref:        # immutable snapshot (§7)
  ranking_policy_version:
  explanation:
  safety_evaluation:
  consent_evaluation:
  created_at:
  expires_at:
  record_schema_version:      # версия схемы записи (v0.2; заменяет recommendation_version)
  presentation_version:       # версия представления; переформатирование без нового id
```

Ограничения (нормативные):

- полные чувствительные данные внутри Recommendation **не хранятся** —
  используются `context_snapshot_ref`, `memory_snapshot_ref`,
  `evidence_refs`;
- Recommendation воспроизводима настолько, насколько возможно (§25), но
  **не становится вторым хранилищем памяти**;
- consent/safety evaluations фиксируются как ссылки на результат
  применённых gates и версии политик, а не копии данных;
- **изменяемый `lifecycle_status` в записи не хранится** (v0.2, ревью):
  актуальное состояние — вычисляемая projection (`active | superseded |
  expired | invalidated`) по времени, событиям и action gates (§14, §17,
  §22); в записи — только `created_at`, `expires_at`,
  `supersedes_recommendation_id`;
- privacy-минимум (v0.2, ревью; расширен v0.3 по OQ-R9): идентификаторы
  псевдонимизированы; sensitive values не копируются. **Privacy export
  minimum (зафиксирован v0.3)** — пользовательскому privacy request
  подлежат: `recommendation_id`; `created_at`; user-visible
  recommendation content; user-visible explanation; категории
  использованных данных; факт использования persistent memory; категории
  источников; связанные с рекомендацией действия пользователя.
  **Не обязательно выдавать как есть:** internal ranking weights;
  anti-fraud signals; security controls; hidden policy internals; model
  hidden reasoning; full raw prompts; данные других субъектов;
  provider confidential data. Остальное — retention period; deletion vs
  legal hold; интерпретация derived data; являются ли digests personal
  data; export format; обработка immutable audit records; эффект удаления
  аккаунта; cross-repository deletion — **owner Privacy/Legal, OQ-R9
  открыт** (§26).

## 4. Ownership recommendation_id

Нормативно:

- `recommendation_id` создаётся **только Recommendation bounded context
  (Recommendation Engine)**;
- клиент, UI, Analytics, Appointment и LLM provider **не создают**
  authoritative `recommendation_id`;
- один `recommendation_id` идентифицирует **одну зафиксированную
  recommendation decision одного варианта** — не весь диалог, не весь
  journey и не всю выдачу (выдача — `recommendation_set_id`).

Модель пересчёта (принятое правило):

- незначительное техническое переформатирование — тот же
  `recommendation_id`, увеличивается `presentation_version`;
- изменение primary option, ranking или evidence — **новый
  `recommendation_id`**; новая запись содержит
  `supersedes_recommendation_id` (§21). Отдельного `decision_revision`
  в immutable-модели не существует (v0.2).

Так attribution остаётся однозначной.

## 5. Recommendation Pipeline

Нормативный pipeline — в **точном соответствии каноническому порядку
gates [[Killer PRD]] §5.1** (consent/privacy → safety →
eligibility/availability → relevance → preference → economic-neutrality →
primary output). v0.2: исправлен порядок — safety filtering предшествует
eligibility; ranking разделён на relevance и preference стадии. Если
техническая реализация потребует eligibility до safety, это — отдельное
архитектурное решение с изменением Killer PRD, а не редакционная правка
этого документа.

| # | Этап | Вход | Выход |
|---|---|---|---|
| 1 | Intent Resolution | пользовательское сообщение + session context | `resolution_ref` (Intent Model output) |
| 2 | Authorization and Consent Gate | resolution + consent state | допуск/отказ (fail-closed, CSR §2) |
| 3 | Context Retrieval | допуск + purpose | `context_snapshot_ref` (immutable) |
| 4 | Memory Retrieval | purpose-limited request (AYLA-DEC-0024 п. 3) | `memory_snapshot_ref` (immutable) |
| 5 | Candidate Generation | intent + context + catalog/provider/availability | Candidate Set (§8) |
| 6 | Safety Filtering | Candidate Set | безопасное подмножество (forbidden candidate не проходит дальше) |
| 7 | Eligibility and Availability Filtering | безопасное подмножество | Eligible Candidates |
| 8 | Relevance Scoring | Eligible Candidates | релевантность к intent/контексту |
| 9 | Preference Ranking | relevance scores + разрешённые предпочтения (§6) | Ranked Candidates |
| 10 | Economic-Neutrality Check | ranking (§11) | подтверждение/блокировка |
| 11 | Recommendation Assembly | ranked set | RecommendationSet: primary + допустимые alternatives |
| 12 | Explanation Assembly | ranking decision + evidence | Explanation (§13) |
| 13 | Persistence | assembled records | сохранённые Recommendation records |
| 14 | Presentation | persisted records | доставка каналу (§16) |
| 15 | Attribution | действие пользователя / результат | qualified action / outcome link (§18–20; владелец — Attribution context, §15) |

## 6. Влияние Memory на Recommendation

Нормативная модель (закрывает содержательную часть OQ №11; формальное
закрытие — после review).

**Граница safety (v0.2, ревью P0-2):** safety и policy constraints — не
конкурирующий источник предпочтений, а обязательный ограничивающий gate:

1. Authorization, consent and safety constraints **define the admissible
   set** — они ограничивают всю последующую обработку и не могут быть
   переопределены запросом, контекстом или памятью.
2. Current explicit request определяет активную цель пользователя
   **внутри** admissible set.
3. Session context уточняет цель.
4. Confirmed persistent memory персонализирует **только внутри
   оставшегося** admissible set.
5. Historical inferred signals — non-authoritative, пока не подтверждены.

Приоритет источников внутри admissible set:

```text
Current explicit user request
> Current session context
> Confirmed persistent memory
> Historical inferred signals (non-authoritative until confirmed)
```

**Memory может влиять только на:**

- candidate eligibility (учёт подтверждённых ограничений);
- ranking (preference weighting по типам фактов — Memory taxonomy,
  Journey v0.3);
- explanation (выбор раскрываемых причин);
- альтернативы (формирование и порядок);
- timing;
- channel or format preferences.

**Memory не может:**

- автоматически создавать медицинские выводы (AYLA-DEC-0023 п. 3);
- отменять явно выраженный текущий запрос пользователя;
- подменять safety constraints;
- обходить consent;
- превращать inferred proposal в факт (pipeline AYLA-DEC-0023 п. 2);
- необоснованно сужать выбор (anti-lock-in, Journey v0.3);
- скрыто увеличивать коммерческую выгоду платформы (§11).

Historical inferred signals не участвуют в ranking как факт, пока не
прошли Memory Learning Loop (confirmation → whitelist check → persist,
AYLA-DEC-0023 п. 2).

## 7. Immutable Snapshots (context, memory, candidates)

Для каждой recommendation decision фиксируются **immutable, версионированные
snapshot references** (v0.2, ревью P0-5). Ссылка на mutable source entity
(текущее состояние, временной retrieval result) запрещена: каждый
`snapshot_ref` обязан разрешаться в неизменяемую версию.

```yaml
snapshot_ref:
  snapshot_id:
  snapshot_version:
  content_digest:      # контроль неизменности содержимого
  captured_at:
  policy_version:

memory_snapshot:
  memory_entry_refs:
    - memory_id:
      memory_version:
      value_digest:    # исходное значение — в защищённом audit-хранилище;
                       # Recommendation хранит только ссылку и digest
      policy_version:
      consent_scope_version:
  category_policy_versions: []
  retrieved_at:
  retrieval_policy_version:
```

Правила:

- значения памяти в Recommendation не копируются, если это не требуется
  для audit;
- **более позднее изменение MemoryEntry (supersede, revoke, delete) не
  переписывает задним числом старую recommendation decision** — snapshot
  остаётся разрешимым в исходную версию (условие deterministic replay и
  attribution);
- snapshot недействителен для новых решений при `revoked`/`expired`
  состоянии соответствующего scope (read gate, AYLA-DEC-0024 п. 5);
- **retention dependency:** Recommendation не обещает deterministic
  replay дольше, чем хранятся необходимые immutable snapshots и версии
  политик; согласование сроков — с retention policy (OQ-E5 реестра).

## 8. Candidate Model

Различаются: **Candidate → Eligible Candidate → Ranked Candidate →
Recommended Option → Alternative**.

```yaml
Candidate:
  candidate_id:
  candidate_type:
  provider_ref:
  service_ref:
  availability_ref:
  price_snapshot:
  evidence_refs: []
  eligibility_status:
  exclusion_reasons: []
  ranking_features:
```

Кандидат, отфильтрованный safety или eligibility gate, **не попадает** ни
в primary recommendation, ни в alternatives (факт — Killer PRD §5.1:
исключённый на любом этапе не возвращается последующими).

## 9. Primary Recommendation

Primary recommendation — не единственный допустимый вариант, а **лучший
вариант по действующей ranking policy** (факт — Killer PRD §5.1: primary
одна). Одновременно доступна не более одной primary (Killer PRD §5.1).

```yaml
primary_option:            # Recommendation record с recommendation_role: primary
  candidate_id:
  rank:
  reason_codes: []
  evidence_refs: []
  explanation:
  match_quality_class: strong_match | acceptable_match | limited_evidence
```

`match_quality_class` (v0.2, ревью; заменяет `confidence_class`) —
категориальный атрибут объяснимости, вычисляемый из: completeness of
evidence; freshness; числа удовлетворённых preference criteria; отсутствия
неразрешённых противоречий. Он **не вычисляется** из LLM self-confidence
и **не означает**: вероятность медицинского успеха; гарантию качества;
вероятность записи; объективную истинность. Числовая confidence в MVP не
используется (OQ-R7 закрыт в v0.2, §26).

## 10. Alternatives

Альтернативы появляются только при условии (факт — Killer PRD §5.1: не
более двух; после отклонения primary фиксируется `rerank_reason`, Composer
повторно проходит с уточнённым constraint):

- прямой запрос пользователя;
- отказ от primary;
- недоступность primary;
- несовпадение цены;
- несовпадение времени;
- несовпадение мастера;
- недостаточная evidence для одного сильного выбора;
- требование policy показать выбор.

Каждая alternative — **отдельная Recommendation record** (§3):

```yaml
alternative:               # Recommendation record с recommendation_role: alternative
  recommendation_id:       # собственный (факт — Killer PRD §5.1)
  recommendation_set_id:   # общий с primary
  parent_recommendation_id:
  rerank_reason:
  candidate_id:
  rank:
  alternative_reason:
  differs_from_primary_by: []
  evidence_refs: []
```

Альтернативы **не показываются** ради искусственного «ассортимента» и не
предлагаются как равноправный каталог по умолчанию (Killer PRD §5.1).

## 11. Economic Neutrality

Факт — Killer PRD §5.3 и Конституция: комиссия, маржа, расходы на
рекламу, тариф или коммерческий статус provider **не влияют** на organic
ranking, порядок кандидатов и выбор primary.

Проверяемое правило (нормативное): commercial benefit to Ayla cannot be
a positive ranking feature unless the placement is explicitly disclosed
and excluded from organic recommendation ranking.

**Paid ranking — out of MVP scope.** Если paid placement появится
позднее, он отделяется от Recommendation Contract: рассчитывается
отдельно, явно маркируется и не заменяет organic primary (Killer PRD
§5.3). Обработка нарушений — quarantine ranking release и operational
handling contract (Killer PRD §5.3), здесь не пересматривается.

## 12. Evidence и Grounding

Каждая рекомендация имеет evidence. Минимальные виды: user-stated
evidence; confirmed memory; provider data; service data; availability
data; price snapshot; policy result; safety constraint; journey context.

```yaml
evidence_ref:
  evidence_id:
  source_type:          # user_stated | confirmed_memory | provider | service |
                        # availability | price | policy | safety | journey
  source_ref:
  observed_at:
  freshness_status:     # fresh | stale_marked | unknown
  verification_status:  # user_confirmed | provider_authoritative |
                        # system_observed | unverified (v0.2, ревью)
  applicability_scope:
```

Запрещено как основание: неподтверждённый inference как факт; скрытый
medical inference; данные без provenance; устаревший availability
snapshot без маркировки `stale_marked`.

## 13. Explanation Contract

Explanation — **производная от реального ranking decision**, а не
постфактум придуманный текст LLM. Отвечает: почему вариант подходит;
какие данные использованы; какие ограничения учтены; почему предложена
альтернатива; какие данные могли устареть.

```yaml
explanation:
  reason_codes: []
  user_visible_reasons: []
  limitations: []
  memory_used: true | false
  memory_disclosure_mode:   # per-scope disclosure согласно CSR
```

Запрещено (факты — Capability Registry §6.5, CAP-005 invariants;
Killer PRD §8): заявлять причины, которых не было в ranking; заявлять
неиспользованный факт; раскрывать sensitive memory без необходимости;
выдавать коммерческий ranking за персонализацию; делать медицинские
утверждения. Персонализация, которую Ayla не может объяснить,
недопустима (Journey v0.3, этап 8).

## 14. Lifecycle

Разделяются три слоя (принятое правило):

**Recommendation decision state — вычисляемая projection** (v0.2: в
immutable record не хранится):

```text
active        — создана, не superseded, не expired, не invalidated
superseded    — заменена новым решением (supersedes_recommendation_id)
expired       — истёк TTL/freshness (expires_at, §22)
invalidated   — дальнейшее использование запрещено policy/action gate
                (consent revocation, safety policy change, provider
                removal — иная природа, чем expiry; v0.2, ревью)
```

**Interaction facts (факты взаимодействия, не состояние aggregate):**

```text
presented, accepted, declined, acted_upon
```

**Outcome facts:**

```text
attribution result (владелец — Attribution context, §15)
```

Recommendation не превращается в агрегат всей пользовательской
аналитики: interaction и outcome facts ссылаются на `recommendation_id`,
но живут в соответствующих контурах (§15, §18).

## 15. Recommendation Events

События предлагаются к регистрации в [[Ayla Domain Event Registry]]
**после финального review этого контракта** (реестр этим документом не
изменяется; регистрация — отдельная задача). Publication matrix принята
**owner ruling OQ-R2/R10 — ACCEPT (v0.3)**:

| Event | Semantic class | Authoritative owner | Publication scope |
|---|---|---|---|
| `recommendation.created` | domain + integration | Recommendation | cross_context |
| `recommendation.superseded` | domain + integration | Recommendation | cross_context |
| `recommendation.expired` | domain | Recommendation | internal |
| `recommendation.invalidated` | domain + integration | Recommendation | cross_context |
| `recommendation.presented` | interaction + integration | Channel Delivery / Interaction | cross_context |
| `recommendation.accepted` | interaction + integration | Channel Delivery / Interaction | cross_context |
| `recommendation.declined` | interaction + integration | Channel Delivery / Interaction | cross_context |
| `qualified_action.attributed` | attribution + integration | Attribution / Measurement | cross_context |

Детали (owner ruling):

- **`recommendation.created`** публикуется после успешного persistence
  Recommendation — **не** после LLM generation, ranking calculation, API
  assembly или presentation. `recommendation.generated` **не
  используется**: Recommendation существует с persistence; LLM-генерация
  — internal technical step.
- **`recommendation.superseded`** публикуется только после создания новой
  Recommendation, содержащей `supersedes_recommendation_id`; payload
  включает оба идентификатора.
- **`recommendation.expired`** — internal в MVP: корректность
  использования обеспечивается `expires_at` и read/action gate (§22);
  integration consumers не должны зависеть от гарантированной доставки
  expiry event. Событие используется для projection, cleanup, analytics,
  observability.
- **`recommendation.invalidated`** — cross_context: downstream обязан
  прекратить действие по рекомендации при consent revocation, safety
  policy change, provider removal, policy prohibition; action gate всё
  равно остаётся обязательным (в v0.2 был candidate — подтверждён
  ruling R2/R10).
- **Interaction events** (`presented`, `accepted`, `declined`):
  authoritative owner — **Channel Delivery / Interaction**, а не
  Recommendation Engine, потому что channel layer знает, что было
  доставлено, какой acknowledgement получен и какое явное действие
  совершил пользователь.

**Attribution event** (подтверждено rulings R2/R10 и P0-4): факт
атрибуции — **`qualified_action.attributed`**, authoritative owner —
**Attribution / Measurement bounded context** (регистрация — через Domain
Event Registry отдельным шагом, OQ-E1). `recommendation.action_attributed`
— **rejected alternative**: Recommendation context не объявляет сам, что
внешнее действие принадлежит ему (attribution = Recommendation
существовала + action произошло + attribution policy применилась).
Контракт задаёт только обязательные ссылки (§18).

## 16. Presentation Semantics

`recommendation.presented` **не означает**: создание объекта; отправку в
очередь; формирование API response; генерацию текста; фактический
просмотр пользователем (`presented ≠ viewed`).

**Owner ruling OQ-R3 — ACCEPT for MVP (v0.3):**
`recommendation.presented` означает, что сообщение с конкретным
`recommendation_id` принято каналом MAX для доставки и получен
transport-level delivery acknowledgement. Это **не означает**, что
пользователь увидел или прочитал сообщение. Владение фактом:

```yaml
authoritative_owner: Channel Delivery / Interaction
producer: channel adapter
payload:
  required: [recommendation_id, recommendation_set_id, channel,
             channel_message_id, delivery_ack_type, acknowledged_at]
  channel: max
delivery_ack_type: accepted_by_channel | delivered_to_recipient |
                   read_by_recipient
```

Правила (owner ruling):

- событие допускается уже при `accepted_by_channel`;
- если MAX позже даёт более сильный acknowledgement
  (`delivered_to_recipient`, `read_by_recipient`), он фиксируется как
  **отдельный interaction observation** — исходное событие
  `recommendation.presented` не переписывается;
- attribution policy учитывает силу acknowledgement:
  `accepted_by_channel` < `delivered_to_recipient` <
  `read_by_recipient`; для MVP наличия `accepted_by_channel` достаточно,
  чтобы считать Recommendation presented в техническом смысле;
- единый delivery standard на все каналы без типа подтверждения не
  применяется; если канал не предоставляет read receipt, фактический
  просмотр не гарантируется.

Внутренний шаг `recommendation.presentation_requested` может остаться
internal technical event и отдельно не регистрируется.

## 17. Acceptance и Decline

- `recommendation.accepted` — **пользователь явно выбрал конкретный
  recommendation option как следующий вариант действия** (строгое
  определение, v0.2). Конкретное действие фиксируется отдельно:

```yaml
acceptance_action: select | proceed_to_booking | request_booking
```

  Открытие booking flow и подтверждение записи — **разные** уровни
  намерения и не считаются одинаковым acceptance. Acceptance **не
  означает** завершённую запись (appointment completion).
- `recommendation.declined` — **только явный отказ**. Бездействие не
  равно decline.
- При выборе alternative фиксируется связь (v0.2 — по модели §3,
  `option_id` не используется):

```yaml
accepted_recommendation_id:      # id записи выбранного варианта
recommendation_role: primary | alternative
recommendation_set_id:
parent_recommendation_id:        # для alternative
```

Alternative атрибутируется только по собственному `recommendation_id`
(факт — Killer PRD §5.1/§6.2).

## 18. Qualified Action Attribution

Qualified action в MVP — типизированное действие; смешение разных
действий в одно событие без `action_type` запрещено. **Owner ruling
OQ-R4 — ACCEPT taxonomy (v0.3):** действия разделяются на четыре
категории — не все обязаны быть qualified:

| Категория | Примеры | Статус в MVP |
|---|---|---|
| Engagement action | `recommendation_selected`, `details_opened`, `alternative_requested` | **Не qualified** — интерес, не бизнес-результат |
| Booking progression action | `booking_flow_started`, `specialist_selected`, `service_selected`, `slot_selected`, `booking_intent_confirmed` | **Qualified** — qualified action начинается с booking progression |
| Transaction action | `appointment_created`, `appointment_confirmed`, `payment_completed` | **Qualified** — создан значимый бизнес-объект |
| Service outcome | `appointment_completed` | **Candidate outcome** — blocked by OQ-E3 / Appointment Contract (Domain Event Registry v0.2, `semantic_status: incomplete`) |

**Product Thesis Validation отделена от qualified action** (owner
ruling): для неё недостаточно `booking_flow_started`; минимально сильный
сигнал — `appointment_created`, более сильные — `appointment_confirmed`,
`appointment_completed`. Конкретный thesis threshold синхронизируется с
Killer PRD / Measurement Framework и этим контрактом не фиксируется.

Recommendation Contract задаёт **обязательные ссылки** для attribution
(владелец записи атрибуции — Attribution / Measurement bounded context,
§15):

```yaml
QualifiedActionAttribution:
  attribution_id:
  recommendation_id:         # выбранный вариант (§17)
  recommendation_set_id:
  action_type:               # обязателен
  action_category:           # engagement | booking_progression |
                             # transaction | service_outcome
  qualifies_for_attribution: true
  qualifies_for_product_thesis: true | false
  action_ref:
  attribution_type: direct | assisted
  attributed_at:
  attribution_policy_version:
  evidence_refs: []
```

Правила (факт — Killer PRD §6.2): временная близость недостаточна; один
qualified action имеет не более одной winning recommendation; отклонённая
или invalidated recommendation не атрибутируется; при неоднозначности —
`unattributed`.

**Нормализация типов (v0.2, ревью):**

- **direct** — явный переход/выбор конкретной Recommendation → qualified
  action в direct window;
- **assisted** — Recommendation была presented + существует допустимое
  evidence связи + действие в assisted window + отсутствует более сильная
  winning recommendation. При отсутствии direct chain применяется
  **отдельная assisted attribution policy**; если её критерии не
  выполнены, действие — `unattributed`, а не assisted по умолчанию;
- **unattributed** — доказуемой связи недостаточно.

## 19. Attribution Window

Attribution window зависит от сценария и типа действия (факт — Killer
PRD §6.3: начальные значения — гипотезы пилота). **Owner ruling OQ-R5 —
CLOSED by ownership (v0.3):** конкретные attribution windows принадлежат
**Measurement Framework и versioned Attribution Window Registry** и этим
контрактом не фиксируются. Recommendation Contract определяет только:

- обязательность `policy_version`;
- prospective application — изменения применяются перспективно и **не
  переклассифицируют** исторические события;
- различение `direct | assisted | unattributed` (§18).

Минимальный контракт:

```yaml
attribution_policy_ref:
  policy_id:
  policy_version:
  scenario_type:
```

При каждом attribution event сохраняются:

```yaml
window_type: direct | assisted
window_started_at:
window_expires_at:
policy_version:
```

Versioned Attribution Window Registry — факт, Killer PRD §6.3: версия
registry сохраняется в каждом attribution событии. Числовые значения окон
остаются открытыми в Measurement Framework — для Recommendation Contract
вопрос решён: **окна не принадлежат этому документу**.

## 20. Killer Moment

Killer moment засчитывается **только при доказуемой связи через
`recommendation_id`** (факт — Killer PRD §6.1, пять условий). Недостаточно:
пользователь увидел рекомендацию; пользователь позже записался; совпала
услуга или provider; временная близость.

Обязательный attribution chain:

```text
recommendation_id
→ presented option
→ user action (action_type)
→ appointment or qualified action
→ в пределах применимого attribution window (direct | assisted)
```

Metric deduplication и reporting windows (например, «не более одного
killer moment одного scenario_type за скользящие 7 дней») управляются
Killer PRD §6.4 / Measurement Framework и **не изменяют underlying
attribution facts** (v0.2, ревью: это measurement policy, а не доменная
семантика Recommendation).

## 21. Replacement и Supersession

При существенном изменении рекомендации — новый `recommendation_id` со
ссылкой `supersedes_recommendation_id` (§4). Старая рекомендация
**остаётся в истории и не переписывается**.

Причины supersession: `user_context_changed`, `availability_changed`,
`price_changed`, `user_declined`, `safety_constraint_changed`,
`consent_changed`, `memory_changed`, `explicit_refresh`.

Изменение consent или memory **не меняет задним числом** старую
recommendation, но может сделать её непригодной для дальнейшего действия
— состояние `invalidated` (§14, §24), отличное от `expired`.

## 22. Expiry

Recommendation имеет TTL или условия истечения: availability устарела;
price snapshot устарел; journey завершён; пользователь изменил intent;
candidate стал недоступен.

Отдельно от expiry (v0.2): **invalidation** — запрет дальнейшего
использования по policy/action gate: consent отозван; safety policy
изменилась; provider removed. Expiry — про freshness; invalidation — про
допустимость.

Инвариант (нормативный): **отсутствие события `recommendation.expired`
не разрешает использовать рекомендацию после `expires_at`** — read/action
gate проверяет актуальность напрямую (аналог consent/memory read gate,
AYLA-DEC-0024 п. 5а).

**Owner ruling OQ-R6 — ACCEPT (v0.3): Recommendation expiry и начатый
booking flow.**

- До начала booking flow Recommendation является источником перехода,
  но **не authoritative source** availability или price.
- После начала booking flow **Booking context принимает ownership** над
  slot, price, provider availability и booking state (включая slot hold,
  AYLA-DEC-0021).
- Истечение или supersession Recommendation **не отменяет автоматически**
  уже начатый booking flow.
- Booking context обязан повторно проверить: availability; current
  price; provider eligibility; safety/action gates; consent
  requirements. Если проверка не проходит, booking flow блокируется или
  требует повторного выбора.

Разделение состояний:

| Ситуация | Поведение |
|---|---|
| Recommendation expired **до** начала booking | Переход запрещён, требуется refresh |
| Recommendation expired **после** начала booking | Flow может продолжиться только после Booking revalidation |
| Recommendation `invalidated` | Flow блокируется независимо от того, был ли он начат, если invalidation reason применим к действию |

`expired ≠ invalidated`: expiry — freshness, invalidation — допустимость
действия.

## 23. Safety

Контракт ссылается на safety policy, а не определяет медицинскую логику
заново (MVP Safety Policy — planned, Roadmap §7.3; границы — Killer PRD
§4.1 OD-K6, §8–9). Минимальные правила:

- forbidden candidate не ранжируется;
- health inference не создаётся из food/beauty сигналов (Killer PRD
  OD-K6);
- user-stated contraindication учитывается как ограничение (user-stated
  safety constraints — AYLA-DEC-0023 п. 3);
- отсутствие safety data не превращается в подтверждение безопасности;
- recommendation не заменяет медицинскую консультацию;
- unsafe recommendation не может быть сохранена как primary;
- при safety block — S8 Boundary Handling (полная UJS; Journey v0.3, N8).

## 24. Consent

До использования Memory проверяются: active consent scope; purpose
compatibility; whitelist category; retention validity; revocation status
(fail-closed, CSR §2).

При отзыве consent после создания Recommendation:

- историческая запись Recommendation сохраняется согласно retention;
- новая персонализированная выдача запрещена;
- старая Recommendation переводится в состояние `invalidated` для
  действия (§14, §22) — использование зависит от action gate;
- повторное раскрытие memory-derived explanation запрещено без
  подходящего scope.

## 25. Observability и Replay

Для deterministic replay фиксируются (proposal):

```yaml
model_provider:
model_version:
prompt_version:
ranking_policy_version:
candidate_snapshot_ref:    # immutable (§7)
memory_snapshot_ref:       # immutable (§7)
context_snapshot_ref:      # immutable (§7)
safety_policy_version:
consent_policy_version:
```

Полный prompt и **hidden reasoning / chain-of-thought модели не
сохраняются** как часть Recommendation Contract (нормативный запрет).
Replay гарантируется только в пределах retention dependency (§7).

## 26. Open Questions и Owner Rulings

В v0.3 владельцем зафиксированы rulings по пакетам: **A — Product
Architecture** (R1, R2/R10, R6), **B — Product + Measurement** (R4, R5),
**C — Channel** (R3), **D — Privacy/Legal** (R9 — открыт).

- **OQ-R1 — ACCEPT (v0.3, пакет A).** Recommendation — immutable
  decision record; RecommendationSet — immutable группирующая запись
  одной выдачи; каждый primary и alternative имеет собственный
  `recommendation_id`; изменение candidate, ranking, evidence,
  consent/safety evaluation или decision semantics создаёт новый
  `recommendation_id`; presentation-only изменение — через
  `presentation_version`; lifecycle — вычисляемая projection (§3, §14).
- **OQ-R2/R10 — ACCEPT (v0.3, пакет A).** Publication matrix
  зафиксирована (§15): `recommendation.created`, `.superseded`,
  `.invalidated` — domain + integration, cross_context, owner
  Recommendation; `recommendation.expired` — domain, internal;
  interaction events — owner Channel Delivery / Interaction;
  `qualified_action.attributed` — attribution + integration, owner
  Attribution / Measurement.
- **OQ-R3 — ACCEPT for MVP (v0.3, пакет C).** Transport-level delivery
  acknowledgement MAX достаточно для `recommendation.presented`;
  `presented ≠ viewed`; событие допускается при `accepted_by_channel`;
  более сильные acknowledgement — отдельные interaction observations,
  исходное событие не переписывается (§16).
- **OQ-R4 — ACCEPT taxonomy (v0.3, пакет B).** Таксономия engagement /
  booking progression / transaction / service outcome принята (§18);
  qualified action начинается с booking progression; Product Thesis
  threshold (минимум `appointment_created`) синхронизируется с Killer
  PRD / Measurement Framework.
- **OQ-R5 — CLOSED by ownership (v0.3, пакет B).** Конкретные
  attribution windows принадлежат Measurement Framework / versioned
  Attribution Window Registry; контракт хранит только versioned policy
  reference и правила prospective application (§19). Для этого документа
  вопрос решён; числовые значения остаются открытыми в Measurement
  Framework.
- **OQ-R6 — ACCEPT (v0.3, пакет A).** После начала booking flow
  ownership availability/price переходит Booking context; обязательна
  повторная валидация; expired ≠ invalidated (§22).
- **OQ-R7 — ЗАКРЫТ (v0.2).** Числовая recommendation confidence не
  входит в MVP; используется `match_quality_class` — категориальный
  атрибут объяснимости, не вероятность (§9).
- **OQ-R8 — post-MVP backlog.** Paid placement вне organic ranking —
  out of MVP scope (§11).
- **OQ-R9 — OPEN (пакет D, владелец Privacy/Legal).** Privacy export
  minimum зафиксирован (§3); открыты для Privacy/Legal: retention
  period; deletion vs legal hold; интерпретация derived data; являются
  ли digests personal data; export format; обработка immutable audit
  records; эффект удаления аккаунта; cross-repository deletion
  (совместно с AMD-020 C5 export/forget). OQ-R9 **не блокирует**
  регистрацию базовых recommendation events — privacy-minimum записи
  сохранён (§3), события не содержат чувствительных значений.

## Change Log

### v0.3 (2026-07-29) — Owner rulings по OQ-R

- **OQ-R1 — ACCEPT:** Recommendation — immutable decision record +
  immutable RecommendationSet; каждый вариант — отдельная запись со
  своим `recommendation_id`; существенное изменение решения — новый id;
  presentation-only — `presentation_version`; lifecycle — projection
  (§3, §14).
- **OQ-R2/R10 — ACCEPT:** publication matrix (§15): created/superseded/
  invalidated — domain + integration, cross_context, owner
  Recommendation; expired — domain, internal; presented/accepted/
  declined — interaction + integration, owner Channel Delivery /
  Interaction; `qualified_action.attributed` — attribution +
  integration, owner Attribution / Measurement. Детали: created — после
  persistence; superseded — payload с обоими id; invalidated подтверждён
  (в v0.2 — candidate).
- **OQ-R3 — ACCEPT for MVP:** transport-level delivery acknowledgement
  MAX достаточно для `recommendation.presented`; enum
  `delivery_ack_type` (accepted_by_channel / delivered_to_recipient /
  read_by_recipient); более сильные ack — отдельные observations;
  `presented ≠ viewed` (§16).
- **OQ-R4 — ACCEPT taxonomy:** engagement / booking progression /
  transaction / service outcome; qualified action — с booking
  progression; Product Thesis Validation отделена (минимальный сигнал
  `appointment_created`), threshold — за Killer PRD / Measurement
  Framework; в схему атрибуции добавлены `action_category`,
  `qualifies_for_attribution`, `qualifies_for_product_thesis` (§18).
- **OQ-R5 — CLOSED by ownership:** concrete windows принадлежат
  Measurement Framework / versioned Attribution Window Registry;
  контракт — только `attribution_policy_ref` и prospective rules (§19).
- **OQ-R6 — ACCEPT:** после начала booking flow ownership
  availability/price — у Booking context; обязательна revalidation;
  expired ≠ invalidated (§22).
- **OQ-R9 — OPEN (Privacy/Legal):** зафиксирован privacy export minimum
  (§3); retention/deletion/export-формат и пр. — за Privacy/Legal;
  не блокирует регистрацию базовых recommendation events.
- Domain Event Registry и Journey Spec этой версией **не изменяются**;
  документ готов к финальному review перед регистрацией событий
  (`recommendation.*`, `qualified_action.attributed`) и закрытием
  OQ-E1 / OQ №11 — отдельными шагами. Статус: draft / proposed.

### v0.2 (2026-07-28) — Review correction (архитектурное ревью v0.1)

- **P0-1 (порядок gates):** pipeline приведён в точное соответствие
  канону Killer PRD §5.1: Safety Filtering (6) предшествует Eligibility
  and Availability Filtering (7); ranking разделён на Relevance Scoring
  (8) и Preference Ranking (9). Зафиксировано: изменение порядка
  eligibility/safety — отдельное архитектурное решение с изменением
  Killer PRD.
- **P0-2 (граница safety):** safety/policy constraints вынесены из
  линейного приоритета источников — они определяют admissible set для
  всей обработки; приоритет источников действует только внутри него.
- **P0-3 (модель идентичности):** принята модель RecommendationSet +
  отдельные immutable Recommendation records (primary и каждая
  alternative со своим `recommendation_id`, `recommendation_role`,
  `parent_recommendation_id`, `rerank_reason`) — согласовано с фактом
  Killer PRD §5.1; контейнерная модель «одна Recommendation со всеми
  вариантами» отклонена; `option_id` упразднён.
- **P0-4 (attribution event):** `recommendation.action_attributed`
  удалён (rejected alternative); факт атрибуции —
  `qualified_action.attributed`, owner — Attribution / Measurement
  bounded context; контракт задаёт только обязательные ссылки.
- **P0-5 (snapshots):** snapshot references — immutable и
  версионированные (`snapshot_id`, `snapshot_version`, `content_digest`,
  `captured_at`, `policy_version`); `memory_entry_ref` с
  `memory_version` и `value_digest`; добавлена retention dependency.
- **P1:** `recommendation_version` заменён на `record_schema_version` +
  `presentation_version`; изменяемый `lifecycle_status` удалён —
  lifecycle как projection (active/superseded/expired/invalidated);
  добавлено состояние `invalidated` (policy/action gate) отдельно от
  `expired`; `recommendation.presented` — owner Channel Delivery /
  Interaction с `delivery_ack_type`, `presented ≠ viewed`;
  `recommendation.accepted` — строгое определение + `acceptance_action`;
  direct/assisted/unattributed нормализованы (assisted — отдельная
  policy, не default); metric deduplication вынесена из доменной
  семантики; `appointment_completed` — candidate qualified action;
  `confidence_class` → `match_quality_class` (OQ-R7 закрыт);
  `evidence_ref` — `verification_status` вместо `confidence_scope`;
  privacy-минимум записи зафиксирован (§3); OQ-R переструктурированы
  (R1 — рекомендация immutable record, R2+R10 объединены, R8 — post-MVP
  backlog, R9 — владелец Privacy/Legal).
- Статус не изменён: draft / proposed. OQ №11 (Journey) и OQ-E1
  (Registry) по-прежнему не закрываются этим документом.

### v0.1 (2026-07-28) — Initial draft

- Документ создан по owner direction: Recommendation как версионированное
  доменное решение (не ответ LLM); Recommendation Record с
  snapshot-ссылками вместо копий данных; ownership `recommendation_id` за
  Recommendation bounded context; модель supersession через новый
  `recommendation_id`.
- Pipeline из 15 этапов, согласованный с каноническим порядком gates
  Killer PRD §5.1; нормативная модель влияния memory (§6) с приоритетом
  источников; Memory Snapshot с запретом ретроактивного переписывания.
- Candidate/primary/alternatives разделены; `confidence_class` вместо
  числовой confidence; economic neutrality закреплена; paid ranking —
  out of MVP.
- Lifecycle разделён на decision state / interaction facts / outcome
  facts; предложены события `recommendation.*` (§15) без регистрации в
  Domain Event Registry; `recommendation.generated` отклонён в пользу
  `recommendation.created`.
- Presentation/acceptance/decline semantics: presented = delivery
  acknowledgement канала; acceptance ≠ booking completion; бездействие ≠
  decline.
- Attribution: `action_type` обязателен; windows — versioned
  configuration, не константы; killer moment — только через
  `recommendation_id`-цепочку.
- Safety/consent gates, expiry с action gate, observability без hidden
  reasoning; Open Questions OQ-R1..R10.
- OQ №11 (Journey) и OQ-E1 (Registry) намеренно не закрыты — после
  review и решений OQ-R. Статус: draft / proposed.
