# A Program to create an iterator using itertools.count()

from itertools import count


counter = count(start=1, step=2)

for _ in range(5):
    print(next(counter))


# Explanation:
# count() creates an iterator that generates numbers continuously.
# The start argument defines the first value.
# The step argument defines how much the value changes after every iteration.
# In this example, the iterator starts at 1 and increases by 2 each time.
# count() can produce values indefinitely, so the for loop is used to request only five values.

# Real-Life Use:
# count() is useful for generating sequential identifiers, counters, event numbers, and repeated numeric sequences.