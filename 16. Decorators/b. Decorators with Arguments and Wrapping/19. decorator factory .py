# A Program to create a configurable decorator factory

from functools import wraps


def announce(message):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print(message)

            return function(*args, **kwargs)

        return wrapper

    return decorator


@announce("Starting calculation...")
def add(first, second):
    return first + second


result = add(10, 20)

print("Result:", result)


# Explanation:
# A decorator factory is a function that creates and returns a decorator based on configuration.
# announce() receives a custom message.
# It then returns decorator(), which receives the target function.
# The wrapper prints the configured message before executing the original function.
# This allows the same decorator structure to be reused with different messages or settings.

# Real-Life Use:
# Decorator factories are useful when reusable behavior needs configurable options such as messages, limits, permissions, or execution settings.