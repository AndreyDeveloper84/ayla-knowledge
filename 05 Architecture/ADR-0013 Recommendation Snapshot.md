---
node_id: ayla.architecture.adr-0013-recommendation-snapshot
title: ADR-0013 Recommendation Snapshot
aliases:
  - ADR-0013
  - ADR-0013 Recommendation Snapshot
  - Recommendation Snapshot
adr_id: ADR-0013
type: adr
status: review
decision_status: superseded-proposed
revision: 1
version: "0.2"
amendments: []
superseded_by:
  - "[[Ayla MVP Recommendation Contract]]"
  - "[[Recommendation Architecture Final Reconciliation]]"
owner: Architecture + Recommendation
priority: P0
knowledge_area:
  - architecture
domain:
  - recommendation
  - booking
  - analytics
concerns:
  - explainability
  - audit
system_owner:
  - ayla-recommendation
source_repository: ayla-knowledge
created: 2026-07-29
updated: 2026-09-12
source_kind: canonical
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
tags:
  - ayla
  - ayla/architecture
  - ayla/adr
  - adr/0013
  - type/adr
  - priority/p0
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Killer PRD]]"
  - "[[Ayla Domain Event Registry]]"
related:
  - "[[ADR-0012 Dynamic User Model]]"
  - "[[Ayla MVP Recommendation Contract]]"
review_cycle: event-driven
---

# ADR-0013 Recommendation Snapshot

## Статус

**Статус документа:** **PROPOSED v1.0 — awaiting owner approval:
superseded** (пакет 2 от 12.09.2026, **B10 (а)**: «ADR-0013 superseded —
смешивает decision, candidate/provider ranking и transaction state»).
**Чем заменён:** [[Ayla MVP Recommendation Contract]] v1.0 §7 (три
логических снимка) и §25 (replay) + канон v1.1 Decision 7 (immutable
Recommendation object) — Final Reconciliation v1.0 §4 конфликт 4, §6.3.
**Что сохраняется:** правило «UX рендерит из snapshot, не из live» — для
каждого из трёх снимков: Decision Snapshot (в Recommendation record),
Execution Mapping Snapshot (в ExecutionOption), Transaction Snapshot (в
PendingBookingIntent / Booking). Open Questions 1–5 (§5) перенесены в
контракт v1.0 §25 как открытые входы.
**Версия:** 0.2 (2026-09-12); при утверждении владельцем `status` →
`superseded`, `decision_status` → `superseded`. Решение ADR **не
принималось** (v0.1 — proposed) и не принимается: текст ниже — история.

> **Владение.** UX не владеет recommendation-правилами. Этот ADR —
> предложение, подготовленное по запросу Product Owner (task UX-ADR-001), и
> подлежит принятию владельцами Architecture / Recommendation (владельцами
> MVP Recommendation Contract, planned Roadmap §3.2). До канонизации
> нормативным документом не является.

## 1. Context

В UX-контрактах (Recommendation UX Addendum, SCR-CUST-004/005/006)
уже используется `recommendation_id` как обязательная ссылка; UX-OD-004
фиксирует сохранение `recommendation_id` через весь booking flow, включая
deep link bot DM → Mini App. Booking без `recommendation_id` —
`unattributed` (Killer PRD §6.2).

Проблема: `recommendation_id` — это ссылка, а не состояние. Спустя время
(недели–месяцы) на вопрос «почему пользователю была показана именно эта
рекомендация?» ответить невозможно:

- live-состояние кандидата, intent, availability и ranking mutates —
  реконструировать состав показанного по одному ID нельзя;
- объяснение «почему подходит» — обязательная capability MVP (Scope Contract
  §4.1 п. 9, Конституция Ст. VII) — не привязано к версии пайплайна, которая
  его породила;
- attribution booking→recommendation фиксирует факт связи, но не snapshot
  того, что именно было показано в момент shown.

Требуется point-in-time объект-снимок, который замораживает контекст показа
в момент генерации рекомендации.

## 2. Decision (proposed)

Вводится **immutable Recommendation Snapshot** — point-in-time объект,
фиксирующий состав и версии окружения одного показанного recommendation.
Snapshot **никогда не мутируется**: любое новое состояние рекомендации
(alternative после rerank, повторный показ) — **новый snapshot** с новым
`recommendation_snapshot_id`.

### Поля snapshot

| Поле | Назначение |
|---|---|
| `recommendation_snapshot_id` | Уникальный идентификатор снимка; на него ссылаются booking (attribution), UX и analytics |
| `recommendation_id` | Ссылка на recommendation, сохраняемая через booking flow (UX-OD-004); для alternative — вместе с `parent_recommendation_id` |
| `candidate_id` | Какой кандидат был выбран pipeline-ом на момент показа |
| `intent_id` | Intent, по которому сформирована рекомендация (Intent Model Output Contract) |
| `generated_at` | Timestamp генерации (UTC) — граница «point-in-time» |
| `explanation_version` | Версия логики/шаблона объяснения, сформировавшего «почему подходит» |
| `ranking_version` | Версия ranking/scoring пайплайна, выбравшего кандидата |
| `memory_version` | Версия memory-состояния, использованного при генерации |
| `availability_version` | Версия/срез availability-данных (слоты, расписание) на момент показа |
| `source_context` | Контекст-источник показа (например: bot DM card, Mini App, deep link) |
| `session_id` | Сессия, в которой сформирован показ |

### Связи

- **Booking → snapshot:** booking ссылается на `recommendation_snapshot_id`
  (в дополнение к `recommendation_id`, который сохраняется по UX-OD-004).
  Это даёт attribution «к состоянию», а не только «к событию»: single-winner
  attribution (Killer PRD §6.3) опирается на зафиксированный состав показа.
- **UX рендерит из snapshot, а не из live-состояния.** Карточка
  (SCR-CUST-004) отображает то, что зафиксировано в snapshot на момент
  shown. Это устраняет класс багов «карточка изменилась после показа»
  (обновилась цена, слот, объяснение между shown и повторным рендером).
  Правило согласуется с существующей нормой «UX не обогащает карточку
  данными вне контракта» (Recommendation UX Addendum §1).

### Phase 1 упрощения

- `memory_version` — **fixed null / отсутствует**: persistent memory
  disabled, Phase 1 = session-only (UX-OD-003). Поле зарезервировано в
  схеме для Phase 2.
- Snapshot живёт **в пределах сессии (session-only)**: гарантии хранения за
  пределами сессии не даются. Persistence policy (TTL, cross-session
  retention) — open question (§5).

## 3. Consequences

### Положительные

- **Объяснимость:** на вопрос «почему показали именно это» есть
  детерминированный ответ: candidate + intent + версии пайплайна на
  момент shown. Поддерживает capability объяснения (Конституция Ст. VII) и
  разбор инцидентов/жалоб.
- **Аналитика:** attribution booking→recommendation привязан к snapshot;
  метрика `booking_from_recommendation` сопоставима с конкретным составом
  показа, а не с изменившимся live-состоянием.
- **Детерминированный UX:** рендер из snapshot исключает расхождения между
  первым и повторным показом; stale-slot и invalidation кейсы (N5,
  economic-neutrality) диагностируются по зафиксированной
  `availability_version`.
- **Поддержка и audit:** snapshot — готовый evidence-объект для support и
  governance-разборов.

### Издержки

- **Хранение:** snapshot на каждый shown-экземпляр (primary + до 2
  alternative) — дополнительный объём хранения; при session-only политике
  объём ограничен, но для аналитики за пределами сессии потребуется
  отдельное persistence-решение.
- **Контракт генерации:** Recommendation Composer обязан эмитировать
  snapshot атомарно с показом; добавляется версионирование полей
  `*_version` — нужна discipline версионирования pipeline-артефактов.
- **Coupling:** booking-схема и UX-контракты получают дополнительную
  ссылку; изменение состава snapshot — breaking change для consumers.

## 4. Alternatives

- **(a) Только `recommendation_id`, без snapshot.** Отклонено: ссылка без
  состояния не даёт объяснимости и не отвечает на вопрос «почему была
  показана эта рекомендация» ретроспективно; live-состояние mutates и
  реконструкция невозможна. Не закрывает требование объяснимости.
- **(b) Snapshot с мутациями (обновляемый объект).** Отклонено: мутация
  уничтожает point-in-time семантику — нельзя доказать, что именно видел
  пользователь на момент shown; возвращается класс багов «состояние
  изменилось после показа». Immutability + «новое состояние = новый
  snapshot» проще и аудируемее.

## 5. Open Questions

1. **Владение генерацией и хранением snapshot.** Кто создаёт и хранит
   snapshot: bot-platform или Ayla backend — в рамках split по ADR-0009?
   Owner: Architecture (platform split).
2. **Persistence policy / TTL.** Живёт ли snapshot за пределами сессии;
   retention для аналитики и разбора инцидентов; связь с privacy
   (session-only норма UX-OD-003 запрещает перенос session data в
   persistent storage до решения Privacy Owner). Owner: Architecture +
   Privacy Owner.
3. **Связь с Domain Event Registry.** Ссылается ли snapshot на/из событий
   `recommendation.generated` / `recommendation.presented`
   (аналог `recommendation.shown`); семейство `recommendation.*` в Registry
   — pending (OQ-E1, семантика не утверждена). Owner: Architecture (Domain
   Event Registry) + Recommendation.
4. **Versioning policy полей `*_version`.** Формат, гранулярность и
   ownership версий `explanation_version`, `ranking_version`,
   `availability_version`, `memory_version`; что считается bump-ом версии.
   Owner: Recommendation / AI Architecture.
5. **Граница «новый snapshot».** Является ли повторный рендер той же карточки
   (без изменения состояния) тем же snapshot; получает ли alternative свой
   snapshot с `parent_recommendation_id`. Owner: Recommendation.

## Источники

- Recommendation UX Addendum (UX-facing constraints): §1 Composition,
  §3 Lifecycle, §4 Attribution (`01 Product/UX MVP/contracts/draft-mvp-recommendation-contract.md`)
- UX Owner Decisions: UX-OD-003 (session-only), UX-OD-004 (preserve
  `recommendation_id` через booking flow) (`01 Product/UX MVP/decisions/ux-owner-decisions.md`)
- Killer PRD: §5.1–5.3, §6.1–6.3
- Ayla Domain Event Registry: `recommendation.*` — pending (OQ-E1)
  (`05 Architecture/Ayla Domain Event Registry.md`)
- MVP Scope and Release Contract: §4.1 п. 9, 11
