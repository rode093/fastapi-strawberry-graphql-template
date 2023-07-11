import typing
import strawberry
from uuid import UUID, uuid4
from schema.types.user_status import UserStatus
import models


@strawberry.type
class User:
    id: UUID
    first_name: str
    last_name: str
    email: str
    status: UserStatus
    created_at: str
    updated_at: str

    def __init__(self, user: models.User = None) -> None:
        if user != None:
            self.id = user.id
            first_name = user.first_name
            last_name = user.last_name
            email = user.email
            status = models.UserStatus.get(user.status_code)
            created_at = user.created_at
            updated_at = user.updated_at
