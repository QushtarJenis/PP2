import psycopg2
from .config import load_config


def delete(phone=None, name=None):
    sql = "DELETE FROM contact WHERE "

    if phone is not None:
        sql += "phone = %s"
        params = (phone,)
    elif name is not None:
        sql += "user_name = %s"
        params = (name,)
    else:
        print("Missing parameter")
        return 0

    deleted_row_count = 0
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                deleted_row_count = cur.rowcount
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return deleted_row_count


if __name__ == "__main__":
    delete(phone="+77071234567")
