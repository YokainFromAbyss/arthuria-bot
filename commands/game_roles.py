import discord
from discord.ext import commands
import json
import json_reader
from commands.utils.selector import RoleSelection
from discord.ext.commands import has_permissions
import io


def embed_creator(description, roles):
    for r in roles:
        description = description + '\n<@&' + str(r['id']) + '> - ' + r['description']
    return description


class SelectView(discord.ui.View):
    def __init__(self, roles, timeout):
        super().__init__(timeout=timeout)
        self.add_item(RoleSelection(roles))


class GameRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.application_command(
            name="game_roles",
            description="Admin Only!",
            cls=discord.SlashCommand)(self.game_view_slash)

    @commands.command()
    @has_permissions(administrator=True)
    async def game_view(self, ctx):
        with io.open('./resources/game_roles_list.json', encoding='utf-8', mode='r') as f:
            data = json.load(f)
            roles = data['roles']
            ids = list(map(lambda r: r['id'], roles))
            role_list = [item for item in ctx.guild.roles if item.id in ids]
            embed = json_reader.game_roles_embed()
            embed.description = embed_creator(embed.description, roles)
            await ctx.send(embed=embed, view=SelectView(role_list, timeout=None))
            await ctx.respond("y", delete_after=0)

    async def game_view_slash(self, ctx):
        await self.game_view(ctx)


def setup(bot):
    bot.add_cog(GameRoles(bot))
