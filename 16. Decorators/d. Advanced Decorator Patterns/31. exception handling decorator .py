# A Program to handle exceptions using a decorator

from functools import wraps


def handle_errors(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)

        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")

        except ValueError:
            print("Error: Invalid value provided.")

    return wrapper


@handle_errors
def divide(first, second):
    return first / second


print("Result:", divide(20, 4))

divide(20, 0)

# Explanation:
# The handle_errors() decorator adds exception-handling behavior around the original function.
# The wrapper() executes the decorated function inside a try block.
# If divide() raises ZeroDivisionError, the decorator catches it and displays an appropriate message.
# ValueError is handled separately so different errors can receive different responses.
# This keeps error-handling logic outside the main function.

# Real-Life Use:
# Exception-handling decorators are useful for API calls, database operations, file processing, and other functions where repeated error-handling logic is required.