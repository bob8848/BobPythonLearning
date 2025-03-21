# fun_py_prime_check.py

def fun_py_prime_check(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_prime_check():
    numbers = [2, 3, 10, 17, 19, 25]
    for num in numbers:
        print(f"{num} is prime: {fun_py_prime_check(num)}")

if __name__ == "__main__":
    test_prime_check()
