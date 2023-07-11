import strawberry
from strawberry.field_extensions import InputMutationExtension
from schema.types.user_status import UserStatus
import models
from typing import List


@strawberry.type
class UserMutation():
    @strawberry.mutation(extensions=[InputMutationExtension()])
    def save_user(self, code: str, label: str) -> UserStatus:
        status = models.UserStatus(code=code, label=label).save()
        return UserStatus(code=status.code, label=status.label)

    @strawberry.mutation()
    def delete_user(self, code: str) -> None:
        models.UserStatus().delete(code=code)
        return None
