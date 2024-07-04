# count_digits_letters.py
def count_digits_letters(s):
    digits = sum(c.isdigit() for c in s)
    letters = sum(c.isalpha() for c in s)
    return digits, letters

if __name__ == "__main__":
    s = input("Enter a string: ")
    digits, letters = count_digits_letters(s)
    print(f"Digits: {digits}, Letters: {letters}")
