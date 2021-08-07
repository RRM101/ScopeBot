import discord
from discord.ext import commands
import aiohttp
import random2

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball'], brief='A game of 8ball', description='a game of 8ball **yes or no**')
    async def _8ball(self, ctx, *, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Why are you so sus!?",
            "Very doubtful."]
        await ctx.send(f'Question: {question}\nAnswer: {random2.choice(responses)}')

    @commands.command(brief='troll', description='troll')
    async def troll(self, ctx):
        await ctx.send('https://tenor.com/view/trollface-lol-laugh-gif-5432260')
        print(f'{ctx.message.author} got trolled!')

    @commands.command(brief='Rickrolls someone...', description='Rickrolls someone... See their reaction!')
    async def rickroll(self, ctx):
        print(f'{ctx.message.author} got rickrolled!')
        await ctx.send('https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')

    @commands.command(hidden=True)
    async def secret(self, ctx):
        print('someone has used the secret command!')
        await ctx.send('Secret text has been put on the console of the bot which you cant see')

    @commands.command(brief='memes from r/dankmemes')
    async def meme(self, ctx):
        print('memed')
        embed = discord.Embed(title="**MEME**", description="meme from r/dankmemes")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'][random2.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    @commands.command(brief='memes from r/memes')
    async def meme2(self, ctx):
        print('memed')
        embed = discord.Embed(title="**MEME**", description="meme from r/memes")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'][random2.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    @commands.command(brief='b e a n', description='b e a n')
    async def bean(self, ctx, member: discord.Member, *, reason='No reason given'):
        message = f"You have been beaned from {ctx.guild.name} for {reason}"
        await member.send(message)
        await ctx.send(f'{member.mention} has been beaned! For: {reason}')
        print(f'{ctx.message.author} has beaned {member} for {reason}!')


def setup(bot):
    bot.add_cog(fun(bot))
    print('Fun cog loaded')