from models.base import Base
from models.user_status_model import UserStatus
from uuid import UUID
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import text, Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID


class User(Base):
    __tablename__ = 'users'

    id = Column(
        "id", UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )

    first_name: Mapped[String] = Column(
        'first_name', String(64), nullable=False),
    last_name: Mapped[String] = Column(
        'last_name', String(64), nullable=False),
    email: Mapped[String] = Column('email', String(64), nullable=False),
    password: Mapped[String] = Column('password', String(512), nullable=False),
    reset_token: Mapped[String] = Column(
        'reset_token', String(512), nullable=True),
    status_code: Mapped[String] = Column('status', String(
        16), nullable=False, foreign_key="user_statuses.code"),
    status: Mapped[UserStatus] = relationship(back_populates="user_statuses")
    created_at = Column('created_at', DateTime(
        timezone=True), server_default=text('NOW()')),
    updated_at = Column('updated_at', DateTime(timezone=True), nullable=True),
