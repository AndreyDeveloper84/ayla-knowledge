---
node_id: ayla.domain.conversation-model

title: Ayla Conversation Model Specification
title_ru: Спецификация модели Conversation Ayla

type: domain-specification
status: draft
decision_status: proposed
canonical_status: candidate
version: "1.0"

owner: Domain Architecture
owners:
  - Product Owner
  - Domain Architecture

reviewers:
  - AI Architecture
  - Backend Architecture
  - Product Design
  - Privacy and Safety

knowledge_area:
  - domain-model
  - product
  - architecture

domain:
  - conversation

system_owner:
  - ayla-conversation

source_repository: ayla-knowledge
source_kind: canonical

classification: internal
data_sensitivity: none
security_sensitivity: low

ai_indexing: allowed
export_policy: full

updated: 2026-08-06
review_cycle: monthly

depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Product Vision]]"
  - "[[Ayla Repository Responsibility Matrix]]"
  - "[[Ayla Glossary]]"
  - "[[OWNER_DECISION_REGISTER]]"
  - "[[Ayla Intent Model Specification]]"
  - "[[Ayla Core Domain Model Specification]]"
  - "[[Ayla MVP Recommendation Contract]]"
  - "[[Consent Scope Registry]]"
  - "[[Ayla MVP User Journey Specification]]"
  - "[[Ayla Domain Context Map]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Ayla Decision Log]]"

related_documents:
  - Ayla Intent Model Specification
  - Ayla MVP User Journey Specification
  - Ayla Domain Context Map
  - Ayla Domain Capability Registry
  - ADR-0014 Conversation Context ID
  - AMD-020 C5 Pilot Personal Context Export-Forget Contract
---

# Ayla Conversation Model Specification

## 1. Статус и готовность

Этот документ — канонический черновик (`draft`, `proposed`) спецификации модели Conversation.
Текущая версия содержит Foundation (Wave 1) и Wave 2 — Core Concepts.
Foundation включает frontmatter, позиционирование, назначение, канонические принципы,
scope, зависимости, терминологию и правила использования терминов.
Wave 2 формализует ядро модели: Conversation, Session, Interaction, Dialogue Turn,
каноническую иерархию, кардинальность и модель идентичности.
Нормативные разделы lifecycle, состояния, контекста, projection, границ и дополнительных
инвариантов будут добавлены в последующих волнах письма спецификации.

## 2. Каноническая позиция

Conversation Model Specification является Source of Truth для следующих понятий
и областей в рамках продукта Ayla:

- Conversation;
- Session;
- Interaction;
- Dialogue Turn;
- Conversation Identity;
- Conversation Lifecycle (conceptual);
- conceptual Conversation State;
- Context Projection.

Этот документ не претендует на статус Source of Truth для Intent, Transformation Goal,
Recommendation, Memory, Consent, Runtime FSM, а также для доменных сущностей и авторитетных
backend-фактов. Соответствующие границы authority зафиксированы в решениях
AYLA-DEC-0055…AYLA-DEC-0062.

## 3. Назначение

Назначение Conversation Model — дать единую продуктовую модель, описывающую структуру,
идентичность, жизненный цикл и контекстное окружение пользовательских разговоров с Ayla.
Модель обеспечивает непрерывность пользовательского опыта, разделяет продуктовые понятия
и runtime-реализацию, а также определяет механизм проекции контекста в смежные домены
без поглощения чужих областей ответственности.

## 4. Канонические принципы

Foundation Conversation Model опирается на следующие принципы, зафиксированные
в решениях AYLA-DEC-0055…AYLA-DEC-0062:

- **Conversation ≠ Session.** Conversation — корневая продуктовая сущность; Session —
  самостоятельная каноническая сущность внутри Conversation, но не заменяет её.
- **Conversation ≠ Memory.** Conversation не владеет Memory и не является хранилищем
  долгосрочных фактов о пользователе.
- **Conversation ≠ Recommendation.** Conversation не владеет Recommendation и не
  определяет механизмы формирования рекомендаций.
- **Conversation owns only Conversation Context.** Conversation владеет только
  Conversation Context; все остальные данные предоставляются смежным доменам через
  Context Projection.
- **Runtime implements Conversation Model.** Runtime-реализация опирается на модель,
  но сама модель не описывает runtime-механики.
- **Conversation Model never defines runtime mechanics.** В документе не вводятся
  prompts, FSM, enum, API, tool dispatch, schema и storage-реализации.
- **Conversation Context is conceptual, not persistent storage.** Контекст определяется
  как концептуальное понятие; форматы хранения и передачи вынесены за пределы модели.
- **Ownership boundaries are authoritative.** Границы ответственности между
  Conversation Model и смежными доменами имеют приоритет над локальными
  переиспользованиями терминов.

## 5. Scope

### 5.1. Входит в scope (IN_SCOPE)

- Концептуальные определения сущностей Conversation Layer: Conversation, Session,
  Interaction, Dialogue Turn.
- Иерархия и кардинальности: Conversation → Session → Interaction → Dialogue Turn.
- Правила Conversation Identity.
- Концептуальные lifecycles сущностей Conversation Layer (без runtime FSM).
- Концептуальное Conversation State (без enum, state machine и storage-реализации).
- Conversation Context и Session Context как единственные данные, которыми владеет Conversation.
- Context Projection как механизм предоставления контекста смежным доменам.
- Инварианты и границы ответственности Conversation Model.

### 5.2. Вне scope (OUT_OF_SCOPE)

- Prompts, prompt assembly, orchestration graph, LLM routing.
- Tool dispatch implementation, retry/reconciliation mechanics.
- Database schema, API и runtime FSM.
- Точные форматы хранения, сериализации и передачи данных.
- Определение Intent, Transformation Goal, Recommendation, Memory, Consent,
  domain entities и авторитетных backend-фактов.

## 6. Non-goals

Этот документ не ставит целью:

- заменить Runtime Canon, Intent Model, Recommendation Contract, Memory Model,
  Consent Scope Registry или Core Domain Model;
- вводить технические implementation-решения;
- описывать UI/UX-взаимодействие вне рамок Conversation Layer;
- определять governance-процессы или процедуры change management.

## 7. Source of Truth

### 7.1. Conversation Model — Source of Truth

| Понятие / область | Owner |
|---|---|
| Conversation | Conversation Model Specification |
| Session | Conversation Model Specification |
| Interaction | Conversation Model Specification |
| Dialogue Turn | Conversation Model Specification |
| Conversation Identity | Conversation Model Specification |
| Conversation Lifecycle (conceptual) | Conversation Model Specification |
| conceptual Conversation State | Conversation Model Specification |
| Context Projection | Conversation Model Specification |

### 7.2. Conversation Model — не Source of Truth

| Понятие / область | Source of Truth |
|---|---|
| Intent | Ayla Intent Model Specification |
| Transformation Goal | Journey / canonical product concept |
| Recommendation | Ayla MVP Recommendation Contract |
| Memory | Memory Model (см. Core Domain Model, AMD-020) |
| Consent | Consent Scope Registry |
| Runtime FSM | Runtime Canon |
| Domain entities и authoritative backend facts | Ayla Core Domain Model Specification |

### 7.3. Чтение и проекция Conversation Model

Conversation Model не становится владельцем перечисленных ниже сущностей, но может
обращаться к ним в режиме чтения или формировать их projection-контексты:

| Операция | Сущности / области | Условие |
|---|---|---|
| **Reads** | Intent | Только чтение; owner — Ayla Intent Model Specification. |
| **Reads** | Transformation Goal | Только чтение; owner — Journey / canonical product concept. |
| **Reads** | Consent | Только чтение; owner — Consent Scope Registry. |
| **Reads** | Backend facts | Только через разрешённые механизмы; owner — Ayla Core Domain Model Specification. |
| **Projects** | Recommendation Context | Без передачи ownership; owner — Ayla MVP Recommendation Contract. |
| **Projects** | Runtime Context | Без передачи ownership; owner — Runtime Canon. |
| **Projects** | Memory Proposal Context | Без передачи ownership; owner — Memory Model. |

## 8. Зависимости

| Раздел / тема | Source of Truth / вход | Как используется |
|---|---|---|
| Позиционирование и scope | OWNER_DECISION_REGISTER (AYLA-DEC-0061, AYLA-DEC-0062) | Границы документа |
| Терминология Conversation Layer | AYLA-DEC-0057, AYLA-DEC-0058, Ayla Glossary | Канонические определения и alias-таблица |
| Иерархия и кардинальность | AYLA-DEC-0055, AYLA-DEC-0056 | Структура модели |
| Conversation Identity | AYLA-DEC-0055 | Правила идентичности |
| Conversation State | AYLA-DEC-0059 | Концептуальный характер состояния |
| Context и Projection | AYLA-DEC-0060 | Границы владения данными |
| Intent / Transformation Goal | Ayla Intent Model Specification, Ayla MVP User Journey Specification | Референсные домены, не определяются заново |
| Consent | Consent Scope Registry | Референс для projection-границ |
| Memory / backend facts | Ayla Core Domain Model Specification | Референс для projection-границ |

## 9. Терминология

### 9.1. Канонические термины

| Термин | Краткое определение |
|---|---|
| **Conversation** | Корневая продуктовая сущность, представляющая непрерывный разговор пользователя с Ayla вокруг одной или нескольких связанных целей. Conversation может включать несколько Session, Interaction и Dialogue Turn. |
| **Session** | Самостоятельная каноническая продуктовая сущность, представляющая операционную сессию общения внутри Conversation. Session имеет собственный концептуальный lifecycle и не сводится только к runtime-соединению. |
| **Interaction** | Логически связанный эпизод общения внутри Session, состоящий из одного или нескольких Dialogue Turn. Является каноническим термином для обозначения эпизода. |
| **Dialogue Turn** | Атомарная единица обмена репликами внутри Interaction. Каждый Turn принадлежит ровно одному Interaction. |
| **Conversation Context** | Контекст, которым владеет Conversation. Включает информацию, необходимую для поддержания непрерывности и смысловой целостности разговора. |
| **Session Context** | Контекст, ассоциированный с конкретной Session и входящий в состав Conversation Context. Не является самостоятельной канонической сущностью; существует только в пределах Conversation Context, которым владеет Conversation. |
| **Context Projection** | Механизм, с помощью которого данные из Conversation / Session Context предоставляются смежным доменам (Recommendation, Memory, Runtime, Consent и др.) без передачи ownership. |
| **Conversation State** | Концептуальное смысловое состояние разговора. В рамках Conversation Model не определяется как runtime FSM, enum или storage state machine. |
| **Continuity** | Свойство Conversation сохранять смысловую и контекстную связность между Session, Interaction и Dialogue Turn во времени и между каналами. |

### 9.2. Legacy aliases

Следующие варианты встречаются в существующих документах и рассматриваются как
исторические или поясняющие alias-ы. В новых материалах рекомендуется использовать
канонический термин.

| Legacy variant | Канонический термин | Статус |
|---|---|---|
| Interaction Episode | Interaction | LEGACY_ALIAS |
| Turn | Dialogue Turn | LEGACY_ALIAS |
| Conversation Turn | Dialogue Turn | LEGACY_ALIAS |
| Channel Session | Session | LEGACY_ALIAS |

### 9.3. Правила использования терминов

Во всей Knowledge Base при описании Conversation Layer применяются следующие правила:

| Используется как основной термин | Не используется как основной термин | Статус варианта |
|---|---|---|
| Interaction | Interaction Episode | LEGACY_ALIAS |
| Dialogue Turn | Turn | LEGACY_ALIAS |
| Dialogue Turn | Conversation Turn | LEGACY_ALIAS |
| Conversation State | Dialogue State | LEGACY_ALIAS |

Legacy-aliases допустимы только при обсуждении истории документа, миграции между
версиями модели или обеспечения совместимости с внешними системами. В новых
материалах, спецификациях, schema и runtime-контрактах используются только
канонические термины.

## 10. Core Model Overview

Модель Conversation состоит из четырёх канонических сущностей, образующих
продуктовую / доменную концептуальную иерархию:

```text
Conversation
    └── Session
            └── Interaction
                    └── Dialogue Turn
```

- **Conversation** — корневая сущность непрерывного разговора пользователя с Ayla.
- **Session** — самостоятельная операционная сессия общения внутри Conversation.
- **Interaction** — логически связанный эпизод общения внутри Session.
- **Dialogue Turn** — минимальная атомарная единица участия внутри Interaction.

Эта иерархия описывает продуктовое / доменное отношение принадлежности
(`belongs to`), а не физическое хранение, дерево БД или граф runtime-процессов.
Каждый уровень добавляет собственную абстракцию: Conversation отвечает за
непрерывность между сессиями и каналами, Session — за операционный период в
рамках канала, Interaction — за смысловую связность эпизода, Dialogue Turn —
за минимальную неделимую единицу обмена.

## 11. Conversation

### 11.1. Canonical definition

**Conversation** — корневая продуктовая сущность, представляющая непрерывный
разговор пользователя с Ayla вокруг одной или нескольких связанных целей.
Conversation сохраняет идентичность независимо от смены Session, канала, устройства
или временной паузы (AYLA-DEC-0055).

### 11.2. Responsibility

Conversation:

- задаёт продуктовую рамку диалога;
- обеспечивает непрерывность пользовательского опыта между Session, Interaction
  и Dialogue Turn;
- владеет только **Conversation Context** (AYLA-DEC-0060);
- выступает отправной точкой для **Context Projection** в смежные домены без
  передачи им ownership.

### 11.3. What establishes Conversation identity

Идентичность Conversation определяется смысловой непрерывностью
пользовательского взаимодействия и контекста, а не техническими характеристиками
соединения. Runtime-реализация реализует эти правила, но не определяет их
(AYLA-DEC-0055, AYLA-DEC-0061).

### 11.4. Relationship to Transformation Goal

Conversation может развиваться вокруг одной или нескольких связанных
Transformation Goal. Transformation Goal — канонический сквозной продуктовый
концепт; Conversation не владеет им и не является его доменным агрегатом.

Новая **независимая** Transformation Goal может инициировать новую Conversation,
но связанная подцель, уточнение или углубление в рамках текущей цели сами по
себе не обязаны создавать новую Conversation.

### 11.5. Relationship to Intent

Conversation может содержать и использовать intent-related context. Intent
интерпретируется внутри Conversation, но **Intent не является дочерней сущностью**
иерархии Conversation Model. Owner Intent — `Ayla Intent Model Specification`
(AYLA-DEC-0062).

### 11.6. Relationship to Session

Conversation включает ноль или более Session. Каждый Session принадлежит
ровно одной Conversation. Смена Session не разрывает Conversation; Conversation
может охватывать несколько Session во времени и между каналами.

### 11.7. What does NOT create a new Conversation

Следующие события сами по себе **не создают** новую Conversation:

- смена Session;
- смена канала;
- смена устройства;
- временная пауза;
- появление нового Interaction;
- появление нового Dialogue Turn;
- связанная подцель или уточнение в рамках текущей Transformation Goal.

### 11.8. What MAY create a new Conversation

В соответствии с AYLA-DEC-0055 новая Conversation может возникнуть, если:

1. пользователь начинает новую независимую Transformation Goal;
2. предыдущая Conversation завершена согласно Conversation Lifecycle;
3. владелец системы или пользователь явно инициирует новую Conversation
   согласно правилам Canon.

### 11.9. Explicitly not defined

В рамках Wave 2 не фиксируется runtime-алгоритм определения «тот же разговор».
Не вводятся эвристики, timeout, FSM или storage-реализация.

## 12. Session

### 12.1. Canonical definition

**Session** — самостоятельная каноническая продуктовая сущность,
представляющая операционную сессию общения внутри Conversation. Session имеет
собственный концептуальный lifecycle и не сводится только к runtime-соединению
(AYLA-DEC-0057).

### 12.2. Belongs to exactly one Conversation

Каждый Session принадлежит ровно одной Conversation. Session не является
глобальным владельцем Conversation и не может существовать вне Conversation.

### 12.3. Product identity

Session обладает собственной продуктовой идентичностью внутри Conversation.
Эта идентичность не заменяет идентичность Conversation и не зависит от
конкретного Dialogue Turn или Interaction.

### 12.4. Conceptual purpose

Session:

- ограничивает операционный период активности пользователя;
- несёт **Session Context** как часть **Conversation Context**, которым владеет
  Conversation;
- обеспечивает continuity внутри своего диапазона;
- является контейнером для нуля или более Interaction.

### 12.5. Channel-scoped nature

Session является channel-scoped: переход между каналами не означает продолжение
той же Session — в другом канале начинается новая Session. При этом Conversation
может продолжаться между каналами через разрешённую context projection
(AYLA-DEC-0055; Ayla MVP User Journey Specification v1.2 §Terminology).

### 12.6. Relationship to continuity

Смена Session не нарушает Conversation identity и не обрывает продуктовую
непрерывность. Session — единица continuity внутри Conversation, а не её
замена.

### 12.7. Relationship to Interaction

Session содержит ноль или более Interaction. Interaction не может
существовать вне Session.

### 12.8. Explicitly not defined

В рамках Wave 2 не описываются session timeout, transport connection,
token lifetime, storage implementation и прочие runtime-детали.

## 13. Interaction

### 13.1. Canonical definition

**Interaction** — логически связанный эпизод общения внутри Session,
состоящий из одного или нескольких Dialogue Turn. Interaction является
каноническим термином для обозначения такого эпизода (AYLA-DEC-0058).

### 13.2. Interaction = logically coherent episode

Interaction объединяет Dialogue Turn, относящиеся к одному смысловому поводу,
одному flow или одной задаче. Внутри Interaction допускаются уточнения,
коррекции и ответвления, пока они остаются в рамках одного связного эпизода.

### 13.3. Belongs to exactly one Session

Каждый Interaction принадлежит ровно одному Session. Interaction не может
переходить между Session и не может существовать вне Session.

### 13.4. Consists of one or more Dialogue Turn

Interaction состоит из одного или нескольких Dialogue Turn. Одиночный Dialogue
Turn может образовывать Interaction, если он сам по себе представляет
завершённый связный эпизод.

### 13.5. Why Interaction is not equal to Session

Session ограничивает операционный период / канал и может включать несколько
разных или последовательных эпизодов. Interaction — это смысловой эпизод внутри
этого периода. Один Session может содержать несколько Interaction; один
Interaction не охватывает несколько Session.

### 13.6. Why Interaction is not equal to Dialogue Turn

Dialogue Turn — атомарная единица обмена репликами. Interaction — это
совокупность Turn-ов, объединённых общей смысловой связностью. Interaction
добавляет уровень эпизода, которого нет у отдельного Turn.

### 13.7. Legacy alias

`Interaction Episode` сохраняется только как legacy alias. В новых материалах
используется канонический термин **Interaction**.

## 14. Dialogue Turn

### 14.1. Canonical definition

**Dialogue Turn** — минимальная атомарная единица участия в Conversation
внутри одного Interaction. Dialogue Turn является минимальной продуктовой
единицей разговора.

### 14.2. Minimum conversation unit

Dialogue Turn фиксирует одну атомарную единицу участия внутри Interaction.
Turn не обязан означать пару `сообщение пользователя + ответ Ayla`; он может
представлять отдельное участие пользователя, Ayla / system или
tool-mediated participation, если это является частью Interaction. Состав
Turn рассматривается только на концептуальном уровне; Wave 2 не определяет
message schema, API payload или prompt format.

### 14.3. Belongs to exactly one Interaction

Каждый Dialogue Turn принадлежит ровно одному Interaction. Turn не может
переходить между Interaction и не может существовать вне Interaction.

### 14.4. User / system / tool participation

На концептуальном уровне Dialogue Turn может включать участие пользователя,
Ayla и/или внешних инструментов. Conversation Model не фиксирует ролевую
модель, формат сообщений или механизм вызова инструментов.

### 14.5. Turn content ≠ authoritative fact

Содержимое Dialogue Turn — это реплика, наблюдение или высказывание в контексте
разговора. Оно не является автоматически авторитетным backend-фактом и не
вводит достоверных доменных данных само по себе.

### 14.6. Inference in a turn ≠ memory fact

Выводы, сделанные в рамках Dialogue Turn (например, inferred context или
hypothesis), не считаются persistent memory fact до тех пор, пока не пройдут
соответствующую обработку и подтверждение в рамках Memory Model.

### 14.7. Turn itself ≠ Intent

Dialogue Turn может выражать Intent, но сам Turn не равен Intent. Intent —
это структурированное представление, определяемое `Ayla Intent Model
Specification`, а Dialogue Turn — единица истории разговора.

### 14.8. Source of Truth for Dialogue Turn semantics

Conversation Model Specification является Source of Truth для канонической
семантики `Dialogue Turn` согласно AYLA-DEC-0062. Если другие canonical
документы (например, `Ayla MVP User Journey Specification` v1.2) используют
более узкое определение (например, Dialogue Turn как обязательную пару
`сообщение пользователя + ответ Ayla`), это расхождение классифицируется как
терминологический mismatch и требует отдельного cross-document amendment.

`CROSS_DOCUMENT_FOLLOW_UP`: уточнить терминологию `Dialogue Turn` в
`Ayla MVP User Journey Specification` v1.2 для alignment с Conversation Model.

## 15. Canonical Hierarchy and Cardinality

### 15.1. Normative hierarchy

Каноническая иерархия и кардинальность зафиксированы следующим образом:

```text
Conversation
1 Conversation → 0..* Session

Session
1 Session → 0..* Interaction

Interaction
1 Interaction → 1..* Dialogue Turn
```

### 15.2. Child-to-parent belonging

- Session принадлежит ровно одной Conversation.
- Interaction принадлежит ровно одной Session.
- Dialogue Turn принадлежит ровно одному Interaction.

### 15.3. Zero-child lifecycle states

Запись `0..*` на стороне дочерней сущности допускает временные состояния, в
которых родительская сущность существует до появления первого дочернего
элемента (например, новосозданная Conversation до первого Session или
новосозданная Session до первого Interaction). Эти состояния относятся к
концептуальному lifecycle и не противоречат приведённой кардинальности.

Interaction определяется как уже существующий logically coherent episode,
поэтому кардинальность `1 Interaction → 1..* Dialogue Turn` не допускает
Interaction без хотя бы одного Dialogue Turn.

### 15.4. Not a database design

Иерархия и кардинальность относятся к продуктовой / доменной модели. В данном
разделе не проектируются foreign keys, storage schema или runtime-структуры
данных.

## 16. Identity Model

### 16.1. Conversation Identity

Conversation Identity основана на AYLA-DEC-0055. Conversation сохраняет
идентичность через:

- смену Session;
- смену канала;
- смену устройства;
- временную паузу.

Conversation Identity **не определяется**:

- каналом;
- устройством;
- timeout;
- одной конкретной Session;
- конкретным Intent.

### 16.2. Session Identity

Session обладает самостоятельной идентичностью внутри Conversation. Session
идентифицируется как операционная единица общения и не заменяет Conversation
Identity. Session не является глобальным владельцем Conversation.

### 16.3. Interaction Identity

Interaction имеет идентичность как связный эпизод общения. Идентичность
Interaction не смешивается с `intent_id`, `recommendation_id` или другими
идентификаторами смежных доменов. Interaction идентифицируется по своей
смысловой целостности внутри Session.

### 16.4. Dialogue Turn Identity

Dialogue Turn имеет собственную идентичность как атомарная единица истории
разговора. Формат ID не определяется в рамках Conversation Model; идентификаторы
и persistence mechanics принадлежат runtime / implementation contracts.

### 16.5. Identity invariants

- Идентичность дочерней сущности **не заменяет** идентичность родительской.
- Смена дочерней сущности (новый Dialogue Turn, новый Interaction, новый
  Session) **не создаёт автоматически** новую родительскую сущность.
- Идентификаторы, форматы ID и persistence mechanics относятся к
  runtime / implementation contracts и не являются частью продуктовой модели
  идентичности.

## 17. Conversation Lifecycle Overview

Conversation имеет начало, может продолжаться через несколько Session, может
переживать паузы, может возобновляться и может завершаться. Смена Session сама
по себе не завершает Conversation.

Эти положения описывают продуктовую семантику Conversation, а не технический
process graph, runtime workflow или state machine.

## 18. Conversation Start

Новая Conversation может возникнуть при появлении нового независимого
conversational purpose или новой независимой Transformation Goal, либо после
завершённой Conversation при начале нового независимого контекста.

Следующие события сами по себе **не порождают** новую Conversation:

- новый Intent;
- новая Session;
- новый канал;
- новое устройство;
- timeout;
- временная пауза.

В рамках Wave 3 не утверждается runtime-алгоритм определения момента начала
Conversation. Если точный критерий требует нового Owner Decision, это должно
быть зафиксировано в `OWNER_DECISION_REGISTER`, а не выведено в спецификации.

## 19. Active Continuity

Conversation может сохранять continuity через:

- несколько Interaction;
- несколько Session;
- допустимую смену канала;
- допустимую смену устройства;
- временные паузы.

Continuity не означает автоматический перенос ownership между каналами или
устройствами (AYLA-DEC-0055; `Ayla MVP User Journey Specification` v1.2
§Terminology). Conversation Model не превращает условия continuity в
runtime-алгоритм, heuristic или classification.

### 19.1. Session lifecycle boundary

Conversation может охватывать несколько Session; одна Session может начинаться
и завершаться, пока Conversation остаётся непрерывной. Wave 3 не проектирует
технический Session FSM (`SESSION_CREATED`, `SESSION_TIMEOUT` и т.п.).

## 20. Pause / Inactive Period

Пауза в Conversation:

- не является closure;
- не уничтожает Conversation Identity;
- не обязана определяться timeout;
- допускает resumption.

Wave 3 не канонизирует термин `Dormant` / `Dormancy` как имя состояния
Conversation при отсутствии соответствующего canon. Не задаются TTL, минуты,
часы, дни или иные технические пороги.

## 21. Resumption / Continuation

Согласно AYLA-DEC-0055:

- смена канала ≠ автоматически новая Conversation;
- смена устройства ≠ автоматически новая Conversation;
- смена Session ≠ автоматически новая Conversation;
- временная пауза ≠ автоматически новая Conversation.

Resumption / continuation сохраняют Conversation Identity, если сохраняется
смысловая и контекстная связность. Conversation Model не вводит similarity
scoring, heuristics, LLM classification, reconciliation algorithm или runtime
detection mechanics.

## 22. Conversation Completion / Closure

Conversation различает:

- **goal/action completion** — достижение результата или выполнение действия
  внутри Conversation;
- **Conversation closure** — завершение самой Conversation как продуктовой
  единицы.

Эти понятия не эквивалентны:

- booking, recommendation acceptance, downstream action или другое действие не
  означают автоматический конец Conversation;
- Conversation может продолжаться для follow-up, clarification, feedback,
  progress или связанного продолжения, пока сохраняется identity.

Closure не равнозначен privacy deletion, retention expiry или удалению данных.
Wave 3 не определяет retention / deletion mechanics.

## 23. Conceptual Conversation State

AYLA-DEC-0059 устанавливает, что Conversation State описывает смысловое
состояние разговора; Conversation Model не определяет runtime FSM, enum,
storage state machine или конкретную реализацию переходов.

Проверка существующего canon:

- **AYLA-DEC-0059** — conceptual state, без runtime FSM/enum;
- **Ayla MVP User Journey Specification v1.2** — описывает базовый lifecycle
  journey (`Conversation → Understanding → Recommendation → Execution →
  Learning`), но не задаёт canonical enum состояний Conversation;
- **Ayla Glossary** содержит определение `Conversation State`, ссылающееся на
  `ADR-0007 Conversation State Enum`; ADR-0007 не разрешён в текущем
  репозитории, что создаёт cross-document inconsistency;
- **текущий Conversation Model** фиксирует только концептуальный характер
  Conversation State.

Поскольку exact vocabulary canonical enum Conversation State в утверждённом
canon отсутствует, в Wave 3 не вводится canonical enum.

```text
Canonical Conversation State enum is NOT_DEFINED in this Wave.
```

Возможные смысловые измерения (initiated, active, paused/inactive,
completed/closed) могут обсуждаться только как поясняющая терминология до
принятия соответствующего Owner Decision.

`CROSS_DOCUMENT_FOLLOW_UP`: разрешить inconsistency между AYLA-DEC-0059 /
Conversation Model и `Ayla Glossary` (`ADR-0007`) в рамках отдельного
терминологического amendment.

## 24. State Invariants

Минимальные lifecycle/state инварианты Conversation Model:

- Session end ≠ Conversation end;
- channel switch ≠ Conversation end;
- device switch ≠ Conversation end;
- pause ≠ Conversation end;
- Action completion ≠ Conversation end;
- new Intent ≠ automatically new Conversation;
- Conversation closure ≠ data deletion;
- conceptual state ≠ runtime FSM transition mechanics.

Wave 3 не создаёт runtime transition table, state machine diagram, API
endpoints, database schema или TTL thresholds.
