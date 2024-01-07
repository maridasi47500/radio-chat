import random
class Spin:
  def __init__(self):
    self.jeu=["gagnant","gagnant","à 1 autre fois peut-être","gagnant","à bientôt","réessayez","vous avez perdu"]
    y=0
    z=0
    self.hey=[]
    self.nombres=[]
    a=int(360/(len(self.jeu)))
    for x in self.jeu:
       self.hey.append(y)
       self.nombres.append(z)
       y+=a
       z+=1
  def getmessage(self):
    hey=[]
    a=0
    for x in self.jeu:
       hey.append((x, self.hey[a]))
       a+=1
    return hey
  def spin(self):
    k=random.choice(self.nombres)
    r=self.hey[k]
    j=self.jeu[k]
    g=j == "gagnant"
    return {"rouetourne":r,"message":j,"gagnant": g}
   
