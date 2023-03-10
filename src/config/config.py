from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnection:

    def __init__(self) -> None:
        self.__connection_string = 'mysql+pymysql://root:test@mysqldb/teste'
        self.session = None

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session = sessionmaker(bind=engine)
        self.session = session()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()