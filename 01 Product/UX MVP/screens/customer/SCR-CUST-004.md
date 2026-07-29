---
node_id: ayla.ux.scr-cust-004
screen_id: SCR-CUST-004
title: SCR-CUST-004 — Recommendation card + explanation + confirm CTA (N9)
name: Recommendation card + explanation + confirm CTA (N9)
type: specification
version: "0.2"
status: draft
task_id: UX-CUST-002a
owner: UX Architecture
knowledge_area:
  - product
domain:
  - recommendation
system_owner:
  - ayla-recommendation
  - ayla-mini-app
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
readiness: PARTIAL (проектируется только незаблокированная часть; TTL/expiry — по CANON §22, session-scoped трактовка — assumption)
sources: [recommendation-ux-addendum (UXA §1–5), CANON Ayla MVP Recommendation Contract v0.3 (SRC-16: §3–4, §9–10, §13–14, §22), SRC-02 (UJS этапы 7–9, N5, N9), UX-OD-004, design-wave-1a §3–4]
---

# SCR-CUST-004 — Recommendation card + explanation + confirm CTA

- **actor:** Ayla → User
- **surface:** bot DM (MAX)
- **mvp_flow:** Happy Path Booking (Wave 1A.1), этапы 7–9, N9

## purpose
Показать одну персонализированную рекомендацию с объяснением «почему это» и
получить явное подтверждение намерения. Подтверждение намерения ≠
подтверждение записи (UX-OD-004).

## user_goal
Получить один понятный следующий шаг (не каталог) и контролировать действие:
ничего не происходит без явного согласия (SRC-02 этапы 7, 9).

## primary_action
Подтвердить рекомендацию (CTA «Записаться») → переход в SCR-CUST-006 (slot
picker) с неизменным `recommendation_id`.

## secondary_actions
- Отклонить (мягкий отказ) → alternative в пределах лимита.
- Отклонить жёстко («не напоминай») → suppression (N9).
- Запросить другой вариант явно → alternative (rerank с уточнённым
  constraint, CANON §10).

## required_data (от Recommendation Composer; UX не обогащает карточку вне контракта — UXA §1, proposal)
- `recommendation_id` — обязателен; сохраняется через весь booking flow,
  включая deep link bot DM → Mini App (UX-OD-004, UXA §4; идентичность —
  CANON §3–4).
- Услуга (service) — обязательно; специалист/салон — обязательно, если
  применимо.
- Объяснение «почему подходит» (displayable) + inline attribution применённого
  контекста — обязательно (факт, Scope Contract §4.1 п. 9); показывается
  только объяснение, классифицированное как displayable (UXA §2).
- Цена, длительность, ближайший слот — **опционально**, «если доступны» до
  решения OQ-REC-4 (не обязательные поля; displayed slot ≠ reservation).

## key_components
- Одна карточка primary (≤1 primary одновременно; до 2 alternatives — по
  условиям CANON §10: явный запрос, отказ, недоступность primary, несовпадение
  цены/времени/мастера, недостаток evidence, требование policy; у каждой
  alternative свой `recommendation_id` + `parent_recommendation_id`,
  CANON §3–4, §10).
- Текст объяснения: соответствует фактически использованному контексту, не
  заявляет неиспользованные факты, не раскрывает sensitive context (SRC-02
  этап 8; CANON §13).
- CTA-кнопки: подтвердить / другой вариант / отказаться.

## states
1. **success (card_shown)** — карточка primary + объяснение + CTA. Действия:
   подтвердить, отклонить, запросить другое.
2. **declined (мягкий)** — после первого отклонения: alternative с
   объяснением (в пределах ≤2, условия — CANON §10) либо, если alternative
   нет, нейтральное acknowledgement без давления. Действия: принять
   alternative, отказаться.
3. **declined / N9 (жёсткий или повторный)** — suppression: жёсткий отказ —
   блокировка предложений без `reconsider_after`; повторный/мягкий финальный —
   нейтральное acknowledgement без CTA. UX не инициирует новых предложений.
   Действия: продолжить диалог вне рекомендации, обычный поиск (SCR-CUST-005),
   выйти.
4. **invalidated (специалист недоступен после показа, N5)** — честное
   сообщение + alternative с объяснением замены (объяснение замены — proposal
   в источнике, A3). Действия: принять alternative, отказаться.
5. **no_displayable_explanation** — Composer не вернул displayable объяснение
   (объяснение отсутствует или классифицировано internal-only) → карточка НЕ
   рендерится, переход в SCR-CUST-005 (правило «no displayable explanation →
   no show», принято owner 2026-07-29, UXA §2; перенос в CANON §13 — recon,
   действие 1).
6. **no_candidates / N3** — кандидатов не осталось: состояние живёт в
   SCR-CUST-005 (честное no recommendation + обычный поиск); здесь — только
   переход.

## dependencies
- Recommendation UX Addendum (UX-facing constraints, UX-GAP-0104) + CANON
  Ayla MVP Recommendation Contract v0.3 (SRC-16) — состав карточки,
  explanation rule, lifecycle (view-model UXA §3 / projection CANON §14),
  suppression.
- UX-OD-004: CTA подтверждает намерение, не запись; `recommendation_id` —
  сквозной; `SAFETY_BLOCKED` → SCR-CUST-016 (вне этого экрана).
- Далее: SCR-CUST-006.

## assumptions
- **A1.** Recommendation UX Addendum — draft (не контракт; UX-facing
  constraints к CANON v0.3), принят как рабочая норма до owner approval
  (пакет решений — reviews/recommendation-owner-review-001.md); доменная
  семантика — CANON (SRC-16).
- **A2.** Правило «нет displayable объяснения → не показываем» — **принято
  owner 2026-07-29** в редакции displayable (объяснение классифицируется
  displayable / internal-only; при internal-only карточка не рендерится).
  Открыт только вопрос владельца классификации (OQ-REC-6: Safety/Trust +
  Recommendation).
- **A3.** TTL/expiry определены в CANON §22 (`expires_at`, projection
  lifecycle, read/action gate); UX опирается на view-model UXA §3. Открыто
  подтверждение session-scoped трактовки Phase 1 против `expires_at`
  (OQ-REC-2) — expiry-состояние в этой версии **не рисуем**.
- **A4.** TTL suppression после мягкого отказа не задан (OQ-REC-3): до
  решения — suppression в пределах текущей сессии.

## blockers
Нет для незаблокированной части (состав карточки, объяснение, CTA).
PARTIAL-статус — из-за UX-GAP-0104 (ожидаются решения Recommendation Owner по
OQ-REC-2/4/6/7). **Финальная сверка экрана с CANON и addendum — после
ответов Recommendation Owner (OQ-REC-2/4/6/7).**

## design_notes
- Запрещено: цена/длительность/слот как обязательные поля (OQ-REC-4); каталог
  равноправных карточек; давление после отказа («Ayla давит»); атрибуция
  отклонённой рекомендации.
- Объяснение — часть карточки, не отдельное сообщение, которое можно потерять.

## changelog
- 2026-07-29 — UX-MERGE-001: ссылки draft-mvp-recommendation-contract →
  recommendation-ux-addendum (UXA) + CANON (SRC-16); C1 — условия alternatives
  приведены к CANON §10 (убрано сужение «только после отклонения/запроса»);
  C2 — A3 приведено к CANON §22 (`expires_at`, action gate; устаревшее «TTL не
  определены» снято); C4 — lifecycle трактуется как UX view-model (CANON §14).
  Финальная сверка — после OQ-REC-2/4/6/7.
- 2026-07-29 — UX-REFINE-001: правило объяснения приведено к редакции
  displayable («no displayable explanation → no show», принято owner
  2026-07-29); состояние 5 переименовано в `no_displayable_explanation`;
  assumption A2 обновлено. Основание: owner ruling 2026-07-29 (OQ-REC-1).
