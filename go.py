import re
import sys
import json
import requests
import random
from discord.ext import commands

"""cog for exploring"""

class Go():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def go(self, ctx, location: str):
        """takes you to a location"""
        r = requests.get("https://pokeapi.co/api/v2/location-area/" + location + "/")
        poke_place = r.json()["encounter_method_rates"][0]
        await self.bot.send_message(ctx.message.channel, poke_place, tts=False)
        
def setup(bot):
    bot.add_cog(Go(bot))  