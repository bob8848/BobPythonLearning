# func_py_generate_fibonacci_series.py
def func_py_generate_fibonacci_series(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

print(func_py_generate_fibonacci_series(10))
