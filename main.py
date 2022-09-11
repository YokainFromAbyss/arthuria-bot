import discord
from discord.ui import InputText, Modal
from discord import utils
from discord.ext import tasks
from discord.ext.commands import Bot
from discord import colour
from discord import embeds
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord import guild
from discord import mentions

from asyncio import sleep
import yaml
import logging
import os

# Init logger
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord-debug.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Втюхиваем конфиг
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents)


# servers = [774157527083646976]


@bot.event
async def on_ready():
    print(f"Я вошла {bot.user}")
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Горнило", type=3))
        await sleep(30)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Испытания Осириса", type=3))
        await sleep(30)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=">помощь", type=3))
        await sleep(30)


# @bot.command(aliases = ['эхо'])
# @has_permissions(administrator=True)
# async def say(ctx, *, phrase,):
#      await ctx.channel.send(phrase)
#      await ctx.message.delete()


# @bot.slash_command(name="монетка", description="Подбрось монетку и узнаешь свою судьбу!")
# async def coin(ctx):
#     coin_x = random.randint(0, 100)
#     if coin_x <= 10:
#         await ctx.respond("Монетка упала на ребро, перекидывай")
#     else:
#         if (coin_x > 10 and coin_x < 46):
#             await ctx.respond("У тебя решка!")
#         else:
#             await ctx.respond("У тебя орёл!")


# Insert all commands
for f in os.listdir("./commands"):
    if f.endswith(".py"):
        print(f'Add command {"commands." + f[:-3]}')
        bot.load_extension("commands." + f[:-3])

bot.run(config['token'])
