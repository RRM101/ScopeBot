from discord.ext import commands

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.reply('I dont have permission to do that')
            print('A command has been executed but I dont have perms to do that')
        if isinstance(error, commands.MissingRole):
            await ctx.reply('You dont have roles/permission to do that!')
            print(
                f'{ctx.message.author} is trying to execute a command which they done have roles/permission to "{ctx.message.content}"')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(f'Put all the required arguments in the command')
            print(f'{ctx.message.author} didnt put all the required arguments')
        if isinstance(error, commands.CommandNotFound):
            print(f'{ctx.message.author} used an invalid command "{ctx.message.content}"')
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply('You dont have permission to do that!')
            print(
                f'{ctx.message.author} is trying to execute a command which they done have permission to "{ctx.message.content}"')

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

        @commands.command(aliases=['pardon', 'forgive'], brief='Unbans the user', description='Unbans the user from this server')
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

def setup(bot):
    bot.add_cog(events(bot))
    print('Events cog loaded')