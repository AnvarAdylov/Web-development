def is_allowed_input(input):
    try:
        int(input)
        return True
    except ValueError:
        print("Ошибка неверный тип данных попробуйте еще раз")
        return False
def is_allowed_value(value):
    if int(value) < 0:
        print("Ошибка введена отрицательная длина пирамиды попробуйте еще раз")
        return False
    else: 
        return True
def pyramid(lineheight):
    print("Your pyramid sir") 
    for i in range (lineheight):
        temp = '*'
        for j in range (i):
            temp = temp + '**'
        print(temp.center(lineheight*2 - 1))    
while True:
        print("Input pyramid height: ")
        temporary_input = input() 
        if (is_allowed_input(temporary_input) and is_allowed_value(temporary_input)):
            pyramid_height = int(temporary_input) 
            break
pyramid(pyramid_height)