
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base
from services.db import DB
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, overload


class UserStatus(Base):
    __tablename__ = 'user_status'

    code = Column(String, primary_key=True)
    label = Column(String, nullable=False)
    users = relationship('User')

    def save(self):
        record = self.get(self.code)
        if record == None:
            record = UserStatus(
                code=self.code, label=self.label)  # record is new
        else:
            record.label = self.label  # record exists so just update the attributes
        with Session(DB().engine) as session:
            session.add(record)
            session.commit()

    @staticmethod
    def get(code: str):
        with Session(DB().engine) as session:
            return session.query(UserStatus).filter(
                UserStatus.code == code).first()

    def all(self, codes: List[str] = list()):
        with Session(DB().engine) as session:
            query = session.query(UserStatus)
            if len(codes) > 0:
                query.filter(UserStatus.code.in_(codes))
            return query.all()

    def deleteMany(self, codes: List[str]):
        with Session(DB().engine) as session:
            session.query(UserStatus).filter(
                UserStatus.code.in_(codes)).delete(synchronize_session=False)
            session.commit()

    def delete(self, code: str):
        with Session(DB().engine) as session:
            session.query(UserStatus).filter(
                UserStatus.code == code).delete(synchronize_session=False)
            session.commit()
