import strawberry
from schema.resolvers.user_status_query import UserStatusQuery


@strawberry.type
class Query(UserStatusQuery):
    pass
