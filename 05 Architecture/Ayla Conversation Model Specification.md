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
Текущая версия содержит только Foundation (Wave 1): frontmatter, позиционирование, назначение,
канонические принципы, scope, зависимости, терминологию и правила использования терминов.
Нормативные разделы иерархии, идентичности, lifecycle, состояния, контекста, projection,
границ и инвариантов будут добавлены в последующих волнах письма спецификации.

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
