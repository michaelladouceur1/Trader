from sqlalchemy.schema import MetaData
from sqlalchemy import Table, Column, Integer, DateTime, Float
import sqlalchemy as db


class DB:
    def __init__(self, database, path=''):
        self.database = database
        self.path = path
        self.create_engine()

    def create_engine(self):
        self.engine = db.create_engine(f'sqlite:///{self.path}{self.database}.db')

    def connect_engine(self):
        self.connection = self.engine.connect()

    # def create_table(self, symbol):
    #     metadata = MetaData()
    #     table = db.Table(symbol, metadata,
    #             Column('open', ))

class SecuritiesDB(DB):
    def __init__(self):
        self.database = 'securities'
        self._super_init()

    def _super_init(self):
        super().__init__(
            self.database
            )

    def create_security_table(self, symbol):
        meta = MetaData()
        table = Table(symbol, meta,
                        Column('id', Integer, primary_key = True),
                        Column('date', DateTime),
                        Column('open', Float),
                        Column('close', Float),
                        Column('high', Float),
                        Column('low', Float))
        meta.create_all(self.engine)


# db = DB('securities')
db = SecuritiesDB()
db.create_table('TSLA')
# db.create_table('AAPL')