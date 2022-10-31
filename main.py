from get_data import *
from formula import *
from ar import *
import matplotlib.pyplot as plt

# ================== Récupération Données ==================

symbol = input("Symbol : ").upper()
comparative_symbol = input("Comparative Symbol : ").upper()
hourly = input("Daily or hourly historical (d/h) : ")
details = input("Frames details of the AR model (y/n) : ")
time_delta = 1
df = hourly_price_historical(symbol, comparative_symbol, 2000, time_delta, hourly)
title = f"{symbol}/{comparative_symbol}-{hourly}"
df.to_csv(f"{symbol}-{comparative_symbol}-{hourly}")

# ================== Moyenne Mobile simple ==================

MoyMobil10 = moyenneMobile(df, 10)
print("MA 10 OK")
MoyMobil50 = moyenneMobile(df, 50)
print("MA 50 OK")

plt.plot(df.timestamp, df.close)
plt.plot(df.timestamp, MoyMobil10, 'r')
plt.plot(df.timestamp, MoyMobil50, 'g')
plt.title(title)
plt.xlabel("Timestamp")
plt.ylabel(comparative_symbol)
plt.legend([symbol, 'MA 10', 'MA 50'])
plt.xticks(rotation=60)
plt.show()

# ================== Moyenne Mobile Exponantielle ==================

MoyMobilEXP10 = MoyenneMobileExp(df, 10)
print("MA EXP 10 OK")
MoyMobilEXP50 = MoyenneMobileExp(df, 50)
print("MA EXP 50 OK")

plt.plot(df.timestamp, df.close)
plt.plot(df.timestamp, MoyMobilEXP10, 'r')
plt.plot(df.timestamp, MoyMobilEXP50, 'g')
plt.title(title)
plt.xlabel("Timestamp")
plt.ylabel(comparative_symbol)
plt.legend([symbol, 'Exponential MA 10', 'Exponential MA 50'])
plt.xticks(rotation=60)
plt.show()

# ================== Indice Stochastique ==================

stocha = stochastic(df)
stocha = stocha[10:]
df1 = df.iloc[10:]
print("Stochastic indice OK")
plt.plot(df1.timestamp, stocha)
plt.title(f"Stochastic Indice {symbol}/{comparative_symbol}")
plt.xticks(rotation=60)
plt.show()

# ================== Modèle Auto-Régressif ==================

AR_model(df, details, symbol, comparative_symbol)
