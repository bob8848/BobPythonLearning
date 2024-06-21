# calculate_histogram.py
import matplotlib.pyplot as plt

def calculate_histogram(data):
    plt.hist(data, bins=10, alpha=0.75)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
calculate_histogram(data)
