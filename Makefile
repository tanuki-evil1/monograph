run:
  uvicorn app.handlers.api.api:app --reload --port 8000

check:
  ruff check .
  ruff format --check .

install:
  uv sync --no-dev

al:
  alembic -c alembic.ini revision --autogenerate -m"$(comment)"

upgrade:
  alembic -c alembic.ini upgrade head
