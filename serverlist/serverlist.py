import discord
from discord.ext import commands


class ShowGuildPlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def servers(self, ctx):
        """
        Force your bot to leave a specified server
        """
        servers = list(self.bot.servers)
        
        await ctx.send(f"Connected on {str(len(servers))} servers:")
        await ctx.send('\n'.join(server.name for server in servers))


    @commands.Cog.listener()
    async def on_ready(self):
        async with self.bot.session.post(
            "https://counter.modmail-plugins.piyush.codes/api/instances/leaveserver",
            json={"id": self.bot.user.id},
        ):
            print("Posted to Plugin API")


def setup(bot):
    bot.add_cog(ShowGuildPlugin(bot))
