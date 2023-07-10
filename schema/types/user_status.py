import strawberry
import models


@strawberry.type
class UserStatus:
    code: str
    label: str

    def __init__(self, user_status: models.UserStatus = None) -> None:
        if user_status != None:
            self.code = user_status.code
            self.label = user_status.label
