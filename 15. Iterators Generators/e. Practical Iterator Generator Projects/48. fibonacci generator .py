# A Program to generate Fibonacci numbers using a generator

def fibonacci(limit):
    first = 0
    second = 1

    for _ in range(limit):
        yield first

        first, second = second, first + second


for number in fibonacci(10):
    print(number)


# Explanation:
# The Fibonacci sequence starts with 0 and 1.
# Every following value is calculated by adding the previous two values.
# The fibonacci() generator stores only the two values needed to calculate the next number.
# After yielding the current value, the variables are updated using tuple unpacking.
# The generator therefore produces the sequence one value at a time without creating a complete list.

# Real-Life Use:
# Generator-based mathematical sequences are useful when only a limited number of values are needed or when sequences become very large.