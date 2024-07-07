# fun_find_median.py
def fun_find_median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n//2] + s[-(n+1)//2]) / 2

print(fun_find_median([3, 1, 4, 1, 5, 9, 2, 6, 5]))
