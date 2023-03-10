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
        
    def update_user(self, name, new_age):
        with DBConnection() as db:
            user = db.session.query(UsersModel).filter_by(name=name).first()
            if user:
                user.age = new_age
                db.session.commit()
                return True
            else:
                return False
            
    def delete_user(self, name):
        with DBConnection() as db:
            user = db.session.query(UsersModel).filter_by(name=name).first()
            if user:
                db.session.delete(user)
                db.session.commit()
                return True
            else:
                return False
