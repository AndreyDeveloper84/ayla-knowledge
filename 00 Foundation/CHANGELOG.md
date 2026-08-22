---
node_id: ayla.foundation.changelog
title: Ayla Foundation Changelog
type: moc
status: approved
canonical_status: approved
version: "1.0"
owner: Product Owner
knowledge_area:
  - foundation
system_owner:
  - ayla-knowledge
source_repository: ayla-knowledge
source_kind: canonical
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
created: 2026-08-12
updated: 2026-08-18
review_cycle: quarterly
---

# Ayla Foundation Changelog

## 2026-08-19 — KB-001 repair: разрешение коллизии AYLA-DEC-0026

- Collision of `AYLA-DEC-0026` (Living Digital Twin ruling, 2026-07-29 ‖ Master MVP Canon Freeze, 2026-08-18) resolved: the ID stays with the Living Digital Twin decision; the freeze record was renumbered to `AYLA-DEC-0080` in Ayla Decision Log v1.11. Content unchanged; references updated across Master MVP contracts, Domain Event Registry, and review reports.
- Governance rule added to both decision ledgers: one AYLA-DEC-ID = one decision.
- Impact report: `docs/audits/2026-08-19-KB-001-DEC-0026-collision-repair.md`.

## 2026-08-18 — Master MVP Canon Freeze (AYLA-DEC-0080)

- `Ayla Master MVP Auth and Authority Contract` and `Ayla MVP Customer Resolution Contract` became the first Technical Canon specifications to complete the Ayla governance lifecycle (Canon Review per Ayla Canon Review Standard v1.0: READY FOR CANON after one Writer pass).
- `appointment.completed` was registered in the Ayla Domain Event Registry (v0.5) under the early-registration precedent of AYLA-DEC-0022 п. 9; normal completion semantics are normatively defined by Ayla MVP Appointment Contract §5A/§5B.
- The Master MVP canonical set moved from `CANON CLOSURE` to `FROZEN FOR ENGINEERING / CONTROLLED PILOT`; further changes to frozen documents require Change Control (an accepted decision or amendment).
- Governance record: AYLA-DEC-0080 (при регистрации — AYLA-DEC-0026; перенумерован 2026-08-19 из-за коллизии KB-001 с решением Living Digital Twin, которое сохраняет AYLA-DEC-0026); review report: `docs/REPLY_MASTER_MVP_CANON_GOVERNANCE_FINAL_FREEZE.md`.

## 2026-08-13 — Ayla Conversation Design Principles canonicalization

- Ayla Conversation Design Principles became the third Product Specification to complete the full Ayla governance lifecycle.
- It establishes twelve cross-cutting conversational Product invariants, CDP-01–CDP-12, spanning goal-orientation, user control, continuity/truth and outcome-over-activity.
- Future BOT specifications (BOT-003, BOT-004, BOT-005) inherit these principles by reference rather than re-deciding them.
- It passed Independent Canon Review with one Writer remediation pass (4 required corrections) and targeted Canon Verification, reaching `READY FOR CANON`.

## 2026-08-12 — BOT-002 canonicalization

- BOT-002 Conversation Lifecycle Specification became the second Product Specification to complete the full Ayla governance lifecycle.
- It establishes the canonical Product mental model: Conversation → Goal → Task → Current Focus.
- It defines Task completion, Conversation closure and safe resumption freshness at Product level.

## 2026-08-12 — BOT-001 canonicalization

- BOT-001 became the first Product Specification to complete the full Ayla Product Decision Lifecycle.
- The Canon Review Standard was successfully used in production.
- The Product Decision Lifecycle was successfully validated through a complete end-to-end cycle.