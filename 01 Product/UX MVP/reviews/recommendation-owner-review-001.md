---
node_id: ayla.ux.recommendation-owner-review-001
task_id: UX-REC-002
title: Decision Package — MVP Recommendation Contract (Owner Review 001)
type: specification
status: archived
version: "0.2"
owner: UX Architecture
knowledge_area:
  - product
domain:
  - recommendation
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
review_status: pending_owner_review
prepared_by: UX-документалист (UX-REC-002)
addressee: Recommendation / AI Architecture Owner
resolves: UX-GAP-0104
basis:
  - contracts/recommendation-ux-addendum.md
  - reviews/recon-recommendation-contract-001.md
  - gaps/UX-GAP-0104.md
  - decisions/ux-owner-decisions.md (UX-OD-004)
---

> **Архив (PROPOSED 2026-09-12 — awaiting owner approval; Final
> Reconciliation v1.0 §6.3).** Действие 1 этого разбора (перенос правила
> «нет displayable объяснения → не показываем» в контракт §13) выполнено в
> контракте v0.4; остальные действия закрыты amendment A4 (Recommendation UX
> Addendum v0.2, пакет 2 B3/B4). Документ сохраняется как отчёт, на месте —
> чтобы не рвать ссылки из `gaps/`, `screens/` и Addendum; `status` →
> `archived`. Содержимое ниже не менялось.


# Decision Package — MVP Recommendation Contract (Owner Review 001)

## Контекст

- Wave 1A.1 стартовала: UX-REC-001 доставил draft Level B; по итогам
  reconciliation (UX-RECON-001, вариант B) draft переписан в
  `contracts/recommendation-ux-addendum.md` (UX-facing constraints к CANON).
- Draft принят как **рабочая норма (assumption)** для SCR-CUST-004/005/006.
- UX-GAP-0104 закрывается **только решениями владельца** по OQ-REC-1…7;
  UX-документалист решений не принимает.

## Decision summary

**Предлагаемое решение:** принять draft как **MVP Recommendation Contract
v0.1** (Level B, UX-facing) с правками по итогам ревью. Draft фиксирует
минимум для UX (composition, explanation rule, lifecycle, attribution,
empty/blocked states), не подменяя полный контракт (planned, Roadmap §3.2):
владение нормами — за Recommendation / AI Architecture. Нормы размечены
«факт — источник» / «(proposal)»; proposal-пункты покрыты OQ-REC-1…7.

## OQ-REC-1…7 — вопросы и рекомендации

### OQ-REC-1 — статус правила «нет объяснения → не показываем» — **RESOLVED**

- **Статус:** resolved by owner 2026-07-29 (редакция displayable explanation).
  Правило принято в переформулированном виде: не «нет explanation», а «нет
  объяснения, которое разрешено показать пользователю» — **no displayable
  explanation → no show**. Explanation классифицируется displayable /
  internal-only (внутренние сигналы, персональные данные, раскрытие ranking
  или provider score → показ запрещён); при internal-only рекомендация не
  показывается, UX переводит сценарий в SCR-CUST-005 (draft §2).
- **Исходный вопрос (снят):** является ли правило «нет объяснения (даже
  redacted) → карточка не рендерится» нормой MVP или остаётся proposal
  (UJS OQ №4)? — отвечено owner-редакцией displayable.
- **Что осталось открытым:** владелец классификации displayable vs
  internal-only → переформулированный OQ-REC-6 (Safety/Trust + Recommendation).

### OQ-REC-4 — обязательные поля карточки: цена / длительность / слот — **BLOCKING**

- **Вопрос:** какие из полей «цена», «длительность», «ближайший слот»
  обязательны на карточке SCR-CUST-004?
- **Рекомендуемый ответ (draft §1, таблица полей):** цена и длительность —
  опционально «если доступны»; ближайший слот — опционально, не является
  reservation (перепроверка при commit booking).
- **Альтернатива:** сделать все три поля обязательными — требует данных, не
  нормированных источниками.
- **Риск ошибочного решения:** обязательность слота — ложное ожидание
  резервации; отказ от цены/длительности — хуже выбор и конверсия метрики.
- **Статус:** blocking — определяет required data SCR-CUST-004.

### OQ-REC-2 — expiry/invalidation и TTL рекомендации — informational

- **Вопрос:** когда `shown → expired`; правила invalidation при устаревании
  слота/кандидата.
- **Рекомендуемый ответ (draft §3):** в источниках не определено; для Phase 1
  session-only — рекомендация живёт в пределах сессии; частные случаи
  invalidation (`integrity_invalidated`, недоступность специалиста/слота)
  применяются как факты.
- **Альтернатива:** задать явный TTL (N минут) в v0.1.
- **Риск:** без TTL возможен показ устаревшей рекомендации; смягчается
  session-only режимом и перепроверкой слота при commit.
- **Статус:** informational, если владелец не возражает против session-scoped
  трактовки.

### OQ-REC-3 — TTL suppression после мягкого отказа — informational

- **Вопрос:** как долго подавлять повторные предложения после мягкого отказа
  (жёсткий — блокировка без `reconsider_after`, факт).
- **Рекомендуемый ответ (draft §3):** до решения — suppression в пределах
  сессии; мягкий отказ → нейтральное acknowledgement без CTA.
- **Альтернатива:** явный TTL — требует persistent состояния, конфликтует с
  Phase 1 session-only (UX-OD-003).
- **Риск:** короткий TTL — назойливость (N9); длинный — потеря релевантных
  предложений.
- **Статус:** informational для Phase 1; решение совместно с Product Owner.

### OQ-REC-5 — семантика событий `recommendation.*` — informational

- **Вопрос:** регистрация `recommendation.*` и `qualified_action.attributed`
  в Domain Event Registry (AYLA-DEC-0025 п. 8 — намеренно не зарегистрированы).
- **Рекомендуемый ответ (draft §3, §4):** UX опирается на зафиксированные
  доменные события (`RecommendationShown`, `RecommendationAccepted`,
  `QualifiedActionAttributed`) и analytics CSR §9.2; pending-семантика экраны
  не блокирует.
- **Альтернатива:** заблокировать attribution-метрики до регистрации событий.
- **Риск:** `booking_from_recommendation` без зарегистрированной семантики
  трактуется командами по-разному.
- **Статус:** informational для UX; owner — Architecture.

### OQ-REC-6 — классификация объяснений displayable vs internal-only — informational

- **Вопрос (переформулирован 2026-07-29, UX-REFINE-001):** кто классифицирует
  объяснение как displayable vs internal-only? Предложение: владелец
  классификации — Safety/Trust Owner совместно с Recommendation Owner; UX
  получает уже классифицированный результат.
- **UX-исход при internal-only** закрыт принятым правилом OQ-REC-1: карточка
  не рендерится, перевод в SCR-CUST-005 (no-recommendation); отдельное
  состояние не вводится.
- **Риск:** без назначенного владельца классификации критерии displayable
  разойдутся между командами; смешение internal-only с `NO_CANDIDATES`
  исказит аналитику причин (код `NO_DISPLAYABLE_EXPLANATION`, draft §5).
- **Статус:** informational — owner — Safety/Trust + Recommendation.

### OQ-REC-7 — deep-link контракт bot DM → Mini App — informational

- **Вопрос:** гарантии доставки и срок жизни `recommendation_id` в Mini App
  поверх UX-OD-004 (contextual deep link).
- **Рекомендуемый ответ (draft §4):** `recommendation_id` сохраняется через
  весь booking flow (UX-OD-004); booking без него — `unattributed`; транспорт —
  за Platform.
- **Альтернатива:** fallback на generic home при потере контекста (запрещён
  UX-OD-004).
- **Риск:** потеря `recommendation_id` → разрыв attribution и занижение
  метрики `booking_from_recommendation`.
- **Статус:** informational для UX; owner — Platform + UX.

## Exact owner questions

Формат ответа: **принять / отклонить / A/B / уточнить параметр**.

1. **(OQ-REC-1, решён)** ~~Принять ли правило «нет объяснения → не
   показываем» как норму MVP Recommendation Contract v0.1?~~ — **принято
   owner 2026-07-29 в редакции displayable:** «no displayable explanation →
   no show», объяснение классифицируется displayable / internal-only.
2. **(OQ-REC-4, blocking)** Принять ли состав полей карточки по draft §1
   (обязательны `recommendation_id`, услуга, специалист, объяснение с inline
   attribution; цена/длительность/слот — опционально)?
   *(принять / отклонить / уточнить обязательность)*
3. **(OQ-REC-2)** Принять ли session-scoped lifetime рекомендации для Phase 1
   без явного TTL? *(принять / уточнить параметр TTL)*
4. **(OQ-REC-3)** Принять ли suppression после мягкого отказа в пределах
   сессии до решения совместно с Product Owner? *(принять / уточнить TTL)*
5. **(OQ-REC-5)** Не возражаете ли против опоры UX на зафиксированные события
   при pending-семантике `recommendation.*`? *(принять / отклонить)*
6. **(OQ-REC-6)** Принять ли, что владелец классификации объяснений
   displayable vs internal-only — Safety/Trust Owner совместно с
   Recommendation Owner? *(принять / уточнить владельца)*
7. **(OQ-REC-7)** Принять ли трактовку UX-OD-004: `recommendation_id` живёт
   через deep link bot DM → Mini App до booking creation, потеря →
   `unattributed`? *(принять / уточнить параметры гарантий)*

**Резюме blocking-вопросов (2026-07-29, UX-REFINE-001; подтверждено UX-MERGE-001):**
OQ-REC-1 решён owner в редакции displayable; открытые blocking-вопросы без
изменений — **OQ-REC-4** (обязательные поля карточки) и **принятие CANON**
(Ayla MVP Recommendation Contract v0.3) как единого recommendation-контракта.

**Итоговый вопрос:** принять ли CANON (Ayla MVP Recommendation Contract v0.3)
как единый recommendation-контракт, а `contracts/recommendation-ux-addendum.md`
— как UX-facing constraints к нему (не контракт), с правками по ответам на
вопросы 2–7 (вопрос 1 уже решён owner 2026-07-29 в редакции displayable)?
*(принять / отклонить / принять частично)*

## Affected artifacts

- `contracts/recommendation-ux-addendum.md` — после ревью: draft → **accepted**
  как UX addendum к CANON (с правками по ответам владельца); предложение о
  переносе displayable-правила в CANON §13 — через owner CANON (recon,
  действие 1).
- SCR-CUST-004 — required data и acceptance по вопросам 1–2.
- SCR-CUST-005 — коды состояний и переходы по вопросам 1, 6.
- SCR-CUST-006 — передача `recommendation_id` в booking по вопросу 7.
- `gaps/UX-GAP-0104.md` — закрывается после ответа на оставшийся
  blocking-вопрос (OQ-REC-4), решений Recommendation Owner (OQ-REC-2/6/7) и
  переноса displayable-правила в CANON §13; OQ-REC-1 решён owner 2026-07-29
  (редакция displayable).

## Changelog

- 2026-07-29 — UX-MERGE-001: проведён reconciliation (UX-RECON-001, вердикт —
  вариант B); UX draft переписан в `contracts/recommendation-ux-addendum.md`
  (UX-facing constraints, не контракт; дубли заменены ссылками на CANON,
  конфликты C1/C2/C4 исправлены, C3 — пометка о переносе в CANON §13).
  Blocking-вопросы без изменений: OQ-REC-4 + принятие CANON. Обновлены
  контекст, итоговый вопрос и affected artifacts под структуру «CANON +
  addendum».
- 2026-07-29 — UX-REFINE-001: OQ-REC-1 отмечен resolved by owner 2026-07-29
  (редакция displayable explanation); OQ-REC-6 переформулирован (владелец
  классификации displayable vs internal-only — Safety/Trust + Recommendation);
  обновлены вопросы 1 и 6, добавлено резюме blocking-вопросов (остаётся
  OQ-REC-4 + итоговое принятие контракта). Основание: owner ruling 2026-07-29.
