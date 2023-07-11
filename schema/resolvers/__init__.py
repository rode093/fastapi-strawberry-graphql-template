import strawberry
from schema.resolvers.user_status_query import UserStatusQuery
from schema.resolvers.user_query import UserQuery


@strawberry.type
class Query(UserQuery, UserStatusQuery):
    pass
