import yfinance as yf

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j][1] < arr[min_idx][1]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def checkStock(symbol):
    try:
        stock = yf.Ticker(symbol)
        return stock
    except:
        return None

def getStockPredictionMean(stock):
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
    if stock.info['numberOfAnalystOpinions'] < 3:
        return None
    assumedPercentChange = ((meanStockPrice/currentStockPrice)*100)-100 # find % increase/decrease
    return assumedPercentChange

def getStockPredictionMedian(stock):
    try:
        if stock.info['marketCap'] < 100000000:
            return None
    except:
         return None
    try:
        currentStockPrice = stock.info['currentPrice']
        meanStockPrice = stock.info['targetMedianPrice']
    except:
         return None
    if stock.info['numberOfAnalystOpinions'] < 3:
        return None
    assumedPercentChange = ((meanStockPrice/currentStockPrice)*100)-100 # find % increase/decrease
    return assumedPercentChange

def getStockInfomation(symbol):
    stock = yf.Ticker(symbol)
    stock.info["targetHighPrice"]
    stock.info["targetLowPrice"]
    stock.info['recommendationMean']
    stock.info["recommendationKey"]
    stock.info["numberOfAnalystOpinions"]
    
fstock = open("stocks.txt", 'r')

stockList = fstock.readlines()

fstock.close()


stockList = stockList[0]
stockList = stockList[0:len(stockList)-1]
stockList = eval(stockList)

print(stockList)
try:    
    listMedian = []
    listMean = []
    print("a")
    for symbol in stockList:
        stock = checkStock(symbol)
        print("a")
        stockPredictionMedian = getStockPredictionMedian(stock)
        print(stockPredictionMedian)
        stockPredictionMean = getStockPredictionMean(stock)
        if (stockPredictionMedian != None):
            listMedian.append([symbol, stockPredictionMedian])
            print(symbol)
        if (stockPredictionMean != None):
            listMean.append([symbol, stockPredictionMean])
except:
    print("Keyboard error: " + listMedian)

selection_sort(listMedian)

print( "List Median is " + str(listMedian))

a = input("You got that?")

selection_sort(listMean)

print( "List mean is " + str(listMean))

# fmean.close()
# fmedian.close()
a = input("You got that?")

