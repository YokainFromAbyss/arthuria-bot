import datetime
import psycopg2
import yaml
import random
from dateutil.parser import *
import logging

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:[%(levelname)s]:[%(name)s]: %(message)s'))
LOG.addHandler(handler)


def connection():
    with open('./resources/config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    conn = psycopg2.connect(dbname=config['dbname'], user=config['dbuser'],
                            password=config['dbpassword'], host=config['dbhost'])
    conn.autocommit = True
    LOG.debug("Create connection for DB: %s, %s, %s", config['dbhost'], config['dbname'], config['dbuser'])
    return conn


def last_news_pull():
    LOG.debug("Getting last news date")
    last_pull = datetime.datetime.utcnow()
    with connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT date_string FROM sync_dates WHERE sync_name='news';")
            records = cursor.fetchall()
            if len(records) == 0:
                cursor.execute(
                    "INSERT INTO sync_dates (sync_name, date_string) VALUES ('news', %s);",
                    [last_pull]
                )
            else:
                last_pull = parse(records[0][0])
            LOG.debug("Last news date: %s", last_pull)
            return last_pull


def update_news_pull(pull_date: datetime.datetime):
    LOG.debug("Update last news date: %s", pull_date)
    with connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE sync_dates SET date_string = %s WHERE sync_name='news';",
                [pull_date]
            )


def game_register(member_id: str):
    LOG.debug("Register user: %s in day_game", member_id)
    with connection() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(
                    """INSERT INTO day_game_list (member_id, win_count, today_winner, now_active) 
                    VALUES (%s, 0, false, true) ON CONFLICT (member_id) 
                    DO UPDATE SET now_active = true;""",
                    [str(member_id)]
                )
                return True
            except psycopg2.Error:
                return False


def game_unregister(member_id: str):
    LOG.debug("Unregister user: %s in day_game", member_id)
    with connection() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(
                    "UPDATE day_game_list SET now_active = false WHERE member_id = %s;",
                    [str(member_id)]
                )
                return True
            except psycopg2.Error:
                return False


def game_roll():
    LOG.debug("Rolling day_game winner")
    today = datetime.datetime.utcnow().date()
    roll = False
    with connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT date_string FROM sync_dates WHERE sync_name='gay_game';")
            records = cursor.fetchall()
            if len(records) == 0:
                roll = True
            else:
                last_roll = datetime.datetime.strptime(records[0][0], "%Y-%m-%d").date()
                if today > last_roll:
                    roll = True

    if roll:
        with connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("UPDATE day_game_list SET today_winner = false WHERE today_winner = true")
                cursor.execute("SELECT member_id FROM day_game_list WHERE now_active = true;")
                res = cursor.fetchall()
                if len(res) == 0:
                    return False, -1
                winner_id = res[random.randrange(len(res))][0]
                cursor.execute(
                    "UPDATE day_game_list SET win_count = win_count + 1, today_winner = true WHERE member_id = %s",
                    [str(winner_id)]
                )

                cursor.execute(
                    """INSERT INTO sync_dates (sync_name, date_string) VALUES ('gay_game', %s) ON CONFLICT (sync_name) 
                    DO UPDATE SET date_string = %s;
                    """,
                    [today, today]
                )
                LOG.debug("New winner: %s today", winner_id)
                return roll, winner_id
    else:
        with connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT member_id FROM day_game_list WHERE today_winner = true;")
                res = cursor.fetchall()
                LOG.debug("Secondary roll today")
                return roll, res[0][0]


def game_top(count: int):
    LOG.debug("Getting %s winners in day_game", count)
    with connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT member_id, win_count FROM day_game_list ORDER BY win_count DESC LIMIT %s;",
                [count]
            )
            res = cursor.fetchall()
            return res
