# func_py_generate_catalan_numbers.py
def func_py_generate_catalan_numbers(n):
    catalan_numbers = [1]
    for i in range(1, n):
        catalan_numbers.append(int(catalan_numbers[-1] * 2 * (2 * i - 1) / (i + 1)))
    return catalan_numbers

print(func_py_generate_catalan_numbers(10))
