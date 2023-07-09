import strawberry
from schema.types.user import *
@strawberry.type
class Query:
    user: User = strawberry.field(resolver=resolve_user)


schema = strawberry.Schema(
    query=Query
)