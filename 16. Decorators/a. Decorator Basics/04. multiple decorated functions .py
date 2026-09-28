# A Program to apply one decorator to multiple functions

def announce(function):
    def wrapper():
        print("Function started.")

        function()

        print("Function finished.")

    return wrapper


@announce
def first_task():
    print("Running first task.")


@announce
def second_task():
    print("Running second task.")


first_task()

print()

second_task()


# Explanation:
# The announce() decorator is created once and can be applied to multiple functions.
# Both first_task() and second_task() use the @announce syntax.
# When either function is called, its decorated wrapper executes.
# The wrapper prints a message before and after the original function runs.

# This demonstrates one of the major benefits of decorators: Reusable behavior can be shared across many functions.

# Real-Life Use:
# A common decorator can provide logging, authentication, validation, or timing behavior across many functions.