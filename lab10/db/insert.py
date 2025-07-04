import psycopg2
from .config import load_config


def insert(user_name, phone):

    sql = """INSERT INTO contact(user_name, phone)
             VALUES(%s, %s) RETURNING id;"""

    id = None
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (user_name, phone))

                # get the generated id back
                rows = cur.fetchone()
                if rows:
                    id = rows[0]

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return id


def insert_many(list):
    sql = "INSERT INTO contact(user_name, phone) VALUES(%s, %s) RETURNING *"

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the INSERT statement
                cur.executemany(sql, list)

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == "__main__":
    # insert("Qushtar", "+77071234567")
    insert_many(
        [
            ("Erzhan", "+77771234567"),
            ("Erlan", "+77781234567"),
            ("Nurbol", "+77081234567"),
        ]
    )
