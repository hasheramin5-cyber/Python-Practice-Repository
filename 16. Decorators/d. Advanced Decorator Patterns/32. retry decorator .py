# A Program to retry a function when it fails

from functools import wraps


def retry(attempts):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return function(*args, **kwargs)

                except Exception as error:
                    print(f"Attempt {attempt} failed: {error}")

            print("All attempts failed.")

        return wrapper

    return decorator


@retry(3)
def connect_to_server():
    print("Trying to connect...")

    raise ConnectionError("Server unavailable")


connect_to_server()

# Explanation:
# retry() is a decorator factory because it receives the number of attempts as configuration.
# The wrapper runs the original function inside a loop.
# If the function succeeds, its result is immediately returned.
# If an exception occurs, the error is displayed and the function is tried again.
# The loop stops after the configured number of attempts.
# This pattern is useful when temporary failures are expected.

# Real-Life Use:
# Retry decorators are commonly useful for network requests, temporary service failures, external APIs, and other operations that may succeed when attempted again.