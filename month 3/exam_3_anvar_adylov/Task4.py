class Checker:
    ROYAL_FLUSH = {"2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0,
                   "9": 0, "10": 1, "J": 1, "Q": 1, "K": 1, "A": 1}

    def __init__(self, hand):
        self.hand = hand

    def check(self):
        ranks = self.count_ranks()
        suits = self.count_suits()
        print(ranks)
        print(suits)
        done = False
        for key in ranks:
            if Checker.dupe_rank(self, key, 4):
                print("8 очков - Каре/четвёрка (four of a kind)")
                done = True
            elif Checker.dupe_rank(self, key, 3):
                for remaining_key in list(ranks)[list(ranks).index(key)+1:]:
                    if Checker.dupe_rank(self, remaining_key, 2):
                        print("7 очков - Фулл-хаус (full house)")
                        done = True
                        break
                print("4 очка - Тройка (three of a kind)")
                done = True
            elif Checker.dupe_rank(self, key, 2):
                for remaining_key in list(ranks)[list(ranks).index(key)+1:]:
                    if Checker.dupe_rank(self, remaining_key, 3):
                        print("7 очков - Фулл-хаус (full house)")
                        done = True
                        break
                    elif Checker.dupe_rank(self, remaining_key, 2):
                        print("3 очка- Две пары (two pairs)")
                        done = True
                        break
                if not done:
                    print("2 очка - Пара (pair)")
                    done = True
        for key in suits:
            if Checker.dupe_suit(self, key, 5):
                if ranks == Checker.ROYAL_FLUSH:
                    print("10 очков - Роял-флеш (royal flush)")
                    done = True
                elif Checker.five_in_row(self):
                    print("9 очков - Стрит-флеш (straight flush)")
                    done = True
                else:
                    print("6 очков - Флеш (flush)")
                    done = True
        if Checker.five_in_row(self):
            if not done:
                print("5 очка - Стрит (straight)")
                done = True
        if not done:
            print("1 очко - Старшая карта (high card)")

    def count_suits(self):
        suits = {"\u2660": 0, "\u2665": 0, "\u2666": 0, "\u2663": 0}
        for item in self.hand.cards_hand:
            suits[item.suit] += 1
        return suits

    def count_ranks(self):
        ranks = {"2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0,
                 "8": 0, "9": 0, "10": 0, "J": 0, "Q": 0, "K": 0, "A": 0}
        for item in self.hand.cards_hand:
            ranks[item.rank] += 1
        return ranks

    def dupe_suit(self, suit, amount):
        suits = self.count_suits()
        if suits[suit] == amount:
            return True
        else:
            return False

    def dupe_rank(self, rank, amount):
        ranks = self.count_ranks()
        if ranks[rank] == amount:
            return True
        else:
            return False

    def five_in_row(self):
        ranks = self.count_ranks()
        if ranks["A"] > 0:
            streak = 1
        else:
            streak = 0
        for item in ranks:
            if ranks[item] > 0:
                streak += 1
                if streak == 5:
                    return True
            else:
                streak = 0
        return False

    def sort(self):
        self.hand.cards_hand.sort(key=lambda x: x.value)
        for item_two in self.hand.cards_hand:
            if item_two.value == 2:
                for item_ace in self.hand.cards_hand:
                    if item_ace.value == 14:
                        temp = [item_ace]
                        self.hand.cards_hand.remove(item_ace)
                        self.hand.cards_hand = temp + self.hand.cards_hand
