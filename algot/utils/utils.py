import pandas as pd 

def convert_to_df(func):
    def wrapper(*args,**kwargs):
        data = func(*args,**kwargs)
        # return pd.DataFrame(data, index=[i['instrument']['symbol'] for i in data])
        return pd.DataFrame(data)
    return wrapper

def timestamp_to_iso(func):
	def wrapper(*args,**kwargs):
		data = func(*args,**kwargs)
		if isinstance(data['datetime'][0], np.int64):
			data['datetime'] = data['datetime'].apply(lambda x: pd.Timestamp(x, unit='ms'))
		return data
	return wrapper