import uuid
import strawberry
from app import entities


@strawberry.type
class UserType:
    user_uuid: uuid.UUID
    name: str
    email: str

    @classmethod
    def from_db(cls, user: entities.User) -> "UserType":
        return cls(user_uuid=user.user_uuid, name=user.name, email=user.email)
