# regex_tester.py
import re

def test_regex(pattern, text):
    matches = re.findall(pattern, text)
    return matches

pattern = r'\b\w{4}\b'
text = "This is a test text with some four-letter words."
print(test_regex(pattern, text))
