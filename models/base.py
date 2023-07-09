from sqlalchemy.orm import DeclarativeBase
from services.db import DB


class Base(DeclarativeBase):
    db = DB()
