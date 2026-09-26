# A Program to understand generator exhaustion

def numbers():
    yield 10
    yield 20


number_generator = numbers()

print(next(number_generator))
print(next(number_generator))

try:
    print(next(number_generator))
except StopIteration:
    print("Generator has been exhausted.")


# Explanation:
# The generator contains two yield statements, so it can provide exactly two values.
# The first next() returns 10 and pauses the generator.
# The second next() resumes execution and returns 20.
# After the second yield, the generator function has no more statements that can produce another value.
# Calling next() again therefore raises StopIteration.
# Generator exhaustion follows the same iterator protocol introduced in the previous part.

# Real-Life Use:
# Detecting exhaustion is important when processing finite streams of generated data.