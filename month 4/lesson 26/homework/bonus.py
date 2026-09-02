def filling(filling):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for index, item in enumerate(filling):
                if index == len(filling) // 2:
                    func(*args, **kwargs)
                print(f'~{item}~')
        return wrapper
    return decorator


def bread(func):
    def wrapper(*args, **kwargs):
        print('</------\\>')
        func(*args, **kwargs)
        print('<\\______/>')
    return wrapper


class Burger:
    fill = ["Салат", "Помидор", "Огурец", "лук"]

    def __init__(self):
        pass

    def __str__(self):
        String = 'Начинка: '
        for item in self.fill:
            String = String + ' ' + item
        return String

    @bread
    @filling(fill)
    def create_burger(self, food="--Котлета--"):
        print(food)


Burger().create_burger("--КотлетЫ--")
