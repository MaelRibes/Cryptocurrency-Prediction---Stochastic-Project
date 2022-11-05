from tqdm import tqdm
from time import sleep


def stochastic_indicator(df):
    stocha = []
    for i in tqdm(range(len(df))):

        close_value = [df["close"][0]]

        for k in range(i):
            close_value.append(df["close"][k])

        lowest_close = min(close_value)
        highest_close = max(close_value)

        if lowest_close == highest_close:
            lowest_close = 0

        last_close = df["close"][i]
        k = 100 * ((last_close - lowest_close) /
                   (highest_close - lowest_close))
        stocha.append(k)
    return stocha


def moving_average_list(listVal, period):
    mm = []
    for i in range(len(listVal)):

        if i <= period:
            mm.append(listVal[i])

        else:
            sum = 0

            for k in range(period):
                sum += listVal[i - k]

            mm.append(sum / period)
    return mm


def moving_average_df(df, period):
    mm = []
    for i in tqdm(range(len(df))):

        if i <= period:
            mm.append(df.close[i])

        else:
            sum = 0

            for k in range(period):
                sum += df.close[i - k]

            mm.append(sum / period)
    sleep(0.5)
    return mm


def exponential_moving_average(df, period):
    listMME = [df["close"][0]]
    for i in tqdm(range(1, len(df))):
        mme = listMME[-1] + (2 / (period + 1)) * (df["close"][i] - listMME[-1])
        listMME.append(mme)
    sleep(0.5)
    return listMME