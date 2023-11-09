
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from mplfinance import original_flavor as mpf

df = pd.read_csv("/Users/Andi/Desktop/stock/Train_JF.csv", usecols=["date", "open", "close", "high", "low"],dtype={"date": object})
df["date"] = pd.to_datetime(df["date"])
df["time"] = date2num(df["date"])


fig = plt.figure()
ax = plt.subplot(1,1,1)
ax.xaxis_date()
arr = df[["time", "open", "close", "high", "low"]].values
mpf.candlestick_ochl(ax,arr,colorup="red",colordown="green")
df["mid"] = df["close"].rolling(window=20).mean()
plt.plot(df["date"],df["mid"],color="yellow",label="Centerline")
df["std"] = df["close"].rolling(window=20).std()
df["up"] = df["mid"] + 2*df["std"]
plt.plot(df["date"],df["up"],color="green",label="Upper resistance line")
df["down"] = df["mid"] - 2*df["std"]
plt.plot(df["date"],df["down"],color="blue",label="Lower support line")


ax.set_ylabel("CLOSE PRICE")
ax.legend()
plt.title("Bollinger Bands channels Strategy")
plt.show()
