# fun_py_is_palindrome.py

def fun_py_is_palindrome(s):
    return s == s[::-1]

def test_is_palindrome():
    text = "racecar"
    print(f"Is '{text}' a palindrome? {fun_py_is_palindrome(text)}")

if __name__ == "__main__":
    test_is_palindrome()
