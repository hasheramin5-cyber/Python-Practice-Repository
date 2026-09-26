# A Program to generate even numbers using a generator

def even_numbers(limit):
    number = 2

    while number <= limit:
        yield number
        number += 2


even_number_generator = even_numbers(10)

for number in even_number_generator:
    print(number)


# Explanation:
# The generator starts with the first positive even number, 2.
# Each yield returns the current even number.
# After yielding a value, number is increased by 2, so the next generated value is also guaranteed to be even.
# The while loop continues until the generated value exceeds the specified limit.

# Real-Life Use:
# Generators can create filtered or specially structured sequences without first storing every value in a list.