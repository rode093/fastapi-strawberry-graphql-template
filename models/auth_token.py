from enum import unique
from operator import index
from models.base_model import Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql
import uuid


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
    created_at = Column(DateTime, nullable=False)
