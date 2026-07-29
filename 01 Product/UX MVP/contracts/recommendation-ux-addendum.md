---
node_id: ayla.ux.recommendation-ux-addendum
task_id: UX-MERGE-001
title: Recommendation UX Addendum
type: specification
status: draft
decision_status: proposed
version: "0.1"
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
updated: 2026-07-29
review_cycle: monthly
prepared_by: UX-документалист (UX-MERGE-001)
basis: UX-GAP-0104
depends_on:
  - "[[Ayla MVP Recommendation Contract]]"
related:
  - "[[Ayla MVP User Journey Specification]]"
unblocks:
  - SCR-CUST-004 (recommendation card)
  - SCR-CUST-005 (no-recommendation)
  - SCR-CUST-006 (slot picker)
scope: MVP Phase 1 (session-only, no proactive)
note: >
  Не контракт. UX-facing constraints к CANON (Ayla MVP Recommendation Contract,
  owner Product Architecture). Не source of truth для recommendation-правил.
---

# Recommendation UX Addendum

> **Статус документа.** Это **не контракт** и **не source of truth** для
> recommendation-правил. Канонический источник доменной семантики —
> **Ayla MVP Recommendation Contract v0.3** (`05 Architecture/`, далее CANON,
> owner Product Architecture). Этот addendum фиксирует только **UX-facing
> constraints** — presentation-слой, который CANON не покрывает: состав
> карточки, коды empty/blocked-состояний, suppression N9, deep-link
> persistence. Все дубли доменной семантики заменены ссылками на CANON
> (результат reconciliation UX-RECON-001, вариант B,
> `reviews/recon-recommendation-contract-001.md`).
>
> Пометки: *(факт — источник)*; **(proposal)** — предложение, не
> зафиксированное в источниках; «CANON §N» — раздел Ayla MVP Recommendation
> Contract v0.3.

## 1. Composition и поля карточки

Доменная семантика — в CANON, здесь не дублируется:

- Идентичность `recommendation_id` (immutable record, RecommendationSet,
  `presentation_version`) — **CANON §3–4**.
- Composition: ≤1 primary + ≤2 alternatives, не каталог — **CANON §9–10**.
  Условия появления alternatives — **по CANON §10** (явный запрос, отказ,
  недоступность primary, несовпадение цены/времени/мастера, недостаток
  evidence, требование policy и др.); ранняя UX-формулировка «только после
  отклонения primary или явного запроса» **отменена** как сужающая канон
  (конфликт C1, recon §3).
- Immutable snapshots, pipeline, eligibility gates — **CANON §5, §7–8**;
  кандидат, исключённый на любом этапе pipeline, не возвращается (факт —
  Killer PRD §5.1; CANON §8).

UX-слой — обязательные поля карточки (SCR-CUST-004):

| Поле | Статус | Основание |
|---|---|---|
| `recommendation_id` | обязателен (факт) | CANON §3–4; Scope Contract §4.1 п. 11 |
| услуга (service) | обязателен (факт) | eligibility/relevance gates, Killer PRD §5.1; CANON §8 |
| специалист / салон (provider) | обязателен, если применим (факт) | eligibility gate; tie-breaker Killer PRD §5.3 |
| объяснение «почему подходит» (displayable, §2) + inline attribution применённого контекста | обязателен (факт) | Scope Contract §4.1 п. 9; Killer PRD §6.1 п. 3; UJS этап 8; CANON §13 |
| цена, длительность | опционально, «если доступны» **(proposal)** | цена может показываться как budget filter, не ranking signal (факт — Killer PRD §5.3; CANON §11); длительность в источниках не зафиксирована → OQ-REC-4 |
| ближайший слот (nearest available slot) | **(proposal)** | displayed slot не является reservation; slot проверяется при commit booking (факт — UJS этап 10; CANON §22 revalidation); наличие слота в карточке источниками прямо не нормировано → OQ-REC-4 |

UX-правило: карточка рендерится только из полей, переданных Recommendation
Composer; UX не обогащает карточку данными вне контракта **(proposal)**.

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
  **Пометка (конфликт C3):** правило предложено к переносу в CANON §13 —
  действие 1 реестра recon (`reviews/recon-recommendation-contract-001.md` §4);
  до переноса норма формально закреплена только здесь.
- Открытым остаётся вопрос владельца классификатора displayable vs
  internal-only (предложение — Safety/Trust + Recommendation) → OQ-REC-6.

## 3. UX view-model lifecycle и suppression

**UX view-model (не контрактная модель):** `created → shown → accepted |
declined | expired | invalidated` — представление для экранов. Контрактная
модель — **CANON §14**: decision state — projection
(`active | superseded | expired | invalidated`), а `presented / accepted /
declined` — interaction facts, не состояния (конфликт C4: смешение фактов и
состояний устранено, для UX допустимо только как view-model).

- **Expiry/TTL:** определены в **CANON §22** — `expires_at`, TTL-условия,
  read/action gate (устаревшая формулировка «TTL в источниках не определены»
  снята, конфликт C2). Открытый вопрос — подтверждение owner трактовки
  session-scoped lifetime Phase 1 против `expires_at` CANON §22 → OQ-REC-2
  (recon, действие 6). Частные случаи invalidation: `integrity_invalidated`
  при post-display нарушении economic-neutrality — рекомендация не может
  продолжать recommendation-derived flow (факт — Killer PRD §5.3; политика —
  CANON §11; UX-статус — §5); недоступность специалиста/слота после показа —
  честное сообщение + alternative (факт — N5, этап 10; CANON §10, §22).
- **События:** каноничны имена **CANON §15** — `recommendation.presented /
  accepted / declined` (owner Channel Delivery / Interaction),
  `qualified_action.attributed` (owner Attribution/Measurement);
  `recommendation.generated` отклонён. Имена Roadmap §6.4
  (`RecommendationShown`, `RecommendationAccepted`, `QualifiedActionAttributed`)
  подлежат синхронизации с CANON §15 при регистрации в Domain Event Registry
  (конфликт C5; recon, действие 2) → OQ-REC-5. Analytics (informative):
  `recommendation_created`, `recommendation_explanation_rendered`,
  `recommendation_dismissed` (факт — CSR §9.2).
- **Suppression после отказа (N9, UX-норма):** после первого отклонения —
  alternative в пределах лимита (≤2, условия — CANON §10). После повторного
  или явно жёсткого отказа дальнейшие предложения подавляются: жёсткий отказ
  («не напоминай») — блокировка **без `reconsider_after`**; мягкий —
  нейтральное acknowledgement без CTA (факт — UJS этап 9, N9). TTL suppression
  для мягкого отказа источниками не задан → OQ-REC-3.
- Отклонённая или invalidated рекомендация не получает атрибуцию (факт —
  Killer PRD §6.2, §5.3; CANON §17–18).

## 4. Attribution — UX-требования

Доменная семантика — в CANON, здесь не дублируется: qualified action,
single-winner, `direct | assisted | unattributed`, обязательные ссылки —
**CANON §15, §18, §20**; attribution window — **CANON §19** (окна принадлежат
Measurement Framework / Window Registry, контракт хранит `policy_version`).

UX-слой:

- **Deep-link persistence (UX-OD-004):** `recommendation_id` сохраняется через
  весь booking flow, включая deep link bot DM → Mini App (contextual deep
  link, не generic home). Booking без `recommendation_id` — `unattributed`
  (факт — Killer PRD §6.2; CANON §18). Гарантии доставки и срок жизни
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
  до owner decision — куда переносится (CANON §18, Attribution/Measurement
  spec или остаётся здесь): recon, действие 3, строка 10 матрицы.

## 5. Empty / blocked states — UX-коды и гарантии для UX

| Состояние | Код | Гарантия для UX | Основание |
|---|---|---|---|
| Нет кандидатов (SCR-CUST-005) | `NO_CANDIDATES` | Явный статус no recommendation; UX **не выдумывает** карточку; доступен обычный поиск/запись без персонализированной primary | факт — Killer PRD §5.3 Fallback; N3 |
| Нет displayable объяснения | `NO_DISPLAYABLE_EXPLANATION` | Объяснение отсутствует или классифицировано internal-only → карточка не рендерится, перевод в SCR-CUST-005; UX не показывает internal-only содержимое ни в каком виде | правило §2, принято owner 2026-07-29; перенос в CANON §13 — recon, действие 1 |
| Специалист недоступен | `PROVIDER_INELIGIBLE` | Кандидат исключается до показа; если недоступность выявлена после показа — честное сообщение + alternative **с объяснением замены (proposal в источнике)** | факт — N5; Killer PRD §5.1; CANON §8, §10 |
| Safety-блокировка | `SAFETY_BLOCKED` | Отдельный статус, **не** no-recommendation: boundary message без CTA на заблокированную услугу; безопасная альтернатива — только после Boundary Handling (S8) | факт — N8; Killer PRD §5.1 этап 2; согласовано с CANON §23, конфликта нет |
| Economic-neutrality alert | `ranking_economic_neutrality_alert` | Не user-facing ошибка; выдача персонализированной primary блокируется, обычный поиск/запись сохраняются | факт — Killer PRD §5.3; UJS этап 7; политика — CANON §11 (handling CANON не фиксирует — конфликт C5 минорный, owner confirm при переносе) |
| Нет слотов после accept | `NO_AVAILABLE_SLOTS` | Переход к SCR-CUST-006 с состоянием slot unavailable + альтернатива (другое время; другой мастер — только в initial booking; в reschedule альтернатива мастера — W2, UX-OD-001) | факт — N4, этап 10; CANON §22 (revalidation), §10; уточнение области — UX-OD-001 |

Дополнительно для SCR-CUST-006 (slot picker): displayed slot не является
reservation; доступность перепроверяется при commit booking (факт — UJS
этап 10; CANON §22). Формат: bot DM — compact, Mini App — expanded
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
  constraint — **CANON §11** и Recommendation Engine Specification
  (owner Recommendation); этот addendum ranking не определяет.
- Роль retrieved memory в candidate generation / ranking / explanation
  (UJS OQ №11) — upstream, owner CANON (§6).

## 7. Open Questions

Статусы по состоянию на 2026-07-29 (recon UX-RECON-001; пакет решений —
`reviews/recommendation-owner-review-001.md`):

1. **OQ-REC-1 — RESOLVED (owner 2026-07-29).** Правило принято в редакции
   displayable: «нет displayable объяснения → не показываем»; классификация
   displayable / internal-only (§2). Перенос в CANON §13 — recon, действие 1.
2. **OQ-REC-2 — OPEN.** Подтверждение трактовки lifetime Phase 1:
   session-scoped против `expires_at` CANON §22 (CANON §14/§22 определяют
   projection и TTL-условия; UX-формулировка «не определено» снята — C2).
   Owner: Recommendation / AI Architecture (recon, действие 6).
3. **OQ-REC-3 — OPEN.** TTL suppression после мягкого отказа (жёсткий —
   блокировка без `reconsider_after`, факт). Owner: Recommendation / AI
   Architecture + Product Owner (recon, действие — строка 8 матрицы).
4. **OQ-REC-4 — OPEN (blocking).** Обязательность полей
   «цена/длительность/ближайший слот» на карточке SCR-CUST-004. Owner:
   Product Owner + UX (recon, действие 7).
5. **OQ-REC-5 — OPEN.** Семантика событий `recommendation.*` и
   `qualified_action.attributed`: синхронизация имён Roadmap §6.4 с
   publication matrix CANON §15 при регистрации в Domain Event Registry (C5).
   Owner: Architecture (recon, действие 2).
6. **OQ-REC-6 — OPEN.** Владелец классификации объяснений displayable vs
   internal-only (предложение — Safety/Trust + Recommendation; UX получает
   классифицированный результат). Owner: Safety/Trust Owner + Recommendation
   / AI Architecture (recon, действие 8).
7. **OQ-REC-7 — OPEN.** Deep-link-контракт bot DM → Mini App: гарантии
   доставки и срок жизни `recommendation_id` поверх UX-OD-004. Owner:
   Platform (ai-bot-platform) + UX (recon, действие 9).

## 8. Acceptance Criteria

1. SCR-CUST-004 рендерит карточку только при наличии `recommendation_id`
   (CANON §3–4) и объяснения, классифицированного как displayable, с inline
   attribution; при отсутствии displayable объяснения — переход в SCR-CUST-005
   (§2).
2. Одновременно показывается ≤1 primary и ≤2 alternative (CANON §9–10);
   alternative несёт собственный `recommendation_id` и
   `parent_recommendation_id` (CANON §3–4, §10).
3. SCR-CUST-005 корректно различает `NO_CANDIDATES`,
   `NO_DISPLAYABLE_EXPLANATION`, `PROVIDER_INELIGIBLE`, `SAFETY_BLOCKED`
   (тексты/CTA по §5; при safety-блокировке — без CTA на заблокированную
   услугу, CANON §23).
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

- **CANON:** Ayla MVP Recommendation Contract v0.3 — §3–5, §7–11, §13–15,
  §17–20, §22–23 (`05 Architecture/Ayla MVP Recommendation Contract.md`;
  SRC-16)
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
