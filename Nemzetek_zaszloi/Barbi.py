import turtle

def teglalap(aa, bb):
  for _ in range(2):
    turtle.fd(aa)
    turtle.lt(90)
    turtle.fd(bb)
    turtle.lt(90)

#def esztorszag(b): paraméter törölve
def Észtország():
  b = turtle.window_height() / 2
  a = b * 1.571
  turtle.pu()
  turtle.goto(-a / 2,-b / 2)
  turtle.pd()

  # fehér
  turtle.fillcolor("white")
  turtle.begin_fill()
  teglalap(a, b / 3)
  turtle.end_fill()

  # fekete
  turtle.goto(turtle.xcor(), turtle.ycor() + (b / 3))
  turtle.fillcolor("black")
  turtle.begin_fill()
  teglalap(a, b / 3)
  turtle.end_fill()

  # kék
  turtle.goto(turtle.xcor(), turtle.ycor() + (b / 3))
  turtle.fillcolor("blue")
  turtle.begin_fill()
  teglalap(a, b / 3)
  turtle.end_fill()
  
  # turtle.pu()
  # turtle.goto(0, 0 - b / 2 - 50)
  # turtle.pd()
  # turtle.write("Észtország", align="center", font = ("Arial", 30, "normal"))
  turtle.pu()
  turtle.home()
  turtle.ht()

# esztorszag(100) törölve

# turtle.done() törölve