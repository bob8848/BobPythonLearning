# func_py_find_perfect_numbers.py
def func_py_find_perfect_numbers(limit):
    perfect_numbers = []
    for num in range(2, limit):
        if sum([i for i in range(1, num) if num % i == 0]) == num:
            perfect_numbers.append(num)
    return perfect_numbers

print(func_py_find_perfect_numbers(10000))
