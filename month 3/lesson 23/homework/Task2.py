import Task1


class DiscountGood(Task1.Good):
    def __init__(self, name, price, amount, discount):
        super().__init__(name, price, amount)
        if not (0 <= discount <= 99):
            raise ValueError("Discount percentage must be between 0 and 99.")
        self.discount = discount

    def total(self):
        return super().total()*((100-self.discount)/100)

    def display(self):
        print(f'{self.name[:20]:20} '
              f'{self.price:7.2f} *{self.amount:3} = '
              f'{self.total():7.2f} (-{self.discount}%)')
