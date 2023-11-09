
import pandas as pd
# "date", "open", "close", "high", "low"
df = pd.read_csv("/Users/Andi/Desktop/stock/Test_JF.csv", usecols=["date", "open", "close", "high", "low"],dtype={"date": object})
# short and long
df["ma5"] = df["close"].rolling(5,min_periods = 1).mean()
df["ma30"] = df["close"].rolling(30,min_periods = 1).mean()

golden_cross = []
death_cross = []
# loop data set
for i in range(1,len(df)):
    # When the short-term moving average value of a day is greater than the long-term moving average value,
    # and the short-term moving average value of the previous day is less than the long-term moving average value
    if df["ma5"][i] >= df["ma30"][i] and df["ma5"][i-1] < df["ma30"][i-1]:
        # golden cross
        golden_cross.append(df["date"][i])
     # When the short-term moving average value of a certain day is less than the long-term moving average value,
    # and the short-term moving average value of the previous day is greater than the long-term moving average value
    if df["ma5"][i] < df["ma30"][i] and df["ma5"][i-1] > df["ma30"][i-1]:
        # add the date cross
        death_cross.append(df["date"][i])

# order
# golden cross,value=1
S1 = pd.Series(1,index = golden_cross)
# death cross，value=o
S2 = pd.Series(0,index = death_cross)

sr = pd.concat([S1,S2]).sort_index()
# present value
first_money = 100000
# the total money
money = first_money
# when this is 0
hold = 0
# the loop
for i in range(0,len(sr)):
    # the date of golden and death cross
    p = df[df["date"] == sr.index[i]]["open"].values[0]
    # golden cross
    if sr.iloc[i] == 1:

        # how many money
        buy = (money // (100 * p))
        # stock
        hold += buy *100
        # the moeny after trading
        money -= buy*100*p
    # death cross
    else:
        # money
        money += hold*p
        # stock 0
        hold = 0
# open price for the last day
p = df["open"].values[-1]
# final money
now_money = hold*p+money
# outcome
print("The Dual Line Strategy:",now_money - first_money)