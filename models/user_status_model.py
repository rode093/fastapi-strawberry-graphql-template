
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base
from services.db import DB
from sqlalchemy.orm import Session


class UserStatus(Base):
    __tablename__ = 'user_status'

    code = Column(String, primary_key=True)
    label = Column(String, nullable=False)
    users = relationship('User')

    def save(self):
        with Session(DB().engine) as session:
            session.add(self)
            session.commit()
