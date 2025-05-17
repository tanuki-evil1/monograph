import uuid
import strawberry
from app import entities

from vi_core.sqlalchemy import AsyncDatabase, UnitOfWork

from app.adapters.postgresql.repositories import UserRepository
from app.settings import settings


@strawberry.type
class UserMutations:
    @strawberry.mutation
    async def create_user(self, name: str, email: str) -> None:
        user = entities.User(name=name, email=email)
        db = AsyncDatabase(settings.database_url)
        async with db.session() as session:
            uow = UnitOfWork(session)
            user_repository = UserRepository(session)
            await user_repository.add_one(user)
            await uow.commit()

    @strawberry.mutation
    async def update_user(self, info: strawberry.Info, user_uuid: uuid.UUID, name: str, email: str) -> None:
        user = entities.User(user_uuid=user_uuid, name=name, email=email)
        db = AsyncDatabase(settings.database_url)
        async with db.session() as session:
            uow = UnitOfWork(session)
            user_repository = UserRepository(session)
            await user_repository.edit_one(user)
            await uow.commit()

    @strawberry.mutation
    async def delete_user(self, info: strawberry.Info, user_uuid: uuid.UUID) -> None:
        db = AsyncDatabase(settings.database_url)
        async with db.session() as session:
            uow = UnitOfWork(session)
            user_repository = UserRepository(session)
            user = await user_repository.find_one(user_uuid=user_uuid)
            if not user:
                raise Exception("User not found")
            await user_repository.delete_one(user)
            await uow.commit()
