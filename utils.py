import pandas as pd 

def convert_to_df(func):
    def wrapper(*args,**kwargs):
        data = func(*args,**kwargs)
        # return pd.DataFrame(data, index=[i['instrument']['symbol'] for i in data])
        return pd.DataFrame(data)
    return wrapper


