def average(list):
    sum = 0.0
    for i in range (len(list)):
        sum += list[i]
    return sum/len(list)
def is_allowed_input(input):
    try:
        float(input)
        return True
    except ValueError:
        return False
def maximum(list):
    max = list[0]
    for i in range (len(list)):
        if max < list[i]:
            max = list[i]
    return max
def minimum(list):   
    min = list[0]
    for i in range (len(list)):
        if min > list[i]:
            min = list[i]
    return min
list_of_ten = []
print("input 10 numbers:")
for i in range (10):
    while True:
        temp = input() 
        if (is_allowed_input(temp)):
            temp = float(temp) 
            break
        else:
            print("Ошибка неверный тип данных попробуйте еще раз")
    list_of_ten.append(temp)
print("input one of command : (avg, min, max):")
command = input()
if (command.lower == 'max'):
    #print("Heres the maximum number from list you provided:", end='')
    print(maximum(list_of_ten))
if (command.lower == 'min'):
    #print("Heres the minimum number from list you provided:", end='')
    print(minimum(list_of_ten))
if (command.lower == 'avg'):
    #print("Heres the average number from list you provided:", end='')
    print(average(list_of_ten))