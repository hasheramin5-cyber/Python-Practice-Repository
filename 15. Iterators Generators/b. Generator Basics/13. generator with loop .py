# A Program to create values using a generator and a loop

def count_numbers(limit):
    number = 1

    while number <= limit:
        yield number
        number += 1


numbers = count_numbers(5)

for number in numbers:
    print(number)


# Explanation:
# The count_numbers() function uses yield inside a while loop.
# The generator starts with number equal to 1.
# Each time the loop reaches yield, the current number is returned and the generator pauses.
# When the next value is requested, execution continues with number += 1 and then checks the while condition again.
# This continues until number becomes greater than the limit.

# Real-Life Use:
# This approach is useful for generating sequences without creating a complete list before processing begins.