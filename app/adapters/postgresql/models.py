import uuid
from sqlalchemy import String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from vi_core.sqlalchemy.base_model import Base


class User(Base):
    __tablename__ = "users"

    user_uuid: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
