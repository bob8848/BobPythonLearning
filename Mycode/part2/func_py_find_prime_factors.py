# func_py_find_prime_factors.py

def func_py_find_prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors

def test_find_prime_factors():
    numbers = [56, 100, 121]
    for num in numbers:
        print(f"Prime factors of {num}: {func_py_find_prime_factors(num)}")

if __name__ == "__main__":
    test_find_prime_factors()
