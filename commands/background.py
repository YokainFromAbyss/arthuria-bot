import discord
from discord.ext import commands, tasks
import random


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
        ]
        self.del_message = "[Original Message Deleted]"
        self.cp_channel = 1053280305852719125
        self.status.start()
        self.checkpoint_cleaner.start()

    @tasks.loop(seconds=60)
    async def status(self):
        ind = random.randint(1, len(self.game_roulette))
        await self.bot.change_presence(status=discord.Status.online,
                                       activity=discord.Game(name=self.game_roulette[ind - 1], type=3))

    @tasks.loop(hours=6)
    async def checkpoint_cleaner(self):
        channel = self.bot.get_channel(self.cp_channel)
        messages = await channel.history(limit=None).flatten()
        for m in messages:
            if m.content == self.del_message:
                await m.delete()

    @status.before_loop
    @checkpoint_cleaner.before_loop
    async def before_background(self):
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(Background(bot))
