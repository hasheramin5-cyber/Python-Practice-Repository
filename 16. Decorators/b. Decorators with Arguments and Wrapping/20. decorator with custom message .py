# A Program to create a custom message decorator

from functools import wraps


def status_message(start_message, end_message):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print(start_message)

            result = function(*args, **kwargs)

            print(end_message)

            return result

        return wrapper

    return decorator


@status_message(
    "Starting student registration...",
    "Student registration completed."
)
def register_student(name):
    print(f"Registering: {name}")

    return True


success = register_student("Mickey Mouse")

print("Success:", success)


# Explanation:
# status_message() is a configurable decorator factory that receives two messages.
# The decorator applies these messages around the original function execution.
# The wrapper first prints the starting message.
# It then calls register_student() and stores the returned value.
# After the function finishes, the ending message is displayed.
# Finally, the original return value is passed back to the caller.
# This demonstrates how decorators can provide reusable behavior while still allowing each decorated function to have different configuration.

# Real-Life Use:
# Configurable status decorators are useful for workflows, task processing, registration systems, API operations, and background jobs.