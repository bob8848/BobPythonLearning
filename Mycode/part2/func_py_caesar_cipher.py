# func_py_caesar_cipher.py
def func_py_caesar_cipher(text, shift, encrypt=True):
    result = ""
    shift = shift if encrypt else -shift
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

print(func_py_caesar_cipher("Hello, World!", 3))
print(func_py_caesar_cipher("Khoor, Zruog!", 3, encrypt=False))
