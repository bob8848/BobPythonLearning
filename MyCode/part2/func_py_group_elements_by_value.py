# func_py_group_elements_by_value.py
from collections import defaultdict

def func_py_group_elements_by_value(lst):
    grouped = defaultdict(list)
    for element in lst:
        grouped[element].append(element)
    return dict(grouped)
