# A Program to create a stateful decorator using a class

from functools import update_wrapper


class CallCounter:
    def __init__(self, function):
        self.function = function
        self.count = 0

        update_wrapper(self, function)

    def __call__(self, *args, **kwargs):
        self.count += 1

        print(f"Call count: {self.count}")

        return self.function(*args, **kwargs)


@CallCounter
def greet(name):
    print(f"Hello, {name}!")


greet("Hasher")
greet("Aadil")
greet("Hammad")


# Explanation:
# A class-based decorator can maintain state between function calls because the decorator object remains available.
# The CallCounter class stores the original function and a count variable.
# Every time the decorated function is called, __call__() increases count by one.
# The count is stored inside the same decorator object, so it is preserved between calls.
# This demonstrates one advantage of class-based decorators:
# they can naturally maintain object state.

# Real-Life Use:
# Stateful decorators can be useful for counting calls, tracking usage, collecting statistics, caching information, and monitoring repeated operations.