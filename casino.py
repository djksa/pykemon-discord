import re
import sys
import json
import requests
import random
from discord.ext import commands

class GetPokemon():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def getpokemon(self, ctx):
        """gets pokemon based on random num -- to be improved later"""

def setup(bot):
    bot.add_cog(GetPokemon(bot))  