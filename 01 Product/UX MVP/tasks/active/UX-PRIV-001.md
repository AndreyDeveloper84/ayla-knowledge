---
node_id: ayla.ux.ux-priv-001
title: UX-PRIV-001 — MVP Personal Data and Consent Mapping
task_id: UX-PRIV-001
owner: Privacy Owner
type: specification
status: in-progress
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

# UX-PRIV-001 — MVP Personal Data and Consent Mapping

- **task_id:** UX-PRIV-001
- **status:** active (draft-for-privacy-owner подготовлен)
- **created:** 2026-07-29
- **prepared by:** Cross-domain Contract Agent (Privacy/Consent) — UX side
- **addressed to:** Privacy Owner (при необходимости — Legal, трек #947 / CSR-OD-x)
- **basis:** owner decision UX-OD-003 (accepted_as_temporary_assumption, 2026-07-29)

## Goal

Подготовить для Privacy Owner проект минимального контракта «Personal Data and
Consent Mapping» для customer UX Phase 1: отобразить старую consent-модель
SRC-12 (enum `PERSONAL_DATA / PHOTO_BIOMETRIC / MARKETING / HEALTH`, 152-ФЗ
soft-gate) на Consent Scope Registry (CSR, 7 scopes), зафиксировать Phase 1
data boundary (session-only + service_necessity) и сформулировать вопросы,
без ответа на которые контракт не может быть утверждён.

UX не принимает privacy-решений: артефакт содержит только предложения
(proposals) и вопросы (questions). Финальное решение — за Privacy Owner.

## Why now

- Release blocker SRC-01 §10 п. 1: релиз блокирован до перевода scopes
  `intent_understanding` и `provider_selection` из `proposed` в `approved`
  (CSR §10.1). Без решения Privacy Owner этот перевод невозможен.
- Блокирует customer UX copy и экраны Phase 1:
  - **SCR-CUST-001** (welcome) — текст первого касания и notice об обработке;
  - **SCR-CUST-002** — зависит от итоговой welcome-модели;
  - **SCR-CUST-009** (booking create) — точка сбора identity-данных;
  - **SCR-CUST-017** — зависит от модели уведомлений/notice.
- UX-OD-003 зафиксировал временную рамку Phase 1 (session-only, без экрана
  consent на `preference_memory` в W1, revalidation before release = true) —
  теперь её нужно отобразить на нормативную модель CSR и согласовать.

## Target artifact

`docs/ux/contracts/draft-privacy-consent-mapping.md` — Minimal Contract
(proposal) для Privacy Owner: mapping SRC-12 ↔ CSR, Phase 1 data boundary,
предложения по статусам scopes, mandatory notice points, проекты
пользовательских формулировок, open questions, acceptance criteria.

## Scope

- Mapping старой модели SRC-12 (4 enum) на 7 scopes CSR (§5), включая
  выделение отдельного юридического слоя 152-ФЗ baseline.
- Phase 1 data boundary: допустимые данные в session-only по четырём
  разрешённым процессам UX-OD-003 (intent_understanding, provider_selection,
  booking_execution, transactional_booking_support) на основе CSR §4/§5 и
  Data Inventory Matrix.
- Предложение по статусам scopes для Phase 1 / Phase 2 (CSR §10.1/§10.2).
- Mandatory notice points в Phase 1 UX (без отдельного consent-экрана) и
  по одному проекту текста на каждую точку.
- Нумерованные open questions для Privacy Owner / юриста.
- Acceptance criteria для утверждения контракта.

## Out of scope

- Принятие privacy-решений (правовые основания, необходимость baseline
  consent, статусы scopes — только предложения).
- Формулировки и экран согласия на `preference_memory` (Phase 2, CSR §10.2).
- `proactive_recommendation`, `cross_domain_personalization`,
  `recommendation_measurement`, `recommendation_explanation` — остаются
  blocked (CSR §5.3–5.6, §12).
- PHOTO_BIOMETRIC (food scanner), MARKETING, HEALTH consent-флоу — кроме
  фиксации их места в mapping-таблице как out-of-Phase-1.
- Export/forget (AMD-020 C5) — Phase 2+; упоминается только как граница.
- Изменение CSR, Data Inventory Matrix, спецификаций экранов и любого кода.
- Юридический канцелярит в пользовательских текстах.

## Questions to resolve (для Privacy Owner)

Полный список — в разделе «Open questions» артефакта. Ключевые:

1. Сохраняется ли `PERSONAL_DATA` как единый baseline-consent 152-ФЗ
   параллельно со scopes CSR, или заменяется связкой «service_necessity
   (без consent record) + `preference_memory` (explicit consent)»?
2. Достаточно ли notice (без клика-согласия) на welcome и booking create
   для Phase 1, или юрист по треку #947 (Variant A→B) требует жёсткий гейт
   до первого ответа?
3. Подтверждение перевода `intent_understanding` и `provider_selection` в
   `approved` для Phase 1 (условие CSR §10.1 / SRC-01 §10 п. 1).
4. Требуют ли booking_execution и transactional_booking_support
   регистрации отдельных scopes в CSR или покрываются service_necessity
   вне personalization-scopes?
5. Кто и где хранит consent records Phase 1, если они появятся (CSR-OD-5
   открыт)?

## Required output

- Файл `docs/ux/contracts/draft-privacy-consent-mapping.md`, frontmatter:
  `status: draft-for-privacy-owner`, `owner: Privacy Owner`, явная пометка
  «UX не владеет privacy-правилами».
- Объём ≤ 2000 слов; всё, что нельзя обосновать источниками (CSR, DIM,
  SRC-01, UX-OD-003, спеки экранов, AMD-020 C5), — open question, не
  домысливание.

## Do not

- Не утверждать и не менять статусы scopes в CSR — только предложить.
- Не вводить consent-экран на `preference_memory` в W1 (запрещено UX-OD-003).
- Не трактовать продолжение диалога как согласие на память.
- Не обещать в пользовательских текстах память/персонализацию, отключённую
  в Phase 1 (старый копирайт SRC-12 «запомню предпочтения» неприменим).
- Не затрагивать persistent storage, маркетинг, проактив, secondary use,
  health inference.

## Output limit

Draft ≤ 2000 слов. Handoff-сводка ≤ 300 слов.
