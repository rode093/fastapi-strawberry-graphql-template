from services.db import DB
import strawberry
from strawberry.field_extensions import InputMutationExtension
from schema.types.user import User
import models
from typing import List
from sqlalchemy.orm import Session


@strawberry.type
class UserMutation():
    @strawberry.mutation(extensions=[InputMutationExtension()])
    def save_user(self, first_name: str, last_name: str, email: str, status: str = "PENDING", password: str = None) -> User:
        user = models.User(first_name=first_name, last_name=last_name,
                           email=email, status_code=status)
        if password != None:
            user.password = password
        with Session(DB().engine) as session:
            user.save(session)
            print(user)
            return User(user=user)

    # @strawberry.mutation()
    # def delete_user(self, code: str) -> None:
    #     models.UserStatus().delete(code=code)
    #     return None
