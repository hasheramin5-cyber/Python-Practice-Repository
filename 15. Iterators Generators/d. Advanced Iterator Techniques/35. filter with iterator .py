# A Program to filter iterator values using filter()

def numbers():
    for number in range(1, 11):
        yield number


number_iterator = numbers()

even_numbers = filter(lambda number: number % 2 == 0, number_iterator)

for number in even_numbers:
    print(number)


# Explanation:
# filter() selects values from an iterable based on a condition.
# The numbers() generator produces values from 1 to 10.
# filter() checks every value using the lambda condition.
# Only values for which the condition returns True are produced.
# filter() itself returns an iterator, which means values are processed lazily instead of creating a complete list immediately.

# Real-Life Use:
# filter() is useful when processing streams of records and only certain values need to continue through a data pipeline.