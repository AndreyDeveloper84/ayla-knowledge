---
node_id: ayla.ux.current-session-brief
title: Current Session Brief
type: dashboard
status: draft
version: "0.2"
owner: UX Architecture
knowledge_area:
  - product
domain:
  - cross-domain
system_owner:
  - ayla-knowledge
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
review_cycle: event-driven
---

# Current Session Brief

session_goal: Customer MVP Screen Inventory → применение owner decisions (UX-SYNC-001 выполнен) → Screen Contracts (UX-CUST-002) → merge recommendation contract (UX-MERGE-001 выполнен)
current_artifact: docs/ux/02-screen-inventory-customer.md (v0.2); contracts/recommendation-ux-addendum.md (v0.1)
current_section: —

accepted_decisions:
  - AYLA-DEC-0001 (D1): платит специалист (690/990₽/мес + 90₽/запись); пользователь не платит
  - AYLA-DEC-0003 (D3): пилот 2026-08-15, Пенза
  - AYLA-DEC-0004 (D4): канал пилота — MAX-бот + MAX Mini App; Telegram вне scope
  - AYLA-DEC-0006 (D6): онлайн-оплата клиентом опциональна
  - Канал/поверхность inventory: customer (MAX bot DM + Mini App webview)
  - UX-OD-001 (2026-07-29, accepted): minimal_conversational_cancel_and_reschedule — отмена через диалог bot DM; перенос = cancel_then_create_new_booking; stage specs — UX-SPEC-001
  - UX-OD-002 (2026-07-29, accepted): honest_self_service_terminal_fallback — human handoff в MVP не требуется; честный fallback без оператора и без авто-выдачи контактов
  - UX-OD-003 (2026-07-29, accepted_as_temporary_assumption): phase_1_session_only_service_necessity — persistent memory disabled; revalidation before release; не заменяет заключение Privacy Owner
  - UX-OD-004 (2026-07-29, accepted): hybrid_booking_surface — bot DM: compact slots/подтверждение намерения/pending/result/retry; Mini App: календарь/детали/управление; contextual deep link
  - UX-OD-005 (2026-07-29, accepted): records_list_as_phase_1_mini_app_home — home Mini App Phase 1 = SCR-CUST-010

active_gaps:
  - UX-GAP-0000: [CLOSED] источники найдены, индекс построен (00-ux-source-index.md)
  - UX-GAP-0001: [CLOSED→зафиксирован] customer-спеки SRC-12 ревизованы в UX-CUST-001; устаревшее вынесено в DEFERRED
  - UX-GAP-0002 (P2): дом UX-документов — рабочий слой ai-bot-platform/docs/ux/, перенос в ayla-knowledge после owner review
  - UX-GAP-0101 (P0, OPEN, release blocker): consent scopes не approved, mapping 152-ФЗ ↔ CSR; temporary assumption UX-OD-003 принята, Privacy task UX-PRIV-001 запущена
  - UX-GAP-0102 (P0, OPEN): Phase 2 gates; не блокирует Phase 1 при persistent memory disabled (UX-OD-003)
  - UX-GAP-0103: [CLOSED 2026-07-29] ошибка синхронизации — Intent Model Specification v0.9.2 approved (ayla-knowledge, 2026-07-28)
  - UX-GAP-0104 (P0, OPEN): MVP Recommendation Contract; recon выполнен (UX-RECON-001, вариант B), второй SoR устранён — UX draft → contracts/recommendation-ux-addendum.md (UX-MERGE-001); open до решений Recommendation Owner (OQ-REC-2/4/6/7) и переноса displayable-правила в CANON §13
  - UX-GAP-0105: [CLOSED 2026-07-29, owner part] UX-OD-001; stage specs — UX-SPEC-001
  - UX-GAP-0106: [CLOSED 2026-07-29, для MVP] UX-OD-002; human handoff — P1-08 (Later, Operations Runbook)
  - UX-GAP-P1-01: [CLOSED] UX-OD-005; P1-02: [CLOSED] UX-OD-004; P1-03…P1-07 open; P1-08 (NEW, Later): human handoff

files_needed:
  - SRC-01 §3–5, §7, §10
  - SRC-02 Stage 1–14, N1–N9, Memory Interaction
  - SRC-06 список решений
  - SRC-12 frontmatter + оглавления (полный текст — только по необходимости readiness)
  - SRC-16 (CANON Ayla MVP Recommendation Contract v0.3) — для SCR-CUST-004/005/006
  - Ayla Intent Model Specification v0.9.2 (ayla-knowledge) — для Screen Contracts SCR-CUST-003
files_not_needed:
  - salon/master поверхности (provider-*.md, master-*.md, admin-surface-spec.md) — отдельные волны
  - frontAyla (мобильные приложения) — этап 2
  - backend-реализация (код, API-контракты) — не для inventory
expected_output:
  - docs/ux/02-screen-inventory-customer.md (таблица экранов + readiness)
  - docs/ux/handoffs/customer-inventory-handoff.md
  - Gap Records P0/P1 в docs/ux/gaps/

next_tasks:
  - Commit UX-MERGE-001: recommendation-ux-addendum + точечные правки SCR-CUST-004/006, review-001, UX-GAP-0104, source-index (SRC-16); CANON не тронут
  - Wave 1A.2: продолжение Screen Contracts (SCR-CUST-005 — после OQ-REC-4; остальные батчи по design-wave-1a)
  - Recommendation owner review: recommendation-ux-addendum + CANON (OQ-REC-2..7; blocking — OQ-REC-4 + принятие CANON; закрывает UX-GAP-0104); передать owner CANON действия recon 1–3 (перенос displayable-правила в §13)
  - UX-CUST-002: Screen Contracts для Design Wave 1A (17 экранов, батчами: booking path → управление записью → вспомогательные)
  - UX-TXT-016: тексты safety boundary message (SCR-CUST-016, спеки нет)
  - Privacy Owner review: draft-privacy-consent-mapping (Q1-Q3 критичны, release blocker UX-GAP-0101)
  - Регистрация UX-OD-001..005 в Ayla Decision Log (ayla-knowledge, review-gate)
  - Owner Review Package 002: НЕ требуется — блокирующих решений для старта Wave 1A нет
