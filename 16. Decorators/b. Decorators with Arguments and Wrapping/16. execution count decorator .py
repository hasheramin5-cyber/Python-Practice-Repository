# A Program to count how many times a function is called

from functools import wraps


def count_calls(function):
    calls = 0

    @wraps(function)
    def wrapper(*args, **kwargs):
        nonlocal calls

        calls += 1

        print(f"{function.__name__} called {calls} time(s).")

        return function(*args, **kwargs)

    return wrapper


@count_calls
def greet(name):
    print(f"Hello, {name}!")


greet("Hasher")
greet("Aadil")
greet("Hammad")


# Explanation:
# The count_calls() decorator keeps track of how many times the decorated function has been executed.
# The calls variable belongs to the enclosing decorator function.
# nonlocal allows wrapper() to modify that variable instead of creating a new local variable.
# Every time wrapper() runs, calls is increased by one.
# The updated count is displayed before the original function is executed.

# Real-Life Use:
# Call-counting decorators can be useful for debugging, monitoring usage, testing, and tracking repeated operations.