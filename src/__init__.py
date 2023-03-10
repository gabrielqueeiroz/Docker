from .config import DBConnection
from .entities import Users as UsersModel
from sqlalchemy import select

class UserRepo:

    def insert_user(self, name, age):
        with DBConnection() as db:
            new_user = UsersModel(name=name, age=age)
            db.session.add(new_user)
            db.session.commit()

    def read_user(self, name):
        with DBConnection() as db:
            db.session.execute(select(name).values(name=name))
