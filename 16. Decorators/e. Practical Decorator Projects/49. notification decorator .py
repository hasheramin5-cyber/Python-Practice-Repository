# A Program to send a notification after an operation

from functools import wraps


def notify(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)

        print("Notification: Operation completed successfully.")

        return result

    return wrapper


@notify
def upload_file(filename):
    print(f"Uploading {filename}...")

    return True


success = upload_file("report.pdf")

print("Upload status:", success)


# Explanation:
# The notify() decorator adds a notification after the original function completes.
# The wrapper first executes upload_file() and stores its returned result.
# After successful completion, a notification message is shown.
# The original result is then returned to the caller.
# This allows notification behavior to be reused by multiple operations without duplicating the same code.

# Real-Life Use:
# Notification decorators can be useful for completed tasks, background jobs, file uploads, order processing, and workflow systems.