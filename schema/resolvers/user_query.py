from uuid import UUID
from schema.types.user import User
from typing import List, Optional
import models

import strawberry


@strawberry.type
class UserQuery:
    @strawberry.field
    def user(self, id: UUID) -> User:
        record = models.User().get(id).first()
        return User(record)

    @strawberry.field
    def users(self) -> List[User]:
        records = models.User().all()
        return list(map(lambda record: User(record), records))
