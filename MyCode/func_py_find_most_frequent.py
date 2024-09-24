# func_py_find_most_frequent.py
from collections import Counter

def func_py_find_most_frequent(numbers):
    return Counter(numbers).most_common(1)[0][0]

print(func_py_find_most_frequent([1, 2, 2, 3, 4, 4, 4, 5]))
