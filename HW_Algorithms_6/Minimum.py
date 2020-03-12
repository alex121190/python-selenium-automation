def minimum(array):
    min1 = array[0]
    min2 = array[0]
    for item in array:
        if item < min1:
            min1 = item
    if array.count(min1) > 1:
        min2 = min1
    array.remove(min1)
    for item in array:
        if item < min2:
            min2 = item
    return min1, min2

print(minimum([-1, -3, 0, 3, 5, -7]))