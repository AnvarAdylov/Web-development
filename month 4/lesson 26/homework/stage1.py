def bread(func):
    def wrapper():
        print('</------\\>')
        func()
        print('<\\______/>')
    return wrapper


@bread
def create_burger(food="--Котлета--"):
    print(food)


create_burger()
