import strawberry


@strawberry.type
class UserStatus:
    code: str
    label: str
