import yfinance as yf
import matplotlib.pyplot as plt

# Ask user for a stock symbol
ticker = input("Enter a stock ticker (e.g., AAPL): ")

# Download the past 6 months of historical data for the stock
stock = yf.Ticker(ticker)
hist = stock.history(period="6mo")

# Print basic stock statistics
print(f"\nBasic Price Statistics for {ticker}\n")
print("Highest Close:", hist['Close'].max())   # Highest closing price in the period
print("Lowest Close:", hist['Close'].min())    # Lowest closing price in the period
print("Average Close:", hist['Close'].mean())  # Average closing price in the period
print("Total Volume:", hist['Volume'].sum())   # Total number of shares traded for the past 6 months


# SMA (Simple Moving Average) - average of the last 20 closing prices
hist['SMA_20'] = hist['Close'].rolling(window=20).mean()

# EMA (Exponential Moving Average) - weighted average giving more importance to recent prices
hist['EMA_20'] = hist['Close'].ewm(span=20, adjust=False).mean()

# Plot Closing Price + Moving AverageS
plt.figure(figsize=(10, 5))

# Plot Closing Price
plt.plot(hist.index, hist['Close'], label='Close Price', color='blue')

# Plot 20-day SMA
plt.plot(hist.index, hist['SMA_20'], label='SMA 20', color='orange')

# Plot 20-day EMA
plt.plot(hist.index, hist['EMA_20'], label='EMA 20', color='green')

# Chart formatting
plt.title(f"Stock Price Chart for {ticker.upper()} with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.legend()

# Show chart
plt.show()