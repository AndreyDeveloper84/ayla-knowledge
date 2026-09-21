---
node_id: ayla.architecture.mvp-recommendation-contract
title: Ayla MVP Recommendation Contract
type: specification
status: draft
decision_status: proposed
version: "0.6"
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
updated: 2026-09-22
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
  - "[[Ayla Glossary]]"
  - "[[Ayla Memory Model Specification]]"
  - "[[BOT-003 Discovery and Recommendation Conversation Specification]]"
  - "[[Recommendation UX Addendum]]"
  - "[[Ayla Decision Policy Contract]]"
  - "[[Recommendation Architecture Final Reconciliation]]"
---

# Ayla MVP Recommendation Contract

> **Статус:** Draft v0.6 — proposed. Это не канонизация: документ определяет
> доменный контракт Recommendation для MVP и подлежит финальному review
> перед регистрацией событий.
>
> **v0.5 (2026-09-21) — поправка по решениям владельца AYLA-DEC-0087,
> 0091, 0094, 0096, 0097, 0100** (бриф этапа B ред. 2, Итог 3 п.14) и по
> решению владельца 21.09 о переносе из ayla-knowledge PR #21 (журнал
> главного окна CD §71, вне git). Суть: Goal не является обязательным
> этапом (§5, §27–§31); исход выбора следующего шага — закрытый набор
> [[Ayla Decision Policy Contract]] (§32); порядок входного пути N-1 (§5,
> §23); аллергический фильтр с `UNKNOWN` (§23); NBA-семейства до пилота не
> включаются (§26, §33); вариант исполнения `plan` без цели Ayla не
> предлагает (§34); Desired Outcome не активируется (§3, §28). Блоки
> поправки помечены «v0.5». Текст v0.4 сохранён. Версия — v0.5, а не
> v1.0: перенос «v1.0 = v0.4 + A1 + A2» из #21 целиком не выполняется
> (Change Log v0.5).
>
> **v0.6 (2026-09-22, KB-F, DRF-2270) — остаток ayla-knowledge PR #21 на
> отдельное утверждение владельца** (журнал главного окна CD §71 п.1, вне
> git: «Полезные изменения из PR #21 собрать отдельно… и представить на
> самостоятельное утверждение»). Перенесено то из A1 и A2 PR #21, что не
> вошло в v0.5 и не противоречит AYLA-DEC-0087…0101 и CD §71 п.2–3:
> предмет записи = WHAT, `action_type` → вариант исполнения (§3, §33,
> §34); `actionable_until` вместо `expires_at` и retention отдельно (§3,
> §14, §15, §22, §26); семантическое разрешение и его уточнение (§5,
> §28–§29); DecisionReadiness — только в тени (§30); четыре состояния
> safety и правило B6 (§5, §23); три логических снимка и replay (§7, §25);
> допуск только `VERIFIED` (§5, §8); альтернативы по действию (§10);
> события B8 (§15, §17); инвариант D4 (§22). Блоки помечены «v0.6 · KB-F».
> **Не перенесено** (конфликт с решениями): NBA-семейства provisional (CD
> §71 п.2), `DesiredOutcome` refs и условие `≥ 1` (AYLA-DEC-0094), «C03 =
> адаптивный DecisionReadiness flow» и замена этапов 7–8 (AYLA-DEC-0097),
> «сквозной» safety-этап и «гейтов ровно два» (AYLA-DEC-0096). Версия —
> v0.6, не v1.0: без этих частей документ не равен тому, что PR #21
> называл «v1.0 = v0.4 + A1 + A2»; статус не изменён (draft / proposed).
> При отказе владельца блоки v0.6 снимаются целиком, документ
> возвращается к v0.5. Таблица — `docs/audits/2026-09-22-pr21-rest-kb-f.md`.
>
> Основания: AYLA-DEC-0002 (memory-first тезис), AYLA-DEC-0018 (Product
> Thesis Validation), AYLA-DEC-0023 (whitelist), AYLA-DEC-0024 (Memory
> Contract), AYLA-DEC-0025 (event rules), AYLA-DEC-0045 / OD-9 (LLM не
> ranking authority; `no_action` — валидный результат),
> [[Ayla MVP User Journey Specification]] v0.3,
> [[Ayla Domain Event Registry]] v0.2,
> [[Ayla Intent Model Specification]],
> [[Ayla Core Domain Model Specification]], [[Consent Scope Registry]],
> [[Ayla MVP Scope and Release Contract]], [[Killer PRD]],
> [[Ayla Glossary]] (Goal, Outcome, Next Best Action).
>
> В v0.4 зафиксирован пакет решений **R-NBA-1…R-NBA-8**: Recommendation =
> Canonical Next Best Action («что сделать»), отделённое от Execution
> Mapping («как») и Provider Ranking («кто»); Recommendation Suitability ≠
> Execution Feasibility (экономическая нейтральность выбора NBA);
> композиционная таксономия NBA (`family + target + action_type`, семейства
> — кандидаты, OQ-R11); Safety — gate, не семейство; контролируемая
> Recommendation Decision Policy; адаптивная clarification (C03) от
> недостающих фактов; нормативная граница C04 (WHAT + WHY) / C05 (HOW).
> Канонический порядок gates Killer PRD §5.1 (consent/privacy → safety →
> …) сохранён; правила eligibility/availability/relevance/preference/
> economic-neutrality **перенесены без удаления** на уровень
> Execution Mapping / Provider Ranking (§5, §8, §34); приведение
> Killer PRD §5 в соответствие — отдельная правка (OQ-R12). В §13 перенесено
> правило owner 2026-07-29 «нет displayable объяснения → не показываем»
> (из [[Recommendation UX Addendum]] §2).
> Новые разделы продуктово-семантического слоя (§27–§34) размещены после
> §26, чтобы сохранить действующие ссылки на разделы v0.3 из
> Recommendation UX Addendum и других документов.
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
- Что такое Canonical Next Best Action и чем Recommendation («что
  сделать») отличается от Execution Mapping («как») и Provider Ranking
  («кто»)? (v0.4)
- Откуда появляются Goal и Outcomes и когда контекст достаточен для
  решения? (v0.4)
- Когда рекомендация появляется как доменный объект и кто её authoritative
  owner?
- Как intent, goal, outcomes, context и memory влияют на решение? (v0.4)
- Чем primary recommendation отличается от альтернатив?
- Как рекомендация объясняется пользователю?
- Как связать рекомендацию с действием и результатом (attribution)?
- Какие события lifecycle можно зарегистрировать (предложение, §15)?
- Какие safety и consent gates обязательны?
- Что считается успешной рекомендацией?

## 2. Граница Recommendation

Recommendation — это **версионированное доменное решение**, связывающее
Intent Resolution, Goal, Outcomes, допустимый Context, допустимую Memory,
Context Sufficiency, применённые Safety/Consent Gates и Recommendation
Decision Policy с конкретным **Canonical Next Best Action (NBA)** —
действием, с которого разумно начать пользователю сейчас (термин —
[[Ayla Glossary]]: «наиболее полезное, безопасное и реалистичное действие
в текущем контексте»; не означает коммерчески наиболее выгодное действие).

Базовая формулировка: Recommendation — зафиксированное решение Ayla
предложить пользователю один основной Next Best Action и, при
необходимости, допустимые альтернативы на основании разрешённого
контекста, evidence и применённых policy gates.

Три разных вопроса (нормативное разделение, v0.4, R-NBA-8):

- **Recommendation Engine — что пользователю следует сделать?** Выбор NBA;
  предмет этого контракта.
- **Execution Mapping — как это можно сделать?** Варианты реализации NBA
  (услуги Ayla, self-care, наблюдение и т. п.) — downstream, §34.
- **Provider Ranking — кто должен реализовать выбранный вариант
  исполнения?** Ранжирование provider/service кандидатов — downstream,
  §8, §34.

Семантика provider ranking **не является** Recommendation Decision Policy
и не влияет на выбор NBA (§31).

Recommendation **не является**:

- Goal (целью пользователя) или Outcome (наблюдаемым результатом) (v0.4);
- услугой (service), provider или слотом (v0.4);
- каталожной выдачей или результатом поиска;
- сырым ответом LLM;
- текстовым сообщением;
- записью (appointment);
- рекламным размещением;
- аналитическим событием.

Recommendation имеет **контролируемое каноническое ядро** (v0.4, R-NBA-1):
AI может интерпретировать его и естественно формулировать представление
(§13, §34), но **не является decision authority** (факт — AYLA-DEC-0045 /
OD-9: LLM не является ranking authority).

Продуктово-семантический слой решения (Goal → Outcomes → Adaptive
Context → Context Sufficiency → Safety → Decision Policy → NBA) определён
в §27–§33; граница с исполнением (C04 = WHAT + WHY, C05 = HOW) — в §34.

## 3. Recommendation Record и RecommendationSet

Модель идентичности (**owner ruling OQ-R1 — ACCEPT, v0.3**; модель v0.2
по ревью P0-3 подтверждена; согласована с фактом [[Killer PRD]] §5.1:
каждая alternative имеет собственный `recommendation_id`):

- **Recommendation — immutable decision record** (не mutable aggregate);
- **RecommendationSet — immutable группирующая запись одной выдачи**
  (одного решения «что предложить сейчас»);
- **Каждый предложенный вариант — отдельная immutable Recommendation
  record** со своим `recommendation_id` (primary и каждая alternative);
- изменение decision subject (NBA), policy evaluation, evidence, consent
  evaluation, safety evaluation или decision semantics создаёт **новый
  `recommendation_id`** (v0.4: заменяет формулировку v0.3 «изменение
  candidate, ranking…» — candidate/ranking перенесены downstream, §8, §34);
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
  decision_subject:           # Canonical Next Best Action = WHAT (v0.4, §33; v0.6 · B2)
    family:                   # ADDRESS | SUPPORT | RECOVER | OBSERVE (candidate, §33); до пилота не заполняется — null (v0.5, §33)
    target:                   # целевой объект действия в терминах домена (= direction_code в Final Reconciliation §5)
                              # action_type из v0.4 перенесён в ExecutionOption (§34; v0.6 · A1 D-7)
    target_outcomes: []       # коды Outcomes, на которые направлен NBA (§28); не ссылки на DesiredOutcome (v0.5, AYLA-DEC-0094)
  result_status:              # RecommendationResult (v0.4, §32)
  readiness_state:            # тень DecisionReadiness (§30; v0.6 · A2, C1): READY | NEEDS_DISCRIMINATION | NEEDS_REQUIRED_CONTEXT | INSUFFICIENT_EVIDENCE | BLOCKED;
                              # не исход выбора следующего шага AYLA-DEC-0097 и не управляет показом
  reason_codes: []
  evidence_refs: []
  context_snapshot_ref:       # Decision Snapshot — один из трёх логических снимков (§7; v0.6 · B10)
  memory_snapshot_ref:        # immutable snapshot (§7); Phase 1 — null
  decision_policy_version:    # версия Recommendation Decision Policy (v0.4, §31)
  taxonomy_version:           # версия Goal/Outcome/NBA taxonomy (v0.4, §28, §33)
  safety_policy_version:      # v0.6 · A2 (канон v1.1 §7.2)
  catalog_mapping_version:    # v0.6 · A2 (канон v1.1 §14.6)
  presentation_policy_version:  # версия правил представления C04 (v0.4, §34)
  explanation:
  safety_evaluation:          # ref: {state, rule_id, policy_version, evidence_ref, activated_at} (§23; v0.6 · A2)
  consent_evaluation:
  created_at:
  actionable_until:           # v0.6 · A2 (B13): = 2 ч ConversationState / active recommendation context;
                              # прежнее имя expires_at (v0.4) снято, чтобы не читалось как срок жизни записи
  record_schema_version:      # версия схемы записи (v0.4; заменяет recommendation_version)
  presentation_version:       # версия представления; переформатирование без нового id
```

> **v0.5 (AYLA-DEC-0094).** `target_outcomes` остаются рабочими кодами
> Outcomes v0.4 (§28). Ссылками на записи `DesiredOutcome` они не
> являются: Desired Outcome в первом релизе не активируется, писателей
> `DesiredOutcome` / `PlanOutcomeLink` / `ProgressObservation` нет, и
> immutable-запись Recommendation не становится вторым носителем
> «желаемого результата». Поля исхода выбора следующего шага (AYLA-DEC-0097)
> в запись Recommendation не копируются — они живут в одной записи
> DecisionOutcome ([[Ayla Decision Policy Contract]]; §32).
>
> **v0.5 (CD §71 п.2).** До пилота `decision_subject.family` не
> заполняется — значение `null`; NBA-семейства включаются только после
> пилота (решение владельца 21.09, журнал главного окна CD §71 п.2, вне
> git; §33).

> **v0.6 · KB-F (PR #21 A2: B2, B13; Final Reconciliation §4 конфликт D).**
> Предмет записи — **NBA = WHAT** (B2: «Recommendation = WHAT.
> Service/master = downstream execution»). «Primary candidate» канона v1.1
> §10.1 читается как *execution candidate* внутри пространства вариантов
> исполнения, а не как предмет записи. Запись **immutable и переживает TTL
> контекста**: 2 ч — actionability (`actionable_until`), хранение — по
> отдельной retention policy (B13: иначе «через два часа нельзя доказать,
> какая Recommendation привела к Booking»). Retention — не поле записи;
> число лет открыто (Final Reconciliation §8 O2). `readiness_state` — тень
> DecisionReadiness (§30): пишется для замера порогов (C1) и ни на что не
> влияет. Минимум для пилота — Final Reconciliation §5 с поправками KB-F в
> его шапке (без `family` и без ссылок на `DesiredOutcome`).

Предмет решения (v0.4, R-NBA-2): `decision_subject` — Canonical NBA, а
не service/provider candidate. Поля v0.3 `candidate_id`, `rank`,
`candidate_set_ref`, `ranking_policy_version` **удалены из decision
record**: кандидаты, ранжирование и связь с выбранным execution option
(service, provider, slot) фиксируются downstream — в Execution Mapping /
Provider Ranking и Booking (§8, §34) — и не являются частью NBA-решения.
Attribution-связь сохраняется через `recommendation_id` (§18–§20).

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
  §22); в записи — только `created_at`, `actionable_until` (v0.6 · B13,
  прежнее `expires_at`), `supersedes_recommendation_id`;
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
- изменение primary NBA, decision policy evaluation или evidence — **новый
  `recommendation_id`**; новая запись содержит
  `supersedes_recommendation_id` (§21). Отдельного `decision_revision`
  в immutable-модели не существует (v0.2).

Так attribution остаётся однозначной.

## 5. Recommendation Pipeline

v0.4 (R-NBA-2/3/8): pipeline разделён **границей исполнения** на два
сегмента. Порядок начальных gates сохранён в точном соответствии
каноническому порядку [[Killer PRD]] §5.1: consent/privacy gate и safety
gate предшествуют любому выбору и не могут быть переопределены. Этапы
eligibility/availability, relevance, preference и economic-neutrality
Killer PRD §5.1 **перенесены без удаления** в execution segment
(Provider Ranking, §34): в v0.3 они применялись к service/provider
кандидатам внутри recommendation decision, что противоречит R-NBA-2/3 —
теперь те же правила действуют над execution options **после** выбора
NBA. Приведение текста Killer PRD §5 в соответствие с этим разделением —
отдельная правка Killer PRD (OQ-R12, §26); до неё этот контракт фиксирует
место применения правил.

> **v0.5 (AYLA-DEC-0096, AYLA-DEC-0087).** (1) **До этапа 1** каждое
> сообщение проходит ступень 1 входного пути — минимальный входной детектор
> опасности только по тексту текущего сообщения, без памяти и профиля;
> кризис и неотложка получают детерминированный ответ всегда, в том числе
> при согласии, не данном или отозванном, и при работе оператора
> ([[Ayla Decision Policy Contract]], «Состояния и переходы»). Этап 2 ниже —
> ступень 2 (согласия и разрешённый контекст); этап 9 — ступень 3,
> **расширенная safety с разрешённым контекстом**. Порядок «consent/privacy
> → safety» Killer PRD §5.1 относится к составлению рекомендации из
> персонального контекста и действует внутри ступеней 2–4 (Journey v1.3).
> (2) Этапы 3–4 — **Goal optional**: Goal 0..1, не синтезируется;
> **рекомендация не требует создания Goal**; Outcome Resolution не требует
> уже существующего Goal (AYLA-DEC-0087; §27–§28). Строки этапов 7–8
> таблицы не меняются; уточнения — в §30.

> **v0.6 · KB-F (PR #21 A1 + A2: B6, C2; WD §20 D-1, D-3, D-6, D-10).**
> Этапы 3–4 — **Semantic Resolution** с optional Goal: выход —
> `SemanticResolutionResult` (`goal?` 0..1, `outcomes[]` 0..N — рабочие
> коды §28, `resolution_status`), Goal не синтезируется; за ним — один
> вопрос семантического уточнения, если он нужен (§28). Для человека такой
> вопрос — исход `CLARIFY` [[Ayla Decision Policy Contract]] (один вопрос;
> AYLA-DEC-0097). Этап 9 несёт четыре состояния safety и правило B6 (§23);
> он остаётся ступенью 3 AYLA-DEC-0096 и «сквозным» не является. Этап 16 —
> допуск только `VERIFIED` (§8). **Не перенесено из PR #21:** замена
> этапов 7–8 на DecisionReadiness (до пилота DecisionReadiness только в
> тени и вопросов не задаёт — §30, AYLA-DEC-0097).

**Сегмент решения (Recommendation Engine — «что сделать»; C01–C04):**

| # | Этап | Вход | Выход |
|---|---|---|---|
| 1 | Intent Resolution (C02) | пользовательское сообщение + session context | `resolution_ref` (Intent Model output 0.5 — не меняется) |
| 2 | Authorization and Consent Gate | resolution + consent state | допуск/отказ (fail-closed, CSR §2) |
| 3 | Semantic Resolution (v0.5: Goal optional; v0.6 · A1) | resolution + user expression + разрешённый journey context | `SemanticResolutionResult`: `goal?` 0..1 с `source`/`confirmed` (не синтезируется, неизвестная связь — `not_established`), `outcomes[]` 0..N с `source`/`confirmed` — рабочие коды, `resolution_status` (§27–§28) |
| 4 | Adaptive Clarification семантики (C02, v0.6 · A1 D-6) | `resolution_status` | `SKIP / CONFIRM_ONE / CHOOSE_MANY / ASK_CONTEXT`; ≤1 вопрос за ход, для человека — исход `CLARIFY` (AYLA-DEC-0097); после ответа — re-resolution (§28) |
| 5 | Context Retrieval | допуск + purpose | `context_snapshot_ref` (immutable) |
| 6 | Memory Retrieval | purpose-limited request (AYLA-DEC-0024 п. 3) | `memory_snapshot_ref` (immutable) |
| 7 | Adaptive Clarification (C03) | missing/needs-confirmation факты, требуемые политикой | уточнённые context facts (§30) |
| 8 | Context Sufficiency Evaluation | RecommendationContext (§29) | sufficiency result (§30) |
| 9 | Safety Gate (v0.5: расширенная safety, ступень 3 AYLA-DEC-0096) | goal?, outcomes, context, safety_input | допуск / `SAFETY_BOUNDARY` (§23, §32); v0.6 · A2: состояние `NORMAL / CLARIFY / CAUTION / STOP` (+ `UNKNOWN`, `NOT_APPLICABLE`), правило B6 (§23) |
| 10 | Recommendation Decision Policy | всё выше | ranked suitable NBAs + reason codes (§31) |
| 11 | Recommendation Assembly | policy output | RecommendationSet: primary NBA + допустимые alternatives |
| 12 | Explanation Assembly (WHY) | decision + реально использованные facts/evidence | Explanation (§13) |
| 13 | Persistence | assembled records | сохранённые Recommendation records |
| 14 | Presentation (C04 = WHAT + WHY) | persisted records | доставка каналу (§16, §34) |

**--- граница исполнения (execution boundary) ---**

**Сегмент исполнения (downstream — «как» и «кто»; C05):**

| # | Этап | Вход | Выход |
|---|---|---|---|
| 15 | Execution Mapping (C05 = HOW) | принятый NBA (§17) | execution options (§34) |
| 16 | CanonicalService / TenantOffer eligibility (v0.6 · A2 C2) | execution option + tenant scope | только `approved`-канон и `mapping_status = VERIFIED`; иначе `NO_VERIFIED_CANDIDATES` (§8, §34) |
| 17 | Provider Ranking | eligible providers | ranked providers (правила Killer PRD §5.1 gates 3–6; §8, §34) |
| 18 | Booking | выбранный provider/slot | booking flow; ownership — Booking context (§22) |
| 19 | Attribution | действие пользователя / результат | qualified action / outcome link (§18–20; владелец — Attribution context, §15) |

Если техническая реализация потребует изменить порядок consent/safety
gates, это — отдельное архитектурное решение с изменением Killer PRD, а
не редакционная правка этого документа (правило v0.2 сохранено).

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

Приоритет источников внутри admissible set (зафиксирован для purpose
«recommendation»; глобального порядка источников Memory не существует —
приоритет определяется per-purpose policy, AYLA-DEC-0079):

```text
Current explicit user request
> Current session context
> Confirmed persistent memory
> Historical inferred signals (non-authoritative until confirmed)
```

**Memory может влиять только на:**

- context fit внутри Decision Policy (учёт подтверждённых ограничений и
  предпочтений; v0.4 — заменяет «candidate eligibility» v0.3);
- priority среди suitable NBA (preference weighting по типам фактов —
  Memory taxonomy, Journey v0.3; v0.4 — заменяет «ranking» v0.3);
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
- скрыто увеличивать коммерческую выгоду платформы (§11);
- создавать или переопределять eligibility/exclusion-правила Decision
  Policy, families или targets (v0.4, §31, §33).

Historical inferred signals не участвуют в decision как факт, пока не
прошли Memory Learning Loop (confirmation → whitelist check → persist,
AYLA-DEC-0023 п. 2).

## 7. Immutable Snapshots (context, memory)

> **v0.6 · KB-F (PR #21 A2: B10; Final Reconciliation §4 конфликт 4).**
> Снимков **три логических**, и они не смешиваются в одном объекте:
> **Decision Snapshot** (в Recommendation record — `context_snapshot_ref`,
> `memory_snapshot_ref`, версии политик), **Execution Mapping Snapshot**
> (в ExecutionOption: услуга, мастер, цена, длительность, `distance_meters`)
> и **Transaction Snapshot** (в PendingBookingIntent / Booking: слот,
> цена на момент подтверждения, exact client-confirmed execution option —
> D4). ADR-0013 «Recommendation Snapshot», строивший один снимок вокруг
> candidate-модели, — `superseded` этим разделом и §25 (B10: «смешивает
> decision, candidate/provider ranking и transaction state»). Правило ADR
> «UX рендерит из snapshot, не из live» сохраняется для каждого из трёх.

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

## 8. Candidate Model (execution domain — downstream of Recommendation)

v0.4 (R-NBA-2/8): модель кандидатов **перенесена на уровень исполнения**.
Candidate — это кандидат на **исполнение уже выбранного NBA** (service/
provider), а не предмет recommendation decision. Candidate Generation,
Relevance Scoring и Preference Ranking выполняются в Execution Mapping /
Provider Ranking (§34), после acceptance NBA, и не могут изменить primary
NBA (§11). Правила этого раздела сохранены из v0.3 без удаления и
действуют на execution-уровне.

Различаются: **Candidate → Eligible Candidate → Ranked Candidate →
Selected Execution Option**.

> **v0.6 · KB-F (PR #21 A2: C2; `docs/OPEN_DECISIONS.md` §76, §105;
> Final Reconciliation §2 слои 12–13, инвариант (г)).** Eligibility услуги
> для Recommendation — **только `mapping_status = VERIFIED`** у
> `approved`-канона; **второй ветки нет**, и «ноль VERIFIED» не разрешает
> откат на `REVIEW_REQUIRED` (§76). Пустой результат — штатное состояние
> с именем **`NO_VERIFIED_CANDIDATES`**, не поломка. Дословно C2: «VERIFIED
> → может участвовать в semantic Recommendation; не VERIFIED →
> Catalog/Search/direct booking при остальных gates возможны, Ayla
> Recommendation — нельзя». VERIFIED-канон + активный мастер + расписание
> доказывают *execution availability*, не *semantic suitability*. Ранжирование
> провайдеров — staged: hard eligibility → semantic fit → transaction fit
> → personalization → quality → tie-break (канон v1.1 Decision 6);
> экономика — вне ranking (§11).

```yaml
Candidate:                  # execution-level, не часть Recommendation record
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

Кандидат, отфильтрованный safety или eligibility gate, **не попадает** в
предлагаемые execution options (факт — Killer PRD §5.1: исключённый на
любом этапе не возвращается последующими; Fake Rescue запрещён). Если
подходящий NBA не имеет допустимых execution options, это — execution
feasibility outcome с честным раскрытием пользователю (§11, §34), а не
основание подменить NBA менее подходящим.

## 9. Primary Recommendation

Primary recommendation — не единственный допустимый вариант, а **лучший
NBA по действующей Recommendation Decision Policy** (§31; факт — Killer
PRD §5.1: primary одна). Одновременно доступна не более одной primary
(Killer PRD §5.1).

```yaml
primary_option:            # Recommendation record с recommendation_role: primary
  decision_subject:        # Canonical NBA (§33)
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

Альтернативы (alternative NBA) появляются только при условии (факт —
Killer PRD §5.1: не более двух; после отклонения primary фиксируется
`rerank_reason`, решение пересчитывается с уточнённым constraint):

- прямой запрос пользователя;
- отказ от primary;
- недостаточная evidence для одного сильного выбора;
- требование policy показать выбор.

Условия v0.3 «недоступность primary; несовпадение цены; несовпадение
времени; несовпадение мастера» **перенесены на execution-уровень** (v0.4,
R-NBA-3): недоступность или несовпадение по цене/времени/мастеру
порождают alternative **execution options** в C05 (§34), а не новые NBA
— сами по себе они не меняют того, что пользователю разумно сделать.

Каждая alternative — **отдельная Recommendation record** (§3):

```yaml
alternative:               # Recommendation record с recommendation_role: alternative
  recommendation_id:       # собственный (факт — Killer PRD §5.1)
  recommendation_set_id:   # общий с primary
  parent_recommendation_id:
  rerank_reason:
  decision_subject:        # альтернативный Canonical NBA (§33)
  alternative_reason:
  differs_from_primary_by: []
  evidence_refs: []
```

Альтернативы **не показываются** ради искусственного «ассортимента» и не
предлагаются как равноправный каталог по умолчанию (Killer PRD §5.1).

> **v0.6 · KB-F (PR #21 A2: B4; Final Reconciliation §4 конфликт B).**
> «Другой вариант» доступен всегда после primary; **список альтернатив
> (≤2, C04.3) не показывается автоматически — пользователь открывает его
> действием**. Запрос альтернативы создаёт новую Recommendation с
> `parent_recommendation_id` и `rerank_reason = ALTERNATIVE_REQUESTED`
> (канон v1.1 §10.2); `Что ещё?` — сигнал сессии, не долговременный
> dislike (§10.3).

## 11. Economic Neutrality

**Recommendation Suitability ≠ Execution Feasibility (v0.4, R-NBA-3).**
Пригодность NBA определяется **независимо от коммерческой и фактической
доступности исполнения**: цена, доступность provider, комиссия, маржа,
платный статус, свободные слоты и т. п. **не могут** сделать менее
подходящий NBA primary. Проверка и раскрытие execution availability
выполняются **после** recommendation decision — на этапах Execution
Mapping / Provider Ranking (§34). Если у подходящего NBA нет доступных
вариантов исполнения, это фиксируется как execution feasibility outcome с
честным раскрытием пользователю (§8, §34), а не как замена NBA.

Факт — Killer PRD §5.3 и Конституция: комиссия, маржа, расходы на
рекламу, тариф или коммерческий статус provider **не влияют** на organic
ranking, порядок кандидатов и выбор primary (на execution-уровне —
§34 — и тем более на выбор NBA).

Проверяемое правило (нормативное): commercial benefit to Ayla cannot be
a positive ranking feature unless the placement is explicitly disclosed
and excluded from organic recommendation ranking.

**Paid ranking — out of MVP scope.** Если paid placement появится
позднее, он отделяется от Recommendation Contract: рассчитывается
отдельно, явно маркируется и не заменяет organic primary (Killer PRD
§5.3). Обработка нарушений — quarantine ranking release и operational
handling contract (Killer PRD §5.3), здесь не пересматривается.

## 12. Evidence и Grounding

Каждая рекомендация имеет evidence. Виды evidence **decision-уровня**:
user-stated evidence; confirmed memory; policy result; safety constraint;
journey context. Виды evidence **execution-уровня** (provider data;
service data; availability data; price snapshot) относятся к execution
options и Provider Ranking (§34) и не являются основанием выбора NBA
(v0.4, R-NBA-3).

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

Explanation — **производная от реального recommendation decision**, а не
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

**WHY (v0.4):** объяснение использует **только** факты и reason codes,
реально повлиявшие на решение. `Context Fact ≠ Reason Code`: context
fact — вход политики; reason code — зафиксированная причина из Decision
Policy (§31); связывание факта с причиной допустимо, только если политика
действительно использовала этот факт. AI может **формулировать** WHY
естественным языком, но **не может изобретать причинные основания**,
которых не было в решении (факт — AYLA-DEC-0045 / OD-9).

**Displayable-правило (owner ruling 2026-07-29; перенесено из
[[Recommendation UX Addendum]] §2):** каждое объяснение классифицируется
как **displayable** (разрешено показать пользователю) или
**internal-only** (внутренние сигналы, персональные данные, раскрытие
ranking/policy internals — показ запрещён). Explanation может существовать
в системе, но быть internal-only. **«Нет displayable объяснения → не
показываем»**: если Recommendation не имеет displayable-объяснения
(включая redacted-вариант только по разрешённым фактам), рекомендация не
предъявляется пользователю, а сценарий переводится в состояние
no-recommendation. Владелец классификации displayable / internal-only —
открытый вопрос OQ-REC-6 (Recommendation UX Addendum §7).

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
expired       — истёк TTL/freshness (actionable_until — v0.6 · B13; §22)
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

> **v0.6 · KB-F (PR #21 A2: B8; канон v1.1 §17.3, §17.5; Final
> Reconciliation §4 конфликт 5).** Таксономия событий **одна** — product
> event backbone канона v1.1 §17.3; этот раздел остаётся publication matrix
> к ней. **`recommendation.accepted` не вводится** (B8: «ENGAGED доказывает
> взаимодействие, `booking_intent.created` — переход к исполнению; generic
> accepted интерпретируется сильнее доказанного»). `recommendation.declined`
> как отдельное событие снято: явный отказ — reaction `REJECTED` (канон
> v1.1 §10.3), фиксируется interaction-слоем. `presented` = transport ack
> (OQ-R3, §16). `qualified_action.attributed` — только по provenance chain
> `Recommendation → PendingBookingIntent → Booking` (§18; канон v1.1
> §17.6): без provenance атрибуции нет. Инвариант: `shown ≠ engaged ≠
> booked ≠ completed ≠ liked`. Записи событий —
> [[Ayla Domain Event Registry]] v0.7 (`proposed` / `deprecated`, KB-F).

| Event | Semantic class | Authoritative owner | Publication scope |
|---|---|---|---|
| `recommendation.created` | domain + integration | Recommendation | cross_context |
| `recommendation.superseded` | domain + integration | Recommendation | cross_context |
| `recommendation.expired` | domain | Recommendation | internal |
| `recommendation.invalidated` | domain + integration | Recommendation | cross_context |
| `recommendation.presented` | interaction + integration | Channel Delivery / Interaction | cross_context |
| `recommendation.explanation_requested` (v0.6 · B8) | interaction | Channel Delivery / Interaction | cross_context |
| `recommendation.alternative_requested` (v0.6 · B8) | interaction | Channel Delivery / Interaction | cross_context |
| `recommendation.engaged` (v0.6 · B8; = `Посмотреть варианты`, не acceptance) | interaction + integration | Channel Delivery / Interaction | cross_context |
| `booking_intent.created` (v0.6 · B8; переход к исполнению, несёт `recommendation_id`) | domain + integration | Booking / Handoff | cross_context |
| `qualified_action.attributed` | attribution + integration | Attribution / Measurement | cross_context |
| ~~`recommendation.accepted`~~, ~~`recommendation.declined`~~ | — | сняты v0.6 (B8) | — |

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
  использования обеспечивается `actionable_until` (v0.6 · B13) и read/action gate (§22);
  integration consumers не должны зависеть от гарантированной доставки
  expiry event. Событие используется для projection, cleanup, analytics,
  observability.
- **`recommendation.invalidated`** — cross_context: downstream обязан
  прекратить действие по рекомендации при consent revocation, safety
  policy change, provider removal, policy prohibition; action gate всё
  равно остаётся обязательным (в v0.2 был candidate — подтверждён
  ruling R2/R10).
- **Interaction events** (`presented`, `explanation_requested`,
  `alternative_requested`, `engaged`; v0.6 · B8):
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

> **v0.6 · KB-F (PR #21 A2: B8, D4; канон v1.1 §10.3, Decision 13).**
> Событие `recommendation.accepted` и поле `acceptance_action` **сняты**
> (B8). Вместо generic acceptance — реакции канона v1.1 §10.3:
> `WHY_REQUESTED / ALTERNATIVE_REQUESTED / ENGAGED / REJECTED /
> CONSTRAINT_ADDED`; `Посмотреть варианты` = `ENGAGED`, **не доказанное
> принятие**. Переход к исполнению доказывается только
> `booking_intent.created` → `PendingBookingIntent(recommendation_id,
> execution_option)`, где **фиксируется именно та execution option,
> которую клиент видел и подтвердил (D4)**. Acceptance ≠ Booking
> сохраняется (BOT-003 §13). Текст v0.4 ниже — история определения;
> действующее правило — этот блок.

- ~~`recommendation.accepted`~~ (v0.4) — **пользователь явно выбрал конкретный
  recommendation option (NBA) как следующий вариант действия** (строгое
  определение, v0.2). Конкретное действие фиксируется отдельно:

```yaml
acceptance_action: select | proceed_to_booking | request_booking   # снято v0.6 (B8)
```

  Acceptance NBA открывает execution segment (C05, §34): выбор execution
  option (услуга, мастер, слот) фиксируется downstream событиями booking
  progression (§18), а не изменением Recommendation record. Открытие
  booking flow и подтверждение записи — **разные** уровни намерения и не
  считаются одинаковым acceptance. Acceptance **не означает** завершённую
  запись (appointment completion).
- ~~`recommendation.declined`~~ (v0.4) — **только явный отказ**. Бездействие не
  равно decline. v0.6: явный отказ = reaction `REJECTED`; бездействие
  по-прежнему ничем не является (B8).
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

Причины supersession: `user_context_changed`, `goal_changed`,
`outcomes_changed`, `user_declined`, `safety_constraint_changed`,
`consent_changed`, `memory_changed`, `explicit_refresh`.

Причины v0.3 `availability_changed` и `price_changed` **перенесены на
execution-уровень** (v0.4, R-NBA-3): изменение доступности или цены не
отменяет NBA — оно пересчитывает execution options в C05 (§34). NBA
пересматривается, только если изменился сам контекст цели/пользователя.

Изменение consent или memory **не меняет задним числом** старую
recommendation, но может сделать её непригодной для дальнейшего действия
— состояние `invalidated` (§14, §24), отличное от `expired`.

## 22. Expiry

> **v0.6 · KB-F (PR #21 A2: B13, D4; канон v1.1 §4, §16.8–§16.9; Final
> Reconciliation §4 конфликт E).** `expires_at` → **`actionable_until`**:
> это TTL *actionability* (= 2 ч ConversationState / active recommendation
> context, канон v1.1 Decision 1), **не срок жизни записи** — immutable
> Recommendation record хранится для attribution/audit по отдельной
> retention policy (B13). Через два часа контекст не продолжается
> напрямую, но `recommendation_id` и цепочка `Recommendation →
> PendingBookingIntent → Booking` остаются доказуемыми.
>
> **Инвариант D4 (revalidation):** авторитетна **конкретная execution
> option, которую видел и подтвердил клиент**. Booking обязан
> snapshot/revalidate **именно её**; любое расхождение (показано 60 мин /
> 1500 ₽, применилось бы 45 мин / другая цена) = **`MATERIAL_CHANGE`** →
> показать пользователю → **новое подтверждение**. Не silent normalization
> и не «ребро всегда главнее». Результат валидации BookingIntent — `VALID /
> NEEDS_RESOLUTION / MATERIAL_CHANGE / BLOCKED` (канон v1.1 §16.9), отличен
> от DecisionReadiness и от исходов AYLA-DEC-0097. **Реестр кодов:**
> `MATERIAL_CHANGE` — зонтичное понятие контракта; в каталоге ему
> соответствуют `409 QUOTE_CHANGED` (`details.field ∈ {price,
> duration_minutes}`, `quoted`, `applied`) и `409 SLOT_UNAVAILABLE`; коды
> каталога не переименовываются (Final Reconciliation §4).

Recommendation имеет TTL или условия истечения: journey завершён;
пользователь изменил intent или goal; контекст, на котором основан NBA,
устарел или перестал быть допустимым. Устаревание availability или price
snapshot — условие пересчёта **execution options** (§34), а не expiry NBA
(v0.4, R-NBA-3).

Отдельно от expiry (v0.2): **invalidation** — запрет дальнейшего
использования по policy/action gate: consent отозван; safety policy
изменилась; provider removed. Expiry — про freshness; invalidation — про
допустимость.

Инвариант (нормативный): **отсутствие события `recommendation.expired`
не разрешает использовать рекомендацию после `actionable_until`** (v0.6 ·
B13; в v0.4 — `expires_at`) — read/action
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

**Safety — это gate, а не Recommendation family (v0.4, R-NBA-5).**
`SAFETY_BOUNDARY` допустим как `RecommendationResult` (§32), но **не
является CanonicalRecommendation**: запись со статусом `SAFETY_BOUNDARY`
не содержит NBA и не может быть primary или alternative.

> **v0.6 · KB-F (PR #21 A2: B6, C3; канон v1.1 Decision 4 §7.1; Final
> Reconciliation §2 слой 6).** Состояние расширенной safety (ступень 3
> AYLA-DEC-0096, этап 9 §5) — **четыре состояния** `NORMAL / CLARIFY /
> CAUTION / STOP` (канон v1.1 §7.1) плюс `UNKNOWN` (fail-closed: до оценки
> считается как STOP) и `NOT_APPLICABLE` (правило не применимо к
> кандидату). Каждая оценка несёт `rule_id`, `policy_version`,
> `evidence_ref`, `activated_at` и allowed/forbidden capabilities. **До
> утверждённой safety-signal matrix (C3) действует B6:** потенциально
> медицинский смысл (боль, отёки, хроническая усталость) **fail-closes
> затронутую capability в `CLARIFY`** — задаётся один decision-changing
> safety-вопрос (для человека — исход `CLARIFY` AYLA-DEC-0097); до ответа
> semantic Recommendation не формируется. `STOP` — исход `BLOCKED` или
> `HANDOFF` AYLA-DEC-0097. Кризис и неотложка по-прежнему обрабатываются
> раньше — ступенью 1 (детерминированный ответ всегда). Матрица — открытый
> вход контракта (`RequiredContextSpec` для `owner = SAFETY`); её
> отсутствие блокирует выход slice к пользователям, но не канонизацию.
> Кроме ступеней 1 и 3 входного пути действует **service-level health gate
> на записи** (`requires_health_check ∈ {True, UNKNOWN}` → `HEALTH_CHECK_*`,
> не `BOOKING_ERROR`; `docs/OPEN_DECISIONS.md` §98): кандидат с таким
> флагом может быть рекомендован как направление, исполнение уходит к
> человеку, и это честно раскрывается в WHY/C05. Значение `UNKNOWN`
> safety и исход `UNKNOWN` аллергического фильтра (ниже) — разные понятия.
> **Не перенесено из PR #21:** «Safety Gate сквозной» и «safety-гейтов
> два» — противоречат порядку четырёх ступеней AYLA-DEC-0096.

Контракт ссылается на safety policy, а не определяет медицинскую логику
заново (MVP Safety Policy — planned, Roadmap §7.3; границы — Killer PRD
§4.1 OD-K6, §8–9). Минимальные правила:

- forbidden NBA не ранжируется; forbidden execution candidate не
  предлагается (§8, §34);
- health inference не создаётся из food/beauty сигналов (Killer PRD
  OD-K6);
- user-stated contraindication учитывается как ограничение (user-stated
  safety constraints — AYLA-DEC-0023 п. 3);
- отсутствие safety data не превращается в подтверждение безопасности;
- recommendation не заменяет медицинскую консультацию;
- unsafe recommendation не может быть сохранена как primary;
- при safety block — S8 Boundary Handling (полная UJS; Journey v0.3, N8).

> **v0.5 (AYLA-DEC-0096).** Safety Gate этого контракта — ступень 3
> входного пути (расширенная safety с разрешённым контекстом). Ступень 1 —
> минимальный входной детектор по тексту сообщения — работает раньше
> любого этапа §5 и не зависит от согласия (§5, [[Ayla Decision Policy Contract]]).

**Аллергический фильтр состава (v0.5, AYLA-DEC-0100).** Отдельный от
safety state жёсткий фильтр для **всех** кандидатов, у которых есть
состав (позиции, продукты, средства), — **в том числе с неизвестным или
неполным составом: для них исход `UNKNOWN`**. Кандидат не выпадает из-под
фильтра из-за того, что его состав неизвестен (AYLA-DEC-0100: «при
неизвестном или неполном составе результат фильтра — “неизвестно”, а не
“безопасно”»; CSR §5.9). Нормы (источник — [[Consent Scope Registry]]
§5.9, `03 AI System/Contracts/allergy-filter-result.schema.json`):

- исход фильтра — ровно один из `CONFLICT` / `NO_CONFLICT_FOUND` /
  `UNKNOWN`; значения «безопасно» нет;
- `CONFLICT` — позиция исключается из выдачи;
- `UNKNOWN` (состав неизвестен или неполон, распознавание неуверенно) —
  **не «безопасно»**: позиция не показывается как подходящая по аллергии;
  это не STOP и не состояние safety — `UNKNOWN` фильтра и любое
  одноимённое значение safety разные понятия;
- `NO_CONFLICT_FOUND` — не утверждение о безопасности; никаких гарантий по
  одному отсутствию найденного аллергена;
- для обработки аллергии читают только этот фильтр (читатель
  `recommendations`) и сканер; кроме того — доступ самого человека к своей
  записи (показ, экспорт, удаление; CSR §5.9);
  **в текст для модели, включая WHY (§13), аллергии не попадают**; каждый
  доступ и отказ журналируются (`memory.allergy.accessed` /
  `memory.allergy.access_denied`, [[Ayla Domain Event Registry]] §6.4);
- запись аллергий активируется только по условиям
  [[Ayla Memory Domain Contract]] §12.1; пока записи нет, фильтр ничего не
  исключает и ничего не утверждает.

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
decision_policy_version:      # Recommendation Decision Policy (§31)
taxonomy_version:             # Goal/Outcome/NBA taxonomy (§28, §33)
memory_snapshot_ref:          # immutable (§7)
context_snapshot_ref:         # immutable (§7)
safety_policy_version:
consent_policy_version:
```

Replay execution-уровня (provider ranking, availability) — зона
ответственности Execution Mapping / Provider Ranking и Booking (§34) и
не входит в replay-контракт NBA-решения (v0.4).

> **v0.6 · KB-F (PR #21 A2: B10).** Replay NBA-решения воспроизводится из
> Decision Snapshot (этот раздел + §7); Execution Mapping Snapshot и
> Transaction Snapshot воспроизводят свои слои отдельно (§7). ADR-0013 §5
> Open Questions 1–5 перенесены сюда как открытые входы (без ответа):
> (1) кто создаёт и хранит snapshot — bot-platform или backend (split
> ADR-0009); (2) persistence/TTL snapshot и privacy (session-only норма
> UX-OD-003) — теперь читается через B13 (retention — отдельная политика);
> (3) связь snapshot с событиями `recommendation.created` / `.presented`;
> (4) versioning policy полей `*_version` и что считается bump-ом;
> (5) граница «новый snapshot» при повторном рендере и у alternative
> (`parent_recommendation_id`).

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
- **OQ-R9 — OPEN (пакет D, владелец Privacy/Legal).** v0.6 · B13:
  retention immutable Recommendation record — отдельная политика, не поле
  записи и не 2-часовой TTL контекста; число лет — открыто (Final
  Reconciliation §8 O2). Privacy export
  minimum зафиксирован (§3); открыты для Privacy/Legal: retention
  period; deletion vs legal hold; интерпретация derived data; являются
  ли digests personal data; export format; обработка immutable audit
  records; эффект удаления аккаунта; cross-repository deletion
  (совместно с AMD-001 C5 export/forget). OQ-R9 **не блокирует**
  регистрацию базовых recommendation events — privacy-minimum записи
  сохранён (§3), события не содержат чувствительных значений.
- **OQ-R11 — OPEN (v0.4, пакет A).** Семейства NBA `ADDRESS | SUPPORT |
  RECOVER | OBSERVE` и состав `target`/`action_type` — **кандидаты**, не
  финальный канон: подлежат валидации против полной MVP Goal/Outcome
  таксономии (§28, §33). Реестр кодов Goal/Outcome как канон пока не
  существует (Goal и Outcome определены в [[Ayla Glossary]]); рабочие коды
  версионируются через `taxonomy_version` (§3) и не претендуют на канон до
  валидации. **v0.5:** семейства `ADDRESS / SUPPORT / RECOVER / OBSERVE`
  **до пилота не включаются** — решение владельца 21.09 (журнал главного
  окна CD §71 п.2, вне git; бриф N-2: «Сложный NBA (скоринг, обучение,
  семейства) — после пилота»). Вопрос о составе семейств остаётся открытым
  на после пилота.
- **OQ-R13 — OPEN (v0.5).** Соответствие `RecommendationResult` (§32) и
  `decision_outcome` [[Ayla Decision Policy Contract]] (DP ОВ-15). В §32
  дана предлагаемая таблица; подтверждает владелец.
- **OQ-R12 — OPEN (v0.4, пакет A).** Приведение Killer PRD §5 в
  соответствие с разделением NBA / Execution / Provider Ranking: Killer
  PRD §5.1–5.2 описывает candidate-centric pipeline над service/provider
  кандидатами; этот контракт (v0.4, R-NBA-2/3/8) переносит правила gates
  3–6 Killer PRD §5.1 на уровень Provider Ranking (§34) без их удаления.
  Правка Killer PRD — отдельный шаг; связанный открытый вопрос о
  нормативном статусе Killer PRD — OD-AUDIT-003 (KB-аудит 2026-08-19). До
  правки Killer PRD место применения его правил фиксируется этим
  контрактом (§5, §34).

## 27. Goal Resolution (v0.4)

> **v0.5 (AYLA-DEC-0087; перенесено из ayla-knowledge PR #21, A1).** Goal
> в Recommendation — **0..1, optional**: рекомендация не требует создания
> Goal. Goal **не синтезируется**: если связь неизвестна — `not_established`.
> Этап 3 §5 «Goal Resolution» обязательным шагом не является: без Goal
> конвейер продолжается. Явный путь «Создать цель» остаётся **отдельным**
> действием пользователя вне рекомендательного конвейера (цель становится
> `ACTIVE` только после явного действия; меняется только явным действием —
> [[Ayla Goal and Desired Outcome Contract]], «Состояния и переходы»,
> таблица переходов). Источники и правило «неподтверждённый inference — не
> user-stated факт» ниже сохраняются.

Goal — желаемый результат на уровне изменения состояния пользователя
([[Ayla Glossary]]); Goal не является услугой или действием. Goal
появляется из следующих источников:

- **явный выбор пользователя (C01)** — выбор цели/сценария на входе
  (соответствует этапам 1–3 [[Ayla MVP User Journey Specification]]);
- **естественный язык** — через Intent Resolution
  ([[Ayla Intent Model Specification]]);
- **подтверждённый inference** — при средней уверенности допустимо
  продолжать с подтверждающей формулировкой; подтверждение пользователя
  обязательно перед side-effect execution (Intent Model, §Confidence and
  Clarification);
- **разрешённый активный journey context** — текущий допустимый контекст
  journey.

Нормативно:

- **неподтверждённый inference не является user-stated фактом**: goal с
  `source: inferred` и `confirmed: false` не используется Decision Policy
  как явная цель пользователя;
- если связь intent ↔ Transformation Goal неизвестна, она **не
  выдумывается** и остаётся `unknown/not_established` (Intent Model,
  §Transformation Goal and Intent; OD-7);
- каждый goal фиксируется с `source` и `confirmed` (§29);
- там, где требуется, clarification/confirmation представлены явно — через
  C03 (§30), а не скрытым допущением.

## 28. Outcome Resolution (v0.4)

> **v0.5 (AYLA-DEC-0087, AYLA-DEC-0094; перенесено из PR #21 A1 с
> изменением).** Outcome Resolution **не требует уже существующего Goal**:
> выход этапов 3–4 §5 — goal 0..1 и outcomes 0..N (рабочие коды ниже).
> **Не переносится из PR #21:** условие готовности «`READY_FOR_DECISION ⇒
> desired_outcomes ≥ 1`» и термин `DesiredOutcome` для этих кодов
> (отброшено, AYLA-DEC-0094); `SemanticResolutionResult`,
> `resolution_status` и режимы семантического уточнения `SKIP /
> CONFIRM_ONE / CHOOSE_MANY / ASK_CONTEXT` (WD D-6 / D-10) — для фиксации
> K-1 не нужны (Goal optional выражен без них) и уходят в отдельный PR
> (CD §71 п.1; KB-F, DRF-2270).
> Desired Outcome в первом релизе не активируется (AYLA-DEC-0094):
> писателей `DesiredOutcome` / `PlanOutcomeLink` / `ProgressObservation`
> нет, новый источник истины «желаемого результата» не создаётся, и
> готовность рекомендации на эту сущность не опирается.

> **v0.6 · KB-F (PR #21 A1: WD §20 D-3, D-6, D-10; WD §11.2 OD-SR-1…6).**
> Вводится upstream-объект **`SemanticResolutionResult`**: `goal?` (0..1),
> `outcomes[]` (0..N — рабочие коды этого раздела), `resolution_status ∈
> {RESOLVED, NEEDS_CONFIRMATION, AMBIGUOUS, INSUFFICIENT}`. Маппинг на
> семантическое уточнение: `RESOLVED → SKIP`, `NEEDS_CONFIRMATION →
> CONFIRM_ONE`, `AMBIGUOUS → CHOOSE_MANY` (когда интерпретации
> совместимы), `INSUFFICIENT → ASK_CONTEXT`; ≤1 вопрос за ход, для
> человека — исход `CLARIFY` AYLA-DEC-0097; после ответа — re-resolution.
> В объект **не входят** family, action, service, provider, price,
> availability, ranking, reason codes, execution route (OD-SR-6).
> `RecommendationSet` несёт `semantic_resolution_ref`. **Не перенесено из
> PR #21:** поле `desired_outcomes[]` и термин `DesiredOutcome` (здесь —
> `outcomes[]`), `semantic_readiness` с условием `READY_FOR_DECISION ⇒ ≥ 1
> desired outcome` — AYLA-DEC-0094.

Outcome — наблюдаемое изменение или завершение сценария после действия
([[Ayla Glossary]]).

- К Goal относится **1..N Outcomes** — желаемые наблюдаемые результаты,
  на которые направлен запрос. *v0.5: 0..N, и Outcomes существуют без
  Goal.*
- Источники Outcomes: явная таксономия / multi-select; естественный язык;
  подтверждённая интерпретация. Каждый outcome фиксируется с `source` и
  `confirmed` (§29); неподтверждённая интерпретация не является user-stated
  фактом (§27).
- **Несколько Outcomes остаются одним запросом / одним journey**, если
  иное не установлено другим каноническим правилом.
- Реестр кодов Goal/Outcome как канон пока не существует; `goal.code` и
  `outcome.code` ссылаются на версионированную Goal/Outcome taxonomy
  (`taxonomy_version`, §3), подлежащую валидации (OQ-R11). До появления
  реестра используются стабильные строковые коды рабочей таксономии, не
  претендующие на статус канона.

## 29. Recommendation Context (v0.4)

Структурированный вход Recommendation Decision Policy (§31):

> **v0.5 (AYLA-DEC-0087; перенесено из PR #21, A1).** `goal` —
> **optional**; отсутствие Goal само по себе **не** `INSUFFICIENT_CONTEXT`.
> Goal уточняется, только если конкретное правило Decision Policy требует
> его для текущего решения.

```yaml
RecommendationContext:
  intent:                   # resolution_ref — выход Intent Model
  semantic_resolution_ref:  # SemanticResolutionResult (§28; v0.6 · A1)
  goal:                     # optional, 0..1 (v0.5, AYLA-DEC-0087)
    code:                   # код Goal taxonomy (§28)
    source:                 # user_selected | user_stated |
                            # confirmed_inference | journey_context
    confirmed: true | false
  outcomes:
    - code:
      source:
      confirmed:
  context_facts:
    - fact_code:
      value:
      source:               # user_selected | user_stated | confirmed |
                            # memory | inferred
      freshness:            # fresh | stale_marked | unknown (§12)
      consent_scope:        # scope_id из [[Consent Scope Registry]]
  journey_context:          # разрешённый активный journey/stage context
  safety_input:             # user-stated ограничения и safety-сигналы (§23)
```

Нормативно:

- различие источников обязательно: user-selected / user-stated / confirmed
  отделены от memory и inferred; inferred не приравнивается к user-stated
  факту;
- факты из memory подчиняются relevance, freshness, consent и safety
  (§6, §24; AYLA-DEC-0024; reconfirmation как usage/freshness gate —
  AYLA-DEC-0073);
- чувствительные значения в Recommendation record не копируются — только
  snapshot refs и digests (§3, §7).

## 30. Context Sufficiency и адаптивная Clarification (C03) (v0.4)

> **v0.5 (AYLA-DEC-0087, AYLA-DEC-0097; перенесено из PR #21 с
> изменением).** Анкета `area → feeling → goal` **не является обязательным
> входом** рекомендации. Отсутствие цели не делает контекст
> недостаточным (§29). Если конкретный ответ человека способен продолжить
> сценарий, исход выбора — `CLARIFY` с одним вопросом; недостаточность
> данных не приравнивается к `NO_ACTION` (AYLA-DEC-0097). Теневые модули
> DecisionReadiness (`decision_readiness/`) и `decision-policy-v1-shadow`
> (`decision_policy.py`; оба — за флагом `DRE_SHADOW_ENABLED`,
> [[Ayla Decision Policy Contract]] R-7, R-8) относятся к порогам
> готовности и recommendation pass и **не являются** выбором следующего
> шага AYLA-DEC-0097 — тот строится отдельным
> детерминированным модулем ([[Ayla Decision Policy Contract]]). Замена
> этого раздела на DecisionReadiness (PR #21, A2) в v0.5 не переносится.

> **v0.6 · KB-F (PR #21 A2 + A1: C1; канон v1.1 Decision 5 §8; WD §20
> D-5, D-10).** DecisionReadiness — детерминированная оценка, достаточно
> ли подтверждённых данных для следующего решения; LLM self-confidence
> механизмом решения не является. **До пилота — только тень (C1):**
> считает и пишет `readiness_state` (§3) для замера порогов, человеку
> вопросов не задаёт и ход разговора не выбирает; что Ayla делает дальше —
> исход AYLA-DEC-0097 ([[Ayla Decision Policy Contract]]). Состояния тени
> (канон v1.1 §8, по смыслу):
>
> ```text
> READY                    → рекомендовать было бы можно
> NEEDS_DISCRIMINATION     → был бы нужен один различающий вопрос
> NEEDS_REQUIRED_CONTEXT   → был бы нужен обязательный вопрос
> INSUFFICIENT_EVIDENCE    → был бы нужен самый широкий полезный вопрос
> BLOCKED                  → рекомендация запрещена политикой
> ```
>
> `BLOCKED` тени и исход `BLOCKED` AYLA-DEC-0097 — разные поля. **Две оси
> достаточности** (D-10, OD-SR-6): семантическая (§28) и решения (здесь);
> пробел в RecommendationContext не переводит `RESOLVED` семантику в
> `INSUFFICIENT`. **Не перенесено из PR #21:** «C03 = адаптивный
> DecisionReadiness flow» — до пилота вопрос человеку выбирает только
> минимальный детерминированный выбор (AYLA-DEC-0097).

Decision Policy (§31) объявляет **required context facts** для каждого
`(family, target, action_type)`. Состояние каждого требуемого факта:
`known | missing | needs_confirmation`.

Нормативно (R-NBA-7):

- sufficiency оценивается **до** выбора NBA и **переоценивается после
  каждого релевантного ответа** пользователя;
- **C03 — адаптивная clarification**: вопросы порождаются из missing /
  needs_confirmation фактов, требуемых политикой, а не из фиксированной
  анкеты (факт — Journey v0.3, этап 5: минимально необходимый вопрос, не
  более 5 вопросов за сессию Discovery; Intent Model: не более 2
  clarification approaches на intent, затем `unresolved`);
- если контекст уже достаточен, **C03 пропускается**;
- различаются исходы:
  - `INSUFFICIENT_CONTEXT` — нужный факт разумно может быть получен
    сейчас → C03;
  - `OBSERVE` — информация в настоящий момент не существует или
    дальнейшие вопросы бесполезны → OBSERVE является **валидным NBA**
    (§33), а не дефектом контекста;
- владение conversation-уровнем sufficiency-диалога — за
  [[BOT-003 Discovery and Recommendation Conversation Specification]]
  (recommendation sufficiency); этот контракт владеет доменной моделью
  результата.

## 31. Recommendation Decision Policy (v0.4)

Recommendation Decision Policy — контролируемый набор правил выбора NBA.
Правила покрывают **как минимум** (R-NBA-6):

- **eligibility** — допустимость NBA в текущем admissible set (§6, §23,
  §24);
- **context fit** — соответствие NBA goal, outcomes и context facts (§29);
- **exclusion** — запрещающие правила (safety, consent, policy);
- **priority** — порядок среди suitable NBA;
- **sufficiency** — достаточность контекста для ответственного выбора
  (§30).

Нормативно:

- **LLM не может** самостоятельно создавать или переопределять families,
  targets, eligibility, exclusions, safety, выбор primary или reason codes
  (факт — AYLA-DEC-0045 / OD-9: LLM не является ranking authority);
- выход политики — ranked suitable NBAs + reason codes + фактически
  использованные факты (вход WHY, §13);
- версия политики фиксируется в записи (`decision_policy_version`, §3);
- economic neutrality (§11) и safety (§23) — внешние ограничения и не
  переопределяются правилами priority;
- provider-ranking семантика не входит в Decision Policy (R-NBA-8, §34);
- *v0.5 (AYLA-DEC-0087; перенесено из PR #21, A1):* Goal — controlled
  priority/alignment, **не override** safety, eligibility, exclusions,
  consent, evidence, context fit.

## 32. RecommendationResult (v0.4)

Исход recommendation pass:

```yaml
status:
  CLEAR_PRIMARY          # один primary NBA
  MULTIPLE_SUITABLE      # несколько равноподходящих NBA: primary по policy
                         # + допустимые alternatives (§9, §10)
  INSUFFICIENT_CONTEXT   # нужны obtainable факты → C03 (§30)
  SAFETY_BOUNDARY        # сработал safety gate; не является NBA (§23)
```

Дополнительно:

- `no_action` («ничего не делать») — валидный объяснимый результат
  (факт — AYLA-DEC-0045 / OD-9; MVP Scope and Release Contract);
  представляется как NBA; размещение в таксономии — при валидации
  (OQ-R11);
- runtime-код для `SAFETY_BOUNDARY` — `SAFETY_BLOCKED` (Journey v0.3,
  этап 7; [[Recommendation UX Addendum]] §5) — эквивалентное каноническое
  имя, дубликат не вводится;
- `NO_CANDIDATES` остаётся **execution-stage** исходом (нет допустимых
  execution options, §8, §34) и здесь не дублируется.

> **v0.5 (AYLA-DEC-0097; бриф Итог 3 п.14: «`no_action` и поля исхода по
> N-2»).** Исход выбора следующего шага — закрытый набор `ACT / CLARIFY /
> NO_ACTION / BLOCKED / HANDOFF` из [[Ayla Decision Policy Contract]];
> каждый исход несёт исход, причину (`reason_code`), ссылки на факты
> (`evidence_refs`), происхождение (`provenance`), заблокированные функции
> (`blocked_capabilities`), время расчёта (`calculated_at`) и версию
> политики (`policy_version`) — по `03 AI System/Contracts/decision-outcome.schema.json`.
> Эти поля хранятся в одной записи DecisionOutcome и в Recommendation не
> дублируются. Recommendation pass этого контракта — поставщик кандидата
> для исхода, а не второй набор исходов.
>
> **Имена не совпадают по смыслу.** `no_action` этого раздела — NBA
> «ничего не делать» (v0.4). `NO_ACTION` Decision Policy — исход «полезного
> действия или вопроса сейчас нет»; недостаточность данных им не является.
> Пока NBA-семейства до пилота не включены (§33), `no_action` как NBA не
> формируется; ситуация «нечего предложить» выражается исходом `NO_ACTION`
> (`reason_code` `nothing_useful`): требование AYLA-DEC-0045 / OD-9
> «обоснованное ничего не делать» до пилота выполняет исход `NO_ACTION`
> (AYLA-DEC-0097, DP-10).
>
> **Предлагаемое соответствие (OQ-R13, подтверждает владелец):**
>
> | `RecommendationResult` | `decision_outcome` |
> |---|---|
> | `CLEAR_PRIMARY`, `MULTIPLE_SUITABLE` | `ACT` |
> | `INSUFFICIENT_CONTEXT` | `CLARIFY`, если конкретный ответ человека продолжит сценарий; иначе `NO_ACTION` или `BLOCKED` с причиной |
> | `SAFETY_BOUNDARY` | `BLOCKED` (`safety_block`); `HANDOFF`, если нужен оператор (`safety_handoff`) |

## 33. NBA Taxonomy (v0.4, candidate)

NBA задаётся **композиционно**: `family + target + action_type`, а не
плоским списком (R-NBA-4).

Начальные candidate families:

| Family | Смысл |
|---|---|
| `ADDRESS` | действие, направленное на изменение состояния по цели |
| `SUPPORT` | поддерживающее действие (сопровождение, поддержание) |
| `RECOVER` | восстановление после регресса/срыва |
| `OBSERVE` | наблюдение/выжидание без немедленного действия |

Статус (нормативный): семейства — **кандидаты, не финальный канон** до
валидации против полной MVP Goal/Outcome таксономии (OQ-R11). LLM не
может вводить новые families или targets (§31). `SAFETY_BOUNDARY` не
является family (§23).

> **v0.5.** Семейства `ADDRESS / SUPPORT / RECOVER / OBSERVE` **до пилота
> не включаются** — ни как вход выбора следующего шага, ни как метка
> записи: до пилота `decision_subject.family` не заполняется (`null`, §3);
> NBA-семейства — после пилота (решение владельца 21.09, журнал главного
> окна CD §71 п.2, вне git). Сложный NBA, скоринг и обучение — после
> пилота (AYLA-DEC-0097). Формулировка PR #21 «provisional для Controlled
> Pilot» не переносится.

> **v0.6 · KB-F (PR #21 A1: WD §20 D-7).** `action_type` — маршрут
> исполнения и **перенесён в ExecutionOption** (§34): композиция NBA в
> записи — `family + target + target_outcomes` (§3), где `family` до пилота
> `null` (блок v0.5 выше). *v0.4: `family + target + action_type`.*
> **Не перенесено из PR #21:** семейства «provisional для Controlled
> Pilot» (B9) — CD §71 п.2.

## 34. Граница C04/C05 и Execution Mapping (v0.4)

Нормативно:

- **C04 = WHAT + WHY** — представление Canonical NBA и его объяснения
  (§13, §16). AI presentation интерпретирует и формулирует ядро
  естественным языком, не изменяя решение (R-NBA-1).
- **C05 = HOW** — после acceptance NBA (§17) Execution Mapping отображает
  NBA в конкретные execution options.

> **v0.6 · KB-F (PR #21 A1 + A2: B2, B3, B4, C2; WD §20 D-6, D-7).**
> Тройное разделение: **Recommendation = NBA = WHAT** (C04), **Execution
> Mapping = HOW** (C05), **Provider = WHO** (C05). **C04 показывает
> направление + WHY + действия** `Подобрать вариант` / `Почему` / `Другой
> вариант`; **услуга, мастер, цена, слот на C04 не показываются** (B3) —
> они на C05. Альтернативы C04.3 — только действием пользователя (B4).
> Execution options несут `action_type` (D-7), Execution Mapping Snapshot
> (§7) и строятся по цепочке `Need → Capability → CanonicalService →
> TenantOffer` (канон v1.1 Decision 11 §14); eligibility — только
> `VERIFIED` (C2, §8), иначе `NO_VERIFIED_CANDIDATES`. Коды этапов (D-6):
> **C01** = Hybrid First Contact (свободный текст + контекстные Quick
> Actions; чип = user expression тем же путём, что и текст); **C02** =
> Intent Resolution + Semantic Resolution с единым семантическим уточнением
> (`SKIP / CONFIRM_ONE / CHOOSE_MANY / ASK_CONTEXT`; «C02.4» — UX-метка
> режима `CHOOSE_MANY`, не стадия); **C03** — уточнение недостающих фактов
> по v0.4 (§30), вопрос — исход `CLARIFY` AYLA-DEC-0097; **C04** = WHAT +
> WHY; **C05** = HOW + WHO. Вариант исполнения «план» — только по правилу
> v0.5 ниже (AYLA-DEC-0091). Маппинг на этапы Journey — по Journey v1.3.
> **Не перенесено из PR #21:** «C03 = адаптивный DecisionReadiness flow»
> (AYLA-DEC-0097).

Каноническая цепочка:

```text
Canonical Recommendation (NBA)
→ Execution Mapping
→ execution options (SERVICE_PATH | self-care | observe | …)
→ Service
→ Provider Ranking
→ Booking
```

- `SERVICE_PATH` означает «реализуемо через услуги Ayla» и **не
  идентифицирует конкретную услугу**;
- **вариант исполнения «план» (v0.5, AYLA-DEC-0091):** без цели Ayla **не
  предлагает и не создаёт** план по своей инициативе; такой план может
  собрать только сам пользователь (ручной конструктор, источник `manual`).
  Предложение собрать план допустимо, только если плана нет и есть
  ACTIVE-цель с шаблоном ([[Ayla Decision Policy Contract]], ступень 6).
  Явный запрос человека «собрать план» без цели — явное намерение: он
  открывает ручной конструктор, а не предложение Ayla. Правило P-1 имеет
  приоритет над текстом ayla-knowledge PR #21 (решение владельца 21.09,
  журнал главного окна CD §71 п.3, вне git);
- на уровне Execution Mapping / Provider Ranking продолжают действовать
  правила Killer PRD §5.1 gates 3–6 (eligibility/availability → relevance
  → preference → economic-neutrality) — перенесены сюда из pipeline v0.3
  **без удаления** (re-home); конкретный provider ranking algorithm —
  отдельный downstream workstream (факт — Journey v0.3, OD-17) и
  Recommendation Engine Specification (planned);
- execution option, исключённый safety/eligibility/availability, не
  предлагается (§8); полная недоступность исполнения подходящего NBA —
  execution feasibility outcome с честным раскрытием (§11), а не основание
  сменить NBA;
- C01–C05 — рабочие коды этапов, введённые этим контрактом (v0.4): C01 —
  вход/выбор цели (этапы 1–3 Journey v0.3), C02 — Intent detection
  (этап 4), C03 — Clarification (этап 5), C04 — Recommendation +
  Explanation (этапы 7–8), C05 — исполнение: availability/booking
  (этапы 10–12). Маппинг на канонические этапы Journey подлежит
  подтверждению при синхронизации с Journey Spec.

## Change Log

### v0.6 (2026-09-22) — KB-F, DRF-2270: остаток ayla-knowledge PR #21, на отдельное утверждение

Основание: решение владельца 21.09 (журнал главного окна CD §71 п.1, вне
git) — полезные изменения PR #21, не нужные для K-1…M-1, представить на
самостоятельное утверждение. Номера — строки таблицы KB-E
(`docs/audits/2026-09-21-pr21-transfer-kb-e.md`); простыми словами —
`docs/audits/2026-09-22-pr21-rest-kb-f.md`. При отказе владельца — возврат
к v0.5.

| Раздел | Изменение (KB-F, из PR #21) | Строка KB-E |
|---|---|---|
| шапка, frontmatter | v0.6; related + Final Reconciliation | 1.1 (остаток) |
| §3 | `decision_subject` = WHAT; `action_type` → ExecutionOption; `readiness_state` (тень); `safety_policy_version`, `catalog_mapping_version`, ref `safety_evaluation`; `expires_at` → `actionable_until`; retention — политика | 1.2, 1.4 (остаток), 1.5, 1.6 |
| §5 | этапы 3–4 → Semantic Resolution + семантическое уточнение; этап 9 — четыре состояния safety; этап 16 — только VERIFIED | 1.7, 1.9 (остаток), 1.10 |
| §7 | три логических снимка; ADR-0013 superseded | 1.11 |
| §8 | только VERIFIED, `NO_VERIFIED_CANDIDATES`; staged ranking | 1.12 |
| §10 | альтернативы только действием | 1.13 |
| §14, §15, §17 | `accepted` / `declined` сняты; `explanation_requested`, `alternative_requested`, `engaged`, `booking_intent.created`; атрибуция только по provenance | 1.14 |
| §22 | `actionable_until` 2 ч; инвариант D4 `MATERIAL_CHANGE` | 1.15 |
| §23 | четыре состояния + `UNKNOWN` / `NOT_APPLICABLE`; B6; медгейт на записи | 1.16 (остаток) |
| §25 | replay по трём снимкам; OQ ADR-0013 1–5 | 1.17 |
| §26 | OQ-R9: retention отдельно от TTL | 1.18 |
| §28–§29 | `SemanticResolutionResult` (`outcomes[]`, `resolution_status`), `semantic_resolution_ref` | 1.7, 1.20 (остаток) |
| §30 | DecisionReadiness — только тень; две оси достаточности | 1.8, 1.23 (остаток) |
| §33, §34 | `action_type` вниз; WHAT / HOW / WHO; C04 без услуги/мастера/цены/слота; коды C01, C02, C04, C05 | 1.26 |

**Конфликт — не перенесено:** семейства provisional (CD §71 п.2);
`DesiredOutcome` refs, `desired_outcomes[]`, `semantic_readiness ⇒ ≥ 1`
(AYLA-DEC-0094); «C03 = адаптивный DecisionReadiness flow», замена этапов
7–8 (AYLA-DEC-0097); «сквозной» safety-этап и «гейтов ровно два»
(AYLA-DEC-0096); журнал «v1.0» PR #21 и номер версии 1.0 (без частей выше
формула «v1.0 = v0.4 + A1 + A2» ложна).

### v0.5 (2026-09-21) — Поправка по AYLA-DEC-0087, 0091, 0094, 0096, 0097, 0100; выборочный перенос из ayla-knowledge PR #21 (DRF-2263)

**Почему v0.5, а не v1.0.** PR #21 поднимал контракт до «PROPOSED v1.0 =
v0.4 + A1 + A2». По решению владельца 21.09 (журнал главного окна CD §71
п.1, вне git) в этот PR идут только изменения, нужные для K-1…M-1; A2
(синхронизация с каноном v1.1: DecisionReadiness, VERIFIED-eligibility,
три снимка, B8-события, `actionable_until`, четыре состояния safety и
др.) и шапка v1.0 — вне предмета и уходят отдельным PR. Из A1 перенесена
только часть про Goal optional. Формула «v1.0 = v0.4 + A1 + A2» стала бы
ложной, поэтому версия — v0.5, статус не изменён (draft / proposed).

| Раздел | Изменение | Основание | Из PR #21 |
|---|---|---|---|
| шапка, frontmatter | v0.5; related + Decision Policy Contract | — | 1.1 — изменено |
| §3 | `target_outcomes` — рабочие коды, не DesiredOutcome refs; `family` до пилота не заполняется (`null`); поля исхода — в DecisionOutcome | DEC-0094, 0097; CD §71 п.2 | 1.3 — отброшено; 1.4 — изменено |
| §5 | ступень 1 до этапа 1; этап 9 = ступень 3; этапы 3–4 — Goal optional (0..1, без синтеза), Outcomes без Goal (0..N); этап 4 «Adaptive Clarification семантики» и режимы `SKIP / CONFIRM_ONE / CHOOSE_MANY / ASK_CONTEXT` не вводятся | DEC-0096, 0087; CD §71 п.1 | 1.9 — изменено; 1.7 — вне предмета (KB-F, DRF-2270) |
| §23 | ссылка на ступень 1; аллергический фильтр ко всем кандидатам с составом, включая неизвестный или неполный (исход `UNKNOWN`); `CONFLICT / NO_CONFLICT_FOUND / UNKNOWN`, без гарантий, вне текста модели, журнал доступа; доступ субъекта — по CSR §5.9 | DEC-0096, 0100; CSR §5.9 | 1.16 — изменено |
| §26 | OQ-R11: семейства до пилота не включаются; новый OQ-R13 | CD §71 п.2; DP ОВ-15 | 1.25 — отброшено |
| §27 | Goal 0..1, без синтеза, «Создать цель» — вне конвейера; `ACTIVE` и смена цели — только явным действием | DEC-0087; [[Ayla Goal and Desired Outcome Contract]] (таблица переходов) | 1.19 — перенесено |
| §28 | Outcomes 0..N без Goal; без условия `≥ 1 desired outcome` и без `DesiredOutcome`; `SemanticResolutionResult`, `resolution_status` и режимы уточнения (WD D-6 / D-10) не переносятся | DEC-0087, 0094; CD §71 п.1 | 1.20 — изменено |
| §29 | `goal` optional; отсутствие Goal ≠ `INSUFFICIENT_CONTEXT` | DEC-0087 | 1.21 — перенесено |
| §30 | анкета не обязательный вход; CLARIFY vs NO_ACTION; теневые DecisionReadiness и `decision-policy-v1-shadow` ≠ выбор DEC-0097 | DEC-0087, 0097 | 1.22, 1.8, 1.23 — изменено |
| §31 | Goal не override | DEC-0087 | 1.24 — перенесено |
| §32 | исходы и поля по DEC-0097 — ссылка на DP; `no_action` ≠ `NO_ACTION`; «обоснованное ничего не делать» (DEC-0045) — исход `NO_ACTION`; предлагаемое соответствие | DEC-0097, 0045 | 1.8 — изменено |
| §33 | семейства до пилота не включаются, `family` = `null`; абзац v0.4 «LLM не может вводить новые families…» восстановлен целиком перед блоком v0.5 | CD §71 п.2 | 1.25 — отброшено |
| §34 | вариант «план» без цели Ayla не предлагает | DEC-0091; CD §71 п.3 | (2.8 FR — по смыслу) |

**Не перенесено из PR #21 (вне предмета, отдельный PR по CD §71 п.1):**
1.2, 1.5, 1.6, 1.7, 1.10–1.15, 1.17, 1.18, 1.26. Строка 1.7 (этап
Semantic Resolution, этап 4 «Adaptive Clarification семантики»,
`resolution_status` и режимы WD D-6 / D-10) — KB-F, DRF-2270: для фиксации
K-1 достаточно «Goal 0..1, не синтезируется, отсутствие Goal ≠
`INSUFFICIENT_CONTEXT`» (§5, §27–§29). Журнал v1.0 из #21 (1.27) не
переносится — вместо него эта запись. Полная таблица —
`docs/audits/2026-09-21-pr21-transfer-kb-e.md`; PR #21 —
`canon/recommendation-v1.0-proposed`, голова `dfd9595d`.


### v0.4 (2026-08-19) — Продуктово-семантический слой: Recommendation = Next Best Action

- **R-NBA-1 (controlled core + AI presentation):** Recommendation имеет
  контролируемое каноническое ядро; AI интерпретирует и формулирует
  представление (C04), но не является decision authority (§2, §34).
- **R-NBA-2 (NBA semantics):** Canonical Recommendation = Next Best
  Action. Предмет решения в record заменён: `decision_subject`
  (family/target/action_type/target_outcomes) вместо
  `candidate_id`/`rank`/`candidate_set_ref`/`ranking_policy_version` (§2,
  §3, §9, §10). Recommendation не является Goal, Outcome, услугой,
  provider или каталожной выдачей.
- **R-NBA-3 (economic neutrality / execution separation):**
  Recommendation Suitability ≠ Execution Feasibility — цена, доступность,
  комиссия, слоты не могут сделать менее подходящий NBA primary (§11);
  availability/price убраны из причин supersession и expiry NBA (§21,
  §22); execution-уровневые evidence отделены от decision-уровня (§12).
- **R-NBA-4 (compositional taxonomy):** NBA = `family + target +
  action_type`; начальные семейства ADDRESS/SUPPORT/RECOVER/OBSERVE —
  кандидаты до валидации против MVP Goal/Outcome таксономии (§33,
  OQ-R11).
- **R-NBA-5 (safety gate):** Safety — gate, не семейство;
  `SAFETY_BOUNDARY` — RecommendationResult, не CanonicalRecommendation
  (§23, §32).
- **R-NBA-6 (Decision Policy):** контролируемые правила eligibility /
  context fit / exclusion / priority / sufficiency; LLM не создаёт и не
  переопределяет families, targets, eligibility, exclusions, safety,
  primary selection, reason codes (§31).
- **R-NBA-7 (adaptive C03):** clarification порождается из
  missing/needs-confirmation фактов, требуемых политикой, а не из
  фиксированной анкеты; sufficiency переоценивается после ответов; C03
  пропускается при достаточном контексте; `INSUFFICIENT_CONTEXT` vs
  `OBSERVE` разведены (§30).
- **R-NBA-8 (engine boundary):** Recommendation Engine = «что сделать»;
  Execution Mapping = «как»; Provider Ranking = «кто». Pipeline разделён
  границей исполнения (§5); Candidate Model перенесён на
  execution-уровень без удаления правил (§8); цепочка `NBA → Execution
  Mapping → execution options → Service → Provider Ranking → Booking`;
  `SERVICE_PATH` не идентифицирует конкретную услугу; C04 = WHAT + WHY,
  C05 = HOW (§34).
- **Goal/Outcome/Context:** Goal Resolution (источники goal, запрет
  выдумывания связи, `source`/`confirmed`, §27); Outcome Resolution
  (1..N, один journey, §28); RecommendationContext с различением
  user-selected/stated/confirmed/memory/inferred (§29); Context
  Sufficiency `known | missing | needs_confirmation` (§30);
  RecommendationResult: `CLEAR_PRIMARY | MULTIPLE_SUITABLE |
  INSUFFICIENT_CONTEXT | SAFETY_BOUNDARY` + канонический `no_action`
  (OD-9); `SAFETY_BOUNDARY` ↔ runtime `SAFETY_BLOCKED`, `NO_CANDIDATES`
  оставлен execution-уровню (§32).
- **WHY:** объяснение использует только факты и reason codes, реально
  повлиявшие на решение; `Context Fact ≠ Reason Code`; AI формулирует,
  но не изобретает причинные основания (§13).
- **Перенос owner ruling 2026-07-29:** классификация объяснений
  displayable / internal-only и правило «нет displayable объяснения → не
  показываем» перенесены в §13 из Recommendation UX Addendum §2 (закрывает
  действие 1 UX-RECON-001 / KB-007; OQ-REC-6 о владельце классификации
  остаётся открытым в Addendum).
- **Сохранено из v0.3 без изменений:** immutable Recommendation +
  RecommendationSet с собственными `recommendation_id` (§3–4);
  supersession-модель (§21); immutable snapshot refs, запрет второго
  хранилища памяти (§7); consent и economic-neutrality правила (§11,
  §24); lifecycle как projection (§14); publication matrix и event
  ownership (§15); `presented ≠ viewed` (§16); acceptance/decline (§17);
  qualified-action attribution, direct/assisted/unattributed (§18);
  attribution windows — Measurement Framework (§19); Killer Moment через
  `recommendation_id` (§20); Booking ownership после начала booking flow
  (§22); replay без hidden chain-of-thought (§25); OQ-R9 остаётся открытым
  (Privacy/Legal).
- **Новые OQ:** OQ-R11 (NBA taxonomy — кандидат до валидации), OQ-R12
  (правка Killer PRD §5 под разделение NBA/Execution/Provider Ranking;
  связан с OD-AUDIT-003). Новые разделы §27–§34 размещены после §26 для
  сохранения ссылок на разделы v0.3 из Recommendation UX Addendum.
- Domain Event Registry, Journey Spec и Killer PRD этой версией **не
  изменяются**. Статус: draft / proposed.

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
