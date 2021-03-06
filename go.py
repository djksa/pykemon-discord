import math
import re
import sys
import json
import requests
import random
from discord.ext import commands

"""cog for exploring"""
# /TODO extend ctx of getpokemon cog to find specific pokemon then add here instead
# of random encounter being long
# so far it only generates a number but i have to get the actual name otherwise the location will NOT matter
class Go():
    def __init__(self, bot):
        self.bot = bot
        self.setup_locations()
        #sets self.locations_array
        
    def setup_locations(self):
        #returns array of locations
        r = requests.get("https://pokeapi.co/api/v2/location-area/")
        locations_list = r.json()["results"]
        locations_array = []
        for i in range(len(locations_list)): 
            locations_array.append(locations_list[i]["name"])
        self.locations_array = locations_array
    
    def locations_array_formatted(self, locations_array):
        #returns str
        locations_array_str = ""
        for location in locations_array:
            locations_array_str += location + " | "
        return locations_array_str
    

    @commands.command(pass_context=True)
    async def locations(self):
        locations_array = self.locations_array
        locations_array.pop()
        #removes last item in array: an empty str
        locations_array_tenth = int(len(locations_array) / 10) #NEED TO FIX LOCATION NAMES BEING CUT ON LAST FEW CHARS OF MESSAGE
        current_index = 0
        for i in range(10):
            if i != 9:
                await self.bot.say("```\nLOCATIONS PAGE : " + str(i + 1) + "\n" + \
                self.locations_array_formatted(locations_array[current_index : current_index + locations_array_tenth]) + "\n```")
                current_index += locations_array_tenth
            else:
                await self.bot.say("```\nLOCATIONS PAGE : " + str(i + 1) + "\n" + \
                self.locations_array_formatted(locations_array[current_index :]) + "\n```")

    def random_encounter(self, poke_encounters):
        #returns int
        poke_index = random.randint(0, len(poke_encounters))
        return poke_index
    
    def grab_pokemon(self, random_encounter, location):
        #returns str
        r = requests.get("https://pokeapi.co/api/v2/location-area/" + location + "/")
        poke_name = r.json()["pokemon_encounters"][random_encounter]["pokemon"]["name"]
        return poke_name

    def pokemon_value(self, chance):
        #returns str
        value = math.pow(2,(-1 * chance)) * 1000000000
        return str(int(value))


    @commands.command(pass_context=True)
    async def go(self, ctx, location: str): # add exception catches for potential wrong inputs
        """takes you to a location"""
        locations_array = self.locations_array
        if location not in locations_array:
             await self.bot.say("```\nNot a real location. Send $locations to get a comprehensive list of locations.\n```")

        else:
            r = requests.get("https://pokeapi.co/api/v2/location-area/" + location + "/")
            poke_encounters = r.json()["pokemon_encounters"]
            random_encounter = self.random_encounter(poke_encounters)
            poke_chance = poke_encounters[random_encounter]["version_details"][0]["encounter_details"][0]["chance"]
            poke_name = self.grab_pokemon(random_encounter, location)
            poke_value = self.pokemon_value(poke_chance)
            poke_img = "http://play.pokemonshowdown.com/sprites/xyani/" + poke_name + ".gif"
            await self.bot.say("` value: $" + poke_value + "`\n" + poke_img)
            await self.bot.send_message(ctx.message.channel, poke_name, tts=True)


def setup(bot):
    bot.add_cog(Go(bot))  





