from unicodedata import name
import discord
from discord.ui import InputText, Modal
import yaml
import asyncio
from asyncio import sleep
from discord import utils
from discord.ext import tasks
from discord.ext.commands import Bot
from discord import colour
from discord import embeds
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import random
from discord import guild
from discord import mentions
import json

# Втюхиваем конфиг
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    print(config)

bot = discord.Bot(intents=discord.Intents.all())

# servers = [774157527083646976]

@bot.event
async def on_ready():
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Горнило", type=3))
        await sleep (30)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Испытания Осириса", type=3))
        await sleep (30)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=">помощь", type=3))
        await sleep (30)
print(f"Я вошла под {bot.user}")

# @bot.command(aliases = ['эхо'])
# @has_permissions(administrator=True)
# async def say(ctx, *, phrase,):
#      await ctx.channel.send(phrase)
#      await ctx.message.delete()

@bot.slash_command(name="монетка", description="Подбрось монетку и узнаешь свою судьбу!")
async def coin(ctx):
    coin_x = random.randint(0, 100)
    if coin_x <= 10:
        await ctx.send_reply("Монетка упала на ребро, перекидывай")
    else:
        if (coin_x > 10 and coin_x < 46):
            await ctx.send_reply("У тебя решка!")
        else:
            await ctx.send_reply("У тебя орёл!")


bot.run(config['token'])
