# THIRD PARTY IMPORTS
import tdameritrade as td
from tdameritrade.auth import refresh_token
import pandas as pd
from datetime import datetime, timedelta
import os 

# LOCAL IMPORTS
from utils.utils import convert_to_df

CURRENT_DATE = datetime.today().strftime('%Y-%m-%d')
PREV_YEAR = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')

class TDAPI:
    def __init__(self):
        self.ACCOUNT_ID = self._get_account_id()
        self.REFRESH_TOKEN = self._get_refresh_token()
        self.API_KEY = self._get_api_key()
        self.ACCESS_TOKEN = refresh_token(self.REFRESH_TOKEN,self.API_KEY)['access_token']
        # print(self.ACCESS_TOKEN)
        self.client = td.TDClient(access_token=self.ACCESS_TOKEN)

    def _get_account_id(self):
        return os.environ.get('TD_BROKER_ID')

    def _get_refresh_token(self):
        return os.environ.get('TD_REFRESH_TOKEN')

    def _get_api_key(self):
        return os.environ.get('TD_API_KEY')

    def get_accounts(self, positions=False):
        return self.client.accounts(positions=positions)

    @convert_to_df
    def get_positions(self):
        return self.client.accounts(positions=True)[self.ACCOUNT_ID]['securitiesAccount']['positions']

    def get_history(self, symbol, **kwargs):
        return self.client.historyDF(symbol, **kwargs)

    def get_movers(self, index, direction='up', change_type='percent'):
        return self.client.movers(index, direction, change_type)

    def get_fundamentals(self, symbol):
        fund = self.client.fundamental(symbol)
        fundDF = pd.DataFrame(fund[symbol]['fundamental'], index=[0])
        return fundDF

    def get_options(self, symbol):
        return self.client.optionsDF(symbol)

    def get_transactions(self):
        return self.client.transactionsDF(self.ACCOUNT_ID)

    def get_quote(self, symbol):
        return self.client.quoteDF(symbol)

    def get_deposits_withdrawals(self, start_date=PREV_YEAR, end_date=CURRENT_DATE):
        return self.client.transactions(acc=self.ACCOUNT_ID, type='CASH_IN_OR_CASH_OUT', start_date=start_date, end_date=end_date)


# td = TDAPI()
# print(td.get_history('TSLA'))