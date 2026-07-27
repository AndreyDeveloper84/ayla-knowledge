---
node_id: ayla.foundation.domain-capability-registry
title: Ayla Domain Capability Registry
type: specification
status: draft
decision_status: proposed
version: "1.2"
owner: Product Architecture
priority: P0
knowledge_area:
  - foundation
  - architecture
  - strategy
domain:
  - cross-domain
concerns:
  - governance
system_owner:
  - shared
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
review_cycle: before-major-change
implements:
  - "[[Ayla Constitution]]"
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Product Vision]]"
  - "[[Killer PRD]]"
  - "[[Ayla Decision Log]]"
related:
  - "[[Ayla MVP Product Thesis]]"
  - "[[Ayla User Journey Specification]]"
  - "[[Ayla Core Domain Model Specification]]"
  - "[[Ayla Domain Context Map]]"
  - "[[ADR-0012 Dynamic User Model]]"
supersedes: []
---

# Ayla Domain Capability Registry

**Версия:** 1.2  
**Статус:** Draft — proposed  
**Владелец:** Product Architecture  
**Область применения:** вся продуктовая экосистема Ayla

---

## 1. Purpose

### 1.1. Назначение документа

Настоящий документ является реестром доменных способностей (domain capabilities) Ayla. Он принадлежит Product Architecture и отвечает ровно на три вопроса:

1. Какая способность нужна продукту?
2. Какой бизнес-результат она создаёт?
3. В каком candidate context она предположительно реализуется?

Domain capability описывает способность бизнеса или продукта достигать значимого результата. Она не описывает конкретную реализацию, сервис, модуль, API, таблицу базы данных, LLM-провайдера, Django application, мобильный экран или repository boundary.

### 1.2. Чем документ не является

Документ не содержит DDD-методологию. Правила выявления, классификации, разделения, объединения и подтверждения контекстов определены в [[Ayla Domain Context Map]] и здесь не дублируются (см. §3).

Документ не подтверждает bounded contexts и не заменяет Product Vision, Killer PRD, Domain Context Map или техническую архитектуру. Он связывает их через прослеживаемый реестр продуктовых способностей.

### 1.3. Происхождение

Документ является переработкой `Ayla Domain Capability Specification` v1.0 (draft) по решениям владельца OD-CAP-1..4: документ переименован в Registry, методологические разделы удалены (возвращены в Domain Context Map), классификация приведена к единой схеме Domain Context Map, Capability Record сокращён, добавлены evidence-, reconciliation- и MVP-матрицы.

### 1.4. Registry lifecycle

Запись реестра проходит жизненный цикл:

```text
identified → under-review → approved → active → deprecated → retired
```

- `identified` — capability зафиксирована в реестре, но содержимое записи неполно или не верифицировано;
- `under-review` — запись заполнена и проходит review против канонических источников;
- `approved` — запись утверждена в установленном порядке (§14), capability ещё не обязана быть реализована;
- `active` — capability реализована и используется в продукте;
- `deprecated` — capability подлежит выводу; новые реализации и новые consumers не допускаются;
- `retired` — capability выведена из реестра; идентификатор зарезервирован навсегда (см. §5.1).

Статусы записей §6 используют эту терминологию.

---

## 2. Scope

### 2.1. Входит в scope

Реестр охватывает способности Ayla, необходимые для:

- понимания пользовательского намерения;
- использования разрешённого персонального контекста;
- формирования объяснимых рекомендаций;
- выполнения действий от имени пользователя;
- поиска услуг и специалистов;
- управления доступностью и записью;
- управления согласием, privacy и safety;
- фиксации результата и обучения на подтверждённых данных;
- атрибуции рекомендаций к действиям;
- поддержки специалистов и салонов;
- биллинга, eligibility и платежных процессов;
- conversation experience и multi-channel delivery;
- управления knowledge, policies и configuration;
- product measurement, audit и observability.

### 2.2. Не входит в scope

Документ не определяет:

- конкретные микросервисы;
- физические базы данных;
- таблицы, индексы и схемы хранения;
- URL и HTTP endpoints;
- внутренние классы и интерфейсы языка программирования;
- конкретные очереди, брокеры, кэши и облачных провайдеров;
- UI-компоненты;
- структуру CI/CD;
- детализацию deployment topology;
- выбор LLM или embedding model;
- конкретную реализацию RAG;
- организационную структуру команды;
- окончательные repository boundaries;
- lifecycle, commands и events capabilities (уровень bounded context / domain specification, см. §5);
- правила выявления, классификации, split/merge и подтверждения capabilities (см. [[Ayla Domain Context Map]]).

Эти решения могут ссылаться на capabilities, но не подменяют их.

### 2.3. Продуктовые границы

Реестр применяется к:

- пользовательскому приложению Ayla;
- Ayla Pro;
- AI-ботам и каналам взаимодействия;
- backend-системам marketplace;
- reusable AI core;
- knowledge repository;
- будущим продуктам экосистемы, если они используют общий канон Ayla.

---

## 3. Authority and Relationship to Other Documents

### 3.1. Позиция в цепочке документов

```text
Ayla Product Vision
        ↓
Killer PRD
        ↓
Ayla Intent Model Specification (planned predecessor — документ ещё не создан)
        ↓
Ayla Domain Capability Registry (настоящий документ)
        ↓
Ayla Domain Context Map
```

Настоящий документ не стоит выше Domain Context Map в иерархии канона. По AYLA-DEC-0011 (см. [[Ayla Decision Log]]):

> Capability Registry может разрабатываться параллельно, но не может быть approved или использоваться для подтверждения bounded contexts до утверждения обязательных predecessor documents по AYLA-DEC-0011.

Ayla Intent Model Specification является обязательным planned predecessor данного реестра; на момент v1.1 документ не создан, поэтому реестр не может перейти к approval.

### 3.2. Отношение к Domain Context Map

Capability identification, classification, split, merge and context confirmation follow the normative rules defined in [[Ayla Domain Context Map]].

Настоящий документ определяет только:

- состав реестра (перечень capability records);
- обязательную структуру Capability Record (§5);
- локальные правила заполнения записей и evidence (§4);
- reconciliation-, MVP- и evidence-матрицы как снимок текущего состояния реестра.

Классификация записей использует строго категории Domain Context Map: `core`, `supporting`, `generic`, `technical-capability`. Одна запись — одна категория; multi-classification запрещена. `governance` и `platform` не являются категориями классификации — это characteristics записи (см. §5).

### 3.3. Статус проверки валидатором

Валидатор `validate_knowledge.py` подтверждает структурную и ссылочную корректность документа, но не подтверждает содержательную согласованность или canonical approval.

### 3.4. Нормативные свойства

До approval конкретные capability records являются архитектурными гипотезами и должны проходить review против канонических источников. После approval нормативным является перечень зафиксированных capabilities и их стабильные идентификаторы.

---

## 4. Source and Evidence Rules

### 4.1. Источники

Основными источниками evidence для записей реестра являются:

1. **Ayla Constitution** — фундаментальные права, ограничения и принципы.
2. **Ayla Product Vision** — стратегическое назначение, value proposition и долгосрочный горизонт.
3. **Killer PRD** — killer experience, trigger-сценарии, recommendation rules, attribution, metrics, privacy и safety constraints.
4. **Ayla Decision Log** — утверждённые owner rulings и cross-repository решения.
5. **Ayla MVP Product Thesis** — scope MVP, сегменты и критерии запуска.
6. **Ayla User Journey Specification** — последовательность пользовательского опыта.
7. **Ayla Intent Model Specification** — модель намерения и уточнения (planned predecessor, документ ещё не создан).
8. **Ayla Core Domain Model Specification** — базовые правила identity, state, lifecycle, facts, inference, commands и events.
9. **ADR-0012 Dynamic User Model** — персональный контекст, память и ограничения обработки.
10. Профильные specifications, contracts и accepted ADR.

В записи реестра включаются только источники, которые реально цитировались исходным документом v1.0 (§3 «Source Documents» и §13 «Traceability Matrix»). Новые источники добавляются только после проверки их содержимого.

### 4.2. Иерархия evidence

При конфликте применяется следующая иерархия:

1. Constitution.
2. Утверждённые Decision Log entries в пределах их scope.
3. Утверждённые Foundation и cross-product policies.
4. Accepted ADR в пределах decision scope.
5. Approved product и domain specifications.
6. API, event и implementation contracts.
7. Код как evidence фактического поведения.
8. Plans, research, handoff, working notes и исторические документы.

Более новая дата документа сама по себе не создаёт более высокий authority.

### 4.3. Evidence Record

Каждая capability должна иметь evidence record в формате:

```yaml
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "6.2"
    claim: "Ayla понимает намерение пользователя, а не только команду"
```

Evidence должно:

- подтверждать бизнес-необходимость capability;
- указывать точный источник и раздел;
- отделять факт от интерпретации;
- не опираться только на имя модуля или существование кода;
- явно отмечать гипотезы и unresolved conflicts;
- хранить связь с owner decision, если capability появилась из решения владельца.

### 4.4. Недостаточное evidence

Недостаточным считается:

- название папки или Django app;
- наличие таблицы базы данных;
- существование API;
- упоминание функции в roadmap без product rationale;
- единственный исторический документ, противоречащий новому канону;
- повторение технической реализации без самостоятельного бизнес-результата.

### 4.5. Правила confidence и evidence_status

1. `confidence: high` запрещён без проверенных evidence-ссылок. Traceability-ссылки v1.0 (§13.3 исходного документа) не проверены против содержимого источников, поэтому в v1.1 максимальный confidence — `medium`, с явным указанием, что ссылка не верифицирована.
2. Если реального evidence в исходном документе нет, запись получает `evidence_status: missing`, `status: identified`, `confidence: low`.
3. Записи, для которых исходный v1.0 не сформулировал явный `business_outcome`, получают `status: identified` до заполнения поля в ходе evidence verification.
4. Сводное состояние evidence фиксируется в §10 Evidence Coverage Matrix.

### 4.6. Evidence для Payment Processing (CAP-023)

Evidence для CAP-023 берётся из Ayla Product Vision (business model) и backend payment contracts. Прежняя трассировка v1.0 на Killer PRD §9 удалена как ошибочная: §9 Killer PRD является разделом «вне scope» и не может служить evidence существования capability (owner direction OD-CAP-4).

---

## 5. Capability Record Schema

Каждая запись реестра заполняется по следующей схеме (сокращённый вариант, owner direction OD-CAP-1/OD-CAP-2):

```yaml
capability_id: CAP-###
canonical_name: Stable cross-document reference name
display_name: ...           # optional; only when differs from canonical_name
name: Human-readable name
status: identified | under-review | approved | active | deprecated | retired
classification: core | supporting | generic | technical-capability
characteristics: []            # subset of: governance, platform
business_purpose: ...
business_outcome: ...
owned_concepts: []
non_owned_concepts: []
authoritative_responsibility: ...
key_invariants: []
upstream_capabilities: []
downstream_capabilities: []
candidate_contexts: []
mvp_scope: in | out | deferred | undetermined
introduced_by: undetermined  # or {source: "Product Vision", version: "1.3"} or {decision: "AYLA-DEC-0012"}
evidence: []
open_questions: []
```

Правила заполнения:

1. `capability_id` стабилен после публикации и никогда не переиспользуется (контракт неизменяемости — §5.1). Формат v1.1+ — `CAP-###` (в v1.0 использовался префикс `AYLA-CAP-###`; нумерация сохранена).
2. `canonical_name` — стабильное имя для ссылок между документами. Для всех текущих записей совпадает с `name`; при последующем переименовании capability меняется `name`/`display_name`, а `canonical_name` и `capability_id` остаются неизменными. `display_name` заполняется только если отличается от `canonical_name`.
3. `classification` — ровно одна категория из Domain Context Map. Бывшая secondary classification v1.0 перенесена в `characteristics` (`governance`, `platform`).
4. `business_purpose` — краткое описание того, зачем capability существует; `business_outcome` — конкретный результат для пользователя, специалиста, бизнеса или governance. Если исходный draft v1.0 не формулировал outcome явно, поле остаётся пустым, а запись получает `status: identified` (см. §4.5).
5. `owned_concepts` — понятия, семантика которых принадлежит capability; `non_owned_concepts` — используемые, но принадлежащие другим capability или SoR.
6. `authoritative_responsibility` — состояние, для которого capability является authority.
7. `key_invariants` — нормативные правила, обязательные во всех реализациях.
8. `upstream_capabilities` / `downstream_capabilities` — зависимости через бизнес-контракты; заполнены по потокам v1.0 (§8 исходного документа), перенесённым в §7 настоящего документа.
9. Lifecycle, commands и events в реестре не описываются: это уровень bounded context / domain specification (см. [[Ayla Domain Context Map]] и [[Ayla Core Domain Model Specification]]). Зафиксированные в v1.0 lifecycle/commands/events при подтверждении контекстов переносятся в соответствующие domain specifications.
10. `introduced_by` — происхождение capability: ссылка на источник с версией (`{source: Product Vision, version: "1.3"}`) или на решение владельца (`{decision: AYLA-DEC-0012}`). Заполняется только там, где происхождение следует из verified evidence записи; где неизвестно — `undetermined`, не выдумывается (см. §11).
11. Служебные поля реестра `confidence` и `evidence_status` добавляются к записи по правилам §4.5 и сводятся в §10. Для CAP-023 дополнительно фиксируются `platform_scope` и `activation_status` (§9).

### 5.1. Контракт неизменяемости Capability ID

1. Capability ID никогда не переиспользуется.
2. После публикации Registry идентификатор постоянен, даже если capability переименовывается (эволюционируют только `name`/`display_name`; `canonical_name` и `capability_id` сохраняются).
3. При удалении capability её статус становится `retired` (§1.4), а идентификатор резервируется навсегда и не выдаётся новой записи.

Цель контракта — упростить traceability: ссылка на `CAP-###` из любого документа всегда указывает на одну и ту же capability независимо от переименований и вывода из эксплуатации.

---

## 6. Capability Registry

### 6.1. CAP-001 — Personal Context Management

```yaml
capability_id: CAP-001
canonical_name: Personal Context Management
name: Personal Context Management
status: under-review
classification: core
characteristics:
  - governance
confidence: medium
evidence_status: partial
business_purpose: поддерживать управляемое, прозрачное и разрешённое представление устойчивого персонального контекста пользователя.
business_outcome: более последовательный персонализированный опыт при сохранении контроля пользователя над данными.
owned_concepts:
  - Personal Context Fact
  - Fact Source
  - Fact Confidence
  - User Confirmation Status
  - Context Category
  - Context Validity
  - Correction Record
  - Deletion Request
  - Context Provenance
non_owned_concepts:
  - Consent Grant
  - Recommendation
  - Conversation Message
  - Appointment
  - Provider Profile
  - Safety Policy
authoritative_responsibility: подтверждённые и разрешённые персональные факты и их provenance.
key_invariants:
  - Inference не становится confirmed fact без предусмотренного основания.
  - Каждый факт имеет source и provenance.
  - Удалённый или revoked context не используется в новых решениях.
  - Capability не расширяет consent scope.
  - Sensitive category имеет явную policy classification.
  - Пользователь может просмотреть, исправить и удалить доступный ему context.
  - Superseded fact сохраняет auditable history в допустимых пределах.
upstream_capabilities:
  - CAP-002
  - CAP-016
downstream_capabilities:
  - CAP-017
  - CAP-003
  - CAP-004
candidate_contexts:
  - Personal Context
  - Memory Management
  - Consent Management
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§1, §4, §6.1, §15"
    claim: "Персональный контекст — часть продуктового обещания Ayla (traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано)."
  - source: "[[Killer PRD]]"
    section: "§2, §6, §8"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
open_questions:
  - "Граница Personal Context / Memory Management / Consent Management — tracked in Ayla Domain Context Map §5.26."
```

### 6.2. CAP-002 — Consent Management

```yaml
capability_id: CAP-002
canonical_name: Consent Management
name: Consent Management
status: under-review
classification: supporting
characteristics:
  - governance
confidence: medium
evidence_status: partial
business_purpose: управлять разрешением на сбор, хранение, использование, передачу и удаление персонального контекста по конкретным целям и категориям данных.
business_outcome: пользователь контролирует processing, а продукт может доказать наличие применимого consent.
owned_concepts:
  - Consent Scope
  - Consent Grant
  - Consent Purpose
  - Data Category
  - Grant Version
  - Consent Status
  - Revocation
  - Expiration
  - Legal Basis Reference
non_owned_concepts: []
authoritative_responsibility: Consent Grant, его scope, версия и статус.
key_invariants:
  - Consent purpose-specific.
  - Отсутствие согласия не является согласием.
  - Новая цель не наследует старый consent автоматически.
  - Revocation блокирует новое использование.
  - Consent version сохраняется в зависимых решениях.
  - UI wording и machine-readable scope согласованы.
  - Обязательное processing и опциональная персонализация не объединяются в неделимый consent.
upstream_capabilities: []
downstream_capabilities:
  - CAP-001
  - CAP-004
  - CAP-007
  - CAP-017
  - CAP-021
candidate_contexts:
  - Consent Management
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§1, §6.1"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§6, §8, §12.1"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
open_questions:
  - "Кто владеет Consent Scope Registry (см. §11)."
```

### 6.3. CAP-003 — Intent Understanding

```yaml
capability_id: CAP-003
canonical_name: Intent Understanding
name: Intent Understanding
status: identified
classification: core
characteristics: []
confidence: medium
evidence_status: partial
business_purpose: преобразовывать естественное выражение пользователя и доступный context в структурированное представление текущего намерения.
business_outcome: null  # не сформулирован явно в v1.0; заполняется при evidence verification
owned_concepts:
  - Intent
  - Intent Type
  - Intent Slot
  - Intent Confidence
  - Clarification Need
  - Clarification Question
  - Intent Status
  - Intent Evidence
non_owned_concepts: []
authoritative_responsibility: структурированное представление текущего intent и его clarification state.
key_invariants:
  - Low-confidence не маскируется как определённый intent.
  - Missing slots выявляются до action.
  - User correction приоритетнее inference.
  - Intent не владеет recommendation result.
  - Evidence сохраняется.
  - Incompatible purpose scope не переносится без подтверждения.
upstream_capabilities:
  - CAP-016
downstream_capabilities:
  - CAP-004
candidate_contexts:
  - Intent Understanding
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§6.2"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое раздела не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§2, §4, §5"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
open_questions: []
```

### 6.4. CAP-004 — Recommendation Formation

```yaml
capability_id: CAP-004
canonical_name: Recommendation Formation
name: Recommendation Formation
status: identified
classification: core
characteristics:
  - governance
confidence: medium
evidence_status: partial
business_purpose: формировать один объяснимый и безопасный primary next step для текущего intent с допустимыми alternatives.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Recommendation
  - Candidate
  - Recommendation Role
  - Status
  - Ranking Release
  - Score Breakdown
  - Explanation
  - Rerank Reason
  - Validity
  - Integrity Status
non_owned_concepts: []
authoritative_responsibility: Recommendation, её роли, ranking release и integrity status.
key_invariants:
  - Используется только разрешённый context.
  - Primary recommendation одна.
  - Alternative имеет собственный recommendation_id.
  - Economic-only parameter не меняет organic ordering.
  - Quarantined release не обслуживает traffic.
  - Explanation не раскрывает запрещённые sensitive facts.
  - Invalidated recommendation не участвует в derived flow.
  - Recommendation не создаёт appointment без отдельного action contract.
  - Candidate проходит safety, eligibility, availability и policy gates до ranking.
upstream_capabilities:
  - CAP-003
  - CAP-017
  - CAP-008
  - CAP-009
  - CAP-010
  - CAP-022
downstream_capabilities:
  - CAP-005
  - CAP-013
  - CAP-006
candidate_contexts:
  - Recommendation
  - Safety Policy
  - Attribution
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§6.3, §8"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§4–§6"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
open_questions:
  - "Recommendation Formation, Explanation, recommendation integrity и organic neutrality enforcement reconcile в один candidate context Recommendation (owner direction, см. §8)."
```

### 6.5. CAP-005 — Explanation and Context Attribution

```yaml
capability_id: CAP-005
canonical_name: Explanation and Context Attribution
name: Explanation and Context Attribution
status: identified
classification: core
characteristics:
  - governance
confidence: medium
evidence_status: partial
business_purpose: показывать, почему Ayla предложила конкретный следующий шаг и какой разрешённый context применён.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Recommendation Explanation
  - Context Usage Disclosure
  - Explanation Template
  - Explanation Visibility
  - Explanation Redaction
non_owned_concepts: []
authoritative_responsibility: объяснение рекомендации и disclosure фактически использованного context.
key_invariants:
  - Explanation соответствует фактически использованному context.
  - Нельзя заявлять неиспользованный факт.
  - Нельзя раскрывать hidden sensitive context.
  - Explanation не заменяет consent.
  - Есть путь исправления неверного context.
upstream_capabilities:
  - CAP-004
downstream_capabilities:
  - CAP-016
candidate_contexts:
  - Recommendation
  - Conversation
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§6.3"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое раздела не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§6.1, §8"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
open_questions: []
```

### 6.6. CAP-006 — Outcome Capture

```yaml
capability_id: CAP-006
canonical_name: Outcome Capture
name: Outcome Capture
status: identified
classification: core
characteristics: []
confidence: medium
evidence_status: partial
business_purpose: фиксировать подтверждённые действия, изменения и результаты, связанные с рекомендациями и пользовательскими целями.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Outcome
  - Outcome Type
  - Outcome Evidence
  - Outcome Confirmation
  - Outcome Status
  - Progress Signal
non_owned_concepts: []
authoritative_responsibility: подтверждённые outcomes и их confirmation status.
key_invariants:
  - Recommendation shown не является outcome.
  - Booking created не равен service completed.
  - Confirmed outcome выше inference.
  - Outcome имеет source and timestamp.
  - Health outcome не превращается в diagnosis.
upstream_capabilities:
  - CAP-004
  - CAP-011
  - CAP-024
downstream_capabilities:
  - CAP-013
  - CAP-007
candidate_contexts:
  - Outcome Learning
  - Appointment
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§6.3"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое раздела не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§6–§7"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
open_questions: []
```

### 6.7. CAP-007 — Outcome Learning

```yaml
capability_id: CAP-007
canonical_name: Outcome Learning
name: Outcome Learning
status: identified
classification: core
characteristics: []
confidence: medium
evidence_status: partial
business_purpose: улучшать будущие решения на основе подтверждённых outcomes, feedback и patterns.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Learning Signal
  - Learning Eligibility
  - Model Feedback Record
  - Preference Update Proposal
  - Evaluation Cohort
  - Learning Version
non_owned_concepts: []
authoritative_responsibility: learning signals, их eligibility и learning versions.
key_invariants:
  - Learning signal имеет provenance.
  - Revoked/deleted data исключается.
  - Negative feedback не создаёт sensitive fact автоматически.
  - Training/evaluation use соответствует consent.
  - Изменение модели воспроизводимо.
upstream_capabilities:
  - CAP-006
  - CAP-013
  - CAP-012
downstream_capabilities:
  - CAP-004
  - CAP-001
candidate_contexts:
  - Outcome Learning
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§6.3, §15"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§7"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое раздела не верифицировано."
open_questions: []
```

### 6.8. CAP-008 — Service Catalog Management

```yaml
capability_id: CAP-008
canonical_name: Service Catalog Management
name: Service Catalog Management
status: identified
classification: supporting
characteristics: []
confidence: medium
evidence_status: partial
business_purpose: поддерживать каноническое представление услуг, категорий, атрибутов, ограничений и связей.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Service
  - Service Category
  - Service Attribute
  - Service Taxonomy
  - Service Restriction
  - Service Version
  - Canonical Service Mapping
non_owned_concepts: []
authoritative_responsibility: канонический каталог услуг, его taxonomy и версии.
key_invariants:
  - Stable service identity.
  - Provider offering не равна canonical service.
  - Inactive service не используется для новой записи.
  - Taxonomy change не переписывает history.
  - Display name не является identity.
upstream_capabilities: []
downstream_capabilities:
  - CAP-004
  - CAP-024
candidate_contexts:
  - Service Catalog
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§6.2–§6.3"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§4–§5"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
open_questions: []
```

### 6.9. CAP-009 — Provider and Specialist Management

```yaml
capability_id: CAP-009
canonical_name: Provider and Specialist Management
name: Provider and Specialist Management
status: identified
classification: supporting
characteristics: []
confidence: medium
evidence_status: partial
business_purpose: управлять идентичностью, профилем, квалификациями, отношениями с салоном и статусом специалистов/providers.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Provider
  - Specialist
  - Salon
  - Membership
  - Qualification
  - Verification Status
  - Provider Status
  - Service Offering
non_owned_concepts: []
authoritative_responsibility: идентичность, квалификации и статусы providers/specialists.
key_invariants:
  - Provider и Specialist различаются.
  - Qualification имеет source.
  - Inactive provider не принимает запись.
  - Profile не владеет availability.
  - Rating не равен qualification.
  - Commercial status не меняет organic recommendation.
upstream_capabilities: []
downstream_capabilities:
  - CAP-004
  - CAP-010
  - CAP-024
candidate_contexts:
  - Specialist and Provider Management
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§6.2–§6.3, §11"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§4–§5"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
open_questions:
  - "Где authoritative provider verification status (см. §11)."
```

---

### 6.10. CAP-010 — Availability Management

```yaml
capability_id: CAP-010
canonical_name: Availability Management
name: Availability Management
status: identified
classification: supporting
characteristics: []
confidence: medium
evidence_status: partial
business_purpose: поддерживать достоверное представление доступных интервалов, рабочих правил и ограничений ресурсов.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Schedule
  - Availability Window
  - Slot
  - Block
  - Working Rule
  - Resource Constraint
  - Availability Version
non_owned_concepts: []
authoritative_responsibility: availability windows, slots и working rules.
key_invariants:
  - Slot проверяется при commit booking.
  - Displayed slot не reservation.
  - Timezone semantics определены.
  - Ресурс не double-booked.
  - Manual block приоритетен.
  - Availability не владеет appointment lifecycle.
upstream_capabilities:
  - CAP-009
downstream_capabilities:
  - CAP-011
  - CAP-004
candidate_contexts:
  - Availability and Scheduling
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§6.2–§6.3"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§4–§5"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
open_questions: []
```

### 6.11. CAP-011 — Appointment Management

```yaml
capability_id: CAP-011
canonical_name: Appointment Management
name: Appointment Management
status: identified
classification: supporting
characteristics: []
confidence: medium
evidence_status: partial
business_purpose: создавать, подтверждать, изменять, переносить, отменять и завершать записи.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Appointment
  - Booking Draft
  - Status
  - Participant
  - Appointment Change
  - Cancellation
  - No-show
  - Completion
non_owned_concepts: []
authoritative_responsibility: Appointment и его status transitions.
key_invariants:
  - Confirmed appointment требует valid slot.
  - Failed eligibility блокирует.
  - Reschedule сохраняет origin.
  - Cancellation не удаляет history.
  - Recommendation acceptance не равна confirmation.
  - External response reconciled.
upstream_capabilities:
  - CAP-004
  - CAP-010
  - CAP-022
downstream_capabilities:
  - CAP-023
  - CAP-021
  - CAP-006
candidate_contexts:
  - Appointment Management
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§2, §6.3"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§4, §6"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
open_questions: []
```

### 6.12. CAP-012 — Feedback Collection

```yaml
capability_id: CAP-012
canonical_name: Feedback Collection
name: Feedback Collection
status: identified
classification: supporting
characteristics: []
confidence: medium
evidence_status: partial
business_purpose: получать структурированную и свободную обратную связь о recommendation, appointment, provider, service и результате.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Feedback
  - Feedback Target
  - Feedback Type
  - Rating
  - Review
  - Moderation Status
  - Provenance
non_owned_concepts: []
authoritative_responsibility: feedback records, их provenance и moderation status.
key_invariants:
  - Feedback связан с автором и target.
  - Rating не равен outcome.
  - Sensitive text проходит policy.
  - Moderation сохраняет audit trail.
upstream_capabilities:
  - CAP-011
  - CAP-004
downstream_capabilities:
  - CAP-007
  - CAP-025
candidate_contexts:
  - Feedback Collection
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§6.3"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое раздела не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§7"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое раздела не верифицировано."
open_questions: []
```

### 6.13. CAP-013 — Recommendation Attribution

```yaml
capability_id: CAP-013
canonical_name: Recommendation Attribution
name: Recommendation Attribution
status: identified
classification: core
characteristics:
  - governance
confidence: medium
evidence_status: partial
business_purpose: определять проверяемую связь между recommendation и qualified action.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Attribution
  - Attribution Type
  - Attribution Window
  - Registry Version
  - Linkage Type
  - Winning Recommendation
  - Status
non_owned_concepts: []
authoritative_responsibility: attribution records и winning recommendation для qualified action.
key_invariants:
  - Temporal proximity недостаточна.
  - Один action имеет не более одной winning recommendation.
  - Rejected/invalidated не атрибутируется.
  - Alternative использует собственный id.
  - Registry version сохраняется.
  - Ambiguity означает unattributed.
upstream_capabilities:
  - CAP-004
  - CAP-006
downstream_capabilities:
  - CAP-007
  - CAP-025
candidate_contexts:
  - Attribution
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§8"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое раздела не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§6–§7"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
open_questions:
  - "Как соотносятся Attribution и Product Measurement (см. §11)."
```

### 6.14. CAP-014 — Safety Policy Enforcement

```yaml
capability_id: CAP-014
canonical_name: Safety Policy Enforcement
name: Safety Policy Enforcement
status: identified
classification: supporting
characteristics:
  - governance
confidence: medium
evidence_status: partial
business_purpose: предотвращать unsafe recommendations, запрещённую обработку чувствительных данных и actions за пределами scope.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Safety Rule
  - Classification
  - Gate
  - Decision
  - Refusal Type
  - Quarantine
  - Escalation
  - Safety Incident
non_owned_concepts: []
authoritative_responsibility: safety rules, gates и quarantine decisions.
key_invariants:
  - Versioned safety rules.
  - Consumer не ослабляет mandatory rule.
  - Quarantined data не используется.
  - LLM не обходит deterministic gates.
  - Failure mandatory check блокирует action.
upstream_capabilities: []
downstream_capabilities:
  - CAP-004
  - CAP-001
  - CAP-016
  - CAP-018
candidate_contexts:
  - Safety Policy
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§6, §15"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§5, §8, §12"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
open_questions:
  - "Граница Safety Policy / Knowledge Governance — tracked in Ayla Domain Context Map §5.26; разделение safety rules между knowledge, core и consumer — см. §11."
```

### 6.15. CAP-015 — Knowledge Governance

```yaml
capability_id: CAP-015
canonical_name: Knowledge Governance
name: Knowledge Governance
status: identified
classification: supporting
characteristics:
  - governance
  - platform
confidence: medium
evidence_status: partial
business_purpose: управлять каноническими знаниями, версиями, authority, provenance, dependencies и публикацией artifacts.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Knowledge Node
  - Canonical Status
  - Knowledge Version
  - Authority
  - Dependency
  - Supersession
  - Source Manifest
  - Validation Result
  - Release Bundle
non_owned_concepts: []
authoritative_responsibility: канонические knowledge nodes, их версии и canonical status.
key_invariants:
  - Freshness не даёт authority.
  - Draft не approved.
  - Filename/node_id стабильны.
  - Supersession явный.
  - Mirror не владеет source.
  - Conflict не решается молча.
  - Breaking policy change versioned.
upstream_capabilities: []
downstream_capabilities:
  - CAP-014
  - CAP-027
candidate_contexts:
  - Knowledge Governance
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§15"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое раздела не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§10–§12"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
open_questions: []
```

### 6.16. CAP-016 — Conversation Experience

```yaml
capability_id: CAP-016
canonical_name: Conversation Experience
name: Conversation Experience
status: identified
classification: supporting
characteristics:
  - platform
confidence: medium
evidence_status: partial
business_purpose: обеспечивать последовательное multi-turn и multi-channel взаимодействие, передавая доменные intents owning capabilities.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Conversation
  - Turn
  - Message
  - Channel Session
  - Dialogue State
  - Presentation Context
  - Handoff
non_owned_concepts: []
authoritative_responsibility: conversation, turns и dialogue state (не authoritative memory).
key_invariants:
  - Transcript не authoritative memory.
  - Domain command идёт owner capability.
  - Channel format не меняет meaning.
  - History truncation не меняет confirmed state.
  - Conversation не владеет recommendation lifecycle.
upstream_capabilities:
  - CAP-018
  - CAP-005
downstream_capabilities:
  - CAP-003
candidate_contexts:
  - Conversation Experience
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§1, §6.4"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§4–§6"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
open_questions:
  - "Conversation Experience — bounded context или application/platform layer (см. §11)."
```

### 6.17. CAP-017 — Memory Retrieval and Rendering

```yaml
capability_id: CAP-017
canonical_name: Memory Retrieval and Rendering
name: Memory Retrieval and Rendering
status: identified
classification: supporting
characteristics:
  - platform
confidence: medium
evidence_status: partial
business_purpose: получать разрешённые facts из authoritative sources и формировать bounded memory block для runtime.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Retrieval Request
  - Memory Block
  - Retrieval Policy
  - Context Budget
  - Redaction Result
  - Rendered Fact Reference
non_owned_concepts: []
authoritative_responsibility: retrieval requests и rendered memory blocks (не backend facts).
key_invariants:
  - Retrieval не создаёт facts.
  - Consent/purpose gates до rendering.
  - Provenance сохраняется.
  - Sensitive data redacted.
  - Token truncation не меняет semantic status.
  - Platform не владеет backend facts.
upstream_capabilities:
  - CAP-001
  - CAP-002
downstream_capabilities:
  - CAP-018
candidate_contexts:
  - Memory Management
  - AI Platform
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§1, §6.1"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§5–§8"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
open_questions:
  - "Граница Memory Management / AI Platform — часть вопроса Personal Context and Memory Management, tracked in Ayla Domain Context Map §5.26."
```

### 6.18. CAP-018 — AI Orchestration and Tool Execution

```yaml
capability_id: CAP-018
canonical_name: AI Orchestration and Tool Execution
name: AI Orchestration and Tool Execution
status: identified
classification: technical-capability
characteristics:
  - platform
confidence: medium
evidence_status: partial
business_purpose: координировать AI-цикл, безопасно вызывать domain tools и возвращать результат в channel.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Orchestration Run
  - Tool Call
  - Tool Result
  - Dispatch Decision
  - Execution Trace
  - Model Interaction
  - Retry Policy
non_owned_concepts: []
authoritative_responsibility: orchestration runs, tool calls и execution traces (не доменные факты).
key_invariants:
  - Tool schema имеет owner.
  - Orchestrator не обходит invariant.
  - Side effect idempotent.
  - Model output не action до confirmation.
  - Replay детерминируем.
  - Adapter не меняет semantics.
  - Cross-tenant leakage запрещена.
upstream_capabilities:
  - CAP-017
downstream_capabilities:
  - CAP-003
  - CAP-004
  - CAP-016
  - CAP-026
candidate_contexts:
  - AI Platform
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§6.3"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое раздела не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§5"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое раздела не верифицировано."
open_questions:
  - "Кто owner machine-readable tool schemas при конфликте consumers (см. §11)."
```

---

### 6.19. CAP-019 — Identity and Access

```yaml
capability_id: CAP-019
canonical_name: Identity and Access
name: Identity and Access
status: identified
classification: generic
characteristics:
  - governance
confidence: medium
evidence_status: partial
business_purpose: управлять identity, authentication и authorization пользователей, специалистов, сотрудников и system actors.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Identity
  - Account
  - Credential
  - Role
  - Permission
  - Session
  - Access Decision
  - Tenant Membership
non_owned_concepts: []
authoritative_responsibility: identities, credentials и access decisions.
key_invariants:
  - Authentication ≠ authorization.
  - Tenant isolation.
  - Privileged action требует permission.
  - Service identity отдельно.
  - Shared privileged credential запрещён.
upstream_capabilities: []
downstream_capabilities:
  - CAP-016
  - CAP-018
candidate_contexts:
  - Identity and Access
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§11–§12"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§8"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое раздела не верифицировано."
open_questions: []
```

### 6.20. CAP-020 — Tenant and Product Configuration

```yaml
capability_id: CAP-020
canonical_name: Tenant and Product Configuration
name: Tenant and Product Configuration
status: identified
classification: supporting
characteristics:
  - platform
confidence: medium
evidence_status: partial
business_purpose: управлять versioned configuration для tenant, продукта, channel и policy-controlled behavior.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Tenant
  - Product Configuration
  - Feature Flag
  - Configuration Version
  - Policy Override Request
  - Experiment Assignment
  - Release Configuration
non_owned_concepts: []
authoritative_responsibility: versioned tenant/product configuration.
key_invariants:
  - Tenant config не нарушает Constitution.
  - Safety/privacy не отключаются flag.
  - Config version сохраняется.
  - Secret не business config.
  - Default safe.
upstream_capabilities:
  - CAP-015
downstream_capabilities:
  - CAP-018
  - CAP-016
candidate_contexts:
  - Tenant and Product Configuration
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§12–§15"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§5, §12"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
open_questions: []
```

### 6.21. CAP-021 — Notification Coordination

```yaml
capability_id: CAP-021
canonical_name: Notification Coordination
name: Notification Coordination
status: identified
classification: supporting
characteristics: []
confidence: medium
evidence_status: partial
business_purpose: планировать и координировать уведомления согласно consent, channel preference и product policy.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Notification Intent
  - Schedule
  - Delivery Preference
  - Status
  - Suppression Rule
  - Template Reference
non_owned_concepts: []
authoritative_responsibility: notification intents, schedules и suppression rules (не transport delivery).
key_invariants:
  - Intent отличается от transport.
  - Marketing/transactional consent разный.
  - Suppression соблюдается.
  - Duplicate event не создаёт duplicate message.
  - Timezone/quiet hours учитываются.
upstream_capabilities:
  - CAP-011
  - CAP-002
downstream_capabilities: []
candidate_contexts:
  - Notification Delivery
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§6.3–§6.4"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§4"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое раздела не верифицировано."
open_questions:
  - "Следует ли Notification Coordination отделить от transport delivery (см. §11)."
```

### 6.22. CAP-022 — Billing Eligibility

```yaml
capability_id: CAP-022
canonical_name: Billing Eligibility
name: Billing Eligibility
status: identified
classification: supporting
characteristics: []
confidence: medium
evidence_status: partial
business_purpose: определять, может ли provider принимать новые записи с учётом subscription, debt и business policies.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Subscription
  - Billing Account
  - Eligibility Decision
  - Eligibility Reason
  - Billing Status
  - Grace Period
non_owned_concepts: []
authoritative_responsibility: eligibility decisions и billing status providers.
key_invariants:
  - Decision versioned and explainable.
  - Appointment не владеет billing state.
  - Recommendation не обходит failure.
  - Reason codes стабильны.
  - Temporary debt не меняет history.
upstream_capabilities: []
downstream_capabilities:
  - CAP-011
  - CAP-004
candidate_contexts:
  - Billing and Eligibility
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§11–§14"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§11.5"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое раздела не верифицировано."
open_questions:
  - "Граница Billing / Payment Processing (ledger, коммерческое обязательство) — tracked in Ayla Domain Context Map §5.26."
```

### 6.23. CAP-023 — Payment Processing

```yaml
capability_id: CAP-023
canonical_name: Payment Processing
name: Payment Processing
status: identified
classification: generic
characteristics: []
confidence: low
evidence_status: partial
business_purpose: инициировать, подтверждать, отменять и reconciliate денежные операции.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Payment
  - Payment Attempt
  - Payment Status
  - Refund
  - Provider Transaction
  - Reconciliation
  - Money Amount
  - Currency
non_owned_concepts: []
authoritative_responsibility: payment operations, их statuses и reconciliation.
key_invariants:
  - Callback verified.
  - Operation idempotent.
  - Amount сохраняет currency.
  - Refund не удаляет original.
  - Payment success не создаёт appointment без contract.
  - Internal status reconciled.
upstream_capabilities:
  - CAP-011
downstream_capabilities:
  - CAP-022
candidate_contexts:
  - Payment Processing
mvp_scope: out
platform_scope: in
activation_status: deferred
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§11–§14"
    claim: "Business-model разделы обосновывают необходимость платёжных операций (traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано)."
  - source: "Ayla business model и backend payment contracts (вне этого vault)"
    section: "n/a"
    claim: "Требуются по owner direction OD-CAP-4; конкретные документы ещё не приложены как evidence."
open_questions:
  - "Приложить конкретные business model / backend contract документы как evidence."
  - "Прежняя трассировка v1.0 на Killer PRD §9 удалена: §9 — раздел «вне scope» и не является evidence (OD-CAP-4, см. §4.6)."
```

### 6.24. CAP-024 — Marketplace Search and Discovery

```yaml
capability_id: CAP-024
canonical_name: Marketplace Search and Discovery
name: Marketplace Search and Discovery
status: identified
classification: supporting
characteristics: []
confidence: medium
evidence_status: partial
business_purpose: позволять находить услуги и специалистов по критериям, когда personalization отсутствует, недостаточна или не выбрана пользователем.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Search Query
  - Search Filter
  - Search Result Set
  - Sort Policy
  - Search Facet
  - Discovery Session
non_owned_concepts: []
authoritative_responsibility: search queries, result sets и sort policies.
key_invariants:
  - Search result не recommendation.
  - Sponsored placement маркируется.
  - Commission не скрывает organic options.
  - Filters используют canonical attributes.
  - Ranking versioned.
  - Safe fallback не выбирает random/highest-commission provider.
upstream_capabilities:
  - CAP-008
  - CAP-009
  - CAP-010
downstream_capabilities:
  - CAP-011
  - CAP-006
candidate_contexts:
  - Marketplace Discovery
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§2, §5–§6"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§5.3"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое раздела не верифицировано."
open_questions:
  - "Marketplace Search — отдельный context или часть Catalog/Recommendation (см. §11)."
```

### 6.25. CAP-025 — Product Measurement and Experimentation

```yaml
capability_id: CAP-025
canonical_name: Product Measurement and Experimentation
name: Product Measurement and Experimentation
status: identified
classification: supporting
characteristics:
  - platform
  - governance
confidence: medium
evidence_status: partial
business_purpose: измерять outcomes, guardrails и experiments так, чтобы метрики отражали реальную полезность.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Metric Definition
  - Metric Version
  - Experiment
  - Cohort
  - Assignment
  - Guardrail
  - Exposure
  - Measurement Window
non_owned_concepts: []
authoritative_responsibility: metric definitions, experiments и guardrails.
key_invariants:
  - Metric versioned.
  - Invalidated recommendation исключается.
  - Experiment не отключает mandatory policy.
  - Metric gaming ограничен.
  - Historical data не переклассифицируется без migration.
upstream_capabilities:
  - CAP-006
  - CAP-013
downstream_capabilities:
  - CAP-027
candidate_contexts:
  - Measurement
  - Evaluation
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§8, §17"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§7"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое раздела не верифицировано."
open_questions:
  - "Нужен ли отдельный Evaluation context (см. §11)."
```

### 6.26. CAP-026 — Audit and Observability

```yaml
capability_id: CAP-026
canonical_name: Audit and Observability
name: Audit and Observability
status: identified
classification: supporting
characteristics:
  - governance
  - platform
confidence: medium
evidence_status: partial
business_purpose: обеспечивать traceability критичных решений, actions, policy checks, model releases и incidents без утечки sensitive context.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Audit Record
  - Trace
  - Alert
  - Incident
  - Incident Status
  - Release Quarantine
  - Recovery Approval
  - Redaction Policy
non_owned_concepts: []
authoritative_responsibility: audit records, traces и incidents.
key_invariants:
  - Sensitive context не попадает в alert без необходимости.
  - Audit immutable в пределах retention.
  - Trace связывает recommendation/tool/action.
  - Confirmed incident запускает containment.
  - Recovery требует evidence and approval.
upstream_capabilities:
  - CAP-018
  - CAP-014
downstream_capabilities:
  - CAP-027
candidate_contexts:
  - Observability
  - Governance
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§15"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое раздела не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§5.3, §8, §12.2"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
open_questions: []
```

### 6.27. CAP-027 — Decision Governance

```yaml
capability_id: CAP-027
canonical_name: Decision Governance
name: Decision Governance
status: identified
classification: supporting
characteristics:
  - governance
confidence: medium
evidence_status: partial
business_purpose: формализовать owner decisions, unresolved conflicts, amendments и breaking changes между продуктами и репозиториями.
business_outcome: null  # не сформулирован явно в v1.0
owned_concepts:
  - Decision Record
  - Decision Status
  - Decision Scope
  - Owner Ruling
  - Amendment
  - Breaking Change
  - Exception
  - Review Obligation
non_owned_concepts: []
authoritative_responsibility: decision records, их scope и status.
key_invariants:
  - Proposed не approved.
  - Decision имеет owner/scope.
  - Breaking change требует consumer impact review.
  - Exception имеет review trigger.
  - Local ADR не меняет cross-product canon вне scope.
  - Code/canon conflict фиксируется.
upstream_capabilities: []
downstream_capabilities:
  - CAP-015
candidate_contexts:
  - Knowledge Governance
  - Architecture Governance
mvp_scope: undetermined
introduced_by: undetermined  # происхождение не установлено: evidence v1.0 не верифицировано (см. §11)
evidence:
  - source: "[[Ayla Product Vision]]"
    section: "§16–§17"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
  - source: "[[Killer PRD]]"
    section: "§10–§12"
    claim: "Traceability-ссылка из v1.0 §13.3; содержимое разделов не верифицировано."
open_questions:
  - "Какая cross-repository policy регулирует breaking changes (см. §11)."
```

---

## 7. Capability Dependencies

Потоки перенесены из v1.0 (§8 исходного документа) без изменений; на их основе заполнены `upstream_capabilities` / `downstream_capabilities` записей §6.

### 7.1. Primary user-value flow

```text
Conversation Experience
        ↓
Intent Understanding
        ↓
Consent Check
        ↓
Personal Context Retrieval
        ↓
Recommendation Formation
        ↓
Explanation and Context Attribution
        ↓
User Decision
        ↓
Search / Appointment / Other Qualified Action
        ↓
Outcome Capture
        ↓
Recommendation Attribution
        ↓
Outcome Learning
```

### 7.2. Marketplace execution flow

```text
Service Catalog
        +
Provider Management
        +
Availability Management
        +
Billing Eligibility
        ↓
Recommendation or Search
        ↓
Appointment Management
        ↓
Payment Processing
        ↓
Notification Coordination
        ↓
Outcome Capture
```

### 7.3. Trust enforcement flow

```text
Constitution
        ↓
Consent Management
        +
Safety Policy
        +
Knowledge Governance
        +
Decision Governance
        ↓
Personal Context / Recommendation / Conversation / Learning / Measurement
```

### 7.4. AI runtime flow

```text
Backend Authoritative Facts
        ↓
Memory Retrieval and Rendering
        ↓
AI Orchestration
        ↓
Intent / Recommendation / Domain Tools
        ↓
Conversation Presentation
        ↓
Audit and Observability
```

### 7.5. Dependency rules

1. Downstream capability не получает ownership upstream state.
2. Capability использует только опубликованный contract.
3. Synchronous dependency обосновывается invariant.
4. Eventual consistency не применяется к immediate safety/eligibility decision.
5. Circular semantic ownership запрещён.
6. Bidirectional data flow допустим, но ownership остаётся ясным.

---

## 8. Capability–Context Reconciliation

Reconciliation показывает, где предположительно реализуется семантика capability, но не определяет физический deployment и не подтверждает bounded contexts (см. §3.1). Mapping перенесён из v1.0 §9.2; колонка resolution отражает текущее состояние согласования.

Возможные значения resolution:

- `maps-to-one-context` — исходный mapping даёт один candidate context без открытых противоречий;
- `maps-to-shared-context` — несколько capabilities reconcile в один общий candidate context;
- `cross-cutting-policy` — capability остаётся сквозной политикой;
- `technical-capability` — запись переклассифицирована как technical capability;
- `deferred` — активация отложена (вне MVP scope);
- `unresolved` — исходный документ не даёт достаточных оснований для выбора.

| Capability ID | Capability | Candidate context(s) | Resolution |
|---|---|---|---|
| CAP-001 | Personal Context Management | Personal Context / Memory Management / Consent Management | unresolved |
| CAP-002 | Consent Management | Consent Management | maps-to-one-context |
| CAP-003 | Intent Understanding | Intent Understanding | maps-to-one-context |
| CAP-004 | Recommendation Formation | Recommendation | maps-to-shared-context |
| CAP-005 | Explanation and Context Attribution | Recommendation | maps-to-shared-context |
| CAP-006 | Outcome Capture | Outcome Learning / Appointment | unresolved |
| CAP-007 | Outcome Learning | Outcome Learning | maps-to-one-context |
| CAP-008 | Service Catalog Management | Service Catalog | maps-to-one-context |
| CAP-009 | Provider and Specialist Management | Specialist and Provider Management | maps-to-one-context |
| CAP-010 | Availability Management | Availability and Scheduling | maps-to-one-context |
| CAP-011 | Appointment Management | Appointment Management | maps-to-one-context |
| CAP-012 | Feedback Collection | Feedback Collection | maps-to-one-context |
| CAP-013 | Recommendation Attribution | Attribution | maps-to-one-context |
| CAP-014 | Safety Policy Enforcement | Safety Policy | maps-to-one-context |
| CAP-015 | Knowledge Governance | Knowledge Governance | maps-to-one-context |
| CAP-016 | Conversation Experience | Conversation Experience | maps-to-one-context |
| CAP-017 | Memory Retrieval and Rendering | Memory Management / AI Platform | unresolved |
| CAP-018 | AI Orchestration and Tool Execution | AI Platform | technical-capability |
| CAP-019 | Identity and Access | Identity and Access | maps-to-one-context |
| CAP-020 | Tenant and Product Configuration | Tenant and Product Configuration | maps-to-one-context |
| CAP-021 | Notification Coordination | Notification Delivery | maps-to-one-context |
| CAP-022 | Billing Eligibility | Billing and Eligibility | maps-to-one-context |
| CAP-023 | Payment Processing | Payment Processing | deferred |
| CAP-024 | Marketplace Search and Discovery | Marketplace Discovery | maps-to-one-context |
| CAP-025 | Product Measurement and Experimentation | Measurement / Evaluation | unresolved |
| CAP-026 | Audit and Observability | Observability / Governance | unresolved |
| CAP-027 | Decision Governance | Knowledge Governance / Architecture Governance | unresolved |

Примечания:

1. По owner direction: Recommendation Formation (CAP-004), Explanation and Context Attribution (CAP-005), а также аспекты recommendation integrity и organic neutrality enforcement внутри CAP-004 reconcile в один candidate context **Recommendation**. В v1.0 для CAP-004 также указывались candidates Safety Policy и Attribution — они сохранены в записи §6.4 как гипотезы, но reconciliation фиксирует shared context Recommendation.
2. Mapping constraints v1.0 сохраняются: один bounded context может реализовывать несколько cohesive capabilities; одна capability может требовать нескольких contexts при явном разделении; shared database не доказывает общий context; shared library не создаёт shared semantic ownership; repository boundary не равна context boundary; один термин не имеет двух authoritative meanings без translation.
3. Resolution `unresolved` разрешается через Context Boundary Review по правилам [[Ayla Domain Context Map]]; соответствующие consolidation questions трекются в Ayla Domain Context Map §5.26.

---

## 9. MVP Scope Matrix

MVP scope фиксируется только там, где исходный документ или ссылки на Killer PRD / owner directions это явно определяют. Для остальных записей scope не определён источниками v1.0 и помечен `undetermined` до сверки с [[Ayla MVP Product Thesis]] в ходе evidence verification.

| Capability ID | mvp_scope | platform_scope | activation_status | Основание |
|---|---|---|---|---|
| CAP-001 | undetermined | — | — | — |
| CAP-002 | undetermined | — | — | — |
| CAP-003 | undetermined | — | — | — |
| CAP-004 | undetermined | — | — | — |
| CAP-005 | undetermined | — | — | — |
| CAP-006 | undetermined | — | — | — |
| CAP-007 | undetermined | — | — | — |
| CAP-008 | undetermined | — | — | — |
| CAP-009 | undetermined | — | — | — |
| CAP-010 | undetermined | — | — | — |
| CAP-011 | undetermined | — | — | — |
| CAP-012 | undetermined | — | — | — |
| CAP-013 | undetermined | — | — | — |
| CAP-014 | undetermined | — | — | — |
| CAP-015 | undetermined | — | — | — |
| CAP-016 | undetermined | — | — | — |
| CAP-017 | undetermined | — | — | — |
| CAP-018 | undetermined | — | — | — |
| CAP-019 | undetermined | — | — | — |
| CAP-020 | undetermined | — | — | — |
| CAP-021 | undetermined | — | — | — |
| CAP-022 | undetermined | — | — | — |
| CAP-023 | out | in | deferred | Owner direction OD-CAP-4: Payment Processing остаётся в реестре, вне MVP scope, в platform scope, активация отложена |
| CAP-024 | undetermined | — | — | — |
| CAP-025 | undetermined | — | — | — |
| CAP-026 | undetermined | — | — | — |
| CAP-027 | undetermined | — | — | — |

---

## 10. Evidence Coverage Matrix

Сводное состояние evidence по правилам §4.5. Ни одна запись не имеет `complete`: все traceability-ссылки v1.0 не верифицированы против содержимого источников.

| Capability ID | evidence_status | confidence | Комментарий |
|---|---|---|---|
| CAP-001 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-002 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-003 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-004 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-005 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-006 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-007 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-008 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-009 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-010 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-011 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-012 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-013 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-014 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-015 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-016 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-017 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-018 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-019 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-020 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-021 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-022 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-023 | partial | low | Только PV (business model); Killer PRD §9 удалён из evidence (OD-CAP-4); backend contracts не приложены |
| CAP-024 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-025 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-026 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |
| CAP-027 | partial | medium | PV + Killer PRD ссылки из v1.0 §13.3, не верифицированы |

---

## 11. Open Questions

Вопросы границ контекстов, пересекающиеся с consolidation questions Domain Context Map, здесь не дублируются — они трекются в [[Ayla Domain Context Map]] §5.26:

- Personal Context and Memory Management (граница с Consent Management, ownership контента, retention, retrieval, deletion);
- Intent Understanding and Recommendation;
- Recommendation, Attribution and Outcome Learning;
- Conversation Experience and AI Orchestration;
- Knowledge Governance and Safety Policy;
- Specialist Management, Availability and Appointment;
- Billing and Payment Processing.

Capability-специфичные открытые вопросы реестра, сгруппированные по типам (нумерация v1.1 сохранена):

### Architecture

1. Где граница Recommendation Formation (CAP-004) и Explanation (CAP-005) внутри shared candidate context Recommendation?
2. Outcome Capture (CAP-006) и Outcome Learning (CAP-007) — один context или два (связано с Context Map §5.26 «Recommendation, Attribution and Outcome Learning»)?
3. Conversation Experience (CAP-016) — bounded context или application/platform layer?
4. Кто owner machine-readable tool schemas (CAP-018) при конфликте consumers?
5. Где заканчивается prompt canon и начинается runtime prompt assembly?
6. Какой context владеет proactive trigger scheduling?
7. Marketplace Search (CAP-024) — отдельный context или часть Catalog/Recommendation?
8. Нужен ли отдельный Evaluation context (CAP-025)?
9. Как соотносятся Attribution (CAP-013) и Product Measurement (CAP-025)?
10. Где authoritative provider verification status (CAP-009)?
12. Как синхронно обновляются library pins в consumers?
17. Следует ли Notification Coordination (CAP-021) отделить от transport delivery?

### Product

18. Как формализовать proactive habit support без преждевременного проектирования?
19. Явные `business_outcome` отсутствуют в v1.0 для CAP-003…CAP-027 — заполняются при evidence verification (см. §4.5).
20. Какие конкретные business model / backend contract документы прикладываются как evidence для CAP-023 (см. §4.6)?

### Privacy

11. Кто владеет Consent Scope Registry (CAP-002)?
14. Как разделяются safety rules (CAP-014) между knowledge, core и consumer?
16. Нужен ли Privacy Operations context для DSAR/deletion/retention?

### Governance

13. Какая cross-repository policy регулирует breaking changes (CAP-027)?
15. Какой repository станет canonical owner backend contracts?
21. `introduced_by` всех записей — `undetermined`: происхождение capabilities не верифицировано (evidence v1.0 не проверено); заполняется при evidence verification по правилу §5 (п. 10).

---

## 12. Acceptance Criteria

Документ готов к approval, когда:

1. Утверждены обязательные predecessor documents по AYLA-DEC-0011 (см. §3.1).
2. Все P0 product flows покрыты capabilities.
3. Каждая capability имеет stable identifier.
4. Определены purpose и outcome для каждой записи.
5. Определены owned/non-owned concepts.
6. Для policy capabilities есть enforceable invariants.
7. Все capabilities имеют verified evidence; Evidence Coverage Matrix не содержит `missing`.
8. Классификация каждой записи — ровно одна категория Domain Context Map; characteristics используются только как `governance`/`platform`.
9. Отражены critical privacy/safety dependencies.
10. Capability–Context Reconciliation не содержит `unresolved` без owner decision или открытого вопроса.
11. MVP Scope Matrix сверена с Ayla MVP Product Thesis.
12. Conflicts вынесены в open questions.
13. Product Vision и Killer PRD трассируются до реестра с верифицированными ссылками.
14. Ни один context не подтверждён только по repository/module.
15. Validator принимает документ.

---

## 13. Change Log

### v1.2 — 2026-07-27

Пять P1-изменений по рекомендациям владельца (документ принят как draft, перед будущей канонизацией):

- добавлен §1.4 Registry lifecycle: `identified → under-review → approved → active → deprecated → retired`; enum `status` в схеме §5 приведён к этой терминологии (прежние `confirmed` / `requires-split` / `requires-merge` / `rejected` из статусной модели реестра убраны);
- добавлен §5.1 «Контракт неизменяемости Capability ID»: идентификатор никогда не переиспользуется, постоянен после публикации даже при переименовании, при удалении capability статус становится `retired`, а идентификатор резервируется навсегда;
- в схему §5 и во все 27 записей добавлено поле `introduced_by` (`{source: ..., version: ...}` / `{decision: AYLA-DEC-####}` / `undetermined`); для всех текущих записей — `undetermined`, так как evidence v1.0 не верифицировано (open question №21, §11);
- в схему §5 и во все 27 записей добавлены `canonical_name` (стабильное имя для междокументных ссылок, для текущих записей совпадает с `name`) и опциональный `display_name` (заполняется только при отличии; сейчас отличий нет); идентификаторы сохранены в формате `CAP-###`;
- §11 Open Questions разделён по типам: Architecture / Product / Privacy / Governance; нумерация вопросов v1.1 сохранена.

### v1.1 — 2026-07-27

Переработка по owner directions OD-CAP-1..4:

- документ переименован из `Ayla Domain Capability Specification` в `Ayla Domain Capability Registry`; node_id обновлён до `ayla.foundation.domain-capability-registry`;
- документ repositioned как реестр capabilities, принадлежащий Product Architecture, отвечающий на три вопроса (нужная способность, бизнес-результат, candidate context); DDD-методология удалена и возвращена в [[Ayla Domain Context Map]] (бывшие §4 Capability Extraction Principles, §5 Capability Classification, §10 Capability Review Rules, §12 Capability Evolution Rules);
- классификация приведена к единой схеме Domain Context Map: одна категория на запись (`core` / `supporting` / `generic` / `technical-capability`), `governance` и `platform` переведены в characteristics; multi-classification упразднена;
- Capability Record сокращён до схемы §5; lifecycle, commands и events вынесены на уровень bounded context / domain specification;
- добавлены Capability–Context Reconciliation (§8), MVP Scope Matrix (§9) и Evidence Coverage Matrix (§10);
- зафиксирована позиция документа в цепочке AYLA-DEC-0011: Registry не выше Context Map и не может быть approved до predecessor documents (§3);
- CAP-023 Payment Processing: `mvp_scope: out`, `platform_scope: in`, `activation_status: deferred`; ошибочная трассировка на Killer PRD §9 удалена, evidence переведён на Product Vision / business model / backend contracts;
- confidence всех записей понижен до `medium`/`low`: traceability-ссылки v1.0 не верифицированы, `confidence: high` без evidence запрещён (§4.5);
- формат идентификаторов приведён к `CAP-###` (нумерация v1.0 сохранена);
- open questions разделены: context-boundary дубли сосланы на Ayla Domain Context Map §5.26, capability-специфичные сохранены в §11.

### v1.0 — 2026-07-27

- создана первая полная версия Domain Capability Specification;
- определены scope, evidence и extraction rules;
- введён Capability Record Standard;
- зафиксированы 27 candidate capabilities;
- добавлены relationships и mapping;
- добавлены review/evolution/breaking-change rules;
- создана initial traceability matrix;
- зафиксированы open questions.

---

## 14. Approval

**Status:** Draft — pending domain, product, privacy and safety review. Approval невозможен до утверждения обязательных predecessor documents по AYLA-DEC-0011 (см. §3.1).

Для approval необходимы:

- Product Owner review;
- Product Architecture review;
- Privacy review;
- Safety review;
- сверка с User Journey и Intent Model Specification (planned predecessor);
- Context Boundary Review;
- отсутствие unresolved P0 contradictions.
