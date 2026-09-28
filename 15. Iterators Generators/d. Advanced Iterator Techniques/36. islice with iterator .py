# A Program to select part of an iterator using islice()

from itertools import islice


def numbers():
    for number in range(1, 101):
        yield number


number_iterator = numbers()

selected_numbers = islice(number_iterator, 10, 15)

for number in selected_numbers:
    print(number)


# Explanation:
# islice() from the itertools module allows part of an iterator to be selected without converting the entire iterator into a list.
# The numbers() generator can produce values from 1 to 100.
# islice() skips the first 10 values and then produces values until position 15.
# The selected values are generated only when the iterator is consumed.
# This is especially useful when working with large or potentially infinite iterators.

# Real-Life Use:
# islice() is useful for pagination, sampling, previewing data, and processing only a specific portion of a large data stream.