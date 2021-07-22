import random
import discord
import json
from aiohttp import ClientSession
from pretty_help import PrettyHelp
from discord.ext import commands
with open("./config.json") as f:
    configData = json.load(f)

token = configData["Token"]
prefix = configData["Prefix"]

client = commands.Bot(command_prefix=prefix,
                      help_command=PrettyHelp(no_category='Commands'))  # , help_command = help_command


@client.event
async def on_ready():
    print('ScopeBot is ready')
    game = discord.Game("Looking at the stars...")
    await client.change_presence(status=discord.Status.online, activity=game)


# the thing after async def is the command that you put on discord | this a test command
@client.command(brief='This is the brief description', description='This is the full description')
async def hello(ctx):
    await ctx.send('hi there!')

# this command exists for testing
@client.command()
@commands.has_permissions(administrator=True)
async def reply(ctx):
    await ctx.reply('work')
    print(f'{ctx.message.author} used the reply command')

# typo go brr
@client.command(hidden=True)
async def hellp(ctx):
    await ctx.reply(f'You made a typo <a:lmao:857570800395354123>,  do {prefix}hello or {prefix}help')
    print(f'{ctx.message.author} made a typo lol')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.reply('You dont have roles/permission to do that!')
        print(f'{ctx.message.author} is trying to execute a command which they done have roles/permission to "{ctx.message.content}"')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(f'Put all the required arguments in the command')
        print(f'{ctx.message.author} didnt put all the required arguments')
    if isinstance(error, commands.CommandNotFound):
        print(f'{ctx.message.author} used an invalid command "{ctx.message.content}"')
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply('You dont have permission to do that!')
        print(
            f'{ctx.message.author} is trying to execute a command which they done have permission to "{ctx.message.content}"')


# b e a n
@client.command(brief='b e a n', description='b e a n')
async def bean(ctx, member: discord.Member, *, reason):
    await ctx.send(f'{member.mention} has been beaned! For: {reason}')
    print(f'{ctx.message.author} has beaned {member} for {reason}!')


@client.command(aliases=['attribution'], brief='credits', description='credits')
async def credits(ctx):
    em = discord.Embed(title="Credits", color=discord.Color.magenta(),
                       description="Credits for the code/images used in the bot")
    em.add_field(name="Image credits", value='The logo of the main bot is made by 0x010C '
                                             'https://commons.wikimedia.org/wiki/User:0x010C')
    em.add_field(name="Code credits", value='the bot is coded and maintained by RickRollMaster101 '
                                            'https://github.com/RickRollMaster101/ScopeBot')
    await ctx.send(embed=em)


# secret
@client.command(hidden=True)
async def secret(ctx):
    print('someone has used the secret command!')
    await ctx.send('Secret text has been put on the console of the bot which you cant see')

# random
# idk if it works so creating pr and test it 
@client.command()
async def random(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://source.unsplash.com/random/200x200?sig=incrementingIdentifier')
      randomjson = await request.json()
   embed = discord.Embed(title="Randoms!", color=discord.Color.purple()) # Create embed
   embed.set_image(url=randomjson['link']) # Set the embed image to the value of the 'link' key
   await ctx.send(embed=embed) # Send the embed


# someone gets rickrolled
@client.command(brief='Rickrolls someone...', description='Rickrolls someone... See their reaction!')
async def rickroll(ctx):
    print(f'{ctx.message.author} got rickrolled!')
    await ctx.send('https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')


# ping of the bot
@client.command(brief='Shows the ping of the bot', description='Shows the ping of the bot')
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
    print(f'{ctx.message.author} wants to know the ping of the bot!')


@client.command(aliases=['8ball'], brief='A game of 8ball', description='a game of 8ball **yes or no**')
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
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
                 "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
    print(f'{ctx.message.author} used the 8ball command!')


# imagine deleting messages
@client.command(aliases=['clear'], brief='Deletes messages', description='Deletes messages in bulk')
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    print(f'{ctx.message.author} is deleting messages')


@client.command(aliases=['yeet'], brief='Kicks the user', description='Kicks the user from this server')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    message = f"You have been kicked from {ctx.guild.name} for {reason}"
    await member.send(message)
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked for {reason}!')
    print(f'{ctx.message.author} has kicked {member} for {reason}!')


# added some checks for ban command need to test this :)),if it works will implement for kick
@client.command(aliases=['rek'], brief='Bans the user', description='Bans the user from this server')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member.mention} is banned! by {ctx.author.name} for {reason}")
    print(f'{ctx.message.author} has banned {member} for {reason}')
    return


@client.command(aliases=['pardon', 'forgive'], brief='Unbans the user', description='Unbans the user from this server')
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            print(f'{ctx.message.author} has unbanned {user.name}#{user.discriminator}!')
            return


@client.command(brief='troll', description='troll')
async def troll(ctx):
    await ctx.send('https://tenor.com/view/trollface-lol-laugh-gif-5432260')
    print(f'{ctx.message.author} got trolled!')

@client.command(brief='shows you a video', description='shows you a random video (more soon!)')
async def video(ctx):
    videos = ['https://cdn.discordapp.com/attachments/770206343306280970/849267760377888788/video1.mp4',
              'https://cdn.discordapp.com/attachments/834713618028691466/856442337789476874/video2.mp4']
    await ctx.send(random.choice(videos))
    print(f'{ctx.message.author} wants to watch a video!')

# put your bot token in config.json
client.run(token)
