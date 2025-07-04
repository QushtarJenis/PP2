import psycopg2
from .config import load_config


def update(phone, new_phone=None, new_name=None):

    if new_phone is None and new_name is None:
        print("Missing parameter")
        return 0

    updated_row_count = 0
    params = [phone]

    sql = "UPDATE contact "

    if new_phone is not None:
        sql += "SET phone = %s"
        params.append(new_phone)

    if new_name is not None:
        sql += " SET user_name = %s"
        params.append(new_name)

    sql += " WHERE phone = %s"

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                cur.execute(sql, tuple(params))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count


if __name__ == "__main__":
    update(1, "Zhenis")
