import math
def split_version_one(number):
    for i in range (0,4):
        print(int(number[i])*(10**(3-i)))

def split_version_two(number):
    for i in range (0,4):
        temp = math.floor(int(number)/(10**(3-i)))
        print(temp*(10**(3-i)))
        number = int(number) - temp*(10**(3-i))


while True:
    print("Введите четырезхначное число от 1000 до 9999:")
    four_digits = input() 
    if int(four_digits) >= 1000 and int(four_digits) <= 9999:
        break
    else:
        print("Ошибка неверный ввод")


split_version_one(four_digits)
split_version_two(four_digits)