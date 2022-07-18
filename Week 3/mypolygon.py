# import turtle
# bob = turtle.Turtle()
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)

# bob.bk(100)
# bob.rt(90)
# bob.fd(100)
# bob.lt(90)
# bob.bk(100)
# bob.rt(90)
# bob.fd(100)
# bob.lt(90)


# for i in range(4):
#  bob.fd(100)
#  bob.lt(90)

# print(bob)

# draw any polygon in turtle

import turtle

# creating turtle pen
t = turtle.Turtle()

# taking input for the no of the sides of the polygon
n = 50

# taking input for the length of the sides of the polygon
l = 4


for _ in range(n):
	turtle.forward(l)
	turtle.right(360 / n)
