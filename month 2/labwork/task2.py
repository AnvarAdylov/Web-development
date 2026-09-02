def is_allowed_input(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

def is_triangle(side1,side2,side3):
    if (side1 >= side2 + side3 or side2 >= side1 + side3 or side3 >= side2 + side1):
        return "no"
    else:
        return "yes"
    
while True:
    print("Введите длину первой стороны:")
    a = int(input()) 
    if (is_allowed_input(a)):
        a = int(a) 
        break
    else:
        print("Ошибка неверный тип данных попробуйте еще раз")
while True:
    print("Введите длину второй стороны:")
    b = int(input())
    if (is_allowed_input(b)):
        b = int(b) 
        break
    else:
        print("Ошибка неверный тип данных попробуйте еще раз")
while True:
    print("Введите длину третьей стороны:")
    c = int(input()) 
    if (is_allowed_input(c)):
        c = int(c) 
        break
    else:
        print("Ошибка неверный тип данных попробуйте еще раз")

print(is_triangle(a,b,c))