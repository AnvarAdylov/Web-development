class Field:

    def __init__(self, size=3):
        self.size = size
        self.gamefield = [['_' for _ in range(self.size)]
                          for _ in range(self.size)]

    def fill_cell(self, x_coordinate, y_coordinate, player_symbol):
        if (x_coordinate < 0 or x_coordinate >= self.size or
                y_coordinate < 0 or y_coordinate >= self.size):
            raise ValueError
        else:
            if self.gamefield[y_coordinate][x_coordinate] == '_':
                self.gamefield[y_coordinate][x_coordinate] = player_symbol
            else:
                raise ValueError

    def display_field(self):
        for i in range(self.size + 1):
            for j in range(self.size + 1):
                if i == 0 and j == 0:
                    print(f'{' ':3}', end='')
                elif j == 0:
                    print(f'{i-1:3}', end='')
                elif i == 0:
                    print(f'{j-1:3}', end='')
                else:
                    print(f'{self.gamefield[i-1][j-1]:>3}', end='')
            print()
