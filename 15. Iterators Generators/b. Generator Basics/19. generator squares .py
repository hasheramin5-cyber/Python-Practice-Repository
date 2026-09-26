# A Program to generate square numbers using a generator

def square_numbers(limit):
    for number in range(1, limit + 1):
        yield number ** 2


squares = square_numbers(5)

for square in squares:
    print(square)


# Explanation:
# The generator loops through numbers from 1 to the specified limit.
# For every number, number ** 2 calculates its square.
# yield immediately provides that square to the caller and pauses execution until another value is requested.
# Therefore the squares are generated one at a time instead of creating a complete list of squares in advance.

# Real-Life Use:
# This approach is useful when calculations produce many values and only one value needs to be processed at a time.