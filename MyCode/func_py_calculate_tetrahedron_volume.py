# func_py_calculate_tetrahedron_volume.py
import math

def func_py_calculate_tetrahedron_volume(edge_length):
    return (edge_length**3) / (6 * math.sqrt(2))

print(func_py_calculate_tetrahedron_volume(4))
