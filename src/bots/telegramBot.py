import yfinance as yf
import time
import datetime
import telebot
previous = {}
prediction = {}
stockList = ['LIFE', 'SGMO', 'ALT']
invested = {'LIFE': 200, 'SGMO': 150, 'ALT': 100}
previous = {'LIFE': 1.958, 'SGMO': 1.24, 'ALT': 2.99}
prediction = {'LIFE': 19.5, 'SGMO': 8.0, 'ALT': 22.0}
DAY = 3


def grabDetails(current):
    for symbol in stockList:
        stock = yf.Ticker(symbol)
        current[symbol] = stock.info['currentPrice']
    return current

BOT_TOKEN = '6452183517:AAGKA2dzsRbHc06amA_RhhfWeLUrFsLwbHw' # old 6115317421:AAHE51UxbBATUyzQPUiC0qr12EfyW0NYSsg

bot = telebot.TeleBot(BOT_TOKEN)
     
@bot.message_handler(commands=['start'])
def start(message):
    for i in range(365):
        current = {}
        current = grabDetails(current)
        for i in range(len(stockList)):
            symbol = stockList[i]
            percentIncrease = ((current[symbol]/previous[symbol])*100)-100
            awayFromPrediction = ((current[symbol]/prediction[symbol])*100)-100
            
            cost = "Bought At: " + str(previous[symbol])
            currentPrice = "Currently: " + str(current[symbol]) 
            increase = "Increase: " + str(round(percentIncrease, 2)) + "%"
            awayFromPrediction = "From " + str(round(abs(awayFromPrediction), 2)) + " % " + "from " + str(prediction[symbol])
            # prediction = str(prediction[symbol]) + "a"
            predicted = "Predicted: " + str(prediction[symbol])
            putIn = "Spent: $" + str(invested[symbol])
            total = "Total: $" +  str(round((((percentIncrease + 100) / 100) * invested[symbol]), 2))
            profit = "Profit: $" + str(round((((percentIncrease + 100) / 100) * invested[symbol]) - invested[symbol], 2))
            date = "Date: " + str(datetime.date.today())
            website = "https://finance.yahoo.com/quote/" + symbol


            bot.send_message(message.chat.id,str(symbol) + "\n\n" + putIn + "\n" + total + "\n" + profit + "\n\n" + cost + "\n" + currentPrice + "\n" + predicted + "\n\n" + increase + "\n" + awayFromPrediction + "\n\n" + date + "\n\n" + website)
        time.sleep(86400)
bot.infinity_polling()

