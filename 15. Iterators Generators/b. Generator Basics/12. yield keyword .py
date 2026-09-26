# A Program to understand the yield keyword

def greet_users():
    yield "Hello Hasher"
    yield "Welcome to Python"
    yield "Keep Learning"


greetings = greet_users()

print(next(greetings))
print(next(greetings))
print(next(greetings))


# Explanation:
# The yield keyword produces a value from a generator function.
# When the first next() call is made, execution starts and pauses at the first yield statement.
# The second next() call resumes execution from that exact point and continues until the next yield.
# The same process happens for the third value.
# Therefore, yield allows a function to pause and resume instead of executing completely in one call.

# Real-Life Use:
# yield is useful for producing streams of data one item at a time.