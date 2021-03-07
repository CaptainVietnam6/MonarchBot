'''
import discord
from discord.ext import commands
import time

class Cogs(commands.Cog):

    def __init(self, client):
        self.client = client

    #hours uptime count
    @commands.command(aliases = ["uptimecount", "countuptime"])
    async def _uptimecount(self, ctx):
        hours_online = 0
        while hours_online != 8760:
            print(f"Uptime count loop update, MonarchBot has been online for {hours_online}")
            time.sleep(3600)
            await ctx.send(f"MonarchBot has been online on webserver for {hours_online} hours")
            hours_online = hours_online + 1

def setup(client):
    client.add_cog(Cogs(client))
'''
#command on pause due to it freezing the entire bot when ran, put in cogs category 
