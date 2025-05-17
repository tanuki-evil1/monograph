# Monograph

GraphQL API с поддержкой Swagger.

## Установка

```bash
# Создание виртуального окружения
python -m venv .venv
source .venv/bin/activate

# Установка зависимостей
pip install -e .
```

## Запуск

```bash
python main.py
```

Приложение запустится по адресу http://0.0.0.0:8000

## Доступные URL

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **GraphQL Playground**: http://localhost:8000/graphql
- **GraphQL Schema SDL**: http://localhost:8000/graphql/schema

## Использование GraphQL с Swagger

1. Откройте Swagger UI по адресу http://localhost:8000/docs
2. В документации будет раздел "GraphQL" с двумя эндпоинтами:
   - POST /graphql - для выполнения GraphQL запросов
   - GET /graphql - для доступа к GraphQL Playground
   - GET /graphql/schema - для просмотра схемы GraphQL в формате SDL

### Пример GraphQL запроса через Swagger

```graphql
query {
  hello
}
```

Этот запрос должен вернуть:

```json
{
  "data": {
    "hello": "Hello World"
  }
}
```

## Разработка

### Добавление новых типов и резолверов

Для добавления новых GraphQL типов и резолверов, отредактируйте файл `app/handlers/api/api.py` или создайте дополнительные модули в директории `app/adapters/graphql/`.
