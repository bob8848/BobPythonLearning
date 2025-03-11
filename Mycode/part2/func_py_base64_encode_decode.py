# func_py_base64_encode_decode.py
import base64

def func_py_base64_encode_decode(text, encode=True):
    return base64.b64encode(text.encode()).decode() if encode else base64.b64decode(text).decode()

encoded = func_py_base64_encode_decode("Hello World")
print(encoded)
print(func_py_base64_encode_decode(encoded, encode=False))
