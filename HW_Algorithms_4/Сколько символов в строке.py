s = input('Введите символ ')
str1 = input('Введие строку ')


def count_symbol(s, str1):
    sum_s = 0
    for i in str1:
        if i == s:
            sum_s += 1
    if sum_s == 0:
        return 'Нет такого'
    return sum_s

count_symbol(s, str1)
print(count_symbol(s, str1))
