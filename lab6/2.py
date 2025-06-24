# 1


# import math

# numbers = [1, 2, 3, 4, 5]
# print(math.prod(numbers))


# 2


# def cout_string(str):
#     upper_count = 0
#     lower_count = 0
#     for ch in str:
#         if ch.isupper():
#             upper_count += 1
#         elif ch.islower():
#             lower_count += 1
#     print("count of upper letters: ", upper_count)
#     print("count of lower letters: ", lower_count)


# str = "hELLO wORLD"
# cout_string(str)


# 3
# def check_palindrome(str):
#     if str == str[::-1]:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")


# check_palindrome("programmer")
# check_palindrome("programmeremmargorp")


# 4

# import time
# import math

# number = float(input())
# milliseconds = int(input())

# time.sleep(milliseconds / 1000)

# result = math.sqrt(number)

# print(f"Square root of {number} after {milliseconds} miliseconds is {result}")


# 5


tuple1 = (True, True, False)
tuple2 = (True, True, True)
tuple3 = (True, 1, "non-empty", [1], 3.14)
tuple4 = (True, 0, "abc")

print(all(tuple1))
print(all(tuple2))
print(all(tuple3))
print(all(tuple4))
