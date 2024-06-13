from discord.ext import commands
import random
import logging

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:[%(levelname)s]:[%(name)s]: %(message)s'))
LOG.addHandler(handler)


class Coin(commands.Cog):
    r"""
    Просто бросает монетку
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="монетка",
        description="Подбрось монетку и узнаешь свою судьбу!"
    )
    async def coin(self, ctx):
        LOG.info("Throw coin by %s", ctx.user.name)
        coin_x = random.randint(0, 100)
        if coin_x <= 10:
            await ctx.respond("Монетка упала на ребро, перекидывай")
        else:
            if 10 < coin_x < 46:
                await ctx.respond("У тебя решка!")
            else:
                await ctx.respond("У тебя орёл!")


def setup(bot):
    bot.add_cog(Coin(bot))
