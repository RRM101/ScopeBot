import discord
import json
from discord.ext import commands
with open("./config.json") as f:
    configData = json.load(f)

token = configData["Token"]
prefix = configData["Prefix"]

# changes the no category name to Commands
help_command = commands.DefaultHelpCommand(no_category = 'Help')

client = commands.Bot(command_prefix=prefix, help_command = help_command)

@client.event
async def on_ready():
    print('ScopeBot is ready')
    game = discord.Game("Looking at the stars...")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.command(hidden=True)
async def hellp(ctx):
    await ctx.reply(f'You made a typo <a:lmao:857570800395354123>,  do {prefix}hello or {prefix}help')
    print(f'{ctx.message.author} made a typo lol')


# put your bot token in config.json
client.load_extension('cogs.events')
client.load_extension('cogs.moderation')
client.load_extension('cogs.fun')
client.load_extension('cogs.random')
client.run(token)
