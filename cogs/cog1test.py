import discord
from discord.ext import commands

class CogsTest(commands.Cog):

    def __init(self, client):
        self.client = client

    @commands.command()
    async def cogs_test(self, ctx):
        await ctx.send("it works yay")

def setup(client):
    client.add_cog(CogsTest(client))