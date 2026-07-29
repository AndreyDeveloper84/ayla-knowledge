---
node_id: ayla.ux.gap-0104
gap_id: UX-GAP-0104
title: UX-GAP-0104 — MVP Recommendation Contract отсутствует
type: specification
severity: P0
domain:
  - recommendation
detected_in: UX-CUST-001 (screen inventory customer)
status: in-progress
gap_status: open
version: "0.2"
owner: UX Architecture
knowledge_area:
  - product
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
date: 2026-07-29
updated: 2026-07-29
review_cycle: monthly
---

# UX-GAP-0104 — MVP Recommendation Contract отсутствует

## annotation (2026-07-29, UX-SYNC-001)

Gap остаётся **open**. Contract task UX-REC-001 запущена; draft ожидается в
`contracts/draft-mvp-recommendation-contract.md`. SCR-CUST-004 остаётся
PARTIAL до появления контракта и решений OQ4/OQ11.

## description

Экран рекомендации (SCR-CUST-004) опирается на три незакрытых основания:

1. MVP Recommendation Contract (planned, Roadmap §3.2) не создан:
   персистентность рекомендации, expiry/invalidation, состав данных карточки.
2. Fallback этапа 8 «без объяснения рекомендация не показывается» — proposal
   (SRC-02 OQ4), требует сверки с Recommendation Contract.
3. Роль памяти в recommendation pipeline (memory influence model) — upstream
   Open Question №11 (SRC-02): как retrieved memory влияет на candidate
   generation, ranking, explanation, alternatives — не определено.

## why_it_matters

SCR-CUST-004 — носитель главной метрики MVP («запрос → рекомендация →
подтверждённое действие», SRC-01 §9) и обязательной объяснимости
(SRC-01 §4.1 п. 9, Конституция Ст. VII). Без контракта нельзя зафиксировать
required data карточки, правила alternatives (этап 9, N9) и поведение при
невозможности объяснения — экран остаётся PARTIAL.

## blocked_screens

SCR-CUST-004; частично SCR-CUST-005 (fallback-варианты), SCR-CUST-006
(альтернативы при N4 получают собственный `recommendation_id`)

## missing_decision

- MVP Recommendation Contract: состав карточки, lifecycle
  (expiry/invalidation), alternatives limit enforcement.
- Решение OQ4: допустим ли показ рекомендации без полного объяснения
  (redacted) или показ блокируется.
- Решение OQ11 (upstream): memory influence model в pipeline.

## required_owner

Product Owner (OQ4, OQ11) + Product Architecture (Recommendation Contract).

## recommended_artifact

Minimal Contract (MVP Recommendation Contract) + Decision Record (OQ4).

## can_use_temporary_assumption

Да, с оговоркой.

## temporary_assumption

Карточка = одна primary recommendation с `recommendation_id` + объяснение +
CTA; до двух alternatives только после отклонения (SRC-02 этапы 7–9 — факты).
Правило «нет объяснения — нет показа» принимать как рабочее (proposal OQ4),
пометив его в спеке экрана как assumption.

## acceptance_criteria

- MVP Recommendation Contract создан; OQ4 и OQ11 закрыты решениями.
- Состав данных карточки и lifecycle рекомендации зафиксированы.
- Правила показа alternatives и redacted explanation подтверждены.

## update 2026-07-29 (UX-REC-001)

Draft Minimal Contract доставлен (UX-REC-001; позже переписан в
`contracts/recommendation-ux-addendum.md` — см. update UX-MERGE-001). Gap
остаётся open до решений владельца по OQ-REC-1…7 (объяснение как норма,
TTL/expiry, TTL suppression, поля карточки, семантика `recommendation.*`,
redacted explanation, deep-link контракт). Принят как рабочая норма
(assumption) для SCR-CUST-004/005/006.

## update 2026-07-29 (UX-MERGE-001)

Reconciliation выполнен (`reviews/recon-recommendation-contract-001.md`,
UX-RECON-001, вердикт — **вариант B**). **Второй source of truth устранён:**
UX draft переписан в `contracts/recommendation-ux-addendum.md` — не контракт,
UX-facing constraints; дубли доменной семантики заменены ссылками на CANON
(Ayla MVP Recommendation Contract v0.3, SRC-16, owner Product Architecture);
конфликты C1/C2/C4 исправлены, C3 — displayable-правило сохранено как
UX-норма с пометкой о переносе в CANON §13. OQ-REC-1 — resolved.

Gap остаётся **open** до:
- решений Recommendation Owner по OQ-REC-2/4/6/7 (session-scoped vs
  `expires_at` CANON §22; обязательные поля карточки — blocking; владелец
  классификации displayable; deep-link гарантии);
- переноса displayable-правила в CANON §13 (recon, действие 1, owner Product
  Architecture).
