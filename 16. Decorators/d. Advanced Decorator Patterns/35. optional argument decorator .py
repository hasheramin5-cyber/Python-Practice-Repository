# A Program to create a decorator that supports optional arguments

from functools import wraps


def debug(function=None, *, prefix="DEBUG"):
    def decorator(target):
        @wraps(target)
        def wrapper(*args, **kwargs):
            print(f"{prefix}: Calling {target.__name__}")

            return target(*args, **kwargs)

        return wrapper

    if function is None:
        return decorator

    return decorator(function)


@debug
def greet():
    print("Hello!")


@debug(prefix="INFO")
def calculate():
    print("Calculating...")


greet()
calculate()


# Explanation:
# This decorator supports two different forms:

# @debug
# and:
# @debug(prefix="INFO")

# The function parameter defaults to None so the decorator can determine whether it was called directly or configured with arguments.
# If no configuration is provided, decorator() is applied directly to the function.
# If configuration is provided, the decorator factory first receives the configuration and later receives the function.
# This pattern makes a decorator flexible and reusable.

# Real-Life Use:
# Optional-argument decorators are useful when a decorator should work with default behavior while still allowing advanced configuration when needed.