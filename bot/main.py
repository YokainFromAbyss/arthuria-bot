import logging
from logging.handlers import TimedRotatingFileHandler
import os

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
intents.members = True
intents.guilds = True
intents.reactions = True
bot = commands.Bot(intents=intents)


# servers = [774157527083646976]

# Insert all commands
for f in os.listdir("./commands"):
    if f.endswith(".py"):
        print(f'Add command {"commands." + f[:-3]}')
        bot.load_extension("commands." + f[:-3])

bot.run(config['token'])
