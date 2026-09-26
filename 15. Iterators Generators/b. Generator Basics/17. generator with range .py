# A Program to create a generator from a range

def generate_numbers(start, end):
    for number in range(start, end + 1):
        yield number


numbers = generate_numbers(1, 5)

for number in numbers:
    print(number)


# Explanation:
# The generator function receives a starting and ending value.
# range() produces the required sequence of numbers.
# The for loop inside the generator retrieves each number and yield sends it to the caller.
# After each yield, the generator pauses and later resumes from the next iteration of the loop.
# This separates the logic for generating values from the code that consumes those values.

# Real-Life Use:
# This pattern can be useful when generating controlled sequences for simulations, data processing, or repeated tasks.