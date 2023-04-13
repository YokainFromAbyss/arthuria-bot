import logging
from logging.handlers import TimedRotatingFileHandler
import os
import random
from asyncio import sleep

import discord
import yaml
from discord.ext import commands

# Init logger
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = TimedRotatingFileHandler(
    filename='discord-debug.log', when='D', interval=1,
    backupCount=30, encoding='utf-8', delay=False
)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Втюхиваем конфиг
with open('./resources/config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents)


# servers = [774157527083646976]


@bot.event
async def on_ready():
    print(f"Я вошла {bot.user}")
    # Играет в
    game_roulette = [
        "Горнило",
        "Испытания Осириса",
        "очко с крысой",
        "могилу",
        "Гамбит",
        "своей попке",
    ]
    while True:
        ind = random.randint(1, len(game_roulette))
        await bot.change_presence(status=discord.Status.online,
                                  activity=discord.Game(name=game_roulette[ind - 1], type=3))
        await sleep(60)


# Insert all commands
for f in os.listdir("./commands"):
    if f.endswith(".py"):
        print(f'Add command {"commands." + f[:-3]}')
        bot.load_extension("commands." + f[:-3])

bot.run(config['token'])
