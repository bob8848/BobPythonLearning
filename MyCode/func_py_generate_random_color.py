# func_py_generate_random_color.py
import random

def func_py_generate_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

print(func_py_generate_random_color())
