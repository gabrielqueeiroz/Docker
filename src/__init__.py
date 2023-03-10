from .config import DBConnection
from .entities import Users as UsersModel

class UserRepo:

    def insert_user(self, name, age):
        with DBConnection() as db:
            new_user = UsersModel(name=name, age=age)
            db.session.add(new_user)
            db.session.commit()

    def read_user(self, name):
        with DBConnection() as db:
            user = db.session.query(UsersModel).filter_by(name=name).first()
            return user
