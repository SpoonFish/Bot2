import os
import discord
import truths
import random
import copy
import datetime

last_played = datetime.datetime.now()-datetime.timedelta(seconds=30)
def ngame(ctx):
    global last_played
    if last_played + datetime.timedelta(seconds=30) > datetime.datetime.now():
        return discord.Embed(title=f'You must wait {(last_played + datetime.timedelta(seconds=30) - datetime.datetime.now()).seconds} more seconds to play this again')
    last_played = datetime.datetime.now()
    embed = discord.Embed()
    embed.title = "GOOO!"
    embed.description = f'You have 12 seconds to say FUCK as much as you can'
    return embed
