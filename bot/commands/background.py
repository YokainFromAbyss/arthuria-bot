import discord
from discord.ext import commands, tasks
import random
import yaml
import datetime

from commands.utils.bunge_api import load_news
import logging

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:[%(levelname)s]:[%(name)s]: %(message)s'))
LOG.addHandler(handler)


class Background(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        # Играет в
        self.game_roulette = [
            "Горнило",
            "Испытания Осириса",
            "очко с крысой",
            "могилу",
            "Гамбит",
            "своей попке",
            "DnD",
            "хентай пазлы",
            "Срачи с Мерси",
        ]
        self.status.add_exception_type(Exception)
        self.status.start()
        # del message cleaner
        self.del_message = "[Original Message Deleted]"
        self.channels = [1053280305852719125, 1069550535331553340]  # чекпоинты, сборы p2p
        self.del_message_cleaner.add_exception_type(Exception)
        self.del_message_cleaner.start()
        # Bungie news posts
        self.content_channel = 1050041513712824330  # контент
        self.news_lookup.add_exception_type(Exception)
        self.news_lookup.start()
        # cleanup AFK not registered members
        self.registration_clean.add_exception_type(Exception)
        self.registration_clean.start()

    @tasks.loop(seconds=60)
    async def status(self):
        LOG.info("Updating status")
        ind = random.randint(1, len(self.game_roulette))
        await self.bot.change_presence(status=discord.Status.online,
                                       activity=discord.Game(name=self.game_roulette[ind - 1], type=3))

    @tasks.loop(hours=6)
    async def del_message_cleaner(self):
        LOG.info("Clearing messages")
        for c in self.channels:
            channel = self.bot.get_channel(c)
            LOG.info("Clearing channel %s", channel.name)
            messages = await channel.history(limit=None).flatten()
            for m in messages:
                if m.content == self.del_message:
                    await m.delete()

    @tasks.loop(minutes=10)
    async def news_lookup(self):
        LOG.info("Lookup news")
        channel = self.bot.get_channel(self.content_channel)
        links = load_news()
        LOG.info("Pull %s news", len(links))
        for link in links:
            await channel.send("Новая статья на bungie.net\n" + link)

    @tasks.loop(minutes=30)
    async def registration_clean(self):
        LOG.info("Clean registration channel")
        with open('./resources/config.yaml') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)['registration']
        # clean channel
        now = datetime.datetime.now(datetime.timezone.utc)
        channel = self.bot.get_channel(config['channel'])
        safe_id = config['safe-user']
        clean_delta = datetime.timedelta(hours=config['timeout-hours']['clean'])
        messages = await channel.history(limit=None).flatten()
        LOG.debug("Find %s messages", len(messages))
        for m in messages:
            if m.author.id != safe_id:
                if clean_delta <= now - m.created_at:
                    await m.delete()
        # kick members
        kick_delta = datetime.timedelta(hours=config['timeout-hours']['kick'])
        LOG.info("Kicking members older then %s", kick_delta)
        for member in channel.members:
            roles = list(map(lambda r: r.id, member.roles))
            if any(x in roles for x in config['unkick-roles']):
                continue
            if config['kick-role'] in roles:
                if kick_delta <= now - member.joined_at:
                    LOG.info("Kicking member: %s", member.name)
                    await member.kick(reason="No registration timeout")

    @status.before_loop
    @del_message_cleaner.before_loop
    @news_lookup.before_loop
    @registration_clean.before_loop
    async def before_background(self):
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(Background(bot))
