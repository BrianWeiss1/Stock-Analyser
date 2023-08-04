# Read the list of stock symbols from the file
with open('documents/stocks2.txt', 'r') as file:
    stock_symbols = file.readlines()
    stock_symbols = eval(stock_symbols[0])
# Process each stock symbol
cleaned_symbols = []
for symbol in stock_symbols:
    cleaned_symbol = symbol.split('^')[0].strip()
    cleaned_symbols.append(cleaned_symbol)

# Write the cleaned symbols back to the file
print(len(cleaned_symbols))
print(cleaned_symbols)
with open('documents/stockstest.txt', 'w') as file:
    file.write(str(cleaned_symbols))

print("Symbols cleaned and saved to 'cleaned_stocks.txt'")
print(len(stock_symbols))
print(len(cleaned_symbols))