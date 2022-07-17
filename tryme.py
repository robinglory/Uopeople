import turtle
bob = turtle.Turtle()

# turtle.fd(100) #making square with simple method
# turtle.rt(90)
# turtle.fd(100)
# turtle.rt(90)
# turtle.fd(100)
# turtle.rt(90)
# turtle.fd(100)

# for i in range (4):
#     turtle.bk(200)
#     turtle.rt(90)
#Drawin turtle with loop

# def square(t):
#     for i in range(4):
#         t.bk(200)
#         t.rt(90)

# square(turtle)
#Function square with t parameter

# def square(t,length):
#     for i in range(6):
#         t.bk(length)
#         t.rt(60)

# square(turtle, 400)
#function with two parameter

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print(bob)

def polygon(t, length, n):
    
    for i in range(n):
        fd(t, length)
        lt(t, 360 / n)

polygon(bob, 50, 8)
wait_for_user()
turtle.mainloop()

