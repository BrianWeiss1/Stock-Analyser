fstock = open("documents/stocks.txt", 'r')

stockList = fstock.readlines()

fstock.close()
stockList = stockList[0]
stockList = stockList[0:len(stockList)]
stockList = eval(stockList)

fstock = open("documents/stocks2.txt", 'r')

stockList2 = fstock.readlines()

stockList2 = stockList2[0]
stockList2 = stockList2[0:len(stockList2)]
stockList2 = eval(stockList2)

fstock.close()

# print(stockList)

# print('\n\n')

# print(stockList2)

stock = None
print(len(stockList))
def append_unique_options(stockList, stockList2):
    for option in stockList2:
        if option.strip() not in stockList:
            stockList.append(option.strip())

append_unique_options(stockList, stockList2)

print(stockList)
print(len(stockList))

# print(stockList.sort())
