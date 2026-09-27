# A Program to use yield from with generators

def first_numbers():
    yield 1
    yield 2
    yield 3


def second_numbers():
    yield 4
    yield 5
    yield 6


def all_numbers():
    yield from first_numbers()
    yield from second_numbers()


for number in all_numbers():
    print(number)


# Explanation:
# The yield from statement is used to delegate part of a generator's work to another iterable or generator.
# The first_numbers() generator produces 1, 2, and 3.
# The second_numbers() generator produces 4, 5, and 6.
# The all_numbers() generator uses yield from to receive values from both generators and produce them as one sequence.
# This allows multiple generators to be combined without manually writing a separate yield statement for every value.

# Real-Life Use:
# yield from is useful when a large generator is divided into smaller generators that each handle a specific part of a task.