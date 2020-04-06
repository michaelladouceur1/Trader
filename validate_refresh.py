from tdameritrade import auth as tda 
import os
import datetime

print(datetime.date.today())

client_id = os.environ.get('TD_API_KEY')
redirect_uri = 'http://localhost:8080'

print(client_id)

# tda.authentication(client_id=client_id, redirect_uri=redirect_uri)