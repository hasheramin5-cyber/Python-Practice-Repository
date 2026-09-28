# A Program to process data lazily using generators

def numbers():
    for number in range(1, 11):
        yield number


def double_values(values):
    for value in values:
        yield value * 2


def filter_large_values(values):
    for value in values:
        if value > 10:
            yield value


number_data = numbers()

doubled_data = double_values(number_data)

filtered_data = filter_large_values(doubled_data)

for value in filtered_data:
    print(value)


# Explanation:
# Lazy data processing means that values are processed only when they are actually requested.
# The numbers() generator produces the original values.
# double_values() receives those values and doubles them.
# filter_large_values() receives the doubled values and keeps only values greater than 10.
# These generators form a processing pipeline.
# No intermediate list is created between the processing stages.
# When the final for loop requests a value, the request travels backward through the pipeline and causes only the necessary amount of work to be performed.

# Real-Life Use:
# Lazy processing is useful for large datasets, file streams, log processing, data pipelines, and applications where memory efficiency is important.