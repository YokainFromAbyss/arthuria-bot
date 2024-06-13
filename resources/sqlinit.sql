CREATE TABLE IF NOT EXISTS sync_dates (
    sync_name text NOT NULL PRIMARY KEY,
    date_string text NOT NULL
);
CREATE TABLE IF NOT EXISTS day_game_list (
    member_id text NOT NULL PRIMARY KEY,
    win_count integer NOT NULL,
    today_winner boolean NOT NULL,
    now_active boolean NOT NULL
);