import requests
import datetime
import pandas as pd


def hourly_price_historical(symbol, comparison_symbol, limit, aggregate, hourly, exchange=''):
    if hourly == "h":
        url = 'https://min-api.cryptocompare.com/data/v2/histohour?fsym={}&tsym={}&limit={}&aggregate={}' \
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if hourly == "d":
        url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym={}&tsym={}&limit={}&aggregate={}' \
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)

    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()['Data']

    df = pd.DataFrame(data)

    df['timestamp'] = [datetime.datetime.fromtimestamp(
        d["time"]) for d in df.Data]

    df['close'] = [d["close"] for d in df.Data]
    return df


def get_top10():
    url = "https://min-api.cryptocompare.com/data/top/totalvolfull?limit=10&tsym=USD"
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df.to_csv("test")
    return [df.CoinInfo[k]["Name"] for k in range(len(df))]
