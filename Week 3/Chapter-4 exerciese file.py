# def square(t):
#     print(t)
# #making square function
# import turtle
# bob = turtle.Turtle()
# #calling turtle module
# for i in range(4):
#     bob.fd(100)
#     bob.rt(90)
# #looping
# square(bob)#nesting loop into function
# #First exercies

# import turtle
# bob = turtle.Turtle()

# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.rt(90)

# square(bob, 150)
# turtle.mainloop()

 
num=int(input("Enter a number: "))

if num>0 and num%2==0:

    print(num, "is a positive even number")

elif num>0 and num%2 !=0:

    print(num, "is a positive odd number")

elif num<0 and num%2==0:

    print(num, "is a negative even number")

elif num<0 and num%2 !=0:

    print(num, "is a negative odd number")

else:

    print(num," is zero")