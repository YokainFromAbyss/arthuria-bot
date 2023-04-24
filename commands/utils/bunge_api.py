import requests
import datetime
import yaml


def load_news():
    with open('./resources/config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    links = []
    key = config['api-key']
    if key == "":
        return links
    headers = {"X-API-Key": key}
    r = requests.get(f"https://www.bungie.net/platform//Content/Rss/NewsArticles/0/", headers=headers)
    resp = r.json()
    news = resp['Response']['NewsArticles']

    now = datetime.datetime.utcnow()
    delta = datetime.timedelta(
        minutes=10,
        seconds=1
    )
    for n in news:
        date = datetime.datetime.strptime(n['PubDate'], "%Y-%m-%dT%H:%M:%SZ")
        diff = now - date
        if diff <= delta:
            links.append("https://www.bungie.net" + n['Link'])
    return links
