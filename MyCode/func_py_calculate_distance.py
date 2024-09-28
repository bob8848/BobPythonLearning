# func_py_calculate_distance.py
import math

def func_py_calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(func_py_calculate_distance(0, 0, 3, 4))
