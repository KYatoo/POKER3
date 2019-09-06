class Card:
#花色和牌面 属性
    def __init__(self,huaSe,paiMian):
        self.huaSe = huaSe
        self.paiMian = paiMian

    def __str__(self):
        if self.paiMian == 1:
            paiMian = 'A'
        elif self.paiMian == 11:
            paiMian = 'J'
        elif self.paiMian == 12:
            paiMian = 'Q'
        elif self.paiMian == 13:
            paiMian = 'K'
        else:
            paiMian = str(self.paiMian)
        return self.huaSe + paiMian
