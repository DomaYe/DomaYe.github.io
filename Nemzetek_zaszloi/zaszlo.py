import turtle

def Franciaország():
  magassag = turtle.window_height()/2
  szelesseg = magassag * 1.5  
  turtle.pu()
  turtle.setpos(-szelesseg / 2, magassag / 2)
  turtle.pd()
  def tegla(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(2):
      turtle.fd(szelesseg /3)
      turtle.right(90)
      turtle.fd(magassag)
      turtle.right(90)    
    turtle.end_fill()

  tegla("#001e96")
  turtle.fd(szelesseg/3)
  tegla("#ffffff")
  turtle.fd(szelesseg/3)
  tegla("#Ee2436")
  turtle.fd(szelesseg/3)
  turtle.right(90)
  turtle.fd(magassag)
  turtle.right(90)
  turtle.fd(szelesseg/2)
  turtle.pu()
  # turtle.goto(turtle.xcor(), turtle.ycor()- 50 )
  # turtle.pd()
  # turtle.write("Franciaország", align="center", font= ("Arial",30,"normal"))
  turtle.pu()
  turtle.hideturtle()
  turtle.home()
