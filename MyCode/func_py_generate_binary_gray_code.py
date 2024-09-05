# func_py_generate_binary_gray_code.py
def func_py_generate_binary_gray_code(n):
    if n == 1:
        return ['0', '1']
    prev_gray_code = func_py_generate_binary_gray_code(n - 1)
    return ['0' + code for code in prev_gray_code] + ['1' + code for code in reversed(prev_gray_code)]

print(func_py_generate_binary_gray_code(3))
