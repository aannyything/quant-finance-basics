
# Exercise 3: Calculate Moving Averages
# 
# Moving averages help smooth out price data to identify trends.
# We'll calculate two types:
# 1. Simple Moving Average (SMA) - average of last N days
# 2. Exponential Moving Average (EMA) - gives more weight to recent prices
#
# YOUR TASKS:
# 1. Fetch 6 months of data for EA (Electronic Arts)
# 2. Calculate and add 20-day and 50-day SMAs to the DataFrame
# 3. Calculate and add 20-day and 50-day EMAs to the DataFrame
# 4. Print the last 5 rows of the DataFrame to see the latest values
# 5. Bonus: Add a column that shows when the 20-day SMA crosses above the 50-day SMA (a "golden cross")
#
# HINTS:
# - Use pandas' .rolling() for SMA
# - Use .ewm() for EMA
# - For the bonus, you can use: df['Signal'] = np.where(df['SMA_20'] > df['SMA_50'], 1, 0)

import yfinance as yf
import pandas as pd
import numpy as np

# Your code here

# 1. Fetch data
print("Fetching EA stock data...")
ticker = yf.Ticker("EA")
data = ticker.history(period="6mo")

# 2. Calculate SMAs (Simple Moving Averages)
# Your code here

#20 day SMA
data['SMA_20'] = data['Close'].rolling(window=20).mean()

#50 day SMA
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# 3. Calculate EMAs (Exponential Moving Averages)
# Your code here

#20 day EMA
#EMA = (Current_Price × (2/(N+1))) + (Previous_EMA × (1 - (2/(N+1)))))
data['EMA_20'] = data['Close'].ewm(span=20, adjust=False).mean()

#50 day EMA
data['EMA_50'] = data['Close'].ewm(span=50, adjust=False).mean()

# 4. Print last 5 rows
print("\nLatest data with indicators:")
# Your code here
print(data.tail(5))

# 5. Bonus: Golden cross signal
# Your code 
data['Signal'] = 0
data.loc[data['SMA_20'] > data['SMA_50'], 'Signal'] = 1
data['Golden_Cross'] = (data['Signal'] == 1) & (data['Signal'].shift(1) == 0)
print(data[data['Golden_Cross']].index) 