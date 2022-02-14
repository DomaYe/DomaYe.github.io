import tkinter as tk
import turtle
import random
import time
from doma import *
from krisztián import *
from lali import *
from Barbi import *
from Patrik_kanada import *
from Patrik_katar import *
from szabi import *
from tibor import *
from tundi import *
from zaszlo import *
from zsolti import *

def start():
  turtle.setup(width=1.0, height=1.0)
  turtle.Screen().bgcolor("#FAF0E6")
  turtle.color("#ddd")
  turtle.shape("turtle")
  iro = turtle.Turtle()
  iro.ht()
  iro.pu()
  iro.goto(0, turtle.Screen().window_height()/3)
  iro.color("black")
  iro.write("Nemzetek zászlói", False,align= "center", font=("Comic Sans MS", 30, "normal"))

def kiir(szoveg):
  iro = turtle.Turtle()
  iro.ht()
  iro.pu()
  iro.goto(0, -turtle.Screen().window_height()/4 - 50)
  iro.write(szoveg, False,align= "center", font=("Comic Sans MS", 26, "normal"))
  time.sleep(3)
  iro.clear()

lista = [Észtország, Luxemburg, Kanada, Indonézia, Lengyelország, Bulgária, Törökország, Franciaország, Magyarország, Ausztria, Csehország, Japán, Madagaszkár]

start()

for orszag in lista:
  turtle.st()
  turtle.color("#ddd")
  orszag()
  turtle.ht()
  kiir(orszag.__name__)
  turtle.clear()


iro = turtle.Turtle()
iro.ht()
iro.pu()
iro.goto(0, turtle.Screen().window_height()/3 - 30)
iro.color("black")
iro.write("Ez a zászló melyik országé?", False,align= "center", font=("Comic Sans MS", 20, "normal"))

elet = 3
pont = 0

while(elet > 0 and len(lista) > 0):
  valaszt = random.choice(lista)
  turtle.st()
  turtle.color("#ddd")
  valaszt()
  turtle.ht()
  tipp = turtle.textinput("Bekérés", "Add meg az ország nevét:")
  if tipp == valaszt.__name__:
    pont += 1
    kiir(f"Eltaláltad! Élet: {elet} Pont: {pont}")
    lista.remove(valaszt)
  else:
    elet -= 1
    if(pont > 0):
      pont -= 1
    kiir(f"Helytelen válasz Élet: {elet} Pont: {pont}")
  turtle.clear()

iro.clear()

if(len(lista) == 0):
  kiir("Gratulálok! Az összes zászlót kitaláltad!")
else:
  kiir("Játék vége! Elfogytak az életeid!")


