import strawberry
from strawberry.field_extensions import InputMutationExtension
from schema.types.user_status import UserStatus
import models


@strawberry.type
class UserStatusMutation():
    @strawberry.mutation(extensions=[InputMutationExtension()])
    def add_user_status(self, code: str, label: str) -> UserStatus:
        status = models.UserStatus(code=code, label=label).save()
        return UserStatus(code=status.code, label=status.label)
