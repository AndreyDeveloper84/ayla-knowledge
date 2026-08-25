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
updated: 2026-08-20
review_cycle: monthly
---

# OWNER_DECISION_REGISTER

Реестр решений владельца продукта. Пуст при инициализации. Старые решения (включая `02 Strategy\Ayla Decision Log.md` и `AYLA-DEC-0011`) не импортируются автоматически.

## Правила

- Approved Owner Decisions обязательны к применению строго в пределах указанного в них scope.
- Один идентификатор `AYLA-DEC-NNNN` = одно решение на всю Knowledge Base. Один ID не может обозначать решения разных уровней (стратегическое, MVP boundary, техническое) или разных предметных областей; перед присвоением номер проверяется по обоим реестрам (этот регистр и `02 Strategy\Ayla Decision Log.md`). Переиспользование и повторная выдача занятого номера запрещены.
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

Примечание по ID: предпочтительный `AYLA-DEC-0012` занят в `02 Strategy\Ayla Decision Log.md` (owner directions по Domain Capability Registry); по правилу ruling использован следующий свободный — `AYLA-DEC-0026` (на момент регистрации Decision Log занимал диапазон до `AYLA-DEC-0025`). 2026-08-18 Decision Log присвоил тот же номер записи «Master MVP Canon Freeze» — коллизия KB-001; разрешена 2026-08-19: AYLA-DEC-0026 сохранён за настоящим решением (Living Digital Twin), freeze-запись перенумерована в AYLA-DEC-0080 (см. Decision Log v1.11 и `docs/audits/2026-08-19-KB-001-DEC-0026-collision-repair.md`).

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

### AYLA-DEC-0063 — Living Digital Twin excluded from mandatory MVP critical path (OD-MVP-1)

```text
ID:             AYLA-DEC-0063 (owner ruling ID: OD-MVP-1)
Date:           2026-08-07
Question:       Является ли Living Digital Twin обязательной частью
                critical path первого MVP?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из
                эскалированных вариантов
Decision:       Living Digital Twin исключается из обязательного critical
                path первого MVP. LDT не является условием запуска MVP,
                controlled pilot, доказательства основной MVP-гипотезы или
                прохождения MVP release gate. LDT сохраняется как
                strategic visual capability, potential differentiator,
                personal representation layer и future validation track —
                не удаляется из продукта и не признаётся ошибочной
                концепцией. Если LDT используется в конкретном релизе,
                LDT-specific требования (recognizability, honesty, identity
                continuity, correction, user control) продолжают
                действовать без ослаблений.
Rationale:      Первый MVP должен проверить способность Ayla создавать
                повторяемую пользовательскую ценность через понимание
                цели, повседневного контекста, рекомендации, действия,
                память и прогресс — не жизнеспособность отдельной
                Twin-модели.
Scope:          Ayla Product Essence (v1.1 → v1.2); Ayla — Product Vision
                (v2.0 → v2.1); Ayla MVP Product Thesis (v0.5 → v0.6); Ayla
                Product Principles (v0.1 → v0.2); Ayla Living Digital Twin
                Manifesto §14 (v1.0 → v1.1, minimal conditional amendment);
                Ayla MVP Scope and Release Contract (v0.3 → v0.4).
Affected docs:  Essence v1.2, Vision v2.1, Thesis v0.6, Principles v0.2,
                LDT Manifesto v1.1, MVP Scope v0.4 (все candidate, ожидают
                Product Owner Final Review). Follow-up: Ayla MVP User
                Journey Specification v1.2 alignment (не выполнено в этой
                канонизации — отдельный gate).
Status:         DECIDED
```

Соотношение с AYLA-DEC-0026: уточняет и частично заменяет — AYLA-DEC-0026
(2026-07-29) установила LDT главным визуальным интерфейсом и не делала
различия между MVP и долгосрочным продуктом. AYLA-DEC-0063 сохраняет
долгосрочную стратегическую роль LDT из AYLA-DEC-0026, но явно разделяет
long-term direction (LDT remains important) и MVP scope (LDT not
mandatory). AYLA-DEC-0026 в части «LDT — долгоживущее цифровое отражение,
потенциальный differentiator» не отменена.

Источник: `Ayla MVP v2 — Owner Decisions` (Owner Approved), раздел
OD-MVP-1; передано в задаче канонизации `AGENT_AYLA_MVP_CANON_AMENDMENTS_AND_ALIGNMENT`.

### AYLA-DEC-0064 — Food Intelligence as first concrete Everyday Signal in MVP (OD-MVP-2)

```text
ID:             AYLA-DEC-0064 (owner ruling ID: OD-MVP-2)
Date:           2026-08-07
Question:       Является ли Food Intelligence / Food Scanner обязательной
                частью MVP, и если да — какова его роль?
Options:        n/a — прямое решение Product Owner (ruling)
Decision:       Food Intelligence / Food Scanner входит в обязательный MVP
                как первый реализованный источник повседневного
                пользовательского контекста (Everyday Signal). Не является
                самостоятельным calorie-tracking продуктом, полноценным
                дневником питания или источником медицинских выводов.
                Food НЕ становится центральной сущностью Ayla и НЕ
                становится вечной частью Product Essence/Thesis — на
                верхних уровнях канона используется generic понятие
                `Signal` / `Everyday Signal`; exact Food scope принадлежит
                MVP Scope and Release Contract.
Rationale:      Даёт MVP конкретный, реализуемый источник контекста для
                Goal → Signal → Context → Recommendation loop без
                превращения продукта в food-first identity.
Scope:          Essence v1.2 §12 (Signal остаётся generic); Thesis v0.6
                §4.1, §4.2, §6; Principles v0.2 §4.4, §4.12 (Observation ≠
                medical fact); MVP Scope v0.4 §3, §4, §6.1.
Affected docs:  Essence v1.2, Thesis v0.6, Principles v0.2, MVP Scope v0.4.
Status:         DECIDED
```

Соотношение с AYLA-DEC-0028 (Food Scanner — FOUR_EQUAL_TRIGGER_MODEL):
уточняет для MVP-контекста — Food остаётся одним из равнозначных
trigger-сценариев на уровне Vision/Killer PRD (AYLA-DEC-0028 не отменена),
и одновременно становится первой конкретной MVP-реализацией класса
`Everyday Signal` на уровне MVP Scope. Оба решения совместимы: trigger
neutrality на продуктовом уровне, конкретный release choice на MVP уровне.

Источник: `Ayla MVP v2 — Owner Decisions` (Owner Approved), раздел
OD-MVP-2.

### AYLA-DEC-0065 — Memory Foundation in MVP from the start, progressive persistence (OD-MVP-3)

```text
ID:             AYLA-DEC-0065 (owner ruling ID: OD-MVP-3)
Date:           2026-08-07
Question:       Входит ли Memory Foundation в MVP с самого начала, и в
                каком объёме?
Options:        n/a — прямое решение Product Owner (ruling)
Decision:       Memory Foundation входит в MVP с самого начала, но MVP не
                обязан до первого пилота реализовывать полноценную
                long-term personalization platform. Используется
                progressive model: Working Context → Memory Candidate →
                Policy/Consent Gate → Persistent Memory. Memory
                оценивается через continuity value, а не через количество
                сохранённых фактов. Persistent memory не следует
                автоматически из любого observation (Observation ≠
                Persistent Memory Fact; AI inference ≠ User Fact).
Rationale:      Обеспечивает MVP работоспособной моделью continuity без
                преждевременного обязательства по полной персонализации.
Scope:          Essence (implicit via §12 Memory Continuity); Thesis v0.6
                §4.3, §8.1 S3; Principles v0.2 §4.5 (Progressive Memory +
                User Control); MVP Scope v0.4 §3, §6.1 (Memory Foundation),
                §6.3.
Affected docs:  Thesis v0.6, Principles v0.2, MVP Scope v0.4.
Status:         DECIDED
```

Источник: `Ayla MVP v2 — Owner Decisions` (Owner Approved), раздел
OD-MVP-3.

### AYLA-DEC-0066 — MVP hypothesis: Goal → Signal → Context → Recommendation → Action → Memory → Progress (OD-MVP-4)

```text
ID:             AYLA-DEC-0066 (owner ruling ID: OD-MVP-4)
Date:           2026-08-07
Question:       Какова целевая проверяемая гипотеза первого MVP?
Options:        n/a — прямое решение Product Owner (ruling)
Decision:       MVP больше не обязан доказывать ценность Living Digital
                Twin. Первый MVP должен доказать способность Ayla
                создавать повторяемый полезный цикл: Goal → Signal →
                Context → Recommendation → Action → Memory → Progress (⟲).
                Booking является одним из downstream Action, а не конечной
                ценностью продукта. Количество сообщений, DAU, число
                booking, время в приложении, число распознанных фото и
                число memory facts — не являются самостоятельным
                доказательством успеха (допустимы как диагностические
                метрики).
Rationale:      Разворачивает и делает проверяемой формулировку central
                thesis без обязательной зависимости от LDT.
Scope:          Essence v1.2 §12, §17 (главный продуктовый цикл и MVP
                hypothesis); Thesis v0.6 §4.1, §4.3 (central hypothesis и
                validation loop); MVP Scope v0.4 §3.
Affected docs:  Essence v1.2, Thesis v0.6, MVP Scope v0.4.
Status:         DECIDED
```

Источник: `Ayla MVP v2 — Owner Decisions` (Owner Approved), раздел
OD-MVP-4; итоговый owner ruling зафиксирован дословно в исходном документе.

**Canonization note (2026-08-07):**

> AYLA-DEC-0063…0066 проведены через Product Essence (v1.1 → v1.2), Ayla —
> Product Vision (v2.0 → v2.1, minimal derived-alignment amendment без
> отдельного amendment plan), Ayla MVP Product Thesis (v0.5 → v0.6), Ayla
> Product Principles (v0.1 → v0.2), Ayla Living Digital Twin Manifesto
> (v1.0 → v1.1, единственное minimal targeted изменение §14) и Ayla MVP
> Scope and Release Contract (v0.3 → v0.4). Все шесть документов
> переведены в статус `draft` / `canonical_status: candidate` и ожидают
> Product Owner Final Review — они не объявлены CANONICAL этой
> канонизацией. `Ayla MVP User Journey Specification v1.2` содержит
> собственный недавний набор owner decisions (AYLA-DEC-0037…0054,
> 2026-08-04) и MUST_HAVE-ссылки на прежний MVP Scope §6.4; alignment этого
> документа с AYLA-DEC-0063…0066 зарегистрирован как отдельный follow-up
> gate и не выполнен в рамках этой канонизации. Три non-canonical execution
> scope/migration документа (Single-Provider Execution Scope, Multi-Provider
> Execution Scope, MVP v0.3 Downstream Migration Plan) содержат
> version-pinned ссылки на «MVP Scope v0.3» и также зарегистрированы как
> follow-up. См. итоговый отчёт канонизации для полного списка.

### AYLA-DEC-0067 — Memory entity/state model: Composition of AYLA-DEC-0024 and ADR-0012 (OD-MEM-1)

```text
ID:             AYLA-DEC-0067 (owner ruling ID: OD-MEM-1)
Date:           2026-08-08
Question:       Как Memory Model примиряет entity/state-модели
                AYLA-DEC-0024 (MemoryProposal / MemoryEntry) и ADR-0012
                (многомерная classification/lifecycle модель)?
Options:        A — DEC-0024 only; B — ADR-0012 replaces DEC-0024;
                C — Composition (выбрано)
Decision:       Composition. MemoryProposal и MemoryEntry с базовым
                lifecycle из AYLA-DEC-0024 остаются canonical entity
                contract: MemoryProposal statuses —
                pending_confirmation | accepted | rejected | expired;
                MemoryEntry — persistent canonical fact без confidence;
                коррекция только через supersession (old entry →
                superseded, new entry → active). Многомерные признаки
                ADR-0012 (knowledge_class, confidence-измерение,
                lifetime, provenance, freshness/sensitivity semantics)
                используются как classification, policy metadata и
                proposal/audit dimensions — не как второй конкурирующий
                lifecycle MemoryEntry.
Rationale:      Не ломает действующий owner decision (AYLA-DEC-0024);
                сохраняет простой persistent contract; позволяет
                использовать многомерность ADR-0012; не создаёт две
                конкурирующие state machines.
Scope:          Memory Domain; entity и lifecycle semantics будущей
                Memory Model. Explicit non-scope: DB schema, ORM model,
                storage representation, exact TTL values, runtime
                transition engine.
Affected docs:  Memory Model v1.0 (Source of Truth, документ
                планируется); AYLA-DEC-0024 (Ayla Decision Log) —
                сохраняет силу; ADR-0012 — canonical в части
                classification/policy layer, non-canonical в части
                конкурирующего entity lifecycle.
Status:         DECIDED
```

Источник: WINDOW-04 — Owner Decision Session (Memory Model
Canonicalization), 2026-08-08; решение OD-MEM-1, статус ACCEPTED.

### AYLA-DEC-0068 — Memory Domain: canonical name and ownership boundary (OD-MEM-2)

```text
ID:             AYLA-DEC-0068 (owner ruling ID: OD-MEM-2)
Date:           2026-08-08
Question:       Как называется canonical conceptual domain будущей
                Memory Model и какова его ownership boundary?
Options:        A — User Context Domain; B — Memory Domain (выбрано);
                C — Memory & Identity Domain
Decision:       Canonical conceptual domain — Memory Domain. Memory
                Model владеет: MemoryProposal, MemoryEntry, memory
                lifecycle semantics, memory epistemic/persistence
                semantics. Memory Model НЕ владеет: Conversation
                Context, Session Context, Consent, Intent,
                Recommendation, Backend Facts, Transformation Goal.
                Memory Service (W3) — runtime/component owner, а не
                название conceptual domain.
Rationale:      Исключает смешение Persistent Memory с Conversation /
                Session Context (риск варианта User Context Domain) и
                не добавляет Identity в scope Memory Model без
                необходимости (риск варианта Memory & Identity Domain).
Scope:          Memory Domain; naming и ownership boundary.
Affected docs:  Memory Model v1.0 (Source of Truth, документ
                планируется). Использования «Memory & Identity Domain»
                и «User Context Domain» в AMD-020, Data Inventory
                Matrix, Core Domain Model §12, MVP User Journey,
                Consent Scope Registry §5.7, Domain Capability Registry
                (CAP-001) подлежат выравниванию при будущих targeted
                amendments — не в рамках этой регистрации.
Status:         DECIDED
```

Источник: WINDOW-04 — Owner Decision Session (Memory Model
Canonicalization), 2026-08-08; решение OD-MEM-2, статус ACCEPTED.

### AYLA-DEC-0069 — Memory canonical terminology (OD-MEM-3)

```text
ID:             AYLA-DEC-0069 (owner ruling ID: OD-MEM-3)
Date:           2026-08-08
Question:       Какой словарь становится canonical в Memory Model при
                наличии competing terms (Working Context, Memory
                Candidate, Context Fact, User Fact и др.)?
Options:        A — принять предложенный vocabulary mapping (выбрано);
                B — Context Fact как равноправный canonical synonym
                MemoryEntry; C — Memory Candidate как отдельная
                canonical entity
Decision:       Canonical vocabulary: Observation — входное
                наблюдение/сигнал, ещё не persistent fact; Conversation
                Context — внешний context, owned by Conversation Model;
                MemoryProposal — canonical persistence candidate;
                MemoryEntry — canonical persisted memory record/fact;
                Authoritative Backend Fact — внешний authoritative
                fact, не MemoryEntry по факту существования. Alias
                mapping: Memory Candidate → alias / explanatory term
                для MemoryProposal; Working Context → non-canonical
                generic term (использовать термин владеющего context);
                Session Context → термин Conversation Model, не entity
                Memory Model; Context Fact → legacy/ambiguous alias,
                canonical persistent term = MemoryEntry; Signal →
                generic input/observation term, не Memory entity;
                User Fact → epistemic classification, не persistence
                entity. Отдельная canonical entity Memory Candidate
                не создаётся.
Rationale:      Фиксирует единый словарь на уже утверждённых entity
                (AYLA-DEC-0024) без создания лишних сущностей и
                параллельных терминов.
Scope:          Memory Domain; терминология Memory Model и alias
                mapping legacy/competing terms.
Affected docs:  Memory Model v1.0 (Source of Truth, документ
                планируется); Ayla Glossary (выравнивание memory-терминов
                при будущем amendment).
Status:         DECIDED
```

Источник: WINDOW-04 — Owner Decision Session (Memory Model
Canonicalization), 2026-08-08; решение OD-MEM-3, статус ACCEPTED.

### AYLA-DEC-0070 — Memory Eligibility is a decision concept, not an entity (OD-MEM-4)

```text
ID:             AYLA-DEC-0070 (owner ruling ID: OD-MEM-4)
Date:           2026-08-08
Question:       Нужна ли отдельная canonical entity/state Memory
                Eligibility?
Options:        A — отдельная сущность/aggregate MemoryEligibility;
                B — decision concept, не persisted entity (выбрано)
Decision:       Memory eligibility — canonical decision concept, но не
                отдельная persisted entity. Это композиция проверок:
                consent + allowed category / whitelist + purpose +
                lifecycle state + freshness/validity +
                sensitivity/safety restrictions. Результат — eligible /
                not eligible для конкретной операции/purpose — не
                становится самостоятельным Source of Truth.
Rationale:      Предотвращает появление ещё одного владельца поверх
                Consent / Memory / Policy; сохраняет eligibility как
                проверку использования, а не как хранимое состояние.
Scope:          Memory Domain; eligibility semantics. Explicit
                non-scope: порядок и short-circuit семантика проверок,
                runtime исполнитель gate. Dependencies (не решаются
                этим решением): CSR-OD-5 (Consent Source of Truth),
                CSR-OD-4 / OD-1 (diet/skin legal boundary).
Affected docs:  Memory Model v1.0 (Source of Truth, документ
                планируется); Consent Scope Registry — остаётся
                владельцем consent-проверки.
Status:         DECIDED
```

Источник: WINDOW-04 — Owner Decision Session (Memory Model
Canonicalization), 2026-08-08; решение OD-MEM-4, статус ACCEPTED.

### AYLA-DEC-0071 — Memory events: semantics in Memory Model, registration stays with DER (OD-MEM-5)

```text
ID:             AYLA-DEC-0071 (owner ruling ID: OD-MEM-5)
Date:           2026-08-08
Question:       Должен ли WINDOW-04 одновременно повышать memory events
                до registration_status: registered?
Options:        A — да, автоматически при approval Memory Model;
                B — нет, registration остаётся DER governance (выбрано)
Decision:       Memory Model канонизирует semantic lifecycle и смысл
                memory events (memory.proposal_created,
                memory.proposal_confirmed, memory.proposal_rejected,
                memory.entry_created, memory.entry_superseded,
                memory.entry_expired, memory.entry_revoked), но
                registration status остаётся собственностью Domain
                Event Registry governance. После стабилизации Memory
                Model выполняется отдельный targeted DER reconciliation
                (proposed → registered) только для событий, прошедших
                DER acceptance criteria. memory.entry_deleted не
                определяется в Memory Model — сохраняется dependency на
                OQ-E4 / deletion contract. Legacy ContextFact* mappings
                закрываются в том же DER reconciliation, а не внутри
                conceptual Memory Model.
Rationale:      Разделяет conceptual canon и event registry governance;
                не смешивает approval модели с acceptance criteria
                регистрации событий.
Scope:          Memory Domain; семантика memory events. Explicit
                non-scope: registration status, payload-схемы,
                producer/consumer wiring. Dependencies (не решаются
                этим решением): Domain Event Registry OQ-E3 / OQ-E4.
Affected docs:  Memory Model v1.0 (Source of Truth, документ
                планируется); Ayla Domain Event Registry — targeted
                reconciliation отдельной задачей.
Status:         DECIDED
```

Источник: WINDOW-04 — Owner Decision Session (Memory Model
Canonicalization), 2026-08-08; решение OD-MEM-5, статус ACCEPTED.

### AYLA-DEC-0072 — Cross-repo memory boundary: responsibility boundaries, not repo mapping (OD-MEM-6)

```text
ID:             AYLA-DEC-0072 (owner ruling ID: OD-MEM-6)
Date:           2026-08-08
Question:       Какой уровень cross-repo boundary канонизирует Memory
                Model?
Options:        A — жёстко закрепить конкретные repositories/components;
                B — канонизировать responsibility boundaries, repo
                mapping в RRM (выбрано)
Decision:       Memory Model канонизирует responsibility boundaries:
                Memory Domain → conceptual MemoryProposal / MemoryEntry
                semantics; Persistent Memory Authority → durable
                write/read state; Retrieval Layer → запросы
                purpose-scoped eligible memory; Rendering Layer →
                model-facing context из уже авторизованной retrieved
                memory; Conversation/Orchestration → consumes memory
                context, но не становится memory SoT. Конкретный
                repo/component mapping (Memory Service W3,
                ai-bot-platform, ayla-ai-core) фиксируется в Repository
                Responsibility Matrix как current implementation
                reference; identity домена не зависит от названия
                репозитория.
Rationale:      Позволяет менять deployment/repo layout без изменения
                conceptual canon; не утверждает неподтверждённые
                repository/component names как вечную архитектуру.
Scope:          Memory Domain; responsibility boundaries. Explicit
                non-scope: конкретные repo names как canon, deployment
                topology, API contracts между компонентами.
Affected docs:  Memory Model v1.0 (Source of Truth, документ
                планируется); Ayla Repository Responsibility Matrix —
                current implementation mapping при будущем обновлении.
Status:         DECIDED
```

Источник: WINDOW-04 — Owner Decision Session (Memory Model
Canonicalization), 2026-08-08; решение OD-MEM-6, статус ACCEPTED.

### AYLA-DEC-0073 — Reconfirmation is a usage/freshness gate, not a lifecycle state (OD-MEM-7)

```text
ID:             AYLA-DEC-0073 (owner ruling ID: OD-MEM-7)
Date:           2026-08-08
Question:       Является ли confirmation_required новым lifecycle state
                MemoryEntry?
Options:        A — да, добавить в canonical MemoryEntry lifecycle;
                B — нет, usage/freshness gate (выбрано); C — отдельная
                canonical entity ReconfirmationRequest
Decision:       confirmation_required / reconfirmation — usage/freshness
                gate, а не persistent lifecycle state. MemoryEntry
                сохраняет свой canonical lifecycle (AYLA-DEC-0024).
                При использовании записи система может определить
                «reconfirmation required before this use» из-за
                freshness, expiry proximity, conflict, changeability,
                sensitivity/safety relevance или policy; до
                reconfirmation запись не используется для операции,
                требующей подтверждения. Отдельная canonical entity
                ReconfirmationRequest не создаётся.
Rationale:      Не раздувает state machine MemoryEntry; reconfirmation
                остаётся политикой использования, а не хранимым
                состоянием.
Scope:          Memory Domain; freshness/reconfirmation semantics.
                Explicit non-scope: TTL-значения, триггеры и механика
                reconfirmation-запроса, UX. Dependencies (не решаются
                этим решением): ADR-0012 OD-2 (red TTL).
Affected docs:  Memory Model v1.0 (Source of Truth, документ
                планируется); ADR-0012 — classification/policy layer
                (freshness semantics).
Status:         DECIDED
```

Источник: WINDOW-04 — Owner Decision Session (Memory Model
Canonicalization), 2026-08-08; решение OD-MEM-7, статус ACCEPTED.

**Регистрационная note (2026-08-08):**

> OD-MEM-1…7 зарегистрированы как AYLA-DEC-0067…0073 по итогам WINDOW-04 —
> Owner Decision Session (Memory Model Canonicalization); все семь rulings
> приняты Product Owner в рекомендованных вариантах. Следующие существующие
> open dependencies сохранены как dependencies, а не как новые решения:
> CSR-OD-5 (Consent Source of Truth); CSR-OD-4 / OD-1 (diet/skin legal
> boundary); ADR-0012 OD-2 (red TTL); Domain Event Registry OQ-E3 / OQ-E4
> (включая memory.entry_deleted tombstone / deletion contract); ADR-0012
> OQ-1 / OQ-2 (verification registry, provenance history format). Эта
> регистрация не изменяет ADR-0012, Domain Event Registry, CANON_INDEX и
> не создаёт Memory Model — подготовка Memory Model v1.0 выполняется
> отдельной командой Product Owner.

### AYLA-DEC-0074 — Semantic Memory Identity (OD-MEM-ID-1)

```text
ID:             AYLA-DEC-0074
Date:           2026-08-09
Question:       What establishes the semantic identity of a MemoryEntry?
Options:        A — textual similarity or record identity; B — semantic meaning and relevant context (selected).
Decision:       A MemoryEntry represents one semantic piece of knowledge within a relevant context. Two records may refer to the same semantic memory only when both the semantic meaning and the relevant context align. Textual similarity alone is insufficient to establish semantic identity. Record identity ≠ semantic identity; text equality ≠ semantic identity; similarity score ≠ semantic identity.
Rationale:      Preserves semantic meaning without conflating record, text, or similarity-based comparison with identity.
Scope:          Memory Domain; semantic identity boundary. Explicit non-scope: embedding thresholds, LLM comparison, canonical keys, specific context dimensions, and deduplication algorithms.
Affected docs:  Ayla Memory Model Specification; Ayla Core Domain Model Specification; Ayla Conversation Model Specification; Ayla MVP User Journey Specification; Ayla Intent Model Specification; Ayla MVP Recommendation Contract.
Status:         DECIDED
```

Source: WINDOW-04 — Memory Identity Owner Decision Session, 2026-08-09 (owner ruling).

### AYLA-DEC-0075 — Memory Granularity (OD-MEM-ID-2)

```text
ID:             AYLA-DEC-0075
Date:           2026-08-09
Question:       What determines the granularity of a MemoryEntry?
Options:        A — sentence, message, or source-event count; B — meaning and relevant context (selected).
Decision:       Memory granularity is determined by meaning and relevant context, not by the number of sentences, messages, or source events. One source message may produce one or multiple MemoryEntry records; multiple source expressions may also relate to one semantic memory when the applicable semantic/context rules say so.
Rationale:      Ensures memory boundaries reflect knowledge meaning rather than input formatting or transport boundaries.
Scope:          Memory Domain; granularity semantics. Explicit non-scope: automatic splitting algorithms, atomic field schemas, subject/predicate/value schemas, and LLM extraction rules.
Affected docs:  Ayla Memory Model Specification; Ayla Core Domain Model Specification; Ayla Conversation Model Specification; Ayla MVP User Journey Specification; Ayla Intent Model Specification; Ayla MVP Recommendation Contract.
Status:         DECIDED
```

Source: WINDOW-04 — Memory Identity Owner Decision Session, 2026-08-09 (owner ruling).

### AYLA-DEC-0076 — Multiple Provenance Sources (OD-MEM-ID-3)

```text
ID:             AYLA-DEC-0076
Date:           2026-08-09
Question:       Does different provenance require a separate MemoryEntry for the same semantic memory?
Options:        A — create a new entry for each provenance source; B — permit multiple independent sources for one semantic memory (selected).
Decision:       One semantic memory may have multiple independent provenance/evidence sources. Different provenance alone does not require creation of a new MemoryEntry. Each source's origin/history must remain traceable; provenance diversity must not be silently erased.
Rationale:      Retains auditable evidence without making source diversity itself a semantic-identity boundary.
Scope:          Memory Domain; provenance multiplicity and traceability semantics. Explicit non-scope: provenance[] fields, Evidence entities, evidence graphs, relation tables, and storage schema.
Affected docs:  Ayla Memory Model Specification; Ayla Core Domain Model Specification; Ayla Conversation Model Specification; Ayla MVP User Journey Specification; Ayla Intent Model Specification; Ayla MVP Recommendation Contract; Domain Event Registry / runtime docs as downstream references where relevant.
Status:         DECIDED
```

Source: WINDOW-04 — Memory Identity Owner Decision Session, 2026-08-09 (owner ruling).

### AYLA-DEC-0077 — Semantic Equivalence vs Duplicate (OD-MEM-ID-4)

```text
ID:             AYLA-DEC-0077
Date:           2026-08-09
Question:       Does semantic equivalence automatically make two MemoryEntry records duplicates?
Options:        A — semantic equivalence automatically authorizes duplicate treatment; B — semantic equivalence is distinct from duplicate semantics (selected).
Decision:       Semantic equivalence does not automatically mean that two MemoryEntry records are duplicates. Semantic similarity ≠ semantic equivalence; semantic equivalence ≠ duplicate; duplicate ≠ merge; merge ≠ deletion. No destructive consolidation may be authorized solely by semantic similarity or equivalence.
Rationale:      Prevents loss of traceability or knowledge through unjustified destructive consolidation.
Scope:          Memory Domain; duplicate and consolidation boundary. Explicit non-scope: duplicate detection algorithms, merge implementation, deletion policy, and similarity thresholds.
Affected docs:  Ayla Memory Model Specification; Ayla Core Domain Model Specification; Ayla Conversation Model Specification; Ayla MVP User Journey Specification; Ayla Intent Model Specification; Ayla MVP Recommendation Contract; Domain Event Registry / runtime docs as downstream references where relevant.
Status:         DECIDED
```

Source: WINDOW-04 — Memory Identity Owner Decision Session, 2026-08-09 (owner ruling).

### AYLA-DEC-0078 — Relevant Context in Semantic Identity (OD-MEM-ID-5)

```text
ID:             AYLA-DEC-0078
Date:           2026-08-09
Question:       Is relevant context part of the semantic identity of a MemoryEntry?
Options:        A — context is external to semantic identity; B — relevant context participates in semantic identity (selected).
Decision:       Relevant context is part of the semantic identity of a MemoryEntry. The decision establishes only that the same meaning in different relevant contexts may represent different semantic memories.
Rationale:      Avoids treating all occurrences of the same wording or meaning as one memory when their applicable context differs.
Scope:          Memory Domain; context participation in semantic identity. Explicit non-scope: the complete set of context dimensions; service, Transformation Goal, scenario, tenant, locale, channel, and time are not mandatory identity dimensions unless separately established by canon.
Affected docs:  Ayla Memory Model Specification; Ayla Core Domain Model Specification; Ayla Conversation Model Specification; Ayla MVP User Journey Specification; Ayla Intent Model Specification; Ayla MVP Recommendation Contract.
Status:         DECIDED
```

Source: WINDOW-04 — Memory Identity Owner Decision Session, 2026-08-09 (owner ruling).

### AYLA-DEC-0079 — Source Precedence Boundary (OD-MEM-ID-6)

```text
ID:             AYLA-DEC-0079
Date:           2026-08-09
Question:       Does the Memory Model define a universal/global precedence order between knowledge sources?
Options:        A — define a global source ranking; B — preserve source precedence as a future domain/policy concern (selected).
Decision:       Memory Model does not define a universal/global precedence order between knowledge sources. Memory Model owns provenance semantics, relationship semantics, and contradiction visibility. It does not globally define backend > user, user > backend, confirmed inference > other sources, or AI > user. Source precedence may depend on knowledge type, policy, purpose/use case, context, consent/safety rules, and future domain decisions.
Rationale:      Preserves the Memory Model boundary and prevents a context-dependent policy choice from becoming an ungoverned global algorithm.
Scope:          Memory Domain; source-precedence boundary. Explicit non-scope: source ranking algorithms and universal priority ordering.
Affected docs:  Ayla Memory Model Specification; Ayla Core Domain Model Specification; Ayla Conversation Model Specification; Ayla MVP User Journey Specification; Ayla Intent Model Specification; Ayla MVP Recommendation Contract; Domain Event Registry / runtime docs as downstream references where relevant.
Status:         DECIDED
```

Source: WINDOW-04 — Memory Identity Owner Decision Session, 2026-08-09 (owner ruling).

### AYLA-DEC-0081 — Memory Domain Package Canonization and Memory/Consent Rulings

```text
ID:             AYLA-DEC-0081
Date:           2026-08-20
Question:       Канонизировать ли Memory Domain package (Memory Domain Contract, Context Resolution Contract, Memory and Context Migration Plan) и подтвердить memory/consent rulings после reconciliation?
Options:        n/a — прямое решение Product Owner (ruling), не выбор из эскалированных вариантов
Decision:       Пакет канонизирован (status: approved / decision_status: accepted / canonical_status: approved, version 1.0). Consent Scope Registry v1.4 подтверждён действующим canonical CSR. Подтверждены OR-MEM-1…6; закрыты OD-MEM-1…4 и CSR-OD-5 (Consent Domain = canonical owner Consent Records, MVP physical custodian ai-bot-platform; memory_green legacy/deprecated; confidence только на MemoryProposal/audit; NutritionProfile — Nutrition Domain SoT с отдельным Privacy/Legal perimeter). Yellow/red activation НЕ разрешён.
Rationale:      Аудит памяти 2026-08-19 (перепроверен по коду) + reconciliation по AYLA-DEC-0023/0024 и Memory Model Spec v1.0 завершены без остаточных cross-document inconsistencies; открытых memory-architecture решений не остаётся.
Scope:          Memory Domain, Consent Domain boundary, Context Resolution. Явный non-scope: yellow/red activation; начало шагов 2+ Migration Plan этим решением не авторизуется; UX/Legal тексты preference_memory, age lookup #597, NutritionProfile perimeter — отдельные follow-up.
Affected docs:  Ayla Memory Domain Contract; Ayla Context Resolution Contract; Ayla Memory and Context Migration Plan; Consent Scope Registry; CANON_INDEX.
Status:         DECIDED
```

Source: CANONIZATION RULING — Memory Domain package, 2026-08-20 (owner ruling).

### AYLA-DEC-0082 — Action Is Not Outcome Evidence (В-5)

```text
ID:             AYLA-DEC-0082
Date:           2026-08-25
Question:       Является ли факт выполнения действия (плана) доказательством
                достижения результата (Desired Outcome)?
Options:        n/a — прямое решение Product Owner (ruling), зафиксировано
                как В-5 (2026-08-24, docs/OD_CARE_CONTRACT_RULINGS.md §2–3);
                канонизация одобрена 2026-08-25 («0082 одобряю»).
Decision:       Не является. Факт выполнения действия не является
                доказательством достижения результата. Outcome Progress
                вычисляется исключительно из наблюдений, относящихся к самому
                результату. Никакое количество выполненных действий не
                изменяет Outcome Progress. Plan Adherence и Outcome Progress —
                две независимые линии, не сводимые ни в одно число, ни в одну
                шкалу, ни в один визуальный индикатор. Норма — hard invariant.
Rationale:      docs/SPEC_CARE_CONTRACT.md §3.3 (нормативная формулировка) и
                О-6 (в каноне нормы не было); классы достоверности LDT §9;
                DRF-1295 («о данных можно, об организме нельзя»); LDT §13
                (Body Dignity). Проверка обратным примером: «вы хорошо
                продвигаетесь в снижении веса» после трёх массажей —
                запрещённая формулировка по пункту 1 нормы (docs/
                DRAFT_AYLA-DEC-0082_ACTION_NOT_OUTCOME_EVIDENCE.md §4).
Scope:          Personal Plan / Progress Observations / Recommendation (NBA);
                все downstream UX- и AI-документы.
Affected docs:  Living Digital Twin Manifesto §9 (v1.2 — пятое запрещённое
                смешение классов + нормативный абзац); эпик DRF-1331.
Status:         DECIDED
```

Source: В-5 (owner ruling, 2026-08-24) + owner approval 2026-08-25; драфт канонизации — окно goals, `docs/DRAFT_AYLA-DEC-0082_ACTION_NOT_OUTCOME_EVIDENCE.md`.
