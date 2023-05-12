import requests
import datetime
import psycopg2
import yaml


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

    last_pull = datetime.datetime.utcnow()
    conn = psycopg2.connect(dbname=config['dbname'], user=config['dbuser'],
                            password=config['dbpassword'], host=config['dbhost'])
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("SELECT date_string FROM sync_dates WHERE sync_name='news';")
    records = cursor.fetchall()
    if len(records) == 0:
        cursor.execute(
            "INSERT INTO sync_dates (sync_name, date_string) VALUES ('news', %s);",
            [last_pull]
        )
    else:
        cursor.execute(
            "UPDATE sync_dates SET date_string=%s WHERE sync_name='news';",
            [last_pull]
        )
        last_pull = datetime.datetime.strptime(records[0][0], "%Y-%m-%d %H:%M:%S.%f")
    cursor.close()
    conn.close()

    # print(last_pull)
    for n in news:
        date = datetime.datetime.strptime(n['PubDate'], "%Y-%m-%dT%H:%M:%SZ")
        # print(n['Link'], date)
        # print(date >= last_pull)
        if date >= last_pull:
            links.append("https://www.bungie.net" + n['Link'])
    return links
