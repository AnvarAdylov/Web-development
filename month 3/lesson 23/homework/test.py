import Task1
import Task2
import Task3

something = Task1.Good('door', 29.99)
something.display()

somethingelse = Task1.Good('door', 29.99, 6)
somethingelse.display()


entirelydifferent = Task2.DiscountGood('item', 399.99, 2, 40)
entirelydifferent.display()

goods = [
    Task1.Good('Bread', 17, 3),
    Task1.Good('Water', 19, 2),
    Task2.DiscountGood('Juice', 80, 1, 20),
    Task1.Good('Toilet Paper', 19, 10)
]

cart = Task3.Cart(goods)
cart.display()
