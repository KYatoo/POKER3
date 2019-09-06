import card
import random
class Poke:
    def __init__(self):
        self.cars = []
        hs = ['红心', '方片', '梅花', '黑桃']
        for i in hs:
            for j in range(1,14):
                self.cars.append(card.Card(i,j))

    def show(self):
        for i in self.cars:
            print(i,end="\t")
    def xipai(self):
        #洗牌
        random.shuffle(self.cars)
    def fapai(self):
        #发牌
        return self.cars.pop()
    def faNpai(self,num):
        pais = []
        for i in range(num):
            pais.append(self.fapai())
        return pais
