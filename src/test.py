import yfinance as yf
def checkStock(symbol):
    try:
        stock = yf.Ticker(symbol)
        return stock
    except:
        return None
    
def getStockPredictionMean(symbol):
    stock = checkStock(symbol)
    # print(stock.info)
    try:
        if stock.info['marketCap'] < 100000000:
            return None
    except:
         return None
    try:
        currentStockPrice = stock.info['currentPrice']
        meanStockPrice = stock.info['targetMeanPrice']
    except:
         return None
    assumedPercentChange = ((meanStockPrice/currentStockPrice)*100)-100 # find % increase/decrease
    return assumedPercentChange
	# stock = checkStock(symbol)
    # if (stock.info['marketCap'] < 100000000): 
    #     return None
    # currentStockPrice = stock.info["currentPrice"] # 100
    # meanStockPrice = stock.info['targetMeanPrice'] # 150
    # assumedPercentChange = ((meanStockPrice/currentStockPrice)*100)-100 # find % increase/decrease
    # return assumedPercentChange # return amount



def getStockPredictionMedian(symbol):
    stock = yf.Ticker(symbol)
    currentStockPrice = stock.info["currentPrice"] # 100
    print(currentStockPrice)
    medianStockPrice = stock.info['targetMeanPrice'] # 150
    print(medianStockPrice)
    if stock.info['numberOfAnalystOpinions'] < 3:
        return None
    assumedPercentChange = ((medianStockPrice/currentStockPrice)*100)-100 # find % increase/decrease
    return assumedPercentChange # return amount

print(getStockPredictionMedian("AIR"))