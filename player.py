import  poke
import  handtype
import max

class Player:
    def __init__(self,name):
        self.name = name
        self.fapai()
        self.hand_type = handtype.handtype(self.pai)
        self.pai.sort(key = max.maxpoker, reverse = True)

    def fapai(self):
        p = poke.Poke()
        p.xipai()
        self.pai = p.faNpai(3)

if __name__ == "__main__":
    a = Player("test")
    p = a.pai
    print(*p)
    p.sort(key = max.maxpoker, reverse = True)
    print(*p)
