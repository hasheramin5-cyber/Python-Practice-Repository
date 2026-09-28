# A Program to attach custom metadata to a decorated function

from functools import wraps


def describe(category, version):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)

        wrapper.category = category
        wrapper.version = version

        return wrapper

    return decorator


@describe("Utility", "1.0")
def add(first, second):
    return first + second


print("Function:", add.__name__)
print("Category:", add.category)
print("Version:", add.version)
print("Result:", add(10, 20))

# Explanation:
# The describe() decorator factory receives custom metadata such as category and version.
# The wrapper function keeps the original function behavior.
# Custom attributes are then attached directly to the wrapper.
# Because the wrapper replaces the original function, these attributes can be accessed through the decorated function name.
# @wraps preserves standard function metadata such as the original function name and documentation.

# Real-Life Use:
# Custom metadata can be useful for plugin systems, command registries, API descriptions, testing frameworks, and application configuration.