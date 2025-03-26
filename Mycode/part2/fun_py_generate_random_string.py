# fun_py_generate_random_string.py

import random
import string

def fun_py_generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def test_generate_random_string():
    print(f"Random string: {fun_py_generate_random_string(10)}")

if __name__ == "__main__":
    test_generate_random_string()
