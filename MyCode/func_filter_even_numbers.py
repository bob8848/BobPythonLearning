# func_filter_even_numbers.py
def func_filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

print(func_filter_even_numbers([1, 2, 3, 4, 5, 6]))
