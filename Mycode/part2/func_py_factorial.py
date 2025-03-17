# func_py_factorial.py

def func_py_factorial(n):
    return 1 if n == 0 else n * func_py_factorial(n - 1)

def test_factorial():
    numbers = [5, 7, 10]
    for num in numbers:
        print(f"Factorial of {num}: {func_py_factorial(num)}")

if __name__ == "__main__":
    test_factorial()
