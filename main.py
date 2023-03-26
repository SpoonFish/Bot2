import os
import ngame
import datetime
import discord
import random
import cmds
from discord.ext import commands
from dotenv import load_dotenv

current_game = ''
current_game_scores = {
    "Bulp (バールプ)" : 0,
    "SpoonFsh" : 0,
    "ria" : 0,
    "Cybin" : 0,
    "チョコ" : 0,
    "col" : 0,
    "greed" : 0,

}
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
prefix = '>'
intents = discord.Intents.all()
client = commands.Bot(intents=intents , command_prefix= ">")
def truthView(ctx):
    class Truth(discord.ui.View):
        
        @discord.ui.button(label=f"Truth", style=discord.ButtonStyle.blurple)
        async def third_button_callback(self, button, interaction, ctx = ctx):
            await truth(ctx)
    return Truth()
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.slash_command(name="games-fuck", description='play the fuck game')
async def fuckgame(ctx):
    global current_game
    current_game = 'ngame'
    embed = ngame.ngame(ctx)
    await ctx.respond(embed = embed)
@client.slash_command(name="truth", description='knowledge is pain, knowledge is power')
async def truth(ctx):
    embed = discord.Embed()
    embed = cmds.tod(ctx)
    try: await ctx.respond(embed = embed, view = truthView(ctx))
    except: await ctx.channel.send(embed = embed, view = truthView(ctx))

@client.event
async def on_message(message):
    global current_game
    if message.author.bot:
        return
    if current_game == 'ngame':
        if ngame.last_played + datetime.timedelta(seconds=12) < datetime.datetime.now():
            embed = discord.Embed()
            embed.title = "The game is over!"
            high = 0
            highp = 'Nobody'
            for p in current_game_scores:
                if current_game_scores[p] > high:
                    high = current_game_scores[p]
                    highp = p
            embed.description = f'**{highp}** wins with {high} points!'
            for player in current_game_scores:
                current_game_scores[player] = 0
            current_game = ''
            await message.channel.send(embed = embed)
        cont = message.content.lower()
        if 'fuck' in cont:
            try: current_game_scores[message.author.name] += 1
            except: pass

    if message.content.startswith(f"{prefix}tod") or message.content.startswith(f"{prefix}truth"):
        embed = cmds.tod(message)
        await message.channel.send(embed = embed, view = truthView(message))
    elif message.content.startswith(f"{prefix}games"):
        if message.content == f"{prefix} games":
            embed = discord.Embed()
            embed.title = "Games:"
            embed.add_field(name="Fuck game (>games fuck)", value="player to send the most n-words in 8 seconds wins! (min 2 players)")
            await message.channel.send(embed = embed)

        if message.content.startswith(f"{prefix}games fuck"):
            current_game = 'ngame'
            embed = ngame.ngame(message)
            await message.channel.send(embed = embed)


client.run(TOKEN)
