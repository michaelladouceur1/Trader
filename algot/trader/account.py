import pandas as pd
from api import TDAPI

class Account:
    def __init__(self, cash=None, positions=None):
        self.tdapi = TDAPI()
        self.cash = self._set_cash(cash)
        self.positions = self._set_positions(positions)
        
    def _set_cash(self, cash):
        if cash is not None:
            return cash
        return self.tdapi.get_accounts()[self.tdapi.ACCOUNT_ID]['securitiesAccount']['currentBalances']['cashAvailableForTrading']

    def _set_positions(self, positions):
        if positions is not None:
            return positions
        raw_positions = self.tdapi.get_positions()
        positions = []
        for pos in raw_positions:
            position = {
                'asset_type': pos['instrument']['assetType'],
                'cusip': pos['instrument']['cusip'],
                'symbol': pos['instrument']['symbol'],
                'average_price': pos['averagePrice'],
                'long_quantity': pos['longQuantity'],
                'market_value': pos['marketValue']
            }
            positions.append(position)
        return positions

    def set_bt_data(self, )

    def buy(self, amount=1):
        pass

    def sell(self, amount=1):
        pass

broker = Account()
print(broker.cash)
print(broker.positions)