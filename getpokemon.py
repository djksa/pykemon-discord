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
        r = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(random.randint(1,800)) + "/")
        poke_name = r.json()["name"]
        poke_img = "http://play.pokemonshowdown.com/sprites/xyani/" + poke_name + ".gif"
        await self.bot.say(":moneybag:`-10`:moneybag:\n")
        await self.bot.send_message(ctx.message.channel, poke_name, tts=True)
        await self.bot.say(poke_img)
        
def setup(bot):
    bot.add_cog(GetPokemon(bot))  