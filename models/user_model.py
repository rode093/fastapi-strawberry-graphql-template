from sqlalchemy import Column, String, text, DateTime, ForeignKey, MetaData
import uuid
from models.base_model import Base


class User(Base):
    __tablename__ = 'user'

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
        "user_status.code"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
