# func_py_sum_of_odd_numbers.py
def func_py_sum_of_odd_numbers(lst):
    return sum(num for num in lst if num % 2 != 0)

print(func_py_sum_of_odd_numbers([1, 2, 3, 4, 5]))
