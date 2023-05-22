import discord
from discord.ext import commands, tasks
import random

from commands.utils.bunge_api import load_news


class Background(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        # Играет в
        self.game_roulette = [
            "Горнило",
            "Испытания Осириса",
            "очко с крысой",
            "могилу",
            "Гамбит",
            "своей попке",
            "DnD",
        ]
        self.status.start()

        self.del_message = "[Original Message Deleted]"
        self.channels = [1053280305852719125, 1069550535331553340]  # чекпоинты, сборы p2p
        self.del_message_cleaner.start()

        self.content_channel = 1050041513712824330  # контент
        self.news_lookup.start()

    @tasks.loop(seconds=60)
    async def status(self):
        ind = random.randint(1, len(self.game_roulette))
        await self.bot.change_presence(status=discord.Status.online,
                                       activity=discord.Game(name=self.game_roulette[ind - 1], type=3))

    @tasks.loop(hours=6)
    async def del_message_cleaner(self):
        for c in self.channels:
            channel = self.bot.get_channel(c)
            messages = await channel.history(limit=None).flatten()
            for m in messages:
                if m.content == self.del_message:
                    await m.delete()

    @tasks.loop(minutes=10)
    async def news_lookup(self):
        channel = self.bot.get_channel(self.content_channel)
        links = load_news()
        for link in links:
            await channel.send("Новая статья на bungie.net\n" + link)

    @status.before_loop
    @del_message_cleaner.before_loop
    @news_lookup.before_loop
    async def before_background(self):
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(Background(bot))
