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
updated: 2026-08-02
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
