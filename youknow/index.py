# I want to create a file that grabs the data from the top 3000 stocks and the top 200 cryptos, see what major events happen in the time frame of 1h, 5min, 10in, and 20min



import yfinance
import time


current = time.time
print(yfinance.Ticker.info)