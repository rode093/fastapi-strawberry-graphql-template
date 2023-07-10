import strawberry
from schema.mutations import BaseMutation
from schema.resolvers import Query
from typing import List


schema = strawberry.Schema(
    query=Query,
    mutation=BaseMutation)
