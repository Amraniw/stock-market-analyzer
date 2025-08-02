import yfinance as yf

# Ask user for a stcok symbol 
ticker = input("Enter a stock ticker (e.g., AAPL): ")

# Download data
stock = yf.Ticker(ticker)
hist = stock.history(period="1d")

# Show first 5 rows
print(hist.head())