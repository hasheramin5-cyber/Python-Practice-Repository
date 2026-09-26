# A Program to create a simple generator function

def numbers():
    yield 1
    yield 2
    yield 3


number_generator = numbers()

for number in number_generator:
    print(number)


# Explanation:
# A generator function is a function that contains the yield keyword.
# Unlike a normal function that usually returns a result and finishes, a generator produces values one at a time.
# Calling numbers() does not immediately execute all the statements.
# Instead, it creates a generator object.
# The for loop requests values from the generator one by one.
# Each yield pauses the function and remembers its current state.
# When the next value is requested, execution continues from the statement immediately after the previous yield.

# Real-Life Use:
# Generators are useful when values should be produced gradually instead of creating the complete collection in memory.