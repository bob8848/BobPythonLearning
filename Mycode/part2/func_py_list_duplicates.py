# func_py_list_duplicates.py
def func_py_list_duplicates(lst):
    seen, duplicates = set(), set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)

print(func_py_list_duplicates([1, 2, 3, 4, 5, 3, 2, 6]))
