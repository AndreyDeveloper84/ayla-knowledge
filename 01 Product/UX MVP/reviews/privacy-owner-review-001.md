---
title: Privacy Owner Review Package 001 — Personal Data and Consent Mapping (Phase 1)
type: specification
status: review
review_status: ready-for-privacy-owner
owner: Privacy Owner
prepared_by: UX-документалист (UX-PRIV-002)
date: 2026-07-29
basis:
  - contracts/draft-privacy-consent-mapping.md (draft, UX-PRIV-001)
  - gaps/UX-GAP-0101.md
  - decisions/ux-owner-decisions.md → UX-OD-003
resolves: UX-GAP-0101 (при полном ответе на Q1–Q10)
node_id: ayla.ux.privacy-owner-review-001
version: "0.1"
domain:
  - consent
system_owner:
  - ayla-user-context
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

# Privacy Owner Review Package 001 — UX-GAP-0101

## Контекст

- Пилот customer UX — 2026-08-15; релизный контур зафиксирован в SRC-01.
- Phase 1 спроектирована session-only по UX-OD-003 (временное допущение, revalidation before release = true): persistent memory отключена, обработка по `service_necessity`, consent-экран не создаётся.
- Без ответа Privacy Owner UX-GAP-0101 остаётся release blocker (SRC-01 §10 п. 1): scopes `intent_understanding` и `provider_selection` в статусе `proposed`, mapping 152-ФЗ ↔ CSR не зафиксирован.

## Decision summary — что предлагается принять

- **P1. Mapping.** `PERSONAL_DATA` из SRC-12 сохранить как отдельный юридический слой 152-ФЗ baseline (notice + правовое основание) **поверх** scopes CSR, а не заменять им scopes. Runtime-гейтинг идёт по scopes, не по enum. Остальные три enum (PHOTO_BIOMETRIC, MARKETING, HEALTH) — вне Phase 1 (draft §1).
- **P2. Approval scopes.** Перевести `intent_understanding` и `provider_selection` из `proposed` в `approved` для Phase 1 (draft §3).
- **P3. `preference_memory` — строго Phase 2.** Отдельный момент explicit consent, формулировки — отдельно, после закрытия CSR-OD-5. В Phase 1 UX никаких обещаний памяти (draft §3).
- **P4.** Четыре blocked-scope (`proactive_recommendation`, `cross_domain_personalization`, `recommendation_measurement`, `recommendation_explanation`) — без изменений (draft §3).
- **Трёхуровневая модель информирования (owner ruling 2026-07-29).**
  Вводятся три уровня вместо двух: **Transparency → Notice → Consent**.
  Не каждое информирование является Notice, и не каждый Notice требует
  Consent. Для Phase 1: Transparency — политика / «что Ayla умеет» (пассивная
  доступность); Notice — SCR-CUST-001 (welcome-строка) и SCR-CUST-009
  (booking create), без клика-согласия, с проектами текстов N1/N2;
  Consent — только scope-требующие операции, первый момент — Phase 2
  (`preference_memory`). Классификация точек — предложение, подтверждается
  Q10 (draft §4.1–4.3, §5).

## Why it matters

Ответ на этот пакет разблокирует: **SCR-CUST-001 copy** (финальный welcome-текст + notice), **SCR-CUST-002** (зависит от итоговой welcome-модели), **SCR-CUST-009** (notice при сборе identity-данных), **SCR-CUST-017** (зависит от модели уведомлений). Без ответа релиз блокирован двойно: approval scopes (SRC-01 §10 п. 1) и незафиксированный mapping делают бессмысленным любой copy по consent — он гарантированно пойдёт на переделку.

## Рекомендации по критичным вопросам (Q1–Q3, blocking)

### Q1 — Baseline-слой 152-ФЗ

- **Recommended:** A — сохранить `PERSONAL_DATA` как отдельный baseline-слой поверх scopes CSR. Обоснование: спеки SRC-12 и правовое основание уже построены на этом слое; разрыв потребует переписывания спек и повторного legal review без выигрыша для Phase 1.
- **Alternatives:** B — формально заменить baseline связкой «service_necessity (без consent record) + preference_memory (explicit consent, Phase 2)».
- **Risks:** при A — параллельные модели требуют поддерживать mapping-таблицу актуальной; при B — ломаются спеки SRC-12 и теряется явное правовое основание для booking-обработки до Phase 2.

### Q2 — Notice vs жёсткий гейт (с учётом трёх уровней)

- **Recommended:** A — достаточно уровней **Transparency + Notice** (draft
  §4.1–4.3, §5) без Consent-момента для session-only + booking; Variant A
  soft-gate остаётся. Обоснование: UX-OD-003 запретил consent-экран в W1, а
  обработка session-only не выходит за service_necessity; жёсткий гейт
  (Consent до первого ответа) ломает core-флоу диалога.
- **Alternatives:** B — жёсткий гейт (Variant B по треку #947): согласие
  (Consent-уровень) до первого ответа бота.
- **Risks:** при A — юрист по треку #947 может флипнуть A→B позднее, что
  потребует вставки гейта; при B — блокируется весь диалоговый вход пилота и
  противоречит принятому UX-OD-003.

### Q3 — Approval scopes

- **Recommended:** принять P2 — `approved` для `intent_understanding` + `provider_selection`. Обоснование: оба scope имеют basis `service_necessity` без consent record для session use (CSR §5.1/§5.2); persistent memory технически off, dependent authorization на `preference_memory` не активируется; runtime contract fail-closed (CSR §6).
- **Alternatives:** отложить approval до полного закрытия всех CSR-OD.
- **Risks:** откладывание = гарантированный срыв пилота (SRC-01 §10 п. 1 — блокер); поспешный approval несёт риск только при включении persistent-контура, который в Phase 1 технически выключен.

## Exact owner questions (Q1–Q10)

**Blocking (Q1–Q3):**

1. **Q1.** Принять вариант A (`PERSONAL_DATA` — отдельный baseline-слой 152-ФЗ поверх scopes CSR) или вариант B (заменить baseline связкой service_necessity + preference_memory)? *(выбрать A/B)*
2. **Q2.** Подтвердить, что для Phase 1 достаточно уровней Transparency + Notice без Consent-момента (без клика-согласия; Variant A soft-gate сохраняется, флип #947 A→B к Phase 1 не применяется, Consent-уровень не вводится)? *(принять / отклонить)*
3. **Q3.** Подтвердить перевод `intent_understanding` и `provider_selection` в `approved` для Phase 1 (P2)? *(принять / отклонить)*

**Informational / Phase 2 (Q4–Q10):**

4. **Q4.** Зафиксировать, что `booking_execution` и `transactional_booking_support` покрываются `service_necessity` вне personalization-scopes CSR, или требуется регистрация отдельных scopes? *(выбрать A/B; рекомендация draft — A с явной фиксацией)*
5. **Q5.** Сохранять ли `PERSONAL_DATA` consent на экране customer-booking-confirm в Phase 1, если persistent memory там отключена? (зависит от Q1) *(принять / отклонить / уточнить параметр — текст предложения)*
6. **Q6.** Подтвердить, что `MARKETING` / Marketing Opt-Out не активируется в Phase 1 и UX-точек не требует? *(принять / отклонить)*
7. **Q7.** Подтвердить, что границы Data Inventory Matrix (draft) применимы к Phase 1 контракту до её approval? *(принять / отклонить)*
8. **Q8.** Допустимо ли, что команды просмотра/отзыва согласий (CSR §8) отсутствуют в Phase 1 (нет granted scopes) и появляются только в Phase 2? *(принять / отклонить)*
9. **Q9.** Если по Q1/Q5 consent record в Phase 1 появится — указать место хранения до закрытия CSR-OD-5 (canonical SoR)? *(уточнить параметр — где хранится)*
10. **Q10.** Подтвердить классификацию точек информирования по уровням Transparency → Notice → Consent (draft §4.2): welcome (SCR-CUST-001) — Notice, booking create (SCR-CUST-009) — Notice, политика/«что Ayla умеет» — Transparency, Consent — только Phase 2? *(принять / скорректировать уровень точки)*

## Affected artifacts

- `docs/ux/contracts/draft-privacy-consent-mapping.md` — исходный draft (P1–P4, N1/N2, Q1–Q10).
- `docs/ux/gaps/UX-GAP-0101.md` — gap record, закрывается при полном ответе.
- `docs/ux/decisions/ux-owner-decisions.md` — UX-OD-003 переводится из `accepted_as_temporary_assumption` в финальное решение после ответа (acceptance criteria draft §8).
- Consent Scope Registry — статусы двух scopes (меняет владелец CSR по решению Privacy Owner).
- Спеки SRC-12 (welcome/registration) — судьба определяется ответом на Q1.
- Экраны SCR-CUST-001, 002, 009, 017 — разблокировка copy/поведения.

## Полный draft

Все обоснования, mapping-таблица, data boundary, проекты текстов N1/N2 и acceptance criteria — в `docs/ux/contracts/draft-privacy-consent-mapping.md` (§1 mapping, §2 data boundary, §3 статусы scopes, §4.1–4.3 трёхуровневая модель и notice-точки, §5 тексты, §6 граница Phase 2, §7 open questions, §8 acceptance criteria).

## Changelog

- 2026-07-29 — UX-REFINE-001: decision summary приведён к трёхуровневой
  модели Transparency → Notice → Consent (owner ruling 2026-07-29); Q2
  переформулирован с учётом трёх уровней; добавлен Q10 (классификация точек
  по уровням, informational — blocking-статусы не менялись).
