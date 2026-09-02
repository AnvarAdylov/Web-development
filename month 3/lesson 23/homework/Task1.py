
class Good:
    def __init__(self, name, price, amount=None):
        self.name = name
        self.price = price
        if amount is None:
            self.amount = 1
        else:
            self.amount = amount

    def total(self):
        return self.amount * self.price

    def display(self):
        print(f'{self.name[:20]:20} '
              f'{self.price:7.2f} *{self.amount:3} = {self.total():7.2f}')
