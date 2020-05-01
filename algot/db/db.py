from sqlalchemy.schema import MetaData
from sqlalchemy import Table, Column, Integer, DateTime, Float, UniqueConstraint, inspect, insert, select
import sqlalchemy as db
from datetime import datetime

class DB:
    def __init__(self, database, path=''):
        self.database = database
        self.path = path
        self._create_engine()
        self._connect_engine()

    def _create_engine(self):
        self.engine = db.create_engine(f'sqlite:///{self.path}{self.database}.db', echo=True)
        self.metadata = MetaData(bind=self.engine)

    def _connect_engine(self):
        self.connection = self.engine.connect()

    def get_table_names(self):
        inspector = inspect(self.engine)
        return [table_name for table_name in inspector.get_table_names()]
    
    def get_table(self, table):
        return Table(table, self.metadata, autoload=True)

class SecuritiesDB(DB):
    def __init__(self):
        self.database = 'securities'        
        self._super_init()

    def _super_init(self):
        super().__init__(
            self.database
            )

    def create_security_table(self, symbol):
        table = Table(symbol, self.metadata,
                        Column('id', Integer, primary_key = True),
                        Column('date', Date, unique=True),
                        Column('open', Float),
                        Column('close', Float),
                        Column('high', Float),
                        Column('low', Float))
        self.metadata.create_all(self.engine)

    def insert_security_data(self, table):
        i = insert(table)
        i = i.values({'date': datetime.now(), 'open': 1203, 'close': 3828, 'high': 3828, 'low': 1})
        self.connection.execute(i)

    # def print_table_data(self, table):
    #     Session = sessionmaker(bind=self.engine)
    #     session = Session()
    #     s = table.select()
    #     result = session.execute(s)
    #     out = result.fetchall()
    #     print(f'\n\n{out}')

db = SecuritiesDB()
table = db.get_table('RGLD')
db.insert_security_data(table)