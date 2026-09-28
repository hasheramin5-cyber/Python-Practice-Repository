# A Program to simulate a retry system for a service

from functools import wraps


def retry_service(attempts):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return function(*args, **kwargs)

                except ConnectionError as error:
                    print(f"Attempt {attempt}: {error}")

            print("Service request failed.")

        return wrapper

    return decorator


connection_attempts = 0


@retry_service(3)
def fetch_data():
    global connection_attempts

    connection_attempts += 1

    if connection_attempts < 3:
        raise ConnectionError("Temporary connection failure.")

    return "Data received successfully."


result = fetch_data()

print("Result:", result)


# Explanation:
# retry_service() creates a configurable retry decorator.
# The number of allowed attempts is provided when the decorator is created.
# fetch_data() simulates a service that temporarily fails.
# Each ConnectionError is caught by the decorator and the function is attempted again.
# When the function succeeds, its result is immediately returned.
# This demonstrates how decorators can encapsulate retry behavior around unreliable operations.

# Real-Life Use:
# Retry systems are useful for network services, external APIs, temporary database failures, and distributed applications.