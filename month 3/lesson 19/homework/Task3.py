def numbers_get(string):
    list_num = list(string.split(","))
    result = map(convert, list_num)
    return list(result)


def convert(x):
    return int(x)


def custom_function():
    print("Введите  последовательность чисел разделенную запятой:")
    string = input('> ')
    list_integers = numbers_get(string)
    return list_integers


something = custom_function()


print(something)
