import discord
import asyncio
from asyncio import sleep
from discord import utils
from discord.ext import tasks
from discord.ext.commands import Bot
from discord import colour
from discord import embeds
from discord.ext import commands
import random
from discord import guild
from discord import mentions

PREFIX = ('>')
bot= commands.Bot(command_prefix=PREFIX, description='Hi')

# СТАТУС
# задаем варианты статуса бота в режиме онлайн
@bot.event
async def on_ready():
  while True:
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Гражданская Оборона"))
    await sleep (60)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Горнило", type=3))
    await sleep (60)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Genshin Impact", type=3))
    await sleep (60)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Догони меня кирпич", type=3))
    await sleep (60)
print("Артурия готова!")

#КОМАНДЫ
# помощь
@bot.command()
async def помощь(ctx):
  emb = discord.Embed(colour=discord.Colour.blue(),title='Префикс бота: >')
  emb.set_thumbnail(url="https://telegra.ph/file/8593bb2489b650090b39b.png")
  emb.set_footer(text='Список команд:\n>помощь\n>префикс\n>версия\n>ссылки\n>да\n>нет\n>ударить\n')
  await ctx.author.send(embed=emb)

# ссылки
@bot.command()
async def ссылки(ctx):
  emb = discord.Embed(colour=discord.Colour.blue(),title='Привет!\nВот ссылки на наш клан:')
  emb.description = ':white_small_square:[Bungie.net](https://www.bungie.net/ru/ClanV2/Index?groupId=4406402)\n:white_small_square:[Discord](https://discord.gg/zAewvnTp3X)'
  await ctx.author.send(embed=emb)

# да
@bot.command()
async def да(ctx):
  await ctx.send('пизда :)')

# префикс
@bot.command()
async def префикс(ctx):
  await ctx.send('Мой префикс: >')

# версия
@bot.command()
async def версия(ctx):
  await ctx.send('Версия бота: 0.0.2b')

# нет
@bot.command()
async def нет(ctx):
  await ctx.send('пидора ответ :)')

# автор
@bot.command()
async def автор(ctx):
  await ctx.send('Автор бота - <@178517568305364992>')

# ударить
@bot.command()
async def ударить(ctx, member: discord.Member = None):
  arg1 = f"{ctx.author.mention} пытается ударить {member.mention}, но промахивается!"
  arg2 = f"{ctx.author.mention} стукает {member.mention}!"
  arg3 = f"{ctx.author.mention} кидает палку в {member.mention} и попадает в лицо."
  arg4 = f"{ctx.author.mention} кастует фаерболл в {member.mention}, но он почему-то гаснет на полпути."
  arg5 = f"{ctx.author.mention} пытается укусить {member.mention} за ногу!"
  arg6 = f"{ctx.author.mention} засовывет снежок в воротник {member.mention}."
  arg7 = f"{ctx.author.mention} дает поджопник {member.mention}."
  arg8 = f"{ctx.author.mention} дает щелбан {member.mention}."
  test_list = [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8]
  if member == None:
      return
  await ctx.channel.send(random.choice(test_list))

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.role_message_id = 960279710754021437  # ID of the message that can be reacted to to add/remove a role.
        self.emoji_to_role = {
            discord.PartialEmoji(name=':green_circle:'): ,  # ID of the role associated with unicode emoji '🔴'.
            discord.PartialEmoji(name=':red_circle:'): ,  # ID of the role associated with unicode emoji '🟡'.
            discord.PartialEmoji(name=':purple_circle:'): ,  # ID of the role associated with a partial emoji's ID.
        }

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        """Gives a role based on a reaction emoji."""
        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        role = guild.get_role(role_id)
        if role is None:
            # Make sure the role still exists and is valid.
            return

        try:
            # Finally, add the role.
            await payload.member.add_roles(role)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass

    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        """Removes a role based on a reaction emoji."""
        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        role = guild.get_role(role_id)
        if role is None:
            # Make sure the role still exists and is valid.
            return

        # The payload for `on_raw_reaction_remove` does not provide `.member`
        # so we must get the member ourselves from the payload's `.user_id`.
        member = guild.get_member(payload.user_id)
        if member is None:
            # Make sure the member still exists and is valid.
            return

        try:
            # Finally, remove the role.
            await member.remove_roles(role)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass


intents = discord.Intents.default()
intents.members = True
bot.run('')
