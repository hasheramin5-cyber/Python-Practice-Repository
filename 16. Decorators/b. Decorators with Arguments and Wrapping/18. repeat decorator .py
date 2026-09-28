# A Program to repeat a function using a decorator

from functools import wraps


def repeat(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                function(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def show_message():
    print("Python is fun!")


show_message()


# Explanation:
# repeat() is a decorator factory that receives the number of times a function should execute.
# Calling repeat(3) creates a decorator configured to repeat the target function three times.
# The wrapper contains a for loop that calls the original function according to the specified count.
# @repeat(3) therefore changes show_message() so that one function call results in three executions.

# Real-Life Use:
# Repeat decorators can be useful for retry systems, repeated notifications, testing, and controlled task execution.