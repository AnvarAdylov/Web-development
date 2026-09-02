
def invert_list(list_of_numbers):
    for i in range (len(list_of_numbers)):
        list_of_numbers[i] = list_of_numbers[i]*(-1)
    return list_of_numbers
'''
Написать функцию, которая будет принимать в качестве аргумента элемент списка чисел и возвращать число с противоположным знаком. С помощью этой функции необходимо поменять знаки на противоположные у всех элементов этого списка. Вывести на экран оба списка - изначальный и результирующий

Пример работы программы: 
'''
list =  [1, -2, 5, 2.5, -4]
print("before invert: ", end = '')
print(list)
print("after invert: ", end = '')
print(invert_list(list))