from datetime import datetime

class Broker:
    def __init__(self):
        self.data = []

    def add_account(self, account=None):
        self.account = account

    def add_cash(self, cash=None):
        self.cash = cash

    def add_positions(self, positions=[]):
        self.positions = positions

    def add_strategy(self, strategy):
        self.strategy = strategy

    def add_data(self, data):
        self.data.extend(data)

    def _check_cash(self):
        pass

    def _log_trade_price(self):
        pass

    def _buy(self):
        pass

    def _sell(self):
        pass

    def _zip_data(self):
        _data = [d['data'] for d in self.data]
        symbols = [d['symbol'] for d in self.data]

        data = []
        for d in zip(*_data):
            data.append(d)

        return data

    def bt(self):
        self.calc_data = self._zip_data()
        print(self.calc_data)
        



data = [ { 'data': [ { 'close': 3828.0,
                'datetime': datetime(2020, 5, 15, 11, 58, 25, 658166),
                'high': 3828.0,
                'id': 1,
                'low': 1.0,
                'open': 1203.0,
                'volume': 140},
              { 'close': 3828.0,
                'datetime': datetime(2020, 5, 14, 11, 58, 25, 658166),
                'high': 3828.0,
                'id': 2,
                'low': 1.0,
                'open': 1203.0,
                'volume': 140},
              { 'close': 3828.0,
                'datetime': datetime(2020, 5, 13, 11, 58, 25, 658166),
                'high': 3828.0,
                'id': 3,
                'low': 1.0,
                'open': 1203.0,
                'volume': 140},
              { 'close': 3828.0,
                'datetime': datetime(2020, 5, 15, 11, 59, 19, 10265),
                'high': 3828.0,
                'id': 4,
                'low': 1.0,
                'open': 1203.0,
                'volume': 140},
              { 'close': 3828.0,
                'datetime': datetime(2020, 5, 14, 11, 59, 19, 10265),
                'high': 3828.0,
                'id': 5,
                'low': 1.0,
                'open': 1203.0,
                'volume': 140},
              { 'close': 3828.0,
                'datetime': datetime(2020, 5, 13, 11, 59, 19, 10265),
                'high': 3828.0,
                'id': 6,
                'low': 1.0,
                'open': 1203.0,
                'volume': 140},
              { 'close': 3828.0,
                'datetime': datetime(2020, 5, 15, 11, 59, 44, 555786),
                'high': 3828.0,
                'id': 7,
                'low': 1.0,
                'open': 1203.0,
                'volume': 140},
              { 'close': 3828.0,
                'datetime': datetime(2020, 5, 14, 11, 59, 44, 555786),
                'high': 3828.0,
                'id': 8,
                'low': 1.0,
                'open': 1203.0,
                'volume': 140},
              { 'close': 3828.0,
                'datetime': datetime(2020, 5, 13, 11, 59, 44, 555786),
                'high': 3828.0,
                'id': 9,
                'low': 1.0,
                'open': 1203.0,
                'volume': 140}],
    'symbol': 'FNV'},
  { 'data': [ { 'close': 3828.0,
                'datetime': datetime(2020, 5, 15, 11, 53, 27, 51428),
                'high': 3828.0,
                'id': 1,
                'low': 1.0,
                'open': 1203.0,
                'volume': 140},
              { 'close': 3828.0,
                'high': 3828.0,
                'id': 1,
                'low': 1.0,
                'open': 1203.0,
                'volume': 140},
              { 'close': 3828.0,
                'datetime': datetime(2020, 5, 14, 11, 53, 27, 51428),
                'high': 3828.0,
                'id': 2,
                'low': 1.0,
                'open': 1203.0,
                'volume': 140},
              { 'close': 3828.0,
                'datetime': datetime(2020, 5, 13, 11, 53, 27, 51428),
                'high': 3828.0,
                'id': 3,
                'low': 1.0,
                'open': 1203.0,
                'volume': 140}],
    'symbol': 'GOOG'}]


broker = Broker()
broker.add_data(data)
broker.bt()