from dataclasses import dataclass, field
import uuid


@dataclass
class User:
    name: str
    email: str
    user_uuid: uuid.UUID = field(default_factory=lambda: uuid.uuid4())
