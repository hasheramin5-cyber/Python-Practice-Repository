# A Program to retrieve generator values using next()

def colors():
    yield "Red"
    yield "Green"
    yield "Blue"


color_generator = colors()

print(next(color_generator))
print(next(color_generator))
print(next(color_generator))


# Explanation:
# Calling colors() creates a generator object.
# The first next() starts execution and returns "Red".
# The generator then pauses at the first yield.
# The second next() resumes execution and returns "Green".
# The third next() resumes again and returns "Blue".
# The generator therefore remembers exactly where execution was paused between next() calls.

# Real-Life Use:
# next() provides precise control when values from a generator need to be retrieved individually.