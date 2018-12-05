#eventually operate so it keeps a log and when you generate a pokemon
#you can assign to a bitcoin or ethereum address by entering address
#server keeps log of that address
#$pokemon update "address" makes it so it looks at all the utxo in that address, sees if there was a transaction 
#that said "move "num" (in message field) "address" (sent to)
#where num is the pokemon number and address is where to, it transfers ownership
#eventually move



import json
import requests
from discord.ext import commands

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

TOKEN = "NTE2OTEwNTE3ODczMjc4OTc2.Dt9ySw.LhJlNITlvyE5_ykG4GBgFCP_ud8"

# this specifies what extensions to load when the bot starts up
startup_extensions = ["getpokemon"]

bot = commands.Bot(command_prefix='$', description=description)

@bot.event
async def on_ready():
    print("!!@@@@==PokeBot Launched==@@@@!!")

@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(TOKEN)