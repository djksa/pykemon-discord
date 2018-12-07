import re
import sys
import json
import requests
import random
from discord.ext import commands

"""cog for exploring"""
# /TODO extend ctx of getpokemon cog to find specific pokemon then add here instead
# of random encounter being long
#so far it only generates a number but i have to get the actual name otherwise the location will NOT matter
class Go():
    def __init__(self, bot):
        self.bot = bot

    def random_encounter(self, poke_encounters):
        #returns int
        poke_index = random.randint(0, len(poke_encounters))
        return poke_index
    
    def grab_pokemon(self, random_encounter, location):
        #returns str
        r = requests.get("https://pokeapi.co/api/v2/location-area/" + location + "/")
        poke_name = r.json()["pokemon_encounters"][random_encounter]["pokemon"]["name"]
        return poke_name


    @commands.command(pass_context=True)
    async def go(self, ctx, location: str):
        """takes you to a location"""
        r = requests.get("https://pokeapi.co/api/v2/location-area/" + location + "/")
        poke_encounters = r.json()["pokemon_encounters"]
        poke_name = self.grab_pokemon(self.random_encounter(poke_encounters), location)
        poke_img = "http://play.pokemonshowdown.com/sprites/xyani/" + poke_name + ".gif"
        await self.bot.send_message(ctx.message.channel, poke_name, tts=True)
        await self.bot.say(poke_img)
        
def setup(bot):
    bot.add_cog(Go(bot))  