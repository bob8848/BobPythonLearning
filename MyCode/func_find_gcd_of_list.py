# func_find_gcd_of_list.py
def func_find_gcd_of_list(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    gcd_value = lst[0]
    for num in lst[1:]:
        gcd_value = gcd(gcd_value, num)

    return gcd_value

print(func_find_gcd_of_list([24, 36, 48]))
