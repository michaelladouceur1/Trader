# Third Party Imports
from sqlalchemy.schema import MetaData
from sqlalchemy import Table, Column, Integer, DateTime, Date, Float, UniqueConstraint, inspect, insert, select
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from datetime import date, timedelta
import time

class DB:
    def __init__(self, database, path='/home/michael/Documents/Coding/Finance/Trader/algot/db/'):
        self.database = database
        self.path = path
        self._create_engine()
        self._connect_engine()

    def _create_engine(self):
        self.engine = db.create_engine(f'sqlite:///{self.path}{self.database}.db', echo=False)
        self.metadata = MetaData(bind=self.engine)

    def _connect_engine(self):
        self.connection = self.engine.connect()

    def get_table_names(self):
        inspector = inspect(self.engine)
        return inspector.get_table_names()
    
    def get_table(self, table):
        return Table(table, self.metadata, autoload=True)

    def insert_data(self, table, data):
        i = insert(table).prefix_with('OR IGNORE')
        i = i.values(data)
        self.connection.execute(i)

    def query_tables(self, tables=None, columns=None):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        cols = columns

        if tables is not None:
            _tables = [self.get_table(table) for table in tables]
        else:
            table_names = self.get_table_names()
            _tables = [self.get_table(table) for table in table_names]

        data = []
        for i, table in enumerate(_tables):
            if tables is not None:
                sym = tables[i]
            else:
                sym = table_names[i]

            if columns is not None:
                _columns = getattr(table, '_columns')
                data.append({
                    'symbol': sym,
                    'data': session.query(*[getattr(_columns, i) for i in columns]).all()
                }) 
            else:
                data.append({
                    'symbol': sym,
                    'data': session.query(table).all()
                })
                
        data = self._label_query(data, columns)

        return data

    def _label_query(self, data, columns):
        label_data = []
        for sec in data:
            new_vals = []
            for vals in sec['data']:
                {k:v for (k,v) in zip(vals, columns)}
                new_vals.append({k:v for (k,v) in zip(columns, vals)})
            label_data.append({
                'symbol': sec['symbol'],
                'data': new_vals
            })
        
        return label_data
        

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
                        Column('datetime', DateTime, unique=True),
                        Column('open', Float),
                        Column('close', Float),
                        Column('high', Float),
                        Column('low', Float),
                        Column('volume', Integer))

        self.metadata.create_all(self.engine)

# data = [
#     {'date': datetime.now(), 'open': 1203, 'close': 3828, 'high': 3828, 'low': 1, 'volume': 140},
#     {'date': datetime.now()-timedelta(days=1), 'open': 1203, 'close': 3828, 'high': 3828, 'low': 1, 'volume': 140},
#     {'date': datetime.now()-timedelta(days=2), 'open': 1203, 'close': 3828, 'low': 1, 'high': 3828, 'volume': 140}
# ]

db = SecuritiesDB()
data = db.query_tables(['FNV'])
print(data)
# print(data.keys())

# db = SecuritiesDB()
# db.create_security_table('GOOG')
# table = db.get_table('GOOG')
# db.insert_security_data(table,data)
# tables = db.get_table_names()
# print(tables)