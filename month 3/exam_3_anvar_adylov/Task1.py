class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["\u2660", "\u2665", "\u2666", "\u2663"]

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise Exception('Not allowed rank')
        if suit not in self.SUITS:
            raise Exception('Not allowed suit')
        self.rank = rank
        self.suit = suit
        if rank == 'J':
            self.value = 11
        elif rank == 'Q':
            self.value = 12
        elif rank == 'K':
            self.value = 13
        elif rank == 'A':
            self.value = 14
        else:
            self.value = int(rank)
        if suit == "\u2660" or suit == "\u2663":
            self.color = 'black'
        elif suit == "\u2665" or suit == "\u2666":
            self.color = 'red'

    def display(self):
        face = f'{self.rank:<5}\n' + f'{self.suit:^5}\n' + f'{self.rank:>5}'
        print(face)
