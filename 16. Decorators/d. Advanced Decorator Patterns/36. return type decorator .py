# A Program to validate a function's return type using a decorator

from functools import wraps


def require_return_type(expected_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)

            if not isinstance(result, expected_type):
                raise TypeError(
                    f"Expected {expected_type.__name__}, "
                    f"but received {type(result).__name__}."
                )

            return result

        return wrapper

    return decorator


@require_return_type(int)
def add(first, second):
    return first + second


result = add(10, 20)

print("Result:", result)

# Explanation:
# require_return_type() receives the expected return type.
# The original function is executed first and its result is stored in result.
# isinstance() then checks whether the returned value has the expected type.
# If the type is incorrect, the decorator raises TypeError.
# If the type is valid, the result is returned normally.
# This demonstrates that decorators can validate not only input arguments but also function results.

# Real-Life Use:
# Return-type validation can be useful when working with APIs, data-processing functions, configuration systems, and functions with strict output requirements.