# func_py_check_prime.py
def func_py_check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(func_py_check_prime(17))
print(func_py_check_prime(16))
