import sys
import random
import Task1
import Task2
import Task3
import Task4


class Game:
    def __init__(self):
        self.field = None
        self.play_again = True
        while self.play_again:
            self.setup_game()
            self.play_again = self.play_again_prompt()

    def setup_game(self):
        size = self.choose_field_size()
        self.field = Task1.Field(size)
        print('Игра "Игрок против игрока" или "Игрок против бота"?')
        print('Введите "exit", чтобы выйти из игры.')
        print('Введите "игрок", чтобы играть против игрока.')
        print('Введите "бот", чтобы играть против бота.')
        play_mode = input('> ')

        if play_mode.lower() == 'exit':
            self.exit_game()

        if play_mode.lower() == 'игрок':
            print('Режим "Игрок против игрока" выбран.')
            self.play_mode = 'player_vs_player'
        elif play_mode.lower() == 'бот':
            print('Режим "Игрок против бота" выбран.')
            self.play_mode = 'player_vs_bot'
        else:
            print('Некорректный выбор.')
            print('Выберите "игрок против игрока" или "игрок против бота".')
            self.setup_game()

        self.play()

    def play(self):
        first_turn = random.choice(['player1', 'player2'])
        print(f'Первым ходит: {first_turn}')
        player1 = Task2.Player('X', self.field)
        checker = Task4.Checker(self.field)
        if self.play_mode == 'player_vs_bot':
            player2 = Task3.Bot('O', self.field)
        else:
            player2 = Task2.Player('O', self.field)
        while True:
            if first_turn == 'player1':
                self.field.display_field()
                print('Ход игрока 1')
                player1.turn()
                if len(self.field.gamefield) > 5:
                    if checker.check_segments():
                        print('Игрок 1 выиграл!')
                        break
                else:
                    if checker.did_i_win():
                        print('Игрок 1 выиграл!')
                        break
                print('Ход игрока 2')
                self.field.display_field()
                player2.turn()
                if len(self.field.gamefield) > 5:
                    if checker.check_segments():
                        print('Игрок 2 выиграл!')
                        break
                else:
                    if checker.did_i_win():
                        print('Игрок 2 выиграл!')
                        break
            else:
                self.field.display_field()
                print('Ход игрока 2')
                player2.turn()
                if len(self.field.gamefield) > 5:
                    if checker.check_segments():
                        print('Игрок 2 выиграл!')
                        break
                else:
                    if checker.did_i_win():
                        print('Игрок 2 выиграл!')
                        break
                self.field.display_field()
                print('Ход игрока 1')
                player1.turn()
                if len(self.field.gamefield) > 5:
                    if checker.check_segments():
                        print('Игрок 1 выиграл!')
                        break
                else:
                    if checker.did_i_win():
                        print('Игрок 1 выиграл!')
                        break

    def exit_game(self):
        print('Игра завершена.')
        sys.exit()

    def choose_field_size(self):
        while True:
            try:
                size = int(input('Введите размеры (минимум 3, максимум 10): '))
                if size < 3:
                    print('Размер поля должен быть не менее 3.')
                    continue
                if size > 10:
                    print('Размер поля должен быть не более 10.')
                    continue
                return size
            except ValueError:
                print('Некорректный ввод. Пожалуйста, введите целое число.')

    def play_again_prompt(self):
        while True:
            play_again = input('Хотите сыграть еще раз? (да/нет): ').lower()
            if play_again == 'да':
                return True
            elif play_again == 'нет':
                return False
            else:
                print('Некорректный ввод. Пожалуйста, введите "да" или "нет".')
