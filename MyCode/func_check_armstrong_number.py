# func_check_armstrong_number.py
def func_check_armstrong_number(num):
    num_str = str(num)
    power = len(num_str)
    return num == sum(int(digit) ** power for digit in num_str)

print(func_check_armstrong_number(153))
print(func_check_armstrong_number(123))
