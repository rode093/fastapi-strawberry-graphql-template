from sqlalchemy.orm import declarative_base
from services.db import DB
from sqlalchemy import Column, String, text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import uuid
Base = declarative_base()


class UserStatus(Base):
    __tablename__ = 'user_statuses'
    __table_args__ = {'schema': 'public'}  # Specify the schema name

    code = Column(String, primary_key=True)
    label = Column(String, nullable=False)
    users = relationship('User')


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'public'}  # Specify the schema name

    id = Column(
        String,
        primary_key=True,
        default=uuid.uuid4()
    )
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    reset_token = Column(String, nullable=True)
    status_code = Column(String, ForeignKey(
        "user_statuses.code"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
