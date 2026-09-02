import Task2
import random


class Bot(Task2.Player):
    def turn(self):
        opponent_field = self.search(self.field)
        while True:
            x = random.randint(0, self.field.size-1)
            y = random.randint(0, self.field.size-1)
            if [y, x] not in opponent_field:
                break
        print(f'я хожу координаты [{x}, {y}]')
        self.field.fill_cell(x, y, self.symbol)

    def search(self, field):
        filled = []
        for i in range(field.size):
            for j in range(field.size):
                if (field.gamefield[i][j] != '_'):
                    filled.append([i, j])
        return filled
