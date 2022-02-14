import turtle
import random


def Luxemburg():
  #turtle.bgcolor("black")
  turtle.shape("turtle")
  #turtle.speed(0)

  #magassag = turtle.window_height()/3
  magassag = turtle.window_height()/2
  szelesseg = magassag * 1.667

  #turtle.setpos(turtle.xcor()-200 , turtle.ycor()-100)   relatív méretek!
  turtle.pu()
  turtle.setpos(-szelesseg/2 , -magassag/2)
  def teglalap(color):
      for _ in range(3):
          turtle.penup()
          turtle.fillcolor(color)
          turtle.pencolor(color)
          turtle.begin_fill()
          turtle.forward(szelesseg)
          turtle.left(90)
          turtle.forward(magassag / 3)
          turtle.left(90)
          turtle.end_fill()
  teglalap("#00a2df")
  turtle.setpos(turtle.xcor(), turtle.ycor() + magassag / 3)
  teglalap("#ffffff")
  turtle.setpos(turtle.xcor(), turtle.ycor() + magassag / 3)
  teglalap("#ee2436")

  turtle.forward(szelesseg/2)
  turtle.left(90)
  turtle.forward(magassag + 50)
  turtle.fillcolor("#ffffff")
  turtle.pencolor("black")
  #turtle.begin_fill()
  # turtle.write("Luxemburg", align="center", font=("Times New Roman", 30, "italic" , "normal"))
  #turtle.end_fill()
  turtle.pu()
  turtle.home()
  #turtle.pd()
  turtle.hideturtle()
