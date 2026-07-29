---
node_id: ayla.foundation.canon-governance.ldt-alignment-report
title: LIVING_DIGITAL_TWIN_ALIGNMENT_REPORT
type: specification
status: draft
version: "0.1"
owner: Product Owner
knowledge_area:
  - foundation
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
created: 2026-07-29
updated: 2026-07-29
review_cycle: monthly
---

# Living Digital Twin Alignment Report

**Основание:** AYLA-DEC-0026 — Living Digital Twin as Ayla's Primary Visual Interface
**Кандидат:** `00 Foundation\Ayla Product Essence.md` version 1.1 (READY_FOR_OWNER_REVIEW) на ветке `canon/essence-v1.1-candidate` (commit `6327947`)
**База:** `00 Foundation\Ayla Product Essence.md` version 1.0 (CANONICAL, на основной ветке, не изменена)
**Модель кандидата:** по решению владельца v1.1 готовится на отдельной ветке поверх стабильного файла (версия в поле `version`, имя файла и `node_id` стабильны согласно schema); merge в основную ветку запрещён до owner approval.

## Inputs

- Ayla Product Essence v1.0 — CANONICAL, база для semantic patch.
- AYLA-DEC-0026 (OWNER_DECISION_REGISTER) — DECIDED, содержание изменения.
- Ayla MVP Reset Roadmap — операционный контекст MVP-границы.
- LDT Window Charter, Input Manifest, Outline — контракт окна и карта изменений.

## Preserved v1.0 Decisions

Сохранены без изменений по смыслу (KEEP):

1. Определение Ayla как персонального AI-помощника, а не каталога услуг / чат-бота / фитнес-трекера / медицинского диагноста / системы записи (§1, §3).
2. Человек — главный герой; Twin — отражение, Ayla — помощник, план — путь, прогресс — результат (§4).
3. Роль Ayla: формулирование цели, consent-контекст, объяснение, уровень уверенности, сопровождение без давления и стыда (§5).
4. Инструменты (питание, вода, сон, фитнес, процедуры, специалисты, запись) — не центры продукта (§1, §13).
5. Комплексный путь и декомпозиция в небольшие действия (§11).
6. Принципы поведения Ayla 1–10 дословно (§14).
7. Список «чем Ayla никогда не должна становиться» (§16, дополнен одним пунктом).
8. Главная ценность MVP и проверяемая гипотеза (§17).
9. Transformation Goal — центральная доменная сущность; Booking — downstream-действие, не центр (§20).
10. Главный UX-принцип «понять состояние / связь с целью / следующий шаг» (§19).
11. Каноническая формула продукта (§23) — дословно, без изменений.

## Required Changes

Источник требований: AYLA-DEC-0026, LDT Window Charter (Scope изменений Essence v1.1), LDT Outline (карта изменений), prompt раздел 6. Все 12 пунктов карты Outline выполнены:

| # Outline | Изменение | Статус |
|---|---|---|
| 1 | Уточнить определение Ayla (§1) | DONE |
| 2 | Product Promise (новый §2) | DONE |
| 3 | Living Digital Twin Philosophy: Recognition, Identity Preservation, Authentic Future (§7) | DONE |
| 4 | Усилить Killer Feature + запрет identity drift (§6) | DONE |
| 5 | 12-шаговый цикл + UX-формула (§12) | DONE |
| 6 | Роль функций Food, Water, Sleep, Fitness, Procedures, Specialists, Booking, Memory, Schedule (§13) | DONE |
| 7 | UX-принцип: Twin — главная визуальная поверхность без запрета паттернов (§9, §19) | DONE |
| 8 | Transformation Goal — центральная доменная сущность (§20) | DONE (KEEP/CONFIRM) |
| 9 | Living Digital Twin — центральная долгоживущая визуальная модель (§7, §20) | DONE |
| 10 | Граница состояний source media / observed / facts / reconstruction / inferred / prediction / desired outcome (§8) | DONE |
| 11 | Критерий принятия решений — 7 вопросов (§22) | DONE |
| 12 | MVP-граница: не-обязательства (ruling §13) и минимальные обязательства (ruling §14) без thresholds (§18) | DONE |

## Section-by-Section Change Matrix

| Section v1.1 | Current meaning (v1.0) | Required change | Change type | Basis | Risk | MVP impact | Target wording |
|---|---|---|---|---|---|---|---|
| §1 Что такое Ayla | AI-помощник к желаемой версии себя | Добавить LDT как главный визуальный интерфейс; разграничить Twin/Goal/Ayla | MODIFY | AYLA-DEC-0026 | Twin может быть прочитан как центр продукта | CLARIFY | Twin — поверхность, Goal — центр, Ayla — оркестратор |
| §2 Product Promise | — | Новый принцип ключевого UX | ADD | AYLA-DEC-0026 | Чтение как «fullscreen Twin везде» | CLARIFY | Принцип опыта, не обязательство экрана |
| §3 Проблема | Сохранить | — | KEEP | — | — | NONE | — |
| §4 Главный герой | Человек | Подтвердить; Twin — отражение | KEEP | AYLA-DEC-0026 | — | NONE | — |
| §5 Кто такая Ayla | Сохранить | — | KEEP | — | — | NONE | — |
| §6 Killer Feature | «Персональный цифровой двойник» | Переименовать в Living Digital Twin; запрет identity drift | MODIFY | AYLA-DEC-0026, TERMINOLOGY_ALIGNMENT | — | CLARIFY | Identity drift недопустим |
| §7 Философия LDT | — | Определение + Recognition + Identity Preservation + Authentic Future | ADD | AYLA-DEC-0026 | Классы признаков как acceptance test | NONE | Принципы, не thresholds |
| §8 Разделение состояний | Частично в §12 v1.0 | Явное разделение 7 категорий | ADD | AYLA-DEC-0026, STRUCTURAL_INTEGRATION | Смешение факта и прогноза | CLARIFY | Принцип, не schema |
| §9 Главный визуальный интерфейс | — | Twin — первичная визуальная точка; вспомогательные слои допустимы | ADD | AYLA-DEC-0026 | Запрет карточек/меню | NONE | Без запрета паттернов |
| §10 Living Timeline | — | Временная непрерывность пути | ADD | AYLA-DEC-0026 | Канонизация UI-деталей | NONE | Без морфинга/анимации |
| §11 Как Ayla помогает | Сохранить | — | KEEP | — | — | NONE | — |
| §12 Главный цикл | 9-шаговый цикл | 12-шаговый цикл + UX-формула | MODIFY | AYLA-DEC-0026 | — | CLARIFY | Цикл из ruling §9 |
| §13 Роль функций | 9 функций | Добавить Sleep; роль как поставщиков данных пути | MODIFY | AYLA-DEC-0026, INTERNAL_CONSISTENCY | Разрозненные трекеры | CLARIFY | Отражение в Twin при основаниях |
| §14 Принципы поведения | 10 принципов | + Explainable Transformation | MODIFY | AYLA-DEC-0026 | Ложная причинность | NONE | Не каждая рекомендация меняет Twin |
| §15 Пользовательский контроль | — | «Не похоже на меня», исправление, перестройка, удаление | ADD | AYLA-DEC-0026 | Описание UI/backend | EXPAND | Принцип, не workflow |
| §16 Никогда не должна | 8 пунктов | + симулятор внешности без пути | MODIFY | AYLA-DEC-0026 | — | NONE | — |
| §17 Ценность MVP | Сохранить | — | KEEP | — | — | NONE | — |
| §18 Граница Twin в MVP | 9 обязательств, 6 не-обязательств | 14 минимальных принципов; расширенный список не-обязательств с маркировкой long-term | MODIFY | AYLA-DEC-0026, MVP_BOUNDARY_CLARIFICATION | Long-term как обязательство MVP | RESTRICT | Без thresholds, SLA, scores |
| §19 UX-принцип | 3 задачи экрана | + первичная визуальная точка | MODIFY | AYLA-DEC-0026 | — | CLARIFY | Ссылка на §9 |
| §20 Архитектурный принцип | Transformation Goal | Подтвердить Goal; добавить Twin как визуальную модель | MODIFY | AYLA-DEC-0026 | Twin заменяет Goal | NONE | Два разных центра разных слоёв |
| §21 Иерархия | Essence → Vision → … | + LDT Manifesto после утверждения v1.1 | MODIFY | STRUCTURAL_INTEGRATION | Manifesto выше Essence | NONE | Ниже Essence |
| §22 Критерий решений | 1 вопрос | 7 вопросов | MODIFY | AYLA-DEC-0026 | — | CLARIFY | Узнавание, идентичность, разделение |
| §23 Каноническая формула | Сохранить | — | KEEP | — | — | NONE | Дословно v1.0 |

## Internal Contradictions Resolved

1. **Человек vs Digital Twin** — Twin объявлен отражением и визуальной поверхностью, не героем и не субъектом (§1, §4, §7). Разрешено через AYLA-DEC-0026 (разделение центров).
2. **Digital Twin vs Transformation Goal** — Goal остаётся центральной доменной сущностью; Twin — центральная долгоживущая визуальная модель другого слоя (§20). Разрешено через AYLA-DEC-0026.
3. **Visual interface vs domain entity** — визуальный интерфейс (Twin) и доменная сущность (Goal) явно разведены по слоям (§1, §20).
4. **Fact vs prediction** — разделение состояний (§8), прогноз не выдаётся за факт (§14, §15).
5. **Authentic future vs idealized future** — запрет универсального идеала и идеализированной модели (§7, §16).
6. **MVP vs long-term vision** — не-обязательства маркированы long-term / research / post-MVP (§18).
7. **User control vs autonomous AI** — контроль у пользователя: исправление, перестройка, удаление (§15).
8. **Recognition vs техническая гарантия** — узнавание как принцип, не acceptance test и не обещание совпадения при любых данных (§7).
9. **Explainability vs ложная причинность** — объяснение без утверждения доказанной причинности (§14, §18).
10. **Wellbeing vs body shaming** — body dignity и anti-shaming в MVP-принципах (§18), «без давления и стыда» (§5).

Новых записей в CANON_CONFLICT_REGISTER не потребовалось — все противоречия разрешены лестницей через AYLA-DEC-0026 и Product Essence v1.0.

## MVP Boundary

Воспроизведена без ужесточения и без ослабления (prompt §7–§8, ruling §13–§14):

- 14 минимальных принципов MVP — на уровне принципа, без thresholds, SLA, model scores, обязательного confidence в процентах (§18 v1.1).
- 13 запрещённых MVP-обязательств — перечислены как «MVP не обязан включать» с маркировкой long-term direction / research area / post-MVP (§18 v1.1).
- Видео — только если необходимо качеству модели.

## Long-Term Vision Separated

Отделены и не представлены как обязательства MVP: медицински точная 3D-реконструкция; гарантированное фотографическое совпадение; точная биомеханика; диагностика кожи; точный состав тела по камере; гарантированный прогноз 30/60/90 дней; доказанная причинность действие→визуальное изменение; отображение «энергии»; автостарение; универсальный морфинг; fullscreen Twin на каждом экране; обязательный confidence в процентах; обновление Twin после каждого действия.

## Open P0 Conflicts

NONE

## Owner Decisions Required

NONE

Остаточных стратегических развилок нет: все вопросы разрешены через AYLA-DEC-0026, Product Essence v1.0, MVP boundary и редакционные уточнения. Развилка по модели файла кандидата (version suffix vs schema) решена владельцем: кандидат готовится на отдельной ветке поверх стабильного файла.

## Candidate Status

```text
Document: Ayla Product Essence
Version: 1.1
Status: READY_FOR_OWNER_REVIEW
File: 00 Foundation\Ayla Product Essence.md
Branch: canon/essence-v1.1-candidate (commit 6327947)
Merge: запрещён до owner approval
Supersedes after approval: Ayla Product Essence v1.0
Basis: AYLA-DEC-0026
```

v1.0 на основной ветке не изменена и остаётся CANONICAL до owner approval.

## Verification

- Каждое изменение трассируется к AYLA-DEC-0026 / INTERNAL_CONSISTENCY / STRUCTURAL_INTEGRATION / TERMINOLOGY_ALIGNMENT / MVP_BOUNDARY_CLARIFICATION (см. матрицу).
- v1.0 не редактировалась на основной ветке; MVP Reset Roadmap, OWNER_DECISION_REGISTER, CANON_CONFLICT_REGISTER не изменены.
- Инварианты: человек — главный герой; Twin — отражение и главный визуальный интерфейс; Transformation Goal — центральная доменная сущность; Ayla — помощник и оркестратор; booking — не центр.
- Технические детали (schema, API, UI-контролы, thresholds) из Essence исключены.
- Валидация на ветке кандидата: 0 errors, 21 warnings (все warnings существующие, новых нет). `git diff --check` чист; trailing double-space line breaks из заголовка и §4 v1.0 заменены на обычные строки (editorial, требование чистого diff).

## Owner Review Revision Pass

### Review Verdict

```text
OWNER REVIEW: CHANGES_REQUESTED
P0: 0
P1: 5
Owner Decisions Required: NONE
```

### Required Changes Applied

Все пять обязательных правок применены в commit `9e0a15d` (ветка `canon/essence-v1.1-candidate`):

1. **P1-1 Product Promise (§2)** — абсолютная формулировка «каждый раз открывая Ayla» заменена на устойчивую верхнеуровневую: «Главный пользовательский опыт Ayla начинается с самого человека…». Twin сохранён в ключевых сценариях; технические и служебные экраны выведены из-под UX-обязательства. Основание: OWNER_REVIEW_P1_1, MVP_BOUNDARY_CLARIFICATION.
2. **P1-2 Killer Feature (§6)** — «точка объединения всех доменов продукта» заменена на «согласованное отражение состояния, прогресса и данных из разных областей продукта». Twin объединяет восприятие, не владеет доменами; Transformation Goal остаётся доменным центром. Основание: OWNER_REVIEW_P1_2, INTERNAL_CONSISTENCY.
3. **P1-3 Архитектурное определение (§20)** — «центральная долгоживущая визуальная модель продукта» заменена на «основная долгоживущая визуальная модель пользователя». Слово «центральная» закреплено только за Transformation Goal; Twin явно моделирует пользователя. Основание: OWNER_REVIEW_P1_3, TERMINOLOGY_ALIGNMENT.
4. **P1-4 Иерархия документов (§21)** — линейная схема заменена нелинейной: Manifesto, Vision, Thesis, Principles — sibling-документы под Essence; MVP Scope строится на совокупности Vision+Thesis+Principles. Manifesto — authoritative input, не родитель Vision/Thesis/Principles. Основание: OWNER_REVIEW_P1_4, STRUCTURAL_INTEGRATION.
5. **P1-5 MVP-граница (§18)** — вводный текст делегирует точный состав реализации в MVP Scope; требования разделены на Core value (6), Trust and control (7), Conditional input (видео — только при подтверждённой необходимости). Список «MVP не обязан включать» сохранён. Основание: OWNER_REVIEW_P1_5, MVP_BOUNDARY_CLARIFICATION.

### Additional Editorial Clarifications

1. **§12 Product loop** — «визуальный и измеримый прогресс» → «визуальный прогресс и подтверждённые изменения состояния» (не обещать обязательную измеримость любого прогресса).
2. **§14 Explainable Transformation** — «основания для наблюдаемого изменения» → «доступные данные, основания интерпретации и ограничения вывода» (снижение риска ложной причинности).
3. **Frontmatter dependency (9.3)** — проверена `.knowledge/schema.yaml`: поля для owner decision references нет (relationships: depends_on, supersedes, implements, adr — только для ADR-типов, related, conflicts_with). Schema не изменена; неподдерживаемое поле не добавлено; `depends_on` для Owner Decision не используется. Ссылка на AYLA-DEC-0026 сохранена в статусном блоке документа («Основание: AYLA-DEC-0026»).

### Remaining P0

0

### Remaining P1

0

### Candidate Status

```text
Document: Ayla Product Essence
Version: 1.1
Status: READY_FOR_OWNER_REVIEW
Branch: canon/essence-v1.1-candidate
Commits: 6327947 (initial candidate) → 9e0a15d (owner review revision)
File: 00 Foundation\Ayla Product Essence.md
Merge: запрещён до owner approval
```

### Verification

- Проверки перед правками: ветка `canon/essence-v1.1-candidate`, базовый commit `6327947` — совпали.
- Все 5 P1 и 2 editorial-правки применены; исходная матрица Alignment Pass не переписывалась.
- Frontmatter кандидата не изменён: `version: "1.1"`, `status: review`, `canonical_status: candidate`; filename и `node_id` стабильны.
- Валидация после правок: 0 errors, 21 warnings (все существующие, новых нет); `git diff --check` чист.
- Product Essence v1.0 на основной ветке не изменена; schema, validator, запрещённые файлы не затронуты; unrelated changes не staged.
- Merge и push не выполнялись; CANONICAL не присвоен; blocker не снят.
