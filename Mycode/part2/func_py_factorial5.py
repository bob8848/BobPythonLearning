# func_py_factorial.py

def func_py_factorial(n):
    if n == 0:
        return 1
    return n * func_py_factorial(n - 1)

def test_factorial():
    print(f"Factorial of 5: {func_py_factorial(5)}")

if __name__ == "__main__":
    test_factorial()
