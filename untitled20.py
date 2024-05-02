import yfinance as yf

# Create a Ticker object for Microsoft (MSFT)
msft = yf.Ticker("tup")

# Option 1: Using __dict__ attribute
# print(msft.__dict__)

# Option 2: Using dir() function
# print(dir(msft))

print((msft.dividends))