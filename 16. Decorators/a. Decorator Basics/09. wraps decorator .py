# A Program to preserve function metadata using functools.wraps

from functools import wraps


def simple_decorator(function):
    @wraps(function)
    def wrapper():
        return function()

    return wrapper


@simple_decorator
def welcome_message():
    """Display a welcome message."""
    print("Welcome!")


print("Function name:", welcome_message.__name__)
print("Function documentation:", welcome_message.__doc__)

welcome_message()


# Explanation:
# functools.wraps() is used inside decorators to preserve important metadata from the original function.
# Without wraps(), the decorated function would normally expose information belonging to wrapper().
# The @wraps(function) syntax copies relevant metadata from the original function to the wrapper.
# As a result, __name__ remains "welcome_message" and __doc__ remains the original documentation string.
# This makes decorators more professional and easier to debug.

# Real-Life Use:
# functools.wraps() should generally be used when creating reusable decorators so function metadata remains meaningful.