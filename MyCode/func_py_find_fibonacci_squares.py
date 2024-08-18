# func_py_find_fibonacci_squares.py
def func_py_find_fibonacci_squares(n):
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return [x**2 for x in sequence]

print(func_py_find_fibonacci_squares(10))
