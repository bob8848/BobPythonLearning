# func_py_generate_repunits.py
def func_py_generate_repunits(n):
    return [int('1' * i) for i in range(1, n + 1)]

print(func_py_generate_repunits(10))
