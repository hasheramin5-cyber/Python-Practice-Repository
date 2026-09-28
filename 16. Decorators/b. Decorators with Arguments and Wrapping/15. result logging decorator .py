# A Program to log the result returned by a function

from functools import wraps


def log_result(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)

        print(f"{function.__name__} returned:", result)

        return result

    return wrapper


@log_result
def multiply(first, second):
    return first * second


answer = multiply(6, 7)

print("Answer:", answer)


# Explanation:
# The log_result() decorator captures the value returned by the original function.
# The wrapper calls multiply() and stores its result.
# The function name and returned value are then displayed.
# Finally, the same result is returned so the caller can continue using it.
# The decorator therefore adds logging without changing the actual calculation performed by multiply().

# Real-Life Use:
# Result logging is useful for debugging, monitoring, and understanding what important functions are returning.