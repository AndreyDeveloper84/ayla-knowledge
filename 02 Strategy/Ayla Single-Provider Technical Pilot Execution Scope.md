---
node_id: ayla.strategy.single-provider-pilot-execution-scope
title: Ayla Single-Provider Technical Pilot Execution Scope
type: specification
status: draft
decision_status: proposed
canonical_status: draft
version: "0.3"
owner: Product Owner
knowledge_area:
  - strategy
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
created: 2026-07-31
updated: 2026-07-31
review_cycle: monthly
depends_on:
  - "[[Ayla MVP Scope and Release Contract]]"
  - "[[Ayla MVP Product Thesis]]"
  - "[[Consent Scope Registry]]"
related:
  - "[[AMD-020 Pilot Scope Registry]]"
  - "[[OWNER_DECISION_REGISTER]]"
---

# Ayla Single-Provider Technical Pilot Execution Scope v0.3

**Статус:** DRAFT / proposed / non-canonical execution scope
**Версия:** 0.3
**Владелец:** Product Owner
**Upstream:** [[Ayla MVP Scope and Release Contract]] v0.3
(draft / proposed / candidate)
**Источник ревизии:** Ayla Single-Provider Technical MVP Scope v0.2
(внешний docx, structured revision)

> **Роль документа (факт):** это **execution scope** — staged
> technical/operational execution для одного контролируемого провайдера.
> Документ не является canonical Foundation artifact, не владеет MVP
> release boundary и не создаёт конкурирующий MVP scope anchor. Схема
> репозитория не поддерживает значение `canonical_status: non-canonical`;
> использовано валидное значение `draft`, а execution-level /
> non-foundation роль зафиксирована здесь и в §1–§2.

## 1. Purpose and Document Role

Этот документ отвечает на вопрос **«как поэтапно выполняется
технический пилот на одном контролируемом провайдере»**: какие фазы,
какие capabilities активируются в каждой фазе, какие gates отделяют
фазы и какие доказательства собираются.

This document:

- is an execution scope;
- stages the controlled single-provider technical pilot;
- is downstream of [[Ayla MVP Scope and Release Contract]] v0.3;
- does not redefine MVP product scope;
- does not prove [[Ayla MVP Product Thesis]];
- does not establish PMF, independent retention, transferability or
  monetization;
- does not activate multi-provider product capabilities.

Название **Technical MVP Scope** не используется: оно создаёт
конкурирующий MVP scope anchor. Единственный владелец MVP release
boundary — MVP Scope v0.3.

## 2. Relationship to Canonical MVP Scope

```text
Ayla MVP Scope and Release Contract v0.3 — release boundary (что входит в релиз)
└── Ayla Single-Provider Technical Pilot Execution Scope v0.3 (этот документ)
      — staged execution на одном провайдере (как и в каком порядке)
```

- Этот документ **reference, а не дублирует** канонические продуктовые
  нормы: release scope, product boundary, LDT boundary, channel set,
  wellness statuses и monetary boundary определены в MVP Scope v0.3 и
  здесь не пересматриваются.
- Все ссылки на «Ayla MVP Scope v0.1» / «Ayla MVP Scope v0.2» из v0.2
  заменены на [[Ayla MVP Scope and Release Contract]] v0.3.
- Фазовая модель A0/A1/A2 принадлежит execution-уровню: MVP Scope v0.3
  фаз не содержит и не содержит обязанности их содержать.
- Конфликт между этим документом и MVP Scope v0.3 разрешается в пользу
  MVP Scope v0.3; конфликт с [[Ayla Product Essence]] — в пользу Essence.

Применённые owner decisions (OWNER_DECISION_REGISTER, DECIDED
2026-07-31): **AYLA-DEC-0027** (required three-channel set),
**AYLA-DEC-0028** (Food Scanner — один из равнозначных триггеров),
**AYLA-DEC-0029** (28-day cycle — A2 exit evidence), **AYLA-DEC-0033**
(статус числовых порогов). AYLA-DEC-0030/0031/0032/0034 относятся к
Multi-Provider Execution Scope и здесь не вводят новых норм, но
учитываются в exit-критериях перехода к B0.

## 3. Pilot Context and Provider Boundary

- **Провайдер:** один контролируемый салон — «Формула тела» (Пенза).
  Только один провайдер на всём протяжении A0–A2; второй провайдер —
  OUT на всём документе.
- **Сегмент:** женщины 28–45 лет; география — Пенза; задача —
  улучшение формы и субъективного состояния тела, питания и
  восстановления.
- **Transformation Goal:** одна активная цель на пользователя.
- **Каналы:** Mobile App + MAX Mini App + MAX Bot (§6). Telegram — вне
  scope (AYLA-DEC-0004).
- **Пользователи:** A0 — internal/close circle; A1 — лояльные клиенты
  «Формулы тела»; A2 — клиенты того же провайдера. Cold acquisition —
  OUT (по AYLA-DEC-0031 это прерогатива B1 и здесь не планируется).
- **Монетизация:** не валидируется в этом пилоте (порядок monetization
  validation — AYLA-DEC-0032 — относится к Multi-Provider Beta).

## 4. What This Pilot Validates

Пилот подтверждает техническую и операционную работоспособность полного
пользовательского цикла на одном контролируемом провайдере:

1. пользователь проходит основной путь без участия разработчика;
2. данные, фотографии, планы, рекомендации, записи и события аналитики
   сохраняются без потерь;
3. Twin baseline, recognition и correction работают на реальных
   пользователях;
4. Safety Gate блокирует недопустимые автоматические рекомендации и
   переводит спорные случаи на ручную проверку;
5. direct attribution `recommendation_id` → действие
   (`booking_id` → `appointment_id` при наличии booking) сохраняется и
   аудируема;
6. оператор салона обрабатывает типовые исключения без изменения кода;
7. ручные вмешательства видимы, классифицированы и измеримы;
8. weekly review формируется на подтверждённых данных и отделяет факты
   от AI-интерпретаций;
9. пользователь может отозвать согласия и удалить данные;
10. три required канала работают поверх единого backend с сохранением
    identity, consent и state.

## 5. What This Pilot Does Not Validate

- Product-market fit Ayla;
- удержание холодной аудитории, не связанной с «Формулой тела»;
- доверие пользователя к незнакомому мастеру или салону;
- переносимость решения на разные каталоги, правила и booking-системы;
- нейтральность выбора между несколькими провайдерами;
- готовность независимых мастеров и салонов платить (monetization
  validation — Multi-Provider Beta, AYLA-DEC-0032);
- экономику масштабирования и низкую стоимость сопровождения;
- эффективность marketplace, ranking и paid placement;
- memory-dependent claims (Phase 1 — session-only, §13);
- причинную атрибуцию вклада Twin (formal controlled experiment —
  DEFERRED, AYLA-DEC-0034).

Все retention- и conversion-показатели этого пилота — предварительные
продуктовые сигналы: среда контролируется владельцем продукта
(см. §18 — статусы метрик).

## 6. Three-Channel Delivery Model

Применяется **AYLA-DEC-0027** (Required MVP Channel Set):

```text
Mobile App:      REQUIRED / PRIMARY PRODUCT EXPERIENCE
MAX Mini App:    REQUIRED / LIGHTWEIGHT EMBEDDED COMPANION
MAX Bot:         REQUIRED / CONVERSATIONAL, NOTIFICATION AND ROUTING COMPANION
Feature parity:  NOT_REQUIRED
Shared backend/domain/state/consent/safety/recommendation/memory/
attribution/analytics: REQUIRED
```

Три канала — один продукт, а не три отдельных продукта: едины identity,
consent, safety, recommendation state, memory boundary, attribution и
analytics. Business logic не дублируется в канальных клиентах.

### 6.1 Channel ownership matrix

| Capability | Mobile App | MAX Mini App | MAX Bot |
|---|---|---|---|
| Registration/account linking | FULL | CONTINUE | START/ROUTE |
| Consent | FULL OWNER | BASIC/VIEW | EXPLAIN/ROUTE |
| Transformation Goal | FULL | BASIC | CONVERSATIONAL |
| Baseline | FULL | BASIC | CONVERSATIONAL INPUT |
| LDT/photo | FULL OWNER | PREVIEW | ROUTE |
| Recognition/correction | FULL | BASIC | ROUTE |
| Recommendation/explanation | FULL | FULL | CONVERSATIONAL |
| Daily check-in | FULL | QUICK | QUICK |
| Weekly plan/review | FULL | SUMMARY | REMIND/ROUTE |
| Booking | FULL | FULL | START/ROUTE |
| Progress/history | FULL OWNER | SUMMARY | NOTIFY |
| Notifications | PUSH | STATUS | CHAT |
| Data control | FULL OWNER | BASIC/ROUTE | COMMAND/ROUTE |

Полная feature parity не требуется: capability обязана быть доступна в
назначенном owning channel; отсутствие второстепенной функции в Mini
App или Bot не блокирует фазу.

### 6.2 Phase channel rollout

```text
A0: Mobile internal build; MAX Mini App test environment; MAX test bot
A1: Mobile closed/internal distribution; Mini App и Bot доступны alpha cohort
A2: все три required канала доступны реальной пилотной когорте
```

Store publication approval **не является blocker A0**. Для A2 требуется
реальная доступность Mobile App пилотной группе — допускается closed
distribution, если это операционно допустимо (маршрут распространения —
open question, §24).

## 7. Phase Model Overview

```text
Phase A0 — Internal Technical Spine       ≈ previous Wave 1 (internal smoke test)
Phase A1 — Controlled Salon Alpha         ≈ previous Wave 2 (salon alpha)
Phase A2 — Full Single-Provider Pilot     ≈ previous Wave 3 (closed technical pilot)
```

Mapping на прежние Wave 1–3 сохранён только как migration note;
нормативно используются только A0/A1/A2.

| Фаза | Участники | Длительность | Цель |
|---|---|---|---|
| A0 | 5–7 internal/close-circle | 5–7 дней | Технический spine; блокирующие дефекты; целостность данных |
| A1 | 15–20 лояльных клиентов «Формулы тела» + оператор салона | 14 дней | Реальный путь и операционная нагрузка |
| A2 | 30–50 клиентов одного провайдера | 28 дней | Стабильность полного 28-дневного цикла |

28-дневный цикл — **A2 exit evidence** (AYLA-DEC-0029): не требуется до
A0/A1; до B0 entry достаточная и явно определённая A2-когорта завершает
28-дневный путь. Точный denominator и достаточная доля определяются
Measurement Framework до A2 launch и здесь не устанавливаются.

## 8. Phase A0 — Internal Technical Spine

**Purpose:** проверить технический spine без доказательства продуктовой
ценности.

**Participants:** 5–7 internal/close-circle participants.
**Duration:** 5–7 дней.

### MUST

- registration and account linking (cross-channel);
- consent flow (раздельные согласия по Consent Scope Registry);
- Transformation Goal;
- minimal baseline (baseline-опрос: энергия, состояние, питание, вода,
  сон, активность как самоотчёт — не dedicated трекеры);
- LDT baseline (управляемая фотофиксация);
- recognition/correction;
- intent conversation;
- explainable recommendation;
- next action, включая валидный исход «ничего не делать»;
- safety gate;
- session-only memory (Phase 1, §13);
- user control (просмотр/исправление/удаление/отзыв);
- audit;
- core analytics;
- cross-channel state continuity.

### SHOULD

- simple weekly plan;
- daily check-in;
- minimal operator console (§16).

### DEFERRED

- booking end-to-end;
- post-procedure check-in;
- food-trigger;
- notifications;
- full weekly review;
- persistent memory.

### OUT

- second provider;
- ranking;
- marketplace;
- monetization validation;
- cold traffic;
- Telegram.

### Exit

- journey проходит без вмешательства разработчика;
- user data loss = 0;
- critical safety incidents = 0;
- consent bypass = 0;
- ключевые события наблюдаемы;
- блокирующие дефекты закрыты;
- account state сохраняется между каналами.

## 9. Phase A1 — Controlled Salon Alpha

**Purpose:** проверить реальный путь на лояльных клиентах
контролируемого салона и операционную нагрузку.

**Participants:** 15–20 лояльных клиентов «Формулы тела» +
администратор/оператор салона.
**Duration:** 14 дней.

**Entry precondition:** LDT media pipeline feasibility checkpoint
пройден (фотофиксация, хранение, recognition/correction работают на
internal cohort A0); в противном случае A1 не стартует с LDT-зависимыми
сценариями.

### MUST

- все A0 MUST;
- booking end-to-end через booking adapter (technical test coverage —
  см. §14);
- direct attribution recommendation → action → booking (при наличии
  booking);
- operator exception handling без разработчика;
- manual intervention log;
- обработка consent/deletion requests;
- переходы Mobile/Mini App/Bot без потери состояния.

### SHOULD

- food trigger как один из равнозначных trigger-сценариев (§12);
- transactional notifications;
- daily check-in;
- partial post-procedure feedback.

### DEFERRED

- full weekly review;
- full 28-day evidence;
- Phase 2 persistent memory;
- second provider;
- ranking;
- cold acquisition.

### Exit

- реальные пользователи завершают путь;
- все recommendation-originated bookings сохраняют attribution;
- ручное сопровождение измерено;
- critical safety incidents = 0;
- LDT recognition/correction работает на реальных пользователях;
- все три канала используемы когортой;
- cross-channel identity и consent остаются консистентными.

## 10. Phase A2 — Full Single-Provider Pilot

**Purpose:** проверить стабильность полного 28-дневного
single-provider cycle.

**Participants:** 30–50 клиентов, один контролируемый провайдер.
**Duration:** 28 дней.

### MUST

- complete journey (MVP Scope §4);
- weekly review;
- post-procedure feedback;
- state comparison (сравнение состояний во времени);
- progress / next state как терминал journey;
- release evidence по MVP Scope §11;
- все три required канала доступны;
- channel source captured;
- direct attribution auditable;
- manual operations measured.

### SHOULD

- repeat photo capture;
- second non-food trigger;
- снижение доли ручных вмешательств.

### DEFERRED

- persistent memory — только если Phase 2 gate (Consent Scope Registry
  §10.2) пройден отдельно;
- multi-provider;
- advanced attribution;
- monetization validation.

### A2 exit before B0

По **AYLA-DEC-0029**: 28-day cycle обязателен как A2 exit evidence; он
не требуется до A0/A1. Достаточная, явно определённая доля A2-когорты
должна завершить journey; точный denominator/threshold принадлежит
Measurement Framework и здесь не устанавливается.

Дополнительно требуется:

- technical/safety acceptance (§18 hard gates);
- provider не зашит в код (добавляется конфигурацией);
- ServiceOffering / booking adapter readiness к подключению второго
  провайдера;
- аналитика различает tenant / provider / cohort / manual intervention;
- documented runbook;
- назначен onboarding owner нового провайдера;
- data loss = 0; critical safety incidents = 0.

## 11. Capability Activation Matrix

| Capability | A0 | A1 | A2 |
|---|---|---|---|
| Registration / account linking | MUST | MUST | MUST |
| Consent flow / user control | MUST | MUST | MUST |
| Transformation Goal | MUST | MUST | MUST |
| Baseline (опрос) | MUST | MUST | MUST |
| LDT baseline / recognition / correction | MUST | MUST | MUST |
| Intent conversation | MUST | MUST | MUST |
| Explainable recommendation | MUST | MUST | MUST |
| Next action («ничего не делать» валидно) | MUST | MUST | MUST |
| Safety gate | MUST | MUST | MUST |
| Session-only memory | MUST | MUST | MUST |
| Audit / core analytics | MUST | MUST | MUST |
| Cross-channel state continuity | MUST | MUST | MUST |
| Weekly plan (simple) | SHOULD | MUST | MUST |
| Daily check-in | SHOULD | SHOULD | MUST |
| Minimal operations surface | SHOULD | MUST | MUST |
| Booking end-to-end (adapter + attribution test coverage) | DEFERRED | MUST | MUST |
| Post-procedure feedback | DEFERRED | SHOULD (partial) | MUST |
| Food trigger (один из равнозначных) | DEFERRED | SHOULD | SHOULD |
| Second non-food trigger | DEFERRED | DEFERRED | SHOULD |
| Transactional notifications | DEFERRED | SHOULD | MUST (минимум) |
| Weekly review (full) | DEFERRED | DEFERRED | MUST |
| Repeat photo capture | DEFERRED | DEFERRED | SHOULD |
| Persistent memory (Phase 2) | DEFERRED | DEFERRED | DEFERRED (gate §13) |
| Ranking / marketplace / second provider | OUT | OUT | OUT |
| Monetization validation / cold traffic / Telegram | OUT | OUT | OUT |

## 12. Food Scanner Correction

Применяется **AYLA-DEC-0028**. Все формулировки v0.2, где Food Scanner
выступал центральным daily loop, обязательной активацией, обязательной
P0-точкой входа, центральной retention-метрикой или первичным сигналом
повторного использования, удалены.

```text
Food Scanner:
CONDITIONAL
один из четырёх равнозначных trigger-сценариев
не обязателен для каждого участника
не центр продукта
```

Продуктовые свойства Food Scanner сохраняются (не удаляются): фото или
загрузка изображения еды; распознавание блюда и основных компонентов;
уровень уверенности и явное указание неопределённости; подтверждение
или исправление пользователем; одна короткая персональная рекомендация,
связанная с целью; история подтверждённых Food Scan; запрет диагнозов,
определения дефицитов и выдачи приблизительных калорий за точные.

Метрики: **trigger-agnostic — primary**; **food-specific — DIAGNOSTIC**
(§18).

## 13. Memory and Consent Phases

```text
Phase 1: session-only memory; persistent memory технически отключена
         (Consent Scope Registry §10.1)
Phase 2: opt-in persistent memory; только после Consent Scope Registry
         §10.2 gate
```

- Persistent memory **не является blocker** для A0/A1/A2;
- persistent memory не требуется для объявления Phase 1 release
  readiness;
- memory-dependent claims не могут быть провалидированы в Phase 1 и не
  входят в exit evidence любой фазы этого пилота;
- до прохождения gate §10.2 действует режим: session context only, no
  proactive recommendations, no cross-domain personalization, no
  persistent inferred signals, no persistent preference storage.

## 14. Booking and Attribution Boundary

Booking — **OPTIONAL downstream product action** (MVP Scope §4, шаг 8).

```text
Technical test coverage requirement (A1/A2): MUST
User outcome: OPTIONAL
```

- В A1/A2 booking flow через adapter обязателен как техническое
  покрытие: adapter, создание записи, подтверждение, перенос/отмена
  через существующий flow провайдера, сохранение attribution.
- Это **не означает**, что каждый пользовательский journey обязан
  завершаться записью: отказ от действия и домашняя альтернатива —
  допустимые исходы.
- Терминал journey — **progress / next state**, а не подтверждение
  записи.
- Attribution: минимальный direct linkage `recommendation_id` →
  выбранное действие; `booking_id` / `appointment_id` привязываются
  только если booking произошёл (MVP Scope §6.3). Assisted / multi-touch
  / cohort attribution — DEFERRED.
- Внешняя booking-система подключается через adapter; Yclients может
  упоминаться только как текущая реализация/пример провайдерской
  системы и не является канонической зависимостью (§20).

## 15. Manual Operations Policy

Разрешённые ручные операции:

- корректировка каталога и availability;
- safety review;
- taxonomy review;
- onboarding assistance;
- fallback booking;
- обработка consent/deletion requests.

Каждое вмешательство логируется:

```text
type / reason / operator / duration / result / affected cohort
```

Запрещено:

- скрытые ручные изменения рекомендаций;
- обход safety gate;
- создание оператором пользовательских фактов;
- нелогированные изменения ranking;
- сокрытие ручной работы из аналитики.

Функциональность, регулярно выполняемая вручную, не считается
автоматизированной.

## 16. Minimal Operations Surface

Разрешение конфликта с MVP Scope `admin tooling — OUT_OF_SCOPE`:

разрешён **minimal pilot operations surface** — enabling operations, а
не user-facing admin product capability:

- список участников и статус onboarding;
- consent/deletion requests;
- safety queue;
- manual intervention log;
- booking sync errors;
- минимальная incident visibility.

Детальные процедуры выносятся в Operations Runbook (execution
artifact), а не в этот документ. Полноценная CRM, loyalty, admin
tooling — OUT.

## 17. Analytics and Release Evidence Mapping

Release evidence MVP Scope §11 маппится на события пилота (имена
событий — из v0.2 §10.3, где они уже определены; новые имена не
выдумываются, финальные имена — open question §24):

| Release evidence (MVP Scope §11) | События пилота |
|---|---|
| goal established | `goal_created` |
| Twin baseline created | `baseline_completed`, `twin_viewed` |
| recognition/correction captured | recognition/correction events (имя TO_BE_DEFINED) |
| recommendation explained | `procedure_recommended`, `explanation_opened` |
| next action accepted/rejected | `accepted`, `rejected`, `plan_action_completed` |
| booking (secondary evidence) | `booking_started`, `booking_created`, `appointment_completed` |
| continuity retained where consented | session continuity events (имя TO_BE_DEFINED) |
| user control exercised | consent/deletion events (Consent Scope Registry §9) |
| safety blocks / tool failures | `safety_escalated`, tool failure events |
| account linking | `signup_completed`, account linking event (имя TO_BE_DEFINED) |
| cross-channel state preserved | cross-channel continuity events (имя TO_BE_DEFINED) |
| channel source captured | channel attribution field в событиях (TO_BE_DEFINED) |
| deep-link/route outcome | deep-link outcome event (TO_BE_DEFINED) |
| mobile-owned LDT/photo/progress path | mobile channel events (TO_BE_DEFINED) |
| MAX companion path | Mini App / Bot path events (TO_BE_DEFINED) |

Сохранённые из v0.2 операционные события: `manual_intervention_created`,
`safety_escalated`, `provider_data_corrected`, `booking_sync_failed`;
retention-контур: `weekly_review_opened`, `weekly_review_completed`,
`plan_adjusted`, `goal_continued`, `goal_abandoned`; daily-контур:
`food_capture_started`, `food_recognition_completed`,
`food_result_confirmed`, `food_result_corrected`,
`daily_checkin_completed`, `plan_action_completed` (food-события —
DIAGNOSTIC, §12/§18).

## 18. Metrics and Threshold Status

Применяется **AYLA-DEC-0033**.

### REQUIRED HARD GATES

- user data loss = 0;
- critical safety incidents = 0;
- consent bypass = 0;
- economic influence on ranking = 0 (где применимо);
- direct attribution chain technically available and auditable.

### WORKING VALIDATION THRESHOLDS

Все процентные цели из v0.2 — рабочие пороги валидации, **не
канонические нормы**:

- ≥95% ключевых сценариев без системной ошибки;
- ≥98% ожидаемых аналитических переходов зафиксированы;
- retention / weekly review completion;
- recommendation-to-booking / booking-to-appointment;
- attribution completeness percentage.

### DIAGNOSTIC

- activation (Core / Behavioral);
- D7/D28 в контролируемой когорте;
- Food Scanner usage (§12);
- manual intervention (объём и тренд);
- response times;
- tool failures;
- recognition correction rate.

Финальные B1 go/no-go пороги здесь **не утверждаются**: FINAL GO/NO-GO
утверждается до B1 после B0 evidence и Measurement Framework.

## 19. Entry and Exit Gates

| Gate | Условия |
|---|---|
| A0 entry | internal build трёх каналов; consent flow реализован; safety gate активен; session-only режим подтверждён |
| A0 exit → A1 entry | §8 Exit полностью; LDT media pipeline feasibility checkpoint (§9) |
| A1 exit → A2 entry | §9 Exit полностью; runbook draft; оператор обучен; mobile closed distribution доступна когорте |
| A2 exit → B0 entry | §10 A2 exit полностью, включая AYLA-DEC-0029 (достаточная A2-когорта завершила 28-дневный путь); hard gates §18 = 0 нарушений; architecture readiness §20; runbook documented; onboarding owner назначен |

Нарушение любого REQUIRED HARD GATE в любой фазе — stop condition (§23),
а не усредняемая метрика.

## 20. Architecture Readiness Boundary

Сохраняются только execution-level readiness statements:

- provider/tenant не зашиваются константами в бизнес-логику;
- один внутренний booking contract; внешняя система — через adapter;
- разделение CanonicalService и ServiceOffering;
- `tenant_id` и `provider_id` в релевантных записях и событиях;
- доступ к данным проектируется с будущей tenant-изоляцией;
- channel clients не владеют business logic; shared API contract для
  всех трёх каналов;
- AI-процессы разделены (recognition, feedback, plan, recommendation,
  safety gate, weekly review, twin rendering); один монолитный prompt
  не допускается.

Детальные entity/model/API definitions принадлежат
Architecture-документам и здесь не дублируются. Yclients не является
канонической зависимостью — только текущая реализация/пример
провайдерской booking-системы.

A0/A1 не блокируются полной B0-архитектурой: для A0 требуются только
«provider не hardcoded» и направление shared contract.

Техническая multi-tenant readiness **не означает** активацию CAP-020
(multi-tenant customization — OUT_OF_SCOPE в MVP Scope §7).

## 21. Safety, Privacy and Data Control

- Детерминированные safety gates применяются ко всем product
  capabilities (MVP Scope §6.5); обход запрещён, в том числе вручную
  (§15).
- Consent: раздельные согласия (персональные данные, фотографии,
  персонализация, сервисные уведомления; маркетинговое — отдельное и
  необязательное); просмотр статуса, отзыв, удаление аккаунта и данных —
  доступны пользователю и обрабатываются оператором (§15/§16).
- Purpose limitation: данные используются только для информированных
  целей; authoritative consent state — из Consent Domain
  ([[AMD-020 Pilot Scope Registry]]), независимый source of truth
  запрещён.
- Privacy default — Consent Scope Registry §10: session context only до
  Phase 2 gate (§13).
- Body dignity / anti-shaming обязательны во всех LDT-взаимодействиях
  ([[Ayla Living Digital Twin Manifesto]] §13).
- Медицинская диагностика, выводы о здоровье и inferred mental state
  запрещены ([[Ayla Constitution]] Ст. X, XII).
- Пользовательские данные и фотографии удаляются по запросу, включая
  производные данные Twin.

## 22. Disallowed Interpretations

```text
Успех A0 не доказывает продуктовую готовность.
Успех A1 не доказывает продуктовую ценность.
Успех A2 не доказывает PMF.
Retention в single-provider пилоте — не независимый рыночный retention.
Данные одного провайдера не доказывают переносимость.
Booking conversion — не North Star продукта.
Использование Food Scanner — не доказательство полной ценности Ayla.
Phase 1 не валидирует memory-dependent claims.
Техническая multi-tenant readiness — не активация CAP-020.
Три канала — не три отдельных продукта.
```

## 23. Risks and Stop Conditions

Немедленная остановка фазы (stop condition):

- любая потеря пользовательских данных;
- любой critical safety incident;
- любой consent bypass;
- потеря attribution chain для recommendation-originated booking без
  возможности восстановления;
- рассинхронизация identity/consent между каналами.

Риски, требующие эскалации к Product Owner (без автоматической
остановки):

- ручное сопровождение не снижается от фазы к фазе;
- recognition correction rate указывает на системную проблему качества
  Twin;
- оператор не справляется с типовыми исключениями без разработчика;
- closed mobile distribution недоступна к A2;
- доля завершения 28-дневного пути явно недостаточна для B0 decision
  (denominator — Measurement Framework).

## 24. Open Questions

Только реальные non-blocking вопросы; решённые OD-TP вопросы не
переоткрываются:

- exact A2 completion denominator (Measurement Framework, до A2 launch);
- exact closed mobile distribution route;
- exact LDT recognition threshold (downstream AI/Measurement);
- exact manual intervention target;
- exact event names для новых channel/cross-channel событий (§17);
- exact operations staffing.

Вопросы для review из v0.2 (достаточность цикла для alpha, разделение
Core/Behavioral Activation, safety/consent gates, перенос/отмена записи
vs deep link, допустимые ручные операции, exit criteria, архитектурные
зависимости) закрыты этой ревизией или переведены в перечень выше.

## 25. Change Log

> Журнал отражает историю изменений и не является нормативной частью.
> Нормативно — текущее состояние разделов 1–24.

### v0.3 (2026-07-31) — Structured revision after Two-Phase Pilot Scope Reconciliation

Выполнено в Two-Phase Pilot Scope Reconciliation Window по промпту
`SINGLE_PROVIDER_TECHNICAL_PILOT_EXECUTION_SCOPE_V0_3_REVISION_PROMPT.md`
после MVP Scope v0.3 Mobile Channel Internal Consistency Review
(verdict: APPROVED_FOR_EXECUTION_SCOPE_REVISION). Источник: внешний
docx «Ayla Single-Provider Technical MVP Scope v0.2».

- **Переименован** из «Technical MVP Scope» в «Technical Pilot Execution
  Scope»: устранён конкурирующий MVP scope anchor; execution role
  зафиксирован (§1–§2); документ не является canonical Foundation
  artifact.
- **Материализован в репозитории** как Markdown
  (`02 Strategy/Ayla Single-Provider Technical Pilot Execution Scope.md`);
  исходный docx остаётся внешним pre-canon artifact.
- **Фазовая модель A0/A1/A2** введена вместо Wave 1–3 (mapping
  сохранён как migration note, §7).
- **Трёхканальная модель добавлена** (AYLA-DEC-0027): Mobile App —
  REQUIRED/PRIMARY; MAX Mini App и MAX Bot — REQUIRED companion;
  feature parity — NOT_REQUIRED; channel ownership matrix и phase
  channel rollout зафиксированы (§6).
- **Food Scanner de-centered** (AYLA-DEC-0028): CONDITIONAL, один из
  четырёх равнозначных триггеров; trigger-agnostic primary метрики,
  food-specific — DIAGNOSTIC (§12).
- **Booking исправлен** до optional downstream outcome: technical test
  coverage — MUST в A1/A2, user outcome — OPTIONAL; терминал journey —
  progress / next state (§14).
- **Memory phases добавлены**: Phase 1 session-only / Phase 2 opt-in
  после Consent Scope Registry §10.2 gate; persistent memory — не
  blocker фаз (§13).
- **LDT boundary выровнен** по MVP Scope §6.4: target image —
  CONDITIONAL desired outcome; video — CONDITIONAL; morphing engine,
  medical simulation, гарантированный прогноз — OUT (см. §8–§10,
  §21; boundary наследуется из MVP Scope v0.3 и не дублируется).
- **Metrics status добавлен** (AYLA-DEC-0033): REQUIRED HARD GATES /
  WORKING VALIDATION THRESHOLDS / DIAGNOSTIC (§18).
- **28-day cycle** зафиксирован как A2 exit evidence (AYLA-DEC-0029);
  denominator — Measurement Framework (§7, §10).
- **Architecture/operations boundaries уточнены**: execution-level
  readiness только; Yclients — не canonical, только пример; minimal
  operations surface отличён от admin tooling (§16, §20).
- **Disallowed interpretations** зафиксированы явно (§22).
- **Stale references удалены**: «Ayla MVP Scope v0.1» →
  [[Ayla MVP Scope and Release Contract]] v0.3 (wikilink).
- **Baseline вода/сон/активность** — baseline-опрос (самоотчёт), не
  dedicated трекеры (§8).
- Применённые owner decisions: AYLA-DEC-0027, AYLA-DEC-0028,
  AYLA-DEC-0029, AYLA-DEC-0033 (непосредственно); AYLA-DEC-0030/0031/
  0032/0034 — учтены в границах перехода к B0/B1 без введения
  multi-provider норм.

### Migration note — v0.2 (pre-canon, внешний docx)

Сохраняется как история, не как активные нормы:

- волновая модель Wave 1 (internal smoke, 5–7 участников, 5–7 дней),
  Wave 2 (salon alpha, 15–20 лояльных клиентов, 14 дней), Wave 3
  (closed technical pilot, 30–50 клиентов, 28 дней) — заменена на
  A0/A1/A2;
- P0 Product Scope v0.2 (регистрация/consent, Transformation Goal,
  Baseline, LDT Lite, «Сегодня», Food Scanner, Weekly Plan/Daily
  Check-in, Safety Gate, Booking/attribution, Post-procedure, Weekly
  Review, уведомления) — перераспределён по фазам в §8–§11;
- acceptance criteria v0.2 (95% сценариев, 98% событий, data loss 0,
  safety 0, attribution) — переведены в статусы §18;
- exit gate в Multi-Provider Beta v0.2 — сохранён и усилен как A2 exit
  before B0 (§10, §19);
- Out of Scope v0.2 (marketplace, ranking, отзывы, платное продвижение,
  CRM/loyalty/payments, wearables, медицина, 3D-реконструкция,
  гарантированный прогноз, автономные назначения, массовый запуск) —
  сохранён в §8 OUT, §5 и MVP Scope §7;
- вопросы для review v0.2 — закрыты или переведены в §24.
