import yfinance as yf
import time
import datetime
import discord
import asyncio
from discord.ext import commands
import os
DAY = 6
stockList = ['LIFE', 'SGMO', 'ALT']
invested = {'LIFE': 200, 'SGMO': 150, 'ALT': 100}
previous = {'LIFE': 1.958, 'SGMO': 1.24, 'ALT': 2.99}
prediction = {'LIFE': 19.5, 'SGMO': 8.0, 'ALT': 22.0}

def checkStock(symbol):
    try:
        stock = yf.Ticker(symbol).info
        return stock
    except:
        return None

async def grabDetails(current):
    for symbol in stockList:
        stock = yf.Ticker(symbol)
        current[symbol] = stock.info['currentPrice']
    return current

async def discordRun():
    TOKEN = "MTA0NjA3MDYwMDUwMzkzMDg5MA.G9UwVr.WYqvFy59UrCG-pVRM3GIyn1kU660u4IKVJKWyI"

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='|', intents=intents)

    @bot.event
    async def on_ready():
        print(f'\nLogged in as {bot.user.name}')

    @bot.command()
    async def add(ctx, arg: str):
        message = await ctx.send("You want "+ str(arg) + ", right?")
        await message.add_reaction('✅')
        await message.add_reaction('❌')


        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['✅', '❌'] and reaction.message.id == message.id

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60, check=check)

            if str(reaction.emoji) == '✅':
                await ctx.send('alr: I will add it to the list')
                time.sleep(5)
                try:
                    stockInfo = checkStock(arg)
                    continument = True
                    try:
                        prediction[arg] = stockInfo['targetMedianPrice']
                    except:
                        await ctx.send('Error 006: Invalid Prediction')
                except:
                    await ctx.send("Error 001: Invalid stock signal")
                if continument == True:
                    # await oneRun(ctx) # add later
                    stockList.append(arg)
                    question = "How much did you invest into the stock? (Input a number)"
                    await ctx.send(question)
                    
                    def check(message):
                        return message.author == ctx.author and message.channel == ctx.channel
                    
                    try:
                        response = await bot.wait_for('message', check=check, timeout=60)  # Wait for a response for 60 seconds
                        message = await ctx.send(f'You said: {response.content}')
                        await message.add_reaction('✅')
                        await message.add_reaction('❌')
                        def check(reaction, user):
                            return user == ctx.author and str(reaction.emoji) in ['✅', '❌'] and reaction.message.id == message.id
                        try:
                            reaction, user = await bot.wait_for('reaction_add', timeout=60, check=check)

                            if str(reaction.emoji) == '✅':
                                time.sleep(2)
                                inputtedNumber = int(response.content)
                                invested[arg] = inputtedNumber
                                previous[arg] = stockInfo['currentPrice']
                                await oneRun(ctx)

                            elif str(reaction.emoji) == '❌':
                                await ctx.send('You Bum: try |add ' + str(arg) + " again")                        
                        except asyncio.TimeoutError: # add single expection
                            await ctx.send("Error 003: Please input a number")
                    except asyncio.TimeoutError:
                        await ctx.send('Error 004: You took too long to respond.')


            elif str(reaction.emoji) == '❌':
                await ctx.send('You Bum: try |add ' + str(arg) + " again")
        except asyncio.TimeoutError:
            await ctx.send('Error 005: You took too long to react.')
    async def oneRun(ctx):
        global DAY
        await ctx.send('Day: ' + str(DAY))
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
            predicted = "Predicted: " + str(prediction[symbol])
            putIn = "Spent: $" + str(invested[symbol])
            total = "Total: $" +  str(round((((percentIncrease + 100) / 100) * invested[symbol]), 2))
            profit = "Profit: $" + str(round((((percentIncrease + 100) / 100) * invested[symbol]) - invested[symbol], 2))
            date = "Date: " + str(datetime.date.today())
            website = "https://finance.yahoo.com/quote/" + symbol


            await ctx.send("```py\n" + str(symbol) + "\n\n" + putIn + "\n" + total + "\n" + profit + "\n\n" + cost + "\n" + currentPrice + "\n" + predicted + "\n\n" + increase + "\n" + awayFromPrediction + "\n\n" + date + "\n\n" + website + "\n```")
            time.sleep(5)
    @bot.command()
    async def start(ctx):
        DAY = 6
        await ctx.send("Starting the bot! ")
        for i in range(365):
            await oneRun(ctx)
            DAY+=1
            time.sleep(18400)
    await bot.start(TOKEN)

if __name__ == "__main__":
    for i in range(100):
        asyncio.run(discordRun())

