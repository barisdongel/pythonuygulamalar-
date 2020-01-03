import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(2)
def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color("pink","red")

turtle.left(140)
turtle.forward(111.65)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.hideturtle()

turtle.getscreen()._root.mainloop()