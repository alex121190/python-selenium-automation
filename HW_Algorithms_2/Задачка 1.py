from random import randint

digits = int(input("Введите разрядность числа "))


def sum_digits(digits):
    if digits < 1:
        print("Неверное значение, надо больше 1")
    else:
        down = 1 * 10 ** (digits - 1)
        up = (1 * 10 ** digits) - 1
        n = randint(down, up)
        print(f"Мы получили число {n}")
        result = 0
        i = 0
        while i < digits:
            result += n % 10
            n = n // 10
            i += 1

    return result
