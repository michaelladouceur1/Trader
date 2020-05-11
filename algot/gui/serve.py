# Local Imports
from api.api import TDAPI
from utils.utils import timestamp_to_iso

class Serve:
    def __init__(self):
        self.tdapi = TDAPI()
        self.accounts = self.tdapi.get_accounts()
        self.positions = self.tdapi.get_positions()

        self.cash = self.get_cash()
        self.investment_value = self.get_investement_value()
        self.total_return = self.get_total_return()
        self.total_liquid_value = self.get_total_liquid_value()

    def get_cash(self):
        print(f'get_cash called...')
        return self.accounts[self.tdapi.ACCOUNT_ID]['securitiesAccount']['currentBalances']['cashAvailableForTrading']

    def get_investement_value(self):
        return self.accounts[self.tdapi.ACCOUNT_ID]['securitiesAccount']['currentBalances']['longMarketValue']

    def get_total_return(self):
        cost, mkt = 0, 0
        for pos in self.positions:
            if pos['instrument']['assetType'] != 'CASH_EQUIVALENT':
                cost += pos['averagePrice'] * pos['longQuantity']
                mkt += pos['marketValue']
                
        total = round(((mkt/cost)-1)*100, 2)
        return total

    def get_total_liquid_value(self):
        return self.cash + self.investment_value

    # def get_history(self):
    #     self.history