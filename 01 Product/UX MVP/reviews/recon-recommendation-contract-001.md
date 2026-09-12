---
task_id: UX-RECON-001
title: Reconciliation — MVP Recommendation Contract (Canon vs UX Draft)
type: specification
status: archived
review_status: pending_owner_review
version: "0.1"
created: 2026-07-29
prepared_by: Reconciliation Agent (UX-RECON-001)
addressee: Recommendation / AI Architecture Owner + Product Architecture Owner
subjects:
  - "05 Architecture/Ayla MVP Recommendation Contract.md (CANON, v0.3, draft/proposed)"
  - "01 Product/UX MVP/contracts/draft-mvp-recommendation-contract.md (UX DRAFT, v0.1, Level B)"
related:
  - reviews/recommendation-owner-review-001.md
  - screens/customer/SCR-CUST-004.md
  - screens/customer/SCR-CUST-006.md
node_id: ayla.ux.recon-recommendation-contract-001
owner: UX Architecture
domain:
  - recommendation
system_owner:
  - ayla-recommendation
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

> **Архив (PROPOSED 2026-09-12 — awaiting owner approval; Final
> Reconciliation v1.0 §6.3).** Действие 1 этого разбора (перенос правила
> «нет displayable объяснения → не показываем» в контракт §13) выполнено в
> контракте v0.4; остальные действия закрыты amendment A4 (Recommendation UX
> Addendum v0.2, пакет 2 B3/B4). Документ сохраняется как отчёт, на месте —
> чтобы не рвать ссылки из `gaps/`, `screens/` и Addendum; `status` →
> `archived`. Содержимое ниже не менялось.


# Reconciliation — MVP Recommendation Contract (Canon vs UX Draft)

> Этот документ — анализ расхождений и предложение merge. Он **не** является
> source of truth, **не** меняет статусы документов и **не** заменяет owner
> decisions. Реальное потребление: SCR-CUST-004 и SCR-CUST-006 (файлы
> существуют); **SCR-CUST-005.md на диске отсутствует** — потребление
> зафиксировано по `02-screen-inventory-customer.md` (строка SCR-CUST-005,
> Not Started) и `waves/design-wave-1a.md` (§1A.3).

## 1. Requirement Ownership Matrix

| # | Требование | В CANON (§, вкратце) | В UX DRAFT (§) | Потребляется экранами | Owner | Действие |
|---|---|---|---|---|---|---|
| 1 | Модель идентичности `recommendation_id` (immutable record + RecommendationSet, свой id у каждого варианта, `presentation_version`) | §3, §4 — immutable decision record; каждый primary/alternative — отдельная запись; новый id при существенном изменении | §1 — `recommendation_id` обязателен; alternative — собственный id + `parent_recommendation_id` (факт Killer PRD §5.1) | SCR-CUST-004 (required_data), SCR-CUST-006 (неизменным) | Canon | Оставить в Canon; из UX DRAFT убрать дубль → ссылка на Canon §3–4 |
| 2 | Immutable snapshots (context/memory/candidates, версионированные refs, retention dependency) | §7 — нормативно, с digest и policy_version | — | Не напрямую | Canon | Оставить в Canon (UX не потребляет) |
| 3 | Composition: ≤1 primary + ≤2 alternatives, не каталог | §9, §10 — primary одна; alternatives по **8 условиям** (запрос, отказ, недоступность, цена/время/мастер, недостаток evidence, policy) | §1 — ≤1 primary, ≤2 alternative; alternative **только после отклонения primary или явного запроса** | SCR-CUST-004 (key_components) | Canon | Оставить в Canon; UX-формулировку сузившую условия — исправить по Canon §10 (конфликт C1) |
| 4 | Обязательные поля карточки: цена / длительность / ближайший слот (OQ-REC-4) | Частично: §8 Candidate — `price_snapshot`, `availability_ref` (доменная модель, не карточка) | §1 — таблица полей: цена/длительность опционально, слот — proposal ≠ reservation | SCR-CUST-004 (required_data: опционально до OQ-REC-4) | UX + Product Owner (OQ-REC-4, blocking) | Оставить UX addendum; owner decision по OQ-REC-4 |
| 5 | Displayable explanation: классификация displayable/internal-only, правило «no displayable → no show» | §13 — Explanation Contract (производная от ranking, запреты); классификации displayable **нет** | §2 — классификация + правило, принято owner 2026-07-29 | SCR-CUST-004 (state 5, A2) | Canon (контракт) + Safety/Trust (классификатор, OQ-REC-6) | Перенести в Canon §13 (по owner ruling); из UX — ссылка (конфликт C3) |
| 6 | Lifecycle / TTL | §14 — projection `active\|superseded\|expired\|invalidated`; §22 — `expires_at`, TTL-условия, read/action gate | §3 — UX-цепочка `created→shown→accepted\|declined\|expired\|invalidated`; «TTL и invalidation в источниках не определены» → OQ-REC-2 | SCR-CUST-004 (A3 — expiry не проектируется) | Canon | Оставить в Canon; UX-формулировку «не определено» обновить (конфликты C2, C4); OQ-REC-2 — owner confirm session-scoped vs `expires_at` |
| 7 | Expiry vs начатый booking flow (OQ-R6: ownership → Booking context, revalidation) | §22 — owner ruling, таблица поведения | — (только «слот ≠ reservation», §5) | SCR-CUST-006 (stale_slot) | Canon | Оставить в Canon |
| 8 | Suppression после отказа (N9): жёсткий — блок без `reconsider_after`; мягкий — нейтральное acknowledgement; TTL мягкого не задан | — (§17 определяет только `declined` как явный отказ) | §3 — правила N9 + OQ-REC-3 (TTL мягкого) | SCR-CUST-004 (states 2–3) | UX / Product (норма — UJS N9) | Оставить UX addendum; OQ-REC-3 — owner decision (Recommendation + Product Owner) |
| 9 | Attribution: qualified action, single-winner, `direct\|assisted\|unattributed`, обязательные ссылки | §15, §18, §20 — `qualified_action.attributed`, owner Attribution/Measurement; таксономия R4 | §4 — `recommendation_id → qualified action`; single-winner; booking без id → `unattributed` | SCR-CUST-004 (design_notes: не атрибутировать отклонённую), SCR-CUST-006 | Canon / Architecture | Оставить в Canon; из UX убрать дубль → ссылка |
| 10 | `linkage_type` (inline_accept, recommendation_deeplink, derived_booking_draft, …) | — (§18 требует только `action_type`, `attribution_type`) | §4 — список допустимых linkage_type (факт — Killer PRD §6.1–6.3) | SCR-CUST-006 (deep link) | Owner decision (Attribution / Measurement) | Вынести owner: перенести в Canon/Attribution spec или оставить UX-перечнем |
| 11 | Attribution window | §19 — CLOSED by ownership: окна принадлежат Measurement Framework / Window Registry; контракт хранит только `policy_version` + prospective rules | §4 — упоминает attribution window без значений | Не напрямую | Canon (отсылка к Measurement) | Оставить в Canon |
| 12 | Empty state `NO_CANDIDATES` (честное no recommendation + обычный поиск) | — (нет UX-статусов; §8 — исключённый кандидат не возвращается) | §5 — код + гарантия контракта для UX | SCR-CUST-005 (не написан; по inventory/wave) | UX | Оставить UX addendum |
| 13 | `SAFETY_BLOCKED` (boundary message, без CTA на заблокированную услугу) | §23 — частично: при safety block — S8 Boundary Handling | §5 — отдельный статус, не no-recommendation | SCR-CUST-005 (не написан); SCR-CUST-004 (`SAFETY_BLOCKED` → SCR-CUST-016) | Safety (policy) / UX (state) | Оставить UX addendum; согласовано с Canon §23, конфликта нет |
| 14 | `NO_AVAILABLE_SLOTS` (после accept → slot unavailable + альтернатива) | §22 (revalidation), §10 (недоступность primary — условие alternative) | §5 — код + переход к SCR-CUST-006 | SCR-CUST-006 (empty / no_available_slots) | UX + Booking | Оставить UX addendum |
| 15 | `NO_DISPLAYABLE_EXPLANATION` (карточка не рендерится → SCR-CUST-005) | — (см. строку 5) | §5 — код + гарантия | SCR-CUST-004 (state 5) | Canon (правило) / UX (состояние) | Правило — в Canon (вместе со строкой 5); UX-состояние — addendum |
| 16 | Economic neutrality (коммерческий интерес — не ranking feature; paid ranking out of MVP) | §11 — нормативно + проверяемое правило | §6 (out of scope ranking), ссылки на Killer PRD §5.3 | Не отображается пользователю | Canon | Оставить в Canon; UX-ссылку сохранить как addendum-указание |
| 17 | `ranking_economic_neutrality_alert` / `integrity_invalidated` (блокировка выдачи, поиск сохраняется) | §11 — обработка нарушений «здесь не пересматривается» (quarantine — Killer PRD §5.3) | §3, §5 — UX-статус + invalidation рекомендации | SCR-CUST-005 (не написан) | Canon (политика) / UX (статус) | UX addendum; при переносе — owner confirm, т.к. Canon явно отказался фиксировать handling (конфликт C5, минорный) |
| 18 | Семантика событий `recommendation.*` | §15 — publication matrix (owner ruling R2/R10): `recommendation.presented/accepted/declined`, owner Channel Delivery | §3, §4 — опора на `RecommendationShown`, `RecommendationAccepted`, `QualifiedActionAttributed` (Roadmap §6.4), семантика pending → OQ-REC-5 | SCR-CUST-004/006 (косвенно) | Canon / Architecture (Domain Event Registry) | Синхронизировать имена при регистрации (конфликт C5'); OQ-REC-5 — owner Architecture |

**Статистика:** всего 18 требований; в обоих документах — 7 (строки 1, 3, 6, 9, 13, 16, 18); только Canon — 3 (2, 7, 11); только UX DRAFT — 8 (4, 5, 8, 10, 12, 14, 15, 17); формулировочных конфликтов — 5 (§3 этого документа).

## 2. Вердикт по варианту: **B**

Canon покрывает ~80% доменной семантики (идентичность, snapshots, pipeline,
lifecycle/TTL, attribution, economic neutrality, safety/consent gates), причём
с owner rulings v0.3. Но Canon **не покрывает** принятое owner правило
displayable explanation (2026-07-29) и UX-уровень: состав карточки, коды
empty/blocked-состояний, suppression N9, deep-link persistence — это не его
слой (presentation). Полное покрытие (вариант A) невозможно без переноса
UX-норм в архитектурный контракт, что сломает границу владения; вариант C
неверен — расхождения локальны, а не системны. UX DRAFT превращается в
**«Recommendation UX Addendum»** (UX-facing constraints, не контракт):
дубли доменной семантики заменяются ссылками на Canon.

## 3. Конфликты формулировок

Канонична формулировка источника с более высоким статусом: CANON
(`source_kind: canonical`, owner Product Architecture, owner rulings v0.3) —
по доменной семантике; UX DRAFT — только по presentation-слою, где Canon
молчит, и только до owner decision.

- **C1. Условия появления alternatives.** CANON §10 — 8 условий (включая
  недоступность primary, несовпадение цены/времени/мастера, недостаток
  evidence, требование policy); UX DRAFT §1 — «только после отклонения primary
  или явного запроса». UX-формулировка **сужает** канон. Канонична: CANON §10
  (оба апеллируют к Killer PRD §5.1, но CANON воспроизводит её полнее).
- **C2. TTL/lifecycle «не определены».** UX DRAFT §3: «персистентность, TTL и
  правила invalidation в источниках не определены» (OQ-REC-2). CANON §14/§22
  (v0.3, та же дата) определяет `expires_at`, TTL-условия, projection
  lifecycle, action gate. Формулировка UX DRAFT устарела относительно Canon
  v0.3. Канонична: CANON §22.
- **C3. Displayable-классификация отсутствует в Canon.** UX DRAFT §2 фиксирует
  owner ruling 2026-07-29 (displayable/internal-only, «no displayable → no
  show»); CANON v0.3 той же датой правило не содержит — §13 без классификации.
  Решение принято owner, но не записано в нормативный источник → расхождение
  статусов: правило живёт только в UX-драфте. Канонична: owner ruling (подлежит
  переносу в CANON §13); до переноса норма формально не закреплена.
- **C4. Модель lifecycle.** CANON §14: decision state — projection
  (`active|superseded|expired|invalidated`), `presented/accepted/declined` —
  interaction facts, не состояния. UX DRAFT §3: единая цепочка
  `created→shown→accepted|declined|expired|invalidated` смешивает факты и
  состояния. Для UX-экранов допустимо как view-model, но не как контрактная
  формулировка. Канонична: CANON §14.
- **C5. Имена событий.** UX DRAFT §3/§4 опирается на `RecommendationShown`,
  `RecommendationAccepted`, `QualifiedActionAttributed` (Roadmap §6.4); CANON
  §15 определяет `recommendation.presented/accepted` (owner Channel Delivery /
  Interaction) и `qualified_action.attributed` (owner Attribution/Measurement),
  при этом `recommendation.generated` отклонён. Канонична: CANON §15 (owner
  ruling R2/R10); синхронизация — при регистрации в Domain Event Registry.

## 4. Предлагаемые действия

1. **Product Architecture (owner CANON):** дополнить CANON §13 Explanation
   Contract классификацией displayable/internal-only, правилом «no displayable
   explanation → no show» и следствием `NO_DISPLAYABLE_EXPLANATION` — по owner
   ruling 2026-07-29 (закрывает C3).
2. **Product Architecture + Domain Event Registry owner:** синхронизировать
   имена событий Roadmap §6.4 (`RecommendationShown/Accepted`,
   `QualifiedActionAttributed`) с publication matrix CANON §15 при регистрации
   (C5; связано с OQ-REC-5 / OQ-E1).
3. **Recommendation / AI Architecture Owner:** решить, куда переносится список
   `linkage_type` (UX DRAFT §4): в CANON §18, в Attribution/Measurement spec
   или остаётся UX-перечнем (строка 10 матрицы).
4. **UX-документалист:** после owner decision по варианту B — переписать UX
   DRAFT в «Recommendation UX Addendum»: удалить дубли (идентичность §1,
   lifecycle §3, attribution §4, composition) со ссылками на CANON; оставить
   UX-facing constraints — поля карточки, коды состояний §5, suppression N9,
   deep-link persistence.
5. **UX-документалист:** в addendum исправить сужающую формулировку условий
   alternatives по CANON §10 (C1) и убрать «TTL не определён» со ссылкой на
   CANON §22 (C2); lifecycle-цепочку переименовать в UX view-model со ссылкой
   на CANON §14 (C4).
6. **Recommendation / AI Architecture Owner:** подтвердить трактовку OQ-REC-2
   (session-scoped lifetime Phase 1 против `expires_at` CANON §22) — после
   переноса ссылок.
7. **Recommendation / AI Architecture Owner (blocking):** решить OQ-REC-4 —
   обязательность цены/длительности/слота на карточке SCR-CUST-004.
8. **Safety/Trust Owner + Recommendation Owner:** решить OQ-REC-6 — владелец
   классификации displayable/internal-only (условие исполнения действия 1).
9. **Platform (ai-bot-platform) + UX:** решить OQ-REC-7 — гарантии deep-link
   bot DM → Mini App поверх UX-OD-004.
10. **UX-документалист:** после решений 6–9 и owner approval варианта B —
    обновить SCR-CUST-004/006 (только точечно, по изменённым ссылкам) и
    написать SCR-CUST-005; до этого — не трогать (см. §5).

## 5. Что НЕ делать

- **Не редактировать CANON** этой задачей — владелец Product Architecture;
  все правки Canon (действия 1–3) — только через его owner.
- **Не помечать UX DRAFT superseded/archived** и не менять его статус до
  owner decision по варианту B.
- **Не менять Screen Contracts SCR-CUST-004/006** до owner decisions по
  конфликтам C1–C5: C1 и C4 затрагивают уже написанные формулировки
  (условия alternatives в key_components SCR-CUST-004, states/assumptions).
- **Не писать SCR-CUST-005** до решения OQ-REC-4 (blocking) и подтверждения
  варианта B — коды состояний зависят от обоих.
- **Не менять статусы OQ-REC-1…7 и UX-GAP-0104** — закрытие только решениями
  владельцев (recommendation-owner-review-001).
- **Не регистрировать события `recommendation.*`** в Domain Event Registry —
  отдельный шаг после финального review CANON (OQ-E1).
- **Не создавать source of truth** — этот документ только reconciliation и
  предложение merge.

## Changelog

- 2026-07-29 — UX-RECON-001: построена матрица владения (18 требований),
  вердикт — вариант B, зафиксированы конфликты C1–C5 и 10 предлагаемых
  действий. Примечание: SCR-CUST-005.md отсутствует на диске; потребление
  зафиксировано по inventory/wave-документам.
