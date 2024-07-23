# fun_py_convert_tuple_to_dict.py
def fun_py_convert_tuple_to_dict(tpl):
    return {tpl[i]: tpl[i+1] for i in range(0, len(tpl), 2)}

print(fun_py_convert_tuple_to_dict(('a', 1, 'b', 2, 'c', 3)))
