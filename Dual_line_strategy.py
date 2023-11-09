
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from mplfinance import original_flavor as mpf


df = pd.read_csv("/Users/Andi/Desktop/stock/Test_JF.csv", usecols=["date", "open", "close", "high", "low"],dtype={"date": object})
df["date"] = pd.to_datetime(df["date"])
df["time"] = date2num(df["date"])
fig = plt.figure()
ax = plt.subplot(1,1,1)
ax.xaxis_date()
arr = df[["time", "open", "close", "high", "low"]].values
mpf.candlestick_ochl(ax,arr,colorup="red",colordown="green")

df["ma5"] = df["close"].rolling(5).mean()
df["ma30"] = df["close"].rolling(30).mean()
plt.plot(df["date"],df["ma5"],color="green",label="5days")
plt.plot(df["date"],df["ma30"],color="red",label="30days")
ax.set_ylabel("CLOSE PRICE")
ax.legend()
plt.title("Dual Line Strategy")
# diaplay
plt.show()