import Task2
import Task3
import Task4
import sys


class Application:
    def __init__(self):
        deck = Task2.Deck()
        while True:
            deck.shuffle()
            hand = Task3.Hand()
            for i in range(0, 5):
                Application.run_out_of_cards(deck)
                hand.pick_card(deck)
            hand.display_cards()
            print('Хотите ли вы заменить карты?')
            print('Введите номера карт которые хотите заменить через пробел:')
            while True:
                try:
                    input_string = input('> ')
                    cards_list = input_string.split()
                    cards_list = Application.input_check(cards_list)
                    break
                except:
                    print("Неверный ввод попробуйте еще раз")
            for item in cards_list:
                Application.run_out_of_cards(deck)
                hand.swap(item-1, deck)
            hand.display_cards()
            checker = Task4.Checker(hand)
            checker.sort()
            checker.check()
            hand.display_cards()
            print('Хотите ли вы сыграть еще раз?')
            user_responce = input('> ')
            if user_responce.lower() == 'no' or user_responce.lower() == 'нет':
                print('wtf')
                sys.exit()
            else:
                pass

    @staticmethod
    def input_check(list):
        try:
            if len(list) > 5:
                raise Exception()
            swap_cards_list = []
            for i in range(0, len(list)):
                temp = int(list[i])
                if 0 < temp <= 5:
                    swap_cards_list.append(temp)
                else:
                    raise Exception()
        except:
            raise Exception
        return swap_cards_list

    @staticmethod
    def run_out_of_cards(deck):
        if len(deck.cards) == 0:
            print("Deck run out of cards!")
            sys.exit()
        else:
            pass
