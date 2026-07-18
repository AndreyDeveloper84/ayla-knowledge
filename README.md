# Ayla Knowledge

Приватный канонический репозиторий знаний продуктовой экосистемы Ayla.

Корень репозитория открывается напрямую как Obsidian vault. Git и GitHub
обеспечивают историю и review, Obsidian — редактирование, навигацию и интерфейс
сравнения.

## Текущий статус

Репозиторий наполняется по одному проверенному документу. Knowledge
Architecture v1.3 остаётся `pending-infrastructure` до завершения Foundation
набора и repository controls.

## Правило версионности

- canonical filename и `node_id` стабильны;
- semantic version хранится во frontmatter и Change Log;
- Git commit идентифицирует точную редакцию;
- tag или release bundle фиксирует согласованный набор документов;
- ручные копии версий внутри vault запрещены.

## Локальная проверка

```powershell
python -m pip install -r requirements-dev.txt
python scripts/validate_knowledge.py
python -m unittest discover -s tests -v
```

## Начать здесь

- [Knowledge Architecture Specification](00%20Foundation/Ayla%20Knowledge%20Architecture%20Specification.md)
- [Ayla Constitution](00%20Foundation/Ayla%20Constitution.md)
- [Machine-readable schema](.knowledge/schema.yaml)
- [Mirror source manifest](.knowledge/sources-manifest.yaml)
