import re
import sys
import json
import requests
import random
from discord.ext import commands

class Casino():
    def __init__(self, bot):
        self.bot = bot

    # @commands.command(pass_context=True)
    # async def casino(self, ctx):
    #     """pykemon casino"""

    @bot.event
    async def on_message(message):
        if message.content.startswith('$casino'):
            await bot.send_message(message.channel, 'Enter $bet followed by an amount')

            def check(msg):
                return msg.content.startswith('$bet')

            message = await bot.wait_for_message(author=message.author, check=check)
            amount_bet = message.content[len('$bet'):].strip()
            await bot.send_message(message.channel, '{} is to be betted'.format(amount_bet))

def setup(bot):
    bot.add_cog(Casino(bot))  