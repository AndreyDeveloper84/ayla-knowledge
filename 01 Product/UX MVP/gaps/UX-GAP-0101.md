---
gap_id: UX-GAP-0101
severity: P0
detected_in: UX-CUST-001 (screen inventory customer)
date: 2026-07-29
status: in-progress
gap_status: open
node_id: ayla.ux.gap-0101
title: "UX-GAP-0101 — Consent-модель: scopes Phase 1 не approved; модель SRC-12 расходится с CSR"
type: specification
owner: UX Architecture
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

# UX-GAP-0101 — Consent-модель: scopes Phase 1 не approved; модель SRC-12 расходится с CSR

## annotation (2026-07-29, UX-SYNC-001)

Gap остаётся **open (release blocker)**. Temporary assumption принята
решением UX-OD-003 phase_1_session_only_service_necessity
(accepted_as_temporary_assumption, `decisions/ux-owner-decisions.md`):
Phase 1 = session-only + service_necessity, persistent memory disabled,
явный экран consent на preference_memory в W1 не создаётся. Это снимает
copy-блок с SCR-CUST-001 и session-only частей SCR-CUST-003/009, но НЕ
закрывает gap: approval scopes и mapping 152-ФЗ ↔ CSR по-прежнему требуются
до релиза. Обязательная параллельная задача Privacy Owner — MVP Personal
Data and Consent Mapping — запущена как UX-PRIV-001. UX-OD-003 не заменяет
заключение Privacy Owner/юриста; revalidation required before release.

## description

Две связанные неопределённости:

1. Release blocker SRC-01 §10 п. 1: consent scopes `intent_understanding` и
   `provider_selection` находятся в статусе `proposed` и должны быть переведены
   в `approved` до релиза Phase 1. Формулировки, которые увидит пользователь,
   зависят от финальных scope definitions (Consent Scope Registry §5).
2. Существующие спеки SRC-12 (global-bot-welcome-consent-spec.md,
   customer-booking-confirm-registration-spec.md) построены на иной модели
   consent: enum `PERSONAL_DATA / PHOTO_BIOMETRIC / MARKETING / HEALTH`
   (152-ФЗ soft-gate, Variant A, legal ACK pending). Каноническая модель —
   7 scopes Consent Scope Registry с fail-closed семантикой (SRC-02 этап 3,
   N2). Эти модели не отображены друг на друга.

## why_it_matters

Consent — сквозная P0-зависимость: от неё зависят welcome-копирайт
(SCR-CUST-001), экран запроса согласия (SCR-CUST-002), registration gate
(SCR-CUST-009) и memory controls (SCR-CUST-017). Проектирование текстов и
поведения согласия по устаревшей модели SRC-12 гарантированно потребует
переделки; проектирование по CSR невозможно, пока scopes не approved.

## blocked_screens

SCR-CUST-001 (частично, copy-уровень), SCR-CUST-002, SCR-CUST-009 (частично,
consent-модель gate), SCR-CUST-017

## missing_decision

- Approval scopes `intent_understanding`, `provider_selection` (Phase 1) и
  `preference_memory` (Phase 2) с финальными пользовательскими формулировками.
- Официальный mapping «152-ФЗ baseline consent из SRC-12» ↔ «scopes CSR»:
  является ли PERSONAL_DATA отдельным юридическим слоем поверх CSR scopes или
  заменяется ими.

## required_owner

Privacy Owner (формулировки, mapping) + Product Owner (approval scopes,
SRC-01 §10).

## recommended_artifact

Decision Record (mapping + статусы scopes), затем Minimal Contract —
пользовательские формулировки consent по каждому MVP scope.

## can_use_temporary_assumption

Да, частично.

## temporary_assumption

Проектировать Phase 1 в session-only режиме без явного consent-экрана
(обработка по `service_necessity`, SRC-02 этап 3); consent-экраны выносить в
W2. Тексты согласия не писать до approval scopes.

## acceptance_criteria

- Scopes `intent_understanding`, `provider_selection` имеют статус approved в
  Consent Scope Registry.
- Зафиксирован mapping 152-ФЗ consent ↔ CSR scopes (Decision Record).
- Утверждённые Privacy Owner пользовательские формулировки для каждого scope,
  используемого на customer-экранах.
