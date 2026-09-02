
class Cart:
    def __init__(self, list):
        self.list = list

    def total_price(self):
        total = 0
        for item in self.list:
            total = total + item.total()
        return total

    def display(self):
        print('Name                    PPU   CNT     Price  Disc.')
        print('==================================================')
        for item in self.list:
            item.display()
        print('==================================================')
        print(f'Total                             = {self.total_price():7.2f}')
