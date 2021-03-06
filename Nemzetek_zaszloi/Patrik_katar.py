import turtle
#turtle.bgcolor("#555555")
turtle.speed(7)

turtle.setup(750,300)
turtle.pu()
turtle.goto(-(turtle.window_width()/3)/2,turtle.ycor()-turtle.window_height()/4)
turtle.pd()

def Katar():
  height = turtle.window_height()/2
  for i in range(2):
    turtle.fillcolor("#8c0c34")
    turtle.begin_fill()
    turtle.fd(turtle.window_width()- turtle.window_width()/3)
    turtle.lt(90)
    turtle.fd(turtle.window_height()/2)
    turtle.lt(90)
    turtle.end_fill()
  for i in range(9):
    turtle.fillcolor("#ffffff")
    turtle.begin_fill()
    turtle.setheading(20)
    #turtle.fd(24)
    turtle.fd(height / 9)
    turtle.setheading(160)
    #turtle.fd(24)
    turtle.fd(24)
    turtle.end_fill()
  turtle.setheading(180)
  turtle.setpos(turtle.xcor(),turtle.ycor()+2.5)
  turtle.begin_fill()
  turtle.fd(turtle.window_width()/3)
  turtle.lt(90)
  turtle.fd(turtle.window_height()/2)
  turtle.lt(90)
  turtle.fd(turtle.window_width()/3)
  turtle.lt(90)
  turtle.color("#ffffff")
  turtle.fd(turtle.window_height()/2)
  turtle.end_fill()
  turtle.color("#ffffff")
  turtle.pu()
  turtle.goto(-turtle.window_width()/15,-turtle.window_height()/2.5)
  turtle.write("Katar",font = ("Arial", 20, "bold"))
  turtle.hideturtle()
  turtle.home()