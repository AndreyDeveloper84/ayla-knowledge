---
node_id: ayla.architecture.recommendation-architecture-final-reconciliation
title: Recommendation Architecture Final Reconciliation
type: specification
status: review
decision_status: proposed
canonical_status: candidate
version: "1.0"
owner: Product Architecture
priority: P0
knowledge_area:
  - architecture
domain:
  - recommendation
concerns:
  - safety
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
created: 2026-09-12
updated: 2026-09-12
review_cycle: event-driven
depends_on:
  - "[[Ayla MVP Recommendation Contract]]"
  - "[[Ayla Intent Model Specification]]"
related:
  - "[[Ayla Domain Event Registry]]"
  - "[[Ayla Goal Outcome Semantic Model Working Design]]"
  - "[[ADR-0013 Recommendation Snapshot]]"
  - "[[BOT-003 Discovery and Recommendation Conversation Specification]]"
  - "[[Recommendation UX Addendum]]"
  - "[[Ayla MVP User Journey Specification]]"
---

> **Статус: PROPOSED v1.0 — awaiting owner approval (F3).** Копия
> `docs/RECOMMENDATION_ARCHITECTURE_FINAL_RECONCILIATION_v1.0_2026-09-12.md`
> (репозиторий Ayla) в `ayla-knowledge` — ход §6.1 п.2 самого документа
> («этот документ → `05 Architecture/Recommendation Architecture Final
> Reconciliation.md`, `type: specification`, `status: approved` — после
> утверждения владельцем»). Текст ниже — без изменений относительно копии
> в `docs/`, включая относительные пути `docs/…`, которые указывают на
> репозиторий Ayla, а не на этот. При утверждении владельцем:
> `status` → `approved`, `canonical_status` → `approved`.

# Recommendation Architecture — Final Reconciliation v1.0

**Статус документа:** `FOR OWNER APPROVAL (v1.0)` — финальная редакция после ответов владельца на все 14 вопросов черновика; канон утверждает владелец.
**Дата:** 12.09.2026. **Автор:** сабагент главного окна по брифу `scratchpad/brief_recon_final.md`.
**Заменяет:** `docs/RECOMMENDATION_ARCHITECTURE_FINAL_RECONCILIATION_DRAFT_2026-09-12.md` (далее «черновик»). Разделы черновика §0 «Резюме» и §8 «Вопросы владельцу» сняты: все вопросы отвечены.
**Основание:** черновик; `docs/OWNER_DECISIONS_2026-09-12_PACKAGE2.md` (далее «пакет 2»: B1–B14, C1–C3, D4, E1–E3); `docs/OWNER_DOCTRINE_MOCKUPS_ARE_CANON_2026-09-12.md` (далее «доктрина 12.09»); источники `ayla-knowledge` по путям §1.2.
**Что этот документ делает:** фиксирует целевой конвейер, реестр принципов, разрешённые конфликты, минимальную схему записи Recommendation, канонизационные ходы и состав первого Controlled Recommendation Slice. **Чего не делает:** не меняет ни один файл `ayla-knowledge`, не описывает реализацию; все ходы §6 — «после утверждения владельцем».

---

## 1. Статус, правило приоритета источников, что заменяется

### 1.1 Что утверждается одним пакетом (B7)

По B7 «(а) одним пакетом»: `05 Architecture/Ayla MVP Recommendation Contract.md` v0.4 → **v1.0** вместе с amendment **A1** (Goal optional, Semantic Resolution) и **A2** (синхронизация с решениями канона v1.1: DecisionReadiness, четыре состояния safety, VERIFIED-гейт, таксономия событий). Состав A1/A2 — §6.2. До утверждения все документы ссылаются на контракт как «proposed contract», не «CANON» (черновик, конфликт 2).

### 1.2 Правило приоритета

При расхождении источников действует порядок (от старшего к младшему):

1. **Решение владельца** — пакет 2 (`docs/OWNER_DECISIONS_2026-09-12_PACKAGE2.md`), доктрина 12.09, `docs/Ayla_Owner_Decisions_Package_2026-09-12.md` (rulings 1–9), `docs/ayla-owner-decisions-2026-09-11.md`, `docs/OPEN_DECISIONS.md` (§76, §98, §99, §103, §105, §145), `docs/OD_C04_GROUNDED_WHY.md`, owner rulings внутри документов знаний (AYLA-DEC-*, OQ-R*, BOT-003-Q*).
2. **Active Canon** — документы `ayla-knowledge` со `status: approved` / `canonical_status: approved`; после утверждения пакета — контракт v1.0 и этот документ.
3. **Working Canon** — `docs/ayla-conversation-state-v1.1-reconciled.md` («Working Canon — Decisions 1–14 reconciled»). По **B1** он **не Active Canon до закрытия его §24**; его принятые решения (1–14) переносятся в контракт v1.0 через A2 и в этот документ. В части, перенесённой сюда и в A2, они действуют как уровень 2; в остальном документ уступает контракту v1.0.
4. **Draft / Proposed** — `status: draft`, `decision_status: proposed`, `canonical_status: candidate|draft`.
5. **Review / Report** — `status: review`, отчёты агентов, планы reconciliation.

Внутри одного уровня — более поздняя дата. Owner ruling внутри draft-документа (OQ-R1…R6 в контракте, owner ruling 2026-07-29 о displayable WHY) имеет силу уровня 1, но не поднимает статус документа-носителя.

Два пункта, которые пакет 2 велит не искажать (дословно): «B2/B3 — Ayla Recommendation это NBA / WHAT, service/master — execution / HOW+WHO. C2 — отсутствие VERIFIED не запрещает услуге существовать в Catalog или direct booking; оно запрещает Ayla выдавать её как semantic Recommendation».

### 1.3 Реестр источников (статусы дословно из frontmatter/шапок, по черновику §1.2)

| Источник (путь в `ayla-knowledge`, если не указано иное) | Статус дословно | Уровень | Ход в пакете |
|---|---|---|---|
| `03 AI System/Ayla Intent Model Specification.md` v1.0 | «Approved v1.0 (2026-08-08, Product Owner) — Active Canon» | 2 | не меняется (§6.4) |
| `03 AI System/Contracts/intent-registry.yaml`, `intent-output.schema.json` | `status: draft`, «v1.0, draft / proposed / candidate» — метка устарела относительно .md | 2 по тексту .md | метаданные — A3 |
| `05 Architecture/Ayla MVP Recommendation Contract.md` v0.4 | «Draft v0.4 — proposed. Это не канонизация» | 4 (OQ-R1…R6 — 1) | → v1.0 + A1 + A2 |
| `05 Architecture/Ayla Goal Outcome Semantic Model Working Design.md` v0.9 | «Non-canonical» | 4 (OD-GO/SR/CI/DC — направления) | дельты §20 → A1; сам — evidence base |
| `05 Architecture/ADR-0013 Recommendation Snapshot.md` v0.1 | «До канонизации нормативным документом не является» | 4 | superseded (B10) |
| `01 Product/BOT-003 Discovery and Recommendation Conversation Specification.md` v0.1 | «CANDIDATE FOR CANON REVIEW» | 4 (Q3/Q4/Q6/Q8/Q9 APPROVED — 1) | candidate → approved |
| `01 Product/UX MVP/contracts/recommendation-ux-addendum.md` v0.1 | «Не source of truth для recommendation-правил» | 4 | → v0.2 (A4) |
| `01 Product/UX MVP/reviews/recommendation-owner-review-001.md`, `recon-recommendation-contract-001.md` | `status: review` | 5 | архив |
| `UX Agents/planning/BOT-003-canon-reconciliation.md`, `UX Agents/reports/BOT-001-reconciliation-report.md` | отчёты | 5 | остаются как есть |
| `approved_v1_1.md` (корень) | `status: superseded`, `canonical_status: deprecated` — это Journey v1.1 | история | → history/archive (B14) |
| `docs/ayla-conversation-state-v1.1-reconciled.md` (репозиторий Ayla) | «Working Canon — Decisions 1–14 reconciled» | 3 (B1) | остаётся в `docs/`; решения — в A2 и сюда |
| `docs/specs/DECISION_READINESS_ENGINE_v1.0.md` (репозиторий Ayla) | DRAFT-спецификация движка | 4 | источник §16.1–§16.2 для §8 |

Оговорка черновика §1.3 сохраняется: «канон v1.1» ниже — это `docs/ayla-conversation-state-v1.1-reconciled.md`, а не `approved_v1_1.md`.

---

## 2. Целевой конвейер — единственная таблица слоёв

Обозначения authority: **LLM** — извлечение/формулировка; **PB** — Product Brain (детерминированная политика в `ayla-ai-core`); **Каталог** — канонический каталог / backend как source of truth; **Владелец** — политика, которую задаёт только владелец. C01–C05 — коды этапов из контракта v0.4 §34 и макетов.

Тройное разделение, зафиксированное владельцем: **Recommendation = NBA = WHAT** (слои 8–10, B2); **Execution Mapping = HOW** (слои 11–12); **Provider = WHO** (слой 13). C04 показывает NBA + WHY; C05 — услугу, мастера, цену, слот (B3).

| # | Слой (код) | На какой вопрос отвечает | Вход | Выход | Authority | Источник | Статус источника / решение |
|---|---|---|---|---|---|---|---|
| 1 | Entry / User Expression (C01) | Что человек сказал или нажал? | сообщение MAX / Mini App, чип C01, deep link | нормализованный `query` + entry context; чип = user expression, тем же путём, что и free text | канал → PB | BOT-001 (approved v1.0); WD OD-C01-1…3; `ai-bot-platform/apps/channels/max/quick_actions.py:96-121` | approved / направления / код |
| 2 | Intent Resolution (C02) | Что человек имеет в виду сейчас? | query + permitted session context + authorization state + safety input | Intent Resolution Output `contract_version 0.5`: `intent_type` (11 + `UNKNOWN`), `status`, `slots`, `safety_flags`, `evidence`, `requires_clarification` | PB (LLM извлекает) | Intent Model §Output Contract | **Active Canon** |
| 3 | Semantic Resolution (Goal / Desired Outcomes) | Какое изменение человек хочет и зачем? | Intent Output + user expression + allowed context | `SemanticResolutionResult`: `goal?` 0..1, `desired_outcomes[]` 0..N, `resolution_status`, `semantic_readiness`; Goal не синтезируется; **Goal optional — рекомендация не требует создания Goal (B5)** | PB (таксономия — Владелец) | WD §11.2 (OD-SR-1…6, OD-DC-1); контракт §27–§29 → A1 | **B5**, A1 |
| 4 | Adaptive Clarification (C03) | Что уточнить, чтобы не спрашивать лишнего? | `resolution_status`, InterpretationGroup, required context facts | `SKIP / CONFIRM_ONE / CHOOSE_MANY / ASK_CONTEXT`; ≤1 вопрос за ход; после ответа re-resolution; **C03 = адаптивный DecisionReadiness flow; анкета `area → feeling → goal` перестаёт быть обязательным входом (B5)** | PB | WD §11.1, §11.3; Intent Model §Confidence and Clarification (≤2 подхода); доктрина 12.09 «повторный вопрос об известном → движок не задаёт» | **B5**, доктрина |
| 4a | «Создать цель» (Mini App) | Хочет ли человек завести цель сам? | явное действие пользователя | `ClientGoal` → Goal `ACTIVE` (канон v1.1 §12.1 «только после explicit user action»); **отдельный явный путь, вне рекомендательного конвейера (B5)** | канал → backend | канон v1.1 §12.1; B5 | **B5** |
| 5 | Context & Memory Retrieval | Что о человеке разрешено знать сейчас? | consent state, purpose, scope | `context_snapshot_ref`, `memory_snapshot_ref` (immutable); admissible set по consent; порядок сбора согласий — E2 | Каталог/backend + консент (Владелец) | контракт §5–§7; Consent Scope Registry (approved v1.2); канон v1.1 Decision 8; E2 | draft / approved / B1 / E2 |
| 6 | Safety gate (сквозной, до Recommendation) | Можно ли продолжать и в каких границах? | extracted signals, red-zone факты, provenance | `NORMAL / CLARIFY / CAUTION / STOP` (+ `UNKNOWN` fail-closed, `NOT_APPLICABLE`); `rule_id`, `policy_version`, allowed/forbidden capabilities. **До утверждённой матрицы §16.2: потенциально медицинский смысл → `CLARIFY` fail-closed для затронутой capability; один decision-changing safety-вопрос; до ответа semantic Recommendation не формируется (B6)** | детерминированный Safety Engine (PB); правила — **Владелец** | канон v1.1 Decision 4; owner 11.09 §3; Intent Model §Safety-sensitive Intents; B6 | **B6**; матрица — открыта (C3, §8) |
| 7 | DecisionReadiness (C03) | Достаточно ли подтверждённых данных для ответственной рекомендации? | SemanticResolutionResult + RecommendationContext + safety state + candidate set | `READY / NEEDS_DISCRIMINATION / NEEDS_REQUIRED_CONTEXT / INSUFFICIENT_EVIDENCE / BLOCKED` + `DecisionEvidence`; вопрос только если меняет admissibility/ranking/execution parameter. **На пилоте — shadow mode: считает, не управляет пользователем, пока пороги не доказаны (C1)** | PB (без LLM) | канон v1.1 Decision 5; `docs/specs/DECISION_READINESS_ENGINE_v1.0.md`; контракт §30 → A2; BOT-003 §6 | B1 / DRAFT / **C1** |
| 8 | **Recommendation = Canonical NBA (C04 ядро, WHAT)** | Что человеку разумно сделать сейчас? | всё выше внутри admissible set | `RecommendationSet`: primary NBA + ≤2 alternatives, `result_status` (`CLEAR_PRIMARY / MULTIPLE_SUITABLE / INSUFFICIENT_CONTEXT / SAFETY_BOUNDARY`), `no_action`, `reason_codes`, `evidence_refs`, версии; families `ADDRESS / SUPPORT / RECOVER / OBSERVE` provisional (B9) | PB (Decision Policy); **LLM не authority** | контракт §31–§33 (R-NBA-1…8); AYLA-DEC-0045 / OD-9; канон v1.1 Decision 7; **B2** | **B2, B9** |
| 9 | Explanation (WHY) | Почему это подходит — и можно ли это показать? | decision + реально использованные facts/reason codes | `explanation` с классификацией `displayable / internal-only`; grounded-пересказ разговора (P0) | PB классифицирует; LLM формулирует | контракт §13; owner ruling 2026-07-29; `docs/OD_C04_GROUNDED_WHY.md` | решение владельца |
| 10 | Presentation C04 (WHAT + WHY) | Как показать решение человеку? | persisted records + displayable explanation | карточка направления + WHY + действия `Подобрать вариант` / `Почему` / `Другой вариант`; **услуга, мастер, цена, слот на C04 не показываются (B3)**; **альтернативы C04.3 — только действием пользователя, не автоматически (B4)**; нет displayable WHY → no-recommendation | канал; макеты — **Владелец** | макеты C04.1–C04.6 (по `docs/RECONCILIATION_C01_C05_MOCKUPS_VS_RUNTIME_2026-09-12.md` §4); доктрина 12.09; UX Addendum → A4 | **B3, B4** |
| 11 | **Execution Mapping (C05, HOW)** | Как это можно реализовать? | принятый NBA | execution options: `SERVICE_PATH | self-care | observe | plan`; Capability ← Need/Outcome | PB по онтологии; онтология — Каталог/Владелец | контракт §34; канон v1.1 Decision 11 §14 (`Need → Capability → CanonicalService → TenantOffer`) | draft / B1 |
| 12 | CanonicalService & TenantOffer resolution (eligibility) | Какая проверенная услуга это реализует здесь? | Capability + tenant scope | **только `approved`-канон и `mapping_status = VERIFIED` (C2, §76, §105)**; иначе `NO_VERIFIED_CANDIDATES` — штатный результат. **Не-VERIFIED услуга остаётся в Catalog / Search / direct booking при остальных gates; как Ayla Recommendation — нельзя (C2)** | **Каталог**; VERIFIED первого slice — владелец лично (B12) | `docs/OPEN_DECISIONS.md` §76, §105, §145; owner 11.09 §1; канон v1.1 §14.2–§14.3; C2; E1 | **C2, B12, E1** |
| 13 | **Provider / Transaction resolution (C05, WHO)** | Кто и когда может это выполнить? | eligible offers; location, availability, price, explicit preference | ranked execution options; staged: hard eligibility → semantic fit → transaction fit → personalization → quality → tie-break; `distance_meters`; на C05 — услуга, мастер, цена, слот (B3) | backend (truth) + PB (semantic ranking); экономика — вне ranking | канон v1.1 Decision 6; контракт §8, §11; пакет 12.09 §3 (distance); D3 (геолокация — contextual consent «Показать рядом со мной») | B1 / draft / решения владельца |
| 14 | User Decision → PendingBookingIntent | Что человек выбрал? | reaction (`WHY_REQUESTED / ALTERNATIVE_REQUESTED / ENGAGED / REJECTED / CONSTRAINT_ADDED`) | `PendingBookingIntent(recommendation_id, execution_option)` с KNOWN/UNKNOWN/FLEXIBLE; acceptance ≠ booking; **фиксируется именно та execution option, которую клиент видел и подтвердил (D4)** | канал → backend | канон v1.1 Decisions 7, 13; контракт §17; BOT-003 §10–§13; D4 | B1 / draft / **D4** |
| 15 | Booking (revalidation + медгейт) | Можно ли создать запись прямо сейчас? | PendingBookingIntent, `requires_health_check` | запись либо маршрутизация к человеку (`True`/`UNKNOWN` → `HEALTH_CHECK_UNKNOWN`, не `BOOKING_ERROR`, §98); revalidation availability/price; **расхождение с подтверждённой опцией → `MATERIAL_CHANGE` → показать → новое подтверждение; не silent normalization (D4)** | backend; политика — Владелец | `docs/OPEN_DECISIONS.md` §98; канон v1.1 §16.8; контракт §22 (OQ-R6); D4 | **§98, D4** |
| 16 | Outcome / Feedback / Analytics | Что произошло и чему это учит? | reactions, outcomes, feedback | append-only evidence; attribution только по provenance chain `Recommendation → PendingBookingIntent → Booking`; события `recommendation.created / presented / explanation_requested / alternative_requested / engaged` + `booking_intent.created`; **`recommendation.accepted` не вводится (B8)**; `shown ≠ engaged ≠ booked ≠ completed ≠ liked` | Attribution / Measurement | канон v1.1 Decision 14, §17.3, §17.5; контракт §15, §18–§20 → A2 | B1 / **B8** |

Инварианты поверх таблицы:

- (а) слои 6 и 7 пересчитываются после каждого значимого события пользователя (канон v1.1 §7.2, §8); ответ на clarification — тот же `intent_id` (Intent Model §Confidence and Clarification п. 4);
- (б) слой 8 не видит цену, доступность, комиссию и слоты (R-NBA-3); цена — только как пользовательский `budget`-constraint;
- (в) слои 11–13 не переписывают NBA: недоступность исполнения — «execution feasibility outcome с честным раскрытием» (контракт §11), не подмена направления;
- (г) слои 12–13 работают только по `VERIFIED` (§76, C2) и только по `approved`-канону (§105); ноль VERIFIED → `NO_VERIFIED_CANDIDATES`, без fallback на `REVIEW_REQUIRED`;
- (д) LLM участвует на слоях 1–3 (извлечение), 9 (формулировка WHY), 10 (рендер); на слоях 6–8, 12–13, 15 — не участвует в решении (канон v1.1 §21; DRE §17.1 «Ни одного вызова LLM»);
- (е) приоритет источников внутри admissible set: explicit current statement > current click > transaction truth > relevant Goal > history/memory (канон v1.1 §20; контракт §6);
- (ж) «Ayla рекомендует» — только для выхода слоёв 8–10; каталог и поиск подписываются «Рядом с вами» / «Доступные услуги» (пакет 12.09 §3);
- (з) два safety-гейта, не один: conversational safety state (слой 6, до Recommendation, B6) и service-level health gate на записи (слой 15, §98); кандидат с `requires_health_check ∈ {True, UNKNOWN}` может быть рекомендован как направление, исполнение уходит к человеку — это раскрывается в WHY/C05 честно;
- (и) 2 ч — TTL контекста и actionability, не срок жизни записи: immutable Recommendation record хранится для attribution/audit по отдельной retention policy (B13).

Отличия от таблицы черновика §2: добавлен слой 4a (явный путь «Создать цель», B5); слой 8 назван Recommendation = NBA/WHAT, 11 — HOW, 13 — WHO (B2/B3); слой 6 получил правило CLARIFY fail-closed (B6); слой 7 — shadow mode (C1); слой 10 — правило альтернатив по действию (B4); слой 12 — формулировку eligibility по C2; слои 14–15 — инвариант D4; слой 16 — снятие `recommendation.accepted` (B8); инварианты (з), (и) — новые.

---

## 3. Реестр устойчивых принципов (17)

Статусы: **К** — Active Canon / Working Canon v1.1 (B1); **В** — решение владельца. Уровня «только draft» после пакета 2 не осталось.

| # | Принцип | Источник (цитата ≤ 2 строк, путь) | Статус |
|---|---|---|---|
| 1 | `Query ≠ Intent` | «Query — нормализованное содержимое текущего обращения, само по себе не достоверный факт и не Intent» — `03 AI System/Ayla Intent Model Specification.md` §Responsibility | К |
| 2 | `Intent ≠ Goal` | «Intent не владеет Transformation Goal и не заменяет её» — там же, §Transformation Goal and Intent; AYLA-DEC-0043 (OD-7) | К + В |
| 3 | `Recommendation ≠ Booking` | «Recommendation не является действием. Orchestration исполняет action только после подтверждения» — Intent Model §Orchestration Intent Model; канон v1.1 §10 | К |
| 4 | `Recommendation ≠ Service` (Recommendation = NBA / WHAT) | «Recommendation **не является**: … услугой (service), provider или слотом» — `05 Architecture/Ayla MVP Recommendation Contract.md` §2; **B2** «Recommendation = WHAT. Service/master = downstream execution» | **В (B2)** + К |
| 5 | LLM не Recommendation Authority | «LLM не может самостоятельно создавать или переопределять families, targets, eligibility, exclusions, safety, выбор primary» — контракт §31 (AYLA-DEC-0045); owner 11.09 §18 п.4 | В |
| 6 | Safety / Consent — gates, не families | «Safety — это gate, а не Recommendation family (v0.4, R-NBA-5)» — контракт §23; канон v1.1 Decision 4; owner 11.09 §3; **B6** (fail-closed CLARIFY до матрицы) | К + В |
| 7 | Не задавать вопрос без material reason | «Next question is allowed only if its answer can change admissibility, ranking, or required execution parameters» — канон v1.1 §8; BOT-003-Q3 APPROVED; **B5** (C03 = адаптивный DRE flow) | К + В |
| 8 | `no_action` — валидный результат | «`no_action` — полноценный объяснимый результат» — AYLA-DEC-0045 по WD §4.7; CDP-11 | В + К |
| 9 | Primary recommendation — default | «When a responsible primary recommendation can be formed, it is Ayla's default conversational presentation (`BOT-003-Q4`)» — BOT-003 §7 | В (Q4 APPROVED) |
| 10 | Alternatives доступны по действию, не каталог | «Alternatives remain reachable when explicitly requested, compared, when the primary is rejected…» — BOT-003 §8; «≤2» — контракт §10; **B4** «список альтернатив НЕ показывается автоматически — пользователь открывает C04.3 действием» | **В (B4)** |
| 11 | WHY обязателен | «Every decision should carry `DecisionEvidence` / reason codes for WHY and auditability» — канон v1.1 §8; Constitution Ст. VII (по Addendum §2) | К |
| 12 | No displayable WHY → no show | «Нет displayable объяснения → не показываем» — контракт §13 (owner ruling 2026-07-29); owner 11.09 §18 п.5 | В |
| 13 | Acceptance ≠ Booking | «Acceptance does not mean a booking was created, a slot reserved, availability guaranteed» — BOT-003 §13; контракт §17; канон v1.1 §10.3; **B8** (`accepted` не вводится) | В + К |
| 14 | Dynamic facts revalidate before action | «Final booking always revalidates transaction truth» — канон v1.1 §10.3; BOT-003-Q12 CLOSED; **D4** (revalidate именно подтверждённую опцию; `MATERIAL_CHANGE` → новое подтверждение) | К + **В (D4)** |
| 15 | Commercial interest не определяет organic Recommendation | «Platform revenue/economic benefit MUST NOT influence organic recommendation ranking» — канон v1.1 §9.1; контракт §11 | К |
| 16 | Recommendation имеет ID, evidence, provenance; запись immutable и переживает TTL контекста | «Recommendation — immutable decision record; RecommendationSet — immutable группирующая запись» — контракт §26 OQ-R1 ACCEPT; канон v1.1 §10.1; **B13** «immutable Recommendation record (хранится для attribution/audit по отдельной retention policy)» | В + К |
| 17 | Search, Catalog и Recommendation — разные контуры; eligibility = VERIFIED | «catalog_visible ≠ recommendation_eligible» — канон v1.1 §14.3; «`Ayla рекомендует` резервируется только для canonical Recommendation» — пакет 12.09 §3; **C2** | К + **В (C2)** |

Вывод: все 17 принципов держатся на Active/Working Canon или решении владельца. Разрыв, названный в черновике («носитель большинства принципов — draft»), закрывается ходом §6.1 п.1 (контракт v1.0).

---

## 4. Конфликты — все закрыты

Формат: суть → чем закрыт → что меняется.

| # | Конфликт (черновик §4) | Статус | Чем закрыт | Что меняется |
|---|---|---|---|---|
| 1 | UX Addendum требует на карточке услугу и мастера; контракт и макет C04.1 делают предметом карточки направление | **ЗАКРЫТ** | **B3 (а)**: «C04 показывает направление/NBA + WHY; услуга, мастер, цена, слот — в C05 после перехода к execution mapping» | Addendum → v0.2 «C04/C05 Presentation Constraints» (A4); OQ-REC-4 закрыт ответом «не на C04; на C05 — по данным TenantOffer»; recon-001 и owner-review-001 — архив |
| 2 | Контракт называется CANON, но сам Draft | **ЗАКРЫТ** | **B7 (а)**: одним пакетом v1.0 + A1 + A2 | frontmatter/шапка контракта; ссылки в Addendum, BOT-003 §20, Journey v1.2 (v0.3 → v1.0) |
| 3 | Goal → Outcome linearity (контракт требует Goal до Outcomes) | **ЗАКРЫТ** | **B5**: «Goal optional для Recommendation — не заставлять создавать Goal ради рекомендации»; **B7**: A1 в пакете | контракт §5 (этапы 3–4 → Semantic Resolution), §27–§30; `RecommendationContext.goal` optional; отсутствие Goal ≠ `INSUFFICIENT_CONTEXT`; Goal влияет через controlled priority, не override; рабочий термин — `DesiredOutcome` (OQ-GO-1 остаётся) |
| 4 | ADR-0013 построен вокруг candidate-модели | **ЗАКРЫТ** | **B10 (а)**: superseded — «смешивает decision, candidate/provider ranking и transaction state» | ADR-0013 `superseded_by: контракт §7 + §25; канон v1.1 Decision 7`; три логических снимка: Decision Snapshot (в record), Execution Mapping Snapshot (в execution option), Transaction Snapshot (в PendingBookingIntent/Booking); правило «UX рендерит из snapshot, не из live» сохраняется |
| 5 | Event taxonomy — четыре несогласованных набора имён | **ЗАКРЫТ** | **B8 (а)**: снять `recommendation.accepted` — «ENGAGED доказывает взаимодействие, `booking_intent.created` — переход к исполнению» | одна таксономия = канон v1.1 §17.3 + контракт §15 как publication matrix (A2); `presented` = transport ack (OQ-R3); `declined` → `REJECTED` reaction; `qualified_action.attributed` — только по provenance chain; PascalCase-имена — справочно |
| A | «Safety до Recommendation» (разбор §9) против «медгейт на записи» (§98) | **ЗАКРЫТ** как два гейта | **B6 (а) CLARIFY** для слоя 6; §98 для слоя 15; инвариант (з) §2 | до матрицы §16.2 потенциально медицинский смысл fail-closes затронутую capability одним safety-вопросом; матрица — C3 (§8) |
| B | «одна primary» против макета «карточка + альтернативы» | **ЗАКРЫТ** | **B4 (а) с уточнением**: «„Другой вариант“ доступен всегда после primary; список альтернатив НЕ показывается автоматически» | C04.3 (≤2, radio) открывается действием; A4 фиксирует это как presentation constraint |
| C | «Goal не обязателен» против обязательной анкеты `area → feeling → goal` (DRF-1451) | **ЗАКРЫТ** | **B5 (б) с оговоркой**: «C03 становится адаптивным DecisionReadiness flow; отдельный явный путь „Создать цель“ в Mini App остаётся» | анкета как обязательный вход в рекомендацию снимается; «Создать цель» — слой 4a; поле, не влияющее на решение, не заявляется учтённым (owner 11.09 §5.3) |
| D | Предмет записи: NBA (контракт) или candidate (канон v1.1 §10.1) | **ЗАКРЫТ** | **B2 (а) NBA**: «Главное архитектурное разделение» | «primary candidate» канона v1.1 §10.1 читается как execution candidate внутри Capability-пространства; в decision record — `decision_subject` = NBA; A2 приводит §10.1 к этому чтению; DecisionReadiness проверяет NBA-уровень и наличие VERIFIED-исполнения |
| E (новый) | Авторитет цены/длительности при расхождении ребра мастера и услуги салона (golden P1: показано 60 мин / 1500 ₽, записано 45 мин) | **ЗАКРЫТ** | **D4 (а), «инвариант сильнее»**: «Авторитетна конкретная execution option, которую видел и подтвердил клиент… MATERIAL_CHANGE → показать пользователю → новое подтверждение. Не silent normalization и не „ребро всегда главнее“» | слой 14 хранит подтверждённую execution option; слой 15 revalidate именно её; расхождение → `MATERIAL_CHANGE` → повторное подтверждение; проверка S5 §7.1 |

Инвариант D4 в формулировке для контракта: **exact client-confirmed execution option → на записи revalidate именно её → любое расхождение = `MATERIAL_CHANGE` → новое подтверждение пользователя**. Ни ребро мастера, ни SalonService не имеют приоритета «по умолчанию»; приоритет — у того, что клиент видел.

Реестр кодов для A2 (замер `docs/MEASURE_D4_QUOTE_CHANGED_393.md`): `MATERIAL_CHANGE` — зонтичное понятие контракта, в каталоге ему соответствуют `409 QUOTE_CHANGED` (#393: `details.field ∈ {price, duration_minutes}`, `quoted`, `applied`) и `409 SLOT_UNAVAILABLE` (слот/мастер); коды каталога не переименовываются. Разрыв: сверка в #393 срабатывает только при присланных `quoted_*`, а бот их не шлёт (`ai-bot-platform` `origin/dev` 5ee4164e) — клиентская половина DRF-1708 у ayla-c1.

---

## 5. Объект Recommendation — минимальная схема для Controlled Pilot

Пометки: **канон** — Active Canon / owner ruling / канон v1.1 (B1); **В** — решение владельца пакета 2; **A1/A2** — входит в контракт v1.0 через amendment.

```yaml
RecommendationSet:                       # одна выдача (OQ-R1) — канон
  recommendation_set_id:
  subject_id:                            # псевдонимизированный — контракт §3
  intent_id:                             # связь с Intent Output 0.5 — канон
  semantic_resolution_ref:               # SemanticResolutionResult — A1 (WD §11.2)
  primary_recommendation_id:
  alternative_recommendation_ids: []     # ≤2; показываются только действием пользователя — В (B4)
  created_at:

Recommendation:                          # immutable decision record — канон (OQ-R1; канон v1.1 §10.1); хранится по retention policy — В (B13)
  recommendation_id:                     # создаёт только Recommendation context — канон
  recommendation_set_id:
  recommendation_role: primary | alternative
  parent_recommendation_id:              # lineage R1 → R2 — канон (v1.1 §10.2)
  rerank_reason:                         # ALTERNATIVE_REQUESTED | REJECTED | CONSTRAINT_ADDED — канон (v1.1 §10.3)
  decision_subject:                      # ЧТО = Canonical NBA — В (B2)
    direction_code:                      # рабочий код направления (taxonomy_version)
    target_outcomes: []                  # DesiredOutcome refs — A1 (контракт §28, OD-DC-1)
    family:                              # ADDRESS | SUPPORT | RECOVER | OBSERVE — В (B9, provisional для Controlled Pilot)
  result_status:                         # CLEAR_PRIMARY | MULTIPLE_SUITABLE | INSUFFICIENT_CONTEXT | SAFETY_BOUNDARY | NO_ACTION — контракт §32 + OD-9
  readiness_state:                       # READY | NEEDS_DISCRIMINATION | NEEDS_REQUIRED_CONTEXT | INSUFFICIENT_EVIDENCE | BLOCKED — канон (v1.1 Decision 5) → A2
  reason_codes: []                       # из Decision Policy, не из LLM — канон (v1.1 §8, §9.3)
  evidence_refs: []                      # user_stated | confirmed_memory | policy | safety | journey — контракт §12; grounded WHY P0 — owner 24.08
  explanation:
    displayable: true | false            # owner ruling 2026-07-29 — канон
    user_visible_reasons: []             # только grounded-пересказ разговора (P0) — owner 24.08
    internal_only: []                    # никогда наружу
  safety_evaluation_ref:                 # {state, rule_id, policy_version, evidence_ref, activated_at} — owner 11.09 §3; state=CLARIFY fail-closed до матрицы — В (B6)
  consent_evaluation_ref:                # scope/purpose — контракт §24 + CSR approved
  context_snapshot_ref:                  # Decision Snapshot: immutable {snapshot_id, snapshot_version, content_digest} — контракт §7; В (B10: один из трёх снимков)
  memory_snapshot_ref:                   # Phase 1: null — контракт §7
  decision_policy_version:               # канон (v1.1 §10.1)
  taxonomy_version:                      # контракт §3
  safety_policy_version:                 # канон (v1.1 §7.2)
  catalog_mapping_version:               # канон (v1.1 §14.6)
  presentation_policy_version:           # контракт §3
  created_at:
  actionable_until:                      # = 2 ч ConversationState / active recommendation context — В (B13); прежнее имя expires_at в контракте §22 переименовать в A2, чтобы не читалось как срок жизни записи
  record_schema_version:

# Retention записи — НЕ поле записи, а отдельная политика (В, B13): число лет — открыто (§8).
# НЕ входит в запись (execution segment, слои 11–13 — HOW/WHO):
#   candidate_id, rank, service_ref, provider_ref, price_snapshot, availability_ref, distance_meters
#   — живут в ExecutionOption (Execution Mapping Snapshot) / PendingBookingIntent (Transaction Snapshot) — В (B2, B10).
# PendingBookingIntent хранит exact client-confirmed execution option — В (D4).
# События: recommendation.created / presented / explanation_requested / alternative_requested / engaged
#   + booking_intent.created; recommendation.accepted не вводится — В (B8).
```

Минимум для пилота (без него запись не считается Recommendation): `recommendation_id`, `recommendation_set_id`, `recommendation_role`, `decision_subject.direction_code` + `target_outcomes` + `family`, `result_status`, `readiness_state`, `reason_codes`, `evidence_refs`, `explanation.displayable`, `safety_evaluation_ref`, версии политик, `catalog_mapping_version`, `actionable_until`.

Изменения относительно черновика §5: `expires_at` → `actionable_until` (B13; retention вынесен в политику); `family` из «отложено §24» → provisional (B9); `alternative_recommendation_ids` — правило показа B4; `context_snapshot_ref` — один из трёх снимков B10; блок событий — B8; `decision_subject` = NBA закрыт B2; PendingBookingIntent — D4.

---

## 6. Канонизационные ходы — все «после утверждения владельцем»

### 6.1 В Active Canon

1. `05 Architecture/Ayla MVP Recommendation Contract.md` — v0.4 → **v1.0** `status: approved / decision_status: accepted / canonical_status: approved`, одновременно с A1 и A2 (B7) и правками по конфликтам 2, 4, 5, D, E.
2. Этот документ → `05 Architecture/Recommendation Architecture Final Reconciliation.md` (`type: specification`, `status: approved`) — карта слоёв §2, реестр §3, разрешённые конфликты §4.
3. `01 Product/BOT-003 Discovery and Recommendation Conversation Specification.md` — candidate → approved: Q3/Q4/Q6/Q8/Q9 уже APPROVED; блокер §20 («зависимости draft») снимается п.1; §5 «Recommendation sufficiency» получает ссылку «= DecisionReadiness (контракт v1.0 §30)».

Снято относительно черновика §6.1: перенос `docs/ayla-conversation-state-v1.1-reconciled.md` в `ayla-knowledge` как канона — **не делается (B1)**. Документ остаётся в `docs/` как Working Canon с открытым §24; его Decisions 1–14 попадают в `ayla-knowledge` через A2 и этот документ.

### 6.2 Amendment

- **A1 к Recommendation Contract** — дельты `05 Architecture/Ayla Goal Outcome Semantic Model Working Design.md` §20: D-1…D-5 (Goal optional, Semantic Resolution вместо Goal/Outcome Resolution — B5), D-6 (C01 Hybrid First Contact, C02 = outcome resolution с Adaptive Clarification, C03 = adaptive DecisionReadiness flow — B5), D-7 (`action_type` → C05), D-9, D-10 (`SemanticResolutionResult` upstream, Context Sufficiency = decision-level). D-8 (families) — закрыт B9 как provisional `ADDRESS / SUPPORT / RECOVER / OBSERVE`.
- **A2 к Recommendation Contract** — синхронизация с каноном v1.1 (B1, B7): §30 → DecisionReadiness (5 состояний); §5 этап Safety → 4 состояния + `UNKNOWN`/`NOT_APPLICABLE` + правило CLARIFY fail-closed до матрицы (B6); §8/§34 → eligibility только `VERIFIED` (C2, §76) и `NO_VERIFIED_CANDIDATES`; §10.1-чтение «primary candidate» = execution candidate (B2, конфликт D); §15–§17 → таксономия v1.1 §17.3 без `recommendation.accepted` (B8); §22 `expires_at` → `actionable_until` + ссылка на retention policy (B13); §7/§25 → три логических снимка (B10); §17/§22 → инвариант D4 (`MATERIAL_CHANGE`).
- **A3 к Intent Model Specification** (additive, минимальный): подтверждение, что `CHOOSE_MANY` живёт downstream от resolver'а и Output Contract 0.5 не меняется; исправить метаданные `intent-registry.yaml` / `intent-output.schema.json` («v1.0, draft / proposed / candidate» при `approved` у .md).
- **A4 к UX Addendum** → v0.2 «C04/C05 Presentation Constraints» (B3, B4): поля C04 (направление + WHY + действия) vs C05 (услуга, мастер, цена, слот); C04.3 — по действию, не автоматически; коды состояний §5 + `NO_VERIFIED_CANDIDATES`, `INSUFFICIENT_CONTEXT`; §3 события по таксономии v1.1; OQ-REC-1 resolved, OQ-REC-4 закрыт «на C05», OQ-REC-2 закрыт B13 (actionability 2 ч, retention отдельно), OQ-REC-3/5/6/7 — в реестр DRF-1349 или закрыть.

### 6.3 Архив / superseded

- `05 Architecture/ADR-0013 Recommendation Snapshot.md` — `superseded_by` контракт v1.0 §7/§25 + канон v1.1 Decision 7 (B10); Open Questions ADR 1–5 переносятся в контракт.
- `01 Product/UX MVP/reviews/recon-recommendation-contract-001.md`, `recommendation-owner-review-001.md` — архив (действие 1 выполнено v0.4; остальное — A4).
- `05 Architecture/Ayla Goal Outcome Semantic Model Working Design.md` — после A1 остаётся non-canonical evidence base для Goal/Outcome Taxonomy Design (WD §23) с шапкой «дельты §20 применены amendment A1».
- `approved_v1_1.md` (корень `ayla-knowledge`) — **в явно обозначенную history/archive area** (B14), например `01 Product/User Journeys/history/`, чтобы имя не читалось как «канон v1.1».
- `UX Agents/planning/BOT-003-canon-reconciliation.md`, `UX Agents/reports/BOT-001-reconciliation-report.md` — остаются как отчёты.

### 6.4 Что не трогать

Intent Resolution Output Contract 0.5, 11 intent types + `UNKNOWN`, 18 слотов — без изменений (WD §19). Killer PRD §5 — отдельная правка OQ-R12, не в этом пакете. `docs/ayla-conversation-state-v1.1-reconciled.md` — не переносится и не переименовывается (B1).

### 6.5 Порядок ходов

```text
Владелец утверждает этот документ (v1.0)
        ↓
A1 + A2 готовятся как diff к контракту v0.4 (инженерия; Output Contract 0.5 не меняется)
        ↓
Контракт v0.4 → v1.0 approved  ──►  BOT-003 candidate → approved
        ↓                              ↓
ADR-0013 → superseded (B10)     UX Addendum → v0.2 (A4)
        ↓
Domain Event Registry: таксономия v1.1 §17.3 без recommendation.accepted (B8) + publication matrix §15
        ↓
Этот документ → ayla-knowledge как approved reconciliation
        ↓
approved_v1_1.md → history (B14)
        ↓
Slice §7: VERIFIED для строк 1, 2, 3, 7 — владелец лично (B11, B12, E1) → флаг полки
```

Правила порядка: ни один ход не запускается «временно» без утверждённого предыдущего; Output Contract 0.5 не меняется ни одним ходом; матрица safety §16.2 не входит в порядок — она блокирует выход slice к пользователям, но не канонизацию документов; её отсутствие называется в контракте v1.0 как открытый вход (`RequiredContextSpec` для `owner = SAFETY`) с правилом B6 до её появления.

---

## 7. Controlled Recommendation Slice первой волны (B11)

Состав по B11 (а): строки **1, 2, 3, 7** черновика §7 + **9** как boundary-control. Владелец: «пилот доказывает полный вертикальный путь, не breadth». Строки 4, 5, 6, 8 черновика — **после первой волны**.

Правила покрытия (E1): coverage driven by scenarios — `pilot scenarios → required capabilities → required canonical services → required tenant offers → human VERIFIED`. Владелец лично утверждает mapping только pilot slice, не все 58 услуг formula-tela (E1, B12); остальные — позже пакетно. Eligibility только `VERIFIED` (C2). Canonical service — по `djangoproject/services/seeds/canonical_catalog_2026-07.csv` (колонки `code`, `service`, `requires_health_check`); коды desired outcome — рабочие, из WD §12–§13 (OQ-GO-4/5 открыты); families — provisional (B9).

### 7.1 Вертикальная цепочка по строкам

| # | User need (дословно) | Desired outcome (рабочие коды) | Safety (слой 6) / DecisionReadiness (слой 7) | NBA (WHAT) | Capability (HOW) | Canonical service (код, `requires_health_check`) → tenant offer formula-tela | VERIFIED |
|---|---|---|---|---|---|---|---|
| 1 | «Хочу выглядеть свежее» (чип C01) | `IMPROVE(FRESH_APPEARANCE)`; scope: лицо (по умолчанию не известно) | Safety `NORMAL`; `NEEDS_DISCRIMINATION` (лицо / общее состояние) либо `DISCOVERY_REQUIRED` при broad aspiration (GO2-W1) | `ADDRESS(FRESH_APPEARANCE)` | быстрый уход/тонизирование кожи лица; лимфодренаж лица | 4.3.24 Экспресс-уход (false); 4.3.25 Уход «сияние кожи» (false); 1.4.4 Лимфодренажный массаж лица (false) → offers formula-tela по этим кодам | владелец лично (B12) |
| 2 | «Беспокоят отёки» (чип C01) | `REDUCE(PUFFINESS)`; scope неизвестен (лицо / ноги) | **Safety `CLARIFY` fail-closed (B6)**: отёки — потенциально медицинский смысл; один decision-changing safety-вопрос; до ответа NBA не формируется; после `NORMAL/CAUTION` → `NEEDS_DISCRIMINATION` (где отёки, когда заметнее — макет C03) | `ADDRESS(PUFFINESS)` | лимфодренаж (лицо/тело/ноги) | 1.4.4 Лимфодренажный массаж лица (false); 1.4.2 Лимфодренажный массаж ног (false); 1.3.22 Массаж при отечности (false); 4.1.12 Консультация по отечности лица (false) | владелец лично |
| 3 | «Хочу снять напряжение» (чип C01) | `REDUCE(MUSCLE_TENSION)` и/или `IMPROVE(RELAXATION)` | Safety `NORMAL`; `NEEDS_DISCRIMINATION` (мышечное vs эмоциональное; зона) | `ADDRESS(MUSCLE_TENSION)` / `SUPPORT(RELAXATION)` | расслабляющий / антистресс массаж; ШВЗ | 1.2.6 Массаж для снятия мышечного напряжения (false); 1.1.5 Массаж шейно-воротниковой зоны (false); 1.2.2 Антистресс-массаж (false); 1.2.1 Relax-массаж (false) | владелец лично |
| 7 | «Ноет спина после работы» (сценарий владельца) | `REDUCE(MUSCLE_TENSION)`, `body_area = BACK`; context: «после длительной работы за столом» (WD §15) | **Safety `CLARIFY` fail-closed (B6)**: боль — сигнал; один safety-вопрос; после `NORMAL/CAUTION` → `READY` или `NEEDS_DISCRIMINATION` (зона спины); при `STOP` — `SAFETY_BOUNDARY` | `ADDRESS(MUSCLE_TENSION, BACK)` | массаж спины при сидячей работе | 1.1.4 Массаж спины (false); 1.3.10 Массаж при сидячем образе жизни (false); 1.3.11 Массаж для офисных сотрудников (false); 1.3.9 Массаж при мышечном напряжении (false); **1.3.24 Массаж при болях в спине (true → §98: запись не создаётся, к человеку)** | владелец лично |
| 9 | «Запиши меня на массаж спины к Анне» (канон v1.1 §19.6) — boundary-control | не рекомендация: `BOOK_APPOINTMENT` по precedence Intent Model | — (EXECUTION mode); медгейт §98 на записи действует | — | — | 1.1.4 Массаж спины (false) через Offer Resolution; **без VERIFIED — direct booking допустим при остальных gates (C2)** | не требуется для direct booking |

Строки 4, 5, 6, 8 черновика («Последнее время сильно устаю», «Хочу больше времени уделять себе», «Готовлюсь к важному событию», «Не знаю, с чего начать») — после первой волны; их описание в черновике §7 сохраняет силу как заготовка.

### 7.2 Проверки, которые slice обязан пройти «глазами»

| # | Проверка | Строка | Что доказывает |
|---|---|---|---|
| S1 | Чип C01 и та же фраза текстом дают один `SemanticResolutionResult` и одну карточку | 1, 2, 3 | единый semantic pipeline (OD-C01-3), не hardcoded путь чип → услуга |
| S2 | При `NO_VERIFIED_CANDIDATES` карточка «Ayla рекомендует» не рендерится; показывается честное состояние с `Посмотреть услуги` / `Уточнить запрос` | любая | §76/C2 без fallback; термин зарезервирован (пакет 12.09 §3) |
| S3 | Направление рекомендовано, но единственная VERIFIED-услуга имеет `requires_health_check = true` → в C05 человек уходит к оператору, запись не создаётся, `HEALTH_CHECK_*` ≠ `BOOKING_ERROR` | 7 | два гейта (конфликт A), §98 |
| S4 | WHY содержит только фразы, произнесённые в этом разговоре; при отсутствии displayable-причины карточки нет | 1, 2, 3, 7 | owner 24.08 + owner 2026-07-29 |
| S5 | Изменение цены/слота после показа не меняет `recommendation_id` и направление; на записи revalidate именно подтверждённую опцию; расхождение (60 мин / 1500 ₽ ↔ 45 мин / другая цена) → `MATERIAL_CHANGE` → новое подтверждение, не silent normalization | 3, 7 | R-NBA-3; канон v1.1 §10.3; **D4** |
| S6 | `Другой вариант` создаёт R2 с `parent_recommendation_id = R1`; бронирование по R2 атрибутируется R2, R1 — assisted; **C04.3 не показывается без действия пользователя** | 3 | канон v1.1 §10.2, §17.6; **B4** |
| S7 | На C04 нет услуги, мастера, цены, слота; они появляются только на C05 после `Подобрать вариант` | 1, 2, 3, 7 | **B3** |
| S8 | «Запиши меня на массаж спины к Анне» не проходит через Recommendation; `BOOK_APPOINTMENT` → EXECUTION; услуга без VERIFIED записывается напрямую при остальных gates | 9 | Intent Model precedence; разбор §15; **C2** |
| S9 | Отёки / боль в спине: до ответа на один safety-вопрос карточка не формируется; движок не задаёт второй safety-вопрос подряд | 2, 7 | **B6**; DRE `MAX_CONSECUTIVE_ASKS_WITHOUT_NEW_EVIDENCE = 2` (§16.1) |
| S10 | Рекомендация формируется без Goal; «Создать цель» доступно отдельно и не требуется для карточки | 1, 3 | **B5** |
| S11 | Через 2 ч после показа контекст не продолжается напрямую, но `recommendation_id` и цепочка `Recommendation → PendingBookingIntent → Booking` доказуемы | 3, 7 | **B13**; канон v1.1 Decision 1, §17.6 |
| S12 | Shadow mode DRE: движок считает `readiness_state` и `question_id`, но пользователю не задаёт; результат пишется для таблицы «при τ=X спрашивали бы в N%» | все | **C1** |

Критерии готовности slice (Stage 2 gate из пакета 12.09 §3 как «как», не как «объём»): `VERIFIED > 0` по каждой из строк 1, 2, 3, 7 (владелец лично, B12); candidate-level Safety с правилом B6; единственный Recommendation Authority; grounded WHY; честные empty states (`NO_VERIFIED_CANDIDATES`, `INSUFFICIENT_CONTEXT`, `SAFETY_BOUNDARY`); `recommendation_id` attribution по provenance chain; проверки S1–S12 пройдены.

---

## 8. Что остаётся открытым

| # | Вопрос | Кто / как закрывается | Правило до закрытия |
|---|---|---|---|
| O1 | Матрица safety-сигналов (`docs/specs/DECISION_READINESS_ENGINE_v1.0.md` §16.2: «Содержимое `RequiredContextSpec` для `owner = SAFETY` — UNKNOWN») | **C3**: черновик от окна идентичности/безопасности в формате `signal → evidence required → severity/context → NORMAL/CLARIFY/CAUTION/STOP → allowed capabilities → required question / handoff`; утверждает владелец | **B6**: `CLARIFY` fail-closed для затронутой capability |
| O2 | Retention policy для immutable Recommendation record — число лет | legal verification (B13: «по отдельной retention policy»); ориентир из пакета 2 — D7/D8 «5 лет — product retention decision до отдельной legal verification» для других записей, на Recommendation не распространён | запись не удаляется по истечении 2 ч; retention — политика, не поле |
| O3 | Пороги DRE `tau_separation`, `N_broad` после shadow mode | **C1**: shadow mode включён; через неделю таблица «при τ=X спрашивали бы в N%» на утверждение владельцу (DRF-1519, DRE §16.1 «Не выдумывается здесь») | shadow mode: движок считает, не управляет |

Не в этом пакете (без изменения статуса): терминология `DesiredOutcome` (OQ-GO-1), постоянство NBA taxonomy после пилота (B9 provisional; OQ-R11/OQ-GO-9), числовые окна attribution (Measurement Framework), TTL suppression (OQ-REC-3), Killer PRD §5 (OQ-R12), строки slice 4, 5, 6, 8 (после первой волны).

---

## 9. Пределы

### 9.1 Что прочитано целиком для этой редакции

Черновик (405 строк); пакет 2 `docs/OWNER_DECISIONS_2026-09-12_PACKAGE2.md`; доктрина `docs/OWNER_DOCTRINE_MOCKUPS_ARE_CANON_2026-09-12.md`; `docs/OWNER_QUESTIONS_2026-09-12.md` §C–§E (формулировки C1–C3, D4, E1–E3); `docs/specs/DECISION_READINESS_ENGINE_v1.0.md` §16.1–§16.2, §17.1.

### 9.2 Что унаследовано от черновика без повторного чтения

Цитаты и пути источников `ayla-knowledge` (Intent Model, контракт v0.4, WD v0.9, ADR-0013, BOT-003, UX Addendum, reviews, BOT-003-canon-reconciliation, `approved_v1_1.md`), канон v1.1 (`docs/ayla-conversation-state-v1.1-reconciled.md`), `docs/OPEN_DECISIONS.md` §76/§98/§105/§145, коды канонического каталога из `canonical_catalog_2026-07.csv`, тексты чипов из `quick_actions.py:96-121` — взяты из черновика §2–§7 как есть. Пределы чтения черновика (§9.1–§9.4 черновика: частичное чтение Journey v1.1 и канона v1.1, копия OPEN_DECISIONS из worktree, непроверенные исходники `anketa.py`/`health_screening`, непроверенные статусы `approved`/`VERIFIED` в БД пилота) сохраняются.

### 9.3 Что этот документ не решает

O1–O3 (§8); состав NBA taxonomy после пилота; содержимое amendment A1/A2 как diff (готовит инженерия после утверждения); фактическое наличие VERIFIED-связей у formula-tela по кодам §7.1 (владелец исполняет по E1); соответствие живого кода пилота слоям §2 (карта разрывов C03 → C02/C04/C05 по доктрине 12.09 — отдельный результат).
