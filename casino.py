import re
import sys
import json
import requests
import random
from discord.ext import commands

class Casino():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def casino(self, ctx):
        """pykemon casino"""

def setup(bot):
    bot.add_cog(Casino(bot))  