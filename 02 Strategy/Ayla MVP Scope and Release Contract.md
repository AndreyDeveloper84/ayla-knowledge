---
node_id: ayla.strategy.mvp-scope-release-contract
title: Ayla MVP Scope and Release Contract
type: specification
status: draft
decision_status: proposed
version: "0.3"
owner: Product Owner
priority: P0
knowledge_area:
  - strategy
  - product
domain:
  - cross-domain
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
created: 2026-07-27
updated: 2026-07-28
review_cycle: monthly
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Product Vision]]"
  - "[[Ayla MVP Product Thesis]]"
  - "[[Killer PRD]]"
  - "[[Ayla Decision Log]]"
  - "[[Ayla MVP Documentation Roadmap]]"
related:
  - "[[Ayla Domain Capability Registry]]"
  - "[[Consent Scope Registry]]"
  - "[[AMD-020 Pilot Scope Registry]]"
  - "[[Ayla User Journey Specification]]"
---

# Ayla MVP Scope and Release Contract

Этот документ — главный документ против разрастания scope MVP. Он порождён
записью AYLA-DEC-0014 ([[Ayla Decision Log]]) и разделом 1.4
[[Ayla MVP Documentation Roadmap]]; нормативную силу получает только после
approval (§12). До approval все положения имеют статус `proposed`.

Документ фиксирует **release scope** — какие capabilities обязаны работать в
первом релизе, а какие явно отложены. Он не дублирует механику killer-сценария
([[Killer PRD]]), пользовательский путь ([[Ayla User Journey Specification]]) и
гипотезу MVP ([[Ayla MVP Product Thesis]]), а ссылается на них.

## 1. MVP Goal

Цель MVP — проверить на пилоте центральный тезис (AYLA-DEC-0002,
[[Ayla MVP Product Thesis]] §4): накопленное и объяснимое понимание
пользователя, а не сама функция записи, создаёт конкурентное преимущество.

Проверка тезиса выполняется через один сквозной сценарий (§3) и одну главную
метрику (§9): переход «осмысленный запрос → полезная рекомендация →
подтверждённое действие» ([[Ayla MVP Documentation Roadmap]] §9.2). Метрики
количества сообщений целью MVP не являются.

Условия, при которых MVP считается проверенным, определены в
[[Ayla MVP Product Thesis]] §8.1/§8.2 (Success/Failure Criteria) и §8.4 (MVP
Phase Exit Criteria) и здесь не переопределяются.

**Граница с AMD-020 (факт, AYLA-DEC-0014):** [[AMD-020 Pilot Scope Registry]]
владеет pilot/memory ownership (какие данные и память допустимы в пилоте);
настоящий документ владеет release scope capabilities (какие способности
продукта входят в релиз). Пересечения разрешаются в пользу более строгого
ограничения; изменение границы — через Change Control (§11).

## 2. Target Users

Факт — [[Ayla MVP Product Thesis]] §5:

- **Provider side:** соло-мастер (независимый специалист без наёмного
  персонала) и малый салон (до 3 мастеров в штате) — симметрично тарифной
  модели AYLA-DEC-0001. Провайдеры вне этих профилей (крупные сети, франшизы)
  — вне scope.
- **Client side:** пользователи в предметной области [[Ayla Constitution]]
  Ст. I, физически находящиеся в зоне охвата пилотных провайдеров.
- **Территория пилота:** Пенза; дата пилота зафиксирована отдельным решением
  AYLA-DEC-0003 и в этом документе не дублируется — при переносе даты
  пересматривается решение, а не этот контракт.

**Персоны пилота (owner decision 2026-07-27):** пилот проверяет только
персоны основного end-to-end сценария (§3): клиент, ищущий услугу или
специалиста; соло-мастер; малый салон до трёх мастеров. Остальные персоны
[[Ayla Product Vision]] §11 — стратегические, не release blockers.

## 3. Primary End-to-End Scenario

Единственный обязательный сквозной сценарий MVP (дословно из
[[Ayla MVP Documentation Roadmap]] §1.2):

```text
Пользователь выражает потребность
→ Ayla уточняет intent
→ подбирает услугу или действие
→ объясняет рекомендацию
→ пользователь подтверждает
→ Ayla создаёт запись
→ пользователь получает подтверждение
```

Остальные сценарии — совместимые, но не обязательные (Roadmap §1.2).
Детализация сценария до этапов, негативных веток и owning capability — задача
MVP User Journey (производный срез [[Ayla User Journey Specification]], 14
этапов + негативные сценарии, AYLA-DEC-0014), а не этого документа.

Сквозной сценарий согласован с активационными gates
[[Consent Scope Registry]] §10: **MVP Phase 1** — session-only vertical slice
(сообщение → понимание запроса → подбор мастера → запись) без персистентной
памяти; **MVP Phase 2** — opt-in persistent preferences. Phase 2 не является
условием релиза Phase 1.

По AYLA-DEC-0018 (accepted 2026-07-28, Option C — факт): Phase 1 остаётся
самостоятельным техническим release gate; его успешное завершение не
подтверждает memory-first продуктовую гипотезу (§1). Разделяются три
понятия:

```text
Phase 1 release acceptance
≠ Phase 2 activation
≠ Product Thesis Validation
```

Phase 2 activation **необходима** для Product Thesis Validation, но сама по
себе её **не доказывает**: validation закрывается только успешным Product
Thesis Validation Scenario. Критерии — в тексте AYLA-DEC-0018; см. также
CSR §10.3.

## 4. Included Capabilities

Основа списка — [[Ayla MVP Documentation Roadmap]] §1.4; разделение на две
группы и включение CAP-014/CAP-018/CAP-022 — по AYLA-DEC-0015 (MVP Monetary
Boundary и enabling capabilities, owner decision 2026-07-27). Маппинг на
Capability ID выполнен по canonical names
[[Ayla Domain Capability Registry]] §6 и остаётся **proposal** до перевода
записей в MVP-active (волна 2, AYLA-DEC-0014): в §9 MVP Scope Matrix реестра
все записи, кроме CAP-023, имеют `mvp_scope: undetermined`.

### 4.1 Product capabilities (user-visible)

| # | Included capability | Capability ID (proposal) | Ограничение MVP |
|---|---|---|---|
| 1 | Intent Understanding | CAP-003 | Минимальный набор intent types (Roadmap §3.1) |
| 2 | Recommendation Formation | CAP-004 | Primary recommendation + alternatives; без продвинутого ML ranking (Roadmap §3.2) |
| 3 | Appointment Management | CAP-011 | Создание, подтверждение, перенос, отмена записи |
| 4 | Service Catalog | CAP-008 | Seed catalog пилотных провайдеров |
| 5 | Provider Management | CAP-009 | Минимальный профиль провайдера |
| 6 | Availability | CAP-010 | Актуальные слоты пилотных провайдеров |
| 7 | Consent Management | CAP-002 | Минимальный scope — только scopes, необходимые Phase 1/2 ([[Consent Scope Registry]] §10) |
| 8 | Personal Context | CAP-001 | Только whitelist персональных фактов (Roadmap §3.4): способ общения, категории услуг, предпочтение времени, предыдущая подтверждённая услуга, явно подтверждённые ограничения, согласие на персонализацию |
| 9 | Explanation | CAP-005 | Объяснение «почему эта рекомендация» — обязательно (Конституция Ст. VII) |
| 10 | Notification | CAP-021 | Транзакционные уведомления по записи |
| 11 | Attribution | CAP-013 | Минимальный direct linkage: `recommendation_id` → qualified action ([[Killer PRD]] §6) |
| 12 | Conversation Experience | CAP-016 | Только сквозной сценарий §3 |

> **AYLA-DEC-0023 (accepted 2026-07-28 — факт):** форма whitelist
> персональных фактов (строка 8 таблицы) заменяется категориальной —
> категории со статусом allowed / requires dedicated consent / forbidden,
> наследованием политики полями и красной зоной default deny. Позиция
> «согласие на персонализацию» как персональный факт вытесняется:
> consent state — authorization metadata, не Context Fact (AYLA-DEC-0024:
> MemoryEntry хранит только ссылку `consent_scope`). Расширение
> whitelist — только owner decision по §11 с проверками DEC-0023 п. 5.
> **Плоский список строки 8 — superseded, non-normative historical
> reference** и не является вторым нормативным источником; нормативна
> категориальная форма AYLA-DEC-0023 (+ MemoryCategoryPolicy,
> AYLA-DEC-0024 п. 7). Редакционное приведение строки 8 — pending.

### 4.2 Mandatory enabling capabilities (`user_visible_capability: false`)

Обязательны для релиза, но не являются user-visible продуктовыми функциями
(AYLA-DEC-0015):

| # | Enabling capability | Capability ID | Release role | Ограничение MVP |
|---|---|---|---|---|
| 1 | Safety Policy Enforcement | CAP-014 | `mandatory-cross-cutting`, `mvp_scope: required` | Детерминированные safety gates ко всем product capabilities ([[Killer PRD]] §8, Roadmap §7.3) |
| 2 | AI Orchestration and Tool Execution | CAP-018 | `enabling-technical-capability`, `mvp_scope: required` | Минимальный набор tools сквозного сценария (Roadmap §6.3) |
| 3 | Audit and Observability | CAP-026 | `mandatory-cross-cutting` | Только критические события (consent, authorization, booking, safety) |
| 4 | Provider monetary integration (Billing Eligibility) | CAP-022 | MVP-active | Только минимальный provider-side charge flow по §5.1; полноценный Billing — deferred (§5) |

Дополнительное нормативное ограничение Included Scope (факт из источников):
автономные действия без подтверждения пользователя запрещены (Roadmap §1.2
out of scope; Конституция).

## 5. Deferred Capabilities

Явно отложено (источник — Roadmap §1.4 Deferred; CAP-023 — по OD-CAP-4 в
редакции AYLA-DEC-0015, остальные CAP-маппинги — proposal):

| Deferred capability | Capability ID (proposal) | Основание |
|---|---|---|
| Payment Processing | CAP-023 | Полноценная payment capability deferred. В MVP допускается только минимальный provider-side charge flow для подписки и booking fee, определённый отдельным integration contract. Клиентская оплата, wallet, payouts, refunds и универсальный payment lifecycle не входят в MVP. |
| Полноценный Billing (сверх §5.1) | CAP-022 | Roadmap §1.4; минимальный provider monetary integration MVP-active по AYLA-DEC-0015 (§4.2) |
| Advanced Outcome Learning | CAP-007 | Roadmap §1.4; полноценное outcome learning — только если потребуется пилоту (Roadmap §1.2) |
| Сложная Experimentation Platform | CAP-025 | Roadmap §1.4; базовые метрики §9 этим не отменяются |
| Расширенный Marketplace Search | CAP-024 | Roadmap §1.4; весь marketplace — out (Roadmap §1.2) |
| Cross-product tenant customization | CAP-020 | Roadmap §1.4; сложная multi-tenant тарификация — out (Roadmap §1.2) |
| Глубокая provider verification | часть CAP-009 | Roadmap §1.4 |
| Автоматическая обработка health outcomes | CAP-006/CAP-007 | Roadmap §1.4; медицинская диагностика и автоматические выводы о здоровье запрещены ([[Killer PRD]] §9, Roadmap §1.2) |

### 5.1 MVP Provider Monetary Boundary

Факт — решение AYLA-DEC-0015 (owner decision 2026-07-27, OD-MVP-PAY-1):

В MVP входит ограниченный денежный контур провайдера:

- списание подписки;
- списание booking fee 90 ₽;
- обработка результата попытки списания;
- обновление billing status;
- применение eligibility gate;
- минимальная reconciliation с платёжным провайдером.

Этот контур **не означает активацию CAP-023 Payment Processing** и не создаёт
универсальный payment domain.

Вне scope остаются:

- клиентская онлайн-оплата услуг;
- wallet и внутренний баланс;
- payouts;
- refunds;
- chargebacks;
- split settlement как универсальная capability;
- полноценный financial ledger.

Также вне MVP (факты из [[Ayla MVP Product Thesis]] §7 и Roadmap §1.2/§1.3):

- Telegram как канал (AYLA-DEC-0004);
- сложная программа лояльности; несколько стран; продвинутые ML-модели;
  сложные модели обучения, долгосрочные cohort mechanics, глубокая
  оптимизация ranking, сложная monetization attribution.

## 6. Required Integrations

Факты из источников:

- **MAX platform** — канал пилота (AYLA-DEC-0004), см. §7.
- **Backend API (beautygo_backend)** — SoR для каталога, провайдеров,
  availability, записей, consent и context facts; набор endpoints MVP —
  по Roadmap §6.2 (current user, consent, context facts, service search,
  provider candidates, availability, appointment create/update/cancel,
  recommendation persistence, attribution, feedback).
- **ayla-ai-core** — библиотека reusable AI logic; **ai-bot-platform** —
  runtime/channel consumer (Roadmap §5.1, рекомендуемая MVP-композиция;
  backend допустим как модульный монолит).
- **LLM provider** — через provider abstraction ayla-ai-core; определён
  model/provider fallback (Roadmap §9.1).
- **YooKassa** — обязательная интеграция только для provider-side charge
  flow: подписка, booking fee 90 ₽, payment result callback и минимальная
  reconciliation. Клиентская онлайн-оплата и полноценный Payment Processing
  остаются вне MVP (AYLA-DEC-0015).

## 7. Required Channels

- **MAX-бот + MAX Mini App** — единственные обязательные каналы MVP
  (AYLA-DEC-0004, Thesis §6).
- Telegram — вне пилотного scope (AYLA-DEC-0004, Thesis §7).
- Универсальная multi-channel спецификация не требуется для MVP (Roadmap,
  «Что не должно блокировать MVP»).

## 8. Non-Functional Minimum

Минимум, обязательный к релизу (факт — Roadmap §9.1 Release Readiness,
сгруппировано):

- **Security:** access control; tenant isolation; управление secrets; правила
  логирования (без PII в логах); rate limits; audit; backup.
- **Privacy:** по умолчанию режим [[Consent Scope Registry]] §10 — session
  context only, no proactive recommendations, no cross-domain
  personalization, no persistent inferred signals, no persistent preference
  storage — до выполнения gate Phase 2.
- **AI:** закреплённые версии prompt; совместимые tool schemas; установленный
  token budget; протестированные hallucination-сценарии; определённый
  model/provider fallback.
- **Operations:** monitoring; alerts; support process; назначенный incident
  owner; возможность rollback; feature flags.
- **Product:** primary journey работает end-to-end; рекомендация объяснима;
  fallback существует; критических тупиков нет.

Числовые SLA/пороги производительности в этом документе не устанавливаются —
единственная зафиксированная метрика времени отклика учитывается как
`median response time` в §9 (Roadmap §9.2).

## 9. Release Metrics

**Главная метрика MVP (факт — Roadmap §9.2):** проверяется не количество
сообщений, а переход:

```text
осмысленный запрос
→ полезная рекомендация
→ подтверждённое действие
```

Минимальный набор метрик пилота (факт — Roadmap §9.2):

- доля resolved intents;
- clarification rate;
- recommendation shown rate;
- recommendation acceptance rate;
- booking conversion;
- booking completion;
- attributed qualified actions;
- recommendation rejection reasons;
- unsafe block rate;
- tool failure rate;
- median response time;
- пользовательская оценка полезности.

Критерии подтверждения/опровержения тезиса по этим метрикам —
[[Ayla MVP Product Thesis]] §8.1/§8.2. **Числовые пороги здесь не
фиксируются:** по Thesis §8.1 они остаются design candidates до данных пилота
или отдельного Measurement Framework (паттерн ADR-0012 OD-5/OD-6).

## 10. Release Blockers

Релиз блокируется до закрытия следующих условий (факты из источников):

1. **Consent gates ([[Consent Scope Registry]] §10.1):** scopes
   `intent_understanding` и `provider_selection` переведены из `proposed` в
   `approved`; persistent memory технически отключена до Phase 2. Для Phase 2
   дополнительно (§10.2): `preference_memory` approved, закрыт CSR-OD-5
   (canonical SoR для consent records), подтверждение формулировок Privacy
   Owner, реализованный runtime authorization contract, negative test
   «отсутствие consent → deny».
2. **Killer PRD canonical approval** заблокирован ADR-0012 OD-1/OD-2, OD-K9 и
   OD-K11 (Thesis §9) — до их закрытия §3 и §12 остаются proposed.
3. **Predecessor documents** по AYLA-DEC-0014, волна 1: MVP User Journey и
   Intent Model Specification — сквозной сценарий §3 не детализирован без них.
4. **AMD-020 Pilot Scope Registry** зависит от Data Inventory Matrix
   (Thesis §9) — граница §1 не может быть проверена до её материализации.

Governance Exit фазы MVP (Thesis §8.4): блокеры выше должны быть закрыты или
явно вынесены в план Phase 1.5; решение о переходе фазы принимает Product
Owner и не является автоматическим.

## 11. Change Control

**Критическое правило (дословно, Roadmap §1.4 и AYLA-DEC-0014):** после
approval любое расширение Included Scope требует owner decision с указанием:

- зачем оно нужно до MVP;
- какой срок добавляет;
- какую текущую задачу вытесняет.

Дополнительно (факт — Thesis §8): входной фильтр для любого кандидата в
Included Scope — admission principle: функция входит в MVP, только если она
напрямую усиливает memory-first тезис (AYLA-DEC-0002) и не нарушает таблицу
MVP-принципов Thesis §8.3.

> **Proposal (не факт):** сокращение Included Scope или уточнение формулировок
> без расширения фиксируется записью в Change Log этого документа и записью в
> [[Ayla Decision Log]]; формальное правило — подтвердить при approval.

## Change Log

> Этот журнал отражает историю изменений документа и не является нормативной
> частью спецификации. Нормативным считается текущее состояние разделов 1–12.

### v0.3 (2026-07-28) — Применено AYLA-DEC-0018 и AYLA-DEC-0023 (единый Change Control)

- **§3** добавлено положение по AYLA-DEC-0018 (accepted, Option C): Phase 1 —
  самостоятельный технический release gate; Product Thesis Validation —
  отдельный acceptance, открытый до Phase 2 и успешного Product Thesis
  Validation Scenario; активация Phase 2 не закрывает validation; Phase 2 не
  становится условием релиза Phase 1.
- **§4.1** добавлено примечание по AYLA-DEC-0023: форма whitelist
  персональных фактов заменяется категориальной; позиция «согласие на
  персонализацию» вытесняется (Consent state ≠ Context Fact, AYLA-DEC-0024);
  редакционное приведение строки 8 таблицы — pending.
- Выполнено в рамках единого Change Control approved-документов по
  AYLA-DEC-0018/0023/0024/0025 (совместно с Consent Scope Registry §10.3 и
  Roadmap §3.4). Статус документа не изменён (draft/proposed; нормативная
  сила — после approval по §12).

### v0.2 (2026-07-27) — Применено AYLA-DEC-0015 (MVP Monetary Boundary)

- **§5.1** добавлен: MVP Provider Monetary Boundary (provider-side charge
  flow: подписка, booking fee 90 ₽, charge result, billing status,
  eligibility gate, минимальная reconciliation) — без активации CAP-023.
- **§5** строка Payment Processing переписана по AYLA-DEC-0015; строка
  Billing уточнена: CAP-022 MVP-active только в части §5.1.
- **§6** добавлена обязательная интеграция YooKassa (только provider-side
  charge flow); статус proposal снят.
- **§4** разделён на §4.1 Product capabilities (12 user-visible) и §4.2
  Mandatory enabling capabilities: CAP-014 (`mandatory-cross-cutting`,
  `mvp_scope: required`), CAP-018 (`enabling-technical-capability`,
  `mvp_scope: required`), CAP-026, минимальный provider monetary integration
  (CAP-022).
- **§2** зафиксировано owner decision по персонам пилота (клиент, ищущий
  услугу/специалиста; соло-мастер; малый салон до трёх мастеров); остальные
  персоны Vision §11 — стратегические, не release blockers.
- Закрыты открытые вопросы v0.1: денежный контур, статус CAP-014/CAP-018,
  персоны пилота, интеграция YooKassa — по AYLA-DEC-0015 / owner decision
  2026-07-27. Остаются открытыми: маппинг CAP-ID до волны 2 (§4) и правило
  сокращения scope (§11).

### v0.1 (2026-07-27) — Initial draft

- Документ создан по AYLA-DEC-0014 и [[Ayla MVP Documentation Roadmap]] §1.4.
- Included/Deferred списки перенесены дословно из Roadmap §1.4; маппинг на
  CAP-ID выполнен по [[Ayla Domain Capability Registry]] §6 и помечен как
  proposal (Registry §9 — `undetermined` для всех записей, кроме CAP-023).
- Зафиксирована граница с [[AMD-020 Pilot Scope Registry]] (pilot/memory
  ownership ≠ release scope) по AYLA-DEC-0014.
- Открытые вопросы: применимость персон к пилоту (§2); статус CAP-014/CAP-018
  (§4); расхождение Thesis §6 и OD-CAP-4 по денежному контуру (§5);
  интеграция YooKassa (§6); правило сокращения scope (§11).

## 12. Approval

**Status:** Draft — pending Product Owner review. Approval невозможен до
выполнения предусловий §10 п. 2–3. Маппинг CAP-ID (§4, proposal) подлежит
сверке при переводе записей Registry в MVP-active (волна 2, AYLA-DEC-0014) и
не блокирует approval этого документа.

Для approval необходимы:

- Product Owner review (scope, change control);
- Product Architecture review (маппинг на Capability Registry);
- Privacy review (согласование с [[Consent Scope Registry]] §10 gates).

С момента approval вступает в силу Change Control (§11): Included Scope
замораживается, и любое его расширение требует owner decision по форме §11.
