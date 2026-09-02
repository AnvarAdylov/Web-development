class Hand:
    def __init__(self):
        self.cards_hand = []

    def pick_card(self, deck):
        self.cards_hand.append(deck.pick_card())

    def display_cards(self):
        for i in range(len(self.cards_hand)):
            print(f'Карта {i+1}')
            self.cards_hand[i].display()

    def swap(self, number, deck):
        self.cards_hand[number] = deck.pick_card()
