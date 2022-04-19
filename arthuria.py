import discord
import asyncio
from asyncio import sleep
from discord import utils
from discord.ext import tasks
from discord.ext.commands import Bot
from discord import colour
from discord import embeds
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import random
from discord import guild
from discord import mentions
import json

#задаем префикс
PREFIX = ('>')
intents = discord.Intents().all()
bot= commands.Bot(command_prefix=PREFIX, intents=intents)

#переменные на всякие штуки
newbierole = "Новичок"
classrole = "⠀⠀⠀⠀⠀⠀⠀⠀КЛАССЫ⠀⠀⠀⠀⠀⠀⠀⠀"
specialrole = "⠀⠀⠀⠀⠀⠀ОСОБЫЕ РОЛИ⠀⠀⠀⠀⠀⠀"
guardianrole = "Страж"


# СТАТУС
# задаем варианты статуса бота в режиме онлайн
@bot.event
async def on_ready():
  while True:
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Гражданская Оборона"))
    await sleep (30)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Горнило", type=3))
    await sleep (30)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Испытания Осириса", type=3))
    await sleep (30)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Железное Знамя", type=3))
    await sleep (30)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Genshin Impact", type=3))
    await sleep (30)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=">помощь", type=3))
    await sleep (30)
print("Артурия готова!")

# автоматически выдает роль при входе на сервер
@bot.event
async def on_member_join(member):
  role = get(member.guild.roles, name=newbierole)
  await member.add_roles(role)
  print(f"{member} получил {role}")

# выдает роли по команде при прохождении собеседования
@bot.command(aliases=['роли', 'РОЛИ'], pass_context=True)
@has_permissions(manage_roles=True)
async def __роли(ctx, member: discord.Member = None):
  role1 = get(member.guild.roles, name=classrole)
  role2 = get(member.guild.roles, name=specialrole)
  role3 = get(member.guild.roles, name=guardianrole)
  role = get(member.guild.roles, name=newbierole)
  await member.add_roles(role1)
  await member.add_roles(role2)
  await member.add_roles(role3)
  await member.remove_roles(role)
  await ctx.channel.send(f"Роли {member.mention} выданы", delete_after=4.0)
  print(f"{member} получил роли {role1}, {role2}, {role3}")

#КОМАНДЫ
# помощь - присылает автору инфу по боту и командам прямо в ЛС
@bot.command(aliases=['помощь', 'ПОМОЩЬ'])
async def __помощь(ctx):
    embed=discord.Embed(title=f":wave: Привет, {ctx.author.display_name}, я Артурия из клана TITAWIN!", description="Мой префикс: `>`.\n Моя версия на данный момент `0.0.4alpha`", color=0x4fff4d)
    embed.set_thumbnail(url="https://telegra.ph/file/14f906d4ad15ba4ccc001.png")
    embed.add_field(name="ИНФО", value="> `помощь`, `алиасы`, `бот`", inline=False)
    embed.add_field(name="ОБЩЕНИЕ", value="> `ударить`, `да`, `нет`, `цитаты`", inline=False)
    embed.add_field(name="КЛАН", value="> `ссылки`", inline=False)
    embed.set_footer(text="Ответ на сообщение от: {}".format(ctx.author.display_name))
    await ctx.author.send(embed=embed)

# очистка - чистит указанное количество сообщений в чате
@bot.command(pass_context=True)
@has_permissions(manage_roles=True)
async def очистка(ctx, limit):
    await ctx.message.delete()
    limit = int(limit)
    deleted = await ctx.channel.purge(limit=limit)
    cofirmdelete_embed = discord.Embed(title='Удалено', description=f'Удалено **{len(deleted)}** сообщений в **#{ctx.channel}**', color=0x4fff4d)
    await ctx.channel.send(embed=cofirmdelete_embed, delete_after=4.0)

# пишет от имени бота
@bot.command()
async def эхо(ctx): 
    channel = discord.Object(id=input('channel id'))
    await bot.send_message(channel, input('message'))

# ссылки - отправляет автору сообщения ссылки на клан в ЛС
@bot.command(aliases=['ссылки', 'ССЫЛКИ', 'links', 'LINKS'])
async def __ссылки(ctx):
  emb = discord.Embed(colour=discord.Colour.blue(),title="Привет!\nВот ссылки на наш клан:", color=0x4fff4d)
  emb.description = ':white_small_square:[Bungie.net](https://www.bungie.net/ru/ClanV2/Index?groupId=4406402)\n:white_small_square:[Discord](https://discord.gg/zAewvnTp3X)'
  await ctx.author.send(embed=emb)

# да - ну тут и так все понятно + удаляет сообщение с командой. Да, я считаю это смешным.
@bot.command(aliases=['да', 'ДА'])
async def __да(ctx):
  await ctx.send('пизда :)')
  await ctx.message.delete()

# нет - аналогично предыдущей команде
@bot.command(aliases=['нет', 'НЕТ'])
async def __нет(ctx):
  await ctx.send('пидора ответ :)')
  await ctx.message.delete()

# ударить - автор упоминает другого юзера, на что бот удаляет сообщение автора и в РП-форме выводит сценку с участием автора и целевого юзера
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
  await ctx.message.delete()

# бот = инфа о авторе бота, ссылки и ссылка на донатик
@bot.command()
async def бот(ctx):
    embed=discord.Embed(title=f"Артурия Пендрагон, бот клана TITAWIN", description="Версия бота: `0.0.4alpha`", colour=discord.Colour.blue())
    embed.set_thumbnail(url="https://telegra.ph/file/e756263abab1ffa102c11.png")
    embed.add_field(name="Разработчик Бота", value="YokainFromAbyss#2300", inline=False)
    embed.add_field(name="Полезные ссылки", value="[Twitter](https://twitter.com/yokainlovesyou), [Клан TITAWIN](https://www.bungie.net/ru/ClanV2/Index?groupId=4406402), [Github](https://github.com/YokainFromAbyss)", inline=False)
    embed.add_field(name="Донат", value="[Закинуть монетку](https://www.donationalerts.com/r/yokainlovesyou)", inline=False)
    embed.set_footer(text="Ответ на сообщение от: {}".format(ctx.author.display_name))
    await ctx.author.send(embed=embed)

# # панель администратора
# @bot.command()
# async def админка(ctx):
#     embed=discord.Embed(title=f":wave: Привет, {ctx.author.display_name}, это панель администратора'", description="Мой префикс: `>`.\n Моя версия на данный момент `0.0.4alpha`", color=0x4fff4d)
#     embed.set_thumbnail(url="https://telegra.ph/file/14f906d4ad15ba4ccc001.png")
#     embed.add_field(name="ИНФО", value="> `помощь`, `алиасы`, `бот`", inline=False)
#     embed.add_field(name="ОБЩЕНИЕ", value="> `ударить`, `да`, `нет`, `цитаты`", inline=False)
#     embed.add_field(name="КЛАН", value="> `ссылки`", inline=False)
#     embed.set_footer(text="Ответ на сообщение от: {}".format(ctx.author.display_name))
#     await ctx.author.send(embed=embed)


# цитата - выводит рандомную цитату из фонда золотых цитат клана TITAWIN
@bot.command(aliases=['цитаты', 'ЦИТАТЫ', 'цитата', 'ЦИТАТА'])
async def __цитаты(ctx):
  q1 = f"Ненавижу мультики, где есть один жирный долбоёб\n@namvseyasno"
  q2 = f"Пол часа ночи @Gyrmanin"
  q3 = f"- Сколько у тебя было IQ в школе?\n- Пятёрка)))\n@namvseyasno"
  q4 = f"Ада блядь та еще... видел порно с ней @Gyrmanin"
  q5 = f"Германин, куда ты опять сиськи свои вставил? @namvseyasno to @Gyrmanin"
  q6 = f"великий китайзиум (с) кто-то"
  q7 = f"ДЭБЭДЛЭ @Gyrmanin"
  q8 = f"Это даже цитатой назвать сложно, это хуйня какая-то @Simmeris"
  q9 = f"У нас токсичные только Диман.. И ты.. @Gyrmanin to @namvseyasno"
  q10 = f"Залетим в Башлем @Gyrmanin"
  q11 = f"Покушать хачи отойтю @Gyrmanin"
  q12 = f"Это не в твой камень огород @Gyrmanin"
  q13 = f"Про \"Дыхание Левиафана\" и стан воителей: Пока ты натягиваешь тетиву, воитель натянет тебя @Primis"
  q14 = f"Таблица Мандилеева @Gyrmanin"
  quote_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14]
  await ctx.channel.send(random.choice(quote_list))
  
bot.run('')
