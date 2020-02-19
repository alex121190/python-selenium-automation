
n = int(input("Введите элемент ряда Фибоначи "))


def fibonacci(n):
    fib1 = 1
    if n < 0:
        print(f'Неверное значение')
        quit()
    elif n == 0:
        print(0)
    elif n == 1 or n == 2:
        print(fib1)
    else:
        fib2 = 1
        i = 0
        while i < n - 2:
            fib1, fib2 = fib2, fib1 + fib2
            i = i + 1
            if i == n - 2:
                print(fib2)

fibonacci(n)
