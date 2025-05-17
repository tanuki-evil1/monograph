# Monograph

Проект Monograph представляет собой бэкенд-приложение, реализующее GraphQL API с поддержкой Swagger UI. Приложение построено на основе FastAPI и предоставляет возможность работы с данными через GraphQL и REST API.

## Архитектура проекта

Проект следует принципам чистой архитектуры и разделен на следующие основные компоненты:

- **Entities**: Бизнес-объекты, представляющие доменную модель
- **Use Cases**: Бизнес-логика приложения
- **Adapters**: Адаптеры для работы с внешними сервисами и хранилищами данных
- **Handlers**: Обработчики запросов, представляющие API

### Структура директорий

```
app/
├── adapters/
│   └── postgresql/  # Адаптеры для работы с PostgreSQL
│       ├── models.py        # SQLAlchemy модели
│       ├── repositories.py  # Репозитории для работы с БД
│       └── registry.py      # Маппинг между моделями и сущностями
├── handlers/
│   ├── api/         # REST API
│   │   └── api.py   # Конфигурация FastAPI
│   └── graphql/     # GraphQL API
│       ├── models.py    # GraphQL типы данных
│       ├── mutation.py  # GraphQL мутации
│       └── query.py     # GraphQL запросы
├── usecases/        # Бизнес-логика
├── entities.py      # Доменные модели
└── settings.py      # Настройки приложения
```

## Технологический стек

- **FastAPI**: Web-фреймворк для создания API
- **SQLAlchemy**: ORM для работы с базой данных
- **Strawberry**: Библиотека для создания GraphQL API
- **Alembic**: Инструмент для миграций базы данных
- **PostgreSQL**: Система управления базами данных
- **Vi-Core**: Внутренняя библиотека с общим функционалом

## Установка

### Предварительные требования

- Python 3.12 или выше
- PostgreSQL

### Шаги установки

1. Клонировать репозиторий

2. Создать виртуальное окружение и активировать его:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# или
.venv\Scripts\activate  # Windows
```

3. Установить зависимости:
```bash
pip install -e .
```

4. Создать файл `.env` на основе `.env.example`:
```bash
cp .env.example .env
```

5. Заполнить файл `.env` настройками подключения к базе данных:
```
DATABASE_USERNAME=username
DATABASE_PASSWORD=password
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=database_name
```

6. Запустить миграции:
```bash
make migrate
```

## Запуск приложения

```bash
make run
```

Приложение запустится по адресу http://localhost:8000

## Доступные URL

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **GraphQL Playground**: http://localhost:8000/graphql
- **GraphQL Schema SDL**: http://localhost:8000/graphql/schema

## Использование GraphQL API

### Запросы (Queries)

#### Получение пользователя по UUID
```graphql
query {
  users {
    user(user_uuid: "uuid-значение") {
      user_uuid
      name
      email
    }
  }
}
```

#### Получение списка всех пользователей
```graphql
query {
  users {
    users {
      user_uuid
      name
      email
    }
  }
}
```

### Мутации (Mutations)

#### Создание пользователя
```graphql
mutation {
  users {
    create_user(name: "Иван Иванов", email: "ivan@example.com")
  }
}
```

#### Обновление пользователя
```graphql
mutation {
  users {
    update_user(
      user_uuid: "uuid-значение",
      name: "Новое имя",
      email: "новый@email.com"
    )
  }
}
```

#### Удаление пользователя
```graphql
mutation {
  users {
    delete_user(user_uuid: "uuid-значение")
  }
}
```

## Разработка

### Создание миграций

Для создания новой миграции используйте:

```bash
make al comment="описание миграции"
```

### Применение миграций

```bash
make migrate
```

### Проверка кода

```bash
make check
```

### Модификация GraphQL схемы

Для добавления новых типов и резолверов:
1. Создайте новый файл с моделями данных в `app/handlers/graphql/models.py`
2. Создайте запросы (queries) в `app/handlers/graphql/query.py`
3. Создайте мутации в `app/handlers/graphql/mutation.py`
4. Зарегистрируйте новые типы в `app/handlers/graphql/__init__.py`

### Добавление новых моделей данных

1. Создайте сущность в `app/entities.py`
2. Создайте SQLAlchemy модель в `app/adapters/postgresql/models.py`
3. Добавьте маппинг между моделью и сущностью в `app/adapters/postgresql/registry.py`
4. Создайте репозиторий в `app/adapters/postgresql/repositories.py`
5. Создайте миграцию с помощью Alembic

## Команда разработки

- Команда разработки
