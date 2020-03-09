string = input(f"Введите строку ")

def longest(string):
    substring = ''
    result = ''
    count = 0
    maximum = 0
    for char in string + ' ':
        if char == ' ':
            if count > maximum:
                maximum = count
                result = substring
            count = 0
            substring = ''
        else:
            substring += char
            count += 1
    return result

print(longest(string))