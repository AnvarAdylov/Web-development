import Task1
import random


class Deck:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["\u2660", "\u2665", "\u2666", "\u2663"]

    def __init__(self):
        self.cards = []
        for item_suit in self.SUITS:
            for item_rank in self.RANKS:
                self.cards.append(Task1.Card(item_rank, item_suit))

    def pick_card(self):
        taken_card = self.cards[-1]
        self.cards.pop(-1)
        return taken_card

    def shuffle(self):
        random.shuffle(self.cards)
