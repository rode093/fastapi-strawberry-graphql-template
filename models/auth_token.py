from datetime import date, datetime, timedelta
from enum import unique
from operator import index
from lib.helpers import create_password_hash
from models.base_model import Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.dialects import postgresql
import uuid
import random
import string

from services.db import DB


class AuthToken(Base):
    __tablename__ = 'token'
    id = Column(
        postgresql.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    access_token = Column(String, unique=True, index=True, nullable=False)
    refresh_token = Column(String, unique=True, index=True, nullable=False)
    access_token_expires_at = Column(DateTime, nullable=False)
    refresh_token_expires_at = Column(DateTime, nullable=False)
    user_id = Column(postgresql.UUID(as_uuid=True),
                     ForeignKey("user.id"), nullable=False)
    status = Column(String, default="ACTIVE")  # Active or Expired
    created_at = Column(DateTime, nullable=False, )

    def __init__(self, user_id: uuid.UUID) -> None:
        self.user_id = user_id
        self.access_token = create_password_hash("".join(random.choices(
            string.ascii_letters, k=16)))
        self.refresh_token = create_password_hash("".join(random.choices(
            string.ascii_letters, k=16)))
        self.access_token_expires_at = datetime.utcnow()+timedelta(hours=1)
        self.refresh_token_expires_at = datetime.utcnow()+timedelta(days=30)
        self.created_at = datetime.utcnow()

    def save(self, session: Session) -> None:
        session.add(self)
        session.commit()
