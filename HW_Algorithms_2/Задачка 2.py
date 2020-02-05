number1 = int(input("Введите первое число "))
number2 = int(input("Введите второе число "))
number3 = int(input("Введите третье число "))

if number1 > number2 and number1 > number3:
    print("Самое большое число - " + str(number1))
elif number2 > number1 and number2 > number3:
    print("Самое большое число - " + str(number2))
else:
    print("Самое большое число - " + str(number3))

