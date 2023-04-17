import json

import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.commands import Option
import re


class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.application_command(
            name="say",
            description="Text or Embed. Use \n to new line",
            cls=discord.SlashCommand)(self.say_slash)

    @commands.command()
    @has_permissions(administrator=True)
    async def say(self, ctx, message: Option(str, required=True)):
        if message.startswith('{'):
            embed_str = re.search('\{(.*)\}', message).group(0)
            embed_json = json.loads(embed_str)
            embed = Embed.from_dict(embed_json)
            await ctx.send(embed=embed)
        else:
            message = message.replace('\\n', '\n')
            await ctx.send(message)

        await ctx.respond("<:Hahaeblan:1085526972458860645>", delete_after=0)

    async def say_slash(self, ctx, message: str):
        await self.say(ctx, message)


def setup(bot):
    bot.add_cog(Say(bot))
