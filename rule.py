import poke
import card

class poker3:
    def __init__(self,hands):
        self.huaseset = set ([i.huaSe for i in hands])
        self.paiMianset = set([i.paiMian for i in hands])
        self.paiMianset = sorted(self.paiMianset)

    #是否同花
    def tonghua(self):
        if len(self.huaseset) == 1:
            return True
        return False

    #是否顺子
    def shunzi(self):
        if self.paiMianset[len(self.paiMianset)-1]-self.paiMianset[0] == 4 and len(self.paiMianset)==5:
            return True
        return False

    #同花顺
    def tonghuashun(self):
        if self.tonghua() == True and self.shunzi() == True:
            return True
        return False

    #是否豹子
    def baozi(self):
        if len(self.paiMianset) == 1:
            return True
        return False

    #是否对子
    def duizi(self):
        if len(self.paiMianset) == 2:
            return True
        return False
    