import turtle
# turtle.pu()
# turtle.setpos(turtle.xcor() -200, turtle.ycor() +100)
# turtle.pd()
# turtle.left(90)
# for i in range(4):
#     turtle.fd(200)
#     turtle.right(90)
#     turtle.fd(100)
# turtle.bgcolor("Black")



def teglalap(color, hossz, magassag):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(hossz)
        turtle.right(90)
        turtle.forward (magassag/2)
        turtle.right(90)
    turtle.end_fill()

def Ukrajna():
  magassag = turtle.window_height()/2
  hossz = magassag * 1.5

  turtle.pu()
  turtle.setposition(- hossz / 2, + magassag / 2)
  turtle.pd()
  teglalap("#005bbb", hossz, magassag)
  turtle.setposition(turtle.xcor(), turtle.ycor()- magassag / 2)
  teglalap("#ffd500", hossz, magassag)

  # turtle.pu()
  # turtle.setposition(0, - magassag / 2) 
  # turtle.rt(90)
  # turtle.fd(50)
  # turtle.pd()
  # turtle.write("Ukrajna", align="center", font=("Arial", 30,"normal"))
  turtle.hideturtle()
  turtle.pu()
  turtle.home()
  turtle.pd()