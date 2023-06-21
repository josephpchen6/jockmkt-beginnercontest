import pandas as pd
import os

df = pd.DataFrame()

for file in os.listdir("jock_mkt_data"):
    df = pd.concat([df, pd.read_csv(f"jock_mkt_data/{file}", engine = 'python')])

df["LAST_PRICE"] = df["LAST_PRICE"] + 0.01
max_shares = 125 // df["LAST_PRICE"].astype(float) #Contest: 500, Free: 125

df = pd.concat([df["NAME"], (df["SUGGESTED_PRICE"] - 1.02 * df["LAST_PRICE"]) / df["LAST_PRICE"], 
    ((0.98 * df["SUGGESTED_PRICE"] - .2) - 1.02 * df["LAST_PRICE"]) / (1.02 * df["LAST_PRICE"]),
    max_shares, max_shares * df["LAST_PRICE"] * 1.02,
    max_shares * (((0.98 * df["SUGGESTED_PRICE"] - .2)) - 1.02 * df["LAST_PRICE"])], axis=1)

df.columns = ["Player", "Profit/Coin (to HOLD)", "Tax-Adjusted Profit/Coin (to SELL)", "Total Shares", "Total Cost", "Total Profit"]

'''
Tax-Adjusted Profit/Coin assumes you will SELL the player after the IPO ends, factoring in taxes both ways
Profit/Coin assumes you will HOLD the player after the IPO ends, thus only factoring in the buyer's tax
(when stocks are sold back to the market, seller's tax is not applied).

NHL: pregame stocks usually increase over time, so if two stocks are (close to) tied, tiebreaker is start time (later = better)
Not really sure if this is the case with the NBA
'''

df = df.sort_values(by=["Total Profit"], ascending = False)

print(df.head(10))
# print(df.to_string())
#Change head value if viewing more players is desired

"he He he ah"
