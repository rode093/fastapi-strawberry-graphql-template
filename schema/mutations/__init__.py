from schema.mutations.user_mutation import UserMutation
import strawberry
from schema.mutations.user_status_mutation import UserStatusMutation


@strawberry.type
class BaseMutation(UserMutation, UserStatusMutation):
    pass
