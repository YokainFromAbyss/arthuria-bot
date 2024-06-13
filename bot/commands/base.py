import logging

import requests
from discord.commands import Option, OptionChoice
from discord.ext import commands

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:[%(levelname)s]:[%(name)s]: %(message)s'))
LOG.addHandler(handler)


class Base(commands.Cog):
    r"""
    Просто бросает в тебя оскорбления
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="base",
        description="Когда не можешь придумать плохие слова!"
    )
    async def base(self, ctx, lang: Option(str, required=False, default='ru',
                                           choices=[OptionChoice(name='RU', value='ru'),
                                                    OptionChoice(name='ENG', value='en')])):
        LOG.info("Create evil paste by %s", ctx.user.name)
        r = requests.get('https://evilinsult.com/generate_insult.php?lang={}&type=json'.format(lang))
        resp = r.json()
        await ctx.respond(resp['insult'])


def setup(bot):
    bot.add_cog(Base(bot))
