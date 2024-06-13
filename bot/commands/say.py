import json

from discord import Embed
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.commands import Option
import re
import logging

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:[%(levelname)s]:[%(name)s]: %(message)s'))
LOG.addHandler(handler)


class Say(commands.Cog):
    r"""
    Выводит текст что передан в параметр message
    Если текст начинается с '{', то превращает его в Embed
    Все переводы строк должны быть указаны через \n
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="say",
        description="Text or Embed. Use \\n to new line",
    )
    @has_permissions(administrator=True)
    async def say(self, ctx, message: Option(str, required=True)):
        LOG.info("Say command by: %s", ctx.user.name)
        LOG.debug("Say message: %s", message)
        if message.startswith('{'):
            embed_str = re.search('\{(.*)\}', message).group(0)
            embed_json = json.loads(embed_str)
            embed = Embed.from_dict(embed_json)
            await ctx.send(embed=embed)
        else:
            message = message.replace('\\n', '\n')
            await ctx.send(message)
        await ctx.interaction.response.send_message("<:Hahaeblan:1085526972458860645>", delete_after=0, ephemeral=True)


def setup(bot):
    bot.add_cog(Say(bot))
