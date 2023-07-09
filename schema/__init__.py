import strawberry
from schema.types.user import User
from schema.types.user_status import UserStatus
from schema.resolvers.user_resolver import resolve_user
from schema.resolvers.user_status_resolver import resolve_user_status


@strawberry.type
class Query:
    user: User = strawberry.field(resolver=resolve_user)


schema = strawberry.Schema(
    query=Query
)
