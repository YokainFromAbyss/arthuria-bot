import discord
from discord.ext import commands
from discord.commands import Option
from discord import Embed

from commands.utils.sql_storage import *


class Game(commands.Cog):
    r"""
    Команды для великолепной игры 'Пидор дня'
    """
    group = discord.SlashCommandGroup("game", "Day game group")

    def __init__(self, bot):
        self.bot = bot

    @group.command(description='Регистрация в великолепное казино!')
    async def register(self, ctx):
        if game_register(ctx.user.id):
            await ctx.interaction.response.send_message("Успех!!", ephemeral=True)
        else:
            await ctx.interaction.response.send_message("Что-то сломалось, пинай одменов((", ephemeral=True)

    @group.command(description='Выйти из казино!')
    async def unregister(self, ctx):
        if game_unregister(ctx.user.id):
            await ctx.interaction.response.send_message("До скорого!", ephemeral=True)
        else:
            await ctx.interaction.response.send_message("Что-то сломалось, пинай одменов((", ephemeral=True)

    @group.command(description='Топ везунчиков')
    async def top(self, ctx, count: Option(str, required=False, default=10)):
        top_list = game_top(count)
        embed = Embed()
        embed.title = f'Топ {count} пидоров'
        embed.colour = 15277667
        description = ''
        counter = 1
        for dis_id, cnt in top_list:
            description = description + f"**{counter}**. <@{dis_id}> - {cnt} \n"
            counter += 1
        embed.description = description
        await ctx.respond(embed=embed)

    @group.command(description='Играем?')
    async def roll(self, ctx):
        roll, winner = game_roll()
        if winner == -1:
            await ctx.respond(f"**Пока никто не играет, ты можешь быть первым!**")
        else:
            if roll:
                await ctx.respond(f"**Пидор дня <@{winner}>!**")
            else:
                await ctx.respond(f"**Сегодня уже победил <@{winner}>**")


def setup(bot):
    bot.add_cog(Game(bot))
