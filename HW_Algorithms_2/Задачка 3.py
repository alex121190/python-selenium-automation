number = int(input("Введите число "))

even = 0
odd = 0

while number > 0:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    number = number//10
print("Четных чисел - " + str(even) + " , а нечетных - " + str(odd))