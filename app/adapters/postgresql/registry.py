from vi_core import Mapper

from app import entities
from app.adapters.postgresql import models


mapper = Mapper()


def user_to_entity(user: models.User) -> entities.User:
    return entities.User(user_uuid=user.user_uuid, name=user.name, email=user.email)


def user_to_model(user: entities.User) -> models.User:
    return models.User(user_uuid=user.user_uuid, name=user.name, email=user.email)


mapper.register(models.User, entities.User, user_to_entity, True)
mapper.register(entities.User, models.User, user_to_model)
