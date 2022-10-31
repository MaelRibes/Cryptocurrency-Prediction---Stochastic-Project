from get_data import *
from formula import *
import matplotlib.pyplot as plt

# ================== Récupération Données ==================

symbol = input("Symbol : ").upper()
comparative_symbol = input("Comparative Symbol : ").upper()
hourly = input("Daily or hourly historical (d/h) : ")
time_delta = 1
df = hourly_price_historical(symbol, comparative_symbol, 2000, time_delta, hourly)
df.to_csv(f"{symbol}-{comparative_symbol}-{hourly}")


# ================== Moyenne Mobile simple ==================

MoyMobil10 = moyenneMobile(df, 10)
print("MA 10 OK")
MoyMobil50 = moyenneMobile(df, 50)
print("MA 50 OK")

plt.plot(df.timestamp, df.close)
plt.plot(df.timestamp, MoyMobil10, 'r')
plt.plot(df.timestamp, MoyMobil50, 'b')
plt.xticks(rotation=60)
plt.show()


# ================== Moyenne Mobile Exponantielle ==================

MoyMobilEXP10 = MoyenneMobileExp(df, 10)
print("MA EXP 10 OK")
MoyMobilEXP50 = MoyenneMobileExp(df, 50)
print("MA EXP 50 OK")

plt.plot(df.timestamp, df.close)
plt.plot(df.timestamp, MoyMobilEXP10, 'r')
plt.plot(df.timestamp, MoyMobilEXP50, 'b')
plt.xticks(rotation=45)
plt.show()


# ================== Indice Stochastique ==================

Stocha = stochastic(df)
print("Stochastic indice OK")
plt.plot(df.timestamp, Stocha)
plt.show()
