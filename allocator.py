from api import TDAPI

class Allocator:
    def __init__(self,securities,cash):
        self.tdapi = TDAPI()
        self.securities = securities
        self.securities_data = self._get_securities_data()
        self.cash = cash

    def _get_securities_data(self):
        securities_data = {}
        data = {
            'periodType': 'month',
            'period': 1,
            'frequencyType': 'daily',
            'frequency': 1
        }

        for security in self.securities:
            securities_data[security] = self.tdapi.get_history(symbol=security, periodType='month', period=1, frequencyType='daily', frequency=1)
        
        return securities_data


alloc = Allocator(['GOOG','AAPL'],10000)
print(alloc.securities_data)
print(type(alloc.securities_data['GOOG']))