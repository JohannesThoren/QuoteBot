import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()
bot = commands.Bot("!")


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@bot.event
async def on_message(message):
    if message.author == client.user:
        return

    await bot.process_commands(message)


bot.run(os.getenv("TOKEN"))
