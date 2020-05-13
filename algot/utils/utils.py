# Third Party Imports
import pandas as pd 
import numpy as np
from datetime import datetime

def convert_to_df(func):
    def wrapper(*args,**kwargs):
        data = func(*args,**kwargs)
        # return pd.DataFrame(data, index=[i['instrument']['symbol'] for i in data])
        return pd.DataFrame(data)
    return wrapper

def timestamp_to_iso(data):
	for dd in data.keys():
		if isinstance(data[dd][0]['datetime'], int):
			for d in data[dd]:
				d['datetime'] = datetime.fromtimestamp(d['datetime']/1000)
	return data