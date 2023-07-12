from discord.ext import commands
import json
import json_reader
from commands.utils.selector import RoleSelection, SelectView
from discord.ext.commands import has_permissions
import io
import logging

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:[%(levelname)s]:[%(name)s]: %(message)s'))
LOG.addHandler(handler)


def embed_creator(description, roles):
    for r in roles:
        description = description + '\n<@&' + str(r['id']) + '> - ' + r['description']
    return description


class GameRoles(commands.Cog):
    r"""
    Выводит Embed для выбора игровых ролей
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="game_roles",
        description="Admin Only!"
    )
    @has_permissions(administrator=True)
    async def game_view(self, ctx):
        LOG.info("Creating game roles selector by: %s", ctx.user.name)
        with io.open('./resources/game_roles_list.json', encoding='utf-8', mode='r') as f:
            data = json.load(f)
            roles = data['roles']
            ids = list(map(lambda r: r['id'], roles))
            role_list = [item for item in ctx.guild.roles if item.id in ids]
            embed = json_reader.game_roles_embed()
            embed.description = embed_creator(embed.description, roles)
            await ctx.send(embed=embed, view=SelectView(RoleSelection(role_list), timeout=None))
            await ctx.interaction.response.send_message("y", delete_after=0, ephemeral=True)


def setup(bot):
    bot.add_cog(GameRoles(bot))
