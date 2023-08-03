fstock = open("documents/stocks.txt", 'r')

stockList = fstock.readlines()

fstock.close()
stockList = stockList[0]
stockList = stockList[0:len(stockList)]
stockList = eval(stockList)
def custom_sort(stock_symbols):
    def sorting_key(symbol):
        return symbol.ljust(10)  # Assuming a maximum length of 10 characters
    
    return sorted(stock_symbols, key=sorting_key)

# Example usage:
print(len(stockList))
stock_symbols = stockList
sorted_symbols = custom_sort(stock_symbols)
print(sorted_symbols)
print(len(sorted_symbols))
