# A Program to filter values using a generator

def filter_positive(numbers):
    for number in numbers:
        if number > 0:
            yield number


values = [-5, 10, -3, 8, 0, 15, -2]

positive_values = filter_positive(values)

for number in positive_values:
    print(number)


# Explanation:
# The filter_positive() generator receives a collection of values.
# It checks each value one at a time using an if condition.
# Only values greater than zero are passed to the caller using yield.
# Because yield produces one value at a time, the generator does not need to create a separate list containing all positive values.
# The original collection remains unchanged.

# Real-Life Use:
# Generator-based filtering is useful when processing large datasets where only matching records need to be processed.