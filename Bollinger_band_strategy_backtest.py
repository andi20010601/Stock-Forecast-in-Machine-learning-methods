
import pandas as pd
df = pd.read_csv("/Users/Andi/Desktop/stock/Test_JF.csv", usecols=["date", "open", "close", "high", "low"])

df['mid'] = df['close'].rolling(window=20).mean()
df['std'] = df['close'].rolling(window=20).std()
df['up'] = df['mid'] + 2*df['std']
df['down'] = df['mid'] - 2*df['std']

sr1 = df['open'] > df['up']
sr2 = df['open'] < df['down']
sale_signal = df['date'][sr1]
buy_signal = df['date'][sr2]


first_money = 100000
money = first_money
hold = 0
s1 = pd.Series(1,index = buy_signal)
s2 = pd.Series(0,index = sale_signal)
sr = pd.concat([s1,s2]).sort_index()
for i in range(0,len(sr)):
    p = df[df["date"] == sr.index[i]]["open"].values[0]
    if sr.iloc[i] == 1:
        buy = (money // (100 * p))
        hold += buy *100
        money -= buy*100*p
    else:
        money += hold*p
        hold = 0
p = df["open"].values[-1]
now_money = hold*p+money
print("Bollinger Bands Strategy Back Test:",now_money - first_money)