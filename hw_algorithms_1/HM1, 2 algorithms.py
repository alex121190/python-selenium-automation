# 1. Sum of positive
def positive_sum(arr):
    summ = 0
    for item in arr:
        if item >= 0:
            summ = item + summ
    return summ

# 2. Even or Odd
def even_or_odd(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"
