# func_py_generate_random_string.py
import random
import string

def func_py_generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

print(func_py_generate_random_string(10))
