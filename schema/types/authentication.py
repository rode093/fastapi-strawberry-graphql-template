import strawberry
import models


@strawberry.type
class AuthToken:
    access_token: str
    refresh_token: str
    access_token_expires_at: str
    refresh_token_expires_at: str

    def __init__(self, token: models.AuthToken) -> None:
        self.access_token = token.access_token
        self.refresh_token = token.refresh_token
        self.access_token_expires_at = token.access_token_expires_at
        self.refresh_token_expires_at = token.refresh_token_expires_at
