class TriangleChecker:
    def __init__(self,a,b,s):
        self.a = a
        self.b = b
        self.s = s
    def is_traingle(self):
     if(self.a<0 or self.b<0 or self.s<0):
        print("Negative numbers won't work!")
     if int(self.a) or int(self.b) or int(self.s):
         if self.a+self.b>self.s and self.a+self.s>self.b and self.b+self.s>self.a:
          print("Hooray, you can build a triangle!")
         else:print("It's a pity, but you can't make a triangle out of it.")
     else:
       print("You only need to enter numbers")
a = TriangleChecker(4,2,3)
a.is_traingle()