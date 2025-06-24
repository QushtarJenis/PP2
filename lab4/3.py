import math

# 1
# def deg2rad(deg):
#     return math.pi * deg / 180


# print(deg2rad(15))


# 2
# def area_of_trapezoid(h, base1, base2):
#     return ((base1 + base2) * h) / 2


# h, base1, base2 = 5, 5, 6
# s = area_of_trapezoid(h, base1, base2)
# print(s)


# 3
# def area_of_regular_polygon(side_num, side_length):
#     return side_num * math.pow(side_length, 2) / (4 * math.tan(math.pi / side_num))
#     # (n * s² ) / (4 * tan(π/n))


# side_num = 4
# side_length = 25
# area = area_of_regular_polygon(side_num, side_length)
# print(area)


# 4
def area_of_parallelogram(base_length, height):
    return base_length * height


base_length = 5
height = 6
area = area_of_parallelogram(base_length, height)
print(area)
