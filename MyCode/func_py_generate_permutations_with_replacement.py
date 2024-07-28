# func_py_generate_permutations_with_replacement.py
from itertools import product

def func_py_generate_permutations_with_replacement(lst, r):
    return list(product(lst, repeat=r))

print(func_py_generate_permutations_with_replacement([1, 2, 3], 2))
