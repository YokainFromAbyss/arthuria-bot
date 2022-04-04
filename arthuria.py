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
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="версия 0.0.2alpha", type=3))
    await sleep (60)
print("Артурия готова!")

#КОМАНДЫ
# помощь
# @bot.command()
# async def помощь(json):
#   const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
#   await lib.discord.channels['@0.3.0'].messages.create(
#     {
#       "channel_id": `${context.params.event.channel_id}`,
#       "content": "",
#       "tts": false,
#       "embeds": [
#     {
#       "type": "rich",
#       "title": `Привет, я Артурия из клана TITAWIN!`,
#       "description": `Мой префикс: `>`.,
#       "color": 0xfdf5cd,
#       "fields": [
#         {
#           "name": `Команда`,
#           "value": `---\n\`помощь\`\n\n\`ссылки\`\n\n\`да\`\n\n\`нет\`\n\n\`ударить\``,
#           "inline": true
#         },
#         {
#           "name": `Действие`,
#           "value": `---\nполный список команд бота\n\nотправлю в ЛС ссылки на bungie.net и Discord Титавина\n\nшуточный ответ на \"да\"\n\nшуточный ответ на \"нет\"\n\nупоминает участника с описанием действия`,
#           "inline": true
#         }
#       ],
#       "thumbnail": {
#         "url": `https://sun9-50.userapi.com/impf/QS-RWZcjQa_A_N_Z1IQh0qjy6BRD2-AFQE81mw/I6_jMI6io_Y.jpg?size=286x282&quality=95&sign=fd83f4890ff6ea18e1da9de57c1eccaf&type=album`,
#         "height": 0,
#         "width": 0
#       },
#       "footer": {
#         "text": `---\nРазработчик бота: YokainFromAbyss#2300`
#       }
#     }
#   ]
# });

@bot.command()
async def помощь(ctx): 
    embed=discord.Embed(title="Привет, я Артурия из клана TITAWIN!", description="Мой префикс: `>`.\n\n Моя версия на данный момент `0.0.2alpha`", colour=discord.Colour.blue())
    embed.set_thumbnail(url="https://telegra.ph/file/14f906d4ad15ba4ccc001.png")
    embed.add_field(name="Команды", value="```>помощь - полный список команд бота\n\n>ссылки - отправлю в ЛС ссылки на наш клан\n\n>да - шуточный ответ на \"Да\"\n\n>нет - шуточный ответ на \"Нет\"\n\n>ударить - упоминает участника с описанием действия```", inline=True)
    await ctx.author.send(embed=embed)

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
async def бот(ctx):
  await ctx.send('Автор бота - <@178517568305364992>, Версия бота: 0.0.2b от 1.04.2022. Выражаю благодарность создателю бота [Indeedstor](https://top.gg/bot/677145368894373965) за вдохновение и желание впервые сделать своего бота.')

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
  arg9 = f"{ctx.author.mention} шепчет на ушко {member.mention} \"Чувствуешь пальчик в жопе? А ручки-то мои у тебя на шее\" :)"
  arg10 = f"{ctx.author.mention} пытается вызвать чуму у {member.mention}, но тут же начинает чихать."
  test_list = [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10]
  if member == None:
      return
  await ctx.channel.send(random.choice(test_list))

intents = discord.Intents.default()
intents.members = True
bot.run('')
