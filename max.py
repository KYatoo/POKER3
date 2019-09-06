import card
import player

def maxpoker(x:card.Card):
    hs = ['黑桃','梅花','方片','红心']
    hindex = hs.index(x.huaSe)
    pindex = (x.paiMian + 11) % 13
    # print(pindex, hindex)
    return [pindex, hindex]

if __name__ == "__main__":
    a = player.Player("test")
    p = a.pai
    print(*p)
    p.sort(key = maxpoker, reverse = True)
    print(*p)
