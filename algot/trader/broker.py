import pandas as pd
from api.api import TDAPI

class Broker:
    def __init__(self,cash=None):
        self.tdapi = TDAPI()
        self.cash = self._set_cash(cash)
        self.positions = self._set_positions()
        self.position_assets = self.positions['asset']
        
    def _set_cash(self,cash):
        if cash is not None:
            return cash
        else:
            return self.tdapi.get_accounts()[self.tdapi.ACCOUNT_ID]['securitiesAccount']['currentBalances']['cashAvailableForTrading']

    def _set_positions(self):
        positions = self.tdapi.get_positions()
        positions['asset'] = [i['symbol'] for i in positions['instrument']]
        positions['assetType'] = [i['assetType'] for i in positions['instrument']]
        positions['cusip'] = [i['cusip'] for i in positions['instrument']]
        positions.drop(columns=['instrument'],inplace=True)
        return positions

    def get_postions(self):
        return self.tdapi.get_positions()

    def buy(self, amount=1):
        pass

    def sell(self, amount=1):
        pass

