# func_find_subsets.py
from itertools import combinations

def func_find_subsets(lst):
    subsets = []
    for i in range(len(lst) + 1):
        for combo in combinations(lst, i):
            subsets.append(combo)
    return subsets

print(func_find_subsets([1, 2, 3]))
