import turtle
import time
#turtle.bgcolor("#555555")
turtle.speed(7)

def rectangle(a, b, color):
  turtle.fillcolor(color)
  turtle.begin_fill()
  for _ in range(2):
    turtle.fd(a)
    turtle.lt(90)
    turtle.fd(b)
    turtle.lt(90)
  turtle.end_fill()



def Kanada():
  #turtle.setup(600,600)
  ideal_height = 280   
  height = turtle.window_height() / 2
  rate = height / ideal_height
  width = height * 2
  turtle.pu()
  turtle.setpos(-width/2,-height/2)
  turtle.pd()
  rectangle(width/4, height, "#d52b1e")
  turtle.fd(width/4)
  rectangle(width/2, height, "#ffffff")
  turtle.fd(width/2)
  rectangle(width/4, height, "#d52b1e")

  turtle.pu()
  turtle.color("#d52b1e")
  turtle.setpos(0, -height/2 + 10)
  turtle.fillcolor("#d52b1e")
  turtle.pd()
  turtle.begin_fill()
  #turtle.lt(90)
  turtle.fd(10 * rate)
  turtle.lt(90)
  turtle.fd(75 * rate)
  turtle.rt(100)
  turtle.fd(75 * rate)  
  turtle.lt(130)
  turtle.fd(30 * rate)
  turtle.rt(90)

  turtle.fd(82.5 * rate)
  turtle.lt(140)
  turtle.fd(30 * rate)
  turtle.rt(115)
  turtle.fd(45 * rate)
  turtle.lt(130)
  turtle.fd(45 * rate)
  turtle.rt(115)
  turtle.fd(30 * rate)
  turtle.lt(140)
  turtle.fd(75 * rate)
  turtle.rt(120)

  turtle.fd(67.5 * rate)
  turtle.lt(140)
  turtle.fd(30 * rate)
  turtle.rt(115)
  turtle.fd(45 * rate)
  turtle.lt(130)
  turtle.fd(45 * rate)
  turtle.rt(115)
  turtle.fd(30 * rate)
  turtle.lt(140)
  turtle.fd(67.5 * rate)
  turtle.rt(120)

  turtle.fd(75 * rate)
  turtle.lt(140)
  turtle.fd(30 * rate)
  turtle.rt(115)
  turtle.fd(45 * rate)
  turtle.lt(130)
  turtle.fd(45 * rate)
  turtle.rt(115)
  turtle.fd(30 * rate)
  turtle.lt(143)
  turtle.fd(90 * rate)
  turtle.rt(90)

  turtle.fd(30 * rate)
  turtle.lt(127)
  turtle.fd(75 * rate)
  turtle.setheading(90*3)
  turtle.fd(75 * rate)
  turtle.lt(90)
  turtle.fd(10 * rate)
  turtle.end_fill()
  
  #turtle.color('black')
  #turtle.pu()
  #turtle.goto(-turtle.window_width()/15,-turtle.window_height()/2.5)
  #turtle.write("Kanada ",font = ("Arial", 30, "normal"))
  
  turtle.hideturtle()
  turtle.home()