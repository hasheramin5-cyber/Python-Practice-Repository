# A Program to execute code before and after a function

def before_after(function):
    def wrapper():
        print("Before function execution.")

        function()

        print("After function execution.")

    return wrapper


@before_after
def process_data():
    print("Processing data...")


process_data()


# Explanation:
# The before_after() decorator surrounds the original function with additional behavior.
# The wrapper() first executes code before calling process_data().
# The original function then runs normally.
# After the original function finishes, the wrapper continues and executes the final print statement.
# This demonstrates that a decorator can add behavior both before and after a function call.

# Real-Life Use:
# This structure is useful for logging, timing operations, resource preparation, cleanup, and transaction handling.