import discord

class VoteView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        voteButton1 = discord.ui.Button(label='Vote on top.gg', style=discord.ButtonStyle.link, url='https://top.gg/bot/1004783529864998932/vote')
        voteButton2 = discord.ui.Button(label='Vote on discordbotlist.com', style=discord.ButtonStyle.link, url='https://discordbotlist.com/bots/perebot/upvote')
        self.add_item(voteButton1)
        self.add_item(voteButton2)