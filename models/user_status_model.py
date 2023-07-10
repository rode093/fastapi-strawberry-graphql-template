
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base


class UserStatus(Base):
    __tablename__ = 'user_status'

    code = Column(String, primary_key=True)
    label = Column(String, nullable=False)
    users = relationship('User')
