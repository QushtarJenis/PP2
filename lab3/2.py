# class Converter:
#     def __init__(self,n):
#         self.n = n
#     def gram2ounce(self):
#         return self.n * 28.3495231
#     def fahrenheit2cel(self):
#         return (self.n - 32) * 5 / 9

# def chickensAndrabbits(head,leg):
#     for chicken in range(head):
#         rabbits = head -chicken
#         if(2*chicken+4*rabbits)==leg:
#          return rabbits,chicken

# rabbits,chickens=chickensAndrabbits(35,94)
# print(rabbits)
# print(chickens)
# print("----------------------Tasks---------------------------")
# import math
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(math.sqrt(num))+1):
#         if num % i == 0:
#             return False
#     return True
# def filter_prime(numbers):
#     numlist =[]
#     for num in numbers:
#         if (is_prime(num)):
#             numlist.append(num)
#     return numlist
# input_str = input("")
# numbers = [int(num) for num in input_str.split()]
# result = filter_prime(numbers)
# for prime in result:
#  print(prime,end=' ')
# print("----------------------Tasks---------------------------")
# from itertools import permutations
# def print_permutations(input_str):
#     perms = permutations(input_str)
#     for perm in perms:
#        s= (''.join(perm))
#     return s

# user_input = input()
# print((print_permutations(user_input)))
# print("----------------------Tasks---------------------------")
# from itertools import permutations

# def print_permutations(input_str):
#     perms = permutations(input_str)

#     for perm in perms:
#        s= (''.join(perm))
#     return s

# _input = input()
# print(_input," => ",(print_permutations(_input)))
# print("----------------------Tasks---------------------------")
# def has_33(nums):
#     for i in range(len(nums)):
#         if(int(nums[i])==3):
#             if(nums[i+1]):
#               return True
#     return False
# nums =input().split(" ")
# print(has_33(nums))
# print("----------------------Tasks---------------------------")
# def has_007(nums):
#   positions =0
#   for num in nums:
#         n = int(num)
#         if n==0 and positions==0:
#             positions+=1
#         elif n==0 and positions==1:
#             positions+=1
#         elif n==7 and positions==2:
#             return True
#   return False
# nums =input().split(" ")
# print(has_007(nums))
# print("----------------------Tasks---------------------------")

# def AreaOfSphere(radius):
#     pi = 3.14259
#     return 4/3*pi*radius**3

# print(AreaOfSphere(3))
# print("----------------------Tasks---------------------------")
# def uniqueNumbers(nums):
#     uniqueNumbers = []
#     for num in nums:
#         n =int(num)
#         if n  not in uniqueNumbers:
#              uniqueNumbers.append(n)
#     return uniqueNumbers

# nums = input().split(" ")
# print(uniqueNumbers(nums))
# print("----------------------Tasks---------------------------")
# def is_palindrome(s):
#     reversed = ""
#     a =len(s)
#     for i in range(len(s)-1):
#         reversed += s[a-i-1]
#     return reversed

# s = input()
# a=s
# b=is_palindrome(s)
# if a==b:
#     print("palindrome")
# else:
#     print("not palindrome")
# print("----------------------Tasks---------------------------")
# n = input().split(" ")
# for i in n:
#         print('*'*int(i),end=" ")
# print("----------------------Tasks---------------------------")
# import random
# randomNum = random.randint(1,20)
# n = input("Take a guess")
# if int(n) == randomNum:
#     print("Yes")
# else:
#     print("No")
# print("----------------------Tasks---------------------------")
    


        
    