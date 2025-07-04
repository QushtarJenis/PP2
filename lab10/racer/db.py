import psycopg2, json
from config import load_config


def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(64) UNIQUE NOT NULL,
            current_level INTEGER NOT NULL DEFAULT 1
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
            score INTEGER NOT NULL,
            coin_score INTEGER NOT NULL,
            level INTEGER NOT NULL,
            state JSONB,
            saved_at TIMESTAMPTZ DEFAULT NOW()
        );
        """,
    )
    cfg = load_config()
    with psycopg2.connect(**cfg) as conn:
        conn.autocommit = True
        with conn.cursor() as cur:
            for cmd in commands:
                cur.execute(cmd)


def get_or_create_user(username):
    cfg = load_config()
    with psycopg2.connect(**cfg) as conn:
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, current_level FROM users WHERE username=%s", (username,)
            )
            row = cur.fetchone()
            if row:
                return row[0], row[1]  # user_id, level
            # create new user
            cur.execute(
                "INSERT INTO users(username) VALUES(%s) RETURNING id, current_level",
                (username,),
            )
            new_id, lvl = cur.fetchone()
            return new_id, lvl


def save_state(id, score, coin_score, level, state):
    cfg = load_config()
    with psycopg2.connect(**cfg) as conn:
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO user_score(user_id, score, coin_score, level, state)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (id, score, coin_score, level, json.dumps(state)),
            )
            cur.execute(
                "UPDATE users SET current_level = %s WHERE id = %s", (level, id)
            )
