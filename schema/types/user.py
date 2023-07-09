import typing
import strawberry
from uuid import UUID, uuid4


@strawberry.type
class UserStatus:
    code: str
    label: str


def resolve_user_status(root) -> UserStatus:
    print(root)
    return UserStatus(code="ACTIVE", label="Active")


@strawberry.type
class User:
    id: UUID
    first_name: str
    last_name: str
    email: str
    password: str = None
    reset_token: str = None
    status: UserStatus = strawberry.field(resolver=resolve_user_status)
    created_at: str
    updated_at: str


def resolve_user(root):
    return User(id=uuid4(), first_name="First", last_name="Last", email="email@my.me", created_at="2023-01-01", updated_at="2023-07-01")
