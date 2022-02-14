import turtle

def Törökország():
  turtle.shape("turtle")
  turtle.speed(5)  
  #turtle.goto(-500, 275)    
  rovid = turtle.window_height() / 2
  hosszu = rovid * 1.5
  turtle.pu()
  turtle.goto(-hosszu/2, rovid/2)
  turtle.pendown()

  turtle.color("white", "red")
  turtle.begin_fill()
  for n in range(2):
    turtle.forward(hosszu)
    turtle.right(90)
    turtle.forward(rovid)
    turtle.right(90)
  turtle.end_fill()

  turtle.penup()
  turtle.goto(-hosszu/10, 0)

  turtle.penup()
  turtle.backward(75/2)
  turtle.left(90)
  turtle.forward(125/2)
  turtle.left(90)
  turtle.pendown()

  turtle.color("red", "white")
  turtle.begin_fill()
  turtle.circle(127.5/2)
  turtle.end_fill()

  turtle.penup()
  turtle.goto(-87/2, 105.5/2)
  turtle.pendown()

  turtle.color("red", "red")
  turtle.begin_fill()
  turtle.circle(107/2)
  turtle.end_fill()

  turtle.penup()
  turtle.color("red", "white")
  turtle.goto(50/2 -8, -35/2 + 8)
  turtle.right(20)
  turtle.begin_fill()
  turtle.setheading(165) 
  for x in range(5):
    # turtle.forward(100/2)
    # turtle.right(144)    
    turtle.fd(50/3)
    turtle.rt(72) 
    turtle.fd(50/3)
    turtle.lt(144) 
  turtle.end_fill()

  

  turtle.penup()
  turtle.goto(350/2, -255/2)
  turtle.right(154)
  turtle.color("white", "white")
  turtle.goto(450/2, -350/2)

  turtle.pencolor("black")
  turtle.pu()
  turtle.goto(0, -rovid/2 -50)
  turtle.pd()
  # turtle.write("Törökország", align="center", font = ("Arial", 30, "normal"))
  turtle.pu()
  turtle.hideturtle()
  turtle.home()

#turtle.done()