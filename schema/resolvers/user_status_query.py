from schema.types.user_status import UserStatus
from typing import List
import models

import strawberry


@strawberry.type
class UserStatusQuery:
    @strawberry.field
    def user_status(self, code: str) -> UserStatus:
        print(code)
        record = models.UserStatus().get(code)
        return UserStatus(record)

    @strawberry.field
    def user_statuses(self) -> List[UserStatus]:
        records = models.UserStatus().all()
        return list(map(lambda record: UserStatus(record), records))
