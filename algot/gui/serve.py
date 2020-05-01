from api.api import TDAPI

class Serve:
    def __init__(self):
        self.tdapi = TDAPI()

    def get_cash(self):
        print(f'get_cash called...')
        return self.tdapi.get_accounts()[self.tdapi.ACCOUNT_ID]['securitiesAccount']['currentBalances']['cashAvailableForTrading']
