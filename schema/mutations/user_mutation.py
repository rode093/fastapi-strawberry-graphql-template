from datetime import datetime
from email import message
from lib.helpers import compare_password_hash, create_password_hash
from schema.types.authentication import AuthToken
from services.db import DB
import strawberry
from strawberry.field_extensions import InputMutationExtension
from schema.types.user import User
import models
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound


@strawberry.type
class UserMutation():
    @strawberry.mutation(extensions=[InputMutationExtension()])
    def save_user(self, first_name: str, last_name: str, email: str, status: str = "PENDING", password: str = None) -> User:
        user = models.User(first_name=first_name, last_name=last_name,
                           email=email, status_code=status)
        if password != None:
            user.password = create_password_hash(password)
        with Session(DB().engine) as session:
            user.save(session)
            print(user)
            return User(user=user)

    @strawberry.mutation()
    def login(self, email: str, password: str) -> AuthToken:
        with Session(DB().engine) as session:
            try:
                # throws exception is none found
                user = session.query(models.User).where(
                    models.User.email == email, models.User.status_code == 'ACTIVE').one()
                if compare_password_hash(password, user.password):
                    # login successful, generate token
                    token = models.AuthToken(user_id=user.id)  # generate token
                    token.save(session)  # store token in db
                    return AuthToken(token)

            except NoResultFound:
                raise Exception("Authentication Failed")
            raise Exception("Invalid Credentials!")
