# def area(radius):
#     a = 3.142 * radius**2
#     return a

# area(8)

# def area(radius):
#     return 3.142 * radius**2

# print(area(8))

# def absolute_value(x):
#     if x<0:
#         return "negative"
#     if x>0:
#         return "postive"

# print(absolute_value(1))
# import math
# def distance(x1 , x2, y1, y2):
#     d1 = (x1 - x2) * (x1 - x2)
#     d2 = (y1 - y2) * (y1- y2)
#     real_d = math.sqrt(d1 + d2)
#     return real_d

# print(distance(8,2,3,6))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(9))

