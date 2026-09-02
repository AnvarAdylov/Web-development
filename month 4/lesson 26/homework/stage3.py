def filling(*args):
    def decorator(func):
        def wrapper():
            for index, item in enumerate(args):
                if index == len(args) // 2:
                    func()
                print(f'~{item}~')
        return wrapper
    return decorator


def bread(func):
    def wrapper():
        print('</------\\>')
        func()
        print('<\\______/>')
    return wrapper


@bread
@filling("Салат", "Помидор", "Огурец", "лук")
def create_burger(food="--Котлета--"):
    print(food)


create_burger()
