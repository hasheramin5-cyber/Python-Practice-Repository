# A Program to create a basic logging decorator

from functools import wraps


def log_function(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Calling: {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Finished: {function.__name__}")

        return result

    return wrapper


@log_function
def add_numbers(first, second):
    return first + second


result = add_numbers(10, 20)

print("Result:", result)


# Explanation:
# The log_function() decorator adds simple logging behavior around another function.
# The wrapper accepts any positional and keyword arguments using *args and **kwargs.
# Before calling the original function, the decorator prints the function's name.
# The original function then executes and its result is stored.
# After execution, another message is printed.
# Finally, the original result is returned to the caller.
# functools.wraps() preserves the metadata of add_numbers().

# Real-Life Use:
# Logging decorators are useful for tracking function calls, debugging applications, monitoring execution, and creating reusable logging behavior.