# fun_py_generate_random_numbers.py

import random

def fun_py_generate_random_numbers(n, start=1, end=100):
    return [random.randint(start, end) for _ in range(n)]

def test_generate_random_numbers():
    print(f"Random numbers: {fun_py_generate_random_numbers(5)}")

if __name__ == "__main__":
    test_generate_random_numbers()
