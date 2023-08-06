import discord
from discord.ext import commands
import os

# Replace 'YOUR_TOKEN_HERE' with your actual bot token
TOKEN = os.environ.get("pythonBotToken")

intents = discord.Intents.default()  # Creates a default set of intents
intents.message_content = True  # Enable message content intent

bot = commands.Bot(command_prefix='|', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def start(ctx):
    await ctx.send("Starting the bot!")

bot.run(TOKEN)

