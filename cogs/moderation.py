import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['rek'], brief='Bans the user', description='Bans the user from this server')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason='No reason given'):
        message = f"You have been banned from {ctx.guild.name} for {reason}"
        await member.send(message)
        await ctx.guild.ban(member, reason=reason)
        await ctx.channel.send(f"{member.mention} is banned! by {ctx.author.name} for {reason}")
        print(f'{ctx.message.author} has banned {member} for {reason}')
        return

    @commands.command(aliases=['pardon', 'forgive'], brief='Unbans the user',
                      description='Unbans the user from this server')
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                print(f'{ctx.message.author} has unbanned {user.name}#{user.discriminator}!')
                return

    @commands.command(aliases=['yeet'], brief='Kicks the user', description='Kicks the user from this server')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason='No reason given'):
        message = f"You have been kicked from {ctx.guild.name} for {reason}"
        await member.send(message)
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} has been kicked for {reason}!')
        print(f'{ctx.message.author} has kicked {member} for {reason}!')

    @commands.command(aliases=['clear'], brief='Deletes messages', description='Deletes messages in bulk')
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        print(f'{ctx.message.author} is deleting messages')


def setup(bot):
    bot.add_cog(Moderation(bot))
    print('Moderation cog loaded')
