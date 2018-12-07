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




    def random_encounter(self, poke_encounters):
        poke_index = random.randint(0, len(poke_encounters))
        r = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(poke_index) + "/")
        poke_name = r.json()["name"]
        return poke_name

    @commands.command(pass_context=True)
    async def go(self, ctx, location: str):
        """takes you to a location"""
        r = requests.get("https://pokeapi.co/api/v2/location-area/" + location + "/")
        poke_encounters = r.json()["pokemon_encounters"]
        pokemon_caught = self.random_encounter(poke_encounters)
        poke_img = "http://play.pokemonshowdown.com/sprites/xyani/" + pokemon_caught + ".gif"
        await self.bot.send_message(ctx.message.channel, pokemon_caught, tts=False)
        await self.bot.say(poke_img)
        
def setup(bot):
    bot.add_cog(Go(bot))  