from sqlalchemy.schema import MetaData
import sqlalchemy as db


class DB:
    def __init__(self, database, path=''):
        self.engine = db.create_engine(f'sqlite:///{path}{database}.db')
        self.connection = self.engine.connect()

    def create_table(self, symbol):
        metadata = MetaData()
        table = Table(symbol, metadata,
                Column('open', ))

db = DB('securities')
db.create_table('AAPL')