---
node_id: ayla.architecture.adr-0014-conversation-context-id
title: ADR-0014 Conversation Context ID
aliases:
  - ADR-0014
  - ADR-0014 Conversation Context ID
  - Conversation Context ID
adr_id: ADR-0014
type: adr
status: draft
decision_status: proposed
revision: 1
version: "0.1"
amendments: []
superseded_by: null
owner: Architecture + Platform
priority: P1
knowledge_area:
  - architecture
domain:
  - user-context
  - cross-domain
concerns:
  - privacy
  - safety
  - audit
system_owner:
  - ayla-platform
  - ayla-user-context
source_repository: ayla-knowledge
created: 2026-07-29
updated: 2026-07-29
source_kind: canonical
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: medium
ai_indexing: allowed
export_policy: full
task_id: UX-ADR-002
tags:
  - ayla
  - ayla/architecture
  - ayla/adr
  - adr/0014
  - type/adr
implements:
  - "[[Ayla Constitution]]"
depends_on:
  - "[[Ayla Constitution]]"
  - "[[Ayla Decision Log]]"
  - "[[ADR-0012 Dynamic User Model]]"
related:
  - "[[Ayla MVP Recommendation Contract]]"
review_cycle: event-driven
---

# ADR-0014 Conversation Context ID

## Статус

**Статус документа:** Draft.
**Статус решения:** Proposed — каноническое утверждение не выполнено.
**Версия:** 0.1 (2026-07-29).
**Owner:** Architecture + Platform.
**Task:** UX-ADR-002.

Этот документ — draft ADR. Решение не принято; формулировки подлежат review
Architecture + Platform. Нормативными остаются UX-OD-001…005
(`01 Product/UX MVP/decisions/ux-owner-decisions.md`) и действующие
архитектурные контракты.

## Context

Переходы между поверхностями `bot DM` ↔ `Mini App` (booking, reschedule,
expanded slot picker) сегодня специфицированы как передача набора разрозненных
идентификаторов в deep link: услуга, специалист, даты, `recommendation_id`,
conversation context ref (UX-OD-004; SCR-CUST-006 required_data; stage R4 в
`customer-cancel-reschedule-stages.md`). Состав контекста deep link
формализован слабо: SCR-CUST-006 фиксирует это как assumption (OQ-REC-7), а
механизм deep link Mini App → bot DM открыт как OQ-3 (Platform owner).

Проблемы текущего подхода:

- **Рассинхрон контекста.** Поверхности перечитывают параметры независимо;
  при параллельных изменениях сессии (stale slot, отменённая запись) клиент
  может показать устаревший набор полей.
- **Утечка логики в URL.** Состав и семантика полей deep link становятся
  частью клиентского контракта; любое изменение backend-модели контекста
  требует синхронного обновления deep link во всех точках входа.
- **Сложность расширения.** Каждое новое поле (booking draft, consent state,
  surface hints) добавляется в URL отдельно, раздувая ссылку и увеличивая
  поверхность ошибок.
- **Неопределённый владелец.** OQ-3 показывает: ни состав контекста, ни
  механизм его передачи не закреплены за Platform.

## Decision

Вводится единый opaque идентификатор **`conversation_context_id`**.

- Deep link имеет форму `miniapp://<surface>?ctx=<conversation_context_id>`
  (и зеркально для bot DM entry). Ссылка не несёт бизнес-полей — только
  surface и opaque ID.
- Backend выполняет **resolve**: по `conversation_context_id` восстанавливает
  typed context bundle:
  - `session_id`;
  - `intent_ref`;
  - `recommendation_snapshot_ref` — ссылка на snapshot рекомендации по
    ADR-0013 (Recommendation Snapshot); `recommendation_id` больше не
    передаётся в URL напрямую, а извлекается из snapshot;
  - `booking_draft_ref` — ссылка на черновик записи, если он существует
    (выбранный слот, hold);
  - `allowed_surfaces` — поверхности, на которых bundle валиден.
- **Свойства ID:** не содержит PII, криптографически непредсказуем
  (random, не sequential), single-tenant scoped — resolve возможен только в
  рамках tenant, выдавшего ID.
- **TTL и повторное использование (proposal):** короткий TTL (минуты–часы,
  конкретные значения — Open Question); при успешном resolve выполняется
  refresh TTL (sliding expiration). ID **multi-use** в пределах сессии —
  Phase 1 session-only (UX-OD-003): bundle живёт не дольше сессии и не
  переносится в persistent storage.
- **Security / privacy:**
  - разворачивание контекста — только серверное; клиент не может
    сконструировать или перечислить чужой контекст (ID непредсказуем и
    привязан к tenant);
  - resolve привязан к session/identity вызывающего: чужой `ctx` в чужой
    сессии не разворачивается;
  - expiry или невалидный ID — отказ resolve с fallback в bot DM по правилам
    recovery UX-OD-002 (`return_to_previous_safe_step`, `retry`, `try_later`,
    `exit`); никаких фиктивных состояний.
- **Что НЕ меняется:** UX-OD-004 остаётся в силе полностью — роли поверхностей
  (bot DM: compact slots, confirmation, pending/result; Mini App: expanded
  calendar, management), запрет generic home при известном контексте,
  обязательный stale_slot state, требование preserve `recommendation_id`
  через весь booking flow. Последнее теперь выполняется через
  `recommendation_snapshot_ref` внутри bundle, а не через параметр URL.

## Consequences

**Положительные:**

- Один устойчивый клиентский контракт (`ctx`) вместо N параметров; добавление
  полей контекста не меняет формат deep link.
- Контекст всегда читается из одного источника (backend), что устраняет
  рассинхрон поверхностей и упрощает stale/recovery логику.
- URL перестаёт нести бизнес-данные: меньше утечек через логи, кэши, share.
- Единая точка расширения для будущих поверхностей (push → Mini App, внешние
  каналы) — тот же resolve API.
- Закрывается вопрос владения: механизм deep link и состав контекста
  закрепляются за Platform (OQ-3).

**Отрицательные / издержки:**

- Требуется новый backend resolve API и хранилище bundle с TTL (Platform).
- Дополнительный сетевой вызов при открытии Mini App (resolve перед рендером
  целевого состояния).
- Нужна явная политика expired ctx на каждом экране-потребителе
  (SCR-CUST-006, SCR-CUST-010/011/013).
- Зависимость от ADR-0013: `recommendation_snapshot_ref` предполагает
  наличие snapshot-контракта рекомендации.

## Alternatives

**(a) Полный набор параметров в URL (status quo).** Отклонено: сохраняет
рассинхрон, утечку логики в URL, линейный рост ссылки при добавлении полей;
не закрывает OQ-3.

**(b) Client-side state (контекст хранится на клиенте / в sessionStorage
Mini App).** Отклонено: нет единого источника истины между bot DM и Mini App
(разные runtime), невозможен refresh контекста, теряется привязка к
session/identity, конфликтует с session-only моделью UX-OD-003 (контекст
должен контролироваться сервером и истекать вместе с сессией).

## Open Questions

| # | Вопрос | Кому |
|---|---|---|
| OQ-1 | Владелец и контракт resolve API: endpoint, схема typed context bundle, гарантии консистентности snapshot | Platform owner |
| OQ-2 | Конкретные значения TTL (создание, sliding refresh, max lifetime) и политика multi-use в пределах сессии | Platform + Architecture |
| OQ-3 | Поведение конкретных экранов при expired/invalid ctx: SCR-CUST-006 (slot picker), SCR-CUST-010/011 (records/detail), SCR-CUST-013 (reschedule) — что показывается до fallback в bot DM | UX + Platform |
| OQ-4 | Связь с anonymity Phase 1: достаточна ли привязка к session/identity при отсутствии persistent identity; влияет ли на модель анонимности | Privacy owner + Architecture |
| OQ-5 | Точный формат ссылки в канале MAX (`miniapp://` vs platform-specific scheme) и зеркальный deep link Mini App → bot DM | Platform owner |

## Источники и связь

- UX-OD-002 (recovery/fallback), UX-OD-003 (session-only Phase 1),
  UX-OD-004 (hybrid surface, preserve `recommendation_id`) —
  `01 Product/UX MVP/decisions/ux-owner-decisions.md`.
- Stage R4 + OQ-3 — `01 Product/UX MVP/flows/customer-cancel-reschedule-stages.md`.
- Deep link в expanded slot picker, OQ-REC-7 —
  `01 Product/UX MVP/screens/customer/SCR-CUST-006.md`.
- ADR-0012 (user context), ADR-0013 (Recommendation Snapshot, draft) —
  `05 Architecture/`.
