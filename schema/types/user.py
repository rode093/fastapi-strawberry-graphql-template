import typing
import strawberry
from uuid import UUID, uuid4
from schema.types.user_status import UserStatus


@strawberry.type
class User:
    id: UUID
    first_name: str
    last_name: str
    email: str
    password: str = None
    reset_token: str = None
    status: UserStatus
    created_at: str
    updated_at: str
