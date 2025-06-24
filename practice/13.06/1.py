list = [10, 20, 30, 40]

it = iter(list)
while True:
    try:
        print(next(it))
    except Exception:
        break
