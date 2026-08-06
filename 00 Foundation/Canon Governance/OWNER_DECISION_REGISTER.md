---
node_id: ayla.foundation.canon-governance.owner-decision-register
title: OWNER_DECISION_REGISTER
type: dashboard
status: draft
version: "0.2"
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
created: 2026-07-29
updated: 2026-08-05
review_cycle: monthly
---

# OWNER_DECISION_REGISTER

Реестр решений владельца продукта. Пуст при инициализации. Старые решения (включая `02 Strategy\Ayla Decision Log.md` и `AYLA-DEC-0011`) не импортируются автоматически.

## Правила

- Approved Owner Decisions обязательны к применению строго в пределах указанного в них scope.
- Owner Decision не может неявно переопределять Product Essence.
- Owner Decision создаётся только если после проверки по лестнице разрешения (см. `CANON_CONFLICT_REGISTER.md`) остаются минимум два разумных варианта, materially меняющих: продукт, MVP, главный journey, обязательства, safety/privacy, критический контракт или срок выпуска.

## Формат записи

```text
ID:             AYLA-DEC-XXXX
Date:           YYYY-MM-DD
Question:       —
Options:        —
Decision:       —
Rationale:      —
Scope:          — (точные границы применения)
Affected docs:  —
Status:         OPEN | DECIDED | SUPERSEDED
```

## Записи

### AYLA-DEC-0026 — Living Digital Twin as Ayla's Primary Visual Interface

```text
ID:             AYLA-DEC-0026
Date:           2026-07-29
Question:       Каково место Living Digital Twin в продукте Ayla?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Living Digital Twin является главным визуальным интерфейсом Ayla
                и долгоживущим цифровым отражением самого пользователя.
Rationale:      см. полный текст ruling (Recognition, Identity Preservation, Authentic Future)
Scope:          Product Essence v1.1; Living Digital Twin Manifesto; Product Vision;
                Product Thesis; Product Principles; MVP Scope; MVP User Journey;
                последующие Domain, UX, AI, Privacy/Safety и Engineering документы.
Affected docs:  Essence v1.1 (CREATE), LDT Manifesto (CREATE after v1.1 approval),
                пять Foundation-документов, реестры Canon Governance.
Status:         DECIDED
```

Каноническая запись решения:

> Living Digital Twin является главным визуальным интерфейсом Ayla и долгоживущим цифровым отражением самого пользователя. Его обязательное свойство — сохранение узнаваемой идентичности. Человек остаётся главным героем продукта, Transformation Goal — центральной доменной сущностью, Ayla — интеллектуальным помощником и оркестратором пути. Ayla показывает не усреднённый идеальный образ, а правдоподобные изменения именно этого человека и ясно разделяет фактическое состояние, реконструкцию, прогноз и цель.

Разделение центров:

```text
Продуктовая ценность: человек
Главный визуальный интерфейс: Living Digital Twin
Центральная доменная сущность: Transformation Goal
Интеллектуальная координация: Ayla
```

Примечание по ID: предпочтительный `AYLA-DEC-0012` занят в `02 Strategy\Ayla Decision Log.md` (owner directions по Domain Capability Registry); по правилу ruling использован следующий свободный — `AYLA-DEC-0026` (Decision Log занимает диапазон до `AYLA-DEC-0025`).

Источник: `D:\Проекты\Ayla\OWNER_RULING_LIVING_DIGITAL_TWIN_PRIMARY_VISUAL_INTERFACE.md` (owner ruling, 2026-07-29). Owner Decision не переопределяет Product Essence; изменение Essence выполняется через подготовку v1.1 с отдельным owner approval.

**Implementation / Canonization note (2026-07-30):**

> Living Digital Twin Manifesto v1.0 approved by Product Owner on 2026-07-30 (APPROVE_WITH_NON_BLOCKING_EDITORIAL_NOTES). Final consistency review passed with P0=0, P1=0, P2=0. Two non-blocking editorial notes (P3-1, P3-2) were applied in commit `b072a05`. Manifesto canonized under Product Essence v1.1. Это исполнительная отметка к AYLA-DEC-0026, не новое продуктовое решение.

**Implementation / Canonization note — Product Vision v2.0 (2026-07-30):**

> Product Vision v2.0 approved by Product Owner on 2026-07-30 (APPROVE_WITH_NON_BLOCKING_EDITORIAL_NOTES). Internal consistency review: APPROVED_FOR_OWNER_REVIEW (P0=0, P1=0, P2=0). P3-1 и P3-2 применены в editorial cleanup (`85ccd5c`); P3-3 принят как намеренная терминологическая вариативность. Повторный owner review не требовался. Product Vision v2.0 канонизирован под Product Essence v1.1 (Manifesto v1.0 — согласующий input для LDT-положений). Это исполнительная отметка (Foundation sequence, документ №1), не новое продуктовое решение.

**Implementation / Canonization note — Product Principles v0.1 (2026-07-31):**

> Ayla Product Principles v0.1 approved by Product Owner on 2026-07-31 (APPROVE_WITH_NON_BLOCKING_EDITORIAL_NOTES). Internal consistency review: APPROVED_FOR_OWNER_REVIEW (P0=0, P1=0, P2=0). PP-ICR-P3-1 применён в editorial cleanup (`ff30f68`). Повторный owner review не требовался. Product Principles v0.1 канонизирован (Foundation document №3); номер версии сохранён — владелец одобрил именно v0.1, изменение номера требует отдельного versioning decision. Документ стал authoritative input для MVP Scope, User Journey, UX Development Standard, Screen Registry, Component Library, Domain decisions, feature prioritization и Measurement Framework. Смысл AYLA-DEC-0026 не изменён. Это исполнительная отметка, не новое продуктовое решение.

**Implementation / Canonization note — Product Thesis v0.5 (2026-07-30):**

> Ayla MVP Product Thesis v0.5 approved by Product Owner on 2026-07-30 (APPROVE_WITH_NON_BLOCKING_EDITORIAL_NOTES). Internal consistency review: APPROVED_FOR_OWNER_REVIEW (P0=0, P1=0, P2=0). ICR-P3-1, ICR-P3-2, ICR-P3-3 применены в editorial cleanup (`65296ca`). Повторный owner review не требовался. Product Thesis v0.5 канонизирован (Foundation document №2); номер версии сохранён — владелец одобрил именно v0.5, изменение номера требует отдельного versioning decision. Документ стал authoritative input для Product Principles, MVP Scope, User Journey и Measurement Framework. Смысл AYLA-DEC-0002, AYLA-DEC-0018 и AYLA-DEC-0026 не изменён. Это исполнительная отметка, не новое продуктовое решение.

### AYLA-DEC-0027 — Required MVP Channel Set (OD-CH-1)

```text
ID:             AYLA-DEC-0027 (owner ruling ID: OD-CH-1)
Date:           2026-07-31
Question:       Какой набор каналов обязателен для MVP пилота?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Mobile application — REQUIRED / PRIMARY PRODUCT EXPERIENCE;
                MAX Mini App — REQUIRED / LIGHTWEIGHT EMBEDDED EXPERIENCE;
                MAX bot — REQUIRED / CONVERSATIONAL, NOTIFICATION AND ROUTING EXPERIENCE.
                Feature parity — NOT_REQUIRED. Shared backend/domain/safety/consent/
                analytics — REQUIRED. Единая идентичность пользователя и cross-channel
                continuity обязательны. Три канала — один продукт, не три независимых
                продукта. Отсутствие второстепенной функции в Mini App или боте не
                блокирует релиз, если capability доступна в назначенном owning channel.
                Mobile выпускается к началу реального пилота A1/A2; mobile release
                readiness включает закрытое тестирование и подготовку публикации;
                store-review timing — release dependency.
Rationale:      Mobile владеет полной визуальной и longitudinal experience (Twin,
                photo capture, progress, history); MAX Mini App — облегчённый embedded
                сценарий; MAX-бот — диалог, уведомления, быстрые действия, маршрутизация.
                Business logic, safety, consent, recommendation, memory и attribution
                не дублируются в каналах.
Scope:          MVP Scope v0.3 (§6.1, §8, §9, §10, §11, §12, §14, §15, Change Log —
                targeted revision, версия сохраняется v0.3); Single-Provider и
                Multi-Provider Execution Scopes; downstream UX/channel/deep-link/push
                документы.
Affected docs:  MVP Scope v0.3 (TARGETED_REVISION_REQUIRED), Ayla Single-Provider
                Technical Pilot Execution Scope, Ayla Multi-Provider Product
                Validation Execution Scope, UX MVP.
Status:         DECIDED
```

Соотношение с AYLA-DEC-0004: уточняет, не отменяет. MAX-бот и MAX Mini App сохраняются как required companion channels; Telegram остаётся вне пилотного scope. Положение «MAX-бот + MAX Mini App — единственные обязательные каналы MVP» (MVP Scope v0.3 §8) устарело и подлежит targeted revision.

Источник: `D:\Проекты\Ayla\TWO_PHASE_PILOT_OWNER_DIRECTIONS_AND_MOBILE_CHANNEL_AMENDMENT_PROMPT.md` §2, §4, §5 (owner ruling, 2026-07-31). Channel ownership matrix и revised phase/channel model — нормативная часть ruling, применяется в targeted revision MVP Scope и revision execution scopes.

### AYLA-DEC-0028 — Food Scanner: один из равнозначных trigger-сценариев (OD-TP-1)

```text
ID:             AYLA-DEC-0028 (owner ruling ID: OD-TP-1)
Date:           2026-07-31
Question:       Является ли Food Scanner обязательным activation trigger или одним
                из равнозначных trigger-сценариев?
Options:        n/a — прямое решение Product Owner (ruling)
Decision:       FOUR_EQUAL_TRIGGER_MODEL. Food Scanner — CONDITIONAL / one equal
                trigger scenario; не является обязательным activation trigger и не
                является центром MVP. Food-specific metrics — DIAGNOSTIC; primary
                metrics — TRIGGER_AGNOSTIC.
Rationale:      Подтверждает AYLA-DEC-0002, Vision §10 и MVP Scope v0.3 §6.1
                (food — CONDITIONAL); снимает food-center framing из execution scopes.
Scope:          Single-Provider и Multi-Provider Execution Scopes (структура daily
                loop, P0 scope, метрики); Measurement Framework (trigger-agnostic
                primary metrics).
Affected docs:  Single-Provider Execution Scope, Multi-Provider Execution Scope,
                Measurement Framework (planned).
Status:         DECIDED
```

### AYLA-DEC-0029 — 28-day cycle: A2 exit evidence (OD-TP-2)

```text
ID:             AYLA-DEC-0029 (owner ruling ID: OD-TP-2)
Date:           2026-07-31
Question:       Обязателен ли полный 28-дневный цикл до первого реального запуска
                и до B0?
Options:        n/a — прямое решение Product Owner (ruling)
Decision:       REQUIRED_AS_A2_EXIT_EVIDENCE. Не требуется до A0 или A1. Требуется:
                достаточная и явно определённая A2-когорта завершает 28-дневный путь
                до B0 entry. Точный denominator и достаточная доля участников
                определяются Measurement Framework до A2 launch.
Rationale:      Ранняя проверка spine не должна блокироваться полным циклом;
                стабильность полного цикла — exit evidence A2, не entry gate.
Scope:          Single-Provider Execution Scope (фазы A0/A1/A2, entry/exit gates);
                Measurement Framework (denominator и доля — до A2 launch).
Affected docs:  Single-Provider Execution Scope, Measurement Framework (planned).
Status:         DECIDED
```

### AYLA-DEC-0030 — Provider mix для B0/B1 (OD-TP-3)

```text
ID:             AYLA-DEC-0030 (owner ruling ID: OD-TP-3)
Date:           2026-07-31
Question:       Какой provider mix обязателен для B0 и B1?
Options:        n/a — прямое решение Product Owner (ruling)
Decision:       B0_CANONICAL_PROFILE_ONLY. B0: «Формула тела» + 1–2 независимых
                провайдера — соло-специалист и/или малый салон до 3 специалистов
                (канонический профиль Thesis §5). B1: 3–5 салонов + 5–10 соло-мастеров.
                Крупный салон — DEFERRED: требует отдельного owner decision и
                отдельной когорты.
Rationale:      Подтверждает канонический provider-профиль; исключает скрытое
                расширение MVP boundary через beta-состав.
Scope:          Multi-Provider Execution Scope (формат B0/B1, состав провайдеров).
Affected docs:  Multi-Provider Execution Scope.
Status:         DECIDED
```

### AYLA-DEC-0031 — Cold acquisition: только B1 после B0 exit (OD-TP-4)

```text
ID:             AYLA-DEC-0031 (owner ruling ID: OD-TP-4)
Date:           2026-07-31
Question:       Когда вводится cold acquisition?
Options:        n/a — прямое решение Product Owner (ruling)
Decision:       B1_ONLY_AFTER_B0_EXIT. До B1 — warm users и пользователи вновь
                подключённых провайдеров. В B0 обязательна хотя бы одна когорта,
                не являющаяся клиентами «Формулы тела».
Rationale:      Repeatability-вопрос отделяется от acquisition-вопроса; premature
                cold traffic смешал бы причины провала.
Scope:          Multi-Provider Execution Scope (когортный дизайн, entry gates B1).
Affected docs:  Multi-Provider Execution Scope.
Status:         DECIDED
```

### AYLA-DEC-0032 — Порядок monetization validation (OD-TP-5)

```text
ID:             AYLA-DEC-0032 (owner ruling ID: OD-TP-5)
Date:           2026-07-31
Question:       Какая модель монетизации проверяется первой и в каком порядке?
Options:        n/a — прямое решение Product Owner (ruling)
Decision:       Порядок: (1) подписка соло-мастера 690 ₽; (2) подписка салона 990 ₽;
                (3) fee за completed booking 90 ₽; (4) комбинированная модель.
                Клиент Ayla не платит. Customer willingness-to-pay не является
                monetization target; вместо неё измеряются willingness to use,
                share permitted data, follow recommendations and book through Ayla.
Rationale:      Соответствует действующей модели AYLA-DEC-0001 и Constitution
                Ст. IV (пользователь не платит за доступ к Ayla).
Scope:          Multi-Provider Execution Scope (Monetization Validation);
                Measurement Framework.
Affected docs:  Multi-Provider Execution Scope, Measurement Framework (planned).
Status:         DECIDED
```

### AYLA-DEC-0033 — Статус числовых порогов (OD-TP-6)

```text
ID:             AYLA-DEC-0033 (owner ruling ID: OD-TP-6)
Date:           2026-07-31
Question:       Какие числовые пороги являются истинными go/no-go, а какие —
                рабочими гипотезами?
Options:        n/a — прямое решение Product Owner (ruling)
Decision:       REQUIRED HARD GATES: user data loss = 0; critical safety
                incidents = 0; economic influence on ranking = 0; consent bypass = 0;
                direct attribution chain technically available and auditable.
                WORKING VALIDATION THRESHOLDS: все процентные цели execution
                документов — retention, weekly review completion,
                recommendation-to-booking, booking-to-appointment, provider
                continuation, provider willingness to pay, attribution completeness
                percentage. FINAL GO/NO-GO утверждается до B1 после B0 evidence и
                Measurement Framework.
Rationale:      Подтверждает Thesis §8.1 (пороги — design candidates) и MVP Scope
                §11; исключает неявную канонизацию beta-порогов через execution docs.
Scope:          Оба Execution Scopes (все числовые пороги получают явный статус);
                Measurement Framework.
Affected docs:  Single-Provider Execution Scope, Multi-Provider Execution Scope,
                Measurement Framework (planned).
Status:         DECIDED
```

### AYLA-DEC-0034 — Контрольная группа в initial beta (OD-TP-7)

```text
ID:             AYLA-DEC-0034 (owner ruling ID: OD-TP-7)
Date:           2026-07-31
Question:       Требуется ли контрольная группа без Twin или без процедур?
Options:        n/a — прямое решение Product Owner (ruling)
Decision:       NO_FORMAL_RCT_IN_INITIAL_BETA. Обязательны: observational cohort
                comparison; qualitative Twin recognition/correction evidence;
                сравнение по глубине Twin-вовлечения; явное заявление, что это не
                устанавливает причинную атрибуцию. Formal controlled experiment —
                DEFERRED to Product Experiment Design after initial beta.
Rationale:      Формальный RCT в initial beta непропорционален; вклад Twin
                оценивается наблюдательно с честным заявлением об ограничениях
                (Honest Representation, Principles 4.5).
Scope:          Multi-Provider Execution Scope (экспериментальный дизайн);
                Product Experiment Design (post-beta).
Affected docs:  Multi-Provider Execution Scope, Product Experiment Design (planned).
Status:         DECIDED
```

### AYLA-DEC-0036 — Wave 1 Simple Reschedule: только same-ID time-only механика (OD-RESCHED-1)

```text
ID:             AYLA-DEC-0036 (owner ruling ID: OD-RESCHED-1)
Date:           2026-08-02
Question:       Какая механика переноса записи обязательна для Wave 1 Simple
                Reschedule и что остаётся deferred?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из
                эскалированных вариантов
Decision:       Wave 1 Simple Reschedule выполняется только как same-ID,
                time-only изменение по AYLA-DEC-0022 (сохраняется
                appointment_id, версия монотонно увеличивается, публикуется
                appointment.rescheduled). Механика cancel_then_create_new_booking
                для переноса ЗАПРЕЩЕНА для Simple Reschedule. Полная
                Cancellation journey остаётся deferred (owner ruling
                2026-07-28, вариант Б; этим решением не расширяется и не
                сужается). Replacement, смена специалиста, смена услуги,
                изменение цены/длительности и cross-tenant перенос остаются
                deferred для Wave 1.
Rationale:      Устраняет расхождение между UX MVP слоем (ранее —
                cancel_then_create_new_booking в UX-OD-001) и канонической
                доменной моделью AYLA-DEC-0022; формализует owner direction от
                2026-08-02, ранее применённую в UX-документах как неформальная
                пометка без registered ID (UX-SYNC-001 → UX reconciliation
                2026-08-02).
Scope:          UX MVP слой Wave 1 Simple Reschedule (bot DM + Mini App,
                customer surface). Не переопределяет AYLA-DEC-0022 по существу
                и не расширяет Wave 1 за пределы time-only переноса в рамках
                исходного Offering.
Affected docs:  decisions/ux-owner-decisions.md (UX-OD-001),
                flows/customer-cancel-reschedule-stages.md (UX-SPEC-001),
                gaps/UX-GAP-0105.md, context/current-session-brief.md,
                02-screen-inventory-customer.md (SCR-CUST-013).
Status:         DECIDED
```

Соотношение с AYLA-DEC-0022: уточняет обязательность применения канонической same-ID/time-only модели к Wave 1 UX-scope и явно запрещает `cancel_then_create_new_booking` как альтернативу для этого сценария; не переопределяет саму доменную модель (п. 1, 2, 9, 10 AYLA-DEC-0022 остаются источником механики).

Источник: owner ruling, Product Owner, 2026-08-02; формализация ранее применённого owner direction в UX-документах.

### AYLA-DEC-0037 — Journey Philosophy (OD-1)

```text
ID:             AYLA-DEC-0037 (owner ruling ID: OD-1)
Date:           2026-08-04
Question:       Какова философия сквозного пользовательского пути MVP и что является его терминалом?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Lifecycle approved v1.1 `Conversation → Understanding → Recommendation → Execution → Learning` сохранён и расширен целевым якорем Transformation Goal и Living Digital Twin как непрерывным представлением контекста, состояния и прогресса; booking — опциональное downstream-действие; терминал journey — progress / next state, а не подтверждение записи.
Rationale:      Утверждённая философия пути продолжает центрировать продукт вокруг человека и его Transformation Goal, сохраняя одобренную в v1.1 структуру.
Scope:          MVP User Journey Specification v1.2 §Purpose, §Journey Operating Model, §Journey Overview.
Affected docs:  Ayla MVP User Journey Specification v1.2.
Status:         DECIDED
```

Источник: Owner Decision Session 2026-08-04; зафиксировано в Change Log v1.2 документа Ayla MVP User Journey Specification.

### AYLA-DEC-0038 — Conversation Lifecycle (OD-2)

```text
ID:             AYLA-DEC-0038 (owner ruling ID: OD-2)
Date:           2026-08-04
Question:       Должен ли journey документ фиксировать продуктовый lifecycle разговора?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Продуктовый lifecycle разговора (Conversation Lifecycle) зафиксирован как продуктовая логика из 10 элементов, которую позже реализует Conversation Runtime; документ не описывает Conversation Runtime/FSM/Storage/Schema.
Rationale:      Разграничение продуктовой логики и runtime-реализации сохраняет journey как продуктовый фундамент.
Scope:          MVP User Journey Specification v1.2 §Journey Operating Model / Conversation Lifecycle.
Affected docs:  Ayla MVP User Journey Specification v1.2.
Status:         DECIDED
```

Источник: Owner Decision Session 2026-08-04; зафиксировано в Change Log v1.2 документа Ayla MVP User Journey Specification.

### AYLA-DEC-0039 — Journey Stages (OD-3)

```text
ID:             AYLA-DEC-0039 (owner ruling ID: OD-3)
Date:           2026-08-04
Question:       Каков состав и роль этапов в MVP Journey v1.2?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Все 14 этапов approved v1.1 сохранены (KEEP/EXTEND); Goal, LDT и Progress оформлены как сквозные концепции, а не обязательные линейные стадии; этапы 10–12 (booking) — опциональная downstream-ветка.
Rationale:      Сохраняет утверждённую структуру v1.1 при расширении её целевыми якорями.
Scope:          MVP User Journey Specification v1.2 §Journey Overview, §Stage Specifications.
Affected docs:  Ayla MVP User Journey Specification v1.2.
Status:         DECIDED
```

Источник: Owner Decision Session 2026-08-04; зафиксировано в Change Log v1.2 документа Ayla MVP User Journey Specification.

### AYLA-DEC-0040 — Living Digital Twin Role (OD-4)

```text
ID:             AYLA-DEC-0040 (owner ruling ID: OD-4)
Date:           2026-08-04
Question:       Какова роль Living Digital Twin в MVP Journey?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Living Digital Twin — центральное пользовательское представление контекста, состояния и прогресса, главный визуальный интерфейс ключевых сценариев; не самостоятельный Source of Truth и не единственный центр продукта; Twin baseline/media — backend domain data, не persistent semantic memory.
Rationale:      Уточняет роль Twin в соответствии с AYLA-DEC-0026 и предотвращает отождествление Twin и memory.
Scope:          MVP User Journey Specification v1.2 §Terminology, §Journey Operating Model, §Memory Interaction.
Affected docs:  Ayla MVP User Journey Specification v1.2.
Status:         DECIDED
```

Источник: Owner Decision Session 2026-08-04; зафиксировано в Change Log v1.2 документа Ayla MVP User Journey Specification.

### AYLA-DEC-0041 — Three MVP Channels (OD-5)

```text
ID:             AYLA-DEC-0041 (owner ruling ID: OD-5)
Date:           2026-08-04
Question:       Как в journey отражается обязательный набор MVP-каналов?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Раздел Cross-channel Experience приведён в соответствие с AYLA-DEC-0027; доступность конкретных действий определяется channel capability matrix, UX contract и rollout phase.
Rationale:      Обеспечивает единую Journey для трёх каналов без требования функциональной симметрии.
Scope:          MVP User Journey Specification v1.2 §Cross-channel Experience.
Affected docs:  Ayla MVP User Journey Specification v1.2.
Status:         DECIDED
```

Источник: Owner Decision Session 2026-08-04; зафиксировано в Change Log v1.2 документа Ayla MVP User Journey Specification.

### AYLA-DEC-0042 — Memory Target State (OD-6)

```text
ID:             AYLA-DEC-0042 (owner ruling ID: OD-6)
Date:           2026-08-04
Question:       Какая модель памяти используется в MVP Journey?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Модель «target state + phase rollout»: Phase 1 — session context + active-flow slots + authoritative backend facts, persistent memory disabled; Phase 2 — opt-in persistent memory после CSR gate; восьмичленное разграничение сущностей — независимы, с собственными владельцами и lifecycle.
Rationale:      Разграничивает сущности памяти и предотвращает упрощения типа LDT = Memory, Session = Memory, Backend Facts = Memory.
Scope:          MVP User Journey Specification v1.2 §Memory Interaction.
Affected docs:  Ayla MVP User Journey Specification v1.2.
Status:         DECIDED
```

Источник: Owner Decision Session 2026-08-04; зафиксировано в Change Log v1.2 документа Ayla MVP User Journey Specification.

### AYLA-DEC-0043 — Intent Boundary (OD-7)

```text
ID:             AYLA-DEC-0043 (owner ruling ID: OD-7)
Date:           2026-08-04
Question:       Какие границы Intent Model применяются в journey?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Границы Intent Model v1.0 приняты как journey-level нормативный язык: Transformation Goal ≠ intent, recommendation intent — system-owned, orchestration state ≠ product intent, downstream action — не только LLM; runtime-канон остаётся Intent Model v0.9.2 / Output Contract 0.5.
Rationale:      Journey использует продуктовую семантику intent, не вводя runtime-контрактов.
Scope:          MVP User Journey Specification v1.2 §Terminology, §Stage Specifications (этапы 4–5, 7–8).
Affected docs:  Ayla MVP User Journey Specification v1.2.
Status:         DECIDED
```

Источник: Owner Decision Session 2026-08-04; зафиксировано в Change Log v1.2 документа Ayla MVP User Journey Specification.

### AYLA-DEC-0044 — ControlAction (OD-8)

```text
ID:             AYLA-DEC-0044 (owner ruling ID: OD-8)
Date:           2026-08-04
Question:       Как классифицировать управляющие команды пользователя в journey?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Управляющие команды пользователя оформлены как ControlAction — owner-approved product concept; ControlAction управляют memory, consent, personalization и conversation ownership; не ProductIntent и не расширение Product Intent Registry; термин не подразумевает отдельного registry/contract/capability.
Rationale:      Создаёт чёткую продуктовую категорию для управляющих действий без введения новых runtime-сущностей.
Scope:          MVP User Journey Specification v1.2 §Terminology, §Stage Specifications (этап 3, N4.2, N4.4).
Affected docs:  Ayla MVP User Journey Specification v1.2.
Status:         DECIDED
```

Источник: Owner Decision Session 2026-08-04; зафиксировано в Change Log v1.2 документа Ayla MVP User Journey Specification.

### AYLA-DEC-0045 — Recommendation Model (OD-9)

```text
ID:             AYLA-DEC-0045 (owner ruling ID: OD-9)
Date:           2026-08-04
Question:       Какова модель рекомендаций в MVP Journey?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Approved lifecycle рекомендаций сохранён; рекомендация привязана к Transformation Goal, если связь установлена; `no_action` — полноценный объяснимый результат; LLM не является ranking authority; acceptance recommendation ≠ booking; attribution осуществляется через `recommendation_id`.
Rationale:      Сохраняет экономическую нейтральность и ответственность рекомендаций, разделяя рекомендацию и действие.
Scope:          MVP User Journey Specification v1.2 §Recommendation and Proactivity Gates, §Stage Specifications (этапы 7–9, 12).
Affected docs:  Ayla MVP User Journey Specification v1.2.
Status:         DECIDED
```

Источник: Owner Decision Session 2026-08-04; зафиксировано в Change Log v1.2 документа Ayla MVP User Journey Specification.

### AYLA-DEC-0046 — Recommendation Gates (OD-10)

```text
ID:             AYLA-DEC-0046 (owner ruling ID: OD-10)
Date:           2026-08-04
Question:       Какие recommendation gates активны в MVP?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       В MVP существуют только user-initiated рекомендации; Proactive Readiness Gate неактивен; persistent memory сама по себе не открывает proactive behavior; любые proactive recommendations требуют отдельного Product/Privacy owner decision.
Rationale:      Соответствует CSR §10 и ограничивает проактивность до явного owner decision.
Scope:          MVP User Journey Specification v1.2 §Recommendation and Proactivity Gates.
Affected docs:  Ayla MVP User Journey Specification v1.2.
Status:         DECIDED
```

Источник: Owner Decision Session 2026-08-04; зафиксировано в Change Log v1.2 документа Ayla MVP User Journey Specification.

### AYLA-DEC-0047 — Negative Scenarios (OD-11)

```text
ID:             AYLA-DEC-0047 (owner ruling ID: OD-11)
Date:           2026-08-04
Question:       Как организованы негативные сценарии в journey v1.2?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Негативные сценарии реорганизованы в 6 классов; добавлены сценарии invalid structured output, unresolved goal, stale state/version conflict, authoritative confirmation delay, memory unavailable, consent revoked, deletion request, abandon/resume, interrupted channel, account linking conflict, human handoff, manual intervention, no_action; runtime mechanics вынесены за пределы документа.
Rationale:      Сохраняет продуктовую полноту негативных сценариев без погружения в runtime implementation.
Scope:          MVP User Journey Specification v1.2 §Negative Scenarios.
Affected docs:  Ayla MVP User Journey Specification v1.2.
Status:         DECIDED
```

Источник: Owner Decision Session 2026-08-04; зафиксировано в Change Log v1.2 документа Ayla MVP User Journey Specification.

### AYLA-DEC-0048 — Learning Loop (OD-12)

```text
ID:             AYLA-DEC-0048 (owner ruling ID: OD-12)
Date:           2026-08-04
Question:       Какие уровни learning фиксируются в MVP Journey?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Уровни learning зафиксированы: Session Learning, Outcome Learning, Memory Proposal, Persistent Memory, Model Training, Personalization, Recommendation Analytics; Memory Proposal допускается в Phase 1 без persistent write и без публикации `memory.*`; цепочка Outcome → Feedback → Optional Memory Proposal → Phase 2 Consent & Eligibility → Persistent Memory Write.
Rationale:      Определяет learning-архитектуру journey без введения runtime storage mechanics.
Scope:          MVP User Journey Specification v1.2 §Memory Interaction, §Stage Specifications (этап 14).
Affected docs:  Ayla MVP User Journey Specification v1.2.
Status:         DECIDED
```

Источник: Owner Decision Session 2026-08-04; зафиксировано в Change Log v1.2 документа Ayla MVP User Journey Specification.

### AYLA-DEC-0049 — Follow-up and Continuity (OD-13)

```text
ID:             AYLA-DEC-0049 (owner ruling ID: OD-13)
Date:           2026-08-04
Question:       Как устроены follow-up и cross-channel continuity в journey?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Follow-up — транзакционное сообщение или согласованный check-in; cross-channel continuity переносит только разрешённую context projection; conversation ownership не переносится автоматически между каналами.
Rationale:      Сохраняет контроль пользователя и чёткие границы сессий при cross-channel переходах.
Scope:          MVP User Journey Specification v1.2 §Cross-channel Experience, §Stage Specifications (этап 13).
Affected docs:  Ayla MVP User Journey Specification v1.2.
Status:         DECIDED
```

Источник: Owner Decision Session 2026-08-04; зафиксировано в Change Log v1.2 документа Ayla MVP User Journey Specification.

### AYLA-DEC-0050 — Scope and Deferred (OD-14)

```text
ID:             AYLA-DEC-0050 (owner ruling ID: OD-14)
Date:           2026-08-04
Question:       Как в journey v1.2 представлен scope?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Добавлен раздел с классификацией IN_SCOPE / PHASED / DEFERRED / TARGET_STATE_ONLY; Journey не дублирует Release Contract; в scope включены простой feedback, Memory Proposal (Phase 1), транзакционные уведомления, booking как опциональная ветка, Simple Reschedule same-ID time-only; phased/deferred элементы явно обозначены.
Rationale:      Создаёт единую классификацию scope внутри journey и разграничивает её с Release Contract.
Scope:          MVP User Journey Specification v1.2 §Scope and Deferred.
Affected docs:  Ayla MVP User Journey Specification v1.2.
Status:         DECIDED
```

Источник: Owner Decision Session 2026-08-04; зафиксировано в Change Log v1.2 документа Ayla MVP User Journey Specification.

### AYLA-DEC-0051 — Event Consistency (OD-15)

```text
ID:             AYLA-DEC-0051 (owner ruling ID: OD-15)
Date:           2026-08-04
Question:       Как в journey v1.2 отражается статус domain events?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Все события приведены к Ayla Domain Event Registry v0.4 с точным registration status (`registered` / `registration proposed` / NOT_DEFINED / LEGACY_ALIAS); терминология canonical event name / registration status / registry status разведена; wildcard-статусы заменены per-event перечислениями.
Rationale:      Гарантирует, что journey не создаёт новых domain events и не повышает их статус.
Scope:          MVP User Journey Specification v1.2 §Stage Specifications, §Event Usage Summary.
Affected docs:  Ayla MVP User Journey Specification v1.2.
Status:         DECIDED
```

Источник: Owner Decision Session 2026-08-04; зафиксировано в Change Log v1.2 документа Ayla MVP User Journey Specification.

### AYLA-DEC-0052 — Capability Consistency (OD-16)

```text
ID:             AYLA-DEC-0052 (owner ruling ID: OD-16)
Date:           2026-08-04
Question:       Как Journey v1.2 ссылается на capabilities?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Поле «owning capability» заменено на «capability reference»; Journey описывает только product availability; формулировка «Capability mapping will be assigned during Capability Registry Wave 2»; capability mapping — исключительно как reference.
Rationale:      Journey не зависит от существования конкретных CAP-ID и не вводит capability ownership.
Scope:          MVP User Journey Specification v1.2 §Stage Specifications (capability reference).
Affected docs:  Ayla MVP User Journey Specification v1.2.
Status:         DECIDED
```

Источник: Owner Decision Session 2026-08-04; зафиксировано в Change Log v1.2 документа Ayla MVP User Journey Specification.

### AYLA-DEC-0053 — Metadata and Domain Consistency (OD-17)

```text
ID:             AYLA-DEC-0053 (owner ruling ID: OD-17)
Date:           2026-08-04
Question:       Какие терминологические и metadata-уточнения внесены в journey v1.2?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Добавлен раздел Terminology (appointment, booking как legacy alias, Transformation Goal, Living Digital Twin, Conversation, Session, Interaction, Dialogue Turn, ControlAction); обязательные разделы типа `user-journey-specification` сохранены; Canon Lineage зафиксирована в текстовом блоке.
Rationale:      Устраняет неоднозначность терминов и обеспечивает соответствие metadata-правилам.
Scope:          MVP User Journey Specification v1.2 §Terminology, frontmatter.
Affected docs:  Ayla MVP User Journey Specification v1.2.
Status:         DECIDED
```

Источник: Owner Decision Session 2026-08-04; зафиксировано в Change Log v1.2 документа Ayla MVP User Journey Specification.

### AYLA-DEC-0054 — Downstream Updates (OD-18)

```text
ID:             AYLA-DEC-0054 (owner ruling ID: OD-18)
Date:           2026-08-04
Question:       Каков статус downstream-документов относительно Journey v1.2?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Downstream scope зафиксирован в Canonical Position; Journey — продуктовый фундамент, не центр синхронизации остальных документов; downstream документы синхронизируются относительно Journey, а не наоборот.
Rationale:      Определяет направление traceability и предотвращает превращение journey в coordination hub.
Scope:          MVP User Journey Specification v1.2 §Canonical Position.
Affected docs:  Ayla MVP User Journey Specification v1.2.
Status:         DECIDED
```

Источник: Owner Decision Session 2026-08-04; зафиксировано в Change Log v1.2 документа Ayla MVP User Journey Specification.

### AYLA-DEC-0055 — Conversation Identity (AYLA-OD-CM-008)

```text
ID:             AYLA-DEC-0055 (owner ruling ID: AYLA-OD-CM-008)
Date:           2026-08-05
Question:       Что определяет идентичность Conversation и когда возникает новая Conversation?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Conversation сохраняет идентичность на протяжении всего жизненного цикла; смена Session, канала связи, устройства или временной паузы сама по себе НЕ создаёт новую Conversation. Новая Conversation возникает только если: (1) пользователь начинает новую независимую Transformation Goal; (2) предыдущая Conversation завершена согласно Conversation Lifecycle; (3) владелец системы или пользователь явно инициирует новую Conversation согласно правилам Canon. Каноническая иерархия: Conversation → Session → Interaction → Dialogue Turn; Session принадлежит ровно одной Conversation, Interaction — ровно одной Session, Dialogue Turn — ровно одной Interaction.
Rationale:      Conversation представляет пользовательскую цель и её развитие во времени; Session — отдельную операционную сессию общения. Разделение сохраняет непрерывность пользовательского опыта, поддерживает multi-session диалог и cross-channel continuity, не смешивает продуктовую модель с runtime и упрощает работу Recommendation, Memory и Runtime Canon. Conversation Identity определяется смыслом пользовательского взаимодействия, а не техническими характеристиками соединения; Runtime Canon реализует эти правила, но не определяет их.
Scope:          Conversation Model (продуктовая модель); иерархия Conversation / Session / Interaction / Dialogue Turn. Не переопределяет runtime mechanics (ADR-0014) и не изменяет существующие scope-ограничения Consent Scope Registry.
Affected docs:  Conversation Model Specification v1.0 (Source of Truth, документ планируется); терминология согласуется с Ayla MVP User Journey Specification v1.2 §Terminology.
Status:         DECIDED
```

Источник: WINDOW-03 — Owner Decision Session (Conversation Model Canonicalization), 2026-08-05; решение AYLA-OD-CM-008, статус ACCEPTED.

### AYLA-DEC-0056 — Conversation is the Root Entity (AYLA-OD-CM-001)

```text
ID:             AYLA-DEC-0056 (owner ruling ID: AYLA-OD-CM-001)
Date:           2026-08-05
Question:       Является ли Conversation корневой сущностью Conversation Model?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Conversation является корневой сущностью Conversation Model; Conversation может включать несколько Session, Interaction и Dialogue Turn.
Rationale:      Устанавливает иерархическую роль Conversation как корня модели и чётко определяет её состав.
Scope:          Conversation Model (продуктовая модель); иерархия Conversation / Session / Interaction / Dialogue Turn.
Affected docs:  Conversation Model Specification v1.0 (Source of Truth, документ планируется).
Status:         DECIDED
```

Источник: WINDOW-03 — Owner Decision Session (Conversation Model Canonicalization), 2026-08-05; решение AYLA-OD-CM-001, статус ACCEPTED.

### AYLA-DEC-0057 — Session is a Canonical Entity (AYLA-OD-CM-002)

```text
ID:             AYLA-DEC-0057 (owner ruling ID: AYLA-OD-CM-002)
Date:           2026-08-05
Question:       Является ли Session самостоятельной канонической продуктовой сущностью?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Session является самостоятельной канонической продуктовой сущностью с собственным концептуальным lifecycle; Session не является только технической runtime-концепцией.
Rationale:      Разграничивает продуктовую сущность Session и runtime implementation, предотвращая свёртывание Session в технический деталь.
Scope:          Conversation Model (продуктовая модель); lifecycle и статус Session.
Affected docs:  Conversation Model Specification v1.0 (Source of Truth, документ планируется).
Status:         DECIDED
```

Источник: WINDOW-03 — Owner Decision Session (Conversation Model Canonicalization), 2026-08-05; решение AYLA-OD-CM-002, статус ACCEPTED.

### AYLA-DEC-0058 — Interaction is a Conversation Episode (AYLA-OD-CM-003)

```text
ID:             AYLA-DEC-0058 (owner ruling ID: AYLA-OD-CM-003)
Date:           2026-08-05
Question:       Какой канонический термин описывает логически связанный эпизод общения в Conversation Model?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Interaction — логически связанный эпизод общения, состоящий из одного или нескольких Dialogue Turn; канонический термин — Interaction. Interaction Episode может сохраняться только как исторический или поясняющий alias в существующих документах.
Rationale:      Фиксирует каноническую терминологию, допуская legacy alias без переписывания существующих документов.
Scope:          Conversation Model (продуктовая модель); терминология Interaction / Interaction Episode.
Affected docs:  Conversation Model Specification v1.0 (Source of Truth, документ планируется).
Status:         DECIDED
```

Источник: WINDOW-03 — Owner Decision Session (Conversation Model Canonicalization), 2026-08-05; решение AYLA-OD-CM-003, статус ACCEPTED.

### AYLA-DEC-0059 — Conversation State is Conceptual (AYLA-OD-CM-004)

```text
ID:             AYLA-DEC-0059 (owner ruling ID: AYLA-OD-CM-004)
Date:           2026-08-05
Question:       Какой характер имеет Conversation State в Conversation Model?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Conversation State описывает смысловое состояние разговора; Conversation Model не определяет runtime FSM, enum, storage state machine или конкретную реализацию переходов.
Rationale:      Разграничивает концептуальную модель и runtime implementation, оставляя технические детали Runtime Canon.
Scope:          Conversation Model (продуктовая модель); conceptual Conversation State.
Affected docs:  Conversation Model Specification v1.0 (Source of Truth, документ планируется).
Status:         DECIDED
```

Источник: WINDOW-03 — Owner Decision Session (Conversation Model Canonicalization), 2026-08-05; решение AYLA-OD-CM-004, статус ACCEPTED.

### AYLA-DEC-0060 — Conversation Owns Only Conversation Context (AYLA-OD-CM-005)

```text
ID:             AYLA-DEC-0060 (owner ruling ID: AYLA-OD-CM-005)
Date:           2026-08-05
Question:       Каким данными владеет Conversation в рамках Conversation Model?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Conversation владеет только Conversation Context; Conversation не владеет persistent memory, authoritative backend facts, recommendation context, consent state или user profile. Эти данные могут использоваться только через разрешённую Context Projection.
Rationale:      Ограничивает область ответственности Conversation, предотвращая неявное поглощение чужих доменов и обеспечивая чёткое разделение ownership.
Scope:          Conversation Model (продуктовая модель); ownership и Context Projection.
Affected docs:  Conversation Model Specification v1.0 (Source of Truth, документ планируется).
Status:         DECIDED
```

Источник: WINDOW-03 — Owner Decision Session (Conversation Model Canonicalization), 2026-08-05; решение AYLA-OD-CM-005, статус ACCEPTED.

### AYLA-DEC-0061 — Runtime Boundary (AYLA-OD-CM-006)

```text
ID:             AYLA-DEC-0061 (owner ruling ID: AYLA-OD-CM-006)
Date:           2026-08-05
Question:       Какие аспекты определяет Conversation Model, а какие остаются за пределами её scope?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Conversation Model определяет сущности, отношения, identity, ownership, conceptual lifecycle, invariants и context projection. Conversation Model не определяет prompts, prompt assembly, orchestration graph, LLM routing, tool dispatch implementation, retry/reconciliation mechanics, database schema, API или runtime FSM.
Rationale:      Чётко разграничивает продуктовую модель и runtime/implementation details, предотвращая размывание ответственности модели.
Scope:          Conversation Model (продуктовая модель); границы scope.
Affected docs:  Conversation Model Specification v1.0 (Source of Truth, документ планируется).
Status:         DECIDED
```

Источник: WINDOW-03 — Owner Decision Session (Conversation Model Canonicalization), 2026-08-05; решение AYLA-OD-CM-006, статус ACCEPTED.

### AYLA-DEC-0062 — Source of Truth Ownership (AYLA-OD-CM-007)

```text
ID:             AYLA-DEC-0062 (owner ruling ID: AYLA-OD-CM-007)
Date:           2026-08-05
Question:       Какие домены находятся в ownership Conversation Model как Source of Truth?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Conversation Model становится Source of Truth для Conversation, Session, Interaction, Dialogue Turn, Conversation Identity, Conversation Lifecycle, conceptual Conversation State и Context Projection. Она не становится Source of Truth для Intent (Intent Model), Transformation Goal (canonical product concept / Journey), Recommendation (Recommendation Contract), Memory (Memory Model), Consent (Consent Scope Registry), Runtime FSM (Runtime Canon) или domain entities and authoritative backend facts (Core Domain Model).
Rationale:      Фиксирует границы authority Conversation Model, предотвращая конфликты Source of Truth с другими доменами.
Scope:          Conversation Model (продуктовая модель); Source of Truth ownership.
Affected docs:  Conversation Model Specification v1.0 (Source of Truth, документ планируется); соответствующие документы остаются Source of Truth для своих доменов.
Status:         DECIDED
```

Источник: WINDOW-03 — Owner Decision Session (Conversation Model Canonicalization), 2026-08-05; решение AYLA-OD-CM-007, статус ACCEPTED.
