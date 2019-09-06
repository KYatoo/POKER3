import  rule
import poke

class handtype:
    def __init__(self,hand):
        type = ["豹子","同花顺","同花","顺子","对子","单条"]
        self.hand = rule.poker3(hand)
        self.handtype()
        self.hhtype =type[self.htype]

    def handtype(self):
        if self.hand.baozi():
            self.htype = 0
        elif self.hand.tonghuashun():
            self.htype = 1
        elif self.hand.tonghua():
            self.htype = 2
        elif self.hand.shunzi():
            self.htype = 3
        elif self.hand.duizi():
            self.htype = 4
        else:
            self.htype = 5



