def compare(number1,number2):
    if number1>number2:
        print(">")
    elif number1<number2:
        print("<")
    else:
        print("=")

while True:
    print("Введите первое число:")
    a = int(input()) 
    print("Введите второе число:")
    b = int(input())
    compare(a,b)
    print("Введите y чтобы завершить программу")
    check = input()
    if check.lower() == "y":
        break