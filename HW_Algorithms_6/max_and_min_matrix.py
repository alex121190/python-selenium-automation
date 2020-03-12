def max_and_min(matrix):
    result = []
    for array in matrix:
        result.append(min(array))
    return max(result)

print(max_and_min([[1,2,3], [4,5,6], [8,7,9]]))