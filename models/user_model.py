from email.policy import default
import uuid
from sqlalchemy import Column, String, Text, text, DateTime, ForeignKey, select
import models
from models.base_model import Base
import strawberry
from sqlalchemy.orm import Session
from services.db import DB
from datetime import datetime
from sqlalchemy.dialects import postgresql
from lib.helpers import create_password_hash


class User(Base):
    __tablename__ = 'user'

    id = Column(
        postgresql.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    reset_token = Column(String, nullable=True)
    status_code = Column(String, ForeignKey(
        "user_status.code"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

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
            self.updated_at = datetime.now()
        else:
            self.created_at = datetime.now()
