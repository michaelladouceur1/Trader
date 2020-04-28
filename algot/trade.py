from trader.broker import Broker
from api.api import TDAPI

tdapi = TDAPI()
account = tdapi.get_accounts()
transactions = tdapi.get_transactions()
print(transactions.columns)
# print(transactions[transactions['type']=='TRADE'])
print(transactions)
# print(account)
broker = Broker()
print(broker.cash)
print(broker.positions.columns)
print(broker.positions)