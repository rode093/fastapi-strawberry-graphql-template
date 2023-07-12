from typing import Union
import strawberry


@strawberry.type
class AuthToken:
    access_token: str
    refresh_token: str
    access_token_expires_at: str
    refresh_token_expires_at: str
