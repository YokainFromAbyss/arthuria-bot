from discord.ext import commands


class Help(commands.Cog):
    r"""
    Выводит список всех команд с описанием и документацией
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="help",
        description="Справочник команд."
    )
    async def help(self, ctx):
        help_text = "```\n"
        for cog in self.bot.cogs:
            c = self.bot.cogs[cog]
            for w in c.walk_commands():
                help_text += "/"
                if w.parent is None:
                    help_text += f"{w.name}\t\t"
                else:
                    help_text += f"{w.parent} {w.name}\t\t"
                help_text += f"{w.description}\n"
            if c.__doc__ is not None:
                help_text += f"{c.__doc__}\n\n"
        help_text += "```"
        await ctx.interaction.response.send_message(help_text, ephemeral=True)


def setup(bot):
    bot.add_cog(Help(bot))