# class Test:
#     def __init__(self, input):
#         self.str = input
     
#     def getstring(self):
#         self.str = input()
        
#     def printString(self):
#         print(self.str.upper())
# t = Test("")
# t.getstring()
# t.printString()
print("----------------------Tasks---------------------------")
class Shape:
    def Area(self):
        print(self.area)
class Square(Shape):
    def __init__(self, input = 0):
        self.length = input
        self.area = self.length * self.length
    def Area(self):
        print(self.area)
class Rectangle(Shape):
    def __init__(self, input2=0,input1 = 0):
        self.length = input1
        self.width = input2
        self.area = self.length * self.width
shape = Square()
shape.Area()
shape = Rectangle(3,5)
shape.Area()
print("----------------------Tasks---------------------------")
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self, x, y):
        self.x += x
        self.y += y
    def distance(self,otherPoint):
        return ((self.x - otherPoint.x) ** 2 + (self.y - otherPoint.y) ** 2) ** 0.5

point1=Point(1,1)
point2=Point(2,2)
point1.show()
point2.show()
point1.move(3,3)
point2.move(3,3)
point1.show()
point2.show()
distance_between_points=point1.distance(point2)
print(distance_between_points)
print("----------------------Tasks---------------------------")
class Bank:
    def __init__(self,owner,balance=0):
        self.balance = balance
        self.owner = owner
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if(self.balance>=amount):
         self.balance -= amount
         print(f"New Balance:{self.balance}")
KaspiBank=Bank(owner="Talant",balance=50000)
KaspiBank.deposit(10000)
KaspiBank.withdraw(20000)
print("----------------------Tasks---------------------------")
class Mathematics:
    def is_prime(n):
        for i in range(2,9):
            if(n % i == 0 and n!=i):
                return False
        return True
Numbers =[1,2,3,4,144,6,7,8,96,10]

newList = list(filter(lambda x:Mathematics.is_prime(x),Numbers))
for i in newList:
    print(i)
print("----------------------Tasks---------------------------")
 
