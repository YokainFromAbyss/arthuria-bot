import requests
import datetime
import yaml

from commands.utils.sql_storage import last_news


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

    last_pull = last_news()

    # print(last_pull)
    for n in news:
        date = datetime.datetime.strptime(n['PubDate'], "%Y-%m-%dT%H:%M:%SZ")
        # print(n['Link'], date)
        # print(date >= last_pull)
        if date >= last_pull:
            links.append("https://www.bungie.net" + n['Link'])
    return links
