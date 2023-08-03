fstock = open("documents/stocks.txt", 'r')

stockList = fstock.readlines()

fstock.close()
stockList = stockList[0]
stockList = stockList[0:len(stockList)]
stockList = eval(stockList)
print(len(stockList))
fstock = open("documents/stocks2.txt", 'r')

stockList2 = fstock.readlines()

stockList2 = stockList2[0]
stockList2 = stockList2[0:len(stockList2)]
stockList2 = eval(stockList2)

fstock.close()
print(len(stockList2))

stock = None
print(len(stockList))
def append_unique_options(stockList, stockList2):
    for option in stockList2:
        if option.strip() not in stockList:
            stockList.append(option)

append_unique_options(stockList, stockList2)

print(stockList)
print(len(stockList))
fileMedSense = open('documents/stocks3.txt', 'w')
fileMedSense.write(str(stockList))
fileMedSense.close()

