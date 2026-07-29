---
screen_id: SCR-CUST-001
name: Welcome / Entry (приветствие, категории, свободный ввод)
version: "0.1"
status: draft
task_id: UX-CUST-002a
readiness: READY_WITH_ASSUMPTIONS
sources: [SRC-02 (UJS этапы 1–2), UX-OD-003, UX-OD-005, PC §4–5 (draft), design-wave-1a §3–4]
node_id: ayla.ux.scr-cust-001
title: SCR-CUST-001 — Welcome / Entry
type: specification
owner: UX Architecture
domain:
  - conversation
system_owner:
  - ayla-conversation
  - ayla-mini-app
knowledge_area:
  - product
source_repository: ayla-knowledge
source_kind: product-requirements
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: full
updated: 2026-07-29
review_cycle: monthly
---

# SCR-CUST-001 — Welcome / Entry

- **actor:** User (гость, без регистрации на этом экране)
- **surface:** bot DM (MAX; сообщения + inline-кнопки)
- **mvp_flow:** Happy Path Booking (Wave 1A.1), этап 1 Entry → этап 2 First interaction

## purpose
Первая точка контакта: принять потребность пользователя (категория или
свободный текст) и запустить диалог. Не анкета, не регистрация, не продажа.

## user_goal
Получить помощь с beauty-потребностью без поиска по каталогу и без заполнения
форм (SRC-02 этап 1).

## primary_action
Отправить запрос: выбрать категорию кнопкой **или** написать свободный текст →
переход в SCR-CUST-003 (intent detection).

## secondary_actions
- Открыть полный текст политики (Transparency-уровень) по ссылке «Подробнее»
  (progressive disclosure).
- Перейти в Mini App (landing — SCR-CUST-010 по UX-OD-005, вне scope этого
  экрана).

## required_data
- Текст приветствия + короткое позиционирование Ayla (1–2 фразы, без обещания
  памяти — persistent memory off, UX-OD-003).
- Список категорий для inline-кнопок (assumption A3).
- Одна строка privacy-уведомления (уровень **Notice** в модели Transparency →
  Notice → Consent) + ссылка «Подробнее» (уровень **Transparency**) —
  PC §4.1–4.3, draft-текст N1 — assumption A2.

## key_components
- Приветственное сообщение (персона Ayla, тёплый тон, без анкеты).
- Inline-кнопки категорий (компактно, ≤1 экран).
- Поле свободного ввода (нативное для bot DM).
- Notice-строка ПДн (уровень Notice; активное уведомление в точке обработки,
  не запрос согласия — Consent-уровень в Phase 1 отсутствует): «Я обрабатываю
  то, что ты пишешь, чтобы помочь с записью. Всё, что ты говоришь, живёт
  только в этом диалоге. Подробнее — [ссылка]» (draft, PC §5 N1). Не
  блокирует диалог.

## states
1. **default** — приветствие + категории + ввод + notice-строка. Действия:
   выбрать категорию, написать текст, открыть «Подробнее».
2. **loading** — запрос отправлен, Ayla обрабатывает (индикатор набора/typing).
   Действия: ждать; повторный ввод не требуется.
3. **error** — канал не доставляет сообщение / сбой платформы MAX. Честное
   сообщение о сбое; действие: повторить позже (повторная доставка при
   следующем открытии — proposal в UJS этап 1, assumption A4). Без
   альтернативного канала в MVP.

## dependencies
- UX-OD-003: session-only + service_necessity; запрещены формулировки
  «запомню», анкета, consent-экран.
- UX-OD-005: Mini App entry приземляется на SCR-CUST-010 (не этот экран).
- PC §4–5 (draft): notice-точка и текст — до approval Privacy Owner.
- Далее: SCR-CUST-003.

## assumptions
- **A1.** Copy приветствия — рабочее допущение до revalidation UX-OD-003
  (accepted_as_temporary_assumption, revalidation before release).
- **A2.** Текст notice — draft N1 из PC §5; финальная формулировка — Privacy
  Owner (OQ Privacy Q2: достаточность уровней Transparency + Notice без
  Consent-момента; Q10: классификация этой точки как Notice — предложение,
  не решение). Уровневая модель Transparency → Notice → Consent — owner
  ruling 2026-07-29; уровень этой точки — assumption до подтверждения
  Privacy Owner.
- **A3.** Точный состав категорий каноном не зафиксирован (seed catalog
  пилота) — дизайнер закладывает 3–6 кнопок, состав уточняет Product Owner.
- **A4.** Поведение при недоставке (retry при следующем открытии) — proposal
  в SRC-02 этап 1.

## blockers
Нет screen-level блокеров. Release-level: UX-GAP-0101 (consent-модель) —
не блокирует дизайн при UX-OD-003.

## design_notes
- Запрещено (SRC-02 этап 1 Forbidden Behavior): запрашивать имя/возраст/вес,
  начинать с анкеты, продавать.
- Запрещено (wave-1a §4): consent-экран, копирайт «запомню предпочтения» из
  stale-спек SRC-12, wellness/food-навигация.
- Один первый экран = один шаг до диалога; никаких onboarding-шагов S3–S5
  (DEFERRED).

## changelog
- 2026-07-29 — UX-REFINE-001: privacy-точка приведена к трёхуровневой
  терминологии Transparency → Notice → Consent (owner ruling 2026-07-29):
  welcome-строка — уровень Notice, «Подробнее» — Transparency; классификация
  помечена как assumption до подтверждения Privacy Owner (Q2/Q10).
