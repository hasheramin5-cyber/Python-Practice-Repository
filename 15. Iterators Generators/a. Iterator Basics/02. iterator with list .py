# A Program to iterate through a list using an iterator

numbers = [10, 20, 30, 40, 50]

numbers_iterator = iter(numbers)

print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))


# Explanation:
# The list contains five values and is converted into an iterator using iter().
# The iterator remembers its current position.
# Each next() call retrieves the next value and advances the iterator to the following position.

# Therefore the values are returned in this order:
# 10 -> 20 -> 30 -> 40 -> 50
# Once a value has been returned, the iterator does not automatically go back to that value.

# Real-Life Use:
# Iterators can process large collections sequentially without manually managing an index.