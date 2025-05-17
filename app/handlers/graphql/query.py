import uuid
import strawberry

from vi_core.sqlalchemy import AsyncDatabase

from app.handlers.graphql.models import UserType

from app.adapters.postgresql.repositories import UserRepository
from app.settings import settings


@strawberry.type
class UserQuery:
    @strawberry.field
    async def user(self, info: strawberry.Info, user_uuid: uuid.UUID) -> UserType | None:
        db = AsyncDatabase(settings.database_url)
        async with db.session() as session:
            user_repository = UserRepository(session)
            user = await user_repository.find_one(user_uuid=user_uuid)
            return UserType.from_db(user) if user else None

    @strawberry.field
    async def users(self, info: strawberry.Info) -> list[UserType]:
        db = AsyncDatabase(settings.database_url)
        async with db.session() as session:
            user_repository = UserRepository(session)
            users = await user_repository.find_all()
        return [UserType.from_db(user) for user in users]
