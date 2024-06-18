def count_frequency(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

def main():
    lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    frequency = count_frequency(lst)
    print(f"Element frequency in the list: {frequency}")

if __name__ == "__main__":
    main()
