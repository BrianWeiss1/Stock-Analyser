import yfinance as yf
import time
from termcolor import colored

previous = {}
prediction = {}
stockList = ['LIFE', 'SGMO', 'ALT']
invested = {'LIFE': 200, 'SGMO': 150, 'ALT': 100}
def __innit__():
    for symbol in stockList:
        stock = yf.Ticker(symbol)
        previous[symbol] = stock.info['currentPrice']
        prediction[symbol] = (stock.info['targetMedianPrice'])
        print(prediction)
__innit__()

def grabDetails(current):
    try:
        for symbol in stockList:
            stock = yf.ticker(symbol)
            previous[stock] = stock.info['currentPrice']
        return True
    except:
        return False


def run(current):
    if (grabDetails(current)):
        return current
    else:
        print("error 301")

import telebot

BOT_TOKEN = '6115317421:AAHE51UxbBATUyzQPUiC0qr12EfyW0NYSsg'

bot = telebot.TeleBot(BOT_TOKEN)
     
@bot.message_handler(commands=['start'])
def start(message):
    for i in range(365):
        bot.send_message(message.chat.id, "Okay, gimme 30 sec")
        time.sleep(30)
        current = {}
        bot.send_message(message.chat.id, "Alr gimme a bit") # find get input
        current = run(current)
        bot.send_message(message.chat.id, "Okay, I got the info:")
        for i in range(len(stockList)):
            symbol = stockList[i]
            percentIncrease = (previous[symbol]/current[symbol])-100
            awayFromPrediction = (current[symbol]/prediction[symbol])-100
            bot.send_message(message.chat.id, "You bought " + str(symbol) + " for " + str(previous[symbol]) + ".\nThe price is now " + str(current[symbol]) + ".\nThis is a " + str(percentIncrease) + "% " + "increase since " + str(time.date()))
            if awayFromPrediction > 0:
                text = colored(awayFromPrediction, 'red')
            else:
                text = colored(awayFromPrediction, 'green')
            bot.send_message(message.chat.id, "You are " + str(text) + " % " + "from " + str(prediction[symbol]))
            bot.send_message(message.chat.id, "In total you have made: $" + str(((percentIncrease+100)/100)*invested[symbol]) + ' from $' + str(invested[symbol]))

        
bot.infinity_polling()



