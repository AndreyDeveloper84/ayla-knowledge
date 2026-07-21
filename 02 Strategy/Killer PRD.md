---
node_id: ayla.strategy.killer-prd
title: Killer PRD v1.1 — Memory-Core Scenario
type: specification
status: draft
decision_status: proposed
version: "1.1"
owner: Product Owner
priority: P0
knowledge_area:
  - strategy
domain:
  - recommendation
  - user-context
concerns:
  - privacy
  - safety
  - explainability
  - governance
system_owner:
  - ayla-recommendation
  - ayla-user-context
  - ayla-conversation
source_kind: canonical
classification: internal
data_sensitivity: medium
data_categories:
  - pii
security_sensitivity: low
ai_indexing: allowed
export_policy: full
created: 2026-07-21
updated: 2026-07-21
review_cycle: before-major-change
depends_on:
  - "[[Ayla Decision Log]]"
  - "[[ADR-0012 Dynamic User Model]]"
  - "[[Ayla User Journey Specification]]"
  - "[[Ayla Constitution]]"
---

# Killer PRD v1.1 — Memory-Core Scenario

> Product Requirements Document. Rework of `PRD_Ayla_Killer_Scenario_v1.0.md` under AYLA-DEC-0002.

| | |
|---|---|
| **Status** | Draft (pending cross-functional review) |
| **Decision status** | Proposed — owner direction recorded; canonical approval pending |
| **Version** | 1.1 |
| **Owner** | Product Owner / W7 (Canon Architect) |
| **Stakeholders** | Recommendation Engine Owner, Privacy/Safety Owner, Conversation Design Owner |
| **Canonical blockers** | ADR-0012 OD-1 (legal ruling on diet/religion sensitivity split) and OD-2 (Privacy/Safety/Legal ruling + amendment ADR-0011 on safety-critical retention) must be closed before canonization or implementation. |

---

## 1. Status and Decision

This document is a **Draft**. The owner direction on the central product thesis — memory as the core of the killer scenario, with food→beauty as one of several equal triggers — is recorded in §2 and §4. Canonical approval and implementation remain blocked pending the cross-functional rulings listed in the frontmatter and in §12.

**Owner decision recorded (2026-07-21):**
> The scenario “food → beauty/wellness recommendation” is fixed as one of several equal contextual triggers. It may be used as the leading demo/example in marketing and onboarding materials, but it does not define the product center, domain model, or implementation priority. The core of the product remains memory-first personalization based on explicitly shared data, confirmed preferences, interaction history, and current context.

---

## 2. Context and Thesis

### 2.1 Problem

Ayla operates in a market where booking itself is a commodity and generic AI memory is already available from large platforms. The only durable differentiation is **contextual personalization that users trust**: Ayla remembers what matters, explains how it uses memory, and converts that memory into a useful next step without hidden commercial bias.

### 2.2 Thesis (AYLA-DEC-0002)

**Memory is the core of the killer scenario.** Food logging, wellness signals, visit history, and explicit preferences are **inputs** to memory, not the product center. The killer moment occurs when Ayla uses legitimately stored, purpose-limited context to make a single, explained, safe recommendation that the user acts on.

### 2.3 Pressure-test from research

Research synthesis (`00-SYNTHESIS.md`, `02-value-prop-validation.md`, `05-competitive.md`) confirms:

- Booking is commodity; YClients/DIKIDI/Alice AI already cover the transaction layer.
- “AI that remembers” is becoming a commodity feature (ChatGPT cross-session memory, Alice “Моя память”).
- The defensible value is **coverage + cross-domain linkage + transparency**, not the raw fact count.
- The window for building switching cost through memory is **12–18 months**.

This PRD narrows the pilot promise from “food-first superapp” to a **memory-first, privacy-visible recommendation experience** with food as one demo trigger.

---

## 3. Definitions

| Term | Definition |
|---|---|
| **Killer moment** | A formal, attributed event in which Ayla issues one primary recommendation using permitted stored memory, shows the user which context was applied, and the user performs a `qualified_action` within the `attribution_window`. |
| **Active user** | A user who has had at least one non-trivial interaction with Ayla in the rolling 7 days preceding the event. Trivial interactions (e.g., a single ignored greeting) do not count. |
| **Qualified action** | A user-initiated, confirmable outcome tied to the recommendation: booking confirmed, guidance accepted and started, safe alternative accepted, or explicit “save for later” with positive feedback. Mere clicks or views do not qualify. |
| **Attribution window** | The time between recommendation presentation and qualified action. Pilot default: 24 hours. A recommendation outside this window is not attributed to the killer moment. |
| **Substantial Recommendation** | A recommendation that materially affects user choice, health, safety, privacy, or spending. It requires verified/declared memory or confirmed user consent; inferred/signal memory alone is not a sufficient basis. |
| **Useful memory coverage** | The share of active users who have the minimal relevant stored context needed for the current scenario. It measures readiness, not created value. |
| **Memory fact count** | Diagnostic count of stored memory entries. It must not be used as an optimization target or team KPI. |

### Allowed and forbidden examples

- ✅ “Пользователь явно сохранил предпочтение вечерних слотов → Ayla предлагает вечернее окно и объясняет, почему.”
- ⛔ “Ayla накопила 50 фактов о пользователе за неделю → это считается успехом продукта.”
- ✅ “Пользователь отсканировал завтрак → Ayla предлагает расслабляющую процедуру как мягкую гипотезу с объяснением и вопросом подтверждения.”
- ⛔ “Ayla вывела дефицит витамина D из фото еды → автоматически рекомендует косметолога без объяснения и без возможности отказа.”

---

## 4. Trigger Scenarios

Food→beauty is **one of four equal trigger scenarios**. In marketing and onboarding it may be shown first because it is vivid and unexpected; in architecture and implementation it has no priority over the others.

### 4.1 Food / nutrition context → beauty/wellness recommendation

**What Ayla may use:** explicitly shared dietary preferences, confirmed allergies, recent food-scan context shared with Ayla for nutrition guidance.

**Safety rule:** A food observation must not automatically become a medical, dermatological, or psychological conclusion. Any recommendation is presented as a soft suggestion with an explanation, and the user can refuse, correct the context, or forbid future use of that signal.

**Example:**
- User scans a heavy meal in the evening.
- Ayla: “Вчера ты упомянул, что вечером часто чувствуешь напряжение в спине. Хочешь, подберу расслабляющую процедуру на завтра?”
- User accepts or declines.

### 4.2 Fatigue / recovery context → relevant care

**What Ayla may use:** explicitly reported state (“устала”, “болит спина”), confirmed preference for recovery procedures, history of accepted recovery recommendations.

**Example:**
- User says “Опять устала после работы”.
- Ayla: “Раньше тебе помогал массаж шеи и спины. Рядом есть окно у Анны сегодня в 19:00. Записать?”

### 4.3 Event preparation → schedule of procedures

**What Ayla may use:** explicitly shared event date, confirmed beauty/wellness preferences, history of visits and timing.

**Example:**
- User says “Через две недели свадьба подруги”.
- Ayla: “До события осталось 14 дней. Если хочешь, могу предложить план процедур с учётом твоих предпочтений и доступных слотов.”

### 4.4 Visit history and preferences → rebooking or master match

**What Ayla may use:** confirmed favorite master, preferred time slots, confirmed service type, booking history.

**Example:**
- User says “Хочу записаться к мастеру”.
- Ayla: “Ты раньше ходила к Марии на маникюр по четвергам. У неё есть окно в четверг в 18:00. Записать?”

---

## 5. Recommendation Composer

The Recommendation Composer is the normative decision pipeline for any Ayla recommendation that uses stored memory. The stages must run in the order below. A candidate eliminated at any stage cannot be revived by later stages.

### 5.1 Stage order

1. **Consent / privacy gate** — Is the required memory stored under a consent_scope that covers this purpose? Is the sensitivity zone compatible with this recommendation? If no, fallback to session-only or ask.
2. **Safety gate** — Does the recommendation contradict safety-critical memory (allergies, contraindications, medical boundaries)? If yes, stop and escalate to S8 Boundary Handling.
3. **Eligibility / availability** — Is the provider/service available at the requested time/location? If no, exclude.
4. **Relevance** — Does the candidate match the current intent and context? If no, exclude.
5. **Preference boost** — Apply confirmed preferences (time, master, service style). Preference must not revive a candidate already excluded by safety, eligibility, or relevance.
6. **Economic-neutrality check** — Ensure organic ranking is independent of Ayla’s commercial benefit.
7. **Top-1 output** — Select and explain the single recommendation.

### 5.2 Examples of elimination at each stage

| Stage | Candidate | Outcome |
|---|---|---|
| Consent/privacy | Recommend using inferred food preference when user has not consented to `proactive_recommendation` scope | Excluded; do not use memory |
| Safety | Recommend shellfish scrub when user has confirmed shellfish allergy | Excluded; escalate to S8 |
| Eligibility | Recommend master who has no slots this week | Excluded |
| Relevance | Recommend nail service for “back pain” intent | Excluded |
| Preference boost | Two equally relevant masters; user prefers evening → evening slot wins | Allowed |
| Economic-neutrality | Higher-commission master is otherwise equal → must not win organic Top-1 | Excluded; if commission flips ranking, flagged for audit |

### 5.3 Economic-neutrality check (testable rule)

- Commission, margin, advertising spend, or provider commercial status **must not increase** the organic recommendation score.
- Sponsored placement, if introduced later, is calculated separately, explicitly labeled, and **does not replace** the organic Top-1.
- Price may be shown and used as a user budget filter, but not as a hidden commercial ranking signal.

**Acceptance test:** Given two candidates identical in safety, eligibility, relevance, and preference fit but different in commission to Ayla, the organic Top-1 must remain the same. Changing commission alone must not flip the ranking.

---

## 6. Killer Moment

### 6.1 Formal definition

A `killer_moment` is an event that satisfies **all five** conditions simultaneously:

1. **One primary recommendation** is issued by Ayla for the current user intent.
2. The recommendation uses **permitted stored memory/context** under an applicable `consent_scope`.
3. Ayla **shows the user which context was applied** (explicit explanation or inline attribution).
4. The user performs a `qualified_action` tied to the recommendation.
5. The action occurs within the `attribution_window` and is linked to the specific `recommendation_id`.

### 6.2 Attribution rules

- Temporal proximity alone is insufficient. The `qualified_action` must reference the `recommendation_id` or an accepted child action derived from it.
- If the user books the same service later without using the recommendation, it is **not** a killer moment.
- If the user declines the recommendation but later returns to the same provider organically, it is **not** a killer moment.

### 6.3 Repeated killer moments

For the weekly per-user metric, repeated killer moments of the same `scenario_type` are counted **at most once per rolling 7 days**. The product is **not** prevented from creating additional useful moments; only the metric caps the count to avoid gaming.

### 6.4 Example

- Ayla: “Ты упоминала, что предпочитаешь вечер, и раньше довольна была расслабляющим массажем у Марии. У неё есть окно сегодня в 19:00. Записать?”
- User: “Да” → booking confirmed within 24 hours.
- Event logged: `killer_moment` with `recommendation_id`, `scenario_type=visit_history`, `context_used=[preferred_time, favorite_master, service_type]`.

---

## 7. Metrics

### 7.1 Metric hierarchy

| Role | Metric | Definition | Target |
|---|---|---|---|
| **Killer Outcome Metric** | `% active users with ≥1 attributed killer moment / rolling 7 days` | Share of active users who experienced at least one killer moment in the last 7 days | ≥ 25% at 60 days post-launch (hypothesis; requires pilot baseline) |
| **Leading Product Metric** | `useful_memory_coverage` | Share of active users who have the minimal relevant stored context for the current scenario | Baseline in pilot; growth target set after Measurement Framework |
| **Diagnostic** | `memory_fact_count` | Count of stored memory entries | Not a target; used only for debugging and capacity planning |
| **Diagnostic** | `proposal_conversion_rate` | Proposals confirmed by user / total proposals shown | Baseline in pilot |
| **Diagnostic** | `rejected_decision_rate` | Proposals rejected by user / total proposals shown | Baseline in pilot; used for anti-spam and cooldown tuning |

### 7.2 Forbidden formulation

- ⛔ “Memory enrichment rate: new facts per week” as a team KPI or success metric.
- ⛔ “Fill rate targets” that incentivize collecting more facts than minimally necessary.

### 7.3 Guiding principle

> `useful_memory_coverage` measures whether the user has the minimal relevant context for the current scenario. It is an indicator of readiness for personalization, **not** proof of created value and **not** artificial lock-in. Coverage without useful recommendations is a failure mode, not a success.

---

## 8. Safety, Privacy, and 152-ФЗ Transparency

### 8.1 152-ФЗ as a visible feature

Transparency is not a footer link. It is a first-class product surface:

- “Что Ayla знает обо мне” — one-tap view of stored memory by category and consent scope.
- “Забыть это” — one-command deletion of a single memory entry or an entire consent scope.
- “Почему ты мне это предложила?” — explanation of which context was used for any recommendation.

### 8.2 Compatibility with ADR-0012 v0.2

| ADR-0012 rule | PRD implication |
|---|---|
| `consent_scope` from versioned registry | Every recommendation must check `consent_scope` (e.g., `provider_selection`, `intent_understanding`, `question_suppression`, `proactive_recommendation`). No ad-hoc scope strings. |
| Inferred/signal memory is not a basis for Substantial Recommendation | Food scan → beauty recommendation must be framed as a soft suggestion, not a medical/cosmetic conclusion. |
| Rejected proposals produce a Decision Record | Rejection is stored as a `ProposalDecision` without the personal value, to prevent re-proposing the same topic and to support audit. |

### 8.3 Food-observation safety rule

A food observation must not automatically become a health, dermatological, or psychological conclusion. The recommendation must:

- be presented as a soft suggestion;
- include the context that triggered it;
- offer an explicit refusal option;
- allow the user to correct the context;
- allow the user to forbid future use of that signal.

---

## 9. Out of Scope

The following are explicitly out of scope for this PRD:

- Detailed Phase 1.5 implementation specifications.
- Concrete implementation of the Recommendation Composer or Memory storage layer.
- Numeric TTL/decay values (deferred to Measurement Framework and ADR-0012).
- Full catalog governance or provider trust model details.
- Medical diagnosis or treatment recommendations.
- Automatic derivation of health conditions from food/wellness signals.
- Final lawful basis wording, consent texts, and retention periods until the corresponding Legal/Privacy decisions are closed (ADR-0012 OD-1, OD-2).

---

## 10. Traceability and Acceptance

| PRD norm | Source | Acceptance check |
|---|---|---|
| Memory is the core; food→beauty is one trigger | AYLA-DEC-0002 | Document review; scenario examples in PRD |
| Four equal trigger scenarios | Owner decision (2026-07-21) | PRD §4 lists four scenarios with equal status |
| Killer moment 5-condition definition | Owner requirements | Event schema includes `recommendation_id`, `context_used`, `qualified_action`, `attribution_window` |
| `% active users with ≥1 killer moment / rolling 7 days` | Owner requirements | Analytics event catalog; dashboard definition |
| `useful_memory_coverage` as leading metric, not North Star | Owner requirements | Metric definition; team KPI sheet excludes `memory_fact_count` as target |
| Repeated killer moment counted once per scenario per 7 days | Owner requirements | Metric aggregation rule; acceptance test |
| Composer stage order | Owner requirements | Recommendation Engine Specification or ADR references this order |
| Economic-neutrality test | Owner requirements; Constitution Ст. IV | Acceptance test: commission change alone does not flip Top-1 |
| Inferred not basis for Substantial Recommendation | ADR-0012 N-04; Journey §5 | QA red-team cases; ranking audit |
| Decision Record for rejected proposals | ADR-0012 OD-10 | Schema review; privacy audit |
| `consent_scope` from registry | ADR-0012 OD-9 | Consent-scope registry exists before feature release |
| 152-ФЗ transparency as visible feature | Constitution Ст. VI, VII; research synthesis | UX mockup review; one-command deletion test |
| Food observation safety rule | Owner decision; Constitution Ст. VIII, XII | Red-team cases; medical/safety review |

---

## 11. Consistency Review

### 11.1 vs Ayla Constitution v2.2

- **Ст. IV (economic neutrality):** Composer includes explicit economic-neutrality check and acceptance test. ✅
- **Ст. VI (minimal necessary knowledge):** Metrics focus on useful coverage, not fact accumulation. ✅
- **Ст. VII (explanation and veto):** Killer moment requires explanation of used context; 152-ФЗ transparency gives one-command deletion. ✅
- **Ст. X (appropriateness):** Proactive recommendations use consent_scope and scenario cooldowns. ✅
- **Ст. XIV (autonomy):** User can refuse, correct, or forbid any signal. ✅

### 11.2 vs Ayla Decision Log

- **AYLA-DEC-0002:** Memory is the core; food→beauty is one trigger. ✅
- **AYLA-DEC-0001 / AYLA-DEC-0004:** No conflict; privacy-first design preserved. ✅

### 11.3 vs Ayla User Journey Specification v1.2

- **§5 Memory Interaction:** Aligned with Memory Proposal flow; inferred/signal not basis for Substantial Recommendation. ✅
- **§6 Proactivity:** Proactive Readiness Gate respected; consent_scope required. ✅
- **§13 Metrics:** `useful_memory_coverage` replaces any fact-count target. ✅

### 11.4 vs ADR-0012 v0.2

- Multi-dimensional memory model is the target reference architecture. ✅
- `consent_scope` registry requirement acknowledged (OD-9). ✅
- Decision Record for rejected proposals acknowledged (OD-10). ✅
- OD-1 and OD-2 are listed as canonical blockers, not bypassed. ✅

### 11.5 vs Wave 0 / pilot contracts

- This PRD does not modify frozen pilot contracts or the 12 green-field contract.
- Implementation of new schema or backfill is marked post-pilot / separate amendment. ✅

### 11.6 Conclusion

No conflicts requiring a stop are identified. Canonization and implementation remain blocked until ADR-0012 OD-1 and OD-2 are closed.

---

## 12. Owner Decisions Required

| ID | Question | Owner direction recorded? | Blocker for canonization? |
|---|---|---|---|
| OD-K1 | Scenario priority: B — four equal triggers, food→beauty as demo example | ✅ Yes | No |
| OD-K2 | Killer moment attribution requires `recommendation_id` linkage | ✅ Yes | No |
| OD-K3 | Economic-neutrality check as testable ranking rule | ✅ Yes | No |
| OD-K4 | `useful_memory_coverage` is leading metric, not North Star | ✅ Yes | No |
| OD-K5 | 152-ФЗ transparency as visible feature | ✅ Yes | No |
| OD-K6 | Medical/health inference from food signals is out of scope | ✅ Yes | No |
| OD-1 (ADR-0012) | Legal ruling on diet/religion sensitivity split | ⏳ Pending legal review | **Yes** |
| OD-2 (ADR-0012) | Privacy/Safety/Legal ruling + amendment ADR-0011 on safety-critical retention | ⏳ Pending cross-functional ruling | **Yes** |

---

## 13. Open Questions

1. **Pilot baseline targets:** What are the baseline values for `useful_memory_coverage`, `proposal_conversion_rate`, and killer-moment rate before setting numeric goals? *(Deferred to pilot data and Measurement Framework.)*
2. **Attribution window tuning:** Is 24 hours the right default, or should it vary by `scenario_type`? *(Design candidate; validate in pilot.)*
3. **Scenario type taxonomy:** Should the four trigger scenarios be formalized as an enum in the analytics schema now, or deferred to Recommendation Engine Specification? *(Suggested: define enum in analytics schema; keep open for refinement.)*
4. **Sponsored placement boundary:** If sponsored placement is introduced post-pilot, which document owns the rule that it cannot replace organic Top-1? *(Suggested: separate Commercial Policy ADR.)*

---

## 14. Change Log

### v1.1 — 2026-07-21

- Reworked from `PRD_Ayla_Killer_Scenario_v1.0.md` under AYLA-DEC-0002.
- Memory established as the core; food→beauty reduced to one of four equal trigger scenarios.
- Removed `memory_enrichment_rate` as a target KPI.
- Added formal 5-condition `killer_moment` definition with `recommendation_id` attribution.
- Split metrics into Killer Outcome Metric, Leading Product Metric, and diagnostics.
- Added normative Recommendation Composer stage order with elimination examples.
- Made economic-neutrality check testable.
- Added 152-ФЗ transparency as a visible feature.
- Aligned with ADR-0012 v0.2: `consent_scope` registry, inferred-not-basis rule, Decision Record for rejected proposals.
- Added explicit out-of-scope items: medical diagnosis, health inference from food signals, final lawful basis/consent/retention until Legal/Privacy closure.
- Added traceability, consistency review, owner decisions, and open questions.

---

**End of document — Killer PRD v1.1**
