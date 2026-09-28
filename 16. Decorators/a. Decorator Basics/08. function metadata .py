# A Program to observe function metadata after decoration

def simple_decorator(function):
    def wrapper():
        return function()

    return wrapper


@simple_decorator
def welcome_message():
    """Display a welcome message."""
    print("Welcome!")


print("Function name:", welcome_message.__name__)
print("Function documentation:", welcome_message.__doc__)


# Explanation:
# Every Python function contains metadata such as its name and documentation string.
# After decoration, welcome_message now refers to the wrapper function returned by simple_decorator().
# Therefore, without additional handling, __name__ and __doc__ may describe the wrapper instead of the original function.
# This behavior becomes important when writing reusable decorators that should preserve the original function's identity.

# Real-Life Use:
# Preserving function metadata is important in debugging, documentation, testing, and professional Python libraries.