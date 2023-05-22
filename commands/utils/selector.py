import discord


def map_selection(role: discord.Role):
    return discord.SelectOption(
        label=role.name
    )


def roles_getter(roles, role_name):
    for r in roles:
        if r.name == role_name:
            return r


class RoleSelection(discord.ui.Select):
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
    def __init__(self, selector, timeout):
        super().__init__(timeout=timeout)
        self.add_item(selector)
