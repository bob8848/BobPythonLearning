# fun_is_anagram.py
def fun_is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print(fun_is_anagram('listen', 'silent'))
print(fun_is_anagram('hello', 'world'))
