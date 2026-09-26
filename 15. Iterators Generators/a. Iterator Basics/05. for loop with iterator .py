# A Program to use an iterator with a for loop

numbers = [10, 20, 30, 40]

numbers_iterator = iter(numbers)

for number in numbers_iterator:
    print(number)


# Explanation:
# The list is first converted into an iterator.
# The for loop repeatedly requests the next value from that iterator.
# Python internally calls next() for each iteration.
# When the iterator has no values left, it raises StopIteration internally.
# The for loop handles StopIteration automatically, so we do not need to write try-except ourselves.

# Real-Life Use:
# This is useful when processing collections sequentially while allowing Python to handle iterator termination.