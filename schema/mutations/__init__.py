import strawberry
from schema.mutations.user_status_mutation import UserStatusMutation


@strawberry.type
class BaseMutation(UserStatusMutation):
    pass
