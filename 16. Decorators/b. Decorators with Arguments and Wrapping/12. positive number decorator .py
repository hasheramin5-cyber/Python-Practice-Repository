# A Program to allow only positive numbers using a decorator

from functools import wraps


def positive_only(function):
    @wraps(function)
    def wrapper(number):
        if number <= 0:
            print("Number must be positive.")
            return

        return function(number)

    return wrapper


@positive_only
def calculate_cube(number):
    print("Cube:", number ** 3)


calculate_cube(4)
calculate_cube(-3)


# Explanation:
# The positive_only() decorator adds a condition before calculate_cube() is executed.
# The wrapper checks whether the provided number is greater than zero.
# If the number is zero or negative, the original function is not executed.
# For a valid positive number, the wrapper calls the original function and passes the value to it.

# Real-Life Use:
# This pattern can be used for validating quantities, prices, measurements, limits, and other positive values.