import discord
from discord.ext import commands
import random


class Coin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.application_command(
            name="монетка",
            description="Подбрось монетку и узнаешь свою судьбу!",
            cls=discord.SlashCommand)(self.coin_slash)

    @commands.command()
    async def coin(self, ctx):
        coin_x = random.randint(0, 100)
        if coin_x <= 10:
            await ctx.respond("Монетка упала на ребро, перекидывай")
        else:
            if 10 < coin_x < 46:
                await ctx.respond("У тебя решка!")
            else:
                await ctx.respond("У тебя орёл!")

    async def coin_slash(self, ctx):
        await self.coin(ctx)


def setup(bot):
    bot.add_cog(Coin(bot))
