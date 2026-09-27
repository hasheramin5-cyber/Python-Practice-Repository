# A Program to create a generator processing pipeline

def numbers():
    for number in range(1, 11):
        yield number


def square_numbers(values):
    for value in values:
        yield value * value


def even_numbers(values):
    for value in values:
        if value % 2 == 0:
            yield value


number_generator = numbers()
squared_generator = square_numbers(number_generator)
even_generator = even_numbers(squared_generator)

for number in even_generator:
    print(number)


# Explanation:
# A generator pipeline connects multiple generators together.
# The numbers() generator produces numbers from 1 to 10.
# square_numbers() receives those values and produces their squares.
# even_numbers() receives the squared values and keeps only the even results.
# No stage needs to create a complete list of intermediate values.
# Each value moves through the pipeline one step at a time.
# This makes generator pipelines efficient for sequential data processing.

# Real-Life Use:
# Generator pipelines are useful in data processing systems, log processing, file processing, and streaming applications.