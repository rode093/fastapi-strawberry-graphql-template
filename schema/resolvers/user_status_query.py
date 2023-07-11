from schema.types.user_status import UserStatus
from typing import List, Optional
import models

import strawberry


@strawberry.type
class UserStatusQuery:
    @strawberry.field
    def user_status(self, code: str) -> UserStatus:
        record = models.UserStatus().get(code)
        return UserStatus(record)

    @strawberry.field
    def user_statuses(self, codes: Optional[List[str]]) -> List[UserStatus]:
        records = models.UserStatus().all(codes)
        return list(map(lambda record: UserStatus(record), records))
