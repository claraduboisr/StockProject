# I am comparing Stock prices with different cryptocurrencies
# Firstly, I tried to compare it with Bitcoin but it's scale was to large in comparisson with Licoin, Etherum and Ripple

from matplotlib import pylab as plt
import pandas

df1 = pandas.read_csv("ETH-USD.csv")
df1['Date'] = pandas.to_datetime(df1.Date)

df2 = pandas.read_csv("LTC-USD.csv")
df2['Date'] = pandas.to_datetime(df2.Date)

df3 = pandas.read_csv("XRP-USD.csv")
df3['Date'] = pandas.to_datetime(df3.Date)

df4 = pandas.read_csv("DASH-USD.csv")
df4['Date'] = pandas.to_datetime(df4.Date)



plt.figure("first")
plt.plot(df1.Date, df1.Open, "r:", label="Litcoin", linewidth=0.5, ms=0.5)
plt.plot(df2.Date, df2.Open, "b:", label="Ethereum", linewidth=0.5, ms=0.5)
plt.plot(df3.Date, df3.Open, "y:", label="Ripple", linewidth=0.5, ms=0.5)
plt.plot(df4.Date, df4.Open, "k:", label="Dash", linewidth=0.5, ms=0.5)

plt.legend(loc="upper left")

plt.show()