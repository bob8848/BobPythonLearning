# func_py_find_largest_odd_number.py
def func_py_find_largest_odd_number(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    return max(odd_numbers) if odd_numbers else None

print(func_py_find_largest_odd_number([2, 4, 6, 7, 9, 10]))
