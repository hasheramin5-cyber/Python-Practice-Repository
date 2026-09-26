# A Program to create a generator expression

numbers = (number * 2 for number in range(1, 6))

for number in numbers:
    print(number)


# Explanation:
# A generator expression provides a short way to create a generator without defining a separate generator function.

# The expression:
# (number * 2 for number in range(1, 6)) generates doubled values one at a time.
# Unlike a list comprehension, parentheses are used instead of square brackets.
# The values are produced only when the generator is iterated.

# Real-Life Use:
# Generator expressions are useful for concise, memory-efficient processing of calculated values.