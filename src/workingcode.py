import yfinance as yf

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

# print(stockList)
# try:    
#     listMedian = []
#     listMean = []
#     for symbol in stockList:
#         stock = checkStock(symbol)
#         stockPredictionMedian = getStockPredictionMedian(stock)
#         stockPredictionMean = getStockPredictionMean(stock)
#         if (stockPredictionMedian != None):
#             listMedian.append([symbol, stockPredictionMedian])
#             print(symbol)
#         if (stockPredictionMean != None):
#             listMean.append([symbol, stockPredictionMean])
# except:
#     print("Keyboard error: " + listMedian)
    
# print(listMedian)
# print("\n\n\n\n\n\n")
# print(listMean)
# print("\n\n\n\n\n\n")

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Assume the minimum element is at index i
        min_idx = i

        # Find the index of the minimum element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j][1] < arr[min_idx][1]:
                min_idx = j

        # Swap the minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
# import ast
fmean = open("meanlist.txt", 'r')
fmedian = open("medianlist.txt", 'r')

listMean = fmean.readlines()
listMean = eval(listMean[0])

listMedian = fmedian.readlines()
listMedian = eval(listMedian[0])
# selection_sort(listMedian)

# print( "List Median is " + str(listMedian))

# # fmean.close()
# # fmedian.close()
# a = input("You got that?")
# selection_sort(listMean)

# print( "List mean is " + str(listMean))

# # fmean.close()
# # fmedian.close()
# a = input("You got that?")


print("List Mean is " + str(listMean))
print("The top 3 investments for buying are: (MEDIAN)")
print("1. " + str(listMedian[len(listMedian)-1]))
print("2. " + str(listMedian[len(listMedian)-2]))
print("3. " + str(listMedian[len(listMedian)-3]))
print("\n")

print("The top 3 investments for shorting are: (MEDIAN)")
print("1. " + str(listMedian[0]))
print("2. " + str(listMedian[1]))
print("3. " + str(listMedian[2]))
print("\n")
previousExtenedAmount = 3
thing = True
while(thing == True):
    extendAnswer = input("Would you like to extend this? (y/n) ")
    print("\n")


    if extendAnswer == 'y' or extendAnswer == 'Y':
        extendAmount = input("How much would you like to extend this by? ")
        print("\n")
        increaseAmount = int(extendAmount)+previousExtenedAmount
        previousExtenedAmount = increaseAmount
        print("The top " + str(increaseAmount) + " investments for buying are: (MEDIAN)\n")
        for i in range(increaseAmount):
            print(str(i+1) + ". " + str(listMean[len(listMean)-(i+1)]))
        print("\n\n\nThe top " + str(increaseAmount) + " investments for shorting are: (MEDIAN)\n")
        for i in range(increaseAmount):
            print(str(i+1) + ". " + str(listMean[i]))
    else:
        thing == False
        break

print("The top 3 investments for buying are: (MEAN)")
print("1. " + str(listMean[len(listMean)-1]))
print("2. " + str(listMean[len(listMean)-2]))
print("3. " + str(listMean[len(listMean)-3]))
print("\n")
print("The top 3 investments for shorting are: (MEAN)")
print("1. " + str(listMean[0]))
print("2. " + str(listMean[1]))
print("3. " + str(listMean[2]))
print("\n")

previousExtenedAmount = 3
thing = True
while(thing == True):
    extendAnswer = input("Would you like to extend this? (y/n) ")
    print("\n")

    if extendAnswer == 'y' or extendAnswer == 'Y':
        extendAmount = input("How much would you like to extend this by? ")
        print("\n")
        increaseAmount = int(extendAmount)+previousExtenedAmount
        previousExtenedAmount = increaseAmount
        print("The top " + str(increaseAmount) + " investments for buying are: (MEDIAN)\n")
        for i in range(increaseAmount):
            print(str(i+1) + ". " + str(listMean[len(listMean)-(i+1)]))
        print("\n\n\nThe top " + str(increaseAmount) + " investments for shorting are: (MEDIAN)\n")
        for i in range(increaseAmount):
            print(str(i+1) + ". " + str(listMean[i]))
    else:
        thing == False
        break
