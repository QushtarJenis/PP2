x = 3


def fnc():
    global x
    x = 5
    print(x)


print(x)
fnc()
print(x)
