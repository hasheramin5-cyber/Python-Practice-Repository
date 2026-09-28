# A Program to log API-style function calls using a decorator

from functools import wraps


def api_logger(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"API Request: {function.__name__}")
        print(f"Arguments: {args}")

        result = function(*args, **kwargs)

        print(f"API Response: {result}")

        return result

    return wrapper


@api_logger
def get_user(user_id):
    return {
        "id": user_id,
        "name": "Mickey Mouse"
    }


response = get_user(101)

print("Final response:", response)


# Explanation:
# The api_logger() decorator adds logging behavior around a function that represents an API-style operation.
# Before the function executes, the decorator displays the function name and provided arguments.
# The original function then creates and returns a response.
# After execution, the returned response is displayed.
# The response is finally returned to the caller unchanged.
# This demonstrates how decorators can add monitoring behavior without modifying the main business logic.

# Real-Life Use:
# API logging decorators are useful for recording requests, responses, debugging information, and application activity.