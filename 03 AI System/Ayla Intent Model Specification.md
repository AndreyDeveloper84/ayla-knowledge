---
node_id: ayla.ai.intent-model
title: Ayla Intent Model Specification
type: ai-specification
status: draft
decision_status: proposed
version: "0.1"
owner: AI Architecture
priority: P0
knowledge_area:
  - ai-system
domain:
  - intent
concerns:
  - safety
  - explainability
system_owner:
  - ayla-ai-core
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
  - "[[Ayla User Journey Specification]]"
  - "[[Ayla MVP Scope and Release Contract]]"
  - "[[Ayla Decision Log]]"
related:
  - "[[Consent Scope Registry]]"
  - "[[Ayla Domain Capability Registry]]"
  - "[[Killer PRD]]"
---

# Ayla Intent Model Specification

> **Статус:** draft. Это не канонизация. По AYLA-DEC-0011 документ является
> критическим predecessor для [[Ayla Domain Context Map]] и
> [[Ayla Core Domain Model Specification]]: эти документы не могут перейти к
> содержательной канонизации, пока Intent Model не зафиксирован содержательно.
> AYLA-DEC-0014 помещает этот документ в волну 1 (продуктовые блокеры) и
> ограничивает его объём MVP-срезом.
>
> **Соглашение о пометках.** Положения, прямо подтверждённые источниками,
> помечены «Факт — <источник>». Всё, что предлагается этим документом впервые,
> помечено «Proposal» и не имеет нормативной силы до approval.

## Purpose

Документ определяет MVP-объём Intent Understanding (CAP-003,
[[Ayla MVP Scope and Release Contract]] §4.1): какие intent types система
обязана распознавать, какие слоты заполнять, когда задавать уточняющий вопрос,
как обрабатывать смену и отмену намерения и в каком формате возвращать
результат intent resolution.

Задача документа — устранить неопределённость, при которой AI, backend и
канал реализовали бы intent handling несовместимо (принцип
[[Ayla MVP Documentation Roadmap]] вводная часть). Документ не описывает
реализацию классификатора (модель, prompt, код) — это зона ayla-ai-core и
Prompt Canon (Roadmap §3.3).

Проверяемая цель (Факт — Roadmap §9.2): качество intent layer измеряется
метриками «доля resolved intents» и «clarification rate» в составе главной
метрики MVP «осмысленный запрос → полезная рекомендация → подтверждённое
действие», а не количеством сообщений.

## Responsibility

Intent Model отвечает за превращение текущего пользовательского сообщения
(query) в структурированное намерение (intent) со слотами, оценкой уверенности
и safety-пометками — ровно в объёме, достаточном, чтобы Recommendation,
Availability и Appointment capabilities могли действовать дальше по сквозному
сценарию (Факт — [[Ayla MVP Scope and Release Contract]] §3):

```text
Пользователь выражает потребность
→ Ayla уточняет intent          ← зона ответственности этого документа
→ подбирает услугу или действие
→ объясняет рекомендацию
→ пользователь подтверждает
→ Ayla создаёт запись
→ пользователь получает подтверждение
```

Факт — [[Ayla Glossary]]: Intent — структурированное представление того, что
человек пытается изменить, понять, выбрать или сделать; Intent не является
ключевым словом, названием услуги или буквальным повторением сообщения. Query —
нормализованное содержимое текущего обращения, само по себе не достоверный
факт и не Intent.

## Owns

- Реестр MVP intent types и их required/optional slots (§ Intent Types,
  § Slots).
- Правила confidence, clarification, multi-intent, correction, supersession,
  expiry (соответствующие разделы).
- Output contract результата intent resolution (§ Output Contract) —
  обязательный минимум по Roadmap §3.1; поля этого контракта являются
  единственными, которые downstream consumers вправе требовать от intent
  resolver в MVP.
- Правило разметки safety-sensitive intents и состав `safety_flags`
  (§ Safety-sensitive Intents) в пределах, не противоречащих будущей MVP
  Safety Policy (Roadmap §7.3, ещё не материализована — см. Open Questions).

## Does not own

- **Recommendation, ranking, candidates** — MVP Recommendation Contract
  (Roadmap §3.2) и [[Killer PRD]]; Intent Model только поставляет resolved
  intent на вход recommendation pipeline.
- **Consent policy и runtime authorization** — [[Consent Scope Registry]]
  (owner: User Context Domain Owner / Privacy Owner). Intent Model читает
  результат authorization check, но не определяет scopes и не хранит consent.
- **Safety policy** — детерминированные gates, red flags, competence boundary
  определяются MVP Safety Policy (Roadmap §7.3) и CAP-014; этот документ
  определяет только, как их результат отражается в intent resolution.
- **Модель Intent как доменную сущность** (stable ID, lifecycle, SoR,
  persistence) — [[Ayla Core Domain Model Specification]] (MVP slice,
  Roadmap §4.3).
- **Prompt assembly, tool schemas, provider abstraction** — ayla-ai-core по
  Prompt Canon (Roadmap §3.3) и Tool Schema Registry (Roadmap §6.3).
- **Коммуникативная таксономия** Intent Type (`goal`, `action`, `information`,
  `management`, `feedback`, `correction`) и Goal Category — определены в
  [[Ayla User Journey Specification]] Stage 3 и [[Ayla Glossary]]; их связь с
  реестром intent types этого документа — Open Question OQ-4, здесь не
  переопределяется.

## Non-goals

Явно вне объёма MVP (Факт — основания: Roadmap §1.2 out of scope, §3.1
«не надо сразу описывать сотни намерений», §3.2 «не детализировать»):

- продвинутые ML-модели классификации и обучение на истории диалогов;
- расширение реестра сверх 12 intent types § Intent Types;
- долгосрочное персонализационное обучение по intent-паттернам (advanced
  Outcome Learning — deferred, [[Ayla MVP Scope and Release Contract]] §5);
- proactive recommendations и cross-domain personalization — выключены до
  Phase 2 gates (Факт — [[Consent Scope Registry]] §10);
- persistent memory для intent understanding — Phase 1 session-only
  (Факт — [[Consent Scope Registry]] §5.1, §10.1);
- мультиязычная и multi-channel спецификация (единственные каналы MVP —
  MAX-бот + MAX Mini App, AYLA-DEC-0004);
- автоматические медицинские выводы из intent (запрещено — Roadmap §1.2,
  [[Killer PRD]] §9).

## Inputs

Вход intent resolution (Факт — состав данных ограничен scope
`intent_understanding`, [[Consent Scope Registry]] §5.1):

- **User Message / Query** — текущее сообщение пользователя в канале MVP
  (MAX-бот / MAX Mini App).
- **Session context** — только разрешённые категории: `explicit_goal`,
  `service_preference`, `provider_preference`, `session_signal`. Persistent
  context этим scope не разрешён; чтение persistent preferences требует
  активного consent на `preference_memory` (required authorization, Phase 2).
- **Authorization state** — результат runtime authorization contract
  ([[Consent Scope Registry]] §6): какие категории данных доступны resolver'у
  в этой сессии. Отсутствие consent → deny (fail-closed).
- **Контекст диалога сессии** — предыдущие сообщения и подтверждённые слоты
  текущей сессии (нужны для multi-intent, correction, supersession).
- **Safety evaluation input** — red-zone факты и сигналы риска, доступные в
  сессии, для передачи в deterministic safety gates (CAP-014).

Ограничение (Факт — [[Consent Scope Registry]] §5.1): scope
`intent_understanding` имеет validity «текущая сессия», authorization basis
`service_necessity`, запрещает `write`/`delete` и persistence
`inferred_signal`. Intent resolver не вправе сохранять что-либо о пользователе
— сохранение фактов выполняется только через PROVIDE_CONTEXT/CORRECT_CONTEXT
и владельца Personal Context (CAP-001) по своим правилам.

## Outputs

Единственный выход — результат intent resolution по Output Contract
(§ Output Contract): структурированный объект, которого достаточно, чтобы:

- Recommendation Formation (CAP-004) собрала candidates для actionable
  intents;
- канал задал пользователю ровно один уточняющий вопрос, когда
  `requires_clarification = true`;
- safety gate заблокировал дальнейший pipeline при непустых `safety_flags`;
- audit/attribution могли связать последующее действие с конкретным
  `intent_id` (событие `IntentResolved` — MVP event, Roadmap §6.4).

Intent Model не вызывает tools и не создаёт side effects: запись, перенос и
отмена выполняются только после подтверждения пользователя соответствующими
capabilities (Факт — автономные действия без подтверждения запрещены:
Roadmap §1.2, [[Ayla Constitution]]).

## Intent Types

Минимальный набор MVP (Факт — дословно Roadmap §3.1; не расширяется). Все 12
типов MVP-critical: каждый прямо обслуживает сквозной сценарий
([[Ayla MVP Scope and Release Contract]] §3), included capabilities (§4.1:
Appointment Management — создание, подтверждение, перенос, отмена; Consent
Management; Personal Context whitelist) или обязательный негативный сценарий
«Ayla не поняла запрос» (Roadmap §2.1).

| Intent type | Description | Required slots | Optional slots | Safety-sensitive | MVP-critical |
|---|---|---|---|---|---|
| `DISCOVER_SERVICE` | Пользователь выражает потребность и ищет подходящую услугу без конкретного исполнителя («устала, хочу расслабиться») | `service_interest` | `time_preference`, `budget`, `provider_preference` | yes | yes |
| `FIND_SPECIALIST` | Поиск конкретного специалиста или подбор по критериям («запишите к Анне», «кто делает лимфодренажный») | — (хотя бы один из optional) | `provider_name`, `service_category` | no | yes |
| `BOOK_APPOINTMENT` | Создать запись на услугу | `service_ref`, `time_slot` | `provider_name`, `comment` | no | yes |
| `RESCHEDULE_APPOINTMENT` | Перенести существующую запись | `appointment_ref`, `new_time_slot` | `reason` | no | yes |
| `CANCEL_APPOINTMENT` | Отменить существующую запись | `appointment_ref` | `reason` | no | yes |
| `ASK_ABOUT_SERVICE` | Вопрос о содержании, длительности, подготовке, противопоказаниях услуги | `service_ref` | — | yes | yes |
| `ASK_ABOUT_PRICE` | Вопрос о стоимости услуги или booking fee | `service_ref` | `provider_name` | no | yes |
| `ASK_ABOUT_AVAILABILITY` | Вопрос о свободных слотах услуги или специалиста | — (хотя бы один из optional) | `service_ref`, `provider_name`, `time_window` | no | yes |
| `PROVIDE_CONTEXT` | Пользователь добровольно сообщает факт о себе (предпочтение, ограничение) | `context_fact` | `fact_category` | yes | yes |
| `CORRECT_CONTEXT` | Пользователь исправляет ранее сообщённый или сохранённый факт | `context_fact_ref`, `context_fact` | — | yes | yes |
| `REVOKE_CONSENT` | Пользователь отзывает согласие на использование данных | — | `consent_scope` | no | yes |
| `UNKNOWN` | Намерение не распознано или вне реестра MVP | — | — | no | yes |

Примечания (Proposal, если не указано иное):

- `safety-sensitive = yes` означает: intent может вовлекать health-adjacent
  или red-zone контекст, поэтому его resolution обязан проходить safety
  evaluation до перехода к recommendation/answer (Факт — механика Safety
  Check: [[Ayla User Journey Specification]] Stage 3; red-zone факты —
  аллергии, противопоказания, конфликт целей). Это разметка обязательной
  проверки, а не запрет intent.
- `ASK_ABOUT_SERVICE` помечен safety-sensitive, потому что ответ может
  касаться противопоказаний; запрещённые медицинские выводы контролируются
  Safety Policy, а не этим документом.
- `REVOKE_CONSENT` не safety-sensitive, но governance-critical: обработка по
  § Multi-intent and Correction и [[Consent Scope Registry]] §8.
- `UNKNOWN` — обязательный fallback тип: resolver обязан вернуть его вместо
  угадывания, когда confidence ниже порога (§ Confidence and Clarification).

## Slots

Slot — именованная единица контекста, которая может быть заполнена,
отсутствовать, конфликтовать или требовать подтверждения (Факт —
[[Ayla Glossary]], Context Slot).

MVP slot registry (Proposal; категории данных согласованы с разрешёнными
категориями scope `intent_understanding` — Факт, [[Consent Scope Registry]]
§5.1):

| Slot | Тип значения | Источник значения | Data category |
|---|---|---|---|
| `service_interest` | Категория услуги seed catalog или свободная формулировка потребности | сообщение пользователя | `explicit_goal` / `service_preference` |
| `service_ref` | Идентификатор или однозначное название услуги | сообщение + каталог (CAP-008) | `service_preference` |
| `service_category` | Категория из seed catalog | сообщение + каталог | `service_preference` |
| `provider_name` | Имя специалиста/салона как сказал пользователь | сообщение | `provider_preference` |
| `provider_preference` | Критерий выбора исполнителя | сообщение | `provider_preference` |
| `time_preference` | Свободное выражение времени («в пятницу вечером») | сообщение | `session_signal` |
| `time_window` | Интервал времени для availability-запроса | сообщение | `session_signal` |
| `time_slot` | Конкретный слот или однозначное время записи | сообщение + Availability (CAP-010) | `session_signal` |
| `new_time_slot` | Новое время при переносе | сообщение + Availability | `session_signal` |
| `appointment_ref` | Ссылка на запись: ID или однозначное описание («моя запись в пятницу») | сообщение + Appointment (CAP-011) | `session_signal` |
| `budget` | Бюджет пользователя в свободной форме | сообщение | `explicit_goal` |
| `comment` | Произвольный комментарий к записи | сообщение | `session_signal` |
| `reason` | Причина переноса/отмены | сообщение | `session_signal` |
| `context_fact` | Факт о пользователе (текст) | сообщение | зависит от содержания; persistence — только whitelist Roadmap §3.4 через CAP-001 |
| `context_fact_ref` | Ссылка на исправляемый факт текущей сессии | диалог сессии | как `context_fact` |
| `fact_category` | Категория факта из whitelist | классификация | — |
| `consent_scope` | Scope из [[Consent Scope Registry]] §5 | сообщение | — |

Правила (Proposal):

- Slot заполняется только из текущей сессии; автоматическая подстановка
  persistent значений запрещена до Phase 2 (Факт — [[Consent Scope Registry]]
  §10.1).
- Slot, заполненный и подтверждённый, повторно не спрашивается, пока он
  релевантен текущему intent, совместим с purpose и не противоречит новому
  сигналу (Факт — [[Ayla User Journey Specification]], Incremental
  Discovery).
- Конфликтующие значения одного slot (старое и новое в одной сессии)
  разрешаются через CORRECT_CONTEXT или clarification — не молчаливым
  перезаписыванием.
- `appointment_ref` и `service_ref` считаются заполненными только при
  однозначном разрешении в сущность backend; неоднозначность → clarification.

## Confidence and Clarification

Confidence — оценка надёжности конкретного структурированного вывода, не
доказательство истинности (Факт — [[Ayla Glossary]]).

Уровни уверенности (Факт — [[Ayla User Journey Specification]] Stage 3,
заданы для формулировок в диалоге; Proposal — использовать те же пороги для
логики clarification):

- **high (> 0.8):** intent считается распознанным; clarification не
  требуется, если заполнены required slots.
- **medium (0.5–0.8):** допустимо продолжать с подтверждающей формулировкой
  («Возможно, ты хочешь…»); подтверждение пользователя обязательно перед
  actionable execution.
- **low (< 0.5):** resolver обязан вернуть `requires_clarification = true`
  либо `intent_type = UNKNOWN`; угадывание запрещено.

Clarification rules (Proposal, если не указано иное):

1. `requires_clarification = true` устанавливается ровно в трёх случаях:
   confidence low; не заполнен хотя бы один required slot; конфликт значений
   слота.
2. `clarification_question` — ровно один конкретный вопрос о
   `missing_required_slots` или конфликте; вопрос обязан ссылаться на то, что
   уже сказал пользователь (не общий «что вы хотите?»).
3. Не более 2 clarification-подходов подряд по одному intent; далее
   `intent_type = UNKNOWN`, `status = unresolved` и fallback по негативному
   сценарию «Ayla не поняла запрос» (Факт — существование сценария: Roadmap
   §2.1; предел 2 — Proposal).
4. Ответ пользователя на clarification обрабатывается как новый вход того же
   intent (тот же `intent_id`), а не как новый intent — Proposal.
5. Для `REVOKE_CONSENT` clarification не может откладывать исполнение: при
   неуказанном `consent_scope` допускается один уточняющий вопрос; повторная
   неоднозначность трактуется как отзыв всех затронутых scopes — Proposal
  (сверить с Privacy Owner, см. OQ-5).

## Multi-intent and Correction

Multi-intent — ситуация, когда одно сообщение содержит несколько значимых
Intent; Primary Intent наиболее существенно определяет следующий шаг,
Secondary — дополнительный (Факт — [[Ayla Glossary]]).

Правила MVP (Proposal):

1. Один результат intent resolution = один Primary Intent. Secondary intents
   из одного сообщения фиксируются в `evidence` и обрабатываются
   последовательными resolution-циклами, а не параллельно.
2. Если два actionable intent равнозначны (например, «запиши на массаж и
   сколько стоит маникюр» — BOOK + ASK), resolver выбирает Primary по
   приоритету: informational intents (ASK_*) разрешаются первыми, actionable
   (BOOK/RESCHEDULE/CANCEL) — только после подтверждения пользователя
   (Факт — запрет автономных действий: Roadmap §1.2).
3. Правила учёта multi-intent в метрике resolved intents (denominator,
   exclusion rules) требуются [[Ayla User Journey Specification]] (Intent
   Resolution Types), но там не зафиксированы — Open Question OQ-3.

Correction:

1. `CORRECT_CONTEXT` заменяет значение факта в пределах текущей сессии; новое
   значение не считается подтверждённым, пока пользователь не подтвердил
   исправление — Proposal.
2. Исправление факта, влияющего на safety (red-zone), обязано запускать
   повторную safety evaluation до продолжения actionable pipeline (Факт —
   аналог Safety Re-evaluation при Intent Shift,
   [[Ayla User Journey Specification]], Dynamic Intent Transition).
3. Событие `ContextFactCorrected` входит в MVP event set (Факт — Roadmap
   §6.4); persistence исправлений — зона CAP-001 Personal Context и Phase 2
   gates, не этого документа.

## Supersession and Expiry

Supersession (смена намерения внутри сессии). Факт —
[[Ayla User Journey Specification]], Dynamic Intent Transition: пользователь
может менять намерение в рамках одной сессии; при сдвиге Ayla:

1. фиксирует Intent Shift;
2. передаёт в Incremental Discovery только разрешённый к повторному
   использованию контекст;
3. перезапускает Safety Re-evaluation для нового intent;
4. обновляет Recommendation Layer;
5. **не продолжает execution по старому intent без нового подтверждения
   пользователя.**

Proposal (операционализация для output contract): сменившийся intent получает
новый `intent_id`; прежний результат считается вытесненным (`status =
superseded`) и недоступным для execution. Связь «новый вытесняет старый»
фиксируется в audit-следе события `IntentResolved`, а не в полях output
contract (состав полей заморожен Roadmap §3.1 — см. OQ-6).

Expiry. Факт — [[Consent Scope Registry]] §5.1: validity scope
`intent_understanding` — текущая сессия; следовательно, resolved intent
действителен только в пределах сессии и не переносится между сессиями.
Proposal: intent в статусе `needs_clarification`, оставшийся без ответа,
считается `expired` по завершении сессии; таймаут внутри активной сессии в
MVP не устанавливается (OQ-2).

## Safety-sensitive Intents

Механика (Факт — [[Ayla User Journey Specification]] Stage 3 Safety Check):
перед переходом к recommendation resolver проверяет red-zone факты (аллергии,
противопоказания), конфликты целей и риск вреда; при высоком риске или
competence boundary Ayla не подтверждает и не продолжает небезопасный путь, а
переходит к Boundary Handling; безопасная альтернатива предлагается только
после него. Детерминированные safety gates обязательны для всех product
capabilities (Факт — [[Ayla MVP Scope and Release Contract]] §4.2, CAP-014).

Отражение в intent resolution (Proposal):

- `safety_flags` — список машиночитаемых кодов. Начальный MVP-набор:
  - `red_zone_context` — intent опирается на red-zone факт;
  - `competence_boundary` — запрос выходит за границы компетенции Ayla
    ([[Ayla Constitution]] Ст. XII);
  - `unsafe_service_request` — запрошенная услуга конфликтует с известными
    ограничениями;
  - `consent_scope_missing` — для resolution требуются данные, недоступные по
    текущему authorization state.
- Непустой `safety_flags` → `status = blocked_safety`, recommendation
  pipeline не запускается; downstream код ошибки — `SAFETY_BLOCKED` или
  `CONSENT_REQUIRED` (Факт — стабильные коды: Roadmap §6.5).
- Safety gates детерминированы: LLM не может «переубедить» gate снятием
  флага; снятие возможно только новым пользовательским вводом, изменяющим
  оценку (например, CORRECT_CONTEXT убрал red-zone факт) — Proposal.
- `unsafe block rate` — обязательная метрика пилота (Факт — Roadmap §9.2).

## Output Contract

Обязательный контракт результата intent resolution (Факт — состав полей
дословно Roadmap §3.1; типы и семантика — Proposal):

```yaml
intent_id:                # стабильный ID результата resolution в пределах сессии (UUID)
intent_type:              # одно из 12 значений реестра § Intent Types
status:                   # resolved | needs_clarification | unresolved | superseded | expired | blocked_safety
confidence:               # число 0.0–1.0; уровни по § Confidence and Clarification
slots:                    # объект {slot_name: value}; только заполненные слоты
missing_required_slots:   # список имён required slots без однозначного значения
evidence:                 # список ссылок на фрагменты сообщений сессии, обосновывающих вывод
requires_clarification:   # boolean; true ровно в случаях § Confidence and Clarification п. 1
clarification_question:   # string | null; обязателен, когда requires_clarification = true
safety_flags:             # список кодов § Safety-sensitive Intents; пустой при отсутствии рисков
```

Инварианты (Proposal):

- `intent_type = UNKNOWN` ⇒ `status ∈ {needs_clarification, unresolved}`.
- `requires_clarification = true` ⇒ `clarification_question ≠ null` и
  `status = needs_clarification`.
- `status = resolved` ⇒ `missing_required_slots = []` и
  `safety_flags = []`.
- `safety_flags ≠ []` ⇒ `status = blocked_safety` и результат не передаётся в
  recommendation pipeline.
- `evidence` не пуст для `status = resolved`: каждый resolved intent обязан
  быть прослеживаем к пользовательскому вводу (Факт — принцип
  прослеживаемости критических решений: [[Ayla Constitution]]; explainability
  — обязательное требование MVP, [[Ayla MVP Scope and Release Contract]]
  §4.1 п. 9).
- Контракт additive-расширяем: новые поля допускаются только через change
  control и совместимость с consumers (Roadmap §5.4); удаление/переименование
  полей — breaking change.

## Open Questions

- **OQ-1. Владелец числовых порогов confidence.** Journey Stage 3 задаёт
  0.8/0.5 для формулировок; использование их как runtime-порогов
  классификатора — proposal этого документа. Подтвердить при approval или
  вынести в конфигурацию ayla-ai-core.
- **OQ-2. Таймаут expiry внутри активной сессии** для intent в статусе
  `needs_clarification` (сейчас: только конец сессии). Требуется решение
  Product Owner совместно с MVP UX State Contract (Roadmap §2.2).
- **OQ-3. Правила метрики resolved intents:** denominator, exclusion rules,
  resolution window, учёт multi-intent, различие user-confirmed/inferred —
  обязательны по Journey (Intent Resolution Types), но нигде не зафиксированы.
  Кандидат на фиксацию: Pilot Measurement Plan (Roadmap §9.2).
- **OQ-4. Связь реестра intent types с коммуникативной таксономией** Journey
  Stage 3 (`goal`/`action`/`information`/`management`/`feedback`/`correction`)
  и Goal Category: одно измерение или два? Решить до канонизации
  [[Ayla Core Domain Model Specification]] (модель Intent).
- **OQ-5. Дефолт при неоднозначном REVOKE_CONSENT** (отзыв всех затронутых
  scopes после одного clarification) требует подтверждения Privacy Owner и
  согласования с [[Consent Scope Registry]] §8 (команды пользователя).
- **OQ-6. Представление supersession-связи** (новый intent вытесняет старый):
  audit-след события `IntentResolved` vs дополнительное поле контракта.
  Текущее решение — audit-след, чтобы не расширять замороженный контракт.
- **OQ-7. Финальный состав `safety_flags`** — синхронизировать с MVP Safety
  Policy (Roadmap §7.3) при её материализации; текущий набор — proposal.
- **OQ-8. Persistence `intent_id`** для связки с attribution
  (`recommendation_id` → qualified action, [[Killer PRD]] §6): хранится ли
  intent result в backend или живёт только в сессии — решить в MVP
  Architecture (Roadmap §5.1).

## Acceptance Criteria

Документ считается готовым к переводу из draft в review, когда выполнено:

1. Определены все 12 intent types из Roadmap §3.1 с description, required и
   optional slots, разметкой safety-sensitive и MVP-critical; ни одного типа
   сверх реестра.
2. Output contract содержит все 10 обязательных полей Roadmap §3.1 с
   типами, допустимыми значениями и проверяемыми инвариантами; каждый
   инвариант выразим как автоматический тест.
3. Правила clarification задают исчерпывающие условия
   `requires_clarification = true` и верхнюю границу числа уточнений;
   «угадывание» при low confidence исключено формулировкой.
4. Supersession и expiry опираются на зафиксированные в источниках механики
   (Dynamic Intent Transition, session validity) и не вводят перенос intent
   между сессиями.
5. Safety-sensitive intents размечены; связь `safety_flags` →
   `blocked_safety` → `SAFETY_BLOCKED`/`CONSENT_REQUIRED` согласована с
   кодами Roadmap §6.5.
6. Все положения, не подтверждённые источниками, помечены Proposal; все
   незакрытые решения собраны в Open Questions и не подменены выдуманными
   значениями.
7. Содержимое не выходит за MVP-границы
   [[Ayla MVP Scope and Release Contract]] §4/§5 и consent-режим Phase 1
   ([[Consent Scope Registry]] §10.1).
8. `python scripts/validate_knowledge.py` — 0 errors по этому документу.

## Change Log

> Журнал отражает историю изменений документа и не является нормативной частью
> спецификации.

### v0.1 (2026-07-27) — Initial draft

- Документ создан как критический predecessor по AYLA-DEC-0011 в объёме
  MVP-среза (AYLA-DEC-0014, Roadmap §3.1).
- Реестр intent types и состав output contract перенесены дословно из
  Roadmap §3.1 без расширения.
- MVP slot registry, пороги confidence как runtime-пороги, лимит
  clarification, правила multi-intent/correction, операционализация
  supersession/expiry и состав `safety_flags` оформлены как Proposal.
- Открытые вопросы OQ-1…OQ-8 зафиксированы без подмены решений.
