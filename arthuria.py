from importlib.resources import path
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
from discord_components import DiscordComponents, ComponentsBot, Button


#задаем префикс
PREFIX = ('>')
intents = discord.Intents().all()
bot= commands.Bot(command_prefix=PREFIX, intents=intents)

#переменные на всякие штуки
newbierole = "Новичок"
classrole = "⠀⠀⠀⠀⠀⠀⠀⠀КЛАССЫ⠀⠀⠀⠀⠀⠀⠀⠀"
specialrole = "⠀⠀⠀⠀⠀⠀ОСОБЫЕ РОЛИ⠀⠀⠀⠀⠀⠀"
guardianrole = "Страж"
huntrole = "Охотник"
titanrole = "Титан"
warlockrole = "Варлок"
global bot_version
bot_version = "`0.0.6a`"

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

@bot.command(aliases = ['эхо'])
@has_permissions(administrator=True)
async def say(ctx, *, phrase,):
     await ctx.channel.send(phrase)
     await ctx.message.delete()

@bot.command()
async def монетка(ctx):
  coin_x = random.randint(0, 100)
  if coin_x <= 10:
    await ctx.channel.send("Монетка упала на ребро, перекидывай")
  else:
    if (coin_x > 10 and coin_x < 46):
      await ctx.channel.send("У тебя решка!")
    else:
      await ctx.channel.send("У тебя орёл!")

@bot.command(aliases=['рандом', 'РАНДОМ', 'RANDOM'])
async def __random(ctx, num1 = None, num2 = None):
    author = ctx.message.author
    avatar = author.avatar_url
    if num1 != None:
        if num2 != None:
            x = int(num1)
            y = int(num2)
            if x < y:
                value = random.randint(x,y)
                embed=discord.Embed(title='Случайное число', description=f'{author.mention}, вот ваше число: \n**{value}**', color=0x4fff4d)
                embed.set_author(name=f"{author}", icon_url=f"{avatar}")
                await ctx.send(embed=embed)
            else:
                await ctx.send("Первое число больше второго")
        else:
            await ctx.send('Вы не ввели наибольшее число!')
    else:
        await ctx.send('Вы не ввели наименьшее число')

# выдает роли по команде при прохождении собеседования
@bot.command(aliases=['роли', 'РОЛИ', 'ROLES'])
@has_permissions(manage_roles=True)
async def __roles(ctx, member: discord.Member = None):
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
async def __help(ctx):
    embed=discord.Embed(title=f":wave: Привет, {ctx.author.display_name}, я Артурия из клана TITAWIN!", description="Мой префикс: `>`.\n Моя версия на данный момент: " + bot_version + "\n Информация о боте: `бот`", color=0x4fff4d)
    embed.set_thumbnail(url="https://telegra.ph/file/14f906d4ad15ba4ccc001.png")
    embed.add_field(name="Информация по командам", value="Чтобы получить информацию по конкретной команде, введите `>help <команда>` ", inline=False)
    embed.add_field(name="ИНФО", value="> `помощь`, `бот`", inline=False)
    embed.add_field(name="ОБЩЕНИЕ", value="> `ударить`, `монетка`, `рандом <наименьшее число> <наибольшее число>`", inline=False)
    embed.add_field(name="КЛАН", value="> `ссылки`", inline=False)
    embed.set_footer(text="Ответ на сообщение от: {}".format(ctx.author.display_name))
    await ctx.author.send(embed=embed)

# @bot.command(aliases=['помощь', 'ПОМОЩЬ'])
# async def __help(ctx, *, com = None):
#   embed = discord.Embed(
#         color = 0x4fff4d,
#         title = f":wave: Привет, {ctx.author.display_name}, я Артурия из клана TITAWIN!",
#         description = "Мой префикс: `>`.\n Моя версия: " + bot_version,
#   ),
#   embed.add_field(name="Информация по командам", value="Чтобы получить информацию по конкретной команде, введите `>help <команда>` ", inline=False),
#   embed.set_thumbnail(url="https://telegra.ph/file/14f906d4ad15ba4ccc001.png")
#   if com is None:
#     await ctx.author.send (embed=embed,
#     ),
#     embed.add_field(name="ИНФО", value="> `помощь`, `бот`", inline=False),
#     embed.add_field(name="ОБЩЕНИЕ", value="> `ударить`, `монетка`, `рандом <наименьшее число> <наибольшее число>`", inline=False),
#     embed.add_field(name="КЛАН", value="> `ссылки`", inline=False),
#     embed.set_footer(text="Ответ на сообщение от: {}".format(ctx.author.display_name))
#   else:
#     if com == 'бот':
#       embbod = discord.Embed(
#         title = "Информация о команде `>бот`",
#         description = "Выводит информацию о Артурии, ее разработчике и полезные ссылки",
#         color = 0x4fff4d
#       )
#     elif com == 'ударить':
#       embpun = discord.Embed(
#         title = "Информация о команде `>ударить @ник`",
#         description = "Альтернатива обычному пингу пользователя",
#         color = 0x4fff4d
#       )

# очистка - чистит указанное количество сообщений в чате
@bot.command(aliases=['очистка', 'чистка', 'очистить', 'CLEAN', 'ОЧИСТКА', 'ЧИСТКА', 'ОЧИСТИТЬ', 'вилка'])
@has_permissions(manage_roles=True)
async def __clean(ctx, limit):
    await ctx.message.delete()
    limit = int(limit)
    deleted = await ctx.channel.purge(limit=limit)
    cofirmdelete_embed = discord.Embed(title='Удалено', description=f'Удалено **{len(deleted)}** сообщений в **#{ctx.channel}**', color=0x4fff4d)
    await ctx.channel.send(embed=cofirmdelete_embed, delete_after=4.0)


# ссылки - отправляет автору сообщения ссылки на клан в ЛС
@bot.command(aliases=['ссылки', 'ССЫЛКИ', 'LINKS'])
async def __links(ctx):
  emb = discord.Embed(title="Привет!", color=0x4fff4d)
  emb.set_thumbnail(url="https://telegra.ph/file/e756263abab1ffa102c11.png")
  emb.add_field(name="Вот наши ссылочки:", value=":white_small_square:[Bungie.net](https://www.bungie.net/ru/ClanV2/Index?groupId=4406402)\n:white_small_square:[Discord](https://discord.gg/zAewvnTp3X)\n:white_small_square:[Тут мы играем в Тарков](https://discord.gg/ZSSMyPGeaf)")
  emb.set_footer(text="Ответ на сообщение от: {}".format(ctx.author.display_name))
  await ctx.author.send(embed=emb)

# ударить - автор упоминает другого юзера, на что бот удаляет сообщение автора и в РП-форме выводит сценку с участием автора и целевого юзера
@bot.command(aliases=['ударить', 'УДАРИТЬ', 'PUNCH'])
async def __punch(ctx, member: discord.Member = None):
  global punch_list
  punch_list = [" но промахивается", " и попадает прям в глаз"]
  global fireball
  fireball = [f" в {member.mention}, но он почему-то гаснет на полпути.", f". {member.mention} ловит его лицом и загорается!"]
  arg1 = f"{ctx.author.mention} пытается ударить {member.mention}," + (random.choice(punch_list))
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
  arg_list = [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12]
  if member == None:
      return
  await ctx.channel.send(random.choice(arg_list))
  await ctx.message.delete()

# бот = инфа о авторе бота, ссылки и ссылка на донатик
@bot.command(aliases=['бот', 'БОТ', 'BOT'])
async def __bot(ctx):
    embed=discord.Embed(title=f"Артурия Пендрагон, бот клана TITAWIN", description="Версия бота: " + bot_version, color=0x4fff4d)
    embed.set_thumbnail(url="https://telegra.ph/file/e756263abab1ffa102c11.png")
    embed.add_field(name="Разработчик Бота", value="YokainFromAbyss#2300", inline=False)
    embed.add_field(name="Полезные ссылки", value="[Twitter](https://twitter.com/yokainlovesyou), [Клан TITAWIN](https://www.bungie.net/ru/ClanV2/Index?groupId=4406402), [Github](https://github.com/YokainFromAbyss)", inline=False)
    embed.add_field(name="Донат", value="[Закинуть монетку](https://www.donationalerts.com/r/yokainlovesyou)", inline=False)
    embed.add_field(name="Благодарности", value="[Ningi](https://www.twitch.tv/n1ngi)\nHAPPYV0DKA#8354 (создатель бота [Indeedstor](https://top.gg/bot/677145368894373965))", inline=False)
    embed.set_footer(text="Ответ на сообщение от: {}".format(ctx.author.display_name))
    await ctx.author.send(embed=embed)

# панель администратора
@bot.command(aliases=['админка', 'АДМИНКА', 'ADMIN'])
@has_permissions(manage_roles=True)
async def __admin(ctx):
    embed=discord.Embed(title=f":wave: Привет, {ctx.author.display_name}, это панель администратора'", description="Мой префикс: `>`.\n Моя версия на данный момент: " + bot_version, color=0x4fff4d)
    embed.set_thumbnail(url="https://telegra.ph/file/14f906d4ad15ba4ccc001.png")
    embed.add_field(name="Команды", value="`>роли @ник` - выдаёт Новичку роли для открытия сервера после собеседования;\n`>очистка <число>` - очищает чат от указанного количества сообщений;", inline=False)
    embed.set_footer(text="Ответ на сообщение от: {}".format(ctx.author.display_name))
    await ctx.author.send(embed=embed)

# рейдовые команды

@bot.command()
async def гайд(ctx, *, raid = None):
  if raid is None:
    await ctx.channel.send('Введите `>рейд (нужный рейд)`. Сейчас доступны: `пж`, `сс`, `сгк`, `кп`')
  else:
    if raid == 'пж':
      embed=discord.Embed(title="ПОСЛЕДНЕЕ ЖЕЛАНИЕ", description="Информация, необходимая для прохождения рейда.", color=0x4fff4d)
      embed.set_thumbnail(url="https://www.bungie.net/img/theme/destiny/icons/fireteams/fireteam_LastWish.png")
      embed.add_field(name="Список желаний:", value="**[Ссылка](https://telegra.ph/Spisok-zhelanij-Poslednee-ZHelanie-04-26)**", inline=False)
      embed.add_field(name="Первый этап. Техноведьма Калли:", value="**[Видео](https://youtu.be/6OClV3FA0ME)\n[Карта этапа](https://cdn.discordapp.com/attachments/951876826454704168/968564674889146408/44dcd70c4d12c144.png)**", inline=False)
      embed.add_field(name="Второй этап. Техноведьма Шуро Чи:", value="**[Видео](https://youtu.be/E8iscYWSvuA)\n[Гифка по прохождению телефона](https://cdn.discordapp.com/attachments/951876826454704168/968570665231859772/fpsp6ce_1.gif)**", inline=False)
      embed.add_field(name="Третий этап. Огр Моргет:", value="**[Видео](https://www.youtube.com/watch?v=yXWL35lzHhA)**", inline=False)
      embed.add_field(name="Четвертый этап. Хранилище:", value="**[Видео](https://www.youtube.com/watch?v=A0MuTKlja7c)\n[Карта этапа](https://cdn.discordapp.com/attachments/951876826454704168/968572250531971122/unknown.png)**\n***Подсказка:***\nСимвол слева - у вас полутьма;\nСимвол справа - у вас полусвет;", inline=False)
      embed.add_field(name="Финальный босс. Тысячеголосая Ривен:", value="**[Видео](https://www.youtube.com/watch?v=di5qdvKTnnQ)\n[Быстрый способ](https://www.youtube.com/watch?v=Ui1MT1ZUUX8&t=1366s)**", inline=False)
      embed.set_footer(text="Удачи тебе в рейде, {}".format(ctx.author.display_name))
      embed.set_image(url="https://assets.reedpopcdn.com/destiny-2-last-wish-raid-start-time-rewards-5382-1536929323933.jpg/BROK/resize/1200x1200%3E/format/jpg/quality/70/destiny-2-last-wish-raid-start-time-rewards-5382-1536929323933.jpg")
      await ctx.author.send(embed=embed)
    elif raid == 'сс':
      embed=discord.Embed(title="САД СПАСЕНИЯ", description="Информация, необходимая для прохождения рейда.", color=0x4fff4d)
      embed.set_thumbnail(url="https://www.bungie.net/img/theme/destiny/icons/fireteams/fireteam_GardenOfSalvation.png")
      embed.add_field(name="Первый этап:", value="**[Видео](https://www.youtube.com/watch?v=AI5dZzBYlMg)**", inline=False)
      embed.add_field(name="Второй этап:", value="**[Видео](https://www.youtube.com/watch?v=N-T0HHj28VI)**", inline=False)
      embed.add_field(name="Третий этап:", value="**[Видео](https://www.youtube.com/watch?v=H9mZ0vGBzY4)**", inline=False)
      embed.add_field(name="Финальный босс:", value="**[Видео](https://www.youtube.com/watch?v=wPCaw0FbeAk)**\n**[Карта этапа](https://i.imgur.com/iEIEy6X.png)**", inline=False)
      embed.add_field(name="Гайд на триумфы:", value="**[Видео](https://youtu.be/43fe3Zmru3U)**", inline=False)
      embed.add_field(name="Квест на Божественность:", value="**[Видео](https://youtu.be/d8K9tCjYXJE)**", inline=False)
      embed.set_footer(text="Удачи тебе в рейде, {}".format(ctx.author.display_name))
      embed.set_image(url="https://www.vgr.com/wp-content/uploads/2019/09/destiny-2-shadowkeep-garden-of-salvation-3.jpg")
      await ctx.author.send(embed=embed)
    elif raid == 'сгк':
      embed=discord.Embed(title="СКЛЕП ГЛУБОКОГО КАМНЯ", description="Информация, необходимая для прохождения рейда.", color=0x4fff4d)
      embed.set_thumbnail(url="https://www.bungie.net/img/theme/destiny/icons/fireteams/fireteam_DeepStoneCrypt.png")
      embed.add_field(name="Предэтап:", value="**[Видео](https://www.youtube.com/watch?v=hpLumgP08eE&t=73s)\n[Карта (большая)](https://ibb.co/CQJghCd)**", inline=False)
      embed.add_field(name="Первый этап:", value="**[Видео](https://www.youtube.com/watch?v=hpLumgP08eE&t=291s)\n[Карта](https://imgur.com/7oQStDq)**", inline=False)
      embed.add_field(name="Второй этап:", value="**[Видео](https://www.youtube.com/watch?v=hpLumgP08eE&t=601s)**", inline=False)
      embed.add_field(name="Третий этап:", value="**[Видео](https://www.youtube.com/watch?v=hpLumgP08eE&t=1453s)**", inline=False)
      embed.add_field(name="Финальный босс:", value="**[Видео](https://www.youtube.com/watch?v=hpLumgP08eE&t=2078s)**", inline=False)
      embed.set_footer(text="Удачи тебе в рейде, {}".format(ctx.author.display_name))
      embed.set_image(url="https://api.dving.org/media/image/28/29/39ff9ee007bf5bb887fb6697b35c.png")
      await ctx.author.send(embed=embed)
    elif raid == 'кп':
      embed=discord.Embed(title="КЛЯТВА ПОСЛУШНИКА", description="Информация, необходимая для прохождения рейда.", color=0x4fff4d)
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/981450909278150666/981450938101420062/unknown.png")
      embed.add_field(name="Символы:", value="[Картинка](https://media.discordapp.net/attachments/981450909278150666/982754245705097277/unknown.png)", inline=True)
      embed.add_field(name="Гайд по сундуку:", value="[Картинка](https://ibb.co/qY5BVpj)", inline=True)
      embed.add_field(name="Предэтап:", value="[Видео](https://www.youtube.com/watch?v=KPecQIsSewU&t=0s)", inline=False)
      embed.add_field(name="Первый этап:", value="[Видео](https://www.youtube.com/watch?v=KPecQIsSewU&t=37s)\n[Карта этапа](https://media.discordapp.net/attachments/951876826454704168/968549500580950046/unknown.png)", inline=False)
      embed.add_field(name="Второй этап:", value="[Видео](https://www.youtube.com/watch?v=KPecQIsSewU&t=198s)", inline=False)
      embed.add_field(name="Третий этап:", value="[Видео](https://www.youtube.com/watch?v=KPecQIsSewU&t=442s)\n[Карта этапа](https://media.discordapp.net/attachments/981450909278150666/982756017282646066/unknown.png?width=1178&height=662)", inline=False)
      embed.add_field(name="Финальный босс:", value="[Видео](https://www.youtube.com/watch?v=KPecQIsSewU&t=665s)\n[Карта этапа](https://media.discordapp.net/attachments/981450909278150666/982756339736526900/unknown.png?width=1178&height=662)", inline=False)
      embed.set_footer(text="Удачи тебе в рейде, {}".format(ctx.author.display_name))
      embed.set_image(url="https://oyster.ignimgs.com/mediawiki/apis.ign.com/destiny-2/f/f0/Votd.jpg")
      await ctx.author.send(embed=embed)
      
bot.run('')
