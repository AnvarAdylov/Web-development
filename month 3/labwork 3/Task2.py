class Player:
    def __init__(self, symbol, field):
        self.symbol = symbol
        self.field = field

    def turn(self):
        while True:
            try:
                print('Введите координату по горизонтали:')
                x = int(input('> '))
                print('Введите координату по вертикали:')
                y = int(input('> '))
                self.field.fill_cell(x, y, self.symbol)
                break
            except ValueError:
                print('Некорректная координата пожалуйста попробуйте еще раз')
