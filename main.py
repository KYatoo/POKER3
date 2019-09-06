import poke
import rule
import handtype
import player

# a=p.fapai()
# print(a)
j=1
# while True:
# for i in range(50):
#     p = poke.Poke()
#     p.xipai()
#     pai = p.faNpai(3)
#     for i in pai:
#         print(i,end="\t")
#     a=handtype.Handtype(pai)
#     print(a.htype)
#     print(a.hhtype)
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
print("电脑的手牌类型为：",humen_player.hand_type.hhtype)