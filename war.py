import  rule
import  handtype
import player
import card
import max

def fight(x:player.Player,y:player.Player):
    # print(x.hand_type.htype, y.hand_type.htype)
    if x.hand_type.htype < y.hand_type.htype:
        return True
    elif x.hand_type.htype > y.hand_type.htype:
        return False
    else:
        for i in range(3):
            if (x.pai[i].paiMian + 11)% 13 > (y.pai[i].paiMian + 11)%13:
                return True
            elif (x.pai[i].paiMian + 11)% 13 < (y.pai[i].paiMian + 11)%13:
                return  False
        if i == 2:
            for i in range(3):
                if x.pai[i].huaSe < y.pai[i].huaSe:
                    return True
                elif x.pai[i].huaSe > y.pai[i].huaSe:
                    return False
            if i == 2 and x.pai[i].paiMian == y.pai[i].paiMian:
                return True

if __name__ == "__main__":
    machine1 = player.Player("machine")
    machine1.pai = [card.Card('黑桃', 12), card.Card("红心", 1), card.Card('方片', 13)]
    machine1.hand_type = handtype.handtype(machine1.pai)
    machine1.pai.sort(key=max.maxpoker, reverse=True)
    machine2 = player.Player("machine2")
    machine2.pai = [card.Card('黑桃', 2), card.Card("红心", 2), card.Card('黑桃', 3)]
    machine2.hand_type = handtype.handtype(machine2.pai)
    machine2.pai.sort(key=max.maxpoker, reverse=True)
    print(*machine1.pai, *machine2.pai)
    if fight(machine1, machine2):
        print("machine1获胜")
    else:
        print("machine2获胜")