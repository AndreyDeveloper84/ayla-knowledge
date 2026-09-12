---
node_id: ayla.ux.recommendation-ux-addendum
task_id: UX-MERGE-001
title: Recommendation UX Addendum
type: specification
status: review
decision_status: proposed
canonical_status: candidate
version: "0.2"
owner: UX Architecture
priority: P0
knowledge_area:
  - product
domain:
  - recommendation
concerns:
  - explainability
  - safety
system_owner:
  - ayla-recommendation
source_repository: ayla-knowledge
source_kind: product-requirements
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
created: 2026-07-29
updated: 2026-09-12
review_cycle: monthly
prepared_by: UX-документалист (UX-MERGE-001)
basis: UX-GAP-0104
depends_on:
  - "[[Ayla MVP Recommendation Contract]]"
related:
  - "[[Ayla MVP User Journey Specification]]"
  - "[[Recommendation Architecture Final Reconciliation]]"
unblocks:
  - SCR-CUST-004 (recommendation card)
  - SCR-CUST-005 (no-recommendation)
  - SCR-CUST-006 (slot picker)
scope: MVP Phase 1 (session-only, no proactive)
note: >
  Не контракт. UX-facing presentation constraints C04/C05 к proposed contract
  v1.0 (Ayla MVP Recommendation Contract, owner Product Architecture). Не
  source of truth для recommendation-правил.
---

# Recommendation UX Addendum — C04/C05 Presentation Constraints

> **Статус документа: PROPOSED v0.2 — awaiting owner approval** (amendment
> **A4**, Final Reconciliation v1.0 §6.2; пакет 2 от 12.09.2026: **B3, B4**;
> утверждает владелец, F3). Это **не контракт** и **не source of truth** для
> recommendation-правил. Источник доменной семантики — **Ayla MVP
> Recommendation Contract v1.0 (proposed)** (`05 Architecture/`, далее
> «контракт», owner Product Architecture). Этот addendum фиксирует только
> **presentation constraints** — что и на каком экране показывается — в
> тройном разделении владельца: **WHAT** (Recommendation = NBA, экран C04)
> → **HOW** (Execution Mapping, экран C05) → **WHO** (Provider, экран C05).
> Слова владельца, которые нельзя исказить: «Ayla Recommendation это NBA /
> WHAT, service/master — execution / HOW+WHO» (B2/B3).
>
> Что изменилось относительно v0.1 (2026-07-29): карточка C04 **больше не
> несёт** услугу, мастера, цену и слот — они на C05 (конфликт 1 Final
> Reconciliation §4, закрыт B3); альтернативы открываются действием (B4);
> события — по таксономии канона v1.1 §17.3 без `recommendation.accepted`
> (B8); коды состояний дополнены `NO_VERIFIED_CANDIDATES` и
> `INSUFFICIENT_CONTEXT`; OQ-REC-1/2/4 закрыты. Где v1.0 молчит
> (suppression N9, deep-link persistence, `linkage_type`), текст v0.1
> сохранён.
>
> Пометки: *(факт — источник)*; **(proposal)** — предложение, не
> зафиксированное в источниках; «контракт §N» — раздел Ayla MVP
> Recommendation Contract v1.0 (proposed); «v0.1: …» — история.

## 1. WHAT → HOW → WHO: что показывает C04, что — C05

Доменная семантика — в контракте, здесь не дублируется:

- Идентичность `recommendation_id` (immutable record, RecommendationSet,
  `presentation_version`) — **контракт §3–4**; запись переживает 2-часовой
  TTL контекста (B13, контракт §22).
- Composition: ≤1 primary + ≤2 alternatives, не каталог — **контракт
  §9–10**.
- Immutable snapshots (три: Decision / Execution Mapping / Transaction),
  pipeline, eligibility — **контракт §5, §7–8**; кандидат, исключённый на
  любом этапе, не возвращается (факт — Killer PRD §5.1; контракт §8).

### 1.1 C04 — WHAT + WHY (карточка направления, макеты C04.1–C04.6)

| Поле / действие | Статус | Основание |
|---|---|---|
| `recommendation_id` | обязателен (факт) | контракт §3–4; Scope Contract §4.1 п. 11 |
| **направление** — Canonical NBA (`family`, `target`, `target_outcomes`) в формулировке для человека | обязателен | контракт §3, §33, §34; **B2, B3** |
| **WHY** — displayable-объяснение (§2), только grounded-пересказ того, что человек сказал в этом разговоре | обязателен | контракт §13; owner ruling 2026-07-29; owner 24.08 (`docs/OD_C04_GROUNDED_WHY.md`) |
| действия: `Подобрать вариант` (→ C05), `Почему` (→ C04.2 / `explanation_requested`), `Другой вариант` (→ C04.3 / `alternative_requested`) | обязательны | Final Reconciliation §2 слой 10; **B4** |
| ~~услуга (service)~~ | **не показывается на C04** | **B3**: «услуга, мастер, цена, слот — в C05 после перехода к execution mapping» (v0.1: обязателен — снято) |
| ~~специалист / салон (provider)~~ | **не показывается на C04** | B3 (v0.1: обязателен, если применим — снято) |
| ~~цена, длительность, ближайший слот~~ | **не показываются на C04** | B3; OQ-REC-4 закрыт ответом «не на C04» (v0.1: proposal — снято) |

Правила C04:

- карточка — про **одно направление**; альтернативы (C04.3, ≤2, radio)
  **не показываются автоматически** — пользователь открывает их действием
  `Другой вариант` (**B4** «с уточнением»: «„Другой вариант“ доступен
  всегда после primary; список альтернатив НЕ показывается автоматически»);
- карточка рендерится только из полей, переданных Recommendation
  Composer; UX не обогащает её данными execution-слоя **(proposal, v0.1
  сохранён)**;
- нет displayable WHY → карточки нет (§2).

### 1.2 C05 — HOW + WHO (execution options: услуга, мастер, цена, слот)

| Поле | Статус | Основание |
|---|---|---|
| execution option (`SERVICE_PATH` → конкретная **услуга** VERIFIED-канона у тенанта) | обязателен для `SERVICE_PATH` | контракт §8, §34; **C2** (только `mapping_status = VERIFIED`) |
| **мастер / салон** (provider) | обязателен, если применим | контракт §8 (staged ranking); Killer PRD §5.3 tie-breaker |
| **цена, длительность** | обязательны как показанные значения | они и есть *exact client-confirmed execution option* — при записи revalidate именно их; расхождение → `MATERIAL_CHANGE` → новое подтверждение (**D4**; контракт §22) |
| **слот** (nearest available / выбранный) | обязателен на slot picker (SCR-CUST-006) | displayed slot ≠ reservation; проверяется при commit (UJS этап 10; контракт §22) |
| `distance_meters` | если есть точка клиента и подтверждённое место мастера; иначе `null` = неизвестно, не «далеко» | пакет 12.09 §3; D3 (геолокация — contextual consent «Показать рядом со мной») |
| `requires_health_check` исполнения | показывается честно: `True`/`UNKNOWN` → запись уходит к человеку, не `BOOKING_ERROR` | контракт §23 (два гейта); `docs/OPEN_DECISIONS.md` §98 |

Правило C05: показанное на C05 **фиксируется** в `PendingBookingIntent`
как та execution option, которую клиент видел и подтвердил (D4); C05 не
переписывает направление C04 — недоступность исполнения раскрывается
честно как execution feasibility outcome (контракт §11, §34).

## 2. Explanation rule (displayable)

- Объяснение «почему эта рекомендация» — обязательная capability MVP
  (факт — Scope Contract §4.1 п. 9; Конституция Ст. VII). Контракт объяснения
  (производная от ranking, запреты) — **CANON §13**.
- **Классификация объяснений (принято owner 2026-07-29):** каждое объяснение
  классифицируется как **displayable** (разрешено показать пользователю) или
  **internal-only** (внутренние сигналы, персональные данные, раскрытие
  ranking или provider score — показ запрещён). Explanation может существовать
  в системе, но быть internal-only.
- Правило **«нет displayable объяснения → не показываем»** (no displayable
  explanation → no show) **принято owner 2026-07-29** и действует здесь как
  UX-норма: если Composer не вернул displayable-объяснение (включая
  redacted-вариант только по разрешённым фактам), UX не рендерит карточку и
  переводит сценарий в состояние no-recommendation (SCR-CUST-005).
  Перенесено в контракт §13 (v0.4) — действие 1 recon выполнено; здесь
  остаётся как UX-норма со ссылкой. WHY на C04 — только grounded-пересказ
  разговора (owner 24.08); нет displayable → no-recommendation.
- Открытым остаётся вопрос владельца классификатора displayable vs
  internal-only (предложение — Safety/Trust + Recommendation) → OQ-REC-6.

## 3. UX view-model lifecycle и suppression

**UX view-model (не контрактная модель):** `created → shown → engaged |
rejected | expired | invalidated` — представление для экранов (v0.1:
`accepted | declined` — снято, **B8**). Контрактная модель — **контракт
§14**: decision state — projection (`active | superseded | expired |
invalidated`); реакции `WHY_REQUESTED / ALTERNATIVE_REQUESTED / ENGAGED /
REJECTED / CONSTRAINT_ADDED` — interaction facts, не состояния (канон
v1.1 §10.3; контракт §17). `Посмотреть варианты` = `ENGAGED`, не
доказанное принятие.

- **Expiry/TTL:** определены в **контракте §22** — `actionable_until`
  (= 2 ч ConversationState / active recommendation context), read/action
  gate. **OQ-REC-2 закрыт (B13):** actionability — 2 ч сессии; immutable
  Recommendation record хранится дольше по отдельной retention policy —
  через два часа контекст не продолжается напрямую, но `recommendation_id`
  и цепочка до Booking доказуемы. UX не трактует «истёк контекст» как
  «записи нет». Частные случаи invalidation: `integrity_invalidated`
  при post-display нарушении economic-neutrality — рекомендация не может
  продолжать recommendation-derived flow (факт — Killer PRD §5.3; политика —
  CANON §11; UX-статус — §5); недоступность специалиста/слота после показа —
  честное сообщение + alternative (факт — N5, этап 10; CANON §10, §22).
- **События:** одна таксономия — канон v1.1 §17.3, publication matrix —
  **контракт §15**: `recommendation.created / presented /
  explanation_requested / alternative_requested / engaged` +
  `booking_intent.created`; `qualified_action.attributed` (owner
  Attribution/Measurement, только по provenance chain). **`recommendation.
  accepted` не вводится, `recommendation.declined` снято (B8)**;
  `recommendation.generated` отклонён. Экспозиция/CTR считаются от
  `presented`, не от `created` (канон v1.1 §17.5). Имена Roadmap §6.4
  (`RecommendationShown`, `RecommendationAccepted`,
  `QualifiedActionAttributed`) — справочные, синхронизируются при
  регистрации в Domain Event Registry (OQ-REC-5 → реестр DRF-1349).
  Analytics (informative): `recommendation_created`,
  `recommendation_explanation_rendered`, `recommendation_dismissed` (факт
  — CSR §9.2).
- **Suppression после отказа (N9, UX-норма):** после первого отклонения —
  alternative в пределах лимита (≤2, условия — CANON §10). После повторного
  или явно жёсткого отказа дальнейшие предложения подавляются: жёсткий отказ
  («не напоминай») — блокировка **без `reconsider_after`**; мягкий —
  нейтральное acknowledgement без CTA (факт — UJS этап 9, N9). TTL suppression
  для мягкого отказа источниками не задан → OQ-REC-3.
- Отклонённая (`REJECTED`) или invalidated рекомендация не получает
  атрибуцию (факт — Killer PRD §6.2, §5.3; контракт §17–18).

## 4. Attribution — UX-требования

Доменная семантика — в контракте, здесь не дублируется: qualified action,
single-winner, `direct | assisted | unattributed`, обязательные ссылки —
**контракт §15, §18, §20**; attribution window — **контракт §19** (окна
принадлежат Measurement Framework / Window Registry, контракт хранит
`policy_version`). Provenance chain `Recommendation → PendingBookingIntent
→ Booking` — единственное основание атрибуции (канон v1.1 §17.6).

UX-слой:

- **Deep-link persistence (UX-OD-004):** `recommendation_id` сохраняется через
  весь booking flow, включая deep link bot DM → Mini App (contextual deep
  link, не generic home). Booking без `recommendation_id` — `unattributed`
  (факт — Killer PRD §6.2; контракт §18). Гарантии доставки и срок жизни
  `recommendation_id` в Mini App поверх UX-OD-004 → OQ-REC-7.
- Для метрики `booking_from_recommendation` UX передаёт: `recommendation_id`,
  `attribution_type`, `linkage_type`, timestamps в UTC, `scenario_type`; для
  alternative — дополнительно `parent_recommendation_id`,
  `recommendation_role=alternative`, `rerank_reason` (факт — Killer PRD
  §6.1–6.3).
- **`linkage_type`** — допустимые значения: `inline_accept`,
  `recommendation_deeplink`, `derived_booking_draft`,
  `saved_recommendation_return`, `explicit_recall`, `alternative_accept`
  (факт — Killer PRD §6.1–6.3). **Пометка:** перечень остаётся UX-перечнем
  до owner decision — куда переносится (контракт §18, Attribution/Measurement
  spec или остаётся здесь): recon, действие 3, строка 10 матрицы. *v1.0
  молчит — оставлено как было.*

## 5. Empty / blocked states — UX-коды и гарантии для UX

| Состояние | Код | Гарантия для UX | Основание |
|---|---|---|---|
| Нет подтверждённых услуг под направление (SCR-CUST-005) | **`NO_VERIFIED_CANDIDATES`** (v0.2) | Штатное состояние с именем, не поломка: карточка «Ayla рекомендует» не рендерится; показывается честное состояние с `Посмотреть услуги` / `Уточнить запрос`; каталог, поиск и прямая запись остаются доступны | **C2**; `docs/OPEN_DECISIONS.md` §76; контракт §8; Final Reconciliation §7.2 S2 |
| Не хватает контекста для ответственной рекомендации | **`INSUFFICIENT_CONTEXT`** (v0.2) | Не карточка, а один вопрос C03 (или честное «пока не могу»); вопрос только если ответ меняет решение; повторный вопрос об известном не задаётся | контракт §30 (DecisionReadiness), §32; B5; доктрина 12.09 |
| Нет кандидатов на исполнение (после C04, на C05) | `NO_CANDIDATES` | Execution-stage исход: направление остаётся, вариантов исполнения нет — честное раскрытие, не подмена NBA; доступен обычный поиск/запись | контракт §8, §11, §34; Killer PRD §5.3 Fallback; N3 |
| Нет displayable объяснения | `NO_DISPLAYABLE_EXPLANATION` | Объяснение отсутствует или классифицировано internal-only → карточка не рендерится, перевод в SCR-CUST-005; UX не показывает internal-only содержимое ни в каком виде | правило §2, принято owner 2026-07-29; перенос в CANON §13 — recon, действие 1 |
| Специалист недоступен | `PROVIDER_INELIGIBLE` | Кандидат исключается до показа; если недоступность выявлена после показа — честное сообщение + alternative **с объяснением замены (proposal в источнике)** | факт — N5; Killer PRD §5.1; CANON §8, §10 |
| Safety-блокировка | `SAFETY_BLOCKED` (= `SAFETY_BOUNDARY` контракта §32) | Отдельный статус, **не** no-recommendation: boundary message без CTA на заблокированную услугу; безопасная альтернатива — только после Boundary Handling (S8) | факт — N8; Killer PRD §5.1 этап 2; контракт §23 |
| Safety `CLARIFY` (до матрицы сигналов) | `SAFETY_CLARIFY` **(proposal, имя кода — при регистрации)** | Один decision-changing safety-вопрос; до ответа карточки нет (потенциально медицинский смысл fail-closes capability) | **B6**; контракт §23; C3 (матрица — открыта) |
| Исполнение требует человека | `HEALTH_CHECK_*` (не `BOOKING_ERROR`) | На C05 честно: направление рекомендовано, запись по этой услуге создаётся через оператора | контракт §23 (два гейта); §98; Final Reconciliation §7.2 S3 |
| Расхождение показанного и применяемого при записи | `MATERIAL_CHANGE` (каталог: `QUOTE_CHANGED`, `SLOT_UNAVAILABLE`) | Показать обе пары значений и переспросить; запись не создаётся молча с другой ценой/длительностью/слотом | **D4**; контракт §22 |
| Economic-neutrality alert | `ranking_economic_neutrality_alert` | Не user-facing ошибка; выдача персонализированной primary блокируется, обычный поиск/запись сохраняются | факт — Killer PRD §5.3; UJS этап 7; политика — CANON §11 (handling CANON не фиксирует — конфликт C5 минорный, owner confirm при переносе) |
| Нет слотов после `ENGAGED` | `NO_AVAILABLE_SLOTS` | Переход к SCR-CUST-006 с состоянием slot unavailable + альтернатива (другое время; другой мастер — только в initial booking; в reschedule альтернатива мастера — W2, UX-OD-001) | факт — N4, этап 10; контракт §22 (revalidation), §10; уточнение области — UX-OD-001 |

Дополнительно для SCR-CUST-006 (slot picker): displayed slot не является
reservation; доступность перепроверяется при commit booking (факт — UJS
этап 10; контракт §22). Формат: bot DM — compact, Mini App — expanded
(UX-OD-004).

## 6. Out of scope (Phase 1)

- Proactive recommendations — Phase 1 работает в режиме no proactive
  (факт — CSR §10); scope `proactive_recommendation` — `blocked`
  (факт — CSR §5.3). Уведомления — только транзакционные по записи.
- Cross-domain персонализация (scope `cross_domain_personalization`)
  — MVP status `blocked`, consent model не утверждена (факт — CSR §5.4).
- Персонализация на persistent memory — Phase 1 session-only (UX-OD-003;
  факт — CSR §5.7, §10; влияние memory на recommendation — CANON §6).
- Ranking-политика, tie-breaker, scoring, economic neutrality как ranking
  constraint — **контракт §11** и Recommendation Engine Specification
  (owner Recommendation); этот addendum ranking не определяет.
- Роль retrieved memory в candidate generation / ranking / explanation
  (UJS OQ №11) — upstream, owner контракта (§6).

## 7. Open Questions

Статусы по состоянию на 2026-09-12 (A4; Final Reconciliation v1.0 §6.2):

1. **OQ-REC-1 — RESOLVED (owner 2026-07-29).** «Нет displayable объяснения
   → не показываем»; перенесено в контракт §13 (v0.4).
2. **OQ-REC-2 — CLOSED (B13).** Actionability — 2 ч ConversationState /
   active recommendation context (`actionable_until`, контракт §22);
   запись immutable, хранится по отдельной retention policy. Число лет —
   не вопрос UX (Final Reconciliation §8 O2).
3. **OQ-REC-3 — в реестр DRF-1349.** TTL suppression после мягкого отказа
   (жёсткий — блокировка без `reconsider_after`, факт). v1.0 молчит; норма
   N9 сохраняется как есть.
4. **OQ-REC-4 — CLOSED (B3).** Цена / длительность / ближайший слот **не на
   C04**; на C05 — по данным TenantOffer как exact client-confirmed
   execution option (D4).
5. **OQ-REC-5 — в реестр DRF-1349.** Синхронизация имён Roadmap §6.4 с
   publication matrix контракта §15 при регистрации в Domain Event
   Registry; сама таксономия закрыта (B8).
6. **OQ-REC-6 — в реестр DRF-1349.** Владелец классификации displayable vs
   internal-only. v1.0 молчит.
7. **OQ-REC-7 — в реестр DRF-1349.** Deep-link-контракт bot DM → Mini App
   поверх UX-OD-004. v1.0 молчит.

## 8. Acceptance Criteria

1. SCR-CUST-004 (C04) рендерит карточку только при наличии
   `recommendation_id` (контракт §3–4) и displayable WHY (§2); карточка
   несёт **направление + WHY + действия** и **не несёт** услугу, мастера,
   цену, слот (B3); при отсутствии displayable объяснения — переход в
   SCR-CUST-005.
2. Одновременно показывается ≤1 primary; ≤2 alternative открываются
   **только действием** `Другой вариант` (B4; контракт §9–10); alternative
   несёт собственный `recommendation_id` и `parent_recommendation_id`.
3. SCR-CUST-005 корректно различает `NO_VERIFIED_CANDIDATES`,
   `INSUFFICIENT_CONTEXT`, `NO_CANDIDATES`, `NO_DISPLAYABLE_EXPLANATION`,
   `PROVIDER_INELIGIBLE`, `SAFETY_BLOCKED` (тексты/CTA по §5; при
   `NO_VERIFIED_CANDIDATES` карточка «Ayla рекомендует» не показывается,
   каталог/поиск доступны — C2).
3a. C05 показывает услугу, мастера, цену, длительность, слот только для
   VERIFIED-исполнения (C2); показанные значения фиксируются в
   `PendingBookingIntent`; расхождение при записи → `MATERIAL_CHANGE` и
   новое подтверждение, не молчаливая запись (D4).
4. SCR-CUST-006 получает `recommendation_id` неизменным из карточки и
   передаёт его в booking creation; deep link в Mini App сохраняет
   `recommendation_id` (UX-OD-004, §4).
5. После жёсткого отказа UX не инициирует повторных предложений; после
   мягкого — нейтральное acknowledgement без CTA (до решения OQ-REC-3 —
   в пределах сессии).
6. Ни одно UX-состояние не показывает proactive или persistent-memory
   персонализацию (Phase 1).
7. Все acceptance-тесты трассируются к источникам; поля без источника помечены
   (proposal) и покрыты соответствующим OQ.

## Источники

- **Контракт:** Ayla MVP Recommendation Contract v1.0 (proposed) — §3–5,
  §7–11, §13–15, §17–20, §22–23, §30–34
  (`05 Architecture/Ayla MVP Recommendation Contract.md`; SRC-16)
- Final Reconciliation v1.0 (`docs/RECOMMENDATION_ARCHITECTURE_FINAL_RECONCILIATION_v1.0_2026-09-12.md`;
  копия — [[Recommendation Architecture Final Reconciliation]]) §2, §4, §6.2 (A4), §7.2
- Пакет 2 решений владельца 12.09.2026 (`docs/OWNER_DECISIONS_2026-09-12_PACKAGE2.md`): B2, B3, B4, B6, B8, B13, C2, D3, D4
- Макеты C04.1–C04.6, C05 (по `docs/RECONCILIATION_C01_C05_MOCKUPS_VS_RUNTIME_2026-09-12.md` §4; доктрина «макеты — канон» 12.09)
- Reconciliation: `reviews/recon-recommendation-contract-001.md` (UX-RECON-001,
  вариант B, конфликты C1–C5)
- UJS MVP: этапы 6–9, N3/N4/N5/N8/N9, §Recommendation and Proactivity Gates,
  OQ №4, №8, №11 (`01 Product/User Journeys/Ayla MVP User Journey Specification.md`)
- Intent Model: §Outputs, §Output Contract, §Confidence and Clarification
  (`03 AI System/Ayla Intent Model Specification.md`)
- Killer PRD: §5.1–5.3, §6.1–6.3 (`02 Strategy/Killer PRD.md`)
- Consent Scope Registry: §5.3, §5.4, §5.7, §9.2, §10
  (`06 Safety and Governance/Consent Scope Registry.md`)
- MVP Scope and Release Contract: §4.1 п. 2, 9, 11 (`02 Strategy/Ayla MVP
  Scope and Release Contract.md`)

## Changelog

- 2026-09-12 — **v0.2 PROPOSED (A4, awaiting owner approval).** Переписан
  под тройное разделение WHAT (C04) → HOW (C05) → WHO (C05): §1 разделён на
  C04 (направление + WHY + действия; услуга/мастер/цена/слот сняты — **B3**)
  и C05 (execution options; exact client-confirmed option — **D4**);
  альтернативы по действию (**B4**); §3 view-model и события — по канону
  v1.1 §17.3 без `accepted`/`declined` (**B8**), TTL → `actionable_until`
  (**B13**); §5 — добавлены `NO_VERIFIED_CANDIDATES` (**C2**),
  `INSUFFICIENT_CONTEXT`, `SAFETY_CLARIFY` (proposal, **B6**),
  `HEALTH_CHECK_*` (§98), `MATERIAL_CHANGE` (**D4**); §7 — OQ-REC-1
  resolved, OQ-REC-2 закрыт B13, OQ-REC-4 закрыт B3, OQ-REC-3/5/6/7 — в
  реестр DRF-1349; §8 — критерии под C04/C05. Не изменено (v1.0 молчит):
  suppression N9, deep-link persistence UX-OD-004, перечень `linkage_type`,
  §6 out of scope. При утверждении владельцем `status` → `approved`.
- 2026-07-29 — UX-MERGE-001: merge по результатам reconciliation
  (UX-RECON-001, вариант B). UX draft переписан в «Recommendation UX
  Addendum» (не контракт, UX-facing constraints): дубли CANON (идентичность
  §3–4, composition §9–10, lifecycle §14/§22, attribution §15/§18–20,
  economic neutrality §11, safety §23) заменены ссылками; оставлен UX-слой
  (поля карточки, коды состояний §5, suppression N9, deep-link persistence).
  Исправлены конфликты: C1 (условия alternatives — по CANON §10), C2
  (TTL/lifecycle — по CANON §22, устаревшее «не определены» снято), C4
  (lifecycle — UX view-model со ссылкой на CANON §14). C3: displayable-правило
  сохранено как UX-норма с пометкой о переносе в CANON §13 (recon, действие
  1). OQ-REC-1 — resolved; OQ-REC-2…7 — open (статусы §7). Заменяет
  `contracts/draft-mvp-recommendation-contract.md` (v0.1, удалён).
- 2026-07-29 — UX-REFINE-001 (наследуется из draft): explanation rule в
  редакции «no displayable explanation → no show» по owner ruling 2026-07-29;
  OQ-REC-1 принят, OQ-REC-6 переформулирован (владелец классификации).
