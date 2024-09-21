# func_py_convert_to_binary.py
def func_py_convert_to_binary(num):
    return bin(num).replace("0b", "")

print(func_py_convert_to_binary(15))
