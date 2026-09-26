# A Program to create an iterator using iter()

numbers = [10, 20, 30, 40]

numbers_iterator = iter(numbers)

print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))


# Explanation:
# A list is an iterable object, which means Python can retrieve its values one by one.
# The iter() function converts the list into an iterator.
# The returned iterator keeps track of its current position.
# Every time next() is called, the iterator returns the next available value and moves forward.

# In this example:
# First next() -> 10
# Second next() -> 20
# Third next() -> 30
# The value 40 has not been requested yet.

# Real-Life Use:
# Iterators are useful when values need to be processed one at a time instead of handling the complete collection.