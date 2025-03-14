# func_py_armstrong_number.py

def func_py_armstrong_number(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def test_armstrong_number():
    numbers = [153, 9474, 9475, 407, 371]
    for num in numbers:
        print(f"{num} is an Armstrong number: {func_py_armstrong_number(num)}")

if __name__ == "__main__":
    test_armstrong_number()
