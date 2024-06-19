def count_vowels_and_consonants(s):
    vowels = 'aeiouAEIOU'
    num_vowels = 0
    num_consonants = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
    return num_vowels, num_consonants

def main():
    text = "Hello, World!"
    vowels, consonants = count_vowels_and_consonants(text)
    print(f"The text '{text}' contains {vowels} vowels and {consonants} consonants")

if __name__ == "__main__":
    main()
