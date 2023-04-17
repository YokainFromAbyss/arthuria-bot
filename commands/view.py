import discord
from discord.ext import commands
import json
import json_reader
from discord.ext.commands import has_permissions
import io

from commands.utils.selector import RoleSelection


def embed_regen(description, roles):
    for r in roles:
        description = description + '\n<@&' + str(r) + '>'
    return description


class SelectView(discord.ui.View):
    def __init__(self, roles, timeout):
        super().__init__(timeout=timeout)
        self.add_item(RoleSelection(roles))


class View(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.application_command(
            name="view",
            description="Admin Only!",
            cls=discord.SlashCommand)(self.view_slash)

    @commands.command()
    @has_permissions(administrator=True)
    async def view(self, ctx):
        with io.open('./resources/pepe_roles_list.json', encoding='utf-8', mode='r') as f:
            ids = json.load(f)['roles']
            role_list = [item for item in ctx.guild.roles if item.id in ids]
            embed = json_reader.roles_embed()
            embed.description = embed_regen(embed.description, ids)
            await ctx.send(embed=embed, view=SelectView(role_list, timeout=None))
            await ctx.respond("y", delete_after=0)

    async def view_slash(self, ctx):
        await self.view(ctx)


def setup(bot):
    bot.add_cog(View(bot))
