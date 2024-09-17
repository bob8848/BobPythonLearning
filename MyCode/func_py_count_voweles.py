# func_py_count_voweles.py
def func_py_count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(func_py_count_vowels("Python is fun"))
