# A Program to add behavior to a function using a decorator

def start_decorator(function):
    def wrapper():
        print("Starting function...")

        function()

    return wrapper


@start_decorator
def display_message():
    print("Function is running.")


display_message()


# Explanation:
# start_decorator() receives the original display_message() function.
# The decorator creates a wrapper() function around it.
# When display_message() is called, the decorated version of the function is executed.
# The wrapper first prints a message and then calls the original function.
# This demonstrates how a decorator can add behavior before the execution of another function.

# Real-Life Use:
# This pattern can be used to add startup messages, validation steps, logging, or preparation logic.