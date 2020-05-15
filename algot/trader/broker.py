class Broker:
    def __init__(self):
        pass 

    def add_account(self, account=None):
        self.account = account

    def add_cash(self, cash=None):
        self.cash = cash

    def add_positions(self, positions=[]):
        self.positions = positions

    def add_strategy(self, strategy):
        self.strategy = strategy

    def add_data(self, data):
        self.data = data 

    def _check_cash(self):
        pass

    def _log_trade_price(self):
        pass

    def _buy(self):
        pass

    def _sell(self):
        pass

    def bt(self):
        symbols = [i for i in self.data.keys()]
        for i, d in enumerate(self.data.values()):
            print(d)

data = [{'FNV': [
    (1564.1, 1654.15, 4653.45),
    (1564.1, 1654.15, 4653.45),
    (1564.1, 1654.15, 4653.45),
]},
{'GOOG': [
    (1564.1, 1654.15, 4653.45),
    (1564.1, 1654.15, 4653.45),
    (1564.1, 1654.15, 4653.45),
]}]

broker = Broker()
broker.add_data(data)
broker.bt()