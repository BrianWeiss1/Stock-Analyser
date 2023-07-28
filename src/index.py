import yfinance as yf
import time

#I want to get the stocks that do well:

# ATM we have 
# LIFE
# SGMO
# ALT
# KZR
previous = {}
prediction = {}
def __innit__():
    stockList = ['LIFE', 'SGMO', 'ALT', 'KZR']
    for symbol in stockList:
        stock = yf.Ticker(symbol)
        print(stock.info)
        previous[stock] = stock.info['currentPrice']
        prediction[stock] = (stock.info['targetMedianPrice'])
__innit__()


# current = {}
# for i in range(365):
#     time.sleep(86400)
    # print("Price Bought at: " + )
    
