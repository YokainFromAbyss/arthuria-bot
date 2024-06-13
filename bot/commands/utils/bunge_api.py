import datetime
import requests
import yaml
from dateutil.parser import *

from commands.utils.sql_storage import last_news_pull, update_news_pull


def load_news():
    with open('./resources/config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    links = []
    key = config['api-key']
    if key == "":
        return links
    headers = {"X-API-Key": key}
    r = requests.get(f"https://www.bungie.net/platform/Content/Rss/NewsArticles/0/", headers=headers)
    resp = r.json()
    news = resp['Response']['NewsArticles']

    last_pull = last_news_pull()
    dates = []

    for n in news:
        date = parse(n['PubDate'])
        if date.timestamp() > last_pull.timestamp():
            dates.append(date)
            links.append("https://www.bungie.net" + n['Link'])
    if len(links) > 0:
        update_news_pull(max(dates))
    return links
