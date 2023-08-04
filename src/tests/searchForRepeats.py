fstock = open("documents/stocks2.txt", 'r')

stockList = fstock.readlines()
stockList = eval(stockList[0])

fstock.close()

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


stockList = remove_duplicates(stockList)

fstock = open('documents/stock2.txt', 'w')
fstock.write(str(stockList))
fstock.close()



