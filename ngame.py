import os
import discord
import truths
import random
import copy
import datetime


answ = 0
time_at_start = last_played = datetime.datetime.now()
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

def mathgame(ctx):
    global time_at_start
    time_at_start = datetime.datetime.now()
    embed = discord.Embed()
    num1 = random.randint(5,50)
    num2 = random.randint(2,12)
    num3 = random.randint(3,20)
    global answ
    answ = num1 * num2 + num3
    form = f"{num1} x {num2} + {num3}"
    embed.title = f"What is {form}?"
    embed.description = f'You have 10 seconds to answer correctly'
    embed.set_footer(text = "Use calculator and ur super gay")
    return embed