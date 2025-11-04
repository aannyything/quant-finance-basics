# Exercise 2: Fetch Your Own Stock Data
# 
# YOUR TASK:
# 1. Pick an esports or gaming company stock ticker:
#    - EA (Electronic Arts)
#    - TTWO (Take-Two Interactive - makes NBA 2K)
#    - ATVI (Activision Blizzard)
# 
# 2. Fetch the last 3 months of data (period="3mo")
# 3. Print the entire DataFrame
# 4. Calculate and print the percentage change from the first to last closing price
#    Formula: ((last_price - first_price) / first_price) * 100
# 5. Print whether the stock went up or down
#
# Write your code below:

import yfinance as yf

# Fetching data of the specific company ("EA")
# Ticker is the company's stock symbol
ticker = yf.Ticker("EA")

#Fetching the last 3 months of data(period="3mo")
#.history to get the history of the ticker
data = ticker.history(period="3mo")
#printing our the Dataframe
print("ATVI Stock Data (Last 3 Months):")
print(data)
print(data['Close'].iloc[-1])
print(data['Close'].iloc[0])
#calculating percentage changes from first (iloc[0]) to last (iloc[-1]) closing price
percentage_change = data['Close'].iloc[-1] - data['Close'].iloc[0] / data['Close'].iloc[0] * 100
print(f"Percentage change: {percentage_change:.2f}%")

#checking if percentage change was positive or negative
if percentage_change > 0:
    print(f"The stock price of EA went up by {percentage_change:.2f}%")
else:
    print(f"The stock price of EA went down by {percentage_change:.2f}%")