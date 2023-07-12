import strawberry


@strawberry.type
class ErrorResponse:
    code: str
    message: str
