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

    df['timestamp'] = [datetime.datetime.fromtimestamp(
        d["time"]) for d in df.Data]

    df['close'] = [d["close"] for d in df.Data]
    return df


def stochastic(df):
    stocha = []
    for i in range(len(df)):

        lowestClose = 0
        highestClose = 0
        Closevalue = [df["close"][0]]

        for k in range(i):
            Closevalue.append(df["close"][k])
        print(len(Closevalue))

        lowestClose = min(Closevalue)
        highestClose = max(Closevalue)

        if lowestClose == highestClose:
            lowestClose = 0

        lastClose = df["close"][i]

        k = 100*((lastClose-lowestClose)/(highestClose-lowestClose))

        stocha.append(k)

    return (stocha)


def moyennemobile(df, period):
    mm = []
    for i in range(len(df)):

        if i <= period:
            mm.append(df.close[i])

        else:

            sum = 0

            for k in range(period):
                sum += df.close[i-k]

            mm.append(sum/period)

    return (mm)


def MoyenneMobileExp(df, period):

    listMME = [df["close"][0]]

    for i in range(1, len(df)):
        mme = listMME[-1]+(2/(period+1))*(df["close"][i]-listMME[-1])
        listMME.append(mme)

    return (listMME)



