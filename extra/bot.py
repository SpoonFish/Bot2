# bot.py
'''import os
import random
import discord
import CP_bot_cmds
from dotenv import load_dotenv
COLOURS = ['red','orange','yellow','green','blue','pink','ruby','sapphire','topaz','emerald','jade','amethyst','diamond']
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

ADMINS = ['SpoonFsh#5129', 'jeels#1028', 'Pereger#1760']
client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


'''

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents= discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)