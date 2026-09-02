def is_allowed_input(input):
    try:
        float(input)
        return True
    except ValueError:
        return False
def relationship(max, min):  
    relationship = {
        'max_to_min': max/min,
        'min_to_max': min/max,
        'difference': max-min
        }
    return relationship
def max_and_min(number_one, number_two):
    if number_one >= number_two:
        return number_one, number_two
    else:
        return number_two, number_one
while True:
    print("Введите первое число:")
    first_input = input() 
    if (is_allowed_input(first_input)):
        first_input = float(first_input) 
        break
    else:
        print("Ошибка неверный тип данных попробуйте еще раз")
while True:
    print("Введите второе число:")
    second_input = input() 
    if (is_allowed_input(second_input)):
        second_input = float(second_input)
        break
    else:
        print("Ошибка неверный тип данныхб попробуйте еще раз")
max_number, min_number = max_and_min(first_input, second_input)

print("Max = %d" % max_number)
print("Min = %d" % min_number)
print("Max to Min = %.1f" % relationship(max_number, min_number)['max_to_min'])
print("Min to Max = %.1f" % relationship(max_number, min_number)['min_to_max'])
print("Difference = %d" % relationship(max_number, min_number)['difference'])
