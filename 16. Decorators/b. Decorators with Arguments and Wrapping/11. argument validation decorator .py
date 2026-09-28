# A Program to validate function arguments using a decorator

from functools import wraps


def validate_number(function):
    @wraps(function)
    def wrapper(number):
        if not isinstance(number, (int, float)):
            print("Invalid input. Please provide a number.")
            return

        return function(number)

    return wrapper


@validate_number
def square(number):
    print("Square:", number ** 2)


square(8)
square("hello")


# Explanation:
# The validate_number() decorator checks whether the argument passed to the function is a number.
# The wrapper() receives the argument before the original square() function is executed.
# isinstance() checks whether the value is an integer or float.
# If the value is not a number, the decorator displays an error and stops the function from running.
# If the value is valid, the original function is called normally.

# Real-Life Use:
# Argument validation decorators are useful for preventing invalid data from reaching important application functions.