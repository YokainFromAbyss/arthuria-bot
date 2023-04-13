import discord
from discord.ext import commands
import json
import json_reader
from discord.ext.commands import has_permissions, MissingPermissions
import io


def map_selection(role: discord.Role):
    return discord.SelectOption(
        label=role.name
    )


def roles_getter(roles, role_name):
    for r in roles:
        if r.name == role_name:
            return r


def embed_creator(description, roles):
    for r in roles:
        description = description + '\n<@&' + str(r['id']) + '> - ' + r['description']
    return description


class Selection(discord.ui.Select):
    def __init__(self, roles):
        self.roles = roles
        options = list(map(map_selection, roles))
        super().__init__(placeholder="Выбери роль", options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        r = roles_getter(self.roles, self.values[0])
        role = interaction.guild.get_role(r.id)
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
        else:
            await interaction.user.add_roles(role)
        await interaction.message.edit(view=self.view)


class SelectView(discord.ui.View):
    def __init__(self, roles, timeout):
        super().__init__(timeout=timeout)
        self.add_item(Selection(roles))


class GameRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.application_command(
            name="game_roles",
            description="Admin Only!",
            cls=discord.SlashCommand)(self.view_slash)

    @commands.command()
    @has_permissions(administrator=True)
    async def view(self, ctx):
        with io.open('./resources/game_roles_list.json', encoding='utf-8', mode='r') as f:
            data = json.load(f)
            roles = data['roles']
            ids = list(map(lambda r: r['id'], roles))
            role_list = [item for item in ctx.guild.roles if item.id in ids]
            embed = json_reader.game_roles_embed()
            embed.description = embed_creator(embed.description, roles)
            await ctx.send(embed=embed, view=SelectView(role_list, timeout=None))
            await ctx.respond("y", delete_after=0)

    async def view_slash(self, ctx):
        await self.view(ctx)


def setup(bot):
    bot.add_cog(GameRoles(bot))
