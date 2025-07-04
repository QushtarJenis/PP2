import sys
from db.insert import insert
from db.create_tables import create_tables
from db.update import update
from db.select import get_all_many
from db.delete import delete


# ---------------------------------------------------------------------------
# Insert
# ---------------------------------------------------------------------------
def insert_from_console():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    insert(name, phone)


# ---------------------------------------------------------------------------
# Update
# ---------------------------------------------------------------------------
def update_contact():
    phone = input("Current phone: ").strip()

    new_name = input("new name: ").strip() or None
    new_phone = input("new phone: ").strip() or None
    row_count = update(phone, new_phone=new_phone, new_name=new_name)
    print(f"Affected {row_count} row")


# ---------------------------------------------------------------------------
# Delete
# ---------------------------------------------------------------------------
def delete_contact():
    mode = input("Delete by [name|phone]: ").strip()
    value = input("Value: ").strip()
    if mode == "name":
        row_count = delete(phone=value)
    else:
        row_count = delete(name=value)
    print(f"Affected {row_count} row")


# ---------------------------------------------------------------------------
# Command loop
# ---------------------------------------------------------------------------
MENU = {
    "create": create_tables,
    "add": insert_from_console,
    "update": update_contact,
    "select": get_all_many,
    "delete": delete_contact,
    "exit": lambda: sys.exit(0),
}


def main():
    create_tables()
    while True:
        cmd = (
            input("\nchoose [create/add/update/select/delete/exit] ➜ ").strip().lower()
        )
        action = MENU.get(cmd)
        if action:
            try:
                action()
            except Exception as exc:
                print("Error:", exc)
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
