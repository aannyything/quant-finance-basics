# Lesson 4: Backtesting Trading Strategies
# Now that we can calculate indicators, let's test a simple trading strategy!

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Let's fetch some data
print("Fetching EA stock data...")
ticker = yf.Ticker("EA")
data = ticker.history(period="1y")  # Get 1 year of data

# 2. Calculate our indicators (SMA crossover)
data['SMA_20'] = data['Close'].rolling(window=20).mean()
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# 3. Create signals
# Buy when 20-day SMA crosses above 50-day SMA
# Sell when 20-day SMA crosses below 50-day SMA
data['Signal'] = 0
data.loc[data['SMA_20'] > data['SMA_50'], 'Signal'] = 1
data['Position'] = data['Signal'].diff()

# 4. Calculate daily returns
data['Returns'] = data['Close'].pct_change()

# 5. Calculate strategy returns
data['Strategy_Returns'] = data['Signal'].shift(1) * data['Returns']

# 6. Calculate cumulative returns
data['Cumulative_Market_Returns'] = (1 + data['Returns']).cumprod()
data['Cumulative_Strategy_Returns'] = (1 + data['Strategy_Returns']).cumprod()

# 7. Plot the results
plt.figure(figsize=(12, 8))

# Plot price and moving averages
plt.subplot(2, 1, 1)
plt.plot(data.index, data['Close'], label='Price', alpha=0.5)
plt.plot(data.index, data['SMA_20'], label='20-day SMA', alpha=0.75)
plt.plot(data.index, data['SMA_50'], label='50-day SMA', alpha=0.75)

# Plot buy/sell signals
buy_signals = data[data['Position'] == 1]
sell_signals = data[data['Position'] == -1]
plt.scatter(buy_signals.index, buy_signals['Close'], 
           marker='^', color='g', label='Buy', alpha=1, s=100)
plt.scatter(sell_signals.index, sell_signals['Close'],
           marker='v', color='r', label='Sell', alpha=1, s=100)

plt.title('EA Stock Price with SMA Crossover Strategy')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot cumulative returns
plt.subplot(2, 1, 2)
plt.plot(data.index, data['Cumulative_Market_Returns'], 
        label='Buy & Hold', alpha=0.7)
plt.plot(data.index, data['Cumulative_Strategy_Returns'],
        label='SMA Crossover Strategy', alpha=0.7)
plt.title('Cumulative Returns: Buy & Hold vs. SMA Crossover Strategy')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('backtest_results.png')
plt.show()

# 8. Print performance metrics
total_market_return = (data['Cumulative_Market_Returns'].iloc[-1] - 1) * 100
total_strategy_return = (data['Cumulative_Strategy_Returns'].iloc[-1] - 1) * 100

print(f"\n--- Performance Summary ---")
print(f"Buy & Hold Return: {total_market_return:.2f}%")
print(f"SMA Crossover Strategy Return: {total_strategy_return:.2f}%")

# 9. Next steps:
# - Try different moving average periods
# triple EMA

#EMA = (Current_Price × (2/(N+1))) + (Previous_EMA × (1 - (2/(N+1)))))
data['EMA_10'] = data['Close'].ewm(span=10, adjust=False).mean()
data['EMA_20'] = data['Close'].ewm(span=20, adjust=False).mean()
data['EMA_30'] = data['Close'].ewm(span=30, adjust=False).mean()

data['Signal'] = 0 
data.loc[(data['EMA_10'] > data['EMA_20']) & (data['EMA_10'] > data['EMA_30']), 'Signal'] = 1
data['Position'] = data['Signal'].diff()

data['Returns'] = data['Close'].pct_change()
data['Strategy_Returns'] = data['Signal'].shift(1) * data['Returns']
data['Cumulative_Returns'] = (1 + data['Strategy_Returns']).cumprod()


# Generate buy/sell signals
buy_signals = data[(data['Position'] == 1) & (data['Signal'] == 1)]
sell_signals = data[(data['Position'] == -1) & (data['Signal'] == 0)]

data['Returns'] = data['Close'].pct_change()
data['Strategy_Returns'] = data['Signal'].shift(1) * data['Returns']
data['Cumulative_Returns'] = (1 + data['Strategy_Returns']).cumprod()

# Plotting 
# Triple EMA Strategy Implementation
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# 1. Fetch data
print("Fetching EA stock data...")
ticker = yf.Ticker("EA")
data = ticker.history(period="1y")

# 2. Calculate Triple EMAs
data['EMA_10'] = data['Close'].ewm(span=10, adjust=False).mean()
data['EMA_20'] = data['Close'].ewm(span=20, adjust=False).mean()
data['EMA_30'] = data['Close'].ewm(span=30, adjust=False).mean()

# 3. Generate signals
data['Signal'] = 0
data.loc[(data['EMA_10'] > data['EMA_20']) & (data['EMA_10'] > data['EMA_30']), 'Signal'] = 1
data['Position'] = data['Signal'].diff()

# 4. Calculate returns
data['Returns'] = data['Close'].pct_change()
data['Strategy_Returns'] = data['Signal'].shift(1) * data['Returns']
data['Cumulative_Returns'] = (1 + data['Strategy_Returns']).cumprod()

# 5. Generate buy/sell signals
buy_signals = data[data['Position'] == 1]
sell_signals = data[data['Position'] == -1]

# 6. Plotting
plt.figure(figsize=(14, 8))

# Plot price and EMAs
plt.subplot(2, 1, 1)
plt.plot(data.index, data['Close'], label='Price', alpha=0.7)
plt.plot(data.index, data['EMA_10'], label='10-day EMA', alpha=0.7)
plt.plot(data.index, data['EMA_20'], label='20-day EMA', alpha=0.7)
plt.plot(data.index, data['EMA_30'], label='30-day EMA', alpha=0.7)

# Plot buy/sell signals
plt.scatter(buy_signals.index, buy_signals['Close'], 
           marker='^', color='g', label='Buy', alpha=1, s=100)
plt.scatter(sell_signals.index, sell_signals['Close'],
           marker='v', color='r', label='Sell', alpha=1, s=100)

plt.title('Triple EMA Crossover Strategy - Price and Signals')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot cumulative returns
plt.subplot(2, 1, 2)
plt.plot(data.index, data['Cumulative_Returns'], label='Strategy Returns', color='b')
plt.title('Cumulative Strategy Returns')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('TripleEMA.png')
plt.show()

# 7. Print performance metrics
total_return = (data['Cumulative_Returns'].iloc[-1] - 1) * 100
print(f"\n--- Strategy Performance ---")
print(f"Total Return: {total_return:.2f}%")
print(f"Number of Trades: {len(buy_signals) + len(sell_signals)}")
print(f"Buy Signals: {len(buy_signals)}")
print(f"Sell Signals: {len(sell_signals)}")