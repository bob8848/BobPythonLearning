# func_py_calculate_factorial_recursive.py
def func_py_calculate_factorial_recursive(n):
    return 1 if n == 0 else n * func_py_calculate_factorial_recursive(n - 1)

print(func_py_calculate_factorial_recursive(5))
