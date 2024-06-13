from discord.ext import commands
import logging

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:[%(levelname)s]:[%(name)s]: %(message)s'))
LOG.addHandler(handler)


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
        LOG.info("Using help by: %s", ctx.user.name)
        help_text = "```\n"
        for cog in self.bot.cogs:
            c = self.bot.cogs[cog]
            if c.__doc__ is not None:
                help_text += f"{c.__doc__}\n"
            for w in c.walk_commands():
                help_text += "/"
                if w.parent is None:
                    help_text += f"{w.name}\t\t"
                else:
                    help_text += f"{w.parent} {w.name}\t\t"
                help_text += f"{w.description}\n"
            if c.__doc__ is not None:
                help_text += "\n_________________\n"
        help_text += "```"
        await ctx.interaction.response.send_message(help_text, ephemeral=True)


def setup(bot):
    bot.add_cog(Help(bot))
