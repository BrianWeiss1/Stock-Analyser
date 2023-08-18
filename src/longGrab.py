import yfinance as yf
import datetime

start_time = datetime.datetime.now()
highSense = {}
mediumSense = {}
lowSense = {}
# low - 500mil+
# medium - 100mil+
# high - 20mil+

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
def grabMarketCap(stockMarketCap, symbol):
    if stockMarketCap == None:
        return False
    if stockMarketCap > 500000000:
        highSense[symbol] = False
        mediumSense[symbol] = False
        lowSense[symbol] = True
        return True
    elif stockMarketCap > 100000000:
        highSense[symbol] = False
        mediumSense[symbol] = True
        lowSense[symbol] = False  
        return True
    elif stockMarketCap > 20000000:
        highSense[symbol] = True
        mediumSense[symbol] = False
        lowSense[symbol] = False
        return True
    else:
        return True

# def getStockPredictionMean(stock):
#     try:
#         if stock.info['marketCap'] < 100000000:
#             return None
#     except:
#          return None
#     try:
#         currentStockPrice = stock.info['currentPrice']
#         meanStockPrice = stock.info['targetMeanPrice']
#     except:
#          return None
#     if stock.info['numberOfAnalystOpinions'] < 3:
#         return None
#     assumedPercentChange = ((meanStockPrice/currentStockPrice)*100)-100 # find % increase/decrease
#     return assumedPercentChange

def getStockPredictionMedian(stock):
    try:
        if grabMarketCap(stock.info['marketCap'], stock.info['symbol']) == False:
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

fstock = open("documents/stocks.txt", 'r')

stockList = fstock.readlines()

fstock.close()


stockList = stockList[0]
stockList = stockList[0:len(stockList)]
stockList = eval(stockList)


stockList2 = []

try:    
    listMedian = []
    # listMean = []
    for symbol in stockList:
        stock = checkStock(symbol)
        stockPredictionMedian = getStockPredictionMedian(stock)
        # stockPredictionMean = getStockPredictionMean(stock)
        if (stockPredictionMedian != None):
            listMedian.append([symbol, stockPredictionMedian])
            print(symbol)
            stockList2.append(symbol)
        # if (stockPredictionMean != None):
        #     listMean.append([symbol, stockPredictionMean])
except:
    print("Keyboard error: " + listMedian)

selection_sort(listMedian)

end_time = datetime.datetime.now()

# Calculate the execution time
execution_time = end_time - start_time
print(f"Execution time: {execution_time}")

a = 'y'
if (a == 'y' or a == 'Y'):
    medianfile = open('documents/medianlist.txt', 'w')
    medianfile.write(str(listMedian))
    medianfile.close()

# selection_sort(listMean)

# if (a == 'y' or a == 'Y'):
#     meanfile = open('documents/meanlist.txt', 'w')
#     meanfile.write(str(listMean))
#     meanfile.close()

if (a == 'y' or a == 'Y'):
    stockUpdatedFile = open('documents/stocks2.txt', 'w')
    stockUpdatedFile.write(str(stockList2))
    stockUpdatedFile.close()

if (a == 'y' or a == 'Y'):
    fileHighSense = open('documents/highSensitivity.txt', 'w')
    fileHighSense.write(str(highSense))
    fileHighSense.close()

if (a == 'y' or a == 'Y'):
    fileMedSense = open('documents/mediumSensitivity.txt', 'w')
    fileMedSense.write(str(mediumSense))
    fileMedSense.close()

if (a == 'y' or a == 'Y'):
    fileLowSense = open('documents/lowSensitivity.txt', 'w')
    fileLowSense.write(str(lowSense))
    fileLowSense.close()