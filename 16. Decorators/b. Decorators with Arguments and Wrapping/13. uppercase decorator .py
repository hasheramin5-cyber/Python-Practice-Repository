# A Program to convert a function's result to uppercase

from functools import wraps


def uppercase(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)

        return result.upper()

    return wrapper


@uppercase
def get_message():
    return "hello from python"


message = get_message()

print(message)


# Explanation:
# The uppercase() decorator modifies the value returned by the original function.
# The wrapper first calls get_message() and stores its result.
# The result is a string, so the upper() method converts all lowercase characters to uppercase.
# The modified result is then returned to the caller.
# The original get_message() function itself remains unchanged.

# Real-Life Use:
# Result-transforming decorators are useful when output needs to be formatted consistently before being returned.