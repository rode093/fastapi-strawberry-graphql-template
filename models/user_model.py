from enum import unique
from operator import index
import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
import models
from models.base_model import Base
from sqlalchemy.orm import Session, relationship, Mapped
from services.db import DB
from datetime import datetime
from sqlalchemy.dialects import postgresql
from lib.helpers import create_password_hash
from typing import List
from models.auth_token import AuthToken
import typing


class User(Base):
    __tablename__ = 'user'

    id = Column(
        postgresql.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    reset_token = Column(String, nullable=True)
    status_code = Column(String, ForeignKey(
        "user_status.code"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    tokens: Mapped[List[AuthToken]] = relationship()

    def save(self, session: Session) -> None:
        self._before_save()
        session.add(self)
        session.commit()

    @staticmethod
    def get(id: str):
        with Session(DB().engine) as session:
            return session.query(models.User).where(models.User.id == id).one_or_none()

    def _before_save(self) -> None:
        self.setDateTimestamps()

    def setDateTimestamps(self):
        if (self.id):
            self.updated_at = datetime.utcnow()
        else:
            self.created_at = datetime.utcnow()

    @staticmethod
    def all() -> List[any]:
        with Session(DB().engine) as session:
            return session.query(models.User).all()
