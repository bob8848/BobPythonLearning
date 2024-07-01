# simple_counter.py
class Counter:
    def __init__(self, start=0):
        self.count = start

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count

if __name__ == "__main__":
    counter = Counter()
    counter.increment()
    counter.increment()
    counter.decrement()
    print(f"Current count: {counter.get_count()}")
    counter.reset()
    print(f"Count after reset: {counter.get_count()}")
