# A Program to use enumerate() with an iterator

def numbers():
    for number in range(10, 15):
        yield number


number_iterator = numbers()

for index, number in enumerate(number_iterator, start=1):
    print(index, number)


# Explanation:
# enumerate() adds an index to values produced by an iterable.
# The numbers() function creates a generator that produces values from 10 to 14.
# enumerate() receives this generator and produces pairs containing the index and the current value.
# The start=1 argument makes the index begin from 1 instead of the default value 0.
# The generator still produces values lazily, so enumerate() does not need to create a complete list first.

# Real-Life Use:
# enumerate() with iterators is useful when processing records, files, logs, or streams where both the position and value are needed.