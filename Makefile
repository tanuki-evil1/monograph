run:
	uvicorn app.handlers.api.api:app --reload --port 8000

check:
	ruff check .
	ruff format --check .
	mypy .

al:
	alembic -c alembic.ini revision --autogenerate -m"$(comment)"

migrate:
	alembic -c alembic.ini upgrade head
