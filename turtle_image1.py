import turtle


bob = turtle.Turtle()
bob.color("red", "yellow")
bob.speed(10) #to increase speed


bob.begin_fill()
for i in range(100):
    bob.forward(200)
    #bob.left(130)
    bob.left(168.5)

bob.end_fill()

turtle.done()