import  poke
import  handtype

class Player:
    def __init__(self,name):
        self.name = name
        self.fapai()
        self.hand_type = handtype.handtype(self.pai)

    def fapai(self):
        p = poke.Poke()
        p.xipai()
        self.pai = p.faNpai(3)
