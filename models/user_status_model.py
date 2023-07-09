from models.base import Base
from uuid import UUID
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import text, Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID


class UserStatus(Base):
    __tablename__ = 'user_statuses'

    code = Column('code', String(16), primary_key=True)
    label = Column('label', String(32), nullable=False)
