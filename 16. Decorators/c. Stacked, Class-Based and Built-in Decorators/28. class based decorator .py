# A Program to create a decorator using a class

from functools import update_wrapper


class Logger:
    def __init__(self, function):
        self.function = function

        update_wrapper(self, function)

    def __call__(self, *args, **kwargs):
        print(f"Calling {self.function.__name__}...")

        return self.function(*args, **kwargs)


@Logger
def greet(name):
    print(f"Hello, {name}!")


greet("SpongeBob")


# Explanation:
# A decorator does not have to be created using a function.
# A class can also act as a decorator when it implements the special __call__() method.
# The Logger object receives the original function during initialization.
# When the decorated function is called, Python invokes the Logger object's __call__() method.
# The __call__() method performs the additional logging behavior and then executes the original function.
# update_wrapper() copies important function metadata to the decorator object.

# Real-Life Use:
# Class-based decorators are useful when decorator behavior needs more structure, helper methods, configuration, or persistent state.