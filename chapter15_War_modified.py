### Chapter 15: 知識を１つにまとめる
# Warというカードゲームを作る。要素には、Card、Deck、Player、Game自体がある。
# 補章より；より良いコードにするために
import sys
from random import shuffle


# Card
class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None,
              "2", "3", "4", "5", "6", "7", "8", "9",
              "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        """スート（マーク）も値も整数値です"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True

        if self.value == c2.value:
            # if self.suit < c2.suit:
            #     return True
            # else:
            #     return False
            return self.suit < c2.suit
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True

        if self.value == c2.value:
            return self.suit > c2.suit
        #     if self.suit > c2.suit:
        #         return True
        #     else:
        #         return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " \
            + self.suits[self.suit]
        return v


# Deck
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    # def rm_card(self):
    def draw(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


# Player
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


# Game
def winner(p1, p2):
    if p1.wins > p2.wins:
        return p1.name
    if p1.wins < p2.wins:
        return p2.name
    return "引き分け！"


class Game:
    def __init__(self):
        name1 = input("プレーヤー1の名前 ")
        name2 = input("プレーヤー2の名前 ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    # def wins(self, winner):
    def print_winner(self, winner):
        w = "このラウンドは {} が勝ちました"
        # w = w.format(winner)
        # print(w)
        print(w.format(winner.name))

    # def draw(self, p1n, p1c, p2n, p2c):
    def print_draw(self, p1, p2):
        d = "{} は　{}、{} は　{}　を引きました"
        # d = d.format(p1n, p1c, p2n, p2c)
        # print(d)
        print(d.format(
            p1.name, p1.card, p2.name, p2.card
        ))

    def play_game(self):
        cards = self.deck.cards
        print("戦争を始めます!")
        while len(cards) >= 2:
            m = "qで終了、それ以外のキーでPlay:"
            response = input(m)
            if response == 'q':
                break
            # p1c = self.deck.rm_card()
            # p2c = self.deck.rm_card()
            # p1n = self.p1.name
            # p2n = self.p2.name
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            # self.draw(p1n, p1c, p2n, p2c)
            self.print_draw(self.p1, self.p2)
            # if p1c > p2c:
            #     self.p1.wins += 1
            #     self.wins(self.p1.name)
            # else:
            #     self.p2.wins += 1
            #     self.wins(self.p2.name)
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.print_winner(self.p1)
            else:
                self.p2.wins += 1
                self.print_winner(self.p2)

        win = winner(self.p1, self.p2)
        print("ゲーム終了、{}の勝利です！".format(win))


# Playing Game
game = Game()
game.play_game()
