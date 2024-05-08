import yfinance as yf
import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict

start_time = datetime.datetime.now()
highSense: Dict[str, int] = {}
mediumSense: Dict[str, int] = {}
lowSense: Dict[str, int] = {}

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
    if stockMarketCap > 500000000: # 5 bil
        highSense[symbol] = False
        mediumSense[symbol] = False
        lowSense[symbol] = True
        return True
    elif stockMarketCap > 100000000: # 1 bil
        highSense[symbol] = False
        mediumSense[symbol] = True
        lowSense[symbol] = False  
        return True
    elif stockMarketCap > 30000000: # 200 mil
        highSense[symbol] = True
        mediumSense[symbol] = False
        lowSense[symbol] = False
        return True
    else:
        return True


def getStockPredictionMedian(stock):
    try:
        # print(stock.info)
        if grabMarketCap(stock.info['marketCap'], stock.info['symbol']) == False:
            return None
        if stock.info['currentPrice'] < 3:  # Check if stock price is over $3
            return None
    except:
         return None
    try:
        currentStockPrice = stock.info['currentPrice']
        medianStockPrice = stock.info['targetMedianPrice']
    except:
         return None
    if stock.info['numberOfAnalystOpinions'] < 3:
        return None
    assumedPercentChange = ((medianStockPrice / currentStockPrice) * 100) - 100
    return assumedPercentChange

def process_stock(symbol):
    stock = checkStock(symbol)
    stockPredictionMedian = getStockPredictionMedian(stock)
    if stockPredictionMedian is not None:
        return [symbol, stockPredictionMedian]


fstock = open("src/documents/stocks.txt", 'r')

stockList = fstock.readlines()

fstock.close()


stockList = stockList[0]
stockList = stockList[0:len(stockList)]
stockList = eval(stockList)

stockList2 = []


with ThreadPoolExecutor() as executor:
    futures = {executor.submit(process_stock, symbol): symbol for symbol in stockList}
    listMedian = []
    for future in as_completed(futures):
        result = future.result()
        if result is not None:
            listMedian.append(result)
            print(result[0])
            stockList2.append(result[0])

selection_sort(listMedian)

end_time = datetime.datetime.now()
execution_time = end_time - start_time
print(f"Execution time: {execution_time}")











end_time = datetime.datetime.now()

# Calculate the execution time
execution_time = end_time - start_time
print(f"Execution time: {execution_time}")

a = 'y'
if (a == 'y' or a == 'Y'):
    medianfile = open('src/documents/medianlist.txt', 'w')
    medianfile.write(str(listMedian))
    medianfile.close()

# selection_sort(listMean)

# if (a == 'y' or a == 'Y'):
#     meanfile = open('documents/meanlist.txt', 'w')
#     meanfile.write(str(listMean))
#     meanfile.close()

if (a == 'y' or a == 'Y'):
    stockUpdatedFile = open('src/documents/stocks2.txt', 'w')
    stockUpdatedFile.write(str(stockList2))
    stockUpdatedFile.close()

if (a == 'y' or a == 'Y'):
    fileHighSense = open('src/documents/highSensitivity.txt', 'w')
    fileHighSense.write(str(highSense))
    fileHighSense.close()

if (a == 'y' or a == 'Y'):
    fileMedSense = open('src/documents/mediumSensitivity.txt', 'w')
    fileMedSense.write(str(mediumSense))
    fileMedSense.close()

if (a == 'y' or a == 'Y'):
    fileLowSense = open('src/documents/lowSensitivity.txt', 'w')
    fileLowSense.write(str(lowSense))
    fileLowSense.close()