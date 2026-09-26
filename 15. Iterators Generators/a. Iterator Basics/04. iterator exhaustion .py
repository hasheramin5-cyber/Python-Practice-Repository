# A Program to understand iterator exhaustion

numbers = [1, 2, 3]

numbers_iterator = iter(numbers)

print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))

try:
    print(next(numbers_iterator))
except StopIteration:
    print("Iterator has been exhausted.")


# Explanation:
# The iterator contains three values.
# The first three next() calls successfully retrieve 1, 2, and 3.
# After the third value has been returned, there are no values remaining in the iterator.
# Calling next() again raises the StopIteration exception.
# StopIteration is Python's way of telling the program that an iterator has reached its end.
# The try-except block catches this exception so the program can continue running normally.

# Real-Life Use:
# StopIteration is important when building systems that process data sequentially until no data remains.