---
node_id: ayla.product.research.mvp-c01-c02-ux-inventory
title: Ayla MVP C01 C02 UX Inventory
type: specification
status: draft
decision_status: proposed
canonical_status: draft
version: "0.1"
owner: Product Architecture
knowledge_area:
  - product
domain:
  - conversation
  - intent
  - recommendation
concerns:
  - knowledge-management
  - audit
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
created: 2026-08-20
updated: 2026-08-20
review_cycle: event-driven
depends_on:
  - "[[BOT-001 First Contact Specification]]"
  - "[[Ayla MVP User Journey Specification]]"
  - "[[Ayla User Journey Specification]]"
  - "[[Ayla MVP Recommendation Contract]]"
  - "[[Ayla Goal Outcome Semantic Model Working Design]]"
related:
  - "[[Ayla Intent Model Specification]]"
  - "[[BOT-002 Conversation Lifecycle Specification]]"
  - "[[BOT-003 Discovery and Recommendation Conversation Specification]]"
---

# Ayla MVP C01 C02 UX Inventory

> **Статус:** Stage 1 research inventory, v0.1 — **non-canonical**.
> Evidence-backed инвентаризация фактически существующих MVP-вариантов C01,
> C02 и C02.4 перед проектированием Goal/Outcome Taxonomy.
>
> Это исследование, не taxonomy design. Порядок работы: EVIDENCE FIRST →
> INVENTORY → GAPS/COLLISIONS → OWNER REVIEW → только потом SEMANTIC
> DECOMPOSITION (Stage 2, отдельная задача).
>
> **Дата среза:** 2026-08-20.

## 1. Purpose and scope

- Зафиксировать, какие C01/C02/C02.4 UX-варианты реально существуют в
  источниках репозитория, с точными формулировками и authority-статусом.
- Wording не нормализуется: разные актуальные формулировки показаны как
  collision.
- Этот документ **не** назначает direction / target.type / target.code /
  scope / Domain Goal code / Journey Mode code / Subject/Factor code /
  Recommendation family и **не** выполняет Desired Outcome semantic mapping.
  UX-фразы хранятся дословно.
- Stage-1 C02 UX option ≠ будущий semantic object; термин «Outcome» к C02
  UX-вариантам здесь не применяется (authority этого не устанавливает).

Границы из [[Ayla Goal Outcome Semantic Model Working Design]] v0.2
сохранены: Intent ≠ Transformation Goal; Goal не синтезируется искусственно;
C01 — human intent entry, не 1:1 Domain Goal selector; C02 может поддерживать
multi-select (owner direction OD-GO-4, не canon); `Desired Outcome` —
proposed terminology; direction+target+scope — working hypothesis;
Subject/Target Registry не создаётся. Working examples из Working Design
не считаются доказательством фактического UX.

Рабочие коды C01–C05 введены [[Ayla MVP Recommendation Contract]] v0.4 §34
(draft/proposed): C01 — вход/выбор цели (этапы 1–3 Journey v0.3), C02 —
Intent detection (этап 4), C03 — Clarification (этап 5). Маппинг на
канонические этапы Journey помечен как «подлежит подтверждению».

## 2. Method and search coverage

Targeted search по: `C01`, `C02`, `C02.4`, multi-select, interpretation,
«не знаю», «с чего начать», «лучше выглядеть», «лучше себя чувствовать»,
«расслабиться», «восстановиться», «заботиться о себе», «подготовиться к
событию», «сохранить результат», Customer/User Journey, UX, MVP, Goal,
Outcome. Затем: candidate docs → relevant sections → authority
classification → inventory.

Прямые вхождения кодов `C01`/`C02` в репозитории находятся только в
[[Ayla MVP Recommendation Contract]] v0.4 и
[[Ayla Goal Outcome Semantic Model Working Design]] v0.2; фактический UX
искался по смыслу (First Contact, категории/кнопки входа, intent detection,
clarification).

`repomix-output.xml` — packed-копия этого же репозитория, самостоятельным
источником не является и в inventory не учитывался.

## 3. Source authority classification

Классы: 1 — current canonical/approved spec; 2 — current draft/proposed
UX/implementation spec; 3 — owner decision; 4 — current design handoff в
knowledge; 5 — historical/reference; 6 — superseded/stale.

| Источник | Класс | Статус (frontmatter) | Что дал для C01/C02 |
|---|---|---|---|
| `01 Product/BOT-001 First Contact Specification.md` v1.0 | 1 | approved / accepted / canonical approved, 2026-08-12 | C01 entry model: free-text primary + 3–5 contextual Quick Actions; labels не канонизированы; 3 greeting states |
| `01 Product/BOT-002 Conversation Lifecycle Specification.md` v1.0 | 1 | approved / accepted / canonical approved, 2026-08-12 | Иерархия Conversation → Goal → Task → Current Focus; граница с BOT-001 |
| `01 Product/User Journeys/Ayla MVP User Journey Specification.md` v1.2 | 1 | approved / accepted / canonical approved, 2026-08-08 | Этапы 1–5: Entry (выбор категории состояния + свободный ввод), First interaction, Consent, Intent detection, Clarification |
| `01 Product/User Journeys/Ayla User Journey Specification.md` v1.2 (полная UJS) | 2 (см. COL-10) | status: review, activation_status: pending-infrastructure, 2026-07-19 | Единственный точный набор C01 labels: Stage 1 First Message (5 кнопок состояний + свободный ввод); Stage 2 Discovery slots |
| `03 AI System/Ayla Intent Model Specification.md` v1.0 (+ contracts 0.5) | 1 | approved (Active Canon), 2026-08-08 | C02-семантика: confidence bands, один вопрос за ход, ≤2 clarification-подходов, `UNKNOWN` sentinel |
| `05 Architecture/Ayla MVP Recommendation Contract.md` v0.4 | 2 | draft / proposed | Коды C01–C05 (§34); pipeline §5; Goal Resolution §27; Outcome Resolution §28 («явная таксономия / multi-select») |
| `05 Architecture/Ayla Goal Outcome Semantic Model Working Design.md` v0.2 | 2/3 | draft / proposed (owner directions OD-GO-1…6, не canon) | OD-GO-3/OD-GO-4: C01 не 1:1 Goal selector; C02/C02.4 multi-select 1..N — owner direction, не UX-факт |
| `01 Product/BOT-003 Discovery and Recommendation Conversation Specification.md` v0.1 | 2 | draft / proposed, canonical_status: candidate, 2026-08-13 | Граница BOT-001 → BOT-003; recommendation sufficiency (C03-сторона) |
| `01 Product/UX MVP/screens/customer/SCR-CUST-001.md` v0.1 | 2 | draft (product-requirements), 2026-07-29 | C01 экран: категории кнопками + свободный ввод; A3: состав категорий каноном НЕ зафиксирован (3–6 кнопок) |
| `01 Product/UX MVP/screens/customer/SCR-CUST-003.md` v0.1 | 2 | draft (product-requirements), 2026-07-29 | C02 экран: формулировки понимания по confidence, один вопрос, quick-reply как вариант дизайна |
| `01 Product/UX MVP/02-screen-inventory-customer.md` v0.6 | 2/4 | draft (product-requirements), 2026-08-02 | Покрытие этапов экранами; readiness; ссылки на stale SRC-12 |
| `01 Product/UX MVP/waves/design-wave-1a.md` v0.2 | 4 | draft (product-requirements), 2026-08-02 | Critical path 001 → 003 → 004; scope волны |
| `UX Agents/answers/A-BOT-001-Q4.md` | 3 | APPROVED, Product Owner, 2026-08-12 | Hybrid First Contact: free-text + 3–5 contextual quick actions; exact copy — follow-up Architect/UX Writer |
| `UX Agents/reports/UX-WINDOW-01-BOT-001-report.md` | 5 | working draft material, 2026-08-11 | Драфтовые наборы кнопок (new/returning/trigger-based) до решения Q4 |
| `UX Agents/reports/UX-WINDOW-02-evidence-report.md` | 5 | evidence report, 2026-08-11 | Фактический состав кнопок текущей реализации (salon-service-first) и реестр конфликтов doc↔impl |
| `UX Agents/questions/Q-BOT-001-04-first-contact-copy.md` | 5 | OPEN на 2026-08-11; фактически закрыт A-BOT-001-Q4 (2026-08-12) | Фиксация расхождения UJS-копи vs реализация |
| SRC-12 specs (`ai-bot-platform/docs/screens/customer-onboarding-flow.md`, `global-bot-welcome-consent-spec.md`, …) | 6 | stale, вне этого репозитория | Только косвенно (цитаты в UX-WINDOW-02); first-hand wording недоступен |
| Handoff `ai-bot-platform/docs/design/handoffs/2026-05-18-customer-first-time-handoff.md` | 6 | historical, вне этого репозитория | Template B1 кнопки — только цитата в UX-WINDOW-02 §4 |

## 4. C01 inventory

C01 = вход/выбор цели (этапы 1–3 MVP UJS). Фактический UX — First Contact
(BOT-001 / SCR-CUST-001). **Канонизированного набора labels не существует** —
это зафиксированное решение, а не пробел документа (BOT-001 §8.2/§12.2;
A-BOT-001-Q4). Ниже — все найденные фактические варианты.

| ID | Exact user-facing label | Source | Section/location | Authority/status | Next step | Notes |
|---|---|---|---|---|---|---|
| INV-C01-001 | «Или напиши своими словами 👇» (свободный ввод) | полная UJS | Stage 1 — First Message | review (COL-10); наследуется MVP UJS этап 1 как «факт» | S2 Discovery (полная UJS) / SCR-CUST-003 (MVP UX) | BOT-001 §11: free text — PRIMARY mode, MUST; Quick Actions не заменяют ввод |
| INV-C01-002 | «Я устала и хочу восстановиться» | полная UJS | Stage 1 — First Message | review (COL-10) | S2 Discovery | UX-WINDOW-01 §4.1 (draft): intent category `recovery` — драфтовая семантика, не канон |
| INV-C01-003 | «Хочу изменить тело или питание» | полная UJS | Stage 1 — First Message | review (COL-10) | S2 Discovery | Полная UJS scenario (line ~1652) использует этот выбор |
| INV-C01-004 | «Хочу начать заниматься» | полная UJS | Stage 1 — First Message | review (COL-10) | S2 Discovery | — |
| INV-C01-005 | «Что-то беспокоит» | полная UJS | Stage 1 — First Message | review (COL-10) | S2 Discovery | Дублируется в returning-наборе UX-WINDOW-01 с другой семантикой (COL-09) |
| INV-C01-006 | «Не знаю, с чего начать — помоги» | полная UJS | Stage 1 — First Message | review (COL-10) | S2 Discovery (guided clarification) | Unknown/discovery entry; Working Design §12: resolution/discovery state, не Goal |
| INV-C01-007 | «Записаться к мастеру» | BOT-001 | §12.2 Examples (non-canonical) | approved, но пример явно non-canonical | Intent progression | Иллюстративный пример Quick Action |
| INV-C01-008 | «Выбрать услугу» | BOT-001 | §12.2 Examples (non-canonical) | approved, пример non-canonical | Intent progression | — |
| INV-C01-009 | «Перенести запись» | BOT-001 | §12.2 Examples (non-canonical) | approved, пример non-canonical | Intent progression | — |
| INV-C01-010 | «Продолжить подбор» | BOT-001 | §12.2 Examples (non-canonical) | approved, пример non-canonical | Intent progression | Контекстный (Active Task) |
| INV-C01-011 | «booking a common service category» (concept-level, без UX-label) | BOT-001 | §8.2 New User examples | approved, пример illustrative | Intent progression | Концепт, не copy |
| INV-C01-012 | «asking what Ayla can help with» (concept-level) | BOT-001 | §8.2 | approved, пример illustrative | Intent progression | — |
| INV-C01-013 | «finding a specialist» (concept-level) | BOT-001 | §8.2 | approved, пример illustrative | Intent progression | — |
| INV-C01-014 | «continue the current Task» (concept-level) | BOT-001 | §10.2 Active Task QA | approved, concept | Task continuation | 3–5 действий, contextual |
| INV-C01-015 | «view or modify a related booking» (concept-level) | BOT-001 | §10.2 | approved, concept | Booking management | — |
| INV-C01-016 | «start a new request» (concept-level) | BOT-001 | §10.2 | approved, concept | New intent | — |
| INV-C01-017 | «Подобрать запись к специалисту» | UX-WINDOW-01 report | §4.2 returning user | historical draft (2026-08-11), pre-Q4 | S2 Discovery | Draft; labels после Q4 не канонизированы |
| INV-C01-018 | «Обсудить план» | UX-WINDOW-01 report | §4.2 | historical draft | S2 Discovery | — |
| INV-C01-019 | «Что-то беспокоит» (returning-вариант) | UX-WINDOW-01 report | §4.2 | historical draft | S2 Discovery | Дубль INV-C01-005 с иной draft-семантикой (COL-09) |
| INV-C01-020 | «Просто поболтать» | UX-WINDOW-01 report | §4.2 | historical draft | S3 Intent Understanding | Low-stakes open turn |
| INV-C01-021 | «Помоги восстановиться» | UX-WINDOW-01 report | §4.3 trigger-based (Recovery post / QR) | historical draft | S2 Discovery | Контекстный trigger-вариант |
| INV-C01-022 | «Проанализировать питание» | UX-WINDOW-01 report | §4.3 trigger-based | historical draft | S2 Discovery | Nutrition-контекст; nutrition вне MVP scope (SCR-CUST-001 design_notes) |
| INV-C01-023 | «Подобрать запись» | UX-WINDOW-01 report | §4.3 trigger-based (booking reminder) | historical draft | S2 Discovery | — |
| INV-C01-024 | «📅 Записаться» | UX-WINDOW-02 report §2.1 | текущая реализация (`WelcomeSkill`) | runtime evidence (reference), не knowledge canon | booking flow impl | Салон-service-first набор; конфликт с UJS зафиксирован (COL-03) |
| INV-C01-025 | «📋 Мои записи» | UX-WINDOW-02 report §2.1 | текущая реализация | runtime evidence | records impl | — |
| INV-C01-026 | «👤 Профиль» | UX-WINDOW-02 report §2.1 | текущая реализация | runtime evidence | Mini App impl | config-gated |
| INV-C01-027 | «🍽 Дневник еды» | UX-WINDOW-02 report §2.1 | текущая реализация | runtime evidence | food impl | Вне MVP-навигации (wave-1a §4) |
| INV-C01-028 | «💧 Вода» | UX-WINDOW-02 report §2.1 | текущая реализация | runtime evidence | water impl | Вне MVP-навигации |
| INV-C01-029 | «📊 Анкета» | UX-WINDOW-02 report §2.1 | текущая реализация | runtime evidence | anketa impl | Прямое нарушение запретов UJS Stage 1 и BOT-001 §13.3 |
| INV-C01-030 | «❓ Задать вопрос» / «❓ Помощь» / «▶️ Начать» | UX-WINDOW-02 report §2.1 | текущая реализация | runtime evidence | FAQ/consent impl | Три отдельные кнопки, сведены в одну строку как один impl-набор |
| INV-C01-031 | «📅 Записаться», «💅 Услуги и цены», «👤 Наши мастера», «📍 Где мы?» | UX-WINDOW-02 §4 (цитата handoff Template B1) | `2026-05-18-customer-first-time-handoff.md` (вне репозитория) | historical, external | — | First-hand источник недоступен (COL-08) |

**Greeting copy (контекст labels):** полная UJS Stage 1: «Привет! Я Ayla.
Помогу разобраться, что тебе сейчас нужно, и подобрать следующий шаг. Что
привело тебя?»; UX-WINDOW-01 returning-вариант: «Чем займёмся сегодня?».
Финальный greeting copy — открытый follow-up из A-BOT-001-Q4
(Architect/UX Writer), в knowledge не зафиксирован (COL-06).

**C01 states (BOT-001, approved):** ровно три greeting states — New User /
Returning User / User with an Active Task (P8). **C01 → далее:** SCR-CUST-001
primary_action: выбор категории или свободный текст → переход в SCR-CUST-003.

## 5. C02 inventory

C02 = Intent detection (этап 4 MVP UJS; RC v0.4 §34). **Фиксированного набора
C02 option labels в действующем UX не существует**: C02 — конверсационный
этап (динамическая формулировка понимания + уточняющие вопросы), а не меню.
Найденные поведенческие паттерны:

| Inventory ID | Parent C01 entry | Exact C02 user-facing label | Subtitle/helper text | Selection behavior | Source | Section/location | Authority/status | Conditions | Notes |
|---|---|---|---|---|---|---|---|---|---|
| INV-C02-001 | любой C01 (свободный ввод или кнопка) | Формулировка понимания (утвердительная, high confidence) | — | single (подтверждение не требуется до side-effect) | MVP UJS; SCR-CUST-003 | этап 4; states 1 | approved / draft | confidence high (>0.8) | Языком, не числом (SRC-02 этап 4) |
| INV-C02-002 | любой C01 | «Возможно, ты хочешь…» (подтверждающая формулировка) | — | single-confirm (подтверждение обязательно перед side-effect) | SCR-CUST-003; Intent Model | key_components; §Confidence and Clarification | draft / approved | medium confidence (0.5–0.8) | Ближайшее существующее поведение к confirmation interpretation |
| INV-C02-003 | любой C01 | Один конкретный уточняющий вопрос (`clarification_question`) | ссылается на сказанное пользователем | single (ответ на вопрос) | SCR-CUST-003; Intent Model | states 2; §Output Contract | draft / approved | `missing_required_slots` / `unmet_slot_requirements` | Лимит: ≤5 вопросов за Discovery (UX), ≤2 подхода на intent (runtime) |
| INV-C02-004 | любой C01 | Честное признание неопределённости (без имитации понимания) | — | n/a | SCR-CUST-003 | states 3 (unclear_input / N1) | draft | low confidence (<0.5) / `conflicting_slot` | Угадывание запрещено; повторная неудача → SCR-CUST-019 |
| INV-C02-005 | любой C01 | Quick-reply кнопки типовых ответов | — | unknown (вариант дизайна; свободный ввод всегда доступен) | SCR-CUST-003 | key_components | draft | — | Состав кнопок не специфицирован |
| INV-C02-006 | C01 (в т.ч. discovery entry) | Multi-select подтверждение нескольких интерпретаций (1..N) | — | multi-select (только proposed) | RC v0.4; Working Design OD-GO-4 | §28; §5 OD-GO-4 | proposed / owner direction (не canon) | несколько одновременно истинных интерпретаций | UX-экрана/состояния нет (COL-05, COL-07) |

Parent relation: в текущих источниках C02 не имеет фиксированного parent-
маппинга от C01 labels — любой C01 entry (кнопка или свободный текст) ведёт в
общий Intent detection (SCR-CUST-001 primary_action → SCR-CUST-003). Это
many-to-many по построению. Матрица соответствий C01 entry → semantic
outputs в Working Design §12 — рабочая декомпозиция (не evidence) и здесь
как parent relation не учитывается.

## 6. C02.4 / interpretation clarification inventory

Формальной спецификации C02.4 (interpretation clarification с multi-select)
в репозитории **нет**. Код «C02.4» введён Working Design v0.2 (D-6, OD-GO-4).
Найденные по смыслу позиции:

| Inventory ID | Trigger/user phrase | Options shown | Multi-select? | Confirmation action | Fallback/free text | Source | Authority/status | Notes |
|---|---|---|---|---|---|---|---|---|
| INV-C024-001 | Несколько правдоподобных интерпретаций слов пользователя | Несколько интерпретаций (состав не специфицирован) | Да (1..N) | Подтверждение выбранных вариантов | Не специфицирован | Working Design v0.2 | owner direction OD-GO-4 (captured, не canon) | Нет UX-экрана, состояний, post-confirm transition |
| INV-C024-002 | Outcome Resolution: источники «явная таксономия / multi-select» | Таксономия (не существует как канон, OQ-R11) | Да | Фиксация `source` + `confirmed` | Естественный язык; подтверждённая интерпретация | RC v0.4 §28 | draft / proposed | Контрактный источник outcomes, не UX-спецификация |
| INV-C024-003 | Medium confidence: «Возможно, ты хочешь…» | Одна интерпретация | Нет (single-confirm) | Подтвердить / поправить | Свободный ввод всегда доступен | SCR-CUST-003; Intent Model | draft / approved | Ближайшее существующее поведение; не multi-select |

## 7. Source-backed transition map

Подтверждённые текущими источниками переходы:

```text
C01 First Contact (BOT-001 / SCR-CUST-001, этапы 1–3 MVP UJS)
  |  выбор категории ИЛИ свободный ввод (SCR-CUST-001 primary_action)
  v
C02 Intent detection (SCR-CUST-003, этап 4 MVP UJS)
  |  requires_clarification == true
  +--> Clarification (этап 5 / SCR-CUST-003 states 2–3) — conditional
  |  повторная неудача (2 подхода) --> SCR-CUST-019 (terminal fallback)
  v
Recommendation (этап 7 / SCR-CUST-004)  [C04 по RC v0.4 §34]
```

- BOT-001 → BOT-003 boundary: BOT-003 стартует, когда progression вошёл в
  Discovery / Recommendation semantics (BOT-003 §5).
- C02.4 в карте отсутствует: позиция clarification-с-выбором-интерпретаций
  задана только в рабочем pipeline Working Design §18 и D-6
  (C02.4 → C03) — не подтверждена UX/Journey источниками.
- **Конфликт порядка (COL-04):** RC v0.4 §5 pipeline ставит Intent
  Resolution (обозначен «C02») шагом 1, а Goal Resolution (обозначен «C01»)
  шагом 3 — то есть в execution-порядке контракта C02 предшествует C01,
  хотя §34 того же контракта маппит C01 на этапы 1–3 (раньше C02, этап 4).
  Сам контракт помечает маппинг «подлежит подтверждению».

## 8. Collision / ambiguity register

Ничего не исправлено; только фиксация.

| ID | Type | Sources | Conflict / ambiguity | Impact on Stage 2 | Owner decision needed? |
|---|---|---|---|---|---|
| COL-01 | WORDING_COLLISION | полная UJS Stage 1 (5 точных state-кнопок) vs BOT-001 v1.0 §8.2/§12.2 (labels MUST NOT be canonicalized; 3–5 contextual) vs SCR-CUST-001 A3 (состав не зафиксирован) | Действует ли набор из 5 UJS-labels как prescriptive для MVP First Contact — не решено; BOT-001 (approved, новее) сознательно labels не фиксирует | Stage 2 не может считать 5 UJS labels финальным C01 set | Да |
| COL-02 | STATE_COLLISION | полная UJS (5 кнопок фикс.) vs BOT-001 / A-BOT-001-Q4 (3–5) vs SCR-CUST-001 A3 (3–6) | Число quick actions расходится | Часть COL-01 | Да (вместе с COL-01) |
| COL-03 | WORDING_COLLISION | UX-WINDOW-02 §2.1/§4 (реализация: salon-service-first, вкл. «📊 Анкета») vs полная UJS Stage 1 + BOT-001 §13.3 | Текущая реализация противоречит запретам (анкета, goal/action-кнопки); дрейф задокументирован | Implementation wording НЕ должно питать Stage 2 как UX-канон | Нет (модель решена Q4; дрейф — implementation follow-up) |
| COL-04 | FLOW_COLLISION | RC v0.4 §5 (C02 шаг 1 → C01 шаг 3) vs RC v0.4 §34 (C01 = этапы 1–3, C02 = этап 4) | Порядок кодов C01/C02 в execution pipeline противоположен journey-порядку | Маппинг C01↔C02↔этапы должен быть подтверждён до декомпозиции | Да (amendment RC; Working Design D-1) |
| COL-05 | SELECTION_BEHAVIOR_COLLISION | OD-GO-4 + RC v0.4 §28 (multi-select 1..N) vs Intent Model + SCR-CUST-003 (один вопрос, single-confirm) | Multi-select интерпретаций предложен, но не согласован с clarification-контрактом | Требует UX/contract решения до появления C02.4 | Да |
| COL-06 | MISSING_SOURCE | A-BOT-001-Q4 follow-up | Финальный greeting copy и quick-action set поручены Architect/UX Writer; в knowledge отсутствуют | Точные актуальные C01 labels недоступны | Да (производство follow-up) |
| COL-07 | MISSING_SOURCE | Working Design D-6 / OD-GO-4; RC v0.4 §28 | C02.4 formal spec отсутствует (trigger render, options, fallback, post-confirm transition) | C02.4 строки Stage 2 будут опираться на незаполненный слой | Да |
| COL-08 | MISSING_SOURCE | SRC-12 stale specs; handoff 2026-05-18 (оба — ai-bot-platform, вне репозитория) | First-hand historical wording недоступен в ayla-knowledge; только цитаты в UX-WINDOW-02 | Не блокирует (historical-only) | Нет |
| COL-09 | DUPLICATE_OPTION | полная UJS Stage 1 vs UX-WINDOW-01 §4.2 | «Что-то беспокоит» встречается в new-user и returning-наборах с разной draft-семантикой («state: concern» vs «self-care») | Если label возродится — семантика неоднозначна | Нет (drafts superseded; зафиксировано) |
| COL-10 | AMBIGUOUS_MEANING | полная UJS frontmatter (status: review, pending-infrastructure) vs UX source index SRC-03 («approved-with-amendments») | Authority-вес единственного точного набора C01 labels неоднозначен | Влияет на класс authority для INV-C01-002…006 | Да (governance-уточнение) |

## 9. Coverage audit

- **C01 entries found:** 16 current rows (INV-C01-001…016: 1 free-text mode,
  5 UJS labels, 7 illustrative/concept BOT-001, 3 Active-Task concepts) +
  15 historical/reference rows (INV-C01-017…031).
- **C02 options found:** 0 фиксированных label-наборов; 6 поведенческих
  паттернов (INV-C02-001…006), из них 1 — только proposed (multi-select).
- **C02 parent relations found:** 0 фиксированных; many-to-many по построению
  (любой C01 → общий Intent detection).
- **C02.4 examples found:** 0 специфицированных; 2 упоминания (OD-GO-4,
  RC §28) + 1 ближайшее существующее поведение (single-confirm).
- **Current authoritative sources:** 12 (см. §3, классы 1–4).
- **Historical-only items:** UX-WINDOW-01 drafts, UX-WINDOW-02
  implementation evidence, SRC-12 specs, handoff Template B1.
- **Conflicts:** 10 (COL-01…COL-10).
- **Missing evidence:** финальный greeting/quick-action copy (COL-06);
  C02 option set (COL-06/COL-07); C02.4 spec (COL-07); SRC-12 first-hand
  (COL-08).

Точечные проверки:

- **C01 без C02 continuation:** не найдено — все C01 входы ведут в Intent
  detection (SCR-CUST-003 / этап 4; historical drafts — в S2 Discovery).
- **C02 без parent:** неприменимо (фиксированных C02 options нет).
- **Option только в handoff:** INV-C01-031 (Template B1) — external,
  historical (COL-08).
- **Макет/Linear wording, не перенесённый в knowledge spec:** финальный copy
  из A-BOT-001-Q4 follow-up в knowledge отсутствует (COL-06).
- **Одинаковые labels с разным поведением:** «Что-то беспокоит» (COL-09);
  варианты «Записаться…» (INV-C01-007 vs INV-C01-024 vs INV-C01-031) —
  разные источники/эпохи, сведены в COL-03/COL-08.
- **C02.4 behavior без formal spec:** COL-07.

## 10. Linear check

Действующие C01/C02-документы не ссылаются на Linear как на UX-authority;
единственное упоминание Linear в репозитории —
[[Ayla Development Discipline]] §4 (решения для исполнителей фиксируются в
Linear или брифе). Полный аудит Linear не выполнялся (по правилу задачи);
Linear не изменялся. Evidence gap по Linear не требуется: knowledge-
источников достаточно для Stage 1 среза.

## 11. Stage 2 boundary

Этот документ не выполняет semantic decomposition. Следующая отдельная
задача после owner review сможет строить: C01 Entry → C02 UX option →
Desired Outcome candidate {direction, target.type, target.code, scope} →
required decision context → ambiguities/collisions.

Минимальные разблокировки для Stage 2: COL-01/COL-02 (статус UJS labels и
состав quick actions), COL-04 (порядок C01/C02 в RC), COL-06 (финальный
copy), COL-05/COL-07 (C02.4 spec).

## 12. Change Log

### v0.1 — 2026-08-20

- Создан Stage 1 evidence-backed inventory C01/C02/C02.4: 31 строка C01
  (16 current + 15 historical/reference), 6 C02-паттернов, 3 позиции C02.4,
  transition map, 10 collisions/gaps (COL-01…COL-10), coverage audit.
- Источник границ: [[Ayla Goal Outcome Semantic Model Working Design]] v0.2;
  working examples из него как evidence не использовались.
