---
node_id: ayla.knowledge.pr21-transfer-kb-e-2026-09-21
title: PR 21 Transfer Table — KB-E — 2026-09-21
type: specification
status: draft
canonical_status: draft
version: "1.0"
owner: Canon Architect / Knowledge Base Auditor (agent)
knowledge_area:
  - foundation
domain:
  - cross-domain
concerns:
  - governance
  - audit
system_owner:
  - ayla-knowledge
source_repository: ayla-knowledge
created: 2026-09-21
updated: 2026-09-21
source_kind: canonical
classification: internal
data_sensitivity: none
data_categories:
  - none
security_sensitivity: low
ai_indexing: allowed
export_policy: sanitized
review_cycle: event-driven
---

# Перенос из ayla-knowledge PR #21 в KB-E (DRF-2263)

**Дата:** 2026-09-21 · **PR #21:** `canon/recommendation-v1.0-proposed`,
голова `dfd9595d`, база `207eeb63` (13 файлов, +1192/−192). PR #21 не
сливается; после подтверждения владельцем он закрывается как superseded
этим PR, ветка до окончания проверки не удаляется.

## Основания

- **Решение владельца по #21** (`docs/orch1.md`, журнал главного окна
  CD §68, вне git): перенести только части, которые не противоречат
  K-1…M-1, и перечислить перенесённое, изменённое и отброшенное.
- **Решение владельца 21.09** (журнал главного окна CD §71, вне git),
  дословно:
  - п.1 — «оставить до отдельного решения и вынести в отдельный PR… Текущий
    PR должен содержать только изменения, необходимые для фиксации K‑1…M‑1»;
  - п.2 — «Семейства ADDRESS / SUPPORT / RECOVER / OBSERVE до пилота не
    включать»;
  - п.3 — «Без цели Ayla не предлагает и не создаёт план по своей
    инициативе. Такой план может собрать только сам пользователь. Это
    правило P‑1 имеет приоритет над старым текстом PR #21».
- **Решения AYLA-DEC-0087…0101** — [[OWNER_DECISION_REGISTER]]; бриф
  `OWNER_DECISION_BRIEF_GOAL_PLAN_DIARY` ред. 2, Итог 3 п.2, 11, 14, 16.
- **Таблица проверки #21** (рабочий файл оркестратора
  `PR21_TRANSFER_TABLE.md`, вне git) — номера строк ниже совпадают с ней.

## Вердикты

- **ПЕРЕНЕСЕНО** — перенесено без изменения смысла.
- **ИЗМЕНЕНО** — перенесено с изменением; как — в строке.
- **ОТБРОШЕНО** — не переносится; причина в строке.
- **ВНЕ ПРЕДМЕТА** — не нужно для K-1…M-1; отложено в отдельный PR по
  CD §71 п.1. Это не отброс: решение по сути остаётся за владельцем.

## Сводка

| Вердикт | Строк |
|---|---|
| ПЕРЕНЕСЕНО | 3 |
| ИЗМЕНЕНО | 20 |
| ОТБРОШЕНО | 4 |
| ВНЕ ПРЕДМЕТА | 41 |
| **Всего** | **68** |

**Счёт строк.** В таблице проверки и в вопросе к владельцу (CD §71)
названо 69 дельт: 8 / 20 / 1 / 40. Перечисление строк той же таблицы даёт
68: 8 / 20 / 1 / **39** «вне предмета». Расхождение — в итоговой строке
«40»; сами строки (1.1…13.1) пересчитаны по одной.

**Отличия от вердиктов таблицы проверки** (все — по решениям, принятым
после неё, или по CD §71 п.1):

- 1.25, 2.7 (семейства provisional) — было «С ИЗМ.», стало ОТБРОШЕНО:
  CD §71 п.2 закрыл противоречие П-2 — после пилота.
- 1.19, 1.21, 1.24 — ПЕРЕНЕСЕНО, как в таблице.
- 1.7 (Semantic Resolution) — было «КАК ЕСТЬ», стало ВНЕ ПРЕДМЕТА — KB-F
  (DRF-2270): вместе с этапом Semantic Resolution в RC приходили этап 4
  «Adaptive Clarification семантики», `resolution_status` и режимы
  `SKIP / CONFIRM_ONE / CHOOSE_MANY / ASK_CONTEXT` (WD §20 D-6 / D-10),
  которых нет ни в DEC-0087, ни в брифе Итог 3 п.14. Для фиксации K-1 их не
  требуется: Goal optional выражен в существующих этапах 3–4 и §27–§29
  (CD §71 п.1). Рецензия KB-E, R-5 / A-1.
- 1.22 — было «КАК ЕСТЬ», стало ИЗМЕНЕНО: перенесено только «анкета не
  обязательный вход»; «C03 = адаптивный DecisionReadiness flow» — часть A2.
- 2.3 — было «КАК ЕСТЬ», стало ИЗМЕНЕНО: файл Final Reconciliation не
  переносится (2.1), смысл строки — в RC §27.
- 2.10 — было «КАК ЕСТЬ», стало ОТБРОШЕНО: дублирует действующий RC v0.4
  §31 и Decision Policy Contract; файл FR не переносится.
- 5.9 (`SAFETY_CLARIFY`) — было «КАК ЕСТЬ», стало ВНЕ ПРЕДМЕТА: правило B6
  для K-1…M-1 не нужно (CD §71 п.1), Recommendation UX Addendum в KB-E не
  правится; уходит в отдельный PR вместе с B6 из 1.16.
- 1.4, 1.8, 1.9, 1.16, 1.23 — ИЗМЕНЕНО уже, чем предлагала таблица:
  DecisionReadiness, четыре состояния safety, `UNKNOWN` fail-closed и B6
  (всё — A2 / канон v1.1) не переносятся; перенесено только то, что
  требуют DEC-0096, 0097, 0100.

## Таблица

### 1. `05 Architecture/Ayla MVP Recommendation Contract.md` → v0.5

| # | Дельта #21 | Вердикт | Основание |
|---|---|---|---|
| 1.1 | frontmatter v1.0, review / candidate; шапка «v1.0 = v0.4 + A1 + A2» | ИЗМЕНЕНО — версия v0.5, статус draft / proposed не изменён; шапка описывает только перенесённое | CD §71 п.1; бриф Итог 3 п.14 |
| 1.2 | §3 `decision_subject` = NBA/WHAT, `action_type` → ExecutionOption (B2) | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 1.3 | §3 `target_outcomes` = DesiredOutcome refs | ОТБРОШЕНО — оставлены рабочие коды v0.4 + пометка DEC-0094 | AYLA-DEC-0094 |
| 1.4 | §3 `readiness_state` (DecisionReadiness) | ИЗМЕНЕНО — поле не переносится (A2); поля исхода DEC-0097 — ссылкой на одну запись DecisionOutcome (§3, §32), без копии в Recommendation | AYLA-DEC-0097; CD §71 п.1 |
| 1.5 | §3 `safety_policy_version`, `catalog_mapping_version`, `safety_evaluation` ref | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 1.6 | §3 `expires_at` → `actionable_until`; retention — политика | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 1.7 | §5 этап 3 Semantic Resolution, Goal optional, не синтезируется | ВНЕ ПРЕДМЕТА — KB-F (DRF-2270): объединённый этап Semantic Resolution, этап 4 «Adaptive Clarification семантики», `resolution_status` и режимы уточнения (WD D-6 / D-10) для K-1 не нужны. Goal optional в §5 этапах 3–4 записан прямо по DEC-0087 (как 1.19, 1.21), без механики #21 | CD §71 п.1; AYLA-DEC-0087 |
| 1.8 | §5 этапы 7–8 → DecisionReadiness; shadow mode C1 | ИЗМЕНЕНО — этапы 7–8 не заменяются; перенесено разведение: тень DecisionReadiness ≠ выбор DEC-0097 (§30); соответствие исходов дано для `RecommendationResult` (§32, OQ-R13) | AYLA-DEC-0097; CD §71 п.1 |
| 1.9 | §5 этап 2 consent, этап 9 «сквозной» safety с 4 состояниями | ИЗМЕНЕНО — ступень 1 до этапа 1; этап 9 = ступень 3 «расширенная safety»; 4 состояния не переносятся | AYLA-DEC-0096 |
| 1.10 | §5 этап 16: VERIFIED-eligibility, `NO_VERIFIED_CANDIDATES` | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 1.11 | §7 три логических снимка; ADR-0013 superseded | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 1.12 | §8 eligibility только VERIFIED; staged ranking | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 1.13 | §10 альтернативы только действием пользователя | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 1.14 | §14/§15/§17: `accepted` / `declined` сняты; новые interaction-события; `booking_intent.created` | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 1.15 | §22 `actionable_until` 2 ч; инвариант D4 `MATERIAL_CHANGE` | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 1.16 | §23 safety 4 состояния + `UNKNOWN` / `NOT_APPLICABLE`; B6; «гейтов два» | ИЗМЕНЕНО — перенесено: ссылка на ступень 1; аллергический фильтр ко всем кандидатам с составом, включая неизвестный или неполный (`UNKNOWN`), `CONFLICT / NO_CONFLICT_FOUND / UNKNOWN`, `UNKNOWN` ≠ «безопасно» и ≠ состояние safety, аллергии вне текста модели, журнал доступа. B6 и 4 состояния — отдельный PR | AYLA-DEC-0096, 0100; CD §71 п.1 |
| 1.17 | §25 replay по трём снимкам; OQ ADR-0013 | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 1.18 | §26 OQ-R9: retention отдельно от TTL | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 1.19 | §27 Goal optional, без синтеза; «Создать цель» вне конвейера | ПЕРЕНЕСЕНО — §27 | AYLA-DEC-0087; [[Ayla Goal and Desired Outcome Contract]] (таблица переходов) |
| 1.20 | §28 `SemanticResolutionResult`, `desired_outcomes ≥ 1`, термин `DesiredOutcome` | ИЗМЕНЕНО — перенесено только: Outcome Resolution не требует Goal, goal 0..1, outcomes 0..N (рабочие коды); условие `≥ 1` и `DesiredOutcome` — отброшены (DEC-0094); `SemanticResolutionResult`, `resolution_status` и маппинг на clarification — вне предмета, KB-F (DRF-2270), как 1.7 | AYLA-DEC-0087, 0094; CD §71 п.1 |
| 1.21 | §29 `goal` optional; отсутствие Goal ≠ `INSUFFICIENT_CONTEXT` | ПЕРЕНЕСЕНО — §29 | AYLA-DEC-0087 |
| 1.22 | §30 анкета не обязательный вход; C03 — адаптивный поток | ИЗМЕНЕНО — перенесено «анкета не обязательный вход»; «C03 = DecisionReadiness flow» (A2) — нет | AYLA-DEC-0087; CD §71 п.1 |
| 1.23 | §30 DecisionReadiness, 5 состояний, shadow | ИЗМЕНЕНО — как 1.8: только разведение тени и выбора DEC-0097, CLARIFY vs NO_ACTION | AYLA-DEC-0097; CD §71 п.1 |
| 1.24 | §31 Goal — controlled priority, не override | ПЕРЕНЕСЕНО — §31 | AYLA-DEC-0087 |
| 1.25 | §26 OQ-R11 / §33: семейства provisional для пилота | ОТБРОШЕНО — семейства до пилота не включаются (§26, §33) | CD §71 п.2; AYLA-DEC-0097 |
| 1.26 | §33/§34 WHAT / HOW / WHO; C04 без услуги; коды C01–C05 | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 1.27 | Change Log v1.0 | ИЗМЕНЕНО — журнал v0.5 собран по фактически перенесённому, со ссылкой на #21 и DEC | CD §68, §71 |

### 2. `05 Architecture/Recommendation Architecture Final Reconciliation.md` (новый в #21)

Файл целиком не переносится (2.1). Строки 2.2–2.10 касаются K-1…M-1; их
смысл внесён в Recommendation Contract, текст копии FR не создаётся.

| # | Дельта #21 | Вердикт | Основание |
|---|---|---|---|
| 2.1 | Узел KB Final Reconciliation целиком | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 2.2 | `target_outcomes` DesiredOutcome refs в минимуме пилота | ИЗМЕНЕНО — смысл в RC §3, §28: не DesiredOutcome, пометка DEC-0094 | AYLA-DEC-0094 |
| 2.3 | «Создать цель» вне конвейера; S10 «рекомендация без Goal» | ИЗМЕНЕНО — смысл в RC §27; файл FR не переносится | AYLA-DEC-0087; [[Ayla Goal and Desired Outcome Contract]] (таблица переходов) |
| 2.4 | safety input → согласие → safety gate | ИЗМЕНЕНО — смысл в RC §5, §23 (ступень 1; доступ к аллергиям) | AYLA-DEC-0096, 0100 |
| 2.5 | DecisionReadiness в shadow mode | ИЗМЕНЕНО — смысл в RC §30: тень ≠ выбор DEC-0097 | AYLA-DEC-0097 |
| 2.6 | `NO_ACTION` в `result_status`; `no_action` как NBA | ИЗМЕНЕНО — имена разведены в RC §32 | AYLA-DEC-0097 |
| 2.7 | семейства provisional для пилота | ОТБРОШЕНО — до пилота не включаются | CD §71 п.2 |
| 2.8 | вариант исполнения `plan` для любого NBA, NBA без Goal | ИЗМЕНЕНО — RC §34: без цели Ayla план не предлагает; только сам пользователь | AYLA-DEC-0091; CD §71 п.3 |
| 2.9 | LLM формулирует WHY на слоях 1–3, 9 | ИЗМЕНЕНО — RC §23: аллергии в текст модели, включая WHY, не попадают | AYLA-DEC-0100 |
| 2.10 | LLM не участвует в решении | ОТБРОШЕНО — дублирует действующий RC v0.4 §31 и Decision Policy Contract («модель только формулирует выбранное») | AYLA-DEC-0097 |
| 2.11 | прочие слои, инварианты, конфликты, ходы, O1–O2 | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |

### 3. `05 Architecture/Ayla Domain Event Registry.md` → v0.6

| # | Дельта #21 | Вердикт | Основание |
|---|---|---|---|
| 3.1 | шапка «Draft v0.6» при frontmatter `1.0-draft` | ИЗМЕНЕНО — одна версия `0.6` во frontmatter и шапке (цепочка Change Log v0.1…v0.5) | бриф Итог 3 п.11 |
| 3.2 | `recommendation.accepted` / `.declined` → deprecated | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 3.3 | + `recommendation.explanation_requested`, `.alternative_requested`, `.engaged` | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 3.4 | + `booking_intent.created` | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 3.5 | §7/§8/§12/§13 под B8 | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 3.6 | Change Log «v0.6 (2026-09-12)» | ИЗМЕНЕНО — v0.6 занята записью волны DEC (события этапа C); B8 не входит | бриф Итог 3 п.11 |

### 4. `05 Architecture/ADR-0013 Recommendation Snapshot.md`

| # | Дельта #21 | Вердикт | Основание |
|---|---|---|---|
| 4.1 | superseded-proposed; OQ 1–5 → RC §25 | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |

### 5. `01 Product/UX MVP/contracts/recommendation-ux-addendum.md`

| # | Дельта #21 | Вердикт | Основание |
|---|---|---|---|
| 5.1 | frontmatter v0.2 | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 5.2 | шапка WHAT → HOW → WHO | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 5.3 | §1.1 C04 / §1.2 C05 | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 5.4 | §2 → контракт §13 | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 5.5 | §3 view-model, TTL, таксономия событий | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 5.6 | + `NO_VERIFIED_CANDIDATES` | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 5.7 | + `INSUFFICIENT_CONTEXT`: «один вопрос C03 или “пока не могу”» | ИЗМЕНЕНО — правило внесено в RC §30, §32: вопрос = `CLARIFY`; иначе `NO_ACTION` / `BLOCKED` с причиной; Addendum в KB-E не правится | AYLA-DEC-0097 |
| 5.8 | `NO_CANDIDATES`; `SAFETY_BLOCKED` = `SAFETY_BOUNDARY` | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 5.9 | + `SAFETY_CLARIFY` (B6) | ВНЕ ПРЕДМЕТА — отдельный PR вместе с B6 (1.16) | CD §71 п.1 |
| 5.10 | `HEALTH_CHECK_*`, `MATERIAL_CHANGE` | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 5.11 | статусы OQ-REC-1…7 | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 5.12 | критерии приёмки 1–3a | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 5.13 | источники, Changelog v0.2 | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |

### 6. `01 Product/BOT-003 Discovery and Recommendation Conversation Specification.md`

| # | Дельта #21 | Вердикт | Основание |
|---|---|---|---|
| 6.1 | frontmatter review v0.2; «PROPOSED v1.0» | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 6.2 | sufficiency = DecisionReadiness | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 6.3 | §20 блок v0.2 | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |

### 7–8. Архивные review

| # | Дельта #21 | Вердикт | Основание |
|---|---|---|---|
| 7.1 | `recommendation-owner-review-001.md` → archived | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 8.1 | `recon-recommendation-contract-001.md` → archived | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |

### 9–10. Journey

| # | Дельта #21 | Вердикт | Основание |
|---|---|---|---|
| 9.1 | путь `approved_v1_1.md` → `history/` в шапке Journey | ВНЕ ПРЕДМЕТА — отдельный PR. Journey v1.3 в KB-E этот ханк не трогает; если B14 примут, отдельный PR правит ту же шапку | CD §71 п.1 |
| 10.1 | перенос `approved_v1_1.md` в `history/` | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |

### 11–12. Intent-контракты

| # | Дельта #21 | Вердикт | Основание |
|---|---|---|---|
| 11.1 | `intent-output.schema.json` description → approved | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |
| 12.1 | `intent-registry.yaml` status → approved | ВНЕ ПРЕДМЕТА — отдельный PR | CD §71 п.1 |

### 13. `05 Architecture/Ayla Goal Outcome Semantic Model Working Design.md`

| # | Дельта #21 | Вердикт | Основание |
|---|---|---|---|
| 13.1 | шапка «дельты §20 применены A1; D-8 закрыт B9» | ИЗМЕНЕНО — одна заметка: DEC-0094 (Desired Outcome не активируется) + фактический перечень перенесённых «WD §20 D-n»; фраза о B9 не переносится; статус и версия не изменены | AYLA-DEC-0094; бриф Итог 3 п.16; CD §71 п.2 |

## Что добавлено по решениям, без источника в #21

- **Journey v1.3:** цель необязательна (в том числе в первом пункте
  IN_SCOPE); План и Дневник — сквозные необязательные концепции;
  proactive-уведомления по opt-in (Gates и оговорка этапа 13); полный
  состав продукта по DEC-0087 в IN_SCOPE, Food Scanner — IN_SCOPE (этап 1);
  область «consent/privacy → safety»; food и water убраны из DEFERRED
  (AYLA-DEC-0087, 0088, 0091, 0095, 0096).
- **Domain Event Registry v0.6:** 18 записей `proposed` — `goal.*` (3),
  `plan.*` (4), `diary.day.*` (2), `food.entry.*` (3),
  `water.entry.recorded`, `decision.evaluated`, `memory.allergy.*` (4);
  OQ-E8…E12.
- **`system.*` (бриф Итог 3 п.11, CD §64)** — в реестр не внесён:
  `system.module.health.degraded` описан в контракте событий бота
  (`docs/architecture/event-contract.md`, слито ai-bot-platform #1946);
  регистрация в DER — отдельным шагом, OQ-E11.

## Отдельный PR (CD §71 п.1)

41 строка «ВНЕ ПРЕДМЕТА» (39 из таблицы проверки + 5.9 + 1.7) — полезные
изменения #21, которые владелец велел собрать отдельно, описать простыми словами и представить на
самостоятельное утверждение. В KB-E они не входят. Владелец отвечал на
вопрос о «40» (фактически 39 строк); 5.9 и 1.7 отложены сверх множества,
о котором спрашивали. 1.7 (и часть 1.20 о `SemanticResolutionResult`) —
KB-F, DRF-2270.
