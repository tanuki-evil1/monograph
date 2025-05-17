from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from vi_core.sqlalchemy import SessionHelper

from app import entities
from app.adapters.postgresql import models
from app.adapters.postgresql.registry import mapper


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.helper = SessionHelper[models.User](session)

    async def add_one(self, new_user: entities.User) -> None:
        await self.helper.save(mapper.map(new_user, models.User))

    async def edit_one(self, user: entities.User) -> None:
        await self.helper.update(mapper.map(user, models.User))

    async def delete_one(self, user: entities.User) -> None:
        await self.helper.delete(mapper.map(user, models.User))

    async def find_one(self, **kwargs) -> entities.User | None:
        stmt = select(models.User).filter_by(**kwargs)
        instance = await self.helper.one(stmt)
        return mapper.map(instance, entities.User) if instance else None

    async def find_all(self) -> list[entities.User]:
        stmt = select(models.User)
        instances = await self.helper.all(stmt)
        return [mapper.map(instance, entities.User) for instance in instances]
