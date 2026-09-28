# A Program to use multiple decorators on the same function

from functools import wraps


def uppercase(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)

        return result.upper()

    return wrapper


def add_exclamation(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)

        return result + "!"

    return wrapper


@uppercase
@add_exclamation
def greet(name):
    return f"Hello, {name}"


message = greet("Hasher")

print(message)


# Explanation:
# A function can have more than one decorator applied to it.
# The greet() function first passes through the add_exclamation decorator.
# The result produced by that decorator is then passed through the uppercase decorator.
# Therefore, the decorators work as a chain around the original function.
# Each decorator performs its own modification without changing the original function directly.
# The @wraps decorator preserves the metadata of the wrapped function.

# Real-Life Use:
# Stacked decorators are useful when multiple reusable behaviors such as logging, validation, authentication, formatting, and caching need to be combined.