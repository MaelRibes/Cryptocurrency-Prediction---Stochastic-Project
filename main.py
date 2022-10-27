from get_data import *

time_delta = 1
df = hourly_price_historical("ETH", "USD", 2000, time_delta)
df.to_csv("EURUSD")

Stocha = stochastic(df)

MoyMobil1 = moyennemobile(df, 10)
MoyMobil2 = moyennemobile(df, 50)


MoymobilEXP1 = MoyenneMobileExp(df, 10)
MoymobilEXP2 = MoyenneMobileExp(df, 50)


plt.plot(df.timestamp, df.close)
plt.plot(df.timestamp, MoymobilEXP1, 'r')
plt.plot(df.timestamp, MoymobilEXP2, 'b')
plt.xticks(rotation=45)
plt.show()

plt.plot(df.timestamp, df.close)
plt.plot(df.timestamp, MoyMobil1, 'r')
plt.plot(df.timestamp, MoyMobil2, 'b')
plt.xticks(rotation=45)
plt.show()


plt.plot(df.timestamp, Stocha)

plt.show()