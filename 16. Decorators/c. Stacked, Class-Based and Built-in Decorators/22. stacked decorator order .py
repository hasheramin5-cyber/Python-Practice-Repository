# A Program to demonstrate the execution order of stacked decorators

from functools import wraps


def first(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("First decorator - before")

        result = function(*args, **kwargs)

        print("First decorator - after")

        return result

    return wrapper


def second(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Second decorator - before")

        result = function(*args, **kwargs)

        print("Second decorator - after")

        return result

    return wrapper


@first
@second
def show_message():
    print("Original function")


show_message()


# Explanation:
# Multiple decorators are applied from the bottom upward.
# In this example, second() is applied to show_message() first.
# The first() decorator then wraps the result of second().
# During execution, the outer decorator runs first.
# The original function is reached only after both decorator wrappers have started their execution.
# After the original function finishes, execution returns through the decorators in the reverse direction.
# Understanding this order is important when combining multiple decorators.

# Real-Life Use:
# Decorator ordering matters when combining operations such as authentication, logging, validation, caching, and timing.