---
node_id: ayla.knowledge.audit-full-kb-canon-v2-2026-08-19
title: Full KB Canon Audit V2 — 2026-08-19
type: specification
status: draft
canonical_status: draft
version: "1.0"
owner: Canon Architect / Knowledge Base Auditor (agent)
knowledge_area:
  - foundation
domain:
  - cross-domain
concerns:
  - governance
  - audit
system_owner:
  - ayla-knowledge
source_repository: ayla-knowledge
created: 2026-08-19
updated: 2026-08-19
source_kind: canonical
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: sanitized
review_cycle: event-driven
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Knowledge Architecture Specification]]"
  - "[[Ayla Knowledge Area Taxonomy]]"
---

# Full KB Canon Audit V2 — 2026-08-19

Режим: READ-ONLY. Канонические документы, metadata, статусы, ADR/Decision Log не изменялись. Commit/push не выполнялись. Полный машинный inventory: `docs/audits/2026-08-19-full-kb-canon-audit-v2.json`.

Git baseline: branch `main`, HEAD `e37df2e feat: complete Memory Model Wave 2B`; 7 modified + 24 untracked paths (pre-existing, не тронуты).

## 1. Executive Summary

Проиндексировано 230 содержательных Markdown-документов (+3 machine-readable contract-файла `03 AI System/Contracts/`, +2 infra-файла `.knowledge/`). Каждому документу присвоен effective status; построены dependency/decision/ownership/SoT/superseding графы; семантическое сравнение выполнено только между связанными документами.

Главный ответ на вопрос аудита: **текущая KB не может использоваться как согласованный Source of Truth без оговорок**. Ядро канона (Constitution → BOT-001/002/CDP-001; Memory/Conversation Models; Master MVP frozen set) согласовано и трассируемо, но governance-уровень содержит дефекты, ломающие трассировку решений: два decision ledger'а с общим ID-пространством и подтверждённой коллизией `AYLA-DEC-0026`; действующие решения, противоречащие друг другу без записи о разрешении (клиентская онлайн-оплата); approved-документы, не амендированные после принятых owner decisions (Reset Roadmap, Documentation Roadmap); инвертированная канонизация (downstream CANONICAL при upstream candidates).

Findings: P0 ×1, P1 ×6, P2 ×10, P3 ×2. Canon blockers: 4. Owner decisions required: 6.

**Вердикт: C — KB PARTIALLY CANONICAL.**

## 2. Governance Baseline

```text
canonical statuses:      schema lifecycle (idea→draft→review→approved-with-amendments→approved→implemented
                         + cancelled/blocked/deprecated/superseded/archived) — SoT: .knowledge/schema.yaml;
                         canonical_status enum (draft/candidate/approved/deprecated);
                         Active Canon = source_kind canonical + status ∈ {approved, approved-with-amendments,
                         implemented, delivered}; одна Active Canon на node (DMR §12, Variant C, CFT-001).
candidate statuses:      canonical_status: candidate; процессные: CANDIDATE FOR CANON REVIEW (PDP §6.2),
                         READY_FOR_OWNER_REVIEW (CANON_INDEX), CANDIDATE FOR PRODUCT OWNER REVIEW
                         (оба governance-стандарта; вне вокабуляра PDP §6.2 — рассинхрон).
historical/handoff:      SUPERSEDED / LEGACY / SUPERSEDED_PENDING_REAPPROVAL (CANON_INDEX; последний
                         использован, но не объявлен допустимым); deprecated/archived (DMR);
                         handoff определён в Glossary §17 (временный, не замена spec/ADR).
acceptance rules:        (a) window-путь: authoring → review → READY_FOR_OWNER_REVIEW → owner approval →
                         CANONICAL присваивает оркестратор (CHARTER, CANON_INDEX); (b) PDP 10 фаз:
                         TRACEABILITY CLEAN + ARCHITECTURE READY FOR WRITER + Canon Review READY FOR CANON
                         → Canonicalization «under Ayla's normal approval rules» (PDP §3.10 — единым блоком
                         нигде не определены; GAP).
owner rules:             Product Owner — sole approver Product decisions (PDP §4); изменение Конституции —
                         founder approval + профильные заключения; CANONICAL только после owner approval.
dependency rules:        implements/depends_on/adr/related/conflicts_with/supersedes; directed, acyclic,
                         target must exist (KAS §7; DMR §7); conflicts_with требует resolution note.
superseding rules:       supersedes только между разными логическими документами; прежняя редакция —
                         не Knowledge Node, живёт в Git history (KAS §3.1–3.2); более новая дата ≠ приоритет.
decision rules:          AYLA-DEC-XXXX; Decision Log (02 Strategy) хранит 0001…0025(+0026,0035);
                         OWNER_DECISION_REGISTER хранит 0026…0079; граница — историческое примечание,
                         не нормативное правило; OD — только после 6-шаговой лестницы (CFT register).
ADR rules:               type adr с adr_id/decision_status/revision/amendments/superseded_by (DMR §6);
                         изменения — через owner decision или ADR + impact analysis + migration plan.
validation entrypoint:   python scripts/validate_knowledge.py (локально + GitHub Actions); renderer:
                         python scripts/render_domain_registry.py --check (DMR из schema.yaml).
source-of-truth hierarchy: Constitution → Product Essence → LDT Manifesto / Vision / Thesis / Principles →
                         MVP Scope → User Journey → Domain Models → UX → Engineering → Implementation
                         (CANON_WORKSTREAM_STATUS; Essence §21). Knowledge-SoT: schema.yaml → DMR → Glossary.
                         Knowledge Area Taxonomy: 00 Foundation, 01 Product, 05 Architecture, 06 Product,
                         07 UX, 08 Engineering, 09 Operations + Strategy/Governance как responsibilities.
```

GOVERNANCE_DEFECT (governance сам противоречив): см. KB-001, KB-005, KB-018; дополнительно зафиксировано: статусные вокабуляры множатся (schema vs KAT §8 vs CANON_INDEX vs PDP §6.2 — PDP запрещает invent statuses, governance их изобретает); оба governance-стандарта (Canon Review Standard, PDP) — draft/candidate, но по ним уже канонизированы BOT-001/002, CDP, Master MVP set; KAS §4 (04 Domain Models/07 Design/08 Business/…) vs KAT §3 (06 Product/07 UX/…) vs schema `knowledge_area` enum (нет `ux`, есть `design`) — три несовместимые карты областей; DMR `provisional_system_owner.allowed_until: 2026-08-15` — срок истёк, правило не пересмотрено.

## 3. Inventory Summary

| Срез | Файлов | Преобладающий effective status |
|---|---|---|
| 00 Foundation (+Canon Governance, windows) | 28 | CANONICAL 4 / CANDIDATE 9 / DRAFT-PROPOSED 4 / HISTORICAL 8 / REFERENCE 3 |
| 01 Product (+UX MVP) | 38 | CANONICAL 4 / CANDIDATE 5 / DRAFT (UX MVP рабочий слой) ~22 / HANDOFF ~7 |
| 02 Strategy | 10 | CANONICAL 3 / CANDIDATE 3 / DRAFT 3 / PROPOSED 1 |
| 03 AI System | 1 (+3 data) | CANONICAL 1; appendices DRAFT |
| 05 Architecture | 16 | CANONICAL 4 / DRAFT-PROPOSED 12 |
| 06 Product | 1 | CANON_CANDIDATE |
| 06 Safety and Governance | 2 | CANONICAL 1 / DRAFT 1 |
| 07 UX | 6 | CANON_CANDIDATE формально; де-факто FROZEN (DEC-0026) |
| 99 Archive/proposals | 6 | HISTORICAL 5 / PROPOSED-stale 1 |
| docs (+temp) | 19 | HANDOFF 19 (12 из них misclassified как source_kind: canonical) |
| UX Agents | 100 | HANDOFF/HISTORICAL ~92 / REFERENCE 8 |
| Корень (Ayla.md, README, approved_v1_1) | 3 | REFERENCE 1 / REFERENCE 1 / SUPERSEDED 1 |
| **Итого** | **230** | (.pytest_cache/README.md — не KB, не индексирован) |

Effective status totals: CANONICAL 18 · CANON_CANDIDATE ~17 · DRAFT/PROPOSED ~45 · REFERENCE ~15 · HANDOFF/HISTORICAL ~130 · SUPERSEDED 4 · UNKNOWN 0.

## 4. Canon Map

```text
[C] Ayla Constitution v2.2
 └─ [C] Knowledge Area Taxonomy v1.0        [K] Knowledge Architecture Spec v1.4 (pending-infrastructure)
 └─ [K] Product Essence v1.2 ── [K] LDT Manifesto v1.1
     ├─ [K] Product Vision v2.1 ─ [K] Product Thesis v0.6 ─ [K] Product Principles v0.2
     └─ [K] MVP Scope & Release Contract v0.4  ← де-факто release boundary
         ├─ [C] MVP User Journey Spec v1.2   (alignment gate к DEC-0063…0066 ОТКРЫТ)
         │    └─ [S] approved_v1_1.md (v1.1, superseded; лежит в корне — нарушение versioning rule)
         │    └─ [?] полная User Journey Spec v1.2 (review; REFERENCE, booking.* / Concierge — stale)
         ├─ [C] MVP Reset Roadmap v1.0  ⚠ не амендирован после OD-MVP-1…4 (KB-004)
         ├─ [C] MVP Documentation Roadmap v1.1 ⚠ booking-терминал, Killer PRD в цепочке (KB-004)
         ├─ [D] Single-Provider / Multi-Provider Execution Scopes
         ├─ [C] Intent Model Spec v1.0 (+[D] machine appendices 03 AI System/Contracts)
         ├─ [C] Conversation Model Spec v1.0 ← AYLA-DEC-0055…0062
         ├─ [C] Memory Model Spec v1.0 ← AYLA-DEC-0067…0079 ([D] ADR-0012 — fenced policy layer)
         ├─ [D] Core Domain Model v1.3 / [D] Domain Context Map v1.0 / [D] Domain Event Registry v0.5
         ├─ [D] MVP Appointment Contract v1.1-draft (§5A/§5B — canonical semantics)
         ├─ [D] MVP Recommendation Contract v0.3 (displayable rule вне него — KB-007)
         ├─ [C] Master MVP Auth & Authority + [C] MVP Customer Resolution (FROZEN, DEC-0026)
         ├─ [K] Salon Operations MVP Contract v0.1
         └─ 07 UX ×6 [K формально / FROZEN де-факто] ← Master MVP set
Product Canon: [C] Product Canon Index → [C] BOT-001 · [C] BOT-002 · [C] CDP-001 · [K] BOT-003 (blocked §20)
Governance: [C] CHANGELOG · [C] Quality Bar · [K] Canon Review Standard · [K] PDP · [R] CANON_INDEX ·
            [R] CANON_WORKSTREAM_STATUS · [R] CANON_CONFLICT_REGISTER · [R] OWNER_DECISION_REGISTER
Decisions: [C] Ayla Decision Log v1.10 (0001…0026, 0035) ‖ [R] OWNER_DECISION_REGISTER (0026…0079) ⚠ KB-001
```

## 5. Coverage Matrix

| Area | Canon Source | Status | Owner | Blockers | Coverage |
|---|---|---|---|---|---|
| Foundation | Constitution, KAT | [C]/[K] | Founder/Product Owner | KB-001, KB-005 | PARTIAL |
| Strategy | Decision Log, Scope v0.4, Thesis | [C]/[K] | Product Owner | KB-002, KB-003, KB-004 | CONFLICTING |
| Product | Canon Index, BOT-001/002, CDP-001 | [C] | Product Owner | — | COMPLETE |
| Journey | MVP UJS v1.2 | [C] | Product Owner | KB-005 (alignment gate) | PARTIAL |
| Intent | Intent Model Spec v1.0 | [C] | AI Architecture | — (appendices draft) | COMPLETE |
| Domain | Memory Model, Conversation Model [C]; CDM/ContextMap/DER [D] | mixed | Domain Architecture | KB-009, KB-010 | PARTIAL |
| Customer UX | UX MVP screens/flows (draft) | [D] | UX Architecture | KB-007, KB-016 | PARTIAL |
| Master/Salon UX | 6 контрактов 07 UX (frozen) | [FROZEN] | UX Architecture | — (KB-016 design evidence) | COMPLETE |
| Booking | MVP Appointment Contract (draft; §5A/§5B canonical semantics) | [D] | Product Architecture | KB-011 | PARTIAL |
| Availability | DEC-0021 + CDM §7.10; command/event names — только в archive brief | [C]-decision | CAP-010 | KB-017 | PARTIAL |
| Recommendation | RC v0.3 (draft) + DER registered events | [D] | Product Architecture | KB-007, KB-009 | PARTIAL |
| Memory | Memory Model Spec v1.0 | [C] | Domain Architecture | — (ADR-0012 слой draft) | COMPLETE |
| Consent | CSR v1.2 (approved; scopes intent_understanding/provider_selection proposed) | [C] | Privacy Owner | CSR-OD-5, KB-008 | PARTIAL |
| Privacy | DIM (draft), AMD-001 (blocked) | [D] | Privacy Owner | KB-008, KB-011 | PARTIAL |
| Safety | Constitution, Quality Bar; MVP Safety Policy НЕ материализована | — | Safety Owner | KB-017 | PARTIAL |
| Health | Scope §6.1 (candidate); ADR-0012 OD-1 (legal pending) | [K] | Product Owner | ADR-0012 OD-1/OD-2 | PARTIAL |
| AI Behaviour | CDP-001, BOT-001/002 | [C] | Product Owner | — | COMPLETE |
| Prompting | не найдено канонического документа (Prompt Canon — planned) | — | не назначен | — | MISSING |
| Tools | Tool Schema Registry — planned (упоминания в RRM/RC) | — | не назначен | — | MISSING |
| Architecture | RRM (proposed), ADR-0012/13/14 (proposed) | [D] | Platform Architecture | OD-RRM-1…7 | PARTIAL |
| Data | DIM v1.0 (draft) | [D] | Safety & Governance | KB-008 | PARTIAL |
| API Boundaries | Master MVP contracts [C]; Appointment/RC drafts | mixed | Domain Architecture | KB-011 | PARTIAL |
| Cross-Repo | RRM write authority (Proposed); breaking-change policy не утверждена | [D] | Platform Architecture | OD-RRM-1…7 | PARTIAL |
| Analytics | Analytics Event Contract — planned; CSR audit-имена не зарегистрированы в DER | — | не назначен | KB-010 | MISSING |
| Monetization | DEC-0001/0007/0008/0010/0032 + конфликт оплаты | [C]-decisions | Founder | KB-002 | CONFLICTING |

## 6. Dependency / Ownership Integrity

- **Циклы зависимостей:** не обнаружены (depends_on/supersedes граф ацикличен по индексу).
- **Неразрешённые ссылки:** Glossary → 7+ несуществующих документов (Event Taxonomy, Booking Lifecycle Specification, Memory Entry Schema, Recommendation Engine Specification, Safety and Boundary Specification, Analytics Event Taxonomy, Core User States) + ADR-0007/ADR-0009 как unresolved — validator warnings (20).
- **Wrong-direction dependencies (approved → draft):** Master MVP Auth + Customer Resolution [C] зависят от MVP Appointment Contract [D]; CSR [C] зависит от ADR-0012 [D], AMD-020 [proposed], DIM [draft]; Intent Model [C] имеет draft machine-appendices; BOT-003 [K] заблокирован draft RC/Appointment (KB-011).
- **Duplicate ownership (основное):** decision ledger ×2 (KB-001); Knowledge Area Taxonomy ×2 (KB-006); Account/Profile: CDM §12/§22 (Identity & Access CAP-019, confirmed DEC-0016) vs AMD-020 PSR + DIM (User Context Domain/W2) (KB-008); Consent SoT: AMD-020/DIM (Consent Domain) vs CSR (pending CSR-OD-5) (KB-008); Recommendation lifecycle ×4 модели (KB-009); Task definition: BOT-001 vs Glossary (P2, не сведено); First Contact logic: BOT-001 Q6 (MAX Bot owns) vs Glossary (channel adapter) — отложено в Technical Canon (N6 CANON-REV-001); «главная метрика» ×3 (KB-014).
- **Ownership gaps:** Prompt Canon, Tool Schema Registry, MVP Safety Policy, Analytics Event Contract, Measurement Framework — обязательные по upstream (Roadmap/Moat/CSR), не материализованы; владельцы не назначены.

## 7. Decision / ADR Propagation

| Decision | Owner | Affected | Status |
|---|---|---|---|
| AYLA-DEC-0001…0010 (монетизация, каналы, moat, дата пилота) | Decision Log | Scope/Thesis/execution scopes | PARTIALLY_PROPAGATED (DEC-0003 просрочен; DEC-0006 конфликтует — KB-002) |
| AYLA-DEC-0011…0025 (predecessor gate, identity, tenant, offering, availability, reschedule, memory, events) | Decision Log | CDM, DER, CSR, Scope, контракты | PROPAGATED (остаток: availability event names — только в archive, KB-017) |
| AYLA-DEC-0026 (LDT ruling, Register) | OWNER_DECISION_REGISTER | Essence v1.1+, Manifesto | PROPAGATED — но ID перекрыт Decision Log (KB-001) |
| AYLA-DEC-0026 (Master MVP Freeze, Log) | Decision Log / CHANGELOG | 2 контракта, DER v0.5, frozen set | PROPAGATED — та же коллизия (KB-001) |
| AYLA-DEC-0027…0034 (каналы, триггеры, пороги, RCT) | Register только | Scope, Thesis, execution scopes | PROPAGATED по содержанию; ОТСУТСТВУЮТ в Decision Log (KB-001) |
| AYLA-DEC-0035 (C7 оплата в miniapp) | Decision Log (перенумерованная коллизия) | beautygo_backend | CONFLICTING (KB-002) |
| AYLA-DEC-0036 (same-ID reschedule) | Register | UX stages, TSM | PROPAGATED |
| AYLA-DEC-0037…0054 (Journey v1.2) | Register | MVP UJS v1.2 | PROPAGATED |
| AYLA-DEC-0055…0062 (Conversation Model) | Register | Conversation Model v1.0 | PROPAGATED |
| AYLA-DEC-0063…0066 (OD-MVP-1…4) | Register (+ docs/temp источник) | Essence/Vision/Thesis/Principles/Scope v0.4 (кандидаты) | PARTIALLY_PROPAGATED — approved Reset Roadmap & Documentation Roadmap НЕ амендированы (KB-004) |
| AYLA-DEC-0067…0079 (Memory) | Register | Memory Model v1.0 | PROPAGATED (follow-ups: Glossary/DER/RRM — open) |
| UX-OD-001…005 | ux-owner-decisions.md (approved) | UX-слой, CDP (working evidence) | PARTIALLY_PROPAGATED — не зарегистрированы в Decision Log (KB-013) |
| OQ-REC-1 (displayable rule) | owner ruling 2026-07-29 | UX addendum, SCR-CUST-004 | NOT_PROPAGATED в RC §13; BOT-003 recon: «NOT canon» (KB-007) |
| OD-RRM-1…7 | RRM | контракты, Schedule UX | ORPHANED (все Proposed; downstream freeze уже случился) |
| BOT-001 Q1–Q9 / BOT-002 MM-D1–5, PD-01–03 / CDP-01–12 / BOT-003 Q3-Q9 | UX Agents decisions/reports | BOT-001/002, CDP-001 [C]; BOT-003 [K] | PROPAGATED (audit trail BOT-002/CDP — только в reports, KB-017) |
| ADR-0012 (Dynamic User Model) | — | Memory Model (fenced), Glossary (stale «reserved») | PROPOSED, блокирован OD-1/OD-2; словарь несовместим с canonical lifecycle (KB-010) |
| ADR-0013 / ADR-0014 | — | UX-слой | PROPOSED; ADR-0013 дублирует snapshot-механизм RC §7 (KB-009) |
| AMD-001 (C5 export/forget) | — | W2/W3/W4 | DRAFT/BLOCKED (self-assessed Quality Bar FAIL) |
| AMD-020 PSR | — | CDM («confirmed» по proposed источнику), CSR (стэйл «approved») | PROPOSED; ownership-конфликты (KB-008) |

## 8. Semantic Findings

Подтверждённые targeted verification (path → правило):

1. **KB-001 (P0).** `02 Strategy/Ayla Decision Log.md:1479` — «AYLA-DEC-0026 — Master MVP Canon Freeze… 2026-08-18»; `00 Foundation/Canon Governance/OWNER_DECISION_REGISTER.md:52` — «AYLA-DEC-0026 — Living Digital Twin as Ayla's Primary Visual Interface… 2026-07-29» (с примечанием «Decision Log занимает диапазон до 0025», т.е. ID взят как свободный, а Log позже занял тот же). Intent Model ссылается на DEC-0026 как LDT-решение; Master contracts/DER/CHANGELOG — как freeze. Дополнительно: Log не содержит 0027…0034/0036+; Register пропускает 0035 (он — в Log). Трассировка «какое решение имелось в виду» сломана ровно на самых цитируемых решениях.
2. **KB-002 (P1).** `Decision Log:144` (DEC-0006, действует: клиент МОЖЕТ оплатить онлайн опционально) + DEC-0035 (C7, штатный сценарий оплаты в miniapp) vs `Decision Log:456` (DEC-0015 п.4: «Вне MVP остаются: клиентская онлайн-оплата») + `MVP Scope §7:454` (OUT_OF_SCOPE). Записи о разрешении нет; UX-GAP-P1-07 open.
3. **KB-003 (P1).** `MVP Product Thesis §1:64-69` — killer-сценарий/атрибуция «остаются нормативны в Killer PRD» vs `MVP Scope §2:130` — «legacy reference only… не является нормативным источником» + `§12:635` LEGACY_REFERENCE_ONLY. Дополнительно approved Documentation Roadmap держит Killer PRD звеном целевой цепочки.
4. **KB-004 (P1).** `MVP Reset Roadmap` (approved/CANONICAL): обязательные daily-трекеры вода/еда/активность/сон (Sprint 3), LDT-центричный vertical slice, booking-терминал, своя «главная метрика» — против Scope v0.4 (trackers DEFERRED, LDT conditional, терминал — прогресс) и OD-MVP-1…4 (accepted). `MVP Documentation Roadmap §1.2` (approved): сквозной сценарий завершается booking — та же непротянутость. Два approved canonical документа противоречат accepted decisions.
5. **KB-005 (P1).** Инвертированная канонизация: CANON_INDEX — Journey v1.2 / Intent Model / Conversation Model / BOT-001/002 / CDP CANONICAL, при том что родители (Essence v1.2, Vision v2.1, Thesis v0.6, Principles v0.2, Scope v0.4) — candidates, ожидающие Product Owner Final Review; CANON_WORKSTREAM_STATUS регистрирует открытый alignment-gate Journey v1.2 ↔ DEC-0063…0066; MVP UJS цитирует Product Principles v0.1 (superseded v0.2).
6. **KB-007 (P1).** Норма «no displayable explanation → no show» (owner ruling 2026-07-29) живёт только в `01 Product/UX MVP/contracts/recommendation-ux-addendum.md`; действие «перенести в CANON §13» (recon-recommendation-contract-001) не выполнено; BOT-003 canon-reconciliation верифицировал, что правило НЕ канон (MVP UJS OQ №4). UX-экраны enforce'ят норму без нормативного дома.

Остальные — в разделе 16.

## 9. Handoff Leakage

- **Подтверждено:** `docs/KNOWLEDGE_AREA_TAXONOMY.md` — конкурирующий дубликат canonical KAT без frontmatter, с иным lifecycle и самонарушением «competing copies are not allowed» (KB-006). `99 Archive` как единственный носитель: имена availability-событий (`slot_hold.*` и др. — brief DEC-0021 §7), YAML-полевые модели и authorization-таблица reschedule (brief DEC-0022), детальный реестр Offering/Assignment (brief DEC-0020), open Q1/Q5 identity (brief DEC-0016) (KB-017). `UX Agents/reports` как единственный audit trail одобрений MM-D1–D5, PD-01–03, PO-1/2/3 (KB-017).
- **Не подтвердилось (решения проведены в канон):** owner-approved Schedule/Availability/Post-Visit decisions (→ Schedule UX/ADS/MAF/IA + CR-repairs); P0-B1…B4 (→ Auth&Authority, Customer Resolution, Appointment §5B); freeze-декларации (→ ADS §17/SYS §19 + DEC-0026); OD-MVP-1…4 (→ Register DEC-0063…0066 + candidate-редакции); BOT-001 Q1–Q9 (→ BOT-001 v1.0, верифицировано CANON-REV-001).
- **Системное:** 12 handoff-документов `docs/` имеют `source_kind: canonical` (misclassification); внешние источники решений (`D:\Проекты\Ayla\OWNER_RULING_*`, `docs/temp/*`) цитируются каноном, но не являются Knowledge Nodes.

## 10. UX vs Design Evidence

CANON_GAP не зафиксирован для Master/Salon UX: behaviour/states/actions/permissions определены текстово и заморожены (SYS §2: textual contract sufficient). **DESIGN_EVIDENCE_GAP (KB-016, P2):** все 6 owner-approved composites физически отсутствуют в репо; `docs/screens agent salon/` — 4 PNG скриншота VS Code, не design evidence; REPLY_SALON_UX_IMPLEMENTATION_READINESS обусловливает UX handoff 6 mockups + 3 copy strings (C1–C3). Frozen UX не переоткрывался.

## 11. AI / Memory / Prompt Boundaries

Pipeline и владельцы (восстановлено): backend facts → SoR по RRM (proposed) → persistence (CDM §12 SoR-таблица, draft) → retrieval (Memory Model read gate [C] + CSR §6 runtime authorization [C]) → context construction (Conversation Model Context Projection [C]) → memory rendering (Memory Model [C]) → prompt assembly (**владелец не определён — Prompt Canon отсутствует**) → model (Intent Model Output Contract 0.5 [C]) → tools (**Tool Schema Registry отсутствует**) → result (Transaction State Model, draft).

Границы, требуемые upstream canon и отсутствующие: Prompt Canon, Tool Schema Registry, MVP Safety Policy (CAP-014), Analytics Event Contract, Measurement Framework (KB-017/Coverage). Memory boundary — согласована (Memory Model владеет semantics, DER — registration, ADR-0012 fenced как policy layer); остаточное трение словарей ADR-0012 (KB-010). Session/channel boundary — открытый конфликт OQ-12 (KB-012).

## 12. Cross-Repo Contract Boundaries

Проверялись только утверждения KB (код других репозиториев не анализировался). RRM определяет Write Authority Model (READ/PROPOSE/COMMAND/WRITE), SoR-назначения и public contract rules — но все OD-RRM-1…7 **Proposed**: формально KB не имеет утверждённой cross-repo ownership-матрицы, при этом Master MVP canon set заморожен для engineering на её основании. Version compatibility / dependency pins / breaking-change policy / synchronized update policy — не утверждены (объявлены как правила RRM, статус proposed). Schema/prompt/tool-schema ownership — упомянут, не назначен. Утверждение «отсутствие реализации в GitHub» finding'ом не является.

## 13. Traceability

Цепочка WHY→DECISION→REQUIREMENT→CONTRACT восстанавливается для: BOT-001/002/CDP (Q→decision→spec, CLEAN), Memory Model (DEC-0023/24+0067…0079), Master MVP (P0-B→ruling→contracts→DEC-0026), Journey v1.2 (OD-1…18). Разрывы: DEC-0026 двусмыслен (KB-001); DEC-0027…0034 цитируются как «факт», отсутствуя в Decision Log (KB-001); approved Reset/Doc Roadmaps не трассируются к актуальным решениям (KB-004); displayable rule без upstream authority (KB-007); UX-OD-001…005 вне Decision Log (KB-013); availability event names без нормативной регистрации (KB-017); implementation detail как Product Canon не обнаружено (CDP/BOT явно запрещают implementation).

## 14. Stale / Duplicate Authority

Stale: Ayla.md Root MOC (7+ неверных версий, отсутствуют Essence/BOT/Canon Governance); Glossary (planned-документы, ADR-0012 «reserved»); Domain Context Map (`Rescheduled`-статус против DEC-0022; CTX-003 против Memory Domain canon; обновлён 2026-08-17, но старше канона); Capability Registry §3.1 («Intent Model не создан» — CANONICAL с 2026-08-08); полная UJS (`booking.*`, Concierge Mode против UX-OD-002); FOUNDATION windows (approved со stale COMPLETE-статусами); DEC-0003 (дата прошла); DMR provisional deadline 2026-08-15; LDT Manifesto §6/§18 (pin на Essence v1.1); Product Essence §13 vs §9 (внутреннее противоречие candidate-редакции); CSR §9 («AMD-020 approved» — на деле proposed); OWNER_DECISION_REGISTER header «Пуст при инициализации». Duplicate authority — раздел 6.

## 15. Validator Results

- **Entrypoint:** `python scripts/validate_knowledge.py` (KAS §10; локально + GitHub Actions; renderer: `render_domain_registry.py --check`).
- **Результат прогона 2026-08-19:** `Knowledge validation: 130 error(s), 20 warning(s)`, exit code 0. Baseline известен: 130/20 (REPLY_MASTER_MVP_FINAL_GAP_CHECK, 2026-08-16) → **новых ошибок аудит не добавил** (прогон выполнен до создания артефактов; этот отчёт имеет валидный frontmatter).
- **Состав ошибок:** ~100 — missing frontmatter в `UX Agents/**`, `docs/temp/*`, `docs/FINAL MASTER…`, `docs/KNOWLEDGE_AREA_TAXONOMY.md`, `.pytest_cache/README.md`; 13 — missing required fields + неизвестный type `critique-report` (`UX Agents/reports/BOT-002-CRITIC-001-…`); **в содержательных документах:** `unknown document type 'standard'` (Canon Review Standard, PDP), `canonical filename must not contain a version suffix` (те же 2 файла), `unknown document type 'map'` (Conversation Product Map), `concerns: engineering-process` вне enum (Development Discipline). Warnings: unresolved wikilinks/related/adr targets (Glossary, DMR, полная UJS).
- **WHAT VALIDATOR CHECKS:** наличие/enum-required frontmatter-полей, зарегистрированные document types, правила имён файлов/node_id, разрешимость relationship targets, уникальность node_id/title среди Active Canon (Variant C), conditional rules, required sections по типам.
- **WHAT VALIDATOR DOES NOT CHECK:** семантические конфликты правил, согласованность frontmatter↔body (draft vs FROZEN), распространение решений, дубликаты authority, handoff leakage, коллизии ID решений, актуальность (stale). **0 errors не означало бы semantic correctness; текущие 130/20 — стабильный baseline, не исправлялся.**

## 16. P0–P3 Findings

> Полный machine-readable список — в JSON (`findings`). Формат: ID · severity · type — суть → evidence.

- **KB-001 · P0 · GOVERNANCE_DEFECT** — два decision ledger'а с общим ID-пространством; коллизия AYLA-DEC-0026 (LDT ruling ‖ Master MVP Freeze); Decision Log неполон (нет 0027…0034, 0036+), Register пропускает 0035. Evidence: `02 Strategy/Ayla Decision Log.md:1479`, `00 Foundation/Canon Governance/OWNER_DECISION_REGISTER.md:52,83`. Tags: traceability, duplicate_authority. Owner decision: YES. Blocks canonicalization: YES.
- **KB-002 · P1 · SEMANTIC_CONFLICT** — клиентская онлайн-оплата: DEC-0006 + DEC-0035 (разрешают) vs DEC-0015 п.4 + Scope §7 (OUT_OF_SCOPE); разрешения нет. Evidence: `Decision Log:144,456`, `Scope:454`. Blocks implementation (billing): YES. Owner decision: YES.
- **KB-003 · P1 · DUPLICATED_AUTHORITY** — нормативный статус Killer PRD: Thesis §1 (нормативен) vs Scope §2/§12 (legacy reference) vs approved Roadmap (звено цепочки). Evidence: `Thesis:64-69`, `Scope:130,635`. Owner decision: YES.
- **KB-004 · P1 · UNPROPAGATED_DECISION** — OD-MVP-1…4 / DEC-0027 / Scope v0.4 не протянуты в approved `MVP Reset Roadmap` (трекеры, LDT slice, booking-терминал, метрика) и `MVP Documentation Roadmap` (booking-терминал §1.2, Killer PRD в цепочке). Tags: semantic_conflict, stale_knowledge. Blocks canonicalization: YES. Owner decision: YES (amend vs supersede).
- **KB-005 · P1 · GOVERNANCE_DEFECT** — инвертированная канонизация: downstream CANONICAL при upstream candidates; открытый alignment-gate Journey v1.2; MVP UJS цитирует Principles v0.1. Evidence: CANON_INDEX vs CANON_WORKSTREAM_STATUS. Blocks canonicalization: YES. Owner decision: NO (завершить Final Review + alignment).
- **KB-006 · P1 · HANDOFF_KNOWLEDGE_LEAK / DUPLICATED_AUTHORITY** — `docs/KNOWLEDGE_AREA_TAXONOMY.md` — конкурирующая копия canonical KAT (без frontmatter, иной lifecycle); `docs/temp/*` — неканонизированные дубликаты Principles/amendment-планов. Owner decision: NO (triage: удалить/архивировать как handoff).
- **KB-007 · P1 · UNPROPAGATED_DECISION** — displayable rule (OQ-REC-1) не перенесено в RC §13; UX enforce без нормативного дома; recon: «NOT canon». Owner decision: YES (канонизировать или отменить). Blocks implementation (SCR-CUST-004): YES.
- **KB-008 · P2 · OWNERSHIP_CONFLICT** — Account/Profile: CDM (CAP-019, confirmed) vs AMD-020/DIM (User Context Domain/W2); Consent SoT: AMD-020/DIM (Consent Domain) vs CSR (pending CSR-OD-5); CDM помечает ownership «confirmed» по proposed-источнику. Owner decision: уже зарегистрировано (CSR-OD-5; требуется расширить на Account/Profile).
- **KB-009 · P2 · SEMANTIC_CONFLICT** — Recommendation lifecycle: CDM §7.11 (status-lifecycle) vs RC v0.3 (immutable record, projection) vs Context Map CTX-004 vs ADR-0013 snapshot-механизм (дубль RC §7). DER зарегистрировал по RC.
- **KB-010 · P2 · STALE_KNOWLEDGE** — пакет: Context Map (Rescheduled; CTX-003), Glossary (unresolved planned docs; ADR-0012 «reserved»), Capability Registry §3.1, полная UJS (booking.*/Concierge), CSR §9 («AMD-020 approved»), Essence §13 vs §9, Manifesto pin на Essence v1.1, ADR-0012 draft-словарь ≠ canonical Memory lifecycle.
- **KB-011 · P2 · DEPENDENCY_DIRECTION** — approved canon опирается на draft/proposed (Master contracts→Appointment draft; CSR→ADR-0012/AMD-020/DIM; Intent appendices draft; BOT-003 §20 blocker).
- **KB-012 · P2 · SEMANTIC_CONFLICT** — Session boundary: Conversation Model (channel-scoped Session) vs Intent Model (handoff ≠ новый resolution) vs CSR (session validity); зарегистрировано как OQ-12. Owner decision: уже зарегистрировано.
- **KB-013 · P2 · TRACEABILITY** — UX-OD-001…005 (approved в UX-слое) не зарегистрированы в Decision Log (next_tasks не выполнено).
- **KB-014 · P2 · DUPLICATED_AUTHORITY** — три «главные метрики» (WCHA / killer outcome / Reset Roadmap retention) без иерархии. Owner decision: YES.
- **KB-015 · P2 · STALE_DECISION** — DEC-0003 (пилот 2026-08-15) просрочен без amendment; DMR provisional_system_owner дедлайн 2026-08-15 истёк.
- **KB-016 · P2 · DESIGN_EVIDENCE_GAP** — 6 owner-approved composites отсутствуют; handoff обусловлен mockups + copy C1–C3. Не Canon Gap.
- **KB-017 · P2 · HANDOFF_KNOWLEDGE_LEAK** — archive/handoff как единственный носитель действующих правил: availability event names (brief DEC-0021 §7), YAML/authorization reschedule (brief DEC-0022), Offering/Assignment details (brief DEC-0020), audit trail MM-D/PD/PO-1…3 (UX Agents reports), Manual Booking invalidation matrix не verbatim в каноне, отсутствующие обязательные контракты (Safety Policy, Prompt Canon, Tool Registry, Analytics Event Contract, Measurement Framework).
- **KB-018 · P3 · METADATA_HYGIENE** — пакет: frontmatter draft/candidate vs FROZEN (6 UX); `source_kind: canonical` у 12 handoff REPLY_*; mojibake в BOT-003 §3/§13/§18–20 и Operations Screen §11.3/§15; `approved_v1_1.md` в корне (нарушение README versioning rule); AMD-001/AMD-020 naming (node_id `amd020`, footer v0.8.1.1); Register header/0035/updated; Ayla.md MOC stale; validator errors в governance-стандартах (type `standard`, version suffix, type `map`, concerns enum).
- **KB-019 · P3 · PROCESS_DUPLICATION** — MD Communication Protocol vs PDP vs orchestration-v2: конфликт места Monitor/Gatekeeper; протокол без frontmatter и канонического дома.

## 17. Canon Blockers

```text
BLOCKER 1 (= KB-001)
Root cause: два decision ledger'а без нормативного правила разграничения ID-пространства AYLA-DEC-*.
Affected area: Governance / Traceability (вся KB).
Affected documents: 02 Strategy/Ayla Decision Log.md; 00 Foundation/Canon Governance/OWNER_DECISION_REGISTER.md;
  Intent Model; Master MVP Auth; Customer Resolution; DER; CHANGELOG; все документы, цитирующие DEC-0026/0027…0034.
Required action: owner ruling — единый ledger или нормативная граница + перенумерация одной из записей DEC-0026
  + дозапись 0027…0034/0036+ в канонический ledger.
Canonical owner: Product Owner (governance). Owner decision required: YES.

BLOCKER 2 (= KB-002)
Root cause: конфликт действующих решений о клиентской онлайн-оплате без записи о разрешении.
Affected area: Monetization / MVP Scope / Billing implementation.
Affected documents: Decision Log (DEC-0006, DEC-0015, DEC-0035); MVP Scope §7; UX-GAP-P1-registry (P1-07).
Required action: owner ruling (подтвердить OUT_OF_SCOPE и supersede DEC-0006/0035, либо вернуть оплату в scope).
Canonical owner: Product Owner / Founder. Owner decision required: YES.

BLOCKER 3 (= KB-004)
Root cause: accepted decisions (OD-MVP-1…4, DEC-0027, Scope v0.4) не протянуты в два approved canonical документа.
Affected area: Strategy → downstream execution.
Affected documents: 02 Strategy/Ayla MVP Reset Roadmap.md; 02 Strategy/Ayla MVP Documentation Roadmap.md.
Required action: amendment или явный supersede обоих документов после Product Owner Final Review.
Canonical owner: Product Owner. Owner decision required: YES.

BLOCKER 4 (= KB-005)
Root cause: канонизация downstream-документов раньше upstream Final Review; открытый alignment-gate Journey v1.2.
Affected area: Foundation → Product → Journey chain.
Affected documents: Product Essence v1.2, Vision v2.1, Thesis v0.6, Principles v0.2, Scope v0.4 (candidates);
  MVP UJS v1.2, Intent Model, Conversation Model, BOT-001/002, CDP (canonical).
Required action: завершить Product Owner Final Review пакета + Journey alignment pass (зарегистрированный gate).
Canonical owner: Product Owner. Owner decision required: NO (процесс уже определён).

TOTAL CANON BLOCKERS: 4
```

## 18. Owner Decision Queue

```text
OD-AUDIT-001
Question: Какова единая модель реестра решений: слияние OWNER_DECISION_REGISTER и Ayla Decision Log,
  или нормативная граница ID-пространства? Какая из двух записей AYLA-DEC-0026 сохраняет ID?
Why: коллизия подтверждена; трассировка сломана на самых цитируемых решениях.
Existing evidence: Decision Log:1479; OWNER_DECISION_REGISTER:52,83; KAT-007 (открыт).
Options: (a) единый ledger (Decision Log), Register → dashboard-view; (b) разные префиксы ID;
  (c) Register как единственный ledger, Log → архив 0001…0025.
Recommended: (a) + перенумерация freeze-записи в свободный ID с supersedes-примечанием.
Affected documents: Decision Log, OWNER_DECISION_REGISTER, CHANGELOG, Intent Model, DER, Master contracts, KAT-007.
Blast radius: все ссылки на DEC-0026…0079 по KB (десятки документов).

OD-AUDIT-002
Question: Клиентская онлайн-оплата в MVP: окончательно OUT_OF_SCOPE (supersede DEC-0006/DEC-0035) или included?
Why: четыре действующие нормы противоречат; billing implementation заблокирован.
Existing evidence: Decision Log:144,456; Scope:454; DEC-0035; UX-GAP-P1-07.
Options: (a) OUT_OF_SCOPE + supersede DEC-0006/0035; (b) включить C7 в scope с amendment Scope §7.
Recommended: (a) — согласуется с DEC-0015 и Scope v0.4.
Affected documents: Decision Log, Scope Contract, execution scopes, UX-GAP-P1-registry, Single-Provider Scope.
Blast radius: billing epic (~23 SP), W1 capture.

OD-AUDIT-003
Question: Нормативный статус Killer PRD: legacy reference (Scope) или носитель normative definitions (Thesis)?
Why: два canon-кандидата противоречат; approved Roadmap — третья позиция.
Existing evidence: Thesis:64-69; Scope:130,635,929-930; Documentation Roadmap (цепочка).
Options: (a) legacy + перенос действующих определений (qualified_action, attribution) в Thesis/RC;
  (b) canonical approval Killer PRD после разблокировки ADR-0012 OD-1/OD-2.
Recommended: (a).
Affected documents: Killer PRD, Thesis, Scope, Documentation Roadmap, RC, Journey.
Blast radius: attribution/метрики, Measurement Framework.

OD-AUDIT-004
Question: Судьба approved MVP Reset Roadmap и MVP Documentation Roadmap после OD-MVP-1…4: amend или supersede?
Why: оба approved-документа противоречат accepted decisions (трекеры, LDT, терминал journey, Killer PRD).
Existing evidence: Reset Roadmap Sprint 1–4/§10; Doc Roadmap §1.2/§2.1; Scope v0.4 §6; DEC-0063…0066.
Options: (a) targeted amendment; (b) supersede актуальными Scope/execution scopes + archive.
Recommended: (b) для Reset Roadmap (операционный слой устарел структурно), (a) для Documentation Roadmap.
Affected documents: оба roadmap; CANON_INDEX; WORKSTREAM.
Blast radius: downstream execution scopes, Migration Plan.

OD-AUDIT-005
Question: Канонический дом правила «no displayable explanation → no show»: RC §13 или отмена?
Why: UX enforce; recon зафиксировал NOT canon; owner ruling 2026-07-29 не перенесён.
Existing evidence: recommendation-ux-addendum §2; recon-recommendation-contract-001 (C3, действие 1);
  BOT-003 canon-reconciliation §2.4; SCR-CUST-004 state 5.
Options: (a) amendment RC §13; (b) отменить правило и снять с UX.
Recommended: (a).
Affected documents: MVP Recommendation Contract, UX addendum, SCR-CUST-004/005/006, BOT-003.
Blast radius: recommendation presentation + BOT-003 canonicalization.

OD-AUDIT-006
Question: Иерархия «главных метрик»: WCHA (Moat) vs killer outcome metric (Killer PRD) vs retention-цикл (Reset Roadmap)?
Why: три документа называют три разные North Star; Measurement Framework отсутствует.
Existing evidence: Moat Spec §17; Killer PRD §7.1; Reset Roadmap §10; Multi-Provider §23.
Options: (a) одна North Star + иерархия diagnostic metrics; (b) по метрике на фазу с явной картой.
Recommended: (a) с регистрацией в Decision Log.
Affected documents: Moat Spec, Killer PRD, Reset Roadmap, Thesis, Measurement Framework (planned).
Blast radius: вся аналитика пилота.
```

(Не включены как уже зарегистрированные/решаемые без нового решения: CSR-OD-5, OQ-12, OQ-REC-2/4/6/7, Privacy Q1–Q10, KAT-001…007, OD-RRM-1…7.)

## 19. Recommended Repair Order

```text
Step 1: Decision ledger unification (OD-AUDIT-001)
Why now: блокер трассировки; каждый следующий finding ссылается на решения по сломанным ID.
Root findings: KB-001. Affected: Decision Log, OWNER_DECISION_REGISTER, CHANGELOG, KAT-007.
Prerequisites: owner ruling. Owner decision required: YES.
Expected result: один нормативный ledger; DEC-0026 однозначен; 0027…0034/0036+ доступны в каноническом реестре.

Step 2: Payment conflict resolution (OD-AUDIT-002)
Why now: единственный P1, напрямую блокирующий implementation (billing).
Root findings: KB-002 (+KB-014 частично). Affected: Decision Log, Scope, UX-GAP-P1-07.
Prerequisites: нет. Owner decision required: YES.
Expected result: одна действующая норма оплаты; gap P1-07 закрыт.

Step 3: Strategy-layer alignment (OD-AUDIT-003, OD-AUDIT-004, OD-AUDIT-006)
Why now: после ledger fix можно корректно фиксировать amendments; снимает CONFLICTING покрытие Strategy/Monetization.
Root findings: KB-003, KB-004, KB-014, KB-015. Affected: Killer PRD, Thesis, Scope, оба Roadmap, Moat Spec.
Prerequisites: Step 1. Owner decision required: YES.
Expected result: Strategy-слой без действующих противоречий; approved-документы соответствуют accepted decisions.

Step 4: Foundation Final Review + Journey alignment (без нового решения)
Why now: снимает блокер 4; процесс уже определён governance (WORKSTREAM).
Root findings: KB-005, KB-010 (Essence/Manifesto часть). Affected: 6 candidate-документов, MVP UJS.
Prerequisites: Step 3 (Scope v0.4 финален). Owner decision required: NO.
Expected result: upstream CANONICAL ≥ downstream CANONICAL; alignment-gate закрыт.

Step 5: Canon-home для UX-норм + ownership reconciliation (OD-AUDIT-005; CSR-OD-5 расширить)
Why now: разблокирует BOT-003 canonicalization и SCR-CUST-004.
Root findings: KB-007, KB-008, KB-009, KB-013. Affected: RC, UX addendum, CDM, AMD-020, DIM, CSR.
Prerequisites: Steps 1–2. Owner decision required: YES (OD-AUDIT-005).
Expected result: displayable rule в RC §13; единый ownership Account/Profile/Consent; UX-OD зарегистрированы.

Step 6: Hygiene & stale sweep (без owner decisions)
Why now: после содержательных исправлений, одним проходом.
Root findings: KB-006, KB-010, KB-016, KB-017, KB-018, KB-019, KB-011, KB-012 (OQ-12 по существующей очереди).
Affected: docs/ дубликаты, Glossary, Context Map, Capability Registry, Ayla.md, frontmatter UX/REPLY,
  approved_v1_1.md, AMD naming, validator baseline.
Prerequisites: Steps 1–5. Owner decision required: NO.
Expected result: validator baseline ↓ к содержательному минимуму; MOC актуален; handoff помечены/перемещены.
```

## 20. Final Verdict

**C — KB PARTIALLY CANONICAL.**

Обоснование (факты): (1) Согласованные канонические цепочки существуют и проверены: Constitution; Product Canon (BOT-001/002, CDP-001) с полной трассировкой Q→decision→spec; Memory/Conversation Models с зарегистрированными decision-пакетами; Master MVP frozen set с governance record. (2) При этом: подтверждённая коллизия AYLA-DEC-0026 и двойной ledger делают недостоверной ссылку на центральный механизм governance (P0); действующие решения противоречат без разрешения (оплата); два approved canonical документа противоречат accepted decisions; канонизация инвертирована (downstream approved при upstream candidates). Это не «неблокирующий долг» (B), но и не тотальная несогласованность (D): ядру канона можно доверять при условии проверки decision-ссылок по двум реестрам. Вердикт E не применим: состояние определимо, доказательная база полная.
