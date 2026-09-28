# A Program to limit how many times a function can be called

from functools import wraps


def call_limit(limit):
    def decorator(function):
        calls = 0

        @wraps(function)
        def wrapper(*args, **kwargs):
            nonlocal calls

            if calls >= limit:
                print("Call limit reached.")

                return

            calls += 1

            return function(*args, **kwargs)

        return wrapper

    return decorator


@call_limit(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Hasher")
greet("Amin")
greet("Aadil")
greet("Hammad")

# Explanation:
# call_limit() receives the maximum number of allowed calls.
# The decorator creates a calls variable that stores how many times the function has already been executed.
# nonlocal allows the wrapper() to update this variable.
# Before executing the original function, the wrapper checks whether the limit has already been reached.
# Once the maximum number of calls is reached, further calls are blocked.

# Real-Life Use:
# Call-limit decorators can be useful for limiting repeated operations, controlling demo features, protecting resources, and creating simple usage restrictions.