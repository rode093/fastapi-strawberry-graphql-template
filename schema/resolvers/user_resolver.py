from schema.types.user import User
import uuid
from schema.resolvers.user_status_resolver import resolve_user_status


def resolve_user(root):
    return User(id=uuid.uuid4(), first_name="First", last_name="Last", email="email@my.me", status=resolve_user_status('New'), created_at="2023-01-01", updated_at="2023-07-01")
