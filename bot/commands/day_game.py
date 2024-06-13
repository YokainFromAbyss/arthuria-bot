import discord
from discord.ext import commands
from discord.commands import Option
from discord import Embed
from discord.utils import get

from commands.utils.sql_storage import *
import logging

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:[%(levelname)s]:[%(name)s]: %(message)s'))
LOG.addHandler(handler)


class Game(commands.Cog):
    r"""
    Команды для великолепной игры 'Пидор дня'
    """
    group = discord.SlashCommandGroup("game", "Day game group")

    def __init__(self, bot):
        self.bot = bot

    @group.command(description='Регистрация в великолепное казино!')
    async def register(self, ctx):
        await ctx.interaction.response.defer(ephemeral=True)
        LOG.info("Register user: %s", ctx.user.name)
        if game_register(ctx.user.id):
            await ctx.interaction.followup.send("Успех!!", delete_after=15)
        else:
            await ctx.interaction.followup.send("Что-то сломалось, пинай одменов((", delete_after=15)

    @group.command(description='Выйти из казино!')
    async def unregister(self, ctx):
        await ctx.interaction.response.defer(ephemeral=True)
        LOG.info("Unregister user: %s", ctx.user.name)
        if game_unregister(ctx.user.id):
            await ctx.interaction.followup.send("До скорого!", delete_after=15)
        else:
            await ctx.interaction.followup.send("Что-то сломалось, пинай одменов((", delete_after=15)

    @group.command(description='Топ везунчиков')
    async def top(self, ctx, count: Option(str, required=False, default=10)):
        await ctx.interaction.response.defer()
        LOG.info("Getting %s winners by user: %s", count, ctx.user.name)
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
        await ctx.interaction.response.defer()
        LOG.info("Getting today winner by user: %s", ctx.user.name)
        roll, winner = game_roll()
        if winner == -1:
            await ctx.respond(f"**Пока никто не играет, ты можешь быть первым!**")
        else:
            if roll:
                with open('./resources/config.yaml') as f:
                    config = yaml.load(f, Loader=yaml.FullLoader)
                guild = ctx.guild
                role = get(guild.roles, id=config['game-role'])
                for m in role.members:
                    await m.remove_roles(role)
                winner = int(winner)
                us = guild.get_member(winner)
                await us.add_roles(role)
                await ctx.respond(f"**Пидор дня <@{winner}>!**")
            else:
                await ctx.respond(f"**Сегодня уже победил <@{winner}>**")


def setup(bot):
    bot.add_cog(Game(bot))
