---
node_id: ayla.knowledge.audit-full-kb-canon-v2-rerun-2026-08-19
title: Full KB Canon Audit V2 — Rerun (post KB-001 repair) — 2026-08-19
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

# Full KB Canon Audit V2 — Rerun (post KB-001 repair) — 2026-08-19

Режим: READ-ONLY. Канонические документы, metadata, статусы, ADR/Decision Log не изменялись; commit/push не выполнялись. Полный машинный inventory: `docs/audits/2026-08-19-full-kb-canon-audit-v2-rerun.json`.

**Имя артефакта:** промпт предписывает `YYYY-MM-DD-full-kb-canon-audit-v2.md`, но артефакт первого прогона (`2026-08-19-full-kb-canon-audit-v2.md/.json`) уже существует и является датированной доказательной записью, на которую ссылается repair-отчёт KB-001. Перезапись запрещена правилом стабильности evidence; поэтому этот прогон сохранён с суффиксом `-rerun`.

**Git baseline (старт аудита, ~18:52 UTC):** branch `drf-1148/canon-under-version-control`, HEAD `c106161 draft: place governance drafts under version control (DRF-1148)`; 6 modified (residual KB-001 repair: CHANGELOG, OWNER_DECISION_REGISTER, Decision Log, Domain Event Registry, Customer Resolution, Master MVP Auth) + untracked: BOT-003, Master Operations Screen Contract, `docs/`, `UX Agents/`, `.claude/`, `repomix-output.xml`. Pre-existing changes не трогались.

**⚠ Audit-window instability (FACT):** во время аудита (~19:00–22:15) working tree активно менялся параллельным процессом: появились 3 новых architecture-документа (Memory Domain Contract, Context Resolution Contract, Memory and Context Migration Plan — все created 2026-08-19), изменены `Ayla MVP Recommendation Contract` (v0.3→v0.4, файл дописывался в момент чтения: 1116→1499 строк, mtime 22:11), `Consent Scope Registry`, `CANON_INDEX`. Индекс отражает состояние на момент чтения каждого документа; targeted verification выполнялась на состоянии ~22:15. Выводы по RC v0.4 и новым memory-контрактам относятся к этому позднему снимку.

## 1. Executive Summary

Проиндексировано **233 содержательных Markdown-документа** (+3 machine-readable contract-файла `03 AI System/Contracts/`), каждому присвоен effective status; построены dependency/decision/ownership/SoT/superseding графы; семантическое сравнение — только между связанными документами; P0/P1-кандидаты перепроверены targeted re-open.

Главный результат rerun: **P0 коллизия AYLA-DEC-0026 (KB-001) устранена и верифицирована** — Decision Log v1.11 хранит 0001…0025, 0035, 0080; OWNER_DECISION_REGISTER хранит 0026…0079; пересечений и пропусков в объединённом диапазоне 0001–0080 нет; правило «один AYLA-DEC-ID = одно решение» зафиксировано в обоих реестрах. Также в содержании **разрешён KB-007**: правило «нет displayable объяснения → не показываем» перенесено в RC v0.4 §13 (2026-08-19).

Главный ответ на вопрос аудита не изменился по классу, но улучшился по составу: **KB по-прежнему не может использоваться как безоговорочный Source of Truth**. Ядро канона согласовано; остаются: конфликт действующих решений о клиентской онлайн-оплате (P1), два approved-документа, противоречащие accepted decisions (P1), инвертированная канонизация (P1), конкурирующий дубликат KAT в `docs/` (P1), частично нечитаемый canon-candidate BOT-003 (P1), и новый незарегистрированный слой memory/context-контрактов с owner rulings вне реестров (P2).

Findings (активные): P0 ×0, P1 ×6, P2 ×13, P3 ×2. Resolved со вчерашнего прогона: KB-001 (P0), KB-007 (P1). Canon blockers: 3. Owner decisions required: 6.

**Вердикт: C — KB PARTIALLY CANONICAL** (улучшение внутри класса C: устранён единственный P0).

## 2. Governance Baseline

```text
canonical statuses:      schema lifecycle (idea→draft→review→approved-with-amendments→approved→implemented
                         + cancelled/blocked/deprecated/superseded/archived) — SoT: .knowledge/schema.yaml;
                         canonical_status enum (draft/candidate/approved/deprecated);
                         Active Canon = source_kind canonical + status ∈ {approved, approved-with-amendments,
                         implemented, delivered}; одна Active Canon на node (DMR §12, Variant C, CFT-001).
candidate statuses:      canonical_status: candidate; процессные: CANDIDATE FOR CANON REVIEW (PDP §6.2),
                         READY_FOR_OWNER_REVIEW (CANON_INDEX), CANDIDATE FOR PRODUCT OWNER REVIEW
                         (оба governance-стандарта; вне вокабуляра PDP §6.2 — рассинхрон сохраняется).
historical/handoff:      SUPERSEDED / LEGACY / SUPERSEDED_PENDING_REAPPROVAL (CANON_INDEX; последний
                         использован, но не объявлен допустимым); deprecated/archived (DMR);
                         handoff определён в Glossary §17 (временный, не замена spec/ADR).
acceptance rules:        (a) window-путь: authoring → review → READY_FOR_OWNER_REVIEW → owner approval →
                         CANONICAL присваивает оркестратор (CHARTER, CANON_INDEX); (b) PDP 10 фаз:
                         TRACEABILITY CLEAN + ARCHITECTURE READY FOR WRITER + Canon Review READY FOR CANON
                         → Canonicalization «under Ayla's normal approval rules» (PDP §3.10 — единым блоком
                         нигде не определены; GAP сохраняется).
owner rules:             Product Owner — sole approver Product decisions (PDP §4); изменение Конституции —
                         founder approval + профильные заключения; CANONICAL только после owner approval.
dependency rules:        implements/depends_on/adr/related/conflicts_with/supersedes; directed, acyclic,
                         target must exist (KAS §7; DMR §7); conflicts_with требует resolution note.
superseding rules:       supersedes только между разными логическими документами; прежняя редакция —
                         не Knowledge Node, живёт в Git history (KAS §3.1–3.2); более новая дата ≠ приоритет.
decision rules:          AYLA-DEC-XXXX; ПОСЛЕ REPAIR KB-001 (2026-08-19): Decision Log (02 Strategy) хранит
                         0001…0025 + 0035 + 0080; OWNER_DECISION_REGISTER хранит 0026…0079; в обоих
                         введено нормативное правило «один AYLA-DEC-ID = одно решение», номера не
                         переиспользуются, выдача ID требует сверки обоих реестров. Граница диапазонов
                         остаётся исторической конвенцией, не нормативным правилом (OD-AUDIT-001 открыт).
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

GOVERNANCE_DEFECT (сохраняются): статусные вокабуляры множатся (schema vs KAT §8 vs CANON_INDEX vs PDP §6.2); оба governance-стандарта — draft/candidate, но по ним канонизированы BOT-001/002, CDP, Master MVP set; три несовместимые карты областей (KAS §4 vs KAT §3 vs schema `knowledge_area` enum — нет `ux`, есть `design`); DMR `provisional_system_owner.allowed_until: 2026-08-15` — срок истёк, правило не пересмотрено (DMR:251). Улучшение: устранена коллизия decision-ID и зафиксировано правило уникальности (KB-001).

## 3. Inventory Summary

| Срез | Файлов | Преобладающий effective status |
|---|---|---|
| 00 Foundation (+Canon Governance, windows) | 28 | CANONICAL 4 / CANDIDATE 9 / DRAFT-PROPOSED 4 / HISTORICAL 8 / REFERENCE 3 |
| 01 Product (+UX MVP) | 38 | CANONICAL 4 / CANDIDATE 6 (вкл. BOT-003) / DRAFT (UX MVP рабочий слой) ~21 / HANDOFF ~7 |
| 02 Strategy | 10 | CANONICAL 3 / CANDIDATE 3 / DRAFT 3 / PROPOSED 1 |
| 03 AI System | 1 (+3 data) | CANONICAL 1; appendices DRAFT (metadata lag) |
| 05 Architecture | 19 | CANONICAL 4 / DRAFT-PROPOSED 15 (вкл. 3 новых memory/context-контракта) |
| 06 Product | 1 | CANON_CANDIDATE (draft формально) |
| 06 Safety and Governance | 2 | CANONICAL 1 / DRAFT 1 |
| 07 UX | 6 | CANON_CANDIDATE формально; де-факто FROZEN (AYLA-DEC-0080) |
| 99 Archive/proposals | 6 | HISTORICAL 5 / PROPOSED-stale 1 |
| docs (+temp) | 19 | HANDOFF 19 (12 misclassified как source_kind: canonical) |
| UX Agents | 100 | HANDOFF/HISTORICAL ~92 / REFERENCE 8 |
| Корень (Ayla.md, README, approved_v1_1) | 3 | REFERENCE 1 / REFERENCE 1 / SUPERSEDED 1 |
| **Итого** | **233** | (.pytest_cache/README.md — не KB, не индексирован) |

Effective status totals: CANONICAL 18 · CANON_CANDIDATE ~20 · DRAFT/PROPOSED ~48 · REFERENCE ~15 · HANDOFF/HISTORICAL ~130 · SUPERSEDED ~5 · UNKNOWN 0.

## 4. Canon Map

```text
[C] Ayla Constitution v2.2
 └─ [C] Knowledge Area Taxonomy v1.0        [K] Knowledge Architecture Spec v1.4 (pending-infrastructure)
 └─ [K] Product Essence v1.2 ── [K] LDT Manifesto v1.1
     ├─ [K] Product Vision v2.1 ─ [K] Product Thesis v0.6 ─ [K] Product Principles v0.2
     └─ [K] MVP Scope & Release Contract v0.4  ← де-факто release boundary
         ├─ [C] MVP User Journey Spec v1.2   (alignment gate к DEC-0063…0066 ОТКРЫТ; цитирует родителей по старым версиям)
         │    └─ [S] approved_v1_1.md (v1.1, superseded; лежит в корне — нарушение versioning rule)
         │    └─ [?→P] полная User Journey Spec v1.2 (review; booking.* / Concierge — stale)
         ├─ [C] MVP Reset Roadmap v1.0  ⚠ не амендирован после OD-MVP-1…4 (KB-004)
         ├─ [C] MVP Documentation Roadmap v1.1 ⚠ booking-терминал, Killer PRD в цепочке (KB-004)
         ├─ [D] Single-Provider / Multi-Provider Execution Scopes (pin на Scope v0.3 — stale)
         ├─ [C] Intent Model Spec v1.0 (+[D] machine appendices 03 AI System/Contracts)
         ├─ [C] Conversation Model Spec v1.0 ← AYLA-DEC-0055…0062
         ├─ [C] Memory Model Spec v1.0 ← AYLA-DEC-0067…0079
         │    └─ [K] NEW 2026-08-19: Memory Domain Contract / Context Resolution Contract /
         │       Memory & Context Migration Plan (rulings OR-MEM-1…6 вне реестров — KB-021)
         ├─ [D] Core Domain Model v1.3 / [D] Domain Context Map v1.0 / [D] Domain Event Registry (v0.5 факт.)
         ├─ [D] MVP Appointment Contract v1.1-draft (§5A/§5B — canonical semantics)
         ├─ [D] MVP Recommendation Contract v0.4 (NBA-слой §27–§34; displayable-правило §13 — KB-007 resolved)
         ├─ [C] Master MVP Auth & Authority + [C] MVP Customer Resolution (FROZEN, AYLA-DEC-0080)
         ├─ [K] Salon Operations MVP Contract v0.1
         └─ 07 UX ×6 [K формально / FROZEN де-факто] ← Master MVP set (⚠ ADS↔MAF embedded-Ayla drift — KB-022)
Product Canon: [C] Product Canon Index → [C] BOT-001 · [C] BOT-002 · [C] CDP-001 · [K] BOT-003 (blocked §20 + mojibake — KB-020)
Governance: [C] CHANGELOG · [C] Quality Bar · [K] Canon Review Standard · [K] PDP · [R] CANON_INDEX ·
            [R] CANON_WORKSTREAM_STATUS · [R] CANON_CONFLICT_REGISTER · [R] OWNER_DECISION_REGISTER
Decisions: [C] Ayla Decision Log v1.11 (0001…0025, 0035, 0080) ‖ [R] OWNER_DECISION_REGISTER (0026…0079)
           — объединённое покрытие 0001–0080 полное и непересекающееся (KB-001 RESOLVED; остаток KB-023)
```

## 5. Coverage Matrix

| Area | Canon Source | Status | Owner | Blockers | Coverage |
|---|---|---|---|---|---|
| Foundation | Constitution, KAT | [C]/[K] | Founder/Product Owner | KB-005, KB-010 | PARTIAL |
| Strategy | Decision Log, Scope v0.4, Thesis | [C]/[K] | Product Owner | KB-002, KB-003, KB-004 | CONFLICTING |
| Product | Canon Index, BOT-001/002, CDP-001 | [C] | Product Owner | KB-020 (BOT-003) | COMPLETE (ядро) |
| Journey | MVP UJS v1.2 | [C] | Product Owner | KB-005 (alignment gate) | PARTIAL |
| Intent | Intent Model Spec v1.0 | [C] | AI Architecture | — (appendices draft) | COMPLETE |
| Domain | Memory/Conversation Models [C]; CDM/ContextMap/DER [D] | mixed | Domain Architecture | KB-009, KB-010, KB-021 | PARTIAL |
| Customer UX | UX MVP screens/flows (draft) | [D] | UX Architecture | KB-016 | PARTIAL |
| Master/Salon UX | 6 контрактов 07 UX (frozen) | [FROZEN] | UX Architecture | KB-022 (embedded-Ayla drift) | PARTIAL |
| Booking | MVP Appointment Contract (draft; §5A/§5B canonical) | [D] | Product Architecture | KB-011 | PARTIAL |
| Availability | DEC-0021 + CDM §7.10; event names — только archive brief | [C]-decision | CAP-010 | KB-017 | PARTIAL |
| Recommendation | RC v0.4 (draft) + DER registered events | [D] | Product Architecture | KB-009 | PARTIAL |
| Memory | Memory Model Spec v1.0 [C] + новый contract-слой [K] | mixed | Domain Architecture | KB-021 | PARTIAL |
| Consent | CSR v1.2 (approved; ключевые scopes proposed) | [C] | Privacy Owner | CSR-OD-5, UX-GAP-0101 | PARTIAL |
| Privacy | DIM (draft), AMD-001 (blocked) | [D] | Privacy Owner | KB-008 | PARTIAL |
| Safety | Constitution, Quality Bar; MVP Safety Policy НЕ материализована | — | Safety Owner | KB-017 | PARTIAL |
| Health | Scope §6.1 (candidate); ADR-0012 OD-1 (legal pending) | [K] | Product Owner | ADR-0012 OD-1/OD-2 | PARTIAL |
| AI Behaviour | CDP-001, BOT-001/002 | [C] | Product Owner | — | COMPLETE |
| Prompting | канонический документ отсутствует (planned) | — | не назначен | — | MISSING |
| Tools | Tool Schema Registry — planned | — | не назначен | — | MISSING |
| Architecture | RRM (proposed), ADR-0012/13/14 (proposed) | [D] | Platform Architecture | OD-RRM-1…7 | PARTIAL |
| Data | DIM v1.0 (draft) | [D] | Safety & Governance | KB-008 | PARTIAL |
| API Boundaries | Master MVP contracts [C]; Appointment/RC drafts | mixed | Domain Architecture | KB-011 | PARTIAL |
| Cross-Repo | RRM write authority (Proposed); breaking-change policy не утверждена | [D] | Platform Architecture | OD-RRM-1…7 | PARTIAL |
| Analytics | Analytics Event Contract — planned; CSR audit-имена не зарегистрированы в DER | — | не назначен | KB-010 | MISSING |
| Monetization | DEC-0001/0007/0008/0010/0032 + конфликт оплаты | [C]-decisions | Founder | KB-002 | CONFLICTING |

## 6. Dependency / Ownership Integrity

- **Циклы зависимостей:** не обнаружены (depends_on/supersedes граф ацикличен; независимо подтверждено freeze-отчётом: 0 циклов на 228 файлах).
- **Неразрешённые ссылки:** Glossary → 7+ несуществующих узлов (Event Taxonomy, Booking Lifecycle Specification, Memory Entry Schema, Recommendation Engine Specification, Safety and Boundary Specification, Analytics Event Taxonomy, Core User States, Knowledge Schema Reference); ADR-0007/ADR-0009 unresolved; **ADR-0011 цитируется ADR-0012, CSR и Memory Domain Contract, но файла ADR-0011 в репо нет** («несинхронизированная mirror-заглушка» вне репо); `07 UX/Ayla Customer Context Screen Contract.md` — ссылка на несуществующий файл из Master App IA (:377); `scripts/validate_amd020_schemas.py` — ссылка из AMD-001 §17 на переименованный файл (фактически `validate_amd001_schemas.py`); битые wikilink-имена: `[[Ayla — Product Vision]]` (Principles:29, Thesis) vs фактический `Ayla Product Vision`; `[[Ayla User Journey Specification]]` (без «MVP») в ADR-0012:55 и Domain Context Map:52.
- **Wrong-direction dependencies (approved → draft):** Master MVP Auth + Customer Resolution [C] depends_on MVP Appointment Contract [D]; CSR [C] зависит от ADR-0012 [D], AMD-020 [proposed], DIM [draft]; Intent Model [C] — draft machine-appendices с metadata lag (headers «draft/proposed/candidate», updated 2026-08-03 при approval 2026-08-08); CDP-001 [C] опирается на явно NON-CANONICAL candidate-источники (Principles v0.2, Essence v1.2, RC); Memory Model [C] §6 ссылается на draft ADR-0012 OD-2/OQ-1/OQ-2; approved MVP UJS depends_on полную UJS в status review с битыми звеньями lineage.
- **Duplicate ownership (основное):** Knowledge Area Taxonomy ×2 (KB-006); Account/Profile: CDM §12/§22 (CAP-019, «confirmed» по proposed-источнику) vs AMD-020 PSR + DIM (User Context Domain/W2) (KB-008); Consent SoT: AMD-020/DIM (Consent Domain) vs CSR (pending CSR-OD-5) — DIM:43 silently принимает сторону Consent Domain (KB-008); Recommendation lifecycle ×4 модели (KB-009); snapshot-концепция ×3 (ADR-0013 proposed vs RC §7 vs Appointment Contract) без разрешения владения (KB-009); навигационная норма «Сегодня | Расписание | Ayla» дублируется как авторитет в 3 UX-документах (SysRec §13, IA §4.2, Schedule §5) + EN/RU неоднородность; «главная метрика» ×3 (KB-014); НОВОЕ: Memory Domain Contract частично дублирует canonical Memory Model v1.0 (lifecycle, Proposal≠Entry, supersession) при декларации «материализует, не дублирует» (KB-021).
- **Ownership gaps (без изменений):** Prompt Canon, Tool Schema Registry, MVP Safety Policy (CAP-014), Analytics Event Contract, Measurement Framework — обязательные по upstream, не материализованы, владельцы не назначены.
- **ID-алиasing решений (self-disclosed):** CSR-OD-4 = ADR-0012 OD-1 = контекст OD-K1 (CSR:1276-1281); OD-MEM-3 = CSR-OD-5 (Memory Domain Contract §13) — один вопрос под несколькими ID.

## 7. Decision / ADR Propagation

| Decision | Owner | Affected | Status |
|---|---|---|---|
| AYLA-DEC-0001…0010 (монетизация, каналы, moat, дата пилота) | Decision Log | Scope/Thesis/execution scopes | PARTIALLY_PROPAGATED (DEC-0003 просрочен; DEC-0006 конфликтует — KB-002) |
| AYLA-DEC-0011…0025 (predecessor gate, identity, tenant, offering, availability, reschedule, memory, events) | Decision Log | CDM, DER, CSR, Scope, контракты | PROPAGATED (остаток: availability event names — только в archive, KB-017) |
| AYLA-DEC-0026 (LDT ruling, Register) | OWNER_DECISION_REGISTER | Essence v1.1+, Manifesto | PROPAGATED; коллизия устранена 2026-08-19 (KB-001 RESOLVED) |
| AYLA-DEC-0035 (C7 оплата в miniapp) | Decision Log | beautygo_backend | CONFLICTING (KB-002) |
| AYLA-DEC-0027…0034, 0036…0079 (каналы, Journey, Conversation, Memory пакеты) | Register только | Scope, UJS, Conversation/Memory Models | PROPAGATED по содержанию; отсутствуют в Decision Log — легализовано split-моделью, но единый ledger не утверждён (KB-023) |
| AYLA-DEC-0080 (Master MVP Canon Freeze; перенумерована из DEC-0026) | Decision Log v1.11 | 2 контракта, DER v0.5, frozen set, CHANGELOG | PROPAGATED; запись есть только в Log — в Register отсутствует (KB-023) |
| AYLA-DEC-0063…0066 (OD-MVP-1…4) | Register (+ docs/temp источник) | Essence/Vision/Thesis/Principles/Scope v0.4 (кандидаты) | PARTIALLY_PROPAGATED — approved Reset Roadmap & Documentation Roadmap НЕ амендированы (KB-004) |
| UX-OD-001…005 | ux-owner-decisions.md (approved) | UX-слой, CDP (working evidence) | PARTIALLY_PROPAGATED — не зарегистрированы в Decision Log (KB-013) |
| OQ-REC-1 (displayable rule) | owner ruling 2026-07-29 | **RC v0.4 §13 (перенесено 2026-08-19)**, UX addendum, SCR-CUST-004 | **PROPAGATED в нормативный текст (KB-007 RESOLVED по содержанию)**; остаток: RC сам draft + OQ-REC-6 (владелец классификации) open |
| R-NBA-1…8 (Recommendation = NBA) | RC v0.4 (2026-08-19, в audit window) | RC §2/3/9/10/27–34 | NOT_PROPAGATED (свежие; BOT-003/UX addendum/Killer PRD не синхронизированы; OQ-R12 открыт) |
| OR-MEM-1…6 (memory storage/context rulings) | внешний prompt владельца (вне репо) | 3 новых контракта 05 Architecture | **ORPHANED в реестрах — нигде в Decision Log/ODR не зарегистрированы (KB-021)** |
| OD-RRM-1…7 | RRM | контракты, Schedule UX | ORPHANED (все Proposed; downstream freeze уже случился) |
| BOT-001 Q1–Q9 / BOT-002 MM-D1–5, PD-01–03 / CDP-01–12 / BOT-003 Q3–Q9 | UX Agents decisions/reports | BOT-001/002, CDP-001 [C]; BOT-003 [K] | PROPAGATED (audit trail — только в untracked `UX Agents/`, KB-017) |
| ADR-0012 (Dynamic User Model) | — | Memory Model (fenced), Glossary (stale «reserved»), Memory Domain Contract (словарный конфликт `confidence`) | PROPOSED, блокирован OD-1/OD-2; словарь несовместим с canonical lifecycle (KB-010 + KB-021) |
| ADR-0013 / ADR-0014 | — | UX-слой | PROPOSED; ADR-0013 дублирует snapshot-механизм RC §7 (KB-009); drift `recommendation.generated` vs `recommendation.created` |
| AMD-001 (C5 export/forget) | — | W2/W3/W4 | DRAFT/BLOCKED (self-assessed Quality Bar FAIL) |
| AMD-020 PSR | — | CDM («confirmed» по proposed источнику), CSR (стэйл «approved») | PROPOSED; ownership-конфликты (KB-008) |

## 8. Semantic Findings (подтверждённые targeted verification)

1. **KB-002 (P1) — VERIFIED.** `02 Strategy/Ayla Decision Log.md:145` (DEC-0006, статус «действует»: клиент МОЖЕТ оплатить онлайн опционально) + `:1443` (DEC-0035, «действует»: штатный сценарий оплаты в miniapp) vs `:462` (DEC-0015 п.4: «Вне MVP остаются: клиентская онлайн-оплата») + `02 Strategy/Ayla MVP Scope and Release Contract.md:454` («клиентская онлайн-оплата услуг» — OUT_OF_SCOPE). Записи о разрешении нет; UX-GAP-P1-07 open.
2. **KB-004 (P1) — VERIFIED (карточки + run-1 evidence).** Reset Roadmap (approved/CANONICAL): обязательные daily-трекеры, LDT-центричный vertical slice (§5 Sprint 2, §9), booking-терминал — против Scope v0.4/OD-MVP-1…4 (LDT CONDITIONAL, trackers DEFERRED). Documentation Roadmap §1.2: сквозной сценарий завершается booking; Killer PRD — звено цепочки.
3. **KB-020 (P1) — VERIFIED.** `01 Product/BOT-003 Discovery and Recommendation Conversation Specification.md` — 7 строк с mojibake (`в†'`, `вЂњ…`, §3/§13/§18–20) + lone CR endings; canon candidate частично нечитаем; его approved decision records лежат в untracked `UX Agents/decisions/`.
4. **KB-021 (P2) — VERIFIED.** 3 новых контракта (created 2026-08-19): `Memory Domain Contract` §1 («не дублирует, материализует») фактически вторично описывает lifecycle/supersession canonical Memory Model v1.0; L394 сам декларирует несовместимость словаря ADR-0012 по `confidence` без разрешения (OD-MEM-1); rulings OR-MEM-1…6 не зарегистрированы ни в одном реестре; источники — внешние `AUDIT_MEMORY_DOMAIN.md` и prompt владельца; события `memory.context_resolved*` заявлены «при реализации», в DER не внесены; Migration Plan не ссылается на `02 Strategy/Ayla MVP v0.3 Downstream Migration Plan.md` (два migration-плана без перекрёстных ссылок).
5. **KB-022 (P2) — VERIFIED (карточки).** `07 UX/Ayla Appointment Detail Screen Contract.md` §9.1/§13: embedded Ayla «may appear / Proposed» (updated 2026-08-14) vs `07 UX/Ayla Master Appointment Flow MVP.md` v0.1.1 CR-3 (2026-08-17): «EMBEDDED Ayla inside Appointment Detail… remains Deferred» — внутри frozen Master MVP set более старый документ не синхронизирован с более поздним repair.
6. **KB-023 (P2) — VERIFIED.** Ledger split после repair: Decision Log хранит 0001…0025+0035+0080, ODR — 0026…0079; объединённое покрытие 0001–0080 полное и непересекающееся (проверено по заголовкам обеих книг), но: записи 0080 нет в ODR (только примечание :84), Log не содержит 0027…0034/0036…0079, граница диапазонов — конвенция, а не нормативное правило; единый ledger требует owner ruling (OD-AUDIT-001).

Остальные — в разделе 16.

## 9. Handoff Leakage

- **Подтверждено (без изменений):** `docs/KNOWLEDGE_AREA_TAXONOMY.md` — конкурирующий дубликат canonical KAT без frontmatter (KB-006). `99 Archive` как единственный носитель действующих правил: имена availability-событий (brief DEC-0021 §7), YAML-полевые модели и authorization-таблица reschedule (brief DEC-0022), детальный реестр Offering/Assignment (brief DEC-0020), open Q1/Q5 identity (brief DEC-0016). `UX Agents/` (untracked) — единственный audit trail одобрений BOT-001/002/003, CDP (KB-017). `docs/temp/Ayla20v220Owner%20Decisions.md` — единственный читаемый источник OD-MVP-1…4.
- **Новое:** источники OR-MEM-1…6 и `AUDIT_MEMORY_DOMAIN.md` (C:\...\Ayla\docs\) — вне репо; решения, на которых построены 3 новых контракта, не имеют in-repo provenance (KB-021). CUX-010/CUX-012 (канонические UX-принципы) зафиксированы только в process-файлах `UX Agents/answers/`.
- **Не подтвердилось (решения проведены в канон):** owner-approved Schedule/Availability/Post-Visit decisions; P0-B1…B4; freeze-декларации (→ ADS §17/SYS §19 + AYLA-DEC-0080); OD-MVP-1…4 (→ Register DEC-0063…0066 + candidate-редакции); BOT-001 Q1–Q9 (→ BOT-001 v1.0).
- **Системное:** 12 handoff-документов `docs/` имеют `source_kind: canonical` (misclassification); полный слой `UX Agents/` (100 файлов) и `docs/` (19) — untracked, т.е. вне версионного контроля канона, при том что на них опираются canonical-доказательные цепочки.

## 10. UX vs Design Evidence

CANON_GAP для Master/Salon UX не зафиксирован: behaviour/states/actions/permissions определены текстово и заморожены (SYS §2: textual contract sufficient). **DESIGN_EVIDENCE_GAP (KB-016, P2):** все 6 owner-approved composites физически отсутствуют в репо; `docs/screens agent salon/` — 4 PNG скриншота VS Code, не design evidence; REPLY_SALON_UX_IMPLEMENTATION_READINESS обусловливает UX handoff 6 mockups + 3 copy strings (C1–C3). Frozen UX не переоткрывался. Новое наблюдение (не Canon Gap): Schedule UX Contract §4 опирается на session image, «not copied into the repository» — нормативная опора на несуществующий артефакт.

## 11. AI / Memory / Prompt Boundaries

Pipeline и владельцы: backend facts → SoR по RRM (proposed) → persistence (CDM §12 SoR-таблица, draft; **Memory Domain Contract v0.1, candidate — новый претендент на физический слой**) → retrieval (**Context Resolution Contract v0.1, candidate — новый единый retrieval boundary `resolve_context`**) → context construction (Conversation Model Context Projection [C]) → memory rendering (Memory Model [C]) → prompt assembly (**владелец не определён — Prompt Canon отсутствует**) → model (Intent Model Output Contract 0.5 [C]) → tools (**Tool Schema Registry отсутствует**) → result (Transaction State Model, draft).

Границы, требуемые upstream canon и отсутствующие: Prompt Canon, Tool Schema Registry, MVP Safety Policy, Analytics Event Contract, Measurement Framework. Memory boundary: semantics согласована (Memory Model [C]), но появился неутверждённый физический слой с собственными rulings (KB-021); новые контракты заявляют fail-closed retrieval и запрет `get_all_memory` — согласовано с каноном, но не approved. Session/channel boundary — открытый конфликт OQ-12 (KB-012).

## 12. Cross-Repo Contract Boundaries

Проверялись только утверждения KB (код других репозиториев не анализировался). RRM: Write Authority Model и SoR-назначения — все OD-RRM-1…7 **Proposed**; формально утверждённой cross-repo ownership-матрицы нет, при этом Master MVP canon set заморожен для engineering на её основании. Version compatibility / dependency pins / breaking-change / synchronized update policy — не утверждены. Новые контракты фиксируют consumer matrix (ai-bot-platform / ayla-ai-core / ayla-analytics / ayla-user-context) и запрет storage I/O для ayla-ai-core — как candidate, не approved. Утверждение «отсутствие реализации в GitHub» finding'ом не является (отдельный будущий аудит KB↔CODE).

## 13. Traceability

Восстанавливаются чисто: BOT-001/002/CDP (Q→decision→spec), Memory Model (DEC-0023/24+0067…0079), Master MVP (P0-B→ruling→contracts→AYLA-DEC-0080), Journey v1.2 (OD-1…18). **Восстановлено после repair:** ссылка DEC-0026 однозначна; freeze-цепочка → DEC-0080. Разрывы: DEC-0027…0034/0036…0079 доступны только во втором реестре (KB-023); approved Reset/Doc Roadmaps не трассируются к актуальным решениям (KB-004); UX-OD-001…005 вне Decision Log (KB-013); OR-MEM-1…6 без реестровой регистрации (KB-021); availability event names без нормативной регистрации (KB-017); цепочка полной UJS содержит битые звенья lineage («blocked: canonical source не найден»); implementation detail как Product Canon не обнаружено.

## 14. Stale / Duplicate Authority

Stale (пакет KB-010 + KB-015): Ayla.md Root MOC (версии/карта репо не отражают 06 Product/07 UX/approval Journey v1.2); README («Knowledge Architecture v1.3» vs v1.4); KAS §4 (несуществующие папки) + самоссылки v1.3 при v1.4; KAT §9 («no 07 UX folder» — папка существует); Glossary (planned-документы, ADR-0012 «reserved»); Domain Context Map (`Rescheduled`-статус против DEC-0022, :2163; CTX-003); Capability Registry §3.1 («Intent Model не создан»); полная UJS (`booking.*`, Concierge, «ADR-0012 planned»); FOUNDATION/LDT windows (stale COMPLETE/OPEN статусы, ссылки на ветку `agent/ux-mvp`, несуществующий deliverable LIVING_DIGITAL_TWIN_HANDOFF.md); CANON_WORKSTREAM_STATUS (pre-reopening таблица); DEC-0003 (дата пилота 2026-08-15 прошла, «действует»); DEC-0005 («ожидает» — устарела); DMR provisional deadline 2026-08-15; LDT Manifesto pin на Essence v1.1; Essence §13 vs §9 + §21; CSR §9 («AMD-020 approved»); execution scopes/Migration Plan pinned на Scope v0.3/Journey v1.1; Single-Provider Scope: LDT MUST против CONDITIONAL (OD-MVP-1); Strategic Moat не амендирован под representation-neutral; ux session-brief (inventory v0.2 при v0.6). Duplicate authority — раздел 6.

## 15. Validator Results

- **Entrypoint:** `python scripts/validate_knowledge.py` (KAS §10; локально + GitHub Actions; renderer: `render_domain_registry.py --check`).
- **Результат прогона 2026-08-19 (~19:00 и повторно ~22:20):** `Knowledge validation: 130 error(s), 20 warning(s)`, **exit code 1** (примечание: run-1 отчёт фиксировал exit 0 — расхождение записи; текущий факт: exit 1 при том же счёте). Baseline: 130/20 (REPLY_MASTER_MVP_FINAL_GAP_CHECK, 2026-08-16) → **новых ошибок нет**, несмотря на появление 3 новых architecture-файлов и BOT-003 (их frontmatter валиден).
- **Состав ошибок:** ~100 — missing frontmatter в `UX Agents/**`, `docs/temp/*`, `docs/FINAL MASTER…`, `docs/KNOWLEDGE_AREA_TAXONOMY.md`, `.pytest_cache/README.md`; 13 — missing required fields + неизвестный type `critique-report` (`UX Agents/reports/BOT-002-CRITIC-001-…`); в содержательных документах: `unknown document type 'standard'` (Canon Review Standard, PDP), `canonical filename must not contain a version suffix` (те же 2 файла), `unknown document type 'map'` (Conversation Product Map), `concerns: engineering-process` вне enum (Development Discipline). Warnings: unresolved wikilinks/related/adr targets (Glossary, DMR, полная UJS).
- **WHAT VALIDATOR CHECKS:** наличие/enum-required frontmatter-полей, зарегистрированные document types, правила имён/node_id, разрешимость relationship targets, уникальность node_id/title среди Active Canon (Variant C), conditional rules, required sections.
- **WHAT VALIDATOR DOES NOT CHECK:** семантические конфликты, frontmatter↔body (draft vs FROZEN), распространение решений, дубликаты authority, handoff leakage, коллизии ID решений, mojibake, stale. **130/20 — стабильный baseline; не исправлялся.**

## 16. P0–P3 Findings

> Нумерация продолжает run-1 (KB-001…KB-019) для трассируемости; новые findings этого прогона — KB-020…. Полный machine-readable список — в JSON.

**Resolved since run-1:**

- **KB-001 · P0 · GOVERNANCE_DEFECT — RESOLVED 2026-08-19.** Коллизия AYLA-DEC-0026 устранена: ID сохранён за LDT-решением, freeze-запись перенумерована в AYLA-DEC-0080 (Decision Log v1.11), ссылки обновлены в 6 документах, правило «один AYLA-DEC-ID = одно решение» внесено в оба реестра; объединённое покрытие 0001–0080 полное и непересекающееся (верифицировано по заголовкам). Остаток оформлен как KB-023. Repair record: `docs/audits/2026-08-19-KB-001-DEC-0026-collision-repair.md`.
- **KB-007 · P1 · UNPROPAGATED_DECISION — RESOLVED по содержанию 2026-08-19.** RC v0.4 §13: «Displayable-правило (owner ruling 2026-07-29; перенесено из Recommendation UX Addendum §2)… Нет displayable объяснения → не показываем» (`Ayla MVP Recommendation Contract.md:609-616`, Change Log v0.4). Остаток: RC сам draft/proposed (покрыт KB-011) и OQ-REC-6 (владелец классификации displayable) open.

**Active:**

- **KB-002 · P1 · SEMANTIC_CONFLICT** — клиентская онлайн-оплата: DEC-0006 + DEC-0035 («действует», разрешают) vs DEC-0015 п.4 + Scope §7 (OUT_OF_SCOPE); разрешения нет. Evidence: `Decision Log:145,462,1443`, `Scope:454`; UX-GAP-P1-07 open. Blocks implementation (billing): YES. Owner decision: YES (OD-AUDIT-002).
- **KB-003 · P1 · DUPLICATED_AUTHORITY** — нормативный статус Killer PRD: Thesis §1 (нормативен) vs Scope §2/§12 (legacy reference) vs approved Documentation Roadmap (звено цепочки); дополнительно Killer PRD содержит устаревший блокер-лист (OD-K9/K11 уже resolved) и memory-first тезис, superseded representation-neutral OD-MVP-3/4. Evidence: `Thesis:64-69`, `Scope:130,635`, `Killer PRD:61,70-96`. Owner decision: YES (OD-AUDIT-003).
- **KB-004 · P1 · UNPROPAGATED_DECISION** — OD-MVP-1…4 / Scope v0.4 не протянуты в approved `MVP Reset Roadmap` (трекеры, LDT slice, booking-терминал, метрика) и `MVP Documentation Roadmap` (booking-терминал §1.2, Killer PRD в цепочке, PascalCase-события §6.4, superseded-блок §3.4 без редакции). Tags: semantic_conflict, stale_knowledge. Blocks canonicalization: YES. Owner decision: YES (OD-AUDIT-004).
- **KB-005 · P1 · GOVERNANCE_DEFECT** — инвертированная канонизация: downstream CANONICAL при upstream candidates (Essence v1.2, Vision v2.1, Thesis v0.6, Principles v0.2, Scope v0.4 — awaiting Final Review; MVP UJS/Intent/Conversation/BOT-001/002/CDP — canonical); открытый alignment-gate Journey v1.2 (Scope §12 ACTIVE/REQUIRED); MVP UJS цитирует родителей по старым версиям (:145-147); CDP опирается на NON-CANONICAL basis. Owner decision: NO (завершить Final Review + alignment).
- **KB-006 · P1 · HANDOFF_KNOWLEDGE_LEAK / DUPLICATED_AUTHORITY** — `docs/KNOWLEDGE_AREA_TAXONOMY.md` — конкурирующая копия canonical KAT (без frontmatter, иной lifecycle, устаревшая карта областей — нет 02 Strategy/03 AI/06 Safety); `docs/temp/*` — неканонизированные дубликаты (вкл. owner-approved Principles-draft и источник OD-MVP-1…4). Owner decision: NO (triage: удалить/архивировать как handoff).
- **KB-020 · P1 · CONTENT_CORRUPTION** — BOT-003 (canon candidate) частично нечитаем: mojibake в §3/§13/§18–20 (7 строк: `в†'`, `вЂњ…`), lone CR endings; decision records (BOT-003-Q3/Q4/Q6/Q8/Q9) — в untracked `UX Agents/decisions/`, вне версионного контроля. Evidence: `01 Product/BOT-003 …md:73-77,195-203,252-299,261-269`. Blocks canonicalization (BOT-003 §20 + читаемость): YES. Owner decision: NO (восстановить кодировку из decision-источников, переложить records под VC).
- **KB-008 · P2 · OWNERSHIP_CONFLICT** — Account/Profile: CDM (CAP-019, «confirmed» по proposed-источнику) vs AMD-020/DIM (User Context Domain/W2); Consent SoT: AMD-020/DIM vs CSR (pending CSR-OD-5); DIM:43 silently принимает сторону Consent Domain. Owner decision: зарегистрировано (CSR-OD-5; расширить на Account/Profile).
- **KB-009 · P2 · SEMANTIC_CONFLICT** — Recommendation lifecycle: CDM §7.11 vs RC v0.4 (immutable record + NBA-слой) vs Context Map CTX-004 vs ADR-0013 (дубль RC §7; drift `recommendation.generated` vs `recommendation.created`). RC v0.4 (R-NBA-1…8) свежий и никуда не протянут (OQ-R12).
- **KB-010 · P2 · STALE_KNOWLEDGE** — пакет (см. раздел 14): Context Map, Glossary, Capability Registry §3.1, полная UJS, CSR §9, Essence/Manifesto, KAS §4/§3.1, KAT §9, Ayla.md, README, CANON_WORKSTREAM_STATUS, windows, execution scopes pin v0.3, ux session-brief.
- **KB-011 · P2 · DEPENDENCY_DIRECTION** — approved canon опирается на draft/proposed (Master contracts→Appointment draft; CSR→ADR-0012/AMD-020/DIM; Intent appendices draft; CDP→candidate basis; Memory Model→ADR-0012; BOT-003 §20 blocker; MVP UJS→полная UJS review).
- **KB-012 · P2 · SEMANTIC_CONFLICT** — Session boundary: Conversation Model vs Intent Model vs CSR; зарегистрировано как OQ-12.
- **KB-013 · P2 · TRACEABILITY** — UX-OD-001…005 (approved в UX-слое) не зарегистрированы в Decision Log (подтверждено: ux-owner-decisions.md:38-40).
- **KB-014 · P2 · DUPLICATED_AUTHORITY** — три «главные метрики» (WCHA / killer outcome / Reset Roadmap retention) без иерархии. Owner decision: YES (OD-AUDIT-006).
- **KB-015 · P2 · STALE_DECISION** — DEC-0003 (пилот 2026-08-15) просрочен, статус «действует» (`Decision Log:113`); DEC-0005 «ожидает» устарела; DMR provisional_system_owner дедлайн 2026-08-15 истёк (DMR:251).
- **KB-016 · P2 · DESIGN_EVIDENCE_GAP** — 6 owner-approved composites отсутствуют; handoff обусловлен mockups + copy C1–C3. Не Canon Gap.
- **KB-017 · P2 · HANDOFF_KNOWLEDGE_LEAK** — archive/handoff как единственный носитель действующих правил: availability event names (brief DEC-0021 §7), YAML/authorization reschedule (brief DEC-0022), Offering/Assignment (brief DEC-0020), audit trail MM-D/PD/PO/BOT-003 (untracked `UX Agents/`), источник OD-MVP-1…4 (`docs/temp/`), CUX-010/012 (answers/), отсутствующие обязательные контракты (Safety Policy, Prompt Canon, Tool Registry, Analytics Event Contract, Measurement Framework), ADR-0011 отсутствует в репо.
- **KB-021 · P2 · DUPLICATED_AUTHORITY / GOVERNANCE** — незарегистрированный memory/context contract-слой (2026-08-19): частичное дублирование canonical Memory Model; OR-MEM-1…6 вне реестров; OD-MEM-1 (словарный конфликт ADR-0012 `confidence`) задекларирован неразрешённым; два migration-плана без перекрёстных ссылок; события `memory.context_resolved*` не внесены в DER. Owner decision: YES (OD-AUDIT-007).
- **KB-022 · P2 · SEMANTIC_CONFLICT** — embedded Ayla в Appointment Detail: ADS §9.1/§13 «Proposed» (upd. 08-14) vs MAF v0.1.1 CR-3 «Deferred» (08-17) — unpropagated repair внутри frozen set.
- **KB-023 · P2 · GOVERNANCE_DEFECT (residual KB-001)** — два decision ledger'а сохраняются: Log (0001…0025, 0035, 0080) ‖ Register (0026…0079); записи 0080 нет в Register; Log не содержит 0027…0034/0036…0079; граница — конвенция, не норма; ID-алиasing (CSR-OD-4=OD-1=OD-K1; OD-MEM-3=CSR-OD-5). Owner decision: YES (OD-AUDIT-001).
- **KB-018 · P3 · METADATA_HYGIENE** — пакет: frontmatter draft/candidate vs FROZEN (6 UX); `source_kind: canonical` у 12 handoff REPLY_* и brief; `approved_v1_1.md` в корне; AMD naming (node_id `amd020`, filename/title mismatch AMD-020↔AMD-001, footer v0.8.1.1, ссылка на `validate_amd020_schemas.py`); версионный дрейф без changelog (DER 1.0-draft/v0.4/v0.5; MAF 0.1 vs 0.1.1; Salon Ops/Schedule UX/IA/SysRec; Intent Contracts metadata lag; KAS самоссылки); `06 Product` vs `06 Safety and Governance` — дублирование номера области; AMD-020 PSR node_id без префикса `ayla.`; `owner`+`owners` дубль (REPLY_SCHEDULE); mojibake в Salon Ops/Master Ops/`UX Agents/questions/`; разорванные OQ-таблицы (MAF:254, ADS:396); BOT-003 data_sensitivity high при отсутствии ПДн-контента; privacy-mapping data_sensitivity none при ПДн-содержании; Research draft без frontmatter; MOT расширение `.md` имени `MASTER_MVP_P0_AUTHORITY_RUNTIME_CLOSURE(1).md`.
- **KB-019 · P3 · PROCESS_DUPLICATION** — MD Communication Protocol vs PDP vs orchestration-v2: конфликт места Monitor/Gatekeeper; протокол без frontmatter/канонического дома; «Текущий цикл BOT-001» в протоколе заморожен в устаревшем состоянии.

## 17. Canon Blockers

```text
BLOCKER 1 (= KB-002)
Root cause: конфликт действующих решений о клиентской онлайн-оплате без записи о разрешении.
Affected area: Monetization / MVP Scope / Billing implementation.
Affected documents: Decision Log (DEC-0006, DEC-0015, DEC-0035); MVP Scope §7; UX-GAP-P1-registry (P1-07).
Required action: owner ruling (подтвердить OUT_OF_SCOPE и supersede DEC-0006/0035, либо вернуть оплату в scope).
Canonical owner: Product Owner / Founder. Owner decision required: YES.

BLOCKER 2 (= KB-004)
Root cause: accepted decisions (OD-MVP-1…4, DEC-0027, Scope v0.4) не протянуты в два approved canonical документа.
Affected area: Strategy → downstream execution.
Affected documents: 02 Strategy/Ayla MVP Reset Roadmap.md; 02 Strategy/Ayla MVP Documentation Roadmap.md.
Required action: amendment или явный supersede обоих документов после Product Owner Final Review.
Canonical owner: Product Owner. Owner decision required: YES.

BLOCKER 3 (= KB-005)
Root cause: канонизация downstream-документов раньше upstream Final Review; открытый alignment-gate Journey v1.2.
Affected area: Foundation → Product → Journey chain.
Affected documents: Product Essence v1.2, Vision v2.1, Thesis v0.6, Principles v0.2, Scope v0.4 (candidates);
  MVP UJS v1.2, Intent Model, Conversation Model, BOT-001/002, CDP (canonical).
Required action: завершить Product Owner Final Review пакета + Journey alignment pass (зарегистрированный gate).
Canonical owner: Product Owner. Owner decision required: NO (процесс уже определён).

TOTAL CANON BLOCKERS: 3
```

## 18. Owner Decision Queue

```text
OD-AUDIT-001 (carried, всё ещё открыт)
Question: Единая модель реестра решений: слияние OWNER_DECISION_REGISTER и Ayla Decision Log, или
  нормативная граница ID-пространства? (Коллизия ID устранена repair 2026-08-19; вопрос о модели — нет.)
Why: split-ledger легализован как конвенция, не как норма; записи 0080 нет в Register; ID-алиasing множится.
Existing evidence: Decision Log v1.11; ODR:33,84,908; repair record KB-001; KB-023.
Options: (a) единый ledger (Decision Log), Register → dashboard-view; (b) нормативная граница диапазонов;
  (c) Register как единственный ledger, Log → архив 0001…0025.
Recommended: (a) — repair уже выбрал Log как носитель спорного ID.
Affected documents: Decision Log, OWNER_DECISION_REGISTER, CHANGELOG, KAT-007.
Blast radius: ссылки на DEC-0026…0080 по KB.

OD-AUDIT-002 (carried)
Question: Клиентская онлайн-оплата в MVP: окончательно OUT_OF_SCOPE (supersede DEC-0006/DEC-0035) или included?
Why: четыре действующие нормы противоречат; billing implementation заблокирован.
Existing evidence: Decision Log:145,462,1443; Scope:454; UX-GAP-P1-07.
Options: (a) OUT_OF_SCOPE + supersede DEC-0006/0035; (b) включить C7 в scope с amendment Scope §7.
Recommended: (a) — согласуется с DEC-0015 и Scope v0.4.
Affected documents: Decision Log, Scope Contract, execution scopes, UX-GAP-P1-registry.
Blast radius: billing epic, W1 capture.

OD-AUDIT-003 (carried)
Question: Нормативный статус Killer PRD: legacy reference (Scope) или носитель normative definitions (Thesis)?
Why: два canon-кандидата противоречат; approved Roadmap — третья позиция; RC v0.4 сохраняет зависимость
  от Killer PRD §5 (OQ-R12).
Existing evidence: Thesis:64-69; Scope:130,635; Documentation Roadmap; Killer PRD:61,70-96; RC v0.4 header.
Options: (a) legacy + перенос действующих определений (qualified_action, attribution, gates) в Thesis/RC;
  (b) canonical approval Killer PRD после разблокировки ADR-0012 OD-1/OD-2.
Recommended: (a).
Affected documents: Killer PRD, Thesis, Scope, Documentation Roadmap, RC, Journey.
Blast radius: attribution/метрики, Measurement Framework.

OD-AUDIT-004 (carried)
Question: Судьба approved MVP Reset Roadmap и MVP Documentation Roadmap после OD-MVP-1…4: amend или supersede?
Why: оба approved-документа противоречат accepted decisions (трекеры, LDT, терминал journey, Killer PRD).
Existing evidence: Reset Roadmap Sprint 1–4/§9/§10; Doc Roadmap §1.2/§3.4/§6.4; Scope v0.4 §6; DEC-0063…0066.
Options: (a) targeted amendment; (b) supersede актуальными Scope/execution scopes + archive.
Recommended: (b) для Reset Roadmap, (a) для Documentation Roadmap.
Affected documents: оба roadmap; CANON_INDEX; WORKSTREAM.
Blast radius: downstream execution scopes, Migration Plan.

OD-AUDIT-006 (carried)
Question: Иерархия «главных метрик»: WCHA (Moat) vs killer outcome metric (Killer PRD) vs retention-цикл (Reset Roadmap)?
Why: три документа называют три разные North Star; Measurement Framework отсутствует.
Existing evidence: Moat Spec §17; Killer PRD §7.1; Reset Roadmap §10; Multi-Provider §23.
Options: (a) одна North Star + иерархия diagnostic metrics; (b) по метрике на фазу с явной картой.
Recommended: (a) с регистрацией в Decision Log.
Affected documents: Moat Spec, Killer PRD, Reset Roadmap, Thesis, Measurement Framework (planned).
Blast radius: вся аналитика пилота.

OD-AUDIT-007 (NEW)
Question: Статус нового memory/context contract-слоя (Memory Domain Contract, Context Resolution Contract,
  Memory & Context Migration Plan, все 2026-08-19): канонизировать как физический слой Memory Domain с
  регистрацией OR-MEM-1…6 в реестре решений — или встроить в существующие канонические документы
  (Memory Model / DER / Migration Plan)?
Why: owner rulings OR-MEM-1…6 существуют только во внешнем prompt-источнике; слой частично дублирует
  canonical Memory Model v1.0; OD-MEM-1 декларирует неразрешённый словарный конфликт с ADR-0012.
Existing evidence: MDC §1/§13/L394; CRC §1/L228-230; MCP §3-§4; отсутствие OR-MEM в Decision Log/ODR.
Options: (a) регистрация OR-MEM в OWNER_DECISION_REGISTER + canonization path по PDP; (b) fold-in в
  Memory Model + отмена отдельных контрактов; (c) оставить как non-canonical implementation specs.
Recommended: (a) с явным разрешением OD-MEM-1 (приоритет DEC-0024) и регистрацией memory.context_* в DER.
Affected documents: 3 новых контракта, Memory Model, DER, ADR-0012, AMD-020 PSR, DIM.
Blast radius: memory/context implementation (W2/W3), consent enforcement.
```

(Снят с очереди как разрешённый по содержанию: OD-AUDIT-005 — displayable-правило перенесено в RC §13 (v0.4); остаточный OQ-REC-6 идёт по существующей очереди UX. Не включены как уже зарегистрированные: CSR-OD-5, OQ-12, OQ-REC-2/4/6/7, Privacy Q1–Q10, KAT-001…007, OD-RRM-1…7, OD-MEM-1…4.)

## 19. Recommended Repair Order

```text
Step 1: Payment conflict resolution (OD-AUDIT-002)
Why now: единственный P1, напрямую блокирующий implementation (billing); KB-001 больше не блокирует трассировку.
Root findings: KB-002. Affected: Decision Log, Scope, UX-GAP-P1-07.
Prerequisites: нет. Owner decision required: YES.
Expected result: одна действующая норма оплаты; gap P1-07 закрыт.

Step 2: Strategy-layer alignment (OD-AUDIT-003, OD-AUDIT-004, OD-AUDIT-006)
Why now: снимает CONFLICTING покрытие Strategy/Monetization; approved-документы приводятся к accepted decisions.
Root findings: KB-003, KB-004, KB-014, KB-015. Affected: Killer PRD, Thesis, Scope, оба Roadmap, Moat Spec.
Prerequisites: Step 1. Owner decision required: YES.
Expected result: Strategy-слой без действующих противоречий.

Step 3: Foundation Final Review + Journey alignment (без нового решения)
Why now: снимает blocker 3; процесс уже определён governance.
Root findings: KB-005, KB-010 (Essence/Manifesto часть). Affected: 6 candidate-документов, MVP UJS.
Prerequisites: Step 2 (Scope v0.4 финален). Owner decision required: NO.
Expected result: upstream CANONICAL ≥ downstream CANONICAL; alignment-gate закрыт.

Step 4: BOT-003 readability + evidence repair (без owner decision)
Why now: разблокирует BOT-003 canon review (§20 blocker + KB-020); дёшево и независимо.
Root findings: KB-020. Affected: BOT-003 (кодировка), UX Agents/decisions → под версионный контроль.
Prerequisites: нет. Owner decision required: NO.
Expected result: читаемый кандидат с in-repo evidence base.

Step 5: Memory/context layer registration (OD-AUDIT-007) + ownership reconciliation (CSR-OD-5 расширить)
Why now: слой создан сегодня и активно правится; чем раньше зарегистрирован, тем меньше дрейф.
Root findings: KB-021, KB-008, KB-009, KB-022, KB-013. Affected: 3 новых контракта, Memory Model, DER,
  CDM, AMD-020, DIM, CSR, ADS/MAF.
Prerequisites: Step 3. Owner decision required: YES (OD-AUDIT-007).
Expected result: OR-MEM зарегистрированы; единый ownership; ADS↔MAF синхронизированы; UX-OD в Log.

Step 6: Decision ledger ruling (OD-AUDIT-001)
Why now: после содержательных шагов — чтобы новые решения сразу писались в финальную модель.
Root findings: KB-023. Affected: Decision Log, OWNER_DECISION_REGISTER, KAT-007.
Prerequisites: нет (можно раньше). Owner decision required: YES.
Expected result: один нормативный ledger или нормативная граница; запись 0080 отражена в обоих view.

Step 7: Hygiene & stale sweep (без owner decisions)
Why now: одним проходом после содержательных исправлений.
Root findings: KB-006, KB-010, KB-016, KB-017, KB-018, KB-019, KB-011, KB-012.
Affected: docs/ дубликаты, Glossary, Context Map, Capability Registry, Ayla.md, README, KAS, frontmatter,
  approved_v1_1.md, AMD naming, validator baseline, untracked-слои под VC.
Prerequisites: Steps 1–6. Owner decision required: NO.
Expected result: validator baseline ↓ к содержательному минимуму; MOC актуален; handoff помечены/перемещены.
```

## 20. Final Verdict

**C — KB PARTIALLY CANONICAL.**

Обоснование (факты): (1) Единственный P0 run-1 устранён и верифицирован: коллизия AYLA-DEC-0026 разрешена, трассировка decision-ссылок восстановлена, правило уникальности ID нормативно закреплено (KB-001 → RESOLVED). (2) Согласованные канонические цепочки сохранены и расширены: Constitution; Product Canon (BOT-001/002, CDP-001); Memory/Conversation Models; Master MVP frozen set (AYLA-DEC-0080); displayable-правило получило нормативный дом (KB-007 → RESOLVED). (3) При этом сохраняются: конфликт действующих решений об оплате (KB-002), два approved-документа против accepted decisions (KB-004), инвертированная канонизация (KB-005), конкурирующий дубликат KAT (KB-006), нечитаемый canon-candidate (KB-020) и новый незарегистрированный decision-слой (KB-021). (4) Отдельный риск надёжности этого вывода: KB активно менялась во время аудита (audit-window instability) — выводы относятся к снимку ~22:15 2026-08-19. Это не B (долг блокирующий), не D (ядро согласовано), не E (состояние определимо, доказательная база полная). Переход в B возможен после Steps 1–4 Recommended Repair Order.
