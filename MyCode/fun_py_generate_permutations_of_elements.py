# fun_py_generate_permutations_of_elements.py
from itertools import permutations

def fun_py_generate_permutations_of_elements(lst):
    return list(permutations(lst))

print(fun_py_generate_permutations_of_elements([1, 2, 3]))
