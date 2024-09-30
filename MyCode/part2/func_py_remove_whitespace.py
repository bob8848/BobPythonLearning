# func_py_remove_whitespace.py
def func_py_remove_whitespace(s):
    result = ""
    for char in s:
        if char != " ":
            result += char
    return result
