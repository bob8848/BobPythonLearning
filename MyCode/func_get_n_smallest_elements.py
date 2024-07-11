# func_get_n_smallest_elements.py
def func_get_n_smallest_elements(lst, n):
    return sorted(lst)[:n]

print(func_get_n_smallest_elements([1, 3, 5, 2, 4, 6], 3))
