# A Program to chain multiple generators together

def first_group():
    for number in range(1, 4):
        yield number


def second_group():
    for number in range(4, 7):
        yield number


def chain_generators(*generators):
    for generator in generators:
        yield from generator


numbers = chain_generators(first_group(), second_group())

for number in numbers:
    print(number)


# Explanation:
# The chain_generators() function receives multiple generators as arguments.
# The outer for loop processes each generator one by one.
# yield from delegates the work of producing values to the current generator.
# After the first generator is exhausted, execution continues with the second generator.
# The result is a single generator that produces values from multiple generators in sequence.
# No complete combined list is created in memory.

# Real-Life Use:
# Generator chaining is useful when multiple data sources, files, streams, or processing stages need to be combined into one sequential data stream.