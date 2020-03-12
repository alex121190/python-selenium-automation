def average_num(array):
    sum1 = 0
    result = []
    for item in array:
        sum1 += item
        average = sum1 / len(array)
    for item in array:
        if item < average:
            result.append(item)
    return result

print(average_num([3, 5, 6, 3, 2, 8]))