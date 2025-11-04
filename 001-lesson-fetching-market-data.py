# Lesson 1: Fetching Market Data
# In quant finance, everything starts with data!
# We'll use the yfinance library to get stock prices from Yahoo Finance.

import yfinance as yf

# Let's fetch data for Nike (NKE) - a sports company you might know!
# The Ticker object represents a stock
ticker = yf.Ticker("NKE")

# Get historical price data for the last month
# The history() method returns a DataFrame with columns:
# - Open: Opening price of the day
# - High: Highest price during the day  
# - Low: Lowest price during the day
# - Close: Closing price of the day
# - Volume: Number of shares traded
data = ticker.history(period="1mo")

print("Nike Stock Data (Last Month):")
print(data)

# Let's look at just the closing prices
print("\nClosing Prices:")
print(data['Close'])

# Get the most recent closing price
# .iloc[-1] means "get the item at index -1"
# In Python, negative indices count from the end:
# -1 = last item, -2 = second to last, etc.
# So data['Close'].iloc[-1] gets the last closing price in the series
latest_price = data['Close'].iloc[-1]
print(f"\nNike's latest closing price: ${latest_price:.2f}")

# Let's see how indexing works:
print("\n--- Understanding iloc indexing ---")
print(f"First closing price (iloc[0]): ${data['Close'].iloc[0]:.2f}")
print(f"Second closing price (iloc[1]): ${data['Close'].iloc[1]:.2f}")
print(f"Last closing price (iloc[-1]): ${data['Close'].iloc[-1]:.2f}")
print(f"Second to last (iloc[-2]): ${data['Close'].iloc[-2]:.2f}")
