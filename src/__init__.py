from .config import DBConnection
from .entities import Users as UsersModel

class UserRepo:

    def insert_user(self, name):
        import logging
        logger=logging.getLogger()
        logger.error('CHEGOU AQUI')
        with DBConnection() as db:
            new_user = UsersModel(name=name)
            db.session.add(new_user)
            db.session.commit()