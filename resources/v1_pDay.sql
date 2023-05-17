CREATE TABLE IF NOT EXISTS day_game_list (
    member_id text NOT NULL PRIMARY KEY,
    win_count integer NOT NULL,
    today_winner boolean NOT NULL,
    now_active boolean NOT NULL
);