# func_py_generate_pentagonal_numbers.py
def func_py_generate_pentagonal_numbers(limit):
    pentagonal_numbers = [n * (3 * n - 1) // 2 for n in range(1, limit + 1)]
    return pentagonal_numbers

print(func_py_generate_pentagonal_numbers(10))
