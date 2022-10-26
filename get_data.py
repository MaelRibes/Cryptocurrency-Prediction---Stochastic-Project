import requests
import datetime
import pandas as pd
import matplotlib.pyplot as plt

def hourly_price_historical(symbol, comparison_symbol, limit, aggregate, exchange=''):
    url = 'https://min-api.cryptocompare.com/data/v2/histohour?fsym={}&tsym={}&limit={}&aggregate={}'\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()['Data']
   
    df = pd.DataFrame(data)

    df['timestamp'] = [datetime.datetime.fromtimestamp(d["time"]) for d in df.Data]
    
    df['close'] =[d["close"] for d in df.Data]
    return df


time_delta=1
df=hourly_price_historical("BTC","USD",2000,time_delta)
plt.plot(df.timestamp,df.close)
plt.xticks(rotation=45)
plt.show()