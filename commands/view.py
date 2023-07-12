from discord.ext import commands
import json
import json_reader
from discord.ext.commands import has_permissions
import io

from commands.utils.selector import RoleSelection, SelectView
import logging

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:[%(levelname)s]:[%(name)s]: %(message)s'))
LOG.addHandler(handler)


def embed_creator(description, roles):
    for r in roles:
        description = description + '\n<@&' + str(r) + '>'
    return description


class View(commands.Cog):
    r"""
    Выводит Embed для выбора PePe ролей на сервере
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="view",
        description="Admin Only!"
    )
    @has_permissions(administrator=True)
    async def view(self, ctx):
        LOG.info("Creating PePe roles selector by: %s", ctx.user.name)
        with io.open('./resources/pepe_roles_list.json', encoding='utf-8', mode='r') as f:
            ids = json.load(f)['roles']
            role_list = [item for item in ctx.guild.roles if item.id in ids]
            embed = json_reader.roles_embed()
            embed.description = embed_creator(embed.description, ids)
            await ctx.send(embed=embed, view=SelectView(RoleSelection(role_list), timeout=None))
            await ctx.interaction.response.send_message("y", delete_after=0, ephemeral=True)


def setup(bot):
    bot.add_cog(View(bot))
