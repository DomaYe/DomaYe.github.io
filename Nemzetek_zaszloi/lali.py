import turtle

a = 0
b = turtle.window_height() / 2

def teglalap(aa, bb):
    for _ in range(2):
        turtle.fd(aa)
        turtle.lt(90)
        turtle.fd(bb)
        turtle.lt(90)

def Magyarország():
  b = turtle.window_height()/2
  a = b * 2
  turtle.pu()
  turtle.goto(-a / 2, -b / 2)
  turtle.pd()

  # zold
  turtle.fillcolor("green")
  turtle.begin_fill()
  teglalap(a, b / 3)
  turtle.end_fill()

  # fehér
  turtle.goto(turtle.xcor(), turtle.ycor() + (b / 3))
  turtle.fillcolor("white")
  turtle.begin_fill()
  teglalap(a, b / 3)
  turtle.end_fill()

  # piros
  turtle.goto(turtle.xcor(), turtle.ycor() + (b / 3))
  turtle.fillcolor("red")
  turtle.begin_fill()
  teglalap(a, b / 3)
  turtle.end_fill()

  turtle.pu()
  turtle.goto(0, 0 - b / 2 - 50)
  turtle.pd()
  # turtle.write("Magyarország", align="center", font = ("Arial", 30, "normal"))

def Ausztria():
  b = turtle.window_height() / 2
  a = b * 1.5

  turtle.pu()
  turtle.goto(-a / 2, -b / 2)
  turtle.pd()

	# piros
  turtle.fillcolor("red")
  turtle.begin_fill()
  teglalap(a, b / 3)
  turtle.end_fill()

	#fehér
  turtle.goto(turtle.xcor(), turtle.ycor() + (b / 3))
  turtle.fillcolor("white")
  turtle.begin_fill()
  teglalap(a, b / 3)
  turtle.end_fill()

	#piros
  turtle.goto(turtle.xcor(), turtle.ycor() + (b / 3))
  turtle.fillcolor("red")
  turtle.begin_fill()
  teglalap(a, b / 3)
  turtle.end_fill()

  turtle.pu()
  turtle.goto(0, 0 - b / 2 - 50)
  turtle.pd()
  # turtle.write("Ausztria", align="center", font = ("Arial", 30, "normal"))

def Indonézia1():
  b = turtle.window_height() / 2
  a = b * 1.5

  turtle.pu()
  turtle.goto(0 - a / 2, 0 - b / 2)
  turtle.pd()

	# fehér
  turtle.fillcolor("white")
  turtle.begin_fill()
  teglalap(a, b / 2)
  turtle.end_fill()

	#piros
  turtle.goto(turtle.xcor(), turtle.ycor() + (b / 2))
  turtle.fillcolor("red")
  turtle.begin_fill()
  teglalap(a, b / 2)
  turtle.end_fill()

  turtle.pu()
  turtle.goto(0, 0 - b / 2 - 50)
  turtle.pd()
  # turtle.write("Indonézia", align="center", font = ("Arial", 30, "normal"))

def Japán():
  b = turtle.window_height() / 2
  a = b * 1.5

  turtle.pu()
  turtle.goto(-a / 2, -b/2)
  turtle.pd()

	# fehér
  turtle.fillcolor("white")
  turtle.begin_fill()
  teglalap(a, b)
  turtle.end_fill()
  turtle.pu()

	# piros kor
  turtle.goto(turtle.xcor() + a / 2, turtle.ycor() + b / 4)
  turtle.pd()
  turtle.fillcolor("red")
  turtle.begin_fill()
  turtle.circle(b / 4)
  turtle.end_fill()

  turtle.pu()
  turtle.goto(0, 0 - b / 2 - 50)
  turtle.pd()
  # turtle.write("Japán", align="center", font =("Arial", 30, "normal"))

def Csehország():
  b = turtle.window_height() / 2
  a = b * 1.5

  turtle.pu()
  turtle.goto(-a / 2, -b / 2)
  turtle.pd()

	# piros
  turtle.fillcolor("red")
  turtle.begin_fill()
  teglalap(a, b / 2)
  turtle.end_fill()

	# fehér
  turtle.goto(turtle.xcor(), turtle.ycor() + (b / 2))
  turtle.fillcolor("white")
  turtle.begin_fill()
  teglalap(a, b / 2)
  turtle.end_fill()

  turtle.goto(0 - a / 2, 0 - b / 2)

	# háromszög
  turtle.lt(45)
  turtle.fillcolor("#11457E")
  turtle.begin_fill()
  turtle.goto(turtle.xcor() + a / 2, turtle.ycor() + b / 2)
  turtle.goto(turtle.xcor() - a / 2, turtle.ycor() + b / 2)
  turtle.goto(0 - a / 2, 0 - b / 2)
  turtle.end_fill()

  turtle.pu()
  turtle.goto(0, 0 - b / 2 - 50)
  
  # turtle.write("Csehország", align="center", font = ("Arial", 30, "normal"))
  turtle.home()
  turtle.pd()

def Spanyolország():
  b = turtle.window_height() / 2
  a = b * 1.5

  turtle.pu()
  turtle.goto(-a / 2, -b / 2)
  turtle.pd()

	# piros
  turtle.fillcolor("red")
  turtle.begin_fill()
  teglalap(a, b / 4)
  turtle.end_fill()

	# narancssárga
  turtle.goto(turtle.xcor(), turtle.ycor() + (b / 4))
  turtle.fillcolor("orange")
  turtle.begin_fill()
  teglalap(a, b / 2)
  turtle.end_fill()

	# piros
  turtle.goto(turtle.xcor(), turtle.ycor() + (b / 2))
  turtle.fillcolor("red")
  turtle.begin_fill()
  teglalap(a, b / 4)
  turtle.end_fill()

  turtle.pu()
  turtle.goto(0, 0 - b / 2 - 50)
  turtle.pd()
  # turtle.write("Spanyoloszág", align="center", font = ("Arial", 30, "normal"))

def Madagaszkár():
  b = turtle.window_height() / 2
  a = b * 1.5

  turtle.pu()
  turtle.goto(-a / 2, -b / 2)
  turtle.pd()

	# zöldes szin
  turtle.fillcolor("#007E3A")
  turtle.begin_fill()
  teglalap(a, b / 2)
  turtle.end_fill()

	#narancssárgás szin
  turtle.fillcolor("#FC4032")
  turtle.goto(turtle.xcor(), turtle.ycor() + (b / 2))
  turtle.begin_fill()
  teglalap(a, b / 2)
  turtle.end_fill()

  turtle.goto(0 - a / 2, 0 - b / 2)

	#fehér
  turtle.fillcolor("white")
  turtle.begin_fill()
  teglalap(a / 3, b)
  turtle.end_fill()

  turtle.pu()
  turtle.goto(0, 0 - b / 2 - 50)
  turtle.pd()
  # turtle.write("Madagaszkár", align="center", font = ("Arial", 30, "normal"))