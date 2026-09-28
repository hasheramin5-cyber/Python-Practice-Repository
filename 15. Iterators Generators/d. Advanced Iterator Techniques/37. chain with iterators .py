# A Program to combine multiple iterators using chain()

from itertools import chain


first = iter([1, 2, 3])
second = iter([4, 5, 6])
third = iter([7, 8, 9])

combined = chain(first, second, third)

for number in combined:
    print(number)


# Explanation:
# chain() from itertools combines multiple iterables into one continuous iterator.
# The first, second, and third variables are separate iterators.
# chain() processes the first iterator completely.
# After the first iterator is exhausted, it moves to the second iterator and then the third iterator.
# The values are produced sequentially without creating a new combined list.

# Real-Life Use:
# chain() is useful when data is divided across multiple collections, files, batches, or streams but needs to be processed as one sequence.