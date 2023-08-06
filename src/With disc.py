import yfinance as yf
import time
import datetime
import telebot
import discord
import asyncio
from discord.ext import commands
import os


previous = {}
prediction = {}
stockList = ['LIFE', 'SGMO', 'ALT']
invested = {'LIFE': 200, 'SGMO': 150, 'ALT': 100}
previous = {'LIFE': 1.958, 'SGMO': 1.24, 'ALT': 2.99}
prediction = {'LIFE': 19.5, 'SGMO': 8.0, 'ALT': 22.0}

def checkStock(symbol):
    try:
        stock = yf.Ticker(symbol)
        return stock
    except:
        return None

def grabDetails(current):
    for symbol in stockList:
        stock = yf.Ticker(symbol)
        current[symbol] = stock.info['currentPrice']
    return current
async def telegramRun():
    DAY = 6

    TELEGRAMBOTTOKEN = os.environ.get("telegramBotToken") # old 6115317421:AAHE51UxbBATUyzQPUiC0qr12EfyW0NYSsg

    bot = telebot.TeleBot(TELEGRAMBOTTOKEN)
    @bot.message_handler(commands=['start'])
    def start2(message):
        for i in range(365):
            bot.send_message(message.chat.id, 'Day: ' + DAY+i)
            day+=1
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


async def discordRun():
    TOKEN = os.environ.get("pythonBotToken")

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='|', intents=intents)

    @bot.event
    async def on_ready():
        print(f'\nLogged in as {bot.user.name}')

    @bot.command()
    async def add(ctx, arg: str):
        print(arg)
        currentDisc = {}

        message = await ctx.send("You want "+ str(arg) + ", right?")
        await message.add_reaction('✅')
        print('a')
        await message.add_reaction('❌')


        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['✅', '❌'] and reaction.message.id == message.id

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60, check=check)

            if str(reaction.emoji) == '✅':
                await ctx.send('alr: I will add it to the list')
                time.sleep(5)
                try:
                    current = grabDetails(arg)
                    continument = True
                except:
                    await ctx.send("Error 1: Invalid stock signal")
                if continument == True:
                    ctx.send(str(current[symbol]))
            elif str(reaction.emoji) == '❌':
                await ctx.send('You Bum: try |add ' + str(arg) + " again")
        except asyncio.TimeoutError:
            await ctx.send('You took too long to react.')
        
    @bot.command()
    async def start(ctx):
        # global day
        DAY = 6
        await ctx.send("Starting the bot! ") #works until this point
        for i in range(365):
            print('a')
            await ctx.send('Day: ' + str(DAY+i))
            current = {}
            current = grabDetails(current)
            for i in range(len(stockList)):
                print('1')
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


                await ctx.send(str(symbol) + "\n\n" + putIn + "\n" + total + "\n" + profit + "\n\n" + cost + "\n" + currentPrice + "\n" + predicted + "\n\n" + increase + "\n" + awayFromPrediction + "\n\n" + date + "\n\n" + website)
                time.sleep(5)
            time.sleep(18400)
    await bot.start(TOKEN)

# Assuming this code is in your main module
if __name__ == "__main__":
    for i in range(100):
        asyncio.run(discordRun())

