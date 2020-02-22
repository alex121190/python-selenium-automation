s = input('Введите символ ')
str1 = input('Введие строку ')

def count_symbol(s, str1):
    sum_s = 0
    for i in str1:
        if i == s:
            sum_s += 1
    return 'Количество символов ' + s + ' в данной строке равно ' + str(sum_s)

count_symbol(s, str1)
print(count_symbol(s, str1))