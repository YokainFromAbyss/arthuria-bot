import discord
from discord.ext import commands


def map_selection(role: discord.Role):
    return discord.SelectOption(
        label=role.name,
        description=f"Нажми если хочешь получить или снять роль {role.name}"
    )


def roles_getter(roles, role_name):
    for r in roles:
        if r.name == role_name:
            return r


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


class View(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.application_command(
            name="view",
            cls=discord.SlashCommand)(self.view_slash)

    @commands.command()
    async def view(self, ctx):
        ids = [
            1016350122667413515,
            1015743894069186642,
            1014272456036462632,
        ]
        role_list = [item for item in ctx.guild.roles if item.id in ids]
        await ctx.send("Выбери роль!", view=SelectView(role_list, timeout=None))
        await ctx.respond("ы", delete_after=0)

    async def view_slash(self, ctx):
        await self.view(ctx)


def setup(bot):
    bot.add_cog(View(bot))
