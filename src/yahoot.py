import yfinance as yf

def grabInfomation(symbol):
    stock = yf.Ticker(symbol)
    print(stock.info)
    print(stock.info["currentPrice"])
    print(stock.info["targetHighPrice"])
    print(stock.info["targetLowPrice"])
    print(stock.info['targetMedianPrice'])
    print(stock.info['recommendationMean'])
    print(stock.info["recommendationKey"])
    print(stock.info["numberOfAnalystOpinions"])

grabInfomation("MSFT")


