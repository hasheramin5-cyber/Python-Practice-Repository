# A Program to use iter() with a sentinel value

def get_number():
    return input("Enter a number or 'stop' to finish: ")


numbers = iter(get_number, "stop")

for number in numbers:
    print("You entered:", number)


# Explanation:
# The iter() function can be used with two arguments:
# a callable object and a sentinel value.
# Python repeatedly calls the callable object.
# The iterator continues producing values until the returned value becomes equal to the sentinel value.

# In this example, get_number() is called repeatedly.
# When the user enters "stop", iteration ends automatically.
# This provides a convenient way to repeatedly call a function until a specific value is returned.

# Real-Life Use:
# Sentinel-based iterators are useful for reading input, processing streams, and repeatedly calling functions until a termination value is received.