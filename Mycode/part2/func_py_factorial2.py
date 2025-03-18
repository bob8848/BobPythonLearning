# func_py_factorial.py

def func_py_factorial(n):
    return 1 if n == 0 else n * func_py_factorial(n - 1)

def test_factorial():
    print(f"Factorial of 5: {func_py_factorial(5)}")
    print(f"Factorial of 7: {func_py_factorial(7)}")

if __name__ == "__main__":
    test_factorial()
