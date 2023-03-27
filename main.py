import os
import ngame
import datetime
import accs
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
            await truth(ctx, name = interaction.user.name)
    return Truth()
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.slash_command(name="games-fuck", description='play the fuck game')
async def fuckgame(ctx):
    global current_game
    if ngame.last_played + datetime.timedelta(seconds=30) < datetime.datetime.now():
        current_game = 'ngame'
    embed = ngame.ngame(ctx)
    await ctx.respond(embed = embed)
@client.slash_command(name="games-math", description='play the math game')
async def mathgame(ctx):
    global current_game
    current_game = 'math'
    embed = ngame.mathgame(ctx)
    await ctx.respond(embed = embed)
    
@client.slash_command(name="save", description='sshhh')
async def ball9(ctx):
    file = accs.save()
    await ctx.respond(file = file, ephemeral = True)
    
@client.slash_command(name="gamble", description='bad idea')
async def ball9(ctx, amount: discord.Option(int)):
    acc = accs.get_acc(ctx.author.name)
    if amount > acc.vars['gold']:
        await ctx.respond("Not enough gold,your broke lol",ephemeral = True)
        return
    if amount < 1:
        await ctx.respond("You have to gamble > 1 gold",ephemeral = True)
        return
    if random.randint(0,1):
        acc.vars['gold'] += amount
        await ctx.respond(embed = discord.Embed(title=f"You won {amount} gold! You have {acc.vars['gold']} gold now"))
        return
    else:
        acc.vars['gold'] -= amount
        await ctx.respond(embed = discord.Embed(title=f"You lost {amount} gold :( You have {acc.vars['gold']} gold now"))
        return
    
@client.slash_command(name="9ball", description='now with an extra ball!')
async def ball9(ctx, thing: discord.Option(str)):
    embed = cmds.ball9(ctx, thing)
    await ctx.respond(embed = embed)

@client.slash_command(name="truth", description='knowledge is pain, knowledge is power')
async def truth(ctx, name=""):
    embed = discord.Embed()
    if name == "": name = ctx.author.name
    embed, gold = cmds.tod(ctx, name)
    if gold > 0:
        accs.get_acc(name).vars["gold"]+=gold
    embed.set_footer(text=f'they have {accs.get_acc(name).vars["gold"]} gold now') 
    try: await ctx.respond(embed = embed, view = truthView(ctx))
    except: await ctx.channel.send(embed = embed, view = truthView(ctx))

@client.event
async def on_message(message):
    global current_game
    if message.author.bot:
        return
    if current_game == 'math' and message.content.isdigit():
        try: answ = int(message.content)
        except: answ = 0
        if ngame.time_at_start + datetime.timedelta(seconds=10) < datetime.datetime.now():
            embed = discord.Embed()
            embed.title = "Outta time!"
            if answ == ngame.answ: embed.description = "Sad, the answer was right :( "
            else: embed.description = ""
            embed.description += f'Nobody wins!'
            await message.channel.send(embed = embed)
            current_game = ''
            return
        if answ == ngame.answ:
            embed = discord.Embed()
            embed.title = f"{message.author.name} got it correct!"
            gold = round(answ/16)+random.randint(1,3)
            accs.get_acc(message.author.name).vars["gold"] += gold
            embed.description = f'+{gold} gold, {message.author.name} now has {accs.get_acc(message.author.name).vars["gold"]} gold'
            await message.channel.send(embed = embed)
            return

        
    elif current_game == 'ngame':
        if ngame.last_played + datetime.timedelta(seconds=12) < datetime.datetime.now():
            embed = discord.Embed()
            embed.title = "The game is over!"
            high = 0
            highp = 'Nobody'
            for p in current_game_scores:
                if current_game_scores[p] > high:
                    high = current_game_scores[p]
                    highp = p
            reward = round((high+5)*random.uniform(0.65,1.13))
            embed.description = f'**{highp}** wins with {high} points! +{reward} gold!'
            accs.get_acc(highp).vars["gold"] += reward
            for player in current_game_scores:
                current_game_scores[player] = 0
            current_game = ''
            await message.channel.send(embed = embed)
            return
        cont = message.content.lower()
        if 'fuck' in cont:
            try: current_game_scores[message.author.name] += 1
            except: pass

    if message.content.startswith(f"{prefix}tod") or message.content.startswith(f"{prefix}truth"):
        embed, gold = cmds.tod(message)
        if gold > 0:
            accs.get_acc(message.author.name).vars["gold"]+=gold
        embed.set_footer(text=f'they have {accs.get_acc(message.author.name).vars["gold"]} gold now') 
        await message.channel.send(embed = embed, view = truthView(message))

    if message.content.startswith(f"{prefix}9ball") or message.content.startswith(f"{prefix}8ball"):
        try:
            embed = cmds.ball9(message, message.content.split(' ')[1])
        except:
            await message.channel.send("You must specify a subject (`>9ball <subject>`)")
            return
        await message.channel.send(embed = embed)

    if message.content.startswith(f"{prefix}gamble"):
        try:
            amount = int(message.content.split(' ')[1])
        except:
            await message.channel.send("Use numbers pls")
            return
        acc = accs.get_acc(message.author.name)
        if amount > acc.vars['gold']:
            await message.channel.send("Not enough gold,your broke lol")
            return
        if amount < 1:
            await message.channel.send("You have to gamble > 1 gold")
            return
        if random.randint(0,1):
            acc.vars['gold'] += amount
            await message.channel.send(embed = discord.Embed(title=f"You won {amount} gold! You have {acc.vars['gold']} gold now"))
            return
        else:
            acc.vars['gold'] -= amount
            await message.channel.send(embed = discord.Embed(title=f"You lost {amount} gold :( You have {acc.vars['gold']} gold now"))
            return
        

    elif message.content.startswith(f"{prefix}games"):
        if message.content == f"{prefix}games":
            embed = discord.Embed()
            embed.title = "Games:"
            embed.add_field(name="FUCK game (>games fuck)", value="player to send the most FUCKs in 12 seconds wins! (min 2 players)")
            embed.add_field(name="MATH game (>games math)", value="do some kwik maths and get the brain going")
            await message.channel.send(embed = embed)

        if message.content.startswith(f"{prefix}games fuck"):
            current_game = 'ngame'
            embed = ngame.ngame(message)
            await message.channel.send(embed = embed)

        if message.content.startswith(f"{prefix}games math"):
            current_game = 'math'
            embed = ngame.mathgame(message)
            await message.channel.send(embed = embed)


client.run(TOKEN)
