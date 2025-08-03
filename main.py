import yfinance as yf
import matplotlib.pyplot as plt

# Ask user for a stcok symbol 

ticker = input("Enter a stock ticker (e.g., AAPL): ")

# Download data

stock = yf.Ticker(ticker)
hist = stock.history(period="6mo")

# Print stock stats

print(f"\nBasic Price Statistics for {ticker}\n")
print("Highest Close:", hist['Close'].max())
print("Lowest Close:", hist['Close'].min())
print("Average Close:", hist['Close'].mean())
print("Total Volume:", hist['Volume'].sum())    # Total number of shares traded for the past 6 months

# Stock's closing price chart over time using matplotlib

plt.figure(figsize=(10, 5))
plt.plot(hist.index, hist['Close'], label='Close Price', color='blue')

plt.title(f"Stock Price Chart for {ticker.upper()}")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.grid(True)
plt.legend()

plt.show()