
def division_by(x, y):
    try:
        answer = x/y
        print('Результат: %.0f' % answer)
    except ZeroDivisionError:
        print('нельзя делить на ноль')


def input_number():
    while True:
        temp_number = input('> ')
        try:
            temp_number = int(temp_number)
            break
        except ValueError:
            print(temp_number + ' не является числом')
    return int(temp_number)


print('Введите x: ')
x = input_number()
print('Введите y: ')
y = input_number()
division_by(x, y)
