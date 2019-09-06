import poke
import rule
import handtype
import player
import war

# while True:
# for j in range(50):
#     p = poke.Poke()
#     p.xipai()
#     pai = p.faNpai(3)
#     for i in pai:
#         print(i,end="\t")
#     a=handtype.handtype(pai)
#     print(a.htype)
#     print(a.hhtype)

while True:
    machine =player.Player("machine")
    name = input("请输入玩家姓名：")
    humen_player=player.Player(name)
    print(humen_player.name,"的手牌为：")
    for i in humen_player.pai:
        print(i,end="\t")
    print("您的手牌类型为：",humen_player.hand_type.hhtype)
    print( "\n电脑的手牌为：")
    for i in machine.pai:
        print(i,end="\t")
    print("电脑的手牌类型为：",machine.hand_type.hhtype)
    if war.fight(humen_player,machine):
        print(humen_player.name,"获胜")
    else:
        print("电脑获胜")
