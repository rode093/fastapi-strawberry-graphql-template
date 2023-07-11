import strawberry
from strawberry.field_extensions import InputMutationExtension
from schema.types.user_status import UserStatus
import models
from typing import List


@strawberry.type
class UserStatusMutation():
    @strawberry.mutation(extensions=[InputMutationExtension()])
    def save_user_status(self, code: str, label: str) -> UserStatus:
        status = models.UserStatus(code=code, label=label)
        status.save()
        return status

    @strawberry.mutation()
    def delete_user_status(self, code: str) -> None:
        models.UserStatus().delete(code=code)
        return None

    @strawberry.mutation()
    def delete_user_statuses(self, codes: List[str]) -> None:
        models.UserStatus().deleteMany(codes=codes)
        return None
