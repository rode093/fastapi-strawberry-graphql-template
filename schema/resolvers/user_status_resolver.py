from schema.types.user_status import UserStatus


def resolve_user_status() -> UserStatus:
    return UserStatus(code="ACTIVE", label="Active")
