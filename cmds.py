import os
import discord
import truths
import random
import copy

recent_truths = []
def tod(ctx):
    global recent_truths
    select_from_truths = copy.deepcopy(truths.truths)
    for tr in recent_truths:
        try: select_from_truths.remove(tr)
        except: pass
    truth = random.choice(select_from_truths)
    recent_truths.insert(0, truth)
    if len(recent_truths) > 25:
        recent_truths = recent_truths[:25]
    embed = discord.Embed()
    embed.title = truth
    embed.description = f'requested by {ctx.author.name}'
    embed.colour = discord.Colour(random.randint(0,255))
    embed.set_thumbnail(url="attachment://image.png")
    embed.set_footer(text='read if gay',) 
    if ctx.author.name == 'ria':
        embed.remove_footer()
        embed.set_footer(text='ria go to sleep..')
    return embed

def ball9(ctx, thing:str):
    embed = discord.Embed()
    result = random.choice(["Yes","OH MOST DEFINITELY", "hell no", "no, bozo","naw","rawwwr uwu","*maybe*", "kinda", "i guess..", "thats just a rumour", "sureee..", "i think so", "quite the opposite", "not reallyyy", "50/50"])
    embed.title = f"{thing.capitalize()}? {result}"
    return embed
