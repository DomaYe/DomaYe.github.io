import turtle as t

def Indonézia():  
  t.showturtle()
  #t.bgcolor('black')
  rovid = t.window_height() / 2
  hosszu = rovid * 1.5
  t.pu()
  t.setpos(-hosszu/2, 0)
  t.pd()  
  teglalap_also(hosszu, rovid / 2)
  teglalap_felso(hosszu, rovid / 2)
  #kiir(rovid/2 + 50, hosszu/2)
  t.pu()
  t.hideturtle()

def teglalap_also(hosszu, rovid):
  for _ in range(2):
    t.color('#ffffff')
    t.begin_fill()
    t.fd(hosszu)
    t.rt(90)
    t.fd(rovid)
    t.rt(90)
    t.end_fill()

def teglalap_felso(hosszu, rovid):
  for _ in range(2):
    t.color('#ff0000')
    t.begin_fill()
    t.fd(hosszu)
    t.lt(90)
    t.fd(rovid)
    t.lt(90)
    t.end_fill()

def kiir (oldal1, oldal2):
    t.pu()
    t.rt(90)
    t.fd(oldal1)
    t.lt(90)
    t.fd(oldal2)
    t.pd()
    t.pencolor('black')
    # t.write("Indonézia",  align="center",font=('Arial', 30, 'normal'))

  
