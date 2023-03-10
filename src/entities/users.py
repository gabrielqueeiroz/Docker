from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.expression import true
from src.config import Base

class Users(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=true)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self) -> str:
        return f"Users [name={self.name}, age={self.age}]"