# A Program to compare a generator with a list

def generate_numbers(limit):
    for number in range(1, limit + 1):
        yield number


numbers_list = [number for number in range(1, 6)]

numbers_generator = generate_numbers(5)

print("List:", numbers_list)
print("Generator:", numbers_generator)

print("Generator values:")

for number in numbers_generator:
    print(number)


# Explanation:
# The list comprehension immediately creates and stores all five numbers in memory.
# The generator function does not create all values at once.
# It produces each number only when the for loop requests it.
# Therefore, lists are useful when we need immediate access to all values, while generators are useful when values can be processed sequentially.
# The generator object itself does not display the generated values because it represents a mechanism for producing them.

# Real-Life Use:
# Generators are especially useful for large datasets, files, streams, and calculations where storing every value at once would consume unnecessary memory.