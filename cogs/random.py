import random2
import discord
from discord.ext import commands

class random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.command()
    async def exec(ctx, *, cmd=None):
        try:
            await ctx.send(f'Your bot friend executed your command --> {cmd}\n\nOutput: {exec(cmd)}') # Command to get the output of some python code
        except:
            await ctx.send(f'Your bot friend could not execute an invalid command --> {cmd}')   
     
    @commands.command(brief='This is the brief description', description='This is the full description')
    async def hello(self, ctx):
        await ctx.send('hi there!')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reply(self, ctx):
        await ctx.reply('work')
        print(f'{ctx.message.author} used the reply command')


    @commands.command(aliases=['attribution'], brief='credits', description='credits')
    async def credits(self, ctx):
        em = discord.Embed(title="Credits", color=discord.Color.magenta(),
                           description="Credits for the code/images used in the bot")
        em.add_field(name="Image credits", value='The logo of the main bot is made by 0x010C '
                                                 'https://commons.wikimedia.org/wiki/User:0x010C')
        em.add_field(name="Code credits", value='the bot is coded and maintained by RickRollMaster101 '
                                                'https://github.com/RickRollMaster101/ScopeBot')
        await ctx.send(embed=em)

    @commands.command(brief='Shows you a random image', description='Shows you a random image')
    async def image(self, ctx):
        variable = [
            "https://picsum.photos/200",
            "https://picsum.photos/420",
            "https://picsum.photos/400",
            "https://picsum.photos/250",
            "https://picsum.photos/430",
            "https://picsum.photos/440",
            "https://picsum.photos/450",
            "https://picsum.photos/460",
            "https://picsum.photos/470",
            "https://picsum.photos/480",
            "https://picsum.photos/490",
            "https://picsum.photos/445",
            "https://picsum.photos/880",
            "https://picsum.photos/290",
            "https://picsum.photos/345",
            "https://picsum.photos/423",
            "https://picsum.photos/456",
            "https://picsum.photos/654",
            "https://picsum.photos/670",
            "https://picsum.photos/970",
            "https://picsum.photos/230",
            "https://picsum.photos/627",
            "https://picsum.photos/623",
            "https://picsum.photos/622",
            "https://picsum.photos/621",
            "https://picsum.photos/983",
            "https://source.unsplash.com/random/800x600",
            "https://source.unsplash.com/random/810x610",
            "https://source.unsplash.com/random/1920x1080",
            "https://source.unsplash.com/random/200x400",
            "https://source.unsplash.com/random/400x600",
            "https://source.unsplash.com/random/500x500",
            "https://source.unsplash.com/random/800x700",
            "https://source.unsplash.com/random/100x500",
            "https://source.unsplash.com/random/400x500",
            "https://source.unsplash.com/random/700x500",
            "https://source.unsplash.com/random/200x300",
            "https://source.unsplash.com/random/150x150",
            "https://source.unsplash.com/random/540x40",
            "https://source.unsplash.com/random/900x500",
            "https://source.unsplash.com/random/123x123", ]
        print(f'{ctx.message.author} wants to see a random image')
        await ctx.send(f'{random2.choice(variable)}')

    @commands.command(brief='Shows the ping of the bot', description='Shows the ping of the bot')
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')
        print(f'{ctx.message.author} wants to know the ping of the bot!')

    @commands.command(brief='shows you a video', description='shows you a random video (more soon!)')
    async def video(self, ctx):
        videos = ['https://cdn.discordapp.com/attachments/770206343306280970/849267760377888788/video1.mp4',
                  'https://cdn.discordapp.com/attachments/834713618028691466/856442337789476874/video2.mp4']
        await ctx.send(random2.choice(videos))
        print(f'{ctx.message.author} wants to watch a video!')


def setup(bot):
    bot.add_cog(random(bot))
    print('Random cog loaded')
