from discord.ext import commands

from commands.utils.sql_storage import game_unregister


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Я вошла {self.bot.user}")

    # @commands.Cog.listener()
    # async def on_member_join(self, member):
    #     print(f"User join {member.id}")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        game_unregister(member.id)


def setup(bot):
    bot.add_cog(Events(bot))
