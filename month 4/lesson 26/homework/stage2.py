def filling(*args):
    def decorator(func):
        def wrapper():
            for item in args:
                print(f'~{item:^}~')
            func()
        return wrapper
    return decorator


def bread(func):
    def wrapper():
        print('</------\\>')
        func()
        print('<\\______/>')
    return wrapper


@bread
@filling("Салат", "Помидор", "Огурец")
def create_burger(food="--Котлета--"):
    print(food)


create_burger()
