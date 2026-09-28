# A Program to validate string length using a decorator

from functools import wraps


def minimum_length(length):
    def decorator(function):
        @wraps(function)
        def wrapper(text):
            if len(text) < length:
                print(f"Text must contain at least {length} characters.")
                return

            return function(text)

        return wrapper

    return decorator


@minimum_length(5)
def display_name(name):
    print("Name:", name)


display_name("Hasher")
display_name("Amin")


# Explanation:
# minimum_length() is a decorator factory because it first receives a configuration value.
# The length argument determines the minimum number of characters required.
# The decorator then receives the actual function.
# The wrapper checks the length of the provided text.
# If the text is too short, the original function is not called.
# Otherwise, the function executes normally.

# Real-Life Use:
# Configurable validation decorators are useful for usernames, passwords, form fields, and other user-provided input.