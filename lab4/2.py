# 1
# def squares_generator(n):
#     for i in range(n):
#         yield i**2


# for i in squares_generator(5):
#     print(i)


# 2
# def even_numbers_generator(n):
#     for i in range(n):
#         if i % 2 == 0:
#             yield i


# n = int(input())

# for i in even_numbers_generator(n):
#     print(i, end=",")


# 3
# def divisible_by_3_and_4_generator(n):
#     for i in range(n):
#         if i % 3 == 0 and i % 4 == 0:
#             yield i


# n = 100
# for i in divisible_by_3_and_4_generator(n):
#     print(i)


# 4
# def squares(a, b):
#     for i in range(a, b):
#         yield i**2


# a, b = 1, 7
# print("generater")
# for i in squares(a, b):
#     print(i)

# print("for loop")
# for i in range(a, b):
#     print(i**2)


# 5
def all_numbers(n):
    while n >= 0:
        yield n
        n -= 1


n = 5
for i in all_numbers(n):
    print(i)
