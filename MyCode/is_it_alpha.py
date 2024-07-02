# is_alpha.py
def is_alpha(s):
    return s.isalpha()

if __name__ == "__main__":
    s = input("Enter a string: ")
    if is_alpha(s):
        print(f"{s} contains only alphabetic characters.")
    else:
        print(f"{s} contains non-alphabetic characters.")
