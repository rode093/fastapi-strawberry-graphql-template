from schema.types.user import User
import uuid
import schema.resolvers
import strawberry


@strawberry.type
class UserQuery:
    @strawberry.field
    def user(self):
        pass
