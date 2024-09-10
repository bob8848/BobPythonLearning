# func_py_find_sum_of_squares.py
def func_py_find_sum_of_squares(n):
    return sum(x ** 2 for x in range(1, n + 1))

print(func_py_find_sum_of_squares(5))
