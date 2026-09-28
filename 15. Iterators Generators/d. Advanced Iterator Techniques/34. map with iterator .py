# A Program to transform iterator values using map()

def numbers():
    for number in range(1, 6):
        yield number


number_iterator = numbers()

squared_numbers = map(lambda number: number ** 2, number_iterator)

for number in squared_numbers:
    print(number)


# Explanation:
# map() applies a function to every value produced by an iterable.
# The numbers() generator produces values from 1 to 5.
# map() receives each value and applies the lambda function.
# The lambda calculates the square of the current number.
# map() returns an iterator, so the transformed values are generated only when they are requested.
# No separate list containing all squared values is created.

# Real-Life Use:
# map() is useful when values from an iterator need to be transformed before being processed by another operation.