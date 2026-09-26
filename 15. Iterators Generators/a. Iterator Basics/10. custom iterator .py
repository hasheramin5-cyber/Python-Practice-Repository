# A Program to create a custom iterator

class CountUp:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


counter = CountUp(5)

for number in counter:
    print(number)


# Explanation:
# A custom iterator is created by defining a class that implements the iterator protocol.
# __iter__() returns the iterator object itself.
# __next__() controls what value should be returned next.
# The current attribute stores the iterator's state, while limit determines when iteration should stop.
# Each next() operation returns the current value and increases current by one.
# Once current becomes greater than limit, __next__() raises StopIteration, which tells the for loop that iteration is complete.

# Real-Life Use:
# Custom iterators are useful when a program needs to control how a sequence of values is generated.