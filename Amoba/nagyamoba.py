
def feltolt(n):
    lista = []
    for i in range(n):
        sor = []
        for j in range(n):
            sor.append('.')
        lista.append(sor)
    return lista

def kirajzol(lista):
  for sor in lista:
    for cella in sor:
        print(cella, end=' ')
    print()

def nyert(lista, jatekos):    
  for sor in lista:
    szamlalo = 0
    for cella in sor:
      if cella == jatekos["szimbolum"]:
        szamlalo += 1            
    if szamlalo == 3:
      return True
  for i in range(len(lista)):
    szamlalo = 0
    for j in range(len(lista)):
      if lista[j][i] == jatekos["szimbolum"]:
        szamlalo += 1
    if szamlalo == 3:
      return True
  szamlalo = 0    
  for i in range(len(lista)):    
    if lista[i][i] == jatekos["szimbolum"]:
      szamlalo += 1
  if szamlalo == 3:
    return True
  szamlalo = 0  
  for i in range(len(lista)):    
    if lista[i][-i-1] == jatekos["szimbolum"]:
      szamlalo += 1
  if szamlalo == 3:
    return True
  return False

def elfogyott(lista):
  for sor in lista:
    if '.' in sor:
      return False
  return True

def feltolt(n):
    lista = []
    for i in range(n):
        sor = []
        for j in range(n):
            sor.append('.')
        lista.append(sor)
    return lista

#palya=[['.','.','.'],['.','.','.'],['.','.','.']]

n = 10
palya = feltolt(n)

def nyert_sor(sorlista, jatekos, oszlop):
    szamol = 1
    col = oszlop - 1
    while col >= 0 and sorlista[oszlop -1] == jatekos["szinbolum"]:
      szamol += 1 
      col += 1
    while col < len (sorlista) and sorlista[col] == jatekos["szimbolum"]:
      szamol += 1
      col += 1
    return szamol == 5


def nyert_oszlop(palya, jatekos, sor, oszlop):
  szamol = 1
  row = sor - 1
  while row >= 0 and palya[row][oszlop] == jatekos["szimbolum"]:
    szamol += 1
    row -= 1
  row = sor + 1
  while row < len(palya) and palya[row][oszlop] == jatekos("szimbolum"):
    szamol += 1 
    row += 1

  return szamol == 5

def lef(palya, jatekos, sor, oszlop):
  szamol = 1
  col = oszlop - 1
  row = sor - 1
  while col <= 0 and row >= 0 and palya[row] == jatekos["szimbolum"]:
    szamol += 1
    col -= 1
    row -= 1
  while col <= len(palya) and row < len(palya) and palya[row] == jatekos["szimbolum"]:
    szamol += 1
    col -= 1
    row -= 1



print("Am??ba (by:Szeszko egyetem)")
print("A megadott ??rt??kek, csak '0' ??s '2' k??z??tt ??rv??nyesek sorban ??s oszlopban is")
player_x=input("Add meg az 1. j??t??kos nev??t: ")
player_o=input("Add meg a 2. j??t??kos nev??t: ")
kirajzol(palya)
print(player_x,", a szimb??lumod a(z) 'x'",sep='')
print(player_o,", a szimb??lumod a(z) 'o'",sep='')

jatekosok = [{'nev': player_x, "szimbolum": "x"}, {'nev': player_o, "szimbolum": "o"}]
vege=False
while not vege:
  for jatekos in jatekosok:
    print(jatekos["nev"], ", te k??vetkezel!",sep='')
    beker_sor=int(input('sor: ')) - 1
    beker_oszlop=int(input('oszlop: ')) - 1
    while beker_sor < 0 or beker_sor > len(palya) - 1 or beker_oszlop < 0 or beker_oszlop > len(palya) - 1 or palya[beker_sor][beker_oszlop] != ".":
      print("ervenytelen koordinata")
      beker_sor=int(input('sor: ')) - 1         
      beker_oszlop=int(input('oszlop: ')) - 1
    palya[beker_sor][beker_oszlop]=jatekos["szimbolum"]
    kirajzol(palya)

    if nyert(palya, jatekos):
      gyoztes = jatekos
      vege = True
      break

    if elfogyott(palya):
        gyoztes ={}
        vege = True
        break
    
    # gyoztes = kiertekel(palya, jatekos) 
    # if gyoztes:            
    #     vege = True
    #     break
if gyoztes: 
  print(gyoztes["nev"], "nyertel") 
else:
  print("Elfogytak a mez??k, d??ntetlen!")       

      