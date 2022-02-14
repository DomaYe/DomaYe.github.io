import turtle
def Bulgária():
  turtle.shape("turtle")
  #turtle.bgcolor("black")
  turtle.pen(fillcolor="white", pencolor="white", pensize=2)
  #turtle.speed(0)
  #turtle.penup()
  #turtle.setpos(turtle.xcor()-300, turtle.ycor() -220)
  #turtle.pendown()
  magassag = turtle.window_height()/2
  szelesseg = magassag * 1.5  

  def teglalap(m, color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range(2):
      turtle.fd(m*1.667)
      turtle.left(90)
      turtle.fd(m/3)
      turtle.left(90)
    turtle.end_fill()


  

  turtle.pu()
  turtle.setpos(- szelesseg / 2, -magassag / 2)
  turtle.pd()
  teglalap(magassag, "#d7210a")
  turtle.setpos(turtle.xcor(), turtle.ycor() + magassag / 3)
  teglalap(magassag, "#00976e")
  turtle.setpos(turtle.xcor(), turtle.ycor() + magassag / 3)
  teglalap(magassag, "white")
  # turtle.penup()
  # turtle.left(90)
  # turtle.forward(130)
  # turtle.pendown()
  # turtle.write("Nemzetek zászlói", align="center", font=("Arial", 8, "normal"))
  # turtle.left(180)  
  # turtle.penup()
  # turtle.forward(szelesseg/2)
  # turtle.right(90)
  # turtle.fd(magassag*2/3 + 50)
  # turtle.pendown()
  # turtle.pencolor('black')
  # turtle.write("Bulgária", align="center", font=("Arial", 30, "normal"))
  turtle.hideturtle()
  turtle.pu()
  turtle.home()




