# A Program to use the next() function with an iterator

colors = ["Red", "Green", "Blue"]

color_iterator = iter(colors)

first_color = next(color_iterator)
second_color = next(color_iterator)

print("First:", first_color)
print("Second:", second_color)


# Explanation:
# iter() creates an iterator from the colors list.
# The first next() call returns "Red" and moves the iterator's position forward.
# The second next() call starts from the new position and returns "Green".
# The iterator therefore maintains its state between separate next() calls.

# Real-Life Use:
# next() is useful when a program needs precise control over retrieving values from a sequence.