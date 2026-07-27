---
node_id: ayla.strategy.mvp-scope-release-contract
title: Ayla MVP Scope and Release Contract
type: specification
status: draft
decision_status: proposed
version: "0.1"
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
updated: 2026-07-27
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
- **Персоны:** определены на уровне продукта в [[Ayla Product Vision]] §11.

> **Открытый вопрос (из Thesis §10, не закрыт здесь):** действуют ли все три
> персоны Vision §11 одинаково для пилота в Пензе, или пилот — валидация
> подмножества.

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

## 4. Included Capabilities

Список включённых capability — дословно из [[Ayla MVP Documentation Roadmap]]
§1.4. Маппинг на Capability ID выполнен по canonical names
[[Ayla Domain Capability Registry]] §6 и помечен как **proposal**: в §9 MVP
Scope Matrix реестра все записи, кроме CAP-023, имеют `mvp_scope:
undetermined`; перевод MVP-active записей — отдельная задача волны 2
(AYLA-DEC-0014), а не содержимое этого документа.

| # | Included capability | Capability ID (proposal) | Ограничение MVP |
|---|---|---|---|
| 1 | Conversation Experience | CAP-016 | Только сквозной сценарий §3 |
| 2 | Intent Understanding | CAP-003 | Минимальный набор intent types (Roadmap §3.1) |
| 3 | Consent Management | CAP-002 | Минимальный scope — только scopes, необходимые Phase 1/2 ([[Consent Scope Registry]] §10) |
| 4 | Personal Context | CAP-001 | Только whitelist персональных фактов (Roadmap §3.4): способ общения, категории услуг, предпочтение времени, предыдущая подтверждённая услуга, явно подтверждённые ограничения, согласие на персонализацию |
| 5 | Service Catalog | CAP-008 | Seed catalog пилотных провайдеров |
| 6 | Provider Management | CAP-009 | Минимальный профиль провайдера |
| 7 | Availability | CAP-010 | Актуальные слоты пилотных провайдеров |
| 8 | Recommendation Formation | CAP-004 | Primary recommendation + alternatives; без продвинутого ML ranking (Roadmap §3.2) |
| 9 | Explanation | CAP-005 | Объяснение «почему эта рекомендация» — обязательно (Конституция Ст. VII) |
| 10 | Appointment Management | CAP-011 | Создание, подтверждение, перенос, отмена записи |
| 11 | Notification | CAP-021 | Транзакционные уведомления по записи |
| 12 | Attribution | CAP-013 | Минимальный direct linkage: `recommendation_id` → qualified action ([[Killer PRD]] §6) |
| 13 | Audit | CAP-026 | Только критические события (consent, authorization, booking, safety) |

Дополнительные нормативные ограничения Included Scope (факты из источников):

- Safety gates ([[Killer PRD]] §8, Roadmap §7.3) и deterministic checks —
  обязательны как cross-cutting требования ко всем included capabilities, без
  расширения списка.
- Автономные действия без подтверждения пользователя запрещены (Roadmap §1.2
  out of scope; Конституция).

> **Открытый вопрос:** CAP-014 (Safety Policy Enforcement) и CAP-018 (AI
> Orchestration and Tool Execution) не входят в Included-список Roadmap §1.4,
> но safety enforcement и tool execution требуются сквозным сценарием.
> Трактовка (cross-cutting требование vs расширение списка через §11) —
> owner decision при approval.

## 5. Deferred Capabilities

Явно отложено (источник — Roadmap §1.4 Deferred; CAP-023 — факт по OD-CAP-4,
остальные CAP-маппинги — proposal):

| Deferred capability | Capability ID (proposal) | Основание |
|---|---|---|
| Payment Processing | CAP-023 | **Факт:** `mvp_scope: out`, `platform_scope: in`, `activation_status: deferred` — OD-CAP-4 (AYLA-DEC-0012), Registry §9 |
| Полноценный Billing | CAP-022 | Roadmap §1.4 |
| Advanced Outcome Learning | CAP-007 | Roadmap §1.4; полноценное outcome learning — только если потребуется пилоту (Roadmap §1.2) |
| Сложная Experimentation Platform | CAP-025 | Roadmap §1.4; базовые метрики §9 этим не отменяются |
| Расширенный Marketplace Search | CAP-024 | Roadmap §1.4; весь marketplace — out (Roadmap §1.2) |
| Cross-product tenant customization | CAP-020 | Roadmap §1.4; сложная multi-tenant тарификация — out (Roadmap §1.2) |
| Глубокая provider verification | часть CAP-009 | Roadmap §1.4 |
| Автоматическая обработка health outcomes | CAP-006/CAP-007 | Roadmap §1.4; медицинская диагностика и автоматические выводы о здоровье запрещены ([[Killer PRD]] §9, Roadmap §1.2) |

Также вне MVP (факты из [[Ayla MVP Product Thesis]] §7 и Roadmap §1.2/§1.3):

- Telegram как канал (AYLA-DEC-0004);
- внутренний баланс/кошелёк провайдера с выводом T+24ч — эпик этапа 2
  (AYLA-DEC-0008);
- сложная программа лояльности; несколько стран; продвинутые ML-модели;
  сложные модели обучения, долгосрочные cohort mechanics, глубокая
  оптимизация ranking, сложная monetization attribution.

> **Открытый вопрос (расхождение источников, требует owner decision):**
> Thesis §6 включает в MVP автосписание подписки и booking fee с провайдера
> через сохранённую карту (AYLA-DEC-0007) и split per-master через YooKassa
> (AYLA-DEC-0008), а CAP-023 Payment Processing имеет `mvp_scope: out`
> (OD-CAP-4). Граница между «провайдерским денежным контуром пилота» и
> deferred Payment Processing в источниках явно не проведена; до owner
> decision этот документ трактует CAP-023 как deferred, а клиентскую
> онлайн-оплату — как опциональную (AYLA-DEC-0006).

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

> **Proposal (не факт):** интеграция с YooKassa не включается в Required
> Integrations до закрытия открытого вопроса §5 о денежном контуре пилота.

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
закрытия открытых вопросов §4, §5 и выполнения предусловий §10 п. 2–3.

Для approval необходимы:

- Product Owner review (scope, change control);
- Product Architecture review (маппинг на Capability Registry);
- Privacy review (согласование с [[Consent Scope Registry]] §10 gates).

С момента approval вступает в силу Change Control (§11): Included Scope
замораживается, и любое его расширение требует owner decision по форме §11.
