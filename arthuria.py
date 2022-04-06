from asyncore import loop
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
import json

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
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Испытания Осириса", type=3))
    await sleep (60)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Железное Знамя", type=3))
    await sleep (60)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Genshin Impact", type=3))
    await sleep (60)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="версия 0.0.3alpha", type=3))
    await sleep (60)
print("Артурия готова!")

#КОМАНДЫ
# помощь
@bot.command(aliases=['помощь', 'ПОМОЩЬ'])
async def __помощь(ctx):
    embed=discord.Embed(title="Привет, я Артурия из клана TITAWIN!", description="Мой префикс: `>`.\n\n Моя версия на данный момент `0.0.3alpha`", colour=discord.Colour.blue())
    embed.set_thumbnail(url="https://telegra.ph/file/14f906d4ad15ba4ccc001.png")
    embed.add_field(name="Команда\n\n", value="`помощь`\n\n`ссылки`\n\n`да`\n\n`нет`\n\n`ударить`", inline=True)
    embed.add_field(name="Описание\n\n", value="полный список команд бота\n\nотправлю в ЛС ссылки на наш клан\n\nшуточный ответ на \"Да\"\n\nшуточный ответ на \"Нет\"\n\nупоминает участника с описанием действия", inline=True)
    await ctx.author.send(embed=embed)

# ссылки
@bot.command(aliases=['ссылки', 'ССЫЛКИ', 'links', 'LINKS'])
async def __ссылки(ctx):
  emb = discord.Embed(colour=discord.Colour.blue(),title='Привет!\nВот ссылки на наш клан:')
  emb.description = ':white_small_square:[Bungie.net](https://www.bungie.net/ru/ClanV2/Index?groupId=4406402)\n:white_small_square:[Discord](https://discord.gg/zAewvnTp3X)'
  await ctx.author.send(embed=emb)

# да
@bot.command(aliases=['да', 'ДА'])
async def __да(ctx):
  await ctx.send('пизда :)')

# нет
@bot.command(aliases=['нет', 'НЕТ'])
async def __нет(ctx):
  await ctx.send('пидора ответ :)')

# ударить
@bot.command(aliases=['ударить', 'УДАРИТЬ'])
async def __ударить(ctx, member: discord.Member = None):
  global punch
  punch = [" но промахивается", " и попадает прям в глаз"]
  global fireball
  fireball = [f" в {member.mention}, но он почему-то гаснет на полпути.", f". {member.mention} ловит его лицом и загорается!"]
  arg1 = f"{ctx.author.mention} пытается ударить {member.mention}," + (random.choice(punch))
  arg2 = f"{ctx.author.mention} стукает {member.mention}!"
  arg3 = f"{ctx.author.mention} кидает палку в {member.mention} и попадает в лицо."
  arg4 = f"{ctx.author.mention} кастует фаерболл" + (random.choice(fireball))
  arg5 = f"{ctx.author.mention} пытается укусить {member.mention} за ногу!"
  arg6 = f"{ctx.author.mention} засовывет снежок в воротник {member.mention}."
  arg7 = f"{ctx.author.mention} дает поджопник {member.mention}."
  arg8 = f"{ctx.author.mention} дает щелбан {member.mention}."
  arg9 = f"{ctx.author.mention} шепчет на ушко {member.mention} \"Чувствуешь пальчик в жопе? А ручки-то мои у тебя на шее\" :)"
  arg10 = f"{ctx.author.mention} пытается вызвать чуму у {member.mention}, но тут же начинает чихать."
  arg11 = f"{ctx.author.mention} делает бэкстаб {member.mention}. Watch your ass!"
  arg12 = f"{ctx.author.mention} прописывает красочную вертуху по лицу {member.mention}"
  test_list = [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12]
  if member == None:
      return
  await ctx.channel.send(random.choice(test_list))

# цитата
@bot.command(aliases=['цитаты', 'ЦИТАТЫ'])
async def __цитаты(ctx, member: discord.Member = None):
  quote1 = f"Ненавижу мультики, где есть один жирный долбоёб\n@namvseyasno"
  quote2 = f"Пол часа ночи @Gyrmanin"
  quote3 = f"- Сколько у тебя было IQ в школе?\n- Пятёрка)))\n@namvseyasno"
  quote4 = f"Ада блядь та еще... видел порно с ней @Gyrmanin"
  quote5 = f"Германин, куда ты опять сиськи свои вставил? @namvseyasno to @Gyrmanin"
  quote6 = f"великий китайзиум (с) кто-то"
  quote7 = f"ДЭБЭДЛЭ @Gyrmanin"
  quote8 = f"Это даже цитатой назвать сложно, это хуйня какая-то @Simmeris"
  quote9 = f"У нас токсичные только Диман.. И ты.. @Gyrmanin to @namvseyasno"
  quote10 = f"Залетим в Башлем @Gyrmanin"
  quote_list = [quote1, quote2, quote3, quote4, quote5, quote6, quote7, quote8, quote9, quote10]
  if member == None:
      return
  await ctx.channel.send(random.choice(quote_list))

bot.run('')
