# fun_count_upper_lower.py
def fun_count_upper_lower(string):
    upper_count = sum(1 for c in string if c.isupper())
    lower_count = sum(1 for c in string if c.islower())
    return upper_count, lower_count

print(fun_count_upper_lower("Hello World"))
