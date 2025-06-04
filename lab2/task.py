# while
# 1. Write a program that outputs all even numbers from 2 to 20.
# i = 1
# n = 20
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# 2. Write a program that counts the sum of all the numbers from 1 to 50 that are divisible by 3.
# i = 1
# n = 50
# sum = 0
# while i <= n:
#     if i % 3 == 0:
#         sum += i
#     i += 1
# print(sum)

# 3. Ask the user for the password until they enter admin123.
# password = input("Password:")
# while password != "admin123":
#     print("Wrong password, please try again!")
#     password = input("Password:")
# print("Correct password!")

# For
# 1. Write a for loop that prints squares of numbers from 1 to 10.
# for i in range(1, 11):
#     print(i)

# 2. Create a list of 5 words and output the length of each word.
# list = ["kbtu", "python", "pp2", "task", "code"]
# for item in list:
#     print(len(item))

# 3. Use nested loops to output the multiplication table from 1 to 5.
# for i in range(0, 10):
#     for j in range(0, 10):
#         if i == 0:
#             if j == 0:
#                 print("x", end=" ")
#             else:
#                 print(j, end="|")
#         else:
#             if j == 0:
#                 print(i, end="|")
#             else:
#                 print(i * j, end="|")
#     print()

# List
# 1. Create a list of 5 numbers. Output: 1. the sum of all the numbers, 2. maximum and minimum values

# import random

# list = [random.randint(0, 100) for _ in range(5)]
# print(list)
# sum = 0
# maximum = None
# minimum = None
# for num in list:
#     if maximum == None:
#         maximum = num
#     if minimum == None:
#         minimum = num

#     if num > maximum:
#         maximum = num
#     if num < minimum:
#         minimum = num
#     sum += num
# print(sum)
# print(maximum)
# print(minimum)

# 2. A list of strings. Replace the second element with "updated" and display the final list.

# list = ["apple", "banana", "cherry", "date"]
# list[1] = "updated"
# print(list)

# 3. Create a list of 5 names. Print only those that start with the letter "A".
# list = ["Azamat", "Batyr", "Aidana", "Aizhan", "John"]
# for name in list:
#     if name.startswith("A"):
#         print(name)
